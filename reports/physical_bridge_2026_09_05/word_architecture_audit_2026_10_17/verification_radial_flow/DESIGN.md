# Radial vacuum flow and nonconstant response: verification design

October 25, 2026. AFTER authored analytical derivation, BEFORE new check
implementation, scientific import, collection or execution. This is not
retrospective preregistration of that reasoning or a frozen P210 amendment.

BANKED IDENTITY: None. Proposed exact controls for an unreviewed
same-action radial reduction and its first-order operator. No new
numbered arc, physical chirality, global vacuum or input payment.

PRIOR ART: The existing curved action, cusp/graded/SM-parallel condensates,
two-field stationary example, neutral-stability decaying-perturbation
argument, and actual graded-cusp response. The constant blocks, graph
domain and paired zero-index controls are reused, not discoveries.

## Question, quantifier and decision

Do direct coordinate and finite-matrix reconstructions agree with the
source-derived radial flow, trace monotone, varying mass block and
transported exterior plane? Exactly TEN named unittest methods below
must complete without skips or expected failures in a subsequently
admitted execution. A failure, altered source, missing case or incomplete
run is preserved and stops certification. These are finite/algebraic
controls, not proof of all infinite-dimensional or physical hypotheses.

Prior: high confidence in the algebra after its authored derivation;
this is verification, not a blind prediction. A pass does not establish
the physical relevance or necessity of the supplied parent or ansatz.

Use exact SymPy arithmetic, Hermitian dagger, positive real y, t=log y,
right differentiation of matrix-valued profiles and the parent's kinetic
measure dt. No saved outputs, numerical fits, observed values or earlier
scientific producers are loaded. Fixed matrices and symbolic coordinate
reconstructions are authored separately from the prose formulas. This
same-author implementation is not an independent scientific verdict.

## Frozen intended method population and controls

1. `test_coordinate_residuals_and_opposite_orientation_control`.
   Differentiate A_x=-H(y)/(4y), q=E(y)/(2sqrt(y)), r=G(y)/(2sqrt(y))
   directly in the old Dbar and F_xy conventions. Recover all three
   differential residuals and moment coefficients, using dot=y*d/dy.
   Generic traceless 2x2 profiles are finite representation controls,
   not enumeration of E8. Wrong curvature orientation must fail.
2. `test_flow_preserves_commuting_constraint_reality_and_parities`.
   Reconstruct derivative of [E,G] by the product rule and verify its
   Jacobi transport. Check Hdot is Hermitian/traceless and p-even/odd
   compatibility on explicit p blocks. A changed relative commutator
   coefficient must fail the constraint transport identity.
3. `test_trace_monotone_by_directional_differentiation_and_wrong_weight`.
   Differentiate the trace polynomial along the actual matrix vector
   field, with generic traceless Hermitian H and complex E,G in 2x2.
   Compare with ||Hdot||^2+8||Edot||^2+8||Gdot||^2. Changing the trace
   polynomial's matter coefficient from two to one must fail on an
   explicit nonzero control. This does not prove boundedness/convergence.
4. `test_old_triples_and_two_field_fixed_points`.
   Recover a root 2x2 triple, the principal 5x5 triple and the old
   nonproportional SU3 two-field fixed point with their actual factors.
   The zero control is also fixed. A rescaled wrong Higgs amplitude is
   not fixed. Do not assume every commuting pair is an sl2 triple.
5. `test_scalar_reduction_and_linearized_stable_unstable_directions`.
   Reduce H=hH0,E=fE0,G=0 on the explicit triples and recover both
   scalar equations. Independently form the Jacobian at (1,1), its
   characteristic polynomial and opposite-sign eigenvalues; retain
   the quadratic remainder. These rates are not physical masses.
6. `test_kinetic_rescalings_and_nonconstant_complex_identity`.
   Reconstruct the unequal derivative coefficients from the actual
   sqrt(y) gauge and unscaled spin kinetic frames. Check D2D1 on an
   arbitrary test function using fdot=(1-h)f/2. Setting a=b away from
   h=1 must leave a nonzero residual. No deleted R/dual slot.
7. `test_operator_square_keeps_derivative_and_trace`.
   Act Bdagger B and BBdagger on arbitrary two-component functions,
   using formal adjoints in dt, and compare the two K^2 +/- Kdot
   formulas. Retain tr K=(1-h)/2 and a nonconstant exact profile as
   an instrument comparator for which dropping Kdot fails. That
   comparator need not solve the physical background equations.
8. `test_both_scalar_extremes_and_constant_recovery`.
   Through integer j=0,1,2,3,4 retain every even-m paired block and
   both orientations of the existing scalar extremes. At h=f=1
   recover their old K and scalar squared thresholds. Total singular
   channel dimension in one spin-j module is 2j+1. This is not a
   particle count or a proof of an essential spectrum.
9. `test_rotating_tail_transported_projector_not_instantaneous_sign`.
   Use the exact rational orthogonal rotation
   R(t)=[[1-t^2,-2t],[2t,1-t^2]]/(1+t^2), omega=2/(1+t^2),
   K=R[[1,-omega],[-omega,-1]]R^T, t>=0. Reconstruct R^T R=I,
   R'=R[[0,-omega],[omega,0]], the actual stable projector
   P=R diag(1,0)R^T and its transport equation. Check its limit and
   that [P,K] is nonzero at t=0. This is a Hermitian-tail comparator,
   NOT an OA vacuum or a solution of the radial BPS ansatz.
10. `test_rotating_tail_both_slots_green_and_integrated_norm`.
   For the same comparator verify x=exp(-t)R e1 and v=exp(-t)R e2
   solve their respective zero-energy equations. Keep both independent
   two-slot traces, their rank and Green nullness. Integrate their
   actual norms to 1/2 and reject the instantaneous 1/(2sqrt(5))
   formula at t=0. Positive kinetic norm is not a generation count.

## Separate analytical and physical review duties

The generic small matrices do not replace the cyclic/Jacobi proof for
all compact E8 directions. Read the action's component and trace/dual
normalizations, its four Weyl fields and the graph domain. Check the
positive-trace real differential and monotonicity, the explicit bounded
trajectory hypothesis, the accumulation-set proof and its refusal to
infer one-point convergence or boundedness from finite area.

Review the half-line integral contraction, its stable-amplitude freedom,
local versus global matching and actual kinetic/commutator integrability.
Review the varying differential mass block, both scalar extremes, the
constant unitary transport and stable-subspace equation. No assertion
that instantaneous eigenvectors give the response is permitted.

Check fixed metric/bundle/charged-block/domain hypotheses for graph-
compact index invariance. This is not an extension of a raw Q8 critical-
trace index to the physical parent; an actual intertwiner is still owed.
Changed end states, angular fields, unbounded profiles, nonzero-moment
stationary points, defects and different physical parents remain outside.
No admitted global SM3 spectrum, anomalies, normalized values or gravity.

## Source and execution boundary

Commit this design and its hash before implementing checks.py. Static
syntax/AST/population and hash reads are metadata only. Before any
scientific import, collection or run, require a complete source/input/
runtime/gate specification, declared fresh outputs, nonauthoring review,
main's exact structured acceptance and strict prospective admission in
a clean quiescent checkout. A design seal or source list is not admission.

Existing frozen infrastructure may be reused only unchanged; a new
wrapper binding needs its own software design and controls. Do not
copy old fixture results as a new wrapper certificate. Until that
source closure and review exist, no direct-run command is authorized.
Historical failures remain noncompliant. Review-access pushing is
not execution permission or banking. P210 remains separate and frozen.
