# B1347 — ENTERING THE OTHER THREE STRATA: the κ-flow measured, the arrow NOT found, and one exact identity

**Date:** 2026-09-12 · **Seat:** cc · **Lane:** MATHEMATICS (dynamics layer).
**Depends on:** B309 (κ = 2 is "nothing"), B496/B497 (the strata), B1342 (the multipliers, and
"stratum 1 of 4"), B1341.
**P0:** this computes multipliers, orbits and classifications on the SL₂ character variety. **The
physics verb-names for these strata live in `speculations/S063` and are deliberately not used here** —
calling stratum 3 "decoherence" is a gloss, not a derivation, and no such name appears below.

---

## The question, and why it is well posed

B497 classified `End(F₂)` in July and ended *"the program to date = stratum 1 of 4."* B1342 derived
**why** — κ is conserved in stratum 1 alone. Nobody had **iterated** them; the atlas's own gloss says
so (*"the non-invertible verbs the programme has never computed"*).

B497's U1 gives `κ′ − 2 = (κ − 2)·M(x,y,z)` in every stratum, so after n steps

> `κ_n − 2 = (κ_0 − 2) · ∏_{j<n} M(p_j)`

The orbit of **distance from nothing** (B309's `κ = 2`, which B1342 showed is a fixed point of the
*whole* monoid) is therefore governed by the multiplier product. So: **does the non-invertible
dynamics drive κ toward 2 or away — and is the answer uniform?** A uniform sign would be a
**direction**, the thing stratum 1 provably cannot have.

## The measurement

400 generic points + 1200 points on the object's own leaf (both roots, four coordinate ranges), 40
steps, classified on the multiplier product.

| stratum | multiplier | generic | on the object's leaf |
|---|---|---|---|
| **1** (Aut, det ±1) | `1` | **FLAT 100%** | **FLAT 100%** |
| **2** (squaring, det 4) | `x²y²` | COLLAPSE 34% / ESCAPE 66% | ESCAPE 100% |
| **2′** (period-doubling, det −2) | `x²` | COLLAPSE 19% / ESCAPE 81% | ESCAPE 100% |
| **3** (Thue–Morse, det 0) | `x²+y²−xyz` | COLLAPSE 18% / ESCAPE 82% | ESCAPE 100% |
| **4** (degenerate, det 0) | `0` | **COLLAPSE 100%** | **COLLAPSE 100%** |

## Q1 — the control failed first, and it was right to

The first classifier returned ESCAPE when **the point** overflowed. But the question is about
`|κ − 2|`, and **stratum 1's points do escape to infinity while κ is exactly conserved.** Conflating
the two made the control fail. Rewritten to track the multiplier product — the quantity actually
asked about — stratum 1 reads **FLAT on every orbit**, as `M ≡ 1` requires. Recorded rather than
silently fixed: a classifier that mislabels the control would have mislabelled everything.

## THE NEGATIVE, and it is the main result

> **The multiplier does NOT supply an arrow.** Strata 2, 2′ and 3 each produce **both** collapse and
> escape from different starting points — 34/66, 19/81, 18/82. That is a **basin structure**, not a
> direction.

This refutes the natural reading — including one this bench voiced before computing — that *"the
multiplier is the arrow."* It is the quantity that would **carry** an arrow; its sign is not uniform,
so it does not **have** one. Leaving stratum 1 does not hand you a direction any more than leaving
extremality hands you `χ ≠ 0`.

**What is uniform** is the two ends: stratum 1 never moves κ at all, and **stratum 4 lands on
`κ = 2` in one step from every start** — total collapse onto "nothing", which is consistent with
B1342's finding that `κ = 2` is a fixed point of the entire monoid.

## THE EXACT IDENTITY

On the object's own leaf — `κ = −2`, i.e. `x² + y² + z² = xyz`, **the Markov surface** — the
Thue–Morse multiplier is not merely large. It is exactly:

> ### `M₃ |_leaf = −z²`
>
> verified as a polynomial identity: `M₃ + z² − (x²+y²+z²−xyz) = 0`.

Consequences, all exact:

* one step sends `κ − 2 = −4 ↦ +4z²`, so **it crosses from below "nothing" to above it**;
* it lands **exactly on** nothing iff `z = 0`;
* the step is expanding iff `|z| > 1`, which is what the 100% in the table is measuring.

**Scope, stated because it bounds the claim:** Thue–Morse does **not** preserve the leaf, so this is
a **one-step** identity. After it the orbit is on another leaf and the general multiplier applies.
The 100%-escape column is therefore explained by the identity's first step plus generic growth — and
the percentage on its own would have been weak evidence, since generic escape at large coordinates is
also ~100%.

## What this does and does not establish

**Establishes.** The other three strata are now *computed*, not merely classified: their κ-flow is
measured, the two extremes are uniform, the middle is a basin structure, and the object's leaf
carries an exact one-step identity for the Thue–Morse verb.

**Does not establish.** No arrow. No direction. No physics reading — the `S063` fence is kept.
And chat1's caveat stands untouched and unaddressed here: a non-invertible map has **no mapping
torus**, so the natural object is an inverse limit, not a manifold, and `χ` need not be defined
there. **Nothing in this arc says the non-invertible side is a place a theory can live.** It says
what the dynamics does, which is the step that had never been taken.
