# Compact gauge orbit is not its straight tangent

October 1, 2026. R73 conditional authored proof, frozen before execution.
Reuse the adopted positive trace metric, cone, residual-square action and
actual local R66 solution, not a selected physical metric or end law.

## 1. Actual compact orbit

N=E02+E23, P=N^2, H=diag(1,0,0,-1), Z=diag(1,-3,1,1).
[H,N]=N, [H,P]=2P; Z commutes with all these and their adjoints.
Let t=exp(-h), k=log(q), beta=6/(q-q^-1), and

    C_r=h' H, C_x=tN, C_y=kZ+beta t^2 P.
    I(C)=[2(r^2 h''+2rh')+alpha t^2+beta^2 t^4/alpha]H/r^2.

The scalar bracket vanishes on the actual exact branch, with
t^2~1/(alpha s), s=-log r. For real theta(r), set g=exp(i theta H).
The convention C^g=g C g^-1-dg g^-1 yields

    C_r^g=(h'-i theta')H,
    C_x^g=t exp(i theta)N,
    C_y^g=kZ+beta t^2 exp(2i theta)P.                (1)

Direct differentiation gives F(C^g)=0 and I(C^g)=I(C), even off shell
in h. The anti-Hermitian radial phase cancels out of C_r+C_r dagger.
It is essential for flatness when theta changes. Take theta constant
theta0 near zero and smoothly zero outside the collar. This is a
single-valued compact gauge map extending by identity into the core.
Calling it a redundancy additionally requires an end law admitting
that apex gauge value. A fixed apex frame changes that hypothesis.

More generally, for any unitary g and complex connection D, put
Q_i=(partial_i g)g^-1, Q_i dagger=-Q_i. In I, differentiation of
g(D+D dagger)g^-1 contributes [Q_i,g(D+D dagger)g^-1]; the contracted
commutator contributes its negative. The Q_i,Q_j commutator vanishes
under symmetric metric contraction. Thus F(D^g)=gF(D)g^-1 and
I(D^g)=gI(D)g^-1. Trace norms and volume are unchanged pointwise.
This is classical residual covariance, not a quantum anomaly proof.

## 2. Finite tangent norm, infinite affine displacement

Near zero theta is constant. The derivative at theta=0 is

    eta=(0,itN,2i beta t^2 P).
    r^2 |eta|^2=2alpha t^2+4beta^2 t^4/alpha ~2/s.   (2)

It is L2 because dr=exp(-s)ds. Its L4 density is the square of (2)
divided by r^2 and diverges. Nevertheless the exact compact path (1)
has zero residual action at every phase on the exact branch.
For real fixed epsilon!=0 the STRAIGHT path C+epsilon eta is flat but

    I(C+epsilon eta)-I(C)
       =epsilon^2[alpha t^2+4beta^2 t^4/alpha]H/r^2.
    r^2 |I(C+epsilon eta)|^2/2
       =epsilon^4[alpha t^2+4beta^2 t^4/alpha]^2/r^2. (3)

On the exact branch (3) is asymptotic to epsilon^4/(r^2 s^2), whose
integral diverges. The tangent has zero linearized residuals, but its
straight finite displacement omits the all-order unit-modulus phases.
It is neither a finite-action exact gauge orbit nor evidence excluding
that orbit. This specializes R64's already banked path distinction to
the actual canonical log background.

For theta0 not 0 modulo 2pi, the difference C^g-C near zero has kinetic
density 2alpha t^2|exp(i theta0)-1|^2 plus a subleading P term. Its
L4 norm diverges. Thus R67's sufficient affine X0 about C is not itself
a gauge-invariant physical exclusion rule for this admitted gauge group.

## 3. A sufficient gauge-saturated interacting class

R70 supplies D=C+a_v+b, where a_v=Z(v_x dx+v_y dy), v in H1((0,R),C^2),
b in X0 with b/r in L2. Its finite nonlinear residuals follow from
bounded v, the weighted cross-bracket estimate and L4 self-products
of b. Take its image D^g under the phase maps above. By section 1,
its residual action is exactly that of D, including nonzero interactions.
This defines a sufficient nonlinear gauge-saturated class, not a linear
Banach chart, classification of all finite-action fields or selected law.
Because g commutes with Z, its neutral profile and weighted peripheral
periods remain those of v. The actual background's pair is conjugated
simultaneously, not fixed entry by entry. The phase orbit's holomorphic
boundary variation vanishes by the strictly upper-triangular trace
pairings; no global counterterm or quantum gauge law is inferred.
In particular this phase does NOT remove R70's neutral-period mismatch.

## 4. Transport fermion and domain together

On coefficient forms let U_g(a)=gag^-1. It is unitary for the positive
trace L2 metric. Covariant differentiation transforms as
d_(C^g)=U_g d_C U_g^-1; formal adjoints do likewise. Therefore

    Q_(C^g)=U_g Q_C U_g^-1.                         (4)

The maximal distributional domain maps isometrically in graph norm;
smooth compactly supported forms map to themselves, so their minimal
graph closures also map isometrically. This argument does not require
a bounded complex similarity or split d/delta cancellation. A chosen
closed end domain must be transported too; keeping arbitrary frozen
component traces is not gauge covariance. R72's witnessed quotient and
its conserved current are transported, not converted into particles.

In R68/R71's normalized form convention, Q=Gamma(partial_r+A/r),
A=[[M+K,-L],[-L,-M-K dagger]]. With U acting on each coefficient,

    A^g=U A U^-1-r U' U^-1
       =U A U^-1-i r theta' (I8 tensor ad H).       (5)

The top K becomes K-i r theta'ad H; the bottom uses its ADJOINT.
Where theta'!=0, A^g need not be Hermitian or anticommute with Gamma.
Nevertheless Gamma A^g is Hermitian and
(A^g)^H J+J A^g=0 for J=-mathG Gamma, with the ordinary coordinate
conjugate transpose in this formula. These are the correct
formal symmetry/current conditions. Rejecting a radial compact frame
for failure of A^g Hermiticity would be another frame-dependent false kill.
Near the apex theta is constant, so the original tail estimates transport
unitarily; the witnessed signature and rank are unchanged.

## 5. Spacetime gauge compensator, not a matter modulus

Allow theta=theta(x^mu,r). The transform of A_mu=0 is
A_mu^g=-i(partial_mu theta)H. In the same covariant convention,

    F_mu,i=partial_mu C_i^g-partial_i A_mu^g+[A_mu^g,C_i^g]=0. (6)

The radial mixed derivative cancels as well as both link commutators.
Leaving A_mu=0 instead produces nonzero mixed curvatures and an
apparent positive kinetic term. That calculation fails to transform the
whole gauge configuration. If the gauge group admits (1), theta is an
orbit coordinate, not a new physical massless scalar or chosen parameter.
If the end gauges are restricted, its status requires the actual end
charges/action, not the local norm alone.

## Limits

No quotient of all 36 R72 witness classes has been classified here.
No full parent, supercharge derivative closure, end degrees of freedom,
core match, quantum gauge prescription, chiral SM or values are derived.
The necessary next task is the interacting end law after its compact
gauge quotient, with the same physical source/anomaly/core accounting.
