#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
MD_ROOT = REPO_ROOT / "data" / "md"

PUBLISHER = "Marginalia"
AUTHOR = ["Salvador Guzman", "ChatGPT"]

MATH = {
    "a-history-of-functional-analysis",
    "a-literary-non-technical-history-of-the-hilbert-p-lya-conjecture",
    "algebra-evolution",
    "analysis-semantics",
    "category-theory",
    "category-theory-research-scope",
    "complex-plane-canvas",
    "complex-plane-culture",
    "geometry-semantics",
    "heaviside",
    "homological-algebra",
    "linear-algebra-history-report",
    "number-theory-from-euler",
    "operators-social-history",
    "topology",
}

COMPUTING = {
    "a-post-chomskyan-theory-of-language-in-the-age-of-llms",
    "chip-industry",
    "css-history",
    "history-of-html",
    "html-history",
    "javascript-history",
    "how-llms-challenge-chomskyan-assumptions-analytical-report",
    "neural-networks",
    "type-theory-history",
}

LAW = {
    "american-judicial-process",
    "federal-legal-landscape",
    "kern-weed",
    "lawyers-institutions-and-moral-order-in-the-yankee-nation-folkways-lens",
    "structure-and-sources-of-american-law",
    "yankee-courts-and-legal-bias",
}

PUBLIC_FINANCE = {
    "current-year-structure-of-taxes-in-the-united-states",
    "critical-review-of-major-official-financial-crisis-inquiry-reports",
}

HEALTH = {
    "gaht",
    "gaht-research-report-summary",
    "global-population-dynamics-peaks-in-population-level-and-growth-rates",
    "male-suicide",
    "male-suicide-research-outline",
}

ENGINEERING = {
    "brickmaking-history-materials-processes-and-production-planning",
    "darrieus-vawt-design-construction-1-10-kw",
    "desalination-plant-design-and-construction",
    "electric-motor-design-principles-types-and-practices",
    "electric-motors-v2",
    "highway-engineering",
    "in-house-vertical-farms",
    "savonius-wind-turbines-comprehensive-design-diy-guide",
}

MEDIA = {
    "fake-populism-and-neil-young",
    "grrm-deconstructed",
    "hasan",
    "hasanabi-popularity-analysis",
    "liberal-gothic",
    "liberal-gothic-an-analytical-report",
    "liberal-gothic-quick-facts",
    "mauler",
    "matrix-culture",
    "meme-culture-and-borderer-right-style-a-research-report",
    "taylor",
}

PHILOSOPHY = {
    "emptiness-of-deleuze",
    "nietzche-math-critique",
    "obj-vs-sub",
}

SOCIALIST_THEORY = {
    "1inventing-socialism",
    "2christian-socialism",
    "3mutualism",
    "4chartist",
    "christian-socialism-report-request",
    "co-opting-the-left",
    "marx-engels",
    "marx-engels-manifesto-analysis",
    "marxism-bibliography",
    "marxism-evolution",
    "marxism-research-clarifications",
    "proudhon-mutualism-report",
}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any) -> bool:  # pragma: no cover - serializer hook
        return True


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def dump_yaml(data: dict[str, Any]) -> str:
    return "---\n" + yaml.dump(
        data,
        Dumper=NoAliasDumper,
        sort_keys=False,
        allow_unicode=True,
        width=100,
        default_flow_style=False,
    ) + "...\n"


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def infer_type(title: str) -> str:
    lower = title.lower()
    if "bibliograph" in lower:
        return "bibliography"
    if "outline" in lower:
        return "outline"
    if "quick facts" in lower:
        return "briefing"
    if "summary" in lower:
        return "summary"
    if "guide" in lower or "field guide" in lower:
        return "guide"
    if "essay" in lower:
        return "essay"
    return "report"


def infer_kind(title: str) -> str:
    lower = title.lower()
    if "bibliograph" in lower:
        return "annotated bibliography"
    if "outline" in lower:
        return "research outline"
    if "quick facts" in lower:
        return "fact sheet"
    if "summary" in lower:
        return "executive summary"
    if "history" in lower:
        return "historical survey"
    if "critique" in lower:
        return "critical analysis"
    if "analysis" in lower or "analytical report" in lower:
        return "analytical report"
    if "guide" in lower:
        return "practical guide"
    return "research report"


