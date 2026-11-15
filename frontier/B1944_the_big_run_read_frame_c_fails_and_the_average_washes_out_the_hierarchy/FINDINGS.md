# B1944 — The big run, read: frame C fails, in every option, and the average over the whole surface washes out the hierarchy

**Verdict: NEGATIVE** (as sealed; computed once, PROVISIONAL until its second computation, the SM seat's SM-C15, re-runs
the three scripts on the pinned files, P-842). Main, 2026-11-15, the run the author set (P-850). By the rule's own terms
(amendment A1), this is a reading of frame C, not the programme's final comparison. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /big run|precision bar|P-341|coarse cell|second computation of the values|rule amended/: 2 of 1678 arcs on main match (OPEN 1, PROVED 1); 4 register rows match (DONE 4)`,
  at B1937. This arc is the look those arcs prepared.
- **The record's earlier looks:** docs/LOOK_LEDGER.md (A9). This run's row is entered there.
- **The literature:** the statistic is the record's own (P-341, B1720, B1735), and the data are the pinned running
  masses at M_Z and the PDG mixing moduli. No outside result predicts frame C's values, so none is cited for them.

## How the look was made
- **When:** after every condition of the rule was met:
  - all four options recomputed independently (X-EXACT-W for the move count, X-MEASURE for the area);
  - the S* exclusion's second computation (W-F22), with its premise written in (A14);
  - two cold reads of the rule (W-F21, W-F23);
  - the look's second computation sealed (SM-C15);
  - the full suite green on a fresh clone (8 923 passed).
- **What ran,** in the rule's order on 2a4d98d43: B1940's `big_run_look_v3.py` (governing), `big_run_windows_v3.py`, and
  B1932's `big_run_look.py` (version 1, reported).
- **The outputs** were committed and pushed before anyone read them (a3d54c621):

  | output | sha256 |
  |---|---|
  | version 3 | 0441eb5c… |
  | the window companion | 952f3fc4… |
  | version 1 | 667ff85f… |

- **How they are read here.** `verification/read_the_look.py` reads only those three files, checks their hashes, and
  uses the data's σ only to express rows as factors. It fits nothing.

## The outcome (`verification/read_the_look_run.txt`)

| option | χ²₇ (bar 22.0) | worst claimed row, as a factor (bar 3) | χ²_six (P-341, reported) | χ²_nine |
|---|---|---|---|---|
| W₋∣a (move count) | 7 476.6 | 7 529.5 | 7 888.3 | 10 042.0 |
| W₋∣b (area) | 6 921.2 | 4 894.6 | 6 418.7 | 8 935.2 |
| W₊∣a (move count) | 7 292.1 | 5 307.9 | 7 297.2 | 9 588.4 |
| W₊∣b (area) | 6 678.9 | 3 314.5 | 5 790.6 | 8 412.0 |

- **The governing outcome is FAIL.** No option passes, and there is no pattern match.
  - The calibrations: 22 % of random targets are fitted as well on χ²₇, and 61 % on the worst factor (the bar is
    under 1 %).
  - The window companion gives 16 % to 25 %.
  - **Version 1 also gives FAIL:** best χ²₇ 6 703.6, calibration 21 %.
- **Frame over measured,** row by row:

  | option | c/t | u/t | s/b | d/b | ∣V_us∣ | ∣V_cb∣ | ∣V_ub∣ |
  |---|---|---|---|---|---|---|---|
  | W₋∣a | 101 | 7 530 | 18.8 | 33.9 | 1.06 | 18.0 | 43.6 |
  | W₋∣b | 63.3 | 4 890 | 11.4 | 21.9 | 1.47 | 16.6 | 73.1 |
  | W₊∣a | 97.3 | 5 310 | 18.6 | 25.4 | 0.89 | 18.8 | 50.8 |
  | W₊∣b | 59.3 | 3 310 | 11.3 | 15.6 | 1.21 | 17.6 | 80.9 |

  The reported lepton rows, frame C's copy of the down rows, are 3.6 to 6.0 (μ/τ) and 53 to 114 (e/τ).

## What the wall teaches
- **The read-out on the whole has no hierarchy steep enough.** Every ratio of frame C's average is too large: from
  about 10 times (s/b) to thousands of times (u/t). The mixing ∣V_cb∣ and ∣V_ub∣ are too large by similar orders.
- **The average is dominated by the bulk of the surface.**
  - Frame C's pointwise ratios fall steeply up the cusp (B1940's table, no data): up m₂/m₃ goes from 0.0089 at
    height 6 to 0.0014 at height 9, and m₁/m₃ from 2e-7 to 2e-11.
  - But the move count and the area alike give most of their weight to the bulk, where the ratios are of order 0.01 to
    1.
- **So the step that removed τ as an input (B1928's average, the same at every point) also removed the hierarchy.**
- **What it points to:** a read-out that gives the cusp its weight by a principle, or a localized one. *[CORRECTED 2026-11-15, B1945 § 4: for this family that is not open ground. The single lines' cusp limits fail W178's skeleton test (harvest row 1497), and the best single τ on the order-5 lines fails (B1698). What survives is structural: at order 5 the leptons copy the down quarks, and P-845's fork of the level is how the frame separates them. The one untested cusp pattern is the averaged one (B1945 § 3; P-859).]* Finding where
  the pointwise ratios meet the measured ones would be a post-hoc look. It is not done here, and nothing in frame C is
  adjusted after this look.
- **∣V_us∣ is the one row near its value in every option** (0.89 to 1.47). The calibration says a pattern this good is
  generic, so it is not evidence.
- **The Higgs world and the measure change the values** by tens of percent. That is nothing against these factors, so
  neither choice rescues the frame.

## Not claimed
- That frame C is the programme's answer, or its final comparison (A1).
- Any re-fit, any τ, and any weight chosen after the look.
- That every read-out on the whole fails: this is the one frame C defines.
