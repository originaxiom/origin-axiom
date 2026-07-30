# B814 — Gate D: the GKY hypothesis FAILS at E₆, from banked data, on day one

cc banking seat, 2026-07-30. **Prereg `46a67d84ae5d892c`, sealed and committed at `380196a8`
BEFORE any computation. Gate 5 absolute — this tests whether a hypothesis is well-posed; it
produces no physical value.**

## The verdict

> **HYPOTHESIS FAILS AT E₆.** The Gang–Kim–Yoon identity requires *every irreducible component of
> `X^irr(M)` to have dimension 1*. At the principal E₆ point of 4₁ the component is a
> **6-fold**. The identity has **no well-posed statement** at E₆ on this manifold.

An incoming probe plan scheduled this check for **week 2**, behind a week of literature. It was
answerable from banked data in an afternoon, and it closes the probe's Gate D **before Gate A is
even reached.**

## The survival branch, closed head-on

The prereg named the outcome that would have left GKY intact and required it be checked rather than
assumed away:

> *"the six blocks are **six separate components of dimension 1 each** (which **satisfies** GKY)"*

**They are not separate.** B575 settles it three ways:

1. **All fifteen cross-pairings vanish.** `B(u_a, u_b) = 0` for every one of the `C(6,2) = 15` pairs,
   in exact arithmetic. The six directions deform **jointly**, not independently — cross-pairings are
   the wrong object entirely if the blocks were separate varieties.
2. **The total is one space.** `dim H¹ = 1` per exponent is stated as *"consistent with the banked
   **H¹ = 6**"* — a single 6-dimensional tangent space, decomposed into six θ-graded 1-dimensional
   blocks, not six tangent spaces.
3. **B575 says it outright:** *"the local E₆ representation variety is **not** the SL(2)-factored
   curve; at quadratic order it is a **smooth 6-fold through the principal point**."*

B370 then carries all six directions **unobstructed to third order**.

## The declared limit, honoured

The prereg fixed the ceiling before the run: *`dim tangent = 6` does not by itself prove
`dim component > 1`* — a singular point can carry a tangent larger than its component.

What upgrades it here is that **B575 does not merely compute a tangent dimension**: it computes the
**quadratic obstruction and finds it identically zero in all six diagonal directions and all fifteen
cross-pairings**, and concludes a *smooth 6-fold*. B370 extends unobstructedness to third order.

**Still: both are explicitly conditional at higher orders** — B370's own words, *"conditional by
nature (higher orders untested — no 'smooth, period' claim)."*

> **Verdict strength: STRONG EVIDENCE, not proof.** A component of dimension 1 would require
> obstructions appearing at fourth order or beyond that annihilate five of six directions while
> leaving the sixth — against a computation showing every direction and every cross-pairing
> unobstructed through third. Possible; not plausible.

**My pre-stated expectation was confirmed, which is weaker evidence than a surprise**, and that is
recorded rather than glossed. The weight is carried by the fifteen vanishing cross-pairings, which
were not a prediction of mine — they were already in the bank.

## What this closes, and what it does not

**Closes:** the probe's Gate D. The GKY identity cannot be *tested* at E₆ on 4₁ because it cannot be
*stated* there. No amount of literature on Gates A–C changes that.

**Does not close** — and the prereg forbids inferring it:
- Gate A (whether an E₆ (2,0) construction exists on a cusped manifold — separately, **no E-type
  M5-brane construction is known**, verified in the literature)
- Gate B (whether higher-rank GKY already exists)
- Gate C (normalisation)
- **The SL(2) case is untouched.** GKY at SL(2) on 4₁ is proved, and the programme's own adjoint
  torsion (`T² − 5T + 1`, `τ₁ = −3`) sits inside its hypothesis perfectly well. **The failure is
  specific to E₆**, and it is a failure of *dimension*, not of the identity.

## The transferable point

The probe's own Gate D was **cheaper than its Gate A and it was scheduled third.** The gate that
could be answered from data already owned sat behind a week of reading. That is the same ordering
error as B804's falsifier-before-literature, in a different costume:

> **Order gates by what they cost, and check what you already own before you buy anything.**

`tests/test_b814_gate_d.py`
