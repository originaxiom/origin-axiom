The second independent review is preserved against `fca1ce32c` in
`review/INDEPENDENT_REPAIR_FOLLOWUP_2026_11_05.md`, with its hash receipt.
It accepts the R1/R2 source repairs and the added R3 coverage, while finding
two blocking implementation defects. The blocked source and its review
remain in their original commits. All thirteen methods are still unrun.

F1 concerned the source-binding probe's metric. The old E,F,H coordinate
basis has positive trace Gram diag(1,1,2). The probe now constructs that
Gram and uses S=diag(1,1,sqrt(2)) as a metric isometry. Both Lie operators
and all four source/target slots are transported by S. Ordinary matrix
adjoint then agrees with the compact source adjoint. A rejecting control
retains the explicit disagreement in the original coordinates. The actual
orthonormal E8 summand representations require no changed adjoint.

F2 concerned the reuse of one variable for two different norms. The actual
E8 coefficient projection now retains `coefficient_norm`, and the radial
bump integral has `bump_norm`. Charge uses the former. Profile normalization
uses the latter. An explicit unequal-norm control makes their distinction
visible. This repairs the expression that would have divided charge by
the bump integral.

These are author corrections following source review. No scientific test
failure or pass has been generated. A V3 review inventory pins the current
source and both prior reviews. Exact non-authoring follow-up, complete
runtime/infrastructure closure, main acceptance and strict prospective
admission remain required before execution. No physical or mathematical
conclusion is promoted by these code corrections alone.
