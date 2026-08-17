# B1068 CELL 3 — the object reaches so(10) with chirality, and stops there

**Date:** 2026-08-17 · **Seat:** cc3 · **Gate 5:** algebra only; no physical
identification is made here. This cell replaces the withdrawn cell 2.

## WHY THIS CELL EXISTS

Cell 2 was withdrawn after four errors, **every one of which pointed toward "no"**. This
cell is built so those specific failures cannot recur silently:

* **the control runs first, in the same script.** Generic `27 × 27-bar` rank-1 weight
  vector pairs must reproduce `dim 45, Killing rank 24 = su(5)`. **It passes.** So the
  instrument demonstrably *can* find `su(5)`, and any later absence is a real absence
  rather than a blind spot. Cell 2 never validated against a known answer.
* **every candidate is gated on rank 1** (stabiliser dimension 61) *before* use. That is
  the check that exposed cell 2's fourth error, and it now runs first.
* **the 27-bar's own cubic is computed**, not borrowed. Cell 2 reused the 27's
  coordinates, which is what produced rank-3 vectors on the bar side.
* **reductive parts come from the Killing form rank, never a dimension.** `dim 44` fits
  both `so(8)⋉16` and `su(5)⋉20`.

A construction bug found and fixed on the way: the `A₂` operators that link the three
27-blocks **annihilate** the 27-bar blocks — they raise the `3`, and the bar side carries
the `3̄`. The bar cubic needs the opposite pair. With the right operators: residual `0`,
`a³ = 6`, the no-`a²b`/`a²c`/`abc` shape prediction holds, and the bar algebra's
square-free discriminant part is **77** with `disc/6237` a perfect square — so **the
27-bar's invariant algebra is also the charge field K**, confirming cell 1 by an
independent route.

## THE RESULT — all 63 subsets of the object's six gated rank-1 invariants

Three from the 27, three from the 27-bar. Confirmed at `p = 1093, 1097, 1151`.

| \|S\| | dim | reductive | count | |
|---|---|---|---|---|
| 1 | 61 | **45** | 6 | `so(10) ⋉ 16` |
| 2 | 45 | **45** | 3 | **`so(10)`, semisimple, rank 5 — CHIRAL** |
| 2 | 44 / 52 | 28 | 12 | |
| 3 | 28 / 36 / 44 | 28 | 20 | |
| 4–6 | 28 | 28 | 16 | `so(8)`, the frame stabiliser |

**`su(5)` — Killing rank 24 — never appears, in any subset.**

## WHAT IS POSITIVE HERE, and it is the first thing that has survived

**The object reaches `so(10)` with chirality intact.** `so(10)` is `D₅`; `n = 5` is odd,
so `−1 ∉ W(D₅)` and `so(10)` has complex representations — the **16** and **16-bar** are
distinct.

This is the **first route in the whole investigation that gets below rank 6 without
destroying the 27's complexity**, and the reason is now exact. The four that failed:

| route | why chirality died |
|---|---|
| `F₄` (θ-split, B953) | no diagram automorphism; all reps real |
| `Fix(τ)` (B959) | `τ` exchanges the 27 and 27-bar, identifying them |
| `F₄` (the degree-0 VEV) | same |
| `so(8)` | `D₄`, `n` even, so `−1 ∈ W`; all reps self-dual |

**`D₅` is the odd one, and it is where the object lands.**

No tension with the rank ceiling: rank drops `6 → 5` because a **VEV stabiliser is not a
centraliser**. The ceiling theorem only ever constrained centralisers.

## WHAT IS NEGATIVE, exhaustively

`SO(10) → SU(5)` is **not reachable** from the object's own invariant idempotents. Every
subset beyond the `so(10)` pairs descends to `so(8)` — rank 4, and achiral. The object
gets exactly one rung down the standard chain and stops.

In the standard chain that step needs a **16** VEV, a spinor of `SO(10)`. Under `so(10)`
the 27 splits as `16 + 10 + 1`; whether the object's rank-1 invariants lie entirely in the
`10 + 1` part is the sharp refinement this leaves open, and it is not computed here.

## LIMITS

- Isomorphism types are identified by dimension **plus** Killing rank **plus**, for the
  28, the independent frame-stabiliser reading. `dim 45` semisimple of rank ≤ 6 admits
  only `so(10)`; that step is an argument, not a structure-constant identification.
- Mod-p rank can only over-estimate a nullity. Three agreeing primes make an artefact
  unlikely without excluding it.
- Novelty is **not** claimed and no literature sweep has been run.
