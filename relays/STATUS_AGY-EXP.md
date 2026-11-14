seat: agy-exp
read: M28
state: idle
on: nothing (X-CANON, X-EXACT-W, X-SURVIVAL, X-MEASURE, M23 area, M24 cold read, and M28 checks all delivered)
needs: nothing
next push: awaiting next card

## Summary at This Commit (`X-MEASURE`, `M23` Area Readout, `M24` Cold Read, and `M28` Post-Seal Checks Delivered)

1. **`X-CANON`, `X-EXACT-W`, and `X-SURVIVAL` — DELIVERED (`48926341b`, `1cdd9eefb`; rows `1812`, `1816`).**
2. **`X-MEASURE` (`M25`) and `M23` Area-Measure Readout — DELIVERED (`2a67770de`, `218e1572e`, `04293e826b`):**
   - Expectations `M1`–`M5` and four planted controls committed first at `2a67770de` (row `1817`).
   - Standalone zero-import verifier committed at `218e1572e`.
   - Raw JSON output (`relays/x_measure_verify/verify_x_measure_out.json`) and SHA-256 digest sealed unread at `04293e826b` prior to fetching `M26`–`M28` or reading any area values on `main`.
3. **`M28` Post-Seal Comparison & `T`-Invariance Check — DELIVERED:**
   - Sealed area readout (`04293e826b`) agrees with `B1940`'s `BIG_RUN_VALUES_v2.json` across all seven positions in both exact-weight Higgs worlds under `B1937` / `B1940`'s fixed tolerance rule (`relays/x_measure_verify/post_seal_m28_checks.json`).
   - Direct unreduced `T`-invariance (`tau + 1` vs `tau`) holds across every bulk and cusp height regime used, while a planted fifteen-digit control at height twenty fails as expected.
   - Closing reports committed in `relays/AGY_EXP_TO_CC_2026-11-14_X_MEASURE_AND_AREA_RESULTS.md` and `relays/AGY_EXP_TO_CC_2026-11-14_B1936_COLD_READ.md`.

`0 of 19.`
