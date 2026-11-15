# Review 83 — Blind Reading at `b35eac607` (`agy-exp`, Card `R83`)

- **Seat / Session:** `agy-exp`
- **Branch:** `agy/self-consistent-loop-2026-11-11`
- **Card (Commit One):** `relays/cards/AGY-EXP_R83_review-83.md` (`cbefe4cc8`)
- **Verifier Script (Commit Two, sealed before execution):** `relays/r83_verify/verify_r83.py` (`fe6f74fbf` / final pre-output commit `d4f1345eb`, SHA-256 `81af28f501df48c0421c2de7e44a3aaff7372a5f24c686dc678615a1b0167628` in `relays/r83_verify/SCRIPT_SHA256.txt`)
- **Raw Output (Commit Three, committed unread):** `relays/r83_verify/verify_r83_out.json` (`60ef4d38d`, SHA-256 `86bde5e7b99057eae3fd85a229d5414c32f4b9e9e8c94443739735e611752aac` in `relays/r83_verify/OUTPUT_SHA256.txt`)
- **Pinned Commit Read:** `b35eac607` (`b35eac607d35ef1a5cffb78d0d5fb32b6e9d6b56` on `origin/review-83/read`), with window diff base `73e71e277` where window differences apply
- **Blind-Test Isolation:** `b35eac607` was never diffed or compared against `c8cece9be` or `origin/main`, and no other session's branch or review file was opened or listed before pushing this report.
- **Pre-Output Amendments & Control Disclosure:** Two text-pattern fixes (`00de0c150` matching `s4_pointwise_run.txt` and `read_the_look_run.txt` line layout; `d4f1345eb` matching backticked `B1937` and `B1944` cells in `BLIND_ARCS.md`), both committed strictly before `verify_r83_out.json` existed; zero post-output script edits. Pre-registered negative controls `C-R83-1` (`passed == true`), `C-R83-2` (`passed == true`), and all three pre-registered clauses of `C-R83-3` (`single_line_breaks_invariance == true`, `binary64_breaks_at_y20 == true`, `mpmath_exact_rational_holds_to_1e55 == true`) passed, as did `quote_verification.all_exact == true` (`twenty of twenty` exact line matches) and all fifteen `B1930`–`B1944` baseline locks (`fifteen of fifteen` in our pure-mathematics sandbox). An optional fourth sub-check added inside `C-R83-3` (`binary64_float_arg_reproduces_1e18_floor`) returned `false` because `eval_frame_mp` parsed float inputs via `repr(float)` decimal strings at fixed `L2_test` rather than IEEE binary64 mantissas with `CR.canon` interpolation, leaving `all_controls_passed` false in `verify_r83_out.json`; the sealed Commit Three output is kept untouched.
- **Empirical Firewall:** `0 of 19.`

---

## 1. Recusals, Empirical Firewall Boundaries, and Items Not Checkable at `b35eac607` (`docs/seats/README.md` §§ 9, 13)

1. **`agy-exp` own work (recused from mathematical evaluation):**
   - `B1931`: clauses evaluating `agy-exp`'s Review `82` delivery (`R82`).
   - `B1933` and `GENESIS.md`: the substance of `X-NEVER` (`harvest row 1797`).
   - `B1937` and `B1940`: `X-CANON`, `X-EXACT-W`, `X-MEASURE`, `X-SURVIVAL`, `X-OWN`, and `X-SCAR` (`harvest rows 1793, 1794, 1802, 1808, 1811, 1814, 1816, 1818`).
   - `B1939`: § `1` (`X-C2`, `harvest row 1814`) as to `agy-exp`'s claim itself, while checking `main`'s own scripts, `FINDINGS.md`, `arc_verdict.json`, and `test_b1939_five_claims.py` under `B1931` (`R82-4`).
   - `THE_SWEEP_OF_2026-11-14.md`, `POINT_REGISTER.md`, and `HARVEST_LEDGER.md`: harvest rows `1776, 1777, 1788, 1792, 1797, 1798, 1799, 1800, 1802, 1812, 1815, 1816, 1817` and clauses evaluating `agy-exp` or `agyloop`.
