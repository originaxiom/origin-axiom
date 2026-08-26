# THE RESIDUAL CHARACTERIZED — the per-factor GUE deviation survives θ-exact AND local-empirical unfolding unchanged: it is not surmise error (memo 68), not unfolding error (this memo), but intrinsic finite-height statistics at T = 3000, sized like the known O(1/log T) correction class
## (outside bench, 2026-08-26; seventy-third memo; closes the B1151 → memo 55 → memo 68 arc; BRANCH II fired)

### THE FACTS (`certificates/unfold_close.py`; asserts GREEN)
- **Anchors.** The exact Gaudin CDF (sine-kernel Fredholm, memo 68
  machinery rebuilt; grid convergence < 1e-10, unit mean) reproduces the
  banked baseline exactly: D_ζ = 0.0416, D_L = 0.0502 (midpoint-density
  unfolding), both to 1e-3 of memo 68's numbers.
- **(B) θ-exact unfolding** — x_n = θ(t_n)/π with the exact Riemann–Siegel
  θ for ζ and the exact Γ-factor phase for L(χ₋₃) (odd primitive mod 3),
  ALL smooth density terms to all orders: D_ζ = 0.0416 (p = 3.8e-4),
  D_L = 0.0502 (p = 5.5e-7) — **identical to baseline to four decimals**.
  The leading-order unfolding was already exact for this purpose.
- **(C) local-empirical unfolding** — sliding-window (w = 25) gap
  normalization, which removes every smooth AND slowly-fluctuating density
  component including S(t) drift: D_ζ = 0.0406, D_L = 0.0513 — the
  residual barely moves.
- **BRANCH II fired** (preregistered): the residual survives both
  refinements. It is an INTRINSIC short-range finite-height deviation of
  the T = 3000 spectra from bulk GUE, of size D ~ 0.04–0.05, compatible
  with the known O(1/log T) correction class for zeta-like spectra
  (1/log(T/2π) ≈ 0.16 at T = 3000 — CITED context, no object-specific
  claim).

> **The arc closes as CHARACTERIZED, not explained away: B1151 found the
> deviation, memo 55 showed the merged statistics are exactly the 2-fold
> superposition of the factors, memo 68 eliminated the surmise, this memo
> eliminates the unfolding. What remains is the finite-height physics of
> the spectra themselves — the expected state of affairs for zeros to
> height 3000, and now the VERIFIED one. Every controllable artifact was
> removed by exact computation; the superposition conclusion (memo 55/68)
> stands on a residual now known to be intrinsic to each factor, not an
> artifact of the bench's own pipeline. Gate 5 untouched (zeros +
> closed-form kernels only).**

### Certificates
`certificates/unfold_close.py`; output `outputs/unfold_close_out.txt`
(in-lane rerun byte-identical). Zeros: the vendored `certificates/c4data/`
(B1151's committed lists, memo 55 provenance).
