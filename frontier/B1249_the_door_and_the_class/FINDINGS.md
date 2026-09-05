# B1249 — 2T CANNOT HOLD THE BIT (and the "door" attribution was wrong)

**Status: banked (frontier). Verdict PROVED.** Instrument + selftest in
`verification/door_class.py` (rc captured directly, E39). Gate 5 clean: no measured value.

B1248 gave the law `det X₀ = squarefree(2 − κ)`, `κ = tr[A,M]` the Fricke–Vogt invariant (K001/B167).
This arc fires it at the chain's own door, **π₁(m004) ↠ 2T ↠(McKay) E₆** — and the control that was
supposed to confirm a door result **refuted the attribution instead**. Both are recorded.

## 1. 2T's κ-spectrum is exactly three values — and the bit is not among them

2T built by closure from `(i, j, ω)`: order **24**, trace spectrum `{−2,−1,0,1,2}`. Over **all 576
pairs**:

> **κ ∈ {−2, 0, 2}** — 24, 384 and 168 pairs. Nothing else.

So `2 − κ ∈ {4, 2, 0}`, class `D ∈ {+1, 2, 0}`, and **the class −1 — the bit — never occurs anywhere
in 2T.** ε = −1 needs `κ − 2` a positive perfect square; 2T's `κ − 2 ∈ {−4,−2,0}` never is.
**This is the arc's real content**, and it is a property of the group, not of any map into it.

## 2. The 48 surjections, reproduced independently

The figure-eight relator `w x w⁻¹ = y`, `w = x⁻¹ y x y⁻¹`, has **72** solutions in 2T, of which **48
generate**. **48 reproduces the banked count** (B237/B1019/B997) from the relator alone, with no
reference to the banked value — the arc's control that group and relator are the right ones.

## 3. THE ATTRIBUTION THAT FAILED — recorded, not quietly dropped

A draft of this arc headlined: *"all 48 surjections give κ = 0 uniformly, so **the door** is not
class-preserving."* **The discriminating control refutes the attribution.** Every generating pair of
2T — **all 384 of them** — already has κ = 0:

| population | count | κ-spectrum |
|---|---|---|
| all pairs of 2T | 576 | {−2, 0, 2} |
| **generating** pairs | **384** | **{0}** |
| relator-satisfying generating pairs (the 48 surjections) | 48 | {0} |

**The relator cuts nothing.** κ = 0 on the surjections is a fact about *generation in 2T*, not about
the figure-eight relator or the door. The correct statement is the weaker and more general one:

> **Any surjection from any group onto 2T sends a generating pair to class D = 2.** Together with §1
> (class −1 is unavailable in 2T at all), **2T cannot carry the bit — however one maps into it.**

That conclusion survives; the door-specific framing does not.

## 4. Ramification — two facts, and NO map between them

| | algebra | ramifies at |
|---|---|---|
| object, both canonical pairs | `(5, −5)` | **nowhere — split** |
| 2T, the Q8 pair | `(−1, −1)` — the **Hurwitz quaternions** | **{2, ∞}** |

Controls: `(−1,−1) → {2,∞}`, `(1,1)` and `(−1,1)` split, `(2,3) → {2,3}` — all matching known answers.

**FENCED, and the fence is the point.** A draft said *"the door **adds** ramification."* **No map
between these two algebras is exhibited**, so a causal reading is exactly the identification error
`T-IDENTIFICATION-IS-AN-INPUT` forbids. What is computed is two separate facts about two separate
pairs. They are recorded side by side and **nothing is claimed to flow between them.**

## Fences

- **NOT claimed: that SU(2) is derived.** 2T sits inside SU(2) **by construction**, so its algebra
  being the Hamiltonians is a property of that construction, not an output of the chain.
- κ is not a homomorphism invariant; no claim is made that it "should" transport.
- No measured physical value. Gate 5 clean.

## Dependencies

B1248 (the law), B237/B1019/B997 (the 48 surjections, reproduced here), B167/K001 (κ), B727 (McKay).
