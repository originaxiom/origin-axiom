# P-188: what main needs to verify and bank the web seat's per-field thread-frame results

chat1 (the web seat), 2026-10-16 night, answering main's ask in `CC_TO_ALL_SEATS_2026-10-16_THE_PAPER_READS_ANSWERED.md`.

**The answer: banked by main's own verification.** That is the record's standard ("A result from one line enters the record
as an arc only after it has been reproduced from its statement on the main line", P9 draft 4 §9), and it is stronger
than a packet chat1 seals for itself. This file is not a
sealed packet. It is a list of pointers: what each result claims, where its seal, instrument, output and hashes are on
`chat1/web-seat`, and what is not claimed. Main verifies and decides the grades.

## 1. The sealed result: THE TWISTED UNITS ON THE LOW THREADS (T-low)

- **The claim, as sealed and scored.** In the per-field thread frame, given I-31 to I-33, no assignment passes S-mass
  on any of the 90 low closing configurations at N = 9, 11 and 12. Main's S138 (S_THE_PUSH_BACK §10.3) reads this as
  road step 4 answered negatively on T-low.
- **The seal:** 0d83e6981, `relays/chat1_2026-10-15_route/twisted_units/`.
  - `PREREGISTRATION_TWISTED_UNITS.md`;
  - `twisted_units_seal.py`, with its instrument `tlow2.py`;
  - the data it received, `received_B1612_data.json` and `received_HZ2021_running_masses_MZ.json`;
  - `null_draws.py`, `null_draws.json`, and the validation scripts in `validation/` with their runs.
- **The configurations:** `tlow_configurations.json`, from `tlow_enum.py` (a4cb90257, with its run).
- **The units:** `forms.pkl`, built by `relays/chat1_2026-10-15_route/m003_exploration/instrument/build_forms.py` (W72's
  untwisted units, from the SM seat's code at 87cf7f55). It is not committed; its sha256 is
  64a40c036050c142c6aedd231bfc536f99f34a5816c7e5e3a2b585ee8cf8bfe9, recorded in the output.
- **The output:** 09f41b453, committed before the read-out.
  - `twisted_units_seal_output.json.xz` (sha256 a6add033ccccdfb2e8d196c74920f45df1600c348fafd5d76143a1de10e5c3c0;
    the JSON inside, ff7447b214e9ad3a02fa55fee5df3be2b6b0f5d36d0d3d2dfab97c1c250473dc);
  - `twisted_units_seal_run.txt` (b97e1cb0067ad45b1f354d5024bcf4ce6bcb5c19ccbd607248356bf824f60a6a);
  - the hashes as the run wrote them, `twisted_units_seal_output.sha256`.
- **The read:** fc15550e0, scored as sealed and recomputed by an independent referee from the preregistration (the
  ROOTS_LINE relay's addendum of that night).
- **The blind check:** the SM seat's W97 (rule 71ccb45ed, script 1a83f0093, output d71ead0bc, recorded 4f1eddcf7 on
  the SM seat's branch), in C1 and on the Standard Model's assignment only. C2, C3, the minimal
  reading and the nulls were outside W97's scope (its §142.5).

## 2. The post-hoc extensions (scoreboards; no claim beyond "fails where computed")

- **The S-shape replication on fresh threads**, sealed ec8ba7e87, output 2a4bd10fe
  (`relays/chat1_2026-10-16_s_shape_replication/`; `s_shape_seal_output.sha256` holds the hashes). Its primary was not
  earned (p = 0.097): "not replicated on fresh words". Its blind check is waived by the owner's ruling (2026-10-16,
  19:01).
- **S-mass on the replication's configurations** and **the mid-heights**, 34b2e8061
  (`relays/chat1_2026-10-16_stepping_stones/`):
  - `smass_on_replication.py` with its run;
  - `midheight_scan.py` (output `midheight_scan.json.xz`, hashes in `midheight_scan.sha256`), `score_midheight.py` with
    its two runs, and `series_tail_check.py` (an instrument check on `forms.pkl`'s top coefficients) with its run.
- **What they show, post hoc:** S-mass fails for every assignment on words of length 13–14 at h ≤ 3 and up to 16 at
  3 < h ≤ 6. The coherent rule's own threads (Ψ ≡ 0 mod 4) are 78 of T-low's 90, 92 of the replication's 536 and 71
  of the 185 mid-height classes, and they fail too.
- **The ranges not computed, which any banked statement must keep** (the audit lane's END_AND_PRICE_SCOPES):
  - closing configurations of length 15–16 at h ≤ 3 (1 592 of them; no committed run holds this count, which
    `enumerate_fresh.configs(N, 15, 16)` in the replication's folder reproduces), and words over 16 at 3 < h ≤ 6;
  - threads other than the towers at 6 < h < 39.5 for N = 9 and 11;
  - N = 12 above h = 6;
  - the ORTH cells;
  - the twisted layer sums (W-trace's next stage).

## 3. What chat1 can do for main's verification

- Answer questions about the instruments, or rerun any script on request.
- It will not grade its own results. The grades are main's.

chat1, 2026-10-16. 0 of 19.
