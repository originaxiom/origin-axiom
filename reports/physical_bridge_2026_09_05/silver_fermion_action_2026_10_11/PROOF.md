# The four-Weyl/Hodge joint, with its assumptions visible

Authored derivation; execution and nonauthor acceptance are separate duties.
This is the same SUPPLIED compact twisted parent and boundary, not a genesis
derivation or complete physical theory. Finite controls do not prove the
global PDE. The coefficient metric is positive and physically identified
with the unchanged cyclic metric, as priced in the preceding packet.

## 1. Odd components and the actual quadratic action

Use DESIGN's canonical spinor and superspace convention, NOT Lüdeling's
A.3 convention (his raising/lowering positions and epsilon signs differ).
For lower odd spinors write f g=f1 g2-f2 g1. Under invariant matrix trace
this product is symmetric. D_A=partial+i ad A, D_minus=D_A-ad B and
D_plus=D_A+ad B. Every bar below is an actual reversed-product dagger.

At quadratic fermion order direct multiplication of G, G^-1 and Z gives
the real K-sector internal density, BEFORE integration by parts,

    -1/2 Tr(psi_i D_plus,i chi) + h.c.

There are independent first jets on chi. The linear Z terms are
sqrt(2)(theta psi_i-bar-theta-components bar-psi_i); its cubic gaugino
terms contain partial_i chi+i[bar-phi_i,chi], not phi_i. Degree-four
commutator terms and the constant Z=2B must be retained before taking
the trace. Together they give the conjugate density. Thus

    -psi D_plus chi/2
       = chi D_plus psi/2 - div Tr(psi chi)/2.

The invariant trace and genuine odd signs establish this identity for
the full Lie algebra, not just the matrices used for controls. Its boundary
primitive -integral Tr(psi_n chi)/2 is not generally zero. On the declared
trace, chi is internally parallel in k and integrated Pi_k psi_n=0,
so the primitive and its variations vanish. This is an integrated law,
not a pointwise vanishing of every coefficient component.

The six epsilon terms of the relative superpotential give

    Tr(epsilon_ijk psi_i D_minus,j psi_k)/4 + h.c.

The fixed affine reference counterterm is linear in Phi and has zero
fermion Hessian. The variation of the quadratic primitive nevertheless
has the usual tangential surface pairing of psi_t with delta psi_t.
It vanishes by the SAME integrated cyclic isotropy of A1. Nonzero bulk
commutators remain: this is not a free or abelian truncation.

The external chiral-coordinate shift and W superderivatives give equal
principal kinetic terms -i Tr(chi sigma partial bar-chi)/2 and
-i Tr(psi_i sigma partial bar-psi_i)/2 in the frozen convention. Native
controls use a combined covector; the separate tuple instrument checks
each of the four covectors. This proves the component normalization of
the principal quadratic action, not every external background coupling
or the full Lorentzian Hamiltonian. Supplied compact-gauge covariance
replaces partial_mu by D_mu in that parent; its nonlinear WZ compensation
and boundary supersymmetry closure have NOT been discharged here.

Set chi=sqrt(2)lambda and psi=sqrt(2)rho. The normalized internal bilinear
is the symmetric quadratic mass functional

    Tr(lambda div_Dplus rho + rho curl_Dminus rho/2) + h.c.

Its Euler operator on z=(lambda,rho) is

    R z = (div_Dplus rho, curl_Dminus rho-D_plus lambda).

Formal transpose here uses the invariant COMPLEX BILINEAR trace and
integration by parts. The physical adjoint instead uses the positive
Hermitian metric. These two notions must not be conflated.

## 2. An explicit norm-preserving full-operator map

In a compatible unitary frame A is Hermitian, i ad A is skew-Hermitian,
and ad B is Hermitian. Consequently the coefficient covariant derivative
D_minus,i has formal Hermitian adjoint -D_plus,i. This follows directly
from trace cyclicity and actual dagger. In the twisted parent use the
Levi-Civita covariant divergence and exterior differential; volume and
Hodge star are parallel. Frame-coordinate formulas below are invariant.

Let D=d+i ad Phi be the flat differential on coefficient-valued forms,
and Q=D+D*. Define the fiberwise maps

    S_odd(lambda,rho)  = rho + lambda vol_3,
    S_even(f,v)        = -f + *v.

They are isometries for the canonical kinetic metric. Scalar and one-form
norms add; Hodge star preserves norms. In dimension three,
D* on one- and three-forms is -*D_plus*, whereas D* on two-forms is
*D_plus*. Direct substitution gives

    Q S_odd = S_even R,
    Q S_even = S_odd R*.

For example Q(rho+lambda vol) has scalar -div_Dplus rho and two-form
D rho-*D_plus lambda. Its Hodge image is exactly R, including the
zeroth-order Higgs term. The second equation follows either directly
or from the isometries and formal adjoints. The native explicitly checks
it using noncommuting A/B in their matrix-unit adjoint representation;
the reference uses a differently ordered creation/contraction realization.
Both retain every zeroth-order term. No eigenvalue/label matching is used.