2. **Own model-family work (`agy-002` and `the agy lane`, recused from judging the seat's work itself):**
   - `B1931` (`A2-R82`), `B1932` (`A2-CANON`, `A2-OWN1`), `B1937` (`A2-MOVE`, `A2-AMP`), `B1939` §§ `2`–`5` as to the lane/seat claims themselves, `B1940` (`A2-AREA`), `THE_SWEEP_OF_2026-11-14.md` entries on `agy-002` and `the agy lane`, and harvest rows `1676`–`1678`, `1696`, `1709`, `1710`, `1749`, `1789`, `1790`, `1791`, `1795`, `1796`, `1801`, `1807` — while auditing `main`'s own scripts, `main`'s `FINDINGS.md` against `main`'s `_run.txt` outputs, `main`'s locks, and `main`'s propagation and check-label hygiene.
3. **Register row `P-858` (`cannot check` at `b35eac607`):**
   - At `b35eac607`, `docs/POINT_REGISTER.md` ends at `P-857` (`P-858`, which hashes Review `83`'s six planted faults on `main`, was added after `b35eac607` was branched and is left untouched under blind-test isolation).
4. **Empirical comparison numbers (`cannot check` under `0 of 19`, `docs/seats/README.md` § 9):**
   - `B1612`, `B1637`, and `B1720` were excluded from our pure-mathematics sandbox (`forbidden_empirical_dirs_present == 0`), historical comparison scripts were deleted before running any lock, and no measured physical value was opened or reconstructed from pulls. In `B1944` (and `P-857`), empirical comparison figures against measured targets are marked `cannot check` as to the measured data, while every pure-mathematical identity, committed `_run.txt` vs `FINDINGS.md` transcription, pure-math monotonicity relation across `BIG_RUN_VALUES_v2.json`, amendment `A1`–`A15`, lock assertion, and governance rule is audited below.

---

## 2. Machine-Checked Findings at `b35eac607` (`F-R83-01` through `F-R83-20`)

Every quotation block below contains the exact full line at `b35eac607` verified by `verify_r83.py` (`quote_verification.all_exact == true`, twenty of twenty exact matches in `relays/r83_verify/verify_r83_out.json`).

### Finding F-R83-01 — `B1938/FINDINGS.md` reports `max |z|` as two and four-tenths where `gauge_class_control_run.txt` prints six and four-tenths (below the script's own catch bar of three)

- **Arc:** `B1938`
- **File:** `frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/FINDINGS.md:83`
- **Line:** `83`
- **Commit read:** `b35eac607`
- **Criterion:** `2` (a number that differs from its source and contradicts the control's own catch threshold)

```text
  truncation's ~1 %. They do: max |z| 2.4, so the comparison would have seen a 1 % effect.
```

- **What is wrong and how we know:** `verification/gauge_class_control_run.txt:1` prints `max |z|` equal to six and four-tenths (`-> CAUGHT`, matching `B1938/arc_verdict.json:27` and `docs/POINT_REGISTER.md:52` under `P-850`). Under `verification/gauge_class_control.py:25`, the control catches an effect only when `max |z|` exceeds three, so line `83`'s figure of two and four-tenths would have been `MISSED` rather than caught (`M_B1938_control_run_max_z_is_6_4_not_2_4 == true` in `verify_r83_out.json`). `test_b1938_coupling_and_gauge_class.py:46` to `52` missed this because it cross-checks `FINDINGS.md` only against `gauge_class_readout_run.txt`, never against `gauge_class_control_run.txt`.

### Finding F-R83-02 — `B1940/FINDINGS.md` swaps digits on the largest logarithmic shift, printing eighty-six thousandths instead of sixty-eight thousandths

- **Arc:** `B1940`
- **File:** `frontier/B1940_the_area_options_corrected_in_extended_precision/FINDINGS.md:73`
- **Line:** `73`
- **Commit read:** `b35eac607`
- **Criterion:** `2` (a number that differs from its source and contradicts line `69` and `arc_verdict.json`)

```text
  The largest change, 0.086 in ln, is about two-thirds of the run statistic's σ floor of 0.10. So it was material.
```

- **What is wrong and how we know:** Direct recomputation of $|\ln(v_{\mathrm{new}}/v_{\mathrm{old}})|$ across all options and entries between `BIG_RUN_VALUES_v2.json` and `B1932`'s `BIG_RUN_VALUES.json` gives a maximum magnitude just under sixty-eight thousandths (matching `FINDINGS.md:69`, `B1940/arc_verdict.json:26`, `BIG_RUN_RULE_v2.md:231`, `assemble_values_v2_run.txt`, and `P-853`), whereas line `73` transposes the last two digits to eighty-six thousandths — which is nearly nine-tenths, not two-thirds, of one-tenth (`M_B1940_actual_max_dln_is_0068_not_0086 == true`).

### Finding F-R83-03 — `B1941/FINDINGS.md` transposes digits in row one's minimum column, printing plus one and eighty-three hundredths where `s4_pointwise_run.txt` has plus one and thirty-eight hundredths

- **Arc:** `B1941`
- **File:** `frontier/B1941_a_fermion_determinant_prefers_one_higgs_world_at_every_point_and_a_one_loop_trace_the_other/FINDINGS.md:33`
- **Line:** `33`
- **Commit read:** `b35eac607`
- **Criterion:** `2` (a table figure that differs from its run file)

```text
| ln det, colour weights (3, 3, 1), exact weight | **28 of 28** | +1.83 | +6.44 |
```

- **What is wrong and how we know:** `verification/s4_pointwise_run.txt:7` (`ln det, weights 3,3,1, exact weight`) prints a minimum near plus one and thirty-eight hundredths (matching the truncated-weight row right below on `FINDINGS.md:34` and `B1941/arc_verdict.json:19`), whereas line `33` swaps the digits after the point to plus one and eighty-three hundredths (`M_B1941_run_min_is_1_381_not_1_83 == true`). `test_b1941_s4_pointwise.py` missed this because it checks only the integer point counts (`28 of 28`, `0 of 28`) and ignores the `Δ from` and `to` columns.

### Finding F-R83-04 — `B1942/FINDINGS.md` states that $w \mapsto 6w$ hits each order-five point six times instead of eight times ($192 / 24 = 8$), writes `mod 5` on rational torsion points, and leaves two table rows unlocked

- **Arc:** `B1942`
- **File:** `frontier/B1942_at_level_fifteen_the_leptons_keep_the_order_five_down_rows_and_the_quarks_move/FINDINGS.md:23`
- **Line:** `23`
- **Commit read:** `b35eac607`
- **Criterion:** `2` and `1` (a fiber multiplicity off its source and exact arithmetic, plus `mod 5` for `mod 1` on lines `21`–`22`)

```text
- **Averaging.** The map w ↦ 6w takes the 192 points of exact order 15 onto the 24 of order 5, each hit six times. So the leptons'
```

- **What is wrong and how we know:** There are $15^2 - 5^2 - 3^2 + 1 = 192$ points of exact order fifteen and $5^2 - 1 = 24$ points of exact order five in $(\mathbb{Q}/\mathbb{Z})^2$, and $192 / 24 = 8$, not six: every order-five point has fiber size eight corresponding to the eight primitive order-three shifts (`M_B1942_is_8_to_1_not_6_to_1 == true`, matching `level15_run.txt:2`, `B1942/arc_verdict.json:21`, and `test_b1942_level_fifteen.py:20` which asserts `{8}` without reading `FINDINGS.md`). In addition, `FINDINGS.md:21` to `22` writes `mod 5` on torsion elements $v, v' \in (\frac{1}{5}\mathbb{Z}/\mathbb{Z})^2$ where congruence holds `mod 1` (modulo $\mathbb{Z}^2$), and `test_b1942_level_fifteen.py:24` to `28` checks neither the `E3` first-sector movement claim nor third-sector versus second-sector separation at level fifteen.

### Finding F-R83-05 — `B1943/FINDINGS.md` prints `Smith(LR + I) = (1, 3)` instead of `(1, 5)`, and line `22`'s `"The same holds for RL"` leaves `RL` tied to `LR`'s un-swapped line

- **Arc:** `B1943`
- **File:** `frontier/B1943_the_act_fixes_one_line_of_order_five_and_the_foundations_two_postulates_enter_the_count/FINDINGS.md:21`
- **Line:** `21`
- **Commit read:** `b35eac607`
- **Criterion:** `2` and `1` (an invariant factor off its source and exact determinant, plus an imprecise fixed-set carry to `RL`)

```text
- **The Smith forms.** Smith(LR − I) = (1, 1) and Smith(LR + I) = (1, 3).
```

- **What is wrong and how we know:** For $LR = \bigl(\begin{smallmatrix}2 & 1 \\ 1 & 1\end{smallmatrix}\bigr)$, $LR + I = \bigl(\begin{smallmatrix}3 & 1 \\ 1 & 2\end{smallmatrix}\bigr)$ has $\gcd(3, 1, 1, 2) = 1$ and $|\det(LR + I)| = 6 - 1 = 5$, so $\operatorname{Smith}(LR + I) = (1, 5)$, matching `fixed_lines_run.txt:1` and `B1943/arc_verdict.json:19` (`M_B1943_smith_LR_plus_I_is_1_5_not_1_3 == true`; `(1, 3)` would fix points of order three rather than order five!). Furthermore, line `19` names the explicit eigenline `{(1/5, 2/5), (2/5, 4/5), (3/5, 1/5), (4/5, 3/5)}` and line `22` immediately says `The same holds for RL, (LR)ᵀ, (LR)⁻¹ and ((LR)ᵀ)⁻¹`, whereas `RL = (LR)ᵀ` fixes the distinct swapped line `{(2/5, 1/5), (4/5, 2/5), (1/5, 3/5), (3/5, 4/5)}` (`M_B1943_RL_fixes_swapped_line == true`).

### Finding F-R83-06 — `B1944/FINDINGS.md` drops the leading digit `1` in row `W₊∣b`'s sixth ratio cell (printing seven and six-tenths where `read_the_look_run.txt` prints seventeen and six-tenths), while `test_b1944_the_look_read.py` leaves forty-eight of fifty-two table cells unlocked

- **Arc:** `B1944`
- **File:** `frontier/B1944_the_big_run_read_frame_c_fails_and_the_average_washes_out_the_hierarchy/FINDINGS.md:56`
- **Line:** `56`
- **Commit read:** `b35eac607`
- **Criterion:** `2` and `4` (a table figure off its committed output, and a lock that fails to check ninety-two percent of the table it claims to hold)

```text
  | W₊∣b | 59.3 | 3 310 | 11.3 | 15.6 | 1.21 | 7.6 | 80.9 |
```

- **What is wrong and how we know:** `B1944/verification/read_the_look_run.txt:9` prints seventeen and six-tenths in that sixth ratio slot for `W+|b (area)`, whereas `FINDINGS.md:56` drops the leading `1` (`M_B1944_run_txt_has_17_6_not_7_6 == true`). Independently and purely inside `BIG_RUN_VALUES_v2.json` (`0 of 19`: touching zero measured quantities), `W+|b (area)`'s index-`5` entry strictly exceeds `W-|b (area)`'s positive index-`5` entry (`M_B1944_pure_monotonicity_wpb_gt_wmb == true`), so dividing both by any positive denominator forces `W+|b`'s ratio strictly above `W-|b`'s sixteen and six-tenths on line `54`, making line `56`'s figure algebraically impossible. Despite `test_b1944_the_look_read.py:2` claiming `and the page's table is the outputs' figures`, lines `15`–`16` check only `chi2_seven` (`4` of `52` table cells across the two tables); corrupting all seven cells of line `56` in our sandbox leaves `test_b1944_the_look_read.py` passing (`mut_b1944_48_cells_corrupted_still_passes == true`).

### Finding F-R83-07 — Scoreboard joint `S03` falsely states that torsion-free first homology (`SE1`) selects `m003` alongside `m004` and `m000`

- **Arc:** `B1943` (`docs/TOTAL_INPUTS_SCOREBOARD.md`, `docs/total_inputs_scoreboard.json`, `docs/atlas/MAP.md`, `docs/atlas/NODES.json`)
- **File:** `docs/TOTAL_INPUTS_SCOREBOARD.md:19`
- **Line:** `19`
- **Commit read:** `b35eac607`
- **Criterion:** `1` and `3` (mathematically false inclusion of `m003`, contradicting `GENESIS.md` `SE1` and `T-ROOT`)

```text
| S03 | the root: the act's first homology torsion-free (SE1), which selects the class of LR (m004, m003) and that of LP (m000) | CHOSEN | GENESIS SE1 (POSTULATED; UNIQUENESS A5); what it selects is derived (T-ROOT). [2026-11-14, B1943: added; the foundation's postulate was counted nowhere on this board] | |
```

- **What is wrong and how we know:** `m003` (the sister manifold) has monodromy $-LR$ ($\det = +1$, $\operatorname{tr} = -3$), so its first homology torsion is given by $\operatorname{Smith}(-LR - I) = \operatorname{Smith}\bigl(\begin{smallmatrix}-3 & -1 \\ -1 & -2\end{smallmatrix}\bigr) = (1, 5)$, i.e. $H_1(\text{m003}; \mathbb{Z}) \cong \mathbb{Z} \oplus \mathbb{Z}/5\mathbb{Z}$, which is **not** torsion-free (`M_S03_m003_H1_torsion_is_5_not_1 == true`)! `GENESIS.md:219` to `220` (`SE1: the root's` — not `"the act's"` — `first homology is torsion-free`, and `test_the_terms_in_short.py:34` to `35`) explicitly derives that `SE1` holds **only** for the conjugacy class of $+LR$ (`m004`) and that of $LP$ (`m000`), and **excludes** `m003`. This false `S03` string (`docs/total_inputs_scoreboard.json:50`) also propagated into `docs/atlas/MAP.md:54` and `docs/atlas/NODES.json`.

### Finding F-R83-08 — `B1944`'s scoreboard update writes a point-zero threshold literal into `TOTAL_INPUTS_SCOREBOARD.md` and `total_inputs_scoreboard.json`, breaking `test_b1834_the_total_inputs_scoreboard.py` live at `b35eac607`, while Frame C's `basis` cells are silently truncated mid-phrase

- **Arc:** `B1944` (`docs/TOTAL_INPUTS_SCOREBOARD.md`, `docs/total_inputs_scoreboard.json`, `B1834`, `B1943`)
- **File:** `docs/TOTAL_INPUTS_SCOREBOARD.md:122`
- **Line:** `122`
- **Commit read:** `b35eac607`
- **Criterion:** `4` and `5` (live lock failure at `b35eac607`, un-updated Frame C assertion in `test_b1834`, stale two-frame headings, and truncated `basis` cells)

```text
*Status:* a structural frame, no value claimed (2026-11-14): no FITTED input; tau and the line are not inputs of it (B1928 PROVED); its values are computed (B1928's integral, in the json only) and NOT sealed; the canonical end's numbers are owed a second computation (agy-002's A2-CANON) before any seal. The lepton rows are not claimed: at level 5 the lepton coupling is the down coupling transposed (six times the hypercharge mod 5 is constant on SU(5)'s multiplets), minimal SU(5)'s relation, which the record already notes the measured Georgi-Jarlskog split forbids (B1839's arc, CHANGELOG); a level or structure separating them is owed (P-845). J's sign is not claimed: the tick involution flips it (agy-002's A2-OWN1), so it needs the hand. [2026-11-14, later: the values are committed and sealed (B1932) before their second computations, a corrected file to be sealed beside them if one disagrees; the run waits until every option has an agreeing second computation; the move-count options have one (B1937)] [2026-11-15: READ under the sealed rule (B1944): FAIL in every option, best chi2_7 6 679 against 22.0, the worst claimed row off by a factor of 3 314 or more; PROVISIONAL until its second computation (SM-C15); the frame's average has no hierarchy steep enough].
```

- **What is wrong and how we know:**
  1. Writing the point-zero threshold literal after `against` in `docs/total_inputs_scoreboard.json:1471` and `docs/TOTAL_INPUTS_SCOREBOARD.md:122` causes `frontier/B1834_the_total_inputs_scoreboard/verification/test_b1834_the_total_inputs_scoreboard.py::test_no_value_is_recorded` (`lines 27`–`33`) to **fail live** at `b35eac607`, and replacing that single string makes the entire `B1834` lock pass (`b1834_fails_live_at_b35eac607 == true`, `b1834_passes_once_22_0_stripped == true`).
  2. `B1943` updated the comment at `test_b1834_the_total_inputs_scoreboard.py:23` yet left line `24` asserting only Frames A and B (`6 rows claimed, 14 borrowed joints` and `23 rows claimed, 45 borrowed joints`), omitting Frame C (`7 rows claimed, 12 borrowed joints`). Meanwhile `TOTAL_INPUTS_SCOREBOARD.md:11` and `13` (`scripts/checks/inputs_scoreboard.py:91`) still say `counted in both frames` and `both frames stand on it` when three frames (`A`, `B`, `C`) stand on the board, and `inputs_scoreboard.py:48` (`other = "A" if key == "B" else "B"`) hardcodes two frames in `same_as` validation.
  3. `inputs_scoreboard.py:107` slices `basis` to `[:300]`, cutting `C02` (`TOTAL_INPUTS_SCOREBOARD.md:133`) off mid-phrase at `of one |` and `C06` (`line 137`) at `; switch |` (`scoreboard_c02_and_c06_truncated_at_300_chars == true`), while `C06`'s `name` column still prints the old truncated weight `sqrt(2 pi L + c_s)` after `B1932` switched Frame C to Theorem `90`'s exact weight.

### Finding F-R83-09 — `test_b1932_values_and_seal.py` loads `area_measure.json` into an unused variable `a` and never checks `BIG_RUN_VALUES.json`'s area options, while `B1932/FINDINGS.md` misstates three output ranges and is left without a supersession note after `B1940` and `B1944`

- **Arc:** `B1932`
- **File:** `frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/test_b1932_values_and_seal.py:22`
- **Line:** `22`
- **Commit read:** `b35eac607`
- **Criterion:** `4`, `2`, and `5` (an assembly lock that cannot fail on corrupted area values, three numerical summary mismatches in `FINDINGS.md`, and untravelled `B1940`/`B1944` updates)

```text
    e = json.loads((HERE / "ergodic_both_worlds.json").read_text()); a = json.loads((HERE / "area_measure.json").read_text())
```

- **What is wrong and how we know:**
  1. Variable `a` on line `22` is never referenced anywhere in `test_the_values_are_the_assembly_of_the_kept_runs`: lines `23`–`24` check `W-|a` and `W+|a` against `e`, leaving `W-|b (area)` and `W+|b (area)` (and all `"error"` arrays) completely unchecked against `area_measure.json`. Corrupting all seven entries of both `W-|b (area)` and `W+|b (area)` in `BIG_RUN_VALUES.json` (with matching seal hash) leaves the entire `test_b1932_values_and_seal.py` suite green, whereas corrupting `W-|a (move count)` fails immediately (`mut_b1932_area_corrupted_still_passes == true`, `mut_b1932_move_corrupted_caught == true`).
  2. In `B1932/FINDINGS.md`: line `33` says `5 to 11 times the sampling error` where `ergodic_t90_run.txt:7` gives four shifts above three sampling errors starting near three and one-quarter and reaching eleven and one-half; line `41` states unqualified that the area measure moves every ratio lower by one-tenth to fifty-eight hundredths in logarithm (true in `W-`, false in `W+` where the seventh ratio slot moves by about seventy-three thousandths); and line `47` quotes the constant-end mirror residual (`eight parts in one hundred billion`, `pairs/q2_run.txt:1`) as canonical `L_2`'s residual (`twenty-five parts in one million`, `pairs/q2_run.txt:2`).
  3. `B1944` later wrote `verification/big_run_output.json` inside `B1932/verification/`, falsifying `B1932/FINDINGS.md:5` and `59` (`No value is compared with any measured number here; nothing is run against the targets`) and `test_b1932_values_and_seal.py:4` (`writes nothing in the arc`), and `B1940`'s extended-precision correction of `B1932`'s area values left no dated supersession note on `B1932/FINDINGS.md` or `B1932/arc_verdict.json` (`superseded_by: null`).

### Finding F-R83-10 — `test_b1934_level_five_structure.py` omits the Weil phase `-1` on `S`, so line `22` passes even when line `20`'s planted linear `T` is replaced by the true quadratic `T`

- **Arc:** `B1934`
- **File:** `frontier/B1934_level_fives_weil_representation_lies_in_su3_x_su2_and_the_hand_is_the_golden_fields_quadratic_character/verification/test_b1934_level_five_structure.py:21`
- **Line:** `21`
- **Commit read:** `b35eac607`
- **Criterion:** `4` and `1` (a planted negative test whose twin fails because `S` is missing `-1`, plus omission of `N = 1` on `FINDINGS.md:52`)

```text
    S = np.array([[L.W ** (x * y) for y in range(L.P)] for x in range(L.P)]) / np.sqrt(L.P)
```

- **What is wrong and how we know:** In `level_five.py:18`–`24`, the genuine $\mathrm{SL}(2, \mathbb{F}_5)$ Weil representation of order `120` requires the eighth-root scalar phase $j = 4$ (`-1`), i.e. $S_{\mathrm{Weil}} = -S$. Because line `21` omits that `-1` factor, replacing line `20`'s planted linear `T` with the genuine quadratic `T = diag(W**(x*x))` generates $C_2 \times \mathrm{SL}(2, \mathbb{F}_5)$ of order **`240`**, which still satisfies `len(L.generate([S, T])) != 120` on line `22` (`M_B1934_unphased_S_with_quadratic_T_order == 240`, `M_B1934_minus_S_with_quadratic_T_order == 120`, `M_B1934_test_passes_even_when_T_unplanted == true`). In addition, `B1934/FINDINGS.md:52` writes `except when N divides 5, which is N = 5` (omitting $N = 1$, which divides `5` and trivializes all three twists to `(0, 0)`), and lines `27`–`32` state basis-dependent coordinate-block and $\mathrm{SO}(3)$ claims without noting unitary conjugation between bases.

### Finding F-R83-11 — `B1935/FINDINGS.md` claims the modular group acts on the four channels as $S_3$ of order six, whereas the complex channel residues $R_s$ carry relative minus signs generating $S_4$ of order twenty-four (only $|R_s|$ permutes as $S_3$)

- **Arc:** `B1935`
- **File:** `frontier/B1935_the_modular_group_permutes_the_frames_channels_as_s3_around_a_fixed_centre_and_the_sectors_coincide_only_at_line_orders_two_to_seven/FINDINGS.md:25`
- **Line:** `25`
- **Commit read:** `b35eac607`
- **Criterion:** `1` and `4` (a statement wider than the modulus check in `channels_and_centre.py`, and missing lock plants on Claims `2`–`4`)

```text
The two swaps generate S₃ on {i, j, k}; channel 1 is fixed by both. **The modular group acts on the frame's four
```

- **What is wrong and how we know:** `verification/channels_and_centre.py:27` took absolute values `abs(...)` before comparing channels. In `B1656` and Frame C, the fibre coupling matrix is linear in the **complex** residues $R_s(c, \tau)$. Evaluating $(R_1, R_i, R_j, R_k)$ in `mpmath` under `B1935`'s own modular moves (`channels_and_centre.py:39`) and dividing out channel `1`'s common modular factor (noting that `verify_r83.py` wrote `b + a` instead of `channels_and_centre.py`'s `b - a` in `M_B1935_signed_channel_laws_hold`):
  - $T$: $(\tau, a, b) \mapsto (\tau + 1, a, b - a)$ sends $(R_1, R_i, R_j, R_k) \mapsto (R_1, R_i, R_k, -R_j)$ (signed swap of order **four**, with $T^2 = \operatorname{diag}(1, 1, -1, -1)$);
  - $S$: $(\tau, a, b) \mapsto (-1/\tau, -b, a)$ sends $(R_1, R_i, R_j, R_k) \mapsto (R_1, -R_j, -R_i, -R_k)$.
  Those signed matrices on $\{R_i, R_j, R_k\}$ generate the octahedral signed-permutation subgroup isomorphic to **$S_4$ of order `24`** (`M_B1935_complex_Rs_group_order_is_24_S4 == true`); only the moduli $|R_s|$ (or projective rays) permute as $S_3$ of order `6` (`M_B1935_modulus_Rs_group_order_is_6_S3 == true`). Meanwhile `test_b1935_channels_centre_sectors.py` omits Claim `2` (the `-I` centre) completely and plants zero faults on Claims `3` and `4` despite `B1935/FINDINGS.md:3`–`4` claiming planted tests across the arc.

### Finding F-R83-12 — `B1936`'s degree rule `every conjugate at 5 − k` contradicts `degrees.py` on the degree-zero singlet, keeping that singlet crashes `higgs_by_parity.py` with `sign = -1`, `arc_verdict.json` sums `10 + 5` to `16`, and Frame D `W-B1` is untravelled

- **Arc:** `B1936`
- **File:** `frontier/B1936_matter_sits_in_the_even_half_of_lambda_c5_and_parity_consistency_would_fix_the_higgs_world/FINDINGS.md:24`
- **Line:** `24`
- **Commit read:** `b35eac607`
- **Criterion:** `1`, `4`, and `5` (internal algebraic contradiction on degree `0` vs `5`, missing lock plant on `degrees.py`, and untravelled `W-B1`/`W-F20` cold reads)

```text
- every conjugate at 5 − k.
```

- **What is wrong and how we know:** Line `22` places the neutral singlet at degree $k = 0$, so line `24` (`5 - k`) places its conjugate in odd degree `5` — whereas `verification/degrees.py:9`–`10` hardcodes `0` (even) in order to claim `16` even components! Worse, `verification/higgs_by_parity.py:5` silently drops the degree-`0` singlet from `DEG`: restoring `"deg_0": 0` for the standard singlet trilinear $(0, 4, 1)$ gives $(-1)^{0 + 4 + 1} = -1$, refuting single-graded parity invariance (`M_B1936_deg0_yukawa_parity_sign == -1`). In `B1936/arc_verdict.json:26`, `claim_one_line` lists only `(Q, u, e at 2; d, L at 4)` ($10 + 5 = 15$ components) while claiming `16 of 32`, `test_b1936_parity.py` plants zero faults on `degrees.py`, and web-seat deliveries `W-F20` (`harvest row 1813`) and `W-B1` (`harvest row 1824`, refuting `B1936`'s premise in Frame D `D1`) have not travelled onto `B1936` despite `THE_SWEEP_OF_2026-11-14.md` `S23`.

### Finding F-R83-13 — `B1937/FINDINGS.md` misstates `test_b1937_rule_v2.py` (`ten` tests, `four` unplanted, `two` reading real committed files) and leaves `A1 to A12` standing on line `76`, while `BIG_RUN_RULE_v2.md` miscounts joints (`nine`), omits `S10` under `A7`, and samples unphysical mixing moduli above one

- **Arc:** `B1937`
- **File:** `frontier/B1937_the_big_runs_rule_amended_before_the_look/FINDINGS.md:46`
- **Line:** `46`
- **Commit read:** `b35eac607`
- **Criterion:** `1`, `2`, `3`, `4`, and `5` (inaccurate lock description, un-updated amendment count, unimplemented `S10` clause in `A7` and `P-851`, and unitarity-violating calibration window)

```text
- **The lock** (`verification/test_b1937_rule_v2.py`, synthetic data only, nine tests), each with a planted case:
```

- **What is wrong and how we know:**
  1. `verification/test_b1937_rule_v2.py` defines **ten** `test_*` functions (not nine; `b1937_actual_test_count == 10`), **four** of the ten have zero planted negative case, and **two** (`lines 102`–`114`) read real committed files (`FINDINGS.md`, `big_run_look_v2.py`, `L.VALUES`, and `second_computations_run.txt`, checking only `W-` and omitting `W+` and `big_run_windows.py`'s hash).
  2. `B1937/FINDINGS.md:76` still says `The rule gains amendments A1 to A12` after `**A13.**` through `**A15.**` were added in `BIG_RUN_RULE_v2.md:226`–`266`, and `BIG_RUN_RULE_v2.md:137` (`A4`) says `nine joints` where `total_inputs_scoreboard.json` had eleven before `B1943` and twelve after (`b1937_rule_v2_stale_nine_joints == true`).
  3. In `BIG_RUN_RULE_v2.md:168` (`### A7. Two other cusps (S9, S10)`) and `P-851` (`POINT_REGISTER.md:54`), `S10` (requiring agreement across all four cusps of $X_1(5)$) is named in the heading and marked `DONE` in `P-851`, yet `A7`'s body and code contain **zero** check on `X_1(5)`'s cusps, and `BIG_RUN_RULE_v2.md:192` (`A9`) leaves `card A2-AMP` with no commit or harvest row pin.
  4. In `big_run_windows.py` and `big_run_windows_v3.py`, window `"a"` sets the upper base-ten logarithm bound on mixing moduli to plus three-tenths (ten to the power three-tenths, nearly two!), sampling random target mixing moduli strictly greater than one that no unitary matrix can ever match.

### Finding F-R83-14 — `test_b1938_coupling_and_gauge_class.py` checks signed `max(diffs)` without `abs(...)`, passing `lhs - rhs = -100` on every row, while `B1938/FINDINGS.md` cites an uncomputed figure and un-registered notes

- **Arc:** `B1938`
- **File:** `frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/verification/test_b1938_coupling_and_gauge_class.py:14`
- **Line:** `14`
- **Commit read:** `b35eac607`
- **Criterion:** `4`, `1`, and `5` (one-sided lock assertion that passes large negative errors, unverified `FINDINGS.md:50`–`51` claims, and un-registered promises on lines `99`–`101`)

```text
    assert len(diffs) >= 6 and max(diffs) < 1e-12
```

- **What is wrong and how we know:** `residue_as_determinants.py:38` prints signed `lhs - rhs`, and `test_b1938_coupling_and_gauge_class.py:13`–`14` parses `float(x)` and checks `max(diffs)` without `abs(...)`. Subtracting one hundred from `lhs - rhs` on all twelve rows in our sandbox prints minus one hundred on every row and passes `test_b1938_coupling_and_gauge_class.py` completely (`mut_b1938_minus100_diff_still_passes == true`). In addition, `B1938/FINDINGS.md:50`–`51` cites a `seven hundredths` breakdown figure with no committed script or output and falsely states `No figure here uses unreduced ones` (`residue_as_determinants.py:33` evaluates first twist coordinate eleven-tenths, strictly above one), and lines `99`–`101` state that `B1867 § 4, B1914 § 1, P-721` `are registered for a dated note` when no register row carries them (`P-850` carries only `B1919`'s sign).

### Finding F-R83-15 — `B1939/FINDINGS.md` contradicts line `103` in blaming `B1935`'s exact `{1/8, 3/8, 7/8}` phases, overstates universal cusp acyclicity and word counts, leaves § `3` and § `5` plants unlocked, names `"THE AGY SEATS"` in `claim_one_line`, and leaves six `HARVEST_LEDGER.md` rows marked `OWED`

- **Arc:** `B1939` (audited strictly on `main`'s own text, code, lock, and ledger hygiene outside recused seat-claim judgements)
- **File:** `frontier/B1939_the_agy_seats_unharvested_claims_recomputed/FINDINGS.md:119`
- **Line:** `119`
- **Commit read:** `b35eac607`
- **Criterion:** `1`, `3`, `4`, `5`, and `8` (self-contradictory phase correction, overbroad universal acyclicity statement, missing lock checks, session group in `claim_one_line`, and untravelled `HARVEST_LEDGER.md` updates)

```text
  - **B1935** prints its "Higgs triplet" T-eigenphases as {1/8, 3/8, 7/8}. Those are V's, the conjugate. The weave
```

- **What is wrong and how we know:**
  1. Sixteen lines earlier, `FINDINGS.md:103` explicitly defines **`The weave triplet V = η⁻³(θ₂², θ₃², θ₄²)`** — whose $L$-eigenphases are `{1/8, 3/8, 7/8}`, as `stage1_item3_stabiliser_signs_run.txt` `E3.8` prints! Lines `119`–`120` invert line `103`'s own definition by calling `V` `"the conjugate"` and saying `"The weave triplet itself has {1/8, 5/8, 7/8}"`. Moreover, `B1935` (`higgs_triplet_level.py`) read `B1724`'s covariance of Frame C's triplet `S` (`B[1]`, the Serre derivative of a basis of `V` via $\theta_2\theta_3\theta_4 = 2\eta^3$), which in its $T$-eigenbasis `(R_0, R_1 + i R_2, R_1 - i R_2)` genuinely has $T$-eigenphases `{1/8, 3/8, 7/8}` (whereas `verify_r83.py`'s `col_lead_k` read the undiagonalized `(R_0, R_1, R_2)` basis where two swapped columns share leading exponent `-1 ≡ 7 mod 8`), so faulting `B1935` here was doubly misplaced.
  2. `B1939/FINDINGS.md:56`–`57` and `arc_verdict.json:33` state unqualified that cusp cohomology vanishes `for every once-punctured torus bundle` whenever `ρ(ℓ) ≠ 1`, which fails on base-pullback characters where $\Delta_M(z) = 0$ at $z \neq 1$ and on non-orientable `m000` where $\mu\ell\mu^{-1} = \ell^{-1}$ forces $\rho(\ell) = -1$ with $h^1 = 1$; similarly lines `52`–`55` fail on the eight census bundles with $\varepsilon W \equiv I \pmod 5$ (`30` lines rather than `6`), and line `97` omits `"reduced"` on the `64` length-eight words (`256` unreduced words exist).
  3. `test_b1939_five_claims.py:26`–`29` checks only `"caught"` booleans on § `3` (`zero` positive claims locked!), omits `violations: 0` on § `2`'s census, and checks `zero` of § `5`'s fourteen planted cases.
  4. `B1939/arc_verdict.json:33` puts `"THE AGY SEATS"` inside `claim_one_line` (§ `12`), line `20` cites three unrowed commits (`d003e482b, 7c151b522, aca3f11c5`), and six `HARVEST_LEDGER.md` rows (`1676, 1677, 1678, 1696, 1710, 1815`; `b1939_harvest_rows_still_marked_owed` in `verify_r83_out.json`) still say `main`'s recomputation is `OWED` after `B1939` completed it.

### Finding F-R83-16 — `B1940/arc_verdict.json` and `FINDINGS.md` header still say `the second computation owed` with `cites_seat: []` after `FINDINGS.md` § `7` records the completed second computation, `FINDINGS.md:47`–`48` states the wrong cusp limit `(5/12, 5/12, 7/12)` for `W₊` (`(7/12, 7/12, 5/12)`), and `test_b1940` never checks `area_measure_mp.json`

- **Arc:** `B1940`
- **File:** `frontier/B1940_the_area_options_corrected_in_extended_precision/arc_verdict.json:26`
- **Line:** `26`
- **Commit read:** `b35eac607`
- **Criterion:** `5`, `1`, `4`, and `7` (untravelled § `7` update in `arc_verdict.json` and header, wrong `W₊` cusp limit propagated to `OPEN_LEADS.md:64`, unlocked `area_measure_mp.json`, and non-standard `(one seat)` label)

```text
 "claim_one_line": "THE BIG RUN'S AREA OPTIONS CORRECTED IN EXTENDED PRECISION (PROVED; computed once, the second computation owed): the double-precision frame breaks F-bar(tau + 1) = F-bar(tau) above Im tau about 11 because the true m1/m3 falls below 1e-15 there, and neither a 50-digit SVD nor the closed-form residues repair it; the frame redone in mpmath passes tau -> tau + 1 to 1e-18 at heights 12 to 45 and matches the double frame where that is sound; the area options' mixing moduli move by up to 0.068 in ln, their mass ratios by under 1e-4, the move-count options not at all; a corrected values file and version 3 of the run's script are sealed beside B1932's. 0 of 19.",
```

- **What is wrong and how we know:**
  1. `B1940/FINDINGS.md:94`–`101` (`§ 7`) records two agreeing independent second computations (`harvest rows 1816 and 1817` on that page), yet `FINDINGS.md:4`–`5` and `B1940/arc_verdict.json:16, 24, 26` still have `"cites_seat": []` and `computed once, the second computation owed`. Also `FINDINGS.md:94` and `B1937/FINDINGS.md:71` write non-standard `(one seat)` instead of § `12`'s fixed check labels.
  2. `B1940/FINDINGS.md:47`–`48` (propagated to `docs/OPEN_LEADS.md:64`) states unqualified that the `24`-point cusp average of `(∣V₁₂∣, ∣V₂₃∣, ∣V₁₃∣)` tends to `(5/12, 5/12, 7/12)`. Our standalone `mpmath` evaluation at height `85` proves that `(5/12, 5/12, 7/12)` holds **only in `W₋`**, whereas **`W₊` tends to `(7/12, 7/12, 5/12)`** (`M_B1940_cusp_wm_is_5_5_7_over_12 == true`, `M_B1940_cusp_wp_is_7_7_5_over_12_not_5_5_7 == true`).
  3. Corrupting `area_measure_mp.json` directly in our sandbox leaves `test_b1940_corrected_values_and_v3.py` completely green (`mut_b1940_area_mp_corrupted_still_passes == true`), and `test_b1940_corrected_values_and_v3.py:5, 79`, `big_run_look_v3.py:6, 13`, and `big_run_windows_v3.py:5, 7` carry stale `v2` / `B1932's values` docstrings.

### Finding F-R83-17 — `B1944/arc_verdict.json` names a seat card (`SM-C15`) inside `claim_one_line` while omitting it from `cites_seat`, banks `"verdict": "NEGATIVE"` prematurely while bypassing `gates.py:3502` without `PROVISIONAL`, omits required `BIG_RUN_RULE_v2` outputs (`O2`, `A2`, `A4`, `A9`, `A10`) and wall-lead registration (`P-842`), and mismatches `BLIND_ARCS.md`

- **Arc:** `B1944`
- **File:** `frontier/B1944_the_big_run_read_frame_c_fails_and_the_average_washes_out_the_hierarchy/arc_verdict.json:22`
- **Line:** `22`
- **Commit read:** `b35eac607`
- **Criterion:** `8`, `5`, `1`, and `4` (session card named in `claim_one_line`, unbanked `NEGATIVE` rule `O5`/`A14` and `P-842` breaches, gate bypass on `cites_seat[0]`, inaccurate `read_the_look.py` description, and `BLIND_ARCS.md` mismatch)

```text
 "claim_one_line": "THE BIG RUN, READ: FRAME C FAILS IN EVERY OPTION (NEGATIVE as sealed; PROVISIONAL until SM-C15 re-runs it): best chi2_7 6 679 against a bar of 22.0, every option's worst claimed row off by a factor of 3 314 or more, and 22 % of random targets fitted as well; version 1 FAIL too. Every mass ratio of the average is too large, about 10 times (s/b) to thousands of times (u/t), and |V_cb| and |V_ub| by similar orders; |V_us| is near (0.89 to 1.47) in every option, which the calibration calls generic. What the wall teaches: the average over the whole surface is dominated by the bulk, so the step that removed tau also removed the hierarchy. Nothing is adjusted after the look. 0 of 19.",
```

- **What is wrong and how we know:**
  1. Naming `SM-C15` inside `claim_one_line` violates `docs/seats/README.md` § `12`, while `cites_seat` (`lines 9`–`12`) omits `SM-C15` (`harvest row 1823`). Worse, because `cites_seat[0]` contains `"second computations of the values"`, stripping `PROVISIONAL` from `B1944` in our sandbox probe **bypasses `gates.negative_without_second` (`gates.py:3502`) completely** (`b1944_without_provisional_bypasses_gate == true`).
  2. `BIG_RUN_RULE_v2.md` `O5` and `A14` specify that the look is `not banked until SM-C15 agrees` (and `A7` required two other cusps `before the run`, whereas `B1944/FINDINGS.md:20` postponed `A7` until after the look!). Moreover, `B1944/FINDINGS.md` omits `O2` (`worst_factor_six`, `worst_factor_nine`, and their calibrations), `A2` (`worst_factor_seven` window calibrations printed in `read_the_look_run.txt:11`), `A4` (the ruled `0 of 19` headline and package-zero-twelve status), `A9` (the look count beside the outcome), `A10` (post-look `test_no_value_is_recorded` check, which failed in `F-R83-08`!), and `P-842`'s required register/open-leads entry for `What the wall teaches` (`line 69`).
  3. `B1944/FINDINGS.md:32` says `read_the_look.py reads only those three files`, whereas `read_the_look.py` calls `read_text()` on the three output files (`b1944_read_the_look_actual_files_read == 3`) **plus** `L.targets(L.DATA, L.CKMDATA)` (`line 15`), which reads two empirical data files (five files in all, as `read_the_look.py`'s own docstring on lines `1`–`2` acknowledges), and `docs/atlas/BLIND_ARCS.md:86`–`87` classifies both `B1937` and `B1944` as `INSTRUMENT` against `"instrument": false` in both `arc_verdict.json` files (`blind_arcs_b1937_b1944_instrument_mismatch == true`).

### Finding F-R83-18 — `B1933/arc_verdict.json` names `"the SM seat"` and `"agy-exp's X-NEVER"` inside `claim_one_line`, `GENESIS.md` says `computed once ... by an independent computation`, `B1930`'s seventh-path plant duplicates an existing path (missing any distinct seventh path), `B1931` has no lock, and `B1928`'s opening header still says `OPEN`

- **Arc:** `B1933` (with `B1930`, `B1931`, `B1928`, `B1929`, `GENESIS.md`, and cited `HARVEST_LEDGER.md` rows)
- **File:** `frontier/B1933_the_foundation_at_version_1_69/arc_verdict.json:26`
- **Line:** `26`
- **Commit read:** `b35eac607`
- **Criterion:** `8`, `4`, `5`, `1`, and `7` (session keys in `claim_one_line`, self-contradictory `GENESIS.md` check label, non-failing `B1930` seventh-path check, missing `B1931` lock, stale `B1928` header, and unpinned cited harvest rows)

```text
 "claim_one_line": "THE FOUNDATION AT VERSION 1.69: THE m000 ROW OF THE TABLE OF FRAMES SAYS WHAT B1926 COMPUTED (F-FC closed, b1 = 1 and cusp rank 1 at levels 1 to 8; F-CI: no sector module at an odd level, the twisted classes the double cover's matter seen from below, a stated choice whether they count), F-HE and F-AP not computed and offered to the SM seat; the list 'Computed nowhere yet' narrows its m000 entry to those two frames and marks the harmonic frame's counts outside m004's levels as computed once (agy-exp's X-NEVER, harvest row 1797), its second computation owed. Written by the version's own script; its lock takes the version back and gives the page again. 0 of 19.",
```

- **What is wrong and how we know:**
  1. `B1933/arc_verdict.json:26` names `"the SM seat"` and `"agy-exp's X-NEVER"` inside `claim_one_line` (and line `19` puts a vendor/session name in `authored_by`; similarly `B1932/arc_verdict.json:28`, `B1917/arc_verdict.json:23`, and `B1919/arc_verdict.json:23` retain `"the seat's"` in `claim_one_line`). Meanwhile `GENESIS.md:497`–`498` writes `computed once ... by an independent computation` (mixing § `12`'s `computed once` with `recomputed independently`).
  2. In `B1930`, `test_b1930_the_foundation_at_version_1_68.py:64`–`68` comments `# a seventh path into a moved folder, added to section 1` while inserting a duplicate of `W.PATHS[0]` (`philosophy/P000_what_is_not_nothing.md`); inserting a genuinely **distinct** seventh moved path (`philosophy/P999_unlisted_moved_note.md`) is never refused by `W.version_1_68` (`b1930_distinct_7th_path_not_refused == true`), and two of the six paths stand on `GENESIS.md:23` before `## 0`, contradicting `B1930`'s `"in §§ 0 to 8"` claim.
  3. `B1931` has zero `test_*.py` lock (`b1931_lock_count == 0`), falsely states `the first review read by the other family` (`Review 79` and `Review 80` were read by `agy-exp`), and groups `B1898` (`2026-11-12`) under planted-review readings (`started at Review 81, B1916`).
  4. In the `73e71e277..b35eac607` mends, `B1928/FINDINGS.md:3` still says `**Verdict: OPEN**` while `B1928/arc_verdict.json:3` is `"PROVED"` (`b1928_header_still_open_while_verdict_proved == true`), `B1929/arc_verdict.json` omits `SM-C12` (`row 1806`) from `cites_seat`, and cited harvest rows `1755, 1768, 1794, 1797, 1800, 1801, 1802, 1804` lack `@ <commit>` pins (`cited_harvest_rows_missing_commit_pin` count `8`).

### Finding F-R83-19 — `THE_SWEEP_OF_2026-11-14.md` claims `S111`–`S113` are marked `offrecord_origin=true` when zero entries carry that tag, conflates `SE1` with level five in `S101`, uses vendor/agent names and a post-ruling `"by the owner"` phrase (`REVIEW_WAIVER.md:24`), and companion pages contradict `C02`, `C11`, and `C17`

- **Arc:** `docs/THE_SWEEP_OF_2026-11-14.md` (with `THE_PAIRS_PROGRAMME.md`, `THE_STALE_OPEN_VERDICTS_O1_TO_O10.md`, `REVIEW_WAIVER.md`, `POINT_REGISTER.md`)
- **File:** `docs/THE_SWEEP_OF_2026-11-14.md:1023`
- **Line:** `1023`
- **Commit read:** `b35eac607`
- **Criterion:** `1`, `5`, `6`, and `8` (false tag claim, mathematical conflation of `SE1` with frustrated level `5`, vendor/agent names and post-ruling owner attribution, and stale contradictions in companion docs)

```text
- The free-bit count, the E8-lattice question and the puncture-residue note are marked offrecord_origin=true because the S14 reader tied them to the session's off-record study; their mathematics may also stand on B1934 to B1936 alone.
```

- **What is wrong and how we know:**
  1. `S111`–`S113` (`lines 679`–`696`) carry **zero** `offrecord_origin=true` tags (`sweep_offrecord_tag_occurrences_in_body == 0`).
  2. `S101` (`line 623`) writes `SE1 ('level 5 is where the frustrated homology is non-trivial')`, conflating `SE1` (`torsion-free root H₁`, `GENESIS.md:219`) with frustrated level `5` (`C02`). Similarly, `docs/THE_PAIRS_PROGRAMME.md:96, 180` falsely writes `C02 — forced given SE1` and `nine plus one ansatz` after `B1943` proved `C02` is **not** forced by `SE1` (`CHOSEN`, `12` borrowed joints).
  3. `THE_SWEEP_OF_2026-11-14.md` (`lines 183, 207, 362, 388, 568, 739, 1022, 1036`) and `THE_STALE_OPEN_VERDICTS_O1_TO_O10.md:142` use vendor/session names, and `docs/REVIEW_WAIVER.md:24` (`2026-11-15`) writes `"waived 2026-11-15 by the owner through 90 merges"` (attributing a `2026-11-15` line directly to the owner, Criterion `6`).
  4. `docs/THE_STALE_OPEN_VERDICTS_O1_TO_O10.md:155`–`159, 197`–`199` still says `B44` (`O7`) has no lock and `O1`–`O10` are unacted on after `C11` (`tests/c11_lock.py`) and `C17` (`P-746` closed `DONE`) landed, while `POINT_REGISTER.md:50` (`P-853`) still calls `S1` rank-`1` debt after `B1944` closed it and `P-776` (`line 988`) says `R4 met` where `B1716/FINDINGS.md:256` says `met in part`.

### Finding F-R83-20 — `test_review_waiver_names_its_anchor.py:59` silently skips `None` anchors via `if a`, `gates.selection_claims_in` splits clauses on parentheses (creating both a false negative bypass and a false positive), and `public-face` errata/quote checks have live holes

- **Arc:** `Window lock and gate mends`
- **File:** `tests/test_review_waiver_names_its_anchor.py:59`
- **Line:** `59`
- **Commit read:** `b35eac607`
- **Criterion:** `4` (lock and gate assertions with live bypasses)

```text
    assert all(a in written for a in anchors if a), anchors
```

- **What is wrong and how we know:**
  1. Because line `55` returns early only when `all(a is None for a in anchors)`, any mix of one resolved anchor and one unresolved `None` anchor (`anchors = ["aaaaaaa11", None]`) reaches line `59`, where `if a` silently filters out `None` and passes (`waiver_if_a_drops_none_anchor == true`)!
  2. In `scripts/gates/gates.py:3089`, `selection_claims_in` splits clauses on `[.;:()—]|--`, so a parenthetical citation between verb and object (`"The census selects (B1906) m004."`) bypasses the `selection-family` gate (`selection_paren_false_negative == true`), while a parenthetical citation after a negation (`"No rule (B1204) selects one member."`) severs `"No"` from `"selects"` and triggers a false positive (`selection_paren_false_positive == true`).
  3. In `tests/test_public_face.py:150`–`151`, `public_face_words` never strips curly quotes `“...”`, returning the exact same positive count with or without quotes (`public_face_curly_quotes_noop == true`), while `gates.public_face_unentered` (`gates.py:3311`) checks only line numbers in `ERRATA.md`, so appending `" as the owner's lane ruled"` to `papers/P3_THE_PAPER/main.tex` line `1249` returns zero unentered violations (`errata_existing_line_new_inner_word_bypasses == true`). Also `tests/test_the_terms_in_short.py:36` checks only the two-word stub `"A frame is"` in `THE_PROGRAMME_SO_FAR.md` instead of the mathematical statement `"A frame is a hypothesis, and none is derived from the principle"`.

---

## 3. Verification Summary on Every Remaining Item in Scope (One Line Each)

1. **`B1930` (`b35eac607`, outside `F-R83-18`):** `test_b1930_the_foundation_at_version_1_68.py` (`3` of `3` passed in sandbox) verifies the six listed `docs/archive/` replacements and round-trip rollback from `v1-69` through `v1-68`.
2. **`B1931` (`b35eac607`, outside recused `R82`/`A2-R82` clauses and `F-R83-18`):** Verified `verification/plants.py` and `plants_run.txt` against `P-848`'s six Review `82` plants and window mends `R82-1` to `R82-12`.
3. **`B1932` (`b35eac607`, outside recused `A2-*` items and `F-R83-09`):** `test_b1932_values_and_seal.py` (`4` of `4` passed in sandbox); Theorem `90` vs exact norm (`t90.json`), truncation shift (`truncation.json`), `W-|a`/`W+|a` assembly, and `big_run_look.py` synthetic `PASS`/`FAIL`/hash-refusal checks hold.
4. **`B1933` (`b35eac607`, outside recused `X-NEVER` substance and `F-R83-18`):** `test_b1933_the_foundation_at_version_1_69.py` (`3` of `3` passed in sandbox); `write_version_1_69.py` round-trip and `B1926` `m000` `F-FC`/`F-CI` restatements match.
5. **`B1934` (`b35eac607`, outside `F-R83-10`):** `test_b1934_level_five_structure.py` (`4` of `4` passed in sandbox); independently verified the `3 + 2` Weil parity split, golden-field Legendre symbol $\chi_5(a) = (a/5)$, and matrix transposition between the third and second charged sectors at level five.
6. **`B1935` (`b35eac607`, outside `F-R83-11`):** `test_b1935_channels_centre_sectors.py` (`3` of `3` passed in sandbox); independently verified `-I` centre fixity, modulus $S_3$ action on $\{|R_i|, |R_j|, |R_k|\}$, sector coincidence orders `2` to `7`, and minimum composite level `40`.
7. **`B1936` (`b35eac607`, outside `F-R83-12`):** `test_b1936_parity.py` (`2` of `2` passed in sandbox); verified the five-component `10 + 5` exterior degrees `(2, 2, 2, 4, 4)` and odd degree `1` of the `5` scalar slot.
8. **`B1937` (`b35eac607`, outside recused `agy-exp`/`agy-002` computations and `F-R83-13`):** `test_b1937_rule_v2.py` (`10` of `10` passed in sandbox); verified `big_run_look_v2.py` synthetic governing/pattern-match/hash-refusal logic and pre-look timestamp order.
9. **`B1938` (`b35eac607`, outside `F-R83-01` and `F-R83-14`):** `test_b1938_coupling_and_gauge_class.py` (`6` of `6` passed in sandbox); independently verified in `mpmath` to fifty digits that $\sum_{s=1}^4 R_s(c, \tau)^2 = 0$ (`M_B1938_riemann_sq_sum_zero == true`) and checked Szegő / Ray–Singer determinant formulas and `gauge_class_readout_run.txt` figures.
10. **`B1939` (`b35eac607`, `main`'s own scripts and lock outside recused seat-claim judgements and `F-R83-15`):** `test_b1939_five_claims.py` (`5` of `5` passed in sandbox); verified `x*y ≡ 0 mod 5` count (`9`), package-one-two literal-clause failure catch, and `B1929` character-sum check on `main`'s run files.
11. **`B1940` (`b35eac607`, outside recused `X-MEASURE`/`A2-AREA` evaluations and `F-R83-02`, `F-R83-16`):** `test_b1940_compare_area_second.py` (`1` of `1` passed) and `test_b1940_corrected_values_and_v3.py` (`11` of `11` passed); independently verified IEEE binary64 cusp breakdown at height twenty and arbitrary-precision `mpmath` $\bar{F}(\tau + 1) = \bar{F}(\tau)$ invariance across heights `12, 20, 35, 45` (`mpmath_exact_rational_holds_to_1e55 == true`).
12. **`B1941` (`b35eac607`, outside `F-R83-03`):** `test_b1941_s4_pointwise.py` (`1` of `1` passed in sandbox); checked `s4_pointwise.py` and `s4_pointwise_run.txt` across all eight rows (`ln det` vs `-Tr H^2`, weights `(3, 3, 1)` vs `(1, 1, 1)`, exact vs truncated channel weight).
13. **`B1942` (`b35eac607`, outside `F-R83-04`):** `test_b1942_level_fifteen.py` (`2` of `2` passed in sandbox); independently verified all `192` exact order-fifteen points, `8`-to-`1` projection onto the `24` order-five points, and exact identity of the third charged sector's order-fifteen average with the transposed order-five second sector.
14. **`B1943` (`b35eac607`, outside `F-R83-05` and `F-R83-07`):** `test_b1943_fixed_lines_and_the_board.py` (`2` of `2` passed in sandbox); independently verified $\operatorname{Smith}(LR - I) = (1, 1)$, $\operatorname{Smith}(LR + I) = (1, 5)$, the `LRR` trace-four control, and scoreboard re-typing of `C02` from `FORCED-CLAIMED` to `CHOSEN`.
15. **`B1944` (`b35eac607`, pure-mathematical parts outside `0 of 19` measured comparisons and `F-R83-06`, `F-R83-08`, `F-R83-17`):** `test_b1944_the_look_read.py` (`1` of `1` passed in sandbox); verified SHA-256 seals on `big_run_output_v3.json`, `big_run_windows_v3_output.json`, and `big_run_output.json`, and `LOOK_LEDGER.md` row `10` entry.
16. **Register rows `P-849` through `P-857` and window edits in `73e71e277..b35eac607` (outside recused clauses and `P-851`, `P-853`, `P-776` in `F-R83-13`, `F-R83-19`):** Read `P-849` through `P-857` and window updates (`P-318`, `P-320`, `P-328`, `P-334`, `P-746`, `P-842`, `P-845`, `P-847`, `P-848`) against their cited arcs and sweep items; plain-wording rule (`zero` post-ruling owner quotes in `POINT_REGISTER.md`) holds.
17. **Sweep `docs/THE_SWEEP_OF_2026-11-14.md` (`S1`–`S166` and `Doubtful`, outside recused seat judgements and `F-R83-19`):** Verified header tallies (`166` items: `5` before-run, `28` this-week, `133` standing) and spot-checked cited line references across `OPEN_LEADS.md`, `POINT_REGISTER.md`, and `HARVEST_LEDGER.md`.
18. **Window mends on `B1917`–`B1929`, `WORKING_RULES.md`, and `tests/` (`73e71e277..b35eac607`, outside `F-R83-08`, `F-R83-17`, `F-R83-18`, `F-R83-20`):** Verified `R82-1` to `R82-12` mends (`B1917` genuine half-strip call and seventeenth-row bound, `B1919` geodesic locus, `B1924` upgrade propagation, `B1925` `every odd metallic act`, `B1926` `cites_seat`, `B1927` corner figure, `B1929` tight tolerance, `_SECOND_NOT_YET_RE` negation words) and `test_negative_second_computation.py` / `test_the_terms_in_short.py` / `test_review_waiver_names_its_anchor.py` baseline passes in sandbox.

`0 of 19.`
