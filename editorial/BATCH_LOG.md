# Editorial batch log

This is the repository-level operational history of corpus cleanup. It complements—never replaces—the richer `data/md/<slug>/CHANGELOG.md` inside each changed article package.

## 2026-08-21

### PR #40 — Finalize global population dynamics report

Packages:
- `global-population-dynamics-peaks-in-population-level-and-growth-rates`

Result:
- corrected the conversion-contaminated title and reclassified the artifact from inherited public-health metadata to an academic/neutral demography and population-studies report;
- rewrote the analysis around the distinction between population level, percentage growth rate, and absolute annual change, retaining the observed global growth-rate peak near 2.3 per cent in 1963 while treating the projected population-level maximum as a separate future event;
- confirmed World Population Prospects 2024 remains the current global UN revision through August 2026 and documented the 19 January 2026 interim update, which corrected Togo estimates and medium projections only, left global/regional aggregates unchanged, and postponed the next full WPP revision to 11 July 2027;
- replaced the inherited single-year pseudo-precision of a 10.289-billion 2084 peak with the UN's published central result of about 10.3 billion in the mid-2080s and an approximately 80 per cent probability that global population peaks within the twenty-first century;
- replaced an unreproducible exact major-region peak table with the UN's directly published country/area peak-timing groups: 63 peaked by 2024, 48 are projected to peak during 2025–2054, and 126 are projected to continue growing through 2054;
- added stock-flow accounting, population momentum, demographic-transition framing, migration effects, and explicit deterministic/probabilistic projection interpretation;
- removed speculative historical mechanism padding that was not sourced to the same standard as the demographic core, plus raw Mermaid, empty visualization placeholders, escaped numbered-link citations, and the duplicated conversion reference export;
- completed duplicate review as independent/keep-separate, advanced revision/version to 1.0.1 and legacy lifecycle `complete` → `ready` / `draft: false`, and intentionally exhausted the explicit ordinary `next_batch` queue rather than inventing a new priority from the corpus census.

### PR #39 — Finalize Borderer meme hypothesis pair

Packages:
- `meme-culture-and-borderer-right-style-a-research-report`
- `distinguishing-borderer-right-coded-vs-left-awkward-authentic-internet-memes-a-research-framewo`

Result:
- replaced the broad report's inherited claim that meme culture naturally maps onto a right-coded Borderer style with a falsifiable style-vector hypothesis separating political ideology from low deference, antagonistic humor, taboo-breaking, anti-elitism, irony, status inversion, performative aggression, and in-group signaling;
- retained bounded far-right evidence on aggressive humor, anti-elitism, hate, conspiracy narratives, and humorous ideological packaging while adding direct counterevidence from r/DankLeft and Spanish political-meme research showing that taboo-breaking, threatening out-groups, ridicule, and antagonism are not right-exclusive;
- added cross-national far-right evidence showing that memes are unevenly central across organizations and countries, plus commemorative far-right meme evidence that rejects a universal crude/anonymous/right-wing meme aesthetic;
- narrowed inherited persuasion, radicalization, and trust claims using field-experimental and panel evidence rather than treating memes as intrinsically powerful ideological conversion devices;
- explicitly treated “borderer” as a proposed analytic style label rather than an established scholarly category or proof of historical Borderer ancestry;
- replaced the companion framework's circular right-aggression/left-empathy classification with independent ideological labels and neutral coding dimensions for targets, hostility, humor, taboo, irony, anti-elitism, status inversion, performative aggression, in-group signaling, self-disclosure, care/solidarity, and aesthetic register;
- redesigned the framework around balanced ideology/platform/topic/time sampling, apolitical negative controls, engagement-independent sampling, template-family leakage protection, reduced-metadata coding where feasible, coder training, per-variable reliability, latent-construct testing, multivariable controls, and held-out platform/community/time validation;
- added preregistered hypotheses and explicit retain/split/reject rules so the proposed borderer construct can fail rather than having its conclusion embedded in the codebook;
- removed conversion citations, raw diagrams/timelines, predetermined expected results, hand-picked illustrative classifications, and four unprovenanced converted images across the pair;
- retained the two packages as a legitimate cultural-analysis/methodology fork, advanced both to revision/version 1.0.2 and lifecycle `review` → `ready` / `draft: false`, and advanced the ordinary queue to the global-population dynamics report.

### PR #38 — Record intergenerational and Puritan publication

Packages:
- `intergenerational-extraction-in-liberal-democracies`
- `puritan-moral-psychology`

