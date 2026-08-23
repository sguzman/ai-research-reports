# Language Under Constraint: A Post-Chomskyan Theory for the LLM Era

## The proposal

The most useful lesson of large language models is not that Chomsky was wrong and statistics were right. That framing preserves the old argument by merely swapping the winner.

A more productive theory begins from a different premise:

> **Language acquisition is a constrained learnability problem.**

A learner encounters a finite, structured stream of experience. The learner itself is not neutral: it has memory, architecture, perceptual channels, representational capacities, objectives, attentional tendencies, and developmental history. Out of that interaction comes a system capable of open-ended linguistic generalization. The scientific task is to determine **which constraints on the learner and the input are necessary to produce the human result**.

Large language models matter because they have expanded the set of learning systems that can be experimentally compared. They show that predictive learning from exposure can produce much richer linguistic structure than many earlier debates assumed. But they also make the residual questions sharper. Their success depends on inductive bias and often enormous data; their failures can be highly structured; their internal representations and developmental trajectories need not match humans; and formal linguistic competence can diverge from grounded, goal-directed language use.

A genuinely post-Chomskyan program should therefore preserve one of generative linguistics' deepest questions—**how finite experience yields structured, productive competence**—while replacing broad impossibility claims and binary nature-versus-statistics arguments with explicit competitions among learners.

This is not a manifesto for abandoning theory in favor of benchmarks. It is a proposal for making theory more falsifiable.

## What “post-Chomskyan” means here

The term does not mean that the history of generative linguistics should be discarded or that every concept associated with Chomsky has been refuted. Chomsky's own program changed substantially from early transformational grammar through Principles and Parameters and Minimalism. Treating “Universal Grammar” as one frozen list of 1960s rules would be historically and theoretically careless.

The break proposed here is methodological.

A post-Chomskyan theory should reject three habits:

1. **Innateness by incredulity.** A structure should not be declared unlearnable merely because no obvious surface cue explains it.
2. **Statistical triumphalism.** A model should not be declared a theory of human acquisition merely because it achieves high predictive accuracy after enormous training.
3. **Benchmark substitution.** Success on generic NLP tasks should not stand in for reproducing the particular generalizations, error patterns, data efficiency, and developmental constraints that a linguistic theory is supposed to explain.

In their place, the field can use a more demanding principle:

> A proposed linguistic constraint earns explanatory weight when removing or weakening it makes human-like acquisition fail across realistic inputs and credible competing learners.

The inverse matters too:

> A proposed innate constraint loses explanatory weight when diverse, relatively general learners repeatedly acquire the target generalization from realistic experience without it.

This makes computational learning evidence symmetrical. Models are not machines for proving empiricism. They are experimental adversaries for any necessity claim.

## Four levels that language theory should keep separate

A major source of confusion is the tendency to ask one model to answer every question about language at once. A more disciplined theory separates at least four levels.

### 1. Learnability

**What can be acquired from what experience by what learner?**

This is the level most directly transformed by modern language modeling. A learnability claim specifies the input, learner, target phenomenon, and success criterion. It can be tested by changing one component while holding the others fixed.

Questions at this level include:

- Can a learner infer filler-gap dependencies from realistic exposure?
- What data support island sensitivity?
- Which aspects of morphology emerge under a given tokenization?
- Does a learner prefer humanly possible structures over carefully controlled impossible alternatives?
- How much experience is required before the generalization appears?

Learnability is where poverty-of-the-stimulus arguments should live or die.

### 2. Representation

**What internal structure supports the acquired behavior?**

Two learners can reach similar outputs through very different representations. A model that passes grammaticality tests may encode hierarchical structure, shallow distributional shortcuts, memorized templates, or some mixture.

A linguistic theory should therefore ask not only whether behavior is correct, but whether the internal organization supports the same kinds of generalization under intervention. Useful tests include representation probing, causal interventions, ablations, novel lexical substitutions, structural recombination, and out-of-distribution evaluation.

This level prevents performance from being mistaken for mechanism.

### 3. Use and performance

**How is linguistic knowledge expressed under finite memory, attention, processing time, task demands, and noise?**

Human speakers know constructions they sometimes fail to process or produce correctly. A useful cognitive theory needs a story about those divergences. Neural models also have context limits, decoding procedures, interference, and task-sensitive errors, but these need not correspond to human performance constraints.

The competence-performance distinction therefore should be treated as an empirical decomposition rather than a slogan. Researchers can ask which model errors arise from representation, which from processing, and which resemble human resource limitations.

### 4. Grounding and functional competence

**How does language connect to perception, action, world knowledge, social inference, goals, and shared situations?**

