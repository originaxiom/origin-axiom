# A derived gauge/connection boundary response with its retained cubic interaction

2026-11-08. **Author analytical derivation, UNREVIEWED.** No scientific
module, test collection, CAS or numerical calculation was run. The
candidate verification design is separate. This note derives an exterior
effective action within the supplied physical parent; it does not derive
that parent from genesis or identify the abstract registering doublet
with an E8 gauge field.

## 1. Exact input-reduction question and reuse

Can an independently chosen boundary response and boundary gauge vertex
be replaced by consequences of the existing field/action/end data?
The answer below is conditional on a particular complete cusp and its
parallel unbroken gauge algebra. It is not a claim that every sector of
the generated architecture has now been physically coupled.

Reuse, with their original review qualifications:

- [The curved E8 parent](../weave_curved_action_2026_10_08/PROOF.md): actual
  kinetic weights, commutator interactions, moment map and complete end.
- [The coupled stationary bundle](../word_architecture_audit_2026_10_17/COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md):
  the nonzero spin condensate, all 248 coefficients and surviving parallel
  U3 gauge algebra. The colour subalgebra is non-Abelian.
- [Same-action transmission](../surface_same_action_transmission_2026_10_16/PROOF.md)
  and [exterior response and joining](../word_architecture_audit_2026_10_17/EXTERIOR_RESPONSE_AND_JOINING.md):
  common traces, sum of outward momenta, retained kernels and Riccati law.
- [The actual cusp response/norm](../word_architecture_audit_2026_10_17/ACTUAL_CUSP_WEYL_RESPONSE_AND_INDUCED_NORM.md)
  and [the gapless spin channel](../word_architecture_audit_2026_10_17/GAPLESS_CUSP_RESPONSE_AND_GAUGE_COUPLING.md):
  earlier fermion results remain distinct; no finite fermion norm at zero
  is inferred from the bosonic result below.
- [The previous unitary-family end price](UNITARY_FAMILY_REGISTER_AND_PHYSICAL_END_PRICE_2026_11_08.md)
  and [its anchor/interaction supplement](UNITARY_FAMILY_ANCHOR_AND_INTERACTION_SCOPE_2026_11_08.md):
  fixed flat representations, varying physical connections and family
  Hilbert spaces are different constructions.

The local response principle, general Schur elimination, gauge coupling
normalization and unbroken gauge algebra are not new discoveries here.
The additions are explicit scalar/vector cusp responses, their norms,
an actual finite cubic tail form factor and the precise curvature map
which allows finite-cut holonomies to vary without changing the remote
sector. A targeted source sweep found no exact previous instance of
this combined calculation; that is not an exhaustive novelty claim.

## 2. Extract the existing gauge sector without adding fields

Let (A0,q0,r0) be the source's specified residual-zero stationary
background. Let g0 be a parallel compact gauge subalgebra whose sections
commute with q0,r0 and their adjoints. For the cited candidate the old
unbroken U3 supplies such sections; its colour SU3 is sufficient here.
Use its inherited positive invariant trace kappa and the same g6.

For a g0-valued gauge perturbation a, the spin covariant derivatives
are unchanged, since [a,q0]=[a,r0]=0. Its curvature is

    F_(A0+a)=F_A0+f,  f=d_A0 a-i a wedge a.

The old moment residual is zero, so the new moment residual is precisely
f_xy. The other internal squared residuals remain zero. In a parallel
frame d_A0 is the ordinary coefficient derivative on g0. This gives the
existing Yang--Mills functional for f, with the inherited metric weights.
Other scalar Euler equations are not discarded: their extra variations
contain commutators with f and vanish because f is in g0. The gauge
equation also stays in g0; its orthogonal complement has no source.

This is a consistent classical BOSONIC sector with fermions zero, not
a new finite four-dimensional truncation or permission to delete the
other physical fluctuations, fermions, ghosts or continuum from a
spectrum/anomaly calculation. The nonzero original condensate is retained.

Take the specified cusp coordinates

    x mod 1,  y>=Y>0,  ds_Sigma^2=ell^2(dx^2+dy^2)/y^2,
    Omega=ell/y.

