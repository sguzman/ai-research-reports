#!/usr/bin/env python3
"""Generate a mechanical census of canonical article packages.

This tool does not make editorial decisions and never edits article packages.
It records cheap, reproducible facts that help editors triage the corpus.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
MD_ROOT = REPO_ROOT / "data" / "md"
APPROVED_PROFILES = {"academic", "technical", "argumentative", "stylized", "personal", "creative"}
LIFECYCLES = {"draft", "review", "ready", "published", "archived"}

ABSOLUTE_PATH_RE = re.compile(r"(?:/win/|/home/|[A-Za-z]:\\\\)")
EXPORT_MARKER_RE = re.compile(r"(?:【\d+†|\[\d+†L\d+|utm_source=chatgpt\.com)")
MERMAID_RE = re.compile(r"(?m)^(?:```mermaid| {4}(?:flowchart|graph|gantt|sequenceDiagram|classDiagram)\b)")
MARKDOWN_LOCAL_RE = re.compile(r"!?\[[^\]]*\]\((?!https?://|#|//|mailto:)([^)\s]+)")

RISK_HINTS = {
    "health_or_self_harm": re.compile(r"(?:suicide|medical|health|gaht|gender[- ]affirm)", re.I),
    "engineering_or_physical_safety": re.compile(
        r"(?:engineering|design|construction|turbine|motor|desalination|vertical[- ]farm|highway)", re.I
    ),
    "time_sensitive_policy_or_market": re.compile(
        r"(?:current[- ]year|tax|population|cryptocurrency|finance|financial|legal[- ]landscape)", re.I
    ),
}


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        docs = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
    except Exception:
        return {}
    for doc in docs:
        if isinstance(doc, dict):
            return doc
    return {}


def count_files(root: Path) -> int:
    if not root.is_dir():
        return 0
    return sum(1 for path in root.rglob("*") if path.is_file())


def clean(value: Any) -> str:
    return value.strip() if isinstance(value, str) else ""


def duplicate_review_status(meta: dict[str, Any]) -> str:
    editorial = meta.get("editorial")
    if not isinstance(editorial, dict):
        return ""
    review = editorial.get("duplicate_review")
    if not isinstance(review, dict):
        return ""
    return clean(review.get("status")).lower()


def census_package(folder: Path) -> dict[str, Any]:
    meta_path = folder / "article.yaml"
    body_path = folder / "main.md"
    meta = load_yaml(meta_path)
    body = body_path.read_text(encoding="utf-8", errors="replace")

    status = clean(meta.get("status")).lower() or "unknown"
    profile = clean(meta.get("editorial_profile")).lower()
    voice = clean(meta.get("voice")).lower()
    artifact_type = clean(meta.get("type")).lower()
    title = clean(meta.get("title"))
    dup_status = duplicate_review_status(meta)

    flags: list[str] = []
    if status not in LIFECYCLES:
        flags.append("legacy_or_unknown_lifecycle")
    if profile not in APPROVED_PROFILES:
        flags.append("editorial_profile_unresolved")
    if not (folder / "CHANGELOG.md").is_file():
        flags.append("changelog_missing")
    if dup_status not in {"reviewed", "not-applicable"}:
        flags.append("duplicate_review_unresolved")
    if ABSOLUTE_PATH_RE.search(body):
        flags.append("absolute_path_in_body")
    if EXPORT_MARKER_RE.search(body):
        flags.append("conversion_or_chatgpt_marker")
    if MERMAID_RE.search(body):
        flags.append("raw_diagram_source")
    if body.count("```") % 2:
        flags.append("unmatched_code_fence")

    h1_count = sum(1 for line in body.splitlines() if line.startswith("# "))
    if h1_count != 1:
        flags.append("h1_count_not_one")

    risk_hints = [name for name, pattern in RISK_HINTS.items() if pattern.search(f"{folder.name} {title}")]

    return {
        "title": title,
        "lifecycle": status,
        "draft": meta.get("draft") if isinstance(meta.get("draft"), bool) else None,
        "type": artifact_type or None,
        "editorial_profile": profile or None,
        "voice": voice or None,
        "duplicate_review": dup_status or None,
        "has_changelog": (folder / "CHANGELOG.md").is_file(),
        "asset_files": count_files(folder / "assets"),
        "legacy_media_files": count_files(folder / "media"),
        "body_bytes": body_path.stat().st_size,
        "h1_count": h1_count,
        "local_link_or_image_count": len(MARKDOWN_LOCAL_RE.findall(body)),
        "risk_hints": risk_hints,
        "mechanical_flags": flags,
    }


def discover() -> dict[str, dict[str, Any]]:
    packages: dict[str, dict[str, Any]] = {}
    for folder in sorted(path for path in MD_ROOT.iterdir() if path.is_dir()):
        if not (folder / "article.yaml").is_file() or not (folder / "main.md").is_file():
            continue
        packages[folder.name] = census_package(folder)
    return packages


def payload() -> dict[str, Any]:
    packages = discover()
    return {
        "schema_version": 1,
        "kind": "mechanical-corpus-census",
        "editorial_warning": "Facts and heuristic risk hints only; this file does not classify, approve, archive, or publish articles.",
        "package_count": len(packages),
        "packages": packages,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a read-only mechanical census of canonical packages.")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of YAML")
    parser.add_argument("--summary", action="store_true", help="emit counts only")
    parser.add_argument("--write", type=Path, help="write the generated census to this path")
    args = parser.parse_args()

    data = payload()
    if args.summary:
        packages = data["packages"]
        unresolved = sum(1 for item in packages.values() if "editorial_profile_unresolved" in item["mechanical_flags"])
        legacy = sum(1 for item in packages.values() if "legacy_or_unknown_lifecycle" in item["mechanical_flags"])
        missing_log = sum(1 for item in packages.values() if "changelog_missing" in item["mechanical_flags"])
        unresolved_dup = sum(1 for item in packages.values() if "duplicate_review_unresolved" in item["mechanical_flags"])
        summary = {
            "packages": len(packages),
            "profile_unresolved": unresolved,
            "legacy_or_unknown_lifecycle": legacy,
            "changelog_missing": missing_log,
            "duplicate_review_unresolved": unresolved_dup,
        }
        print(json.dumps(summary, indent=2))
        return 0

    text = (
        json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        if args.json
        else yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120)
    )
    if args.write:
        target = args.write if args.write.is_absolute() else REPO_ROOT / args.write
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        print(f"wrote {target.relative_to(REPO_ROOT)} ({data['package_count']} packages)")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
