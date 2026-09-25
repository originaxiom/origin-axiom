# F08 authored construction and operator dictionary

Frozen before execution. This is a standard homogeneous-bundle construction
applied to the adopted parent, with explicit analytic and algebraic checks.
No independent review, novel general theorem or completed physical model.

## 1. Global balanced bundle and full classical equations

Let R(g)=g tensor conjugate(g). This is a homomorphism of the REAL Lie
group SL2(C) into SL4(C), not a holomorphic map. R(-g)=R(g), and R(k) is
unitary for k in SU2. Thus geometric PSL2 holonomy directly defines the
bundle, independently of its SL2 sign lift. This removes that choice for
this coefficient; it does not derive physical fermion spin structures.

On H3 with g=z^-2(dx^2+dy^2+dz^2) take the fundamental precursor
C0=(E/z,iE/z,H/(2z)), E=E01, H=diag(1,-1). Define

    C_i=C0_i tensor I2+I2 tensor conjugate(C0_i).

The two tensor factors commute. Flatness and the full real moment equation
are inherited from C0 and its conjugate, and checked directly as matrices:

    dC+C wedge C=0,
    div_g(C+Cdag)+g^ij[C_i,C_jdag]=0.

The descent is explicit. For the hyperbolic section q, write
q(gamma p)=h(gamma)q(p)k_gamma(p)^-1. Applying R gives transition R(k_gamma),
unitary in the positive product metric. C, A=(C-Cdag)/2 and Psi=(C+Cdag)/2
therefore descend. The existing SU4 embedding integrates these transitions
into the same E8 parent. The full residual-square classical potential is
zero, including its compactly supported first variation in all parent
directions. No background spacetime curvature equation is supplied.

Use the orthonormal columns

    u0=(00+11)/sqrt(2), u1=(01+10)/sqrt(2),
    u2=i(01-10)/sqrt(2), u3=(00-11)/sqrt(2).

In this unitary basis C is real and preserves J=diag(-1,1,1,1). Its
Hermitian coefficients in the orthonormal coframe are S_i=N_i+N_i^T,
N_i=E_(0,i+1). A=0 direct-sum omega_LC and Psi_i=S_i/z in coordinates.
This identifies E with (R direct-sum TM) tensor C as a positive metric
bundle, not as a flat direct sum. The boosts mix its scalar and tangent
pieces. J is an additional indefinite bilinear invariant, NOT the kinetic
metric, which remains positive definite.

The norm is sum Tr(S_i^2)=6, hence ||Psi||^2=6 Vol(M)<infinity.
R39's trace-index 60 gives 360 Vol(M) in its unrescaled E8 adjoint trace.
These are normalization checks, not physical measured constants.

## 2. Exactly the compact D5 gauge algebra survives

Use the already-checked decomposition
248=(45,1)+(1,15)+(10,6)+(16,bar4)+(bar16,4).
The simultaneous kernels of S_i on 4 and on exterior-square(4) are zero.
The matrices commuting with all S_i on End(4) are only scalars, so the
traceless commutant is zero. These are exact common-kernel computations,
not a dimension-name match. Consequently the nonnegative internal gauge
quadratic form can vanish only in (45,1). Those D5 sections are parallel,
finite norm on finite volume, and in the natural form closure by complete
cutoffs. The surviving compact Lie algebra is the existing so(10), with
no extra ten generators and no new Wilson twist required. The global
gauge-group quotient is not asserted.

## 3. The physical one-form question is a Codazzi equation

With the actual coframe connection, nabla_(A,LC) Psi=0. Hence the same
mixed-term cancellation as F05 gives, initially on compact smooth forms,

    Delta_C=Delta_A+H_p, H_p=T*T+TT*, T=Psi wedge.

Both summands have nonnegative quadratic forms. Exact algebra gives
H0=H3=diag(3,1,1,1); H1,H2 have eigenvalues 0(5),2(3),3(4).
The degree-one result is precisely four times F06's corrected center
operator. That is an explicit map, not just the number five recurring.

Write a one-form u_i=t_i u0+sum_j b_ij uj. In the normalized frame

    <u,H1 u>=|tr b|^2+3 sum_i |t_i|^2
              +sum_(i<j)|b_ij-b_ji|^2.

Thus H1 u=0 means t=0 and b symmetric trace-free. A acts as the actual
Levi-Civita connection on the spatial coefficient, so d_A u=0 is exactly
nabla_i b_kj=nabla_k b_ij. The adjoint condition is div b=0, which follows
by contracting this Codazzi equation with symmetry and zero trace.