Result:
- verified the build-derived Marginalia pages at `/research/intergenerational-extraction-in-liberal-democracies/` and `/research/puritan-moral-psychology/` and confirmed that both render the source-audited canonical rewrites rather than legacy copies;
- confirmed the intergenerational page carries the cohort-incidence framing that distinguishes genuine uncompensated lifetime burden shifting from ordinary age redistribution, pension insurance, life-cycle wealth accumulation, and public borrowing;
- confirmed the Puritan page carries the evidence-graded genealogy distinguishing direct transmission, documented reception/reuse, morphological continuity, and analogy, including the transatlantic and alternative-lineage qualifications from the final audit;
- advanced both canonical lifecycles `ready` → `published` while retaining `draft: false`;
- added package-local lifecycle-only changelog entries and moved both queue items to `done-for-now` / P3 maintenance;
- left article prose, sources, assets, and revision/version 1.0.2 unchanged for both reports;
- left `proudhon-mutualism-report` at `ready` because its build-derived page had not yet been verified in the deployed `gh-pages` tree.

### PR #37 — Finalize Proudhon mutualism report

Packages:
- `proudhon-mutualism-report`

Result:
- replaced the inherited conversion-heavy report with a source-audited reconstruction of Proudhon’s evolving mutualism rather than preserving a static “markets without capitalism” blueprint;
- corrected the inherited property-versus-possession simplification by incorporating Proudhon’s mature antinomy in which property could function both as exploitation and as a dispersed counterweight to centralized state power;
- separated Proudhon’s own reciprocity and value arguments from Josiah Warren’s later cost principle and from the Greene/Tucker American individualist-mutualist synthesis;
- bounded the 1849 Banque du Peuple evidence to what the historical record supports: more than 13,000 individual adhesions, roughly fifty workers’ associations, nearly thirty agencies, and liquidation before long-run banking viability could be observed;
- treated Bastiat’s interest critique and Marx’s critique of Proudhonian political economy as rival causal frameworks rather than neutral verdicts;
- distinguished French First International reception, American individualist mutualism, and the broader cooperative movement instead of collapsing them into one Proudhonian lineage;
- incorporated specialist scholarship on Proudhon’s anti-feminism and patriarchal family authority as a substantive internal limitation of his anti-domination politics;
- removed Wikipedia/Fandom/Scribd/quote-site citation dependence, escaped numbered-link/reference-export residue, and the workstation-absolute image reference, replacing them with named primary texts and specialist scholarship;
- deleted obsolete converted asset `assets/media/rId50.png`, retained `3mutualism` as archived exact-duplicate provenance, advanced revision/version to 1.0.2 and lifecycle `review` → `ready` / `draft: false`, and advanced the ordinary queue to the P2 meme/corpus and population-demography targets.

### PR #36 — Finalize Puritan genealogy report

Packages:
- `puritan-moral-psychology`

Result:
- replaced the inherited linear Puritan-to-modern-progressivism thesis with an evidence-graded genealogy distinguishing direct transmission, documented reception/reuse, morphological continuity, and analogy;
- retained New England covenantal community, moral discipline, jeremiadic correction, and exemplary mission as historically important Puritan forms without treating them as a fixed transhistorical psychology;
- identified revivalism and the Social Gospel as the strongest transformed Protestant transmission path into later reform, while preserving the theological and institutional changes between those stages;
- incorporated current Puritan historiography, especially John Coffey's warning that broad theories of Puritan modernity remain vigorously disputed and are better tested through documented reception and use;
- added Daniel Rodgers's transatlantic Progressive reform networks and the direct Toynbee Hall influence on Hull House as major counterevidence to a self-contained New England genealogy;
- added African American prophetic traditions and Black reuse of Pilgrim-Puritan origins as independent and interacting reform lineages rather than derivatives of white Puritanism;
- recast Winthrop's `city upon a hill` legacy as a documented case of twentieth-century recovery and canonization using Abram Van Engen rather than assuming uninterrupted national memory from 1630;
- removed the inherited DEI/bias-response/cancel-culture endpoint because the article supplied analogy rather than traceable historical descent;
- removed escaped numbered-link citations, conversion tables, the duplicated reference export, first-person process narration, and the obsolete converted Mermaid PNG;
- completed duplicate review as independent/keep-separate, advanced revision/version to 1.0.2 and lifecycle `review` → `ready` / `draft: false`, and advanced the persistent queue to Proudhon mutualism.

### PR #35 — Record liberalism report publication

Packages:
- `liberalism-social-disembedding-and-managed-dependency`

