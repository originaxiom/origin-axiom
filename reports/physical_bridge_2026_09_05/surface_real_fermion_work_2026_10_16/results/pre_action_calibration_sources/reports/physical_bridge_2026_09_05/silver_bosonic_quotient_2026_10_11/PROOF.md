# A real gauge slice, derived from the actual integrated boundary

Authored conditional analytic proof before execution. Finite exact controls
verify the named algebra/compatibility mechanisms, not the global PDE or
all E8 constants. Outside review is owed. Parent, cut, metric and L are
supplied. This extends earlier compact/static and complete-cusp split
results without importing the latter's inverse or domain.

## 1. The physical zero equations separate real gauge and moment

Fix the SAME compact oriented core, flat structure-valued background
phi=A+iB with H=0 and mu=div_A B=0, and positive compatible metric.
D=D_minus=D_A-ad B; its formal Hermitian adjoint on one-forms is
D*=-div_Dplus, D_plus=D_A+ad B. For a=u+i v,

    div_Dplus a=kappa+i m,
    kappa=div_A u+i[B_i,v_i], m=div_A v+i[u_i,B_i].

Both kappa and m are Hermitian with actual dagger. Static PROOF5 gives
the real scalar Hessian ||Da||^2+||m||^2. Thus its smooth null directions
satisfy Da=0,m=0. A compact infinitesimal gauge parameter lambda is
Hermitian, with delta a=Dlambda, delta u=D_A lambda,
delta v=i[B,lambda]. Full product differentiation gives

    delta m=i[mu,lambda], D(Dlambda)=i[H,lambda],
    P lambda=D*Dlambda=-D_A^2 lambda+[mu,lambda]+sum[B_i,[B_i,lambda]],
    kappa(Dlambda)=-P lambda+[mu,lambda].

No first derivatives were frozen; their cross terms cancel. At the
harmonic background P=-D_A^2+sum ad(B)^2 is REAL Hermitian-bundle
preserving and positive in its admitted homogeneous domain. Therefore
compact gauge is a Hessian null direction. Imaginary primitives are NOT
the same gauge: m(iDlambda)=-P lambda at mu=0. Unless P lambda=0,
iDlambda is flat but not moment-zero. One may not quotient the physical
Hessian null space by arbitrary complex gauge transformations.

## 2. The mixed scalar boundary Laplacian is not assumed

Essential scalar trace is a_t in A1 and integrated Pi_k v_n=0. Allowed
real lambda has boundary value in INTERNALLY PARALLEL compact k; it has
no essential normal-derivative condition. The background is entirely
structure-valued, so every c in k extends as the SAME global parallel
field, D_A c=0,[B,c]=0. D_t lambda=0 on the boundary. Dlambda therefore
preserves a_t in A1 and its imaginary normal projection: [B_n,lambda]
has zero k projection (here it vanishes at the trace itself).

Let P0 be D*D with homogeneous smooth boundary

    lambda|Sigma in k, Pi_k D_A,n lambda=0.

This is the DEGREE-ZERO part of the previously proved Q^2 realization,
Q=D+D* on alpha in A,beta in A^perp. Indeed Qlambda=Dlambda. To have
Qlambda in Dom Q its tangential one-form must lie in A1, which holds
because D_t lambda=0, and its normal scalar must be perpendicular to
A0=k, giving precisely the integrated normal condition above. Flatness
gives Q^2lambda=P lambda with no two-form component. The prior Hilbert
complex identifies Q^2 degree by degree with the Hodge Laplacians;
degree-zero is a reducing selfadjoint sector. It is not merely an
unproved restriction of an arbitrary selfadjoint operator.

Green's identity retains

    integral <Dlambda,Dzeta>
       =integral <P lambda,zeta>+integral_Sigma <D_n lambda,zeta>.

For real lambda,zeta, taking the real part yields the physical compact
gauge pairing. Their boundary values are parallel k, and [B_n,c]=0;
the normal boundary pairing is the integrated D_A,n pairing. Homogeneous
normal data make it zero. The prior elliptic Q and compact resolvent give
selfadjoint nonnegative P0, compact resolvent and smooth eigenfunctions.
Iterating Q's boundary regularity gives smooth P0 solutions for smooth
sources: Qlambda in Dom Q solves Q(Qlambda)=source, then Qlambda and
lambda bootstrap together. At nonzero boundary Fourier covector the
finite-rank parallel-k projector has zero symbol, so scalar value is
Dirichlet and the scalar decaying principal solution is forced to zero.
Its finite harmonic sector is handled by the full Hilbert domain above,
not by this high-frequency symbol alone.

If P0 lambda=0, positivity gives Dlambda=0. A parallel section whose
boundary value is c in k equals its globally parallel extension c by
uniqueness of covariant transport. Conversely all such c lie in the
kernel. Thus ker P0=k_C and its REAL part is compact k. In particular
there is a positive spectral gap on k-perp, but no numerical value is
claimed. Compactness plus the elliptic estimate gives coercivity there.
The residual constants are kept as unbroken gauge symmetry, not removed
as nonexistent gauge/vector/gaugino states.

## 3. The source and boundary data satisfy the actual Fredholm condition

