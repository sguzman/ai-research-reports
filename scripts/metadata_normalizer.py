#!/usr/bin/env python3

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
MD_ROOT = REPO_ROOT / "data" / "md"
STANDARD_PATH = MD_ROOT / "metadata-standard.yaml"

ALIAS_PAIRS: tuple[tuple[str, str], ...] = (
    ("cover-image", "cover_image"),
    ("epub-cover-image", "epub_cover_image"),
    ("series-title", "series_title"),
    ("series-number", "series_number"),
)

TEXT_FIELDS_TO_CLEAN: frozenset[str] = frozenset(
    {
        "abstract",
        "description",
        "summary",
        "subtitle",
        "title",
        "linkTitle",
        "reference-section-title",
    }
)


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def dump_yaml(data: dict[str, Any]) -> str:
    return "---\n" + yaml.safe_dump(
        data,
        sort_keys=False,
        allow_unicode=True,
        width=100,
        default_flow_style=False,
    ) + "...\n"


def merge_with_standard(standard: Any, data: Any) -> Any:
    if isinstance(standard, dict):
        incoming = data if isinstance(data, dict) else {}
        merged: dict[str, Any] = {}
        for key, template_value in standard.items():
            merged[key] = merge_with_standard(template_value, incoming.get(key))
        for key in sorted(incoming, key=lambda item: str(item)):
            if key not in merged:
                merged[key] = incoming[key]
        return merged
    if data is None:
        return deepcopy(standard)
    return data


def clean_text_value(value: str) -> str:
    lines = [line.rstrip() for line in value.splitlines()]
    cleaned = [line for line in lines if line.strip() != ""]
    return "\n".join(cleaned).strip()


def clean_text_fields(data: Any, key_name: str | None = None) -> Any:
    if isinstance(data, dict):
        return {key: clean_text_fields(value, key) for key, value in data.items()}
    if isinstance(data, list):
        return [clean_text_fields(value, key_name) for value in data]
    if isinstance(data, str) and key_name in TEXT_FIELDS_TO_CLEAN:
        return clean_text_value(data)
    return data


def sort_keys_recursively(data: Any) -> Any:
    if isinstance(data, dict):
        return {
            key: sort_keys_recursively(data[key])
            for key in sorted(data, key=lambda item: str(item))
        }
    if isinstance(data, list):
        return [sort_keys_recursively(item) for item in data]
    return data


def sync_aliases(data: dict[str, Any]) -> None:
    for left, right in ALIAS_PAIRS:
        left_value = data.get(left)
        right_value = data.get(right)
        if left_value not in (None, "", [], {}):
            data[right] = deepcopy(left_value)
        elif right_value not in (None, "", [], {}):
            data[left] = deepcopy(right_value)


def normalize_project(folder: Path, standard: dict[str, Any], create_missing: bool, write: bool) -> tuple[str, str]:
    article = folder / "article.yaml"
    if not article.exists():
        if not create_missing:
            return folder.name, "skipped_missing_article"
        data = deepcopy(standard)
    else:
        try:
            data = load_yaml(article)
        except Exception:
            return folder.name, "skipped_parse_error"
        data = merge_with_standard(standard, data)

    data = clean_text_fields(data)
    sync_aliases(data)
    data = sort_keys_recursively(data)
    rendered = dump_yaml(data)

    if write:
        article.write_text(rendered, encoding="utf-8")
    return folder.name, "written" if write else "would_write"


def collect_projects() -> list[Path]:
    return sorted(path for path in MD_ROOT.iterdir() if path.is_dir())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Normalize project article.yaml files to metadata-standard.yaml without inventing semantic metadata"
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write structural changes to disk. Does not invent semantic metadata. Without this flag, runs as a dry run.",
    )
    parser.add_argument(
        "--create-missing",
        action="store_true",
        help="Create article.yaml from the standard when a project folder lacks one. Leaves semantic fields blank.",
    )
    parser.add_argument(
        "folders",
        nargs="*",
        help="Optional project folder names under data/md to normalize.",
    )
    args = parser.parse_args()

    standard = load_yaml(STANDARD_PATH)
    projects = collect_projects()
    if args.folders:
        wanted = set(args.folders)
        projects = [project for project in projects if project.name in wanted]

    for project in projects:
        name, status = normalize_project(
            project,
            standard,
            create_missing=args.create_missing,
            write=args.write,
        )
        print(f"{name}\t{status}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
