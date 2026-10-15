# Dependency launch failure, not a failed mathematical assertion

The unchanged nine-file regression command exited1 in1.013707s before
pytest could start. Stdout0 bytes; stderr111 bytes records that the
Python executable has no pytest module. The temporary dependency target
used before the turn interruption no longer exists. The current
Python version was independently checked as3.12.14; neither sympy nor
pytest is globally installed there. No new test assertion ran.

Both snapshots match:19 scientific input pins,12,877 tracked files and
index unchanged. The before snapshot completed before child launch.
Complete stdout/stderr, snapshots and receipt remain byte-faithful.

The symbolic runtime will be restored with sympy1.14.0 and mpmath1.3.0
in a persistent isolated workspace target, together with pinned
pytest8.4.0. Actual transitive versions will be recorded. The science
producer's Python/Sympy versions and every mathematical source, proof,
criterion and test stay unchanged. The previous temporary pytest patch
version was not archived, so an exact test-framework patch-version
reproduction is NOT claimed. The same test selection will run into a
separate regression_restored capture; this directory is not overwritten.
