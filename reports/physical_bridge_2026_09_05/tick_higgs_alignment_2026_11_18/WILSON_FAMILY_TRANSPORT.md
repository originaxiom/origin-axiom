# Derive the Wilson-family connection in a common magnetic bundle

2026-11-18. P-C8 author hand derivation; not independently checked.
No scientific code, CAS, imports, quadrature or tests ran. This extends
the zero-Wilson calculation of COVARIANT_LIFTS_AND_KINETIC_RESPONSE.md
using the same literal magnetic functions and positive unit-cell norm.
It derives a kinematic comparison within that supplied construction,
not a law making different Wilson backgrounds coexist physically.

## 1. Fix the domain before differentiating a Wilson line

Write tau=X+i y, z=x+tau u, zeta=xi+tau eta, with x,u in [0,1].
Here xi,eta are real Wilson-displacement coordinates; they are not
the relative complex coordinate called xi in cim_closed.py. Put

    chi_j(x,u;tau,xi,eta)
       =exp[i pi N(xi u-eta x)] psi_j(z+zeta,tau;0).    (1)

The second expression uses psi with its displacement included in
its argument only once. The source's equivalent call is psi_j with
argument z and Wilson line zeta. N is positive and the spin is fixed.
For the Higgs N=6 and spin=(0,0).

At zero spin the source functions obey

    psi(x+1,u;zeta)=exp[i pi N(u+eta)] psi(x,u;zeta),
    psi(x,u+1;zeta)=exp[-i pi N(x+xi)] psi(x,u;zeta).

Equation (1) therefore has the fixed boundary transitions

    chi(x+1,u)=exp(i pi N u) chi(x,u),
    chi(x,u+1)=exp(-i pi N x) chi(x,u).                 (2)

Fixed spin adds its fixed characteristic phases to (2); it does
not change the parameter derivatives below. Differentiating the
unretwisted psi at nonzero zeta while pretending its boundary
transitions are fixed would give a different ambient problem.

For D=d-i A the connection in this common bundle is

    A=pi N(x du-u dx)+2pi N(xi du-eta dx).             (3)

This follows from A(z+zeta)=pi N Im[(bar z+bar zeta)dz]/y and the
gauge phase in (1), at fixed tau. Thus the retwisting also carries
the actual flat Wilson contribution. In particular a displacement
by 1/N is already a large-gauge period; the displacement torus and
the physical flat-connection torus must not be silently conflated.

## 2. The normalized projection fixes a scalar connection

In the series expansion put a=j/N and r=n+a+u+eta. Including the
retwisting, differentiation at fixed x,u gives

    partial_xi chi = i pi N(2r-eta) chi,
    partial_eta chi = i pi N(xi+2 tau r) chi,           (4)

where r on the right multiplies each summand, not the whole sum
after it is evaluated. The x integral kills distinct Fourier
indices. The n sum and u integral turn r into a real-line Gaussian,
exactly as in the zero-Wilson calculation. Hence <r>=0 and
<r²>=1/(4pi N y). The tau derivatives have the same centered r²
term as before. It follows that

    Gamma_jk=<chi_j,d chi_k>
       =i delta_jk [dX/(4y)+pi N(xi d eta-eta d xi)].  (5)

For an actual coefficient c in Phi=sum c_j chi_j the projected
derivative is dc+Gamma c. For the source bubble variable h=bar c
it is dh-Gamma h. These are dual conventions for one construction,
not two kinetic choices. They must not be mixed with each other's
endpoint or mode transitions.

In this specified common-bundle embedding, parallel transport is
scalar on a simply connected parameter patch. Its curvature is

    d Gamma=i[dX wedge dy/(4y²)
                         +2pi N d xi wedge d eta] I_N. (6)

Thus even this derived comparison is not path independent as a
vector transport. Its scalar path phase cancels from conjugation
of a bubble. Nontrivial endpoint gauge and mode transitions still
have to be carried; (6) does not make all Wilson fibres one fixed
physical vacuum or remove those transitions.

