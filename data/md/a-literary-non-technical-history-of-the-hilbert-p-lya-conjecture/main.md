# The Unheard Instrument

There is a useful way to imagine the Riemann zeros, provided the image is not mistaken for evidence.

Imagine hearing a sequence of notes through a wall. The intervals are too structured to sound arbitrary, yet no instrument is visible. One can catalogue the notes. One can discover statistical regularities among them. One can notice that other, known instruments produce strikingly similar patterns. Eventually the question becomes almost irresistible:

> **What is vibrating?**

That question is the emotional center of the Hilbert–Pólya idea. The nontrivial zeros of the Riemann zeta function have long suggested a spectrum: a collection of numbers that might be the eigenvalues of some natural operator. If the right operator were self-adjoint, its spectral values would be real. In the right formulation, that reality would force the zeros onto the critical line and prove the Riemann Hypothesis.

But the wall has never opened.

No accepted Hilbert–Pólya operator is known. The name itself is retrospective: neither David Hilbert nor George Pólya published a conjecture under that title. The historical evidence for Pólya's version comes from a letter written roughly seven decades after the conversation he remembered; the evidence for Hilbert's version is even more indirect. Later mathematics supplied spectacular reasons to take spectral analogies seriously—Selberg trace formulas, the function-field Riemann Hypothesis, Montgomery's pair correlation, Dyson's random matrices, Odlyzko's computations, quantum chaos, noncommutative geometry—but none of these results establishes that the Riemann zeros are the spectrum of a hidden self-adjoint object.

That distinction makes the story better rather than worse. Hilbert–Pólya is not a century-long near-proof whose final lemma has somehow escaped everyone. It is a **research dream that repeatedly encounters structures resembling the one it asks for, without yet finding the object itself**.

This is the history of that dream: how an unpublished intuition acquired a name, how twentieth-century mathematics made it look less absurd, why random matrices transformed its reputation, and why the strongest evidence still stops short of the conclusion people most want to draw.

## 1. Before the instrument: Riemann's zeros

The story begins without spectra.

