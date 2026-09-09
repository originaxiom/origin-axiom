# B1255 — THE GENERATION INDEX HAS THE RIGHT GALOIS TYPE AND THE WRONG COMMUTATOR: the pattern behind twelve lost three-nesses, named — and the one three-ness in the record that survives both of their kills, killed here by a third test

**Date:** 2026-09-05 · **Seat:** cc · **Status:** PROVED (exact tier throughout; two MB12 controls, both directions)

## The question (owner-set, after B1253 refuted its own headline)

> *"How come we convinced ourselves we got three generations then we refuted it. What went wrong
> and why we gave up? No room left for investigation or other path, or analyze the pattern that
> led us to believe we derived three gen? Maybe the patterns tells us the phenomena that gives
> real results."*

The instruction is the method: do not file the refutation and move on — **read the failures as a
family and ask what they have in common.**

## 1. The pattern: every lost three-ness was built on ℚ(√−3), and that field can only make 1+2

Twelve three-nesses have been tested and lost across the corpus. They trace to a single arithmetic
fact: **3 ramifies in ℚ(√−3)** — one prime with multiplicity. Ramification produces *conjugates*
or *gradings*, never *copies*. And a quadratic field has **at most two** primes above any rational
prime, so three-fold splitting is impossible there in principle.

This independently reproduces **B298's degree-2 obstruction**, and it re-reads **B1253's price**
(*"the object gives 1 abelian + 2 chiral; the SM needs 3 chiral"*) as the same **1 + 2** in
representation-theoretic costume — the split of μ₃ into one rational root and one conjugate pair.

**Why we kept believing it:** each appearance looked independent. None of them were.

**What the pattern predicts:** a genuine three needs an **irreducible cubic**, where the Galois
group permutes the roots transitively and **no root is distinguished**.

## 2. The record contains exactly that — twice, in the same family (verified here, not cited)

| | irreducible /ℚ | disc squarefree kernel | Galois | real roots |
|---|---|---|---|---|
| **μ13** (the field K = ℚ[ρ]/μ13 the colored sector lives over) | ✔ | **{7, 11}** | **S₃** | 3/3 |
| **HIER** (the hierarchy cubic; roots = the v_g²) | ✔ | **{7, 11}** | **S₃** | 3/3 |

Both **totally real**, both in the **√77 family**, roots reproducing the banked v_g² to 1e−38.
This is the type ℚ(√−3) provably cannot supply, and it **survives both kills** that ended the
earlier three-nesses:

- **B324's kill** (*"the three are g-conjugates sharing one character"*) does not bite: three
  generations are **required** to share one character — identical gauge quantum numbers is what
  makes them generations — and are distinguished by their **values**. Same minimal polynomial,
  different values, is exactly the generation type.
- **B1253's kill** (*all 15 sixteen-blocks lie in one Weyl orbit*) does not bite: Weyl conjugacy is
  **gauge** equivalence — one particle rebased. Galois conjugacy over ℚ is **not** a symmetry of
  physics; the three roots are three distinct real numbers.

## 3. The third test — and it refutes the reading

A flavour index must **commute with the gauge grading**: in the Standard Model, gauge symmetry acts
identically on all three generations. Computed on the object's own data (banked B883 27, the four
B854 charge invariants, Mc = 3R₈+7R₁₄+13R₁₆+17R₂₂, and D₂ as B1250 decoded it):

- D₂ reproduces: **11 flips = 1 + 10, the 16 fixed** — the SO(10) grading;
- the colored block is **18-dimensional**, splitting **12 / 6** across D₂ — exactly the independent
  SO(10) prediction for 27 = 16 + 10 + 1 (12 colored in the 16, 6 in the 10);
- W18 **is** D₂-invariant; but

> **[C18, D₂|W18] ≠ 0, and 0 of the 6 colored atoms is a D₂-eigenspace.**

The generation index is **transverse to the gauge grading**, not orthogonal to it. And behind that
sits a dimension count that closes the route permanently:

> **27 = 16 + 10 + 1 carries the 16 with MULTIPLICITY ONE. Three copies need dim ≥ 48 > 27.**

**Three generations cannot live inside one 27.** Registered as **I-24, REFUTED**.

## 4. What survives, and it is not nothing: the non-commutation IS the hierarchy

B923 (reproduced here on bench, 95 s, all PASS) shows the same invariant in two gauges:

| gauge | the diagonal CCl invariant |
|---|---|
| canonical H₊ | **(x+3)³ — generation-DEGENERATE**, three identical values |
| τ-twisted H′ = H₊·D₂ | **HIER** — three distinct real roots |

Had the generation operator and the twist commuted, they would be simultaneously diagonalisable and
the splitting would be **gauge-blind**: degenerate copies with **no hierarchy**. So the very failure
that denies g the flavour role is **the mechanism that lifts the degeneracy**. *Identical, then
split by the operator that defines the generation's gauge content* is the physical shape of
generations. What the object does not supply, inside one 27, is the three **copies**.

## 5. Where the count must therefore come from

Not from within the 27 — that is now closed by a dimension count rather than by a failed search.
It must come from **multiplicity**: B1253's h¹ = 3, whose stated price is unchanged and now
**sharply localised as the only surviving route** — *make the trivial (Sym⁰, abelian) summand
chiral, or exhibit a bundle whose three classes are all chiral.* B632 flagged this at banking as
"a structural difference"; it is the one remaining door.

## Controls (MB12, both directions)

- **The S₃ verdict can fail:** the cyclic cubic x³−3x²+1 (disc = 81) is exhibited and correctly
  typed **C3** — the test is not a tautology.
- **The commutator test can return zero:** [D₂, Cartan₀] = 0 is exhibited — "≠ 0" is content, not
  a broken comparison.
- The 12/6 split is checked against the **independent** SO(10) prediction, not asserted.
- B1250's own control stands: **0 of 4000** random 11-subsets admit an affine character.

## Verification

`verification/generation_type.py --selftest` — arithmetic tier runs standalone; the object tier
needs `SESSION_SCRATCH` holding B923's step-1 invariants cache.

- **Feeds on:** B923 (v_g² = roots(HIER) as identity; the two gauges), B918 (HIER pinned exactly),
  B1250 (the D₂ decode), B1252 (the Cartan metric), B1253 (the h¹ price), B883 (the 27),
  B854 (the charge invariants), B298/B324/B307 (the prior obstructions).
- **Registers:** I-24 **REFUTED**.
