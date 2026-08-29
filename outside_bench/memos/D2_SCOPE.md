# THE D2 SCOPE QUESTION, MEASURED — the two readings are not symmetric: the variable reading is refuted by a law banked before the run, and the ladder is not post-hoc
## (outside bench memo 130, 2026-08-29; certificate `certificates/d2_scope.py`, GREEN; decision sheet `THE_D2_DECISION.md`; the owner's "let's elaborate D2 decision options")

B1197 returned SPLIT on the D2 gate and routed the scope choice to the
owner, saying honestly that *"both readings are defensible and the run
cannot choose between them."* This cell does not choose either — it
**measures** them on cc's own banked data, so the decision rests on
numbers.

- **Reproduction, and an error of mine filed.** cc's **15** violations
  reproduce exactly under cc's own rule. My first recount gave **30**
  because I dropped cc's **1e-9 tolerance**; the sub-tolerance
  "increases" are the mirror ties. **cc's tolerance is load-bearing and
  correct; I was wrong**, and this is recorded rather than quietly fixed.
- **S1 — the effective sample halves.** B289's sign law gives each mirror
  pair equal volume and equal |CS|, so the **78 closings are 39 distinct
  (Vol, |CS|) points**. cc's 78 is right as closings; a fair null needs
  the 39.
- **S3 — the global relation is WEAK.** 15 violations of 38 against a
  20,000-shuffle null of **19.0 ± 1.8** (z = −2.18, P = 0.026);
  **Kendall τ = −0.174**. A faint tendency — so the two readings are far
  apart, and the trajectory restriction is not a technicality.
- **S4 — coherence is not asymptotic.** Near-cusp restriction never
  cleans the census (Vol ≥ 1.95 still leaves 5 of 13). The payable
  reading cannot be upgraded to "asymptotically coherent for all
  families".
- **S5 — |CS| is not a FUNCTION of Vol.** Seven closings inside a volume
  window of width **0.005149** carry |CS| spanning **0.143940** — **28×**
  faster variation — at the near-cusp end. The condition *"the same clock
  up to monotone reparameterization"* requires a function, so the
  variable reading fails **single-valuedness**, strictly stronger than
  non-monotonicity, with nothing weaker to retreat to.
- **S5b — and the one-line version predates the run.** B289's sign law —
  **B1197's own positive control, 156/156** — gives CS(p,−q) = −CS(p,q)
  at the **same volume**, so one volume carries two opposite CS values
  for all 39 pairs. **Signed CS was never a function of Vol.** |CS| is
  already the repair; S5 kills the repair. **The variable reading is
  refuted twice over, by cc's own control.**
- **S6 — the ladder is not post-hoc.** B289 independently names the (1,n)
  family *the scale ladder* (CS one sign, CS(1,−n) = −CS(1,n), |CS| → 0
  toward the amphichiral origin), and the weld book's **addendum 2,
  written before the run**, preregistered exactly that test with the
  census as the extension. **Restricting to it is a scope choice, not
  selection of the passing subset.**

**WHAT THIS CHANGES.** B1197 left the readings symmetric. They are not:
the **variable** reading is refuted more strongly than reported and by
banked law; the **trajectory** reading is cleaner than reported and was
preregistered. So the owner's choice is not *"which of two
equally-supported readings"* — it is the single question **"is a clock
identified along one realized history, or between two variables on the
space of possible histories?"** The second is dead either way.

**The bench's recommendation** (labeled as such, in
`THE_D2_DECISION.md` §4): **Option A — pay LEAP-1 with the scope premise
written in as its own priced line and a refuter armed**, the shape SP-1
was given. Not because A is convenient, but because **declining or
holding would take its authority from a test that nothing could have
passed.** Option D (reformulate the variable) is **closed** by S5b, and
Option C (hold) is now a decision to hold *forever*, since no further run
can break the tie — which should be recorded as such rather than as
"pending".

**What A does not buy:** LEAP-1's original cost is untouched — no banked
computation connects the object's tick to a cosmological clock, and B721's
tracial result still forces an imported external weight. **A pays a leap;
it does not discharge one.**

**Fences.** Geometry and counts only, all read from banked data; no
measured value enters and no clock identification is asserted here.
Gate 5 untouched.

### ADDENDUM 1 (2026-08-29) — cc's sharper witness adopted, and the timestamp verified
- **S5c, added to the certificate:** the **steepest pair** in the census
  is **(1,7) vs (2,7)** — ΔVol = **0.000264476**, Δ|CS| = **0.143204579**,
  a ratio of **541.5×**. Two closings at essentially the same volume carry
  |CS| differing by a factor of three. **cc's witness**, re-derived here
  and credited; it is sharper than this memo's original 28× window figure,
  which stands but is no longer the best available.
- **S6 strengthened by a verified timestamp:** weld-book addendum 2 was
  committed **2026-08-28 13:30:33 UTC**; B1197 ran **2026-08-28 19:49:17
  UTC** — the trajectory statement **predates the run by 6h 19m**. So the
  ladder reading is the **original** form of the condition, with the
  census proposed as its "full check", not a retrofit. cc's observation,
  verified from git here.
- **A framing correction to this memo's own argument.** This memo argued
  **eliminatively** (the variable reading was never satisfiable, so do not
  decline on it). cc is right that this establishes only that *the gate
  returned nothing* — **it is not a licence to pay.** The deciding
  argument is **positive** and belongs in the record: a cosmological clock
  parameterizes **one realized history** by construction, so requiring
  single-valuedness across all Dehn closings is a **category error**.
  Adopted as the ground for SCOPE-1a.
This addendum is the only mutation.
