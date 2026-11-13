# B1908 — The tube at k = 3: why the mesher stopped is found, and its value is not resolved at these grids (P-739; R80-9)

**Verdict: OPEN** (the cause of the stop is found exactly and mended; the level-surface modulus at k = 3 is not resolved by
this mesher at the grids tried, so the question of P-739 stays open). cc (main), computed 2026-11-12, landed 2026-11-13
(S306p). No data; a modulus of the object's own level surfaces, compared only with the web seat's sealed computation of the
same modulus. **0 of 19.**

## 1. The answer first

- **The cause of the stop at k = 3.** Both diagnoses on record were wrong: B1854's first (the mesher's lattice condition) and
  its correction at Review 77 (the two unlabelled translation checks). B1847's `fibre_faces.monodromy_from_relators`
  searches integer matrices with p, q, r from −40 to 40. In the presentation's basis the monodromy of b++L⁶R(LR)^k is
  [[−1, −3], [8, 23]] at k = 1, [[15, −28], [−23, 43]] at k = 2, [[109, −71], [−66, 43]] at k = 3, [[−21, 55], [−160, 419]]
  at k = 4 and [[−55, 144], [−419, 1097]] at k = 5, with traces 22, 58, 152, 398 and 1042, the traces of the word's own
  matrix. At k = 3 the entries lie beyond 40, the search finds nothing, and the mesher stops at an assertion that has no
  message.
- **The mend.** `verification/monodromy_exact.py` solves the same equations exactly instead of searching. At k = 1 and 2 it
  gives exactly the matrix the search gives (the control), and at k = 1 the mesher's run with it reproduces the kept run.
  At k = 3 the lattice basis taken from the words is w₁ = μ, w₂ = −λ, as at k = 1: the two translation checks were never the
  cause.
- **Not resolved.** With the solver, the mesher runs to the end at k = 3, but the level surfaces nearest the core are not
  resolved: their determinant is off by 3 to 8 per cent, where it was at most 2 at k = 1 and 2, and refining the grid from
  120 to 160 moves the nearest levels further, not closer. Main's k = 3 value neither confirms nor contradicts the web
  seat's sealed 6.069. Nothing is banked from the values.

## 1a. Seen first

`VERDICT topic-sweep /tube|P-739|level surface|B1854|B1847/: 11 of 1647 arcs on main match (NEGATIVE 1, PROVED 10); 13
register rows match (DONE 4, QUEUED 9)`. What bears on it: B1846 (the metric's read-out, the tube), B1847 (the level
surface's modulus at k = 1, the mesher), B1852 (the real part zero by topology), B1854 (k = 2 on main, k = 3 not reached,
with the two diagnoses this arc corrects). **Literature:** none beyond the arcs; the monodromy of a fibred word is its
matrix up to conjugacy, a standard fact the traces check.

## 2. The values at k = 3 (Im τ of the covariant root at the level s₀ + d; `runs/`, `k3_extrapolation.json`)

*Both columns are computed by one formula in `k3_extrapolation.py`; the run files also print the covariant root, which agrees
to 3 × 10⁻⁴. [Corrected before landing: main's draft of 2026-11-12 had 7.044 at d = +0.0005 on grid 160; the value is
7.0435, which rounds to 7.043.]*

| d | grid 120 | det E − 1 | grid 160 | det E − 1 |
|---|---|---|---|---|
| −0.0020 | 5.687 | −7.3 × 10⁻³ | | |
| −0.0010 | 6.035 | −3.8 × 10⁻² | 5.990 | −5.4 × 10⁻³ |
| −0.0005 | | | 6.356 | −3.1 × 10⁻² |
| +0.0005 | 6.649 | +4.6 × 10⁻² | 7.043 | +6.4 × 10⁻² |
| +0.0010 | 6.994 | −7.5 × 10⁻² | 7.959 | +6.6 × 10⁻² |
| +0.0020 | 5.864 | +2.9 × 10⁻³ | | |
| +0.0050 | 4.666 | −6.2 × 10⁻³ | | |

- B1854's two fits on grid 120 give 6.6940 and 6.6895. A parabola through the three levels with |det E − 1| under 1 per cent
  gives 6.0291, with no residual: three points, three unknowns, so it tests nothing.
- The largest |det E − 1| is 7.5 × 10⁻² here, against 1.0 × 10⁻² in B1854's runs at k = 2 and 2.0 × 10⁻² in B1847's at k = 1.
- **Reading:** the core's |dθ| falls from 0.042 at k = 1 to 0.0195 at k = 3, and the mesher's error near the core grows with
  it. What would settle k = 3: a method whose error at the core does not grow with k, or levels further from the core with a
  fit that uses them, or a third opinion at the seat's resolution, as P-739 allows.

## 3. What this resolves

- **Review 80's item R80-9** (at its fourth carry): its ask, that the stop be diagnosed, is met, and the diagnosis is not the
  one it named. The two diagnoses in B1854 are corrected there by a dated note.
- **P-739 stays open:** the value at k = 3, and with it the seat's limit, is not reproduced on main.

## 4. What is not shown

- That the mesher would converge at a finer grid: grid 160 did not.
- The values of k = 4 and 5 on main: only their monodromies are computed.

## Files

- `verification/monodromy_exact.py` → `monodromy_exact_run.txt`: the exact monodromy at k = 1 to 5, with the search as control
  at k = 1 and 2 (needs SnapPy).
- `verification/stage_e_gamma_k3.py`: B1847's mesher with the basis taken from the words and the exact solver;
  `verification/tube_driver_k3.py` runs it; `runs/` holds the runs at grids 120 and 160 and the k = 1 control
  (`driver_*_run.txt`); `first_k3_runs/` holds the runs before the solver, which stop.
- `verification/k3_extrapolation.py` → `k3_extrapolation.json`: the table and the fits from `runs/`.
- The lock: `verification/test_b1908_the_tube_at_k3.py`.

## Reproduce

```
cd frontier/B1908_the_tube_at_k3_the_stop_found_the_value_not_resolved/verification
python3 -B monodromy_exact.py          # seconds
python3 -B k3_extrapolation.py         # reads runs/
python3 -B tube_driver_k3.py 3 120     # k and the grid; the mesher takes an hour and more per member, setup included
```
