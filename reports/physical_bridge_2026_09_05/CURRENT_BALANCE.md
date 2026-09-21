# R41: what the actual nonsplit coefficient requires of a source

2026-09-21. Own branch audit/physical-bridge-2026-09-05.
Scientific snapshot 75c6873819c14e4781e81df91c307fda02ed884a was sealed,
pushed and server-confirmed before execution. Its six scientific files
are unchanged. Path-local research, no shared B or I allocation.

## Result and consequence

The surviving block U1 in R40 is the WRONG source direction to support
the actual nonsplit four within the specified complete, finite-energy,
block-compatible model. It acts as a scalar on that four and supplies
zero in each of three necessary traceless flag balances. This is a
specialization of F01/R39's existing argument, not a new general
harmonic-metric theorem and not a rejection of all source mechanisms.

There is a constructive algebraic distinction: noncentral directions
inside the parent have nonzero projections of the required sign. The
boundary version retains compensating flux, so the verified local cusp
and boundary/source route are NOT excluded. Neither a signed projection
nor a local cusp alone is a globally sourced physical background.

Sources: [sealed design](CURRENT_BALANCE_DESIGN.md),
[authored argument](CURRENT_BALANCE_PROOF.md),
[exact producer](current_balance.py), [prior](CURRENT_BALANCE_PRIOR.md),
[native result](CURRENT_BALANCE_NATIVE_FIRST.json),
[custody receipt](CURRENT_BALANCE_RECEIPTS.json).

## 1. All three necessary conditions

For the actual invariant rank-k subbundle, k=1,2,3, let
xi_k=4 P_k-k Id_4 and let eta_k be its off-diagonal extension block
in a positive metric's adapted orthonormal frame. With D=A+Psi and
the real moment equation I=-2 d_A^*Psi=S, the exact local identity is

    <Psi,d_A xi_k> = -2 |eta_k|^2.

Under the stated smooth complete finite-volume boundaryless hypotheses,
finite integral |Psi|^2 and integrable projected source, the authored
compact-cutoff argument gives

    integral tr(xi_k S) = 4 integral |eta_k|^2 > 0,   k=1,2,3.

Strict positivity follows from the already checked single Jordan block:
none of the three proper invariant flag subbundles has an invariant
complement. This is not a computed positive numerical lower bound.
The exact matrix tests verify the local identity, projector norm and
norm bound; they do not certify the infinite-domain proof independently.

The condition is not merely total charge neutrality or one scalar
Poisson equation. It asks for three representation-valued balances.
On a truncated domain, with outward normal n, it instead reads

    integral tr(xi_k S) = 4 integral |eta_k|^2
                         +2 integral_boundary tr(xi_k Psi(n)).

The negative boundary flux can compensate the positive extension term.
One must derive its allowed values and variations from the same action.
Dropping that term would produce a false kill. Infinite energy or
singular metrics invalidate this cutoff conclusion unless a separate
argument supplies the missing estimate.

## 2. The actual parent directions, with both outcomes

Extend xi_k by zero onto R40's determinant line. In the block metric
H5=diag(H4,(det H4)^-1), the parent moment map is
I5=diag(I4,-tr I4). The exact pairings are:

| source direction in the defining five | three flag pairings |
|---|---|
| T=diag(1,1,1,1,-4) | (0,0,0) |
| U=diag(3,-1,-1,-1,0) | (12,8,4) |
| -U | (-12,-8,-4) |
| [E_04,E_04^dagger] | (3,2,1) |

Thus S5=s T cannot satisfy the first section's requirements in this
block-compatible finite-energy setting. No theorem about every metric
on the rank-five bundle or every group called U1 is asserted.

The three neutral parent directions E_01,E_02,E_03 commute with T,
and their Hermitian commutators sum to U. The E_04 direction has
T-charge five, and its commutator has T-pairing five as well as the
nonzero flag projections. These are real algebraic possibilities in
the specified parent, not invented extra fields.

