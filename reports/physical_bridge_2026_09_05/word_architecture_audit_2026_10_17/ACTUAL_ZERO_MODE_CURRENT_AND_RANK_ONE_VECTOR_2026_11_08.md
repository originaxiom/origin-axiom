# From three charged coefficients to an actual one-sided current

2026-11-08. **NEW AUTHOR HAND DERIVATION: UNREVIEWED, UNRUN.**
This is not a banked result or independent certificate. No scientific
import, collection, matrix/CAS evaluation or numerical test was performed.
Source baseline is physical30f348e15755a3c5a824e75d5ed6ba354e200bb3;
the AGY source-map review is separate. The candidate up-count and its
complete-domain argument remain independent-review obligations.

SUCCESSOR NOTICE: CONJUGATE_SECTOR_VECTOR_AND_PAIRED_CURRENT_POLE_2026_11_08.md
now constructs the previously unresolved second, right-current vector
at the same tree-level pole, with a conditional norm-equality argument.
This single-mode proof remains a valid candidate at its stated scope;
read the successor before interpreting it as an isolated chiral sector.
The successor is also author-only, unreviewed and unrun.

## 1. Fixed candidate and bounded question

Keep the supplied compact E8 curved action, its positive kinetic metrics,
complete once-punctured elliptic surface of curvature -1/ell^2, balanced
two-triple stationary background and the coherent quaternion gauge/flavour
lift. Here eta=O is the extending spin and chi=0 means that the optional
old order-three Wilson is absent. Keep h4, not a trivial gauge bundle.
These choices are hypotheses, not foundational reductions.

Reuse the actual M and D0 in weave_physical_mass_2026_10_08/PROOF.md,
the real gauge operator in SAME_ACTION_REAL_GAUGE_FIXING_AND_ONE_LOOP_WEIGHTS.md,
the combined transitions in COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md,
and the new cusp extension in COUPLED_UP_SECTOR_PARABOLIC_COUNT_2026_11_08.md.
WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md already gives the
source vertex and the discrete positive charge-one vector problem.
None of those source proofs is replaced by a finite Koszul square here.

The bounded question is whether the proposed three up and three down
coefficients actually couple through that action. The candidate conclusion
is narrower than three weak families:

* The candidate zero-mode spaces have a physical 2+1 slot decomposition.
* A single principal-grade charged vector cannot give a rank-three
  quark current on those spaces.
* There is an explicit global holomorphic charged-vector eigenmode,
  with squared mass 7/(2 ell^2), whose zero-mode quark current has rank
  one on the left and vanishes on the right.

The last statement retains the independent conjugate LEFT fields; it does
not erase their particles or all other vector interactions. It does not
identify the observed W, derive a closed weak SU2, or establish SM3.

## 2. Exhibit physical representatives before using a count

Use the unitary coordinate change

    (q',r')=((q+r)/sqrt(2),(q-r)/sqrt(2)),
    qhat'=E_+/(2 ell), rhat'=E_-/(2 ell).

Transport the epsilon pairing, trace-dual outputs and degree-two slot:
this determinant-minus-one coordinate change is not a new flavour symmetry.
Both spin-slot kinetic weights remain Omega. Put H=H_++H_-, and write
mu=m+n for the eigenvalue of H/2. The gauge transitions commute with H
even when they exchange the two triples; this grading is globally defined.

The source four-slot metric is

    ||psi||^2=integral dxdy kappa(
        Omega^2 lambda†lambda + (1/2)a†a
                              + Omega(u'†u'+v'†v')).          (1)

In the up block (10,6), the two degree-zero-Koszul Dolbeault H1
representatives are pure a modes on the highest span

    |2,0>, |0,2>,                  mu=+2.                   (2)

They solve Dz a=0 with the actual weighted adjoint, while both raising
operators annihilate their gauge coefficient. Substitution into M gives
zero in every row. Their candidate dimension is two, not one for each
choice of a local frame. Their global bundle is the source G0(-p).

The one new up middle H0 representative is a pure spin pair supported on

    u': |-2,0>,   v': |0,-2>,       mu=-2.                   (3)

