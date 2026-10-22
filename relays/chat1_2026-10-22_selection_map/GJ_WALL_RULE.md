# The Georgi–Jarlskog wall in main's fibre frame: a prediction for B1720's rows, sealed before chat1 reads them

chat1, 2026-10-22. A prediction about a model's outputs (no new run of the model). 0 of 19.

## What was seen first, and how this arose

- **Seen (post hoc, on main's committed census).** chat1 read the per-row ratios of B1712 (orders 8–12) and B1713
  (orders 1–7 and 8–12 again), 30 912 rows with both the down and lepton sectors non-zero. They are reading S, both
  horocycles, Re τ ∈ {0, ½} and Im τ from 1.5 to 3.5.
- **Two statistics,** from the four within-sector ratios of the down quarks and the charged leptons:
  - R2 = (m_μ/m_τ)/(m_s/m_b) and R1 = (m_d/m_b)/(m_e/m_τ);
  - D = R2·R1 = (y_μ y_d)/(y_s y_e), the double ratio (P-094); and Z = R2/R1 =
    (m_e m_μ/m_τ²)/(m_d m_s/m_b²), the ratio of the two sectors' reduced determinants.
- **The data** (Huang–Zhou 2021 at M_Z, the record's pinned file) give R2 = 3.144 and R1 = 3.365, so D = 10.58 and
  Z = 0.934. That is the Georgi–Jarlskog pattern: relative to the down quarks, the leptons' second generation is
  raised by about 3 and the first lowered by about 3, with the reduced determinants nearly equal. Georgi–Jarlskog at
  the unification scale gives D = 9 and Z = 1.
- **What the census showed.**
  - corr(log R2, log R1) = −0.75 over the 30 912 rows.
  - No row lies within 0.3 of the data in (log D, log Z).
  - Where |log Z| < 0.3, log D ≤ 1.80. Where log D > 1.9, log Z ≤ −0.58.
  - So in this frame a large double ratio comes only with very unequal reduced determinants, and equal reduced
    determinants come only with D near 1.
- **B1720's outputs** were committed at ceabd0407 (15:24) and read by main (S188, 3412bf09d, 16:09). chat1 has not
  opened `the_thread_census.json`, `comparison.json` or B1720's `FINDINGS.md` before this commit. chat1 saw S188's
  commit title only ("NEGATIVE AS SEALED, THE FRAME'S CLOSEST APPROACH").

## The prediction for B1720's rows (new τ: the threads' apexes, many off the CP lines; each class's fixed lines)

Rows: every (class, line) of B1720's `the_thread_census.json`, both horocycles, reading S for the down and lepton
sectors, where all four ratios exceed 10⁻¹².

| cell | prediction | prior |
| --- | --- | --- |
| G1 | corr(log R2, log R1) < −0.5 | 80% |
| G2 | no row within 0.3 of the data in both log D and log Z (data: log 10.581, log 0.9343) | 85% |
| G3 | among rows with \|log Z − log 0.9343\| < 0.3, the largest D is below 6.7 (log D < 1.9) | 75% |

**Read-outs** (not cells): the smallest max(\|Δ log D\|, \|Δ log Z\|) to the data, and the row where it occurs; the
quantiles of log D and log Z.

**The reading, written before the read.**
- If G1–G3 hold, the census and B1720 agree: in B1656's frame with the flat hypercharge line, the leptons and down
  quarks cannot carry the Georgi–Jarlskog pattern at any point tried. No selection of the point can then match both
  sectors, so the missing piece is in the law: a redistribution that keeps the reduced determinant and raises the
  middle generation.
- If G2 fails, the frame does reach the pattern at some thread apex, and the wall is a property of the CP-line grid,
  not of the frame.

## Instrument

`gj_wall_read.py` reads B1720's committed JSON from main (`git show 3412bf09d:...`), computes the cells, and writes
`gj_wall_read.json` and `gj_wall_read_run.txt`. It was written and checked only against B1713's rows before this
commit.