However these commutators already belong to the BULK moment equation.
Treating the same term as a new external source double-counts it. A
neutral current does not Higgs T, and a charged direction can change
the preserved flat coefficient. Curvature, derivatives, off-diagonal
equations and all source variations must still be satisfied.

An upper off-block extension retains V as an invariant subbundle. The
whole-rank projector identity is -5|alpha|^2/2; the existing source-free
finite-energy splitting argument still applies. A lower off-block map
can remove V's invariance, but then R40's old index is not automatically
the new bundle's index. No existence or chirality claim is made for it.

## 3. A retained positive already excludes one proposed pairing mechanism

Complex conjugation preserves the dimension of the interior restriction
kernel. A same-base invertible conjugate-linear flat E->E* map would
therefore force n(E)=n(E*), just as a linear flat isomorphism does.
R40's frozen exact pairs are V:(1,0), W:(1,0), exterior-square W:(2,1).
They obstruct BOTH linear and conjugate-linear flat isomorphisms to
the dual, in precisely that marked coefficient problem.

This is a functorial consequence of a previously earned positive, not
a new cohomology calculation. It prevents importing F08's particular
anti-linear flat pairing onto the actual R40 coefficient. It does not
exclude form-degree-changing, base-induced or nonlocal spectral maps,
or establish unequal normalizable fermion spectra. The metric, action,
end conditions and all fermion degrees still need to be one model.

## 4. Executions, controls and preserved failures

- Exact native run: exit zero, all flag/norm/source/extension checks pass.
- New test file: 16 passed, including scalar/noncentral, both signs,
  split/nonsplit, charged/neutral and upper/lower controls.
- Fixed sixteen-file regression: 252 passed, four failed. The four IDs
  are exactly R40's; none was removed, waived or edited.
- Incoming F08 unchanged reuse: 19 passed. Same implementation, not
  independent analytic certification. [Reception](FORK_F08_RECEPTION_2026_09_21.md).

Before execution, review strengthened the norm verifier: positive
coefficients alone are insufficient; even powers are checked, and x*y
is an explicit failing control. No executed source was adjusted to pass.
Preseal custody first rejected the unrefreshed seal-ledger artifact hash;
the updated hash then passed. Governance also caught received branch
names in the first input manifest; the original draft and exact names
are retained locally with digests, while the public revision retains
the exact commit objects. Both changes preceded the scientific seal.

The final preseal governance population had 26 passes and the four
historical failing categories, not full green. Relay debt aged from
21 to 25 flagged entries across the date boundary; that is not an
unchanged-detail claim. No main-bank acceptance or full-suite run is
claimed. [Reporting checks](CURRENT_BALANCE_FINAL_CHECKS.txt).

## 5. Next discriminator toward physics

For the retained coefficient, derive a noncentral source or boundary
variation law that provides these balances in the SAME parent/action.
Compute all residuals, not just projections. Then derive the complete
positive-norm fluctuation domain, all form/gauge/source/end modes and
anomaly matching; only then can the algebraic difference be tested as
physical chirality. Do not add arbitrary rescue fields or fit a density.

If changing the coefficient or admitting infinite background norm is
the route, state it explicitly and recalculate the physical problem.
R28 already distinguishes Higgs norm from the residual-square static
potential: divergence of one alone does not settle the other.

Post-execution intake: F10 FINDINGS at
5dc9b73017bb10bbed4b293f0271518a2c9e6c0b describes a projective deformation
and an exact cusp-tail candidate with a different norm issue. Only its
FINDINGS were read here; no proof or execution is adopted by R41. The
next intake must check those sources before using the proposed escape.
This does not replace or close the fixed-coefficient source duty.

The result improves a concrete compatibility test. It does not derive
three physical generations, a quantum mirror-removal phase, gravity,
physical constants, an empirical prediction or a complete TOE.
