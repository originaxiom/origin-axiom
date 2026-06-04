# B70 — trace-ring proof attack (Track A1): the two-block obstruction is RANK-1

**Date:** 2026-06-04. **Status:** exploratory, committed. Proven core P1–P16 untouched. Script:
`two_block_rank1.py` (exact sympy). Standalone Lie-theory / invariant-theory; no physics claim. This is
the first result of the Phase-8 Track-A attack on the `a_d` trace-ring proof (B58 proper).

## Context — the precise open barrier

The candidate `a_d` formula (B62 θ-split, V26) matches n≤5 exactly but is **unproven**; the proof needs
the ambient `SL(n,ℂ)` trace ring. Every prior route (cotangent V21, Sym²ᵏ V27, pinv-limit V24, the
nilpotent gate V36) hit the **same** barrier: the even-k / `e₂=tr(Λ²A)` sector requires genuine
**two-block words** `tr(AᵃBAᵇB)` whose fixed-line Hessian has a non-separable `a·b` coupling that no
single-index `(r−1)^d` recursion generates (single-block V+Λ² traces span only 12/15 at SL(4), B65).

## Result — the obstruction is RANK-1 (rigorous, on the traceless sl(n) tangent)

Computing the full `(a,b)`-dependence of the fixed-line Hessian (the `ε²` coefficient; traces vanish at
first order at `c=n`) of the two-block word `tr(AᵃBAᵇB)`, on the **proper traceless `sl(n)` tangent**
(tracelessness imposed by substitution *after* the matrix products — the up-front projection blows up
symbolically; this version is uncompromised):

- It is **bidegree (2,2)** in `(a,b)` (≤ n−1, by the `c=n` nilpotency).
- Its **only non-separable term is `a·b·tr(X²)`** — a **single rank-1 bilinear coupling**. Every
  separable `aⁱ` / `bʲ` piece is single-index (already reachable by the nilpotent recursion).
- **The coupling form is exactly the `e₂` coordinate:** `tr(X²) = −2·(Hessian of e₂=tr(Λ²A))`
  (the identity `e₂-Hessian = −tr(X²)/2` on `sl(n)`, verified). So the *single* two-index generator is
  pinned **precisely** to `e₂` — the even-k sector.

**Robustness (all RANK-1, verified on traceless `sl(n)`):** SL(4) `tr(AᵃBAᵇB)`, SL(4) `tr(AᵃB²AᵇB)`,
and SL(5) `tr(AᵃBAᵇB)` — every case has its non-separable content as the single `(1,1)` monomial
`a·b·tr(X²)`. (The SL(5) symbolic case takes several minutes — long runs, no shortcuts.)

## Why this is progress

The barrier was previously known only qualitatively ("a non-separable two-index coupling exists,
unreachable by single-index recursion"). This **sharpens it to a rank-1 statement**: the entire
two-block obstruction at SL(4) is **one** bilinear generator `a·b·tr(X²)`, living in the power-2 (`e₂`)
sector. So the trace-ring closure problem is **bounded** — it does not require an unboundedly complex
multi-block algebra, only the incorporation of a *single two-index generator* tied to the `e₂` invariant.
This both explains why every single-index route stalled (they cannot produce even one `a·b` term) and
gives the **minimal** extra structure a first-principles closure must add.

## e₂-sector closure — the rank-1 generator does NOT suffice; the closure is bounded at bidegree (3,3)

**The bound is correct, but it rests on the UNIPOTENT fixed-line object — not the generic ε-series.**
(Correction, 2026-06-04, after independent recheck.)

`e2_sector_closure.py` first measured the two-index `(a,b)`-content of `tr(AᵃBAᵇB)` via the **generic**
traceless tangent `A=(I+εX)^a`. That object's content **grows unbounded** with ε-order — the max
single-index degree equals the ε-order (1, 2, 3, …, **7** by ε⁸):

| ε-order | max single-index degree in a two-index monomial |
|---|---|
| ε² | 1 | ε³ → 2 | ε⁴ → 3 | ε⁵ → 4 | ε⁶ → 5 | ε⁷ → 6 | ε⁸ → 7 |

So the generic ε-series does **not** demonstrate a `(3,3)` cap; the lone `(3,3)` it prints at ε⁶ is one
monomial among a growing set. **The right object is the unipotent fixed line** (`c=n` ⇒ every trace
`=n` ⇒ `A` unipotent, `(A−I)ⁿ=0`), on which

    A^a = (I+N)^a = Σ_{j=0}^{n−1} C(a,j) N^j    (exact, N^n=0)  ⇒  a-degree ≤ n−1 = 3,

so `tr(AᵃBAᵇB)` has bidegree **≤ (3,3)** — a one-line consequence of the `c=n` nilpotency (the proven
B58_sl4 fact that fixed-line derivative sequences are degree `≤ n−1` in word-length, here per index).
`e2_unipotent_bound.py` verifies this directly: with `A=I+N_A` (upper-nilpotent of index `n`) and
`B=I+N_B` (lower-nilpotent, so the word is non-triangular), the bidegree is **exactly (3,3)** for a
full-index `N_A` (and `(idx−1, idx−1)` for index `idx`). The optimistic "one generator closes it" is
refuted (the content is genuinely two-index past `(1,1)`), but the closure is a **bounded, finite**
problem (bidegree `≤(3,3)`), with the rank-1 `(1,1)` term as its leading order — not an unbounded wall.

## Honest status

Two banked results: (1) the two-block obstruction's *leading order* is rank-1, exactly `e₂` (rigorous,
traceless sl(n), n=4,5 — `two_block_rank1.py`, unaffected by the correction); (2) the *full* e₂-sector
closure needs a **bounded** (bidegree `≤(3,3)`) multi-generator two-index set, the bound being a
one-line consequence of the `c=n` unipotency (`e2_unipotent_bound.py`; the earlier
`e2_sector_closure.py` generic-ε-series was the wrong object and is kept only as the unbounded-growth
contrast). Together these turn the long-standing "two-block barrier" from a vague wall into a
**precise, finite, bounded** structure — the genuine content a first-principles trace-ring proof must
assemble. The full symbolic assembly of that bounded set into `J(m)` (gated vs B65) is the substantial
continuation; labeled **computer-assisted structural characterization**, not PROVEN. Proven core
untouched.
