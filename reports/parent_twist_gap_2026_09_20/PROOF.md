# F05 authored join: a smaller gauge algebra is not yet a matter spectrum

This is a pre-execution analytic candidate. Standard ingredients are
credited below; the application and its exact normalization are checked
here. No independent expert review or physical completion is asserted.

## 1. A global central twist changes the bundle without changing local PDEs

Let h be the chosen complete geometric SL2 holonomy lift and rho=Sym^3(h)
in R39's normalized SU2-invariant Hermitian metric. Given a character
chi:pi1(M)->{1,i,-1,-i}, define rho_chi(gamma)=chi(gamma)rho(gamma).
It is a representation into SL4(C), since chi^4=1. The SU4 subgroup
already exhibited by R38/R39 integrates into the candidate E8 parent.

Tensor the homogeneous coefficient bundle by the flat unitary line L_chi.
On a simply connected patch the line has a parallel unit frame, so the
local connection and Higgs fields are exactly R39's C,A,Psi. On overlaps,
the old unitary transitions acquire locally constant central phases.
All local curvature and moment-map residuals remain zero, and the positive
Higgs norm stays finite. The resulting E8 transition functions likewise
define a global classical background. This is an actual global bundle
construction, not adding a matrix to the local invariance equations.

For m004's documented presentation, chi(a)=1, chi(b)=i respects the relator
aaabABBAb, has chi(mu)=i, chi(lambda)=1 and exact order four. No geometry
or action has selected it. A primitive cube-root scalar would instead
fail det(rho_chi)=1 and is not licensed by this SU4 construction.

## 2. Gauge reduction and the failure of the displayed self-duality

R39 identifies one invariant vector in exterior-square(4), none in 4,
and none in traceless End(4). Its local invariant algebra consists of
D5's 45 generators plus ten generators from (10,6). Under the central
element iI4, the 4 has phase i, bar4 phase -i, 6=exterior-square(4)
phase -1, and adjoint 15 phase +1. Thus the ten additional locally
parallel generators now carry the nontrivial character chi^2, whereas
all D5 generators remain globally parallel.

Equivalently the entire B5 root system loses exactly its ten short roots
+/-e_i, retaining the forty long roots +/-e_i+/-e_j and its five Cartan
directions. This is compact so(10), not merely a count of 45. We assert no
unverified global quotient of Spin(10). Complete finite-volume cutoffs
put the surviving constant-norm parallel adjoint sections in the natural
gauge quadratic-form domain, as in R39.

R39's antisymmetric J is invariant under rho but transforms by chi^2
under rho_chi. With chi of order four it is not a global V_chi-to-V_chi^*
map. More strongly, the exact m004 generator has

    tr Sym^3(h(b)) = -8+4 omega !=0,
    tr V_chi(b)=i*(-8+4 omega),
    tr V_chi^*(b)=-i*(-8+4 omega),
    omega=(-1+i sqrt(3))/2.

The traces differ, so these representations are not isomorphic. This
uses the known exact geometric matrices in B1297 and is independently
checked; a literal matrix inequality alone would not suffice. For an
order-two scalar twist chi^2=1, both the invariant wedge line and J
remain. Removing this particular pairing mechanism does NOT itself
establish unequal spectra or nonzero chirality.

## 3. The actual positive operator contains more information than the index

Work in g=z^-2(dx^2+dy^2+dz^2), and let

    C_x=E/z, C_y=iE/z, C_z=H/(2z),
    A=(C-C^dagger)/2, Psi=(C+C^dagger)/2.

In the orthonormal coframe (dx/z,dy/z,dz/z), the Hermitian coefficients of
Psi are

    S_1=(E+F)/2, S_2=i(E-F)/2, S_3=H/2.             (1)

Their squares sum to (15/4)I4; hence the defining-four Higgs norm is 15,
agreeing with R39. Direct computation with the hyperbolic Christoffel
symbols gives

    partial_i Psi_j+[A_i,Psi_j]-Gamma^k_ij Psi_k=0.  (2)

Thus Psi is parallel as an endomorphism-valued one-form for A and the
Levi-Civita connection, not constant as a coordinate matrix. Omitting
the Christoffel or connection term is not a valid simplification.

Let T=Psi wedge, d_C=d_A+T. For compactly supported forms expand the
Hodge Laplacian. The mixed terms
d_A T^*+T^*d_A+d_A^*T+T d_A^* vanish by (2): their first-order terms
cancel by the wedge/contraction identities, and their zeroth-order
terms are covariant derivatives of Psi. Consequently

    Delta_C=Delta_A+H_p,   H_p=T^*T+TT^*.           (3)

This is the Matsushima--Murakami identity already used in R27, now checked
in the explicit R39 positive metric. Delta_A=d_A^*d_A+d_A d_A^* is
nonnegative on compactly supported forms even though A is not flat.
We do not replace it by an unqualified rough Laplacian.

With epsilon_i denoting exterior multiplication by the orthonormal
coframe, exact exterior-algebra multiplication gives

    H_p=(15/4)I+sum_(i,j) epsilon_i iota_j [S_i,S_j]. (4)

On degree zero and three this is (15/4)I4. On degrees one and two its
eigenvalues and multiplicities are

    9/4 (6), 19/4 (4), 25/4 (2).                   (5)

