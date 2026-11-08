# Architecture wrapper design, before implementation

2026-11-08. Software binding only. Reuse the unchanged strict/custody
runner in `word_architecture_audit_2026_10_17/verification_v3/run_checks.py`,
whose SHA256 is
`1cc1c9e299be3f85df41d066b2673c2c62b33e83ad978603f769cf04fd8adbf0`.
The previously sealed producer, seven-check source and scientific design
at `7e0159033` must remain unchanged.

The new entrypoint is in this directory. It will locate the old runner
relative to the physical-bridge root, check its bytes before import,
then bind HERE, ENTRY and the exact seven class/method identifiers to
the unchanged runner. The old runner's own actual ROOT is retained;
this directory is deeper than the earlier wrapper's directory. A tiny
`checks.py` bridge will expose only RegisterArchitectureControls from
the sealed test source. It is imported by the old runner only AFTER
actual strict admission and custody checks. The local producer remains
the sole non-stdlib scientific import.

The specification will pin actual scientific input proofs, design,
producer, check source, bridge, wrapper, environment and the reused
gate/checker source closure. The runtime has no third-party mathematical
dependency. Exact commands and new output paths are declared. A manifest
is not evidence that admission, tests or independent review succeeded.

Before relying on this binding, eight future synthetic software fixtures
must exercise the actual wrapper and bridge text in temporary layouts:

1. Correct relative path, exact seven identifiers and exactly one delegate
   import/call, including the correct repository-relative entrypoint.
2. Changed runner bytes reject before delegated import/output.
3. Missing runner rejects without substituting a runner or science.
4. Nonzero delegated exit is preserved.
5. A delegated exception is preserved.
6. Static AST population equals the literal expected list; missing, extra
   and duplicate method identifiers reject without importing science.
7. A generated sentinel test source exposes exactly the required class
   and seven methods through the bridge, without exporting another class.
8. Missing declared class rejects; no substitute empty class is created.

These fixtures will import only generated sentinel modules. They will
not import production gates, the real scientific producer or real checks.
Their implementation and results, if any, must be sealed separately and
reported as engineering evidence. No fixture has been written or run at
the time of this design. Reuse of the previous wrapper pattern or its
past engineering results does not establish these eight outcomes.

The new proof about unitary families is outside this mathematical packet.
No test for it may be silently appended to the seven-check population.
Scientific execution still requires completed independent nonauthoring
review, main's exact separate acceptance, and strict admission from a
clean isolated checkout. No ADMISSION or author-written acceptance is
created by this work. Inherited staged work stays untouched.