Use zero-angular fields in the parallel g0 frame and write

    b=a_x,  a_y=c,  a_mu=v_mu,
    f_mu_nu=partial_mu v_nu-partial_nu v_mu-i[v_mu,v_nu],
    f_mu_y=partial_mu c-partial_y v_mu-i[v_mu,c],
    D_mu b=partial_mu b-i[v_mu,b],
    D_y b=partial_y b-i[c,b].

After Wick rotation of the four external coordinates, the exact inherited
bosonic gauge action on this sector is

    S_g = 1/(2g6^2) integral d4z integral_Y^infinity dy kappa(
         Omega^2 sum_(mu<nu) f_mu_nu^2
         +sum_mu f_mu_y^2+sum_mu (D_mu b)^2
         +Omega^-2 (D_y b)^2).                       (1)

Hermitian fields and D=partial-i ad A fix the signs. The trace metric
is the source one throughout. In particular the scalar b and external
vector have DIFFERENT radial kinetic weights. Replacing both by a
flat half-line norm would change the theory. At nonlinear order c's
equation is the Gauss constraint; a gauge choice must not erase it.

The supersymmetric Yang--Mills origin and WZW qualification are standard
primary context in Arkani-Hamed--Gregoire--Wacker, Sections 2.3 and 3.2:
https://arxiv.org/html/hep-th/0101233v2 . The local reductions in (1)
use the repository's explicit component action, not an inference from
an equation number in a different HTML/PDF rendering. The curved action,
metric, twist and global physical identification remain supplied inputs.

## 3. Derive the two Euclidean exterior responses

At quadratic order use radial gauge c=0 and a transverse external
vector, p_mu v_mu=0. This is a channel calculation within (1), not a
choice of physical fermion boundary condition. Put s=|p|^2>=0 and

    nu(s)=sqrt(1+4 ell^2 s),
    P_b(s,y)=(y/Y)^(-(1+nu)/2),
    P_v(s,y)=(y/Y)^((1-nu)/2).                        (2)

