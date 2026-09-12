# R26: localized curvature can preserve the sourced chiral sector

September 12, 2026. Path-local result; no global B allocation.
Scientific design, proof candidate, producer and tests were sealed and
pushed at `46b34c09` before execution and remain unchanged. This report
discharges the frozen proof candidate's pre-execution status; it is not
independent proof acceptance or a completed physical theory.

## Result and scope

Conditional on R18/R19's strong-source maximal-domain theorem, the
actual graded Dirac index survives bounded Hermitian odd perturbations
supported in the regular interior, or uniformly vanishing at every end
of the punctured manifold. For the original pair-free sector, a
perturbation smaller in operator norm than the original positive gap
preserves exactly three odd and zero even zero modes. An explicitly
nonflat compactly supported unitary connection belongs to this class
at sufficiently small nonzero amplitude.

This answers the registered analytic backreaction sub-question, not the
stationary source/end problem. Gauge curvature destroys the original
cochain differential but need not destroy its graded Dirac index.
The retained three/zero Spin(10)-multiplet interpretation additionally
requires preservation of that charged block and scalar action on its
spinor factor. It is not licensed after arbitrary gauge mixing or
symmetry breaking.

The full argument is in [the frozen proof](INDEX_STABILITY_PROOF.md);
the predeclared population and controls are in
[the design](INDEX_STABILITY_DESIGN.md). The proof is an application of
standard local elliptic, Rellich and Fredholm results to this declared
operator, not a newly discovered abstract index theorem. The exact
primary propositions and the earlier banked identities are recorded in
[the prior-art receipt](INDEX_STABILITY_PRIOR.md).

## 1. The actual operator, including its adjoint

Keep the sourced geometry, metric, charged bundle, real potential H,
and the complete domain

    E = Dom(d0,max) intersection Dom(d0,max*),
    D0 = d0,max+d0,max*,  d0=d_A+dH wedge.

For a real unitary connection perturbation a and real mass one-form v,
the existing exterior/metric-adjoint implementation gives

    B = -i q [epsilon(a)-iota(a)] + epsilon(v)+iota(v),
    D = D0+B,
    B^2 = (q^2 |a|^2+|v|^2) I.

The last identity is for scalar coefficients; it is not transferred to
noncommuting matrix coefficients. The actual map is Hermitian and odd
in form parity. Wrong adjoint signs and an even scalar shift fail the
corresponding controls. Boundedness preserves the maximal differential
and adjoint domains. The resolvent factorization at imaginary spectral
parameters greater than the perturbation norm establishes
self-adjointness on the same E, without selecting a new singular
extension. Both factor order and the inverse-difference identity are
checked by noncommuting finite controls.

Odd form degree is the positive four-dimensional chirality convention
already fixed in R23. Thus the block T0:E_odd -> L2_even has index +3,
whereas the original cochain Euler characteristic is -3. Once curvature
makes d0 squared nonzero, the counts are odd/even kernels, not an
asserted curved cohomology H1.

## 2. Why the index survives without compact resolvent

Local elliptic regularity bounds the H1 norm of a graph-bounded sequence
on each regular compact patch. Rellich compactness then makes bounded
multiplication supported there compact from E, with its graph norm,
to L2. This is not compact multiplication on L2 itself and does not
require compact resolvent of D0. Uniform decay at all ends extends
the conclusion by norm approximation with compact cutoffs. A source
line approached at finite cusp height is an end too.

The odd block is therefore a compact perturbation of the original
bounded Fredholm map on its fixed graph-domain space. Its index stays
k for every finite perturbation amplitude in that relative-compact
class. For a pair-free original kernel, the original even-block gap
delta separately gives

    ||(D0+B)u_even|| >= (delta-||B||) ||u_even||.

When ||B||<delta, no even zero mode appears; the fixed index forces
exactly k odd zero modes. No numerical value for delta has been
computed. This proves that a stable neighborhood exists under the
R18/R19 hypotheses; certifying a specified physical solution would
require quantitative bounds for that solution and its gap.

The two statements are deliberately different. In an infinite model
with a noncompact resolvent, a rank-one perturbation creates one extra
odd/even pair at the gap crossing while preserving net index k.
Changing every infinite tail channel instead can remove Fredholmness;
that perturbation is not relatively compact and reaches the gap norm.
The finite controls check the changed blocks and exact distances;
the displayed infinite tail, not a finite matrix census, supplies the
noncompact examples. Trivial and Alexander-exceptional original
holonomies retain their distinct four/one starting counts.

## 3. A genuinely curved member, not a stationary vacuum

In a coordinate ball whose closure avoids every source and end, take
the smooth bump b=exp(-1/(1-|x|^2)) inside the unit ball, zero outside,
and the globally extended one-form

    a = epsilon b(x) x0 dx1.

