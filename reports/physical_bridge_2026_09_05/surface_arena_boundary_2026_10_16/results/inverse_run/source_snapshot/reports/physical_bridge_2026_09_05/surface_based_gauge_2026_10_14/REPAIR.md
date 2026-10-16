# Preserved first attempts and exact-arithmetic repair

Original seal547f35d354968f13ddbe1b1e0236469152f0da0b was committed,
pushed successfully and server-head verified BEFORE both attempts.

`results/first_science`: native exited1 at import,0.056021s. Temporary
dependencies from the preceding work were no longer present. No mathematics
ran. All29 input pins and12,599 tracked files were unchanged. Restore an
isolated runtime: Python3.12.14, SymPy1.14.0, mpmath1.3.0, pytest8.4.0;
bundled NumPy2.3.5. No system/project environment altered.

`results/dependencies_restored`: native ran3.168193s, exited1 with no
stderr. It evaluated the full relations and recorded all phase predicates.
The24 EVEN phase-integrality predicates and136-dimension exhaustion
failed. Inspection found `av**(-j)` with av a Python +/-1: at j=1 it
becomes float. Odd av=+/-SymPy I was exact. `int(value)` then truncated
near-integers in this FAILED diagnostic; those even counts are NOT results.
The run is preserved byte-faithfully, never silently replaced.

The sole mathematical-code repair is to sympify the projector scalar
BEFORE exponentiation. Add a regression requiring exact Integer inverses.
No lift, group word, root, character, criterion, phase grid, gauge invariant
equation, proof or prediction is changed. This is post-result instrument
repair, not an unobserved first run or an altered target.
Updated source hashes are committed and published before the rerun.
The original seal remains recoverable in Git and ARTIFACT_HASHES.txt;
the corrected manifest and REPAIR_HASHES.txt record the current pins.

The actual family matrices are signed quarter-turns, not transpositions.
Do not infer their commutant from the naive permutation picture. No
unbroken algebra name, physical Higgs, chiral spectrum or SM result has
been banked from either failed attempt.
