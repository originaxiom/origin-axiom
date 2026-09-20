# F09 authored interaction and operator argument

Frozen before execution; finite exact tests are not independent review
of the analytic application. This applies only to F08's supplied parent.

## 1. A gapped coefficient sector already in the parent

The decomposition used in F08 includes (10,6), with 6=exterior-square E.
Functorially induce the full flat connection C and its positive-metric
split A+Psi. The exterior representation respects commutators, adjoints
and covariant derivatives. Hence flatness, moment equation and parallel
Higgs identities descend unchanged. No additional scalar field or local
source has been added. For a scalar fourth-root twist the six transition
is multiplied by chi^2, a real sign; local equations are unchanged.

On p-forms put T=sum_i exterior_multiply(e^i) tensor exterior_lie(S_i),
where S_i are F08's boosts. The exact matrices H=T*T+TT* give

    H0=H3=2 I6,
    spec(H1)=spec(H2)={1 (10),3 (6),4 (2)}.

The same parallel-Higgs computation as F08 yields Delta6=Delta_A+H.
Complete cutoffs and bounded Higgs coefficients extend the form identity
to the unique ordinary-L2 realization. Therefore Delta6^1>=1 and it has
no L2 zero mode, on every base in scope, including real-sign twists.
In curvature-radius-one units its positive Hodge resolvent obeys

    ||(Delta6^1+p^2)^-1|| <= 1/(1+p^2), p^2>=0.

This is an internal operator statement. It is not an absolute physical
mass prediction. In particular, a full bosonic propagator needs its
gauge fixing, constraints and normalization retained; a four-fermion
Wilson coefficient cannot be asserted from this inequality alone.

## 2. The actual invariant vertex and its statistics

R38 identified the one-form parent vertex Tr(psi wedge [w,psi]). In
the (spinor,4)--(spinor,4)--(10,6) channel, the Spin(10) factor is the
already-checked symmetric spinor-to-vector tensor. The SU4 factor is
the volume contraction E tensor E tensor exterior-square E -> C.
It is antisymmetric in the first two coefficient labels. Together
with the alternating internal form tensor it is symmetric in the
combined coefficient/form labels, as required for the left-Weyl
bilinear; multiplication by the spin epsilon gives an antisymmetric
Grassmann coefficient matrix. It need not vanish for a repeated profile.

Write K_(AB),(CD)=epsilon_ABCD in the ordered unit exterior basis.
The complete sl4 equations L(X)^T K+K L(X)=0 prove its invariance;
the induced differential also obeys the exterior-product Leibniz law.
The normalized profile factor is

    V(u,v,w)=sum_k Q_k(u,v)^T K w_k,
    Q_k=sum_(i<j) epsilon_ijk (u_i wedge v_j+v_i wedge u_j)/2.

The omitted overall constant is common and fixed by the parent, not
a freely chosen mirror coupling. The unnormalized alternating sum
over all i,j is 2V. The Spin(10) factor, kinetic normalizations and
g7 are not fitted or computed anew here.

For F08's possible zero modes u_i=(0,b_i1,b_i2,b_i3), identify a spatial
bivector with its oriented three-vector (23,-13,12). Then

    Q(u,u)=cofactor(b),
    cofactor(b)=b^2-tr(b^2) I/2 for symmetric trace-free b.

For real b, diagonalization and tr(b)=0 imply
sum_(i<j) lambda_i^2 lambda_j^2=(sum_i lambda_i^2)^2/4. Hence
|Q|^2=|b|^4/4. A nonzero REAL tensor in the pointwise kernel therefore
has a nonzero local vertex source. For b=diag(1,-1,0), w3=e0 wedge e3,
V=-1 in this normalization. This refutes a universal equal-profile
wedge cancellation for bundle-valued one-forms. In contrast, a profile
factoring as a single spatial one-form times one coefficient vector
has Q=0. Over C, the nonzero trace-free symmetric b=v v^T with
v=(1,i,0) has rank one, b^2=0 and Q=0. The reality qualifier matters.
None of these pointwise examples supplies a global physical zero mode.

## 3. Whole coupling tensors, not selected-profile ratios

F08 gives a global antiunitary a(v)=J conjugate(v) from E_chi to its
dual, where J=diag(-1,1,1,1). On the six take L=exterior-square J.
Then K^T=K=K^-1, L^T=L=L^-1, and L^T K L=-K. The induced antiunitary
a6=L conjugation maps the six coefficient to its dual with the same
complete operator domain. Exterior functoriality gives

    Q(a u,a v)=L conjugate(Q(u,v)),
    V_dual(a u,a v,a6 w)=-conjugate(V(u,v,w)).

The determinant sign is conventional and immaterial to norms; it is
retained rather than silently discarded. The natural volume identifies
the dual six back with six by K. Then S=K L is real orthogonal,
S^2=-I and commutes with the induced connection. S conjugation is
therefore an antiunitary square-minus-one symmetry of the six Hodge
operator and its resolvents. This is an internal quaternionic structure,
not a claim to identify physical time reversal. Real chi^2 is needed
for descent. A general complex scalar twist is not automatically in
the same SL4 parent and does not preserve that descent statement.

The pointwise vertex relation integrates whenever the integrals exist.
On any finite-dimensional paired normalized spectral subspaces, the
entire trilinear coupling tensors are related by conjugation and unitary
changes of basis. Their Hilbert-Schmidt norms, and singular values of
any corresponding flattening, agree. No discrete complete eigenbasis
is assumed on the noncompact base. In the full spaces the analogous
statement concerns a defined bounded multilinear form, not a divergent
sum over a continuum.

For any L2 source j, antiunitarity and the spectral theorem also give

    <Tj,(Delta6+p^2)^-1 Tj>=<j,(Delta6+p^2)^-1 j>, T=S conjugation.

This quadratic response is real and nonnegative. For a bilinear source
built from profiles, L2 integrability of that source is an ADDITIONAL
condition; L4 profiles suffice. Global L2 matter alone does not prove it.
The finite positive-matrix control checks both directions: a symmetric
propagator gives equal whole responses, while an explicitly noncommuting
positive propagator can distinguish them. A selected mediator can have
zero versus nonzero overlap even when the full paired spaces agree.

## 4. Physical consequence and non-conclusions

This earns a nontrivial parent one-form vertex on the tensor sector and
a controlled six-coefficient spectral problem. It does not earn a
mirror-selective coupling hierarchy in the unchanged balanced vacuum.
The pairing is stronger than equality of free eigenvalues: it constrains
the actual normalized wedge tensor in this channel. This is not a
statement about every parent interaction, the complete quantum measure,
a spontaneously selected phase or all possible sourced backgrounds.

The next candidate should specify which background/interaction/domain
breaks this intertwining while satisfying the full equations and keeping
the desired gauge group, anomalies and normalizable states. Nonzero
vector VEVs are not silently a solution: R33 already tracks their gauge
breaking. The added H-theory's quartic and source positives remain
valid on their own assumptions. No global number of Codazzi modes,
chirality, physical parameter, gravity or full TOE is established here.

Primary action: https://arxiv.org/html/1812.06072v2 (2.13 and B.29).
Prior proofs: F08, R38, R33/R34. This connection is not claimed novel
in the literature, and no other seat's scientific files are changed.
