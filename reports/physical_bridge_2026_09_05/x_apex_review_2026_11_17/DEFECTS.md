# X-APEX source defects

Source head 5de6493f5f1a0300dca64c0fb90afd26925ef1c9.
All four cards, result notes, scripts and JSON outputs have been read
in full at that head. The supplied hash files were checked as bytes.
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

The other wall retained by the final synthesis is also a restricted
control. Its script at :2637-2639 defines one scalar c and the supplied
sine-squared potential, while :3472 names its output an E6 joining BVP.
It constructs no full E6 field X(c), real Gauss response or normal
operator there. Its tiny scalar ODE residual does not resolve that
earlier C5/C6 physical-field duty.

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

The final matrix repeats the inference as unconditional pure mathematics
at relays/x_apex_4_verify/verify_x_apex_4.py:4164-4171. Its helper at
:183-225 is again the finite Dirichlet sine calculation. The changed
matrix row therefore retains the same gap in scope.

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

The final script's retained PR-10 control at :2999-3053 uses different
species weights, twists and circumference 4 L4, and still calls Branch
B conditional. Stage three is not simply substituting its cusp mass
into that same operator. These are distinct mass-model choices that
must be reconciled before combining their conclusions.

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

## XA-08 — The central-scalar correction did not reach the master row

- Claim: relays/x_apex_4_verify/verify_x_apex_4.py:4093 writes
  "non-projective (ST)^3 = S^2 = C" in the unconditional row.
- Source: same file:2583-2585 defines S=gamma^-1 F, with F the
  normalized finite Fourier transform.
- Contradicting row: same file:4156 states the central parity scalars
  "(-1, +1, -1) on N in {3, 5, 15}". The gate requires this at :4320.

Since F^2=C, the written generators obey S^2=gamma^-2 C. At the
tested dimensions three and fifteen the required scalar is -1, so
the first row's S^2=C is false for those very witnesses. The test
at :3522-3524 compares (ST)^3 with S^2 and never with C. Preserve
the nonprojective relation and CRT computation, and carry the central
factor into the first row, its JSON statement and downstream uses.
This is the earlier scalar correction failing to travel, not a
refutation of the correctly normalized Weil construction.

## XA-09 — The final norm witness reverts to a different metric

- Claim: same script:4267-4270 names the P-C3c..f parent cubic and
  triplet mass relations, using "triplet_sigma_star_live".
- Source: same file:2896-2899 instead sets
  "om = mp.mpf(1) / (rv * (mp.mpf(1) + abs(mp.log(rv))))".
- Source: same file:2912-2927 uses one quadrature level and a sharp
  disk indicator. The master gate requires sigma greater than 17/25
  at :4331, where its literal is 0.68.

This does not use the hyperbolic uniformization or smooth partition
introduced in the preceding X-SYNTHESIS-1 repair. That repair's result
note, lines 17 and 23-29, reports its different source metric and refined
sigma in (4041/10000,4043/10000). Its script passes the solved metric
into the norm calculation at :433,447 and :584-591. These earlier
numerical values are received evidence, not recomputed here. The
source comparison itself shows that the final witness changes its
metric and quadrature again. Its old seed-specific sigma threshold
cannot certify the repaired parent norm. Identify and transport the
same metric and normalization before promoting this witness.

## XA-10 — The new resolvent trajectory does not receive the advertised precision check

- Claim: the X-APEX-4 result note:20 places the new resolvent infrared
  trajectory beside the f64/mpmath and full-flow Haar certificates.
- Source: relays/x_apex_4_verify/verify_x_apex_4.py:3884-3887 builds
  the new resolvent in f64; :3931 calls eval_vector_f64 with its inverse.
- Source: same file:3943 compares "vec_cas_111" with "obs_m32".
- Source: same file:3958-3999 builds the full-flow Haar input from
  build_zero_knob_uv_state_mp and its old puncture-jet M_R, not the
  new six-plet resolvent. The U6 check at :3894-3903 is separate.

