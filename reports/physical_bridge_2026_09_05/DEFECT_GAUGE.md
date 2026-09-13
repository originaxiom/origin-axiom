# R29: a coupled finite-width source, and the gauge mass it does not retain

2026-09-13. Path-local added-model result, not a main B arc or a complete TOE.
The design, proof, producer and tests were sealed and pushed at **f8bb9fba**
before scientific execution. [Design](DEFECT_GAUGE_DESIGN.md),
[argument](DEFECT_GAUGE_PROOF.md), [pre-seal intake](DEFECT_GAUGE_PRESEAL_PRIOR.md).

## Result

The added charge-four tube fields give a stationary zero-residual
classical source construction on compact truncations. They avoid the
whole-manifold parallel-Higgs obstruction because their domains are
contractible tubes, not the whole manifold. The resulting extra-U1
transverse vector operator is derived, including internal profile
variation. At finite radius on a compact truncation its lowest
eigenvalue is positive.

The bare shrinking-tube version does NOT retain a positive gauge gap
on the stated bulk Hilbert space, however large its nonnegative
localized mass coefficient becomes. The constant-profile mass estimate
can stay finite while the spectral bottom tends to zero. This is a
capacity effect, not a failure of the finite-width solution and not an
exclusion of renormalized defect theories.

Neither result supplies the resolved fermion domain, anomaly completion,
a measured spectrum or an object-selected source. The old conditional
three/zero kernel remains on its original singular domain.

## 1. The positive: source density carried by an actual varied field

Use the actual R21 H subgroup, with D5-singlet character q=4. The exact
Cartan-lattice calculation rechecks that character and retains the global
order-three holonomy obstruction. No fundamental 27 of E6/Z3 is imported.

The declared model adds a charged complex Q_a on each contractible tube
U_a, weight sigma_a, a positive potential fixing its input amplitude v_a,
and the residual

    D = div h - kappa sum q_a sigma_a |Q_a|^2 1_(U_a).

Its potential is the sum of C|dh|^2, C D^2, gauge curvature energy,
sigma_a |D_i Q_a|^2 and sigma_a lambda_a (|Q_a|^2-v_a^2/2)^2.
Four-dimensional covariant kinetic terms are included. Both the scalar
equation and the gauge current are varied; rho is not held fixed while
varying Q. Natural tube conditions are stated in the proof.

On a compact smooth truncation with nonempty boundary, take parallel
Q_a=v_a/sqrt(2) on each tube and the original flat connection. The
Dirichlet Poisson construction

    Delta F = kappa sum q_a sigma_a v_a^2/2 1_(U_a),  h=dF

sets every residual to zero. This is a coupled stationary minimum of
the specified nonnegative static functional. The Hessian is a residual
Jacobian square, not asserted strictly positive. The global existence
argument uses the standard weak Poisson problem; no numerical solve
of the actual global originating geometry is claimed.

In the exact hyperbolic tube,

    sigma=1/(pi*sinh(epsilon)^2),  beta=kappa*q*v^2/(4*pi),
    h_r=beta*tanh(r)/sinh(epsilon)^2 inside,
        beta/(sinh(r)*cosh(r)) outside.

The field is regular at the axis and continuous/piecewise smooth at the
join. Its integrated dynamical density equals the exterior side flux.
Removing the shift recovers R28's bare nonzero core cost.

The costs remain explicit: tube localization, sigma, v, coefficients,
outer data and the bosonic action are supplied. In particular this is
NOT a full-parent supersymmetric completion; omitted allowed couplings
such as a full-parent h--Q potential have not been shown absent or
radiatively protected. Their addition can change the solution.
Zero-extension of Q would be a different, discontinuous construction.

Uniform per-axis normalization also makes a collective Q amplitude's
kinetic weight proportional to axis length. Infinite-axis continuation
is not a finite-norm complete end-sector solution. Changing beta retains
R28's logarithmic bulk kinetic cost. A fixed nonnormalizable background
is not thereby forbidden, but is not an ordinary 4D scalar modulus.

## 2. The actual gauge operator, not the constant-profile estimate

Transverse four-dimensional fluctuations have

    H_epsilon = -Delta_M + g7^2 sum q_a^2 v_a^2 sigma_a 1_(U_a).

Here g7 denotes the input coupling defined by the central-component
kinetic term, not an asserted equality to a parent-normalized or measured
coupling. The phase and A_i mixing is longitudinal and does not remove this
transverse operator. The central h commutator vanishes. Its Hilbert
space is bulk L2, with the specified gradient/potential form domain;
it is not a field living only on the source line.

On compact M_S let delta be the Neumann Poincare gap, mu=average V and
K=ess sup V. The derived finite-radius bound is

    lambda0 >= mu*delta/(2*delta+mu+2*K) > 0.

No numerical value of delta on the actual cusp geometry was produced.
Removing Q restores the constant zero mode. The uncharged D5 vectors
remain massless in this restricted model; it is not yet SM breaking.

The normalized constant mode has expectation average V. Uniform tube
normalization can make this independent of epsilon, but it is only
a Rayleigh upper bound. In the complete space the constant need not
even be in the potential form domain if the integrated weight diverges.

## 3. The thin-limit result, including the actual cusp

In the exact hyperbolic tube the profile zero inside epsilon and one
outside R, with logarithmic interpolation in tanh(r), has energy

    2*pi*L / log(tanh(R)/tanh(epsilon)) -> 0.

It pays NO potential cost, regardless of the nonnegative mass height
inside the excluded tube. Finite chart products, endpoint controls
and smooth approximation extend the argument to finitely many compact
smooth source arcs. Thus the spectral bottom tends to zero on a fixed
compact bulk space.

