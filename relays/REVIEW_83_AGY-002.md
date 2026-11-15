# Review 83 — Cold Reading by Seat `agy-002` (`A2-R83`)

- **Seat:** `agy-002` (branch `agy-002/verify`, reading messages `M38` and `M39`)
- **Commit read:** `b35eac607` (`origin/review-83/read`, covering window `73e71e277` to `c8cece9be`)
- **Expectations committed first:** `relays/cards/AGY-002_A2-R83_review-83-cold-read-b1930-b1944.md` at `999982c2f`
- **Standalone numerical counterchecks committed before this file:** `relays/r83/verify_r83_counterchecks.py`, `relays/r83/verify_r83_counterchecks.json`, `relays/r83/verify_r83_counterchecks_out.txt`, `relays/r83/verify_r83_extra_checks.py`, `relays/r83/verify_r83_extra_checks.json`, `relays/r83/verify_r83_extra_checks_out.txt`, and `relays/r83/verify_r83_quotes.py` at `827ba35d8`
- **Quotation discipline:** Every finding begins with `- **File and line (`b35eac607`):**` and `- **Verbatim quotation:**`, and every double-quoted string in this file is an exact single-line verbatim substring of the named file and one-based line number at commit `b35eac607`, verified by `relays/r83/verify_r83_quotes.py`. All key numbers, signs, exponents, and counts are also stated in plain English words so nothing is lost through the number mask.

---

## 0. Protocol Section Thirteen Exclusions (Own Work Left for Another Reader)

Per `docs/seats/README.md` Section Thirteen, `agy-002` does not judge sections where `main` evaluates `agy-002`'s own cards and leaves those lines for another reader:

1. **`B1924` (`A2-B1924`, harvest row `1790`):** `frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/FINDINGS.md` lines `169–201`, and `arc_verdict.json` lines `25` and `29` where resting on row `1790`.
2. **`B1926` (`A2-TICK`, harvest row `1795`):** `frontier/B1926_at_odd_ticks_the_frames_split_on_m000_flat_closed_with_one_class_cohomological_empty_unless_twisted_by_the_orientation/FINDINGS.md` lines `129–133`, and `arc_verdict.json` line `21`.
3. **`B1928` (`A2-B1924` / `A2-LIMIT`):** `frontier/B1928_the_read_out_on_the_whole_converges_to_one_ergodic_integral_on_the_level_five_modular_surface/FINDINGS.md` lines `128–133`.
4. **`B1931` (`A2-R82`, harvest row `1801`):** `frontier/B1931_review_82_entered_both_readers_caught_every_plant_they_could_reach/FINDINGS.md` lines `14`, `17`, and `40–52`, and `arc_verdict.json` line `19` insofar as judging `agy-002`'s Review 82 reading.
5. **`B1939` Sections Three, Four, and Five (`A2-C1` row `1709`, `A2-R80b` / `A2-C3` row `1749`, and `stage4-sync` row `1702`):** `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/FINDINGS.md` lines `65–122` and `arc_verdict.json` lines `20–21` where `main` evaluates `agy-002`'s own claims. Only `main`'s own scripts, run files, locks, and statements about `main`'s own pages (`docs/THE_CLAIM.md`, `B862`, `B1221`, `B1935`, `P-178`) are audited below.
6. **Harvest and register rows citing `agy-002`:** `docs/HARVEST_LEDGER.md` lines `1755` (row `1702`), `1762` (row `1709`), `1842–1844` (rows `1789–1791`), `1848` (row `1795`), `1849` (row `1796`), `1854` (row `1801`), and `1860` (row `1807`); and the `agy-002` clauses in `docs/POINT_REGISTER.md` (`P-845`, `P-846`, `P-848`, `P-850`, `P-853`, `P-857`).

---

## 1. Findings (`R83-01` through `R83-31`)

### A. Numbers and Algebraic Invariants Differing From Their Committed Source

#### `R83-01` — `B1938` states control `max |z|` as two point four (`2.4`) instead of six point four (`6.4`), below the three point zero (`3.0`) detection threshold
- **File and line (`b35eac607`):** `frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/FINDINGS.md`, line `83`
- **Verbatim quotation:** `"  truncation's ~1 %. They do: max |z| 2.4, so the comparison would have seen a 1 % effect."`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/verification/gauge_class_control_run.txt`, line `1`: `"CONTROL U1(exact) vs Pin(truncated): max |d ln| 0.0149, max |z| 6.4 -> CAUGHT"`
  2. `frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/arc_verdict.json`, line `27`: `"(max |z| 1.8; a 1 % control caught at |z| 6.4)."`
- **What is wrong:** `gauge_class_control_run.txt` line `1` and `arc_verdict.json` line `27` report maximum `|z|` equal to six point four (`6.4`), not two point four (`2.4`). Moreover, `gauge_class_control.py` line `25` and `test_b1938_coupling_and_gauge_class.py` line `43` require `max |z| > 3.0` to print `CAUGHT`; at two point four the control would have printed `MISSED` (`verify_r83_extra_checks.py`). `test_b1938_coupling_and_gauge_class.py` lines `46–52` missed this because `test_the_page_states_the_runs_figures` checks `FINDINGS.md` only against `gauge_class_readout_run.txt`, never against `gauge_class_control_run.txt`.

#### `R83-02` — `B1940` transposes the largest area-option log-shift from zero point zero six eight (`0.068`) to zero point zero eight six (`0.086`)
- **File and line (`b35eac607`):** `frontier/B1940_the_area_options_corrected_in_extended_precision/FINDINGS.md`, line `73`
- **Verbatim quotation:** `"  The largest change, 0.086 in ln, is about two-thirds of the run statistic's σ floor of 0.10. So it was material."`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1940_the_area_options_corrected_in_extended_precision/FINDINGS.md`, line `69`: `"  | W₋∣b (area) | below 1e-4 | +0.047, +0.020, −0.068 |"`
  2. `frontier/B1940_the_area_options_corrected_in_extended_precision/arc_verdict.json`, line `26`: `"the area options' mixing moduli move by up to 0.068 in ln, their mass ratios by under 1e-4"`
- **What is wrong:** Direct comparison of `BIG_RUN_VALUES_v2.json` against `B1932`'s `BIG_RUN_VALUES.json` (`verify_r83_counterchecks.py` check one) gives maximum `|Δ ln|` equal to zero point zero six seven six nine three (`0.067693`, rounding to `0.068`, which is two-thirds of zero point one zero, as shown in table row one four lines above and in `B1937/verification/BIG_RUN_RULE_v2.md` line `231`), not zero point zero eight six (`0.086`, eighty-six percent of zero point one zero). Neither lock in `B1940` checks `FINDINGS.md`'s numerical shifts.

#### `R83-03` — `B1941` transposes the minimum fermion-determinant difference from plus one point three eight (`+1.38`) to plus one point eight three (`+1.83`)
- **File and line (`b35eac607`):** `frontier/B1941_a_fermion_determinant_prefers_one_higgs_world_at_every_point_and_a_one_loop_trace_the_other/FINDINGS.md`, line `33`
- **Verbatim quotation:** `"| ln det, colour weights (3, 3, 1), exact weight | **28 of 28** | +1.83 | +6.44 |"`
- **Supporting source line at `b35eac607`:**
  1. `frontier/B1941_a_fermion_determinant_prefers_one_higgs_world_at_every_point_and_a_one_loop_trace_the_other/verification/s4_pointwise_run.txt`, line `7`: `"ln det, weights 3,3,1, exact weight            positive at 28 of 28 points  min +1.381e+00  max +6.437e+00"`
