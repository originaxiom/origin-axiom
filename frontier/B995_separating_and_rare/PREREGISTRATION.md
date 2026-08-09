# B995 — PREREGISTRATION: the separating-and-rare census

**SEALED BEFORE COMPUTE. 2026-08-09.** Nothing below was written after seeing a result.

## P0 — the quantifier

Computes over **hyperbolic 3-manifolds and their fundamental groups**: m004, the five registered
family members, and a census population. This is precisely a **member-vs-class** question.

## The question

**B993** proved the programme's cornerstone atom is generic (32.8%) and that Reid-uniqueness is
consumed at zero steps, so the chain is **class-level**. Its own scope note (B803's addendum) leaves
exactly one address open: *a step depending on the **GROUP Γ itself** is not a class statement.*

**B687/B743** killed 23 of 23 dimensionless invariants over the real algebraic tower.

> **A Tier-2 result therefore requires an invariant that is BOTH (a) group-level, AND (b) not
> base-rate-common. Every candidate the programme has found is one or the other, never both.**

**This cell asks whether any invariant is both.**

## The invariant list — FIXED HERE, no additions after compute

Group-level (Γ or the manifold), computable from SnapPy without further choices:

1. `|H1 torsion|`
2. the **full H₁ elementary-divisor multiset** (finer than its product)
3. **Alexander polynomial** — coefficient vector, and its **degree**
4. **number of surjections π₁ ↠ 2T** (the B266 atom, as a registered control — expected to fail)
5. **|H₁(cover)| torsion for the first cyclic covers** (degrees 2, 3)
6. **number of exceptional Dehn fillings** (slopes giving non-hyperbolic fillings)
7. **length of the shortest geodesic** (systole), bucketed
8. **symmetry group order** `|Isom(M)|`

*(Volume, trace field, invariant quaternion algebra and arithmeticity are EXCLUDED by construction:
Reid/B803 make them commensurability invariants, so they cannot separate a member from its class.)*

## The separation set — B855's two registered rows

**golden** (PSL(2,𝒪₋₃)): m003, m206 · **silver** (PSL(2,𝒪₋₁)): m136, m129, m135.
An invariant **SEPARATES** iff m004's value differs from **every** one of these five.

## The base-rate population

`OrientableCuspedCensus(cusps=1)`, **first 1000 by volume** (declared; coverage stated in output,
and any manifold skipped for computability is counted and reported, never silently dropped).
**RARE** iff m004's value occurs in **≤ 5%** of the population.

*Threshold rationale, fixed in advance: 32.8% (surjection count) and 60.8% (trivial torsion) both
failed obviously; a value above a few percent cannot carry a uniqueness claim.*

## The two outcomes

- **OUTCOME A** — at least one invariant is **SEPARATING and RARE**. That invariant is the **Tier-2
  target**, and it proceeds to an **adversarial fan-out** (independent attempts to refute it:
  is the population right? is it secretly commensurability-invariant? is it a convention? does it
  survive the silver row?). **No Tier-2 claim is made in this cell.**
- **OUTCOME B** — **none** is both. Then **`WHAT_WOULD_COUNT.md` falsifier 2 fires**: the programme's
  honest statement becomes *a theory about the commensurability class of ℚ(√−3)*, and Tier 2 is
  unreachable by any invariant on this list.

## THE DECLARED PRIOR

> **OUTCOME B is expected.** Three independent searches have produced the same shape (separating-but-
> common, or rare-but-class-shared), and B743's *"zero gated hits"* over the whole algebraic tower is
> a strong prior. **This cell is expected to close the question negatively.**

Recorded so that an Outcome A, if it comes, is worth something — and so that Outcome B cannot be
re-described afterwards as anything but what was expected.

## What would make this cell INVALID

- adding an invariant after seeing results · moving the 5% threshold · changing the population ·
  dropping a family member from the separation set · silently skipping manifolds.