The precision and full-flow covariance receipts bind the equal-weight
puncture-jet state. They cannot be read as numerical certificates for
the resolvent trajectory. The latter's separate U6 and T checks remain
what they test. Label every certificate by the actual state/operator,
or apply the requested comparisons to the same new resolvent state.
This does not assert that the new trajectory is numerically wrong.

## XA-11 — The zero-bit Frame-C infrared vector imports a selected vacuum's scales

- Claim: same script:4407 names the delivery
  "zero_bit_frame_c_gramian_vector"; :4210 uses its infrared ratio
  as the witness for the zero-bit Gramian row.
- Source: same file:3748 constructs uv_mp at the selected point
  (4/15,8/15), while :3768-3777 forms the level-five averaged Gramians.
- Source: same file:3784-3793 obtains s1_top, s2_top and s3_top from
  that uv_mp, rescales each averaged sector to those selected values,
  and runs the nonlinear RGE with the selected normalization.

UV singular-value ratios of an averaged Gramian do not depend on an
overall sector scale. Their nonlinear infrared running does. The
reported infrared extension consequently inherits this selected
vacuum's three scales; it is not a selection-free consequence of the
average alone. This finding leaves the UV Gramian and its covariance
intact, including main's new A2-AMP correction. Price this normalization
or derive one from the same averaged construction before labelling
its infrared vector zero-bit.

## XA-12 — Finite-height determinants are labelled leading-coefficient certificates

- Claim: same script:4129 states
  "zero leading-minor phase cancellations across all 288 torsion vacua".
- Source: same file:3313 evaluates tau_hi_minor at height six;
  :3328-3346 tests full matrices and determinants at that one height.

A nonzero determinant at a finite height does not establish that its
lowest cusp coefficient is nonzero. If a leading coefficient cancels,
subleading terms can still give a nonzero finite-height determinant.
The code does not extract those coefficients or bound the remainder
relative to the leading powers. The census remains a finite-height
check; the asymptotic statement needs a coefficient calculation or an
appropriate bound. This is not evidence that any particular leading
coefficient actually vanishes.

## XA-13 — Complete-flow convergence checks omit most fields

- Claim: same script:4189 says the 286 trajectories
  "converge smoothly" and :3498 reports their maximum step-halving difference.
- Source: same file:3385-3389 only compares lambda and Yu between
  the 600-step and 1200-step runs.

Yd, Ye, W4, the gauge couplings and the derived spectrum/current
observables are not included in that convergence metric. This does
not certify the complete state or all its small singular-value ratios.
Narrow the receipt to the two checked quantities or bind the stated
convergence criterion to the full delivered observables. No numerical
failure of an omitted field is inferred from its absence here.

## XA-14 — Every solver exception is classified as physical divergence

- Claim: same script:4189 says the two excluded points "diverge".
- Source: same file:3379-3382 uses "except Exception:" and appends
  every exception to blowup_records without its type or message.

An implementation error, SVD failure or finite-step overflow would
be counted in the same way as an actual ODE divergence. The receipt
does not preserve which event happened. The separately reported
large ultraviolet expansion parameter still marks those two points
outside the stated perturbative control. It does not turn every
caught numerical/programming exception into a mathematical blowup.
Preserve the first exception and its source, distinguish numerical
failure from a certified divergence, and keep the conclusion scoped
to the tested approximation.

## XA-15 — The advertised v17 reachability guard is a smaller syntactic check

- Claim: the X-APEX-4 card:13 names "source-reachability checks" and
  explicitly includes a ban on "itertools.count synthesis".
- Source: relays/x_apex_4_verify/verify_x_apex_4.py:67-73 lists only
  Counter, ChainMap, defaultdict, deque and reduce as forbidden names.
  The visitor at :81-115 checks imports, names and selected function
  bodies, without constructing or following a call/dependency graph.

The allowed itertools module and an attribute call itertools.count()
are not rejected by these conditions. Nor does the selected-function
literal check traverse ordinary helper calls. These are hand-traced
static countercases, not executed planted-error fixtures. The existing
script need not use either route for the claimed guard coverage to
be too broad. Implement the stated dependency rules or name this as
the narrower import/name/literal audit actually performed. Its pass
cannot serve as a full v17 reachability or derivation certificate.
