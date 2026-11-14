# Review 82 — Blind Reading at `86930f574` (`agy-exp`, Card `R82`)

- **Seat / Session:** `agy-exp`
- **Branch:** `agy/self-consistent-loop-2026-11-11`
- **Card (Commit One):** `relays/cards/AGY-EXP_R82_review-82.md` (`121228888`)
- **Verifier Script (Commit Two, sealed before execution):** `relays/r82_verify/verify_r82.py` (`6adcc6f09`, SHA-256 `e22f25adbef78942691d946c1c7841cb88f871b679393ef3ad21b095bf0c6958` in `relays/r82_verify/SCRIPT_SHA256.txt`)
- **Raw Output (Commit Three, committed unread):** `relays/r82_verify/verify_r82_out.json` (`064d53fca`, SHA-256 `d40fad611e3dd23a34705690004777a5086c11f68ece847c2ae6fd0b1e836b82` in `relays/r82_verify/OUTPUT_SHA256.txt`)
- **Pinned Commit Read:** `86930f574` (`86930f57458df41f9f3e97b78d8128de344d2b0c` on `origin/review-82/read`), with window base `0e637ea9e` where differences apply
- **Blind-Test Isolation:** `86930f574` was never diffed or compared against `73e71e277` or `origin/main`, and no other session's branch or review file was opened or listed before pushing this report.
- **Pre-Output Amendments:** Zero (`verify_r82.py` ran cleanly on its first execution from `6adcc6f09`; all three pre-registered negative controls `C-R82-1`, `C-R82-2`, and `C-R82-3` passed; all fourteen baseline pytest suites passed in an isolated pure-mathematics sandbox; all fifteen quotations below matched character-for-character at their exact line numbers at `86930f574`).
- **Empirical Firewall:** `0 of 19.`

---

## 1. Recusals and Items Not Checkable at `86930f574` (`docs/seats/README.md` §§ 9, 13)

1. **`agy-exp` own work (recused from mathematical evaluation):**
   - `B1923`: rows `B1` (`B1868`), `C1` (`B1855`), and the `X-C1b`/`X-C1c` clause on `(rows 926, 945, 949)` (plus the corresponding `X-NEG` addenda on `B1855` and `B1868`).
   - `B1924`: the bracketed `2026-11-14` Furstenberg note on lines `68` to `71` of `FINDINGS.md`.
   - `B1928`: lines `59` to `61`, `70`, and `92` to `93` of `FINDINGS.md`, and line `13` of `arc_verdict.json` (`X-NEG`, harvest row `1776`).
   - `B1929`: `X-C9`'s proof and three dissertation slips (`harvest row 1788`), while auditing `main`'s own scripts (`main_siegel.py`, `end_to_end.py`), `test_b1929_twisted_eta.py`, and record-keeping hygiene in `arc_verdict.json`.
   - `POINT_REGISTER.md` and `HARVEST_LEDGER.md`: harvest rows `1776` and `1788`, and the clauses in `P-842`, `P-845`, and `P-846` evaluating `agy-exp`.
