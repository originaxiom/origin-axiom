# Preliminary author cross-checks while main's review is pending

2026-11-08. **AUTHOR ANALYTICAL CROSS-CHECKS, NOT INDEPENDENT REVIEW.**
Source target1661880340cd0ac6aee0c412d87be4123dcc1397, especially
ACTUAL_ZERO_MODE_CURRENT_AND_RANK_ONE_VECTOR_2026_11_08.md. No scientific
imports, collection, CAS/matrix/numerical evaluation or tests executed.
The calculations below are hand arguments. Their agreement improves the
internal consistency case; it neither proves every hypothesis nor changes
the candidate's UNREVIEWED/UNRUN status.

The owner's question is right: checks before final acceptance can expose
mistakes and inform exploration. Existing execution rules still distinguish
author hand/source scrutiny from admitted computational verification.
This document implements the former and names the latter's priorities.

## 1. Recover the vector mass by a different operator identity

Let mu=m+n be the eigenvalue of H/2, on the source V_j tensor V_j
coefficient. The stationary bundle has

    F_A/dvol=-H/(4ell^2),
    [D_x,D_y]=-i ad(F_xy).

In the source conformal metric, the scalar/gauge norm is Omega^2 dxdy,
whereas ||Dbar w||^2 in D0's form is integrated against dxdy. Thus

    Dbar^{*v}Dbar=-Omega^-2(D_x-iD_y)(D_x+iD_y)
                =nabla* nabla-ad(F_A/dvol)
                =nabla* nabla+mu/(2ell^2).                (1)

No derivative of Omega is omitted: in two dimensions the scalar rough
Laplacian in conformal coordinates is exactly
-Omega^-2(D_x^2+D_y^2). This statement uses the gauge norm, not the
spin-slot norm. Complete cutoffs extend the quadratic-form identity.

The actual Higgs term calculated directly from D0 is

    c_mn=[2j(j+1)-m^2-n^2-mu]/(2ell^2).

Combining it with (1) gives the independent useful form

    Pv=nabla* nabla+[2j(j+1)-m^2-n^2]/(2ell^2).            (2)

It is manifestly invariant under simultaneous weight reversal. For the
charge-one j=3/2, mu=-2 pair, m^2+n^2=5/2. Therefore

    Pv=nabla* nabla+5/(2ell^2).

Its proposed holomorphic w0 obeys Dbar w0=0, so (1) gives
nabla* nabla w0=w0/ell^2. Formula (2) again gives
Pv w0=7w0/(2ell^2). This agrees with the direct raising-norm sum 3+4.

For the Hermitian conjugate, Q and mu reverse. The rough Laplacian has
the same eigenvalue, while (1) now gives
Dbar^{*v}Dbar(w0†)=2w0†/ell^2. The positive-grade raising-norm sum is
instead 0+3, giving Higgs term3/(2ell^2). Their sum is again7/(2ell^2).
The conjugate is not assumed holomorphic. This is a useful check on
reality, curvature sign, derivative adjoint and the relative factor two.

An explicit wrong-control hand comparison: halve only the Higgs term
while retaining the declared source connection. The two masses would
then be7/(4ell^2) and11/(4ell^2), violating compact conjugation. Such a
mutation does not describe the same stationary action. Scaling all
geometry consistently would be a different model, not this control.

## 2. The extension and cusp convergence agree independently

For rank-two flat periphery -I, the single-valued extension frame is
f_i=z^(1/2)e_i. Its determinant has one zero, det(f)=z det(e), so the
extension degree is -1. The dual frame gives E(V*)=E(V)*(-p). These
facts forbid replacing it with two degree-zero compact flat lines.

In S^2 the actual radial norm for pole order N in that frame is
integral r^(2-2N) dr. A simple pole has finite integral; a double pole
diverges. The allowed compact sheaf is E(V)(p), degree+1. The flat-norm
maximum principle gives h0(E(V))=h0(E(V*))=0; compact genus-one RR and
duality then give h0(E(V)(p))=1, h1=0. The degree calculation and the
physical convergence test consequently select the same bundle.

This checks the local determinant/pole bookkeeping and the use of the
classical compact theorem. The global transition identification and
passage to the actual operator domain remain analytical review duties.
It is not a numerical endpoint test with an arbitrary finite cutoff.

## 3. The transition matrices have the required peripheral

