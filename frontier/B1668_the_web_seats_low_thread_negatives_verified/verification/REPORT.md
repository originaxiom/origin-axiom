# P-188 verification of the web seat's T-low and per-field census results (cc, 2026-10-17)

All work in audit/drafts/p188/. Nothing tracked was edited; nothing committed. Single-threaded, nice 10, at most 2 processes.
Files were checked out with `git show <commit>:<path>` (tu/ = 0d83e6981 seal files + 09f41b453 output; ss/ = 34b2e8061; sshape/ = 2a4bd10fe, needed for the h<=3 numbers).

## RESULT 1: the twisted units on the low threads (T-low)

### (a) Seal and integrity: PASS
- The output JSON records sha256 of six seal inputs (tlow2.py, null_draws.json, tlow_configurations.json, both received_*.json, twisted_units_seal.py). The files at 0d83e6981 hash to exactly those six values. `git diff 0d83e6981 origin/chat1/web-seat` on the seal files (incl. the preregistration, null_draws.*, units_cells.py) is empty.
- Committed xz (09f41b453) sha256 = a6add033... as recorded; `xz -d` gives ff7447b2... as recorded; run log b97e1cb0... as recorded.
- forms.pkl: rebuilt from `build_forms.py` (web-seat tree, c9fb02637; only change in my copy: `<repo>` path set to this repo; the SM-seat/main commits it reads, 87cf7f55 and 1d2dac43d, are present). Build took 1257 s. sha256 = 64a40c036050c142c6aedd231bfc536f99f34a5816c7e5e3a2b585ee8cf8bfe9, equal to the preregistration's `64a40c036050c142...` and to the "forms.pkl sha256" recorded in the output. Byte-identical rebuild.
- Null draws: running null_draws.py (seed 20261015, box 18) regenerates null_draws.json with the identical sha256 e309023f...; my own check of the 199 used draws: all satisfy H=-(Q+u), d=H-Q, e=H-L, none has a charge = 0 mod 9, 11 or 12, max |q| = 17.
- Controls recorded in the output hold (closure 2e-49, 6e-52; uncarried line fails at 4.96 and 84.1).

### (b) Re-execution of 6 of 90 configurations: PASS (bit-identical)
Sample: `random.Random(20261017).sample(range(90), 6)` = [35, 3, 56, 23, 84, 15]. Driver `repro_driver.py` imports `twisted_units_seal.one_configuration` unmodified, runs it on `instrument/forms.pkl`, compares the whole record (closure, plan, all 7200 cells: s, U, r_calc, r_calc_53, bits, Npts, height) to the stored one.

| idx | N | word | line | numbers compared | differing | time (stored) |
|---|---|---|---|---|---|---|
| 35 | 11 | LLLLRRLRRRLR | (3,2) | 161702 | 0 | 139 s (100) |
| 3 | 9 | LLLLLRRRLRRR | (2,7) | 161678 | 0 | 125 s (103) |
| 56 | 11 | LLRRRRLRRRLR | (4,10) | 161702 | 0 | 130 s (96) |
| 23 | 11 | LLLLRLRRRLRR | (1,10) | 161702 | 0 | 141 s (101) |
| 84 | 12 | LLRLRRLRRLR | (3,1) | 161708 | 0 | 139 s (104) |
| 15 | 9 | LLRLLRRLRR | (3,5) | 161678 | 0 | 127 s (101) |

Every number agrees exactly (max relative difference 0.0). Logs: repro_run_*.txt.

### (c) Independent re-scoring: PASS (every checked number reproduces)
`score_mine.py` was written from the preregistration (sections 3-6) without importing their scorer; it reads the stored records (216,000 assignment-cells = 90 configurations x (5 per-field + 7 minimal cells) x 200 assignments) and the received data files. Log: score_mine_tu_run.txt, extra_checks_run.txt.

