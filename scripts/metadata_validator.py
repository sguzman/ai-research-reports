#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
MD_ROOT = REPO_ROOT / "data" / "md"
STANDARD_PATH = MD_ROOT / "metadata-standard.yaml"

# Exact-meaning compatibility aliases that should match.
ALIAS_PAIRS: tuple[tuple[str, str], ...] = (
    ("cover-image", "cover_image"),
    ("epub-cover-image", "epub_cover_image"),
    ("series-title", "series_title"),
    ("series-number", "series_number"),
)

# Non-cover fields expected to carry substantive information in a complete record.
REQUIRED_SUBSTANTIVE_FIELDS: tuple[str, ...] = (
    "title",
    "description",
    "abstract",
    "slug",
    "date",
    "edition",
    "revision",
    "author",
    "creator",
    "publisher",
    "rights",
    "license",
    "lang",
    "language",
    "identifier",
    "type",
    "format",
    "categories",
    "tags",
    "keywords",
    "subject",
    "subjects",
    "reference-section-title",
    "status",
    "series",
    "series-title",
    "report-year",
)


@dataclass
class ProjectIssue:
    folder: str
    article_exists: bool
    parse_error: str | None
    missing_keys: list[str]
    extra_keys: list[str]
    blank_required_fields: list[str]
    alias_mismatches: list[str]

    @property
    def is_clean(self) -> bool:
        return (
            self.article_exists
            and self.parse_error is None
            and not self.missing_keys
            and not self.extra_keys
            and not self.blank_required_fields
            and not self.alias_mismatches
        )


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def is_blank(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() == ""
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) == 0
    return False


def format_alias_mismatch(left: str, right: str, left_value: Any, right_value: Any) -> str:
    return f"{left} != {right} ({left_value!r} vs {right_value!r})"


def validate_project(folder: Path, standard: dict[str, Any]) -> ProjectIssue:
    article = folder / "article.yaml"
    if not article.exists():
        return ProjectIssue(
            folder=folder.name,
            article_exists=False,
            parse_error=None,
            missing_keys=list(standard.keys()),
            extra_keys=[],
            blank_required_fields=[],
            alias_mismatches=[],
        )

    try:
        data = load_yaml(article)
    except Exception as exc:  # pragma: no cover - exercised against malformed files
        return ProjectIssue(
            folder=folder.name,
            article_exists=True,
            parse_error=str(exc),
            missing_keys=[],
            extra_keys=[],
            blank_required_fields=[],
            alias_mismatches=[],
        )

    missing_keys = [key for key in standard if key not in data]
    extra_keys = [key for key in data if key not in standard]
    blank_required_fields = [
        key for key in REQUIRED_SUBSTANTIVE_FIELDS if key in data and is_blank(data[key])
    ]

    alias_mismatches: list[str] = []
    for left, right in ALIAS_PAIRS:
        if left in data and right in data and data[left] != data[right]:
            alias_mismatches.append(format_alias_mismatch(left, right, data[left], data[right]))

    return ProjectIssue(
        folder=folder.name,
        article_exists=True,
        parse_error=None,
        missing_keys=missing_keys,
        extra_keys=extra_keys,
        blank_required_fields=blank_required_fields,
        alias_mismatches=alias_mismatches,
    )


def collect_projects() -> list[Path]:
    return sorted(path for path in MD_ROOT.iterdir() if path.is_dir())


def build_summary(issues: list[ProjectIssue]) -> dict[str, Any]:
    blank_counter: Counter[str] = Counter()
    for issue in issues:
        blank_counter.update(issue.blank_required_fields)

    return {
        "project_count": len(issues),
        "clean_count": sum(1 for issue in issues if issue.is_clean),
        "missing_article_count": sum(1 for issue in issues if not issue.article_exists),
        "parse_error_count": sum(1 for issue in issues if issue.parse_error is not None),
        "projects_with_missing_keys": sum(1 for issue in issues if issue.missing_keys),
        "projects_with_extra_keys": sum(1 for issue in issues if issue.extra_keys),
        "projects_with_blank_required_fields": sum(
            1 for issue in issues if issue.blank_required_fields
        ),
        "projects_with_alias_mismatches": sum(1 for issue in issues if issue.alias_mismatches),
        "common_blank_required_fields": blank_counter.most_common(),
    }


def print_text_report(issues: list[ProjectIssue], summary: dict[str, Any], only_failing: bool) -> None:
    print("Metadata validation summary")
    print(f"  projects: {summary['project_count']}")
    print(f"  clean: {summary['clean_count']}")
    print(f"  missing article.yaml: {summary['missing_article_count']}")
    print(f"  parse errors: {summary['parse_error_count']}")
    print(f"  projects with missing keys: {summary['projects_with_missing_keys']}")
    print(f"  projects with extra keys: {summary['projects_with_extra_keys']}")
    print(
        "  projects with blank required fields:"
        f" {summary['projects_with_blank_required_fields']}"
    )
    print(f"  projects with alias mismatches: {summary['projects_with_alias_mismatches']}")
    print()

    interesting = issues if not only_failing else [issue for issue in issues if not issue.is_clean]
    for issue in interesting:
        if issue.is_clean and only_failing:
            continue
        print(issue.folder)
        if not issue.article_exists:
            print("  - missing: article.yaml")
            continue
        if issue.parse_error:
            print(f"  - parse_error: {issue.parse_error}")
            continue
        if issue.missing_keys:
            print(f"  - missing_keys: {', '.join(issue.missing_keys)}")
        if issue.extra_keys:
            print(f"  - extra_keys: {', '.join(issue.extra_keys)}")
        if issue.blank_required_fields:
            print(f"  - blank_required: {', '.join(issue.blank_required_fields)}")
        if issue.alias_mismatches:
            print(f"  - alias_mismatches: {'; '.join(issue.alias_mismatches)}")
        if issue.is_clean:
            print("  - clean")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate project metadata against metadata-standard.yaml")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Show clean projects too in text mode",
    )
    args = parser.parse_args()

    standard = load_yaml(STANDARD_PATH)
    issues = [validate_project(project, standard) for project in collect_projects()]
    summary = build_summary(issues)

    if args.json:
        payload = {
            "summary": summary,
            "projects": [
                {
                    "folder": issue.folder,
                    "article_exists": issue.article_exists,
                    "parse_error": issue.parse_error,
                    "missing_keys": issue.missing_keys,
                    "extra_keys": issue.extra_keys,
                    "blank_required_fields": issue.blank_required_fields,
                    "alias_mismatches": issue.alias_mismatches,
                    "is_clean": issue.is_clean,
                }
                for issue in issues
            ],
        }
        print(json.dumps(payload, indent=2))
    else:
        print_text_report(issues, summary, only_failing=not args.all)

    return 1 if any(not issue.is_clean for issue in issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
