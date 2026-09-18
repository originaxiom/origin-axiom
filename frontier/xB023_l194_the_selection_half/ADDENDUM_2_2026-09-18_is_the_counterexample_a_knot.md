# xB023 ADDENDUM 2 (2026-09-18) — SEALED BEFORE THE CELL EXISTS: is `o10_143849` actually a knot complement in S³, and what does §3's prediction look like once the proxy is replaced by the real predicate?

**Beyond the seal.** `PREREGISTRATION.md` untouched (`277542e7…`). **Addendum 1 untouched** — it is
banked at `385c286d` with its refutation standing. This addendum does **not** revise it; it closes the
one line Addendum 1 §5 explicitly left open and named as decisive for what the refutation is *of*.

## 0. THE RESIDUE, QUOTED FROM THE THING IT CAME FROM

> **A residue worth one line, and not more:** `o10_143849` has `H₁ ≅ ℤ` — **necessary, not
> sufficient** for being a knot complement in S³. Whether it actually is one is **unchecked**, and if
> it is not, Corollary 2.5 never applied to it and the refutation is of this seat's inference rather
> than of any reading of the paper.

## 1. WHY IT IS NOW DECIDABLE RATHER THAN MERELY TESTABLE

SnapPy 3.3.2's `CensusKnots` is documented as

> *"the knot exteriors which can be triangulated by **at most 10 ideal tetrahedra**"*

— Callahan–Dean–Weeks, Champanerkar–Kofman–Patterson, Dunfield, Li — **3116 of them**, distributed
`{2:1, 3:2, 4:4, 5:22, 6:43, 7:129, 8:301, 9:765, 10:1849}`. **It is a complete tabulation at each
tetrahedron count in that range, not a sample.**

`o10_143849` **is a 10-tetrahedron manifold.** Therefore:

> **If it is a knot complement in S³, it MUST appear in `CensusKnots`. Membership is decisive in both
> directions**, modulo the correctness of that published tabulation — which is an external
> dependence and is named as one here, not hidden.

**This is why the residue is worth doing now and was not worth doing yesterday:** the instrument that
makes it a decision rather than a guess is the completeness claim, and that claim was not checked
until this addendum checked it.

## 2. THE CELLS — declared before `knot_or_not.py` exists

**N1 — the banked datum, re-derived, not recalled.** Addendum 1's counterexample is re-measured from
scratch: cusps, orientability, full symmetry group, amphicheirality, `H₁`, volume, and the CS class
at 30 digits through `ManifoldHP` on the isometry signature.
*Prediction:* **exact agreement** with Addendum 1 — 1 cusp, amphicheiral, `H₁ ≅ ℤ`, class **quarter**.
*Kill:* any disagreement means Addendum 1's table is wrong and **that** becomes the headline.

**N2 — THE DECISION.** Is `o10_143849 ∈ CensusKnots`? And `identify()` across all four censuses
(`OrientableCuspedCensus`, `LinkExteriors`, `CensusKnots`, `HTLinkExteriors`).
**Control, required:** the same test on **all 14 zero-class `H₁ ≅ ℤ` members** — without it this cell
measures the counterexample and not the proxy.
*Prediction:* **`o10_143849` is NOT a census knot**, hence **not a knot complement in S³**; and **at
least 8 of the 14** zero-class members **are**.
*Kill condition, binding:* **if `o10_143849` IS a census knot**, then Corollary 2.5 applies to it and
gives `η = 0` while `cs = ¼` — **an explicit witness that the cusped `η → cs` step fails**, not merely
a blocked one. **That outcome is the headline and is the better result of the two**, and this seat
states so before knowing which it gets.

**N3 — the same question through a different instrument.** A knot complement in S³ has a meridian
whose filling is S³. Enumerate every slope of normalized length `≤ 6` at the maximal cusp (the
6-theorem: every longer slope fills hyperbolically, hence not to S³), keep those whose filling has
trivial `H₁`, and test each for trivial `π₁` / non-hyperbolicity.
*Prediction:* **no S³ filling**, agreeing with N2.
*Required honesty, declared now:* SnapPy's cusp translations are **unverified floating point** and
the 6-theorem needs the **maximal embedded** cusp, so N3 is **corroboration by a second instrument,
not an independent proof**, and the arc must say that rather than let two agreeing numbers read as
two proofs.

**N4 — §3's PREDICTION, RE-RUN WITH THE REAL PREDICATE.** Addendum 1 tested `H₁ ≅ ℤ`, which is
*necessary only*. Replace it with `∈ CensusKnots`, which for this census is *exact*. Over the full
one-cusped orientable census: among the **amphicheiral** manifolds that **are** knot complements in
S³, how do the CS classes split?
*Prediction:* **every amphicheiral census knot sits at class zero; none at quarter** — i.e. **§3's
prediction is TRUE of the predicate it meant and false only of the proxy it used.**
*Kill:* one amphicheiral census knot at class quarter refutes the corrected form too, and that is
then the headline.
*Vacuity control, binding:* if fewer than **5** amphicheiral census knots exist, the cell is
**UNDERPOWERED** and must be reported as such rather than as a confirmation.

## 3. WHAT THIS ARC WILL NOT CLAIM WHATEVER IT FINDS

Not that Addendum 1's refutation is withdrawn — **§3's prediction is dead as stated in either
branch**, and this addendum cannot resurrect it. Not that a pattern over 3116 census knots is a
theorem: **the `η → cs` step stays blocked by Proposition 2.2's `(1/3)ℤ` slack** regardless of how
clean N4 comes out, and an empirical regularity over a finite census is **evidence for a conjecture,
not a proof of one**. No value, no generation count, no physics reading. **Gate 5 absolute.**
Nothing to `CLAIMS.md`. **L194 stays OPEN in every branch.**

## 4. THE SEAT'S PRIOR, DECLARED

N1 confirms · **N2 returns NOT-a-knot** — the count `14` on the zero side is suspiciously close to the
number of amphichiral knots of low crossing number, which is the reasoning behind this prior and is
stated so it can be scored · N3 agrees · **N4 holds, and its honest reading is that Addendum 1's
refutation was of this seat's PROXY, not of Meyerhoff–Ouyang** · and **the best outcome for the
mathematics is the one this seat is predicting against** (N2's kill), because a witness is worth more
than a clean table.
