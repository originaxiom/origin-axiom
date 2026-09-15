# R29: a coupled finite-width source, and the gauge mass it does not retain

## VERDICT AS THE SEAT STATES IT

"The added charge-four tube fields give a stationary zero-residual classical
source construction on compact truncations... The resulting extra-U1
transverse vector operator is derived... At finite radius on a compact
truncation its lowest eigenvalue is positive. The bare shrinking-tube
version does NOT retain a positive gauge gap on the stated bulk Hilbert
space, however large its nonnegative localized mass coefficient becomes...
This is a capacity effect, not a failure of the finite-width solution and
not an exclusion of renormalized defect theories."

## DECLARED INPUTS AND HYPOTHESES

- Prescribed: R21's actual H subgroup, D5-singlet character q=4, and "the
  global order-three holonomy obstruction" (rechecked, not re-derived from
  scratch).
- Added bosonic model: charged complex Q_a on each contractible tube U_a,
  weight sigma_a, potential fixing amplitude v_a; "Q fields live only on
  tubes with natural covariant Neumann data. The source densities are
  varied through Q, not independent fixed rho."
- Explicit exclusions: "No zero-extension, full-parent representation
  supply, supersymmetric completion, missing |hQ|^2 term or natural
  hierarchy is smuggled in. Additional fermions are not part of this
  bosonic round."
- g7 "denotes the input coupling defined by the central-component kinetic
  term, not an asserted equality to a parent-normalized or measured
  coupling."
- Exact hyperbolic tube geometry (dr^2+sinh(r)^2 dtheta^2+cosh(r)^2 dz^2)
  as the geometric setting for the explicit core solution.
- Renormalization comparator sourced from de Rham arXiv:0707.0884, eq.(25)
  — "this elementary algebra is a control on this positive-bare route, NOT
  a universal renormalization obstruction."
- Seals: sealed and pushed at `f8bb9fba` before scientific execution.

## CONTROLS

- "The Hessian is a residual Jacobian square, not asserted strictly
  positive" — avoids overclaiming a strict local minimum.
- "Nonzero wrong source, wrong vacuum amplitude and omitted
  connection/phase-derivative controls must fail the respective
  identities."
- Two-sided spectral control: flat Fourier rank-one matrices (a "TOY, not a
  hyperbolic discretization") at four cutoffs N=1,2,4,8 show the smallest
  eigenvalue shrinking below the constant-only estimate of 0.25, while "the
  exact square-shell bound proves the all-cutoff vanishing, not an
  extrapolation of these four numbers."
- Dimensional comparator: "One transverse dimension is an important
  positive comparator: its mode sum converges and the corresponding delta
  form has a continuous H1 trace and a uniform positive lower bound... The
  dimensional qualifier is essential; localized Higgs fields are not
  universally ineffective" — prevents overgeneralizing the codimension-two
  result.
- Closability control: explicit sequence u_n showing the literal positive
  line-mass term is "not closable on bulk L2" — "This is stronger and more
  precise than saying a delta function is undefined, but it is NOT a no-go
  for renormalized point interactions."

## TESTS ON THIS BENCH

`python3 -m pytest tests/test_physical_bridge_defect_gauge*.py -q --no-header -p no:cacheprovider`

`24 passed in 5.04s`

No failures. (The seat's own broader run reports a 51-file population at
428 passed/16 failed/8 errors with the "24 failed/error IDs... exactly
R28's, none added or missing" — not re-run here.)

## CLAIMS FOR MAIN

1. A finite-width, stationary, zero-residual coupled classical source
   solution exists for the charge-four tube model on compact truncations
   with boundary. — PROVED-BY-SEAT (conditional on the added bosonic
   model's stated inputs).
2. At any fixed finite tube radius on a compact truncation, the extra-U1
   transverse gauge operator has a strictly positive lowest eigenvalue. —
   PROVED-BY-SEAT (explicit Poincare-gap bound
   `lambda0 >= mu*delta/(2*delta+mu+2*K) > 0`; "no numerical value of
   delta on the actual cusp geometry was produced").
3. As the tube shrinks to zero radius, the spectral bottom of this gauge
   operator tends to zero regardless of the mass coefficient's height — a
   codimension-two capacity effect, not exclusion of renormalized/finite-
   width defect theories. — PROVED-BY-SEAT.
4. A literal delta-function line-mass term is not closable on the bulk
   Hilbert space (explicit non-Cauchy sequence). — PROVED-BY-SEAT.

## CONFLICTS WITH MAIN

Searched `git -C <repo> grep -l -F "<phrase>" -- docs frontier`
for "extra-U1" (one hit, frontier/B1306_the_older_debt/inputs/fc_codex_hostile_inventory.md
— an inventory listing, not a competing claim) and "not closable on bulk"
(no hits). NONE found that contradicts R29's stated result or scope.

## WHAT MAIN WOULD HAVE TO VERIFY

The R21 H-subgroup construction and its charge-four character (external to
this round); independently re-derive the Poincare-gap bound's constants
mu, delta, K for the actual m202 cusp geometry, since "no numerical value
of delta on the actual cusp geometry was produced" here.
