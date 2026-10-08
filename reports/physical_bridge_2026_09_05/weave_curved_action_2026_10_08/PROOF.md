# One classical curved action for the complete fermion roster

Authored conditional construction, with exact algebraic checks. Metric,
compact E8, coupling, R twist and complete-domain law are supplied. This
does not derive them from genesis or certify quantum ultraviolet physics.

## Fields and their common parent

Let Sigma have metric g=Omega^2(dx^2+dy^2), orientation dx wedge dy,
complex coordinate z=x+iy, and spin line S with S^2=K_Sigma. Use the
compact algebra in a faithful unitary representation with positive trace
kappa on Hermitian generators. Complex adjoint fields use the induced
positive Hermitian norm; commutators are never set to zero by assumption.
All overall trace factors can be absorbed in the supplied g6^2>0.

The four-dimensional N=1 fields, depending on Sigma, are a vector V,
the affine connection chiral field A=A_x+i A_y, and two adjoint chiral
fields Q,R with values in S. Their independent left Weyl fields are the
scalar gaugino, the connection/form fermion, and two spin fermions.
Under z'=exp(i theta)z their coefficients have charges0,+2,-1,-1 in the
previous convention. Coefficient and frame weights are opposite: a spin
coefficient with charge-1 multiplies the holomorphic frame(dz)^(1/2).
This is the previous single-twist dictionary, not a replacement theory
with some companions removed. Right fields are Hermitian conjugates.

Arkani-Hamed--Gregoire--Wacker equation35 gives the complete non-Abelian
ten-dimensional N=1 parent in four-dimensional superspace. Keeping only
one complex derivative reduces its epsilon superpotential to the adjoint
hypermultiplet derivative and cubic connection coupling. Explicitly, with
Phi1 the connection and q=Phi2,r=Phi3, its derivative numerator is
Tr(r d q-q d r), and its cubic numerator is6 Tr(Phi1[q,r]). With the
published factors the result is -Tr(q(d r-[Phi1,r]/sqrt2)) plus
(1/2)d Tr(qr), up to the common trace/coupling factor. This calculation
keeps the total derivative. The connection change A_conn=-Phi1/sqrt2,
with A_conn=-iA in the Hermitian convention below, identifies the affine
connection in the superpotential. This is not, by itself, a check of all
superspace component rescalings: we fix the physical normalization below
by the positive kinetic metric, its actual gauge moment map and the full
flat Yang--Mills scalar energy. Equation35 is the parent-structure check,
not an independent certificate of every curved component convention.

For unconstrained supergauge transformations the vector superspace action
includes their equation24 WZW completion; it vanishes in Wess--Zumino
gauge but is not absent from the gauge-complete formulation. We use the
physical component gauge action, equivalently that completed superspace
action. The finite tests do not reproduce the whole WZW superspace
variation. Source equation36 is not used to infer equation35's coefficient.

## The curved functional specifies the interactions

In the holomorphic spin frame write the coefficients as q,r and set
Dbar_A = partial_x+i partial_y-i[A, .]. The Hermitian connection components
are A_x,A_y, so F=partial_x A_y-partial_y A_x-i[A_x,A_y] is Hermitian.
Define the physical orthonormal spin coefficients qhat=Omega^(-1/2)q,
rhat=Omega^(-1/2)r, and M=[qhat,qhat dagger]+[rhat,rhat dagger].

The field-space metric at fixed Omega is

    G(delta,delta)=integral dxdy kappa(
        (1/2) delta A dagger delta A
        + Omega(delta q dagger delta q+delta r dagger delta r)).

The four-dimensional gauge kinetic metric is Omega^2 kappa, integrated
over dxdy. The covariant four-dimensional kinetic terms use this SAME
metric and the affine gauge action on A; they include F_mu a, not a
collection of unrelated scalar derivatives. All physical kinetic signs
are positive in the usual Lorentzian convention. There are no arbitrary
kinetic weights tuned to get a desired index.

The moment map follows from this metric, rather than being chosen
independently. Use the Kahler form i G_{I Jbar} delta phi^I wedge
delta phibar^J, and gauge tangent k_epsilon A_a=D_a epsilon,
k_epsilon q=i[epsilon,q]. Direct contraction gives, in the convention
i_k omega=-delta<epsilon,mu>,

    mu=F+Omega([q,q dagger]+[r,r dagger]).