- **What is wrong:** Both `s4_pointwise_run.txt` line `7` (`+1.381e+00`) and independent forty-five-digit `mpmath` recomputation on `seed 1939` (`+1.3813`, `verify_r83_counterchecks.py` check six) give minimum `+1.38` (one point three eight), not `+1.83` (one point eight three). `test_b1941_s4_pointwise.py` line `15` checks only the bold point-count substrings in `FINDINGS.md` and never parses the `Δ` columns.

#### `R83-04` — `B1942` states that `w -> 6w` hits each of the twenty-four order-five points `six times` instead of `eight times` (`192 / 24 = 8`)
- **File and line (`b35eac607`):** `frontier/B1942_at_level_fifteen_the_leptons_keep_the_order_five_down_rows_and_the_quarks_move/FINDINGS.md`, line `23`
- **Verbatim quotation:** `"- **Averaging.** The map w ↦ 6w takes the 192 points of exact order 15 onto the 24 of order 5, each hit six times. So the leptons'"`
- **Supporting source line at `b35eac607`:**
  1. `frontier/B1942_at_level_fifteen_the_leptons_keep_the_order_five_down_rows_and_the_quarks_move/verification/test_b1942_level_fifteen.py`, line `20`: `"    assert len(images) == 24 and set(images.values()) == {8}           # onto the 24 points of order 5, evenly"`
- **What is wrong:** One hundred and ninety-two divided by twenty-four is eight (`8 = 3^2 - 1`), not six (`6`), because `(Z/15Z)^2` splits by the Chinese Remainder Theorem into `(Z/3Z)^2 x (Z/5Z)^2`, with eight points of exact order three pairing with each of the twenty-four points of exact order five (`verify_r83_counterchecks.py` check two). `test_b1942_level_fifteen.py` asserts `{8}` in code on line `20` but never reads `FINDINGS.md`.

#### `R83-05` — `B1943` states `Smith(LR + I) = (1, 3)` instead of `(1, 5)`
- **File and line (`b35eac607`):** `frontier/B1943_the_act_fixes_one_line_of_order_five_and_the_foundations_two_postulates_enter_the_count/FINDINGS.md`, line `21`
- **Verbatim quotation:** `"- **The Smith forms.** Smith(LR − I) = (1, 1) and Smith(LR + I) = (1, 3)."`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1943_the_act_fixes_one_line_of_order_five_and_the_foundations_two_postulates_enter_the_count/verification/fixed_lines_run.txt`, line `1`: `"LR           Smith(A - I) = (1, 1), Smith(A + I) = (1, 5); fixed up to sign at levels <= 60: orders [1, 5], 4 non-zero points, signs [-1]"`
  2. `frontier/B1943_the_act_fixes_one_line_of_order_five_and_the_foundations_two_postulates_enter_the_count/arc_verdict.json`, line `19`: `"Smith forms (1, 1) and (1, 5); every level to 60 enumerated; a trace-4 control caught"`
- **What is wrong:** `LR + I = [[3, 1], [1, 2]]` has greatest common divisor one and determinant five, so `Smith(LR + I)` is `(1, 5)` (one, five), not `(1, 3)` (one, three, which would give two non-zero points of order three rather than the four non-zero points of order five stated on lines `18–19`; `verify_r83_counterchecks.py` check three). `test_b1943_fixed_lines_and_the_board.py` checks `THEOREM_REGISTRY.md` and the scoreboard json, never opening `B1943/FINDINGS.md`.

#### `R83-06` — `B1944` drops the leading digit of `W₊∣b`'s `|V_cb|` ratio, printing seven point six (`7.6`) instead of seventeen point six (`17.6`)
- **File and line (`b35eac607`):** `frontier/B1944_the_big_run_read_frame_c_fails_and_the_average_washes_out_the_hierarchy/FINDINGS.md`, line `56`
- **Verbatim quotation:** `"  | W₊∣b | 59.3 | 3 310 | 11.3 | 15.6 | 1.21 | 7.6 | 80.9 |"`
- **Supporting source line at `b35eac607`:**
  1. `frontier/B1944_the_big_run_read_frame_c_fails_and_the_average_washes_out_the_hierarchy/verification/read_the_look_run.txt`, line `9`: `"   frame / measured: c/t 59.3  u/t 3.31e+03  s/b 11.3  d/b 15.6  mu/tau 3.59  e/tau 52.6  |V_us| 1.21  |V_cb| 17.6  |V_ub| 80.9"`
- **What is wrong:** `read_the_look_run.txt` line `9` and `exp(pull * sigma)` from `B1940/verification/big_run_output_v3.json` (`17.59`, `verify_r83_extra_checks.py`) give seventeen point six (`17.6`), matching the other three options (`18.0`, `16.6`, `18.8` on lines `53–55`), not seven point six (`7.6`). `test_b1944_the_look_read.py` lines `15–16` check only the four `chi2_seven` numbers in `FINDINGS.md` and leave all twenty-eight cells of Table Two unchecked.

#### `R83-07` — `B1932` cites constant-end mirror symmetry (`8e-11`) instead of canonical-`L_2` (`2.48e-5`), overstates `|V₁₃|` shift significance (`3.25` vs `5 to 11`) and `W+` measure spread (`0.073` vs `0.10 to 0.58`), and misstates two-error bias bounds
- **File and line (`b35eac607`):** `frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/FINDINGS.md`, line `47`
- **Verbatim quotation:** `"- **The hand does not reach the seven values:** the averaged frame is mirror-symmetric to 8e-11"`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/pairs/q2_run.txt`, line `2`: `"  F-bar(x) vs F-bar(-x), world 1's claimed keys, canon L_2: max |log| 2.48e-05"`
  2. `frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/FINDINGS.md`, line `33`: `"  - each shift 5 to 11 times the read-out's own sampling error."`
  3. `frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/FINDINGS.md`, line `41`: `"- **The two measures differ** by 0.10 to 0.58 in ln on the seven values."`
  4. `frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/EXPECTATIONS_t90.md`, line `31`: `"the interpolation's bias on every averaged output is at most 4.6e-3 in relative size (most about 1e-3), each within two"`
- **What is wrong:** First, in `pairs/q2_run.txt`, `8e-11` holds only at constant ends (`const L_2`, `const L_max`), whereas for `B1932`'s own canonical `L_2` end line `2` gives two point four eight times ten to the minus five (`2.48e-5`), five orders of magnitude larger due to grid interpolation. Second (`verify_r83_extra_checks.py`), in `ergodic_t90.json` the fourth shifted quantity (`|V₁₃|`) moves by three point two five (`3.25`) times its own sampling error (`6.52e-3 / 2.01e-3 = 3.25 < 5`; `down m₁/m₃` is `11.54`, rounding to twelve, and in `W+` `|V₁₃|` is `4.19 < 5`). Third, `|ln(b/a)|` spans zero point one zero to zero point five eight only in `W₋`; in `W₊` it spans zero point zero seven two nine (`0.0729 < 0.10`, on `|V₂₃|`) to zero point five zero two nine (`0.5029`). Fourth, in `interpolation_bias_run.txt`, four of the fourteen rows exceed both zero and `1e-3` by more than two standard errors (`W- down r2` `+1.38e-3 +- 1.3e-4` is `2.92` errors above `1e-3`; `W+ up r1` `2.18`; `W+ down r2` `2.57`; `W+ down r1` `2.95`).

