# Conditional odd form estimate without squaring the half-pole

Authored analytic argument, not independent specialist acceptance.
The actual global spin/gauge/Spin-c pointed realization remains assumed.
Use the supplied semi-flat metric, flat retained E8 coefficient, periodic
fibre spin and either EXTREME graded trace law. The scalar background
is zero. A condensate, intermediate Lambda or nonflat gauge connection
would require a new estimate. The full ordinary and canonical bundles
are NOT identified globally by a bounded local shift.

## Core and one controlled vertical gradient

Write GammaV=i c3c4 and decompose psi=psi_++psi_-. For the extreme
allowing only positive critical traces, take the dense local graph core
to consist of smooth compact-base sections away from the section plus
cutoff z^(-1/2) critical profiles in GammaV=+1. The negative component
of this core has support away from the puncture. Closure gives its
minimal vertical domain. The opposite extreme interchanges plus/minus
and uses conjugate profiles. Both horizontal spin components are kept.
Finite unitary coefficient charts and a partition of unity give this
same core on the admitted cusp bundle. Horizontal vector fields vanish
normally at the section, so their action on a critical profile is L2.

On an ordinary flat fibre, for a regular/minimal component eta,

    ||E3 eta||^2+||E4 eta||^2=||D_V eta||^2,
    D_V=c3 E3+c4 E4.

Start on compact support away from the puncture, where the flat unitary
connection and commuting vertical derivatives give the identity by
integration by parts. Actual flat seam transports are unitary, so seam
terms cancel. The identity controls the gradient of every difference
in a vertical graph-core approximation; closure therefore proves it
on the MINIMAL domain. No positive half-pole gradient is bounded this
way. Its divergent derivative is exactly the reason to use the opposite
component, not a defect discarded by the argument.

The source puncture_fredholm proof exhibits the graph domain as minimal
plus finite critical representatives; total_domain supplies a compatible
compact-base total core. Their four source proofs were personally read
in full and stored byte-faithfully. Gil--Krainer--Mendoza Proposition3.5
and Theorem3.6, https://arxiv.org/html/math/0410176 (accessed2026-10-14),
were reread personally for minimal domains and the finite asymptotic
quotient. Their compact cone theorem is NOT applied to the whole
noncompact surface. The new form transfer below is derived here.

## Keep the full horizontal expression

In the actual physical norm set D=V+H, with V=D_V and

    H=c1 E1+c2(E2-1/(2ell))+c1c3c4/(4ell)+i beta c1/ell.

Here beta=-6n or3/4-6n in the respective parent. The contracted density
and mixed spin terms are both retained. H is formally symmetric on
compact-base sections with the physical density. V is vertically
symmetric on the extreme trace law. H preserves vertical chirality.

The four actual frame brackets give, on the puncture-free core,

    {V,H}=F=K3 E3+K4 E4,
    K3=(-c1c4+c2c3)/(2ell),
    K4=(-c2c4-c1c3)/(2ell).

There are no remaining horizontal derivatives or second-order terms.
The density constant and scalar beta c1 anticommute with V; the mixed
spin term supplies essential half-coefficients. Both K3 and K4 are
skew-Hermitian, reverse GammaV and have norm1/ell. Since E3,E4 are
skew in each flat fibre, F is formally symmetric there.

On the specified core the mixed form

    2 Re <V psi,H psi>=<psi,F psi>

is an integration-by-parts identity, NOT a statement that H psi lies
in Dom(V) or psi lies in Dom(D^2). To verify it near the puncture:
every vertical chirality pairing in this form couples plus to minus.
The MINUS component is zero in a neighbourhood of the puncture on
this core, and H preserves that property. Thus the deleted-circle
boundary term vanishes before taking its radius to zero. Only after
the form estimate is proved do we pass to graph closure. No integration
of a divergent squared positive-component gradient is used.

Vertical chirality reversal and symmetry let us write the cross form as

    <psi,F psi>=2 Re <psi_+,F psi_->.

Transfer derivatives in the other pairing onto the regular component;
its support is away from the puncture on the core, so no critical trace
term occurs. The gradient identity and the two matrix norm bounds give

    |<psi,F psi>| <= (2sqrt(2)/ell)||psi|| ||V psi||.

