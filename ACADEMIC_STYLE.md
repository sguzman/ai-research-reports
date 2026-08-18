# Academic editorial standard

This standard applies by default to research reports, research briefs, notes, histories, technical explainers, and other nonfiction analytical material in this repository.

The goal is publication-ready prose that reads as a self-contained academic document rather than as the transcript of an interaction with an AI system.

Creative work is an explicit exception. Fiction, memoir, dialogue, satire, poetry, or intentionally personal work should be classified accordingly in metadata (for example with a `fiction`, `memoir`, or `creative-writing` tag/category). A fanciful argument is not automatically exempt merely because its subject is speculative.

## Mandatory prose rules

Editorial review must ruthlessly correct ordinary spelling, punctuation, capitalization, agreement, malformed sentences, conversion errors, and obvious typographical mistakes while preserving technical terms, proper nouns, quotations, and the author's substantive argument.

Normal academic material must use impersonal, third-person prose. First-person narration (`I`, `we`, `our`, `my`, and equivalents) is rewritten unless it appears inside a necessary quotation. Second-person address (`you`, `your`, and equivalents) is rewritten. The document must not address the reader as though it were continuing a chat.

The article must not refer to the user, the prompt, the assistant, an earlier conversation, or instructions that produced it. Phrases such as `the user requested`, `as requested`, `your prompt`, or `would you like` are generation residue, not article content.

The article should not narrate its own existence. Avoid constructions such as `this report examines`, `this article argues`, `in this paper`, `the present study will`, or `the report below`. State the substantive claim directly. Section-level signposting is acceptable when genuinely useful, but the prose should not repeatedly describe the document instead of discussing the subject.

Likewise, avoid report-stage meta-language such as `testing out a hypothesis`, `this report tests the hypothesis`, or similar narration of the assignment. When hypothesis language is intellectually necessary, formulate the hypothesis and assess the evidence directly: identify the proposition, evidence, counterevidence, explanatory power, and limits.

An academic article is not required to pretend certainty. Qualifiers such as `the evidence suggests`, `a plausible interpretation is`, `the available record does not establish`, and `the hypothesis would predict` are preferable to conversational or self-referential framing.

## Structural rules

The H1 should be a clean publication title. Citations, URLs, prompt text, parenthetical source dumps, and conversion artifacts do not belong in the title.

Headings should describe subject matter rather than the writing process. Avoid headings such as `Research Request`, `How I Approached This`, `Testing the Hypothesis`, `What You Asked`, `Next Steps`, or boilerplate AI conclusions.

Repeated summaries, duplicated conclusions, assistant outros, abandoned prompt fragments, and padded transitions should be removed. A shorter clean article is preferable to preserving generated filler.

## Links, images, files, and diagrams

Every local image or file referenced by an article must actually exist inside that article package. Canonical articles must not depend on accidental files elsewhere in the repository or on paths that happened to exist on the conversion machine.

Local image and file links are checked mechanically by `scripts/article_lint.py`. Missing targets and paths escaping the article package are errors.

External links and externally hosted images should be verified during intake or substantive revision. Link rot years later is not an editorial defect in the historical article; the requirement is that links be valid at the time the article is accepted or republished. Links that are already dead, malformed, redirected to unrelated material, or obviously wrong during review must be repaired or removed.

Diagrams must render rather than merely exist as source text. Mermaid should use a fenced `mermaid` block and a recognized diagram directive. Indented Mermaid-like text, unmatched code fences, empty diagrams, or references to missing diagram assets must be repaired before publication. The blog rendering should be checked when a diagram or image is important to the argument.

## Quotations and false positives

First- or second-person language inside a necessary quotation is not rewritten merely to satisfy style rules. Automated lint is intentionally conservative: it identifies places requiring inspection, while editorial review determines whether the language is the author's narration, a quotation, a title, a technical token, or another legitimate exception.

## Change control

Editorial cleanup must not be silent. When an existing article is modified, the repository's established changelog/revision mechanism should record substantive and corrective changes. Pure mechanical publication projection into Marginalia does not create a second editorial history.

If the changelog mechanism is unavailable in the checked-out revision, editorial work should preserve the article and report the missing mechanism rather than inventing a competing format. Once the canonical changelog format is available, both legacy cleanups and newly submitted articles should use it consistently.

## Publication threshold

`ready` means more than factually plausible. A normal academic article should not enter `ready` while it contains unresolved perspective breaks, prompt leakage, self-reference, known spelling/grammar errors, missing local files, broken diagrams, or links known to be broken at review time.

`scripts/article_lint.py --strict` is the mechanical floor, not a substitute for editorial judgment.