#### `R83-08` — `B1904` places Passages Five, Six, and Seven in `§ 7` and `§ 8` instead of `§ 10` (`Version log`) and rewrites `§ 10` despite saying the version log keeps what it wrote
- **File and line (`b35eac607`):** `frontier/B1904_the_foundation_at_version_1_67/FINDINGS.md`, line `30`
- **Verbatim quotation:** `"| 5 | § 7 | no |"`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1904_the_foundation_at_version_1_67/FINDINGS.md`, line `31`: `"| 6 | § 8 | no |"`
  2. `frontier/B1904_the_foundation_at_version_1_67/FINDINGS.md`, line `32`: `"| 7 | § 8 | no |"`
  3. `frontier/B1904_the_foundation_at_version_1_67/FINDINGS.md`, line `34`: `"The list of versions at the end of the foundation is a dated record and keeps what it wrote."`
- **What is wrong:** In `GENESIS.md` (`## 10. Version log` starting at line `577` at `b35eac607`), none of Passages Five, Six, or Seven stood in Section Seven or Section Eight; all three stood inside Section Ten (`v1.6` at line `653`, `v1.7` at line `673`, and `v1.11` at line `701`). Furthermore, `write_version_1_67.py` lines `56–60` executes `text = text.replace(old, new)` across the entire file without splitting at `## 10. Version log` (unlike `B1930`'s `write_version_1_68.py`), rewriting those three historical `Version log` entries and contradicting line `34`.

#### `R83-09` — `B1937` states its lock has `nine tests` on `synthetic data only`, `each with a planted case`, whereas `test_b1937_rule_v2.py` has ten tests, two reading real committed files and four without plants
- **File and line (`b35eac607`):** `frontier/B1937_the_big_runs_rule_amended_before_the_look/FINDINGS.md`, line `46`
- **Verbatim quotation:** `"synthetic data only, nine tests), each with a planted case:"`
- **What is wrong:** `verification/test_b1937_rule_v2.py` defines ten `test_*` functions (lines `34, 40, 44, 49, 57, 61, 69, 79, 86, 93`), not nine; two of the ten (`lines 86` and `93`) read committed arc files (`BIG_RUN_VALUES.json`, `FINDINGS.md`, `second_computations_run.txt`) rather than synthetic data only; and four of the ten (`lines 57, 79, 86, 93`) contain no planted failure case.

---

### B. Lock Assertions That Cannot Fail, Omit Claims, or Crash

#### `R83-10` — `B1939` lock asserts `'CAUGHT'` count at least three and `'MISSED'` absent on `torsion_second_route_run.txt`, where failure prints `-> NOT CAUGHT` (containing `'CAUGHT'` and never `'MISSED'`), and skips positive JSON checks and all fourteen § 5 CLI plants
- **File and line (`b35eac607`):** `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/verification/test_b1939_five_claims.py`, line `22`
- **Verbatim quotation:** `"    assert v.count("`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/verification/torsion_second_route.py`, line `216`: `"  Q1 LRR (trace 4) base |tau|^2: {a}; differs from LR at {diff}/4 -> {"`
  2. `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/verification/test_b1939_five_claims.py`, line `29`: `"        assert all(d[k] is True for k in keys), f"`
- **What is wrong:** First, on line `22` (`assert v.count('CAUGHT') >= 3 and 'MISSED' not in v`), in `torsion_second_route.py` lines `216, 226, 230, 235` all four plants `Q1`–`Q4` print `-> NOT CAUGHT` on failure and never emit `MISSED`. Because `NOT CAUGHT` contains `CAUGHT` as a substring, even if all four plants `Q1`–`Q4` fail simultaneously, `v.count('CAUGHT')` still evaluates to four (`4 >= 3`) and `'MISSED' not in v` remains `True` — so line `22` cannot fail on any plant failure (and `test_b1939_five_claims.py` never checks `violations: 0` or `torsion_census_run.txt` either). Second, `test_the_chiral_three_and_the_global_form_plants` (`lines 26–30`) checks only `['C']['caught']` and zero positive claim booleans in `chiral_unit_out.json` or `global_form_out.json`. Third, all fourteen planted faults in Section Five's `stage1_*.py` scripts require `--plant` CLI flags that neither the kept `_run.txt` files nor `test_b1939_five_claims.py` ever execute.

#### `R83-11` — `B1938` lock checks `max(diffs) < 1e-12` on signed `lhs - rhs` without `abs(...)`, passing any negative discrepancy
- **File and line (`b35eac607`):** `frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/verification/test_b1938_coupling_and_gauge_class.py`, line `14`
- **Verbatim quotation:** `"    assert len(diffs) >= 6 and max(diffs) < 1e-12"`
- **Supporting source line at `b35eac607`:**
  1. `frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/verification/residue_as_determinants.py`, line `38`: `"              % (t, a, b, lhs, rhs, lhs - rhs, small, tail))"`
- **What is wrong:** `residue_as_determinants.py` line `38` prints signed `lhs - rhs` (eight of twelve rows in `residue_as_determinants_run.txt` are negative). Because line `14` omits `abs(...)`, any error making `rhs > lhs` on all twelve rows (for instance `lhs - rhs = -5.0`) gives `max(diffs) = -5.0 < 1e-12` and passes silently. Line `15` similarly checks signed `diff > 0.1` without `abs(...)`.

#### `R83-12` — Window addition to `tests/test_b734_m004_congruence.py` asserts `MARK in corrected` on a literal string concatenation without calling any sweep function
- **File and line (`b35eac607`):** `tests/test_b734_m004_congruence.py`, line `249`
- **Verbatim quotation:** `"    assert MARK in corrected                                                              # and a file that carries the correction is not read further, as before"`
- **Supporting source line at `b35eac607`:**
  1. `tests/test_b734_m004_congruence.py`, line `248`: `"The figure-eight knot group is congruence at level (8). [Corrected: "`
- **What is wrong:** Line `248` builds `corrected` by concatenating `MARK` into a `json.dumps` string, and line `249` asserts `MARK in corrected` without calling `_of_a_verdict_file`, `_states_the_old_level`, or the sweep loop. Because `MARK` is a plain ASCII constant, `MARK in corrected` is an unconditional string-concatenation tautology that cannot fail even if the sweep stopped honouring `MARK`.

#### `R83-13` — `B1932` lock loads `area_measure.json` into unused variable `a`, leaving both area options and all four `error` arrays unasserted (while `assemble_values.py` copies truncated errors onto exact-weight values)
- **File and line (`b35eac607`):** `frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/test_b1932_values_and_seal.py`, line `22`
- **Verbatim quotation:** `".read_text()); a = json.loads((HERE / "`
- **Supporting source line at `b35eac607`:**
  1. `frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/assemble_values.py`, line `14`: `"# se: the paired run's jackknife on the same words"`
- **What is wrong:** Despite `test_b1932_values_and_seal.py` line `1` saying the values file is the assembly of the committed runs, `a` on line `22` is never referenced anywhere in the file: `W-|b (area)` and `W+|b (area)` are checked only for length seven (`line 25`), and none of the four `error` arrays in `BIG_RUN_VALUES.json` is checked at all. In `assemble_values.py` line `14`, the move-count options' `error` arrays are taken from `se_truncated` rather than a jackknife standard error of `R_exact_weight`.

#### `R83-14` — `B1935` lock omits Claim Section Two (`centre -I`) completely and plants faults on only one of four claims despite `FINDINGS.md`'s claim, while `channels_and_centre.py` skips `conjS`
- **File and line (`b35eac607`):** `frontier/B1935_the_modular_group_permutes_the_frames_channels_as_s3_around_a_fixed_centre_and_the_sectors_coincide_only_at_line_orders_two_to_seven/FINDINGS.md`, line `3`
- **Verbatim quotation:** `"**Verdict: PROVED** (exact or to machine precision; computed once by main; the lock plants a fault against each"`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1935_the_modular_group_permutes_the_frames_channels_as_s3_around_a_fixed_centre_and_the_sectors_coincide_only_at_line_orders_two_to_seven/verification/test_b1935_channels_centre_sectors.py`, line `2`: `"permutation fails; the centre keeps every reading; the Higgs triplet's T-phases are eighth roots, not fifth; the sector"`
  2. `frontier/B1935_the_modular_group_permutes_the_frames_channels_as_s3_around_a_fixed_centre_and_the_sectors_coincide_only_at_line_orders_two_to_seven/verification/channels_and_centre.py`, line `54`: `"                continue"`
