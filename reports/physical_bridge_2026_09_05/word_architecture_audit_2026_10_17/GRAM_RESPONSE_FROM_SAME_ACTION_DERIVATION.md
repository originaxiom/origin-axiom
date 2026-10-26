# When the same action generates an inverse-Gram response

October 26, 2026. UNREVIEWED author hand derivation and source audit.
No scientific code, symbolic engine, collection, optimization or test
was run. This continues the owner's approved input-reduction mission;
it does not replace the physical SM3/gravity objective with a frame fit.

## Named duty and recovered source

Does agy's proposed h=conjugate(Sigma_down)^(-1)v follow from an existing
physical action, rather than a new action invented to produce h?
Does that action also select the asymmetric residue-zero condition?

Reused: the complete action and stationarity sections of
weave_curved_action_2026_10_08/PROOF.md; the actual bilinear, cubic,
boundary and normalization discussion in REDUCTION_CARD_02; the
EXTERIOR_RESPONSE_AND_JOINING and FULL_MODE_ELIMINATION notes; agy's
B1761 actual producer, B1757 nine2() and the source audit just recorded.
The existing curved-parent action already retains positive kinetics,
the full moment square and the nonzero covariant Yukawa. No new field
content or mode truncation is derived here.

## 1. Distinguish three objects before identifying them

For a fixed chosen three-component Higgs coordinate h, the frame defines

    Y(h)=sum_a h_a Y_a,
    Sigma_ab=Tr(Y_a^dagger Y_b).

Hence h^dagger Sigma h=||Y(h)||_HS^2. This positive semidefinite Gram
is an exact mathematical output of that chosen vertex map. It is
positive definite only when the three matrices Y_a are independent.
Its trace normalization is a common positive scalar and cancels after
projective normalization of Sigma^(-1)v. That particular scalar is
not another adjustable Higgs-direction parameter.

The following are nevertheless different data:

1. The vertex Gram Sigma on the space of chosen Higgs coefficients.
2. The physical kinetic metric G_H from the integrated mode profiles.
3. The quadratic fluctuation Hessian A_H of the full stationary action.

Neither equal size nor positivity identifies them. In the supplied
curved action the potential is a sum of covariant residual squares.
At a zero-residual background, write C(Phi0+x)=Jx+O(x^2). The quadratic
potential is ||Jx||^2, with its stated source weights. This fixes the
real Hessian (up to the declared factor-of-two convention) from the
LINEARIZED residual map. The Yukawa vertices arise instead from higher
field derivatives/covariant couplings. They are not in general J^dagger J.
The full Hessian also includes gauge constraints and boundary work.

If the physical modes really realize the frame's Y_a, that is a useful
map to exhibit. It is not supplied by the Gram's definition itself.

## 2. Exact classical cubic control: no Higgs source at the empty origin

As a CONDITIONAL finite-mode control, suppose the actual field/action
map yields the ordinary cubic superpotential

    W_Y=L^T Y(h) R

with canonical matter kinetic metrics. This supposition is not a proof
that this mode truncation follows from our infinite-dimensional parent.
Its auxiliary potential is directly

    V_F=||Y(h)R||^2+||Y(h)^T L||^2
                       +sum_a |L^T Y_a R|^2.        (1)

At L=R=0, all three terms vanish for every h. Their first and second
derivatives with respect to h vanish too. Thus this cubic alone supplies
neither a Higgs source nor its positive Sigma quadratic potential at
the matter-free origin. Gauge D terms at a zero-moment, zero-field
origin start quartically in the scalar amplitudes. A separate internal
mass operator can contribute a quadratic term; it must be the actual
operator/domain, not assigned the name Sigma without a map.

This agrees with the existing curved-action source: at its flat
q=r=0 background the Hessian consists of the curvature and spin
derivative norms, while commutator interactions begin at higher order.
It does not exclude nonzero condensates, end sources, flux, a different
stationary background or quantum corrections.

There is a useful positive explanation for why a vertex Gram CAN appear.
If a specified matter state has covariances

    <R R^dagger>=c_R I, <conjugate(L) L^T>=c_L I,

