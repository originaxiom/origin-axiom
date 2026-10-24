# Fixture path expectation repair

The first six-fixture run at source fa31bb1a2 exited 1: five passed,
the binding expectation failed because it compared a lexical macOS
temporary path with the wrapper's correctly resolved path. The full
failure precedes this repair in commit 5d40ba4fa. The raw local capture
SHA256 is 952b4589d0cf823e49474f4e07034f87ee1fbf90fb7c1bb991fd85d817cf189a;
its committed presentation normalizes private path strings only.

The fixture now resolves its synthetic root before constructing expected
paths, matching the production wrapper. No check is dropped, no acceptance
criterion is relaxed, and the six declared cases are unchanged. This is
a post-first-run software-fixture correction. The wrapper, frozen v3
runner and scientific check sources remain byte-identical. A new run
must be retained separately; the original failure is not overwritten.
