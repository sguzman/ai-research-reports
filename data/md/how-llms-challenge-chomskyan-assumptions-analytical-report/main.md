# The Learner in the Corpus: What LLMs Actually Show About Chomsky

## Argument in brief

Large language models have changed the argument over language acquisition, but not in the simple way suggested by headlines about machines having “refuted Chomsky.” Their most important scientific contribution is methodological: **they make claims about learnability experimentally tractable**.

For decades, a central dispute in linguistics has concerned the gap between the linguistic evidence available to a learner and the structured knowledge human speakers ultimately acquire. Generative linguists have often argued that some of that gap is too large to cross without substantial innate constraints. Critics have replied that the input may be richer, and general learning mechanisms more powerful, than the argument assumes. The difficulty has always been operational: what could a learner actually extract from a realistic corpus under specified learning assumptions?

Modern neural language models provide imperfect but unusually powerful tools for attacking that question. They can be given controlled amounts of linguistic input, trained under explicit architectures and objectives, and tested on generalizations that go beyond memorized strings. Sometimes they acquire structures that had been presented as difficult to learn from exposure. Sometimes they fail. Those failures can themselves become evidence about the insufficiency of the data, the learner, or both.

The resulting picture is neither **Chomsky vindicated** nor **Chomsky demolished**. It is much more useful:

1. some specific poverty-of-the-stimulus arguments have been weakened by successful computational learners;
2. other candidate poverty-of-the-stimulus cases remain alive and may even be strengthened by model failures under realistic input constraints;
3. current models are not “bias-free” learners and therefore cannot show that language is acquired without inductive bias;
4. success at formal linguistic patterning does not establish that the same mechanism explains human cognition, meaning, reasoning, or grounded language use;
5. broad claims about what neural networks can or cannot learn increasingly need to survive direct computational tests.

That is the real break introduced by LLM-era linguistics. The dispute is moving from **what seems learnable in principle** toward **which learners acquire which structures from which inputs under which constraints**.

## Five claims that should not be collapsed into one

Arguments about Chomsky and LLMs become confused when several distinct questions are treated as interchangeable.

### 1. Can a statistical learner acquire a particular linguistic generalization?

This is a learnability question. It can often be tested directly by training models on specified corpora and evaluating their behavior on held-out constructions.

### 2. Can a learner do so from developmentally plausible input?

A structure may be learnable from hundreds of billions of tokens yet not learnable from anything resembling the linguistic experience of a child. Data quantity, distribution, modality, and developmental order therefore matter.

### 3. Does successful learning eliminate the need for innate bias?

No. Every learner has inductive biases. A Transformer has an architecture, tokenization scheme, context structure, optimization procedure, objective function, parameterization, and training regime. The relevant scientific question is not **bias or no bias**, but **which biases are necessary for which generalizations** and whether those biases must be specifically linguistic.

### 4. Is the learner a good model of human linguistic cognition?

Behavioral success on a construction does not establish identity of mechanism. A model may demonstrate that information is extractable from a corpus without reproducing the representations, data efficiency, developmental trajectory, memory limits, error profile, or neural organization of human learners.

### 5. Does linguistic success amount to understanding or thought?

This is a different question again. Work in cognitive science increasingly distinguishes **formal linguistic competence**—mastery of linguistic form and structural regularities—from the broader capacities required to use language in reasoning, social interaction, world modeling, and action. An LLM can be scientifically informative about the first without thereby becoming a complete model of the second.

A serious assessment of “LLMs versus Chomsky” has to keep these questions separate.

## What the poverty-of-the-stimulus argument actually asks

The argument from the poverty of the stimulus is strongest when a human learner reliably acquires some linguistic generalization that does not appear to be warranted by the learner's experience unless the learner arrives with relevant prior structure.

The crucial phrase is **does not appear to be warranted**. Establishing that negative claim is difficult. Human corpora are large and structured; indirect statistical cues can be subtle; proposed general-purpose learning procedures can extract regularities that are not obvious to introspection. Merely observing that children are rarely explicitly taught a rule does not establish that their input contains insufficient evidence for acquiring it.

This is where computational models become valuable even when they are not accepted as cognitive replicas. A learner can be trained on a controlled corpus and asked whether it develops the relevant generalization. A successful learner is a constructive counterexample to at least one claim of impossibility: it shows that **some specified learning system can extract enough information from the specified data**. A failed learner is weaker evidence because failure may reflect limitations of the architecture or optimization rather than poverty of the stimulus. But if many capable learners fail, and performance improves when the relevant evidence is artificially enriched, the failure becomes increasingly interesting.