It is a holomorphic section of S^3 V3 with the actual pole bound, or
E(V3)(p) on the compactification. For this pair F_+u'=F_-v'=0,
E_-u'=E_+v'=0 and Dbar u'=Dbar v'=0. These identities directly kill
the gauge-adjoint row and all Hessian rows of M. Thus this is a physical
zero representative, not just an abstract class requiring an untracked
nonunitary change of its slot norm.

The down block (16,4), with coefficient 3_(-1/3), has pure a representatives
on |3/2,3/2>, mu=+3, of dimension two. Its middle pair is

    u': |-3/2,+3/2>, v': |+3/2,-3/2>,   mu=0.               (4)

The induced core maps on this pair are alpha sigma_x and I, with
alpha=+1 or -1 for the specified coherent lifts. At eta=O and chi=0,
exactly one eigenline has trivial compact flat character. Its H0 section
is nonzero everywhere on the compact elliptic curve and has both spin
components nonzero. Formula M again vanishes directly: the appropriate
lowering operators annihilate u',v', the cross raising terms vanish,
and the section is covariantly holomorphic. Its physical norm is finite.

The independent up-conjugate and down-conjugate LEFT sectors have the
same slot and principal grades. They are not identified with one another
or removed by the reality of the higher-dimensional adjoint. Conditional
on the earlier complete counts, these representatives exhaust each
charged three-dimensional multiplicity space. The representative
construction itself does not prove that exhaustion.

## 3. The current fixes different grades for its two blocks

For a source-normalized vector w, Q(w)=+1, the source kinetic term gives

    g_mn(w)=g6 sum_i integral dxdy h_i
                             kappa(psi_i,m†[w,psi_i,n]),    (5)
    h_i=(Omega^2,1/2,Omega,Omega),
    integral dvol kappa(w†w)=1.

It is diagonal in the physical slots. Consequently the form/spin cross
blocks vanish pointwise for every w, without a guess about their radial
profiles. Orthogonality of H weights then gives:

| Current for Q(w)=+1 | Source -> target mu | Required mu(w) | Rank bound |
|---|---|---:|---:|
| left down -> up, a slots | +3 -> +2 | -1 | 2 |
| left down -> up, spin slots | 0 -> -2 | -2 | 1 |
| left up-conjugate -> down-conjugate, a slots | +2 -> +3 | +1 | 2 |
| left up-conjugate -> down-conjugate, spin slots | -2 -> 0 | +2 | 1 |

The last two rows are the right-handed quark current when written with
independent left conjugates; an overall sign/transpose on conversion does
not change the vanishing or rank. They must be tested rather than inferred
from a zero electromagnetic index. Grade-zero or grade-three directions
do not connect these particular charged zero-mode spaces.

The actual Pv=D0†D0 preserves principal grade: Dbar commutes with H,
and each Higgs raising map is followed by its lowering adjoint. This is
also true of its closed form domain, since the finite orthogonal grade
projections preserve compact-support cores and the quadratic form. It
is not an assertion that the entire first-order fermion map commutes
with H without any slot grading.

Therefore a full-rank-three left current from ONE vector mass eigenmode
requires components in both grades -1 and -2 at the same eigenvalue,
with nonzero corresponding overlaps. This is a necessary condition,
not an exclusion of such a degeneracy. A sum of eigenmodes with different
masses is not one particle pole. A derived change of background/domain
could change this condition and must be analyzed as that new construction.

## 4. Derive a charged-vector eigenmode from the actual Pv

The gauge-parameter norm is integral Omega^2 kappa(w†w). Using (1) and
D0=sqrt(2)(Dbar,-i ad_q',-i ad_r') gives the quadratic form

    <w,Pv w> = integral dxdy (|Dbar w|^2
                     +2 Omega(|[q',w]|^2+|[r',w]|^2)).     (6)

Here q'=sqrt(Omega)E_+/(2ell), similarly r'. Thus on an orthonormal
joint weight (m,n) of V_j tensor V_j, the Higgs contribution is

    c_mn=((j-m)(j+m+1)+(j-n)(j+n+1))/(2ell^2),
    Pv=Dbar^{*v}Dbar+c_mn,                                (7)