def domain_bundle(folder: str, title: str) -> dict[str, Any]:
    if folder in MATH or any(word in title.lower() for word in ["algebra", "topology", "geometry", "number theory", "analysis", "category theory"]):
        return {
            "loc": {
                "class": "QA",
                "label": "Mathematics",
                "description": "Mathematics, mathematical history, and mathematical methods.",
            },
            "domain": "mathematics",
            "discipline": "mathematics",
            "subdiscipline": "mathematical history and theory",
            "categories": ["Mathematics", "History of Mathematics"],
            "subjects": ["Mathematics", "History of mathematics"],
            "audience": "general mathematically literate reader",
        }
    if folder in COMPUTING or any(word in title.lower() for word in ["html", "css", "javascript", "llm", "neural network", "chip", "type theory"]):
        return {
            "loc": {
                "class": "QA76",
                "label": "Computer science",
                "description": "Computer science, software, web standards, and computing history.",
            },
            "domain": "computing",
            "discipline": "computer science",
            "subdiscipline": "computing history and software systems",
            "categories": ["Computing", "Technology"],
            "subjects": ["Computer science", "Technology"],
            "audience": "general technically literate reader",
        }
    if folder in LAW or any(word in title.lower() for word in ["law", "legal", "court", "judicial", "judge", "lawyer"]):
        return {
            "loc": {
                "class": "KF",
                "label": "Law of the United States",
                "description": "United States law, courts, legal doctrine, and legal institutions.",
            },
            "domain": "law",
            "discipline": "law",
            "subdiscipline": "united states law",
            "categories": ["Law", "United States Law"],
            "subjects": ["Law", "United States law"],
            "audience": "general legal reader",
        }
    if folder in PUBLIC_FINANCE or "tax" in title.lower() or "financial-crisis" in title.lower():
        return {
            "loc": {
                "class": "HJ",
                "label": "Public finance",
                "description": "Public finance, taxation, and fiscal policy.",
            },
            "domain": "public finance",
            "discipline": "economics",
            "subdiscipline": "public finance",
            "categories": ["Public Finance", "Economics"],
            "subjects": ["Public finance", "Fiscal policy"],
            "audience": "policy-oriented general reader",
        }
    if folder in HEALTH or any(word in title.lower() for word in ["suicide", "gaht", "population"]):
        return {
            "loc": {
                "class": "RA",
                "label": "Public aspects of medicine",
                "description": "Public health, health policy, epidemiology, and medicine in society.",
            },
            "domain": "health",
            "discipline": "public health",
            "subdiscipline": "health policy and epidemiology",
            "categories": ["Health", "Public Health"],
            "subjects": ["Public health", "Health policy"],
            "audience": "general policy-oriented reader",
        }
    if folder in ENGINEERING or any(word in title.lower() for word in ["motor", "wind", "desalination", "brick", "highway", "farm"]):
        loc = {
            "class": "TA",
            "label": "Engineering",
            "description": "Engineering, applied technology, infrastructure, and industrial design.",
        }
        if any(word in title.lower() for word in ["motor", "maxwell", "heaviside"]):
            loc = {
                "class": "TK",
                "label": "Electrical engineering",
                "description": "Electrical engineering, motors, electromagnetism, and power systems.",
            }
        return {
            "loc": loc,
            "domain": "engineering",
            "discipline": "engineering",
            "subdiscipline": "applied design and technology",
            "categories": ["Engineering", "Technology"],
            "subjects": ["Engineering", "Technology"],
            "audience": "technically curious general reader",
        }
    if folder in MEDIA or any(word in title.lower() for word in ["neil young", "martin", "lorenz", "gothic", "meme", "film criticism", "matrix"]):
        return {
            "loc": {
                "class": "PN",
                "label": "Literature and media studies",
                "description": "Literature, media studies, criticism, and cultural analysis.",
            },
            "domain": "culture",
            "discipline": "media and cultural studies",
            "subdiscipline": "criticism and interpretation",
            "categories": ["Culture", "Media Studies"],
            "subjects": ["Culture", "Media studies"],
            "audience": "general reader",
        }
    if folder in PHILOSOPHY or any(word in title.lower() for word in ["deleuze", "objectivity", "subjectivity", "symbols"]):
        return {
            "loc": {
                "class": "B",
                "label": "Philosophy",
                "description": "Philosophy, theory, epistemology, and conceptual criticism.",
            },
            "domain": "philosophy",
            "discipline": "philosophy",
            "subdiscipline": "social and political philosophy",
            "categories": ["Philosophy", "Theory"],
            "subjects": ["Philosophy", "Theory"],
            "audience": "general reader",
        }
    if folder in SOCIALIST_THEORY or any(word in title.lower() for word in ["socialism", "marx", "mutualism", "communist"]):
        return {
            "loc": {
                "class": "HX",
                "label": "Socialism. Communism. Anarchism",
                "description": "Socialism, communism, anarchism, and related intellectual history.",
            },
            "domain": "political theory",
            "discipline": "political theory",
            "subdiscipline": "socialist and radical thought",
            "categories": ["Political Theory", "History", "Socialism"],
            "subjects": ["Political theory", "Socialism"],
            "audience": "general reader",
        }
    return {
        "loc": {
            "class": "JA",
            "label": "Political science (General)",
            "description": "Politics, political history, social theory, and public debate.",
        },
        "domain": "politics",
        "discipline": "political science",
        "subdiscipline": "history and social analysis",
        "categories": ["Politics", "History", "Political Theory"],
        "subjects": ["Politics", "History"],
        "audience": "general reader",
    }


def unique_keep_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if not item:
            continue
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def basic_tags(slug: str, categories: list[str]) -> list[str]:
    tags = [slug]
    tags.extend(slugify(cat) for cat in categories[:3])
    return unique_keep_order(tags)[:6]