On the candidate vector two-plane, A=i alpha sigma_x, D=i sigma_z,
alpha^2=1, and B=DA. Hence A^2=D^2=B^2=-I, AD=-DA, AB=D and
[A,B]=(AB)^2=-I. The coherent central sign changes alpha but not this
peripheral. A replacement by commuting compact characters gives +I
instead and cannot be used with the same extension calculation.

The corresponding form-current two-plane has A=alpha sigma_x and
D=-I. Its two compact characters are (+,-) and (-,+), and its
peripheral is identity. These are different actual bundles even though
both have rank two. Equal rank is not a spectral identification.

## 4. The current selection survives conjugates and basis changes

The source current is diagonal in (lambda,a,u',v'). The exhibited form
and spin modes therefore have zero cross matrix elements before any
integration. Principal weights then require -1 and -2 for the left form
and spin blocks, and +1 and +2 for the corresponding right blocks
written using independent LEFT conjugates. This reproduces all four
rows rather than checking only the desired left-current example.

For w0, the bracket with the nonzero down spin mode is a global
holomorphic up spin mode. The two extremal Spin5 bracket components
are nonzero and map different spin slots, so they cannot cancel each
other in the positive product norm. Defining the normalized up mode
from that product makes its overlap g6 times that positive norm.
Unitary changes of the zero-mode bases preserve rank and vanishing.

This cross-check does not calculate the norm's value, exclude additional
zero modes, remove right-current vectors elsewhere, or establish weak
SU2 closure. A rank-one projected current remains a rank-one result.

## 5. A sharper spectral target, with a scoped lower bound

On the entire mu=-2 charged-vector two-plane,

    Pv=Dbar^{*v}Dbar+7/(2ell^2).

Its nonnegative form implies a lower bound7/(2ell^2); the proposed
holomorphic w0 attains it. Conditional on the extension argument, the
ground eigenspace in THIS subspace is one dimensional. This is not a
lowest-eigenvalue claim for every charged vector or a uniform bound
through changing metrics. It is a stronger internal check on (8) of
the candidate proof than merely finding a local trial profile.

For the mu=-1 form-current two-plane,

    Pv=Dbar^{*v}Dbar+3/ell^2
      =nabla* nabla+5/(2ell^2).                           (3)

Its S^1 coefficient splits into the two nontrivial compact characters,
so there is no holomorphic zero of Dbar at eta=O. Under the retained
odd-sector compact-resolvent hypothesis its lowest eigenvalue is
strictly above3/ell^2, with no claimed quantitative excess. To join
the spin-current ground mode at one pole, this particular bundle must
have a Dbar^{*v}Dbar eigenvalue exactly1/(2ell^2), equivalently a rough
Laplacian eigenvalue1/ell^2. This is a precise future calculation,
not a proven equality or impossibility.

The additional mu=-1 weight (-1/2,-1/2) has
Pv=Dbar^{*v}Dbar+4/ell^2, so it cannot join the7/(2ell^2) pole. It
remains in the full vector theory. Higher spin-current eigenvalues
have their own possible joins; failure at this pole would not exclude
every alternative. Even a same-pole rank-three join still owes the
normalized singular values, neutral currents and weak algebra.

## What these checks earn and what to verify next

Internal analytical comparisons agree on the proposed mass, conjugate
partner, extension, selection rule and bounded current witness. They
use the same inherited hypotheses and are not statistically independent
evidence. There is no justified numerical confidence percentage yet.

Highest-value admitted computational checks, once the current gate is
satisfied, are:

1. Actual source D0 and M matrices with their weights and BOTH chiral
   Spin10 modules; recover the Higgs sums and pure representatives.
   This should also repair the older generic-Koszul V1 coverage gap.
2. Actual full-E8 compensator restrictions and the extremal spinor
   brackets, with omitted-flavour, wrong-centre, wrong-grade, omitted-
   conjugate and factor-two mutations required to fail.
3. Exact formal cusp exponents, extension determinants and full charged
   count bookkeeping, backed by separate global proof review.
4. Only then, a source-complete global spectral/overlap computation on
   a specified actual metric and bundle. Preserve convergence evidence,
   alternative domains and possible continuum effects. A fitted modulus
   chosen to enforce the desired eigenvalue would be a residual input.

The prospective ten-duty design already records the finite-control
scope. It is not yet registered or implemented. The adopted rule requires
exact source-complete nonauthoring review, separate main acceptance and
strict admission before scientific execution. Calling a run exploratory
does not itself amend that rule. The owner may explicitly authorize a
bounded preliminary-execution policy; no such amendment is inferred
from asking which checks would be useful. Historical status, first
failures and formal banking requirements must remain intact.
