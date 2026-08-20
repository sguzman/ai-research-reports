#!/usr/bin/env python3
"""Read-only duplicate and overlap candidate finder for canonical article packages.

This tool intentionally stops at candidate generation. It never edits metadata,
chooses a canonical article, archives a source, or performs a merge.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
MD_ROOT = REPO_ROOT / "data" / "md"

FENCED_BLOCK_RE = re.compile(r"(?ms)^```[^\n]*\n.*?^```\s*$")
HTML_TAG_RE = re.compile(r"<[^>]+>")
MARKDOWN_LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)\n]+\)")
MARKDOWN_HEADING_RE = re.compile(r"(?m)^#{1,6}\s+")
CITATION_MARKER_RE = re.compile(r"(?:\[\\?\[?\d+\\?\]?\]|【[^】]+】)")
WORD_RE = re.compile(r"[a-z0-9]+(?:['’-][a-z0-9]+)?", re.I)


@dataclass(frozen=True)
class Document:
    slug: str
    path: str
    words: tuple[str, ...]
    shingles: frozenset[tuple[str, ...]]
    normalized_hash: str


@dataclass(frozen=True)
class Candidate:
    left: str
    right: str
    relationship_hint: str
    jaccard: float
    containment: float
    length_ratio: float
    left_words: int
    right_words: int


def iter_packages(slugs: set[str] | None = None) -> Iterable[Path]:
    for folder in sorted(MD_ROOT.iterdir()):
        if not folder.is_dir():
            continue
        if slugs and folder.name not in slugs:
            continue
        if (folder / "main.md").is_file():
            yield folder


def normalize_body(body: str) -> tuple[str, ...]:
    text = FENCED_BLOCK_RE.sub(" ", body)
    text = MARKDOWN_LINK_RE.sub(lambda m: f" {m.group(1)} ", text)
    text = HTML_TAG_RE.sub(" ", text)
    text = MARKDOWN_HEADING_RE.sub("", text)
    text = CITATION_MARKER_RE.sub(" ", text)
    return tuple(word.lower() for word in WORD_RE.findall(text))


def make_shingles(words: tuple[str, ...], width: int) -> frozenset[tuple[str, ...]]:
    if len(words) < width:
        return frozenset()
    return frozenset(tuple(words[i : i + width]) for i in range(len(words) - width + 1))


def load_document(folder: Path, shingle_width: int) -> Document:
    body = (folder / "main.md").read_text(encoding="utf-8", errors="replace")
    words = normalize_body(body)
    normalized = " ".join(words).encode("utf-8")
    digest = hashlib.sha256(normalized).hexdigest()
    return Document(
        slug=folder.name,
        path=str((folder / "main.md").relative_to(REPO_ROOT)),
        words=words,
        shingles=make_shingles(words, shingle_width),
        normalized_hash=digest,
    )


def overlap_metrics(left: Document, right: Document) -> tuple[float, float, float]:
    if not left.shingles or not right.shingles:
        return 0.0, 0.0, 0.0
    common = len(left.shingles & right.shingles)
    union = len(left.shingles | right.shingles)
    smaller = min(len(left.shingles), len(right.shingles))
    jaccard = common / union if union else 0.0
    containment = common / smaller if smaller else 0.0
    length_ratio = min(len(left.words), len(right.words)) / max(len(left.words), len(right.words))
    return jaccard, containment, length_ratio


def classify_hint(
    left: Document,
    right: Document,
    jaccard: float,
    containment: float,
    length_ratio: float,
    similarity_threshold: float,
    containment_threshold: float,
) -> str | None:
    if left.normalized_hash == right.normalized_hash:
        return "exact-normalized-duplicate"
    if jaccard >= similarity_threshold and length_ratio >= 0.60:
        return "near-duplicate-candidate"
    if containment >= containment_threshold and length_ratio < 0.85:
        return "containment-or-derivative-candidate"
    return None


def find_candidates(
    docs: list[Document],
    similarity_threshold: float,
    containment_threshold: float,
    min_words: int,
) -> list[Candidate]:
    results: list[Candidate] = []
    for i, left in enumerate(docs):
        if len(left.words) < min_words:
            continue
        for right in docs[i + 1 :]:
            if len(right.words) < min_words:
                continue
            jaccard, containment, length_ratio = overlap_metrics(left, right)
            hint = classify_hint(
                left,
                right,
                jaccard,
                containment,
                length_ratio,
                similarity_threshold,
                containment_threshold,
            )
            if hint is None:
                continue
            results.append(
                Candidate(
                    left=left.slug,
                    right=right.slug,
                    relationship_hint=hint,
                    jaccard=round(jaccard, 4),
                    containment=round(containment, 4),
                    length_ratio=round(length_ratio, 4),
                    left_words=len(left.words),
                    right_words=len(right.words),
                )
            )
    return sorted(
        results,
        key=lambda item: (
            item.relationship_hint != "exact-normalized-duplicate",
            -item.containment,
            -item.jaccard,
            item.left,
            item.right,
        ),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find exact and heuristic duplicate/derivative candidates without modifying the corpus."
    )
    parser.add_argument(
        "--slug",
        action="append",
        default=[],
        help="Limit the corpus side of the scan to one or more canonical slugs. Repeat as needed.",
    )
    parser.add_argument(
        "--shingle-width",
        type=int,
        default=5,
        help="Word shingle width used for overlap scoring (default: 5).",
    )
    parser.add_argument(
        "--similarity-threshold",
        type=float,
        default=0.72,
        help="Jaccard threshold for near-duplicate candidates (default: 0.72).",
    )
    parser.add_argument(
        "--containment-threshold",
        type=float,
        default=0.88,
        help="Smaller-document containment threshold (default: 0.88).",
    )
    parser.add_argument(
        "--min-words",
        type=int,
        default=120,
        help="Ignore documents shorter than this many normalized words (default: 120).",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.shingle_width < 2:
        raise SystemExit("--shingle-width must be at least 2")
    for value, name in (
        (args.similarity_threshold, "--similarity-threshold"),
        (args.containment_threshold, "--containment-threshold"),
    ):
        if not 0.0 <= value <= 1.0:
            raise SystemExit(f"{name} must be between 0 and 1")
    if args.min_words < 1:
        raise SystemExit("--min-words must be positive")

    # A slug restriction means "report candidates involving these slugs", not
    # "compare only these slugs to one another". Load the whole corpus first.
    docs = [load_document(folder, args.shingle_width) for folder in iter_packages()]
    candidates = find_candidates(
        docs,
        similarity_threshold=args.similarity_threshold,
        containment_threshold=args.containment_threshold,
        min_words=args.min_words,
    )

    if args.slug:
        selected = set(args.slug)
        unknown = selected - {doc.slug for doc in docs}
        if unknown:
            raise SystemExit(f"unknown article slug(s): {', '.join(sorted(unknown))}")
        candidates = [c for c in candidates if c.left in selected or c.right in selected]

    if args.json:
        payload = {
            "candidate_count": len(candidates),
            "parameters": {
                "shingle_width": args.shingle_width,
                "similarity_threshold": args.similarity_threshold,
                "containment_threshold": args.containment_threshold,
                "min_words": args.min_words,
            },
            "candidates": [asdict(candidate) for candidate in candidates],
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    if not candidates:
        print("No duplicate/derivative candidates met the configured thresholds.")
        return 0

    print(
        "relationship_hint\tleft\tright\tjaccard\tcontainment\tlength_ratio\tword_counts"
    )
    for candidate in candidates:
        print(
            f"{candidate.relationship_hint}\t{candidate.left}\t{candidate.right}\t"
            f"{candidate.jaccard:.4f}\t{candidate.containment:.4f}\t"
            f"{candidate.length_ratio:.4f}\t"
            f"{candidate.left_words}/{candidate.right_words}"
        )

    print(
        "\nCandidate scores require editorial review under DUPLICATE_POLICY.md; "
        "this tool makes no disposition."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