Kyle Mahowald and colleagues' distinction between formal and functional linguistic competence is useful here. A model can become highly competent at linguistic form without thereby possessing the full machinery required for human language use in the world.

Grounding should not be invoked as a mystical veto on text-based models. It should be decomposed experimentally: reference, perceptual categories, action consequences, speaker intentions, common ground, social prediction, causal world models, and interaction can each be tested.

These four levels interact, but collapsing them produces bad arguments. A model's failure at grounded reasoning does not erase evidence about syntactic learnability. Its syntactic success does not establish a theory of human thought.

## The central unit: a learner-input-target triple

The basic object of the theory is not “language” in the abstract. It is a **learner-input-target triple**:

\[
(L, D, T)
\]

where:

- \(L\) is a learner with specified architecture, memory, objective, and inductive biases;
- \(D\) is the learner's experience, including amount, distribution, modality, ordering, and social context;
- \(T\) is a target human generalization or developmental pattern.

The central empirical question is whether training \(L\) on \(D\) yields behavior matching \(T\).

This sounds simple, but it changes the grammar of the debate. Statements such as “children could not learn this from experience” or “Transformers learn syntax from data” are incomplete until the relevant \(L\), \(D\), and \(T\) are specified.

The same target can then be tested across a family of learners:

\[
L_1, L_2, \ldots, L_n
\]

and a family of input regimes:

\[
D_1, D_2, \ldots, D_m.
\]

The result is not a single benchmark score but a **learnability surface**: a map of which combinations produce the human generalization, how much data they require, which errors they make, and which counterfactual patterns they also learn.

A structural prior becomes scientifically interesting when it changes that surface in a way that aligns with humans.

## Architecture is bias

The phrase “learned from data alone” should largely disappear from serious discussion.

No learner encounters data alone. A Transformer imposes a computational form. A recurrent network imposes another. A child arrives with a body, sensory systems, memory capacities, attention, motivation, social orientation, and a developmental trajectory. Even a simple Bayesian learner has a hypothesis space and prior.

The meaningful dispute is therefore not whether language requires bias. It is **how much of the relevant bias must be specifically linguistic**.

Several possibilities should be placed in competition:

- rich language-specific structural constraints;
- weak language-specific priors combined with strong general sequence-learning biases;
- domain-general hierarchy or memory constraints;
- perceptual and motor structure that indirectly favors linguistic regularities;
- social-pragmatic biases toward communicative interpretations;
- architectural biases emerging from efficient prediction or compression;
- combinations of these.

This reframing improves both sides of the old debate. Generative linguists no longer need to defend an all-or-nothing “innate grammar” object. Statistical learners no longer get to hide architecture inside the word *general*.

## Developmental realism is part of the theory

A model trained on a trillion tokens and a child exposed to years of multimodal social interaction are not comparable simply because both eventually produce grammatical English.

The BabyLM research program is important because it treats **sample efficiency** as a first-class scientific variable. Constraining models to much smaller corpora forces architecture, objectives, data composition, and learning strategy to do more explanatory work.

A post-Chomskyan program should push this further. Developmental realism has several dimensions:

### Quantity

How many words, utterances, interactions, or hours of experience are available before the human target behavior appears?

### Distribution

Children do not receive a uniform sample of the web. Their input is concentrated in recurring speakers, environments, constructions, routines, and communicative needs.

### Order

Experience arrives through time. A model that succeeds only when late, complex structures are mixed into training from the beginning may be learning under a developmental regime unlike the human one.

### Modality

Children hear prosody, see gestures and objects, track gaze, act on the world, and participate in shared situations. Text-only corpora strip away information that might either simplify or complicate acquisition.

### Interaction

Human learners can alter their future input by attending, responding, asking, imitating, and acting. Their data distribution is partly endogenous.

A useful computational theory should gradually add these dimensions instead of assuming that “more realistic” always means “more data.” Sometimes additional modalities reduce ambiguity and make learning easier; sometimes they impose new integration problems. That too is empirical.

## The evidence can support richer innateness

A post-Chomskyan program should be designed so that a strong innateness result is possible.

Suppose researchers identify a human generalization that emerges reliably and early. They construct developmentally realistic corpora containing the evidence plausibly available to learners. A broad family of high-capacity, domain-general learners repeatedly fails. Adding more generic capacity does not help. Enlarging the corpus within realistic bounds does not help. But introducing a specific structural prior causes rapid, human-like acquisition while also improving the learner's rejection of impossible alternatives.

That would be evidence **for** the prior.

The conclusion would be stronger than an argument from intuition because competing learners had been allowed to try.

