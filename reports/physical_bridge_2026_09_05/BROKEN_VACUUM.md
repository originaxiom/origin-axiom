# R8: neutral and charge-breaking leading minima; full fermion rank retained

The specified compact-E6 model now has an explicitly solved **leading
electroweak-broken light-field potential**, not just negative Higgs masses.
Its neutral minima preserve the actual color algebra and Q=T3+Y. However,
charge-breaking minima have the same leading energy: existence is computed,
electromagnetic vacuum selection is not. All physical leading zero modes
are retained. The full neutral fermion matrix has rank 27 at the evaluated
backgrounds, including a small seventeenth light mass absent from the
rank-16 leading light projection.

These are conditional physical-model calculations, not a source-derived
action, a completed quantum vacuum, pole masses, observed families, or TOE.
They do not reset the already verified 14-to-12 reduction to an open gap;
see [the recovery receipt](RECOVERED_PHYSICAL_STEPS.md).

Design, code and eight tests were sealed together at **6a02639d** before
execution. The first scientific run succeeded in **60.23 s**. Its complete
[output](broken_vacuum_first_run.json) and [captured checks](BROKEN_VACUUM_CHECKS.txt)
are retained. [EXTENSION_6.md](EXTENSION_6.md) keeps its pre-execution wording
and hash unchanged; this document records the subsequent disposition.

## 1. Fixed model and controlled expansion, not an RG flow

Use R7's four scalar 27s, real adjoint and one Weyl 27, with its compact
positive kinetic metrics and MS-bar/Landau-gauge one-loop convention.
Four-dimensional spacetime, field content, the scalar action, its tuned
offset a=1/2, coupling ratios and renormalized boundary conditions remain
inputs. This is not an identification of that action with the program's
E6(-26) geometric representation. Other allowed operators have not been
shown absent or radiatively protected.

For the predeclared epsilon=.01 and .0025, every tree-potential coefficient
is multiplied by epsilon, g=.5 sqrt(epsilon), all Yukawas=.25 sqrt(epsilon),
and mu=sqrt(epsilon), keeping high VEV units fixed. These are different
weakly coupled theories, **not running one theory between two scales**.
Tree squared masses scale as epsilon, the full one-loop force as epsilon
squared, and the leading normal displacement as epsilon. Fresh scaled
instruments recompute all 3x294 scalar/Weyl/vector force components at each
epsilon; the normalized maximum discrepancy is 2.06e-15.

The leading Higgs coordinates are order sqrt(epsilon), their potential
depth is order epsilon cubed, and their squared curvatures are order
epsilon squared. Small expansion parameters and the checks below do not
constitute an all-orders error bound. In particular, the unevaluated next
order matters on directions flat at leading order.

## 2. Keep the entire physical tree kernel and integrate heavy exchange

The 294-real-scalar tree Hessian has 209 positive modes and 66 gauge
directions, leaving 19 physical light coordinates:

```text
x = (O[8], T[3], u[4], d[4]),  ||U||^2=u^2/2, ||D||^2=d^2/2.
```

Actual E6 generators construct O and T; actual weight actions identify U,D.
All 19 coordinates are kinetically orthonormal, belong to the constraint
kernel, are orthogonal to the full gauge orbit, and close under all twelve
SM generators. Maximum geometry residual is 2.04e-15, not a count inferred
from a branching label alone.

Write the quadratic constraints as c(z0+Lx)=C2(x), with J L=0. Solve for the
quadratic heavy response N(x) on **all 209 positive modes**:

```text
H0 N(x) = -2 J^T W C2(x),
V4(x) = (C2(x)+J N(x))^T W (C2(x)+J N(x)).
```

All 190 quadratic monomials and all 7315 quartic monomials are accounted
for. The analytic response is N_A=-(O^2+T^2)Y/10; other components vanish.
It cancels the adjoint-norm constraint since Tr27(Y^2)=5. O,T commute with
Y and annihilate the high singlets. The surviving Higgs norm and triplet
action residuals are orthogonal to J's image. Thus the effective quartic is

```text
V4 = .2/4 (u^2)^2 + .2/4 (d^2)^2 + .02/24 T^2 (u^2+d^2).
```