def basic_keywords(title: str, subtitle: str, categories: list[str], loc_label: str) -> list[str]:
    items = [title]
    if subtitle:
        items.append(subtitle)
    items.extend(categories[:3])
    if loc_label:
        items.append(loc_label)
    return unique_keep_order(items)[:8]


def assign_report_numbers(articles: list[tuple[Path, dict[str, Any]]]) -> dict[str, int]:
    dated = []
    for article_path, data in articles:
        date = data.get("date", "")
        if isinstance(date, str) and date.strip():
            dated.append((date.strip(), article_path.parent.name))
    dated.sort(key=lambda row: (row[0], row[1]))
    return {folder: index for index, (_, folder) in enumerate(dated, start=1)}


def main() -> int:
    articles = []
    for article in sorted(MD_ROOT.glob("*/article.yaml")):
        articles.append((article, load_yaml(article)))

    numbering = assign_report_numbers(articles)

    for article_path, data in articles:
        folder = article_path.parent.name
        title = data.get("title", "") or ""
        subtitle = data.get("subtitle", "") or ""
        slug = data.get("slug", "") or ""
        date = data.get("date", "") or ""
        bundle = domain_bundle(folder, title)

        # Global standardization
        data["author"] = list(AUTHOR)
        data["authors"] = list(AUTHOR)
        if not data.get("creator"):
            data["creator"] = ["Salvador Guzman"]
        data["publisher"] = PUBLISHER
        if not data.get("license"):
            data["license"] = "CC0-1.0"
        if not data.get("rights"):
            data["rights"] = "CC0-1.0"
        if not data.get("lang"):
            data["lang"] = "en"
        if not data.get("language"):
            data["language"] = "English"
        if not data.get("edition"):
            data["edition"] = "1"
        if not data.get("revision"):
            data["revision"] = "1.0.0"
        if not data.get("reference-section-title"):
            data["reference-section-title"] = "References"
        if not data.get("format"):
            data["format"] = "markdown"
        if not data.get("type") and title:
            data["type"] = infer_type(title)
        if not data.get("status"):
            data["status"] = "draft" if data.get("draft") else "complete"
        if title and not data.get("linkTitle"):
            data["linkTitle"] = title
        if date:
            if not data.get("publishDate"):
                data["publishDate"] = date
            if not data.get("lastmod"):
                data["lastmod"] = date
        if title and not data.get("summary"):
            data["summary"] = data.get("description") or data.get("abstract") or ""
        if slug and not data.get("identifier"):
            data["identifier"] = f"urn:marginalia:{slug}"

        # Series and numbering
        number = numbering.get(folder)
        if number is not None:
            number_str = f"{number:03d}"
            year_int = int(date[:4]) if date else 0
            year_str = str(year_int) if year_int else ""
            data["report-no"] = number_str
            data["report-number"] = number_str
            data["report_no"] = number
            data["report_number"] = number
            data["report-year"] = year_str
            data["report_year"] = year_int
            if not data.get("series"):
                data["series"] = "Marginalia Reports"
            if not data.get("series-title"):
                data["series-title"] = data["series"]
            data["series-number"] = number
            data["series_title"] = data["series-title"]
            data["series_number"] = number

            report = data.get("report", {}) or {}
            report["id"] = data.get("identifier", "")
            report["organization"] = PUBLISHER
            report["series"] = data.get("series", "")
            report["number"] = number_str
            report["year"] = year_int
            report["version"] = data.get("revision", "")
            report["name"] = title
            report["topic"] = title
            if subtitle and not report.get("scope"):
                report["scope"] = subtitle
            if not report.get("kind") and title:
                report["kind"] = infer_kind(title)
            if not report.get("type") and data.get("type"):
                report["type"] = data["type"]
            if not report.get("domain"):
                report["domain"] = bundle["domain"]
            if not report.get("discipline"):
                report["discipline"] = bundle["discipline"]
            if not report.get("subdiscipline"):
                report["subdiscipline"] = bundle["subdiscipline"]
            if not report.get("audience"):
                report["audience"] = bundle["audience"]
            if not report.get("topic"):
                report["topic"] = title
            data["report"] = report

        # LOC
        loc = data.get("library_of_congress_classification", {}) or {}
        if not loc.get("class"):
            loc["class"] = bundle["loc"]["class"]
        if not loc.get("label"):
            loc["label"] = bundle["loc"]["label"]
        if not loc.get("description"):
            loc["description"] = bundle["loc"]["description"]
        data["library_of_congress_classification"] = loc

        # First-pass topical fields for blank records
        if not data.get("categories") and title:
            data["categories"] = bundle["categories"]
        if not data.get("subject") and title:
            data["subject"] = bundle["subjects"]
        if not data.get("subjects") and title:
            data["subjects"] = bundle["subjects"]
        if not data.get("tags") and slug:
            data["tags"] = basic_tags(slug, data.get("categories", []))
        if not data.get("keywords") and title:
            data["keywords"] = basic_keywords(
                title,
                subtitle,
                data.get("categories", []),
                data["library_of_congress_classification"].get("label", ""),
            )

        article_path.write_text(dump_yaml(data), encoding="utf-8")
        print(article_path.parent.name)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
