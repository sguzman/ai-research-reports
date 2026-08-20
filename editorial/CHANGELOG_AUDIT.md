# Article changelog coverage audit

Baseline: `95875fed7b2687c3ef5e19d21e17529302133298`

Audit date: 2026-08-20

The baseline-to-current Git comparison shows **21 article packages changed by the new editorial pipeline**, including the Savonius technical-guide batch in PR #20. Every one of those packages has an article-local `CHANGELOG.md` addition or modification in the corresponding editorial history.

This establishes coverage; it does not mean every article is finished. `review` and `draft` packages retain their documented blockers.

| Package | Editorial PR(s) that changed it | Changelog coverage | Current editorial meaning |
| --- | --- | --- | --- |
| `3mutualism` | #13 | covered | archived duplicate/repackaging of canonical Proudhon report |
| `american-judicial-process` | #2, #6, #7, #11, #15, #16 | covered across successive stages | canonical report cleaned, source-audited, finalized, published |
| `brickmaking-history-materials-processes-and-production-planning` | #2, #6, #8 | covered across triage, mechanical cleanup, current-claims audit | review; remaining historical/materials source-quality work |
| `critical-review-of-major-official-financial-crisis-inquiry-reports` | #2, #6 | covered | review; prompt/voice mechanics repaired, source audit remains |
| `distinguishing-borderer-right-coded-vs-left-awkward-authentic-internet-memes-a-research-framewo` | #14 | covered | related methodological fork retained separately in review |
| `fallen-aristocracy` | #4 | covered | review; structural cleanup complete, source/factual audit remains |
| `gaht-research-report-summary` | #11 | covered | archived exact duplicate/provenance artifact |
| `gaht` | #9, #11 | covered across classification and duplicate resolution | canonical review target; high-stakes medical audit remains |
| `intergenerational-extraction-in-liberal-democracies` | #4 | covered | review; source-quality/current-link work remains |
| `judges-in-the-judicial-process-of-the-united-states` | #2, #11 | covered across archival and explicit duplicate provenance | archived exact duplicate of report 095 |
| `liberalism-as-political-domestication` | #4 | covered | review; source-quality/current-link work remains |
| `liberalism-social-disembedding-and-managed-dependency` | #6 | covered | review; source-quality/asset/current-link work remains |
| `male-suicide-research-outline` | #12 | covered | archived duplicate whose “outline” label did not match its finished body |
| `male-suicide` | #12 | covered | canonical review target; mechanical and high-stakes source audit remains |
| `meme-culture-and-borderer-right-style-a-research-report` | #14 | covered | related cultural-analysis fork retained separately in review |
| `nietzche-math-critique` | #2, #17 | covered across reclassification and stylized cleanup | published stylized essay; Marginalia management migration still operationally pending |
| `proudhon-mutualism-report` | #13 | covered | canonical review target; citation/source cleanup remains |
| `puritan-moral-psychology` | #9 | covered | review; genealogy/source-quality audit remains |
| `republicans-as-moderating-opposition-without-a-rival-order` | #4 | covered | review; converted-table rendering and source audit remain |
| `savonius-wind-turbines-comprehensive-design-diy-guide` | #20 | covered | technical/instructional review target; numerical, conversion, and major safety defects repaired; image provenance, duplicate review, and render inspection remain |
| `testing-the-hypothesis-that-culture-is-parasitic-on-unsatisfied-human-needs` | #4 | covered | review; source/factual/overlap review remains |

## Required future behavior

Coverage is enforced as a workflow invariant: if an editorial PR changes an article package, its article-local `CHANGELOG.md` must change in the same PR.

Changelog entries should be rich enough to reconstruct the editorial action without relying on the PR description. They should identify material repairs, lifecycle/profile decisions, source/factual corrections, relationship decisions, and significant remaining blockers.

If a later editor discovers that an older entry is too vague, append a new audit/backfill entry; do not silently rewrite historical entries merely to make the history look cleaner.
