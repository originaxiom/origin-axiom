# W181 — the cusp limits on the integer-λ lines in the exact norms: B1656's frame with only the norms' linear part moved to a separate scale Y, its limit in Im τ at fixed Y, then in Y^{−1/2} (the rule, committed before the script)

The SM-derivation seat, 2026-11-03, at the owner's "resume" (named in relay §338, item 6).
Committed and pushed before the script that reads it exists. Nothing here is a result.

## Why

- **W179 and W180 left the integer-λ lines undetermined** (NOTE, W179 and W180).
  - W179's G0 listed 50 finite cusp pairs on 25 lines not settled by Im τ = 48, all on lines with an integer-λ kernel.
    Main counts 46 pairs on 23 lines beside the two G2 lines (relay §338, item 4).
  - W180 froze each norm at c_s^∞ + B_s Y. Its rest ρ_s falls as e^{−π Im τ} on the λ = ±½ channels and reaches the
    light features, so the frozen frame is not the true frame for the six (H0 failed on all 98 pairs). Every D∞ was
    withheld.
  - On the two G2 lines ρ_s cancels in D. There the frozen D equals the true D at Im τ 64–128 to 10⁻¹³ and falls to
    6.59 at Y = 4096.
  - Main ruled premature, until those pairs are determined, the ask that the factor enter GENESIS's dictionary data
    (FK11). c stays one discrete input (P-488).
- **This arc keeps the exact norms** at the height computed and moves only their linear part B_s Im τ to a scale Y.
  At Y = Im τ the frame is the true frame by construction. It takes the limit in Im τ at fixed Y, then the limit in Y.

## The structure (hand reasoning for this rule; nothing computed)

- **The shifted frame F(y, Y).** This is W178's frame at Im τ = y: its residues, κ, DR, L, coupling and readings, no
  cut, and the θ-zero rule. Each norm is replaced by c_s(y) + B_s (Y − y).
  - c_s(y) is W177's exact series at Im τ = y, and B_s is W180's split coefficient: 4π²/|1 − W_s Q^{−l₀}|² on an
    integer channel, 0 otherwise. So the λ = ±½ channels keep W177's norms exactly.
  - F(y, y) is W178's frame, the true frame.
- **At fixed Y, every piece is a q-series in y.**
  - The residues, κ and DR are q-series, and L is held at its Im τ = 4 value for Im τ ≥ 4.
  - The norms are c_s^∞ + B_s Y + ρ_s(y), where ρ_s is a series in e^{−π Im τ} (W180, post hoc 1).
  - So each of the six is linear in y up to exponentially small terms, with slopes that do not depend on Y for generic
    Y. Where the down and lepton slopes agree, ln D(y, Y) tends to a limit H(Y) as y → ∞.
- **The limit in Y.**
  - The six depend on the weights only through their ratios, since the coupling is linear in M.
  - The integer channels' weights grow as √(B_s Y); the others stay near √1.203.
  - Set u = Y^{−1/2}. Expanding √(g² + ρ) in ρ, H is a ratio of Laurent polynomials in u and √(B_s − 7.507 u²). So
    ln H is analytic in u near 0⁺.
  - ln D∞ = lim_{u→0} ln H(u) is finite when the lowest powers of u cancel between the down and lepton features.
    Otherwise D runs as Y^q, with q a multiple of ½.
- **The interchange.** The true D(y) = F(y, y) = H(y) + R(y), where R(y) is a polynomial in y times an exponentially
  small factor. So lim_{y→∞} D(y) = lim_{Y→∞} H(Y).
- **Against W180.** W180's limit frame set u = 0 inside the frame, which changes the exponents (its H4). Here the
  limit is taken of H(u), not inside the frame.

## The computation (fixed now)