For the complete finite-volume cusp, an outer cutoff at S has gradient
energy (A/2)(1-exp(-2))*exp(-2S). First avoid the finitely many source
segments meeting that cutoff, taking epsilon->0; then take S->infinity.
The denominator tends to the nonzero total volume. This proves the
same spectral-bottom conclusion without claiming compact resolvent,
full spectral convergence or an isolated new massless particle.

Increasing the bare positive Higgs strength alone cannot defeat these
trial profiles. That is the precise constrained mechanism. Finite
physical widths, changed metric/kinetic domains, renormalized defect
fields, bulk condensates and nonabelian source theories are not excluded.

A literal positive line-mass term has a further problem: it is not
closable on bulk L2. Smooth approximations to the proof's shrinking
logarithmic profiles tend to zero in bulk H1 but retain a fixed line
trace. Differences have zero trace while each individual line energy
stays positive. This is the explicit failure of closability, not just
a statement that delta functions are informal.

## 4. Two-sided independent spectral controls

The flat Fourier rank-one matrices are a TOY, not a hyperbolic
discretization. At eta=0.25 their actual smallest eigenvalues are:

| cutoff N | matrix size | smallest eigenvalue | constant-only estimate |
|---|---:|---:|---:|
| 1 | 9 | 0.095057305 | 0.25 |
| 2 | 25 | 0.073838779 | 0.25 |
| 4 | 81 | 0.058447456 | 0.25 |
| 8 | 289 | 0.047563266 | 0.25 |

Independent symmetric diagonalization agrees with the secular root;
the exact square-shell bound proves the all-cutoff vanishing, not an
extrapolation of these four numbers. A uniform positive mass instead
keeps its exact gap; no Higgs returns zero.

One transverse dimension is an important positive comparator: its
mode sum converges and the corresponding delta form has a continuous
H1 trace and a uniform positive lower bound. The dimensional qualifier
is essential; localized Higgs fields are not universally ineffective.

de Rham's primary scalar-brane renormalization formula, (25), is checked
with its exact sign and inverse. Its positive renormalized EFT is kept:
the bare positive shrinking-support result is not a prohibition of
renormalization, extra brane fields or a changed operator domain.
[Primary paper](https://arxiv.org/abs/0707.0884).

## 5. What changed toward the physical goal

This supplies an actual finite-radius field carrying the source density
in a declared coupled classical model. It also prevents using its
constant-profile mass estimate to claim removal of the extra U1 at
zero radius. The useful next task is consequently sharper:

1. Derive a fermionic source/end sector and its variational domain for
   a finite-width or explicitly renormalized completion.
2. Recompute the charged spectrum and full anomaly in that same model.
   Replacing h~beta*dr/r by a smooth core is not R26's bounded
   regular-interior perturbation, so the original three/zero result
   cannot be transferred by citation.
3. Compute normalized gauge-current overlaps as well as masses.
   A light extra vector is not automatically excluded or decoupled;
   this round supplies neither its full matter couplings nor bounds.
4. Price or derive the source widths, fields and parameters; check a
   full-parent lift, omitted couplings and the complete cusp limit.

The anomaly-free R21 added-field construction remains a positive.
The R25 mirror result remains scoped to its wall and gauge background.
This round solves neither by assumption. SM interactions, selection,
gravity and observational predictions remain common-theory duties.

## 6. Verification and custody

The first native run passes all **29 checks**, exit zero, in 3.6301 s
inside the producer (4.7463 s including process startup). The **24 new
tests pass in 5.10 s**. The six-file focused run passes **92 tests in
84.24 s**. The **51-file broad run** completes at exit one:
**428 pass / 16 fail / 8 error**, one optional-GUI warning, in 368.72 s.
Its test population is exactly R28's 50 files plus the new file;
its 24 failed/error IDs are exactly R28's, none added or missing.

All runs have durable exclusive captures. The native/new/focused public
outputs are byte-identical to raw; the broad output redacts only declared
environment prefixes. Scientific assertions and tolerances are unchanged.
[Native output](DEFECT_GAUGE_NATIVE_FIRST.json),
[new tests](DEFECT_GAUGE_TESTS_FIRST.txt),
[focused](DEFECT_GAUGE_FOCUSED_FIRST.txt),
[broad](DEFECT_GAUGE_REGRESSION.txt),
[commands, digests and exact population comparison](DEFECT_GAUGE_RUN_RECEIPTS.json).

The tree remained read-only throughout science. Pre-execution metadata
recomputed all 63 design seals and 393 latest-row artifacts correctly;
older literal-provenance and static-vacuity debts were not waived.
[Pre-execution record](DEFECT_GAUGE_PREEXEC.txt).
Reporting gates give 26 PASS / 4 FAIL, with all four failed-detail strings
unchanged from the preceding checkpoint. All 400 then-latest artifact hashes
and 63 design seals match; 292 relative links resolve. The existing debts
remain. [Final reporting checks](DEFECT_GAUGE_FINAL_CHECKS.txt) preserve the
complete gate output and distinguish post-run receipt/hash checks from the run.

One additional incoming producer was read after sealing: B1402's
decomposition script. Its shadow group is explicitly enumerated, but
its lambda readouts are literal inputs; this is not an independent
regeneration of those readouts. It was not executed here or used in
R29's source/gauge argument. The earlier intake's read boundary and
immutable remote pins are retained.

No new B number, branch merge, PR, main bank or external relay.
The original proof/design/source/tests stay unchanged from f8bb9fba.
Their pre-run wording is retained as provenance; this report supplies
the executed disposition. Author-side controls do not replace
independent proof review or full-repository verification.
