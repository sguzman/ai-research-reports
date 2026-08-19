# Editorial standard

This repository contains more than one kind of writing. A research report, a polemical essay, a deliberately Nietzschean performance, a personal reflection, and a work of fiction should not be forced into the same prose voice.

Editorial control therefore separates **form**, **editorial profile**, and **voice**.

- `type` describes what the artifact is: for example `report`, `research-brief`, `note`, `essay`, `fiction`, `dialogue`, or `reference`.
- `editorial_profile` selects the rules that govern its prose: `academic`, `argumentative`, `stylized`, `personal`, or `creative`.
- `voice` records an intentional voice when useful: for example `neutral`, `polemical`, `nietzschean`, `literary`, or another concise description. It is descriptive rather than a free pass for accidental generation residue.

These dimensions are independent. A short `essay` may be `stylized`; a long `report` should normally be `academic`; a `note` may be `academic` or `personal` depending on its purpose.

## Universal integrity rules

These rules apply to every profile unless the apparent violation is itself deliberate content, such as a quotation reproducing an error.

1. Correct ordinary spelling, punctuation, capitalization, agreement, malformed sentences, conversion defects, and obvious typographical errors while preserving proper nouns, technical vocabulary, foreign terms, quotations, and intentional orthography.
2. Remove accidental AI-production residue: references to the user, prompt, assistant, previous conversation, requested output, willingness to continue, or other traces of the generation interaction.
3. Remove malformed or fabricated citations and repair citation/link mismatches discovered during review.
4. Require a clean publication title. Prompt fragments, URLs, citation markers, export debris, and source dumps do not belong in the H1 or metadata title.
5. Remove duplicated conclusions, abandoned prompt fragments, assistant outros, padding created by generation, and obvious conversion duplication.
6. Every local image, diagram, download, or support file referenced by `main.md` must exist and be portable with the canonical article package.
7. New and normalized local support files belong under `data/md/<slug>/assets/`. Legacy `media/`, root-level cover files, and other historical layouts are migration debt rather than a reason to perpetuate the layout.
8. External links and externally hosted images must be valid and relevant when an article is ingested or substantively revised. Later link rot does not retroactively invalidate a historical revision.
9. Diagrams must actually render. A source-language diagram is not considered publication-ready merely because its text parses.
10. Editorial changes to an established article are recorded in its `CHANGELOG.md` using the repository's existing timestamp/summary table convention.

## Editorial profiles

### `academic`

Use for research reports, research briefs, technical histories, literature reviews, analytical notes, reference articles, and other writing intended to read as impersonal scholarly prose.

Default rules:

- third-person or impersonal narration;
- no first-person authorial narration except necessary quotation or a methodologically necessary statement that cannot be expressed cleanly otherwise;
- no second-person address;
- no direct address to `you` or the reader;
- no production-stage language such as `testing out a hypothesis`, `as requested`, or narration of the assignment;
- avoid self-reference such as `this report examines`, `this article argues`, `the present paper`, or `the report below` when the substantive claim can be stated directly;
- uncertainty should be expressed evidentially (`the evidence suggests`, `a plausible interpretation is`, `the record does not establish`) rather than conversationally;
- headings describe subject matter rather than the writing process.

A hypothesis may of course be tested. The defect is narrating the assignment instead of formulating the proposition, evidence, counterevidence, predictions, and limits directly.

### `argumentative`

Use for serious essays whose purpose is to make an argument in a recognizable authorial voice rather than simulate an academic report.

- first person is allowed when it carries genuine argumentative responsibility;
- second-person address is normally avoided unless rhetorically deliberate;
- polemical or forceful language is allowed;
- limited self-reference is allowed when structurally useful;
- prompt/assistant residue, broken citations, accidental repetition, and infrastructure defects remain prohibited.

### `stylized`

Use for essays intentionally written through a strong literary, philosophical, historical, or imitative voice—for example a Nietzschean critique.

- perspective, cadence, repetition, address, aphorism, rhetorical excess, and deliberate self-description may be features rather than defects;
- the `voice` field should identify the intended style when doing so is useful for future editors;
- editors preserve the performance rather than normalizing it into academic prose;
- accidental AI-production residue and technical defects remain prohibited.

A stylized work is not necessarily fiction. It may make real arguments while using a deliberately non-neutral voice.

### `personal`

Use for memoir, personal reflection, first-person notebook prose, autobiographical argument, or material whose point depends on the author's perspective.

- first person is expected;
- second person may be used deliberately;
- self-reference is not inherently defective;
- factual claims, citations, links, assets, grammar, and generation residue still receive normal review.

### `creative`

Use for fiction, poetry, dialogue, satire, dramatic writing, and other material whose language is governed primarily by artistic intent.

- perspective and voice are unrestricted;
- intentional grammatical deviation may be preserved;
- infrastructure, attribution, asset, citation, and accidental-generation defects are still corrected where applicable.

## Classification rule

Do not infer `academic` merely because an artifact is stored in this repository or was generated by a research tool. Classification is an editorial decision.

For legacy articles that lack `editorial_profile`, the field should remain explicitly unresolved during the census rather than being bulk-filled by heuristics. The editor may suggest a profile from the text and metadata, but a profile becomes canonical only when the article is reviewed.

`voice` should be blank or `neutral` when there is no meaningful special voice. It should not contain vague filler.

## Change control

Existing per-article changelogs use this form:

```markdown
# Changelog

| Timestamp | Summary |
| --- | --- |
| YYYY-MM-DD HH:MM:SS TZ | Concise description of the editorial change. |
```

Keep newest entries first. Record substantive corrections, perspective normalization, metadata reclassification, citation repair, asset migration, and other changes that materially alter the canonical package. Pure one-way publication into Marginalia does not create a second editorial history.

## Publication threshold

`ready` means the article has passed the **universal integrity rules** and the rules of its declared `editorial_profile`. `published` additionally means the approved canonical article has been projected successfully to the publication target.

A strong voice is not a defect. An accidental voice break is. The point of the metadata profile is to make that distinction explicit and enforceable.
