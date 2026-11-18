# Source support for the existing complete-cusp inverse

2026-11-18. Author clarification of P-C3e equation (3), under the existing
M7/M8 review. Not independently checked. No scientific code, collection,
CAS or numerical integration ran. This writes out the four hypotheses
left conditional by main's `physical-c3e-03` record at `5dec726d6`.
It introduces no new background, action, boundary coefficient or state.

The result concerns the real gauge response of the **specified E6
classical sector on one fixed, connected, finite-area punctured
hyperbolic surface**. It is not an inverse for the complete E8 fermion
operator, an external-space interface, or every generated architecture.
The unbroken colour directions outside E6 and the other sector's neutral
fermion continuum remain present in the source theory.

## 1. Four premises, with their literal sources

All repository source references below are pinned to physical `8d5c91032`.
They are author proofs; a source reference alone does not independently
verify its claim.

| Duty named in main's record | Existing source | Clarification here |
|---|---|---|
| Background exactly parallel on the whole cusp | `physical_state_orbit_2026_11_16/PARALLEL_BACKGROUND_ORTHOGONAL_REDUCTION.md`, 54–70; the coherent transitions preserve the pair | The gauge potential is parallel as an endomorphism, not merely asymptotically constant; §2 gives the separated operator |
| Global gauge kernel exactly Q | Same source; `fixed_sector_light_system_2026_11_16/COMPLETE_PHYSICAL_KERNEL_AND_CORE_CHARACTERS.md`, 11–16; `neutral_source_response_2026_11_16/COMMON_REFLECTION_REDUCTION_AND_CORE_LIFTS.md`, 92–108 | §3 gives the compact-representation and complete-energy argument, including global preservation of Q |
| Uniform angular estimate in the presence of drift | `fixed_sector_light_system_2026_11_16/CUSP_GAUGE_INVERSE_AND_LOCAL_STATIONARY_BRANCH.md`, 27–58, 98–108 | §4 gives an explicit barrier uniform over all nonzero angular frequencies of this fixed bundle |
| Schauder and core matching | That proof, 18–25 and 81–120 | §§5–6 give lifted coordinate bounds, trace control and admission to the same complete domain |

Here and below paths in that table start with
`reports/physical_bridge_2026_09_05/`. The background's existence, its
joint spin/flavour/gauge gluing and the specified E6 restriction remain
premises for independent review. This note does not replace those
construction proofs with an inference from finite matrix checks.

## 2. The actual gauge operator and the drift correction

In the source orthonormal spin frame, the parallel pair is

    qhat=(E_+ + E_-)/(2 sqrt(2) ell),
    rhat=(E_+ - E_-)/(2 sqrt(2) ell).

The raising generators belong to two commuting principal su2 triples
in the orthogonal so5 factors. Both have total H/2 weight one. Their
spin and gauge connections cancel. The flat joint transitions preserve
their pair and its positive flavour metric. Thus the actual finite
Hermitian endomorphism

    M_g = sum_(z=qhat,rhat) (ad_z^dagger ad_z + ad_z ad_z^dagger)

is parallel and positive. On the cusp it commutes with ad_H and the
unitary peripheral transition. These finite commuting normal matrices
admit a simultaneous eigenbasis. No physical trace or kinetic metric
is changed by this unitary decomposition.

Use `g=ell²(dx²+dy²)/y²`, `t=log y`, with x-period L. The literal source
connection in its flat tensor frame is `A_x=-H/(4y)`, `A_y=0`
(`REFLECTION_ENDPOINT_GAP_AND_GLOBAL_JOIN_DUTY.md`, 55–62). Define w
by `[H,v]=2w v`. Then `D_x=partial_x+i w/(2y)`, with the equivalent
opposite convention changing the sign inside the square below. For
peripheral eigenphase `exp(2 pi i sigma)`, put

    nu=2 pi (n+sigma)/L, n in Z.

If `m²` is the corresponding M_g eigenvalue, the exact scalar channel is

    L_(nu,w,m) = ell^-2[-partial_t²+partial_t
                                  +(nu exp(t)+w/2)²] + m².       (1)

