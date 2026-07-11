# B531 — Trace-Map Gate Campaign

## Pre-registration

### What we know (from B530 XXXII–XXXIII)

| entry | status | value |
|---|---|---|
| gap 1 IDS | EXACT | φ/S = 0.272020 |
| gap 2 IDS | EXACT | (φ+1)/S = 0.440137 |
| gap 3 IDS | EXACT | (S−√φ)/S = 0.786151 |
| gap 1 slope | CONVERGED (d7-9) | 0.184 |
| gap 2 slope | CONVERGED (d7-9) | 0.153 |
| gap 3 slope | UNCONVERGED | oscillates 0.12–0.15 |
| slope ratio s1/s2 | CONVERGED (d9) | 1.204 |
| saturation ε=5 | CONVERGED | 1.10, 2.82, 0.71 |

### What T1 will compute

Transfer-matrix Lyapunov exponent γ(E,ε) at depths 8–12 (N up to ~2M).
Gap edges from the γ > 0 regions → gap widths → slopes.

### Pre-registered predictions

- Slopes at depth 10 will match depth 9 eigendecomposition values (0.184, 0.153)
  to 3 digits (cross-validation)
- Gap 3 will either converge to a definite slope or show a power law W ~ ε^α with α > 1

### What T1 CANNOT determine

- Whether the slopes have closed-form expressions (needs T3)
- What's specific to this substitution vs generic (needs T2)