For the opposite extreme transfer onto psi_+ instead; the bound is the
same. A mixed/intermediate Lambda is not justified by this proof: both
chiralities can have critical coefficients, and derivative-transfer
and plane-variation terms need their own account.

Apply 2sqrt(2)ab<=a^2/2+4b^2 with a=||V psi||,b=||psi||/ell:

    ||D psi||^2 >=||V psi||^2/2+||H psi||^2
                                      -4||psi||^2/ell^2.       (1)

This inequality itself provides graph control of V and H. For a Cauchy
sequence in the total graph norm, apply(1) to its differences: V and
H become Cauchy in L2. Their limits are their distributional actions,
with the same extreme vertical domains by closedness, fibrewise/direct
integral closure and local chart localization. The form therefore extends
to the admitted total graph closure. It DOES NOT establish that H psi
lies in Dom(V); the source's explicit g still violates that stronger claim.

## The complementary TOTAL block is now estimated

For the odd Q8 coefficient A^2=B^2=-I and AB=-BA. Choosing an orthonormal
basis of the A=i eigenspace and transporting it with B decomposes the
fibre representation into identical two-dimensional quaternion blocks.
All112 odd directions give56 such blocks, including conjugate modules.
This is a unitary fibre argument, not a choice of a physical family basis.
The upstream extreme-domain vertical gap proof and projection control
thus extend to this finite direct sum with the same metric constants.

Let P be the fibrewise kernel projection and Q=I-P. Retain the supplied
admitted global transitions. The upstream horizontal_projection proof
gives bounded [D,P] and B=QDP, since its cylinder-profile estimates are
unchanged by finite multiplicity. The scalar R shift commutes with P;
this statement is LOCAL on the candidate's OWN bundle, not a global
ordinary/canonical identification. Thus Q preserves the total domain
and QDQ is a closed selfadjoint diagonal block. On Q sections,

    ||V psi||^2 >= c^2(y/A)||psi||^2

for y large, with the upstream unspecified c>0. Using(1) and the bounded
opposite-block leakage P DQ=B^*,

    ||QDQ psi||^2 >=[c^2 y/(2A)-4/ell^2-||B||^2]||psi||^2.   (2)

This is a growing uniform TAIL bound, not an estimate of the inverse
of D_V substituted for the actual inverse of QDQ. It holds for both
extreme domains and every horizontal/fibre frequency under these
hypotheses. It is the new conditional complementary estimate.

## Actual harmonic phases and the physical limit of the conclusion

The retained L6 has fourth power-I6. On the full odd E8 coefficient
T^4=-I112. T commutes with A, so the projected cylinder kernel, which
selects A=i or-i, has only odd-eighth x phases. Supplied cusp section
signs+/- shift them by1/2 and preserve the minimum distance1/8 from
an integer. Native and separate exact character projectors enumerate
all A=+/-i phase ranks; they are READ-OUTS, not generations.

The source profile projection has geometric beta_P=gamma/4-6n;
the canonical block instead adds its fixed3/4, on its own bundle.
That changes only a bounded constant in the confining projected cusp
operator; the leading2pi(k+alpha)y term keeps |k+alpha|>=1/8. The
previous projected confinement proof therefore remains conditional
with beta_P=gamma/4+3/4-6n. It is not an index-invariance assertion.

Given local compactness of the admitted total domain, the growing(2)
tail bound and confining finite-rank P block give compact graph embedding
of both diagonal ODD blocks; the bounded off-diagonal restores an odd
operator with compact resolvent. This uses the source local normal-family
derivative/Rellich control, not an unverified compactness assertion about
a merely selfadjoint operator. If those global hypotheses are not admitted,
the conclusion stays a conditional end calculation.

Combined with the separate regular-even tail estimate, the admitted
canonical full operator is a candidate for Fredholmness at0, under the
specified zero-scalar/extreme-domain/global hypotheses. Its actual index
and kernel have NOT been computed or equated to the flat count. The
ordinary n=0 benchmark retains the EVEN Weyl sequence and is not repaired
by controlling this odd sector. The same scalar/flux/embedding/metric
and extreme choice remain supplied, not derived from genesis.

The next tasks are independent analytic scrutiny and actual pointed
global admission, then the complete charged kernels, physical Higgs/
source/end action and stationary equations, interactions and anomalies.
No first-generation masses, SM parameters, three-family selection,
observer/qualia mechanism or gravity follows from this estimate.
