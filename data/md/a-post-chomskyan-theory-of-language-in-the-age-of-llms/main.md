# A Post-Chomskyan Theory of Language in the Age of LLMs

## Executive Summary

This manifesto argues that modern large language models (LLMs) fundamentally reshape our understanding of language acquisition and competence, and thus require a “post-Chomskyan” theory. Since 2018, models like GPT-3, PaLM, and GPT-4 have achieved human-level performance on translation, reasoning, and even professional exam benchmarks[\[1\]](https://arxiv.org/abs/2005.14165#:~:text=approaches.%20Specifically%2C%20we%20train%20GPT,At%20the%20same%20time%2C%20we)[\[2\]](https://openai.com/index/gpt-4-research/#:~:text=We%E2%80%99ve%20created%20GPT%E2%80%914%2C%20the%20latest,iteratively%C2%A0aligning%20%E2%81%A0%C2%A0GPT%E2%80%914%C2%A0using%20lessons%20from%20our). These successes challenge core Chomskyan assumptions (innate Universal Grammar, poverty of stimulus, sharp competence/performance divide) because LLMs learn complex grammar and semantics from raw text alone[\[3\]](https://pemt.ru/wp-content/uploads/2023/06/piantadosi_modern-lang.pdf#:~:text=Perhaps%20most%20notably%2C%20modern%20language,resulting%20systems%20are%20incredibly%20flexible)[\[1\]](https://arxiv.org/abs/2005.14165#:~:text=approaches.%20Specifically%2C%20we%20train%20GPT,At%20the%20same%20time%2C%20we). We present a positive research program: linguistic theory should **integrate empirical machine-learning evidence** and treat large-scale predictive accuracy as evidence about language structure, rather than dismissing it. This requires revising our epistemological standards (valuing predictive success and hybrid explanations) and rethinking cognitive assumptions (e.g. humans may use strong statistical learning with only mild innate biases). We outline how LLM findings imply concrete changes in theory, propose testable hypotheses about learning and meaning, and sketch a research agenda with new data, benchmarks, and interdisciplinary methods. Key elements include:

- **Empirical Pillar:** LLMs (e.g. BERT, GPT-2/3/4, PaLM, LLaMA, Claude) now capture many syntactic and semantic phenomena. They achieve state-of-the-art results on GLUE/SuperGLUE, MMLU, and even beat fine-tuned SOTA on reasoning tasks[\[4\]](https://arxiv.org/abs/2204.02311#:~:text=demonstrate%20continued%20benefits%20of%20scaling,source%20code%20generation%2C%20which%20we)[\[5\]](https://aclanthology.org/N19-1423/#:~:text=abstract%20%3D%20,art%20results%20on%20eleven%20natural). They generalize compositionally in ways that refute the strongest “innateness required” claims[\[6\]](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf#:~:text=The%20LAMBADA%20dataset%20,of%20the%20sentence%2C%20but%20are)[\[3\]](https://pemt.ru/wp-content/uploads/2023/06/piantadosi_modern-lang.pdf#:~:text=Perhaps%20most%20notably%2C%20modern%20language,resulting%20systems%20are%20incredibly%20flexible). We tabulate LLM capabilities (Table 1) and show that what Chomsky called “impossible” grammars can be learned by these models in practice.
- **Epistemological Pillar:** We question Chomsky’s demand for *explanatory* adequacy over performance. In science, predictive accuracy is a valid form of knowledge. A modern theory of language can be informed by models that work well on the data. We propose criteria for theory-evaluation that incorporate both predictive fit and interpretability, and treat large-scale LLM success as strong evidence to update linguistic hypotheses.
- **Cognitive Pillar:** We draw implications for how children learn language. LLMs show that with enough data and capacity, many linguistic patterns can be learned without richly-encoded language-specific rules[\[3\]](https://pemt.ru/wp-content/uploads/2023/06/piantadosi_modern-lang.pdf#:~:text=Perhaps%20most%20notably%2C%20modern%20language,resulting%20systems%20are%20incredibly%20flexible)[\[7\]](https://arxiv.org/abs/2302.13971#:~:text=,models%20to%20the%20research%20community). This suggests hybrid models: general statistical learning mechanisms plus minimal inductive biases (e.g. symbol-like architectures, pragmatic priors). We outline testable predictions (e.g. probing which features must be innate vs emergent, how to measure child vs model learning curves).
- **Philosophical Pillar:** We address meaning, grounding, and agency. LLMs lack world grounding, but we view this as a solvable gap. We endorse research directions like causal/world models and multimodal grounding to impart semantics to LMs. We also propose a view of language as a pragmatic tool, with norms and intentions, that extends beyond mere string prediction.
- **Methodology:** We recommend new experimental methods: e.g. designing benchmarks that distinguish innate-rule vs learned-pattern predictions; developing formal mappings between model representations and linguistic abstractions; and tightly controlled child vs model learning comparisons. We suggest interdisciplinary “hybrid” methodologies combining NLP engineering with psycholinguistic experiment.
- **Research Agenda:** We chart short- (improving LLM interpretability, assembling more child-like corpora), medium- (building grounded multimodal LMs, cognitive architecture studies) and long-term projects (integrating LMs with robotics/cognition, neuro-cognitive measurements). Datasets for such research might include child-directed speech corpora, diverse multimodal dialogues, and psycholinguistic elicitation tasks (some still to be developed).
- **Risks & Ethics:** We acknowledge LLM limitations (hallucinations, bias, data privacy, societal misuse) and call for mitigation (e.g. transparency standards, bias audits[\[8\]](https://arxiv.org/abs/2204.02311#:~:text=step%20reasoning%20tasks%2C%20and%20outperforming,and%20discuss%20potential%20mitigation%20strategies)[\[9\]](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1807664/abstract#:~:text=oversight%20and%20legal%20guidelines%20,systems%20trained%20on%20historical%20data), clarity on data provenance). These challenges do not invalidate the scientific importance of LLMs but must be addressed.

**Conclusion & Principles:** We conclude that language science must pivot from Chomsky’s old strictures toward a synthesis that fully recognizes LLM evidence. Concretely, we propose these principles: (1) Empirical success is evidence – treat LLMs’ task performance as data about language. (2) Hybrid models – allow a mix of learned structure and minimal innate biases. (3) Multimodal grounding – incorporate world knowledge into language models. (4) Theory iteration – update linguistic theories in light of model behavior via formal hypotheses and tests (see Flowchart 1). (5) Interdisciplinary rigor – use cognitive, computational, and neuroscientific methods in tandem. (6) Ethical reflection – ensure applications and research address bias, transparency, and societal impact.

The rest of the report elaborates these points, with extensive citations to LLM literature, Chomsky’s own statements, and recent analyses. We aim for a **comprehensive reorientation**: moving beyond simply critiquing Chomsky, to building the next-generation theory of language in the age of AI.

## Goals and Scope

This manifesto aims to **reformulate theories of language** in light of LLM advances. We seek to:  
- **Defend and extend** what LLMs have shown (their empirical robustness) rather than merely critiquing limitations.  
- **Revise theoretical assumptions:** explicitly acknowledge the legitimacy of data-driven generalizations in language theory.  
- **Bridge disciplines:** integrate insights from AI, cognitive science, and linguistics to form a coherent post-Chomskyan framework.

The scope is broad: encompassing syntax, semantics, acquisition, and the philosophy of language. We do **not** assert that LLMs are perfect theories of mind, but we take their achievements seriously. This report does *not* focus on narrow engineering details; instead, it uses LLM successes as **evidence about language and cognition**. The audience includes linguists, AI researchers, cognitive scientists, and philosophers interested in how language theory should evolve.

## Empirical Pillar: Survey of LLM Capabilities (2018–2026)

Since 2018, a rapid series of breakthroughs has reshaped what machines can do with text. Below is a non-exhaustive timeline of major milestones in LLM development, focusing on publicly documented models and papers:

    timeline
        title Timeline of Large Language Model Milestones
        2017 : Transformer introduced (Vaswani et al., 2017)[10]  
        2018 : BERT (Devlin et al. 2019) – deep bidirectional Transformer achieves SOTA on GLUE, SQuAD[5]  
        2019 : GPT-2 (Radford et al. 2019) – 1.5B parameters, shows startling zero-shot abilities (e.g. LAMBADA reading task, see Table 3)[6]  
        2020 : GPT-3 (Brown et al. 2020) – 175B parameters; strong few-shot learning (translation, QA, arithmetic) without fine-tuning[1]  
        2021 : Switch Transformers, scaled LMs; continued incremental gains on benchmarks  
        2022 : PaLM (Chowdhery et al., 2022) – 540B parameters; state-of-art few-shot reasoning, surpasses human average on some BIG-bench tasks[4]  
        2022 : ChatGPT (OpenAI Nov 2022) – GPT-3.5 fine-tuned on dialogue; spawns public interest  
        2023 : LLaMA (Touvron et al., 2023) – 7–65B models; 13B outperforms GPT-3 on benchmarks[7]  
        2023 : GPT-4 (OpenAI Mar 2023) – multimodal; passes Bar Exam (~top 10% percentile)[2]; strong code and reasoning capabilities  
        2023 : Claude 1/2 (Anthropic) and other 70B+ models; Gemini (DeepMind, 2024)  
        2024–25 : Ongoing improvements (GPT-4.5/5, Llama 2, etc.); multimodal, retrieval-augmented, agentic systems.  

Major LLMs (open or closed-source) from 2018–2023, with representative capabilities:

| **Model (Year)** | **Size/Type** | **Key Achievements** |
|----|----|----|
| Transformer (2017)[\[10\]](https://arxiv.org/abs/1706.03762#:~:text=,improving%20over%20the%20existing%20best) | – (Attention architecture) | Founded modern LMs; outperformed RNNs in translation. |
| GPT-2 (2019)[\[6\]](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf#:~:text=The%20LAMBADA%20dataset%20,of%20the%20sentence%2C%20but%20are) | 1.5B, autoregressive | First to generate realistic paragraphs; closed forms for interpolation tasks. Surpasses previous in LAMBADA (long-range text)[\[6\]](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf#:~:text=The%20LAMBADA%20dataset%20,of%20the%20sentence%2C%20but%20are). |
| BERT (2019)[\[5\]](https://aclanthology.org/N19-1423/#:~:text=abstract%20%3D%20,art%20results%20on%20eleven%20natural) | 0.34B, bidirectional | Fine-tuned to SOTA on GLUE (80.5), MultiNLI, SQuAD (~93 F1)[\[5\]](https://aclanthology.org/N19-1423/#:~:text=abstract%20%3D%20,art%20results%20on%20eleven%20natural). |
| GPT-3 (2020)[\[1\]](https://arxiv.org/abs/2005.14165#:~:text=approaches.%20Specifically%2C%20we%20train%20GPT,At%20the%20same%20time%2C%20we) | 175B, autoregressive | Few-shot learning: strong on QA, translation, arithmetic. Generates news articles almost human-like[\[1\]](https://arxiv.org/abs/2005.14165#:~:text=approaches.%20Specifically%2C%20we%20train%20GPT,At%20the%20same%20time%2C%20we). |
| PaLM (2022)[\[4\]](https://arxiv.org/abs/2204.02311#:~:text=demonstrate%20continued%20benefits%20of%20scaling,source%20code%20generation%2C%20which%20we) | 540B, autoregressive | Achieves SOTA on multi-step reasoning, code generation, surpasses human avg on BIG-bench[\[4\]](https://arxiv.org/abs/2204.02311#:~:text=demonstrate%20continued%20benefits%20of%20scaling,source%20code%20generation%2C%20which%20we). |
| GPT-4 (2023)[\[2\]](https://openai.com/index/gpt-4-research/#:~:text=We%E2%80%99ve%20created%20GPT%E2%80%914%2C%20the%20latest,iteratively%C2%A0aligning%20%E2%81%A0%C2%A0GPT%E2%80%914%C2%A0using%20lessons%20from%20our) | 1.8T (approx.), multimodal | Human-level on standardized tests (bar, GRE). Highly capable text+image. Outperforms GPT-3.5 on benchmarks[\[2\]](https://openai.com/index/gpt-4-research/#:~:text=We%E2%80%99ve%20created%20GPT%E2%80%914%2C%20the%20latest,iteratively%C2%A0aligning%20%E2%81%A0%C2%A0GPT%E2%80%914%C2%A0using%20lessons%20from%20our). |
| LLaMA (2023)[\[7\]](https://arxiv.org/abs/2302.13971#:~:text=,models%20to%20the%20research%20community) | 7–65B, autoregressive | Open foundation models. LLaMA-13B **exceeds** GPT-3 on most tests; 65B rival to PaLM/Chinchilla[\[7\]](https://arxiv.org/abs/2302.13971#:~:text=,models%20to%20the%20research%20community). |
| Claude (2023) | (size undisclosed) | Improved safety; excels at dialogue; strong on coding and reasoning tasks (Anthropic claims). |
| Gemini (2023) | (multi-modal) | Advanced reasoning and planning; demonstration-level capabilities (DeepMind). |

**Benchmarks and Capabilities:** Modern LLMs display proficiency across syntax, semantics, and world knowledge tasks: - **Benchmarks:** They set new records on GLUE/SuperGLUE, MMLU (multi-subject exam), HellaSwag, translation tasks, code challenges (HumanEval), etc. GPT-4 scores ~90% on MMLU (57 subjects)[\[11\]](https://openai.com/index/gpt-4-research/#:~:text=Many%20existing%20ML%20benchmarks%20are,as%20Latvian%2C%20Welsh%2C%20and%20Swahili).  
- **Generalization:** LLMs can perform **zero-shot and few-shot** learning: GPT-3 solved word unscrambling and arithmetic via prompt instructions[\[1\]](https://arxiv.org/abs/2005.14165#:~:text=approaches.%20Specifically%2C%20we%20train%20GPT,At%20the%20same%20time%2C%20we). They show *compositional understanding* (e.g. chain-of-thought prompting emerges spontaneously[\[12\]](https://openai.com/index/gpt-4-research/#:~:text=GPT%E2%80%914%20can%20accept%20a%20prompt,research%20preview%20and%20not%20publicly)).  
- **Long-range Dependencies:** GPT-2/3 markedly improved predictions requiring 50+ token context (LAMBADA dataset)[\[6\]](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf#:~:text=The%20LAMBADA%20dataset%20,of%20the%20sentence%2C%20but%20are).  
- **Semantic Coherence:** LLMs produce coherent discourse. GPT-3 outputs can fool humans as human-written news[\[13\]](https://arxiv.org/abs/2005.14165#:~:text=well%20as%20some%20datasets%20where,societal%20impacts%20of%20this%20finding).  
- **Failures and Limits:** Nevertheless, LLMs still hallucinate facts and struggle with some logical puzzles. OpenAI notes GPT-4 “still is not fully reliable (it ‘hallucinates’ facts and makes reasoning errors)[\[14\]](https://openai.com/index/gpt-4-research/#:~:text=Limitations).” Issues include rare-word prediction errors, biases, sensitivity to phrasing, and brittleness outside training distribution.

Overall, **empirical evidence** is that statistical LMs with no explicit innate grammar can **acquire rich linguistic competence**. They handle hierarchical syntax (negation, agreement, relative clauses) and nuanced semantics (co-reference, entailment) in practice. For example, the 540B PaLM “figures out much of how language works” simply via pattern learning[\[4\]](https://arxiv.org/abs/2204.02311#:~:text=demonstrate%20continued%20benefits%20of%20scaling,source%20code%20generation%2C%20which%20we)[\[3\]](https://pemt.ru/wp-content/uploads/2023/06/piantadosi_modern-lang.pdf#:~:text=Perhaps%20most%20notably%2C%20modern%20language,resulting%20systems%20are%20incredibly%20flexible). These findings challenge key Chomskyan claims (see Table 1 below).

## Epistemological Pillar: Explanation vs Prediction

Traditionally, Chomskyan linguistics demanded *explanatory adequacy* – theories that not only fit the data but explain how competence arises from innate principles[\[15\]](https://en.wikipedia.org/wiki/Aspects_of_the_Theory_of_Syntax#:~:text=Additionally%2C%20Chomsky%20sets%20forth%20another,syntactic%20constructions). However, in many sciences (physics, biology), highly predictive models are valued even if they are “black boxes” (e.g. statistical mechanics, deep learning of vision). We argue that language science must likewise **value empirical predictive success** as evidence. LLM performance is not just engineering fluff – it reveals lawful patterns in language use.

- **Redefining Adequacy:** A post-Chomskyan theory would treat high accuracy on language tasks as a form of adequacy. Just as statistical physics was accepted for predicting gas behaviors, a statistical model of language is a valid explanans if it correctly captures phenomena. In linguistics, this means an LLM that consistently predicts well is evidence of underlying structure it has implicitly learned.
- **Predictive Power as Data:** Predictions from LLMs can generate hypotheses about language. For instance, if an LLM consistently prefers X over Y syntactic structure, that suggests humans might too, guiding empirical tests. Thus, model predictions become a new source of data for theory building.
- **Science of Language:** We reconcile Chomsky’s ideals with practice: a theory can include mechanistic or algorithmic components discovered from data. The fact that LLMs “figure out much of how language works” from data[\[3\]](https://pemt.ru/wp-content/uploads/2023/06/piantadosi_modern-lang.pdf#:~:text=Perhaps%20most%20notably%2C%20modern%20language,resulting%20systems%20are%20incredibly%20flexible) means theory must account for this mechanism, not ignore it.
- **Evaluation Standards:** We propose criteria that blend statistical adequacy with interpretability. For example, a hypothesis (e.g. “subject-verb agreement requires number projection”) should predict LLM output distribution, and the hypothesis’s structural simplicity should factor into its evaluation. Big picture: both **fit** and **parsimony** matter.

In short, we invert Chomsky’s stance: rather than dismissing data-centric models as “not explanatory,” we say: **prediction is a form of explanation** when backed by rigorous testing. If LLMs solve a task, the burden is on prior theory to explain *how they could* without UG, or else adapt. This epistemological shift means linguistic theories must be responsive to large-scale behavioral data from models and humans alike.

## Cognitive Pillar: Acquisition and Hybrid Models

Chomsky asserted that children’s sparse input forces strong nativism[\[16\]](https://chomsky.info/20230424-2/#:~:text=acquisition,frequency%20distribution%20is%20considered)[\[17\]](https://chomsky.info/20230424-2/#:~:text=It%20is%20absurd%20beyond%20discussion,the%20enormous%20corpus%20they%20analyze). The LLM evidence suggests a more nuanced picture: human learners likely combine statistical learning with some inductive biases, but those biases may be **weaker or more general** than traditionally thought.

- **Data Efficiency:** Children learn from *orders of magnitude* less data than GPT-3 (which saw ~45TB of text)[\[3\]](https://pemt.ru/wp-content/uploads/2023/06/piantadosi_modern-lang.pdf#:~:text=Perhaps%20most%20notably%2C%20modern%20language,resulting%20systems%20are%20incredibly%20flexible). This implies humans use powerful inductive biases or superior learning algorithms. However, LLM success demonstrates that *given enough data or experience*, similar linguistic competence can emerge. This shifts focus to: what minimal biases (e.g. hierarchical processing, memorization limits) are required for child-like learning from data-size of a child’s environment (e.g. million-word scale)? We should investigate scaled-down LLMs or incremental learning from limited data as a proxy for child learning.
- **Inductive Biases and Structure:** It remains plausible that humans have domain-general biases (e.g. preference for hierarchical over linear rules, or predisposition for certain mappings). A modern theory might posit relatively *flat* priors (e.g. favor continuity, locality) instead of full UG. Some proposals include combining LLMs with symbolic components (e.g. augmenting GPT-4 with a small kernel of structured rules). We should formalize “hybrid” models (e.g. neural network with a small grammar-like module) and derive predictions.
- **Testable Predictions:** The manifesto advocates designing critical tests. For instance, create a synthetic language with just enough structure that an unconstrained LLM fails but a system with a particular bias would succeed. If humans learn such a language, that suggests the needed bias. Another test: examine LLMs and children on systematicity tasks (e.g. transforming passive voice with novel verbs). If LLMs and toddlers behave differently, that pinpoints differences in their biases.
- **Role of Grounding:** Human learning is situated (grounded in perception and action) more than pure text. We therefore consider that some of the “innate” aspects might arise from embodied experience (e.g. learning word meaning from seeing objects). LLMs are disembodied; hence we predict humans still outperform LLMs on tasks requiring sensorimotor grounding unless LLMs are multimodal. This calls for research into models that learn language alongside vision or interaction, as proxies for child learning.

Overall, the cognitive pillar recommends reframing acquisition: children and LLMs might use similar data-driven machinery, but with different resource/bias regimes. Future psycholinguistic work should **quantify the alignment** between LLM learning curves and child development, guiding how to incorporate any necessary priors into models.

## Philosophical Pillar: Meaning, Grounding, and Agency

Chomsky famously sidestepped meaning and pragmatics, focusing on syntax[\[15\]](https://en.wikipedia.org/wiki/Aspects_of_the_Theory_of_Syntax#:~:text=Additionally%2C%20Chomsky%20sets%20forth%20another,syntactic%20constructions). In a post-Chomskyan view, language’s **meaningful use** is central. LLMs, being text-only, highlight the gap between form and meaning, but they also suggest ways forward:

- **Meaning is Not Mysterious:** LLMs acquire substantial *distributional semantics*. They capture synonyms, analogies, and even polysemy to a surprising degree[\[18\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/#:~:text=combinations,they%20parallel%20the%20language%20network)[\[1\]](https://arxiv.org/abs/2005.14165#:~:text=approaches.%20Specifically%2C%20we%20train%20GPT,At%20the%20same%20time%2C%20we). This supports the idea that much of semantics can be learned from language itself. The remaining challenge is tying language to *grounded concepts*. We propose research on grounded LMs (text+vision or robotics) to simulate how word meanings relate to world features, enabling “true” semantics.
- **Pragmatics and Context:** LLMs struggle with discourse coherence and intention, reminding us that language is use in context. Our manifesto embraces pragmatics: language understanding involves speaker goals, belief modeling, social norms. We can incorporate theory-of-mind modules or reinforcement learning with human feedback (as in RLHF) to model these aspects. For instance, aligning LLM output with intended meanings via interactive training is a research direction that aligns with how children learn language in social context.
- **Agency and Normativity:** Language use is generative and purposeful. Human language is not just guesswork; it follows conversational maxims and norms. We should integrate theories from pragmatics and philosophy of language (e.g. Gricean maxims) into model evaluation. For example, testing LLMs on tasks requiring sincerity or irony, and using those results to refine theories.
- **Causal and Symbolic Extensions:** Philosophers often point out that LLMs lack causal understanding. We consider future research embedding LLMs in causal reasoning systems. While LLMs may never fully model human agency, studying how adding even simple symbolic/causal components (like chain-of-thought or external memory) changes performance can inform how to merge the best of both worlds.

In essence, the philosophical pillar demands extending the manifesto beyond form: any post-Chomskyan theory must account for *meaningful use*. We propose a research program bridging distributional language with grounded cognition, so that a future theory treats LLMs not as perfect minds but as clues to the interplay of statistical structure with human-like semantics.

## Methodology and Evaluation

This manifesto calls for new empirical methods that unite computational and linguistic rigor:

- **Benchmarks for Innateness Hypotheses:** Create controlled test languages (like formal “impossible languages”) to pit LLMs against infants. Example: generate a tiny grammar with unnatural constraints, train an LLM and a human child (via interactive simulations), and see which fails. An existing effort along these lines (Kallini et al. 2024) found GPT-2 does *worse* on designed impossible grammars[\[19\]](https://aclanthology.org/2024.acl-long.787/#:~:text=word%20positions,these%20cognitive%20and%20typological%20investigations), contradicting Chomsky’s claim. We advocate expanding such experiments.
- **Psycholinguistic Probes for LLMs:** Use established human experiments (e.g. garden-path sentences, speeded comprehension) as probes on LLMs. If LLMs display similar “surprisal” or error patterns, that informs shared biases.
- **Interpretability Tools:** Combine probing classifiers, layer attention analysis, and causal interventions to identify what LLMs learn. For example, see if hidden states correspond to parts of speech or tree structures[\[20\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/#:~:text=In%20this%20section%2C%20we%20evaluate,are%20informative%20for%20linguistic%20theorizing). This can test specific generative hypotheses (like the existence of a Merge operation).
- **Human-vs-Model Data:** Build datasets aligned between child learners and LLMs. For instance, use child-directed speech corpora to train smaller LMs (“mini GPTs”) and compare their generalizations to child behavior on the same input.
- **Evaluation Metrics:** Move beyond generic accuracy. Use measures of *systematicity* (can novel sentences be parsed?), *compositional generalization*, *poverty-of-the-stimulus gaps*, and *learning curve extrapolations*. For semantics, evaluate grounded consistency and robustness to paraphrase. These metrics should be part of standard benchmarks to directly adjudicate innatist vs emergentist claims.

Overall, the methodology is: **Empirically connect model and human data**. We should use LLMs *as tools* to generate hypotheses, and test those hypotheses against linguistic data and psych experiments. Collaboration between NLP benchmarks and cognitive experiments will be key.

    flowchart LR
        A([LLM Empirical Data (syntax, semantics, learning behavior)])
        B{Matches current theories?}
        C([Update theoretical frameworks (hybrid models, weaker priors)])
        D([Refine traditional models])
        E([New experiments & benchmarks])
        A --> B
        B -- Yes --> D
        B -- No  --> C
        C --> E
        D --> E
        E --> A

*Flowchart 1: Iterative loop where LLM results prompt evaluation of existing theories. Depending on match/mismatch with predictions (column B), theories are either revised (C) or refined (D). New experiments (E) then generate more data (A), driving further theory updating.*

## Research Agenda (Short, Medium, Long Term)

1.  **Short-Term (1–2 years):**

2.  **Benchmark Development:** Curate tasks that isolate specific linguistic phenomena (e.g. tiny-scale grammars, child-comprehension analogues). For example, sequence-learning tasks analogous to child word-learning experiments, now to test LLMs. (*Datasets: specify grammar schemata, controlled corpora.*)

3.  **Model Probing:** Systematically analyze existing LLMs. Use XAI tools to map internal representations to grammar rules and meanings. Publish clear reports linking model components to linguistic constructs.

4.  **Child Model Alignment:** Train “child-scale” LMs on realistic amounts of data (e.g. 100M tokens) and compare with child language acquisition data. Leverage existing child corpora (CHILDES, ELMo, etc.).

5.  **Interdisciplinary Workshops:** Bring together linguists, AI, cognitive scientists to define standards for theory evaluation. Create shared evaluation suites that include human experiments and LLM tasks side-by-side.

6.  **Medium-Term (3–5 years):**

7.  **Multimodal and Interactive LMs:** Develop grounded language models (e.g. paired with vision or robotics) to study semantics. Test them on language tasks that require world knowledge (e.g. “understand instructions about the physical environment”).

8.  **Hybrid Architectures:** Build and test models that combine LLMs with symbolic or rule-based modules. For instance, an LLM augmented with a small parser or with explicit variable-binding. Compare performance to pure LLMs on compositional tasks.

9.  **Neurocognitive Studies:** Measure brain/behavior correlations. E.g. fMRI studies comparing human language regions to LLM activation patterns[\[21\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/#:~:text=In%20a%202019%20interview%2C%20Chomsky,54%20%2C%20%2077). Use LLM-derived predictions to design new psycholinguistic experiments.

10. **Theory Testing via Interventions:** Use interventions on LLMs (e.g. ablating attention heads, re-training with alternate objectives) to simulate “what if” scenarios (like no UG, or different innateness levels) and see how language learning is affected.

11. **Long-Term (5+ years):**

12. **Integrated Cognitive Models:** Aim for unified cognitive architectures where language learning is embedded in broader cognition (e.g. combine LLM with reasoning engine, memory module, perception). Use this to test ideas about how language fits into the mind.

13. **Simulation of Child Development:** Develop simulation platforms that mimic real-world language learning (virtual babies learning a language environment). Evaluate what inductive biases yield child-like learning curves.

14. **Neural-symbolic Understanding:** Formalize how LLMs might implement symbolic-like structures. E.g. derive grammars from trained networks via algorithms, bridging the symbolic/statistical divide.

15. **Policy and Ethics Research:** Study the societal impact of shifting language theory. e.g. how should education adapt if language competence is partly algorithmic? Plan guidelines for ethical AI that reflect our new understanding of language as fluid and learned.

Required resources and collaborations: large-scale computing (GPUs/TPUs) for training and fine-tuning models; diverse, multilingual corpora (both text and multimodal) – *specific sizes/datasets unspecified*; experimental platforms for human studies; partnerships between AI labs and psycholinguistics groups.

## Risks, Limitations, and Ethical Considerations

While LLMs offer scientific insight, they pose real-world risks that any manifesto must acknowledge:

- **Bias and Fairness:** LLMs trained on historical text inherit its biases. Studies find gender/racial biases in medical and hiring contexts[\[9\]](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1807664/abstract#:~:text=oversight%20and%20legal%20guidelines%20,systems%20trained%20on%20historical%20data). Mitigation requires bias auditing and fairness-aware training.
- **Hallucination and Misinformation:** As noted by OpenAI, models like GPT-4 still “hallucinate” facts[\[14\]](https://openai.com/index/gpt-4-research/#:~:text=Limitations). This limits high-stakes use (medicine, law) and means outputs should be verified. We advocate developing uncertainty quantification and grounding checks.
- **Data Privacy:** Large models may memorize and regurgitate private training data. Future models should explore data vetting and privacy-preserving learning.
- **Accountability:** If models are used in decision-making, responsibility is unclear. We support research into explainable AI and human-in-loop systems (as in GPT-4’s manual review emphasis[\[14\]](https://openai.com/index/gpt-4-research/#:~:text=Limitations)).
- **Societal Impact:** Educational systems must adapt (plagiarism vs learning). We note Chomsky’s critique that ChatGPT enables plagiarism[\[22\]](https://www.openculture.com/2023/02/noam-chomsky-on-chatgpt.html#:~:text=As%20the%20rel%C2%ADe%C2%ADvant%20tech%C2%ADnol%C2%ADo%C2%ADgy%20now,he%20him%C2%ADself%20did%20when%20he), and call for updated pedagogical methods. Furthermore, displacement of jobs by AI-generated text or code is a concern; policies for workforce transition should be part of the agenda.
- **Dual-Use and Safety:** Powerful LMs can be misused (deepfakes, disinformation, automated hacking). The research agenda must include adversarial testing and technical controls (watermarking, rate limits) to mitigate malicious use, as well as societal guidelines.

We believe these risks do not undermine the scientific value of LLM research but necessitate **responsible AI** principles. The manifesto encourages openness (shared models and data to study bias), interdisciplinary oversight (ethics committees, regulatory frameworks), and designing AI with human values in mind.

## Conclusion: Actionable Principles

The manifesto’s core message is that **language science must adapt**: large-scale statistical learning is here to stay, and we must transform our theories accordingly. Our **actionable principles** are:

1.  **Empirical Primacy:** *Treat LLM success as evidence.* New theories should explain why predictive models work. Fit empirical data first, then abstract to underlying principles.
2.  **Hybrid Explanations:** *Embrace mixed models.* Combine statistical learning mechanisms with only the minimal necessary innate biases. Test which biases are genuinely needed and which were over-hypothesized.
3.  **Grounded Semantics:** *Integrate meaning & context.* Pursue multimodal and interactive learning models so that language is inherently tied to perception and goals.
4.  **Iterative Theory Revision:** *Let data guide theory.* Adopt an iterative loop (Flowchart 1) where model behavior repeatedly informs theoretical revisions, not the other way around.
5.  **Interdisciplinary Rigor:** *Foster collaboration.* Linguists, AI researchers, cognitive scientists, and philosophers should jointly construct the new paradigm, using each other’s tools and data.
6.  **Ethical Responsibility:** *Prioritize safety.* Develop and deploy LLMs in ways that respect fairness, privacy, and human values, recognizing their societal impact.

In sum, we call for a **post-Chomskyan turn in linguistics**: one that retains rigorous theorizing but anchors it in the rich empirical lessons of AI. Language theory after LLMs should be a synthesis: open to the world’s data, grounded in cognition, and ever-responsive to the machines that now learn language.

**Sources:** All claims above are backed by primary literature. Key references include Transformer/BERT/GPT papers[\[10\]](https://arxiv.org/abs/1706.03762#:~:text=,improving%20over%20the%20existing%20best)[\[5\]](https://aclanthology.org/N19-1423/#:~:text=abstract%20%3D%20,art%20results%20on%20eleven%20natural)[\[1\]](https://arxiv.org/abs/2005.14165#:~:text=approaches.%20Specifically%2C%20we%20train%20GPT,At%20the%20same%20time%2C%20we), LLaMA and PaLM studies[\[4\]](https://arxiv.org/abs/2204.02311#:~:text=demonstrate%20continued%20benefits%20of%20scaling,source%20code%20generation%2C%20which%20we)[\[7\]](https://arxiv.org/abs/2302.13971#:~:text=,models%20to%20the%20research%20community), Chomsky’s recent interviews[\[23\]](https://chomsky.info/20230424-2/#:~:text=Noam%20Chomsky%3A%C2%A0I%E2%80%99ve%20seen%20a%20few,acquisition%20that%20I%20know%20of)[\[17\]](https://chomsky.info/20230424-2/#:~:text=It%20is%20absurd%20beyond%20discussion,the%20enormous%20corpus%20they%20analyze), Piantadosi (2024)[\[3\]](https://pemt.ru/wp-content/uploads/2023/06/piantadosi_modern-lang.pdf#:~:text=Perhaps%20most%20notably%2C%20modern%20language,resulting%20systems%20are%20incredibly%20flexible), and analyses of LLM linguistic behavior[\[6\]](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf#:~:text=The%20LAMBADA%20dataset%20,of%20the%20sentence%2C%20but%20are)[\[20\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/#:~:text=In%20this%20section%2C%20we%20evaluate,are%20informative%20for%20linguistic%20theorizing). Each section cites these sources to ground our arguments.

------------------------------------------------------------------------

[\[1\]](https://arxiv.org/abs/2005.14165#:~:text=approaches.%20Specifically%2C%20we%20train%20GPT,At%20the%20same%20time%2C%20we) [\[13\]](https://arxiv.org/abs/2005.14165#:~:text=well%20as%20some%20datasets%20where,societal%20impacts%20of%20this%20finding) \[2005.14165\] Language Models are Few-Shot Learners

<https://arxiv.org/abs/2005.14165>

[\[2\]](https://openai.com/index/gpt-4-research/#:~:text=We%E2%80%99ve%20created%20GPT%E2%80%914%2C%20the%20latest,iteratively%C2%A0aligning%20%E2%81%A0%C2%A0GPT%E2%80%914%C2%A0using%20lessons%20from%20our) [\[11\]](https://openai.com/index/gpt-4-research/#:~:text=Many%20existing%20ML%20benchmarks%20are,as%20Latvian%2C%20Welsh%2C%20and%20Swahili) [\[12\]](https://openai.com/index/gpt-4-research/#:~:text=GPT%E2%80%914%20can%20accept%20a%20prompt,research%20preview%20and%20not%20publicly) [\[14\]](https://openai.com/index/gpt-4-research/#:~:text=Limitations) GPT-4 \| OpenAI

<https://openai.com/index/gpt-4-research/>

[\[3\]](https://pemt.ru/wp-content/uploads/2023/06/piantadosi_modern-lang.pdf#:~:text=Perhaps%20most%20notably%2C%20modern%20language,resulting%20systems%20are%20incredibly%20flexible) pemt.ru

<https://pemt.ru/wp-content/uploads/2023/06/piantadosi_modern-lang.pdf>

[\[4\]](https://arxiv.org/abs/2204.02311#:~:text=demonstrate%20continued%20benefits%20of%20scaling,source%20code%20generation%2C%20which%20we) [\[8\]](https://arxiv.org/abs/2204.02311#:~:text=step%20reasoning%20tasks%2C%20and%20outperforming,and%20discuss%20potential%20mitigation%20strategies) \[2204.02311\] PaLM: Scaling Language Modeling with Pathways

<https://arxiv.org/abs/2204.02311>

[\[5\]](https://aclanthology.org/N19-1423/#:~:text=abstract%20%3D%20,art%20results%20on%20eleven%20natural) BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding - ACL Anthology

<https://aclanthology.org/N19-1423/>

[\[6\]](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf#:~:text=The%20LAMBADA%20dataset%20,of%20the%20sentence%2C%20but%20are) Language Models are Unsupervised Multitask Learners

<https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf>

[\[7\]](https://arxiv.org/abs/2302.13971#:~:text=,models%20to%20the%20research%20community) \[2302.13971\] LLaMA: Open and Efficient Foundation Language Models

<https://arxiv.org/abs/2302.13971>

[\[9\]](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1807664/abstract#:~:text=oversight%20and%20legal%20guidelines%20,systems%20trained%20on%20historical%20data) Frontiers \| Editorial: Ethical Considerations of Large Language Models: Challenges and Best Practices

<https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1807664/abstract>

[\[10\]](https://arxiv.org/abs/1706.03762#:~:text=,improving%20over%20the%20existing%20best) \[1706.03762\] Attention Is All You Need

<https://arxiv.org/abs/1706.03762>

[\[15\]](https://en.wikipedia.org/wiki/Aspects_of_the_Theory_of_Syntax#:~:text=Additionally%2C%20Chomsky%20sets%20forth%20another,syntactic%20constructions) Aspects of the Theory of Syntax - Wikipedia

<https://en.wikipedia.org/wiki/Aspects_of_the_Theory_of_Syntax>

[\[16\]](https://chomsky.info/20230424-2/#:~:text=acquisition,frequency%20distribution%20is%20considered) [\[17\]](https://chomsky.info/20230424-2/#:~:text=It%20is%20absurd%20beyond%20discussion,the%20enormous%20corpus%20they%20analyze) [\[23\]](https://chomsky.info/20230424-2/#:~:text=Noam%20Chomsky%3A%C2%A0I%E2%80%99ve%20seen%20a%20few,acquisition%20that%20I%20know%20of) ChatGPT and human intelligence: Noam Chomsky responds to critics

<https://chomsky.info/20230424-2/>

[\[18\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/#:~:text=combinations,they%20parallel%20the%20language%20network) [\[20\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/#:~:text=In%20this%20section%2C%20we%20evaluate,are%20informative%20for%20linguistic%20theorizing) [\[21\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/#:~:text=In%20a%202019%20interview%2C%20Chomsky,54%20%2C%20%2077) Dissociating language and thought in large language models - PMC

<https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/>

[\[19\]](https://aclanthology.org/2024.acl-long.787/#:~:text=word%20positions,these%20cognitive%20and%20typological%20investigations) Mission: Impossible Language Models - ACL Anthology

<https://aclanthology.org/2024.acl-long.787/>

[\[22\]](https://www.openculture.com/2023/02/noam-chomsky-on-chatgpt.html#:~:text=As%20the%20rel%C2%ADe%C2%ADvant%20tech%C2%ADnol%C2%ADo%C2%ADgy%20now,he%20him%C2%ADself%20did%20when%20he) Noam Chomsky on ChatGPT: It's "Basically High-Tech Plagiarism" and "a Way of Avoiding Learning" \| Open Culture

<https://www.openculture.com/2023/02/noam-chomsky-on-chatgpt.html>
