# Sheaf index, local Green data and complete-cusp kinetic test

Authored conditional mathematical argument, sealed before the packet's
execution. It is not a full physical compactification or nonauthor proof
acceptance. All bundle-to-physics identifications remain priced.

## 1. The index formula is a valid sheaf formula

Let E be the compact elliptic curve, p its marked point, S a square root
of K_E (degree zero), and W the rank-six unitary local system on E-p
specified by the three quaternion doublets. Around p the holonomy is -I.
For the canonical parabolic extension E_0 choose all weights alpha=1/2.
The local holomorphic frame has norm proportional to r^(1/2): if e is
a multivalued flat frame of monodromy -1, z^(1/2)e is single-valued.

For a unitary local system, deg(E_0)+sum(alpha)=0. This follows from
the determinant/residue calculation in Mehta--Seshadri Proposition 1.9
and Corollary 1.10, not from the computed move commutant. Thus deg E_0=-3.

Choose a d-dimensional subspace Lambda in the puncture fibre and allow
one additional pole in those directions. Locally a frame direction in
Lambda changes from z^(1/2)e to z^(-1/2)e. This upper modification E_Lambda
fits an exact sequence

    0 -> E_0 -> E_Lambda -> C_p^d -> 0.

The skyscraper quotient has length d. Degree increases by d. Riemann--
Roch on a genus-one curve, after tensoring by S, gives

    chi(E_Lambda tensor S) = deg(E_Lambda) = d-3.

This verifies the supplied formula at SHEAF-EULER-characteristic level.
It counts h0-h1, not automatically h0, and certainly not an already
identified number of four-dimensional SM fermions. The adjoint sheaf
under Serre duality is the complementary modification of the dual
coefficient: the pole lengths sum to six and the two indices are opposite.
E_0* is not the weight-normalized canonical extension of W*, so these
must not be identified without the puncture shift.

We do NOT claim that writing this exact sequence proves the global graph
domain/Fredholm equivalence for every metric or physical kinetic operator.
For the finite-distance regular-singular Dirac problem that equivalence
requires a closed-domain elliptic parametrix (and outside analytic review).
For the complete-cusp problem below it is not the same Hilbert-space index.

Source: https://repository.ias.ac.in/20407/1/305.pdf (1980), pp. 213-214.

## 2. Smooth deleted point: critical coefficients and Green form

Use a smooth conformal metric bounded above and below near p and a unitary
flat gauge on the punctured disc. In Cartesian spin frames the local
massless Dirac operator is

    D_0 = -i [[0, partial_x-i partial_y],
              [partial_x+i partial_y, 0]].

The critical solutions are

    psi_+ = z^(-1/2) u,     psi_- = bar(z)^(-1/2) v,

with u,v in C^6. They are L2 near zero in the smooth metric, since their
radial squared norm is proportional to integral dr. The other angular
harmonics are separated by integer increments. This is local leading
data, not the dimension of the full global kernel.

The radial Clifford matrix is [[0,e^(-i theta)],[e^(i theta),0]]. Its
current integrated over a small circle pairs (u,v) and (u',v') as
2pi times u* v'+v* u'. Inner versus outer normal changes its overall sign,
not its isotropic subspaces. A grading-invariant subspace splits into a
plus and minus subspace. Isotropy says these are orthogonal; maximality
says their dimensions sum to six. Hence they are

    Lambda_plus direct-sum Lambda_plus^perp.

Every rank d=0..6 is possible at this coefficient level. Full U(6)
invariance restricts Lambda_plus to 0 or C^6 by irreducibility of the
defining representation. That is a symmetry/naturality assumption, not
the definition of locality. A projector onto a boundary subbundle is
local, but its ellipticity must still be checked. Local coefficient
examples below do not establish that every such projector is an admissible
smooth-boundary PDE condition at a finite cutoff.

Source for these distinctions: https://arxiv.org/html/1307.3021v1,
sections 3.2-3.6 and 4.1. Our singular-point classification is derived
from its Green form, not asserted as an application of its smooth-boundary
theorem without checking hypotheses.

## 3. Preserve the one-form positive; test the spinor identification

Write g_cusp = Omega^2 |dz|^2, Omega=1/(r |log r|), 0<r<e^(-1).
For an ordinary twisted one-form F=f(z)dz, inverse metric and volume
cancel. Its radial norm is proportional to

    integral |f|^2 r dr.

For f~z^(-1/2), this is integral dr and is finite in both the smooth
and cusp metrics. This is precisely the W21 Hodge norm; its triplet is
NOT refuted by changing the metric.

