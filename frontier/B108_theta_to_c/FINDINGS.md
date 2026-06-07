# B108 — does `θ=−w₀` predict the Dehn-filling scalars `c`? (Task 1 — the prize)

**Status: `computer-assisted` + symbolic.** Executes the CC-web "Final Computation Arc" Task 1 / speculation
**S012** — the top-priority computation, serving both the physics speculation ("residual symmetry per vacuum")
and the central math prize (the `ρ_n` catalog proof). The **hinge test** was mandatory: `θ` must predict **all
four** per-eigenvector degree=rank scalars `c`, not some. **It does not.** This is a clean structural **negative
with a precise obstruction**. NO physics; no `CLAIMS.md` promotion; proven core P1–P16 untouched. Script
`probe.py`; test `tests/test_b108_theta_to_c.py`.

## The objects
Per the B106 D4 anatomy, the Dehn-filling reps satisfy `Lᵢ = c·Mᵢ^k` per eigenvector with
```
   c = 1  (SL(3) W1),   1  (SL(3) W2),   −1  (SL(4) principal),   i  (SL(4) secondary).
```
`θ = −w₀` is the opposition involution — the **contragredient** (`−w₀` = the `A_{n−1}` diagram automorphism), an
**involution** (`θ² = 1`). On the trace ring it is the exchange matrix `P` (B54/B62/B64).

## 1a / 1b — `θ` IS a tower symmetry (the positive half)
On the SL(3) Lawton coordinates, `P² = I` (involution) and **`[P, J(m)] = 0`** symbolically — `θ` **commutes with
the trivial-point Jacobian `J(m)`**, i.e. it is a genuine symmetry of the tower, and its `±1` eigenspaces are
exactly the Dickson **parity sectors** (B62 height-2 split `(1,0), (1,1), (2,1)` at `n=3,4,5` → `char(M²)`,
`char(M²)·char(−M²)`, `char(M²)²·char(−M²)`). *So on the tower side, `θ` is exactly the right structure* — which
is why it was the natural candidate to also organize the Dehn-filling `c`.

## 1c — `θ` at the Dehn-filling reps: the contragredient sends `c ↦ c⁻¹`
At each Dehn-filling rep `θ` acts as the contragredient `(A,B) ↦ (A⁻ᵀ, B⁻ᵀ)`. Under it `μ ↦ μ*` and `[A,B] ↦
[A*,B*]` invert their eigenvalues, so `L = c·M^k` maps to `L⁻¹ = c'·M⁻ᵏ`, giving **`c' = c⁻¹`** — verified
numerically on **all four** components (every realization, ≥2 seeds): `c · c_dual = 1` to `<1e-3`. Explicitly
`−1 ↦ −1`, `1 ↦ 1`, but **`i ↦ −i`**.

## 1d — THE HINGE TEST (the verdict)
`θ` **fixes `c` iff `c² = 1`** (iff `c_dual = c`). Hence:

| component | `c` (B106 seed 0) | order | `θ`-fixed (`c²=1`)? | predicted by `θ`? |
|---|---|---|---|---|
| SL(3) W1 | `1` | 1 | yes | ✅ |
| SL(3) W2 | `1` | 1 | yes | ✅ |
| SL(4) principal | `−1` | 2 | yes | ✅ (matches `c=(−1)^{n−1}`, B83) |
| **SL(4) secondary** | **`i`** | **4** | **no** (`i ↦ −i`) | **❌** |

**The hinge requires all four — it FAILS.** The precise **obstruction**: `θ = −w₀` is an **involution (order 2)**;
its eigenvalues are `±1` (multiplicative orders 1, 2); the secondary's `c = i` has **multiplicative order 4**. An
order-2 symmetry **cannot single out an order-4 scalar** — it sees the `ℤ/4 = {1, i, −1, −i}` only as the `ℤ/2`
flip `i ↔ −i`. So `θ` *pairs* the secondary (`c=i`) with a `c=−i` partner rather than *predicting* it.

*(Honest robustness note: the secondary's realization is branch-sensitive — some seeds land on a degenerate `c=−1`
rep; the genuine secondary, B106 seed 0, carries the order-4 `c=i`, and that is the component that fails. `|c|=1`
and `c↦c⁻¹` hold for **every** realization, across seeds.)*

## Verdict
**NEGATIVE on the hinge.** `θ=−w₀` organizes the **tower** (commutes with `J(m)`, gives the Dickson parity) and
accounts for the order-`≤2` Dehn-filling scalars (`c ∈ {1, −1}`, matching `c=(−1)^{n−1}` for the principal), but
the **order-4 secondary `c=i` is beyond an involution's reach**. So **degree=rank's `c` is NOT predicted by `θ`
alone**, and degree=rank's mechanism stays **OPEN**.

**What this buys the `ρ_n` proof (the constructive part of a negative):** it pinpoints the *missing ingredient* —
an **order-4 (`ℤ/4`) structure** that `θ` does not carry. The natural candidate is the **forced cusp spectrum
`{1, i, −i}`** (B95: at `n=3` the principal spectrum is `{1, i, −i}`, with `a=i` of order 4) — the order-4
element lives in the *cusp/peripheral* data, not in the opposition involution. Paper 1 should frame degree=rank's
`c` as the central open question, with the obstruction "the `c`-source is order 4; `θ` is order 2" made precise
here, and the cusp-spectrum `ℤ/4` as the lead.

```bash
python frontier/B108_theta_to_c/probe.py
python -m pytest tests/test_b108_theta_to_c.py -q
```
No physics claim; proven core P1–P16 untouched.
