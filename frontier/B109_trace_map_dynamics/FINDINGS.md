# B109 — the trace-map dynamics at the void (D2 / Task 2)

**Status: `computer-assisted` + symbolic.** Executes the CC-web "Final Computation Arc" Task 2 (D2 extended) and
banks it (Task 6). The figure-eight trace map iterated near the **trivial fixed point** (the "void"). **Verify-
don't-trust outcome:** the probing session's empirical *coordinate-axis* facts do **not** reproduce, but the
rigorous **linearization** does — and it **unifies and sharpens** them. NO physics (the eigenvalues are
mathematical structure); no `CLAIMS.md` promotion; proven core P1–P16 untouched. Script `probe.py`; test
`tests/test_b109_trace_map_dynamics.py`.

## The correction (what verify-don't-trust found)
The reported facts were stated along **coordinate axes** ("bounded along `z=tr(AB)`"; "the asymmetry `(1,−1,0)`
is the slow mode, 144-step lifetime"). Re-run, the coordinate-axis perturbations **diverge in 4–5 steps** (the
slow *coordinate* is `tr B`, an artifact). The honest object is the **eigen-decomposition of the linearized
map**, which reproduces the *spirit* of the facts exactly and merges Fact 1 and Fact 2 into one.

## SL(2) — the linearization `DT₁²` at the void `(2,2,2)`
With `T₁(x,y,z) = (z, x, xz−y)` (B67) and the figure-eight monodromy `T₁²`, the Jacobian at the void has
```
   eigenvalues { 1,  φ⁴ = (7+3√5)/2 ≈ 6.854,  φ⁻⁴ = (7−3√5)/2 ≈ 0.146 }   →   1 center, 1 unstable, 1 stable.
```
- **One center direction** (`λ=1`, Lyapunov exponent **0**), and its eigenvector is **`(1,−1,−1)` — the `A↔B`
  asymmetry**. So the handoff's "bounded direction" (Fact 1) and "slow asymmetry mode" (Fact 2) are the **same
  object**: the unique marginal center eigenvector *is* the asymmetry direction.
- **Lyapunov exponents `{0, ±4 log φ}`** (`±1.9248`): the unstable/stable rates are `±4 log φ` — the golden
  inflation exponent of the spectral RG (B107), now read off the void's linearization.
- **Local boundedness:** the nonlinear orbit along the `(−1,1,1)` ray stays **bounded, max‖v‖ ≈ 3.46** at
  `ε = 10⁻³` (matching the reported 3.47), but **escapes** for `ε ≳ 10⁻²` — the center manifold is bounded only
  *locally* and on the preferred (sign-sensitive, the quadratic nonlinearity) ray. *Honest scope:* the clean fact
  is the linear one (`λ=1` exactly, Lyapunov 0); the boundedness is the expected marginal-direction behaviour.

## The void as a critical point of `κ = tr[A,B]`
`κ = x²+y²+z²−xyz−2`; at the void `∇κ = 0` (a **critical point**) and `κ = +2`. Its Hessian has
```
   eigenvalues { −2, 4, 4 }   →   signature (2,1)   →   a SADDLE (indefinite).
```
So the void is a **(2,1) saddle** of the Fricke invariant — Fact 3 plus the classification. *(Note: `κ=+2` is the
void/trivial rep; the **parabolic/geometric cusp is `κ=−2`** (B98/B101) — the correction the archived COSMOGONY
draft had backwards; carried as the canonical reading in `speculations/PHYSICS_EXERCISE.md`.)*

## SL(3) — the center manifold IS the tower's parity sector
The trivial-point Jacobian at SL(3) **is** the Dickson tower (B89-T). Its 8 eigenvalue magnitudes are the tower
(`{φ⁻⁶, φ⁻⁴, φ⁻², 1, 1, φ², φ⁴, φ⁶}` for the figure-eight `M²`; the standard `{1,1,φ²,φ⁻²,φ³,φ,φ⁻¹,φ⁻³}` for the
single twist `M`), of which **exactly two have `|λ|=1`** — the **`{1, −1}` parity sector**. So:

| | center (`|λ|=1`) directions | = |
|---|---|---|
| SL(2) | **1** | the `(t+1)` parity factor |
| SL(3) | **2** | the `{1,−1}` parity sector |

**The void's center-manifold dimension = the number of root-of-unity tower eigenvalues = the parity-factor
degree.** "How many bounded directions" is a **tower invariant**, not a coordinate count — and the bounded
directions are the *parity eigenvectors*, not coordinate axes (which is exactly why the naive empirical facts did
not reproduce).

## Verdict
The void's dynamics are governed by the Dickson tower read as a linearization: a saddle of `κ` with signature
`(2,1)`, with an unstable/stable pair at rate `±4 log φ` and a marginal **center manifold equal to the tower's
root-of-unity (parity) sector** (dim 1 at SL(2), 2 at SL(3)); at SL(2) the single center direction is the `A↔B`
asymmetry. The handoff's coordinate-axis facts are corrected to this rigorous, tower-connected statement.

```bash
python frontier/B109_trace_map_dynamics/probe.py
python -m pytest tests/test_b109_trace_map_dynamics.py -q
```
No physics claim; proven core P1–P16 untouched.