For another derivation, -S_i are spin-3/2 su2 generators, the form factor
in degrees one/two is spin one, and (4) is 15/4 minus their spin coupling.
The total spins 5/2,3/2,1/2 give (5). The executable derivation constructs
T and its ordinary positive adjoint, obtains characteristic polynomials,
and checks an independent block formula; it does not fit floating spectra.
Our curvature -1 normalization is fixed by (1), not borrowed from a
different Killing-form normalization in a reference.

## 4. Pass the lower bound to the complete-space domain

For every compactly supported smooth coefficient form, (3)--(5) imply

    ||d_C u||^2+||d_C^*u||^2 >=(9/4)||u||^2.       (6)

The locally constant unitary twist only changes transitions, not this
calculation, so (6) holds for V_chi and separately for V_chi^*. It also
holds mathematically after tensoring by any flat unitary finite-rank
bundle: the extra connection commutes with the geometric S_i and preserves
(2). No finite-image assumption is needed for this local estimate.
Only the scalar fourth-root twists have the specified rank-four parent
realization; larger tensor factors are not silently inserted in E8.

The metric is complete, coefficients are smooth, and Q=d_C+d_C^* has a
Dirac principal symbol and Hermitian zeroth-order part. F02's cutoff proof
therefore gives its unique ordinary-L2 self-adjoint closure. Compact smooth
forms are a graph core. Since d_C^2=0, ||Qu||^2 equals the left side of (6)
on that core, including sums of degrees. Passing to its closure gives

    ||Qu|| >=(3/2)||u||,
    spectrum(Q) avoids (-3/2,3/2),  ker Q=0.         (7)

In particular there are NO L2 harmonic one-forms in either spinor
coefficient bundle on this background and domain. This is stronger than
the equality of their uncomputed kernels in R39, but is a same-background
application of the already-known positivity mechanism, not a new
general vanishing theorem. It neither identifies all ordinary cohomology
with L2 cohomology nor denies boundary cohomology classes.

The scalar-curvature length ell restores the mathematical lower bound
9/(4 ell^2). This is not an observed mass or a sharp computed global
eigenvalue. Translating to a particular canonically normalized 4D mass
requires its action coefficients; positivity and the absence of zero modes
do not depend on a common positive overall rescaling.

## 5. The ten removed gauge generators have a spectral, not only group, test

Their invariant coefficient line is L_(chi^2), with zero Higgs action and
a flat unitary connection. For m004's chosen character, meridian transport
is -1 and longitude transport +1. On a cusp torus, lifted coefficients
are antiperiodic in x1 and periodic in x2. Therefore their transverse
covariant Laplacian has a strictly positive lowest eigenvalue

    kappa=min_(m,n in Z) 4*pi^2 |(m+1/2,n)|^2_(h0^-1)>0.

For any fixed positive h0 this follows from discreteness of the shifted
dual lattice and exclusion of zero. On the end above r=R, its quadratic
form obeys

    integral_end |d_L u|^2 >= kappa exp(2R) integral_end |u|^2. (8)

A form-norm bounded sequence has uniformly small tails by (8), and Rellich
compactness applies on each compact core. Thus the complete scalar form
domain embeds compactly in L2. The scalar Laplacian has compact resolvent.
Its zero kernel would consist of parallel sections, impossible for this
nontrivial line. Hence its bottom is strictly positive. We have NOT computed
its numerical value or selected a physical hierarchy.

This proves that the extra ten gauge directions are removed from the zero
sector in the declared complete-space problem, not merely omitted from a
representation roster. The trivial-character control has a finite-norm
parallel zero mode and no shifted-lattice lower bound, as it should.
If chi^2 is trivial on some cusp, argument (8) is unavailable there; the
specific compact-resolvent assertion is not transferred to that case.

## 6. Breaking self-duality is not the same as closing the gap

In a FIXED Hilbert space suppose Q'=Q+B with B a bounded self-adjoint
zeroth-order operator and ||B||=b<3/2. The bounded perturbation retains the
self-adjoint domain and

    ||Q'u|| >= ||Qu||-||Bu|| >=(3/2-b)||u||.         (9)

Thus Q' still has no zero mode. A same-space path seeking a massless
spinor must leave this norm ball or change a hypothesis. This is only a
necessary threshold; crossing it does not produce a BPS background or
chirality. A finite matrix control attains zero precisely at the threshold.

Flatness/harmonicity of Q' is not assumed for the inequality, but any
physical proposed deformation must independently solve its complete
equations. Changes of metric, bundle topology, unbounded asymptotics,
singular sources, boundary domains and quantum interacting phases are
outside (9). Nor does (9) establish that a character-variety deformation
has a bounded same-space operator difference.

## 7. What this earns, and what it leaves

The positive construction is a globally valid order-four Wilson-twisted
variant of the existing candidate parent, with finite Higgs norm and
unbroken compact so(10). It keeps the action and local BPS solution, rather
than importing an unrelated gauge selector. It is still an unselected
choice in an unselected E8 parent on a supplied spacetime.

Its matter test fails for a known, now quantitatively matched reason:
the geometric coefficient operator is uniformly positive. Removing its
particular global self-duality does not restore light spinor matter.
This narrows the next physical task to an actual source/nongeometric
background that changes the operator enough to close this gap, with the
full field content and domains retained. It does not close the nonsplit
or sourced routes, whose different hypotheses remain explicit in F01--F04
and R19/R29/R30.

The paper inputs are the adopted classical action and the positivity
mechanism; the detailed global twist, normalization, operator and cusp
arguments above are supplied explicitly. Three physical generations,
SM breaking, quantum anomalies/interactions, gravity and empirical
discrimination have not been derived.
