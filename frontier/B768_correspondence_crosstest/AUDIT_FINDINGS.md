# AUDIT FINDINGS — B768: the correspondence cross-test

cc3 audit seat, 2026-07-23. Branch `audit/b768-correspondence`. Gate 5-Q.

## Verdict: CONFIRMED

No issues found in the mathematical or logical layer.

## Checks performed

| check | verdict |
|---|---|
| V1: transition matrix T stochastic, eigenvalues {1, -1/phi} | CONFIRMED |
| V2: Fibonacci word bb-exclusion, transition frequencies match T | CONFIRMED |
| V3: E20 flag on subdominant = hearing amplitude | CONFIRMED — properly applied |
| V4: gamma3 == c scope (5 discrete axes, continuous untested) | CONFIRMED — scope correct |
| Side A: all 9 signatures point to real banked objects with real test locks | CONFIRMED |
| Discriminator gate logic (rows 3 and 7) | CONFIRMED — both sound |
| F3 kill chain (theta/Agency killed by own falsifier) | CONFIRMED — pre-declared, independently caught, propagated |
| F1 assessment (gamma5 UNDECIDED, strengthened) | CONFIRMED — correctly scoped |

## Key observations

1. **The E20 flag is correctly applied.** V3 (subdominant = -1/phi = hearing amplitude)
   is a numerical identity between two golden quantities. Without a mechanism linking
   the Fibonacci word's Markov spectrum to the weld's theta-odd trace, this is H-class
   (recorded, not structural). cc's discipline here is exactly right.

2. **The F3 kill is clean.** The falsifier was pre-declared by the courier, the
   Haggard-Tsakiris over-read was caught independently in receipt #2, and the
   Synofzik line confirms graded FoA in receipt #3. The kill propagates correctly
   to C7 (the uniqueness tiebreaker), which is now dead three ways.

3. **The V4 scope statement is honest.** gamma3 == c on all 5 discrete axes; the
   continuous axes (T2/T5/T8) are explicitly noted as untested. This matches our
   B766 audit finding exactly.

4. **The discriminator gates are logically sound.** A candidate must HOST the
   transparency surprise (fiber_dim=0) and the time=basepoint identity ((1-phi)^2 =
   phi^-2), not merely accommodate them. The assignment passes both because its
   readings are BUILT ON these identities, not fitted around them.

## Artifacts

- `audit_compute.py` — independent re-derivation (8 checks)
- `audit_output.txt` — full output
- `tests/test_b768_audit.py` — 13 tests, all passing
