# Corpus audit: inherited baseline

Snapshot audited: `main` at `95875fed7b2687c3ef5e19d21e17529302133298` (2026-07-01).

This is a **read-only baseline** of the inherited canonical corpus. No established article body, metadata file, asset, or changelog was modified to produce this inventory.

The purpose is to measure migration debt before enforcing the new editorial standard. Findings are not automatic rewrite instructions: profile-sensitive prose requires human/editorial judgment.

## Structural census

The complete recursive Git tree at the snapshot contains:

- **115 canonical article packages** under `data/md/<slug>/` with both `article.yaml` and `main.md`.
- **12 article packages with `CHANGELOG.md`** (10.4% of the 115-package corpus).
- **24 packages with a canonical `assets/` directory** (20.9%).
- **9 packages with legacy top-level `media/` trees outside `assets/`** (7.8%).
- **9 packages with root-level cover/image files**; one of these (`3mutualism`) also has `assets/`.
- At least one pair of canonical packages has an **exactly identical `main.md` blob**: `american-judicial-process` and `judges-in-the-judicial-process-of-the-united-states` both point to blob `33ceb05911f42b2fb04f76e7f29352e6a6ef8237`.

The 12 packages with an existing changelog are:

1. `critical-review-of-major-official-financial-crisis-inquiry-reports`
2. `emptiness-of-deleuze`
3. `fallen-aristocracy`
4. `gaht-research-report-summary`
5. `gaht`
6. `global-population-dynamics-peaks-in-population-level-and-growth-rates`
7. `intergenerational-extraction-in-liberal-democracies`
8. `liberalism-as-political-domestication`
9. `liberalism-social-disembedding-and-managed-dependency`
10. `puritan-moral-psychology`
11. `republicans-as-moderating-opposition-without-a-rival-order`
12. `testing-the-hypothesis-that-culture-is-parasitic-on-unsatisfied-human-needs`

The 24 packages already using `assets/` are:

`3mutualism`, `brickmaking-history-materials-processes-and-production-planning`, `civilizing-injustice-colonial-conquest-and-moral-pretexts`, `complex-plane-culture`, `darrieus-vawt-design-construction-1-10-kw`, `distinguishing-borderer-right-coded-vs-left-awkward-authentic-internet-memes-a-research-framewo`, `electric-motor-design-principles-types-and-practices`, `formalizing-the-elite-xenophilia-hypothesis`, `heaviside`, `highway-engineering`, `in-house-vertical-farms`, `liberal-gothic-an-analytical-report`, `male-suicide-research-outline`, `male-suicide`, `mass-and-indiscriminate-immigration-as-indirect-corporate-welfare`, `maxwells-equations-a-human-centered-historical-and-scientific-analysis`, `meme-culture-and-borderer-right-style-a-research-report`, `nations-right-wing-critique`, `piketty-liberal-pmc-critique`, `proudhon-mutualism-report`, `savonius-wind-turbines-comprehensive-design-diy-guide`, `symbolic-post-masculinity`, `testing-the-hypothesis-that-culture-is-parasitic-on-unsatisfied-human-needs`, and `united-states-of-empire`.

The 9 packages with legacy top-level `media/` trees are:

`american-conservatism`, `intergenerational-extraction-in-liberal-democracies`, `liberalism-as-political-domestication`, `liberalism-equality-and-the-leftward-drift-thesis`, `liberalism-social-disembedding-and-managed-dependency`, `modern-progressive-marxism`, `puritan-moral-psychology`, `republicans-as-moderating-opposition-without-a-rival-order`, and `the-female-shadow`.

This mixed layout is evidence that the new `assets/` rule must be treated as a **normalization target**, not as proof that legacy articles are currently broken merely because their files predate the rule.

## Recovered changelog convention

Existing changelogs consistently use a per-article Markdown table:

```markdown
# Changelog

| Timestamp | Summary |
| --- | --- |
| 2026-07-01 06:14:34 CST | Concise description of the editorial change. |
```

Existing entries already record removal of prompt-conditioned framing, conversion from `the user` language to impersonal prose, and neutralization of metadata summaries. The new workflow should preserve and extend this convention rather than invent a repository-wide competing ledger.

## Confirmed editorial defects and classification failures

### 1. Stylized work falsely represented as a report

`nietzche-math-critique/article.yaml` currently declares both top-level `type: report` and `report.is_report: true`, with `report.kind: research report`. Its body is deliberately rhetorical and Nietzschean: it describes itself as an accusation, uses aphoristic repetition and intentionally severe polemical language, and plainly is not trying to sound like a neutral academic report.

This is the clearest reason to separate:

```yaml
type: essay
editorial_profile: stylized
voice: nietzschean
```

The audit does **not** change that article yet. It records the current classification as migration debt for editorial review.

### 2. Prompt leakage and title/citation contamination in a nominal report

`american-judicial-process/main.md` begins with a citation glued directly to its H1 title and later says, literally, `Because the user did not specify a state`. It also contains an indented `flowchart LR` block rather than a publication-safe rendered diagram. These are direct examples of the universal and academic-profile defects the new rules are intended to catch.

The identical-body package `judges-in-the-judicial-process-of-the-united-states` inherits the same body defects because both package paths point to the same `main.md` blob at this snapshot.

### 3. Canonical duplicate/package drift

The exact duplicate body above is not automatically proof that one package should be deleted: aliases, migration history, or metadata differences may explain why both exist. It is, however, proof that **package identity and duplicate handling require explicit review** rather than title-based or filename-based assumptions.

### 4. Metadata model overstates report-ness

The inherited metadata schema and generated records are strongly report-centric (`report.*`, report numbering, `is_report`, series fields). This made it easy for non-report material to be described as a report merely because the tooling expected that shape.

The new standard therefore adds independent `editorial_profile` and `voice` fields and explicitly permits `essay`, `fiction`, `dialogue`, and other non-report forms without fabricating report metadata.

## What this audit does not claim

This baseline is exact for repository-tree structure at the pinned snapshot, but it is **not yet a full sentence-by-sentence semantic audit of all 115 bodies**. GitHub-side text search is not reliable enough to use as a complete corpus parser, and no local checkout was available in the current execution environment.

Accordingly, counts of first-person narration, second-person narration, prompt leakage, citation mismatches, spelling errors, and broken remote URLs are intentionally **not fabricated** here. Those counts should be generated by the read-only linter/audit tool against a local checkout or by explicit per-package retrieval before any bulk rewrite begins.

The structural census is still sufficient to establish the first migration priorities: classification, changelog coverage, duplicate review, asset normalization, and profile-aware linting.

## Recommended cleanup sequence

1. Merge/finalize the editorial taxonomy and profile rules before article rewrites.
2. Make linting profile-aware so a Nietzschean essay cannot be “fixed” into neutral prose.
3. Run a complete local read-only linter pass and save the machine-readable findings.
4. Select a small pilot set representing different inherited failure modes:
   - `american-judicial-process` — academic cleanup, prompt leakage, H1 citation, diagram, duplicate identity;
   - `nietzche-math-critique` — stylized reclassification without prose neutralization;
   - one asset-heavy technical report — asset-path/rendering validation;
   - one article with an existing changelog — verify revision-history procedure.
5. Tune rules from the pilot.
6. Only then clean the corpus in batches, recording each established article's changes in its own changelog.

No automatic bulk rewrite should occur before step 5.