In 1859 Bernhard Riemann published a paper of only a few pages on the distribution of prime numbers. Euler had already shown that the zeta function could be written as a product over primes. Riemann pushed the subject into the complex plane and connected fluctuations in the counting of primes to the zeros of the analytically continued zeta function. The paper became foundational precisely because it made the apparently erratic prime numbers answerable to the analytic behavior of a single complex function. [Clay Mathematics Institute, “Riemann's 1859 Manuscript”](https://www.claymath.org/collections/riemanns-1859-manuscript/)

The nontrivial zeros lie in the critical strip between real parts 0 and 1. Riemann proposed that all of them have real part exactly one half. That is the Riemann Hypothesis.

A convenient modern normalization makes the spectral temptation easy to see. One forms an entire function usually written as \(\Xi(t)\), obtained from the completed zeta function after substituting

\[
s=\frac12+it.
\]

In this language, the Riemann Hypothesis is equivalent to saying that **every zero of \(\Xi(t)\) is real**. Bombieri's official Clay problem description uses this normalization explicitly. [Enrico Bombieri, “The Riemann Hypothesis”](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)

That formulation creates an obvious invitation. Real eigenvalues are exactly what self-adjoint operators produce. If the zeros of \(\Xi\) could be identified—canonically, completely, and independently—with the spectrum of such an operator, their reality would cease to look like a miracle of complex analysis. It would become a consequence of spectral structure.

The important word is **if**.

It is easy to state the dream backward: “suppose the zeros are eigenvalues of a self-adjoint operator.” But a proof cannot quietly assume the property it is meant to explain. The desired object must be defined without first knowing that the zeros are real, and its spectral correspondence with all the zeros must itself be proved.

The instrument cannot be built by writing the already-known notes onto its keys.

## 2. A conjecture that was never quite written down

The phrase **Hilbert–Pólya conjecture** gives the impression of a documented joint proposal. The surviving history is much stranger.

### Pólya's remembered conversation

Andrew Odlyzko, while investigating the statistical behavior of high zeta zeros, wrote to George Pólya asking about the origin of the spectral idea. Pólya answered on January 3, 1982. He recalled spending roughly 1912–1914 in Göttingen and trying to learn analytic number theory from Edmund Landau. Landau asked whether Pólya knew a physical reason the Riemann Hypothesis should be true. Pólya said that it would be so if the nontrivial zeros were connected with a physical problem in such a way that the hypothesis became equivalent to the reality of that problem's eigenvalues.

Pólya added a crucial historical detail: **he never published the remark**. Odlyzko preserves the correspondence among his materials on the origins of Hilbert–Pólya. [Andrew Odlyzko, “Correspondence about the Hilbert-Polya Conjecture”](https://www-users.cse.umn.edu/~odlyzko/)

The letter is excellent evidence that Pólya remembered having the idea. It is not evidence that a formal research program circulated under his name in the 1910s, nor that he had identified a candidate operator. The phrase “Hilbert–Pólya conjecture” imposes later unity on what was initially an intuition.

### Hilbert through Hellinger through Weil

The Hilbert side is more indirect still.

André Weil later recorded a story told to him by Ernst Hellinger, one of Hilbert's students. According to Hellinger, after discussing Fredholm theory and the reality of eigenvalues for symmetric kernels, Hilbert told a seminar that with such a theorem they would prove the Riemann Hypothesis. This fits Hilbert's work on integral equations and the emerging spectral theory of the early twentieth century. But there is no corresponding Hilbert paper laying out the modern conjecture, no explicit operator for the zeta zeros, and no evidence that Hilbert developed the suggestion into a program.

That makes the familiar attribution historically plausible but evidentially uneven. Pólya left a retrospective first-person account. Hilbert survives through an anecdote transmitted by a student to another mathematician and later recorded in Weil's scientific commentary.

The earliest published formulation recognizably resembling the later Hilbert–Pólya program appears much later, in Hugh Montgomery's 1973 paper on pair correlation. [Hugh L. Montgomery, “The Pair Correlation of Zeros of the Zeta Function,” *Proceedings of Symposia in Pure Mathematics* 24 (1973)](https://www.ams.org/tran/1981-267-01/S0002-9947-1981-0621970-5/)

So the historical sequence is almost backwards from the name:

1. Hilbert and Pólya leave remembered spectral intuitions, not published constructions.
2. Spectral mathematics develops enormously without producing the zeta operator.
3. Mid-century analogies make the idea more concrete.
4. Montgomery and Dyson uncover statistics that make the spectral dream newly compelling.
5. Only in retrospect does “Hilbert–Pólya” become a convenient name for the whole family of hopes.

The name is useful. It should not be mistaken for a lost theorem statement.

## 3. What self-adjointness would actually buy

A little precision protects the metaphor from becoming nonsense.

An operator is a rule acting on mathematical objects—vectors, functions, states. Certain special inputs can be returned as scalar multiples of themselves. The corresponding scalars are eigenvalues. In physical models, eigenvalues often represent measurable quantities such as energies or squared vibration frequencies.

A self-adjoint operator is an operator possessing a symmetry condition strong enough, under the appropriate analytic hypotheses, to force its spectrum to be real. This is why self-adjoint operators are central in quantum mechanics: observables require real measurement values.

The Hilbert–Pólya aspiration can therefore be phrased schematically:

> Construct, for reasons intrinsic to arithmetic or geometry, an operator \(H\) whose spectrum corresponds exactly to the zeros of \(\Xi(t)\), and prove that \(H\) is self-adjoint or that an equivalent positivity principle holds.

Then the spectral parameters would be real, which is exactly what the Riemann Hypothesis demands in the \(\Xi(t)\) formulation.

But several weaker achievements are not enough.

### A fitted spectrum is not an explanation

Once a real discrete sequence is already known, one can manufacture abstract operators having that sequence as spectrum. Such an operator may encode the data without explaining it. If its definition simply says, in effect, “put these numbers on the diagonal,” nothing has been gained.

A meaningful Hilbert–Pólya construction therefore needs more than spectral coincidence. It should be **independently motivated**—by geometry, dynamics, representation theory, arithmetic, or another structure that exists before the zeros are inserted by hand.

### A statistical match is not an exact spectrum

Two spectra can have the same local spacing statistics while having entirely different individual eigenvalues and different underlying operators. Random-matrix statistics can identify a universality class without identifying a unique Hamiltonian.

### Spectral language alone is not enough

Jeffrey Lagarias makes the strongest caution explicit in his Clay Mathematics Institute survey: a geometric or spectral interpretation of the zeta zeros **by itself** does not prove the Riemann Hypothesis; some appropriate positivity property still has to be established. [Jeffrey C. Lagarias, “The Riemann Hypothesis: Arithmetic and Geometry”](https://www.claymath.org/library/proceedings/cmip06.pdf)

This point is easy to lose because “self-adjoint spectrum” sounds almost synonymous with a proof. In practice, producing the relevant space, operator, domain, exact spectral identity, and positivity/self-adjointness is the problem—not a routine final check after the imaginative work is done.

The hard part of the instrument is not imagining its sound. It is proving what the instrument is made of.

## 4. Selberg: a nearby world where the analogy becomes mathematics

The spectral dream became more credible because mathematics discovered structures that looked uncannily like what the zeta problem seemed to want.

The most important early example is the **Selberg trace formula**.

For a compact hyperbolic surface, the Laplace operator has a genuine spectrum. The surface also has closed geodesics: periodic paths whose lengths form a geometric collection. Selberg's trace formula relates these two sides. In rough terms, a sum over spectral data can be rewritten using geometric data from closed geodesics. Jens Marklof's exposition describes the formula precisely as a bridge between the spectrum of the Laplacian and the lengths of closed geodesics. [Jens Marklof, “Selberg's Trace Formula: An Introduction”](https://people.maths.bris.ac.uk/~majm/bib/selberg.pdf)

The analogy with prime number theory is irresistible because Riemann's explicit formulas also connect two apparently different worlds:

| Prime-number world | Selberg world |
| --- | --- |
| prime numbers and their powers | primitive closed geodesics and their repetitions |
| zeros of a zeta function | spectral parameters of a Laplacian |
| explicit formula | trace formula |

Selberg also introduced a zeta function built from primitive closed geodesics, and its zeros are related to the Laplace spectrum. Here, unlike in the original Riemann problem, the geometric object and operator are visible.

This does **not** prove that ordinary primes are secretly geodesics on some undiscovered surface. It proves something subtler and more valuable: the architecture desired by Hilbert–Pólya is mathematically natural enough to occur elsewhere.

The unheard instrument has cousins.

That changes a fantasy into a legitimate research heuristic without turning the heuristic into a theorem.

## 5. Geometry wins in the function-field world

An even stronger analogy comes from zeta functions over finite fields.

For algebraic varieties over finite fields, there are zeta functions with Riemann-Hypothesis-like statements. Grothendieck's cohomological framework expresses these zeta functions using the action of the Frobenius map on cohomology. The relevant zeros and poles are governed by eigenvalues of Frobenius. Deligne's proof of the final Weil conjecture establishes the required absolute-value bounds on those eigenvalues. [Lagarias, “The Riemann Hypothesis: Arithmetic and Geometry”](https://www.claymath.org/library/proceedings/cmip06.pdf)

This is one of the most powerful reasons mathematicians continue to hope that the classical Riemann Hypothesis has a hidden geometric explanation. In a neighboring arithmetic universe, an RH-type theorem really is controlled by geometric objects, cohomology, and spectral data.

But the analogy must be stated carefully.

Frobenius is not simply the missing self-adjoint Hilbert-space operator for the ordinary zeta function. Deligne's argument is not “Hilbert–Pólya solved over finite fields” in the literal modern operator-theoretic sense. The function-field story uses algebraic geometry, cohomology, weights, and positivity/purity phenomena specific to that setting.

What it establishes is a precedent:

> **A zeta function can encode an arithmetic counting problem whose Riemann-Hypothesis-type zero constraint becomes intelligible through a deeper geometric action.**

That is far stronger than a metaphor. It is still not a transportable proof of the number-field case.

The missing object over the integers may resemble the function-field machinery. Or the resemblance may be misleading precisely where the two arithmetic worlds differ most.

## 6. Tea at the Institute: Montgomery meets Dyson

The event that transformed Hilbert–Pólya from an old spectral intuition into a modern mathematical-physics obsession happened over tea.

In 1972 Hugh Montgomery was studying correlations among high zeros of the zeta function. Assuming the Riemann Hypothesis in order to write the zeros on the critical line with real ordinates, he proved a restricted pair-correlation result and conjectured a fuller law describing how normalized zeros repel one another.

On April 6, 1972, while visiting the Institute for Advanced Study, Montgomery spoke with Freeman Dyson. Dyson recognized the formula immediately: it matched the pair-correlation behavior associated with eigenvalues of large random Hermitian—or, equivalently in the relevant symmetry class, unitary—matrices. The Institute for Advanced Study now marks that conversation as the beginning of a fifty-year fusion between number theory and random matrix theory. [Institute for Advanced Study, “50 Years of Number Theory and Random Matrix Theory”](https://www.ias.edu/math/events/50yntrmt); [IAS, “From Prime Numbers to Nuclear Physics and Beyond”](https://www.ias.edu/ideas/2013/primes-random-matrices)

Montgomery published his paper the following year. His full pair-correlation formula was a conjecture, not a proof of random-matrix behavior for all zero statistics. But the connection was startling because random Hermitian matrices were already used to model complex quantum spectra.

The zeros had not merely been called “notes.” Their local correlations now resembled a well-studied spectral universality class.

That was the moment the metaphor acquired teeth.

### What the GUE connection supports

It supports the claim that the local statistics of high Riemann zeros behave like eigenvalue statistics in the Gaussian Unitary Ensemble and related unitary random-matrix models. Later theory and computation strengthened this enormously.

### What it does not establish

It does not identify a particular self-adjoint operator whose exact eigenvalues are the zeta zeros.

It does not prove that such an operator is unique.

It does not prove the Riemann Hypothesis, because Montgomery's original setup for the pair-correlation conjecture already treats the zeros under RH in the form needed for the comparison.

It does not prove that the underlying “Riemann dynamics” must be a literal physical system.

Random-matrix universality is powerful precisely because many microscopically different systems share the same statistics. A universality class can tell us a great deal while refusing to tell us what the individual object is.

## 7. Odlyzko turns the analogy into an experiment

Random-matrix predictions became unusually testable because the zeta zeros can be computed at extraordinary heights.

Andrew Odlyzko performed large-scale computations of zeros and their statistics, including blocks very high on the critical line. Those computations found striking agreement with random-matrix predictions and became some of the best-known numerical evidence behind the number-theory/random-matrix connection. Odlyzko maintains tables of computed zeros and papers on their spacing and distribution. [Andrew Odlyzko, zeta-zero tables and papers](https://www-users.cse.umn.edu/~odlyzko/)

The empirical story matters, but its logic must remain clean.

Numerical verification can establish that every zero checked in a finite range lies where RH predicts. Statistical tests can establish that large samples resemble GUE predictions with remarkable accuracy. Neither operation reaches the universal quantifier “all zeros,” and neither converts a statistical resemblance into an exact spectral identity.

The distinction can be summarized sharply:

- **Verification:** every zero checked so far lies on the critical line.
- **Statistical evidence:** large collections of zero spacings agree impressively with random-matrix predictions.
- **Hilbert–Pólya:** an independently defined spectral structure explains the zeros and forces their location.

These are three different achievements.

As of 2026, the Clay Mathematics Institute's current problem page states that the first **10,000,000,000,000** nontrivial zeros have been checked. The problem remains open. [Clay Mathematics Institute, “Riemann Hypothesis”](https://www.claymath.org/millennium/Riemann-Hypothesis/)

Ten trillion correct notes do not prove that the unseen instrument exists. They do make any hypothetical wrong note very remote in the tested ordering.

## 8. Quantum chaos and the search for dynamics

Once the zero statistics looked quantum-mechanical, a more ambitious question followed. If the zeros are energy levels, what classical dynamics would quantize into them?

Quantum chaos studies quantum systems whose classical counterparts are chaotic. Semiclassical trace formulas connect quantum energy levels to classical periodic orbits. This suggested a tantalizing dictionary:

- Riemann zeros ↔ quantum energy levels;
- primes and prime powers ↔ primitive periodic orbits and repetitions;
- Riemann explicit formula ↔ semiclassical trace formula.

Michael Berry and Jonathan Keating developed this analogy in detail. In their 1999 *SIAM Review* article, they compared the zero-counting formula with semiclassical eigenvalue asymptotics, discussed the random-matrix statistics, and speculated that the unknown classical dynamics might be related to the Hamiltonian

\[
H=xp.
\]

[Michael V. Berry and Jonathan P. Keating, “The Riemann Zeros and Eigenvalue Asymptotics”](https://epubs.siam.org/doi/10.1137/S0036144598347497)

The proposal is famous because the simplest classical phase-space counting associated with \(xp\), after suitable restrictions or regularization, reproduces the leading smooth growth of the number of Riemann zeros. It is a beautiful clue.

It is not the instrument.

The bare \(xp\) dynamics is not a complete quantum system with the full Riemann zeros as its rigorously established spectrum. Boundary conditions, self-adjoint realizations, and the missing fluctuating information remain nontrivial. The smooth counting term says how many notes should have appeared by a given height; it does not specify the entire melody.

The difference between **eigenvalue asymptotics** and **exact eigenvalues** is exactly where many proposed solutions disappear.

## 9. Connes: the spectrum becomes absence

Alain Connes pushed the spectral idea in a direction far removed from the image of an ordinary vibrating drum.

In his work on noncommutative geometry, Connes constructed a framework using the adèle class space and interpreted the explicit formulas of number theory as a trace formula. His 1998 preprint, published in *Selecta Mathematica* in 1999, describes the critical zeros as an **absorption spectrum**, while hypothetical off-critical zeros would appear as resonances. The approach gives a geometric interpretation of the explicit formula on a noncommutative space and reduces RH to the validity of the required trace formula. [Alain Connes, “Trace Formula in Noncommutative Geometry and the Zeros of the Riemann Zeta Function”](https://alainconnes.org/publications/)

This is a profound spectral realization, but it should not be reported as “Connes found the Hilbert–Pólya operator and only a technicality remains.” His framework changes what “spectrum” and “geometry” look like. The zeros appear through an absorption mechanism rather than simply as the discrete positive spectrum of a familiar self-adjoint Hamiltonian.

The attraction of Connes's approach is that it tries to explain the **explicit formula itself**—the duality between primes and zeros—through a trace formula, instead of merely fitting an operator to a list of zero ordinates.

That is exactly the sort of explanatory depth a successful Hilbert–Pólya theory ought to have.

The remaining problem is exactly what Lagarias emphasizes: spectral interpretation must be accompanied by the positivity or trace-formula property strong enough to force RH. [Lagarias](https://www.claymath.org/library/proceedings/cmip06.pdf)

The instrument, if it exists, may not look like an instrument at all.

## 10. The candidate-operator trap

Hilbert–Pólya attracts proposed Hamiltonians because the payoff appears brutally simple: write down the operator, show it is self-adjoint, match the spectrum, collect the Millennium Prize.

The history of candidate operators shows why each verb in that sentence hides a major theorem.

In 2017 Carl Bender, Dorje Brody, and Markus Müller proposed a Hamiltonian related in its classical limit to \(2xp\). Their analysis was explicitly conditional: if the relevant metric construction could be made rigorous so that the operator became genuinely self-adjoint on the appropriate space, the result would imply RH. [Bender, Brody, and Müller, “Hamiltonian for the Zeros of the Riemann Zeta Function”](https://arxiv.org/abs/1608.03679)

Soon afterward Jean Bellissard published a comment arguing that the proposed proof strategy did not work. [Jean Bellissard, “Comment on ‘Hamiltonian for the Zeros of the Riemann Zeta Function’”](https://arxiv.org/abs/1704.02644)

The episode is useful not as a cautionary tale about one group but as a model of the entire difficulty. Candidate constructions must survive questions such as:

- What is the exact Hilbert space?
- What is the domain of the unbounded operator?
- Is the operator truly self-adjoint, not merely formally symmetric?
- Are all relevant eigenvalues present, with the correct multiplicities?
- Is the correspondence proved without assuming RH in disguised form?
- Does the construction explain the prime side of the explicit formula?
- Are boundary conditions mathematically justified rather than chosen to reproduce the target zeros?

A proposed formula can be ingenious and still leave the Hilbert–Pólya problem almost entirely intact.

The history is full of footprints. A footprint is not an animal.

## 11. What would count as finding the instrument?

The phrase “find the Hilbert–Pólya operator” is too vague to function as a research standard. A convincing realization would need several properties at once.

### 1. Independent definition

The operator or geometric system should arise from arithmetic, geometry, dynamics, representation theory, or another independently motivated construction. Its definition should not simply insert the known zeros as spectral data.

### 2. Exact correspondence

There must be a theorem identifying the relevant spectrum with **all** nontrivial zeros in the correct normalization, including multiplicities and any required symmetries.

Matching the average zero density is not enough. Matching GUE spacing statistics is not enough. Matching the first billion eigenvalues numerically would still not be enough.

### 3. Genuine spectral reality or positivity

The construction must possess the self-adjointness, skew-adjointness after the proper shift, or equivalent positivity property that forces the zero parameters into the required real locus.

This is where the Riemann Hypothesis is actually won.

### 4. An explanation of primes

The deepest versions of the program should explain why the explicit formula connects primes to zeros. A trace formula in which prime powers arise naturally as periodic-orbit or geometric terms would explain vastly more than an operator whose spectrum merely happens to be correct.

### 5. No smuggled hypothesis

The construction cannot begin by assuming the zeros are on the critical line, define an operator from their real ordinates, and then cite self-adjointness as a proof. Nor can a boundary condition be justified solely because it selects the desired zeros.

This is the logical hygiene test for every spectacular “Riemann Hamiltonian” announcement.

## 12. An evidence ledger

The century-long accumulation of spectral evidence is impressive precisely when each item is allowed to say only what it says.

| Development | What it genuinely supports | What it does **not** establish |
| --- | --- | --- |
| Hilbert/Hellinger and Pólya/Landau stories | spectral intuition existed early in the twentieth century | a published joint conjecture or candidate operator |
| Selberg trace formula | a real setting where spectra and prime-like closed geodesics are linked by a trace formula | that ordinary primes are closed geodesics of an unknown surface |
| function-field RH | deep geometric/cohomological structure can force RH-type zero constraints | a self-adjoint operator for the classical Riemann zeta function |
| Montgomery–Dyson | zero correlations match unitary random-matrix spectral statistics | exact eigenvalues of a unique Hamiltonian; RH itself |
| Odlyzko computations | enormous finite samples support RH and random-matrix predictions | a proof for all zeros or existence of the operator |
| Berry–Keating \(xp\) | semiclassical dynamics can reproduce important zero-counting structure and suggests a chaotic system | the full Riemann spectrum as a rigorously defined self-adjoint quantum Hamiltonian |
| Connes's noncommutative geometry | explicit formulas admit a sophisticated spectral/trace-formula interpretation | completion of the positivity/trace argument needed for RH |
| proposed Hamiltonians | useful laboratories for identifying necessary operator-theoretic conditions | proof until domain, spectrum, self-adjointness, and completeness are rigorously established |

The table explains why Hilbert–Pólya can simultaneously look extraordinarily well motivated and remain extraordinarily incomplete.

There is no contradiction between those judgments.

## 13. Why the metaphor keeps returning

The musical image survives because it compresses an unusually complicated research program into a sensory question.

Prime numbers appear irregular. Riemann turns their fluctuations into zeros. The zeros display statistical repulsion resembling quantum spectra. Trace formulas elsewhere pair spectral levels with geometric periodic structures. Function-field analogues reveal cohomological machinery behind RH-type statements. Physics offers a language of Hamiltonians and energy levels. The pieces line up just well enough that “there must be an instrument” feels almost compulsory.

But mathematics has learned an important lesson from universality: **many different mechanisms can sing with the same statistical accent**.

Random matrices are powerful partly because microscopic details wash out. A GUE law does not identify the microscopic system. It classifies behavior shared across many systems. The same fact that makes the Montgomery–Dyson connection profound makes it inadequate as an existence proof for a unique Riemann Hamiltonian.

The metaphor also survives because it encodes a philosophical preference. A spectral explanation would turn an arithmetic statement into a structural necessity. Instead of proving, by intricate inequalities, that infinitely many complex zeros all happen to stay on one line, one would discover an object for which leaving the line is impossible for the same reason a self-adjoint Hamiltonian cannot have a nonreal energy level.

That would not merely settle RH. It would answer a more satisfying question: **why should RH have been true in the first place?**

The desire for that kind of explanation is legitimate. It is not evidence that the desired explanation exists.

## 14. Where the story stands

As of 2026, the Riemann Hypothesis remains one of the unsolved Clay Millennium Prize Problems. Clay's current page reports verification of the first \(10^{13}\) nontrivial zeros. No accepted counterexample is known. No accepted proof is known. No accepted Hilbert–Pólya operator is known. [Clay Mathematics Institute](https://www.claymath.org/millennium/Riemann-Hypothesis/)

The spectral program nevertheless occupies a stronger position than it did in Pólya's remembered conversation with Landau.

In the 1910s the idea was a physical reason one might hope for.

After Selberg it had a rigorous geometric analogue.

After the Weil conjectures it had an arithmetic cousin in which geometry really controlled RH-type zeros.

After Montgomery and Dyson it had a statistical fingerprint associated with quantum spectra.

After Odlyzko that fingerprint survived enormous numerical tests.

After Berry–Keating, Connes, and many later constructions, researchers had increasingly precise pictures of what any hidden dynamics or trace formula would need to reproduce.

And still the decisive implication has not arrived.

This is not a story of steady progress toward an inevitable operator. It is a story of **converging analogies whose common source remains unknown**.

## Conclusion: the silence behind the wall

The literary temptation is to end by promising that someday the wall will open and the instrument will be found.

Mathematics does not owe the story that ending.

Perhaps there is a natural self-adjoint operator whose spectrum is exactly the Riemann zeros. Perhaps the correct object is geometric but not recognizably Hamiltonian. Perhaps noncommutative geometry or a future cohomology theory will make the explicit formula into a genuine trace formula. Perhaps RH will be proved by a route that makes the Hilbert–Pólya dream look prophetic only in hindsight. It is even possible that the spectral program will remain an extraordinarily productive analogy without ever becoming the proof.

What survives every outcome is the quality of the question.

Riemann taught number theorists to hear prime-number fluctuations through zeros. Hilbert and Pólya are remembered for asking whether those zeros themselves might be heard as a spectrum. Selberg showed that arithmetic-looking zeta functions and genuine spectra can coexist. Montgomery and Dyson discovered that the zeros carry the statistical accent of quantum eigenvalues. Modern work has kept refining the possible shape of the missing mechanism.

Yet no one has identified what is vibrating.

That absence is not an embarrassment to be covered with metaphor. It is the central fact.

The Hilbert–Pólya idea remains compelling because the notes are there, the spectral resemblances are real, and the mathematical cousins are profound. It remains a conjectural program because **an unheard instrument is still unheard**.

## Sources

- Michael V. Berry and Jonathan P. Keating. “The Riemann Zeros and Eigenvalue Asymptotics.” *SIAM Review* 41, no. 2 (1999): 236–266. https://doi.org/10.1137/S0036144598347497
- Carl M. Bender, Dorje C. Brody, and Markus P. Müller. “Hamiltonian for the Zeros of the Riemann Zeta Function.” *Physical Review Letters* 118 (2017): 130201. https://arxiv.org/abs/1608.03679
- Jean Bellissard. “Comment on ‘Hamiltonian for the Zeros of the Riemann Zeta Function.’” 2017. https://arxiv.org/abs/1704.02644
- Enrico Bombieri. “The Riemann Hypothesis.” In *The Millennium Prize Problems*. Clay Mathematics Institute / American Mathematical Society. https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf
- Alain Connes. “Trace Formula in Noncommutative Geometry and the Zeros of the Riemann Zeta Function.” *Selecta Mathematica* 5 (1999): 29–106. https://doi.org/10.1007/s000290050042
- Jack P. Greene. *[Not used; intentionally omitted from this mathematical article.]*
- Jeffrey C. Lagarias. “The Riemann Hypothesis: Arithmetic and Geometry.” *Clay Mathematics Proceedings* 6 (2006): 127–141. https://www.claymath.org/library/proceedings/cmip06.pdf
- Jens Marklof. “Selberg's Trace Formula: An Introduction.” Lecture notes. https://people.maths.bris.ac.uk/~majm/bib/selberg.pdf
- Hugh L. Montgomery. “The Pair Correlation of Zeros of the Zeta Function.” In *Analytic Number Theory*, Proceedings of Symposia in Pure Mathematics 24 (1973): 181–193.
- Andrew M. Odlyzko. “Correspondence about the Hilbert-Polya Conjecture,” zeta-zero tables, and related papers. https://www-users.cse.umn.edu/~odlyzko/
- Bernhard Riemann. “On the Number of Primes Less Than a Given Magnitude” (1859), manuscript and English translation hosted by the Clay Mathematics Institute. https://www.claymath.org/collections/riemanns-1859-manuscript/
- André Weil. Commentary on “Sur les ‘formules explicites’ de la théorie des nombres premiers,” *Œuvres scientifiques / Collected Papers*, vol. II, historical source for the Hellinger–Hilbert recollection.
- Institute for Advanced Study. “50 Years of Number Theory and Random Matrix Theory.” https://www.ias.edu/math/events/50yntrmt
- Clay Mathematics Institute. “Riemann Hypothesis.” https://www.claymath.org/millennium/Riemann-Hypothesis/