Result:
- verified the build-derived Marginalia page at `/research/liberalism-social-disembedding-and-managed-dependency/` and confirmed it carries the source-audited title, description, dependency-shift executive summary, and canonical rewritten body;
- advanced canonical lifecycle `ready` → `published` while retaining `draft: false`;
- added a package-local lifecycle-only changelog entry and moved the queue item to `done-for-now` / P3 maintenance;
- left article prose, sources, assets, and revision/version 1.1.0 unchanged.

### PR #34 — Finalize intergenerational-extraction report

Packages:
- `intergenerational-extraction-in-liberal-democracies`

Result:
- replaced the inherited generational-war framing with a stricter lifetime cohort-incidence test: ordinary age redistribution, life-cycle wealth accumulation, pension insurance, and gross public debt no longer count as extraction without evidence that politically advantaged present cohorts improve their lifetime net position by shifting uncompensated costs to younger or future cohorts;
- replaced the provisional U.S. 2024 fertility rate with the final NCHS value of 1.5995, refreshed Japan and Germany fertility evidence through 2025 where available, and retained Israel as the high-fertility counterexample;
- refreshed 2026 IMF debt context, OECD `Pensions at a Glance 2025` replacement-rate modelling, the 2026 Social Security Trustees projections, and CBO fiscal evidence;
- removed the inherited inference that debt is automatically a one-for-one transfer to future taxpayers, distinguishing current-consumption borrowing from productive investment and grounding the forward-burden channel in future investment, output, interest-cost, and fiscal-space effects;
- reframed Federal Reserve and Bundesbank age-wealth profiles as life-cycle evidence rather than proof of cohort exploitation;
- added Tepe and Vanhuysse as comparative counterevidence to a simple gerontocracy model, distinguishing demographic increases in aggregate pension spending from benefit generosity per retiree;
- made housing the strongest directly observed political mechanism using evidence on homeowner turnout, local meeting participation, opposition to new construction, and representative voting;
- updated the four-country comparison around demographic pressure, fiscal exposure, pension adjustment, and electoral-age structure rather than a synthetic extraction ranking;
- removed escaped numbered-link citations, the duplicated conversion reference export, tracked source URLs, and three obsolete converted diagram assets;
- completed duplicate review as independent/keep-separate, advanced revision/version to 1.0.2 and lifecycle `review` → `ready` with `draft: false`, and advanced the persistent queue to Puritan moral psychology followed by Proudhon mutualism.

### PR #33 — Record culture-parasitism publication

Packages:
- `testing-the-hypothesis-that-culture-is-parasitic-on-unsatisfied-human-needs`

Result:
- verified the build-derived Marginalia page at `/research/testing-the-hypothesis-that-culture-is-parasitic-on-unsatisfied-human-needs/` and confirmed it carries the source-audited title, description, and rewritten canonical body;
- advanced canonical lifecycle `ready` → `published` while retaining `draft: false`;
- added a package-local lifecycle-only changelog entry and moved the queue item to `done-for-now` / P3 maintenance;
- left article prose, sources, assets, and revision/version 1.0.2 unchanged.

### PR #32 — Merge liberalism disembedding/domestication cluster

Packages:
- `liberalism-social-disembedding-and-managed-dependency`
- `liberalism-as-political-domestication`

Result:
- adjudicated the two reports as a substantive merge cluster rather than preserving two heavily overlapping canonical articles;
- retained `liberalism-social-disembedding-and-managed-dependency` as canonical and rewrote its inherited atomization thesis into a dependency-shift framework distinguishing inherited personal dependence, market dependence, welfare/administrative mediation, credential dependence, and platform/algorithmic mediation;
- treated welfare decommodification and defamilialization as genuine counterexamples to any simple claim that modern liberal orders merely increase dependency, while preserving administrative mediation as a distinct contestability question;
- incorporated the non-canonical report's distinctive Weberian legal-rational administration, Scott-style legibility, and Foucauldian governmentality material as a subordinate mechanism inside the broader synthesis;
- grounded current algorithmic-management and social-connection claims in 2025 OECD evidence and retained U.S. generalized-trust decline only with explicit causal caution rather than ideological attribution;
- replaced five obsolete converted chart/PNG dependencies with native Markdown structures and deleted the now-unused `rId42`, `rId47`, `rId51`, `rId55`, and `rId60` assets;
- completed duplicate review as `merge-cluster / merge-into-canonical`, recorded `liberalism-as-political-domestication` in the canonical package's `merged_from`, and recorded the reciprocal `merged_into` provenance on the archived source package;
- preserved the archived source's substantive prose for provenance, repaired four broken repo-root-style image targets exposed by lint, and advanced it `review` → `archived` / `draft: true` at revision 1.0.2;
- added rich changelog entries to both packages, advanced the canonical synthesis `review` → `ready` / `draft: false` at revision 1.1.0, and moved the editorial queue to the next ordinary review cluster.

