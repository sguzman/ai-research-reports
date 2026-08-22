# Editorial operations

This directory is the persistent handoff surface for corpus cleanup. It exists so an editor or another AI can resume the work from the repository without needing the conversation that produced earlier changes.

The canonical article source remains `data/md/<slug>/`. This directory does **not** replace article metadata, article-local changelogs, or lifecycle state.

## Files

- `QUEUE.yaml` — current operational queue, priorities, blockers, and next actions. Articles not listed there are untriaged unless their package/changelog says otherwise.
- `BATCH_LOG.md` — chronological record of editorial batches and the packages they changed.
- `CHANGELOG_AUDIT.md` — coverage audit for article packages changed since the editorial baseline.

## Two different kinds of state

Do not confuse editorial lifecycle with work-queue state.

Canonical lifecycle lives in each `article.yaml`:

- `draft`
- `review`
- `ready`
- `published`
- `archived`

Operational work state in `QUEUE.yaml` answers a different question: what should an editor do next?

Typical work states:

- `queued` — selected for an upcoming batch
- `in-progress` — currently being edited/audited
- `blocked` — cannot advance until a named problem is resolved
- `maintenance` — already publishable/published but needs a specific migration or refresh
- `done-for-now` — no currently scheduled editorial work

An article may therefore be lifecycle `review` and work-state `queued`, or lifecycle `published` and work-state `maintenance`.

## Batch protocol

Target roughly 5–15 related packages per cleanup batch. Smaller batches are appropriate for high-risk medical/legal/technical audits or large body rewrites.

For every batch:

1. Read the relevant article bodies and metadata before changing them.
2. Check duplicate/derivative relationships before spending heavily on prose cleanup.
3. Classify `type`, `editorial_profile`, and `voice` from the artifact itself.
4. Repair universal integrity defects.
5. Apply the declared profile's rules.
6. Verify factual/current claims to the depth required by the subject and lifecycle target.
7. Repair/migrate assets and diagrams when needed.
8. Audit the public-facing title as an editorial object, not as generation metadata.
9. Update metadata and lifecycle conservatively.
10. **Update `data/md/<slug>/CHANGELOG.md` for every changed article package in the same PR.**
11. Update `editorial/QUEUE.yaml` and append the batch to `editorial/BATCH_LOG.md` after the batch disposition is known.
12. Publish only from canonical `ready`/`published` source through the one-way Marginalia boundary.

## Title quality rule

A title is part of the article, not a transcript of the assignment that produced it. Before an article can be `ready`, inspect `title`, `linkTitle`, and the body H1 for generation/process language.

Prefer titles that are **memorable, evocative, sharp, or immediately useful**. A good title should name the intellectual object, tension, image, mechanism, event, or argument. Academic articles may be plain and descriptive; stylized articles may be romantic, severe, strange, funny, or beautiful. In either case, the title should sound chosen by an author rather than emitted by a task runner.

Avoid titles whose main function is to narrate the research process or document type, especially generic constructions such as:

- `Testing the Hypothesis That ...`
- `Testing a ... Hypothesis: A Research Framework`
- `An Analytical Report on ...`
- `A Research Report on ...`
- `A Comprehensive Guide to ...`
- `Exploring ...`
- `Investigating ...`
- `A Study of ...`

These phrases are not absolutely forbidden when the research method or document form is genuinely the subject, but they require an affirmative editorial reason. "This is technically a report/framework/guide" is not enough.

Prefer transformations such as:

- `Testing the Hypothesis That Culture Is Parasitic on Unsatisfied Human Needs` → `The Hungry Mirror: Culture and Unmet Human Need`
- `Testing a “Borderer” Meme-Style Hypothesis: A Research Framework` → `The Borderer Signal: Separating Meme Style from Ideology`

Stable slugs and URLs do **not** need to change when a display title improves. Treat the slug as plumbing and the title as prose. When retitling, keep `title`, `linkTitle`, the body H1, and any title-bearing report metadata coherent; update the package changelog in the same PR.

The editorial linter treats obvious process-title patterns as warnings for non-public work and as errors for `ready`/`published` packages. The heuristic is intentionally narrow: human editorial judgment remains responsible for titles that are technically lint-clean but still dead, generic, pompous, or obviously machine-made.

## Article changelog invariant

The article-local changelog is the authoritative human-readable editorial history for that package.

Every editorial PR that changes anything inside an established `data/md/<slug>/` package must also add a newest-first entry to that package's `CHANGELOG.md`. This includes:

- body edits;
- metadata/profile/lifecycle changes;
- citation/source corrections;
- factual corrections;
- duplicate/merge/archive decisions;
- asset migrations;
- diagram changes;
- publication-state changes recorded in the canonical repository.

A good entry says **what changed, why it changed, and what important blockers remain**. Avoid vague entries such as “cleaned article” or “updated metadata.” When a batch performs several materially different repairs, the changelog entry should name them.

Pure one-way rendering into Marginalia does not create a second article editorial history. When publication changes canonical lifecycle (`ready` → `published`), that canonical lifecycle change does receive an article-local entry.

## Handoff rule

At the end of a working session, leave enough state in the repository that another editor can answer:

- What was already changed?
- Why?
- Which articles are canonical versus archived duplicates?
- Which claims or systems still need verification?
- What is the next batch?
- What must not be silently normalized because it is intentional voice?

If the repository and chat disagree, prefer the repository's current canonical files and Git history.