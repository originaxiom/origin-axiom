# An exact electroweak-breaking branch of the same curved action

November 2, 2026. **UNREVIEWED author analytical construction.** No
scientific producer, CAS, matrix implementation, import, collection or
test execution. The result is conditional on the supplied E8 spin-parent,
metric/bundles and complete-domain law. It is not a foundational selection,
three-generation construction, quantum vacuum or gravity theory.

## 1. The physical duty and sources

The [order-three R-doublet calculation](ORDER_THREE_R_HIGGS_AND_DERIVED_TREE_VERTICES.md)
exhibits actual harmonic weak doublets and their native cubics. A small
Higgs value in a linearized kernel is not yet a stationary background:
the full moment equation has to be solved, including the companion Q.
This note solves it explicitly, keeping the same action and end law.

Reuse the actual vacuum equations and positive kinetic/potential metrics
in [the curved parent](../weave_curved_action_2026_10_08/PROOF.md), the
global spin/flat-holonomy construction and full principal embedding in
[the parallel phase](../weave_sm_parallel_2026_10_08/PROOF.md), and the
compact J/dual construction in
[the full flat-family note](FULL_FLAT_FAMILY_METRIC_AND_DISCONNECTED_CENTRALIZER.md).
The explicit D5 matrices below verify the required dual map directly;
neither the full E8 component-count table nor a global charge-conjugating
symmetry of the chosen Wilson state is needed. The older two-spin moment comparison is
a uniqueness statement within a fixed orbit and is not used as existence.

Read-only prior-work location used already_banked on "parallel electroweak
Higgs stationary". B987's Higgs-support findings were previously read.
The old HIGGS_SECTOR.md was read in full: its R7/R8 model adds scalar27s
and potential coefficients and does not supply this spin-parent branch.
The order-three running jump is already known. No repository-wide absence
or literature-priority claim is made.

## 2. Four literal E8 roots close the required moment

Use the source's one-based Euclidean coordinates e1,...,e8, positive
root-vector trace norm one, and

  w=(0,0,0,-1,1,-2,0,2), H=2w.

The bundle five in increasing w grade uses coordinates (6,4,7,5,8).
Its unit V1 highest bivector, from the preceding source, is

  Z=sqrt(2/5) b1 wedge b4 - sqrt(3/5) b2 wedge b3.

Let h_- be its neutral R_Hd component in bar5_g. Its two root terms
can be framed as

  alpha=e4+e8, beta=e5+e7,
  h_-=sqrt(2/5) E_alpha - sqrt(3/5) E_beta.                (1)

The phases are the actual bundle-bivector intertwiner's phases, as in
the previous source. Both roots have w grade1 and QY charge-3. With
T3=WEAK/2 and physical Y=QY/6, their charges are (+1/2,-1/2), so
they are neutral under Q_em=T3+Y. The combined h_- has unit norm,
with each underlying root vector normalized to one.

Define h_+ as the unit dual highest vector using the old J5 intertwiner,
explicitly realized in (4). It is the neutral R_Hu vector with the
opposite gauge weight. The earlier compact Chevalley/J map gives one
compatible phase choice, but no full-group classification is required.
On roots its two terms are

  gamma=-e5-e6, delta=-e4-e7.                             (2)

Their squared coefficient magnitudes remain 2/5 and 3/5. The adjoint
root phases of s matter for the vector but not the following moment
calculation. As highest V1 vectors,

  [H,h_+]=2h_+, [H,h_-]=2h_-, [E,h_+]=[E,h_-]=0.

Define Y0=h_++h_-. The two gauge sectors are orthogonal, so
kappa(Y0-dagger Y0)=2. Every difference of distinct roots among
alpha,beta,gamma,delta has squared length4 or6, not2. Consequently
all cross terms in [Y0,Y0-dagger] vanish. In this simply-laced root
normalization [E_alpha,E_alpha-dagger]=H_alpha corresponds to alpha.
The remaining Cartan vector is exactly

  (2/5)(alpha+gamma)+(3/5)(beta+delta)
       =(-e4+e5-2e6+2e8)/5=H/10.

Thus the ACTUAL identities are

  [E,Y0]=0, [H,Y0]=2Y0,
  [Y0,Y0-dagger]=H/10.                                  (3)

Put G=sqrt(10)Y0. Then [G,G-dagger]=H, [H,G]=2G and [E,G]=0.
Also kappa(E-dagger E)=kappa(G-dagger G)=20 and
kappa(E-dagger G)=0. This is not the old flavour orbit with R
proportional to Q: the two Lie vectors are independent.

