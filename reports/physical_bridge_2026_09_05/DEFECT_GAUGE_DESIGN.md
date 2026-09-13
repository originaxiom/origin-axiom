# R29 — dynamical tube fields and the transverse gauge spectrum

2026-09-13. Pre-execution design; no empirical target or B allocation.

BANKED IDENTITY: R21's actual H subgroup has primitive D5-singlet
charge four, nonparallel under the existing nontrivial order-three
whole-manifold holonomy. R28's commuting smooth core is exactly
supported by a prescribed moment-map shift; a physical field carrying
that shift was not yet supplied there.

PRIOR ART: DEFECT_GAUGE_INTAKE_2026_09_13.md and
DEFECT_GAUGE_PRESEAL_PRIOR.md. R16 already has a weighted local
capacity calculation. Positive defect renormalization is established
prior art, not excluded by a bare positive-potential limit. The full
argument to be checked is DEFECT_GAUGE_PROOF.md.

## P0--P6 and priced model

P0: compute a declared added H bosonic theory on compact connected
truncations with contractible source tubes, then a separate spectral
limit for shrinking supports on fixed compact or complete finite-volume
hyperbolic three-manifolds with finite proper smooth source arcs.
Both rows/members are covered only when these analytic hypotheses hold.
No object-level source selection, actual m202 numerical spectrum or
physical coupling prediction is inferred. Flat Fourier matrices have
their own toy-domain quantifier.

P1--P4: PB-BOUNDARY/X33 is the existing source/end duty. Full prior
retrieval, relevant laws, leads and kill-graph hatches were read.
The present calculation changes the whole-manifold scalar hypothesis
of R21/R22 explicitly; it does not repeat or refute that restricted
obstruction. It keeps their source-domain and anomaly duties visible.

P6: expect a positive finite-width classical construction, but loss of
a bare localized gauge gap in a shrinking codimension-two limit.
If a variational identity or spectrum control fails, retain the first
run and do not promote the affected claim. No universal defect kill.

Take H=C_(E6/Z3)(u) as in R21. Inputs: fixed internal metric/flat H
bundle, prescribed contractible tube domains/weights, q_a=4 unless
signed explicitly, positive C,kappa,g7,lambda_a,v_a, Minkowski 4D
spacetime, and the action in the proof. Q fields live only on tubes
with natural covariant Neumann data. The source densities are varied
through Q, not independent fixed rho. The density shape and scale
remain inputs. No zero-extension, full-parent representation supply,
supersymmetric completion, missing |hQ|^2 term or natural hierarchy is
smuggled in. Additional fermions are not part of this bosonic round.

Seal this design, proof, new producer and tests in ARTIFACT_HASHES and
SEAL_LEDGER, commit and push before first scientific import/execution.
Keep the tree read-only during native/test runs and preserve every
first stdout, failure and exit status. No tests compare observations.

## A. Gauge covariance and all coupled equations

Derive the Cartesian local density and its gradients in h-divergence,
curl, Q components, Q derivatives and gauge variables. At the claimed
zero-residual solution every component must vanish. Its Hessian must
equal the positive weighted residual-Jacobian square, without claiming
strict positivity. Nonzero wrong source, wrong vacuum amplitude and
omitted connection/phase-derivative controls must fail the respective
identities. Retain the full Q derivative of the source moment map.

Check the allowed charge-four character from the exact R21 Cartan
lattice and the unchanged order-three holonomy. Contractible restriction
is a mathematical input, not a finite computed census of all tubes.
Use the standard Dirichlet Poisson existence argument for the compact
construction and the exact hyperbolic core for explicit verification.
No whole-geometry Poisson solve is claimed.

## B. Core and vector normalization

Use dr^2+sinh(r)^2 dtheta^2+cosh(r)^2 dz^2, period 2*pi and length L.
Derive the unit cross-section weight, sourced rho and beta relation,
regularity, side matching, zero cap flux and integrated source. The
joined core is continuous/piecewise smooth, not globally C-infinity.

Derive the actual four-dimensional transverse-vector quadratic form
including internal derivatives and phase mixing. Check its coefficient
g7^2 q^2 v^2 sigma and the independent transverse cancellation. The
constant matrix element is an upper bound, never a lowest-mode claim.
Check the finite-radius Poincare bound algebra and its V=0 control.

## C. Small capacity with the actual metric and ends

Compute the exact logarithmic harmonic radial cutoff energy and endpoint
values; check by numerical quadrature at (epsilon,R)=(.01,.2),(.003,.4),
with relative tolerance 2e-10. A wrong Euclidean weight must not satisfy
the same exact harmonic identity. Include axial cutoff/L2 bounds.

Verify the cusp exhaustion gradient integral and tail-volume bound.
The all-small-radius and all-source-strength result is the explicit
variational proof, not a finite epsilon sample. Preserve the ordered
epsilon->0 followed by S->infinity, and no compact-resolvent claim.
Spell out the nonclosable line-trace sequence and its smooth
approximation. Do not transfer that statement to weighted fermion domains.

## D. Independent finite-mode and renormalization controls

Use the flat rank-one Fourier matrices for N=1,2,4,8, eta=.25,1.
Direct symmetric eigenvalue computation and the secular equation must
agree to absolute 3e-10; eigenvector residual must be below 3e-10.
Check the upper bound and exact shell sum S_N>=4 H_N for N=1..8.
Missing every nonzero mode returns eta and is the intentionally wrong
truncation. A uniform positive mass and eta=0 recover known opposites.

Compare one transverse dimension at eta=.25, N=1,2,4,8,16,32,
including its uniform lower bound. This numerical comparator does not
prove the hyperbolic theorem. Check de Rham (25)'s rational identities,
positive-bare bound, inverse coupling pole and sign-changing control;
the paper's positive renormalized EFT is not discarded.

## Outcomes and verification

Report finite regulated coupled existence, the actual gauge operator,
finite-width positivity, shrinking-support spectral-bottom behavior
and literal line-form domain separately. Distinguish old capacity prior
from its present gauge consequence. No anomaly, SM, chirality-domain,
source-selection or TOE closure.

First native command uses the established Python 3.12 environment and
durable exclusive capture. Run the new mathematical tests, focused
R21/R22/R26/R28 controls, then exactly R28's broad population plus this
new file. Compare failed/error IDs; no old assertion or tolerance edit.
Reporting gates are recorded without waivers. Independent proof
review and main acceptance remain outstanding; push only this branch.
