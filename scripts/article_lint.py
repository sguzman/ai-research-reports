#!/usr/bin/env python3
"""Read-only editorial and lifecycle checks for canonical research article packages.

This tool intentionally never edits the corpus. It is designed to be safe enough to
run on every candidate article before publication.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
MD_ROOT = REPO_ROOT / "data" / "md"

PUBLIC_STATUSES = {"ready", "published", "complete"}
DRAFT_STATUSES = {"draft", "review"}
KNOWN_STATUSES = PUBLIC_STATUSES | DRAFT_STATUSES | {"archived"}

URL_RE = re.compile(r"https?://", re.I)
RAW_CITATION_RE = re.compile(r"【[^】]*\d+[^】]*】")
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
FRONTMATTER_RE = re.compile(r"\A---\s*\n")
PROMPTISH_TITLE_RE = re.compile(r"\b(report request|research scope|prompt)\b", re.I)
BROKEN_LINK_RE = re.compile(r"\[[^\]]+\]\(\s*https?:\s+//", re.I)

AI_RESIDUE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("assistant_refusal", re.compile(r"\bI[’']m sorry,\s+but I (?:can(?:not|'t)|won't)\b", re.I)),
    ("assistant_offer", re.compile(r"\bWould you like me to\b", re.I)),
    ("assistant_offer", re.compile(r"\bLet me know if you(?:'d| would) like\b", re.I)),
    ("assistant_meta", re.compile(r"\b(?:as|based on) your (?:request|prompt)\b", re.I)),
    ("assistant_meta", re.compile(r"\bI (?:can|will) (?:also )?(?:provide|create|expand|revise)\b", re.I)),
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


def clean_scalar(value: Any) -> str:
    return value.strip() if isinstance(value, str) else ""


def first_h1(body: str) -> str:
    match = H1_RE.search(body)
    return match.group(1).strip() if match else ""


def iter_packages(root: Path, slug: str | None) -> Iterable[Path]:
    if slug:
        target = root / slug
        if not target.is_dir():
            raise FileNotFoundError(f"unknown article slug: {slug}")
        yield target
        return
    for path in sorted(root.iterdir()):
        if path.is_dir():
            yield path


def add(findings: list[Finding], severity: str, code: str, slug: str, message: str, path: Path) -> None:
    findings.append(
        Finding(
            severity=severity,
            code=code,
            slug=slug,
            message=message,
            path=str(path.relative_to(REPO_ROOT)),
        )
    )


def check_package(folder: Path) -> list[Finding]:
    findings: list[Finding] = []
    slug = folder.name
    meta_path = folder / "article.yaml"
    body_path = folder / "main.md"

    if not meta_path.exists():
        add(findings, "error", "missing_metadata", slug, "missing article.yaml", folder)
        return findings
    if not body_path.exists():
        add(findings, "error", "missing_body", slug, "missing main.md", folder)
        return findings

    try:
        meta = load_yaml(meta_path)
    except Exception as exc:
        add(findings, "error", "invalid_metadata", slug, f"article.yaml does not parse: {exc}", meta_path)
        return findings

    body = body_path.read_text(encoding="utf-8", errors="replace")
    title = clean_scalar(meta.get("title"))
    meta_slug = clean_scalar(meta.get("slug"))
    status = clean_scalar(meta.get("status")).lower()
    draft = meta.get("draft")

    if not title:
        add(findings, "error", "missing_title", slug, "metadata title is blank", meta_path)
    if not meta_slug:
        add(findings, "error", "missing_slug", slug, "metadata slug is blank", meta_path)
    elif meta_slug != slug:
        add(
            findings,
            "error",
            "slug_mismatch",
            slug,
            f"folder slug is {slug!r} but metadata slug is {meta_slug!r}",
            meta_path,
        )

    if not status:
        add(findings, "error", "missing_status", slug, "metadata status is blank", meta_path)
    elif status not in KNOWN_STATUSES:
        add(
            findings,
            "error",
            "unknown_status",
            slug,
            f"status {status!r} is not one of {sorted(KNOWN_STATUSES)}",
            meta_path,
        )
    elif status == "complete":
        add(
            findings,
            "warning",
            "legacy_status",
            slug,
            "status 'complete' is accepted for legacy material; prefer 'published' for the canonical lifecycle",
            meta_path,
        )

    if not isinstance(draft, bool):
        add(findings, "error", "invalid_draft", slug, "draft must be a YAML boolean", meta_path)
    elif status in DRAFT_STATUSES and draft is not True:
        add(
            findings,
            "error",
            "lifecycle_mismatch",
            slug,
            f"status {status!r} requires draft: true",
            meta_path,
        )
    elif status in PUBLIC_STATUSES and draft is not False:
        add(
            findings,
            "error",
            "lifecycle_mismatch",
            slug,
            f"status {status!r} requires draft: false",
            meta_path,
        )

    if title and URL_RE.search(title):
        add(findings, "error", "url_in_title", slug, "title contains a raw URL", meta_path)
    if title and PROMPTISH_TITLE_RE.search(title):
        add(
            findings,
            "warning",
            "promptish_title",
            slug,
            "title looks like an intake/prompt artifact rather than a publication title",
            meta_path,
        )

    for field in ("description", "summary", "abstract"):
        value = clean_scalar(meta.get(field))
        if not value:
            add(findings, "warning", f"blank_{field}", slug, f"{field} is blank", meta_path)
            continue
        if value == title:
            add(
                findings,
                "warning",
                f"{field}_equals_title",
                slug,
                f"{field} merely repeats the title",
                meta_path,
            )
        if URL_RE.search(value) and len(value) < 500:
            add(
                findings,
                "warning",
                f"url_in_{field}",
                slug,
                f"{field} contains a raw URL; inspect for conversion contamination",
                meta_path,
            )

    h1 = first_h1(body)
    if not h1:
        add(findings, "error", "missing_h1", slug, "main.md has no H1 heading", body_path)
    elif title and h1 != title:
        add(
            findings,
            "warning",
            "h1_title_mismatch",
            slug,
            f"H1 {h1!r} differs from metadata title {title!r}",
            body_path,
        )

    if FRONTMATTER_RE.search(body):
        add(
            findings,
            "warning",
            "body_frontmatter",
            slug,
            "main.md appears to contain YAML frontmatter; canonical metadata belongs in article.yaml",
            body_path,
        )

    if RAW_CITATION_RE.search(body):
        add(
            findings,
            "warning",
            "raw_chat_citation",
            slug,
            "body contains raw ChatGPT citation markers such as 【...】",
            body_path,
        )

    if BROKEN_LINK_RE.search(body):
        add(
            findings,
            "error",
            "broken_markdown_link",
            slug,
            "body contains a malformed Markdown URL with whitespace inside the scheme",
            body_path,
        )

    for code, pattern in AI_RESIDUE_PATTERNS:
        if pattern.search(body):
            add(
                findings,
                "warning",
                code,
                slug,
                f"body contains probable assistant/prompt residue matching {pattern.pattern!r}",
                body_path,
            )

    h1_count = len(H1_RE.findall(body))
    if h1_count > 1:
        add(
            findings,
            "warning",
            "multiple_h1",
            slug,
            f"main.md contains {h1_count} H1 headings",
            body_path,
        )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read-only editorial/lifecycle checks for data/md/<slug> article packages."
    )
    parser.add_argument("--slug", help="check one article instead of the whole corpus")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="return nonzero when warnings are present as well as errors",
    )
    args = parser.parse_args()

    if not MD_ROOT.is_dir():
        print(f"error: missing article root: {MD_ROOT}", file=sys.stderr)
        return 2

    try:
        findings = [f for folder in iter_packages(MD_ROOT, args.slug) for f in check_package(folder)]
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    if args.json:
        print(
            json.dumps(
                {
                    "errors": len(errors),
                    "warnings": len(warnings),
                    "findings": [asdict(f) for f in findings],
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        for f in findings:
            print(f"{f.severity.upper():7} {f.slug}: {f.code}: {f.message} [{f.path}]")
        print(f"\nerrors={len(errors)} warnings={len(warnings)}")

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
