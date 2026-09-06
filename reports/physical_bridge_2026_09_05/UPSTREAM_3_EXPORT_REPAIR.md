# Post-result export repair — scientific instrument unchanged

BANKED IDENTITY / P0: the third upstream audit was sealed at f3696b21.
All assertions in analyze() completed, including the fetched B1259 selftest,
before main() failed while writing its JSON. The old float producer uses
NumPy int64 keys in its census. JSON rejects those keys. The retained partial
g2_isolation_first_run.json is NOT valid JSON and is not a successful run.

The original seven tests were then run unchanged: six passed, one failed
at the explicit JSON round-trip. Its captured output is preserved in
G2_ISOLATION_FIRST_TESTS.txt. This is an instrument defect, not a physical
negative. The original source, tests and failed artifact remain untouched.

Before rerun, add a separate wrapper that recursively converts NumPy scalar
keys/values to their native Python types. Reject unsupported types rather
than dropping data or converting arbitrary objects to strings. Serialize
the whole result before opening an exclusive new output path. Test nested
integer-key conversion, the retained original failure, full result round-trip
with every exact census intact, and rejection of unsupported/nonfinite data.

P5/P6: hash and commit this design, wrapper and tests before execution.
Expected outcome is successful export with no changed mathematical output.
New result path g2_isolation_rerun_1.json; no overwrite. This is not a repair
of B1259's physical inference, and no new physics calculation is introduced.
