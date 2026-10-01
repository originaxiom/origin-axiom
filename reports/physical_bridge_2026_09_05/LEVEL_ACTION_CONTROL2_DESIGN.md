# R69 canonical cocycle-equality control

October 1, 2026, after the separately sealed rank repair at 684b8035.
Its first native result has 42/43 controls true. Its combined run has
32 passes and eight failures: six original converter failures and two
control-file failures associated with cocycle_relations. Preserve both
producers, all tests and both outputs unchanged.

The raw jac*coc structural equality is false, even though the exact
representations satisfy the relators and every independently computed
index, affine/Fox map and boundary identity passes. Hypothesis: the raw
product is an unexpanded algebraic zero, not a non-cocycle. No result
of a new canonical-zero diagnostic is presumed to have run.

The new instrument changes only this Boolean equality to equality after
exact expansion. All original index values, matrices, characters and
other checks stay unchanged. Three additional safeguards retain the
previous false raw equality, test zero by exact rank, and add a basis
vector in a known nonzero column of jac: that perturbed vector must
fail the cocycle equation. This tests the same mathematical criterion,
not a weaker requirement or a selected target index.

46 fixed controls are expected if the hypothesis holds. If any fails,
preserve and diagnose it rather than claiming full acceptance. Commit,
push and server-confirm these three new paths before import/execution.
Run the new native and the previous six-file selection plus the new
eight-test file. Expected population 48: 40 pass and the same eight
failure IDs retained, if the new controls pass. No old failure is erased.

The original scope and physics fences remain. Success is a selected
exact coefficient verification and conditional action connection,
not a derivation of physical generations, a chosen level or end law.