| item | read-out claims | mine |
|---|---|---|
| accepted assignment-cells / failures | 216,000, none | 216,000, none (worst closure 5.1e-36, r_calc 0 everywhere) |
| S-mass passes, any assignment, either reading | 0 | 0 per-field, 0 minimal (so PRIMARY not earned, p = 1) |
| S-mass per-field N=9/11/12 | 0/0/0 | 0/0/0 |
| SM best chi2 per-field | 983 (N=12 LLLRLLRRRLRR C3/E4) | 983.26, same cell |
| SM best chi2 minimal | 602 | 601.77 (N=12, C3/ORTH) |
| best null chi2 per-field / minimal | 267 / 471 | 267.32 / 471.29 |
| SM rank by best cell, per-field / minimal | 77th / 33rd of 200 | 77 / 33 |
| S-shape per-field pooled | SM 84 of 450, null mean 46.6, p = 0.03 | 84, 46.57, 0.03 |
| S-shape per N | N=11: 60 vs 22.8; N=9: 12 vs 12.7; N=12: 12 vs 11.1 | 60/22.79; 12/12.66; 12/11.12 (p 0.03, 0.58, 0.39) |
| S-shape minimal | 0, 0.34, p 1 | 0, 0.342, 1.0 |
| S-ckm per-field / minimal | 0 (0.44, p 1) / 2 (0.65, p 0.215) | 0 / 2 with identical null means and p |
| SM passing chi_shape max / failing min | 7.45 / 7.96 | 7.446 / 7.958 |
| SM configuration-cells | 1080 | 1080 |
| W94 span | "four decades", data 3.14 | SM ratio 0.0060 .. 217 |
| sign-flip pairs in the null | 88 pairs, 111 distinct | 88 pairs, 111 distinct; all 88 bitwise identical in every cell; SM's negative not in null |
| configuration classes | 26 | 26 (by identical SM singular values; 21 words) |
| distinct per-field config-cells | 130 | 130 |
| SM S-shape passes by class | 21 distinct cells in 9 of 26 classes; class-level p = 0.305 | 21, 9, p = 0.305 |

Verdict "no assignment passes S-mass in either reading": reproduced. Caveats of my scorer: r_rho in the shape statistic is not fully specified in the preregistration ("W88's r_rho"); I used hypot(rc/|ln R1|, rc/|ln R2|) for the calc side, irrelevant here because r_calc = 0 in all records (so no ambiguity affects any number). The by-class p (0.305) and the 88-pair finding are post-hoc items of the read-out; they reproduce. The "T-tower exponents >= 0.68" and "S-shape a-variation p 0.05,0.04,0.03,0.12,0.10" items were not rechecked (not S-mass headline numbers).

## RESULT 2: per-field census at every depth (34b2e8061)

### Hashes: PASS
midheight_scan.json.xz = d5c342e6... (as recorded); decompressed json ed721726... (as recorded); midheight_scan_run.txt ad2184ca... (as recorded). The h<=3 numbers (578/263) are not in midheight but in the S-shape replication (smass_on_replication.py); its output at 2a4bd10fe checked too: xz 44c9f0b7..., json cf030ab3..., run 6447c090... all match s_shape_seal_output.sha256.

### Independent re-score (score2_mine.py; log score2_mine_run.txt): PASS
- midheight_scan.json (3 < h <= 6, 185 classes, 113 assignments, 925 class-cells/assignment, 104,525 accepted): S-mass passes SM 0, nulls 0. SM best chi2 28281.0 (N=9 LLLLLRLLRRRRRLRR (3,8) C3/E4); best null 14482.6 (null002, same word, C3/ORTH); SM rank 96 of 113; by band SM best 28281 (3-4), 120860 (4-5), 284727 (5-6); nulls 14483, 105655, 238054. Equal to stored score_midheight_run.txt.
- S-shape replication (h <= 3, words of length 13-14, 136 classes, 680 class-cells, 76,840 accepted): passes 0/0; SM best 578.2 (N=12 LLLRLLRLRRLLRR (1,4) C3/ORTH), best null 262.9 (null015), SM rank 22 of 113. Equal to stored smass_on_replication_run.txt.
- So "no assignment passes S-mass at h <= 3 (best chi2 578 / 263) or at 3 < h <= 6 (28 281 / 14 483)" reproduces exactly. (Band-best null label differs, null036 vs null002, only through a tie between a sign-flip pair; the chi2 value is the same.)

I did not re-execute the midheight or replication instruments (outside the requested scope); only their stored outputs were scored.

## Overall
- Task (a) seal / integrity: PASS
- Task (b) re-execution of 6/90: PASS (bit-identical)
- Task (c) independent re-score of T-low: PASS
- Result 2 hashes and independent S-mass re-score: PASS
- No discrepancies found. Minor notes: re-execution time ~130 s vs 100 s stored (CPU sharing); the preregistration is not hashed in the output (covered by git, byte-identical to HEAD).