- **Pairs:** the 49 resolved integer-λ lines at Re τ 1/8 and 3/8, 98 pairs, as in W180. None is picked. Three subsets
  are named from W179's record:
  - the **50 unsettled pairs** (G0's list): the 46 of relay §338 and the four on (1/2, 1/5) and (1/2, 3/10);
  - the **12 settled pairs**, all exact ties;
  - the **36 running pairs**.
- **Heights:** y ∈ {48, 64, 96, 128}.
  - The precisions are W178's two at each height plus 40 digits, for the powers of Y. Where a feature is unresolved,
    they are doubled once.
  - The status rule per feature is W178's.
- **The Y ladder:** Y ∈ {48, 64, 96, 128, 256, 1024, 4096, 16384, 65536, 262144} at every height.
  - The frame's pieces are computed once per pair and height; only the weights change with Y.
  - That is 392 tasks and 3920 sets of six, on four workers.
- **The quantities:**
  - the exponents e(Y) = −[f(128, Y) − f(96, Y)]/(2π · 32), per feature;
  - ln r₂, ln r₁ and ln D from the six, as in W179 and W180;
  - **agreeing pairs:** at Y = 1024, the down and lepton exponents of both features in D agree within 10⁻⁶;
  - **the y-limit at Y:** it passes when |ln D(128, Y) − ln D(96, Y)| ≤ 10⁻⁸, with the four features resolved at
    both heights;
  - **the Y-limit:** Neville's polynomial extrapolation of ln D(128, Y) in u = Y^{−1/2} to u = 0, over the six
    Y = 256 … 262144 (u = 1/16 … 1/512), called N₆, and over the top five, called N₅;
  - **D∞ = e^{N₆}**, accepted on an agreeing pair when all six Y pass the y-limit and |N₆ − N₅| ≤ 10⁻⁶;
  - **D's power of Y:** q = [ln D(128, 262144) − ln D(128, 65536)]/ln 4.
- **The data,** read once: D = 10.58 ± 0.11 (P-094's received file, as in W179 and W180).

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| K0 | **The tie.** F(48, 48) agrees with W178's stored six at Im τ 48 within 10⁻⁶ in ln, on every feature resolved in both, on all 98 pairs | 97% |
| K1 | **The truth on the G2 lines.** ln D of F(y, y) at y = 64, 96 and 128 on (1/2, 1/5) and (1/2, 3/10) at Re τ 1/8 equals W179 post hoc 1's within 10⁻⁶ | 95% |
| K2 | **The G2 control.** On the two G2 lines at both Re τ, ln D of F(64, Y) equals W180's frozen ln D at Im τ 64 within 10⁻⁶, for Y = 48, 64, 96, 128, 256, 1024 and 4096 | 90% |
| K3 | **The y-limit.** On every agreeing pair, every Y in the ladder passes the y-limit | 70% |
| K4 | **The Y-limit.** On every agreeing pair, \|N₆ − N₅\| ≤ 10⁻⁶ | 65% |
| K5 | **The class.** The agreeing pairs are exactly W179's 62 finite pairs on integer-λ lines | 85% |
| K6 | **The twelve ties.** On W179's 12 settled integer-λ pairs, \|ln D\| ≤ 10⁻¹² at every height and Y | 85% |
| K7 | **No exact cusp D near the data.** No accepted D∞ lies within 3σ of 10.58, that is in [10.25, 10.91] | 75% |
| K8 | **The G2 lines' limit.** D∞ on (1/2, 1/5) and (1/2, 3/10) at both Re τ is accepted and lies in [6.0, 6.6] | 70% |
| R | **Read-outs** (no predictions): per pair, ln D(y, Y) at every point, the exponents and the y-limit's differences; on agreeing pairs N₆, N₅, D∞ (or the flag), r₂∞, r₁∞ and q; the true D on the diagonal at Im τ 48 (stored), 64, 96 and 128 beside D∞, and the pairs whose diagonal crosses the window; the distinct accepted D∞ to 10⁻⁶ and the ten nearest to the data | — |

## What the outcomes mean (fixed now)

- **K0 or K1 fails:** the instrument is not W178's frame at Y = Im τ. Every D∞ is withheld and the failure recorded.
- **K2 fails** (with K0 and K1 holding): ρ_s does not cancel in D on the G2 lines at every Y. W180's frozen ladder
  beyond Y = 128 is not the truth there, and this arc's values supersede it.
- **K3 fails on a pair:** that pair is not at its y-limit by Im τ 128 at the Y named. If any of the six extrapolation
  Y fails, the pair's D∞ is withheld and flagged, with ln D(128, Y) and q reported.
- **K4 fails on a pair:** the ladder does not resolve the expansion in u, or D runs as a power of Y. The pair's D∞ is
  withheld and flagged, with q reported.
- **K5 fails:** W179's classification misfiled the pairs named. They are corrected here, and W179 gets a dated note.
- **K6 fails:** moving the linear part breaks a tie the true frame keeps. The shift is then not neutral on those
  lines, and that is recorded.
- **K7 holds, with K3 and K4 holding on every agreeing pair:**
  - Every one of W179's 110 finite cusp pairs is determined: the 48 settled off the integer-λ lines, the 12 ties, and
    the 50 here.
  - B1656's frame then gives no finite cusp D within 3σ of the data on any census line.
  - Main's condition (relay §338, item 4) is met. The ask that the factor be a candidate entry for GENESIS's
    dictionary data (FK11) goes to main again, for main to rule. It is not a derivation.
- **K7 fails** (an accepted D∞ within 3σ):
  - It is the record's first exact cusp D near the data, and the line is a thread choice (W140).
  - Its specificity is read from how many distinct D∞ the census produces.
  - It becomes a sealed target for the next arc. Nothing is banked from it here.
- **K8 fails while K2–K4 hold:** the hand extrapolation of W180's frozen ladder was wrong about the limit. The exact
  value is recorded.

## Weave or thread

- **neither (a frame census over every census line with an integer-λ kernel, at the cusp, in the exact norms).** The
  frame is B1656's. The lines are the frame's whole class (a ∈ {0, 1/6, 1/3, 1/2}), none picked. The weave's own
  answer on the split stays W140's, D ≡ 1.

## What stays out

- The other 163 resolved lines, settled in W178 and W179.
- Finite heights and τ = i (W179's Part B).
- Other frames, readings and horocycles; the up sector's factor; the CKM.
- Main's B1814 census, rerun blind only at the owner's word (relay §338, item 5).

## Looks

- One look at the data, counted: K7 and the read-outs read D once. No line is selected for a later fit.

## Seen before the rule (disclosed)

- **W179's and W180's outputs and post hocs, read in recording them:**
  - every count and list;
  - G0's list with each pair's D at Im τ 32 and 48, re-read for this rule:
    - (0, 2/7) and (0, 3/11) lie between 20 and 34, falling;
    - the G2 lines fall from 12.3 to 10.4;
    - the other pairs lie between 0.13 and 4.4;
  - the 12 settled integer-λ pairs, all exact ties at every height;
  - W180's frozen ln D on the G2 lines at Im τ 64, Y = 48 to 4096.
- **A hand extrapolation of W180's recorded values** set K8's box. The values were the frozen ln D on the G2 lines at
  Y = 256, 1024 and 4096. The ratio of successive differences is 0.46, near ½, as for a series in Y^{−1/2}. Two
  Richardson steps give D ≈ 6.3.
- **W179 post hoc 1's timings** (6.5, 17.9 and 47.5 s per point at Im τ 64, 96 and 128) set the plan's cost.
- **Hand reasoning:**
  - the shifted frame;
  - its q-series dependence on y at fixed Y;
  - the analyticity in u;
  - the interchange.
- **Not computed:** no shifted-frame value at any line, height or Y.

## Discipline

- This rule is committed and pushed before the script exists in the tree.
- One run. Its output is committed before it is read. The only checks before that are the exit, failures, NaN, paths
  and warnings.
- Any later check is labelled post hoc.

0 of 19.
