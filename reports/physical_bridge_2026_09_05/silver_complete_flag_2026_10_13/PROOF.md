# Complete positive flag complex on the fixed silver cusp

Authored before execution. This is an analytic argument with finite exact
controls, not independent specialist acceptance. It concerns one supplied
smooth complete base, flat coefficient and end class. It does not derive
those data from the founding principle.

## Fixed differential and end weights

Use the source snapshots of the foundation admission and transport proofs.
The complete minimal and maximal flat differential domains coincide by
scalar cutoff commutators; Q=D+D* has its unique self-adjoint closure.
Bounded comparison of the admitted harmonic H_b with K_b gives the same
closed differential complex and reduced cohomology. Adjoint domains and
profiles need not be the same. We calculate with K_b, not an exactly split
global H_b. Gate4's compulsory mixing is preserved by this comparison.

In the temporal peripheral frame D=dr partial_r+d_T, with r-independent
flat d_T=d+N_X dx+N_Y dy. The peripheral split is literal; it need not
extend through the core. A and Xi commute, and d_T preserves each flag
weight. In a simultaneous eigenbasis the squared L2 density of a component
with j tangential covectors and flag weight w is, up to a fixed positive
torus metric factor,

    rho_(a,w,j)(r)=exp((2j-2)r/ell-2ar
                     +ell b w(exp(2r/ell)-1)).

The same density applies if that component also has dr. For W the weights
are +1 four times and -4 once; for F they are +2 six times and -3 four
times. Dual weights reverse. All charged weights are nonzero. Polynomial
or exponential-linear factors from A do not defeat the superexponential
sign. Positive weights exclude constant end sections; negative weights
admit constant sections in all tangential form degrees.

## Bounded radial homotopies

Take a sufficiently high seam R. Since there are finitely many weights,
radial eigenvalues and degrees, choose a common kappa>0 so that
partial_r log rho>=2kappa for every positive component and <=-2kappa
for every negative component on r>=R. Increasing R achieves this for
every fixed b>0. No bound uniform as b tends to0 is asserted.

Write a form alpha(r)+dr wedge beta(r). For the positive block set

    h_+ u(r)=-integral_r^infinity beta(s) ds.

The conjugated Volterra kernel has norm bounded by exp(-kappa(s-r))
for s>=r. Young's inequality gives its L2 norm <=1/kappa, component
by component. On smooth forms of compact upper support,
D h_+ + h_+ D = identity. Maximal graph approximation at infinity and
the bounded operator extend that identity to the closed complex. Thus the
positive block is acyclic. This does not mean it has no local Q zero
Cauchy columns: those live on a half-end with a lower boundary term.

For the negative block choose a smooth normalized averaging function
eta supported in [R,R+1]. Let p u=integral eta(t) alpha(t)dt on the
torus, and let i extend this section constantly in r. Define

    h_- u(r)=integral eta(t) integral_t^r beta(s) ds dt.

On the tail its Volterra kernel is bounded by exp(-kappa(r-s)); on the
fixed strip all weights are mutually bounded and the remaining averaging
operator is bounded. Constant extension is bounded because every negative
component is integrable. The operators commute with the fixed d_T and

    p i=identity,  D h_-+h_- D=identity-i p.

The averaged trace avoids an unbounded point-evaluation map on the maximal
graph domain. These identities first hold for smooth forms and then in
the graph closure. The negative complex therefore retracts boundedly onto
the full torus complex of its negative flag coefficient, including its
nontrivial unipotent differential. It is not replaced by independent
global scalar lines or by its H1 alone.

## Core matching and the finite complex

Cover M by a compact core with a collar and the high exterior. The
overlap is a finite cylinder. A radial smooth partition has bounded
derivative, so multiplication gives bounded maps on the differential
graph domains. The usual restriction and difference maps give the
Mayer-Vietoris cone, with a bounded right inverse obtained from this
partition. Compact collar contraction compares the overlap to the torus;
the exterior contractions above retain its negative part and kill its
positive part. Eliminating the common negative overlap yields

    C_complete(E) quasi-isomorphic to
    Cone(C(core;E) -> C(torus;E_positive))[-1].

