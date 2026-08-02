# B850 — the foliation-algebra lead has a computable shadow, and it closes the lead: III₁ generically, not for this object

cc banking seat, 2026-08-02. Prereg sealed **before** computing: `f9d13b4d880301f7`.
Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.

## 0. What was at stake

The incoming bundle calls the foliation-algebra question *"the only item in fifteen rounds that
could change the reframe's architecture rather than relocate its obstruction"* — and files it as
**one sentence to an operator-algebraist**, noting the corpus has one file mentioning
"hyperfinite."

It matters because **B723 Probe 2 found the thermal clock is carried entirely by an external
weight**, and an imposed weight is not spontaneous. If the algebra is **III₁**, Connes' theorem
makes the modular flow unique up to inner automorphism — the weight stops being a choice and
*"spontaneous"* is earned.

**This arc claims the question has a computable shadow and the corpus already has the data type.**

## 1. The instrument

Discrete faithful representation over **ℤ[ω]**, generators `A = [[1,1],[0,1]]`,
`B = [[1,0],[−ω,1]]`, **relator `w a = b w` verified symbolically** — computed, not cited. Exact
traces; lengths `ℓ = 2 log|λ|` at 40 dps.

> **Positive control PASSES: shortest length = 1.08707014499574, against m004's known systole
> 1.087070144995.**

## 2. The binary — verified, and pre-stated as forced

| | verdict | ratios tested | rational | irrational |
|---|---|---|---|---|
| **m004** | **DENSE** | 12 | **2** | 10 |
| **m003** (arithmetic sister) | **DENSE** | 12 | 2 | 10 |
| **m015 = 5₂** (non-arithmetic) | **DENSE** | 12 | 2 | 10 |

**CORRECTED after the full suite caught an order-dependent bug — the first published table said
"0 rational" and that was an artifact, not a fact.** Two failures compounded: `complex()` collapsed
the intended 40 dps to double precision, and both `lengths_from_group` and `ratio_is_rational`
read the **global** `mp.mp.dps`, so any other module's precision setting silently changed this
arc's numbers. Genuine relations then failed a residual bar tighter than the achievable accuracy
and were **miscounted as irrational**. Precision is now pinned locally with `workdps` and the
tolerance scales with the coefficient size; the result is **identical at global dps 15, 25, 40 and
60**, which is now locked.

**The two rational ratios are exactly 2.0 and 3.0 — powers of the systole element.** The
enumeration ranges over group elements, not primitive conjugacy classes, so g² and g³ appear with
lengths exactly twice and three times the systole. **Rational ratios are therefore EXPECTED, not
anomalies**, and they say nothing about the group generated, since powers already lie inside it.
The criterion was always *"one irrational ratio ⟹ DENSE"* and **ten remain**, so **the verdict is
unchanged** — but the original lock asserting `n_rational == 0` **passed for the wrong reason** and
has been replaced by one requiring `n_rational ≥ 1`.

**The seal pre-stated that this outcome is FORCED**, not discovered: geodesic flows on
finite-volume hyperbolic manifolds are mixing, and mixing requires a non-lattice length spectrum.
**So §2 is a verification and is reported as one.** It confirms the instrument agrees with
classical theory; it is not the arc's result.

## 3. The arc's actual product: GENERIC

> **m004, its arithmetic sister, and a non-arithmetic control all return the same verdict.**
> **GENERICITY: GENERIC.** Type: **III₁ — CONDITIONAL on the cited reduction.**

So the foliation route, if the reduction transfers, answers *"is the apparatus internal?"*
**affirmatively — for every cusped hyperbolic 3-manifold.** The external weight can be dispensed
with, and dispensing with it says nothing whatever about m004.

**That closes the bundle's only architecture-changing lead in the same way §3.3 closed the
scattering side.** The pattern is now three-for-three: the SSB mechanism is field-level
(φ_m004 = φ_orbifold), the order parameter is absent at the manifold level and mis-levelled at the
state level (B849), and the internal-clock route is generic. **The reframe keeps being right and
keeps not being about this object.**

**The reduction remains a DECLARED CITATION.** That length-spectrum density gives type III₁ is
**not verified in this sandbox**, and the seal names its weak point in advance: m004's flow is
**not uniformly hyperbolic** (cusp excursions) and the foliation carries an **infinite** invariant
measure — exactly why compact-Anosov ⟹ III_λ does not transfer. **A specialist is still owed the
question.** What this arc changes is the question's cost: it is no longer *"what is the type?"* but
*"does the standard ratio-set argument survive the cusp?"* — and the answer to the first is
predicted, with the data to check it.

## 4. Cell 4 — and a bug that inverted its verdict

Distinct traces per length, words ≤ 6:

| manifold | arithmetic? | max | mean |
|---|---|---|---|
| **m004** | yes | **4** | **1.67** |
| m003 | yes | 3 | 1.47 |
| m015 = 5₂ | **no** | 2 | 1.07 |

Ordering **arithmetic > arithmetic > non-arithmetic**, matching the Vignéras expectation that
arithmetic manifolds carry higher length-spectrum multiplicity. Pre-stated expectation 3 confirmed.

> **But it read as REFUTED until a bug was fixed, and the bug reversed the answer.**
> The m004 path collected a **set of exact traces**; the control path counted **every word**. The
> comparison was distinct-traces-per-length against words-per-length — apples to oranges, inflating
> the controls ~100× and reporting **m015 max = 602 against m004's 4.**

**Exploratory, no verdict, and weakly powered**: 27/45/82 lengths from a length-6 enumeration, with
maxima of 4/3/2. It is a direction, not a measurement.

## 5. Three implementation defects in two arcs, all caught by the seal

Worth naming as a pattern rather than three incidents:

1. **B849 Cell 3** — prereg said *"zero-or-half-period"*; code checked only `== 0`; reported m003 as
   a lemma violation when it sat on the other permitted value.
2. **B850 Cell 4, first form** — prereg said *"for m004 **against** the non-arithmetic control"*;
   code measured m004 alone. A number with nothing to compare it to.
3. **B850 Cell 4, second form** — the comparison existed but compared incommensurable quantities,
   and **gave the opposite verdict.**

**Every one is the criterion stated correctly and the artifact testing something smaller or
other.** In all three the *seal, written first*, is what exposed it — which is the argument for
sealing that no amount of care substitutes for.

## 6. What this arc does NOT do

- **Does not state the type as computed.** CONDITIONAL on a cited reduction whose cusped-case
  validity is the open question.
- **Does not refute the reframe.** GENERIC relocates its mechanism outside the object; it does not
  make the mechanism wrong.
- **Does not settle Cell 4.** Small counts, short enumeration, exploratory.
- **Nothing to `CLAIMS.md`.**

## Carried forward

1. **The specialist question is now sharper and cheaper**: not *"what is the type?"* but *"does the
   ratio-set argument survive a cusp with infinite transverse measure?"* — with a predicted answer
   and the length data to check it against.
2. **Cell 4 deserves a real run** — longer enumeration, more controls, and a stated power analysis
   before any arithmeticity signature is claimed.
3. **T3–T7 remain** (finite-size scaling up the congruence tower, the parabolic pressure function,
   the cascade count, exponents). **T4 is the one I would do next**: B451 computed the *horseshoe*,
   which is uniformly hyperbolic and analytic by theorem, so it could not have found a transition.

`tests/test_b850_length_spectrum.py`