For the connection block, integration by parts leaves the surface
integral Tr(epsilon delta A_t)ds. For each spin field the contraction
is exactly -delta Tr(epsilon Omega[q,q dagger]) with no integration
by parts. Tests compare the full universal cyclic expressions and
detect changing the connection or matter coefficient. Together with
the gauge kinetic metric Omega^2, this fixes the auxiliary D energy
to mu^2/(2 Omega^2). The inverse chiral metric gives the two derivative
terms and the coefficient2 of the connection F-term commutator below.

The holomorphic functional is, in these real-coordinate conventions,

    W = (1/2) integral dxdy kappa(q Dbar_A r-r Dbar_A q).

Its invariant form is the integral of the corresponding(1,1) form from
S tensor S=K. This is globally defined under spin and gauge changes.
The antisymmetric expression differs from integral q Dbar_A r by the
explicit boundary primitive +(i/2)integral_boundary kappa(qr)dz:
Stokes gives integral dxdy Dbar f=-i integral_boundary f dz in the
stated orientation. A common constant phase multiplying the whole W
does not change the auxiliary-field energy; it cannot be assigned only
to a boundary term. No such relative phase is silently suppressed here.

G, the gauge kinetic metric, W and the affine gauge action specify the
gauged four-dimensional N=1 functional on this infinite-dimensional
field space. This is NOT a finite zero-mode truncation. In component
notation the fermion terms are the covariant kinetic terms for lambda
and all three chiral fermions, the Hessian coupling
-1/2 W_IJ psi^I psi^J+h.c., and the standard gaugino coupling to the
gauge Killing vector with metric G. The latter includes Dbar_A lambda
because the connection gauge action is affine. This gives the scalar/
form fermion block as well as the two spin fields; no Yukawa is replaced
by a freely chosen zero. The flat-space normalization below checks that
the scalar functional is the reduced Yang--Mills one, not an unrelated
N=1 theory with the same field names.

Eliminating auxiliaries gives the complete internal bosonic potential

    g6^2 V = integral dxdy kappa(
       Omega^(-1)(|Dbar_A q|^2+|Dbar_A r|^2)
       + 2|[q,r]|^2
       + (1/(2 Omega^2))|F+Omega([q,q dagger]+[r,r dagger])|^2).

Here |X|^2 means X dagger X inside kappa. Equivalently the last term is
(1/2)integral dvol |F/Omega^2+M|^2, and the quartic F term is
2 integral dvol |[qhat,rhat]|^2. Its three coupled vacuum equations are

    Dbar_A q=Dbar_A r=0,   [q,r]=0,
    F/Omega^2+[qhat,qhat dagger]+[rhat,rhat dagger]=0.

These are conditions on the full background; satisfying just the first
holomorphic equation or quoting a character count is not sufficient.

## The flat limit and curvature term are checked together

In an orthonormal flat frame let q=(X1+i X2)/sqrt2,
r=(X3+i X4)/sqrt2, with all Xi Hermitian. Universal cyclic trace algebra
gives

    (1/2)kappa(M^2)+2|[q,r]|^2
      = (1/2)sum_{I<J}|[XI,XJ]|^2.

Both sides include the same trace. This identity needs the mixed
commutators and Jacobi/cyclic cancellation; the test compares every
cyclic word rather than only plugging commuting matrices into it.
The positive potential reduces to the usual scalar commutator energy
with no missing pair. Dropping[Q,R] fails, as does dropping a moment
source. An independent exact matrix implementation checks noncommuting
examples as well as the commuting control.

For D_a=partial_a-i[A_a,.], integration of the mixed derivative in
|D_1 q+iD_2 q|^2 contributes -kappa(F[q,q dagger]) plus the boundary
current. The cross term of(1/2)(F+M)^2 cancels it. The remaining flat
bosonic energy is

    integral kappa((1/2)F^2 + (1/2)sum_{a,I}|D_a XI|^2
                    + (1/2)sum_{I<J}|[XI,XJ]|^2)

plus the explicit surface term. This is the dimensional reduction of
the full gauge action, not merely agreement on its zero set.

