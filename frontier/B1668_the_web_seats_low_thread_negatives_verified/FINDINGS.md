# B1668 — THE WEB SEAT'S LOW-THREAD NEGATIVES, VERIFIED ON MAIN: the twisted units on the low threads (sealed) and the per-field census at every depth reproduce exactly — no assignment of the Standard Model's charges, and none of the nulls, passes the mass test in either reading

**Verdict: NEGATIVE (a verification arc; the tested claim — that some assignment passes S-mass — fails, as the web seat
found).** cc (main), 2026-10-17. POINT_REGISTER P-188. 0 of 19.
- The verification was done by one reading pass for main and re-executed in part. Main's scripts, run logs and report
  are in `verification/`. The web seat's data are not copied into main; they are fetched from its commits.
- **Why:** the paper's §8 open question needed these negatives, and the paper cites arcs only. The web seat's results
  could not be cited until main verified and banked them.

## 0. Seen first

`VERDICT topic-sweep /S-mass|twisted units|low threads|T-low|per-field|thread frame|midheight/: 1 of 1439 arcs on main match (PROVED 1)`
— B1652 (the frame tribunal; it read the web seat's selection report). The web seat's own record:
- THE TWISTED UNITS ON THE LOW THREADS: sealed 0d83e6981, output 09f41b453, read-out fc15550e0 (harvest row 1241);
- the S-shape replication: sealed ec8ba7e87, output 2a4bd10fe (row 1249);
- the per-field census at every depth: 34b2e8061 (row 1250);
- the SM seat's blind check W97.

**Literature:** the mass data are the running masses at M_Z of Huang and Zhou (2021), as the web seat's sealed files
received them. No literature result is used in the verification.

## 1. What was verified

**Result 1: the twisted units on the low threads.** 90 configurations at N = 9, 11, 12. Two readings (per-field,
minimal). 200 assignments: the Standard Model's charges and 199 seeded nulls.

| task | what was run | result |
|---|---|---|
| (a) the seal | the six input hashes recorded in the output against the files at 0d83e6981; the output's xz and decompressed hashes; the stored units file `forms.pkl` rebuilt from its builder (1257 s); the 199 nulls regenerated from seed 20261015 | **PASS:** every hash equal; `forms.pkl` rebuilt byte-identically (sha256 64a40c03…); the nulls regenerated identically, all gauge-invariant, none with a charge ≡ 0 mod N |
| (b) re-execution | six configurations drawn by `random.Random(20261017).sample(range(90), 6)` = [35, 3, 56, 23, 84, 15], run with the unmodified sealed instrument (`repro_driver.py`, `run_repro.sh`) | **PASS, bit-identical:** about 161 700 numbers per configuration, maximum relative difference 0.0 (`repro_run_35.txt` holds 35, 3, 56; `repro_run_23.txt` holds 23, 84, 15) |
| (c) independent re-scoring | main's own scorer, written from the preregistration without the seat's code (`score_mine.py`), over all 216 000 assignment-cells | **PASS:** 0 S-mass passes in either reading, for the SM and every null. SM best χ² 983.26 (per-field) and 601.77 (minimal); best nulls 267.32 and 471.29; the SM ranks 77th and 33rd of 200. The read-outs all reproduce: S-shape per-field 84 against a null mean of 46.57 (p = 0.03); minimal S-ckm 2 (p = 0.215); 88 bitwise-identical sign-flip pairs among the nulls; 26 configuration classes; class-level p = 0.305 |

**Result 2: the per-field census at every depth** (the S-shape replication's outputs for h ≤ 3; the mid-height scan for
3 < h ≤ 6).

| task | result |
|---|---|
| the stored outputs' hashes | **PASS** (both outputs and their run logs) |
| main's own S-mass re-score (`score2_mine.py`) | **PASS:** 0 passes at both depths. h ≤ 3 (136 classes): SM best 578.2, best null 262.9, SM rank 22 of 113. 3 < h ≤ 6 (185 classes): SM best 28 281.0, best null 14 482.6, SM rank 96 of 113 |

## 2. What it says

- **The web seat's negatives stand on main.** In the surface frame's twisted units on the least-volume closing threads,
  and in the per-field thread frame at every depth computed, no assignment passes the mass test. That covers the SM's
  charges and every null alike. The SM's best fits are no closer than the nulls'.
- **Together with B1660 and B1667, these bound the frames on record.**
  - B1660: one Higgs at ω on eighteen lines.
  - B1667: the end supplies no hierarchy.
  - This arc: the surface and thread frames' low threads and every depth.
  - In none of these frames does a hierarchy of the observed kind come out at the levels tested. In the per-field frame
    the hierarchies come out too strong, and more so with depth.
- **What it does not show:**
  - that no frame works;
  - anything about frames or end conditions outside those computed;
  - the T-tower exponents and the S-shape's sensitivity to its allowance, which were not rechecked.
  - The mid-height and replication instruments were re-scored from their stored outputs, not re-executed.

## 3. Files

`verification/`:
- `REPORT.md`, the reading pass's report;
- `repro_driver.py` and `run_repro.sh`, with the two run logs;
- `score_mine.py` and `score2_mine.py`, main's scorers, with their logs;
- `extra_checks.py` and its run;
- `forms_rebuild_run.txt` and `null_draws_regeneration_run.txt`.

The scripts read the web seat's files checked out from the commits named above. The lock is
`tests/test_b1668_the_web_seats_low_thread_negatives_verified.py`.