## 3. Independent compact D5 matrix realization of the same identities

All four roots and the old A4 raising chain lie in the closed D5 root
subsystem on coordinates4,...,8. There is a faithful finite matrix
realization available for subsequent checks, without computing every
E8 bracket. It is an actual embedded subsystem, not an identification
by dimension. On B plus B-dual write

  X=[[A,B],[C,-A^T]], B^T=-B, C^T=-C,
  kappa(X-dagger X)=(1/2)Tr_10(X-dagger X).

The defining five has H5=diag(-4,-2,0,2,4), with E5 raising coefficients
2,sqrt(6),sqrt(6),2. Embed E=diag(E5,-E5^T), H=diag(H5,-H5).
Let B_Z be the skew matrix for the unit bivector Z, and use the source
J5=anti-diag(1,-1,1,-1,1). Then

  h_-=[[0,B_Z],[0,0]],
  h_+=[[0,0],[J5 B_Z J5,0]].                             (4)

The lower block has coefficients sqrt(2/5) on b0 wedge b3 and
-sqrt(3/5) on b1 wedge b2. Direct multiplication gives the top block
of [Y0,Y0-dagger] as

  diag(-2/5,-1/5,0,1/5,2/5)=H5/10,

and the negative transpose on the lower block. The two highest-vector
identities give [E,Y0]=0. Root norms are one with this trace, agreeing
with section2. These are authored matrix formulas checked by hand;
the proposed executable reconstruction has NOT been implemented or run.

## 4. Exact global solution with the backreaction retained

Fix any source carrier and extending spin, curvature radius ell>0,
and any exact-order-three marked Wilson character chi. Keep the old
connection A=s_spin H/2+C, whose curvature is

  F_A=-H dvol/(4ell^2).

Choose complex numbers a,b with |a|^2+|b|^2=1, and set the physical
orthonormal spin coefficients to

  qhat=a E/(2ell), rhat=b G/(2ell).                       (5)

These are GLOBAL spin/gauge sections, not constant coefficients on an
unrelated trivial bundle. E and G have principal weight+1, so their
S tensor S^(-1) factors cancel. E has flat charge zero and the two
terms of G have chi^(+/-3)=1. Each is covariantly parallel in its
actual combined spin/gauge line. Local flat gauges are glued by the
original holonomies; no assumption that a Lie-algebra representative C
commutes pointwise with a constant bare charged matrix is needed.

All three old vacuum equations now hold:

  Dbar_A q=Dbar_A r=0,
  [q,r]=0,
  F_A/dvol+[qhat,qhat-dagger]+[rhat,rhat-dagger]
       =(-1+|a|^2+|b|^2)H/(4ell^2)=0.                  (6)

The Q rescaling is compulsory. Turning on r=bG/(2ell) while leaving
q=E/(2ell) gives the nonzero moment |b|^2 H/(4ell^2). It is a rejecting
control on "assign a Higgs value and retain the old background".

In the holomorphic orbit chart with t=b/a, a can be taken positive:

  a=(1+|t|^2)^(-1/2), b=t(1+|t|^2)^(-1/2).

Both E and tG are rescaled by the same bounded Hermitian direction
exp(xH), x=-(1/4)log(1+|t|^2). Since [H,E]=[H,G]=2 times that vector,
this is precisely their complex-gauge moment response, with A fixed.
It is an explicit response; no implicit-function or PDE existence
theorem is borrowed from an ordinary K-valued Higgs problem.

## 5. Domain, stationarity and the complete bosonic sign

The physical profiles in (5) are bounded and spin/gauge parallel.
Finite area gives finite positive kinetic norms. The old complete
cutoff estimates put them and their variations in the same complete
graph class as the source principal background. Their derivatives
and commutator residuals are admitted; no physical wall, defect,
added source, altered peripheral or discarded surface term is used.

Because EVERY residual in the old positive-square functional vanishes,
the first variation vanishes for every admitted variation in the full
E8 theory. The full bosonic Hessian is the sum of the squared linearized
residual norms. It is nonnegative on the actual gauge quotient, with
the old positive kinetic terms. This is a classical stationary minimum
family, not merely a minimum restricted to a chosen amplitude.

No new Higgs potential, mass coefficient, quartic or kinetic weight is
supplied. This does not prove quantum stability, a selected isolated
vacuum or an observed electroweak scale. Gauge directions and flat
moduli remain zero directions; they must not be removed from counts.

## 6. Compute the unbroken gauge action