### PR #31 — Finalize culture-parasitism hypothesis for publication

Packages:
- `testing-the-hypothesis-that-culture-is-parasitic-on-unsatisfied-human-needs`

Result:
- substantially rewrote the report around four distinct claims—compensatory use, symbolic substitution, affective reproduction, and system-level reproductive dependence—instead of letting evidence for one level stand in for another;
- grounded bounded compensatory mechanisms in Mandel et al. on self-discrepancy and compensatory consumption, Derrick et al. on favored-media social surrogacy, and Kay et al. on compensatory control;
- retained online outrage research as evidence that social feedback and sharing incentives can reinforce high-arousal cultural expression, while removing the unsupported inference that those studies prove platforms create or require unmet needs;
- used current IAB/PwC advertising-market figures and WHO loneliness prevalence only as scale/background context rather than causal proof of cultural dependence;
- added self-determination theory and arts/well-being findings as explicit counterexamples to a universal theory in which culture disappears as needs are satisfied;
- removed the legacy `Related Marginalia Essays` section and old `/posts/` URLs from the evidentiary architecture, recording related corpus artifacts only through canonical relationship metadata;
- replaced two converted Mermaid PNG dependencies with native Markdown structures and deleted both unprovenanced, now-unused assets;
- completed duplicate review as independent/keep-separate inside a broader related culture-theory cluster;
- updated scope/method/notes, advanced revision/version to 1.0.2, and advanced lifecycle `review` → `ready` with `draft: false` and no known source, conversion, asset, or duplicate blocker remaining.

Transport provenance: PR #30 contained the same branch/result but was closed unmerged after the connector refused the draft→ready transition. The unchanged branch was reopened as non-draft PR #31 and merged as `ebb24d99ffba75df2a702a0281fa0993bc90bdf9`; PR #30 itself did not merge.

### PR #29 — Record build-derived publication of ready reports

Packages:
- `brickmaking-history-materials-processes-and-production-planning`
- `critical-review-of-major-official-financial-crisis-inquiry-reports`
- `fallen-aristocracy`
- `republicans-as-moderating-opposition-without-a-rival-order`

Result:
- verified all four build-derived pages in the deployed Marginalia `gh-pages` tree under their canonical `/research/<slug>/` paths;
- confirmed the generated pages carry the final source-audited titles/descriptions and render the approved canonical bodies rather than legacy `content/posts` copies;
- advanced canonical lifecycle `ready` → `published` for all four packages while retaining `draft: false`;
- added package-local changelog entries that identify the verified deployed path and explicitly state that this publication closure changed no article prose, sourcing, assets, or revision/version;
- moved the four operational queue entries from `ready-for-publication` to `done-for-now` / P3 maintenance;
- left the next substantive batch unchanged: culture-as-parasitic hypothesis followed by liberalism/social-disembedding.

### PR #28 — Finalize fallen-aristocracy and Republican-order reports

Packages:
- `fallen-aristocracy`
- `republicans-as-moderating-opposition-without-a-rival-order`

Result:
- rewrote `fallen-aristocracy` around a disciplined category of hereditary or estate-based elites that lose formal privilege while retaining convertible prestige, education, wealth, networks, or organizational capacity;
- separated strong cases from category errors: French noble émigrés, former samurai as an explicit functional analogue, and post-First World War aristocratic intellectuals now carry the comparison, while Russian White émigrés, Byzantine scholars, and Latin American creoles are retained only as boundary/negative cases;
- replaced deterministic status-loss psychology with a conditional model of status threat, residual elite capacity, restoration opportunity, resource convertibility, and successor-state incorporation, supported by Oxford, Cambridge, Library of Congress, Larousse, and peer-reviewed status-threat evidence;
- substantially revised the Republican moderating-opposition thesis rather than merely updating links: TANF is treated as durable institutional replacement, the ACA as retrenchment without comprehensive replacement, tax policy as affirmative architecture, USMCA as replacement within an inherited trade paradigm, and Public Law 119-21 immigration enforcement as affirmative capacity building;
- reclassified Gramm-Leach-Bliley and the First Step Act as bipartisan directional changes rather than evidence for a simple one-party ratchet;
- replaced the Republican report's weak legacy source mix and conversion-heavy tables with direct CBO, CRS, USTR, Federal Reserve History, Senate, and historical-institutionalist sources;
- removed the Republican package's obsolete rendered timeline asset after the rewritten body no longer depended on it;
- completed duplicate review for both packages as independent/keep-separate after repository title/body searches found no competing canonical treatment;
- added rich package-local changelog entries, updated descriptive/scope metadata, bumped both reports to revision/version 1.0.3, and advanced both `review` → `ready` with `draft: false`.

