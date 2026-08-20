# Scripts

## Supported editorial tooling

- `editorial_lint.py` — profile-aware, read-only editorial/lifecycle/integrity validation. It never rewrites article content.
- `duplicate_audit.py` — corpus-level, read-only duplicate/derivative candidate finder. It never chooses canonical status, archives a package, or merges prose.
- `editorial_queue.py` — read-only coverage report comparing canonical article packages against the persistent operational queue in `editorial/QUEUE.yaml`.

The linter implements the mechanically safe subset of [`../EDITORIAL_STANDARD.md`](../EDITORIAL_STANDARD.md): universal AI-residue/structure/asset checks plus perspective checks selected by `editorial_profile`. Legacy articles with no profile are reported as `unclassified_profile`; the tool deliberately does **not** infer a profile and therefore does not apply academic perspective rules to them.

Local dependency validation covers both ordinary Markdown links/images and converted HTML `<img src="…">` / `<a href="…">` references. Local targets must stay inside the article package and resolve to real files; canonical local support belongs under `assets/`, with legacy locations treated as warnings in draft/review and errors once an article is ready or published.

Examples:

```bash
python scripts/editorial_lint.py --slug example-article
python scripts/editorial_lint.py --json
python scripts/editorial_lint.py --strict
```

Pull requests that change files beneath `data/md/<slug>/` are also checked by `.github/workflows/editorial-lint.yml`. The workflow identifies the changed article packages, requires each changed package's `CHANGELOG.md` to be changed in the same PR, and then runs the read-only linter on each package. It is intentionally not a rewriting, metadata-normalizing, or publication workflow.

## Editorial queue coverage

`editorial_queue.py` treats `editorial/QUEUE.yaml` as an operational handoff ledger, not as canonical lifecycle metadata. It discovers real packages from `data/md/`, reports which packages are represented in the queue, lists untriaged packages, and fails only when the queue contains a stale slug that no longer exists as a canonical package.

Examples:

```bash
python scripts/editorial_queue.py
python scripts/editorial_queue.py --untriaged
python scripts/editorial_queue.py --json
```

An article not listed in `editorial/QUEUE.yaml` is simply untriaged; it is not implicitly clean, ready, or low priority. See [`../editorial/README.md`](../editorial/README.md) for the batch/handoff protocol.

## Duplicate candidate audit

`duplicate_audit.py` normalizes article bodies, computes exact normalized-body hashes, and compares word-shingle overlap across the corpus. It reports three kinds of hints:

- `exact-normalized-duplicate`
- `near-duplicate-candidate`
- `containment-or-derivative-candidate`

Examples:

```bash
python scripts/duplicate_audit.py
python scripts/duplicate_audit.py --slug american-judicial-process
python scripts/duplicate_audit.py --slug gaht --slug gaht-research-report-summary
python scripts/duplicate_audit.py --json
```

The default heuristic uses 5-word shingles, a 0.72 Jaccard threshold for similarly sized near-duplicates, and 0.88 containment of the smaller shingle set for likely containment/derivation. These are candidate-generation thresholds, not editorial truth. They may be tuned when the corpus provides evidence that they are too noisy or too strict.

A high score does **not** authorize automatic deletion, archiving, merging, or metadata changes. The editor must inspect the pair under [`../DUPLICATE_POLICY.md`](../DUPLICATE_POLICY.md), distinguish duplicate from derivative/fork/shared-topic overlap, preserve unique material, and record any final relationship in canonical metadata and changelogs.

Spelling, grammar, factual review, quotation judgment, intentional voice, duplicate disposition, merge synthesis, numerical/safety review, and live external-link verification remain editorial responsibilities rather than blind rewrites.

## Legacy tooling

The following scripts predate the current editorial workflow and should be treated as **legacy migration utilities**, not canonical automation:

- `metadata_enrich.py`
- `metadata_normalizer.py`
- `metadata_validator.py`

They may encode assumptions that were useful during earlier bulk migration work but are not trusted to decide editorial quality, publication state, editorial profile, duplicate disposition, or canonical metadata for new articles.

Do not run legacy scripts automatically from GitHub Actions and do not make publication depend on them. When their remaining useful behavior is understood, replace it with smaller explicit tools and retire the legacy implementation.

The canonical workflow is documented in [`../EDITORIAL_WORKFLOW.md`](../EDITORIAL_WORKFLOW.md), the profile rules in [`../EDITORIAL_STANDARD.md`](../EDITORIAL_STANDARD.md), duplicate/synthesis policy in [`../DUPLICATE_POLICY.md`](../DUPLICATE_POLICY.md), persistent operational state in [`../editorial/`](../editorial/), and the inherited baseline in [`../CORPUS_AUDIT.md`](../CORPUS_AUDIT.md).