Seek a real lambda with

    P lambda=kappa(a), lambda|Sigma in k,
    Pi_k D_A,n lambda=q=-Pi_k u_n.

For any globally parallel real c in k, trace invariance and Stokes give

    integral_X <c,kappa(a)>=integral_Sigma <c,u_n>.

The [B,v] pairing vanishes because [c,B]=0, and the covariant derivative
becomes the derivative of <c,u>. Hence source integral PLUS prescribed
outward flux is zero. That is exactly the Green/Fredholm condition,
not an arbitrary extra zero-mode assumption. Pi_k is defined by this
integrated pairing; normalization/Gram factors cancel on both sides.

For full existence, construct a smooth real collar lift l with l|Sigma=0
and Pi_k D_A,n l=q; r times a cutoff times the globally parallel q, in
an outward defining coordinate, supplies it. It changes no tangential
trace. Green gives integral <c,P l>=-integral_Sigma <c,q>.
Therefore kappa(a)-P l is orthogonal to ker P0. Its unique k-perp
solution through P0's spectral inverse, plus l, solves the complete
inhomogeneous problem. Realness follows real P, data and kernel; smooth
boundary regularity follows the inherited Q^2 bootstrap. Uniqueness is
modulo global k. This is an analytic existence argument, not a finite
rank or numerical inverse masquerading as a silver PDE solve.

Freezing the normal gauge derivative would generally make this system
inconsistent. Conversely imposing pointwise normal scalar zero would
change the law. The interval-times-torus control uses the SAME constant
value on its two ends and their integrated outward flux; it is a toy
of the actual finite-rank boundary mechanism, not the core's topology.

## 4. The real quotient maps faithfully to harmonic H1

Let a satisfy the physical essential traces and Hessian zero equations.
Solve section3 and put a_h=a+Dlambda. Because H=mu=0,
Da_h=0,m(a_h)=0; the solved equation gives kappa(a_h)=0. Together these
imply D*a_h=0. Its tangential trace stays in A1. Its real normal k
projection vanishes by the gauge fixing, and its imaginary one by the
original primary law. Hence its full normal scalar trace lies in
(A0)^perp. It is EXACTLY a degree-one harmonic of the same Q realization.

Conversely every such degree-one harmonic decomposes uniquely into real
Hermitian u,v, satisfies the original primary trace, and has Da=m=0.
All extra auxiliary-eliminated scalar laws of static PROOF4 vanish on
these zero modes: their linear residuals H and mu vanish identically,
including their normal derivatives. This is a zero-mode statement, NOT
their redundancy on general fields or a full multiplet Sobolev theorem.

If two representatives in the slice differ by an allowed Dlambda, their
kappa difference and normal projection give the homogeneous P0 problem.
Thus lambda is in k and Dlambda=0; the representatives are identical.
The map is therefore bijective from the SMOOTH LINEAR physical Hessian
null space modulo ALLOWED real gauge tangent directions to harmonic H1.
The quotient inherits its complex structure from this harmonic space;
we did not quotient by complex primitives to obtain it. Gauge fixing is
also physically orthogonal: the REAL kinetic pairing with Dlambda is
-integral <kappa,lambda>+integral_Sigma <u_n,lambda>, zero in the slice.
Compactness and positive metric make nonzero harmonic norms finite and
positive. Their numerical overlaps are not computed here.

The prior unchanged Hilbert/cone comparison identifies this H1 with
H1(K). The canonical Weyl map already identifies its degree-one
left fields with the SAME H1, so scalar/fermion zero profiles pair at
conditional tree level on THIS construction. Everything is k-equivariant:
the operator, allowed traces and inverse on k-perp commute with compact
k. Its residual stabilizer acts on charged modes as a representation;
quotienting that linear representation by the finite/global stabilizer
would instead be a nonlinear moduli-space question. Charged duals and
neutral/gauge endpoints are not deleted. Charged H0=H3=0 remains the
previous proof, not a new rank census or a choice of three families.

## 5. Limits and sources

This identifies smooth LINEAR physical scalar zero directions with the
same conditional Weyl cohomology. It does not show every zero direction
integrates to a nonlinear solution; higher Kuranishi/Yukawa obstructions
remain. Full time-dependent gauge/constraint evolution, a closed complete
multiplet Hamiltonian, boundary states/anomalies/inflow, normalized physical
interactions and quantum/large gauge require separate work. All35 L
choices and larger-carrier positives survive; parent/boundary/vacuum/
parameters/gravity and full parameter-free SM/TOE are not derived.

Local authority: static PROOF4/5, complementary PROOF's Hilbert domain,
spectral-completion PROOF3 and fermion PROOF2/3. Older
NEUTRAL_VELOCITY_PROOF1/5 already establishes the zero-form gauge/moment
split and a compact harmonic tangent on a DIFFERENT complete-cusp domain.
Its gap/inverse is not used to solve this mixed compact boundary.
Primary boundary regularity personally re-read: Bär--Ballmann3.9-3.15,
[Guide](https://arxiv.org/html/1307.3021v1). These theorems supply inherited
regularity, not our OA parent, boundary or physical interpretation.