the first two terms of (1) average to

    (c_R+c_L) h^dagger Sigma h.                    (2)

For a general state the covariances are matrices and yield a different
weighted Gram. Equation (2) is not an invitation to supply an isotropic
state for free; the state and its physical interpretation must be
derived or priced. It also produces NO term linear in h. The last
term of (1) is independent of h, and averaging it cannot provide one.
Nor is this classical state average a quantum determinant computation.

## 3. Actual complementary-field elimination fixes both response pieces

Use real coordinates for all independent compact-real variations;
complex coordinates are their faithful repackaging. Near a specified
background with a differentiable action, write its quadratic/linear part

    E(h,y)=1/2 h^T A h+h^T B^T y+1/2 y^T C y
                                  -j_h^T h-j_y^T y,
    A=A^T, C=C^T.                                 (3)

All blocks, sources, Hilbert metrics and domains must come from the
same functional. If C has a genuine inverse on the admitted complement,
stationarity in y gives

    y=C^(-1)(j_y-Bh),
    A_eff=A-B^T C^(-1)B,
    j_eff=j_h-B^T C^(-1)j_y.                       (4)

The remaining equation is A_eff h=j_eff. Substitution also retains
the constant -1/2 j_y^T C^(-1)j_y, relevant when sources or other
background fields vary. It cannot be discarded in their equations.
These are the old Schur elimination formulas with their linear source
restored, not a new heavy-mode method.

At a source-free stationary origin both j entries are zero, hence
j_eff=0. Eliminating homogeneous heavy fields does not manufacture
a nonzero source by matrix inversion. Expanding about an already
selected nonzero background instead changes A,B,C and the relation
between h and its absolute field value. The selected background must
stay in the input ledger until derived.

If C has a kernel, let P be its orthogonal kernel projection and C^+
the inverse on its complement, WHEN that inverse is admitted. Then

    P(j_y-Bh)=0,
    y=C^+(j_y-Bh)+k, k in ker C,
    (A-B^T C^+B)h+B^T k=j_h-B^T C^+j_y.            (5)

The compatibility equation and k remain. A pseudoinverse with k dropped
would change the physical system. Continuous spectrum can also prevent
a bounded inverse without any kernel; no finite-matrix argument proves
otherwise for the global surface operator. Retained norm feedback is
the separate derivative/Green identity already derived in the preceding
full-mode work, not a freely fitted Sigma.

## 4. The exact bridge that would pay the Higgs-direction choice

In the COMPLEXIFIED convention used by the proposed ansatz, one would
need an admitted positive Hermitian H_eff and source j_eff such that

    H_eff=c conjugate(Sigma_down),
    j_eff=d v,

with the scalar d/c either fixed or irrelevant only to the complete
relational observables being tested. Then the stationary direction is
indeed conjugate(Sigma_down)^(-1)v, up to that scalar. An explanation
of a projective direction does not by itself fix its physical amplitude,
electroweak scale, relative sector amplitude or coupling normalization.
The finite action would have to be bounded/stable in all admitted
directions and satisfy the other fields' stationary equations too.

This is a concrete sufficient bridge, not a proof these identities hold.
The unresolved source is as important as the unresolved Hessian.
Its existence cannot be inferred from a vector's closeness to a fit.

The formula must also be frame-covariant. If h=T h' is a general
invertible change of coordinates, then

    H'=T^dagger H T, j'=T^dagger j,
    h'_response=T^(-1) H^(-1)j.                     (6)

A seed given as a vector v instead transforms as T^(-1)v. It becomes
the required covector by the actual metric, j=G_H v. Omitting that
metric is harmless only in the declared orthonormal convention, with
all fields and sources transported together. Complex-conjugate sectors
require their actual conjugate transformation laws as well. The raw
matrix recipe is not a license for independently resetting them.

At fixed norm h^dagger G_H h=v_H^2, stationarity instead gives
(H_eff+mu G_H)h=j_eff. With no source it selects a generalized eigenvector.
One cannot generally normalize the unconstrained response afterward
and assert it solves that constrained action. These are different
variational problems, both potentially physical if actually derived.

## 5. Does the present action force the order-ten condition?

