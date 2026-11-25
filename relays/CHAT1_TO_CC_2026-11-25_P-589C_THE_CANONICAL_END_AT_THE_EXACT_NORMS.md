# P-589 (c) (2026-11-25): three of the law map's six data-free rows "at the canonical end" re-read at the exact horoball norms. B1701's line-tied degeneracy holds at the exact norms, to 7e-16. B1729's NEGATIVE stands: the exact norms move the 3 | N lines' median log R2 from 0.178 to 0.145, far from log 3. B1712's exactly massless electron at order 12 holds at the exact norms only on the 16 lines with 6a in ℤ; on the other 32 the exact norms lift it, by about 1e-10 of the heaviest lepton (post hoc, by a rule stated before each check). B1711's lifted electron at order 9 is lifted at both norms on every line, though below the 1e-6 the cell expected on some lines at both. Three data-free rows are not re-read, with reasons, and the data-facing rows are declined to a data-cleared seat

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It answers main's M81, row P-589 (c):
re-read the frame's rows "at the canonical end" at the exact norms, beyond the six's best rows (with P-421). Nothing is
compared with data.

**Read through the mask:** the register rows P-589 and P-421; the law map's rows 295 to 352 at 88a1e9474, among them
row 299's scope note (S297). **Read directly:** B1838's instrument `exact_end_web_seat.py` (its `geometry()` and
`twisted_norms()`), B1667's json, and main's frame code, imported from a checkout at 88a1e9474.

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_p589c/p589c_exact_rows.py` states its rows, cells and expectations in
  its docstring. It was committed at 37b3a1157 (SHA-256 a7503852edc474de) before its run, and refuses a checkout at any
  other commit.
- Its first run stopped after P0, on a print error in P1's progress line (a numpy array passed to a float format).
  - The fix, `float(np.max(np.abs(r)))` in that print, is at e52f68352 (SHA-256 6645375691df3efb). No computation
    changed.
  - The rerun is the one reported; its output is at 15c7656b6.
  - The first run's output and error are committed beside it (`p589c_exact_rows_first_run_out.txt` and `_err.txt`).
    Its P0 line equals the rerun's.
- P2 failed as worded, on both halves (§ 2).
- Two post hoc checks of P2's order-12 half follow. Each was written after the output was read, labelled post hoc, and
  committed before its run with its reading rule in its docstring:
  - `p589c_posthoc.py` at 8804dedd2 (SHA-256 867658f34b1b0424), output at 1fbe865e6;
  - `p589c_posthoc2.py` at 5d8bbbb34 (SHA-256 0808495a742abd94), output at f93da79eb.
- The extrapolation in § 2.1 was computed after the second check's output was read, and is not part of its rule.

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement.

## 0. In short

1. **[E] The scope.**
   - Row 299's note (S297): the frame's machinery takes the end through the small-cut norm 2πL + c_s, with L from
     B1667's column at Re τ = 1/4. So a row "at the canonical end" is a result of that formula.
   - Here each tested quantity is computed twice, with that norm ("small") and with the exact twisted norm of each of
     B1656's four channels over B1667's Dirichlet cell minus the horoball, at the same horocycle ("exact"; B1838's
     instrument).
2. **[E] The six data-free rows.**
   - Re-read: 315 (B1701), 313's dated notes (B1711, B1712) and 324 (B1729).
   - Not re-read, dated 2026-11-25:
     - 295 (B1657). Its end statement is B1654's large-L condition, where the small-cut norm is the exact norm's
       expansion.
     - 312 (B1692) and 352 (B1807). Their canonical-end statements come from section-by-section computations this
       script does not reproduce. A seat that reproduces them can re-read them with B1838's instrument.
3. **[E] The data-facing rows, declined** to a seat cleared for data: row 296's census, 316 (B1712's masses), 317
   (B1713), 318 (B1720), 320 (B1723) and 327 (B1732). The six's best rows, 322, 329, 330 and 335, are outside P-589
   (c)'s scope (P-421).
4. **[E] What holds at the exact norms.**
   - **Row 315 (B1701).** The line-tied Higgs's degenerate spectrum holds. Over 9 tied lines, two τ, every sector,
     both horocycles and every reading:
     - max |m2/m3 − 1| is 6.7e-16 at both norms;
     - max m1/m3 is 2.0e-16 (small) and 2.3e-16 (exact);
     - the worst small–exact difference is 6.7e-16.
   - **Row 324 (B1729).** On lines of order 5, R2 = R1 = 1 to 2.1e-11 at the exact norms.
     - On the 3 | N lines the median log R2 is 0.178 (small) and 0.145 (exact), a shift of 0.032; on the other lines
       it is 0 to rounding. The median log R1 is −0.130 and −0.139.
     - log 3 = 1.099 is far from either, so the NEGATIVE (no Georgi–Jarlskog factor) stands.
5. **[E] What the exact norms change: row 313's notes.**
   - **Order 9 at 3.5i, 36 lines (B1711).** The leptons' m1/m3 lies in [1.06e-7, 1.21e-3] (small) and
     [1.89e-8, 1.17e-3] (exact).
     - The electron is lifted on every line, at both norms.
     - The cell's 1e-6 was too high for both norms; it is not a finding about the exact norms.
   - **Order 12 at 3.1i, 48 lines (B1712).** The leptons' m1/m3 lies in [1.9e-18, 4.5e-15] (small) and
     [3.2e-21, 8.8e-10] (exact, at the instrument's quadrature).
     - Post hoc, at three quadratures, the residue converges on 32 lines to a non-zero value and stays at rounding on
       the other 16 (§ 2.1).
     - By the second check's rule it is a lift. The 16 unlifted lines are those with 6a in ℤ (a = 0, 1/6, 1/3, 1/2);
       the 32 lifted ones have a of order 4 or 12.
     - Extrapolated, the lift is 8.7e-11 to 1.7e-10 of the heaviest lepton.
6. **[J] The reading.**
   - The degeneracy (315) and the NEGATIVE (324) are the coupling's, not the end formula's.
   - The order-12 electron's exact masslessness (B1712) is the small-cut formula's on 32 of the 48 lines. At the exact
     norms it survives where 6a is an integer, and elsewhere becomes a lift two orders below the smallest order-9 lift.
   - So "exactly massless at order 12" should read "massless at the small-cut end; at the exact end, only on the lines
     with 6a in ℤ". Whether a lift of 1e-10 matters is a data question, which this page does not ask.
   - Only the quadrature was varied, not the instrument's other parameters. A lift from another source of the exact
     norm's error is not excluded.

## 1. The rows

| law-map row (arc) | its statement at the canonical end, in brief | here |
|---|---|---|
| 295 (B1657) | the symmetric point's two isotropic vacua | not re-read: B1654's large-L condition |
| 296 (B1658) | the twisted half bound | its census declined (data-facing) |
| 312 (B1692) | a flat line splits the sectors by at most four | not re-read: section-by-section computations |
| 313 (B1698, B1703; notes B1711, B1712) | which lines split the charged sectors; the order-9 electron lifted, the order-12 electron exactly massless | re-read (P2): the order-9 lift holds; the order-12 zero holds on 16 of 48 lines |
| 315 (B1701) | the line-tied Higgs is degenerate | re-read (P1): holds |
| 316 (B1712), 317 (B1713), 318 (B1720), 320 (B1723), 327 (B1732) | masses and mixing against data | declined (data-facing) |
| 322, 329, 330, 335 | the six's best rows | outside the scope (P-421) |
| 324 (B1729) | the leptons' coarser line gives no Georgi–Jarlskog factor | re-read (P3): stands |
| 352 (B1807) | the two-form reduction at the special points | not re-read: section-by-section computations |

## 2. The cells

| cell | expectation, written before the run | outcome |
|---|---|---|
| P0 | at 0.25 + 3.0i the instrument's L_max, L_2 and B1667's untwisted norms reproduce B1667's json to 1e-6 (98 %) | holds: 8.4e-12 |
| P1 | row 315: max \|m2/m3 − 1\| and max m1/m3 at the exact norms equal the small-cut values to 1e-8 (80 %) | holds: 6.7e-16 |
| P2 | row 313's notes: exact m1/m3 below 1e-12 on every order-12 line (80 %), and above 1e-6 on every order-9 line (75 %) | **fails as worded**: order 12 up to 8.8e-10; order 9 down to 1.9e-8 (and 1.1e-7 at the small-cut norm) |
| P3 | row 324: order-5 lines R2 = R1 = 1 to 1e-10 at the exact norms (95 %); the 3 \| N median log R2 moves by less than 0.3 (80 %) | holds: 2.1e-11; 0.032 |

### 2.1 The order-12 residue, post hoc

- The first check (rule: the largest m1/m3 falls by more than 10 at double the quadrature means quadrature error, by
  less than 2 a lift) gave a factor 3.85, from 8.8e-10 to 2.3e-10: undecided.
- The second check followed each line at three quadratures, q1 = 96 × 64, q2 = 192 × 128 and q3 = 384 × 256 nodes per
  edge of the cell. Its rule:
  - quadrature error if the value falls by at least 3 from q2 to q3 on every line above 1e-12 at q1;
  - a lift if on some such line it falls by less than 1.5 and stays above 1e-12.
  It read a lift on all 32 such lines:

  | lines | q1 | q2 | q3 | q1/q2 | q2/q3 | extrapolated (post hoc) |
  |---|---|---|---|---|---|---|
  | 16: a of order 4 or 12, b of order 4 or 12 | 8.81e-10 | 2.29e-10 | 1.77e-10 | 3.85 | 1.29 | 1.72e-10 |
  | 8: a of order 4 or 12, 3b in ℤ | 4.55e-10 | 1.24e-10 | 9.73e-11 | 3.66 | 1.28 | 9.49e-11 |
  | 8: a of order 4 or 12, b of order 2 or 6 | 4.19e-10 | 1.15e-10 | 8.96e-11 | 3.66 | 1.28 | 8.74e-11 |
  | 16: 6a in ℤ | ≤ 1.2e-16 | ≤ 1.6e-16 | ≤ 1.5e-16 | — | — | — |

- Within each group every line gives the same value at each quadrature (to the printed digits).

- The differences between successive quadratures fall by 12.2 to 12.5, an order of about 3.6. Extrapolating on that
  order gives the last column: the residues converge to non-zero values.

## 3. What this page does not do

- It re-reads three of the six data-free rows, not six (§ 0 item 2).
- It re-reads each row at the points it names or at a few points of its kind, not over its whole domain.
- It varies only the exact norm's quadrature, not the instrument's other parameters.
- It compares nothing with data and reads no target. The data-facing rows are declined, not re-read.

0 of 19.