where the adjoint in the derivative term uses precisely (6) and the
gauge norm. This is not the generic Koszul operator in the unresolved
older V1 finite check. Neither g6 nor an arbitrary mass coefficient is
inserted in (7); the same overall action coefficient cancels on kinetic
normalization. The supplied length ell remains.

Every Q=+1 vector is in (16,4)'s singlet and has j=3/2 in each factor.
Its mu=-2 subspace is exactly

    |-3/2,-1/2>, |-1/2,-3/2>.

The raising squared norms are 3 and 4 in either order. Consequently
c_mn=7/(2ell^2) on this entire two-plane. No variable potential or
coupling to a different grade was discarded.

Let alpha be its coherent highest character. Lowering five times and
using Ad_A F_+=i F_- gives, up to a transported constant unitary frame,

    A_w=i alpha sigma_x, D_w=diag(i,-i), B_w=D_w A_w.

They square to -I and have peripheral commutator -I. The gauge-parameter
bundle in this grade is S^2 Vw, Vw the resulting rank-two unitary flat
bundle. This is not two degree-zero compact lines. In a puncture frame
f=z^(1/2)e, its canonical extension E(Vw) has degree -1 and
E(Vw*)=E(Vw)*(-p). These are the local determinant and dual-frame
identities already proved as a candidate in the up-sector report.

For completeness, the same maximum-principle argument gives h0(E(Vw))=0:
a compact holomorphic section has flat norm tending to zero at p, and
that norm is subharmonic away from p. For every unitary flat twist L,
the argument also gives h0(E(Vw) tensor L)=0. Elliptic Riemann-Roch and
Serre duality then give h0(E(Vw)(p))=1, h1=0. This applies the classical
compact theorem; it is not a substitute for the physical endpoint.

For S^a with flat periphery -I, the actual gauge norm at a=2 has radial
integral proportional to

    integral r^(2-2N) dr,

for pole order N in the extension frame. Hence N<=1 is allowed and
N=2 is excluded. The compact sheaf dictated by that norm is exactly
E(Vw)(p), since eta^2=O. The nonzero holomorphic section w0 is smooth
on the core and decays in physical norm like r^(1/2) log(1/r) or faster
at the cusp. Complete cutoffs approximate it in the form norm. Its weak
equation from (6) extends from the core to that realization, giving

    Dbar w0=0,       Pv w0=7/(2ell^2) w0.                 (8)

It is therefore in the operator domain, not merely a local indicial
solution. Normalize its positive gauge norm to one. Its Hermitian
conjugate supplies the opposite-charge component of a real charged
vector. No observed mass or universal spectral gap through changing
moduli is asserted.

## 5. Show the surviving current is nonzero without guessing profiles

It is not enough that E8 has some nonzero spinor bracket. The bracket
must be nonzero on the actual extremal representatives in (3)-(4).
Under Spin5 x Spin5, 16=4 tensor 4 and 10=(5,1)+(1,5).
The Spin5 four has invariant nondegenerate skew form J; under its
principal SU2, 4=V_(3/2) and Lambda^2(4)=V2+V0. The vector-five map
is the projection onto V2. The Spin10 symmetric map 16 tensor 16 ->10
therefore has the two components

    Gamma5 tensor J,          J tensor Gamma5.           (9)

Their coefficients are nonzero: the actual E8 root bracket supplies
the nonzero Spin10 ten intertwiner, the ten is irreducible under Spin10,
and the two five-spaces are exchanged inside Spin10. The A3 factor is
the ordinary exterior map 4 tensor 4 ->6. In the present channel its
singlet wedged with the down triplet is nonzero and has charge +2/3.
This fixes an existing bracket; it introduces no adjustable Yukawa.

Write the two components of w as w1 on |-3/2,-1/2> and w2 on
|-1/2,-3/2>. For the down u' in (4), only w2 can land in the ten:
it gives |-2,0>. Its first factor is the nonzero weight-minus-two
wedge of |-1/2> with |-3/2>, necessarily in V2, and its second factor
is the nonzero J pairing of opposite extreme weights. For the down
v', only w1 survives, giving |0,-2> by the analogous J/Gamma5 pair.
Thus the fibre map is diagonal up to exchanging w1,w2, with two nonzero
constant coefficients. The nonzero down section has both components,
so this map is injective on the vector two-plane at every core point.

