# R26 first broad-regression capture loss

The 47-file expanded regression was launched after the complete native
and 56-test focused successes. Its first returned session was 46055,
with no stdout at that first yield. On continuation the session handle
was unknown and no pytest/index-stability/gate process was present in
the process table. The orchestration stores were also unavailable.
No terminal exit code or completed output is recovered for that run.
It is not counted as green, failed mathematically, or a complete suite.

The scientific producer, proof, design and tests remain unchanged from
seal 46b34c09. A replacement expanded run uses the SAME 46 filenames
listed in BOUNDARY_WALL_REGRESSION.txt, plus the new index-stability test,
with -q -p no:randomly --tb=short and the established Python 3.12.1
environment. It is explicitly a REPEAT after a stopped/missing process,
not resumption of a live process and not recovery of its first output.

The replacement's complete raw output and terminal receipt are written
exclusively under the supplied temp001 directory as
`oa_r26_broad_retry.log` and `.json`. An existing target causes failure,
not overwrite. The capture helper flushes output while the command runs;
only a successful terminal receipt can establish its exit status.
Public reporting will redact environment path prefixes, not failures.
