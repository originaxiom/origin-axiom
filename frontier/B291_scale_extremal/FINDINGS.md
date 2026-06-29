# B291 — Is any closing scale-distinguished? The min-volume closing, and axis-stratified selection

**Status: banked. The extremum is verified two methods + triangulation-stable; the axis-stratification is the
finding. Nothing to `CLAIMS.md`.** Phase III of the seam arc (wall #5, scale). B290 showed the seam generates a scale
ladder but does not identify filling↔level. B291 asks the independent question: is there a **scale-extremal** closing,
and does it coincide with the dynamical (B287) or arithmetic (B288) distinguished closing?

## The result
1. **A min-volume closing exists and is stable.** Over the grid `|p|,|q|≤8`, the minimal-volume hyperbolic filling is
   **`m004(±5,1) = m003(−2,3)`, vol `0.98136883`** (the figure-eight's smallest hyperbolic filling — *not* the Weeks
   manifold `0.94271`). Two methods agree (`volume() = Re(complex_volume) = 0.981368829`); the min-volume slope is
   **invariant across randomized triangulations** (5/5).
2. **The systole gives no finite distinguished closing.** The shortest geodesic `~ |core| ~ 2π/n → 0` as the slope
   grows, so the systolic **infimum over all fillings is `0`** — not attained at any finite closing.
3. **Selection is axis-stratified.** The min-volume closing `m004(5,1)` is **non-arithmetic** (trace field `x⁴−x−1`,
   B288 — re-verified in pyenv) and is **not** the fiber/Sol closing (B287's `(0,1)` is non-hyperbolic, vol `0`). So
   the **scale-extremal axis selects a *different* closing** than the dynamical (`A=LR`) and arithmetic (`ℚ(√−3)`)
   axes.

## The selection taxonomy (the texture of "selective vs catalogue")
| axis | distinguished closing | character |
|---|---|---|
| **dynamical** (B287) | `(0,1)` — Sol torus bundle, monodromy `A=LR` | re-sees the proven core (P1/P8) |
| **arithmetic** (B288) | *none* | E₆/`ℚ(√−3)` lost on closing |
| **scale** (B291) | `(5,1) = m003(−2,3)`, min volume | non-arithmetic; not the fiber |

The seam **is** selective — but *along different axes it picks different closings*, and no single closing is
distinguished on all axes. That is the precise answer to "selective vs catalogue": **selective per axis, with no
universal selection** — exactly what B294 will tabulate.

## Two methods + stability (verify-don't-trust)
- Volume via SnapPy `volume()` and independently via `Re(complex_volume)` (Cheeger–Chern–Simons real part) — agree to
  `<1e-7`.
- The min-volume slope is re-computed on **5 randomized triangulations** — stably `(±5,1)`, not a triangulation
  artifact.
- The min-volume closing's non-arithmeticity is **re-verified in pyenv** (degree 4, `x²+3` irreducible over it).

## The fence
Pure geometry. A clean extremum exists; it does **not** pick a unique distinguished world — different axes select
different closings. "min-volume = our universe" is a `[HOOK]`, not banked. Nothing to `CLAIMS.md`.

`scale_extremal.py` (sage-python: SnapPy volume landscape + Regina identify + stability + systole) · `verdict.py`
(pyenv; re-checks non-arithmeticity) · `tests/test_b291_scale_extremal.py`. Related: `B287` (the dynamical closing),
`B288` (the arithmetic census), `B290` (the scale ladder), `B286` (the seam), `B250` (volume/Lobachevsky).
