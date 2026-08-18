# Editorial workflow

This repository is the canonical source for AI-assisted research articles. The blog repository (`sguzman/marginalia`) is a publication target, not a second editorial source of truth.

## Canonical article package

Each article lives at:

```text
data/md/<slug>/
  main.md
  article.yaml
  assets/          # optional
```

`main.md` contains the article body. `article.yaml` owns identity, descriptive metadata, lifecycle state, and publication intent. Generated blog frontmatter must never be copied back into this repository.

## Operating model

Article intake is deliberately operator-driven.

1. Generate or collect a candidate article outside the repository.
2. Convert DOCX/PDF to Markdown explicitly when needed.
3. Run an editorial review of the text before trusting generated metadata.
4. Enforce `ACADEMIC_STYLE.md` for ordinary nonfiction/report material.
5. Verify external links and externally hosted images that matter to the article at review time.
6. Create or update the canonical package in this repository.
7. Run `scripts/article_lint.py --strict`.
8. Resolve errors and warnings, distinguishing legitimate quotations/creative exceptions from narration defects.
9. Record corrections through the repository's established changelog/revision mechanism when that mechanism is present.
10. Move lifecycle state forward only after editorial approval.
11. Publish the approved canonical package into Marginalia as a one-way projection.

No GitHub workflow should convert source documents, rewrite article metadata, or commit generated changes back into this repository. CI may validate; it must not edit.

## Lifecycle

The canonical lifecycle is:

```text
draft -> review -> ready -> published
                    |
                    +-> archived (when appropriate)
```

Rules:

- `draft`: incomplete or newly imported. `draft: true`.
- `review`: being fact-checked or edited. `draft: true`.
- `ready`: editorially approved and eligible for publication. `draft: false`.
- `published`: confirmed present in the publication target. `draft: false`.
- `archived`: retained but not eligible for normal publication.
- `complete`: accepted only as a legacy status; migrate it to `published` when an article is next touched.

`ready` is the publication gate. The existence of a folder, DOCX file, Markdown file, or Hugo post is never publication intent.

For ordinary academic material, `ready` also means the article has been checked for spelling and grammar, first/second-person narration, self-reference, prompt/assistant residue, assignment-stage hypothesis language, missing local assets, malformed or presently broken links, and broken diagrams. Creative work may intentionally differ, but that exception should be explicit in its classification rather than accidental.

## Metadata profiles

The same canonical schema can support differently sized pieces without forcing a short article to imitate a monograph.

### `note`

Use for short, focused pieces. The editorially important fields are title, description, date, authorship, classification, lifecycle, and stable identity.

### `research-brief`

Use for shorter research articles that make an evidence-backed argument. Add a meaningful summary or abstract, useful discovery metadata, and enough methodological or scope information to understand what the piece is claiming.

### `report`

Use for substantial reports. Populate the full report, series, and export metadata where it is actually meaningful.

Blank compatibility fields may remain present in `article.yaml`; they should not be filled with invented detail merely to satisfy a schema.

## Editorial validation

`scripts/article_lint.py` is read-only. It never rewrites the corpus.

```bash
python scripts/article_lint.py --slug example-article
python scripts/article_lint.py --json
python scripts/article_lint.py --strict
```

The linter intentionally checks for problems that schema validation misses: lifecycle contradictions, URL-contaminated titles, prompt or assistant residue, raw ChatGPT citation markers, malformed links, first/second-person narration, self-reference, hypothesis-testing meta-language, local links/images whose targets do not exist inside the article package, paths that escape the package, multiple H1s, unmatched code fences, and suspicious Mermaid rendering.

Some checks remain editorial rather than mechanical. In particular, spelling/grammar and current health of remote HTTP links are verified during review because blind automation is too error-prone for academic vocabulary, proper nouns, quotations, and transient network failures.

## Publication boundary

Marginalia may read canonical packages and derive Hugo posts. A publisher must:

- never modify this repository;
- never change `draft` or `status`;
- publish only explicitly eligible states (`ready` or `published`);
- preserve personal and non-generated Marginalia posts;
- be idempotent;
- fail closed when source metadata is malformed.

The publication target may keep a generated manifest for observability, but that manifest is never authoritative over `article.yaml`.
