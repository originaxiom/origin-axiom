# Charged cone modes survive a vanishing boundary trace

September 30, 2026. Path-local R63. On R62's admitted normal background,
a nontrivial charged link can have no cohomology yet still have critical
radial modes on the cone. The full operator distinguishes two decaying
modes with separate zero differential/adjoint residuals from two modes
that only solve their sum by cancellation. These are local candidates,
not physical particles, chirality or a completed supersymmetric domain.

The original run passed 68/69 controls and 26 tests with two failures.
A separately sealed symbolic-variable repair passes 73/73 effective
checks and four new tests. The combined unchanged population gives
**30 passed, two original failures retained**. No green full-suite or
independent analytic certificate is asserted.

## The actual radial operator

Take the SAME supplied action and incomplete cone dr^2+r^2 h.
Let C=wX with normal X and zero radial coefficient. On a simultaneous
eigenline the connection is w a, a=alpha(X). Charged here means charged
under this supplied background, not an identified Standard Model
particle. The parent, background and link metric remain inputs.

For Fourier momentum k=2 pi m and an orthonormal link frame, let
z=i k+w a, lambda=z^dagger z. With L=wedge(z)+wedge(z)^dagger,
P=diag(0,1,1,2), and radial L2(dr) normalization, the eight-component
operator is

    Q = gamma (partial_r+A/r),
    gamma = [[0,-1],[1,0]],
    A = [[P-1,-L],[-L,1-P]].

All blocks have size four. The normalization sends link p-forms to
r^(p-1)alpha_p+dr wedge r^(p-1)beta_p. Beta_p has total degree p+1.
Direct metric Hodge differentiation reproduces every matrix entry,
including the complex conjugation in the adjoint. The generic
characteristic polynomial is

    ((t^2-lambda)^2-t^2)^2.

The eigenvalues are +/-(sqrt(lambda+1/4)-1/2) and
+/-(sqrt(lambda+1/4)+1/2), each twice. For 0<lambda<3/4, four lie in
the open critical interval (-1/2,1/2). At lambda=0 there are four
zero eigenvalues; at lambda>=3/4 none lie in that interval. The
endpoint is checked by its logarithmic norm/cutoff behavior, not
rounded away in a numerical diagonalization.

