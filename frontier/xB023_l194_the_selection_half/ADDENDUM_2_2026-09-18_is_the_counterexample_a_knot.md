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

---

## 5. THE RESULT — all four cells ran, `verification/knot_or_not.py`, 0 errors

### N1 — the banked datum holds

`o10_143849`: 1 cusp · 10 tetrahedra · orientable · all tetrahedra positively oriented ·
vol `9.146160309759706` · `H₁ = ℤ` · symmetry group `ℤ/4`, full and amphicheiral · **CS class
quarter**. **Exact agreement with Addendum 1 on all six checked fields.** The counterexample is real
and was not a measurement artefact.

### N2 — THE DECISION: `o10_143849` is **NOT** a knot complement in S³

| | |
|---|---|
| calibration, positive — `CensusKnots.identify(m004)` | **`K2_1(0,0)`** — found |
| calibration, negative — `CensusKnots.identify(m003)` | **`False`** — correctly rejected |
| **`CensusKnots.identify(o10_143849)`** | **`False`** |
| `identify()` across all four censuses | **`['o10_143849(0,0)']`** — nothing else |

**It has 10 tetrahedra and the tabulation is complete at 10, so this is a decision, not a failed
search.** **Meyerhoff–Ouyang Corollary 2.5 never applied to it.**

**The control — and it exceeded the prediction.** Of the **14** zero-class amphicheiral `H₁ ≅ ℤ`
members (predicted: at least 8 would be knot complements), **13 are**:

`m004 → K2_1` · `s726 → K6_34` · `s912 → K6_43` · `t07734 → K8_151` · `t12587 → K8_291` ·
`o10_054391 → K10_409` · `o10_124310 → K10_1324` · `o10_136013 → K10_1526` · `o10_138649 → K10_1584`
· `o10_141596 → K10_1643` · `o10_143319 → K10_1685` · `o10_143320 → K10_1686` · `o10_150404 → K10_1846`

**The fourteenth, `t12071`, is NOT one either.** So the proxy `H₁ ≅ ℤ` is imperfect on **both** sides —
but very differently: **13 of 14 on the zero side, 0 of 1 on the quarter side.**

### N3 — the second instrument: calibrated, consistent, and **NOT** a proof — with one cell of it failing outright

The 6-theorem search found **no S³ filling** of `o10_143849`. Its calibration passed: on `m004` it
found the S³ fillings at `(±1,0)` (length `1.0000`, trivial `π₁`), and on the target only four
homology-sphere slopes `(±1,0), (0,±1)` (all of length `3.4792`, cusp area `11.697730`), each of which
**stalls at a 2-generator/2-relator presentation under 60 randomisations — exactly as `m004(1,1)`
does**, and `m004(1,1)` is `+1` surgery on the figure-eight, a **genuinely non-trivial** homology
sphere, while true S³ collapses to `(0,0)` on the first try.

**But the certificate cell FAILED, and is reported rather than dropped.** A proper finite-index
subgroup of `π₁` would *prove* the filling is not S³. The search found one for the calibration
(`m004(1,1)` has a degree-7 cover, `H₁ = ℤ/2 + ℤ/2`, and a degree-8 one, `H₁ = ℤ/12`) and **found
none for any of the target's four slopes up to degree 10** — the same silence S³ itself gives. **So
N3 does not prove its own negative.**

**And a second honest downgrade, which the seal did not anticipate:** *"M has an S³ filling"* and
*"M is a knot complement in S³"* are **the same statement** (the core of the filling solid torus is
the knot), so N3 was never logically independent of N2 — it is **downstream** of it. Its real value
is narrower than the seal claimed and is stated at that width: **it is a consistency check that could
have exposed an error in the tabulation N2 depends on, and did not.**

### N4 — §3's prediction, re-run with the real predicate: **IT HOLDS**

Scanning all **3116** census knots: **13 are amphicheiral**, and

