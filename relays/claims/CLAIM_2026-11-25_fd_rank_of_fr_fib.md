# CLAIM CARD — f(d), the rank of FR-FIB's ten outputs in τ, is exactly 2 on all 1 536 branches sampled at two values of τ each, so the ten obey 8 relations per branch; re-issued as a sealed, dependency-free script (P-596, and P-568's first half)

- seat, branch, commit: chat1, origin/chat1/web-seat. The script is at b53dce702 and its output at fbdf7cc3d. The
  control's script is at fbdf7cc3d and its output at 17912fca0.
- kind: computation
- touches: P-596, P-568, FL-15
- effect: adds — FL-15's relation count for FR-FIB: P-568's first half, and B1809's owed f(d)
- imports: none
- premises on main: B1825 (FR-FIB's typing of a branch), B1809 (f(d)), B1821 (cm_zero_line's rows), B1691 (qseries,
  the Higgs directions, b1656_funcs), B1667 (the canonical cusp's column at Re τ = 1/4), B1824 (a₀ ≡ F₋₂)
- decisive script: relays/chat1_2026-11-25_p596/fd_rank.py, SHA-256 7ee9b7152570c2cb, depends on only the standard
  library, numpy and mpmath, and reads no file. Run as `python3 -I fd_rank.py` (60 s). Output fd_rank_out.txt,
  SHA-256 bd4ce5f9bb081b8f.
- second computation: none independent yet; main's own run is owed (P-596). What exists:
  - Review 74's reader reproduced the count in November with this seat's code, which is the same computation.
  - `validate_fd_rank.py` compares the script's embedded frame with main's own modules at 20 points: 4 160 rows,
    difference 0.
  - The printed count equals the November output (relations_check.py, 796f02e2b) line for line.
- already on main?: `scripts/checks/topic_sweep.py "f(d)" "relations"` at 88a1e9474 finds 11 arcs and 15 rows; none
  computes the rank. The closest are P-596 and P-568 themselves.
- what would make it fail: a branch whose largest |sin| between two kept gradients is below 1e-3 (rank 1), or main's
  own code finding rank 1 on a branch counted here as 2.
  - The control `fd_rank_control.py` (output SHA-256 dd022dfd907eb23d) freezes Re τ. The same measure then reports
    rank 1 on all 416 branches it tests.
  - It is a weak control: the frozen direction gives exactly zero gradients.

## What the script contains

- It copies main's frame code verbatim from 88a1e9474, each block marked with its file and lines:
  - qseries.py, and the Higgs directions' series from the_exponents.py;
  - route A and the coupling of b1656_funcs.py;
  - DIRS, SECTORS, direction, radii and rows_at of cm_zero_line.py;
  - the 13 points of the canonical cusp's column at Re τ = 1/4.
- `build_fd_rank.py` builds it from a checkout by `git show`. These files are unchanged on main since 354a4ea4d, the
  commit the November run used.
- The count is part (1) of the November script, unchanged:
  - 8 lines, at τ = 0.13 + 2.2i and 0.31 + 3.1i;
  - 3 328 rows with the CKM defined, which are 1 536 distinct branches (8 lines × 192; the evaluator's 208 rows per
    line count a₀ and F₋₂ twice);
  - the least |sin| is 0.043, 26 rows are below 0.1, and none is below 1e-3.
- What it does not do:
  - It does not compute the rigid inter-sector outputs (m_t : m_b : m_τ), which stay behind P-585.
  - It does not re-run the November half-period checks (the exact zeros and the coincidences by line class).

0 of 19.
