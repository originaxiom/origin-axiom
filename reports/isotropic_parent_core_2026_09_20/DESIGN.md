# F06 pre-execution design: can the isotropic parent current solve all equations?

2026-09-20. Fork-local research at input `28c87f5a`, not a shared B arc,
main banking pass, global physical vacuum or claim of literature novelty.

## Scope and prior

This tests a local D5-invariant SU4 sector of the already specified E8
parent, on a supplied conformally Euclidean three-dimensional domain with
boundary. It does NOT quantify over all manifolds, full-relations objects,
harmonic metrics or backgrounds. The metric is allowed to vary in this
test; a result cannot be transferred to the fixed hyperbolic base.

R39's full matrix equations and rank/Gram test are already available at
`8d2cced2`. R29's scalar tube action is different. The point here is to
solve the remaining differential equations for one isotropic current, not
repeat the rank test or identify added zero-form fields with one-forms.
The chosen priority follows the approved common-model origin gate.

Expected positive: a three-component charge-four one-form ansatz solves
complex flatness and the entire moment equation when its conformal factor
v>0 satisfies the ordinary Euclidean equation Delta v=-4 a^2. A quadratic
v gives an explicit smooth local core without added source fields.

Expected costs: its scalar curvature is positive, so this restricted
construction cannot itself be a hyperbolic patch. Its maximal quadratic
extension has a degenerate metric at finite proper distance and divergent
Higgs norm; only compact subdomains inside that surface are smooth finite
cores. No gluing, complete solution, selected metric or chiral spectrum
is expected from these checks.

An additional mathematical comparison is disclosed before execution: the
quadratic core should obey Ric=(32/3)Tr(Psi tensor Psi), the Einstein--
harmonic-map equation for a DECLARED auxiliary three-dimensional action
integral(R-(32/3)|Psi|^2). That is not the gravitational action derived
from the original program or the seven-dimensional SYM parent. The
coefficient, trace, spacetime dimension and action change are explicit;
neither an observed gravitational coupling nor a 4D Einstein equation is
claimed. Retain or reject this comparison on its actual tensor equation.

Alternative: any residual, normalization, regularity or operator control
fails. Preserve its first result; do not repair a sealed expectation in
place. No execution of the new scientific producer precedes its seal.

## Fixed conventions

- Euclidean coordinates x1,x2,x3; g=v^2 delta, v>0, real a>0.
- U=diag(3,-1,-1,-1), N_i=E_(0,i+1), defining-four trace.
- h=d(log v)/8, alpha_i=a v^(-1/2) N_i; C_i=h_i U+alpha_i.
- A=(C-Cdag)/2, Psi=(C+Cdag)/2.
- F_ij=partial_i C_j-partial_j C_i+[C_i,C_j].
- I=v^-3 partial_i(v(C_i+C_i dagger))+v^-2 sum_i[C_i,C_i dagger].
- Positive norm |Psi|^2=v^-2 sum Tr(Psi_i^2); no switch to E8 adjoint
  trace without R39's known factor of sixty.
- Quadratic core v=c-(2 a^2/3)|x|^2, c>0. Its maximal positive radius
  is R=sqrt(3c/(2a^2)); calculations on r<R are local.
- The lower-column comparator is C_dual=-C^T; it reverses the h/source
  sign, not merely the label of the charged representation.

## Controls and acceptance criteria

1. Derive F and the FULL I matrix from the displayed connection and
   metric with arbitrary first/second jets of v; expected
   I=(Delta v+4a^2)U/(4v^3). Off-diagonal and su3 equations must vanish.
2. Check charge, isotropic Gram and the rank-two comparator. Removing one
   component while retuning the central equation must leave a nonzero
   traceless lower-block residual. Zero amplitude/constant v is a control.
3. Derive Christoffels and Ricci directly, not only a scalar formula.
   Under the PDE, expected R=16a^2/v^3+2|dv|^2/v^4>0. For v=1/z
   the metric has R=-6 but I is nonzero: this must fail the BPS test.
4. Derive the positive norm and the full Einstein comparison. The
   trace-free Hessian deformation with Delta v unchanged must preserve
   BPS while FAILING the proposed Einstein equation. It is not automatic.
5. Verify finite proper distance and positive logarithmic coefficient of
   the Higgs-norm integral at r=R. Keep the nonzero boundary flux; no
   closed/global extension or zero-width limit by omission.
6. At the normalized core center a=c=1, construct T=Psi wedge exactly.
   Expected H1=T*T+TT* has eigenvalues 0 (5), 1/2 (6), 3/4 (1), with
   symmetric trace-free tensor kernel. Compute the full covariant
   derivative of Psi: it must be nonzero while its trace vanishes.
   Thus F05's parallel-Higgs identity is not transferable. Neither
   pointwise kernel nor lost lower bound is called a physical zero mode.

## Prior retrieval and reading boundary

Personally reread R29 DEFECT_GAUGE_PROOF, R38 PARENT_VERTEX_PROOF,
R39 PARENT_BACKGROUND_PROOF at its sealed pin, the common-model audit,
R35's retained local T-brane route and F05's code/proof. The standing
working/banking/compute/campaign instructions were revisited. The original
audit's full framework and ladder reading remains antecedent work.

already_banked was run for `parabolic moment fundamental charge source`
(broad incidental hits) and `isotropic coframe conformal` (no settled arc
matching two of three terms). Code and law/open-lead searches were also
read. The targeted R39 search recovers the explicit isotropic-Gram hatch.
An initially unquoted Git pathname glob failed in zsh; the quoted retry
is the usable result. The atlas card is a coarse older vocabulary, not
an absence certificate. No corpus-wide novelty or absence claim is made.
The previous all-history resweep remains the retrieval background, and
the known fetch authentication failure prevents a fresh-head guarantee.

Primary HTML rechecked: Braun et al. 1812.06072v2, equations 2.17--2.24;
the full parent BPS system is distinguished from its subsequent commuting
source truncation. PW 0905.1968v1's abstract/opening and section-2.5 entry
were navigated; no new result is imported from that navigation. The
1906.02212v2 HTML request failed; its prior R35 reading is not counted as
a new full-paper read. No PDF or agent summary is used in this checkpoint.

Seal this design, proof, producer and tests before first execution. Keep
all F01--F05 and R39 sources frozen. Findings must state the metric and
boundary price at least as prominently as the local positive.