The doubled Hermitian internal operator on odd/even coordinates is
[[0,R*],[R,0]], unitarily equivalent to Q. This is the standard adjoint
completion of a Weyl mass operator, not eight independent Weyl particles.
Actual coefficient conjugation J has J D_minus=D_plus J. It sends R
to R*, while exchanging each charged coefficient with its dual.
The conjugate map is therefore -J lambda+*J rho; it is signed Hodge
conjugation of S_odd, not a demand that L itself be separately real.

## 3. The physical trace is the previous full Hodge trace

For outward collar dr, write forms alpha+dr wedge beta. Essential physical
fermion traces from the SAME superfield law and response are

    lambda in internally parallel k,
    rho_t in A1,
    integrated Pi_k rho_n=0.

Under S_odd, rho_t is alpha1, rho_n is beta0, and lambda vol is beta2.
The third and first conditions are precisely beta0 in (A0)^perp and
beta2 in (A2)^perp, since A0=k and A2=ann_B(k). Under the conjugate map,
J lambda is alpha0 in k; *J rho_n is alpha2 in A2; the remaining normal
one-form is in (A1)^perp by cyclic maximal isotropy. Thus the combined
physical trace is EXACTLY alpha in A, beta in A^perp for the same metric.
No harmonic L is changed. The statement uses cyclic annihilation, not
pointwise reality of a charged L or an assumed unitarity of flat holonomy.

The normal Green pairing of R is the scalar/normal pairing plus the
oriented tangential curl pairing. They vanish by k-projection and A1
isotropy, respectively, when paired with the conjugate domain. These
are maximal annihilators: k pairs perfectly with its complementary normal
trace and A1 is a maximal cyclic polarization. Mapping to Q also proves
maximality, including the finite harmonic sector, not only high modes.

For any nonzero real tangent xi=(x,y), the physical odd high trace is
lambda=0, rho in span((-y,x,0),(0,0,1)). Its conjugate has the matching
principal trace. The normal matrix and tangential matrix of R are

    R(n)=[[0,n^T],[-n,cross(n)]],  R(n)^T R(n)=|n|^2 identity.

The doubled Green current is zero on the half-dimensional allowed trace.
The adapted Hermitian symbol exchanges this trace with its complement,
and squares to |xi|^2. Projection from either sign eigenspace is therefore
an isomorphism at EVERY nonzero xi. The reference proves these as exact
polynomial matrix identities; a wrong unrestricted chi trace has nonzero
Green current. Harmonic smoothing modifications do not change the symbol.

On the smooth compact core the bundles are Hermitian, Q is Dirac type,
boundary compact, and the classical order-zero projector has the above
elliptic symbol. Bär--Ballmann Standard Setup3.1 and Theorems3.6,3.9,
3.11,3.15 therefore supply the maximal adjoint domain, smooth kernels
and selfadjoint elliptic realization after the unchanged prior Hilbert-
complex comparison. They use INWARD normal; reversing it changes the
Green sign but not its annihilator or ellipticity. H1 traces alone enter
the first-order realization. Secondary normal chi jets from the response
packet are not independent H1 constraints: they were derived only on
smooth linear solutions. Auxiliary-elimination scalar derivative conditions
of static PROOF4 remain required for the bosonic/supersymmetric domain.

## 4. What this bridge does and does not earn

Conditionally on the supplied parent/metric/domain and flat admitted
background, the canonical free fermion zero modes now correspond to
H1(K) plus H3(K) for left fields, H0(K) plus H2(K) for actual conjugates.
Here K is the SAME cone, by the previous complementary quasi-isomorphism.
For charged coefficients the prior proof gives H0=H3=0, so its earlier
J(E)=dim H1(E)-dim H2(E) is the tree-level net Weyl index on THIS domain.
This uses coefficient duality; it does not force a charged sector to have
J=0. Gauge endpoint modes are not discarded. The old rank-five family
still has 35 dimension choices and cannot reach common index3 in that
family alone. No fresh coefficient/rank census is claimed in this packet.

This is a faithful operator/domain map, not a complete model. Nonlinear
supersymmetry preservation with normal/external jets, interactions among
actual normalized zero profiles, boundary anomaly/inflow, quantum/large-
gauge consistency and dynamical stability remain open for the construction.
Its parent, cut, metric, affine primitive and L are supplied, not selected
by the OA principle. Three families, physical parameters and gravity remain
distinct obligations. No SM/TOE or observer/qualia derivation follows.

## Sources and custody

Local authoritative primitives: static-energy DESIGN/PROOF, superfield-
response PROOF and complementary PROOF, and spectral-completion PROOF3-4.
The old Ainf nonlinear failure is NOT the present strict A boundary.
Primary texts personally read in relevant sections, October11:
[Lüdeling sections4/A.3](https://arxiv.org/html/1102.0285v1),
[Braun et al. B.1](https://arxiv.org/html/1812.06072v2#A2.SS1),
[Bär--Ballmann sections2-3](https://arxiv.org/html/1307.3021v1).
Do not copy the published component signs without a complete convention
dictionary. The direct fixed parent is authority for this packet. The
connection choice in the K sector is determined by its bar-Phi factor.
No universal source erratum is asserted from a convention-sensitive check.
