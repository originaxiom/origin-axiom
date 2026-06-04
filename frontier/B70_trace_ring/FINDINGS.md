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

## Result — the obstruction is RANK-1

Computing the full `(a,b)`-dependence of the fixed-line Hessian (the `ε²` coefficient; traces vanish at
first order at `c=n`) of the SL(4) two-block word `tr(AᵃBAᵇB)`:

- It is **bidegree (2,2)** in `(a,b)` (≤ n−1=3, by the `c=n` nilpotency).
- Its **only non-separable term is `a·b·tr(X²)`** — a **single rank-1 bilinear coupling**. Every
  separable `aⁱ` / `bʲ` piece is single-index (already reachable by the nilpotent recursion).
- `tr(X²)` is the **degree-2 even-k invariant** (the Hessian of the power trace `tr(A²)`; recall
  `tr(A²)=tr(A)²−2 e₂`, so this is exactly the `e₂` sector).

## Why this is progress

The barrier was previously known only qualitatively ("a non-separable two-index coupling exists,
unreachable by single-index recursion"). This **sharpens it to a rank-1 statement**: the entire
two-block obstruction at SL(4) is **one** bilinear generator `a·b·tr(X²)`, living in the power-2 (`e₂`)
sector. So the trace-ring closure problem is **bounded** — it does not require an unboundedly complex
multi-block algebra, only the incorporation of a *single two-index generator* tied to the `e₂` invariant.
This both explains why every single-index route stalled (they cannot produce even one `a·b` term) and
gives the **minimal** extra structure a first-principles closure must add.

## Honest status / next step

This is a **characterization of the barrier, not yet the proof** (per the Phase-8 plan's stated likely
outcome). The continuation: attempt to **close the SL(4) e₂ sector** by augmenting the single-block
trace data with this one rank-1 two-index generator, assemble the full 15×15 `J(m)` symbolically, and
gate against B65's exact factorization. If the single `a·b·tr(X²)` generator closes the 12/15→15/15
gap and reproduces B65 from the construction, that is the SL(4) proof-of-concept for the general
trace-ring proof; if it does not, characterize precisely what additional structure the substitution
mixing requires. Labeled here as **computer-assisted structural characterization**, not PROVEN.
Proven core untouched.
