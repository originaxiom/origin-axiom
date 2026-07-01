# B337 — structure ⊕ ordering: the deepest form of the ratio-vs-magnitude wall (Chat-2's insight, probed)

**Status: banked (frontier) as a structural theorem. We probed Chat-2's multiplicity insight ourselves (Attack B of the
symmetry-broken sweep). Firewalled; nothing to `CLAIMS.md`.** The single-object hierarchy arc tested only the
**symmetric** configuration (three generations = one seed cycled by the commensurator ℤ/3). Chat-2 caught the gap: the
**multiplicity** configuration (three *distinct* metallic seeds) was never tested. It resolves into a tension, not a
value.

## The two configurations (verified)
- **Single object (symmetric ℤ/3).** The B324 ω-circulant of the three ℤ/3-conjugate generations has
  `|eigenvalue|² = {52, 1, 1}` — **democratic**: one heavy, two *exactly equal* light. Structure, no ordering.
- **Multiplicity (distinct seeds m=1,2,3).** The genuine overlap `M = tr(AᵢAⱼ⁻¹) = [[2,3,6],[3,2,3],[6,3,2]]`
  (non-circulant — heterogeneity is real; overlaps grow with seed-distance) has eigenvalues `{10.2, −4, −0.2}`, ratios
  `1 : 0.39 : 0.019` — **ordered**: three distinct magnitudes. Ordering, but at a cost.

## The two hard questions — both bite (this is the real content)
- **(a) Is `{1,2,3}` forced? No.** B125's arithmeticity is a **two-element selector `{1,2}`** (golden `ℚ(√−3)`, silver
  `ℚ(i)`), *not* `{1,2,3}` — and `m=3` is **non-arithmetic** (deg ≥ 4). Taking three seeds as the three generations is an
  **ansatz**: it *relocates* the arbitrariness (which seeds?) rather than removing it.
- **(b) Does the structure survive? No.** The seeds have **distinct hyperbolic trace fields** (`ℚ(√−3)`, `ℚ(i)`, deg≥4;
  B125) → they do **not** share one E₆. The gauge group, `sin²θ_W = 3/8`, the cascade — all of which came from `m=1`'s
  `ℚ(√−3)` ℤ/3 symmetry — are **lost** when the seeds are made distinct.

## The theorem
> **Structure ⊕ ordering.** A symmetric configuration (shared arithmetic `ℚ(√−3)`, the ℤ/3) forces the *structure* (E₆,
> `3/8`, cascade) but a *democratic* (degenerate) spectrum. A heterogeneous configuration (distinct seeds, distinct
> fields) gives an *ordered* spectrum but **no** shared structure. The **same** condition — the shared arithmetic, i.e.
> the ℤ/3 symmetry — that forces the structure is exactly what forbids the ordering. **No single static configuration
> has both.**

This is the deepest form of the ratio-vs-magnitude wall reached so far: no longer "the object can't produce values", but
*structure and value require **opposite** symmetry conditions* (symmetric for the gauge group, broken for the masses),
and no static configuration satisfies both.

## Caveat (honest) and the escape
- **B325 caveat:** both overlaps are `tr(AᵢAⱼ⁻¹)`, **not** the physical E₆-cubic mass matrix — so the *specific*
  ordering (`1:0.39:0.019`) is not a mass prediction. The robust content is the **tension** (symmetric⇒degenerate vs
  distinct⇒ordered), which is independent of the overlap-vs-mass caveat.
- **The escape** (both chats): the SM has *both* (unified UV + ordered IR) via **breaking along a flow** —
  symmetric-UV → broken-IR. Whether a *flow* connects the two static endpoints is **Attack C** (B338 / `S047`), and the
  physical flow (RG / spontaneous breaking) is external `[LEAP]`.

## The firewall (held)
A structural theorem about symmetry conditions; no value produced (the ordering is caveated per B325). Nothing to
`CLAIMS.md`.

## The fence
Exact ℤ[ω] overlap (B324) + metallic monodromy discriminants + B125 arithmeticity/field records (sympy). No physics
values. Nothing to `CLAIMS.md`.

`structure_xor_ordering.py` (pyenv) · `tests/test_b337_structure_xor_ordering.py`. Related: **B324** (the ω-circulant),
**B335** (the single-object degeneracy is exact), **B325** (overlap ≠ mass), **B125** (arithmeticity `{1,2}`, the
distinct fields), **B131/S032-B** (heterogeneity is where choice enters — the banked precedent), **B338/S047** (the
bridge). Lit: standard.
