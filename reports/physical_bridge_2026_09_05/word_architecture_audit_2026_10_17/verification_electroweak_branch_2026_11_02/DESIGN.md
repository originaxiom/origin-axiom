# Exact stationary-branch controls: pre-implementation design

November 2, 2026. AFTER the author's hand derivation, BEFORE creating,
importing, collecting or executing its new checks.py. This is verification
of an authored claim, not a prospective discovery or permission to execute.

## Quantifier, prior and decision

Finite exact controls for the new order-three stationary branch in the
old curved E8 spin-parent. The author expects all eight named methods
below to pass. Every method must run exactly once with no skips, xfails,
interruption or hidden population. A failed identity/control is preserved
and halts its claim; corrected code is sealed separately before a rerun.

The controls cannot establish the global spin/bundle/domain hypotheses,
physical fermion spectrum, quantum stability, state selection or genesis
identification. A finite pass is not the full physical goal.

## Inputs and conventions

Use the actual old action, same principal H/E, positive root trace norm
one and the faithful D5 subalgebra on E8 coordinates4,...,8. The new proof
EXACT_ORDER_THREE_ELECTROWEAK_BRANCH.md states its explicit 10-by-10
matrix realization, with kappa=(1/2)Tr10. The source ordered bundle-five
coordinate list is (6,4,7,5,8); do not silently replace it by (4,...,8).
Its raising coefficients are2,sqrt6,sqrt6,2. Adjoint means Hermitian
adjoint with that stated positive metric. No empirical targets are read.

The proposed runtime is CPython3.12.1 with SymPy1.14.0, mpmath1.3.0,
PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1, SYMPY_GROUND_TYPES=python,
and optimization disabled. It is a proposal, not a revalidated runtime.

## Eight intended methods of ElectroweakBranchChecks

1. `test_actual_D5_roots_and_E8_embedding`: reconstruct the standard
   E8 root set and the40 D5 roots on the last five coordinates. Verify
   inclusion, closure when a sum is a root, literal four-root grades,
   hypercharge/weak/EM charges and all distinct-root differences.
   The wrong unpermuted grade order must fail a known raising-root test.
2. `test_compact_ten_matrix_metric_and_principal_triple`: reconstruct
   H5,E5,F5,J5 and their10-by-10 D5 matrices. Check orthogonal-form
   preservation, actual adjoints, all triple brackets and the root/trace
   normalization. A missing lower negative transpose must fail.
3. `test_highest_doublets_and_actual_involution`: reconstruct the unit
   bivector Z, its two skew blocks and the Chevalley/J map. Check both
   R vectors have norm one, opposite charges, grade1, neutral EM action,
   and are exchanged by the involution fixing E,H,E-dagger. Omitting
   either component of Z must fail its highest-vector condition.
4. `test_moment_closure_in_roots_and_matrices`: derive H/10 independently
   from the four-root Cartan sum and the faithful matrices; check all
   cross terms and [E,Y0]=0. A one-doublet control must leave a nonzero
   charge moment and cannot have the same H/10 Cartan vector.
5. `test_second_triple_gram_and_independent_flavour_direction`: G=sqrt10Y0
   gives a second triple with the SAME H, norm20 and orthogonality to E.
   Check the two-field Gram determinant and its invariance under an
   explicit compact conjugation and nontrivial unitary flavour rotation.
   Substituting G=E must collapse that determinant to zero.
6. `test_complete_scaled_vacuum_and_backreaction_control`: for symbolic
   a,b or a normalized t chart verify both commuting/grade equations
   and the full moment. Use an explicit nonzero point as a positive
   control. Leaving Q unscaled must fail there. This checks all internal
   residual algebra, not a new PDE or a full nonlinear function-space norm.
7. `test_radius_norm_balance_and_nonzero_domain_comparators`: restore
   ell in F,qhat,rhat and derive zero moment, total norm5/ell^2 and the
   Gram determinant25|ab|^2/ell^4. A wrong one-power radius in a Higgs
   must fail. Finite-area/cutoff and derivative bounds remain analytical,
   not certified by these finite expressions.
8. `test_actual_SM_neutral_stabilizer_and_three_broken_directions`:
   start from the actual S(U3 x U2) Lie block in defining-five matrices,
   impose BOTH neutral fundamental/dual fixed-vector equations and
   recover dimension9 with the explicit U3 embedding. Check the EM
   generator, the two charged and one neutral broken directions and
   positive Higgs mass quadratic form on their span. Removing the Higgs
   must restore dimension12; do not infer the full E8 global gauge group
   or its component count from these finite five-dimensional checks.

## Verification and execution boundary

Commit this design before creating checks.py. Static AST/source metadata
inspection is allowed after implementation. No scientific import,
collection or execution is authorized. Do not use P210's acceptance or
the sixteen-control inventory as admission of this new package.

Complete source/input/test/environment closure, wrapper engineering
verification, genuinely independent proof/code review, main's separate
acceptance and strict prospective admission on a clean quiescent checkout
remain necessary. No direct runnable entrypoint or new output namespace
is provided here. Historical failures and prior seals stay unchanged.