Nur Lan, Emmanuel Chemla, and Roni Katzir's 2026 work on parasitic gaps and across-the-board movement illustrates the shape of such an argument. Their current networks fail on important parts of wh-movement under natural training conditions, while enrichment of the relevant evidence improves performance. They appropriately treat the result as tentative rather than final because failure may still belong to the learner rather than the input. The post-Chomskyan response is not to dismiss the failure. It is to build better competing learners and see whether the result survives.

A theory becomes more credible when it can win an adversarial experiment rather than an argument over plausibility.

## The evidence can also dissolve proposed innate structure

The reverse path is equally important.

Wilcox, Futrell, and Levy's work on filler-gap dependencies and island constraints shows that autoregressive models can acquire nontrivial hierarchical behavior from exposure, weakening a poverty-of-the-stimulus argument for that particular structure. If such successes replicate across architectures, child-scale data regimes, languages, and stronger diagnostics, the explanatory burden on a rich innate constraint should decline.

This does not imply a blank slate. The successful learner has biases. But the location of explanation moves. What once appeared to require a language-specific prohibition may instead emerge from more general properties of prediction, memory, representation, or distribution.

The correct theoretical reaction is not embarrassment. It is compression: remove machinery that no longer earns its keep.

A good post-Chomskyan theory should be willing to become **less innate** or **more innate** phenomenon by phenomenon.

## Possible languages as a ranking problem

Generative linguistics has long asked why human languages occupy only a restricted region of the space of logically possible communication systems. LLMs create a new way to operationalize that question.

Instead of demanding that a learner assign a binary label—possible or impossible—the theory can study a **learnability ranking**. Given synthetic languages controlled for superficial complexity, how rapidly does the learner acquire each one? How much data does it require? How robustly does it generalize? Does the ranking correlate with human typological plausibility?

Kallini and colleagues' 2024 impossible-language experiments are an early example of this approach: GPT-2-small models found several manipulated languages harder to learn than English. Tim Hunter's subsequent criticism of a confounded comparison is equally important. The lesson is not that the experiment failed; it is that the possible-language problem now has experimental design criteria.

A stronger program would require:

- multiple independently motivated impossible-language transformations;
- controls for description length and statistical complexity;
- different architectures and tokenizations;
- human artificial-language learning where feasible;
- held-out structural generalization rather than training loss alone;
- preregistered predictions about which systems should be easy or hard;
- replication across natural languages.

The target is not to rediscover a traditional Universal Grammar by neural network. It is to identify which constraints repeatedly emerge as necessary to reproduce the shape of the human language space.

## Representation should be tested causally

Behavioral benchmarks alone are too permissive. A model can arrive at the right answer for the wrong reason.

A stronger linguistic model should survive **causal representation tests**. Researchers can intervene on internal states, remove heads or pathways, alter memory, substitute lexical items, scramble irrelevant cues, and construct minimal pairs designed to destroy surface heuristics while preserving structure.

Theoretical concepts such as dependency, constituent, feature, agreement, reference, and scope should earn their place by supporting interventions and predictions, not merely by being recoverable from a linear probe after training.

This creates a productive exchange between symbolic linguistic theory and neural modeling. Linguistic categories propose candidate causal abstractions; models provide systems in which those abstractions can be searched for and manipulated.

The goal is neither “the network secretly contains X-bar theory” nor “the network is uninterpretable but scores well.” It is to discover representations with **causal explanatory leverage**.

## Human-model convergence is stronger evidence than model success

A model becomes more informative about human language when several dimensions converge at once.

A useful hierarchy of evidence is:

| Evidence | What it supports |
| --- | --- |
| High next-token or benchmark performance | the model predicts the evaluated data well |
| Correct novel structural generalization | the model learned something beyond local memorization |
| Success under realistic data limits | the input may contain enough information for that learner |
| Human-like learning curve | acquisition difficulty may be similarly ordered |
| Human-like error profile | learner limitations may overlap |
| Human-like impossible-language selectivity | inductive biases may align |
| Causally similar internal representations | mechanism may overlap more deeply |
| Cross-linguistic and developmental replication | explanation is less likely to be English- or benchmark-specific |

No single row is a magic threshold. But the evidentiary claim should scale with the degree of convergence.

This prevents the word *human-like* from doing unlimited work.

## Formal competence should be allowed to stand on its own

A recurring mistake in arguments about LLMs is to treat language as invalid unless it comes bundled with a complete theory of thought.

Mahowald and colleagues' distinction between formal and functional linguistic competence gives a cleaner architecture for theory. A system may model syntax, morphology, lexical relationships, and combinatorial semantics impressively while remaining weak at persistent world models, social reasoning, perception, or action.