Ordinary spinors have a different conformal transport. The isometric
spin-bundle identification beta gives

    D_cusp(Omega^(-1/2) beta psi_0)
       = Omega^(-3/2) beta(D_0 psi_0).

The two-dimensional kinetic norm of the transported zero spinor is

    integral Omega |psi_0|^2 r dr dtheta.

For a nonzero square-root-pole coefficient this contains

    integral dr/(r |log r|),

which diverges. At cutoff epsilon its divergent part is
log|log epsilon|, not a finite limit. For a regular sqrt(z) coefficient
the density is r/|log r| and is integrable. Positive definiteness prevents
different orthogonal parity blocks from cancelling the divergence.

This conclusion assumes the ORDINARY spinor kinetic action and canonical
conformal transport. A differential-form/Kahler-Dirac/topologically
twisted fermion action, weighted kinetic measure, physical cutoff, source
or asymptotic potential is a different problem, not excluded here.
The physical action must choose and justify it.

Conformal source: https://arxiv.org/html/1311.4182, Theorem 4.1, N=0.
The native check independently differentiates the conformal spin-connection
formula rather than trusting the exponent by name.

## 4. The actual twisted cusp channel, not the untwisted theorem

The spin structure on the punctured fibre is the restriction of a spin
structure on E. On a small circle it is bounding: a polar orthonormal
frame rotates once, and its spin lift returns -1. The gauge holonomy is
also -I. Their tensor product is +I. Thus the tangential covariant Dirac
operator on this circle has zero modes in all six gauge channels.
This is frame-independent total holonomy; gauge holonomy alone is not
the tangential spinor periodicity.

Use the hyperbolic cusp coordinate t=log(-log r). The metric is
dt^2+e^(-2t)dtheta^2. The unitary radial transformation multiplies the
orthonormal spinor coefficient by e^(-t/2), moving volume e^(-t)dt to
dt. In a zero tangential channel the radial operator becomes

    D_rad = [[0,-partial_t],[partial_t,0]],

up to a constant unitary Clifford convention. Its symbol at momentum
lambda has eigenvalues +/-lambda. The operator is massless: no extra
asymptotic Higgs or weighted-kinetic term is silently included.

For b(s)=s^2(1-s)^2 on [0,1], extended by zero, let

    u_(T,L)(t)=c L^(-1/2) b((t-T)/L) exp(i lambda t) v_lambda,

where v_lambda is a normalized constant symbol eigenvector and
c^(-2)=integral_0^1 b^2. The function and first derivative vanish at the
endpoints, so it is in H1 and is approximable by smooth compactly
supported sections. Direct integration gives norm one and

    ||(D_rad-lambda)u_(T,L)||^2
       = (integral b'^2)/(L^2 integral b^2) = 12/L^2.

Take L_n=n, T_n=n^3: supports eventually escape every compact set and
are disjoint for successive large n. They converge weakly to zero.
This is a Weyl sequence for every real lambda, including zero.
Its compactly supported members extend by zero into the full surface,
irrespective of modifications confined to its compact core.

Consequently zero is in the essential spectrum of this complete,
massless, standard spin Dirac problem. Its graph operator is not Fredholm
at zero; nor can both graded chiral blocks provide a Fredholm chiral
operator and its adjoint there. This is NOT an assertion that its index
equals zero or that its kernel has no states. On a complete manifold
the standard unitary Dirac closure is essentially selfadjoint; a point
at infinite distance is not a finite boundary carrying the preceding
free extension coefficients.

Baer math/0010233 section 3 Lemma 1 and Theorem 1 personally checked:
https://arxiv.org/pdf/math/0010233. The local flat twist changes the
vertical operator, so the preceding Weyl proof is supplied explicitly.
Baer's untwisted one-cusp Corollary 1 has DISCRETE spectrum because an
untwisted bounding spin circle has no zero mode. It cannot be applied
unchanged after tensoring by this -I gauge holonomy.

## 5. What this can and cannot discharge

The packet supports the conditional sheaf formula and local current
classification while testing a previously unspecified kinetic choice.
It does not derive a physical choice of metric, boundary response,
parent fields, reality, gauge half, hypercharge or interactions. It is
neither a negative about the whole weave nor a selected chiral SM.

Positive hatch: the W21 form-based kinetic realization is not subject to
the ordinary-spinor norm objection. Another hatch is a finite-distance
cut with a dynamical boundary response; an asymptotic mass/twist may also
change the cusp operator. Each must be obtained from the SAME stated
action and carry stationarity, positivity and the full charged spectrum.
The old silver formal boundary result supplies a benchmark, not this
missing physical dictionary. Nonauthor analytic acceptance remains owed.
