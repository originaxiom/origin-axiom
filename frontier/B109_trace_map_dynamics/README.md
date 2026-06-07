# B109 — the trace-map dynamics at the void (D2 / Task 2)

The figure-eight trace map iterated near the **trivial fixed point** (the "void"). The CC-web probing session's
empirical *coordinate-axis* facts did **not** reproduce; the rigorous **linearization** does, and unifies them.
NO physics; no `CLAIMS.md` promotion; P1–P16 untouched.

- **`probe.py`**
  - **`sl2_void_linearization()`** — `DT₁²(2,2,2)` eigenvalues `{1, φ⁴, φ⁻⁴}`: 1 center / 1 unstable / 1 stable;
    the center eigenvector is the **`A↔B` asymmetry** `(1,−1,−1)` (so "bounded direction" = "slow asymmetry mode"
    = one object); Lyapunov exponents `{0, ±4 log φ}`.
  - **`sl2_center_orbit()`** — the center-direction orbit is **locally bounded** (max‖v‖ ≈ 3.46 at `ε=10⁻³`,
    matching the reported 3.47) and escapes for larger `ε` (honest scope: a marginal center manifold).
  - **`kappa_void_critical_point()`** — the void is a critical point of `κ=tr[A,B]` (`κ=+2`, `∇κ=0`) with Hessian
    `{−2,4,4}`, signature **(2,1)** — a saddle. *(The parabolic cusp is `κ=−2`, B98/B101.)*
  - **`sl3_void_center_count()` / `center_manifold_summary()`** — the SL(3) trivial-point Jacobian is the Dickson
    tower; exactly **2 of 8** eigenvalues have `|λ|=1` (the `{1,−1}` parity sector). The center-manifold dimension
    = the tower's root-of-unity (parity) sector: **1 at SL(2), 2 at SL(3)**.
- **`FINDINGS.md`** — the corrected facts + the tower connection.

**Result.** The void is a `(2,1)` saddle of `κ` whose dynamics are the Dickson tower as a linearization: an
unstable/stable pair at `±4 log φ` and a marginal **center manifold = the tower parity sector**. The "number of
bounded directions" is a tower invariant, and the bounded directions are parity eigenvectors, not coordinate axes
— which is why the naive empirical facts did not reproduce.

```bash
python frontier/B109_trace_map_dynamics/probe.py
python -m pytest tests/test_b109_trace_map_dynamics.py -q
```
No physics claim; proven core P1–P16 untouched.
