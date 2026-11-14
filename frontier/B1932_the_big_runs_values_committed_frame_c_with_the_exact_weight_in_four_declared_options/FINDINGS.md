# B1932 — The big run's values, committed before any comparison: frame C with the exact weight, in four declared options

**Verdict: OPEN** (the values are computed once by main and committed; the independent second computations are owed
before the run, agy-002's A2-CANON and agy-exp's X-CANON). Main, 2026-11-14 night, for the run the author set for
2026-11-15. Register rows P-845 and P-848 [corrected 2026-11-14 (B1937): P-850, the big run's row; P-848 is Review 82's opening]. **No value is compared with any measured number here.** 0 of 19.


## Seen first

- **Swept:** `VERDICT topic-sweep /exact horoball norm|Theorem 90|channel weight|truncat|big run|values committed/: 22 of 1673 arcs on main match (NEGATIVE 4, OPEN 4, PROVED 13, RETRACTED 1); 10 register rows match (DONE 6, QUEUED 4)` — B1838 (the exact end; Theorem 90 banked in its note), B1839 and B1841 (the six re-read), B1735 (the precision bar, P-341). None computed the read-out on the whole with the exact weight, and no value of it was committed before.
- **The literature:** the exact horoball norm's expansion is the agy lane's Theorem 90 (banked in B1838's note); the statistic and its calibration are the record's own precedent (P-341, B1720's compare.py, B1735); no outside source computes this read-out.

## The values
- **The file:** `verification/BIG_RUN_VALUES.json`, sha256 `df1c9bee002ecf5eeb7f1f360e497a5c091bf092cdbaa499352ea3201d02b536`.
- **What they are:** frame C's seven outputs (up m₂/m₃ and m₁/m₃, down m₂/m₃ and m₁/m₃, ∣V₁₂∣, ∣V₂₃∣, ∣V₁₃∣).
  - The read-out on the whole (B1928, proved twice), with the canonical end, the horocycle of length 2 (B1927).
  - **The exact channel weight** (below).
- **The four declared options:** the Higgs world W₋ (up S̃, down S, leptons S; the record's practice) or W₊, by the
  move-count measure (a) or the area measure (b).
- **Errors:** (a) jackknife sampling over 3 000 words, about 1e-3; (b) the end above Im τ = 6, bracketed two ways, at
  most 5.4e-3.

## Found before the seal: the channel weight's truncation moved the values
- **The weight frame C used** was √(2πL₂ + c_s), the leading form of the channel kernel's norm outside the horoball.
- **Against the exact horoball norm** (B1667's cell, the frame's twisted kernel), at 8 points from Im τ 0.9 to 3:
  - the norms differ by 0.14 % to 0.33 % in median;
  - yet four of the seven averaged outputs move by about 1 % in ln, up to 1.6 % (`truncation.py`).
- **Theorem 90's leading form,** N = 2πL₂ + c_s − π∣a₀∣²e^{−2L₂}, matches the exact norm to about 1e-5. The seven
  outputs then agree to 3e-5 (`t90.py`). It is the weight from now on.
- **On the read-out,** paired on the same 3 000 words (`ergodic_t90.py`):
  - up m₁/m₃ −0.81 %, down m₁/m₃ −1.15 %, ∣V₁₂∣ −0.68 %, ∣V₁₃∣ −0.65 %;
  - the other three under 0.07 %;
  - each shift 5 to 11 times the read-out's own sampling error.
- **A note on the scripts' geometry:** reached by long Newton walks, it gives L₂ below B1667's committed values at low
  Im τ (at τ = i, 2.603 and 2.697 against 2.7193). The comparisons above are at each run's own L₂, and the correction
  enters through e^{−2L₂} only. The grid run uses B1667's committed ends.

## The measures, and the Higgs world, are inputs that move the values
- **The area measure (b)** weights the cusp by 1/height, where the averaged frame keeps changing. The move count (a)
  makes cusp excursions exponentially rare.
- **The two measures differ** by 0.10 to 0.58 in ln on the seven values.
- **The two Higgs worlds** differ by 4 to 400 errors (P-847).
- **In frame C the Higgs bit is a genuine input,** on three computations:
  - main's mirror test (`pairs/higgs_pair.py`);
  - agy-exp's X-SCAR;
  - main's run of the web seat's W-F16 test (`dc_run.txt`: 3.06 in log; control 6e-14).
- **The hand does not reach the seven values:** the averaged frame is mirror-symmetric to 8e-11 (`pairs/q2_run.txt`).

## The comparison, sealed beside the values
- **The rule:** `verification/BIG_RUN_RULE.md`, every element from the record's binding precedent (P-341; B1720's
  compare.py).
- **The script:** `verification/big_run_look.py`, sha256 `2c5f67741235f97b45de3a265e2b42ebbc8c17750b57bf32ab20abd9da541219`. It carries the values' sha256 and refuses any other
  values file.
- **Its dry run** on synthetic data passes matching data, fails mismatched data and refuses a wrong hash (the lock).
- **Order:** the second computations are compared with the committed values before the run; the run's output is
  committed before it is read.

## Not claimed
No value is compared, and no statement about nature is made. The leptons and J's sign are outside the seven. The
remaining declared joints of frame C stay inputs (the author's direction of 2026-11-14: settle what moves the values
first, the inputs later).
