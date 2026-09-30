# Boundary current and radial profiles on the logarithmic cone

September 30, 2026. R67 authored analysis frozen before computation.
R66's local existence argument is an input, not independently reviewed
by the finite controls below. This is a conditional classical analysis.

## The action identity with its boundary retained

Use C=A+Psi, A dagger=-A and Psi dagger=Psi, with the positive trace
inner product and the actual R66 cone metric. Let D be the unitary
covariant derivative including Levi-Civita on form indices. Put
F_A=dA+A wedge A, K=Psi wedge Psi and mu=delta_A Psi. Then

    F_C=F_A+K+d_A Psi, I=-2mu,
    V=(2/g7 squared) integral (|F_C| squared+|mu| squared).

The anti-Hermitian F_A+K and Hermitian d_A Psi are orthogonal in the
real positive pairing. Commuting the two covariant derivatives gives
the pointwise integration-by-parts identity

    |F_C| squared+|mu| squared
     =|F_A| squared+|K| squared+|D Psi| squared
        +Ric^{ij} tr(Psi_i Psi_j)+div J,                   (1)
    J^i=tr(Psi^i D^j Psi_j-Psi_j D^j Psi^i).

For clarity, the intermediate identity is
|d_A Psi| squared+|delta_A Psi| squared-|D Psi| squared
=Ric(Psi,Psi)-2 Re<F_A,K>+div J. Its nonabelian curvature term
cancels the cross term in |F_A+K| squared. Equation (1) is the standard
covariant Bochner identity, not a new general theorem. R28 already
verified its commuting tube analogue. Here the actual nonabelian fields,
metric-derived Ricci and boundary current are independently contracted.
No integration on a singular endpoint precedes regulation.

On epsilon<=r<=R with unit coordinate torus area, define
B(r)=r squared J^r and E_exp=r squared times the four nondivergence
terms in (1). The supplied action obeys exactly

    (g7 squared/2)V_[epsilon,R]
        =integral_epsilon^R E_exp dr+B(R)-B(epsilon).     (2)

The current is compact-gauge-invariant: Psi and its covariant derivative
transform by conjugation and trace is invariant. This particular boundary
term is fixed by rewriting the chosen bulk functional. It is not a
derivation of a complete physical boundary theory or a license to omit
the accompanying fermionic terms.

## Actual logarithmic flux

