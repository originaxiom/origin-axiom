# Exact ground space and the law a selector must satisfy

2026-11-18. P-C8 author hand derivation, not independently checked.
No scientific code, CAS, collection or numerical integration ran.
The source matrices are literally those of main `c34a926a2`,
`verification/checks/level6_higgs.py:23–24` in B1957. The flux-six
construction and its kinetic prescription are supplied model premises.
Nothing here identifies this coefficient space with an SM multiplet.

## 1. Exact recovery of the six eigenphases

Write `F_N[j,k]=exp(-2 pi i j k/N)/sqrt(N)` and

    T = diag(exp(i pi k²/6)), S=exp(-i pi/4) F_6,
    U = T S^-1 T^-1 S.

Use the real permutation of bases

    k=3a+4b mod 6, a mod 2, b mod 3.

With omega=exp(2 pi i/3), direct substitution gives

    T = diag(1,-i) tensor diag(1,omega,omega),
    F_6 = F_2 tensor conjugate(F_3).

Indeed `k²/12 = 3a²/4 + b²/3 mod 1`, and
`kk'/6 = aa'/2 + 2bb'/3 mod 1`. Consequently

    U = A_2 tensor A_3,
    A_2 = diag(1,-i) F_2 diag(1,i) F_2,
    A_3 = T_3 F_3 T_3^-1 F_3^-1.

The first factor is exactly

    A_2=(1/2)[[1+i,1-i],[-1-i,1-i]]
       =(I+i(-sigma_x+sigma_y+sigma_z))/2.

Its trace and determinant are one, so its eigenvalues are
`exp(+-i pi/3)`. For the second factor put `c=(1-omega²)/3`. Then

    A_3=diag(omega²,1,1)+c (1,omega,omega)^t (1,1,1).

The odd vector `(0,1,-1)` has eigenvalue one. The complementary
even plane has trace zero and determinant one: the full trace is
`omega²+2+c(1+2omega)=1` and det A_3=1. Its eigenvalues are i and -i.

Thus, without a floating-point eigensolver,

    spec U = {exp(+-i pi/6), exp(+-i pi/3), exp(+-5i pi/6)},
    det(lambda I-U)=(lambda²-lambda+1)(lambda^4-lambda²+1).

U has exact order twelve. The parity `P:k -> -k` is
`I_2 tensor P_3`. Its odd two-space carries phases +-pi/3;
the other four eigenvectors, including both ground vectors, are even.

## 2. Exact tick square and the lift group's leakage

Since `S²=-iP`, P commutes with T, and S is symmetric unitary,

    conjugate(T)=T^-1, conjugate(S)=S^-1,
    T S T^-1 S^-1 = T S^-1 T^-1 S = U.

For the antiunitary `Sigma=T S K`, K coefficient conjugation,

    Sigma²=U.                                          (1)

Composition implies Sigma U=U Sigma as maps. Antilinearity therefore
takes an eigenvalue to its complex conjugate. The two normalized
ground vectors v_+,v_- of phases +-theta, theta=pi/6, are exchanged.
This preserves the genuine matrix content of SM-C20 exactly.

The same factorization explains SM-C19's repaired lift test. If
`A_2 u_+=exp(i pi/3)u_+`, `A_2 u_-=exp(-i pi/3)u_-` and
`A_3 b_+=i b_+`, `A_3 b_-=-i b_-`, then

    v_+=u_- tensor b_+, v_-=u_+ tensor b_-.

In this basis `Z³=sigma_z tensor I_3` and `X³=sigma_x tensor I_3`.
Their product is the third Pauli direction up to a scalar phase.
Orthogonality of b_+,b_- gives

    <v_-,g v_+>=0,
    |<v_+,g v_+>|²=1/3,
    ||(I-P_ground)g v_+||²=2/3                         (2)

for each of Z³, X³ and Z³X³. The middle equality uses the Bloch
axis `(-1,1,1)/sqrt(3)` of A_2. Thus these operators do not act as
an exchange or a closed representation on the ground pair. An
identification of the half-period lift data with that pair cannot
be inferred from both being described by a binary label.

## 3. The quadratic problem admits coherent ground directions

In the lift-averaged mass prescription, the bubble is b I_6 (proved
directly from its closed form in the companion note). On

    E=span_C(v_+,v_-),

the kinetic term and mass matrix are scalar:

    K|E=theta²/L² I_2,
    M_H²|E=(theta²/L²-c b) I_2.                         (3)

Every unit `h=a v_+ + b_0 v_-`, with `|a|²+|b_0|²=1`, is a ground
direction of this quadratic problem. Already modulo a common phase,
these directions are CP1. A direction is a monodromy eigenline only
when a=0 or b_0=0. Restricting to those two lines is a further condition,
not a consequence of their equal mass-squared.

The underlying twisted-circle kinetic problem gives an explicit
admissibility control. On a circle of length L let

    h(s)=a exp(i theta s/L)v_+ + b_0 exp(-i theta s/L)v_-.

Then `h(s+L)=U h(s)` and
`-h''=(theta/L)² h`. All combinations satisfy the same boundary
condition and have the same Rayleigh quotient. The equal-weight
combination is a concrete ground section that is neither U eigenline.
This is the linear circle model used to prescribe K, not a new
complete-cusp or nonlinear Higgs solution.

