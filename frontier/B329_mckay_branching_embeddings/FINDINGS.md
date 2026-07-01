# B329 — `27|₂T` for both natural embeddings: Level 3 is unreachable by any canonical `2T↪E₆`

**Status: banked (frontier). Attacks the B327 residual in-sandbox (compute-before-deferring). Firewalled; nothing
to `CLAIMS.md`.** B327 reduced the mass-hierarchy question to the branching `27|₂T` and the fork *self-dual (quaternionic)
SU(2) → `n₁=n₂`, Level 4* vs *non-self-dual complex embedding → `n₁≠n₂`, Level 3*. This probe computes `27|₂T`
**explicitly for both natural embeddings** and finds **both give `n₁=n₂` → Level 4** — the "complex embedding escapes to
Level 3" hope fails for the canonical candidates.

## Method
Built the **2T character table from scratch** (24 Hurwitz unit quaternions → 7 conjugacy classes → 7 irreps
`1,1′,1″,2,2′,2″,3`; verified orthonormal, `Σ dimᵢ² = 24`), then decomposed the 27 for each embedding via character
inner products. Cross-checks the independent literature value (deep-research R7 ITEM 1).

## Results (verified)
- **(a) Principal — quaternionic `2T ⊂ SU(2) ⊂ E₆`** (the 27 = spin 8 ⊕ 4 ⊕ 0 of B327, restricted):
  **`27|₂T = 3·1 ⊕ 3·1′ ⊕ 3·1″ ⊕ 6·3`.** It factors through `2T/{±1} = A₄` (the spinor irreps `2,2′,2″` are **absent**;
  `−I` acts trivially), the character is **real**, and `n₁ = n₂ = 3`.
- **(b) Trinification — complex `2T ⊂ SU(3) ⊂ E₆`** (via the faithful complex `3 = 1′⊕2′`; `27 = (3,3̄,1) ⊕ (1,3,3̄) ⊕
  (3̄,1,3)`): **`27|₂T = 9·1 ⊕ 3·1′ ⊕ 3·1″ ⊕ 3·2′ ⊕ 3·2″`**, character **real**, `n₁ = n₂ = 0`.
- **Non-vacuity witness.** The SU(3) `3` *alone* restricts to `2T` as `1′⊕2′`, whose character **is complex**
  (`−1 ± √3·i` at the two order-3 classes). So `n₁=n₂` is a genuine obstruction, not a triviality: it is the E₆ 27's
  **balanced `3/3̄` trinification pairing** that cancels the complex parts and restores reality.

## Interpretation — the atom, tightened
`n₁ ≠ n₂` requires `27|₂T` to be **non-self-conjugate**, i.e. `27|₂T ≇ (27|₂T)* = 27̄|₂T`. Since E₆'s outer automorphism
`σ` (diagram flip) swaps `27 ↔ 27̄`, this needs a **non-`σ`-stable (chiral) embedding** `2T↪E₆`. Both natural candidates
— the quaternionic SU(2) and the diagonal-trinification SU(3) — are `σ`-stable, so **both give `n₁=n₂` → Level 4**. This
**strengthens B327**: it is not only the self-dual SU(2) but *also* the complex SU(3) route that lands at Level 4; **Level
3 is unreachable by any canonical embedding.** Getting Level 3 would require a chiral `2T↪E₆` that the arithmetic does not
supply — the standard binary-tetrahedral realization the arithmetic gives is `σ`-stable.

## The firewall (held)
This decides which *level* the hierarchy computation lives at, not any mass value. Even a hypothetical `n₁≠n₂` gives
`O(1)`-distinct eigenvalues, not the `10⁻⁵` magnitude (the structural theorem still forbids the value from the single
seed). Nothing to `CLAIMS.md`.

## Verdict
Banked **[VERIFIED]**: `27|₂T = 3·1⊕3·1′⊕3·1″⊕6·3` (principal) and `9·1⊕3·1′⊕3·1″⊕3·2′⊕3·2″` (trinification), both
`n₁=n₂`. The hierarchy is **Level 4** for every canonical `2T↪E₆`; the residual specialist datum is whether the
arithmetic could force a chiral (non-`σ`-stable) embedding — for which no natural candidate exists. `OPEN_PROBLEMS.md`
gate B updated.

## The fence
2T built from Hurwitz quaternions; character table verified orthonormal (sympy). Branchings by character inner product;
the principal 27 = spin 8⊕4⊕0 imported from B327. No physics values. Nothing to `CLAIMS.md`.

`mckay_embeddings.py` (pyenv) · `tests/test_b329_mckay_branching_embeddings.py`. Related: **B327** (the self-duality
reduction), **B325/B324** (the ω-circulant + its refuted "protection"), **B302** (`ℚ(√−3) → 2T`), **OPEN_PROBLEMS.md**
gate B. Lit (R7): the principal `27 = V(16)+V(8)+V(0)` is Gross (Duke 1999) / Kostant; the `2T` branching is
PARTIALLY-KNOWN (routine corollary, explicit table apparently unpublished — NEEDS-SPECIALIST to close, circle: Griess /
Reeder / Gross).
