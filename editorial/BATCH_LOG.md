# Editorial batch log

This is the repository-level operational history of corpus cleanup. It complements—never replaces—the richer `data/md/<slug>/CHANGELOG.md` inside each changed article package.

## 2026-08-21

### PR #24 — Rewrite male-suicide report from current primary evidence

Packages:
- `male-suicide`

Result:
- replaced the 278 KB inherited conversion artifact with an approximately 5,300-word academic synthesis rather than preserving generated bulk for its own sake;
- corrected the mortality trend using final NCHS evidence: male suicide rose substantially through 2018 but had no statistically significant trend from 2018–2023; the final 2023 male rate was 22.7 per 100,000 with 39,046 male deaths;
- separated the final 2024 all-sex decline from the latest final sex-specific 2023 analysis instead of inferring an unsupported male 2024 rate;
- refreshed age, method, 2021 race/ethnicity, 2021 occupation, 2023 Veteran, and 2024 NSDUH evidence from federal sources;
- distinguished suicide mortality from self-reported ideation and attempts and removed simplistic explanations that treated the male death ratio as a direct measure of suicidal distress;
- removed fictional case studies, static crisis-resource directories, duplicate H1 structure, absolute workstation image paths, ChatGPT/Pandoc citation residue, weak popular-press/Wikipedia citation chains, assignment-stage methodology, and generated prescriptive padding;
- removed the unsupported linear 2030 forecast and assumed intervention trajectory rather than cosmetically updating an invalid forecasting model;
- replaced overconfident treatment claims with endpoint-specific evidence for suicide-focused cognitive therapy, safety planning/follow-up, continuity of care, lethal-means safety, and condition-specific psychiatric treatment;
- explicitly corrected the inherited fixed-percentage lithium claim because contemporary randomized-trial meta-analyses remain statistically inconclusive;
- removed five now-unused legacy chart assets so stale or unverified graphics cannot later enter the build-derived publication tree;
- normalized title, scope, descriptive metadata, report notes, and revision/version to 1.2;
- kept the article fail-closed at `review` / `draft: true` pending one independent high-stakes claim-to-source and rendering pass.

Infrastructure in the same PR: made the generated 115-package corpus census self-refresh on same-repository PR branches, while fork PRs remain read-only and must supply a fresh snapshot themselves.

### PR #23 — Add mechanical corpus census

Result:
- added `scripts/corpus_census.py`, a read-only mechanical census generator that records lifecycle/profile/changelog/duplicate-review presence, asset/media counts, body size, H1 count, local-link counts, obvious conversion/path/diagram defects, and conservative literal risk hints without making editorial decisions;
- committed the first complete `editorial/CENSUS.yaml` snapshot covering all 115 canonical packages;
- added CI generation and freshness validation so the census has durable repository presence rather than living only in chat or an ephemeral audit;
- established the baseline counts of 58 legacy `complete` packages, 96 unresolved profiles, 92 missing changelogs, and 106 unresolved duplicate reviews, plus mechanical defect/risk hints for triage.

## 2026-08-20

### PR #20 — Rewrite Savonius guide under technical profile

Packages:
- `savonius-wind-turbines-comprehensive-design-diy-guide`

Result:
- classified the artifact as `guide` / `technical` / `instructional` and moved legacy `complete` to fail-closed `review`;
- replaced the conversion-heavy DIY recipe with an engineering design/prototype guide whose worked calculations are explicitly illustrative rather than universal specifications;
- corrected the tip-speed/RPM relation, the inconsistent power/electrical-output tables, the erroneous 5 m/s daily-energy claim, and the undersized 6 m/s design example;
- replaced cubed-annual-mean-wind reasoning with a power-curve/wind-frequency approach consistent with current DOE small-wind guidance;
- corrected Betz-limit framing and removed universal TSR/geometry claims that the underlying Savonius literature does not justify across configurations;
- repaired the absolute workstation image path to canonical `assets/media/rId31.png`;
- removed orphaned ChatGPT/export markers, raw Mermaid/Gantt source, and the redundant conversion-generated reference export;
- replaced generic shaft/bearing/tower dimensions and a universal $450–800 BOM with design-dependent requirements and a quotation-based engineering worksheet;
- strengthened safety boundaries using DOE, IEC 61400-2, and OSHA 29 CFR 1910.252, including rooftop turbulence/vibration, used-container hot work, positive overspeed protection, loss-of-load behavior, electrical interconnection, and structural/foundation design;
- added a rich article-local changelog.

Remaining blockers: provenance/publication rights for the retained conceptual image, duplicate-candidate review, and final rendered-publication inspection. The article remains `review` rather than being promoted on the strength of prose cleanup alone.

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
- PR #18 — technical/instructional editorial profile;
- PR #19 — persistent editorial queue, batch log, changelog coverage audit, queue reporter, and same-PR changelog enforcement;
- PR #23 — full mechanical corpus census and generated-snapshot CI.

Future batches should append here after their final disposition is known.