An actual gauge quotient, superselection rule or interaction could
reduce this space. None is assumed absent. Their field-level action
must be given before calling the physical freedom one bit. A different
source rule could explicitly restrict to monodromy eigenmodes; that
restriction would need its own derivation or input entry.

## 4. What the antiunitary forces, and what it leaves

Phases of v_+,v_- can be chosen so that on E

    Sigma(z_+,z_-)=(exp(i theta) conjugate(z_-),
                                            conjugate(z_+)). (4)

Let `J=diag(1,-1)`. The orientation-odd ground observable is

    J=(U-U^dagger)/(2i sin(theta)) on E,
    Sigma J Sigma^-1=-J.                              (5)

The latter includes conjugation of i. For a Hermitian quadratic
response H on E, invariance under Sigma implies commutation with U
by (1), hence H is diagonal in v_+,v_-. Sigma exchanges the diagonal
entries, so **H=alpha I_2**. A fully tick-symmetric quadratic law
protects this doublet's degeneracy; it does not prefer one line.

There is also no Sigma-fixed coefficient ray in E. If
`Sigma h=lambda h`, antiunitarity gives `U h=|lambda|² h=h` for
a unit h, whereas neither eigenvalue of U on E is one. This is a
statement about a fixed coefficient ray. It excludes no covariantly
varying section, history or symmetry-breaking physical state; those
carry the argument and transition data too.

If a reference orientation epsilon=+-1 is **independent data** and
is exchanged by the tick, covariance instead requires

    H_-epsilon = Sigma H_epsilon Sigma^-1.

Applying it twice again makes H_epsilon commute with U. Every such
pair is exactly

    H_epsilon=alpha I_2+kappa epsilon J,
                                 alpha,kappa real.    (6)

This is a useful restriction on the selection law: the orientation
splitting operator is fixed up to a single coefficient. Its actual
coefficient and sign still need an action, end equation or global
constraint. The averaged prescription (3) has kappa=0. Symmetry alone
allows either sign and zero.

Even on an eigenline-only ansatz there are two equivariant assignments,
`epsilon -> [v_epsilon]` and `epsilon -> [v_-epsilon]`. The product
of the two signs is unchanged by a simultaneous exchange. It ceases
to be an independent physical distinction only if a specified gauge
equivalence removes it, an interaction fixes it, or the orientation
reference is itself derived from the Higgs state. The last possibility
is allowed; it requires its own registering/observer map. This argument
does not assume that the source actually contains an independent
orientation label and does not prove a universal extra-input theorem.

## 5. Interactions can reduce the state space: the exact quartic target

Assume the common Higgs phase is a gauge symmetry, the reduced response
is an analytic local potential, and the whole tick acts on that
potential, with no separate odd reference. Put

    N=|z_+|²+|z_-|², Delta=|z_+|²-|z_-|²,
    w=z_+ conjugate(z_-).

Under U, w -> exp(2i theta)w, a primitive sixth root; under Sigma,
`w -> exp(i theta)w`, Delta -> -Delta. At polynomial degree four,
common-phase invariance and U eliminate every phase-dependent
monomial; Sigma equates the two pure coefficients. Therefore

    V4=A N²+B Delta², A,B real.                       (7)

At a separately specified nonzero N the directional minima are

| Coefficient | Minimizing directions |
|---|---|
| B<0 | The two pure eigenlines |
| B>0 | Equal magnitudes; a relative phase remains at this order |
| B=0 | All CP1 directions |

For example A=2,B=+1 and A=2,B=-1 both give bounded positive quartics
with the same symmetries and different directional minima. These are
algebraic adverse controls, not potentials added to the programme.
Both have their unrestricted minimum at N=0 if no other term is
present. A nonzero physical vacuum and its amplitude remain separate
duties. Nonanalytic radiative functionals are not covered by a
polynomial quartic classification.

For the **complete relaxed** quartic, an exact target is

    B=V4_eff(v_+)-V4_eff((v_+ + v_-)/sqrt(2)).          (8)

It must include all source and massive-field response. An analogous
direct target for (6) is half the difference of the two diagonal
quadratic matrix elements at fixed reference. Computing these from
the existing action could earn a selector. Typing either coefficient
or transferring it from different fields would not.

## 6. Conditional orbit spaces, with the reference retained

This section is a coefficient-space calculation, not a decision that
time evolution is gauge. If one quotients CP1 by the projective tick,
use the Bloch sphere with azimuth arg(w) and height Delta/N. Sigma
rotates the azimuth by pi/6 and flips the height. Its even subgroup U
rotates by pi/3. The underlying space CP1/<U> is a sphere: multiply
azimuth by six, retaining the poles. On that sphere Sigma is the
antipodal map. Thus the underlying space CP1/<Sigma> is RP2.
There are finite stabilizers at the poles before taking that last
quotient; no smooth RP2 metric or trivial descended line is asserted.

If an independent sign epsilon is retained and flipped at the same
time, fixing epsilon=+1 leaves only the even subgroup. The underlying
diagonal quotient of `{+-1} x CP1` is then a sphere, with its two
eigenline poles distinct. This recovers the relative-alignment issue
without discarding the measuring reference. Enlarging the equivalence
group can change these quotients only through an actual admitted action
on all the marked data.

The conditional geometric results are positives of the specified
six-mode model. They derive neither a physical weak doublet nor three
chiral SM generations, the observer or gravity. The programme's
foundational input count is unchanged.
