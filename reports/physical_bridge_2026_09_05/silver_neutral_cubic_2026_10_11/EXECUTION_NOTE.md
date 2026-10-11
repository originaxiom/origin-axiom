# Execution custody and replay scope

Science/design/proof/test seal: e4564d4c323d0568ce54a7a179d11fbab279f88b.
Source pin:0e5ab0c054bea0136e19eedc6b7d403cfcd2b58c.
Python3.12.1 and SymPy1.14.0 were verified before imports.
Native and reference first executions exited0 with23 and11 predicates.
Their complete JSON stdout was retained before the interruption.

An original selected51-test launch was in flight across continuation.
Its process and tool handle were absent on resumption; its terminal
output/exit status was not recovered. Five progress dots are not a
pass certificate. No status is inferred from the process ending.

The identical six test files were therefore replayed on the unchanged
seal after31 source/seal hashes, byte counts and committed bytes passed.
The tree remained read-only until replay terminal exit0. Complete stdout
was accumulated from tool chunks, with an external task-owned custody
copy to prevent another interrupted-turn loss. The final result is
51 passed in330.25s, preserved in REGRESSION_FINAL.log.

Selected files:
tests/test_physical_bridge_silver_neutral_cubic.py
tests/test_physical_bridge_silver_interaction_radical.py
tests/test_physical_bridge_silver_charged_cubic.py
tests/test_physical_bridge_silver_selective_boundary.py
tests/test_physical_bridge_silver_framed_coupled_domains.py
tests/test_physical_bridge_silver_fermion_action.py

This is a focused regression, not the full repository or slow suite.
Both exact methods are authored by the same seat; analytic independence
and global Hilbert/PDE acceptance are not thereby discharged.