For linguistic science, that is not a disqualification. It is a decomposition.

The post-Chomskyan program should therefore resist two temptations:

- **inflation:** claiming that formal linguistic success proves understanding, agency, or general intelligence;
- **deflation:** claiming that imperfect grounding makes formal linguistic success theoretically irrelevant.

Text-only language models can answer questions about the learnability and representation of linguistic form. Grounded multimodal and interactive systems can answer additional questions about how those forms connect to the world.

The models should be judged against the level they are being asked to explain.

## A concrete experimental protocol

The constructive program can be expressed as a repeatable research cycle.

### Step 1: choose a target phenomenon

Define a human generalization narrowly enough to test: a syntactic dependency, morphological pattern, semantic inference, pragmatic expectation, phonological restriction, or developmental error.

### Step 2: characterize human behavior

Measure judgments, production, comprehension, learning age, variability, and characteristic errors rather than relying on an idealized rule alone.

### Step 3: construct realistic input regimes

Estimate what relevant evidence is available to learners. Include alternative corpora with different assumptions about quantity, distribution, modality, and developmental order.

### Step 4: specify competing learner families

Use learners that differ in the bias under dispute. Do not compare a richly engineered neural architecture with an imaginary blank slate.

### Step 5: predeclare diagnostic predictions

Specify what each theoretical position predicts before training. A benchmark becomes much more probative when it can distinguish hypotheses rather than simply rank systems.

### Step 6: train and evaluate out of distribution

Test novel lexical items, structural recombinations, rare environments, and counterfactual constructions. Include possible and impossible alternatives.

### Step 7: intervene on representations

Use ablations and causal manipulations to determine which internal mechanisms support the behavior.

### Step 8: compare data efficiency and learning trajectory

Ask not only whether the final model succeeds but when, with how much evidence, and in what order.

### Step 9: update the theory

If generic learners succeed robustly, reduce the weight assigned to rich domain-specific prior structure. If they fail robustly and a targeted prior repairs the failure, increase it.

### Step 10: replicate across languages and modalities

A theory of human language should not depend on one English benchmark or one model family.

This cycle is deliberately boring compared with declarations of a new paradigm. That is a virtue. It makes theoretical change cumulative.

## What happens to explanatory adequacy?

Chomsky's distinction between descriptive and explanatory adequacy should not be thrown away. It should be computationally sharpened.

A system that predicts observed sentences may be descriptively impressive without explaining why a human learner converges on one grammar rather than countless alternatives. The post-Chomskyan answer is not that prediction itself equals explanation. It is that **a learning system becomes explanatory when its priors, input, and learning dynamics jointly account for human convergence**.

Explanatory adequacy can therefore be decomposed into questions:

- Why does this learner prefer the attested generalization?
- Which alternatives does it reject?
- What information in the input drives the transition?
- Which prior biases are indispensable?
- Why does acquisition occur at roughly the observed data scale?
- Why do the learner's errors resemble or differ from human errors?
- Does the account generalize cross-linguistically?

A neural system that answers those questions may be explanatorily useful even if it does not look like a traditional grammar. A formal grammar that cannot survive realistic learnability tests may be descriptively elegant without explaining acquisition.

The standard should be reciprocal.

## What happens to Universal Grammar?

Universal Grammar becomes a hypothesis space rather than a sacred object or a defeated relic.

At the richest end, human language acquisition may require highly specific structural priors. At the leanest end, much apparent linguistic specificity may emerge from general learning architecture, memory, perception, communication, and the statistical structure of human languages. The empirical program should locate different phenomena along that continuum.

This may produce a **mosaic theory of innateness**:

- some constraints arise from domain-general computation;
- some from perceptual or memory limits;
- some from communicative pressures;
- some from historically accumulated properties of languages adapted to learners;
- some may still require language-specific biological structure.

There is no scientific requirement that one answer govern every level.

That possibility is more interesting than the old binary because it turns the contents of human linguistic preparedness into a research output rather than a premise.

## Falsifiers for the post-Chomskyan program

A theory that celebrates every result cannot fail. This program needs explicit conditions that would weaken it.

### It would weaken if generic learner comparison stops discriminating theories

If radically different learner families always reproduce the same patterns whenever scaled sufficiently, computational comparison may reveal little about human priors unless developmental constraints restore discrimination.

### It would weaken if human linguistic targets cannot be specified reliably

A learnability experiment is only as meaningful as the phenomenon it attempts to reproduce. If judgments, developmental data, or cross-linguistic generalizations are unstable, the target itself needs revision.

