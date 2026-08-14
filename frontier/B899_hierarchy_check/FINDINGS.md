# B899 — M8: the hierarchy-source check — NO SUPPORT (honest negative, fenced)

**Date:** 2026-08-05 · **Seat:** cc (banking) · **Status:** computed; geometry only, fenced throughout

## The question (M8, registered in masterplan v2)

Do the operational S₃-breaking magnitudes (the sealed cells' per-frame
deviations — the first naturally small invariant numbers) correlate with μ's
root geometry (per-root nearest-spacing; |μ′| at each root), through the
banked frame→root bijection? Stated up front: three data points per
comparison — nothing here could be more than a registered orientation; four
pre-declared comparisons, log-log, no fitting beyond a slope.

## The result: no

| comparison | log-log slope | residual | order match |
|------------|--------------|----------|-------------|
| B890 vacua vs nearest-spacing | 3.65 | 2.74 (large) | **yes** |
| B890 vacua vs \|μ′\| | 2.13 | 5.36 | no |
| B891 matter vs nearest-spacing | −1.43 | 5.23 | no |
| B891 matter vs \|μ′\| | −1.87 | 3.58 | no |

The single order-match is exactly what chance predicts: each 3-point
comparison matches ordering with probability 1/6 under the null, and four
comparisons give ≈ 52% probability of at least one match. The residuals are
large on every comparison (a clean power law on 3 log-points would sit near
0). **Verdict: the leakage/deviation magnitudes are NOT explained by μ's
root spacings or by |μ′| at the roots under the registered comparisons.**
The hierarchy-shaped structure in the invariant small numbers (real —
B889/B896) has some other source; the dual-protocol rule applies (an
unearned negative is as bad as numerology — this one is earned exactly as
far as the four registered comparisons and no farther; other invariants of
the root geometry were not scanned, deliberately, to keep the look-elsewhere
budget honest).

## Files

- `m8_check.py` → `results.json`
- Locks: `tests/test_b899_m8.py`

## Depends on

B866 (μ), B889 (the map), B890/B891 (the magnitudes), B896 (the isotypic
shape of the asymmetry).