At nu=0 this has `c=m²+w²/(4ell²)`, exactly the indicial constant of
P-C3e. The measure is a constant multiple of `exp(-t)dt dx`.

**Terminology correction:** the cross term `nu w exp(t)` is not a
bounded function of t. Its coefficient w ranges over a finite bounded
list, and it is relatively dominated by the quadratic angular term.
The original proof's two references to a bounded linear drift are to
be read with this correction, not as a bounded-coefficient perturbation
in the unscaled radial equation. Physical connection coefficients on
fixed-size lifted hyperbolic charts are bounded; §5 proves that different
statement explicitly.

## 3. Why the complete gauge kernel is Q in this sector

Complexifying the E6 adjoint under the two compact principal su2s gives

    (0,0)_Q + (1,0)+(3,0)+(0,1)+(0,3)+(2,2)
                                            +2(3/2,3/2).       (2)

The dimensions are `1+3+7+3+7+25+32=78`. This roster is already used in
P-C3d/e. To see its origin, each vector five is spin two;
`Lambda²(V2)=V1+V3`, and the cross term is `(2,2)`. Each Spin5 spinor
four has H-weights `3,1,-1,-3`, so is spin 3/2. The Spin10 half-spinors
therefore restrict to `(3/2,3/2)`, twice in E6. Only Q is a trivial
compact module.

The two linear combinations qhat,rhat recover E_+,E_- separately.
Their equal coefficients also cancel the cross terms in M_g, leaving
`(4ell²)^-1 sum_(s=+,-) (ad_Es^dagger ad_Es+ad_Es ad_Es^dagger)`.
Vanishing of the positive M_g form requires commuting with both
raising generators and their compact adjoints. It is therefore
equivalent to invariance under both compact su2s. Equation (2) makes
`ker M_g=R Q` on real gauge sections, with a fixed positive eigenvalue
lower bound mu on its pointwise orthogonal complement. No numerical
value of mu is required or supplied.

The source compensators lie in Spin10 times its commuting electromagnetic
circle. Their rotations, P, Zeta and the old electromagnetic Wilson
all preserve Q. Their curved connection is spin-induced through H,
which commutes with Q. Consequently Q is a global parallel section,
not just a pointwise vector with a trivial cusp phase.

For the nonnegative complete realization, the source energy is

    <u,P_v u>_v = ||nabla u||_v² + <u,M_g u>_v.         (3)

An L2 kernel section has both terms zero. It is parallel and takes
values in RQ, hence is a constant multiple of Q on the connected
surface. Conversely Q is L2 because the area is finite, and exhausting
smooth cutoffs put it in the complete graph domain. There is no extra
kernel introduced by imposing reflection J=+1: Q lies in that sector
and the kernel of a reducing restriction is a subspace of the old one.

There is also a positive L2 inverse bound off this kernel on the fixed
surface. The parallel Q projection splits off a scalar Laplacian.
Its mean-zero spectral gap lambda_1 is positive for a fixed complete
finite-area hyperbolic surface. The complementary gauge block has
the pointwise M_g bound mu. Thus

    <u,P_v u>_v >= min(lambda_1,mu) ||u||_v²,  u perp Q. (4)