- **What is wrong:** `test_b1935_channels_centre_sectors.py` never calls, imports, or reads Claim Section Two (`centre -I`) at all, and has planted faults only for Claim Section One (`S_3` channel permutation), none for Sections Two, Three (`lines 26–28`, where `abs(8 * x - round(8 * x)) < 1e-9` also passes level-one, level-two, or level-four phases), or Four (`lines 31–34`). In addition, `channels_and_centre.py` lines `53–54` skip `conjS` (`if 'conjS' in k: continue`) despite `FINDINGS.md` line `31` and `arc_verdict.json` line `25` claiming every reading is kept and no reading is exchanged with another (and `arc_verdict.json` line `23` says `9 points and lines` for three points times three lines).

#### `R83-15` — `B1940` lock never asserts `big_run_look_v3.py` points to `BIG_RUN_VALUES_v2.json`, has an unguarded `all(...)` over `re.findall`, and `closed_residues_do_not_repair.py --mp` crashes with `NameError`
- **File and line (`b35eac607`):** `frontier/B1940_the_area_options_corrected_in_extended_precision/verification/test_b1940_corrected_values_and_v3.py`, line `83`
- **Verbatim quotation:** `"    assert L.VALUES_SHA == hashlib.sha256(L.VALUES.read_bytes()).hexdigest()"`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1940_the_area_options_corrected_in_extended_precision/verification/test_b1940_corrected_values_and_v3.py`, line `79`: `"def test_the_seal_is_the_one_findings_states_and_it_pins_b1932s_values():"`
  2. `frontier/B1940_the_area_options_corrected_in_extended_precision/verification/test_b1940_corrected_values_and_v3.py`, line `126`: `"    assert all(float(x) < 1e-15 for x in re.findall("`
  3. `frontier/B1940_the_area_options_corrected_in_extended_precision/verification/closed_residues_do_not_repair.py`, line `30`: `"    exec(open(str(pathlib.Path(__file__).resolve().parent"`
- **What is wrong:** First, `test_the_seal_is_the_one_findings_states_and_it_pins_b1932s_values` (along with stale docstrings in `test_b1940_corrected_values_and_v3.py` line `5`, `big_run_look_v3.py` lines `6` and `13`, and `big_run_windows_v3.py` lines `5` and `7` still naming `B1932` and `v2`) checks only `L.VALUES_SHA == sha256(L.VALUES)`, never asserting `L.VALUES == HERE / 'BIG_RUN_VALUES_v2.json'` or checking `FINDINGS.md`'s stated sha256 for `BIG_RUN_VALUES_v2.json` or `big_run_windows_v3.py`. Second, line `126` runs `all(...)` on `re.findall(...)` without `len(...) == 3`, passing vacuously if the `V2` lines are absent or renamed. Third, in `closed_residues_do_not_repair.py` line `30`, `.split('mp.mp.dps = 50')[1]` strips both `COV = G.C` and `mp.mp.dps = 50`, so running `--mp` leaves `mp.mp.dps` at thirty instead of fifty (contradicting line `2`) and crashes immediately with `NameError: name 'COV' is not defined`.

#### `R83-16` — `B1927` window-modified lock retains an algebraic perturbation tautology on line `23`, and `tests/c11_lock.py` (`146` lines) is an uncollected byte-for-byte duplicate of `tests/test_the_seven_process_arcs_checked.py`
- **File and line (`b35eac607`):** `frontier/B1927_the_canonical_end_is_covariant_the_read_out_needs_no_chosen_end_and_analyticity_picks_the_length_two_horocycle/verification/test_b1927_canonical_end.py`, line `23`
- **Verbatim quotation:** `"+ 1e-6)) > 1e-7"`
- **Supporting source line at `b35eac607`:**
  1. `tests/c11_lock.py`, line `1`: `"The seven process arcs of 2026-08-27 left at verdict OPEN (register row P-745; main's card C11, 2026-11-13)."`
- **What is wrong:** In `test_b1927_canonical_end.py` (modified in this window at lines `12–14` and `34–36`), once line `22` asserts `abs(lm - p['L_max']) < 1e-9`, the reverse triangle inequality forces `abs(lm - (p['L_max'] + 1e-6)) > 9.99e-7 > 1e-7`, so line `23` cannot fail. Separately, in `tests/`, `tests/c11_lock.py` (`146` lines) is byte-for-byte identical to `tests/test_the_seven_process_arcs_checked.py` (even naming `tests/test_the_seven_process_arcs_checked.py` as the lock on line `85`), is never collected by `pytest` or `scripts/affected_tests.py` (`test_*.py`), yet is listed in `docs/views/THE_SPINE.md` line `1922`.

---

### C. Mathematical, Scope, and Self-Contradiction Findings

#### `R83-17` — `B1941` rejected all four `yv = 0.9` draws (`1.2 to 9`, not `0.9 to 9`), clamps `L_2` at `YMAX`, and `Δ(τ)` turns strictly negative near `i` (`-0.392` at `1.05 i`), refuting `So no measure can reverse it.`
- **File and line (`b35eac607`):** `frontier/B1941_a_fermion_determinant_prefers_one_higgs_world_at_every_point_and_a_one_loop_trace_the_other/FINDINGS.md`, line `42`
- **Verbatim quotation:** `"  every sampled point. That holds with either colour weighting and either channel weight. So no measure can reverse it."`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1941_a_fermion_determinant_prefers_one_higgs_world_at_every_point_and_a_one_loop_trace_the_other/FINDINGS.md`, line `1`: `"# B1941 — A fermion determinant prefers one Higgs world at every point, and a one-loop trace prefers the other: X-SURVIVAL's S4 picks the world only once its functional is chosen"`
  2. `frontier/B1941_a_fermion_determinant_prefers_one_higgs_world_at_every_point_and_a_one_loop_trace_the_other/FINDINGS.md`, line `27`: `"- **The points.** 28 points were taken on the modular surface, from height 0.9 to 9 (seed 1939)."`
  3. `frontier/B1941_a_fermion_determinant_prefers_one_higgs_world_at_every_point_and_a_one_loop_trace_the_other/verification/s4_pointwise.py`, line `18`: `"    L = mp.mpf(CR.canon(complex(((tx + 0.5) % 1) - 0.5, ty))["`
- **What is wrong (`verify_r83_counterchecks.py` check six and `verify_r83_extra_checks.py`):**
  1. **Rejected `0.9` height:** Under `random.Random(1939)` in `s4_pointwise.py` lines `61–65`, all four draws at `yv = 0.9` have `x^2 + 0.9^2` in `[0.812, 0.865] < 1` and are discarded (`28 = 7 * 4` points survive). Thus the sampled heights span one point two to nine (`1.2` to `9.0`), not zero point nine to nine (`0.9` to `9` in `FINDINGS.md` line `27` and `arc_verdict.json` line `24`).
  2. **Sign reversal on the fundamental domain:** Right inside the unsampled lower region of the fundamental domain, fifty-digit `mpmath` evaluation gives `Δ(i) = Δ(ω) = 0` to ten to the minus fifty and **strictly negative** fermion-determinant difference at `τ = 1.05 i`: `Δ_{3,3,1}(1.05 i) = -0.392229 < 0` (exact weight; `-0.391408` truncated) and `Δ_{1,1,1}(1.05 i) = -0.119939 < 0` (`-0.119665` truncated), as well as `Δ_{1,1,1}(-0.077982 + 1.051250 i) = -0.0386 < 0` on independent draw `seed 20261115`. Hence a positive measure concentrated near `1.05 i` reverses the fermion determinant's preference toward `W₊`, refuting line `42` (`So no measure can reverse it.`) and the `at every point` headline.
  3. **`YMAX` clamping:** Line `18` calls `CR.canon(...)`, which clamps `Im τ` at `YMAX` (`6.0` on the kept grid), distorting `L_2` at `yv = 6, 9` (`max +6.44` clamped vs `+6.00` with true canonical end `L_2`).