For the curved spin frame put sigma=log Omega. The unitary spin
connection in coordinate directions is s_x=(partial_y sigma)/2,
s_y=-(partial_x sigma)/2, with nabla=partial+i s-i ad A. Its curvature
is ds=-(Delta sigma)/2=(Omega^2/4)R_scalar. Thus the same derivative
identity gives rough covariant gradient energy, the term
(R_scalar/4)(|qhat|^2+|rhat|^2), the cancelling gauge-curvature cross
term, and a surface current. On the curvature-1 cusp R_scalar=-2,
the curvature term is negative, but the COMPLETE squared operator is
nonnegative. Dropping either derivative or boundary terms would change
the theory. This is exactly the risk already documented in R28.

A simple discriminating patch control is q=x+iy with zero connection:
Dbar q=0 while its rough gradient energy is2 per unit area. Its boundary
current supplies-2. Neither an isolated rough-energy term nor an isolated
negative curvature term is a correct stability test.

## Variations, gauge covariance and the end

Ignoring no surface term, variation of W gives the bulk terms
delta q Dbar r-delta r Dbar q-i delta A[r,q] under kappa, and the
antisymmetric surface pairing(-i/2)kappa(q delta r-r delta q)dz,
with dxdy and dz related as above. Hence the connection F term is
proportional to[r,q], not zero. The Hessian contains the spin derivative
pair and every connection-spin Yukawa generated by q[A,r]. Its cubic
is nonzero already in the retained complexified family sl3 subalgebra:
A=E12,q=E31,r=E23 gives Tr(q[A,r])=1. This is a local vertex; it does
not evaluate an uncomputed global wavefunction overlap.

For a unitary gauge change U, Dbar' q'=U(Dbar q)U^(-1) requires the
connection's derivative compensator. A position-dependent control checks
this; a constant U alone cannot test that law. The invariant trace then
makes W and all potential residual norms gauge invariant. The complete
four-dimensional covariant action has the same transformation rule.

For the original complete cusp take the graph closure of compactly
supported smooth sections for the unitary complete-manifold Dirac/form
operators. In nonlinear configurations also require the commutator
residuals to be L2 and variations to be differentiable in these norms.
For the spin bilinear, choose exhausting cutoffs chi_T with derivative
tending uniformly to zero. Its boundary error is bounded by a constant
times ||d chi_T||_infinity ||q||_L2 ||delta r||_L2 and the analogous
term with q,r exchanged. It tends to zero. This is a graph-domain
statement, not arbitrary pointwise decay imposed at one finite circle.
Products entering the nonlinear energy must remain integrable; this
argument is not a theorem on all possible weak nonlinear solutions.

Nonzero boundary/source data, an inserted surface multiplet or a finite
cutoff would change this variational problem and must be separately
specified. The antisymmetric form makes the surface pairing visible;
integration by parts does not generate a physical end mechanism for free.

## Stationarity, full Hessian and the unresolved physical isolation

At the existing flat quaternion connection A0 with q=r=0, F=0 and all
three residuals vanish. For every admissible differentiable finite-energy
path, the first variation of their squared norms is zero without a
discarded surface term. The Hessian is their positive linearized norm
sum. Its terms are the connection curvature norm and the two spin
Dirac norms; the commutator potentials start at higher order. Gauge
directions are zero directions, not negative kinetic states. The flat
connection moduli are not lifted by claiming positivity.

The affine gaugino coupling gives the same scalar/form kinetic pair as
before; the W Hessian gives the same two spin slots. Therefore the
previous finite zero roster and its mass-protection statement refer to
this one supplied classical action at this origin. The action contains
nonzero gauge and spin Yukawa interactions away from the origin. Quantum
masses, global anomaly acceptance and nonlinear stability beyond this
nonnegative classical energy statement are not computed.

The ordinary-spin zero-angular cusp channel still has free radial
operator. Its bosonic supersymmetric partner has the squared operator,
not a curvature-induced gap. An escaping Weyl sequence retains residual
10/L^2. Thus the full classical action has not removed the previous
gapless continuum. An explicitly inserted constant mass changes this
threshold, but is a comparator only. Before claiming an isolated physical
chiral sector we need a stationary nonzero coupled background or an actual
end mechanism that changes the asymptotic operator, with complete charged
spectrum, gauge symmetry and anomaly accounting on that SAME background.

Sources: https://arxiv.org/abs/hep-th/0101233v2, equations23--35 and section5;
https://arxiv.org/abs/hep-th/0601098v2, section3 and AppendixA. Their uses
are the flat non-Abelian parent and twist convention. The curved
field-space/action/domain connection above remains an authored conditional
construction awaiting independent specialist review, not a source claim
that OA, an observer or a complete physical Standard Model was derived.
