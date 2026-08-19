# Editorial workflow

This repository is the canonical source for AI-assisted research articles and other long-form written artifacts. The blog repository (`sguzman/marginalia`) is a publication target, not a second editorial source of truth.

## Canonical article package

Each article lives at:

```text
data/md/<slug>/
  main.md
  article.yaml
  CHANGELOG.md      # created/maintained once the article has editorial history
  assets/           # optional; canonical location for local support files
```

`main.md` contains the body. `article.yaml` owns identity, descriptive metadata, editorial classification, lifecycle state, and publication intent. `CHANGELOG.md` records canonical editorial changes. Generated blog frontmatter must never be copied back into this repository.

Legacy packages may still contain root-level covers or `media/` trees. Those are migration debt. New ingestion and normalization place article-local dependencies under `assets/`.

## Operating model

Article intake is deliberately operator-driven.

1. Generate or collect a candidate artifact outside the repository.
2. Convert DOCX/PDF to Markdown explicitly when needed.
3. Inspect the text before trusting generated metadata.
4. Classify the artifact's **form** (`type`), **editorial profile** (`editorial_profile`), and intentional **voice** (`voice`) under `EDITORIAL_STANDARD.md`.
5. Apply universal integrity rules and the selected profile-specific prose rules.
6. Verify external links and externally hosted images that matter to the article at review time.
7. Normalize local support files beneath `assets/` and repair image/file/diagram references.
8. Create or update the canonical package.
9. Run read-only mechanical validation.
10. Resolve findings editorially; a linter finding is evidence for inspection, not permission to destroy intentional voice.
11. Record changes in the article's `CHANGELOG.md` using the established timestamp/summary table convention.
12. Move lifecycle state forward only after editorial approval.
13. Publish the approved canonical package into Marginalia as a one-way projection.

No GitHub workflow should convert source documents, rewrite article prose or metadata, infer an editorial profile, or commit generated changes back into this repository. CI may validate; it must not edit.

## Lifecycle

The canonical lifecycle is:

```text
draft -> review -> ready -> published
                    |
                    +-> archived (when appropriate)
```

Rules:

- `draft`: incomplete or newly imported. `draft: true`.
- `review`: being fact-checked, classified, or edited. `draft: true`.
- `ready`: editorially approved and eligible for publication. `draft: false`.
- `published`: confirmed present in the publication target. `draft: false`.
- `archived`: retained but not eligible for normal publication.
- `complete`: accepted only as a legacy status; migrate it to `published` when an article is next substantively touched and its publication state is confirmed.

`ready` is the publication gate. The existence of a folder, DOCX file, Markdown file, or Hugo post is never publication intent.

`ready` means both the universal rules and the declared editorial profile have been satisfied. A `stylized` essay is not required to sound academic; an `academic` report is.

## Three independent metadata dimensions

### `type`: what the artifact is

Examples include:

- `note`
- `research-brief`
- `report`
- `essay`
- `reference`
- `dialogue`
- `fiction`

Size does not by itself determine style. A short note may be academic; a long essay may be stylized.

### `editorial_profile`: what prose rules apply

Allowed initial profiles:

- `academic`
- `argumentative`
- `stylized`
- `personal`
- `creative`

See `EDITORIAL_STANDARD.md` for the contract of each profile.

Legacy articles without this field are **unclassified**, not implicitly academic. The census may propose candidates, but classification becomes canonical only through editorial review.

### `voice`: what intentional voice should be preserved

Examples include `neutral`, `polemical`, `nietzschean`, and `literary`. Blank is valid when no special voice needs to be recorded.

`voice` is descriptive. It never excuses prompt leakage, broken citations, missing files, or other accidental defects.

## Metadata depth by form

The canonical schema can support differently sized pieces without forcing a short article to imitate a monograph.

- `note`: core identity, description, date, authorship, classification, lifecycle, and stable identity.
- `research-brief`: add a meaningful summary/abstract, useful discovery metadata, and enough method/scope information to understand the claim.
- `report`: populate report, series, methods, scope, and export metadata where genuinely meaningful.
- `essay`/creative forms: do not fabricate report metadata merely because legacy tooling expected every artifact to be a report.

Blank compatibility fields may remain present; do not invent values merely to satisfy an old schema.

## Changelog convention

The repository already contains per-article changelogs. Preserve that convention:

```markdown
# Changelog

| Timestamp | Summary |
| --- | --- |
| YYYY-MM-DD HH:MM:SS TZ | Concise description of the editorial change. |
```

Keep newest entries first. New articles do not need fictional history, but once an established canonical package is corrected, reclassified, fact-repaired, or structurally migrated, the change should be recorded.

## Editorial validation

`scripts/article_lint.py` is read-only and never rewrites the corpus. The profile system in `EDITORIAL_STANDARD.md` is authoritative: perspective findings must be interpreted according to `editorial_profile` rather than blindly applied to every artifact.

Mechanical checks are appropriate for lifecycle contradictions, URL-contaminated titles, prompt/assistant residue, raw citation markers, malformed links, local dependency integrity, H1 structure, unmatched code fences, and diagram/source hazards. Spelling/grammar, quotation judgment, factual review, intentional voice, and live external-link health require editorial judgment.

The baseline state of the inherited corpus is documented in `CORPUS_AUDIT.md`. That file is an inventory, not a license for automatic rewriting.

## Publication boundary

Marginalia may read canonical packages and derive Hugo posts. A publisher must:

- never modify this repository;
- never change `draft`, `status`, `editorial_profile`, or `voice`;
- publish only explicitly eligible states (`ready` or `published`);
- preserve personal and non-generated Marginalia posts;
- reproduce canonical local assets;
- be idempotent;
- fail closed when source metadata or dependencies are malformed.

The publication target may keep generated observability data, but it is never authoritative over the canonical package.