### PR #27 — Finalize financial-crisis inquiry review

Packages:
- `critical-review-of-major-official-financial-crisis-inquiry-reports`

Result:
- substantially rewrote the inherited report around claim-to-source comparison instead of preserving a rhetorically strong but technically loose anti-state causal narrative;
- retained the legitimate critical thesis that official institutions are part of the financial order they later investigate, while replacing claims of institutional intent with a narrower testable argument about administrative and causal framing;
- corrected the common but inaccurate shorthand that the SEC's 2004 CSE amendments simply removed a universal 12:1 leverage cap; the final rule did permit approved internal-model calculations for some market/credit-risk deductions, while imposing minimum capital, reporting, risk-management, and consolidated-supervision conditions;
- retained and strengthened the separate accountability case against the CSE program using the SEC Inspector General's findings on leverage, liquidity, concentration, stress testing, model oversight, and supervisory weakness, plus the SEC's subsequent termination of the voluntary program;
- separated the narrow CRA/GSE affordable-housing-goals hypothesis from broader GSE guarantee, funding, portfolio, and mortgage-market questions; Federal Reserve threshold/quasi-experimental studies provide little support for the claim that CRA or the affordable-housing goals principally drove the subprime boom;
- retained AIG counterparty-at-par scrutiny but qualified the inference using GAO evidence that multiple Maiden Lane III structures were considered and that documented discretion does not by itself prove a safe or legally feasible haircut alternative existed;
- recast shadow banking as private maturity transformation embedded in a public legal and emergency-support order rather than either a purely unregulated market or a disguised state system;
- explicitly recognized that the FCIC majority and U.K. Treasury Committee directly blamed regulatory failures, which limits any universal bureaucratic-self-exoneration theory;
- replaced the escaped numbered conversion-citation lattice with named direct official, watchdog, and research sources;
- extended metadata scope through 2013 because the retained Parliamentary Commission on Banking Standards report postdates the old 2007–2011 boundary;
- completed duplicate review as independent/keep-separate and advanced lifecycle `review` → `ready` with `draft: false` at revision 1.0.3.

### PR #26 — Finalize brickmaking report for publication

Packages:
- `brickmaking-history-materials-processes-and-production-planning`

Result:
- completed the remaining historical/materials source-quality review and treated the pass as a publication gate rather than another indefinite review cycle;
- grounded the Hoffmann continuous-kiln history in Historic England evidence and added peer-reviewed ceramics/materials support for clay mineralogy, firing behavior, porosity, and defect mechanisms;
- corrected the inherited EPA AP-42 soft-mud moisture range from 20–30% to 15–28%;
- rechecked the current EPA AP-42, ASTM C67/C67M, EPA NESHAP, OSHA silica, and Wienerberger hydrogen-project links used by the prior standards/regulatory audit;
- removed two decorative converted brickfield images because the package recorded no provenance or publication rights and neither image was analytically necessary;
- completed duplicate review as independent/keep-separate after the full 115-package census showed no competing brickmaking artifact;
- advanced revision/version to 1.0.4 and lifecycle `review` → `ready` with `draft: false`;
- left no known source, conversion, asset, or duplicate blocker before build-derived publication.

### PR #25 — Rewrite GAHT report from current primary evidence

Packages:
- `gaht`

Result:
- replaced the inherited bullet-heavy overview with a current evidence review of feminizing GAHT;
- separated established adult physical effects from uncertain long-term outcomes and avoided presenting observational associations as settled causal effects;
- treated puberty suppression and adolescent hormone treatment as distinct evidence questions rather than extrapolating adult evidence into minors;
- removed generic dosing instructions and prescribing-style monitoring language from the public-facing research article;
- corrected overstatements about inevitable infertility, universal bone loss, lipid normalization, and adolescent pelvic or brain development;
- replaced the inherited blanket benefits-outweigh-risks conclusion with endpoint-specific uncertainty and evidence-quality language;
- distinguished empirical treatment evidence from professional guideline recommendations and from jurisdictional policy or court decisions;
- explicitly separated current Endocrine Society/WPATH recommendations from NHS England commissioning policy and the U.S. Supreme Court's legal ruling in `United States v. Skrmetti`;
- removed legacy cover metadata pointing to a nonexistent root-level asset;
- normalized title, scope, period, evidence-method metadata, and revision to `r4`;
- kept the article fail-closed at `review` / `draft: true` pending one independent high-stakes claim-to-source and rendered-publication pass.

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