The debate therefore becomes an experimental triangle:

| Component | Question |
| --- | --- |
| **Input** | What evidence is actually available, in what quantity and distribution? |
| **Learner** | What architecture, objective, memory, and inductive biases process that evidence? |
| **Target** | What human generalization must be reproduced, including successes and characteristic errors? |

An argument about innateness is only as good as its control over all three.

## A real success: filler-gap dependencies and islands

One of the clearest examples of LLMs changing a traditional learnability argument is Ethan Gotlieb Wilcox, Richard Futrell, and Roger Levy's study, [“Using Computational Models to Test Syntactic Learnability”](https://direct.mit.edu/ling/article/55/4/805/113304/Using-Computational-Models-to-Test-Syntactic), published in *Linguistic Inquiry*.

English wh-dependencies involve relationships between a displaced element and a gap, as in questions where a fronted phrase is interpreted at a later position. Human speakers are also sensitive to **island constraints**: some syntactic environments sharply restrict where such dependencies may occur. These phenomena have often figured in poverty-of-the-stimulus reasoning because the relevant constraints are abstract, hierarchical, and not taught explicitly.

Wilcox and colleagues trained autoregressive neural language models and tested them with factorial psycholinguistic diagnostics rather than asking whether they merely produced plausible sentences. The models acquired the basic filler-gap contingency, showed evidence of unbounded and hierarchical generalization, and attenuated their expectation for a gap inside island environments. The authors therefore concluded that their results provide evidence **against a poverty-of-the-stimulus argument for this particular structure**.

That qualification is essential. The result does not establish that Universal Grammar is false, that children learn syntax exactly like the tested networks, or that every island phenomenon follows from distributional learning. It does something more precise and scientifically valuable: it weakens the claim that the relevant filler-gap and island behavior is simply unavailable to a sufficiently capable learner from exposure.

This is what a computational challenge to an innateness argument should look like. It identifies a phenomenon, a corpus, a learner, a diagnostic, and a result.

## The counter-result: harder wh-movement phenomena

The same methodology can also produce evidence in the opposite direction.