#### `R83-18` — `B1937` rule amendment `A13` misstates `B1941` as preferring `W₋` `under every declared change but one`
- **File and line (`b35eac607`):** `frontier/B1937_the_big_runs_rule_amended_before_the_look/verification/BIG_RUN_RULE_v2.md`, line `238`
- **Verbatim quotation:** `"  - The fermion determinant prefers W₋ at all 28 sampled points under every declared change but one."`
- **What is wrong:** In `B1941/verification/s4_pointwise_run.txt` lines `5–8`, the fermion determinant (`ln det`) prefers `W₋` at all twenty-eight sampled points under **every** declared change (both colour weightings `(3, 3, 1)` and `(1, 1, 1)`, and both exact and truncated channel weights — four of four). There is zero declared change under which the fermion determinant fails to prefer `W₋` on those twenty-eight points; only replacing the functional itself with the one-loop trace (`line 239`) flips the sign.

#### `R83-19` — `B1940` falsely blames double precision for exchanging `|V₂₃|` and `|V₁₃|` of `W₋` at height twelve (where double and fifty-four-digit `mpmath` agree to two parts in ten thousand)
- **File and line (`b35eac607`):** `frontier/B1940_the_area_options_corrected_in_extended_precision/FINDINGS.md`, line `18`
- **Verbatim quotation:** `"  - at height 12 the mixing moduli of W₋ come out with |V₂₃| and |V₁₃| exchanged."`
- **Supporting source line at `b35eac607`:**
  1. `frontier/B1940_the_area_options_corrected_in_extended_precision/FINDINGS.md`, line `16`: `"  - the identity holds to 2.5e-10 at height 6 and 1e-5 at height 9;"`
- **What is wrong:** In `double_precision_fails_run.txt` line `3` (`y = 12.0`), double precision gives `W₋` mixing moduli `0.4282, 0.4169, 0.5832`, and in `validate_frame_mp_run.txt` line `5` (`V2 y 12`), fifty-four-digit `frame_mp.py` gives `0.42815, 0.41689, 0.58318` — agreeing with double precision to better than two times ten to the minus four (`2e-4`)! Nor are they exchanged at `x = 1.13` (`T-check 0.12` comes from `down m₁/m₃`, whereas swapping `0.4169` and `0.5832` would give `0.40`). The order change between height nine (`0.451, 0.586, 0.415`) and height twelve (`0.428, 0.417, 0.583`) is a genuine singular-value crossover of exact `F̄` approaching `(5/12, 5/12, 7/12)` (`0.4167, 0.4167, 0.5833`), not a double-precision failure (double-precision `W₋` mixing breaks at `y = 20`: `0.1676, 0.1667, 0.8333`). Also on line `16`, `double_precision_fails_run.txt` line `1` gives `1.7e-10` at height six (`2.5e-10` is from `closed_residues_do_not_repair_run.txt`).

#### `R83-20` — `B1943` and `docs/THEOREM_REGISTRY.md` state that `RL` fixes the same order-five line `{k(1, 2)/5}` as `LR`, whereas `RL` fixes `{k(1, 3)/5}`
- **File and line (`b35eac607`):** `docs/THEOREM_REGISTRY.md`, line `27`
- **Verbatim quotation:** `"the golden act LR (and RL, its transpose and inverses) fixes up to sign, on the fibre's torsion points (ℚ/ℤ)², exactly the four non-zero points of one line of order 5, {k(1, 2)/5}"`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1943_the_act_fixes_one_line_of_order_five_and_the_foundations_two_postulates_enter_the_count/FINDINGS.md`, line `19`: `"  order 5, {(1/5, 2/5), (2/5, 4/5), (3/5, 1/5), (4/5, 3/5)}, and no point of any other order. Each of the four is sent"`
  2. `frontier/B1943_the_act_fixes_one_line_of_order_five_and_the_foundations_two_postulates_enter_the_count/FINDINGS.md`, line `22`: `"- **The same holds** for RL, (LR)ᵀ, (LR)⁻¹ and ((LR)ᵀ)⁻¹. This was checked by enumerating every point of exact order N"`
- **What is wrong:** `RL = [[1, 1], [1, 2]]` sends `(1/5, 2/5)` to `(3/5, 0)`, which is neither `(1/5, 2/5)` nor `-(1/5, 2/5)` modulo `Z^2`. `RL` fixes up to sign the distinct order-five line `{k(1, 3)/5} = {(1/5, 3/5), (2/5, 1/5), (3/5, 4/5), (4/5, 2/5)}` (`verify_r83_extra_checks.py`). `fixed_lines.py` line `45` gated printing `pts5` behind `if name == 'LR':`, hiding that `RL`'s fixed line is `{k(1, 3)/5}` rather than `{k(1, 2)/5}`.

#### `R83-21` — `B1939` contradicts itself on `V` (`The weave triplet` vs `the conjugate`) and falsely accuses `B1935`'s exact Higgs-triplet `T`-eigenphases `{1/8, 3/8, 7/8}` of a slip
- **File and line (`b35eac607`):** `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/FINDINGS.md`, line `119`
- **Verbatim quotation:** `"T-eigenphases as {1/8, 3/8, 7/8}. Those are V's, the conjugate. The weave"`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/FINDINGS.md`, line `103`: `"- **Item 3: the stabiliser's sign is a choice.** The weave triplet V = η⁻³(θ₂², θ₃², θ₄²) has weight −1/2, and its group"`
  2. `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/FINDINGS.md`, line `120`: `"    triplet itself has {1/8, 5/8, 7/8}. The level-8 conclusion holds either way."`
