# Nonlinear end response from the existing action

2026-11-16. PHYSICAL-C5 author analytical continuation, pending independent
review. No scientific producer, import, CAS, collection or test ran.
The construction is conditional on the earlier physical source action,
complete domains and gauge-inverse proofs. It makes no SM3 or gravity
closure claim.

## 1. Reuse the actual configuration metric and Gauss equation

The starting point is P-C3b's
FINITE_BULK_CONNECTIONS_QUARTIC_AND_REAL_GAUSS.md. It already constructed
a finite-action affine path X_s=(A_s,q_s,r_s) in fixed smooth bundles,
the exact restricted potential and its real gauge response

    V(s)=B s^2(1-s)^2, B>=0,
    k_s alpha=(Dbar_(A_s) alpha,i[alpha,q_s],i[alpha,r_s]),
    L_s=Re k_s^dagger k_s,
    b_s=Re k_s^dagger dot X_s,
    alpha_s=L_s^+ b_s,
    K(s)=||dot X_s||_c^2-<b_s,L_s^+ b_s>_v.            (1)

The metrics and coefficients in (1) are the original physical metrics.
The vector metric carries Omega^2/G. The chiral norm includes the
connection factor 1/2 and spin factor Omega/G. The superscript + is
the inverse on the kernel complement, with unbroken gauge modes kept.
At a varying stabilizer a smooth coordinate representative needs a
separate argument. The statements below work on a regular segment where
the horizontal field curve and K are smooth and K>0.

