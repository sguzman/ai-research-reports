# Editorial batch log

This is the repository-level operational history of corpus cleanup. It complements—never replaces—the richer `data/md/<slug>/CHANGELOG.md` inside each changed article package.

## 2026-08-20

### PR #17 — Clean stylized Nietzschean essay without neutralizing voice

Packages:
- `nietzche-math-critique`

Result:
- preserved `essay` / `stylized` / `nietzschean` classification and deliberately severe rhetoric;
- removed only an accidental duplicate numbered final-section heading;
- documented protected stylistic features;
- kept canonical lifecycle `published`.

Remaining operational work: migrate the legacy Marginalia copy into canonical publisher management.

### PR #16 — Record judicial report publication

Packages:
- `american-judicial-process`

Result:
- recorded successful managed Marginalia publication;
- advanced canonical lifecycle `ready` → `published`;
- bumped canonical report revision/version;
- no body change.

### PR #15 — Finalize judicial report for publication

Packages:
- `american-judicial-process`

Result:
- corrected the distinction between 91 federal judicial districts with Article III judges and the three term-appointed territorial district courts;
- added the Court of International Trade to the Article III inventory;
- replaced transient magistrate/bankruptcy salary links with the durable 92%-of-district-judge statutory rule;
- strengthened Texas, Arizona, California, and federal official-source links;
- rechecked 2026 compensation and the enacted Arizona 2027 salary schedule;
- advanced `review` → `ready`.

### PR #14 — Classify related Borderer meme reports

Packages:
- `meme-culture-and-borderer-right-style-a-research-report`
- `distinguishing-borderer-right-coded-vs-left-awkward-authentic-internet-memes-a-research-framewo`

Result:
- duplicate review concluded `fork / keep-separate`, not duplicate;
- broad cultural-analysis report retained separately from the coding/corpus methodology framework;
- both classified `report` / `academic` / `neutral`;
- framework title metadata repaired;
- both moved legacy `complete` → `review`.

### PR #13 — Resolve duplicate Proudhon mutualism reports

Packages:
- `proudhon-mutualism-report`
- `3mutualism`

Result:
- confirmed the same substantive report under different packaging/conversion quality;
- selected cleaner `proudhon-mutualism-report` as canonical and moved it to `review`;
- archived `3mutualism` as duplicate/repackaging provenance;
- preserved legacy `mutualism` identity as alias;
- left source-quality/citation cleanup for canonical review.

### PR #12 — Resolve duplicate male-suicide report cluster

Packages:
- `male-suicide`
- `male-suicide-research-outline`

Result:
- determined the supposed research outline contains the same finished substantive report;
- restored folder-consistent canonical slug/identity for `male-suicide`;
- returned inherited `published` → `review` because body integrity and high-stakes evidence review remain incomplete;
- archived the fake-outline duplicate;
- recorded body, asset, epidemiology, intervention, policy, and projection blockers without substantively rewriting those claims.

### PR #11 — Apply duplicate relationships to known corpus cases

Packages:
- `american-judicial-process`
- `judges-in-the-judicial-process-of-the-united-states`
- `gaht`
- `gaht-research-report-summary`

Result:
- added explicit bidirectional exact-duplicate provenance to the judicial report-095/report-096 pair;
- retained `american-judicial-process` as canonical and report 096 as archived provenance;
- established that the GAHT “summary” body is substantively the same report, not a useful independent summary artifact;
- retained `gaht` as canonical `review` target and archived the duplicate summary package;
- removed refusal-contaminated metadata from the archived GAHT copy;
- did not validate or rewrite clinical claims.

### PR #9 — Classify third editorial batch

Packages:
- `puritan-moral-psychology`
- `gaht`

Result:
- classified both as `report` / `academic` / `neutral`;
- repaired canonical `gaht` package identity and preserved its legacy alias;
- moved both legacy `complete` → `review`;
- explicitly quarantined GAHT for dedicated primary medical/regulatory review rather than ordinary cleanup.

## 2026-08-19

### PR #8 — Verify brickmaking standards and current claims

Packages:
- `brickmaking-history-materials-processes-and-production-planning`

Result:
- corrected inherited ASTM C109 misuse to current brick-specific ASTM C67/C67M testing framework;
- updated product-specification references;
- grounded manufacturing/emissions claims in EPA/OSHA sources;
- removed generic commercial CAPEX/OPEX precision that could not be defended as universal engineering data;
- replaced it with an estimation workflow;
- corrected 2026–2028 Wienerberger hydrogen-kiln milestones;
- kept lifecycle `review` for remaining historical/materials source-quality work.

### PR #7 — Verify judicial-process institutional sources

Packages:
- `american-judicial-process`

Result:
- replaced brittle generated footnote lattice with direct official institutional sources;
- verified federal structure and 2026 compensation;
- removed stale state salary examples and an unverified homemade 51-jurisdiction count;
- repaired obvious citation-to-claim mismatches;
- advanced `draft` → `review` while preserving final legal review as a blocker.

### PR #6 — Clean second editorial batch

Packages:
- `american-judicial-process`
- `brickmaking-history-materials-processes-and-production-planning`
- `critical-review-of-major-official-financial-crisis-inquiry-reports`
- `liberalism-social-disembedding-and-managed-dependency`

Result:
- repaired judicial H1/prompt leakage/raw diagrams/reference export;
- repaired brickmaking absolute image paths, raw diagram/Gantt blocks, orphan figure markers, and reference export;
- removed second-person/prompt framing, assistant outro, raw timeline source, and reference-export duplication from the financial-crisis review;
- classified social-disembedding report and moved legacy `complete` → `review`;
- kept every package fail-closed pending source/factual review.

### PR #4 — Classify and clean first editorial batch

Packages:
- `fallen-aristocracy`
- `liberalism-as-political-domestication`
- `republicans-as-moderating-opposition-without-a-rival-order`
- `intergenerational-extraction-in-liberal-democracies`
- `testing-the-hypothesis-that-culture-is-parasitic-on-unsatisfied-human-needs`

Result:
- classified the five packages as academic/neutral review material;
- normalized `fallen-aristocracy` heading structure and methodology voice and removed raw diagram/reference-export residue;
- migrated the Republican report's timeline image from legacy `media/` to canonical `assets/media/` and removed body-generation residue;
- repaired culture-report diagram paths, stripped ChatGPT tracking parameters, removed current-document framing, and removed the reference dump;
- moved inherited `complete` states to `review` where applicable;
- left factual/source/rendering blockers explicit.

### PR #2 — Pilot editorial cleanup and corpus triage

Packages:
- `nietzche-math-critique`
- `american-judicial-process`
- `judges-in-the-judicial-process-of-the-united-states`
- `brickmaking-history-materials-processes-and-production-planning`
- `critical-review-of-major-official-financial-crisis-inquiry-reports`

Result:
- proved the form/profile/voice model on deliberately stylized versus academic material;
- reclassified *Dead Symbols and their Worship* as a stylized Nietzschean essay without neutralizing it;
- selected judicial report 095 as canonical and archived exact-body report 096;
- moved defective legacy `complete` reports to `review` rather than treating migration status as evidence of quality;
- established article-local changelogs for newly touched packages and preserved existing history.

## Infrastructure milestones

The following PRs changed editorial infrastructure rather than article packages:

- PR #1 — canonical editorial pipeline and baseline corpus audit;
- PR #3 — pull-request editorial lint workflow;
- PR #5 — HTML local-asset validation;
- PR #10 — duplicate/merge/synthesis policy and read-only duplicate detector;
- PR #18 — technical/instructional editorial profile.

Future batches should append here after their final disposition is known.