# Scripts

## Supported editorial tooling

- `editorial_lint.py` — profile-aware, read-only editorial/lifecycle/integrity validation. It never rewrites article content.

The linter implements the mechanically safe subset of [`../EDITORIAL_STANDARD.md`](../EDITORIAL_STANDARD.md): universal AI-residue/structure/asset checks plus perspective checks selected by `editorial_profile`. Legacy articles with no profile are reported as `unclassified_profile`; the tool deliberately does **not** infer a profile and therefore does not apply academic perspective rules to them.

Examples:

```bash
python scripts/editorial_lint.py --slug example-article
python scripts/editorial_lint.py --json
python scripts/editorial_lint.py --strict
```

Spelling, grammar, factual review, quotation judgment, intentional voice, duplicate resolution, and live external-link verification remain editorial responsibilities rather than blind rewrites.

## Legacy tooling

The following scripts predate the current editorial workflow and should be treated as **legacy migration utilities**, not canonical automation:

- `metadata_enrich.py`
- `metadata_normalizer.py`
- `metadata_validator.py`

They may encode assumptions that were useful during earlier bulk migration work but are not trusted to decide editorial quality, publication state, editorial profile, or canonical metadata for new articles.

Do not run legacy scripts automatically from GitHub Actions and do not make publication depend on them. When their remaining useful behavior is understood, replace it with smaller explicit tools and retire the legacy implementation.

The canonical workflow is documented in [`../EDITORIAL_WORKFLOW.md`](../EDITORIAL_WORKFLOW.md), the profile rules in [`../EDITORIAL_STANDARD.md`](../EDITORIAL_STANDARD.md), and the inherited baseline in [`../CORPUS_AUDIT.md`](../CORPUS_AUDIT.md).
