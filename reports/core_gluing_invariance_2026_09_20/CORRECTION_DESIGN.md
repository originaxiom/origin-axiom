# F07 post-failure verification repair

This design is AFTER the first run and the diagnostic in FIRST_RUN.md.
It is frozen BEFORE executing test_verify_v2.py. No scientific prediction,
producer, proof, original test or original seal is overwritten.

The adjoint identity failed a structural SymPy equality on an unsimplified
exact complex product. Replace that comparison with entrywise exact expanded
residual equality, and do the same for the metric self-adjointness identity.
There is no floating tolerance, changed metric or changed differential.

The new file must:

1. Rerun all sixteen unaffected original test cases, explicitly enumerated,
   including all four parameterized form degrees.
2. Check the repaired adjoint identity and every originally unreached
   assertion: changed adjoint, actual metric self-adjointness, changed
   Laplacian, predicted polynomial and nonzero determinant.
3. Assert coverage of every original test function.
4. Isolate the original unsimplified scalar cancellation and show that a
   genuinely incorrect adjoint gives a nonzero expanded residual. Thus the
   repair can still fail and is not an always-true comparison.

Expected: eighteen corrected checks pass. If not, retain the next failure
without editing sealed source. The global analysis and gluing statement
remain authored proofs, not certified by these finite controls.
