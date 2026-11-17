# X-APEX source defects

Source head 5de6493f5f1a0300dca64c0fb90afd26925ef1c9.
Interim reading: stages one through three and all four cards/result
notes read in full; stage four's script and output remain in progress.
Evidence label: not independently checked. No scientific execution,
CAS or empirical comparison. This report supplies source findings,
not a banking decision. Exact quotations below are excerpts at the
cited one-based lines. Custody and coverage are recorded separately.

The cusp, normal-response and chain subjects overlap earlier physical
constructions. The findings concern what these particular artifacts
test; they do not independently accept this lane's underlying proofs.

## XA-01 — The cusp contraction check changes the operator and carrier

- Claim: relays/AGY_EXP_TO_PHYSICAL_AND_CC_2026-11-17_X_APEX_1_RESULTS.md:20,
  "Certifies a grid-convergent Kantorovich / Banach contraction ball".
- Source: relays/x_apex_1_verify/verify_x_apex_1.py:523-525,
  "lap_eigs = (4 * (math.pi ** 2)) * (m1 * m1 + (m2 * m2) / (im_tau * im_tau))"
  and "l0_eigs = lap_eigs + (mq_val * mq_val) * om2_avg".
- Source: same file:509-512 replaces the conformal factor by its area
  average and sets "mq_val = 1" and "g_quad = rf(3, 5)".

This is a massive flat-torus scalar Fourier operator and a supplied
quadratic nonlinearity. It does not build the punctured hyperbolic
gauge operator, its actual Higgs commutators, Q-kernel projection,
constant cusp asymptote or weighted source spaces. The lowest flat
mode already has the inserted positive mass, independent of grid
refinement. Consequently this check cannot establish the physical
complete-cusp inverse or contraction named by the report. Stage four's
acknowledged continuum norm duty does not account for this different
finite operator. The finite flat-model computation is not refuted.

## XA-02 — The missing-projection control also removes the mass

- Claim: relays/cards/AGY-EXP_X-APEX-1_e8-dual-e6-bridge-chiral-2d-parity-and-cusp-banach-contraction.md:27,
  "omitting the harmonic projection drops".
- Source: relays/x_apex_1_verify/verify_x_apex_1.py:511,525 retains
  "mq_val = 1" in the positive case.
- Source: same file:569-572 computes the control from the massless
  flat Laplacian alone, with no projected positive-case operator.

Removing a projection from the massive positive-case matrix would
leave its constant eigenvalue positive. The control instead changes
the operator by removing its mass. Its zero therefore does not test
the projection failure named by the card. Keep it as a massless-
Laplacian control or test the actual projection on the same operator.

## XA-03 — The wall gradient omits normal Fourier variations

- Claim: relays/AGY_EXP_TO_PHYSICAL_AND_CC_2026-11-17_X_APEX_2_RESULTS.md:18,
  "non-unwinding positive relaxed wall tension" in the stated 2D parent.
- Source: relays/x_apex_2_verify/verify_x_apex_2.py:133,165 varies only
  "w_int.reshape(n_int - 1, 3)" for a(x), f0(x), f1(x).
- Source: same file:140-148 contains the two-mode covariant term and
  the averaged nonlinear moment energy; :192 returns only that gradient.

For q=f0+f1 exp(iy), the untruncated moment contains
2 Omega f0 f1 cos(y). Its nonlinear q equation contains the Fourier
coefficients f0^2 f1 at mode -1 and f0 f1^2 at mode 2, in addition
to modes 0 and 1. With A_y independent of y, the linear covariant
term preserves Fourier mode and cannot supply those coefficients.
Where the two profiles overlap, the omitted normal equations therefore
need additional fields or modes. Their residual is neither varied nor
reported here. A small restricted three-function gradient does not
establish stationarity of the full 2D parent. Both size runs at
:244-245 also keep the same mesh spacing; they test size, not mesh
refinement. This finding does not exclude a completed 2D solution.

## XA-04 — A Dirichlet cusp Ritz value is used as a full physical gap

- Claim: relays/AGY_EXP_TO_PHYSICAL_AND_CC_2026-11-17_X_APEX_3_RESULTS.md:19,
  "unconditionally eliminating `PR-10` `Branch A`".
- Source: relays/x_apex_3_verify/verify_x_apex_3.py:320-323 specifies
  "sin(m * pi * y / L_y)" on the finite interval [0,L_y].
- Source: same file:380-383 compares two 48-mode Dirichlet cusp
  calculations and a pointwise lower bound for that tail potential.

The sine basis imposes zero values at the cut and outer endpoint.
The complete manifold/core matching is absent. Rayleigh-Ritz minima
are upper bounds on the corresponding complete spectral infimum;
a large restricted value cannot supply the asserted lower bound for
the full physical operator. The tail potential bound is also confined
to that tail and its prescribed cross-section. A nontrivial cusp spin
structure removes the periodic transverse channel, but this calculation
does not exclude core modes or derive the full physical mass used to
choose Branch B. This scopes the inference, not the spin-bordism claim.

## XA-05 — The Branch-B minimum uses a newly chosen mass model

- Claim: same X-APEX-3 result note:19 again calls the branch choice
  unconditional.
- Source: relays/x_apex_3_verify/verify_x_apex_3.py:423,
  "m_broken_gauge = m_spin_cusp * mp.mpf(2)".
- Source: same file:430-433 assigns the species weights -34, -29
  and 315/2 to three Bessel terms.

The selected mass ratio and weights define the potential being
minimized. They are not read from a computed physical mass operator,
full mode spectrum or domain in this routine. The comment at :429
chooses their ultraviolet sum to match the desired supertrace. A
minimum of this supplied potential cannot close the parent spectrum
or mass-ratio duty. Those inputs must be derived or stated as borrowed
premises before calling the result unconditional.

## XA-06 — A finite grid and one Newton basin do not certify uniqueness

- Claim: X-APEX-3 result note:18, "unique global minimum".
- Source: relays/x_apex_3_verify/verify_x_apex_3.py:213-231 uses a
  48-by-48 grid with winding cutoff 90, followed by one guarded
  Newton solve at cutoff 360.
- Source: same file:274-286 checks the returned point and its local
  Hessian, with no global remainder or exclusion certificate.

These tests identify a numerical candidate and its local stability.
They do not rule out an intervening lower basin, another degenerate
minimum or a finite-cutoff change. Narrow the theorem/uniqueness
wording or supply an analytic/global bound for the stated potential.
This does not assert that the candidate minimum is wrong.

## XA-07 — The written Weyl element has order four, not two

- Claim: the X-APEX-1 card:14 calls W_swap a "Weyl involution".
- Source: relays/x_apex_1_verify/verify_x_apex_1.py:206,
  "perm = [4, 3, 5, 0, 1, 2, 6, 7]".

The permutation sends e0 to e4 to e1, so its square does not fix e0.
It is the disjoint product (0 4 1 3)(2 5) and has order four. The
source's conjugacy and determinant tests do not test an involution.
Correct that word or supply a different involutive witness; the
centralizer dimensions do not depend on this correction.