At the center its curvature is (epsilon/e) dx0 wedge dx1. The actual
covariant square equals -i q da wedge on all eight exterior basis
elements. Hence the example is nonflat when epsilon is nonzero; the
unchanged exact real mass does not restore the cochain differential.
On this compact patch, smooth metric comparison bounds the operator
perturbation by C|q epsilon| and gives finite additional curvature
energy. Small nonzero amplitude therefore preserves the pair-free
kernel in the specified scalar charged sector.

No Maxwell, Higgs, BPS or coupled source equation is solved by this
construction. Finite additional curvature energy does not prove finite
action for the original singular source, and no new source amplitude,
end wall or Wilson period is silently treated as a compact interior
perturbation. The local polynomial H used in the executable curvature
control is an operator-identity test, not a replacement physical source.

## 4. Executed evidence and preserved failures

The first launches used a system interpreter lacking SymPy and pytest
and stopped before the scientific calculation. The unchanged-code
launcher correction was recorded at `8dfbd9bc` before retry; no package
was installed or updated. The established Python 3.12.1 environment
uses SymPy 1.14.0, pytest 9.0.3 and SciPy 1.16.3. See
[the launch-failure receipt](INDEX_STABILITY_LAUNCH_FAILURE.txt).

The first successful native run is explicitly labeled a launcher retry:
[complete JSON](index_stability_launcher_retry.json), 57.2103 seconds,
exit zero. Actual-map, Hermiticity, oddness, scalar norm, covariant-square
and resolvent controls pass. Sixty comparison rows cover k=0,1,3,5,
three matched-block sizes, and five amplitudes including the pair
crossing. These are exact algebraic controls, not a numerical spectrum
of the singular manifold or an interval PDE certificate.

The [focused run](INDEX_STABILITY_CHECKS.txt) has 56 passes and one
optional-GUI warning in 84.65 seconds: 13 new R26 tests plus the
unchanged R18/R19/R22 selections. The first broad-run terminal capture
was lost; it is not counted as a complete run or recovered evidence.
[The loss and replacement declaration](INDEX_STABILITY_REGRESSION_CAPTURE_LOSS.md)
preserve that distinction. After confirming no original process was
live, the same population was rerun with durable, exclusive file-backed
capture, using [the capture helper](capture_checked_run.rb).

The completed [47-file expanded regression](INDEX_STABILITY_REGRESSION.txt)
has **354 passes, 14 failures and 8 errors**, with one optional-GUI
warning, in 337.17 seconds; terminal exit one. Its 22 FAILED/ERROR IDs
are exactly R25's: none added, none missing. The raw log's digest and
exact command population are in the receipt. Only environment prefixes
are redacted publicly; raw output remains outside the repository.
Original science, tests, tolerances and first failures were not edited.
The tree was read-only throughout the completed scientific runs.

All remote heads and tags were fetched in the pre-execution intake.
The prior search includes all reachable current Git objects and retained
old forced-update tips; its complete repeated capture is preserved.
Search hits are not absence proofs or novelty certificates. R26 uses
the earlier R18/R19 positive results and R22 cochain warning at their
actual scope, without adopting another branch's parabolic cohomology
index as this singular operator's index.

The [final all-head intake](INDEX_STABILITY_INTAKE.md) records later
outside and paper-review updates, including the received finite-field
nonzero index and two-sided isotropy correction. They are read, not
independently rerun; the original scientific dependency pins are unchanged.

Reporting-gate and custody status is maintained separately in
[the banking receipt](BANKING_RECEIPT.md). This result is not full-suite
green, an independent banking pass, a main merge, or an accepted TOE.

## 5. What changes next

The retained path has moved from asking whether any curvature destroys
chirality to asking whether the actual coupled solution belongs to a
controlled index class. The next discriminating task is one source/end
action with explicit variational domains, allowed gauge transformations
and a stationary background. Its source behavior, cusp behavior and
charged-sector map must be checked against this theorem, not assumed.

R26 does not cancel the extra U(1) anomaly: keeping the same chiral
representations preserves that duty. The R25 free wall still supplies
mirrors, and localization alone still does not remove their coupling
to the unchanged constant gauge mode. Gauge breaking requires a fresh
full-bundle representation and anomaly calculation. Neutral spectra,
finite low-energy couplings, source selection, common gravity and
empirical normalization remain outstanding. These are requirements
on this construction, not universal exclusions of other completions.

Closing sentence: **Within the fixed strong-source charged domain,
bounded Hermitian odd perturbations compactly supported in the regular interior
or uniformly vanishing at all ends preserve the graded index; below
the original gap they preserve the pair-free kernel, including an
explicit nonflat trial connection. Only this analytic stability
sub-duty closes; a stationary source/end and quantum completion
remain open.**