| CS class | zero | quarter | other |
|---|---|---|---|
| **amphicheiral knot complements in S³** | **13** | **0** | **0** |

Not underpowered (13 ≥ 5). **The 13 are the identical set N2's control reached from the census side
— two opposite enumeration directions, symmetric difference empty.**

**A control nobody designed, which the run supplies for free:** amphicheirality forces `cs ≡ −cs`
(mod ½), hence `cs ∈ {0, ¼}`. Addendum 1's scan recorded **`other = 0` across all 181** amphicheiral
one-cusped census manifolds. **181 of 181 agreement with a theorem** validates the amphicheirality
test and the CS-class function jointly.

### POST HOC — labelled as such, because it was not sealed

Among the **181** amphicheiral one-cusped census manifolds the base rate of class zero is
**106/181 = 0.586**. Thirteen draws would put **7.6** in class zero; **13** landed there.
**Fisher one-sided exact `p = C(106,13)/C(181,13) = 6.88 × 10⁻⁴`** — about **1 in 1453**.
*(The proxy's own table, `H₁ ≅ ℤ`: `p = 2.78 × 10⁻³`.)*
**This statistic was computed after seeing N4 and is weaker evidence than a sealed one.** The draws
are also **not independent** — several of the thirteen are small-crossing amphichiral knots and the
census is not a random sample of anything.

---

## 6. WHAT THIS CHANGES, AND WHAT IT DOES NOT

**It does NOT resurrect §3.** Addendum 1's prediction named `H₁ ≅ ℤ` and `H₁ ≅ ℤ` produced a
counterexample. **The prediction is dead as stated, in this branch exactly as in the other**, and
Addendum 1 stands unedited.

**It relocates the failure precisely.** The refutation was of **this seat's proxy**, not of
Meyerhoff–Ouyang. Addendum 1 §5 named both branches before the answer was known; this is the branch
it named second.

**It leaves a well-posed conjecture where a refuted prediction was** — registered as **L224**:

> **An amphichiral hyperbolic knot in S³ has `cs ≡ 0` (mod ½).** True on 13 of 13 in the complete
> ≤10-tetrahedron tabulation. **NOT a theorem here.** Corollary 2.5 gives `η = 0`; the step to `cs`
> is blocked by **Proposition 2.2's `(1/3)ℤ`** slack — `3η` well defined mod `ℤ` pins `cs` only mod
> `½`, the resolution SnapPy already has. **The gap is exactly one quantified slack, and it is
> named.**

**The object's selection now has three accounts, and their status is not equal.** (i) `η(m004) = 0`,
a **theorem** via Cor 2.5 — unaffected by any of this. (ii) The **free involution**: 78/78 orientation
double covers at class zero against a 27.2 % base rate (xB023) — **empirical**. (iii) **Being an
amphichiral knot in S³**: 13/13 (this addendum) — **empirical, post hoc `p ≈ 7 × 10⁻⁴`**. **m004
satisfies all three. m003 satisfies none** — it is not a knot or link complement in S³ at all
(`H₁ = ℤ ⊕ ℤ/5` has torsion), and `o10_143849` is now **also** known not to be one, which is why it
was never a witness against (iii).

## 7. SCORING THE SEAT'S PRIOR

§4 predicted: N1 confirms **(correct)** · N2 returns NOT-a-knot **(correct)** · at least 8 of 14
**(correct — 13)** · N3 agrees **(correct, but N3 is weaker than §4 believed, in two ways §4 did not
foresee)** · N4 holds **(correct)**. **Five for five.**

§4 also said **"the best outcome for the mathematics is the one this seat is predicting against"** —
N2's kill, which would have produced an explicit witness that cusped `η = 0` coexists with `cs = ¼`.
**That outcome did not occur.** **The seat got the tidier result and the weaker one, and having said
so in advance is the only reason that sentence means anything now.**

**L194 remains OPEN.** No value, no generation count, no physics reading, nothing to `CLAIMS.md`.
**Gate 5 absolute.**
