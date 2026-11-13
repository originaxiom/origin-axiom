# SM-C7 steps 3 and 4: what calibration found about B1656's channel norm, and the expectations, sealed before the run

*Steps 3 and 4 were released by main at the owner's word (docs/seats/sm.md, M19; register row P-840). B1656 is read only
for its kernel and its regularised norm: `relays/sm_c7/b1656_kernel.py` is its definitions, copied unchanged from
main at f503b1f38, with no measured value in them. M19's rule holds: nothing is set beside a measured number, and the
step-4 table is committed and compared with nothing. This page is pushed before the population is computed.*

## What calibration found (outside the population)

The record is `relays/sm_c7/calibration/calibration_run_steps34.txt`, from cal10 to cal18 beside it.

- **c_s is not twice step 2's Kronecker function plus a τ-only term** (cal10 to cal13: no fit).
- **c_s is the Kronecker limit of the shifted lattice sum at the kernel's own multiplier point** (Parseval, cal14 to
  1e-6). Exactly (cal15, cal17: to 1e-11, on four channels at five points):

  c_s(τ, ū) = F_{u_s}(τ) + π log Im τ + C,   C = −2π(γ + log π) = −10.8193029842,

  - F_u is the constant term at s = 1 of Σ over (m, n) in u + ℤ² of yˢ|mτ + n|^{−2s}, with the pole π/(s − 1)
    removed;
  - u_s is the real coordinates of the summed twist ū, plus the channel's half-period: 1: 0; i: (0, ½); j: (½, 0);
    k: (½, ½).
- **The τ-only part is the same for every line and channel, and it is not modular.** π log Im τ + C is unchanged by
  τ → τ + 1 and moves by −π log|τ|² under τ → −1/τ (cal16). So along a closed geodesic the frame's own c_s has no
  canonical average. Its line part F_u does.
- **c_s depends on the line through a shift u, not a character.** F_u is the Kronecker limit of the u-shifted
  lattice. Step 2's Kronecker coefficient was of the character-twisted lattice: the two are a finite Fourier
  transform apart.
- **The shifted Hecke formula**, ∫ over one period of E^(u)(z, s) ds = H(s)·Σ over (u + ℤ²)/⟨M⟩ of |Q(v)|^{−s}, holds
  at s = 2 to 2 × 10⁻⁸ on a calibration matrix (cal17). At s = 1 it makes ⟨F_u⟩ the Kronecker limit of the thread's
  shifted partial zeta at u.
- **The pairing with step 1.** For u = Jc this is the same shifted partial zeta whose odd part at s = 1 is 4π² times
  the slope (step 1: the period of G^(Jc)*).

## The conventions for the run

- **A character's line:** the summed twist ū with real coordinates Jc; channel s adds h_s.
- **The apex:** the record's apex (B1720), the highest lift of the thread's closed geodesic; the frame's c_s is
  evaluated there by B1656's own code.
- **Averages:** over one period of 48 nodes. The window starts at t₀ = −ℓ/2, and is repeated from t₀ + 0.37ℓ to test
  whether the average is canonical.
- **A channel's u_s is "closed" when M fixes it.** Only closed u_s have a geodesic average; for the others, only the
  apex value is reported.

## Expectations (`relays/sm_c7/expectations_steps34.json`)

- **3a:** |c_s(apex) − (F_{u_s}(apex) + π log Im(apex) + C)| ≤ 10⁻⁸ on every entry.
- **3b:**
  - ⟨F_u⟩ is the same for both windows within 10⁻⁸ (canonical);
  - the frame's c_s averaged on the representative's semicircle moves by more than 10⁻⁶ between the windows, on every
    level (not canonical).
- **3c:** F_u(apex) differs from ⟨F_u⟩ by more than 10⁻⁶ on at least 99% of closed entries. The apex is not where the
  line part equals its geodesic average.
- **3d:** the shifted Hecke formula at s = 2 holds within 10⁻⁶, one character per level.
- **3e:** ⟨F_Jc⟩ is not an affine function of step 2's (π/2ℓ)Z_tot(1, χ_c) within a level: the best fit's largest
  residual exceeds 10⁻³ on every level with at least four characters.
- **Plants, each to miss by more than 10⁻⁶ on at least 99% of entries:**
  - P5, the wrong channel's half-period;
  - P6, π log Im τ dropped;
  - P7, c in place of Jc.
- **The outcome rule:**
  - **A, for the shifted partial zeta at u:** 3a holds, 3b holds and 3c holds;
  - **B:** the apex equality holds on more than 1% of closed entries;
  - **D:** 3a fails.

  Nothing is adjusted after the run.