F02 gives the complete ordinary-L2 self-adjoint realization. The coefficients
Psi have bounded orthonormal norm, and compact cutoffs pass the positive
form identity to its domain. A global L2 harmonic one-form must therefore
lie in the displayed algebraic kernel and satisfy Codazzi. Conversely a
smooth L2 trace-free Codazzi tensor gives d_C u=d_C* u=0 distributionally,
so belongs to the maximal Dirac domain, equal to the unique closure.
Consequently

    ker_L2 Delta_C^1 = complex L2 trace-free Codazzi tensors on M.

For an additional unitary scalar line this is the analogous line-valued
covariant equation. The equality supplies an operator dictionary; it does
not compute its dimension for any particular cusp quotient or cover.
Neither the rank-five tensor fiber nor the indefinite form J is a derived
four-dimensional graviton or a generation count.

The closed-manifold Codazzi/cohomology literature is relevant navigation.
Bera's Proposition 4.3 concerns the linearized Sp(1) Seiberg--Witten
equations, not this E8 action. Its Lemma 4.6 is explicitly cocompact.
Our L2 identification above is the direct operator argument, not a transfer
of those closed-base cohomology or census claims to a cusp.

## 4. The cusp zero mode cannot be mistaken for normalizable matter

For the untwisted cusp in the frame e_i=z partial_i let b=b(z) be symmetric
trace-free. The nonzero spatial connection coefficients are
nabla_(e_a)e_b=delta_ab e3 and nabla_(e_a)e3=-e_a for a,b=1,2.
The Codazzi equations with indices (1,2,1),(1,2,2) force b23=b13=0.
The remaining independent equations are

    z b11'=b11-b33, z b22'=b22-b33, z b12'=b12.

Writing s=b11+b22, d=b11-b22 gives z s'=3s, z d'=d.
Their full solution is

    b11=(c z^3+d0 z)/2, b22=(c z^3-d0 z)/2,
    b33=-c z^3, b12=e z.

The positive squared norm, including cusp volume z^-3 dx dy dz, is
(3/2)|c|^2 z^3+(|d0|^2/2+2|e|^2)/z. Thus every nonzero zero-Fourier
Codazzi mode is non-L2. This excludes a specific potential false-positive,
not higher Fourier modes, global cusp forms, or all Codazzi tensors. A
nontrivial unitary cusp character can remove this Fourier channel altogether.

## 5. Removing the strict algebraic gap does not remove mirror pairing

The untwisted real C satisfies C_i^T J+J C_i=0 and Jdag J=I. Thus J is
a global unitary same-degree map from d+C to its dual d-C^T, including
adjoints and complete domains. The two charged spinor coefficient sectors
have equal spectra and equal zero multiplicities, whether zero or nonzero.

Now tensor by a unitary scalar character chi with chi^4=1 to remain in
the same rank-four SL4 parent. J as a LINEAR bilinear identification no
longer descends when chi^2 is nontrivial. Nevertheless C is real in the
Lorentz frame and its compact transitions are real orthogonal. Therefore

    A_anti(v)=J conjugate(v)

is a global antiunitary E_chi -> E_chi^* map: coefficient conjugation
changes chi into chi^-1, and J intertwines the remaining real factor.
It preserves form degree, compact supports, norm and graph closures, and
intertwines the differentials and adjoints. Spectral pairing survives.
This proof requires unitary characters; it is not asserted for arbitrary
nonunitary infinite-image factors or untransported boundary conditions.

For exact m004 generators the balanced trace of b is 4, whereas Sym3(h(b))
has nonreal trace -8+4 omega. This witnesses different global holonomy.
After a fourth-root twist the balanced trace becomes 4i, dual -4i: linear
self-duality fails but the displayed antiunitary map still acts. This is
precisely why complex trace data alone do not certify spectral chirality.

## 6. Consequence for the next physical step

This yields another complete finite-norm full-parent classical background
and a concrete geometric operator problem on the object's hyperbolic base.
F07's fixed-holonomy premise is genuinely changed. It supplies a useful
countercontrol to extending F05's Sym3 gap to every rank-four coefficient.
It does not yet supply any nonzero normalizable matter, much less a chiral
Standard Model. Within this class the explicit pairing already prevents
an unpaired free spinor spectrum.

The next valuable use is the Codazzi/end dictionary or a candidate that
changes this actual pairing, not a census advertised as a chirality cure.
Any proposed interaction/source mechanism must act on the same normalizable
fields and retain the full action, anomaly and end sectors. The existing
nonsplit/source positives are different data and are not excluded here.