Assume a and b are nonzero. A real gauge zero mode is covariantly
parallel and commutes with both Higgs fields and their adjoints, by
the source's positive gauge-operator norm. Commutation with nonzero
qhat and qhat-dagger therefore gives the old principal triple's
connected SU5_g centralizer. The order-three holonomies restrict it
to the source S(U3 x U2), retaining its actual faithful group action.

Inside its defining five, h_+ is a weak neutral fundamental vector
f5 and h_- is its dual; their bundle intertwiners are nonzero. The
gauge action must fix BOTH vectors, since they occupy distinct gauge
representation summands. Their stabilizer in S(U3 x U2) is

  {diag(U3,det(U3)^(-1),1): U3 in U(3)}.                  (7)

Thus the connected unbroken group is U3, with Lie algebra
su3_colour plus u1_em. The EM generator on the defining five is
diag(-1/3,-1/3,-1/3,1,0), equal to the old Y+T3. The weak raising
and lowering generators have EM charges+1,-1; one additional neutral
weak/hypercharge direction is broken. Their gauge mass quadratic form
is positive because their commutator with R is nonzero. No global
component count or full massive vector spectrum is claimed.

At b=0 the known SM group returns. The endpoint a=0 requires a separate
centralizer analysis and is not included in (7). This theorem is not
an exclusion of further branches or different Higgs directions.
The older parallel-ansatz obstruction explicitly required the full SM
group to remain unbroken. It is not contradicted: b!=0 changes that
hypothesis and (7) computes the changed group.

## 7. The family is physical freedom, not a scale prediction

The total Higgs norm is fixed by the moment balance:

  kappa(qhat-dagger qhat+rhat-dagger rhat)=5/ell^2.

But the relative configuration is not fixed. For example the determinant
of the two-field Hermitian Gram matrix is

  det Gram(qhat,rhat)=25|a b|^2/ell^4.                    (8)

It is invariant under compact gauge transformations and the old global
SU2 flavour rotations. It vanishes at b=0 and is positive in the
interior family. These backgrounds cannot be erased as the old
rank-one flavour orbit. Measuring data must also travel under any
proposed further equivalence; no such quotient is imposed here.

Within the neutral two-doublet direction, equality of their physical
norms cancels the light hypercharge moment. A single nonzero doublet
with the old neutral Q and flat C leaves that moment uncancelled.
The balanced pair and the compensating Q response are derived
compatibility conditions in this ansatz. The amplitude b, relative
state and physical Higgs direction among all allowed fields remain
unselected. The branch is not a solution of the foundational state law.

## 8. Fermion and index duties must be reopened correctly

The old R=0 complete harmonic roster and its projected cubics are
data AT THE SYMMETRIC POINT. At b!=0 the full mass operator includes
both Q and R in its W Hessian and gauge Killing map. Its zero modes,
mixings and thresholds have to be computed in that same new background;
neither the old roster nor the old up-cubic zero is a complete finite-VEV
fermion mass calculation.

For small b, the Higgs changes are small bounded zero-order perturbations
of the old complete first-order operator, on the same graph domain.
Fredholmness persists in a sufficiently small neighbourhood of the old
gapped Fredholm point. The fixed residual colour/EM block indices can
then be transported. The original full SM representation blocks cannot:
the branch breaks that group. A zero colour/EM chiral index is also
not by itself an obstruction to observed charged Dirac fermions after
electroweak breaking. Do not convert that residual index into a new
false programme-wide kill.

No three chiral SM generations, complete anomaly/inflow calculation,
phenomenological mass spectrum, supersymmetry breaking or gravity is
derived here. The symmetric parent still has its known nonchiral
spectrum. This branch establishes an actual classical Higgs response,
not those separate missing physical identifications.

## 9. Before/after and verification boundary

Before: light R doublets with actual cubics, but no derived nonlinear
stationary continuation when they acquire values. After: equations
(3)--(6) give an exact same-action, globally admitted continuation with
Q backreaction, nonnegative full bosonic Hessian and computed colour/EM
stabilizer. There is no new fitted potential or boundary law.

Still supplied: the physical parent, curvature/carrier, embedding,
spin/end class and the order-three R-sector restriction. The vacuum
amplitude and physical state distribution remain undetermined. No
foundational input row is marked removed; full SM3/gravity remains
the destination.

Independent scrutiny must check the actual J/dual map and root phases,
closed D5-to-E8 map, highest vector, moment coefficient,
global spin/flat-line cancellation, complete-domain nonlinear admission,
stationarity and all gauge stabilizers. The finite matrix control
design is sealed separately before implementation; it cannot certify
these global analytical hypotheses or inherit an older review.
