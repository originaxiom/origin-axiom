# B1913 — The flat area is not on the curve: the read-out's measure is forced, and the one ingredient left is the reading of the mark (P-776's condition R6)

**Verdict: PROVED** (the flat density is shown not to be a function on the curve, and its greatest place to depend on the
chart; the invariant density's place does not). cc (main), 2026-11-13 (S306p). Main's own code, with B1885's construction of
the state imported. No data; no value of the modulus on record is read, and no point is compared with any. **0 of 19.**

## 1. The answer first

- **What R6 asks:** the read-out on the whole (P-776) must give a place that survives its chosen ingredients. The record had it
  not met: the greatest place of the golden state's density moves 0.056 when the density is taken against the chart's flat
  area instead of the hyperbolic one (B1885, P-776's row).
- **Main's reading, written before the run:** an ingredient of a read-out on the whole must be defined on the curve, that is,
  unchanged by the group. The hyperbolic area is the only invariant area up to scale, and against it the state's density is
  |f|², a function on the curve. The flat density |f|²/y² changes by |cz + d|⁴ under a move, so it is not a function on the
  curve, and its greatest place depends on which chart of the curve is drawn.
- **What the run shows:**
  - |f|² is unchanged by two moves of Γ₀(5) (ratio 1.0 for (1, 0, 5, 1) and (2, −1, 5, −2)); |f|²/y² changes by exactly
    |cz + d|⁴ (78.1456 and 21.5296 at the point tried).
  - The greatest place of |f|², found in the standard chart and in the chart moved by (1, 0, 5, 1), is the same point,
    B1885's z\* (distance 0).
  - The greatest place of |f|²/y² is (0.2562, 0.3141) in the standard chart and (0.3149, 0.3430) when found in the moved
    chart and carried back: two different points of the curve, 0.065 apart. The first is the 0.056 shift on record.
- **So the measure is not an ingredient to choose:** invariance forces it, and the flat area is excluded because it is not on
  the curve. A monotone function of |f|² has the same greatest place, so the density's power is not an ingredient either.
- **What R6 still holds open:** which curve. The record counts the greatest place as one mirror pair on the line's surface
  and two pairs on the one-twin surface (P-776); that is the reading of the mark, an admissible ingredient that does change
  the outcome, and it waits on how the ruling on the tick and the ruling on even ticks stand together (P-771, P-769).

## 1a. Seen first

`VERDICT topic-sweep /flat area|Euclidean area|R6|survives its chosen|admissible ingredient/: 32 of 1652 arcs on main match
(NEGATIVE 1, OPEN 2, PROVED 29); 23 register rows match (DECLINED 1, DONE 18, QUEUED 4)`. B1885 (the state and the 0.056
shift), B1912 (the state is the lowest twin-odd state, and simple), P-776 (the eight conditions; R6's record), B1881 (main's
criterion for an outcome of the whole). **Literature:** the invariant area of the hyperbolic plane is y⁻² dx dy, unique up
to scale under PSL₂(ℝ); standard.

## 2. The check (`verification/the_flat_area_is_not_on_the_curve.py`, mpmath at 20 digits, 900 terms)

| | result |
|---|---|
| \|f\|² at z and at γz, two moves | ratio 1.0, 1.0 |
| \|f\|²/y² at z and at γz | ratio 78.1456, 21.5296 = \|cz + d\|⁴ |
| the greatest place of \|f\|², standard chart and moved chart carried back | the same point, (0.2515397781, 0.3697671434) |
| the greatest place of \|f\|²/y², the same two ways | (0.2562, 0.3141) and (0.3149, 0.3430), 0.065 apart |

## 3. What is not shown

- That R6 is met as a whole: the reading of the mark is left, as said.
- The other seven conditions are not re-examined here; R3 is B1912's.

## Files

- `verification/the_flat_area_is_not_on_the_curve.py` → `.json`, `_run.txt`.
- The lock: `verification/test_b1913_the_flat_area.py`.

## Reproduce

```
cd frontier/B1913_the_flat_area_is_not_on_the_curve_the_measure_is_forced/verification && python3 -B the_flat_area_is_not_on_the_curve.py
```

## Dated correction, 2026-11-13 (main's own, found the same day)

§ 1's last bullet said the reading of the mark "waits on how the ruling on the tick and the ruling on even ticks stand
together (P-771, P-769)". That relation is not open: the owner ruled the relation on 2026-11-11, with B1879's computation in hand (P-771; GENESIS v1.65, GM5c and SE2): every tick is in the ledger, and 'only even ticks are observed' is no longer a ruling but a condition the weight must deliver, a named condition to derive, not counted as derived. With every tick a move, B1881's case is in force (the
mark's mirror is a move of the group that keeps the line). What remains of R6 is therefore not a ruling to wait for: it
is the weight's condition, the same one that types the orientation bit, and it is not counted as derived. The words
above are kept as written.
