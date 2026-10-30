# P-530's data-free checks (the web seat, 2026-10-30)

Three checks behind § 2 of `relays/CHAT1_TO_CC_2026-10-30_P530_THE_SECTOR_ASSIGNMENT.md`. Each is data-free: it reads no
measured value and computes no fit. Each builds on B1726's committed `compute()` and modules.

- `zero_line_readings.py`: on the zero line (τ = 0.35 + 2.75i, L_max, one shared section, H = I), which of the eight
  readings, at c = 1 and c = 3, split which sectors. c is applied as B1726's `compare.py` applies it.
- `zero_line_tau_scan.py`: at ten values of τ and both horocycles, whether S and S̃ differ on the zero line, and whether
  the three sectors coincide within one reading.
- `per_field_metric.py`: on the zero line (S in every sector, c = 1), whether a per-field generation metric H (B1822)
  splits the sectors.

They were written by the note's two read-only referees and re-run by the seat with identical output before this commit.
The outputs below were produced from these committed copies against main at 37f6ec56a (S271).

Run: `python3 -I <script> <path to a checkout of main>`.
