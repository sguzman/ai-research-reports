# Scripts

## Supported editorial tooling

- `article_lint.py` — read-only editorial and lifecycle validation. Safe to run against the corpus; it never writes files.

## Legacy tooling

The following scripts predate the current editorial workflow and should be treated as **legacy migration utilities**, not canonical automation:

- `metadata_enrich.py`
- `metadata_normalizer.py`
- `metadata_validator.py`

They may encode assumptions that were useful during earlier bulk migration work but are not trusted to decide editorial quality, publication state, or canonical metadata for new articles.

Do not run legacy scripts automatically from GitHub Actions and do not make publication depend on them. When their remaining useful behavior is understood, replace it with smaller explicit tools and retire the legacy implementation.

The canonical workflow and lifecycle rules are documented in [`../EDITORIAL_WORKFLOW.md`](../EDITORIAL_WORKFLOW.md).