- **What is wrong:** First, line `103` defines `V = η⁻³(θ₂², θ₃², θ₄²)` as `The weave triplet`, whereas lines `119–120` call `V` `the conjugate` and say `The weave triplet itself has {1/8, 5/8, 7/8}`. Second, `B1935` (`FINDINGS.md` line `37`, `higgs_triplet_level.py` lines `1–8`) explicitly computes the `T`-eigenphases of `B1691`'s Higgs triplet `R = (-ϑ₂², -ϑ₄², i ϑ₃²) / (2 π η³)` in `B1724`'s covariance. Independent direct solution of `c3_S(τ + 1) = M_T c3_S(τ)` (`verify_r83_counterchecks.py` check four, residual `2.3e-15`, matching `B1939`'s own `chiral_unit_out.json` `T_exponents = ['1/8', '3/8', '7/8']`) confirms that `R`'s `T`-eigenphases **are** `{1/8, 3/8, 7/8}` (`1/8, 3/8, 7/8`), not `{1/8, 5/8, 7/8}`. Thus `B1935` made no convention slip.

#### `R83-22` — `B1939` overstates `1 + 4` torsion lines across `all 285 members` (eight bundles have `6 + 24` lines), misattributes quotes to `B862` and `B1221`, miscounts headline overstatements, and omits draft line `34`
- **File and line (`b35eac607`):** `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/FINDINGS.md`, line `52`
- **Verbatim quotation:** `"  is b+-LR = m003, the sister, with H₁ = ℤ ⊕ ℤ/5. On all 285 members of the lane's census, by two routes:"`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/FINDINGS.md`, line `1`: `"# B1939 — Five unharvested claims of the agy seats, recomputed on new code: three hold, two hold only as amended, and two overstatements on main's pages are found"`
  2. `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/FINDINGS.md`, line `54`: `"  - the four ramified lines are acyclic, with τ = ±ζᵐ(ρ(ℓ) − 1). So ∣τ∣ is 2 sin(π/5) or 2 sin(2π/5), and the product"`
  3. `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/FINDINGS.md`, line `84`: `"a choice the SM cannot make about itself"`
  4. `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/FINDINGS.md`, line `100`: `"The three wording mends are owed before WP-1.2 lands: lines 31 to 33 of its draft."`
- **What is wrong:** First, `torsion_census_run.txt` line `5` (`{2: 277, 3: 8}`) and `run2_census.json` show that only two hundred and seventy-seven of the two hundred and eighty-five census bundles have one cusp-unramified line and four ramified lines; the remaining eight (`εW ≡ I mod 5`, `H_1(M; F_5) ≅ F_5^3`) have six unramified fibre lines and twenty-four ramified mixed lines. Second, on line `84`, `'a choice the SM cannot make about itself'` stands in `docs/THE_CLAIM.md` line `28`, not in `B862`'s headline, while `'fixed by the algebra and the 27'` occurs nowhere in `B1221` (which already carries its `2026-08-31` primitivity addendum). Third, line `1` says `two overstatements`, whereas line `81` is singular (`The overstatement found on main's pages`) and `arc_verdict.json` line `33` counts one public grade plus two convention slips (one of which is false per `R83-21`). Fourth, in `docs/handoffs/MAIN_TO_BUILDER_2026-11-12/wp12/arc_draft/FINDINGS.md`, lines `31–33` are statements `B, C, D`, whereas the projective-versus-linear mend at `p = 2` is statement `E` on line `34`.

#### `R83-23` — `B1905` summary widens `W3`'s zero extremum/flow count to all walls and claims `W4` (`A count`) was settled `by census only`
- **File and line (`b35eac607`):** `frontier/B1905_selection_and_chirality_across_the_record/FINDINGS.md`, line `26`
- **Verbatim quotation:** `"  about the object's own structure; symmetry settles what cannot be split; an extremum, a flow or a measure has not"`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1905_selection_and_chirality_across_the_record/FINDINGS.md`, line `27`: `"  settled a wall."`
  2. `frontier/B1905_selection_and_chirality_across_the_record/FINDINGS.md`, line `80`: `"- **A count.** Settled by census only; three was looked for and does not occur where it was looked for."`
  3. `frontier/B1905_selection_and_chirality_across_the_record/FINDINGS.md`, line `133`: `"- Eleven rows had a kind written as one string where a list was asked; the script reads both."`
- **What is wrong:** In `sweep_tables_run.txt` and `rows.json.txt`, only wall `W3` (`A value`, line `78`) has zero settlements by extremum, flow, or measure. Across all walls, `A extremum` settled six of twenty-five arcs (`24 %`: `W1` one, `W2` two — stated on line `76` itself — `W7` one, `W8` two) and `G dynamics` (dynamics, flow, rate) settled three of nineteen (`16 %`: `W1` one, `W2` one, `W7` one); only `J measure` settled zero of twenty-four. On line `80`, wall `W4` (`A count`) has thirteen settled arcs, of which `B1497` settled `W4` with `['K other']` and no census at all, and eleven of the other twelve combine census with `C symmetry`, `K other`, or `H read-out`. Also on line `133`, `rows.json.txt` has zero live rows and one hundred and twenty-five `'neither'` rows (`'n/a'`) with `principle` as a string, not eleven; and lines `82–84` list seven pairs while saying `the eight most frequent pairs` (omitting `C+K: 13`).

#### `R83-24` — `B1938` states `No figure here uses unreduced ones`, whereas `residue_as_determinants.py` evaluates unreduced `c = (1.10, 0.20)`
- **File and line (`b35eac607`):** `frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/FINDINGS.md`, line `50`
- **Verbatim quotation:** `"- **Caveat.** Characteristics must be reduced mod ℤ² first; unreduced ones fail by up to 7e-2. No figure here uses"`
- **Supporting source line at `b35eac607`:**
  1. `frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/verification/residue_as_determinants.py`, line `33`: `"    for (a, b) in ((0.2 + .5, -0.4 + .5), (0.6 + .5, 0.2), (0.35, 0.15 + .5), (0.1, 0.7)):"`
- **What is wrong:** The second tuple `(0.6 + .5, 0.2) = (1.10, 0.20)` has `a = 1.10 >= 1` (`al = 0.6 > 1/2`) and is printed verbatim on lines `2, 6, 10` of `residue_as_determinants_run.txt` (`c=(1.10,0.20)`), contributing three of the twelve rows summarized in `FINDINGS.md` lines `48–49` without reduction modulo `Z^2` (it passed only because `b = 0.2` lies in `[0, 1)` while `a` enters `minus_zeta_prime0` solely via `exp(2 pi i n alpha)`).

---

### D. Stale Statuses, Sweep/Rule Omissions, and Scoreboard/Ledger Travel Defects

#### `R83-25` — `B1937` omits `S20` and leaves `S10` unmet in `BIG_RUN_RULE_v2.md`, counts `nine` joints for Frame C in `R1`, conflicts with `B1944`'s banking before `SM-C15`, and leaves `B1937/FINDINGS.md` and `arc_verdict.json` stale at `OPEN` / `Version 2 governs`
- **File and line (`b35eac607`):** `frontier/B1937_the_big_runs_rule_amended_before_the_look/verification/BIG_RUN_RULE_v2.md`, line `115`
- **Verbatim quotation:** `"*Written after the sweep listed 21 points that bear on the run"`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1937_the_big_runs_rule_amended_before_the_look/verification/BIG_RUN_RULE_v2.md`, line `50`: `"  - Any outcome is banked only after the look's second computation: a seat with the pinned files re-runs both scripts on"`
  2. `frontier/B1937_the_big_runs_rule_amended_before_the_look/verification/BIG_RUN_RULE_v2.md`, line `137`: `"| R1 | every ingredient listed and typed | met: frame C's nine joints, each typed (the scoreboard) |"`
  3. `frontier/B1937_the_big_runs_rule_amended_before_the_look/verification/BIG_RUN_RULE_v2.md`, line `168`: `"**A7. The conditions before the run (S8, S10, S11, S12, S14, S16).** The run waits for every one of these:"`
  4. `frontier/B1937_the_big_runs_rule_amended_before_the_look/FINDINGS.md`, line `3`: `"**Verdict: OPEN** (the run has not been made; the area options' second computation is owed). Main, 2026-11-14, after the"`
- **What is wrong:** First, despite line `115` saying each of `S1` to `S21` is met below or made a condition, `S20` (`THE_SWEEP_OF_2026-11-14.md` line `205`) appears nowhere in `BIG_RUN_RULE_v2.md`, and `S10` (`F̄` integrability at the four cusps of `X_1(5)` by proof/bound or else entered as an open premise) is listed in `A7`'s heading on line `168` yet never proved or entered as an open premise (`A7` treats only floating-point precision loss above height eleven). Second, line `137` counts `nine` joints (`C01`–`C09`), omitting the shared joints (`S01`–`S03`, twelve borrowed joints total). Third, `B1944` banked `NEGATIVE` (`PROVISIONAL`) before the look's second computation (`SM-C15`) ran, contrary to line `50` and `A14` (`lines 253–255`). Fourth, `B1937/FINDINGS.md` (`lines 3, 45, 72, 76`) and `arc_verdict.json` (`lines 3, 28`) remain at `OPEN`, `Version 2 governs`, and `A1 to A12`, stale against `BIG_RUN_RULE_v2.md` `A13`–`A15`, `B1940`, and `B1944`.

#### `R83-26` — `B1940` leaves `cites_seat: []` and `their second computation owed` in its header and `arc_verdict.json` contradicting its own `The second computation` section, and `compare_area_x_measure.py` shells out to unreachable commit `04293e826`
- **File and line (`b35eac607`):** `frontier/B1940_the_area_options_corrected_in_extended_precision/FINDINGS.md`, line `5`
- **Verbatim quotation:** `"once, their second computation owed). Main, 2026-11-14, before the big run's look. Register rows P-853, P-850, P-845."`
- **Supporting source lines at `b35eac607`:**
  1. `frontier/B1940_the_area_options_corrected_in_extended_precision/FINDINGS.md`, line `101`: `"- **Label:** the area options are recomputed independently (one seat)."`
  2. `frontier/B1940_the_area_options_corrected_in_extended_precision/arc_verdict.json`, line `24`: `"the corrected values computed once, their second computation owed"`
  3. `frontier/B1940_the_area_options_corrected_in_extended_precision/verification/compare_area_x_measure.py`, line `11`: `"04293e826:relays/x_measure_verify/verify_x_measure_out.json"`
- **What is wrong:** `B1940/FINDINGS.md` lines `94–101` enter the second computation (`X-MEASURE`, row `1826`), yet `FINDINGS.md` line `5`, `BIG_RUN_VALUES_v2.json` (`computed`), and `arc_verdict.json` lines `16, 24, 26` still state `cites_seat: []` and `their second computation owed`. Moreover, `compare_area_x_measure.py` line `11` runs `git show 04293e826:...` on a branch commit absent from a fresh single-branch clone of `main` (and is never tested by either `B1940` lock).

#### `R83-27` — `B1932` states `No value is compared with any measured number here` while `verification/big_run_output.json` is committed inside `B1932/verification/` (with four scriptless `_run.txt` files), and `B1935/arc_verdict.json` omits coincidences at `N = 2, 4`
- **File and line (`b35eac607`):** `frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/FINDINGS.md`, line `5`
- **Verbatim quotation:** `"2026-11-15. Register rows P-845 and P-848 [corrected 2026-11-14 (B1937): P-850, the big run's row; P-848 is Review 82's opening]. **No value is compared with any measured number here.** 0 of 19."`
- **Supporting source line at `b35eac607`:**
  1. `frontier/B1935_the_modular_group_permutes_the_frames_channels_as_s3_around_a_fixed_centre_and_the_sectors_coincide_only_at_line_orders_two_to_seven/arc_verdict.json`, line `25`: `"with the frame's charges, up and down coincide at 2, 3, 6, up and leptons (negated and transposed) at 7, down and leptons (transposed) at 5, and no two sectors at any order above 7."`
- **What is wrong:** Inside `B1932/verification/`, `big_run_output.json` is committed at `b35eac607` containing full measured-target `chi2_7`, pulls, and p-values (contradicting `B1932/FINDINGS.md` lines `5` and `59` and `arc_verdict.json` line `32`), and four committed `_run.txt` files (`dc_run.txt`, `pairs/q2_run.txt`, `interpolation_bias_run.txt`, `interpolation_check_run.txt`) have no committed `.py` producer scripts. Separately, in `B1935/arc_verdict.json` line `25`, `sector_coincidences_run.txt` lines `4–9` show `up` and `leptons` also coincide at `N = 2` (`equal` and `negated`), and `down` and `leptons` also coincide at `N = 2, 4` (`equal`) and `N = 2` (`negated`).

#### `R83-28` — `docs/TOTAL_INPUTS_SCOREBOARD.md` and `scripts/checks/inputs_scoreboard.py` still hardcode two frames (`both frames stand on it`) and slice `C02` and `C06` `basis` cells mid-word at three hundred characters
- **File and line (`b35eac607`):** `docs/TOTAL_INPUTS_SCOREBOARD.md`, line `13`
- **Verbatim quotation:** `"## The shared block (both frames stand on it)"`
- **Supporting source lines at `b35eac607`:**
  1. `scripts/checks/inputs_scoreboard.py`, line `49`: `"                other = "`
  2. `scripts/checks/inputs_scoreboard.py`, line `110`: `"[:300]))"`
  3. `docs/TOTAL_INPUTS_SCOREBOARD.md`, line `133`: `"| C02 | the line class of order 5: the ground's frustrated level | CHOSEN | 7 | | P-721 | GENESIS SE3 (POSTULATED, main's entry, counted in the budget): the ground is the act, its level 5. Given the premise that the frame's line is fixed by the act up to sign, the level is forced by THEOREM_REGISTRY T-THE-ACTS-FIXED-LINE (B1943: LR fixes up to sign exactly the four non-zero points of one |"`
  4. `docs/TOTAL_INPUTS_SCOREBOARD.md`, line `137`: `"| C06 | the channel weights sqrt(2 pi L + c_s) at that end | CHOSEN | 7 | |  | B1656's frame as banked; the exact horoball norms (A09) are not used; frame A's A09 [2026-11-14, before the look: the big run uses the exact channel weight N = 2 pi L_2 + c_s - pi ∣a0∣^2 e^{-2 L_2} (Theorem 90's leading form, B1838's note), which matches the exact horoball norm to about 1e-5; switch |"`
- **What is wrong:** `inputs_scoreboard.py` line `94` (`TOTAL_INPUTS_SCOREBOARD.md` line `13`) still says `both frames stand on it` and line `49` sets `other = 'A' if key == 'B' else 'B'` even though three frames (`A`, `B`, `C`) now stand on the board. Furthermore, line `110` slices `basis` at `[:300]`, chopping `C02` mid-sentence at `of one |` and `C06` mid-word at `switch |` (while `C06`'s joint name on lines `137` and `144` still reads `sqrt(2 pi L + c_s)` after the run switched to Theorem Ninety's exact weight).

#### `R83-29` — Scoreboard changes (`S03` added, `C02` re-typed, Frame C added) did not travel to `THE_PAIRS_PROGRAMME.md`, `B1858/MAP.md`, `B1834`, or `B1861`
- **File and line (`b35eac607`):** `docs/THE_PAIRS_PROGRAMME.md`, line `96`
- **Verbatim quotation:** `"C02 (the order-5 line) is forced given SE1, and C05 is settled (K4)."`
- **Supporting source lines at `b35eac607`:**
  1. `docs/THE_PAIRS_PROGRAMME.md`, line `180`: `"chosen joints in frame C, now nine plus one ansatz."`
  2. `frontier/B1858_the_closure_map/MAP.md`, line `125`: `"## 5. The values (the scoreboard's two frames)"`
  3. `frontier/B1834_the_total_inputs_scoreboard/arc_verdict.json`, line `26`: `"[REVIEW 75 NOTE: the counts are as of S300c; the live scoreboard (frame A 6 rows and 13 joints, frame B 44, F7 FORCED-BY-MAIN) is in docs/TOTAL_INPUTS_SCOREBOARD.md.]"`
  4. `frontier/B1861_the_closure_programme/FINDINGS.md`, line `127`: `"- **The kinds follow the record's own grades,** and the builder checks them: the scoreboard's 13 borrowed joints of the"`
- **What is wrong:** After `B1943` added shared joint `S03` (`SE1`) and re-typed `C02` as `CHOSEN` resting on postulate `SE3`, `THE_PAIRS_PROGRAMME.md` line `96` still calls `C02` `forced given SE1` and line `180` still gives Frame C `nine plus one ansatz` instead of eleven chosen plus one ansatz (`12` borrowed joints; `P-855` on `POINT_REGISTER.md` line `1067` notes staleness only against `B1934` and `B1935`, missing `B1943`). Likewise, `B1858/verification/build_map.py` lines `143–149` and `351` (`MAP.md` line `125`) read only `A` and `B` (`the scoreboard's two frames`), omitting Frame C (`C01`–`C09`) completely; and `B1834` (`FINDINGS.md` line `98`, `arc_verdict.json` line `26`) and `B1861` (`FINDINGS.md` lines `127–129, 189`, `test_b1861_the_closure_programme.py` line `186`) still state `13 borrowed joints` (`10 chosen`) and `frame B 44` instead of `14` (`11 chosen`) and `45`.

#### `R83-30` — `docs/HARVEST_LEDGER.md` pin table lags behind rows harvested in the same file
- **File and line (`b35eac607`):** `docs/HARVEST_LEDGER.md`, line `30`
- **Verbatim quotation:** `"2026-11-14 (S306p, night): rows 1820 to 1822 (W-F22 and W-F23 read in full; W-F17's addendum 2 registered)"`
- **Supporting source line at `b35eac607`:**
  1. `docs/HARVEST_LEDGER.md`, line `40`: `"2026-11-12 (S306p, Review 80's landing): rows 1737 and 1741"`
- **What is wrong:** Line `30` pins `chat1` at `fa1f2abd` (`rows 1820 to 1822`) even though lines `1877–1878` of the same file harvest rows `1824` (`@ 70fd6912`) and `1825` (`@ 135a2d5b`); and line `40` leaves `agy002` pinned at `4ae026d9` (`2026-11-12`, rows `1737 and 1741`) while rows `1789–1791`, `1795`, `1796`, `1801`, and `1807` from `2026-11-14` stand harvested in the table below.

#### `R83-31` — `docs/THE_CLAIM.md` line `28` retains unconditional `DERIVED` on `[SU(3)×SU(2)×U(1)]/ℤ₆` after `B1939` and `P-803`, and `THE_SWEEP_OF_2026-11-14.md` / `P-851` state `B1900 to B1937` where `B1899`–`B1903` do not exist
- **File and line (`b35eac607`):** `docs/THE_CLAIM.md`, line `28`
- **Verbatim quotation:** `"> | the **global form [SU(3)×SU(2)×U(1)]/ℤ₆** — *a choice the SM cannot make about itself* | **DERIVED** | B862 |"`
- **Supporting source lines at `b35eac607`:**
  1. `docs/THE_SWEEP_OF_2026-11-14.md`, line `4`: `"pages and relays since 2026-11-12, and main's arcs B1900 to B1937 with the planning pages. They listed every lead, owed"`
  2. `docs/THE_SWEEP_OF_2026-11-14.md`, line `218`: `"- **Point:** Main's five draft arcs of 2026-11-12, reserved as B1899 to B1903, were never built or landed:"`
- **What is wrong:** First, despite `B1939` (`FINDINGS.md` lines `81–87`, `arc_verdict.json` line `33`) identifying the unscoped `DERIVED` grade on `[SU(3)×SU(2)×U(1)]/ℤ₆` as an overstatement on `main`'s pages (requiring faithful `27` + primitivity), `docs/THE_CLAIM.md` line `28` remains unamended at `b35eac607`. Second, `docs/THE_SWEEP_OF_2026-11-14.md` line `4` and `docs/POINT_REGISTER.md` line `1063` (`P-851`) say `main's arcs B1900 to B1937`, whereas `S34` on lines `218–220` and the footer on line `1036` (`B1904-B1937`) state that `B1899` to `B1903` were never built or landed, so the swept range begins at `B1904`, not `B1900`.

---

## 2. Independent Recomputations and Cleanly Verified Items (`relays/r83/` at `827ba35d8`)

1. **`B1940` (`τ -> τ + 1` check and extended-precision frame, `verify_r83_counterchecks.py` check one):** Recomputed independently in pure fifty-five-digit `mpmath` across heights `1.5` to `200` (`1.5, 3, 6, 9, 11, 12, 15, 20, 30, 45, 80, 120, 200`): `F̄(τ + 1) = F̄(τ)` holds to two point two three times ten to the minus fifty-five (`2.23e-55`, and `1.11e-16` after float conversion), whereas double precision breaks above height eleven (`0.0833` at `y = 12`, `0.3333` at `y = 30`). All sha256 seals in `B1940` match.
2. **`B1942` and `SM-C13` (`verify_r83_counterchecks.py` check two):** Recomputed independently at forty-five digits: at order five, `leptons == down^T` holds with zero discrepancy (`0.0`); at order fifteen, `w -> 6w` maps the one hundred and ninety-two exact-order-fifteen points onto the twenty-four order-five points with uniform multiplicity eight (`[8, 8]`, catching `R83-04`), and `lep(order 15) == down(order 5)` to `0.0` across three moduli while planted charge `(-2, 6)` breaks equality by `0.0344`.
3. **`B1943` (`verify_r83_counterchecks.py` check three and `verify_r83_extra_checks.py`):** Confirmed `Smith(LR - I) = (1, 1)` and `Smith(LR + I) = (1, 5)` (catching `R83-05`), exhaustive `N = 2..60` fixed-up-to-sign torsion enumeration for `LR` (`{k(1, 2)/5}`), `(LR)^T`, `(LR)^-1`, and `RL` (`{k(1, 3)/5}`, catching `R83-20`), plus `LRR` control orders `[2, 3, 6]`.
4. **`B1934`, `B1935`, `B1936` (`verify_r83_counterchecks.py` check four):** Recomputed level-five Weil representations (`k = 1, 2`, order `120`, `3 + 2` block error `0.0`, `det = 1`, golden traces, `-I = -1` on doublet), Legendre symbol hand on all thirty-two elements `±J^n K^e` at `(1, 2)` (`32/32` vs planted `6/32` at `(1, 1)`), `B1935` `S_3` channel permutations, exact `{1/8, 3/8, 7/8}` `T`-eigenphases (`2.3e-15`), `N = 2..60` sector coincidences, and `B1936` exterior degrees `k = 2(6Y) mod 5`.
5. **`B1938` (`verify_r83_counterchecks.py` check five):** Recomputed Poisson-Mellin identity `|ϑ[c](0)/η|^2 = det Δ_χ` (`χ = c - (1/2, 1/2)`) at fifty digits, matching to two point six three times ten to the minus forty-six (`2.63e-46`, planted `χ = c` failing by `0.3006`), `∑_s R_s^2 = 0` to `2.12e-16`, and `R_1(up) = 0` at order five to `2.45e-16`.
6. **`B1930`, `B1931`, `B1933`, `B1937` scripts, `B1944` scripts, `THE_SWEEP_OF_2026-11-14.md`, and `P-849`–`P-857` (noting `POINT_REGISTER.md` at `b35eac607` ends at `P-857` on line `1069`):** `B1930` (`v1.68` archived paths), `B1931` (`plants.py` sha256 `c6014cdd…` and Review 82 window mends), and `B1933` (`v1.69` `m000` entry) verified clean; `B1937` calibration/tolerance scripts and `B1944` `chi2_seven` figures verified from committed json outputs without touching external measured data outside `main`'s committed files (Section Nine Point One).

0 of 19.
