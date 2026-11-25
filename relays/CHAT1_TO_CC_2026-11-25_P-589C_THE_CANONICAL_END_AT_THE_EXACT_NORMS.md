# P-589 (c) (2026-11-25): four of the law map's data-free rows "at the canonical end" re-read at the exact horoball norms, and all four hold. B1701's line-tied degeneracy holds to 7e-16. B1729's NEGATIVE stands: the 3 | N lines' median log R2 moves from 0.178 to 0.145, far from log 3. B1712's exactly massless order-12 electron (rows 313 and 316) holds on all 48 lines, to 2.5e-16, once B1667's accessory parameter is on its uniformising branch at Re τ = 0 (post hoc). The committed run used a stuck accessory parameter there, so its order-12 "lift" of 1e-10, first reported here, was an artefact and is retracted. B1711's order-9 electron is lifted on every line at both norms, though below the 1e-6 the cell expected on some lines. Rows 295, 311, 312 and 352 are not re-read, with reasons, and the data-facing parts are declined to a data-cleared seat

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It answers main's M81, row P-589 (c):
re-read the frame's rows "at the canonical end" at the exact norms, beyond the six's best rows (with P-421). Nothing is
compared with data.

**Read through the mask:** the register rows P-589 and P-421; the law map's rows 293 to 352 at 88a1e9474, among them
row 299's scope note (S297) and its S305j note. **Read directly:** B1838's instrument `exact_end_web_seat.py` (its
`geometry()` and `twisted_norms()`), B1667's code and json, B1726's `census.py`, and main's frame code, imported from a
checkout at 88a1e9474.

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_p589c/p589c_exact_rows.py` states its rows, cells and expectations in
  its docstring. It was committed at 37b3a1157 (SHA-256 a7503852edc474de) before its run, and refuses a checkout at any
  other commit.
- Its first run stopped after P0, on a print error in P1's progress line (a numpy array passed to a float format).
  - The fix, `float(np.max(np.abs(r)))` in that print, is at e52f68352 (SHA-256 6645375691df3efb). No computation
    changed.
  - The rerun is the one reported; its output is at 15c7656b6.
  - The first run's output and error are committed beside it. Its P0 line equals the rerun's.
  - The error file carried machine paths. They were reduced to file names at e6edaa735 (SHA-256 0d6f40d857ee45b4
    before, bd561f418ab4383c after); the earlier version stays in the history.
- P2 failed as worded, on both halves (§ 2).
- **The instrument's fault, found by the referee read.** On Re τ = 0, B1667's `track()` and `solve_accessory()` do not
  fix the accessory parameter c. The realness conditions (Im tr A_a = Im tr A_b = 0) hold there for every real c, so c
  stayed where it entered that line: 8.19e-4 at 1.6i, 3.1i and 3.5i alike.
  - At 3.1i that gave L_max = 4508 and L_2 = 9.535, against B1667's column's 0.6466 and 2.334.
  - The L_max horoball's radius then sat at the bisection floor, about 1e-12, where the theta sums lose digits.
  - So P1's 1.6i half and both halves of P2 were computed at a wrong geometry. P0 (at 0.25 + 3.0i) could not see this:
    B1667's grid starts at Re τ = 0.05, and B1838's rows avoid Re τ = 0.
  - This seat confirmed the stuck value and the uniformising one (c = 0.665 tracked to 0.01 + 3.1i) before writing the
    third check.
- **Three post hoc checks follow.** Each was written after the output it answers was read, labelled post hoc, and
  committed before its run with its reading rule in its docstring:
  - `p589c_posthoc.py` at 8804dedd2 (SHA-256 867658f34b1b0424), output at 1fbe865e6;
  - `p589c_posthoc2.py` at 5d8bbbb34 (SHA-256 0808495a742abd94), output at f93da79eb;
  - `p589c_posthoc3.py` at 3ef6819ba, one code line rewrapped at 41e0fcbd2 (SHA-256 6bd69d2bbcc3f6f5), output at
    34396fbbe. It was written after the referee read, which had already probed the corrected geometry; its rule was
    fixed before its own run.
- The first two post hoc checks measured how the artefact responds to quadrature refinement. Their output is kept as a
  record (§ 2.1). The extrapolation in their table was computed after the second check's output was read, and three
  points fit any geometric error model exactly, so it was no test of convergence.

**Typing.** [E] means established on record, by a run here, or by the referee where it says so. [J] means this seat's
judgement.

## 0. In short

1. **[E] The scope.**
   - Row 299's note (S297): the frame's machinery takes the end through the small-cut norm 2πL + c_s at these heights,
     so a row "at the canonical end" is a result of that formula. B1726's `compute()` reads L from B1667's column at
     Re τ = 1/4.
   - Here each tested quantity is computed twice:
     - "small", with that norm;
     - "exact", with the exact twisted norm of each of B1656's four channels over B1667's Dirichlet cell minus the
       horoball, at the horocycles B1667's geometry gives at τ (B1838's instrument).
   - The two horocycles agree with the column's to 2e-3 where the accessory parameter is uniformising. At Re τ = 0 that
     needs the third check's c* (§ 2.2).
2. **[E] The data-free rows.**
   - Re-read:
     - 315 (B1701);
     - 313's dated notes (B1711, B1712);
     - row 316's zero clause (B1712), whose paired channels with equal norms are exactly what the exact norms test;
     - 324 (B1729).
   - Not re-read, dated 2026-11-25:
     - 295 (B1657). Its end statement is under B1654's canonical end condition, the small-cut formula at free L; row
       293's note gives the large-L reading.
     - 312 (B1692). Its canonical-end statement is S167's spread note, over the four sections it tested, which this
       script does not reproduce. Its B1693 part is data-facing.
     - 311 (B1691) and 352 (B1807). Their canonical-end statements come from section-by-section computations this
       script does not reproduce. 352's points near i lie on Re τ = 0, so a re-read must take the accessory parameter on
       its uniformising branch there.
   - A seat that reproduces them can re-read them with B1838's instrument.
3. **[E] The data-facing rows, declined** to a seat cleared for data:
   - 296 (B1658): no canonical-end statement (it leaves the end's joint law open); its comparison with the scoreboard
     ratios is data-facing;
   - 316's line census against data;
   - 317 (B1713), 318 (B1720), 320 (B1723) and 327 (B1732).
   - The six's best rows, 322, 329, 330 and 335, are outside P-589 (c)'s scope (P-421).
4. **[E] What holds at the exact norms.**
   - **Row 315 (B1701).** The line-tied Higgs's degenerate spectrum holds. Over 9 tied lines at 0.5 + 2.4i and 1.6i,
     every sector and both horocycles:
     - the readings were S, S̃ and conj S for up, and S alone for down and leptons (the docstring's S̃ for those was not
       run);
     - max |m2/m3 − 1| is 6.7e-16 at both norms, and max m1/m3 is 2.0e-16 (small) and 2.3e-16 (exact);
     - the worst small–exact difference is 6.7e-16;
     - the 1.6i half, rerun at the uniformising accessory parameter (Q1), gives 4.4e-16, 1.5e-16 and 4.4e-16.
   - **Row 324 (B1729).** On lines of order 5, R2 = R1 = 1 to 2.1e-11 at the exact norms.
     - On the 3 | N lines the median log R2 is 0.178 (small) and 0.145 (exact), a shift of 0.032. The median log R1 is
       −0.130 and −0.139, the same at both norms, within B1729's spread by order.
     - On the other lines the pooled median is 0, because order 5's lines are identically 1 and hold the median. Per
       the referee, B1729's json gives log R2 −0.001 and 0.036, and log R1 0.027 and −0.114, at orders 10 and 13.
     - log 3 = 1.099 is far from either, so the NEGATIVE (no Georgi–Jarlskog factor) stands.
   - **Rows 313 and 316 (B1712): the order-12 electron, at 3.1i, 48 lines, both horocycles, readings S and S̃.** At the
     uniformising accessory parameter (Q2) the leptons' m1/m3 lies in [1.0e-20, 2.5e-16] (exact) and [1.9e-18, 4.5e-15]
     (small). The zero holds at the exact norms on every line.
   - **Row 313 (B1711): the order-9 electron, at 3.5i, 36 lines.** At the uniformising accessory parameter the leptons'
     m1/m3 lies in [1.05e-7, 1.21e-3] (exact) and [1.06e-7, 1.21e-3] (small). The electron is lifted on every line, at
     both norms alike. The cell's 1e-6 was too high for both; that is not a finding about the exact norms.
5. **[E] The retraction.** This page's first version reported that the exact norms lift the order-12 electron on 32 of
   48 lines by about 1e-10. That was the stuck accessory parameter's artefact:
   - the third check's control (Q0) reproduces the committed 8.814e-10 at the stuck c;
   - at the uniformising c the residue is at rounding on all 48 lines;
   - per the referee, at the stuck geometry the residue sat on the L_max horocycle alone, and moving its inner radius
     from 1e-12 to 1e-9 and then 1e-6 shrank it to 1.2e-12 and then 2.1e-15, the signature of rounding;
   - the "6a in ℤ" pattern was the artefact's.
6. **[J] The reading.**
   - The degeneracy (315), the NEGATIVE (324) and the order-12 zero (313, 316) are the coupling's, not the end
     formula's: each holds at the exact norms.
   - For main, beyond this page: B1667's `track()` and `solve_accessory()` do not determine c on Re τ = 0. Any re-read
     near τ = i with B1838's instrument, row 352's included, must take c by continuity from Re τ > 0.

## 1. The rows

| law-map row (arc) | its statement at the canonical end, in brief | here |
|---|---|---|
| 295 (B1657) | the symmetric point's two isotropic vacua | not re-read: B1654's canonical end condition |
| 296 (B1658) | the twisted half bound, under equal framed data | no canonical-end statement (left open); its scoreboard comparison declined (data-facing) |
| 311 (B1691) | the exponents at the two fixed points; a note at the canonical radius | not re-read: section-by-section computations |
| 312 (B1692) | a flat line splits the sectors by at most four | not re-read: S167's spread note over its four sections; its B1693 part data-facing |
| 313 (B1698, B1703; notes B1711, B1712) | which lines split the charged sectors; the order-9 electron lifted, the order-12 electron exactly massless | re-read (P2, Q2): both hold |
| 315 (B1701) | the line-tied Higgs is degenerate | re-read (P1, Q1): holds |
| 316 (B1712) | the electron exactly massless at order 12; a line census against data | the zero re-read with 313's note (holds); the census declined (data-facing) |
| 317 (B1713), 318 (B1720), 320 (B1723), 327 (B1732) | masses and mixing against data | declined (data-facing) |
| 322, 329, 330, 335 | the six's best rows | outside the scope (P-421) |
| 324 (B1729) | the leptons' coarser line gives no Georgi–Jarlskog factor | re-read (P3): stands |
| 352 (B1807) | the two-form reduction at the special points | not re-read: section-by-section computations; needs the uniformising c at Re τ = 0 |

## 2. The cells

| cell | expectation, written before the run | outcome |
|---|---|---|
| P0 | at 0.25 + 3.0i the instrument's L_max, L_2 and B1667's untwisted norms reproduce B1667's json to 1e-6 (98 %) | holds: 8.4e-12 |
| P1 | row 315: max \|m2/m3 − 1\| and max m1/m3 at the exact norms equal the small-cut values to 1e-8 (80 %) | holds: 6.7e-16 (its 1.6i half at the stuck accessory parameter; rerun at the uniformising one, Q1, 4.4e-16) |
| P2 | row 313's notes: exact m1/m3 below 1e-12 on every order-12 line (80 %), and above 1e-6 on every order-9 line (75 %) | **fails as worded**, as run at the stuck accessory parameter: order 12 up to 8.8e-10; order 9 down to 1.9e-8 (and 1.1e-7 at the small-cut norm). At the uniformising one (Q2): order 12 at most 2.5e-16 (holds); order 9 down to 1.05e-7 (fails at both norms) |
| P3 | row 324: order-5 lines R2 = R1 = 1 to 1e-10 at the exact norms (95 %); the 3 \| N median log R2 moves by less than 0.3 (80 %) | holds: 2.1e-11; 0.032 |

### 2.1 The first two post hoc checks (a record of the artefact)

- The first check (rule: the largest m1/m3 falls by more than 10 at double the quadrature means quadrature error, by
  less than 2 a lift) gave a factor 3.85, from 8.8e-10 to 2.3e-10: undecided.
- The second followed each line at three quadratures, 96 × 64, 192 × 128 and 384 × 256 nodes per edge of the cell. By
  its rule it read a lift on 32 lines, with values levelling off near 1e-10 (1.77e-10, 9.73e-11 and 8.96e-11 at the
  finest, by group), and the 16 lines with 6a in ℤ at rounding.
- Both ran at the stuck accessory parameter. They tested the quadrature, not the instrument's geometry, and the
  levelling off was the rounding floor of the theta sums near a horoball of radius 1e-12. Their reading is withdrawn.

### 2.2 The third post hoc check: the uniformising accessory parameter

- **The rule for c on Re τ = 0, fixed before the run.** c_ε = solve_accessory(ε + iy, track(ε + iy)) for ε = 0.01,
  0.005 and 0.0025, and c* = Re c_0.0025.

  | τ | c* | spread over ε | L_max (column) | L_2 (column) | smallest margin, L_max and L_2 |
  |---|---|---|---|---|---|
  | 1.6i | 0.401417 | 5.0e-5 | 0.6639 (0.6640) | 2.5152 (2.5170) | 0.0001, 0.42 |
  | 3.1i | 0.665051 | 4.0e-9 | 0.6466 (0.6466) | 2.3334 (2.3337) | 0.0001, 0.40 |
  | 3.5i | 0.692854 | 3.3e-10 | 0.6447 (0.6447) | 2.3121 (2.3121) | 0.0001, 0.40 |

  The L_max horoball is the maximal one: it touches the cell's edge, so its margin is near 0.
- **Q0, the control.** With the stuck c at 3.1i, the largest exact order-12 lepton m1/m3 is 8.814e-10, the committed
  value.
- **Q1.** P1's 1.6i half: max |m2/m3 − 1| 4.4e-16 at both norms, max m1/m3 1.7e-16 (small) and 1.5e-16 (exact), worst
  difference 4.4e-16. Holds.
- **Q2.** Order 12 at 3.1i: exact [1.0e-20, 2.5e-16], small [1.9e-18, 4.5e-15]. Order 9 at 3.5i: exact
  [1.05e-7, 1.21e-3], small [1.06e-7, 1.21e-3].
- **The reading, by the rule.** The order-12 zero holds at the exact norms, the committed residue was the stuck
  accessory parameter's, and the lift is retracted. The order-9 electron is lifted on every line (above 1e-12), though
  not above 1e-6 everywhere. P1's 1.6i half holds.

## 3. What this page does not do

- It re-reads four of the data-free rows (313, 315, 316's zero, 324), not 295, 311, 312 or 352 (§ 0 item 2).
- It re-reads each row at the points it names or at a few points of its kind, not over its whole domain.
- It does not test B1841's principled entry level E4 = L_2 − π/4 (row 299's S305j note), which is not among the
  horocycles here.
- It varies the exact norm's quadrature, not its other parameters, except through the third check's geometry.
- It compares nothing with data and reads no target. The data-facing rows are declined, not re-read.

0 of 19.
