# B37 — Addendum (2026-10-03, B1463): the self-model predicate could not fire

This arc's step [3] asserts `not any(component.has(I) for component in trace_map)` for a symbol I that never occurs in a
map written in x, y, z. The predicate is False on every such map (B1463, `two_corrections.py::ar3`): it is a test of
literal symbol presence, not of reading, and it could not have failed (MB12; the E82 class). The audit lane's rewriting
T′ = (z, x, 2xz − y + (r − I), r), equal to T on the record graph and preserving it, fires the predicate; a map that
genuinely reads r off the graph changes an orbit. So the conclusion "the trace map never reads κ" is not supported by
this arc's test; what the arc did establish — κ is conserved (step [2]) and the nonlinear term is 2xz − y — stands.
Whether the trace map reads κ in the reads-and-branches sense is GENESIS FK12's question (B20 and B37 are cited there
"in B37's literal sense only"). Found by the audit lane (its ACT_REGISTER AR3), carried by the SM seat (sm:B1521 C2),
re-derived on main in B1463.