2. **Own model-family work (`agy-002` and `the agy lane`, recused from judging the seat's work itself):**
   - `B1923`: rows `A1`, `A6` (`harvest row 1621`), `A7`, and `C5` (`B1884` supplemental note), plus the `A2-NEG` addenda on `B1839` and `B1841` and bracketed `row 1789` notes on harvest rows `945` and `949`.
   - `B1924`: `agy-002`'s delivery `A2-B1924` (`harvest row 1790`), while independently checking the pure group/matrix identity $W(w^*) = W(w)^T$ and auditing `main`'s own internal consistency in `B1924/FINDINGS.md` and `B1924/arc_verdict.json`.
   - `POINT_REGISTER.md` and `HARVEST_LEDGER.md`: harvest rows `1621` and `1790`, and the `agy-002` / `agy lane` evaluation clauses in `P-845` and `P-846`.
3. **Register row `P-848` (cannot check at `86930f574`):**
   - At `86930f574`, `docs/POINT_REGISTER.md` has `1058` lines and ends at `P-847` (`P-848`, which hashes the planted-faults list for Review `82`, was added on `main` when opening Review `82` after `86930f574` was branched and is left untouched under blind-test isolation).
4. **Measured physical quantities:** Not read anywhere (`0 of 19`; historical comparison scripts were deleted from the temporary sandbox before running any lock).

---

## 2. Machine-Checked Findings at `86930f574` (`F-R82-01` through `F-R82-15`)

Every quotation block below contains the exact full line at `86930f574` verified by `verify_r82.py` (`quote_verification.all_exact == true` in `relays/r82_verify/verify_r82_out.json`).

### Finding F-R82-01 — `B1917`'s planted half-strip assertion in `test_b1917_one_l_function.py` divides `R` by two algebraically and cannot fail whenever line `31` passes

- **Arc:** `B1917`
- **File:** `frontier/B1917_the_slope_and_the_kronecker_function_one_l_function_on_the_threads_geodesic/verification/test_b1917_one_l_function.py:32`
- **Line:** `32`
- **Commit read:** `86930f574`
- **Criterion:** `4` (a check that cannot fail)

```text
    assert abs(L / (H.H(2) * R / 2) - 2) < 1e-4            # planted: half the orbit strip is off by exactly 2
```

- **What is wrong and how we know:** Line `31` immediately precedes line `32` by asserting that `abs(L - H.H(2) * R) / abs(L)` lies below ten to the minus five. Instead of calling `H.rhs` over a half-width orbit strip (`t < log(lam)` rather than `2 * log(lam)`), line `32` divides the already-computed number `H.H(2) * R` by `2`, testing $|2 L / (H(2) R) - 2| = 2 |L / (H(2) R) - 1|$. Whenever line `31` holds, $|L / (H(2) R) - 1|$ is below one part in ninety-nine thousand nine hundred and ninety-nine, so line `32`'s left-hand side is algebraically bounded by roughly one-fifth of line `32`'s threshold (`M_B1917_line32_cannot_fail_when_line31_holds == true`, `M_B1917_line32_rhs_calls_count == 1` in `verify_r82_out.json`). Line `32` can never fail when line `31` passes.

### Finding F-R82-02 — `B1917`'s lock leaves the seventeenth character's relative error completely unbounded above

- **Arc:** `B1917`
- **File:** `frontier/B1917_the_slope_and_the_kronecker_function_one_l_function_on_the_threads_geodesic/verification/test_b1917_one_l_function.py:24`
- **Line:** `24`
- **Commit read:** `86930f574`
- **Criterion:** `4` (a lock assertion that fails to bound all rows it purports to hold)

```text
    assert len(rows) == 17 and sum(r["rel"] < 1e-7 for r in rows) == 16
```

- **What is wrong and how we know:** Requiring sixteen of the seventeen rows in line `24`'s sum to lie below ten to the minus seven places no upper bound on the seventeenth row (`["+LR", 3]`, `[1, 0]`, index `8` of `hecke_s2.json`), requiring only that its relative error not lie below the tight threshold. Mutating that row's `"rel"` in `hecke_s2.json` to ten to the ninety-ninth power in our sandbox leaves the entire `test_b1917_one_l_function.py` suite green (`M_B1917_line24_row17_rel_1e99_suite_still_passes == true`).

### Finding F-R82-03 — `B1917/FINDINGS.md` cites `hecke_s2.py` for a growing `m`-range convergence figure that neither `hecke_s2.py` nor its outputs compute

- **Arc:** `B1917`
- **File:** `frontier/B1917_the_slope_and_the_kronecker_function_one_l_function_on_the_threads_geodesic/FINDINGS.md:27`
- **Line:** `27`
- **Commit read:** `86930f574`
- **Criterion:** `1` and `2` (a statement and number unsupported by the cited script and outputs)

```text
    character whose series has no phase in n converges to 1.6 × 10⁻⁷ as the m-range grows (`hecke_s2.py`). Main's
```

- **What is wrong and how we know:** `verification/hecke_s2.py` defines `lhs(..., Mmax=60, Nmax=4000)` (`line 29`) and calls `lhs(M, (i / N, j / N))` once per character at fixed `Mmax=60` (`line 95`). Neither `hecke_s2.py`, `hecke_s2.json`, nor `hecke_s2_run.txt` varies `Mmax` or produces the figure stated on line `27`; for the unphased-in-`n` row (`+LR`, power `3`, `(1, 0)`), `hecke_s2_run.txt:9` and `hecke_s2.json` record a relative error near two parts in ten thousand (`string_1_6_in_hecke_s2_run_or_py == false`, `mmax_loop_in_hecke_s2_py == false` in `verify_r82_out.json`).

### Finding F-R82-04 — `B1919/FINDINGS.md` attributes twenty-four cases at three points of the golden geodesic to `seat_formula.py`, which evaluates four cases at one point while two JSON `tau` points lie off the golden geodesic

- **Arc:** `B1919`
- **File:** `frontier/B1919_the_channel_norm_is_the_shifted_lattices_kronecker_limit_at_the_kernels_shift/FINDINGS.md:18`
- **Line:** `18`
- **Commit read:** `86930f574`
- **Criterion:** `1` and `3` (statement wider than the cited script, and coordinates rounded off the claimed locus)

```text
  (a pair of Hurwitz zetas and a Bessel series), the norm by main's quadrature of B1656's definition: on 24 cases (eight
```

- **What is wrong and how we know:** Together with lines `17`, `19`, and `50` (`verification/seat_formula.py` `->` `seat_formula_check.json`, `on 24 cases (eight characteristics at each of three points of the golden geodesic)`), this attributes `seat_formula_check.json` and all `24` cases to `seat_formula.py`. In fact, `seat_formula.py` (`lines 44` to `52`) evaluates only `4` characteristics at `1` modulus and writes no JSON file (`seat_formula_py_writes_json == false`), so `seat_formula_check.json` has no tracked producer script in `verification/`. Moreover, two of the three `tau` points stored in `seat_formula_check.json` use four-digit rounded coordinates that miss the golden-geodesic semicircle $(x - 1/2)^2 + y^2 = 5/4$ by roughly eight parts in one hundred thousand (`rounded_taus_off_geodesic_count == 2` in `verify_r82_out.json`).

### Finding F-R82-05 — Cited `HARVEST_LEDGER.md` row `1713` still says `REGISTERED` and `Main's own computation is OWED` after `B1912` and `B1923`

- **Arc:** `B1923` / cited harvest row `1713`
- **File:** `docs/HARVEST_LEDGER.md:1766`
- **Line:** `1766`
- **Commit read:** `86930f574`
- **Criterion:** `5` (an update in `B1912` and `B1923` that did not travel to the cited harvest row)

```text
| 1713 | web seat (chat1) | TWO DELIVERIES. (a) ITS SEALED CARD ON THE GOLDEN STATE (P-783), DELIVERED: by a scan and not a proof, the state is the lowest in all four classes and simple; no state at either of the two values the agy lane reported; computed once, expectations committed first, a second check written after the sealed output was read and said so; no independent recomputation in the record, by its own statement. (b) THE COLD READ OF THE THREE-PART PUBLIC STRUCTURE, with no computation | "by a scan, not a proof" | relays/CHAT1_TO_CC_2026-11-11_P-783_THE_GOLDEN_STATE_IS_THE_LOWEST_AND_SIMPLE.md, relays/chat1_2026-11-11_p783/, relays/CHAT1_TO_CC_2026-11-11_A_COLD_READ_OF_THE_THREE_PART_STRUCTURE.md @ dbbcd470 on web-seat | **THE COLD READ, READ IN FULL; THE RESULT ON THE GOLDEN STATE REGISTERED, ITS HEAD READ (S306p)**: (a) the two values it names are spectral parameters of states a lane reported, whose settlement main's card asked for; they are not read-out points, and nothing of the owner's hold applies, which answers the question row 1708 left. Main's own computation is OWED and belongs to the modulus (WP-4.1). (b) THE COLD READ: a stranger would not believe the count of looks, which the parties assemble; the list of inputs, which is the authors'; or that a check shares nothing with the statement, where copying by hand cannot be seen. Of the five conditions the one whose output can be read is the strongest; sealing expectations does not make a checker blind who has read the record, as every session has; two conditions are missing, a perturbed statement that the check must reject, and the publication of every result of the check, failures included. What no page asks for and a stranger needs: a map of what is known, giving for each mathematical step the textbook or paper it comes from and what is claimed as new. It says of itself that it is not a stranger. Register row P-807; it goes to the public form (P-787) | — | 2026-11-11 |
```

- **What is wrong and how we know:** In the Review `82` window, `B1923/FINDINGS.md:12` and `41` (`done: the web seat's sealed scan (harvest row 1713), its own code, agrees ... (read today; B1912 carries a note)`), `B1923/arc_verdict.json:18`, and `B1912/FINDINGS.md:78` record both `main`'s computation (`B1912`) and the reading of harvest row `1713` as `B1912`'s independent second computation, yet `docs/HARVEST_LEDGER.md:1766` still stands at `THE RESULT ON THE GOLDEN STATE REGISTERED, ITS HEAD READ`, `Main's own computation is OWED`, and `—` in the arcs column.

### Finding F-R82-06 — `B1924/FINDINGS.md` upgrades the arc from `OPEN` to `PROVED` at line `193` while leaving `OPEN` and the owed second computation standing in its top header

- **Arc:** `B1924`
- **File:** `frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/FINDINGS.md:3`
- **Line:** `3`
- **Commit read:** `86930f574`
- **Criterion:** `5` (a dated upgrade and correction that did not travel to the arc's own header)

```text
**Verdict: OPEN** (numerical evidence at the 10⁻² level; no limit is proved; an independent second computation is
```

- **What is wrong and how we know:** `B1924/FINDINGS.md:193` writes `Verdict upgraded from OPEN to PROVED` and `B1924/arc_verdict.json:3` sets `"PROVED"`, yet `B1924/FINDINGS.md:3` to `4` still declares `OPEN` and `an independent second computation is owed` (and line `1`'s title still says `the dependence on the twin fades`, which line `182` states is superseded; likewise `test_b1924_read_out_on_the_whole.py` never locks the upgraded finite-`n` twin-equality theorem).

### Finding F-R82-07 — `B1924/arc_verdict.json` leaves `(OPEN)` and `no independent second computation yet` standing in `claim_one_line` and `scope.hypotheses`, and names a session key inside `claim_one_line`

- **Arc:** `B1924`
- **File:** `frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/arc_verdict.json:29`
- **Line:** `29`
- **Commit read:** `86930f574`
- **Criterion:** `5` and `8` (untravelled upgrade in `claim_one_line` and `scope.hypotheses`, plus session key credited in `claim_one_line`)

```text
 "claim_one_line": "[UPGRADED 2026-11-14 from OPEN on agy-002's second computation, harvest row 1790; CORRECTED: the twin is not fading but exactly equal at every n] THE READ-OUT ON THE WHOLE, FIRST RUNS (OPEN): with P-845's condition (allowed words at level 5, each thread's average of the frame at its own line with the invariant end, combined by the move count and weighted by length), the read-out changes from n = 16 to n = 22 by no more than its sampling error (about 1.3e-2; per number median |z| 0.94 at the mark and 0.67 at the twin, none above 2 at the mark), and the read-outs at the mark and at its twin, clearly different at n = 10 (paired median |z| 2.35, 58% above 2), are not told apart at n = 16 (0.92, 4%) or n = 22 (0.57, 0%). The limit is not proved; longer histories, an independent second computation (agy-002) and the end are owed before tau and the reading point leave the budget. [CORRECTED 2026-11-14: all of it at two chosen constant values of the free end L~, which are not B1724's two ends.] Values in the json only; nothing compared. 0 of 19.",
```

- **What is wrong and how we know:** First, `scope.hypotheses` (`line 27`) was not updated at all and still ends with its original open-evidence clause (`no limit proved; no independent second computation yet`), while `claim_one_line` (`line 29`) still carries `(OPEN)` and `an independent second computation (agy-002) and the end are owed` right after the bracketed upgrade. Second, naming `agy-002` inside `claim_one_line` violates `docs/seats/README.md` section twelve (`line 181`: `No session is credited in a statement of the mathematics`).

### Finding F-R82-08 — `B1925`'s dated correction drops `odd` and claims the tick's structure picks `every metallic act`, while `Nothing else on this page changes` leaves three false `"prime level"` statements standing

- **Arc:** `B1925`
- **File:** `frontier/B1925_the_selection_tested_by_changing_it_the_metallic_rivals_bronze_keeps_the_tick_structure_only_nothing_left_over_picks_golden/FINDINGS.md:126`
- **Line:** `126`
- **Commit read:** `86930f574`
- **Criterion:** `1`, `3`, and `5` (claim wider than and contradicted by the arc's own outputs, plus untravelled correction on the same page and in `P-846`)

```text
So the tick's structure picks **every metallic act**, not "every odd m with m² + 4 prime". Nothing else on this page
```

- **What is wrong and how we know:** Dropping `odd` makes the sentence false: for every even metallic parameter (`m = 2, 4, 6` in `metallic_rivals.json`, `FINDINGS.md:23, 25, 27, 34`, `test_b1925_metallic_rivals.py:33` to `35`, and our independent check across `m = 2..12` in `verify_r82_out.json`), $\ker(G_m + I \bmod (m^2 + 4))$ is not cyclic of order $m^2 + 4$ and no single frustrated line exists (`arc_verdict.json:28`: `holds for every odd metallic m ... and fails for even m`; `HARVEST_LEDGER.md:1807`: `a mark at every odd m`). Furthermore, writing `Nothing else on this page changes` (`lines 126` to `127`) leaves `"every odd m whose level is prime"`, `"every odd m with m² + 4 prime"`, and `"every odd metallic act with a prime level"` standing un-mended at `FINDINGS.md:33`, `53`, and `74` (and in `docs/POINT_REGISTER.md:1057` under `P-846`'s `2026-11-14 (B1925)` bracket).

### Finding F-R82-09 — `B1926/FINDINGS.md` writes a session (`W-F4`) as an authority whose reading settles the stated choice, and `B1926/arc_verdict.json` omits both `SM-C10` and `W-F4` from `cites_seat`

- **Arc:** `B1926`
- **File:** `frontier/B1926_at_odd_ticks_the_frames_matter_exists_only_twisted_by_the_orientation_the_tick_inverts_the_scar/FINDINGS.md:125`
- **Line:** `125`
- **Commit read:** `86930f574`
- **Criterion:** `8` and `5` (a session written as an authority settling an open choice, contradicting the rest of the page, `arc_verdict.json`, and `HARVEST_LEDGER.md`)

```text
- **The web seat's W-F4** (harvest row 1773), whose reading settles it. It recomputes this page's addendum independently and completes it: the
```

- **What is wrong and how we know:** Writing `whose reading settles it` presents a session's card (`W-F4`) as an authority deciding the open stated choice of `FINDINGS.md:57` to `58` and `113` to `118` (`main's reading, not a ruling; register row P-846`), violating `docs/seats/README.md` section thirteen Criterion `8` (`a session written as an authority`) and section twelve (`No session accepts, approves or rules`), and contradicting `B1926/arc_verdict.json:29` (`Whether the twisted modules count as the frame's matter is a stated choice`) as well as `docs/HARVEST_LEDGER.md:1826` (`row 1773`, which is marked `RECEIVED`, not verified on `main`, and records no settlement). In addition, `B1926/arc_verdict.json:17` to `19` (`cites_seat`) lists only `W-C8 part 2a` (`row 1755`) and omits both `SM-C10` (`row 1765`) and `W-F4` (`row 1773`) cited in `FINDINGS.md:120` to `128`.

### Finding F-R82-10 — `B1927/FINDINGS.md`'s corner table prints a step ratio in line `73` that disagrees with `arc_corner_run.txt`, `arc_corner.json`, and `arc_verdict.json`

- **Arc:** `B1927`
- **File:** `frontier/B1927_the_canonical_end_is_covariant_the_read_out_needs_no_chosen_end_and_analyticity_picks_the_length_two_horocycle/FINDINGS.md:73`
- **Line:** `73`
- **Commit read:** `86930f574`
- **Criterion:** `2` (a number that differs from its source)

```text
  | L_max, the maximal horoball | **1.79** (both angles) | 1.98 |
```

- **What is wrong and how we know:** `verification/arc_corner_run.txt` (`lines 1` and `3`), `verification/arc_corner.json` (both `80` degrees and `70` degrees), and `arc_verdict.json:19` all record `L_max`'s inner step ratio as one hundred and ninety-nine hundredths (just under two, matching a linear corner, and inside `test_b1927_canonical_end.py:77`'s `abs(rmax - 2)` check), whereas `FINDINGS.md:73` prints one hundred and seventy-nine hundredths (`string_1_79_in_arc_corner_outputs == false` in `verify_r82_out.json`). Also in `B1927/FINDINGS.md:100` to `107`, the `Files` list omits `verification/arc_corner.py`, `verification/mirror_lines.py`, and `verification/arc_gap_run.txt` (the last of which has no tracked producer script in `verification/`).

### Finding F-R82-11 — `B1928/arc_verdict.json` says `three hypotheses unchecked`, contradicting `B1928/FINDINGS.md` (`every hypothesis checked`)

- **Arc:** `B1928`
- **File:** `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/arc_verdict.json:21`
- **Line:** `21`
- **Commit read:** `86930f574`
- **Criterion:** `5` (updates in `FINDINGS.md` § 3 and the morning addendum did not travel to `arc_verdict.json`)

```text
 "claim_one_line": "THE READ-OUT ON THE WHOLE IS ONE AVERAGE OVER THE 24 POINTS OF ORDER 5 (OPEN: a proof sketch with three hypotheses unchecked): the letters' images generate SL(2, F5), which is perfect and acts transitively on the 24 points, so closed orbits equidistribute with their holonomy and R_n -> integral of F-bar against the path measure, the same at the mark, its twin and every point of order 5 (the twin's fading a theorem, the reading point removed). Predicted and confirmed: the ergodic integral of F-bar along 3 000 unconstrained words (error 6.6e-4) agrees with B1924's read-outs at n = 22 and 28, mark and twin (medians 0.46 to 0.76; one flagged sample 1.08); with the canonical end, medians 0.84 to 1.18. A seat's check of the proof is owed. 0 of 19.",
```

- **What is wrong and how we know:** `B1928/FINDINGS.md:3` states `every hypothesis checked`, `FINDINGS.md:101` states `H1 is met` (`h1_check.py`), and `FINDINGS.md:104` to `125` adds the morning addendum arguing `H2` and `H3` with `h2_h3_check.py`, yet both `scope.hypotheses` (`arc_verdict.json:19`) and `claim_one_line` (`arc_verdict.json:21`) still say `with H1 (discontinuities mu-null), H2 (tightness), H3 (length weights) unchecked` and `(OPEN: a proof sketch with three hypotheses unchecked)`.

### Finding F-R82-12 — `B1928` leaves `Hölder` roof claims standing in `PROOF_DRAFT.md` while its morning addendum says the roof `r` is unbounded `near L^∞ and R^∞`, where the per-letter roof vanishes rather than diverging

- **Arc:** `B1928`
- **File:** `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/FINDINGS.md:107`
- **Line:** `107`
- **Commit read:** `86930f574`
- **Criterion:** `1` and `5` (contradiction with un-mended `Hölder` lines `38` and `63` of `PROOF_DRAFT.md`, and mislocated divergence locus of the Farey return-time roof)

```text
  shift space. The suspension is not compact, because the roof r is unbounded near L^∞ and R^∞. But r grows only like
```

- **What is wrong and how we know:** First, `verification/PROOF_DRAFT.md:38` and `63` still stand un-mended claiming that the single-letter return-time roof $r(x)$ is **Hölder** (`and the return time r(x) is the hyperbolic length between successive crossings, Hölder in x`), contradicting `PROOF_DRAFT.md:76` and `FINDINGS.md:107`. Second, `FINDINGS.md:107` and `PROOF_DRAFT.md:76` mislocate the blow-up at `L^∞ and R^∞`: for `main`'s own closed-geodesic length formula $\ell(L^k R) = 2\operatorname{arcosh}((k + 2)/2)$ in `h2_h3_check.py`, adding one more interior cusp letter ($k \mapsto k + 1$, approaching the parabolic fixed points $L^\infty$ or $R^\infty$) increments the geodesic length by $2\operatorname{arcosh}((k + 3)/2) - 2\operatorname{arcosh}((k + 2)/2) \sim 2/k \to 0$ (`cusp_step_decay_vs_switch_growth` in `verify_r82_out.json`), whereas the $\ln k$ divergence lives at the **letter-switching** crossings $R^\infty . L^\infty$ and $L^\infty . R^\infty$ that exit and re-enter the cusp.

### Finding F-R82-13 — `B1929`'s end-to-end lock asserts a ten-billion ceiling on `worst` instead of a tight tolerance, passing even when Bohn's $\rho_A$ is shifted by one thousand or stored Siegel windings are negated

- **Arc:** `B1929`
- **File:** `frontier/B1929_the_records_odd_l_value_is_the_twisted_eta_invariant_of_the_closed_torus_bundle/verification/test_b1929_twisted_eta.py:56`
- **Line:** `56`
- **Commit read:** `86930f574`
- **Criterion:** `4` (a lock assertion whose ten-billion threshold cannot fail on false values)

```text
    assert worst < 1e10
```

- **What is wrong and how we know:** `end_to_end_run.txt` reports a maximum discrepancy around three parts in one hundred trillion across all `601` characters, yet `test_end_to_end_on_stored_windings` asserts `worst` is below ten to the tenth power. In our sandbox mutation tests (`verify_r82_out.json`), corrupting `rho_467` in `received_sm/run_c9.py` by adding `+1000` (destroying the identity $\eta_A = -\mathcal{L}_{\mathrm{odd}}(1, \chi_c)/\pi^2$ by one thousand on every character!) leaves **all three tests** in `test_b1929_twisted_eta.py` passing (`M_B1929_line56_rho_corrupted_by_plus_1000_full_suite_still_passes == true`), and negating every stored `Delta` in `main_siegel.json` (flipping the orientation sign) likewise passes `test_end_to_end_on_stored_windings` (`M_B1929_line56_negated_delta_end_to_end_test_still_passes == true`).

### Finding F-R82-14 — `B1929/arc_verdict.json` credits a session key inside `claim_one_line`

- **Arc:** `B1929`
- **File:** `frontier/B1929_the_records_odd_l_value_is_the_twisted_eta_invariant_of_the_closed_torus_bundle/arc_verdict.json:27`
- **Line:** `27`
- **Commit read:** `86930f574`
- **Criterion:** `8` / `docs/seats/README.md` § 12 (`No session is credited in a statement of the mathematics`)

```text
 "claim_one_line": "THE RECORD'S ODD L-VALUE IS THE TWISTED ETA INVARIANT OF THE CLOSED TORUS BUNDLE: eta_A(T^2_M) = rho_A + eta(T^2_M) = -L_odd(1, chi_c)/pi^2 for every hyperbolic act and every non-trivial fixed torsion character (found post hoc by the SM seat, proved by agy-exp through the Siegel functions' transformation law). Main's own code: L_odd(1)/(pi i Delta) = -2.0000000000 on all 561 characters with a non-zero Siegel winding (Re Delta < 3e-14), and the identity end to end on all 601 to 3.1e-14. The odd L-value flips with the orientation: a candidate carrier for the hand on the closed bundle. 0 of 19.",
```

- **What is wrong and how we know:** While `agy-exp` recuses on judging `X-C9`'s mathematical proof, naming the session key `agy-exp` inside `claim_one_line` violates `docs/seats/README.md` section twelve (`line 181`: `No session is credited in a statement of the mathematics`; provenance belongs in `cites_seat` and `HARVEST_LEDGER.md`, not in the one-line mathematical claim).

### Finding F-R82-15 — `scripts/gates/gates.py`'s `negative-second-computation` gate counts `"no second computation"` and `"without an independent second computation"` in `cites_seat` as a completed second computation

- **Arc / Instrument:** `negative-second-computation` gate (`WORKING_RULES.md` rule of `2026-11-13`, `P-842`)
- **File:** `scripts/gates/gates.py:3131`
- **Line:** `3131`
- **Commit read:** `86930f574`
- **Criterion:** `4` (a gate filter that lets explicit negations of a second computation pass without `PROVISIONAL`)

```text
_SECOND_NOT_YET_RE = re.compile(r"\b(owed|assigned|pending|not yet|awaited|awaiting|to come|to be made|outstanding)\b", re.I)
```

- **What is wrong and how we know:** `negative_without_second` (`lines 3153` to `3156`) treats any `cites_seat` string matching `second computation` and not matching `_SECOND_NOT_YET_RE` as a completed second computation (`made`), waiving `PROVISIONAL` in `claim_one_line`. Because `_SECOND_NOT_YET_RE` omits explicit negations and requirement words (`no`, `none`, `without`, `neither`, `lacks`, `lacking`, `missing`, `needed`, `required`), feeding `gates.negative_without_second` a `NEGATIVE` file at `B1999` with no `PROVISIONAL` and `"cites_seat": ["no second computation"]`, `["without an independent second computation"]`, or `["second computation needed"]` passes the gate with zero violations (`C-R82-3` in `verify_r82_out.json`).

---

## 3. Verification Summary on Every Remaining Item in Scope (One Line Each)

1. **`B1918` (`86930f574`):** Read `FINDINGS.md` (including its top retraction banner and bottom dated retraction), `arc_verdict.json` (`RETRACTED`, `superseded_by: "B1919"`), `step3_norm.py`, `step3_average.py`, their outputs, `docs/RETRACTIONS.md:287`, and `test_b1918_the_channel_norm.py` (`3` of `3` pytest tests passed in sandbox); retraction and numbers match across all files.
2. **`B1920` (`86930f574`):** Read `FINDINGS.md`, `arc_verdict.json`, `hecke_shifted_s2.py`, `golden_average.py`, their run files, and `test_b1920_the_line_part.py` (`2` of `2` pytest tests passed, including the unshifted-lattice planted failure); statements, scope, and run figures match.
3. **`B1921` (`86930f574`):** Read `FINDINGS.md`, `arc_verdict.json`, `s_shift.py`, `s_shift.json`, `s_shift_run.txt`, and `test_b1921_the_s_shift.py` (`2` of `2` pytest tests passed, including the unshifted-end plant); verified algebraically that $\pi \ln\operatorname{Im}(-1/\tau) = \pi\ln\operatorname{Im}\tau - 2\pi\ln|\tau|$ cancels $L \mapsto L + \ln|\tau|$ in $2\pi L + c_s = 2\pi\tilde{L} + F_u$.
4. **`B1922` (`86930f574`):** Read `FINDINGS.md`, `arc_verdict.json`, `periodic.py`, `periodic.json`, `periodic_run.txt`, and `test_b1922_periodic.py` (`2` of `2` pytest tests passed, including the non-fixed line `(1/5, 3/5)` and `S*` non-periodicity controls); numbers and scope (`reach: "single"`, golden thread) match.
5. **`B1923` (`86930f574`, outside recused own-seat/family rows and `F-R82-05`):** Independently constructed the $\mathrm{SL}(2, \mathbb{F}_5)$ Weil representation on $\mathbb{C}^5$ without importing `weil_twin.py`, confirming even-subspace traces $(1 - \sqrt{5})/2$ at $a = 1, 4$ and $(1 + \sqrt{5})/2$ at $a = 2$, verified the `docs/LAW_MAP.md` `B1019`/`B997` narrowings and `B1884` bracketed mend in `0e637ea9e..86930f574`, and ran `test_b1923_the_twin_and_the_triplet.py` (`3` of `3` passed).
6. **`WORKING_RULES.md` (`2026-11-13` rule), `tests/test_negative_second_computation.py`, and `tests/GATE_CONTROLS.json` (`86930f574`, outside `F-R82-15`):** Read lines `354` to `384` of `WORKING_RULES.md`, `tests/GATE_CONTROLS.json:54`, and all `80` lines of `tests/test_negative_second_computation.py` (`5` of `5` twin-paired tests passed in sandbox); the rule text, starting arc `B1923`, and `GATE_CONTROLS.json` registration align with `P-842`.
7. **Register rows `P-839` through `P-847` (`86930f574`, outside recused clauses and `P-846`'s un-mended `B1925` `"prime level"` note in `F-R82-08`):** Read lines `1050` through `1058` of `docs/POINT_REGISTER.md` in full against the arcs and working-rule entries they cite (`P-839` on `FK12`, `P-840` and `P-841` in plain words with no post-`2026-11-11` direct quotation of the author, `P-842` on `negative-second-computation`, `P-843` on `B1923`'s Weil lead, `P-844` on look-elsewhere freedom, `P-845` on thread measures, `P-846` on `m000` and `B1926`/`B1929`, and `P-847` on `SIXY['H'] = 3`); every owed follow-up named across `B1917` through `B1929` has a corresponding register row.
8. **Cited `HARVEST_LEDGER.md` rows (`926, 945, 949, 1754, 1755, 1764, 1765, 1773`, outside recused rows `1621, 1776, 1788, 1790` and row `1713` in `F-R82-05`):** Read each cited row at `86930f574` against the arc citing it (`B1923`, `B1925`, `B1926`, `B1929`); dispositions and check labels match their evidence once `B1926/FINDINGS.md:125` (`F-R82-09`) is corrected to match row `1773`.

`0 of 19.`
