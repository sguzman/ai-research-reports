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

`main.md` contains the body. `article.yaml` owns identity, descriptive metadata, editorial classification, lifecycle state, document relationships, and publication intent. `CHANGELOG.md` records canonical editorial changes. Generated blog frontmatter must never be copied back into this repository.

Legacy packages may still contain root-level covers or `media/` trees. Those are migration debt. New ingestion and normalization place article-local dependencies under `assets/`.

## Operating model

Article intake is deliberately operator-driven.

1. Generate or collect a candidate artifact outside the repository.
2. Convert DOCX/PDF to Markdown explicitly when needed.
3. Inspect the text before trusting generated metadata.
4. Classify the artifact's **form** (`type`), **editorial profile** (`editorial_profile`), and intentional **voice** (`voice`) under `EDITORIAL_STANDARD.md`.
5. Run a corpus duplicate/overlap check before expensive body cleanup. Use `scripts/duplicate_audit.py` as a candidate finder and apply `DUPLICATE_POLICY.md` editorially.
6. If meaningful overlap exists, classify the relationship and choose a disposition: keep separate, archive a duplicate, retain a deliberate derivative, merge into an existing canonical work, or synthesize a new canonical target.
7. Apply universal integrity rules and the selected profile-specific prose rules to the artifact that should remain active.
8. Verify external links and externally hosted images that matter to the article at review time.
9. Normalize local support files beneath `assets/` and repair image/file/diagram references.
10. Create or update the canonical package and relationship metadata.
11. Run `scripts/editorial_lint.py --strict`.
12. Resolve findings editorially; a linter finding is evidence for inspection, not permission to destroy intentional voice.
13. Record changes, including duplicate/merge decisions, in the article's `CHANGELOG.md` using the established timestamp/summary table convention.
14. Move lifecycle state forward only after editorial approval and duplicate/relationship resolution.
15. Publish the approved canonical package into Marginalia as a one-way projection.

No GitHub workflow should convert source documents, rewrite article prose or metadata, infer an editorial profile, choose a canonical duplicate, merge reports, or commit generated changes back into this repository. CI may validate and nominate candidates; it must not edit or make editorial dispositions.

## Duplicate review during intake

Duplicate review should occur early enough to avoid polishing redundant source documents unnecessarily.

The minimum review asks:

- Is the body an exact or normalized exact duplicate of an existing package?
- Does another package share substantially the same thesis, outline, examples, citations, or long passages?
- Is the candidate actually a summary or derivative of an existing work?
- Is the overlap topical only, with genuinely different form, argument, method, audience, or voice?
- Does either version contain unique claims, evidence, citations, tables, diagrams, or assets that should survive?
- Should one existing package remain canonical, or would a new synthesis target be stronger?

Do not use source-file boundaries as the final organization of a merged work. For merge clusters, pool material with provenance and synthesize at the claim and section level under a unified subject-driven outline.

See `DUPLICATE_POLICY.md` for relationship classes, disposition rules, metadata, and provenance requirements.

## Lifecycle

The canonical lifecycle is:

```text
draft -> review -> ready -> published
                    |
                    +-> archived (when appropriate)
```

Rules:

- `draft`: incomplete or newly imported. `draft: true`.
- `review`: being fact-checked, classified, edited, or checked for duplicate relationships. `draft: true`.
- `ready`: editorially approved and eligible for publication. `draft: false`.
- `published`: confirmed present in the publication target. `draft: false`.
- `archived`: retained but not eligible for normal publication. This is also the lifecycle used for accidental duplicates, superseded sources, and merged sources after their provenance is recorded.
- `complete`: accepted only as a legacy status; migrate it to `published` when an article is next substantively touched and its publication state is confirmed.

`ready` is the publication gate. The existence of a folder, DOCX file, Markdown file, or Hugo post is never publication intent.

`ready` means the universal rules, the declared editorial profile, and required duplicate/relationship review have been satisfied. A `stylized` essay is not required to sound academic; an `academic` report is.

Duplicate, superseded, merged-source, derivative, and fork are relationship descriptions rather than lifecycle states. This keeps editorial maturity separate from provenance and avoids expanding publication logic unnecessarily.

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

## Relationship metadata

`article.yaml` may record inter-document relationships independently of lifecycle:

```yaml
relationships:
  exact_duplicates: []
  near_duplicates: []
  derived_from: []
  derivatives: []
  merged_from: []
  merged_into: ""
  related: []

editorial:
  duplicate_review:
    status: ""
    relationship: ""
    disposition: ""
    canonical_slug: ""
    rationale: ""
```

Use canonical slugs. Leave fields empty when unresolved rather than inventing relationships.

## Metadata depth by form

The canonical schema can support differently sized pieces without forcing a short article to imitate a monograph.

- `note`: core identity, description, date, authorship, classification, lifecycle, stable identity, and relationships when applicable.
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

Keep newest entries first. New articles do not need fictional history, but once an established canonical package is corrected, reclassified, fact-repaired, structurally migrated, declared duplicate/derived, or used in a synthesis, the change should be recorded.

## Editorial validation

`scripts/editorial_lint.py` is read-only and never rewrites the corpus. The profile system in `EDITORIAL_STANDARD.md` is authoritative: perspective findings are selected according to `editorial_profile` rather than blindly applied to every artifact. Legacy articles with no profile are reported as unclassified and are not automatically subjected to academic perspective rules.

`scripts/duplicate_audit.py` is also read-only. It reports exact normalized-body matches and heuristic high-similarity/high-containment candidate pairs. It does not decide whether a pair is a duplicate, derivative, fork, or merge cluster and does not edit metadata.

Mechanical checks are appropriate for lifecycle contradictions, URL-contaminated titles, prompt/assistant residue, raw citation markers, malformed links, local dependency integrity, H1 structure, unmatched code fences, and diagram/source hazards. Spelling/grammar, quotation judgment, factual review, intentional voice, duplicate disposition, merge synthesis, and live external-link health require editorial judgment.

The baseline state of the inherited corpus is documented in `CORPUS_AUDIT.md`. That file is an inventory, not a license for automatic rewriting.

## Publication boundary

Marginalia may read canonical packages and derive Hugo posts. A publisher must:

- never modify this repository;
- never change `draft`, `status`, `editorial_profile`, `voice`, or document relationships;
- publish only explicitly eligible states (`ready` or `published`);
- never publish `archived` duplicate or merged-source packages through the normal research pipeline;
- preserve personal and non-generated Marginalia posts;
- reproduce canonical local assets;
- be idempotent;
- fail closed when source metadata or dependencies are malformed.

The publication target may keep generated observability data, but it is never authoritative over the canonical package.