There is no relative-doublet orientation term at this order. This rational
analytic expression agrees with every numerically eliminated coefficient:
44 are nonzero, maximum coefficient discrepancy 5.56e-17. The normal
response and stationary-equation discrepancies are below 4.45e-15.
The factor 1/12 in the canonical weak-generator square is also checked
symbolically on both doublets, using Tr27(t_a^2)=3.

Omitting heavy exchange leaves the false pure-octet quartic .2; including
it gives 1.08e-30 numerically, in agreement with analytic zero. The original
potential along z0+t Lx+t^2 N(x), for t=.04,.02,.01,.005, converges to the
quartic prediction. The last error is 2.70e-8 on a predicted coefficient
.00199780306 (relative 1.35e-5), passing both predeclared controls.

## 3. Solve the complete leading potential, including both orientations

Independently compute the entire 19x19 one-loop light curvature and add the
leading normal-shift tree contribution once. It agrees with the predicted
irreducible blocks to 2.91e-16 and commutes with every actual SM action.
Write its eigenvalue coefficients as kappa, to avoid confusing a negative
coefficient with a positive mass:

| block | multiplicity | kappa at reference mu=1 |
|---|---:|---:|
| color octet O | 8 | +.007519833193 |
| weak triplet T | 3 | +.007366050627 |
| U doublet | 4 | -.018284666133 |
| D doublet | 4 | -.020847297820 |

The light potential, up to an orientation-independent constant, is

```text
Vlead = epsilon^2/2 (kappaO O^2+kappaT T^2+kappaU u^2+kappaD d^2)
      + epsilon V4.
```

Positive octet/triplet coefficients and the nonnegative triplet-Higgs
interaction force O=T=0 at every global minimum **of this leading EFT on
this high-scale branch**. Completing the two radial squares gives

```text
u^2 = -epsilon*kappaU/.2,  d^2 = -epsilon*kappaD/.2,
Vmin/epsilon^3 = -(kappaU^2+kappaD^2)/.8 = -.000961173552454.
```

Relative orientations remain arbitrary at this order. Both evaluated
representatives have the same energy and a vanishing full 19-component
gradient, with normalized error below 1.74e-17. Their 19x19 Hessians have
13 positive eigenvalues and six angular zeros. Dividing squared masses by
epsilon squared gives eight copies of .007519833193, three of
.007692150326, radial values .036569332265 and .041694595639, and six zeros
(numerical residuals below 4e-17).

This is an analytic minimum of the leading potential, not a sampled
assertion that it beats every other high-scale branch or persists as the
same minimum in the complete quantum theory.

## 4. Actual gauge actions distinguish the neutral and charged states

At each epsilon construct z=z0+Lx+epsilon*delta+N(x), using the complete R7
normal shift. Compute the full 78-generator action with the positive scalar
and gauge kinetic metrics. Do not count only the projected SM generators.

| representative | nonzero Higgs weight indices | unbroken gauge dimension | broken EW generators | remaining physical leading scalar zeros |
|---|---|---:|---:|---:|
| neutral | U:8, D:22 | 9 = color 8 + Q | 3 | 3 |
| charge-breaking | U:8, D:21 | 8 = color only | 4 | 2 |

The actual color action vanishes on both backgrounds; Q annihilates only
the neutral one. All gauge tangents are annihilated by the leading light
Hessian to the tested precision. The smaller zero count in the charged
case reflects an extra eaten mode, not greater vacuum energy or stability.
All 78 vector squared masses are retained, including numerical zero
residuals; they are not silently clipped.

The neutral projected W,W,Z squared masses obey mZ^2/mW^2=8/5, conditional
on this action's chosen unified gauge metric. This is not a new measured
weak-angle prediction. Relative full/projected light-vector errors decrease
from 1.75e-4 to 4.36e-5 (neutral), and 2.64e-4 to 6.57e-5 (charged), when
epsilon decreases from .01 to .0025.

