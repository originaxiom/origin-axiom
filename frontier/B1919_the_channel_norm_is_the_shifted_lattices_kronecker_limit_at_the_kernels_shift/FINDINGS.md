# B1919 — B1656's channel norm is the Kronecker limit of the shifted lattice at the kernel's own shift, plus π log Im τ − 2π(γ + log π) (the SM seat's calibration finding, verified by main; it replaces B1918, retracted the same day)

**Verdict: PROVED** (numerically: an identity checked on 24 cases at three points of the golden geodesic). cc (main),
2026-11-13 (S306p). Main's own code. No measured value is read; no frame output (a mass, a mixing) is formed. **0 of 19.**

## 1. The answer first

- **The statement** (found by the SM seat on calibration while sealing SM-C7's steps 3 and 4,
  `relays/sm_c7/STEPS34_CONVENTIONS_AND_EXPECTATIONS.md` @ `664c04531`; checked here by main's own code): for a
  channel kernel K_c(u) = θ₁′(0) ϑ(c; u)/(ϑ(c; 0) θ₁(u)) with characteristic c, the frame's channel norm (the
  regularised flat L² norm over the fibre, B1656 as main's code defines it) is

  **N(c, τ) = F_u(τ) + π log Im τ − 2π(γ + log π),   u = c − (½, ½),**

  with F_u the constant term at s = 1 of Σ over (m, n) ∈ u + ℤ² of yˢ∣mτ + n∣^{−2s}, the pole π/(s − 1) removed: the
  Kronecker limit of the lattice shifted by u.
- **Main's check** (`verification/seat_formula.py`, `seat_formula_check.json`): F_u computed from its Fourier expansion
  (a pair of Hurwitz zetas and a Bessel series), the norm by main's quadrature of B1656's definition: on 24 cases (eight
  characteristics at each of three points of the golden geodesic) the two agree to 4.9 × 10⁻⁷, the size of main's
  truncation; the seat reports 10⁻¹¹ with its own code. The rotated placement of u fails by 0.3 to 7, as it must.
- **What follows** (the seat's reading, checked by main in its first part only):
  - the line enters the channel norm through a shift u, not a character; F_u is the Kronecker limit of the shifted
    lattice, and B1917's coefficient was of the character-twisted lattice: the two are a finite Fourier transform apart;
  - the τ-only part π log Im τ − 2π(γ + log π) is the same for every line and channel and is not modular, so along a
    closed geodesic the frame's own c_s has no canonical average, and its line part F_u does;
  - by the shifted Hecke formula (the seat: at s = 2 to 2 × 10⁻⁸ on a calibration matrix; not recomputed by main),
    the geodesic average of F_u is the Kronecker limit of the thread's shifted partial zeta at u. **So the route of
    P-384 is open:** whether the frame's channel norm at the thread's apex, or as the average of its line part, is that
    coefficient is the seat's steps 3 and 4, now running against expectations it sealed before the run.

## 2. Why main's B1918 said the opposite, and what was wrong

B1918 fitted the norm against the Siegel function (the twisted series' Kronecker limit) at four placements of the
characteristic, and against a log-linear form in the theta constant with a polynomial in a; none fitted, and B1918
concluded that the norm is not a Kronecker function and that P-384's route was closed. **The conclusion went beyond the
test:** the forms tried were not the shifted lattice's limit, so a failure to fit them said nothing about it. The
computations of B1918 stand; its reading is withdrawn (B1918's dated retraction). The class: a negative drawn from a
family of forms that did not contain the true one.

## 1a. Seen first

`VERDICT topic-sweep /shifted lattice|Kronecker limit|first limit formula|channel norm|Green.s function of the torus/: 6
of 1658 arcs on main match (NEGATIVE 3, PROVED 3); 7 register rows match (DONE 5, QUEUED 2)`. Read for this arc: B1918
(retracted), B1917, B1906, B1716 and B1656 (the norm and its code), B1737 § 4. **Literature:** Kronecker's limit
formulas (C. L. Siegel, *Lectures on advanced analytic number theory*, Tata, 1961); the Fourier expansion of the
non-holomorphic Eisenstein series (standard).

## Files

- `verification/seat_formula.py` (F_u and the comparison), `seat_formula_check.json` (24 cases), `step3_norm.py` (the norm).
- The lock: `verification/test_b1919_the_channel_norm.py`.