The earlier proof already obtained the restricted action

    E[s]=integral [K(s) (s')^2+V(s)] dx.                (2)

Its potential B is the actual integral of the parent's commutator and
moment residuals on this chosen affine path. This note reuses that
result. It does not select that path or assign B a new numerical value.

## 2. Derive the half-line response without a Robin coefficient

Suppose B>0, 0<s0<1 and K extends smoothly and positively to s=0.
Consider x>=0, s(0)=s0 and s(x)->0. Put

    W(s)=2 integral_0^s sqrt[K(u)V(u)] du.              (3)

The exact completion of the restricted energy is

    E=integral K(s) [s'+sqrt(V(s)/K(s))]^2 dx+W(s0).   (4)

Indeed the cross term is dW(s(x))/dx and W(s(infinity))=0.
The first-order decreasing solution obeys

    s'=-sqrt(V/K).

Near zero V=B s^2+O(s^3), so the travel integral to zero diverges
logarithmically and this solution has an infinite tail. Thus the
restricted on-shell half-line functional is

    Gamma(s0)=W(s0),
    d Gamma/ds0=2 sqrt[K(s0)V(s0)]
                =-2K(s0)s'(0).                        (5)

The last quantity is the outward canonical momentum. It is the nonlinear
Dirichlet-to-Neumann response in this one-dimensional restricted channel.
The assumed positive K and the specified asymptotic vacuum make (5)
an attained half-line response for interior s0. Endpoints at another
vacuum require a limiting argument and need not attain that infimum.

For constant K=K0, the source quartic gives explicitly

    Gamma(s0)=sqrt(K0 B) [s0^2-(2/3)s0^3],
    Gamma''(0)=2 sqrt(K0 B),
    decay exponent m_s=sqrt(B/K0).                     (6)

For varying K the same last two expressions use K(0) at leading order.
The full restricted 0-to-1 wall tension, when its endpoint conditions
are attained, is

    T_path=2 sqrt(B) integral_0^1 u(1-u) sqrt(K(u)) du. (7)

For constant K this equals sqrt(K B)/3. Equations (5)–(7) derive a
boundary stiffness and nonlinear response from the chosen path's actual
potential and Gauss metric. A separate scalar potential coefficient is
unnecessary in this conditional reduction.

## 3. Finite intervals give a composition law

For an increasing monotone extremal between a<b, the first integral is

    K(s)(s')^2-V(s)=C.

On a branch where V+C>0 the interval length and energy are

    L=integral_a^b sqrt[K(s)/(V(s)+C)] ds,
    Gamma_L(a,b)=integral_a^b
                    sqrt[K(s)] [2V(s)+C]/sqrt[V(s)+C] ds.            (8)

One must solve the length equation and choose the minimizing admissible
branch. Multivalued branches and endpoint degeneracies are retained.
The endpoint derivatives of an on-shell branch are -p_left,p_right,
where p=2K s'. The variational composition law is

    Gamma_(L+R)(a,c)=inf_b [Gamma_L(a,b)+Gamma_R(b,c)]. (9)

Here Gamma denotes the minimum over the allowed restricted paths. A
stationary intermediate b equates the two oriented momenta. If a core
source has an actually derived functional S_core(b), its derivative
enters the same momentum balance. Equations (8)–(9) provide a direct
way to sew core and end responses from a common action while keeping
their signs, normalization and state data.

The earlier ACTUAL_CORE_MEAN_RESPONSE_AND_FLUX_SEWING_2026_11_08.md
already derived a quadratic gauge-sector response. Equations (3)–(9)
apply the same variational duty to this nonlinear restricted field
channel. The old surface-variational square completion is also retained.
These are applications of standard variational methods to the source
fields, with their limitations made explicit.

## 4. The full normal equation is the next decisive test

Work locally in the regular real gauge quotient with its physical
configuration metric. Let v_s be the horizontal tangent of X_s and let
nabla be that metric's Levi-Civita derivative. The bosonic parent residual
for a static one-coordinate profile is

    R_full=grad V-2[v_s s''+nabla_s v_s (s')^2].        (10)

Its tangent component is exactly

    <v_s,R_full>=V'(s)-2K(s)s''-K'(s)(s')^2.           (11)

The normal component is

    P_perp R_full=P_perp grad V-2 II_s (s')^2,
    II_s=P_perp nabla_s v_s.                          (12)

Thus a scalar extremal only discharges (11). The actual orthogonal
field equations (12), with the real Gauss constraint already solved,
are the required remaining equations. Evaluating (12) on the actual
affine path is a bounded, high-value next calculation. A nonzero result
identifies a necessary transverse response. It does not exclude other
paths or completed stationary solutions.

A proposed transverse correction must solve its actual linearized
operator on the complete domains, keep all zero modes and control the
nonlinear remainder. A finite matrix gap alone cannot invert a sector
with a cusp continuum at zero. The scalar response (5) is therefore a
restricted response until these coupled equations have been discharged.
Fermion zero modes, their domains and any fermionic effective action
retain separate derivation duties on that completed solution.

## 5. The stationary charged family supplies a different control

P-C3e's CUSP_GAUGE_INVERSE_AND_LOCAL_STATIONARY_BRANCH.md constructs,
subject to its analytic inverse lemma, a local charged-form family

    X(t)=exp[-psi(t,rho(t))].X_raw(t,rho(t)),
    F=mu=0, psi=O(t^2), rho=1+O(t),
    m_Q^2(t)=4 e_Q^2 t^2+O(t^3).                       (13)

Every static member has zero internal potential. On a regular finite
segment of this actual family, real Gauss elimination therefore leaves
a derivative action integral K(t)(t')^2 dx. Write its finite metric
length as ell_g=integral sqrt(K(t)) dt. For an interval of width W,
constant metric-arclength speed gives the trial energy

    E_trial=ell_g^2/W.                                (14)

These trial configurations need not solve the normal equations. They
are admissible energy upper bounds if the same bulk and end data permit
the entire segment. As W grows their energy tends to zero. Consequently
this local connected vacuum segment supplies no positive potential
barrier by itself. This is scoped to its connected segment and allowed
source data. It does not connect the distant state-axis endpoints or
discard a registering/source constraint that forbids such a path.

The leading canonical charged-mode kinetic term gives another direct
check. With P=t exp(i theta_+), R=t exp(i theta_-) and canonical Q gauge
field B_mu, its phase part is

    t^2 [(partial theta_+-e_Q B)^2
                           +(partial theta_-+e_Q B)^2]
      =(t^2/2) [(partial(theta_++theta_-))^2
                  +(partial(theta_+-theta_-)-2e_Q B)^2].            (15)

The gauge-direction phase produces the vector mass in (13). The
gauge-invariant phase has a derivative term. A periodic scalar potential
for it needs an actual additional residual or generated effect. The
classical stationary family has V=0. Equation (15) retains only the
leading canonical charged modes, while (13) retains higher-order metric
and field response.

## 6. What X-FRONTIER-4B's wall calculation establishes

The upstream function solve_coupled_e6_state_axis_join_bvp_mp implements

    E_c=integral [(c')^2+m_Q^2 sin^2 c] dx             (16)

and calls its massive case with m_Q=2. For this scalar model the exact
whole-line solution is

    c(x)=2 arctan exp[m_Q(x-x0)], c'=m_Q sin c,
    E_c=4m_Q.

This hand control explains its reported wall action near eight.
It checks a useful scalar model. An identification with the full
stationary E6 field construction requires an explicit X(c), its metric,
its actual residual potential equal to (16), the Gauss solution and
the normal equations (12). The source function exhibits none of those
field maps. Equation (13) supplies a vector mass on one local family.
Equations (13)–(15) alone do not yield the scalar potential in (16).

## 7. The bounded continuation

The strongest next calculation uses the actual affine source fields to
evaluate P_perp grad V and II in (12), while respecting their registering
defect and endpoint law. Either they cancel and yield a real stationary
candidate, or their discrepancy gives the required source for a controlled
transverse solve. The local vacuum family (13) supplies a zero-potential
recovery control. Equations (5) and (9) then specify the boundary response
that a successful completed path must reproduce in its restricted channel.

The same-action field/domain and registering/end map is still incomplete.
No independent foundational input has been counted removed here. The
path selection, global core/end geometry, action normalization, physical
family identification and gravity duties remain visible.

The use of a field-induced collective-coordinate metric is established
in Manton, Oles, Romanczukiewicz and Wereszczynski, sections I–III of
Kink Moduli Spaces — Collective Coordinates Reconsidered. Those sections
were read personally for this continuation. Our equations above follow
directly from the declared source action and endpoint variations.
[Primary paper](https://arxiv.org/html/2008.01026v2)