Nur Lan, Emmanuel Chemla, and Roni Katzir extended the wh-movement test in [“Large Language Models and the Argument from the Poverty of the Stimulus”](https://doi.org/10.1162/ling_a_00533), published in *Linguistic Inquiry* in 2026. They focus especially on **parasitic gaps** and **across-the-board movement**, constructions in which an additional gap can alter the acceptability pattern that a simple island account would predict.

Their networks did not adequately approximate the human pattern when trained on natural corpora roughly intended to approach developmentally relevant scales. More importantly, one model improved substantially when its training corpus was artificially enriched with examples of the rare constructions. Lan and colleagues interpret this result cautiously but argue that it is consistent with the stimulus being too poor, rather than the learner merely lacking enough capacity.

The comparison with Wilcox et al. is more important than either result in isolation:

- a family of neural learners can acquire some nontrivial wh-dependency generalizations from ordinary distributional input;
- success on those easier diagnostics does not automatically extend to the entire system;
- model failure on the harder phenomena becomes informative when enriched evidence improves learning;
- neither paper settles how much innate structure humans possess.

The LLM era therefore does not replace poverty-of-the-stimulus reasoning with a blanket statistical-learning victory. It gives the argument a **finer grain**. Instead of asking whether “syntax” is learnable, researchers can ask which pieces of a syntactic system are recoverable by which learners under which data regimes.

## Data scale is not a technical footnote

The inherited version of this report repeatedly treated an LLM trained on web-scale text as if it were a direct counterexample to child language acquisition. That inference is too strong.

Large production models are ordinarily trained on vastly more text than a child hears or reads during language development. A model that succeeds only after consuming an enormous corpus may demonstrate that a pattern is present in the statistical structure of language while saying little about whether a human learner could infer it from developmentally realistic exposure.

This is why the [BabyLM Challenge](https://aclanthology.org/events/babylm-2024/) matters for linguistic theory. The challenge deliberately constrains pretraining data—most prominently to 10-million- and 100-million-word tracks—to study sample-efficient language learning rather than treating scale as free. Its existence reflects a genuine methodological problem: computational systems and children often occupy radically different input regimes.

Developmentally constrained modeling does not make a neural network into a child. The child receives speech, gesture, shared attention, perception, social feedback, action, and a temporally ordered developmental environment rather than a shuffled text corpus. But matching the data budget more closely removes one of the most obvious confounds. A claim that a generic learner can explain human acquisition becomes much stronger if it survives **child-scale data, child-like ordering, and child-relevant evaluation**.

Conversely, a model that fails under such conditions should not immediately be declared proof of innate grammar. The architecture may simply be poor. The correct response is competitive modeling: change the learner while holding the input and target behavior fixed.

## No neural learner is “without priors”

Another inherited overclaim was that LLMs learn language through “statistics alone” with no innate structure. That phrasing confuses the absence of hand-coded linguistic rules with the absence of inductive bias.

Transformers impose strong assumptions about computation. They process token sequences through particular attention and feed-forward operations; they use positional information, finite context, specific training objectives, and optimization procedures; and their tokenization determines which regularities are visible at the input level. Even apparently generic architectural choices can favor some patterns over others.

The scientifically useful comparison is therefore not:

> Universal Grammar **versus** a learner with no prior structure.

There is no second object.

The useful comparison is:

> **Which prior structures are needed to produce human-like generalization from realistic input?**

Those priors might be language-specific, domain-general, architectural, memory-based, attentional, social, perceptual, or combinations of these. LLMs make the hypothesis space larger because they demonstrate the surprising power of relatively general predictive learners. They do not make priors disappear.

Roni Katzir's [reply to Piantadosi](https://doi.org/10.5964/bioling.13153) is valuable precisely because it presses on this distinction between a successful engineering system and a theory of human linguistic cognition. Even if one disagrees with Katzir's broader assessment, the burden is correct: a cognitive theory needs to explain not merely that a pattern can be generated, but why humans learn the patterns they do, with the representations, limitations, and data they actually have.

## “Impossible languages” become experimentally testable

A second important dispute concerns the **possible-language problem**. Generative theories have often sought constraints that characterize languages humans could naturally acquire while excluding formally imaginable but humanly impossible systems.

Noam Chomsky and coauthors have argued that data-driven language models are not constrained in the right way and can in effect learn systems that a human child would not. That claim is empirically testable.

Julie Kallini and colleagues did exactly that in [“Mission: Impossible Language Models”](https://aclanthology.org/2024.acl-long.787/). They constructed synthetic transformations of English designed to span a range from relatively natural-looking alterations to strongly unnatural rules, including transformations based on word position. They trained GPT-2-small models on the resulting languages and found that the models generally had greater difficulty learning the impossible languages than ordinary English. Their result challenges the categorical claim that the model class is indifferent between possible and impossible languages.

But this result should not be upgraded into “Transformers have discovered Universal Grammar.” Tim Hunter's 2025 response, [“Kallini et al. (2024) Do Not Compare Impossible Languages with Constituency-based Ones”](https://aclanthology.org/2025.cl-2.7/), argues that the most important comparison in the original experiment contains a confound and therefore cannot support the strongest typological conclusion.

The dispute is scientifically productive either way. A vague argument about what neural networks “would learn” has become a design problem:

1. define an independently motivated space of possible and impossible languages;
2. control complexity and surface statistics;
3. train multiple learner classes;
4. compare learning curves and generalization;
5. ask whether the ranking matches human acquisition and typology.

The key advance is not a final verdict. It is that **possible-language bias can now be measured rather than merely asserted**.

## Competence and performance are not erased by prediction

The inherited report also treated LLM success as though it refuted the distinction between linguistic competence and performance. It does not.

Chomsky's distinction was intended to separate a speaker's linguistic knowledge from the contingent limitations and disturbances involved in actual language use. Whether that exact formulation is the best theory is contestable, but the general scientific need to distinguish **knowledge from the process that expresses knowledge under finite resources** remains.

A model's next-token behavior is also produced by a particular computational process under particular constraints. Its errors need not have the same source as human errors. Katzir emphasizes this point: superficially similar agreement mistakes, for example, do not automatically imply the same competence-performance decomposition in humans and models.

Computational modeling can therefore refine this distinction rather than eliminate it. A useful model should ask separately:

- what representations support the generalization;
- what computations retrieve and use them;
- what errors arise from the learned representation;
- what errors arise from memory, context, decoding, or task demands.

If anything, neural models make the old distinction more experimentally concrete because internal representation and online behavior can be manipulated separately.

## Language is not identical to thought

A system's linguistic fluency also should not be used as a shortcut to claims about full human cognition.

Kyle Mahowald, Anna Ivanova, Idan Blank, Nancy Kanwisher, Joshua Tenenbaum, and Evelina Fedorenko argue in [“Dissociating language and thought in large language models”](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/) for a distinction between **formal linguistic competence** and **functional linguistic competence**. Contemporary LLMs are often remarkably strong at the former: they capture many structural, lexical, and combinatorial regularities of language. Their ability to connect language reliably to world knowledge, reasoning, situation models, and social goals is more uneven and can depend on additional training or systems.

That distinction prevents two symmetrical mistakes.

The first is the pro-LLM mistake:

> fluent language therefore proves human-like thought.

The second is the anti-LLM mistake:

> failures of reasoning or grounding therefore prove that the model has learned nothing scientifically interesting about language.

Both inferences are too broad. A language model can be a strong experimental model of some formal linguistic phenomena without being a complete model of a person.

## What has actually been weakened

The strongest LLM-era challenges to Chomskyan linguistics are narrower than “Universal Grammar is dead,” but they are still substantial.

### 1. Armchair claims of unlearnability are less defensible

If a proposed poverty-of-the-stimulus argument says a generalization cannot plausibly emerge from distributional evidence, a successful learner can now put pressure on that claim. The burden shifts toward demonstrating why the model's data, architecture, or evaluation invalidates the counterexample.

### 2. Some specific poverty-of-the-stimulus arguments have lost force

Wilcox et al.'s filler-gap/island results are a concrete example. The appropriate conclusion is local: one formerly difficult-looking domain contains more learnable structure than a strong poverty-of-the-stimulus reading predicted.

### 3. Generic statistical learners are more structurally powerful than many linguists expected

Modern predictive models learn hierarchical and long-distance regularities that earlier caricatures of “mere statistics” would not have predicted. That matters even when the models remain cognitively implausible in other respects.

### 4. Categorical claims about impossible-language indifference require evidence

Kallini et al. show why this is now an experimental question. Hunter's critique then shows how demanding the experiment must be.

### 5. Linguistic theory can use model failure as evidence

Lan, Chemla, and Katzir demonstrate the reverse direction: computational learners can be used to strengthen an argument for insufficient input when failure persists under controlled conditions and improves after targeted enrichment.

A method that can produce evidence for either side is scientifically more valuable than a benchmark designed only to celebrate model capability.

## What LLMs have not established

Several stronger claims in the inherited article do not survive review.

| Claim | Status after review |
| --- | --- |
| LLMs show grammar can be learned with **no inductive bias** | **Rejected.** Every model embodies biases; the question is which kinds are required. |
| Web-scale LLM training directly models child acquisition | **Rejected.** Data scale, modality, developmental order, and social environment differ dramatically. |
| Successful neural syntax refutes Universal Grammar in general | **Not established.** Results bear on particular proposed constraints and learning arguments. |
| Current LLMs are equally able to learn humanly possible and impossible languages | **Empirically challenged, not settled.** Kallini et al. report asymmetries; Hunter identifies an important confound. |
| Competence/performance is obsolete because prediction works | **Rejected.** Representation and use remain distinct explanatory problems. |
| Linguistic fluency demonstrates human-like thought or grounding | **Rejected.** Formal language competence and broader functional cognition must be evaluated separately. |
| LLM failures vindicate strong language-specific innateness | **Not established.** Failure can arise from the learner, input, optimization, or evaluation. |
| LLMs are irrelevant to linguistic theory unless they are humanlike in every respect | **Rejected as a methodological requirement.** Models can test learnability and information in the input without being complete cognitive replicas. |

## A better standard: adversarial learnability experiments

The most promising synthesis is to treat computational learners as **adversarial tests of linguistic necessity claims**.

Suppose a theory claims that humans must possess prior structure **B** to acquire phenomenon **P** from input **D**. A serious test should not simply train the largest available model and celebrate a benchmark score. It should construct a family of learners with different biases and ask what is minimally required to reproduce the human pattern.

A strong experiment therefore specifies:

1. **Target phenomenon.** What exact human generalization is at issue?
2. **Input regime.** How much data, of what kind, in what distribution and developmental order?
3. **Learner family.** What architecture and inductive biases are present?
4. **Training objective.** What information is the learner rewarded for extracting?
5. **Human benchmark.** What judgments, production patterns, acquisition timing, and error profiles must be matched?
6. **Counterfactuals.** Does the learner also acquire patterns humans systematically reject?
7. **Ablations.** Which biases or data sources are necessary for success?
8. **Replication across learners.** Is the result peculiar to one architecture or robust across plausible alternatives?

Under this standard, success and failure are both useful. A generic learner that repeatedly acquires a structure from realistic data weakens the case for rich domain-specific prior knowledge. A wide family of generic learners that repeatedly fails while humans converge rapidly—and succeeds only when supplied with a particular structural bias—strengthens the case for that bias.

The argument becomes cumulative rather than theatrical.

## Relationship to the constructive companion essay

This report is deliberately an **evidence audit**, not a replacement theory of language. Its companion package, `a-post-chomskyan-theory-of-language-in-the-age-of-llms`, develops the positive research program that follows from the audit.

The division of labor is important:

- **this article:** What has LLM evidence actually weakened, preserved, or left unresolved in Chomskyan arguments?
- **the companion:** What should a language theory look like once computational learnability becomes a first-class source of evidence?

Keeping the two artifacts separate prevents a manifesto from predetermining the empirical verdict.

## Conclusion

Large language models have not settled the innateness debate. They have made it better.

They show that powerful predictive learners can acquire linguistic structure that was once easy to dismiss as beyond “statistics.” They have weakened particular poverty-of-the-stimulus arguments and forced claims about impossible languages to become experimental. At the same time, developmentally constrained failures, data-efficiency gaps, architectural differences, and the distinction between formal language and broader cognition block the stronger conclusion that human language acquisition has been explained by scale alone.

The durable lesson is methodological:

> **Do not ask whether language is innate or statistical in the abstract. Ask what a specified learner can acquire from a specified input, which biases make the difference, and whether the resulting generalization actually matches humans.**

That question is harder than declaring either Chomsky or the LLMs victorious. It is also finally testable.

## Sources and further reading

### Core learnability studies

- Ethan Gotlieb Wilcox, Richard Futrell, and Roger Levy, [“Using Computational Models to Test Syntactic Learnability”](https://direct.mit.edu/ling/article/55/4/805/113304/Using-Computational-Models-to-Test-Syntactic), *Linguistic Inquiry* 55, no. 4 (2024): 805–848. DOI: 10.1162/ling_a_00491.
- Nur Lan, Emmanuel Chemla, and Roni Katzir, [“Large Language Models and the Argument from the Poverty of the Stimulus”](https://doi.org/10.1162/ling_a_00533), *Linguistic Inquiry* 57, no. 2 (2026): 315–342.
- Julie Kallini, Isabel Papadimitriou, Richard Futrell, Kyle Mahowald, and Christopher Potts, [“Mission: Impossible Language Models”](https://aclanthology.org/2024.acl-long.787/), *Proceedings of ACL 2024*, 14691–14714. DOI: 10.18653/v1/2024.acl-long.787.
- Tim Hunter, [“Kallini et al. (2024) Do Not Compare Impossible Languages with Constituency-based Ones”](https://aclanthology.org/2025.cl-2.7/), *Computational Linguistics* 51 (2025): 641–650. DOI: 10.1162/coli_a_00554.

### Data efficiency and cognitive comparison

- Michael Y. Hu et al., eds., [*The 2nd BabyLM Challenge at the 28th Conference on Computational Natural Language Learning*](https://aclanthology.org/2024.conll-babylm/), Association for Computational Linguistics, 2024.
- Roni Katzir, [“Why Large Language Models Are Poor Theories of Human Linguistic Cognition: A Reply to Piantadosi”](https://doi.org/10.5964/bioling.13153), *Biolinguistics* 17 (2023), e13153.
- Kyle Mahowald, Anna A. Ivanova, Idan A. Blank, Nancy Kanwisher, Joshua B. Tenenbaum, and Evelina Fedorenko, [“Dissociating Language and Thought in Large Language Models”](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/), *Trends in Cognitive Sciences* 28, no. 6 (2024): 517–540. DOI: 10.1016/j.tics.2024.01.011.

### Positions in the debate

- Steven T. Piantadosi, “Modern Language Models Refute Chomsky's Approach to Language,” in *From Fieldwork to Linguistic Theory: A Tribute to Dan Everett*, Language Science Press, 2024.
- Noam Chomsky, Ian Roberts, and Jeffrey Watumull, “The False Promise of ChatGPT,” *The New York Times*, March 8, 2023.
- Noam Chomsky, [“ChatGPT and Human Intelligence: Noam Chomsky Responds to Critics”](https://chomsky.info/20230424-2/), interview, April 24, 2023.
- Noam Chomsky, *Aspects of the Theory of Syntax*, MIT Press, 1965; and *The Minimalist Program*, MIT Press, 1995, for the historical development of the generative research program rather than a frozen caricature of Universal Grammar.
