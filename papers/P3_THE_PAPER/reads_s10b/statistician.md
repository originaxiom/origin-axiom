# Hostile review — lens: statistician / philosopher of science hostile to numerology

Target: `<home>/origin-axiom/papers/P3_THE_PAPER/main.tex`, working tree of 2026-09-16 (1671 lines).
Scope of this lens: base rates and their populations/orderings, look-elsewhere effects,
pre-registration, the meaning of "generic"/"forced", selection effects in choosing the object,
whether "parameter-free" is well-defined, whether the three-way ledger is a real partition,
unfalsifiable negatives, and whether the falsifiers are executable by an outsider.

---

## FATAL

### F1. "Parameter-free" is used as a category label for items the paper itself says are conditional

> \emph{Parameter-free, and had}: the object up to one bit and its selection as a minimiser; the invariant trace field $\Q(\sqrt{-3})$ and the $2T$ door; $E_6$ and the $27$ by McKay; the termination of the breaking chain; the direction of hypercharge and the $\Z_6$ global form (given the colour frame and the shaping the ledger lists); three structural copies of the Standard-Model content on the closings, vector-like...
(line 1432, "The ledger in three columns")

versus, a few paragraphs later:

> This is not a parameter-free Standard Model, and it is not a theory of everything.
(line 1439)

and, in the abstract itself:

> and --- given the colour frame and the Standard-Model shaping that the ledger lists as inputs --- the global form $[\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)]/\Z_6$ of the Standard-Model factor
(lines 55–56)

