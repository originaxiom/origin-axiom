# A protected same-action quartic for the actual charged spin modes

2026-11-16. P-C3c author hand proof, independent review pending. No
scientific code, CAS, collection, integration or tests ran. This is a
local nonlinear result on specified actual mode directions, conditional
on the preceding source/domain and P-C3b mode/normalization proofs.

## 1. Fix actual modes, without a new scalar potential

Use the coherent odd or aligned background with its unbroken Q_em.
The previous physical calculation constructs three chiral zero modes
and one vector zero mode, with their source kinetic normalizations,

    e_A, neutral connection/form mode bar(omega) Q_em,
    e_+, e_-, opposite-charge pure-spin modes of charge +/-1,
    v_Q, internally constant unbroken gauge generator.

All four profiles are normalizable on the finite-area complete surface.
The three chiral modes are orthonormal after their derived positive
rescalings. They have both H e=0 and k^dagger e=0, where H is the
actual kinetic-normalized superpotential Hessian and k the actual
gauge Killing map at the background. They are not arbitrary compact
cohomology representatives. Other physical modes remain in the parent.

The same parent's cubic, evaluated on this space, was derived as

    W_light=y A t_+ t_-,                                (1)

with the normalized gauge current coupling e=e_Q>0 and

    |y|^2/e^2=2 A_omega A_g/I_omega^2>2                 (2)

for the stated cusp metric. The flat equality control has ratio two.
Neither y nor e is independently assigned. Their absolute values and
the retained shape dependence are conditional on the supplied parent.

## 2. Identify bounded dual modes of the full linearized residual

Write the complete potential in its supersymmetric component form

    V=||F(X)||^2+one-half ||D(X)||_v^2.

F is the actual superpotential gradient with the inverse chiral metric,
and D is the actual moment with the inverse vector metric. This is
the same residual norm as the companion equation (1), in auxiliary
field coordinates. The factor one-half on D is retained.

For each chiral mode e in {e_A,e_+,e_-}, its trace-dual normalized
F-component annihilates the entire linearized F response. Indeed
the complex-bilinear Hessian is symmetric, so

    e^T H beta=(H e)^T beta=0                           (3)

for every admitted correction beta. The pairing is its physical
trace-dual pairing, not a conjugate identification of charged left
fields. The normalized duals are bounded functionals on the F-residual
Hilbert space. Complete-domain transpose and integration by parts
are those of the actual physical mass proof.

The normalized D dual v_Q also annihilates every linearized moment
response. The Hamiltonian identity gives Dmu_Q(beta) as the symplectic
pairing of k_Q(X0) with beta, and k_Q(X0)=0 for the unbroken generator.
Equivalently the direct curvature term integrates to its vanishing
complete-domain surface primitive, while Q commutes with the background
spin pair. This includes any second-order correction in the connection,
spin fields or any other gauge coefficient.

These are four explicit bounded members of ker L^dagger in the full
real residual space, with the D residual normalized by 1/sqrt(2).
Their existence requires no inverse of the neutral continuum.

## 3. Allow every second-order field correction

Consider the actual admitted two-jet family

    X(epsilon)=X0+epsilon(A e_A+t_+ e_++t_- e_-)
                                  +epsilon^2 beta+o(epsilon^2).        (4)

Beta can use all parent fields in the nonlinear domain, with controlled
graph/product expansion. No finite-mode truncation of beta is imposed.
Other first-order mode coefficients are set to zero for this specified
tangent. They are retained as separate possible tangents.

Symmetry of the actual third derivative and (1) give the three projected
quadratic F residuals

    F_A^(2)=y t_+ t_-,
    F_+^(2)=y A t_-, F_-^(2)=y A t_+.                    (5)

Equation (3) makes these projections independent of beta. The unbroken
moment projection is fixed by the very same normalized current,

    D_Q^(2)=e(|t_+|^2-|t_-|^2).                         (6)

For a direct normalization check, v_Q=Q/sqrt(Z_Q) in the vector metric
and Z_Q=kappa(Q,Q) A_g/G. Projection of the raw moment gives
(G sqrt(Z_Q))^-1 integral kappa(Q,mu) dxdy. The spin terms give
the raw charges times their full kinetic norms. Canonical rescaling
therefore yields +/-1/sqrt(Z_Q)=+/-e as in (6). The neutral connection
mode is Abelian and supplies no quadratic Q charge. This checks the
D coefficient without introducing a separately chosen quartic.

Bessel's inequality on these orthogonal physical auxiliary directions
then gives the complete-potential coefficient bound

    lim_(epsilon->0) V(X(epsilon))/epsilon^4
      >= |y|^2 {|t_+t_-|^2+|A|^2(|t_+|^2+|t_-|^2)}
                                +(e^2/2)(|t_+|^2-|t_-|^2)^2.        (7)

Additional auxiliary components can increase the coefficient. Their
relaxation can remove their own range parts. It cannot cancel the four
fixed projections (5)-(6). The result concerns a controlled two-jet
through this vacuum and tangent; it is not a minimized exact potential
at arbitrary amplitude.

## 4. A scale-independent positive relation survives heavy relaxation

Put x=|t_+|^2, z=|t_-|^2. The part of (7) independent of A is

    |y|^2 xz+(e^2/2)(x-z)^2
      =(|y|^2/4)(x+z)^2+(e^2/2-|y|^2/4)(x-z)^2.

Equation (2) makes the second coefficient nonpositive. Since
0<=(x-z)^2<=(x+z)^2, it follows that

    lim V/epsilon^4 >= (e^2/2)(|t_+|^2+|t_-|^2)^2
                          +|y|^2|A|^2(|t_+|^2+|t_-|^2).            (8)

The same non-strict bound holds in the flat equality control. For
nonzero charged tangent the lower bound is strictly positive, even
after every admitted second-order correction in (4). Switching off
one charge leaves its D cost. Equal-magnitude charges cancel D but
leave the nonzero F_A source. With both charged coefficients zero,
this bound vanishes and the existing neutral Wilson branch is retained.

Thus these charged zero modes are genuine linear massless fields
with an unavoidable leading interaction. Their specified charged
tangents are not flat vacuum moduli with a smooth two-jet completion.
A different first-order light combination can have extra terms in
(5)-(6); it must be evaluated in the larger actual tensor. Equation
(8) excludes no such combination and no different generated sector.

## 5. Consequences and remaining work

R83 correctly warned that a frozen residual norm can disappear under
field relaxation. Here actual normalizable dual modes prove that a
specific positive part cannot disappear. No closed-range or whole-
parent inverse has been borrowed to establish that statement. A
neutral continuum does not erase these bounded source projections.

The leading scalar interaction now follows from the actual cubic,
kinetic norms, unbroken current and source moment. It has no additional
free self-quartic coefficient. This is a conditional reduction within
the supplied model. No foundational input, selected vacuum, full
stationary interface, physical three-family composition, chiral SM
spectrum or gravity is counted derived here.

Independent review must check the zero-mode and trace-dual premises,
global normalizability, the source equality of F residual conventions,
the real moment normalization, all four adjoint-kernel statements,
the allowed nonlinear two-jet topology and the scope of Bessel's bound.
In particular a finite algebraic test of (8) would not verify those
analytic and physical hypotheses. Scientific execution still requires
its own complete prospective design and exact admission.