Take its global holomorphic down spin zero mode d_s and w0 from (8).
Dbar is a derivation, so [w0,d_s] is holomorphic. It lies in exactly
the up spin bundle (3); the same raising/lowering identities show
M[w0,d_s]=0. Gauge/flavour covariance of the original bracket glues it
globally without choosing a new relative phase. It is not identically
zero by the injectivity just established. It also has finite physical
norm: w0 and d_s decay at the end, their product is smooth on the core,
and the extremal equations give its complete-domain approximation.

Conditional on the candidate one-dimensional up spin H0, put

    u_s=[w0,d_s]/||[w0,d_s]||_spin,

with unit normalized d_s and w0. The spin-slot part of (5) is then

    g_s = g6 ||[w0,d_s]||_spin > 0,                     (10)

up to a harmless phase. This proves nonvanishing symbolically; it does
not compute the value of the norm integral. That value depends on the
supplied geometry and profiles and is not a parameter-free prediction.

In the physical 2+1 zero-mode bases, (5) consequently has

    G_L(w0)=diag(0_(2x2),g_s),       G_R(w0)=0.           (11)

The right zero follows from the explicit conjugate-sector rows of the
table, not from omitting conjugates or equating kernel and cokernel.
The rank-one statement is unchanged by unitary changes within the
properly transported zero-mode spaces.

## 6. What remains, and the next decisive calculation

Equations (8)-(11), if independently upheld, connect a global vector
profile, a classical mass, actual fermion zero modes and a nonzero
normalized one-sided current in ONE supplied stationary theory. They
advance the physical interaction duty beyond an allowed root bracket
or three equal counts. They are not yet a verified breakthrough.

Keep all other charged-vector modes, including positive grades that
can couple to right-handed quarks. No claim is made that they are heavier,
absent, decoupled or irrelevant. Keep scalar partners, conjugate fermions,
the neutral continuum, possible degeneracies and the full gauge theory.
The vector/Goldstone and higher-mode Ward identities, anomalies and
consistent low-energy reduction remain duties. Projecting (11) out as
an autonomous chiral gauge theory would be unjustified.

For a full-rank three-pair one-pole current in this candidate, the next
question is the actual mu=-1 form-current spectrum and overlaps, and
whether it shares an eigenvalue with a mu=-2 spin-current mode. The
form-current weights (-3/2,+1/2),(+1/2,-3/2) have Higgs constant
3/ell^2. Their flat A=alpha sigma_x, D=-I bundle splits into the two
nontrivial characters (+,-),(-,+). Its S^1 holomorphic H0 is zero at
eta=O, so the shortcut (8) supplies no form mode. This does not exclude
nonholomorphic eigenfunctions or an exact spectral coincidence. The
additional mu=-1 weight (-1/2,-1/2), with Higgs constant 4/ell^2,
belongs to the complete vector problem even though its direct overlap
with these highest form modes vanishes. No sector is deleted from Pv.

Even a rank-three same-pole current would not finish this duty. One must
test its normalized singular values, compatible neutral currents and
the weak algebra, including couplings through retained massive modes.
For an exact three-doublet charged current, unitary changes of family
basis cannot repair unequal singular values or a nonzero right current.
Those are further constraints on a derived vector mixture, not licenses
to fit its relative coefficients after seeing the target.

No new independent foundational input is paid here. In particular the
act/register-to-action map, eta=O, pure-h4 carrier/background selection,
physical metric and ell, g6, spin/flavour transport and family-state
interpretation remain hypotheses or open derivations. The result does
not address masses of the quarks, family mixing, full SM anomalies,
gravity or observer/qualia earning conditions. Failure of this candidate
would scope to these hypotheses, not the whole generated architecture.

Review must check the original operator normalization, global transition
and endpoint calculations, exact physical representatives, compact
extension theorem application, complete operator domain and nonzero
spinor bracket. Finite control code cannot replace those analytical
duties. See verification_weak_current_2026_11_08/DESIGN.md for the
post-derivation preimplementation controls. Nothing here authorizes a
scientific run or promotes a canonical claim.
