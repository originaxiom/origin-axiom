# R49: canonical neutral modes enter the nonlinear action domain

September 27, 2026. Original science sealed at f593a2a5;
post-failure comparison diagnostic sealed at 86c78ef0. Each was pushed
and server-confirmed before its own execution. Own branch only:
audit/physical-bridge-2026-09-05. No shared B/I number or main-bank claim.

## Result and evidence grade

For each fixed real q>0, q!=1, on the SAME R42/R44 canonical
finite-energy background, the complete End0(E) harmonic spaces are
finite-dimensional and their modes lie in Lp for every finite p>=2,
under the inherited all-jet cusp/core hypotheses. There is a positive
spectral gap on the orthogonal complement of the global harmonic
space, not a computed numerical global gap or full kernel dimension.

In particular R47's nonzero neutral harmonic projection belongs to
Dom(Q) intersect L4. Its quadratic bracket residuals have finite L2
norm. This pays the previously outstanding nonlinear ADMISSIBILITY
step in R46's supplied parent action.

**Grade:** authored analytic argument with explicit inherited/external
geometry, supported by exact finite operator checks. Not independent
specialist acceptance, a numerical global PDE solution, a nonlinear
solution branch, a selected q or a physical chiral spectrum.

## The operator, with its actual metrics

Use r=log(R)/2, v=2 log(q)t+r/2 and coframe
(dr,exp(-r)dx,dv). The limiting base metric is
diag(3/4,3/8,3/4); the induced positive defining coefficient metric,
up to an irrelevant common scalar on End0, is
diag(3/8,1/4,3/8,3/8). Neither is silently replaced by an identity.

With H0=diag(1,0,0,-1), N=E02+E23, D=diag(1,-3,1,1), set
A=ad(H0), B=ad(N), L=ad(D)/2. On the constant-meridian model sector,
every exterior degree has the coefficient operator

    Delta_inf(lambda,nu)
      = (4/3)[(-lambda^2+lambda+nu^2)I + T],
    T = A^2+A+2 B^*B+L^2.

The verified exact spectra of T are

| coefficient | eigenvalues and multiplicities |
|---|---|
| full fifteen-dimensional End0(E) | 0:1, 2:3, 6:11 |
| nine-dimensional zero-longitude-weight restriction | 0:1, 2:3, 6:5 |

These are end-operator channels, not particle or generation counts.
The extra six channels are retained. The coframe derivative and
the radial adjoint -partial_r+1 are load-bearing; omitting either
fails a discriminating control.

Density conjugation gives a model exterior threshold 1/3 in this
internal metric normalization. Nonzero meridian modes instead have
a decaying Cartan homotopy using B^5=0. All-jet metric convergence
transfers any lower bound gamma<1/3 sufficiently far out. It does
not require the actual geometry to preserve individual Fourier modes.
This is NOT a compact-resolvent claim for the whole neutral sector.

Compact-core elliptic compactness then gives the finite kernel and
closed ranges. An Agmon weight exp(epsilon r), epsilon<1/2, followed
by the lifted-ball estimate with covering multiplicity O(exp(r)),
gives Lp for every finite p. Collapse cannot simply be ignored.
For example exp(3r/8) is L2 but not L4 with measure exp(-r)dr;
finite quadratic norm alone did not pay this step.

The full proof and dependency transfer are in
[NEUTRAL_REGULARITY_PROOF.md](NEUTRAL_REGULARITY_PROOF.md).
R44's global cusp/core and all-jet application, the complete domains,
and the new elliptic/Agmon transfer remain explicit review duties.
There is no L-infinity conclusion and no uniform q->1 estimate.

## What is paid in the action

For u=s alpha, where alpha is R47's harmonic mode and alpha=a+psi
is its compact/Hermitian split, the supplied residual-square action
has the finite nonnegative straight-line quartic

    V(s alpha) = (2 s^4/g7^2)
      [ ||alpha wedge alpha||^2 + ||sum_i [a_i,psi_i]||^2 ].

No value or nonvanishing of these global profile integrals is computed.
Even a nonzero straight-line quartic would not rule out a curved
flat branch: other fields can relax at order s^2. Conversely its
finiteness does not prove that branch exists. The next question is
the coupled nonlinear obstruction/response on the fixed background,
not naming q a physical modulus or stabilizing it by inspection.

## First failure, preserved and diagnosed

The original native output returned 25 true and two false controls.
Both failed polynomial comparisons printed the expected factorization.
The error was in this seat's comparison: SymPy 1.14.0 returns a
characteristic-polynomial generator without the real=True assumptions
of the supplied symbol. Both print as z but are distinct symbols.
Subtracting their expressions does not compare the same polynomial.

The separately sealed diagnostic reconstructed the original matrices.
Exact QQ coefficient lists, use of the returned generator, kernel
dimensions and polynomial spectral projectors agree on both spectra.
Wrong coefficients, an actual eigenvalue perturbation and truly
symbolic coefficients are rejected. General symbols are NOT merged
by printed name. The original producer, tests, proof and outputs
remain unchanged. This is a comparator diagnosis, not a post-hoc
change to the predicted operator or its spectrum.

| First execution | Actual outcome |
|---|---|
| original native controls | 25 true, 2 false; exit 1 |
| original dedicated tests | 13 pass, 1 fail |
| original fixed six-file regression | 79 pass, 2 fail |
| separately sealed diagnostic | 26 exact checks pass; generator mismatch confirmed |
| diagnostic dedicated tests | 6 pass |
| original six files plus diagnostic | 85 pass, same 2 failures |

The retained IDs are
tests/test_physical_bridge_neutral_tangent.py::test_received_generic_pairing_and_dual_inverse_identity
and
tests/test_physical_bridge_neutral_regularity.py::test_full_and_zero_weight_potential_not_particle_count.
The first is R47's previously diagnosed structural-zero comparison.
Neither original failure is relabeled green.

Raw receipts and first outputs are indexed in
[NEUTRAL_REGULARITY_RECEIPTS.json](NEUTRAL_REGULARITY_RECEIPTS.json).
All 53 predecessor paths and nine scientific/diagnostic paths are
checked against their commits. Trees were read-only during executions.
The initially sandbox-blocked DNS push is retained; the later authorized
push and server confirmation preceded all science. Two approval attempts
were aborted before execution and produced no capture, not hidden runs.
Preserved pytest stdout contains trailing whitespace, so the full
diff whitespace check reports that raw-data line; it is not rewritten.

## Incoming work and mission consequence

The two supplied September handoffs were personally read at core/report
level before these tests. Their provenance, scientific reception grades,
useful M6 nonsplit candidate and m010/Sym^3 selection leads are recorded
in [WEB_HANDOFF_INTAKE_2026_09_26.md](WEB_HANDOFF_INTAKE_2026_09_26.md).
No incoming unrerun claim was added as a premise of R49. The library's
entire historical artifact collection has not been read.

The canonical route now has a nonzero finite-norm neutral direction
that can enter the specified nonlinear action. That is a constructive
advance, but R48's classical pairing remains. Next duties are nonlinear
integration/obstructions, actual normalized interactions and parameter/
phase selection, plus independent global review. The distinct nonsplit
R40/R41 and received M6 source/end routes remain open; no universal
chirality kill follows.

The full mission still requires a common physical action/domain,
physical chiral spectrum, quantum/anomaly completion, derived or priced
parameters, gravitational dynamics and discriminating observations.
Four historical governance-failure categories remain, including 41
stale relay debts; no full-suite, independent banking or TOE certificate.
