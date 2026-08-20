# Duplicate and merge policy

This repository treats duplication as an editorial relationship problem, not merely a file-cleanup problem. AI-assisted research can easily produce multiple reports that repeat the same thesis, evidence, structure, or prose. Those artifacts must not automatically coexist as independent finished works.

The default objective is to preserve useful material while reducing false multiplicity. Exact and near-duplicate reports should be reviewed for canonicalization, derivation, or synthesis before they can be considered publication-ready.

## Core rule

Every newly ingested or substantively revised article should be checked against the canonical corpus for meaningful overlap before substantial editorial effort is spent on it.

A duplicate candidate is not automatically deleted. The editor determines the relationship, disposition, and provenance first.

## Relationship classes

### Exact duplicate

The article body is identical or differs only by formatting, metadata, trivial punctuation, or other non-substantive changes.

Default disposition:

- designate one canonical package;
- archive the duplicate package rather than deleting it;
- record the canonical target in relationship metadata and both relevant changelogs;
- do not publish the archived duplicate independently.

### Near duplicate

The documents substantially share thesis, structure, evidence, examples, citations, or prose but contain some unique material.

Default disposition:

- compare both for source quality, structure, unique claims, citations, assets, and editorial cleanliness;
- choose an existing canonical target when one version is clearly stronger; or
- create a synthesis target when neither version should dominate;
- preserve useful unique material before archiving or superseding a source package.

### Derived summary or brief

A shorter artifact intentionally compresses or adapts a longer canonical work.

Default disposition:

- keep it only when it has a distinct editorial purpose;
- classify its actual form, such as `research-brief` or `note`, rather than pretending it is another full report;
- record `derived_from` and, when useful, the reverse `derivatives` relationship;
- permit independent publication only when the derivative is editorially complete in its own right.

### Fork or alternate treatment

Two artifacts share a topic or source base but differ materially in argument, audience, form, method, or voice.

Examples include an academic report and a stylized philosophical essay on the same subject, or a technical reference and a policy argument built from overlapping evidence.

Default disposition:

- keep both when the difference in purpose is genuine;
- record a related-work relationship when useful;
- do not force unlike forms into one synthesized voice merely because their subject overlaps.

### Merge cluster

Several overlapping documents contain useful but redundant material and none deserves to survive unchanged as the sole canonical version.

Default disposition:

- create or designate a synthesis target;
- treat all source documents as a material pool with provenance;
- build a unified outline from the subject matter, not from source-file boundaries;
- merge repeated claims, choose the strongest available sourcing, reconcile contradictions, and retain genuinely unique material;
- archive contributing packages after the synthesis is accepted, recording `merged_into` on sources and `merged_from` on the target.

## What not to do during a merge

Do **not** concatenate reports and call the result a synthesis.

Do **not** mechanically divide the final report into disjoint sections based on which source document supplied them. Source boundaries are provenance information, not necessarily the right intellectual structure.

Do **not** silently discard a weaker duplicate before checking whether it contains unique evidence, examples, citations, tables, diagrams, or formulations worth preserving.

Do **not** allow an automatically detected similarity score to decide deletion, publication, or canonical status.

## Preferred synthesis method

When documents should be merged, use claim- and section-level synthesis:

1. **Inventory the cluster.** Record every candidate package and its current lifecycle state.
2. **Map overlap.** Compare thesis, section outline, claims, examples, citations, tables, figures, and assets.
3. **Extract unique value.** Mark material that exists only in one source or is materially better there.
4. **Resolve conflicts.** Where sources disagree, fact-check rather than choosing whichever wording appears in the preferred file.
5. **Choose the target architecture.** Use the subject's natural conceptual structure, not the order of the source files.
6. **Synthesize.** Combine redundant material into one treatment, preserve useful distinctions, and remove duplicated argumentation.
7. **Repair provenance.** Update relationship metadata and changelogs for the synthesis target and all archived sources.
8. **Re-run ordinary editorial review.** A merged document must still satisfy its profile, citation, asset, factual, and publication rules.

A source may remain separately publishable when it has a genuinely different purpose. For example, a concise research brief derived from a long report can coexist with the report if that relationship is explicit.

## Duplicate-review criteria

No single signal is authoritative. Review should consider a combination of:

- exact normalized-body identity;
- title and slug similarity;
- section-heading overlap;
- shared thesis or conclusion;
- repeated examples and case studies;
- repeated citations or citation sequence;
- long shared passages or paraphrase-equivalent passages;
- similar tables, figures, or local assets;
- one document being substantially contained within another;
- chronology suggesting regeneration or later expansion of the same assignment.

A high similarity score is a candidate-generation tool, not an editorial verdict.

## Disposition model

Duplicate handling uses the existing lifecycle rather than inventing parallel publication states.

- A normal active artifact remains `draft`, `review`, `ready`, or `published` as appropriate.
- A duplicate, superseded source, or merged source that should no longer publish normally becomes `archived`.
- The reason it is archived is stored in duplicate-review and relationship metadata.
- An intentional derivative may remain active under the normal lifecycle.

This separates **editorial maturity** from **document relationships**.

## Relationship metadata

Canonical packages may use:

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
    status: ""       # pending | reviewed | not-applicable
    relationship: "" # independent | exact-duplicate | near-duplicate | derived | fork | merge-cluster
    disposition: ""  # keep-separate | archive-duplicate | supersede | merge-into-canonical | synthesize-new-canonical
    canonical_slug: ""
    rationale: ""
```

Relationship values should use canonical slugs. Do not invent a relationship merely to fill metadata.

## Changelog requirements

When an established article is declared a duplicate, derivative, merge source, or canonical synthesis target, record the decision in its article-local `CHANGELOG.md`.

The entry should identify:

- the relationship found;
- the canonical or related slug;
- whether unique material was preserved or merged;
- the resulting lifecycle state when it changed.

## Publication rule

An unresolved duplicate candidate may remain in `draft` or `review`, but it should not advance to `ready` until its relationship to the competing material has been resolved.

Archived duplicates and merged sources are never normal publication inputs. Marginalia remains a one-way projection of explicitly approved canonical artifacts.

## Automated detection

`scripts/duplicate_audit.py` is a read-only candidate finder. It can identify exact normalized-body duplicates and high-similarity or high-containment pairs, but it never edits files or chooses a disposition.

The editorial decision remains human/operator controlled because similarity cannot distinguish all legitimate forks, summaries, stylistic variants, and independent treatments of a shared topic.