The usual strict neutral-versus-charge-breaking minimum comparison uses a
positive charged-scalar squared mass; we are instead on a flat boundary.
Inferring strict selection from that theorem here would discard the actual
zero modes. See Branco et al., [section 5.9, equation (198)](https://arxiv.org/pdf/1106.0034v3).

## 5. The leading rank-16 projection is not the full fermion rank

Use the exact, kinetically orthonormal 27x17 kernel K of C(S+N). Compare
K^T M_H K with **all 27 singular values** of the full matrix evaluated at
the displaced broken background. The result is orientation-dependent:

| representative | leading projected rank / 17 | full numerical rank / 27 | exact rational finite-VEV control rank | cubic on S+N+u HU+d HD |
|---|---:|---:|---:|---|
| neutral | 16 | 27 | 27 | -u d |
| charge-breaking | 8 | 18 | 18 | 0 |

The separate exact control uses high singlets S,N unchanged and rational
Higgs amplitudes 1/10 and 1/9. Ranks and cubic are computed from the actual
B883/B884 tensor, not inferred from the leading projection. The full
neutral matrix also satisfies Q^T M+M Q=0.

In the neutral case the seventeenth light singular mass is
**1.22533519e-5** at epsilon=.01 and **1.52689624e-6** at epsilon=.0025,
in high-VEV units. The leading projection gives zero for it. Dividing by
epsilon^(3/2) gives .01225335 and .01221517: consistent with a subleading
mass, not an all-orders asymptotic proof. The projected/full light-spectrum
relative error falls from .022925 to .011427; the full successful output
retains the small mass rather than losing it behind a rank-16 label.

These are pointwise singular masses at the specified approximate
backgrounds. The exact control is a finite-VEV example, not a theorem about
all allowed couplings or the exact quantum vacuum. Higher-order background
corrections and self-energies are required before promoting the smallest
entry to a predicted physical pole mass. Neither the rank nor the cubic
supplies a three-generation or observed-neutrino identification.

## 6. A physical classical phase direction, with its anomaly retained

The full classical action admits psi->exp(i alpha)psi and all four scalar
27s->exp(-2i alpha)phi, with the adjoint unchanged. Polynomial terms have
definite common phase and appear through norms; the Yukawa tensor is
linear in phi. Generic complex-field controls check the potential and
Yukawa covariance to 5.56e-17 and 6.21e-17, respectively.

The exact SU5-commuting Cartan compensation satisfying Gc S=Gc N=2 is
Gc=(2,0,8/5,6/5,4/5,2/5) in the specified Cartan basis. Its residual scalar
charges are -18/5 on U and -12/5 on D. Projecting the combined phase tangent
off the **full** gauge orbit gives neutral physical norms .132399 and
.066206 at the two epsilons. The charged control's residual is numerical
zero: its larger broken gauge orbit compensates that phase. Neither count
is imposed on the other orientation.

However, Tr27[(1+Gc)(H_color/2)^2]=3 exactly. This is a nonzero mixed color
anomaly trace in the stated normalization, not a domain-wall number or an
axion mass. Thus no exact quantum Goldstone is asserted. The remaining
phase direction, nonperturbative effects and physical scales require
further calculation; an observational exclusion cannot be read from a
classical massless-mode count alone. The distinction between a scalar-only
phase and the full Yukawa symmetry is important in two-doublet models;
see Branco et al., [section 6.7.2](https://arxiv.org/pdf/1106.0034v3).

## 7. Verification and the next bounded physical task

The new R8 tests return **8 passed in 57.33 s**. The combined physical-audit
and selected upstream regression returns **99 passed, 3 failed in 96.30 s**.
Those three failures are the preserved original G2 NumPy-key exporter test
and the two original R7 small-step subtraction controls. Their separately
sealed repairs pass. No R8 failure or relaxed tolerance was introduced.
This is not the full repository suite and does not erase its earlier debt.
Final publication-gate disposition is recorded separately in
BROKEN_VACUUM_GATES.txt; no publication certificate is claimed.

The next physical task is the **first nonzero relative-Higgs orientation
potential**, retaining heavy-field response, scalar/gauge/fermion loops,
the complete allowed-operator counterterm basis and the input conditions
that set its finite coefficients. Evaluate neutral and charged competitors
and all residual modes consistently at that order. A pointwise unresummed
log of a negative Goldstone squared mass is not an automatic physical kill;
the issue and resummation are explained by Martin,
[arXiv:1406.2355](https://arxiv.org/abs/1406.2355).

Separately retain the full light-fermion matching problem, especially the
seventeenth mass, before redoing empirical coupling/threshold comparisons.
No new alignment term, inert parity, SUSY D-term, observed scale or absolute
value of a negative squared mass has been inserted to select a desired
answer. Selection of the action itself, physical families, spacetime and
gravity remain distinct obligations of the overall goal.