## 3. Recover the half-period mode operators with their gauge factors

For zero spin, substitution in the same series gives

    chi_j(xi+1/N,eta)
       =exp[i(2pi u+pi eta)] exp(2pi i j/N) chi_j(xi,eta),
    chi_j(xi,eta+1/N)
       =exp[-i(2pi x+pi xi)] chi_(j+1)(xi,eta).        (7)

For a fixed second characteristic beta, the second identity also
contains exp(-2pi i beta/N). It is a scalar phase. The coordinate
dependent factors in (7) are the large-gauge transformations of
(3), not discardable discrepancies in the mode matrix. After they
are carried, the mode parts are the clock and cyclic shift. At
N=6, a half-period gives Z³ and X³ up to scalar phases; the inverse
shift has the same cube. Their anticommutation is retained. This
recovers the lift operators used in C18/C19 without identifying
their action with the ground pair, which they do not preserve.

Equations (5) and (7) must be used together. A scalar local connection
does not authorize dropping a mode-valued endpoint transition.

## 4. The same transport respects the balanced triple overlap

Use N_L=N_R=3, N_H=6 and exact lifted balance

    3 zeta_L+3 zeta_R=6 zeta_H.

The three retwisting phases cancel in
chi_L chi_R conjugate(chi_H). Thus the source's actual overlap is
unchanged, not replaced by another theta function. The two matter
spin phases cancel the conjugate Higgs characteristic as already
required by the original product.

The induced scalar connection on this product is
Gamma_L+Gamma_R-Gamma_H. If

    xi_rel=(xi_L-xi_R)/2, eta_rel=(eta_L-eta_R)/2,

then exact flux-weighted balance gives

    Gamma_L+Gamma_R-Gamma_H
       =i[dX/(4y)+6pi(xi_rel d eta_rel-eta_rel d xi_rel)]. (8)

This is a direct compatibility check between the relative-coordinate
closed overlap and its three actual mode bundles. It does not say
that the overlap is covariantly constant. Its variation can have
components outside the zero-mode tensor subspace. It also does not
replace the full matter operator or fermion domains.

## 5. The positive geometric kinetic term is fixed too

The part of d chi orthogonal to the N zero modes has squared norm

    <d chi_j,(I-P_zero)d chi_k>
       =delta_jk[|d tau|²/(8y²)
                    +(pi N/y)|d xi+tau d eta|²].       (9)

The first term is the centered r² variance. The second is the
centered r variance from (4). The cross term vanishes because
<r(r²-<r²>)>=0. The expression is positive and retains the original
unit-cell measure. It is a scalar in mode space for this embedding;
it cannot by itself select a ground eigenline.

Dropping (9) is a connection-only approximation to the full raw
derivative norm. The gauge constraint and heavy-mode response in
an actual higher-dimensional action can change that approximation.
No physical scalar mass correction is claimed without that action.

## 6. Exactly what has been earned, and what remains

The given normalized magnetic functions now determine a common
bundle frame, its projected Wilson/tau connection, its geometric
kinetic term, and the required endpoint mode transitions. No new
matrix comparison was typed into these formulas. The declared
embedding and ambient connection remain premises. A different
ambient base connection is not ruled out by this calculation.

For a proposed sum over distinct Wilson backgrounds, (5) supplies
a candidate comparison along specified paths. A global action must
still say whether those backgrounds are sectors of one theory,
alternative vacua, sites coupled by links, or samples in a measure.
It must specify the paths or joining equations and include their
gauge response. Averaging over all half-period frames is one further
operation; bundle covariance alone is not that operation.

Within a simply connected patch the comparison's scalar path phase
cancels from a bubble. On nontrivial loops (7) remains. These facts
constrain a proper joining law rather than supplying it. They close
part of the kinetic/frame calculation left open in the companion
proof, not the physical choice of joint state, vacuum or carrier.
Foundational inputs counted removed remain zero.