Equivalently this is the compact mixed de Rham complex with relative
tangential data in the positive subbundle and free tangential data in the
negative subbundle. The seam subbundles are d_T-invariant, so it is a
complex. Its adjoint normal data are complementary; these standard local
relative/absolute principal symbols are elliptic. Compact mixed Hodge
theory and local collar extension give its smooth de Rham cohomology.
Marked cellular comparison computes that cohomology. This comparison is
not equality of finite cochains and unknown harmonic wavefunctions.

For the inherited marked core use C^0=E,C^1=E^3,C^2=E^2. If P,Q are
the two commuting cusp holonomies, let B,F be the bulk coboundary and
relator matrices, R1 their literal cusp word derivatives and

    D_T=(P-I,Q-I)^T, G_T=(I-Q,P-I),
    R2=-Q Fox(abAB)_(a,b) diag(t^-1,t^-1).

The old spectral completion supplies and verifies
R1 B=D_T and R2 F=G_T R1. Let pi project onto the positive peripheral
coefficient (not a global flat projection), and m be its rank. The cone
has dimensions (n,3n+m,2n+2m,m) and differentials

    d0=(B,pi)^T,
    d1=((F,0),(diag(pi,pi)R1,-D_positive)),
    d2=(pi R2,-G_positive).

Verify d1d0=d2d1=0, including the R2 sign. Native full ranks give every
degree. The separate LES method computes induced restriction ranks
r0,r1,r2 by quotienting exact boundary classes, then uses

    h_k=dim H^(k-1)(torus;positive)-r_(k-1)
        +dim H^k(core;E)-r_k.

The actual nonzero maps, not only domain dimensions, are load-bearing.
Since both finite spaces have Euler characteristic0, the cone index is0.
This Euler statement does not determine its H1,H2 or endpoints by itself.

## Closed ranges and charged harmonic kernels

In the orthonormal end frame the underlying hyperbolic de Rham Dirac
operator has bounded curvature; the nonabelian lifted end coefficients
are bounded zero-order terms. The flag term is

    V_flag=-b exp(2r/ell) hat-c(dr) Xi_E.

Here hat-c=epsilon+iota, and it anticommutes with every principal
c=epsilon-iota. Xi_E commutes with the remaining end coefficients.
Squaring Q therefore leaves no uncontrolled first-order wall term:
V_flag^2=b^2 exp(4r/ell) Xi_E^2. Its derivative and cross terms with
bounded coefficients are bounded below by -C exp(2r/ell)-C. The base
Weitzenbock estimate gives, for compact upper-supported tail forms,

    ||Q u||^2 >= ||nabla u||^2/2
      +integral (c b^2 exp(4r/ell)-C exp(2r/ell)-C)|u|^2,

for some c>0 because no charged weight is zero. Constants depend on the
fixed end; their numerical values are not computed here. The scalar
commutator cutoff proof extends the form estimate to the complete graph
domain. Tail mass of a graph-bounded sequence tends uniformly to0.
Local elliptic estimates and Rellich compactness on each compact cut
then give compact graph embedding. Thus Q has compact resolvent, finite
kernel, and its differential has closed range. This is a charged result;
it is false as a proof for the zero-flag neutral channels.

Flatness gives ||Q u||^2=||D u||^2+||D* u||^2 on the complete domain,
so global zero modes are closed and coclosed in each degree. The finite
cone gives all their multiplicities. Bounded H_b/K_b comparison transfers
closed differential ranges and harmonic multiplicities, not this specific
positive spectral estimate or wavefunctions. The positive b transport
already proved on the foundation branch makes these counts independent
of b>0. It does not select b or make it a finite-norm modulus.

## Physical scope

Hodge duality pairs E with E* and degree k with3-k, using dual metrics;
the positive/negative flag assignments reverse. The full Weyl map of the
supplied twisted parent still must be used, rather than reading one H1
as net chirality. A zero charged index in this model is not a no-go for
defects, new sourced ends, incomplete bases, boundary sectors, other
generated carriers or the full programme. Conversely the compact cover's
three-family selected-plane result is not a count for this domain.

No extra species are discarded. Neutral/gauge zero weights, their
threshold and global modes, full real bosonic gauge quotient, superfield
variations at infinity, couplings, anomalies and UV/gravity remain duties.
The geometric coefficient, parent, end metric and positive asymptotic
class are supplied. No observer or qualia is identified by this complex.
Primary existence source: https://arxiv.org/html/2109.01776v1. Its
application and the separate complete-domain argument are frozen under
sources. Finite predicates support their explicit algebra only.
