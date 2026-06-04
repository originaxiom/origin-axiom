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

## e₂-sector closure attempt — the rank-1 generator does NOT suffice (but the closure is bounded/finite)

`e2_sector_closure.py`. The fixed-line Jacobian uses the **full ε-series** (the 15 coordinates separate
only across orders 1..L — the B58-Phase-A "rank-3 Fricke block" fact); the rank-1 result above is the
**leading (ε²) order**. Computing the non-separable (two-index) content of `tr(AᵃBAᵇB)` at higher
ε-orders (traceless X,Y):

| ε-order | non-separable `(a,b)`-bidegrees | max bidegree |
|---|---|---|
| ε² | `(1,1)` | (1,1) — **rank-1** |
| ε³ | `(1,1),(1,2),(2,1)` | (2,1) |
| ε⁴ | `…,(2,2),(3,1)` | (3,1) |
| ε⁵ | `…,(2,3),(4,1)` | (4,1) |
| ε⁶ | `…,(3,3),(5,1)` | (5,1) |

**The two-index content grows with ε-order** — so a *single* rank-1 generator does **not** close the
e₂ sector; the closure needs the higher-bidegree two-index structure across orders. This is the honest
verdict: the optimistic "one generator closes it" is refuted.

**But the closure is BOUNDED / finite.** The fixed-line derivative sequences have degree `≤ n−1 = 3`
(the `c=n` nilpotency — B58_sl4), so the Jacobian-relevant two-index content caps at **bidegree
`(3,3)`**. The e₂-sector closure is therefore a **finite, bounded multi-generator problem** (a
two-index generator set of bidegree `≤(3,3)`), with the rank-1 `(1,1)` term as its leading order — not
a single generator, but **not an unbounded wall either.**

## Honest status

Two banked results: (1) the two-block obstruction's *leading order* is rank-1, exactly `e₂` (rigorous,
traceless sl(n), n=4,5); (2) the *full* e₂-sector closure needs a **bounded** (bidegree ≤(3,3))
multi-generator two-index set, not one generator. Together these turn the long-standing "two-block
barrier" from a vague wall into a **precise, finite, bounded** structure — the genuine content a
first-principles trace-ring proof must assemble. The full symbolic assembly of that bounded set into
`J(m)` (gated vs B65) is the substantial continuation; labeled **computer-assisted structural
characterization**, not PROVEN. Proven core untouched.
