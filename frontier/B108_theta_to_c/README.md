# B108 — `θ=−w₀ → c`? the opposition involution vs the Dehn-filling scalars (Task 1)

The top-priority computation: does the opposition involution `θ=−w₀` (the engine of the tower's Dickson-parity
decomposition) **predict** the per-eigenvector degree=rank scalars `c = {1, 1, −1, i}` (B106 D4)? If yes, the
Dehn-filling sector is tied to the tower structure and the `ρ_n` catalog proof gains its missing piece. The
**hinge test** demanded all four. NO physics; no `CLAIMS.md` promotion; P1–P16 untouched.

- **`probe.py`**
  - **`theta_is_tower_symmetry()` (1a/1b)** — `θ` is the contragredient involution `P` (`P²=I`) and **commutes
    with `J(m)`** (symbolic, SL(3)); it organizes the Dickson parity (B62 height-2 split). *The positive half.*
  - **`contragredient_c()` (1c)** — at the Dehn-filling reps `θ` acts as `(A,B)↦(A⁻ᵀ,B⁻ᵀ)`, sending **`c ↦ c⁻¹`**
    (verified all four components, every seed).
  - **`hinge_test()` (1d)** — `θ` fixes `c` iff `c²=1`: it predicts W1/W2 (`c=1`) and the principal (`c=−1`), but
    **NOT** the secondary (`c=i`). **Hinge FAILS.**
- **`FINDINGS.md`** — the tables, the obstruction, and the forward pointer.

**Result (clean NEGATIVE with a precise obstruction).** `θ=−w₀` is an **involution (order 2)** — its eigenvalues
are `±1` (orders 1, 2) — but the SL(4) secondary's `c=i` has **multiplicative order 4**. An order-2 symmetry
cannot single out an order-4 scalar (`i ↦ −i`). So degree=rank's `c` is **not** predicted by `θ` alone and stays
**OPEN**. The missing ingredient is an **order-4 (`ℤ/4`) structure** `θ` does not carry — candidate: the forced
cusp spectrum `{1, i, −i}` (B95). Paper 1 frames degree=rank as the central open question with this obstruction.

```bash
python frontier/B108_theta_to_c/probe.py
python -m pytest tests/test_b108_theta_to_c.py -q
```
No physics claim; proven core P1–P16 untouched.