This instantiates the standard cone mechanism and explicitly treats
the supplied flat charged coefficient. The reduction to harmonic-link
data in [Albin et al., section 3.1 and Lemma 3.1](https://arxiv.org/html/1307.5473v3)
uses a spectral-gap hypothesis. That theorem is not a certificate for
the full interacting physical extension here.

## The whole Fourier population in the declared link metrics

For helicity w, the real and imaginary parts of w a have equal squared
norm. With H=h^-1 and v=Im(w a),

    lambda_m(a) = 2 |v+pi m|_H^2 + 2 pi^2 m^T H m.

For EVERY a and every nonzero integer m, this is at least 2 pi^2
on the unit-area square link and 4 pi^2/sqrt(3) on the unit-area
hexagonal link. Both exceed 3/4. The integer quadratic-form bound,
not a finite Fourier sweep, excludes extra critical modes there.

The zero Fourier mode instead has lambda_0=c|a|^2, c=|w|_H^2.
For a!=0 the link local system has zero cohomology: w1/w2 is
nonreal, so both holonomies cannot be one. The Fourier Koszul
contracting homotopy is checked directly. Nevertheless sufficiently
small nonzero a has the four critical radial data described above.

Rescaling the link metric by ell^2 divides lambda by ell^2.
No fixed finite scale excludes all these small eigenvalues uniformly
as a varies towards zero. A chosen background or metric can have a
gap; its selection and stability in a family are additional duties.
None of these thresholds predicts a physical coupling or mass.

## Finite separate residuals distinguish the four modes

Put eta=sqrt(lambda+1/4)-1/2, so 0<eta<1/2 in this charged critical
range. In a complex unitary link frame z=(sqrt(eta(eta+1)),0),
all four homogeneous modes are L2 and solve Q u=0, but:

| Radial branch | Total form degrees | Separate d_a and d_a^dagger |
|---|---|---|
| Two decaying r^eta modes | One mode of degree 1, one of degree 2 | Both residuals zero |
| Two growing r^-eta modes | Degrees 0/2 mixed and degrees 1/3 mixed | Nonzero opposite residuals, each with divergent norm |

For each growing mode the squared residual coefficient is
eta(eta+1)^2(2eta+1)>0 and the radial density is r^(-2eta-2).
The two decaying modes form a maximal isotropic plane for the
critical Green pairing; their pairing with the growing modes is
nondegenerate. This is the separate graph-norm test on homogeneous
modes, not a proof of full supercharge closure or a classification
of every interacting operator domain.

Their tangential coordinate traces vanish at the tip. R62's
restriction on nonzero constant boundary traces cannot exclude them.
Conversely their linear residuals do not prove finite nonlinear
action: eta can lie below R62's generic sufficient remainder bound.
Second-order relaxation and the allowed full domain require testing.

The degree-one mode has an explicit local scalar primitive r^eta
in the normalized frame. It is complex-exact locally. Whether an
admitted compact gauge transformation removes it, and whether it
extends globally with the required end conditions, are NOT settled
by that identity. Do not count it as a particle before those tests.

## A radial gauge transformation has its own boundary cost

For a commuting anti-Hermitian B, g(r)=exp(B log r) removes B dr/r
on the punctured cone. Its unitary action preserves the L2 norm.
A nonzero diagonal example, however, has different limits along
two sequences approaching the tip. Such a map is not in an
apex-continuous gauge group.

This supplies an explicit unitary transport, not a derivation of
the physical gauge group. The B=0 spectral calculation is not a
silent claim that every radial pole is removable by an allowed
transformation. Domain transport and gauge equivalence stay separate.

## Failure retained and correction verified

Original seal a7b9167149cb69db12411fd99a76016921dc47e3 and correction
seal 6933cee152caef2f4a7cc79ef6b5b1a452f0cdc3 were each pushed and
server-confirmed before their scientific runs. All seven sealed
paths and thirteen pinned inputs remain unchanged.

The first polynomial comparison used a real-assumed symbol t while
SymPy 1.14.0 returned a different, same-printed generator without that
assumption. A captured identity-matrix diagnostic reproduces the
false comparison. The correction uses the returned generator and
polynomial coefficients. It verifies the SAME original polynomial,
rejects a wrong density shift and a changed coefficient, and retains
the original failed dictionary. The old wrong-density-shift comparison
also used mismatched generators, so it too was recomputed explicitly.

The original source and tests were not edited or rebound. The new
four-test file passes; the fixed combined 32-test population retains
exactly the original two failed IDs. The failure was in comparison
mechanics, not evidence excluding the candidate physical model.

[Original design](CONE_SPECTRUM_DESIGN.md), [input pins](CONE_SPECTRUM_INPUTS.json),
[original producer](cone_spectrum.py), [original tests](../../tests/test_physical_bridge_cone_spectrum.py),
[repair design](CONE_SPECTRUM_CONTROL_DESIGN.md), [repair producer](cone_spectrum_control.py),
[repair tests](../../tests/test_physical_bridge_cone_spectrum_control.py),
[all published run receipts](CONE_SPECTRUM_RECEIPTS.json), and
[custody checker](cone_spectrum_receipt_check.rb).

## Next physical duty

Test the surviving degree-one candidates in the actual compact gauge
quotient and nonlinear equations, with their conjugate partners.
Then impose a common bosonic/fermionic variational domain and the
supercharge derivative conditions. Global gluing and normalizable
spectrum must follow in that same model, not by copying an index from
another coefficient system. The link/background/end law still needs
its connection to the generated architecture.

The [full physics mission](PHYSICS_MISSION.md), including chiral
matter, realistic interactions, quantum consistency, gravity and
observations, is unchanged. The all-head fetch found no new commits.
No other seat's worktree was modified or corpus absence claimed.
The recorded custody pass checks 999 artifact hashes, 348 distinct
sealed paths and 197 relative Markdown links, while retaining the
same 24 failed/error IDs in the older fixed test populations. This
is byte custody and recorded-population verification, not a rerun of
those scientific suites. The R63-specific checker covers all seven
sealed scientific files, thirteen inputs and ten raw run captures.

Governance returns 26 passes and the same four historical failures:
attribution, test-vacuity, seal-provenance and relay-debt. These are
recorded debts, not waived gates. The review counter is 246 merges
since the last review. This own-branch checkpoint does not constitute
full-suite certification, independent analytic review or main-bank
acceptance. The two original R63 test failures are separately retained
as described above.