For unit boundary values the two quadratic functionals, apart from
the same trace and 1/(2g6^2), are

    Q_b=integral [s b^2+(y^2/ell^2)(b')^2]dy,
    Q_v=integral [(v')^2+(ell^2 s/y^2)v^2]dy.         (3)

Their Euler equations are respectively

    -((y^2/ell^2)b')'+s b=0,
    -v''+(ell^2 s/y^2)v=0.                            (4)

Substitution of (2) checks (4). The complementary powers are not
normalizable in the ACTUAL coefficient norms: dy for b, Omega^2 dy
for v. At s=0 the rejected b branch is constant; the admitted vector
branch IS constant and has finite norm. Confusing these two statements
would remove the old normalizable gauge generator.

The outward normal of the exterior at Y points toward decreasing y.
The on-shell boundary momenta from (3) are -Y^2 b'(Y)/ell^2 and
-v'(Y). Thus the exact response functions are

    R_b(s,Y)=Y(1+nu)/(2 ell^2),
    R_v(s,Y)=(nu-1)/(2Y).                             (5)

The classical quadratic exterior action is

    Gamma_tail^(2)=1/(2g6^2) integral_p kappa(
           b0(-p) R_b b0(p)
           +v0_mu(-p) R_v v0_mu(p)),                 (6)

on the declared transverse chart. Both functions are nonnegative.
The scalar response at zero is Y/ell^2; the vector response at zero
is zero. Neither is an independently selected Robin coefficient.

## 4. The same response fixes the exterior norm

Direct integration of the Poisson solutions gives

    N_b(s)=integral_Y^infinity P_b^2 dy=Y/nu,
    N_v(s)=integral_Y^infinity Omega^2 P_v^2 dy
                                                 =ell^2/(Y nu).

Direct differentiation of (5), independently, gives

    partial_s R_b=N_b,  partial_s R_v=N_v.            (7)

The divided-difference Green identity gives the same result: for two
parameters s,t the cross norms are 2Y/(nu_s+nu_t) and
2ell^2/[Y(nu_s+nu_t)], equal to the respective divided differences
of R. This is the bosonic counterpart of the already-derived response
norm principle, not a transfer of the fermionic zero-energy gap formula.

In particular,

    R_b=Y/ell^2+Y s-Y ell^2 s^2+...,
    R_v=(ell^2/Y)s-(ell^4/Y)s^2+... .                 (8)

The positive leading kinetic weights are Y/g6^2 and ell^2/(Y g6^2).
The latter is the old tail-area gauge normalization, since the cusp
area above Y is ell^2/Y. These are contributions from one tail, not
measured whole-model couplings. A finite derivative expansion of the
square root is not an independent higher-derivative fundamental action;
the exact response and its domain must be retained.

## 5. A finite non-Abelian cubic vertex is already forced by (1)

The mixed cubic term in (1), in radial gauge, is

    S_vbb^(3)=-i/g6^2 integral d4z dy
                        kappa(partial_mu b [v_mu,b]). (9)

The vector field-strength square likewise fixes its usual cubic
term `-i/g6^2 integral Omega^2 kappa((partial_mu v_nu-
partial_nu v_mu)[v_mu,v_nu])`, summed over mu<nu.
No new interaction constant has been introduced.

The cubic coefficient of a stationary boundary functional is obtained
by inserting its linear Poisson solutions into the bulk cubic. Quadratic
cross terms with second-order field corrections vanish by the linear
Euler equations and zero correction to the specified boundary trace.
This determines the formal cubic coefficient; a global nonlinear branch
existence theorem is not supplied by this perturbative argument.

For p+q+k=0, put nu_sum=nu(p)+nu(q)+nu(k). Elementary power integration
then gives the two exact tail form factors

    I_vbb(p,q,k)=integral P_b(p)P_b(q)P_v(k)dy
                      =2Y/(nu_sum-1),
    I_vvv(p,q,k)=integral Omega^2 P_v(p)P_v(q)P_v(k)dy
                      =2ell^2/[Y(nu_sum-1)].          (10)

Their denominator is at least two for Euclidean momenta. The derivative
and Lie-bracket factors in the cubic vertex are those in (9), with
each field replaced by its boundary value. Thus (10) is a genuine finite
overlap, not a Lie-algebra dimension or an invented phase. For example
the colour SO3 subalgebra generated by Hermitian i times real 3-by-3
rotation matrices has a nonzero triple bracket trace. The existing
colour sector supplies nonvanishing vertices of this type.

As p,q,k tend to zero, I_vbb tends to Y and I_vvv to ell^2/Y. The
mixed cubic coefficient equals the scalar kinetic weight, and the
pure vector cubic coefficient equals its gauge kinetic weight, before
canonical normalization. This is the inherited gauge coupling relation.
Normalizing the tail alone gives g_tail=g6 sqrt(Y)/ell. It is not an
observed parameter: whole-core/tail normalization uses the full area
and recovers the previously derived g4, without a new boundary coupling.

Quartic terms, induced c/longitudinal corrections and fermion responses
are still required for the complete nonlinear gauge-invariant boundary
functional. Their existence and coefficients are constrained by the
retained parent, not licensed for deletion by this cubic calculation.

## 6. Sewing fixes the actual response; the cut is not a new scale

For the full bosonic source write mu=F+Omega([q,q dagger]+[r,r dagger])
and R_q=Dbar_A q, R_r=Dbar_A r. Direct variation at a smooth cut gives
the internal boundary work

    g6^2 theta_n = integral ds_0 kappa[
        (mu/Omega^2)(n_x delta A_y-n_y delta A_x)]
      +2 Re integral ds_0 Omega^-1 kappa[
        (n_x+i n_y)(R_q dagger delta q+R_r dagger delta r)]. (11)

Here n and ds_0 are Euclidean coordinate normal and line element;
the conformal factors have already been included. This retains the
spin moment source in mu. In the reduced scalar channel at the lower
end it gives exactly R_b b0. The other spacetime gauge momenta follow
from the mixed f_mu_y term of (1). The old superpotential primitive
and full fermionic Green pairing remain in their source formulations.

Joining a true core to this same tail gives the old variational law

    common field traces,
    delta Gamma_core/delta b0 + delta Gamma_tail/delta b0=0, (12)

and the corresponding vector/scalar/fermion/gauge conditions. Do not
set both outward momenta separately to zero. The full core response
has not been computed here. At quadratic order its scalar response
adds to R_b; zero modes and constraints must be kept if elimination
is singular. At cubic order (9)--(10) contribute the actual boundary
current, rather than an independently supplied matrix.

There is an exact cut-independence control in the scalar static channel.
For a shell a<=y<=b, its on-shell action has response matrix

    C [[1,-1],[-1,1]], C=ab/[ell^2(b-a)].             (13)

Attach the tail response R_b(0,b)=b/ell^2 and eliminate only the shared
shell/tail trace. Its Schur complement is

    C-C^2/(C+b/ell^2)=a/ell^2=R_b(0,a).              (14)

This is a direct same-action calculation, reusing the old general
sewing rule. The Riccati identities give its frequency-dependent form:

    partial_Y R_b=ell^2 R_b^2/Y^2-s,
    partial_Y R_v=R_v^2-ell^2 s/Y^2.                (15)

The seam location changes individual tail coefficients while leaving
the reconstructed joined variational problem unchanged. No arbitrary
new microscopic length has been derived from Y.

## 7. Curvature changes finite-cut records without changing the remote sector

For one commuting parallel generator H, the static extension is

    b(y)=b0 Y/y,  f_xy=H b0 Y/y^2.                   (16)

Its connection kinetic norm is proportional to b0^2 Y, and its internal
energy to b0^2 Y/ell^2: both are finite. Unlike a constant flat shift,
it tends to zero at infinity. It is an exterior solution for given
boundary trace, not by itself a source-free global stationary mode.
The core must satisfy (12). Positivity alone selects no nonzero b0.

The finite-circle gauge holonomy changes as

    P(y)=P_background(y) exp(i H b0 Y/y),
    P_background(y) -> P_infinity.                  (17)

when H is the chosen parallel generator. The background transport itself
can depend on y because the old spin-induced connection is nonflat;
it must not be replaced by its asymptotic limit at a finite circle.
More generally, in radial gauge, differentiating parallel transport
W_x=i A_x W along the circle gives the exact identity

    P^-1 partial_y P=-i integral_0^1 W^-1 F_xy W dx. (18)

With A_y nonzero, replace partial_y P by its based covariant derivative.
Equation (18), and its elementary commuting case (16)--(17), explains
how the finite-cut record can differ from the distant one: the curvature
retains the relation between them. A flat F2 representation alone omits
that radial/path data. Composition of fixed loop holonomies remains
valid; their invariance under changing the representative path does not
survive arbitrary curvature.

This does NOT establish transitions between distinct asymptotic kappa
leaves of the previous SU2 family. The actual physical gauge holonomy
here is E8-valued; the abstract quaternion flavour representation and
its raw two-dimensional trace are different typed data. Their proposed
physical identification still has to be earned. Nor has an atom in a
family Hilbert space been dynamically coupled by merely drawing (17).
What is now explicit is one finite-energy interacting physical gauge
response, on the actual source fields, preserving the chosen remote end.

## 8. Before/after ledger and next decisive duties

| Item | Conditional result here | Remaining input or duty |
|---|---|---|
| Independent scalar/vector boundary response | Replaced by (5) from (1) and complete-end norm | Supplied parent, cusp metric and end; core response |
| Independent exterior kinetic normalization | Replaced by (7) from the same response | Whole-model normalization and scale remain |
| Freely chosen cubic boundary gauge coupling | Replaced by the finite inherited form factors (10) | Full nonlinear/fermionic completion and physical on-shell amplitudes |
| Finite-cut holonomy response | Curvature law (18) and finite-norm example (16) | Field/reference identification with the foundational register |
| Mixing different asymptotic sectors | Not demonstrated | Derived end/architecture dynamics, if allowed |
| SM chirality, generations, numerical parameters, gravity | Not computed | Full original physical mission remains |

This is a candidate CONDITIONAL SAME-MODEL reduction of boundary-response
freedom. It is not yet independently reviewed, executed or banked, and
does not pay a foundational action/field/carrier row. Next: exact controls
for (3)--(18), complete source review, the actual core response with all
constraints, and the derived full-field/register map. The old gapless
spin sector is retained; this bosonic response has not removed it.
