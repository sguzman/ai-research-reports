#!/usr/bin/env python3
"""Report coverage of the persistent editorial work queue without modifying it."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
MD_ROOT = REPO_ROOT / "data" / "md"
QUEUE_PATH = REPO_ROOT / "editorial" / "QUEUE.yaml"


def load_queue() -> dict[str, Any]:
    data = yaml.safe_load(QUEUE_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("editorial/QUEUE.yaml must contain a YAML mapping")
    articles = data.get("articles")
    if not isinstance(articles, dict):
        raise ValueError("editorial/QUEUE.yaml must contain an articles mapping")
    return data


def discover_packages() -> set[str]:
    return {
        path.name
        for path in MD_ROOT.iterdir()
        if path.is_dir()
        and (path / "article.yaml").is_file()
        and (path / "main.md").is_file()
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only editorial queue coverage report.")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument(
        "--untriaged",
        action="store_true",
        help="print only canonical package slugs that are not yet represented in the queue",
    )
    args = parser.parse_args()

    queue = load_queue()
    packages = discover_packages()
    tracked = set(queue["articles"])
    untriaged = sorted(packages - tracked)
    stale = sorted(tracked - packages)

    if args.untriaged:
        for slug in untriaged:
            print(slug)
        return 0

    payload = {
        "packages": len(packages),
        "tracked": len(packages & tracked),
        "untriaged": len(untriaged),
        "stale_queue_entries": len(stale),
        "untriaged_slugs": untriaged,
        "stale_queue_slugs": stale,
    }

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(
            f"packages={payload['packages']} tracked={payload['tracked']} "
            f"untriaged={payload['untriaged']} stale_queue_entries={payload['stale_queue_entries']}"
        )
        if stale:
            print("\nStale queue entries:")
            for slug in stale:
                print(f"- {slug}")
        if untriaged:
            print("\nUntriaged packages:")
            for slug in untriaged:
                print(f"- {slug}")

    return 1 if stale else 0


if __name__ == "__main__":
    raise SystemExit(main())