Use R66's H,N,P,D and write u=exp(-2h), s=-log(r), v=h_s. Direct
evaluation of J gives, off shell,

    B=4r(h') squared+2h'(alpha u+beta squared u squared/alpha)
       +[alpha u+12k squared/alpha+beta squared u squared/(2alpha)]/r.

Equivalently,

    rB=4v squared-2v(alpha u+beta squared u squared/alpha)
          +alpha u+12k squared/alpha+beta squared u squared/(2alpha).

On the exact R66 branch, both residuals vanish and E_exp=-B'. Its
asymptotics are

    B=[12k squared/alpha+1/s+O(log(s)/s squared)]/r.       (3)

Thus the expanded bulk integral alone diverges, while the signed
boundary term in (2) cancels it exactly at every regulator. Keeping
only the rough or expanded bulk cost would falsely reject the known
zero-residual background. Conversely the zero action does not remove
the end-law problem; it identifies which boundary contribution a
change of functional representation must preserve.

The limiting reference C_infinity=kD dy already has
B_infinity=12k squared/(alpha r). Subtracting this reference alone
leaves B-B_infinity~1/(r s), still divergent. The elementary comparator
beta squared=alpha cubed, h=log(alpha(s+c))/2, tests these formulas
exactly. The q values used there remain controls, not physical selection.

## A sufficient affine bosonic variational space

On the punctured collar let X0 be the closure of smooth compactly
supported matrix one-forms in the norm

    ||a||_2+||d_C a||_2+||d_C dagger a||_2+||a||_4.

The closed differential graph and L4 intersection make this a Banach
space. Compactly supported nonzero fields show it is nonempty. For
the fixed flat, moment-flat background C, the nonlinear residuals are
linear differential terms plus pointwise quadratic brackets. Holder
and the uniform finite-dimensional bracket bound place the quadratic
terms in L2. The real orthogonal compact/Hermitian split of d_C dagger
a gives the gauge-fixing and moment linearizations, as in R46.
Consequently V(C+a) is a finite nonnegative C1 polynomial on X0 and
C is stationary there with V(C)=0. Compactly supported compact gauge
transformations preserve this affine variational class.

This statement does not put C-C_infinity in X0, nor impose that a
background belong to its own fluctuation space. It constructs a
sufficient fixed-background BOSONIC variational class, not the physical
choice of class. In particular closure of a quadratic form and its
second-order realization do not identify a self-adjoint first-order
fermion operator or establish all supersymmetry boundary conditions.
No such identification is claimed here.

## Actual radial tangent and the outer datum

At fixed k,beta, varying h by f(r) gives the one-form

    a_f=(f'H, -f exp(-h)N, -2beta f exp(-2h)P)=d_C(fH).

Flatness gives d_C a_f=0. Direct formal adjunction gives

    d_C dagger a_f=-[f''+2f'/r-A_h f/r squared]H,
    A_h=alpha u+2beta squared u squared/alpha>0.           (4)

The kinetic radial density is

    r squared |a_f| squared=2[r squared(f') squared+A_h f squared].

The autonomous radial equation allows translations h(s+c), so its
derivative f=h_s=v obeys the exact Jacobi equation
(r squared f')'=A_h f. From R66, v~1/(2s). The original ODE gives
v_s=v-(alpha u+beta squared u squared/alpha)/2
=-alpha squared u squared/2+O(u cubed)~ -1/(2s squared);
this derivative estimate does not assume that an asymptotic O term
can be differentiated freely. It follows that

    r squared |a_v| squared~1/(2s cubed),
    r squared |a_v|^4~1/(4r squared s^6).                 (5)

The formal local tangent is L2 and has d_C a_v=d_C dagger a_v=0,
but is not L4 and hence not in X0. These are exact equation identities
and improper-integral asymptotics, not a global particle count. The
Hermitian radial change f'H cannot be compact gauge: any compact
variation of Psi_r=h'H has zero projection on H by trace cyclicity,
while tr(H f'H)=2f' is nonzero near the tip. The positive complex
transformation producing the tangent is not an allowed compact gauge
removal by this argument.

Multiplication of (4) by f and integration gives

    integral_epsilon^R r squared |a_f| squared dr
       =2[r squared f f']_epsilon^R                       (6)

for a Jacobi solution. For f=v, the apex term tends to zero like
r/(4s cubed). Its nonzero norm is supplied by the OUTER datum. Setting
either f(R)=0 or f'(R)=0 forces f=0 within this radial class when the
apex term vanishes. This does not obstruct other global solutions;
it prevents turning the local translation into a free global mode.

## Chern-Simons boundary variation is a separate test

R60 derived the boundary one-form -tr(C wedge delta C) for the supplied
complex Chern-Simons functional, before any extra boundary functional.
On the present triangular parameter family, the boundary pullback is
zero for arbitrary variations of h,k,beta: C_x is strictly upper
triangular and C_y has only diagonal and strictly upper entries.
Their traced products with these variations vanish. This does NOT make
the boundary form zero on all L2 fluctuations.

A concrete countercontrol is a_y=exp(h)N dagger, a_r=a_x=0. It has
radial norm density 2exp(2h)/alpha~2s, so it is L2. Nevertheless
tr(C_x a_y)=2, and d_C a has xy component H, with squared norm density
2/r squared. It therefore fails graph admission. The countercontrol
distinguishes three predicates: a finite kinetic norm, vanishing
boundary pairing and finite differential norm.

The physical fermion reality/current and interacting supercharge
domains remain to be derived about C, with the global core included.
Neither the local bosonic class nor the formal local Jacobi solution
settles them. The action, link metric and physical realization are
still supplied inputs; no chiral spectrum or complete theory is claimed.