### It would weaken if internal model explanations remain causally opaque

Behavioral similarity without mechanistic understanding limits cognitive inference. Better interpretability is therefore not optional when claims move from learnability to representation.

### A lean-bias theory would be weakened by repeated child-scale failures

If diverse, high-capacity, domain-general learners repeatedly fail on human generalizations under realistic input while targeted language-specific priors consistently repair those failures, the evidence should move toward richer innate linguistic structure.

### A rich-UG theory would be weakened by repeated generic success

If diverse learners repeatedly acquire supposedly unlearnable structures from realistic input, reproduce human developmental order, reject impossible alternatives, and do so without the proposed language-specific machinery, those constraints should lose explanatory status.

These are not rhetorical concessions. They are the mechanism by which the theory changes.

## Relationship to the evidence-audit companion

The constructive framework is paired with `how-llms-challenge-chomskyan-assumptions-analytical-report`, retitled **The Learner in the Corpus**.

The companion asks what existing LLM evidence actually establishes about Chomskyan claims. The constructive program begins one step later and asks what research design follows once the evidence is treated with those limits.

The division is:

- **The Learner in the Corpus:** adjudication of existing evidence;
- **Language Under Constraint:** a positive framework for future linguistic theory and experiments.

The two remain separate because a constructive program should not be allowed to manufacture its own empirical verdict.

## Conclusion

The LLM era does not require linguistics to choose between Chomsky and the machine.

It creates the possibility of a more demanding science.

The lasting Chomskyan question remains: how does a finite learner exposed to finite experience acquire a system capable of structured, open-ended language? What changes is the evidentiary standard. Proposed necessities can increasingly be tested against actual learners. Statistical success can be forced to survive child-scale data, impossible-language controls, developmental trajectories, and causal representation tests. Model failures can become evidence for stronger priors rather than embarrassing exceptions.

A post-Chomskyan theory should therefore be neither anti-innate nor anti-statistical. It should be **constraint-seeking**.

Its central question is:

> **What is the smallest, best-supported set of learner and environmental constraints that reproduces the human language trajectory—and what experiment would prove that set insufficient?**

That is a theory of language capable of learning from the machines without mistaking the machines for the answer.

## Sources and further reading

### Empirical foundations

- Ethan Gotlieb Wilcox, Richard Futrell, and Roger Levy, [“Using Computational Models to Test Syntactic Learnability”](https://direct.mit.edu/ling/article/55/4/805/113304/Using-Computational-Models-to-Test-Syntactic), *Linguistic Inquiry* 55, no. 4 (2024): 805–848. DOI: 10.1162/ling_a_00491.
- Nur Lan, Emmanuel Chemla, and Roni Katzir, [“Large Language Models and the Argument from the Poverty of the Stimulus”](https://doi.org/10.1162/ling_a_00533), *Linguistic Inquiry* 57, no. 2 (2026): 315–342.
- Julie Kallini, Isabel Papadimitriou, Richard Futrell, Kyle Mahowald, and Christopher Potts, [“Mission: Impossible Language Models”](https://aclanthology.org/2024.acl-long.787/), *Proceedings of ACL 2024*, 14691–14714.
- Tim Hunter, [“Kallini et al. (2024) Do Not Compare Impossible Languages with Constituency-based Ones”](https://aclanthology.org/2025.cl-2.7/), *Computational Linguistics* 51 (2025): 641–650.
- Michael Y. Hu et al., eds., [*The 2nd BabyLM Challenge at the 28th Conference on Computational Natural Language Learning*](https://aclanthology.org/2024.conll-babylm/), Association for Computational Linguistics, 2024.

### Cognitive and theoretical boundaries

- Roni Katzir, [“Why Large Language Models Are Poor Theories of Human Linguistic Cognition: A Reply to Piantadosi”](https://doi.org/10.5964/bioling.13153), *Biolinguistics* 17 (2023), e13153.
- Kyle Mahowald, Anna A. Ivanova, Idan A. Blank, Nancy Kanwisher, Joshua B. Tenenbaum, and Evelina Fedorenko, [“Dissociating Language and Thought in Large Language Models”](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/), *Trends in Cognitive Sciences* 28, no. 6 (2024): 517–540.
- Steven T. Piantadosi, “Modern Language Models Refute Chomsky's Approach to Language,” in *From Fieldwork to Linguistic Theory: A Tribute to Dan Everett*, Language Science Press, 2024.
- Noam Chomsky, *Aspects of the Theory of Syntax*, MIT Press, 1965.
- Noam Chomsky, *The Minimalist Program*, MIT Press, 1995.
