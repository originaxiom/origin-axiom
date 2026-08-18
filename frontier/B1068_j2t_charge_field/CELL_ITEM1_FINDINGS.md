# B1068 ITEM 1 — the real forms, exhausted: right rank or right chirality, never both

> ## ⚠ ARGUMENT RE-SCOPED 2026-08-17 (B1073) — the conclusion survives, the argument does not
>
> **The 254 cases measured `Stab(s)`** — the stabiliser of the pure spinor *alone*, dim 61 — **not
> the object's `su(5)`**, which is the composed `A = Stab(e_i, ēbar_j, s) = (34, 24)` of
> `cell11_compose.py`. And the τ used here is the **64 inner sign gradings**, i.e. the 2-torsion
> slice of the family of root-lattice characters, with **no check that it intertwines**
> (`T(X·v) = θ(X)·T(v)` appears nowhere in `cell16_reality.py`, `cell18_realforms.py` or
> `cell20_outer.py`).
>
> **B1073 tested the right object with a τ built and gated properly** — intertwining verified
> 2106/2106 at three split primes — and swept ~1557 characters per prime (the 2-torsion slice, the
> uniform μ-family over all of `F_p^*`, and 400 random characters). **`B = A ∩ τ(A)` has Killing
> rank 3, and no character in the swept family gives 24.**
>
> So this cell's **conclusion stands** — `su(5)` is not real by this route — while its **argument
> was on the wrong algebra with an unverified conjugation**. Recorded as a
> true-conclusion-wrong-argument, the pattern B971 already carries once, so that it does not repeat
> silently. B1073's own negative is scoped to the family it swept, never to "no conjugation
> exists".

**Date:** 2026-08-17 · **Seat:** cc3 · **Prereg:** `PREREG_ITEMS_1_TO_4.md`, committed
`aee98999` **before** compute. **Gate 5:** algebra only.

## THE RESULT — 254 real-form cases, inner and outer

| class | cases | result | rank | chirality |
|---|---|---|---|---|
| **inner** (63 sign-gradings × 2 spinors) | 126 | `so(10)`, dim 45, Killing rank 45 | **5** | **CHIRAL** — `D₅`, `n` odd, `−1 ∉ W` |
| **outer** (64 gradings × 2 spinors) | 128 | `so(9)`, dim 36, Killing rank 36 (104); reductive 21 (24) | **4** | **ACHIRAL** — `B₄`, `−1 ∈ W` always |

> **`su(5)` is real in NO real form of `E₆` reachable this way — 254 of 254.**
> **The object gets the right rank or the right chirality. Never both.**

The 128 outer cases match `B907`'s "all 128 frame-diagonal inner and τ-composite outer
involution representatives" exactly.

## THE PREREGISTERED EXPECTATION, CONFIRMED

The prereg declared in advance: *"if the outer forms inherit `Fix(τ)`'s self-duality, rank 4
is bought with chirality — the trade-off already met three times, and it must be named as a
fourth, not dressed as new."*

That is what happened. `so(9)` is `B₄`, and `−1 ∈ W(B_n)` for every `n`, so every `so(9)`
representation is self-dual. **This is the fifth independent arrival at the same trade-off**,
after `B953`'s θ-split, `B959`'s τ-fold, the degree-0 VEV landing on `F₄`, and `so(8)`.

## THE CONSTRUCTION, and the bug the gate caught

σ is an automorphism of `e₆`, **not** of `e₈`. Permuting the first six *root* coordinates
keeps a block root inside its own block, so σ must act on the `e₆`-**weight**. And that
weight pairs over **all eight** coordinates — a 27-root has `c₇ ≠ 0` and the `E₈` Cartan
couples node 5 to node 6.

**Truncating the pairing to six coordinates was the first attempt**, and the gate caught it
cold: 16 of 27 images landed in neither block. Corrected, the gate reads **27 of 27 into the
27-bar, 0 back into the 27** — exactly what the representation theory demands.

This is the construction deliberately *not* rushed at the end of the previous run. The
caution was warranted: the naive version was wrong, and it would have produced a clean-looking
sweep over a broken map.

## THE CLASS THIS NEGATIVE COVERS — per THE RULE

Covered: **all real forms of `E₆` obtained as `τ_θ = θ ∘ τ_compact` with θ inner or outer**,
exhaustively, 254 cases.

**Outside it:** real forms not of that shape (none are known to this seat — the classification
says every real form arises this way, so this class is believed complete, but that
completeness is **cited, not verified here**); and the object's descent by operations that
are not stabilisers or centralisers at all — of which **only "a quotient that is not a
commutant" now survives**, orbifold projections having been reclassified as centralisers
(see the item-2 record).

## GATES

| gate | result |
|---|---|
| σ carries the 27's weights onto the 27-bar's | **27 of 27**, 0 back into the 27 |
| su(5) control (generic `27 × 27-bar` → Killing rank 24) | **PASS**, in-process |
| Casimir multiplicities on the 27 | **{1, 10, 16}** |
| Φ·Ψ = W mod p | **PASS** |
| all 64 outer gradings enumerated | 64, none skipped |