The theta residue identity identifies where one vertex channel vanishes.
It does not make that vanishing an Euler equation. In the conditional
cubic control (1), L=R=h=0 solves those equations for every admitted
flat line w. If the SAME flat connection family and remote domain are
allowed, curvature is zero and the classical source-free moment/derivative
potential supplies no preference among those w either. If some w are
globally inadmissible, demonstrate that from the actual bundle/domain.

Therefore the displayed local classical equations alone do not force
R_i^up=0. A derived nonzero state, its energy, its stability, a boundary
response or a genuinely generated admissibility condition might do so.
Their existence is not excluded. Adding a positive term |R_i^up(w)|^2
by hand would enforce the desired zero, but replaces the selector by
an action choice until that term and the other contributions are derived.

Likewise minimizing an unearned near-null measure does not derive its
cutoff 0.05 or the fitted-strip modulus. Preserve the exact conditional
order-ten arithmetic while earning the state law that would apply it.

## Before and after input accounting

| Item | Result of this derivation | Unpaid dependency |
|---|---|---|
| Trace-normalization scalar of Sigma in a projective inverse response | Cancels; no extra direction parameter | Physical amplitude/metric still separate |
| Independent arbitrary response vector once H_eff,j_eff are fixed | Replaced by their actual stationary solution, if inverse admitted | Derive those actual operators, sources and domains |
| Vertex Gram as Higgs Hessian | Possible in a specified isotropic-state control, not automatic at empty origin | State/covariance and full parent map |
| Nonzero inverse-Gram seed | Cannot be generated by eliminating homogeneous source-free quadratic fields alone | End/state/nonlinear background producing j_eff |
| Order-ten asymmetric-zero selector | Conditional arithmetic retained; no local classical selection at empty origin | Physical nonzero-state/admission/dynamics law |

The next discriminating task is to identify an EXISTING same-parent
boundary/nonzero-background source with the required trace and compute
both entries of (4), including complement kernels and kinetic response.
Do not choose a new source solely to reproduce v_DR. If no such map
has yet been exhibited in the inspected sources, keep this bridge
conditional rather than declare a programme-wide absence or obstruction.

No foundational input row is paid here. New executable controls must
be sealed prospectively and reviewed before execution. This note is
outside the completed four-proof review and the frozen P210 package;
agy's selected scalar checks do not constitute its independent review.

## Existing fermionic sources: positive backreaction, different source type

Before interpreting the unsupplied source as an absence, the full
surface_gauss_charge_2026_10_16 proof and the source/Hessian portions
of surface_all_boson_response_2026_10_16 were personally reread. They
already derive ALL ten fermion-induced currents from the actual parent,
their real Grassmann contraction, Gauss constraint and explicit electric/
spatial responses. Those are positive source constructions, not omitted
interactions. The norm and phase boundary flux are retained as well.

Their actual form is degree two in real odd variables:

    Psi=sum_s psi_s xi_s,
    j_N=sum_(s<t) j_N,st xi_s xi_t.

Let body be the augmentation homomorphism of this finite exterior
algebra, sending every xi_s to zero. It commutes with the displayed
ordinary differential operations and products. Applying it to the
coupled equations removes these nilpotent currents and returns the
original bosonic body equations. An induced degree-two response cannot
select a new ordinary nonzero body Higgs direction just because its
coefficient resembles a source vector. This is the same distinction
the Gauss source proof already makes for electric charge.

For the frozen-parent response problem with an admitted inverse C,
equation (4) maps a degree-two j_y to a degree-two j_eff and h response;
it does not turn their body nonzero. Source singularities, noninvertible
operators and independent body boundary data require separate analysis,
not division by a nilpotent element. Thus the actual fermionic source
does not by itself complete the proposed body inverse-Gram mechanism.

A quantum state expectation or fermion condensate could give an ordinary
bilinear current. That would require the state, its correlations,
renormalization, backreaction and actual operator; it is not obtained
by substituting a positive norm for Grassmann variables. This leaves a
specific useful continuation: derive such a state or a classical body
boundary/condensate response from admitted data, while preserving the
already computed nilpotent backreaction. Neither is declared impossible.
