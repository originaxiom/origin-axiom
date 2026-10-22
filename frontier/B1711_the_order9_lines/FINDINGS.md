# B1711 — W59'S ORDER-9 LINES AT THE BAND τ (P-256): NEGATIVE AS SEALED — THE RECORD'S EIGHTEEN ORDER-9 LINES SPLIT ALL THREE SECTORS, BUT WITH THE END-DATA HIGGS THE BEST POINT IS A FACTOR 4.17 OFF (AT THE GRID'S EDGE), AND 9.8% OF RANDOM HIERARCHIES FIT AS WELL

**Verdict: NEGATIVE as sealed (H1, H2, H3 fail).** cc (main), 2026-10-22. Sealed `6fee45181` (sha256 8b1c45f4) before
its instruments ran; the outputs committed unread at `2d78304d7` and read once. A test of a structure, not a value
derived. 0 of 19.
- **The model (no data).** W59's eighteen order-9 lines (B1656's LINES18; by B1703 each splits all three charged sectors
  and protects the leptons' first generation at leading order), the end-data Higgs ∂R, B1667's canonical end, Re τ ∈
  {0, ½}, Im τ = 1.5–3.5: one continuous number, 216 discrete choices.
- **Against the data** (Huang–Zhou 2021 at M_Z):
  - **H1 FAILS** — the best worst factor is **4.17** (the line (7/9, 7/9) and its conjugate (2/9, 2/9), Re τ = 0,
    **Im τ = 3.5, the grid's upper edge**, L₂). There the model over the measured is up 1.29, 2.41; down 0.25, 0.57; leptons 0.34, 4.17 (m₂/m₃, m₁/m₃): the
    down quarks' and the leptons' second-to-third ratios come out three to four times too small, and the electron, protected
    at leading order, is lifted at the canonical end to four times its measured ratio.
  - **H2 FAILS** — 9.8% of random hierarchies fit as well (median 22.5).
  - **H3 FAILS** — minimum χ² 321.
  - Per line: the (·, 7/9)-type lines are the best (4.17–4.25); others miss by 6–16.
- **What it means.** With B1698 (the tick's order-5 lines, best 2.33 but d = e), the record's selected lines — the tick's
  and W59's — both fail in this frame: the one degenerates d and e, the other splits them but not to the data's
  pattern and with the electron lifted too far. The best point sits at the grid's edge, disclosed and not extended: there the
  down quarks' and the leptons' m₂/m₃ are already 0.25 and 0.34 of the measured, and every sector's m₂/m₃ falls as Im τ
  grows (B1691's exponent ½), so a larger Im τ moves them further away — a reading from the law, not computed beyond 3.5.
- **What it does not do.** The other order-9 lines (72 of exact order 9), other Higgs sections, β's role.

## Seen first

`VERDICT topic-sweep /order.?9 lines?|lines? of order 9|eighteen lines|W59's (eighteen )?lines|LINES18/ (full text): 14 of 1482 arcs on main match (NEGATIVE 3, PROVED 11)` —
B1656 and B1660 (W59's lines at ω, with a free Higgs and a fitted end: B1660 NEGATIVE), B1668, B1673, B1684 (W59 on main),
B1686 (the potential's state is not W59's lines), B1692, B1693, B1695, B1703 (the census). None tests these lines with the
end-data Higgs at the band τ. **Literature:** none beyond the cited arcs.

(As sealed; copied from `PREREGISTRATION.md`.)

## Disclosed

- **Known before the seal.** The six measured ratios; B1694–B1702's results (B1698's best 2.33 on order-5 lines; the
  up quarks' floor 0.0134 at Im τ = 2, B1702); B1703's laws (order 9 splits all three and protects the leptons).
- **Model values on order-9 lines exist on main, unread:** B1703's census JSON holds (m₂/m₃, m₁/m₃) for every line of
  order ≤ 16 at τ = 0.31 + 2.4 i and 0.13 + 1.9 i (and 0.41 + 2.9 i), at L_max, with the same Higgs. Main read only its
  coincidence and protection flags, never the ratios; those τ are off this test's CP lines.
- The instruments were import-tested before the seal (no computation). B1660 tested these lines at ω with a free Higgs;
  this test fixes the Higgs and frees Im τ.

## Files

- `PREREGISTRATION.md` (sealed), `ARTIFACT_HASHES.txt`; `verification/the_order9_lines.py` → `the_order9_lines.json`,
  `the_order9_lines_run.txt`; `verification/compare.py` → `comparison.json`, `compare_run.txt`; `verification/b1656_funcs.py`.
- The lock: `tests/test_b1711_the_order9_lines.py`.
