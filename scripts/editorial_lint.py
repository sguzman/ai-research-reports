#!/usr/bin/env python3
"""Read-only, profile-aware editorial checks for canonical article packages."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
MD_ROOT = REPO_ROOT / "data" / "md"

PROFILES = {"academic", "technical", "argumentative", "stylized", "personal", "creative"}
PUBLIC_STATUSES = {"ready", "published"}
DRAFT_STATUSES = {"draft", "review"}
KNOWN_STATUSES = PUBLIC_STATUSES | DRAFT_STATUSES | {"complete", "archived"}

H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
URL_RE = re.compile(r"https?://", re.I)
PROMPTISH_TITLE_RE = re.compile(r"\b(report request|research scope|prompt)\b", re.I)
PROCESS_TITLE_RE = re.compile(
    r"\btesting\s+(?:the|a|an)\s+[^:\n]{0,120}\bhypothes(?:is|es)\b|"
    r"(?:^|:\s*)(?:a|an)\s+(?:research|analytical|methodological)\s+"
    r"(?:report|framework|overview)\b|"
    r"\b(?:research|analytical)\s+report\b|"
    r"\bresearch\s+framework\b|"
    r"(?:^|:\s*)a\s+comprehensive\s+guide\b",
    re.I,
)
RAW_CHAT_CITATION_RE = re.compile(r"【[^】]*\d+[^】]*】")
PANDOC_NUMBERED_LINK_RE = re.compile(r"\[\\\[\d+\\\]\]\(https?://", re.I)
BROKEN_SCHEME_RE = re.compile(r"\[[^\]]+\]\(\s*https?:\s+//", re.I)
MARKDOWN_TARGET_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\n]+)\)")
HTML_IMG_RE = re.compile(r"<img\b[^>]*\bsrc\s*=\s*[\"']([^\"']+)[\"'][^>]*>", re.I)
HTML_LINK_RE = re.compile(r"<a\b[^>]*\bhref\s*=\s*[\"']([^\"']+)[\"'][^>]*>", re.I)
FENCED_BLOCK_RE = re.compile(r"(?ms)^```[^\n]*\n.*?^```\s*$")
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
MERMAID_RE = re.compile(r"(?ms)^```mermaid\s*\n(.*?)^```\s*$")
UNFENCED_DIAGRAM_RE = re.compile(
    r"(?m)^(?: {4}|\t)(?:flowchart|graph|sequenceDiagram|classDiagram|"
    r"stateDiagram(?:-v2)?|erDiagram|gantt|pie|journey|mindmap|timeline)\b"
)

FIRST_PERSON_RE = re.compile(
    r"\b(?:we|us|our|ours|ourselves|me|my|mine|myself)\b|"
    r"\bI\s+(?:am|was|have|had|do|did|think|argue|show|examine|use|will|would|"
    r"can|could|should|propose|suggest|consider|believe|find|found|conclude|assume|define|call)\b",
    re.I,
)
SECOND_PERSON_RE = re.compile(r"\b(?:you|your|yours|yourself|yourselves)\b", re.I)
SELF_REFERENCE_RE = re.compile(
    r"\b(?:(?:in|throughout|within|for)\s+)?(?:this|the present)\s+"
    r"(?:report|article|paper|study|analysis|essay|text)\b|"
    r"\bthe\s+(?:report|article|paper|study|analysis|essay|text)\s+"
    r"(?:argues|examines|explores|shows|discusses|considers|will|aims|seeks)\b",
    re.I,
)
HYPOTHESIS_META_RE = re.compile(
    r"\b(?:test|tests|tested|testing)\s+(?:out\s+)?"
    r"(?:(?:a|an|the|this|that|our|its)\s+)?hypothes(?:is|es)\b|"
    r"\bhypothes(?:is|es)\s+(?:is|are|was|were|will\s+be)\s+(?:being\s+)?tested\b",
    re.I,
)

AI_RESIDUE: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("assistant_refusal", re.compile(r"\bI[’']m sorry,\s+but I (?:can(?:not|'t)|won't)\b", re.I)),
    ("assistant_offer", re.compile(r"\bWould you like me to\b", re.I)),
    ("assistant_offer", re.compile(r"\bLet me know if you(?:'d| would) like\b", re.I)),
    ("assistant_meta", re.compile(r"\b(?:as|based on) your (?:request|prompt)\b", re.I)),
    ("assistant_meta", re.compile(r"\bI (?:can|will) (?:also )?(?:provide|create|expand|revise)\b", re.I)),
    ("user_prompt_leak", re.compile(r"\bthe user (?:did not|didn[’']t|asked|requested|specified)\b", re.I)),
    ("request_meta", re.compile(r"\b(?:as requested|per the request|the requested report)\b", re.I)),
    ("next_steps", re.compile(r"\bnext[- ]step research plan\b", re.I)),
)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    slug: str
    message: str
    path: str


def load_yaml(path: Path) -> dict[str, Any]:
    docs = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
    for doc in docs:
        if isinstance(doc, dict):
            return doc
    raise ValueError("no YAML mapping found")


def scalar(value: Any) -> str:
    return value.strip() if isinstance(value, str) else ""


def add(findings: list[Finding], severity: str, code: str, slug: str, message: str, path: Path) -> None:
    findings.append(
        Finding(severity, code, slug, message, str(path.relative_to(REPO_ROOT)))
    )


def iter_packages(slug: str | None) -> Iterable[Path]:
    if slug:
        path = MD_ROOT / slug
        if not path.is_dir():
            raise FileNotFoundError(f"unknown article slug: {slug}")
        yield path
        return
    for path in sorted(MD_ROOT.iterdir()):
        if path.is_dir():
            yield path


def prose_only(body: str) -> str:
    text = FENCED_BLOCK_RE.sub("", body)
    text = INLINE_CODE_RE.sub("", text)
    text = HTML_IMG_RE.sub("", text)
    text = HTML_LINK_RE.sub("", text)
    return MARKDOWN_TARGET_RE.sub(lambda m: m.group(2), text)


def local_target(folder: Path, raw: str) -> Path | None:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(None, 1)[0]
    parsed = urlsplit(target)
    if parsed.scheme or target.startswith(("#", "//")):
        return None
    path = unquote(parsed.path)
    return (folder / path).resolve() if path else None


def check_targets(folder: Path, body: str, status: str, findings: list[Finding]) -> None:
    slug = folder.name
    body_path = folder / "main.md"
    package_root = folder.resolve()
    assets_root = (folder / "assets").resolve()

    def check_one(kind: str, raw: str) -> None:
        target = local_target(folder, raw)
        if target is None:
            return
        try:
            target.relative_to(package_root)
        except ValueError:
            add(findings, "error", "local_target_outside_package", slug,
                f"{kind} escapes the article package: {raw!r}", body_path)
            return
        if not target.is_file():
            add(findings, "error", "missing_local_target", slug,
                f"missing local {kind}: {raw!r}", body_path)
            return
        try:
            target.relative_to(assets_root)
        except ValueError:
            severity = "error" if status in PUBLIC_STATUSES else "warning"
            add(findings, severity, "legacy_asset_location", slug,
                f"{kind} resolves inside the package but outside canonical assets/: {raw!r}", body_path)

    for match in MARKDOWN_TARGET_RE.finditer(body):
        kind = "image" if match.group(1) else "file link"
        check_one(kind, match.group(3).strip())

    for match in HTML_IMG_RE.finditer(body):
        check_one("HTML image", match.group(1).strip())

    for match in HTML_LINK_RE.finditer(body):
        check_one("HTML file link", match.group(1).strip())


def check_diagrams(folder: Path, body: str, status: str, findings: list[Finding]) -> None:
    slug = folder.name
    body_path = folder / "main.md"
    if body.count("```") % 2:
        add(findings, "error", "unbalanced_code_fence", slug,
            "unmatched triple-backtick fence may break rendering", body_path)

    if UNFENCED_DIAGRAM_RE.search(body):
        severity = "error" if status in PUBLIC_STATUSES else "warning"
        add(findings, severity, "unfenced_diagram", slug,
            "diagram-like source is indented rather than safely rendered/fenced", body_path)

    if MERMAID_RE.search(body):
        severity = "error" if status in PUBLIC_STATUSES else "warning"
        add(findings, severity, "mermaid_source", slug,
            "article contains Mermaid source; publishable content requires a verified rendered asset", body_path)


def style_excerpt(text: str, pattern: re.Pattern[str]) -> str | None:
    match = pattern.search(text)
    if not match:
        return None
    excerpt = text[max(0, match.start() - 45): match.end() + 70]
    return re.sub(r"\s+", " ", excerpt).strip()


def check_profile_style(folder: Path, profile: str, text: str, findings: list[Finding]) -> None:
    slug = folder.name
    body_path = folder / "main.md"

    checks: list[tuple[str, re.Pattern[str], str]] = []
    if profile == "academic":
        checks.extend([
            ("first_person", FIRST_PERSON_RE, "academic narration contains probable first person"),
            ("second_person", SECOND_PERSON_RE, "academic narration contains probable second-person address"),
            ("self_reference", SELF_REFERENCE_RE, "academic narration contains probable document self-reference"),
            ("hypothesis_stage_meta", HYPOTHESIS_META_RE, "academic narration contains probable assignment-stage hypothesis language"),
        ])
    elif profile == "argumentative":
        checks.extend([
            ("second_person", SECOND_PERSON_RE, "argumentative prose contains second-person address; verify that it is deliberate"),
            ("self_reference", SELF_REFERENCE_RE, "argumentative prose contains document self-reference; verify that it is useful"),
            ("hypothesis_stage_meta", HYPOTHESIS_META_RE, "argumentative prose contains probable assignment-stage hypothesis language"),
        ])
    # technical, stylized, personal, and creative intentionally have no generic perspective checks.

    for code, pattern, message in checks:
        excerpt = style_excerpt(text, pattern)
        if excerpt:
            add(findings, "warning", code, slug, f"{message}; inspect: {excerpt!r}", body_path)


def check_package(folder: Path) -> tuple[list[Finding], str]:
    findings: list[Finding] = []
    slug = folder.name
    meta_path = folder / "article.yaml"
    body_path = folder / "main.md"

    if not meta_path.is_file():
        add(findings, "error", "missing_metadata", slug, "missing article.yaml", folder)
        return findings, "missing"
    if not body_path.is_file():
        add(findings, "error", "missing_body", slug, "missing main.md", folder)
        return findings, "missing"

    try:
        meta = load_yaml(meta_path)
    except Exception as exc:
        add(findings, "error", "invalid_metadata", slug, f"article.yaml does not parse: {exc}", meta_path)
        return findings, "invalid"

    body = body_path.read_text(encoding="utf-8", errors="replace")
    text = prose_only(body)
    title = scalar(meta.get("title"))
    link_title = scalar(meta.get("linkTitle"))
    meta_slug = scalar(meta.get("slug"))
    status = scalar(meta.get("status")).lower()
    profile = scalar(meta.get("editorial_profile")).lower()
    draft = meta.get("draft")

    if not title:
        add(findings, "error", "missing_title", slug, "metadata title is blank", meta_path)
    if meta_slug != slug:
        add(findings, "error", "slug_mismatch", slug,
            f"metadata slug {meta_slug!r} does not match folder", meta_path)
    if status not in KNOWN_STATUSES:
        add(findings, "error", "unknown_status", slug, f"unknown status {status!r}", meta_path)
    elif status == "complete":
        add(findings, "warning", "legacy_status", slug,
            "status 'complete' is legacy; confirm publication before migrating to 'published'", meta_path)

    if not isinstance(draft, bool):
        add(findings, "error", "invalid_draft", slug, "draft must be a YAML boolean", meta_path)
    elif status in DRAFT_STATUSES and draft is not True:
        add(findings, "error", "lifecycle_mismatch", slug, f"{status} requires draft: true", meta_path)
    elif status in PUBLIC_STATUSES and draft is not False:
        add(findings, "error", "lifecycle_mismatch", slug, f"{status} requires draft: false", meta_path)

    if not profile:
        add(findings, "warning", "unclassified_profile", slug,
            "editorial_profile is unresolved; perspective rules are intentionally not inferred", meta_path)
    elif profile not in PROFILES:
        add(findings, "error", "unknown_profile", slug,
            f"editorial_profile {profile!r} is not one of {sorted(PROFILES)}", meta_path)

    if title and URL_RE.search(title):
        add(findings, "error", "url_in_title", slug, "metadata title contains a raw URL", meta_path)
    if title and PROMPTISH_TITLE_RE.search(title):
        add(findings, "warning", "promptish_title", slug,
            "title resembles generation/intake framing", meta_path)

    for field_name, field_value in (("title", title), ("linkTitle", link_title)):
        if field_value and PROCESS_TITLE_RE.search(field_value):
            severity = "error" if status in PUBLIC_STATUSES else "warning"
            add(findings, severity, "process_title", slug,
                f"{field_name} resembles AI/research-process framing rather than a public-facing title: {field_value!r}",
                meta_path)

    h1s = H1_RE.findall(body)
    if not h1s:
        add(findings, "error", "missing_h1", slug, "main.md has no H1", body_path)
    else:
        h1 = h1s[0].strip()
        if title and h1 != title:
            add(findings, "warning", "h1_title_mismatch", slug,
                f"H1 {h1!r} differs from metadata title {title!r}", body_path)
        if len(h1s) > 1:
            add(findings, "warning", "multiple_h1", slug,
                f"main.md contains {len(h1s)} H1 headings", body_path)

    if PANDOC_NUMBERED_LINK_RE.search(body):
        add(findings, "warning", "numbered_link_artifact", slug,
            r"escaped numbered Markdown links such as [\[1\]](url) remain", body_path)
    if RAW_CHAT_CITATION_RE.search(body):
        add(findings, "warning", "raw_chat_citation", slug,
            "raw ChatGPT citation marker remains", body_path)
    if BROKEN_SCHEME_RE.search(body):
        add(findings, "error", "broken_markdown_link", slug,
            "malformed URL scheme in Markdown link", body_path)

    for code, pattern in AI_RESIDUE:
        excerpt = style_excerpt(text, pattern)
        if excerpt:
            add(findings, "warning", code, slug,
                f"probable AI-production residue; inspect: {excerpt!r}", body_path)

    if profile in PROFILES:
        check_profile_style(folder, profile, text, findings)

    check_targets(folder, body, status, findings)
    check_diagrams(folder, body, status, findings)
    return findings, profile or "unclassified"


def main() -> int:
    parser = argparse.ArgumentParser(description="Profile-aware read-only editorial lint.")
    parser.add_argument("--slug", help="check one canonical article package")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true",
                        help="return nonzero for warnings as well as errors")
    args = parser.parse_args()

    if not MD_ROOT.is_dir():
        print(f"error: missing article root: {MD_ROOT}", file=sys.stderr)
        return 2

    findings: list[Finding] = []
    profile_counts: dict[str, int] = {}
    try:
        for folder in iter_packages(args.slug):
            package_findings, profile = check_package(folder)
            findings.extend(package_findings)
            profile_counts[profile] = profile_counts.get(profile, 0) + 1
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    if args.json:
        print(json.dumps({
            "packages": sum(profile_counts.values()),
            "profiles": dict(sorted(profile_counts.items())),
            "errors": len(errors),
            "warnings": len(warnings),
            "findings": [asdict(f) for f in findings],
        }, indent=2, ensure_ascii=False))
    else:
        for finding in findings:
            print(f"{finding.severity.upper():7} {finding.slug}: "
                  f"{finding.code}: {finding.message} [{finding.path}]")
        print(f"\npackages={sum(profile_counts.values())} profiles={dict(sorted(profile_counts.items()))}")
        print(f"errors={len(errors)} warnings={len(warnings)}")

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())