The scalar cusp fact is not a claim that the global gap equals
`1/(4ell²)`: small positive compact-core eigenvalues are allowed.
For orientation, compact-support Dirichlet tail functions satisfy
`integral |u'|² exp(-t) >= (1/4) integral |u|² exp(-t)`, by writing
`u=exp(t/2)v`. The scalar essential spectrum begins at `1/(4ell²)`;
the compact core leaves zero isolated. The standard cusp decomposition
and threshold are stated and derived in Christianson–Guillarmou–Michel,
*Random Walk on Surfaces with Hyperbolic Cusps*, §6.2, pp.22–23:
[author copy](https://www.imo.universite-paris-saclay.fr/~colin.guillarmou/randomcusp2504.pdf).
Its scalar Fourier operator is a recovery control, not a proof of our
matrix drift estimate. No uniform gap over degenerating surfaces or
varying global moduli is asserted in (4).

## 4. A uniform bound for all nonzero angular channels

Keep the finite set of peripheral phases fixed. The nonzero frequency
set then has a positive minimum magnitude nu_min and
`sum_(nu != 0) nu^-2 < infinity` on each of the finitely many channels.
This is not a bound uniform as an arbitrary holonomy tends to a phase
with a zero frequency.

Take the same positive delta as P-C3e and put a=delta+2. Let w_max be
the largest absolute total-H/2 weight. Choose a finite T, only for the
estimate, so that

    nu_min² exp(2T) >= 4 [w_max²/4 + a²+a].              (5)

For t>=T the elementary inequality

    (nu exp(t)+w/2)² >= (nu²/2) exp(2t) - w²/4

gives, for b(t)=exp(-a t),

    L_(nu,w,m) b >= nu²/(4ell²) exp(-delta t).           (6)

The derivative contribution is `-(a²+a)ell^-2 b`, and m²>=0;
these signs and constants explain the margin in (5).

For source coefficient f_nu and trace g_nu=u_nu(T), set
`F_nu=sup_(t>=T) exp(delta t)|f_nu(t)|`. A barrier is

    B_nu(t)=|g_nu| exp[-a(t-T)]
                 +(4ell²/nu²) F_nu exp(-a t).           (7)

It is nonnegative at the trace and `L B_nu >= |f_nu|`. To justify
comparison without an assumed value at infinity, first solve the
Dirichlet problem on [T,R] with boundary values g_nu,0. The positive
potential permits comparison for the real and imaginary components,
giving `|u_nu| <= 2 B_nu`. The coefficient two is a harmless bound for
combining them. The positive tail form gives the unique finite-energy
half-line limit. The restriction of the original complete L2 solution
has that trace and solves the same equation; the energy identity for
their zero-trace difference identifies them. Thus the estimate applies
to the actual solution, not to a chosen IR boundary condition.

The source Fourier coefficients obey `F_nu <= C ||f||_(C_delta^0)`.
The smooth trace on this fixed finite collar has absolutely summable
Fourier coefficients, bounded by its C2 norm. Summing (7) therefore
gives

    ||u_nonzero(t)|| <= C [||g||_C2 + ||f||_(C_delta^0)]
                                                   exp[-(delta+2)(t-T)]. (8)

The constants may depend on the fixed transition, T, delta, ell and
finite representation. They do not depend on the angular index. This
is the missing angular-sum control. It uses the growing drift, rather
than deleting it. Applying (5) to nu=0 would fail and is forbidden.

For completeness, the finite zero-frequency channels have the same
decay conclusion used in the earlier proof. For c>0,
`L_c exp(-delta t)=[c-delta(1+delta)/ell²]exp(-delta t)` is positive
by delta<beta_c. A trace-plus-source barrier gives C_delta decay. For
the one c=0 Q coefficient, growing exp(t) is excluded by L2. The
equation implies

    u_Q'(t)=ell² exp(t) integral_t^infinity exp(-s) f_Q(s) ds,
    u_Q(t)=a_infinity+O(exp(-delta t)).                 (9)

In particular `|u_Q-a_infinity| <= ell² ||f_Q||_(C_delta^0)
exp(-delta t)/(delta(1+delta))`. The asymptotic constant is allowed
by finite area and is fixed by the global solution, not supplied as a
new end datum.

## 5. Derivatives and the compact collar

At a lifted cusp point (x0,y0), use

    (x,y)=(x0+y0 X,y0 Y).

On any fixed small hyperbolic ball around (0,1), Y is bounded above
and away from zero, uniformly in y0. The pulled-back metric is
`ell²(dX²+dY²)/Y²` and the pulled-back gauge one-form is
`-H dX/(4Y)`. M_g is constant in this frame. All coefficients and their
fixed-order derivatives are uniformly bounded, and ellipticity has
a fixed positive constant. This gives charts on the local universal
cover even though the base cusp's injectivity radius shrinks.

The interior Schauder estimate therefore has the same constant on
these balls. Its hypotheses and C0 remainder are given explicitly by
Haslhofer, *PDE II – Schauder estimates*, Theorem 0.1, pp.1–4:
[author notes](https://www.math.utoronto.ca/roberth/pde2/schauder_estimates.pdf).
For our finite system the principal part is the scalar metric Laplacian
on each real component; bounded matrix first/zero-order terms are
handled by componentwise estimates and derivative interpolation.
The weight exp(delta t) and its logarithmic derivatives are uniformly
controlled on each chart. Higher-order estimates follow by
differentiating the smooth bounded coefficients. Hence the weighted
C0 bound from §§3–4 gives the two-derivative Hölder gain for the
decaying part of the same solution.

On a fixed compact collar, local elliptic estimates bound its C2 trace
and C^(k+2,alpha) norm by the source C^(k,alpha) norm and the global
L2 norm of the solution. Equation (4) controls that L2 norm. The
collar term in (8) is thus controlled by f. The Q constant in (9) is
controlled by a collar value and its decaying particular solution.
No independently adjustable Dirichlet trace or cutoff value enters.

## 6. Domain, source constraint and the existing nonlinear step

Use the original spaces, with k>=2, 0<alpha<1 and
`0<delta<min(1,beta_c)` over the finite positive zero-frequency list:

    X_delta = R chi_tail Q + C_delta^(k+2,alpha),
    Y_delta,0 = {f in C_delta^(k,alpha): <Q,f>_v=0}.

The Q coefficient is normalized with the original physical vector
inner product, including Omega², kappa and the action scale. It is
not replaced by a convenient flat metric. The globally fixed gauge
condition is `<Q,u>_v=0`.

Finite area, the constant parallel Q tail and the decaying physical
derivatives imply u,nabla u,P_v u are L2. Exhausting radial cutoffs
with bounded derivatives tending to zero approximate u in the graph
norm: `[P_v,chi]u` contains only controlled first derivatives of u
and derivatives of the cutoff. Compact-core smoothing then gives the
original complete realization. This also proves the claimed graph
admission of the allowed Q asymptote. Conversely the L2 inverse from
(4), local regularity and §§4–5 put every f in Y_delta,0 into X_delta.

Selfadjointness and P_v Q=0 give `<Q,P_v u>_v=0`; no unrecorded flux
condition is appended. The only kernel is Q and the stated convention
removes it. The estimates give the existing bounded bijection

    P_v : X_delta intersect Q-perp -> Y_delta,0.        (10)

Changing the artificial cutoff changes the decomposition coordinates
and an equivalent norm, not the physical boundary law. A multi-cusp
problem would need all its asymptotic coefficients and a separate
matching argument; one may not copy the single coefficient used here.

The source's nonlinear moment step still uses this exact inverse.
The positively weighted Hölder class is closed under products (the
product decays faster); the constant tail is along Q, commuting with
the unperturbed connection and pair. It acts boundedly on the stated
decaying charged modes. Near zero, matrix exponentials, products and
two physical derivatives therefore define the real-analytic moment
map on X_delta into C_delta^(k,alpha). The compactly supported moment
projection in P-C3e (5), rather than subtraction of a constant Q
source, preserves that decaying target space.

All background variations produced this way have bounded physical
coefficients. At fixed geometry their change of the first-order mass
map is a bounded zero-order perturbation, so the original graph domains
are unchanged. This does not imply Fredholmness or index stability in
a sector whose neutral continuum touches zero. Those fields remain
part of the full theory. The moment balance and its two implicit-function
steps retain their separate original proof and review duties.

## 7. What this does and does not discharge

This supplies an author argument for the estimate the existing proof
already claimed. It corrects the drift wording and exposes where the
fixed-background assumptions enter. Independent review must still check
the literal joint transitions, compact roster, source metric, cutoff
domain argument, uniform barrier comparison and nonlinear mapping.
Neither this note nor main's finite moment-model pass substitutes for
that review.

If independently sustained, the consequence is a **local stationary
charged family in the supplied fixed-metric action**, with the selected
mode directions and amplitude still explicit. It does not construct
the global join between distinct endpoints, select a vacuum, supply
weak-current chirality, earn three SM families, or vary the geometry.
The corresponding SM3/gravity and foundational input-reduction duties
remain open. No foundational input is counted removed.