**Why it fails.** The paper is entitled to deny being "parameter-free" (it does so explicitly at line 1439) and is also entitled to say that the global form is derived only *given* the colour frame and the SM shaping (it says so in the abstract). What it cannot coherently do is then label the very same conditional item — "the direction of hypercharge and the $\Z_6$ global form (given the colour frame and the shaping the ledger lists)" — under a column header reading "**Parameter-free**, and had." The parenthetical inside the column entry concedes the item is conditional on two named inputs in the very sentence that calls it parameter-free. This is not a stylistic quibble: "parameter-free" is exactly the notion this lens is asked to test for well-definedness, and the paper uses it in two incompatible senses within four pages of the same section — once as "no free parameter was consumed" (the column header) and once, correctly, as "conditional on listed inputs" (the parenthetical, and the wall section's denial). A referee reading only the column header would come away with a stronger claim than the paper is willing to defend three paragraphs later.

**Minimal repair.** Drop "Parameter-free" as the column's name. Call it "Forced, given the ledger's priced inputs, and had" — which is exactly what the parenthetical already says — and reserve "parameter-free" (if used at all) for items that genuinely consume no listed input (e.g. $E_6$ and the $27$ by McKay, the termination theorem's mathematical content apart from its chirality-datum premise).

### F2. A named falsifier points at a computation the paper itself says cannot be re-run from a clean checkout

Falsifier 8:

> \textbf{Exhibit a non-zero index, with its four identities intact,...on an unprotected twist sector of a chiral cover of the object.} This too is an upgrade trigger rather than a falsifier: it would move the chirality bit from \emph{withheld at every computed sector} to \emph{supplied on the tower}, and \S\ref{sec:chirality} names where to look (the multi-cusped chiral covers).
(lines 1361–1366)

But the body text, about the multi-cusped chiral covers specifically, says:

> The index on several boundary tori has since been derived from the same pair sequence and reported zero on the $54$ multi-cusped chiral covers, in a run whose scripts are not yet reproducible from a clean checkout; we report it as reported.
(line 1025)

**Why it fails.** The PROMPT for this review asks explicitly whether the paper's falsifiers are executable by an outsider. Falsifier 8 sends the reader to exactly the one computation the paper itself flags, in its own body text, as not currently reproducible from a clean checkout. An outside reader who wants to check whether the falsifier has already fired (i.e. whether a non-zero index already exists somewhere on the 54 multi-cusped covers) cannot verify the paper's own "reported zero" claim, let alone go further and search for a non-zero case, without first reconstructing an un-reproducible pipeline. This is a fatal executability gap in the one section whose entire purpose is to hand a critic a computation they can run.

**Minimal repair.** Either (a) make the multi-cusped-cover script reproducible from a clean checkout before publication and cite that fact next to falsifier 8, or (b) add one clause to falsifier 8 itself: "at present this computation is not independently re-runnable from a clean checkout (see the multi-cusped-cover note in §chirality); until it is, this falsifier is stated but not executable by an outside reader."

### F3. The paper's own verification machinery has already certified a false claim as "settled," with no error-rate accounting for the rest

> Two limits of that machinery have already fired and we state them: the check's control proves only that a claim pointed at a non-existent record is reported, not that no claim was left off the list, whose completeness is editorial; and a lock is traceability, not re-derivation --- in one recorded case a lock pinned a family-wide claim that was later withdrawn.
(lines 1463–1465, Appendix)

cross-referenced to the actual incident:

> An earlier draft strengthened this to a family-wide statement over the object's trace-field family. That strengthening was withdrawn when the count behind it proved orientation-blind: by the orientation-aware test, 38 of the family's 112 members are amphichiral, not all.
(footnote, line 1044, §observer)

**Why it fails.** "Settled" and "lock" are the paper's own labels for its highest evidentiary tier, used on roughly 54 rows / 75 claim–record pairs in the provenance appendix, and repeatedly invoked in the body ("theorem," "verified," "certified") to close off further scrutiny. The appendix concedes, in its own limitations paragraph, that this exact machinery has at least once certified as locked a claim that was in fact false (the family-wide amphichirality statement, which survived at least one full drafting pass before an orientation-aware re-test caught it). A statistician's question is immediate and is not answered anywhere in the paper: what is the estimated false-"settled" rate over the remaining rows, given a demonstrated non-zero rate on the one occasion an adversarial re-test was actually run? The paper reports the numerator (one caught error) with no visible denominator (how many rows have ever been adversarially re-tested, as opposed to computed once and locked). Without that denominator, "settled" functions rhetorically as "we believe this," not as evidence with a known error rate — precisely the numerology-adjacent failure mode this paper otherwise polices hard.

**Minimal repair.** Add one sentence to the appendix's limitations paragraph stating how many of the 54 settled rows have undergone an independent second derivation or adversarial re-test (as the amphichirality row eventually did) versus how many rest on a single computation that was locked and never revisited. If that number is not known, say so explicitly, the way the paper says so for other open questions.

---

## SERIOUS

### S1. Census order is treated as if it were a random or representative sample; the object sits at its extreme

> The construction begins with a surjection $\pi_1(m004) \twoheadrightarrow 2T \cong \mathrm{SL}(2,3)$... over the first $400$ one-cusped orientable census manifolds in census order, every homomorphism to $\mathrm{SL}(2,3)$ was enumerated... $145$ of $400$ ($36.25\%$) admit such a surjection
(lines 146–150)

> Extending the count above to the first $5000$ one-cusped census manifolds, $1696$ ($33.92\%$) admit the surjection.
(line 175)

**Why it fails.** SnapPy's census order enumerates manifolds by increasing triangulation complexity (roughly, increasing volume), which is a computational artifact, not a probability sample from any population of "hyperbolic 3-manifolds" — no such uniform measure exists, and the paper never asserts one. $m004$ is not a typical draw from "the first 400" or "the first 5000": it is (with its sibling $m003$) the minimal-volume one-cusped orientable hyperbolic 3-manifold, i.e. it sits at the very front edge of exactly the ordering the paper samples from. Comparing an object at the extreme of an ordering to "the first $N$ in that ordering" is not the same statistical operation as comparing a randomly chosen manifold to the census; low-complexity manifolds are known to carry more symmetry and more special arithmetic on average, for reasons that have nothing to do with the object's genesis story. The paper's own numbers hint at this: the surjection rate falls from 36.25% at $n=400$ to 33.92% at $n=5000$, a drift with the very ordering the paper is using as its measuring stick, and this drift is reported without comment on what it implies about extrapolating "roughly one in three" as a stable population rate. The word "probability" is also used loosely for a tautology elsewhere ("conditioned on the appearance of a single ADE label, the probability that it 'recurs' across the others is $1$," line 133) in a way that borrows statistical vocabulary the paper has not earned for its census claims specifically.

**Minimal repair.** State explicitly, once, that census order is an enumeration by complexity, not a probability sample; name $m004$'s own rank in that ordering (it is at or near rank 1); and either (a) recompute the base rate over a complexity-matched stratum, or (b) add one sentence acknowledging that the reported percentage is a property of a specific, non-random enumeration and may not equal the rate in any well-defined larger population.

### S2. "Pre-registered" is invoked repeatedly as an evidentiary shield without ever specifying the registration mechanism

Representative instances:

> Four independent routes were pre-registered to test whether the quadratic field carrying the exceptional algebra could be reached from the combinatorial data alone
(lines 396–397)

> a look-elsewhere probability of $16.4\%$, which is not rare; ... failure of pre-commitment, the pair having been produced by the scan rather than named before it
(lines 806–809)

> formula and domain were pre-registered before evaluation
(line 939)

**Why it fails.** In the field this vocabulary is borrowed from (clinical trials, pre-registered replications), "pre-registered" carries force only because a party independent of the analyst timestamps and locks the hypothesis before the data are examined. Here, every registration, seal and lock is made, held and later graded by the same team, inside a repository that team alone controls — and the same document independently documents extensive multi-draft revision of numbers it once asserted as settled (the two-implementation disagreement at line 151, the retracted "$16\sigma$"/"within $1\sigma$" claim at line 1281, the amphichirality retraction at line 1044). None of this means the internal pre-registrations are fabricated after the fact — the paper's revision culture argues the opposite, that errors get caught — but the paper never states *how* a reader could distinguish a genuine pre-registration from a post-hoc claim of one (a commit hash, an immutable log, a third-party timestamp). Until it does, "pre-registered" here means "we say we wrote it down first, in a system we control," which is meaningfully weaker than the term signals to a reader trained on its normal usage, and the paper leans on that stronger reading to dismiss look-elsewhere concerns.

**Minimal repair.** Add one sentence, cited at the first use of "pre-registered," defining the operational guarantee (e.g. "committed to the public repository at a named, dated commit before the evaluating script was ever executed against it") and note that the guarantee is self-administered, not third-party-witnessed.

### S3. The selection effect in choosing the object itself is conceded historically but never priced

> We did not begin with this discipline. The programme applied base-rate reasoning to numerical coincidences long before it applied the same test to its flagship structural claim; when the test was finally run, the structure came back generic.
(lines 178–181, "On our own history")

**Why it fails.** This passage is honest, and it is also the paper's own admission of exactly the selection-effect problem this lens is asked to probe: the genericity test in §generic answers "how common is this behaviour among manifolds like $m004$, once $m004$ has already been chosen as the object of study" — it never asks, and the passage above shows the authors know it never asks, "how many other candidate objects, knots, groups or lattices were examined and quietly abandoned before $m004$'s $E_6$ recurrence was written up as the flagship result?" That second question is the more basic file-drawer question about object choice, prior to and independent of the entry-point base rate the paper does compute. Nowhere in §axioms or §ledger — both of which otherwise price every input they can find, including ones as diffuse as "the decision to look for structure in a mathematical object at all" (A0, line 194) — is this object-selection effect priced, bounded, or even flagged as unpriceable the way A0 is.

**Minimal repair.** Extend the "On our own history" scope note with one sentence stating, even approximately, how many other candidate objects were examined before $m004$ became the flagship, or explicitly add this as an unpriced item alongside A0 in §axioms, rather than leaving it implicit in a historical aside.

### S4. "Generic" is used in two unrelated technical senses without disambiguation

Population base-rate sense (the sense that governs all of §generic):

> roughly one in three admits the surjection... (abstract, line 44)

versus the algebraic-geometry generic-point sense:

> the most generic non-trivial second measurement lands on $\mathfrak{su}(3) \oplus \mathfrak{su}(2) \oplus \mathfrak{u}(1)^3$ exactly, the $A_2{+}A_1$ Levi, skipping $\mathrm{SU}(5)$ over $\R$
(line 602–604)

**Why it fails.** Fifty lines earlier the paper has spent an entire section teaching the reader to distrust the word "generic" as smuggled evidence ("Programmes of this kind typically observe that $E_6$ recurs... and treat the coincidence as evidence. It is not," line 129). By §middle the same word reappears meaning "true on a Zariski-dense open subset of a variety" — an entirely different, purely mathematical notion with no population or evidential content at all. A reader primed by §generic's rhetorical training (be suspicious of "generic") has no signal that this second occurrence is a harmless technical term, not a second instance of the very move the paper spent pages warning against. This is the textbook shape of an equivocation risk: same word, load-bearing in one register, innocuous in another, never flagged.

**Minimal repair.** Footnote the first algebraic-geometric use of "generic" (line ~602) to state explicitly that this is the Zariski/measure-theoretic sense, unrelated to the population base rates of §generic.

### S5. The "believed unreachable" column mixes universal no-gos with object-specific theorems under one label

> \emph{Believed unreachable, each by a stated theorem}: a Standard-Model ratio among the object's periods and regulators (exhaustive at stated bounds); the hypercharge normalisation from the anomaly equations alone (homogeneity); the scale (Mostow); the modular period from the object's own algebra (traciality); a chiral spectrum from the geometric holonomy on any one-cusped manifold (injectivity)... or from the cyclic tower (the two conjugations)...
(line 1432, "The ledger in three columns")

**Why it fails.** The paper itself states elsewhere, correctly, that the hypercharge-normalisation no-go "holds for any $\mathrm{U}(1)$ charge assignment in any theory, so it is not a limitation peculiar to this construction" (line 838–839) and that Mostow rigidity is a generic geometric fact "and the reason §withheld can state the scale row as a theorem rather than a gap" (line 1302–1303). These are true, general facts that would apply to any object of the relevant type whatsoever and say nothing about $m004$ specifically. They are listed in the very same column, under the very same heading, as genuinely hard-won, object-specific results such as the vanishing of the index on the cyclic tower (which needed two theorems about this Alexander module specifically). A reader skimming the three-column summary — which the paper itself recommends as the place "the reader who wants the whole boundary in one place can have it" (line 1432) — has no way to tell, from the column alone, which entries are substantive negative results about this object and which are vacuously true of every construction of the kind, and so the column's length overstates how much the object-specific investigation actually closed off.

**Minimal repair.** Mark the vacuous/universal entries (homogeneity, Mostow, traciality) with a distinct symbol or a trailing clause ("— true of any such construction, not specific to the object") so the column separates "impossible for anyone" from "impossible for this object, and here is why."

---

## MINOR

### M1. The abstract rounds a statistic the body insists on stating exactly

> roughly one in three admits the surjection
(abstract, line 44)

versus the body's own stated discipline:

> That count is not distinctive, and we give it exactly rather than approximately: ... $145$ of $400$ ($36.25\%$)
(line 146–149)

**Why it fails.** Minor, but telling for a paper whose entire rhetorical stance is "we give exact counts, not vibes": the one sentence most readers will actually read (the abstract) reverts to the loose "roughly one in three" the body explicitly rejects as a lesser standard.

**Minimal repair.** Abstract: "about a third (36.25% at $n=400$, 33.92% at $n=5000$) admits the surjection."

### M2. The 16.4% look-elsewhere figure is asserted without its reference model

> a look-elsewhere probability of $16.4\%$, which is not rare
(line 807)

**Why it fails.** No null model, trial count definition, or independence assumption is given in the text for how 16.4% was computed over "352 pairs" that are not obviously independent (multiple periods derived from the same object, multiple targets related by RG running are correlated). The number cannot be audited from the paper alone.

**Minimal repair.** Add a one-clause definition, e.g. "(the binomial tail probability of at least one two-significant-figure match among 352 comparisons under the stated null, treating [X] as the unit of independence)."

### M3. Significance-testing vocabulary is borrowed for a curve-fit deviation, not a hypothesis test

> against the experimental error it is off by about fifty standard deviations
(line 1283)

**Why it fails.** This is a deviation of a theoretical curve (already known, by two cited precedents, to fail at this order) from a measured central value, expressed in units of the *experimental* error bar alone — not a formal significance test with a defined null and alternative. "Fifty standard deviations" reads to most audiences as an extraordinarily strong rejection, but the miss is neither surprising nor informative beyond what Amaldi–de Boer–Fürstenau and Langacker–Luo already established; the σ-language imports more rhetorical weight than the comparison carries.

**Minimal repair.** "off from the measured value by about fifty times the experimental uncertainty, on a curve already known by cited precedent to miss at this scale."

---

## (a) The single strongest objection, and does the paper already answer it?

The strongest objection is that this paper's entire evidentiary apparatus — its base rates, its "pre-registrations," its "sealed" menus, its "settled"/"lock" verdicts — is self-administered: computed, sealed, graded and locked by the same team, inside a repository that team alone controls, with no independent auditor at any stage. That would be a survivable design if the self-administered process had a known error rate near zero, but the paper's own appendix discloses that it does not: the verification machinery has already certified at least one claim (the family-wide amphichirality statement) as locked and settled when it was false, and the paper gives no basis anywhere for estimating what fraction of the remaining ~54 settled rows might carry the same kind of error, since we are only ever told about the ones that were caught. Does the paper already answer this? Partially, and better than most papers of this kind would: it is unusually forthcoming about its own retractions, states plainly that "all verification reported here is internal... no external review or endorsement is claimed" (abstract, closing sentence), and even names the specific limitation in its appendix ("a lock is traceability, not re-derivation... in one recorded case a lock pinned a family-wide claim that was later withdrawn," line 1464). That transparency is real credit. But disclosing that the auditing process is fallible is not the same as bounding how fallible it is, and a document this dependent on internally-computed numerical claims needs either an estimated error rate, a stated audit-coverage fraction, or a concrete plan for external re-derivation — none of which is offered. The objection is named but not closed.

## (b) What does the paper actually prove, in one sentence — and does the abstract say the same thing?

What a referee would say the paper actually proves: *given a stipulated chain of un-derived choices (three axioms before the object, one after, plus several finite inputs the paper's own ledger names — the colour frame, the Standard-Model shaping, the real-structure closing, and others), a body of internally-verified computation on the figure-eight knot complement's arithmetic and the $E_6$ algebra McKay hands it reproduces the classical anomaly-driven hypercharge and $\mathrm{SU}(5)$-global-form computation, while every bounded, internally-run search for an additional Standard-Model value in the same object's own numbers comes back empty.* That is a negative result about this object's numerical content, dressed in the vocabulary of a positive derivation. Does the abstract say the same thing? Substantially yes, and more honestly than most papers making comparable claims would manage — the arena/content split, the explicit withholding of values, and the withheld chirality bit are all stated up front. But the abstract's framing — "we ask what gauge structure can be extracted... without importing a value" — undersells, in its very first sentence, how much *is* imported before the "forced" part of the computation ever starts: six externally-supplied discrete inputs by the ledger's own count, not values but genuine unforced choices, are spent before the anomaly conditions do their allegedly value-free work. A referee would tighten the abstract's opening claim to something closer to: "after several stipulated and un-derived choices are fixed, the remaining computation is forced and adds no new numerical value" — a real result, but visibly narrower than "without importing a value" suggests to a reader who has not yet reached §ledger.
