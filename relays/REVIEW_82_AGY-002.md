# Review 82 — Cold Reading by Seat `agy-002` (`A2-R82`)

- **Seat:** `agy-002` (branch `agy-002/verify`, reading messages `M28` and `M30`)
- **Commit read:** `86930f574` (`origin/review-82/read`, covering window `0e637ea9e` to `73e71e277`)
- **Expectations committed first:** `relays/cards/AGY-002_A2-R82_review-82.md` at `1dde76be0`
- **Standalone numerical counterchecks committed before this file:** `relays/r82/verify_r82_checks.py`, `relays/r82/verify_r82_checks_out.txt`, and `relays/r82/verify_r82_checks_results.json` at `6125fca5c`
- **Quotation discipline:** Every double-quoted string in this document is an exact single-line verbatim substring of the named file and one-based line number at commit `86930f574`. All key numbers, signs, exponents, and counts are also stated in plain English words so nothing is lost through the number mask.

---

## 0. Protocol Section Thirteen Exclusions (Own Work Left for Another Reader)

Per `docs/seats/README.md` Section Thirteen, `agy-002` does not judge sections where `main` evaluates `agy-002`'s own cards and leaves those lines for another reader:

1. **`B1923` (`A2-R80b`, harvest row `1749`):** `frontier/B1923_the_load_bearing_negatives_reexamined_and_the_twin_chooses_the_icosahedral_triplet/FINDINGS.md` lines `14–16` and `47`, and `arc_verdict.json` line `17` (and the `B1884` mend clause on line `32`).
2. **`B1924` (`A2-B1924`, harvest row `1790`):** `frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/FINDINGS.md` lines `167–195` (`Second computation, corrections and upgrade`), and `arc_verdict.json` lines `3`, `17–19`, and the `[UPGRADED ...]` prefix on line `29`.
3. **Register and harvest rows citing `agy-002`:** `docs/HARVEST_LEDGER.md` lines `998` (row `945` addendum), `1002` (row `949` addendum), `1802` (row `1749`), `1842` (row `1789`), `1843` (row `1790`), and `1844` (row `1791`); `docs/POINT_REGISTER.md` lines `543` (`P-332` `2026-11-14` closure note), `931` (`P-720` `2026-11-14` note), and `1056` (`P-845` final bracket on row `1790`).

*(Neutral handoff note for another reader on those excluded boundaries: when `B1924`'s json status on line three was upgraded to proved, `B1924/FINDINGS.md` line three remained open and `B1924/arc_verdict.json` line twenty-nine retained its earlier open tag inline; and when `P-332` was marked done on `docs/POINT_REGISTER.md` line `543`, no dated note was added to `frontier/B1121_pair_orbits/FINDINGS.md`. Both sit on `agy-002` boundaries and are handed off unjudged.)*

---

## 1. Findings (`R82-01` through `R82-28`)

### A. Lock Assertions That Cannot Fail or Omit the Selected Case

#### `R82-01` — `B1929` lock asserts ten to the plus ten (`1e10`) instead of ten to the minus ten (`1e-10`)
- **File and line (`86930f574`):** `frontier/B1929_the_records_odd_l_value_is_the_twisted_eta_invariant_of_the_closed_torus_bundle/verification/test_b1929_twisted_eta.py`, line `56`
- **Verbatim quotation:** `"    assert worst < 1e10"`
- **What is wrong:** `test_end_to_end_on_stored_windings` checks the maximum discrepancy `worst` between Bohn's twisted eta invariant and minus the real part of the odd L-value over pi squared across all six hundred and one characters. `B1929/FINDINGS.md` line `32` reports agreement to three point one times ten to the minus fourteen (`3.1e-14`), and line `32` of the same test file uses ten to the minus ten (`< 1e-10`). Line `56` omits the minus sign in the exponent and asserts `worst` is less than ten billion (`1e10`).
- **Evidence (`relays/r82/verify_r82_checks.py` check one):** Flipping the sign of the odd L-value or zeroing it produces an order-one discrepancy (about five point three three), which still passes `< 1e10`. Thus the primary end-to-end lock cannot fail on any bounded discrepancy.

#### `R82-02` — `B1917` lock's planted half-width strip check is an algebraic tautology implied by the preceding line
- **File and line (`86930f574`):** `frontier/B1917_the_slope_and_the_kronecker_function_one_l_function_on_the_threads_geodesic/verification/test_b1917_one_l_function.py`, line `32`
- **Verbatim quotation:** `"assert abs(L / (H.H(2) * R / 2) - 2) < 1e-4            # planted: half the orbit strip is off by exactly 2"`
- **What is wrong:** Line `32` never calls `H.rhs` on a half-width fundamental strip; it divides the scalar `H.H(2) * R` already computed on line `30` by two. Because line `31` has just asserted `abs(L - H.H(2) * R) / abs(L) < 1e-5`, for any nonzero numbers `L` and `X` with relative difference `u` below ten to the minus five, the quantity `abs(L / (X / 2) - 2)` is bounded above by `2 u / (1 - u)`, which is at most two point zero zero zero zero two times ten to the minus five — strictly below ten to the minus four (`1e-4`).
- **Evidence (`verify_r82_checks.py` check two):** Once line `31` passes, line `32` cannot fail under any mutation of `hecke_s2.py`.

#### `R82-03` — `B1925` lock's `-A` order-exchange assertion is a polynomial determinant identity that cannot fail
- **File and line (`86930f574`):** `frontier/B1925_the_selection_tested_by_changing_it_the_metallic_rivals_bronze_keeps_the_tick_structure_only_nothing_left_over_picks_golden/verification/test_b1925_metallic_rivals.py`, line `53`
- **Verbatim quotation:** `"assert SE.smith_order(-a - 1, -b, -c, -d - 1) == lev    # -A exchanges the two orders"`
- **What is wrong:** Line `51` defines `lev = SE.smith_order(a + 1, b, c, d + 1)`. In `selection_equivalence.py` lines `16–18`, `smith_order(x, y, z, w)` returns `abs(x * w - y * z)`. Because negating all four entries of any two-by-two matrix leaves its determinant unchanged (`(-x)(-w) - (-y)(-z) == x w - y z`), `SE.smith_order(-a - 1, -b, -c, -d - 1) == lev` holds identically as an algebraic tautology for every four-tuple `(a, b, c, d)`, even for non-unimodular matrices, without checking Smith invariants or testing `(-A) + I` against `A - I`.
- **Evidence (`verify_r82_checks.py` check seven):** Verified to hold identically across two hundred random integer four-tuples with arbitrary determinants. (In the same lock, `test_snappy_names` lines `59–63` catches `ImportError` with `return` rather than `pytest.skip`, passing silently when `snappy` is absent.)

#### `R82-04` — `B1927` lock computes S-covariance for the selected length-two end `l2_s` but never asserts on it
- **File and line (`86930f574`):** `frontier/B1927_the_canonical_end_is_covariant_the_read_out_needs_no_chosen_end_and_analyticity_picks_the_length_two_horocycle/verification/test_b1927_canonical_end.py`, line `29` (with lines `30–31`)
- **Verbatim quotation:** `"lm_s, l2_s = GR.ends(-1 / t, cs)"`
- **What is wrong:** `test_covariance` computes both `lm_s` (`L_max`) and `l2_s` (`L_2`) at `-1 / t` on line `29`, but lines `30–31` assert covariance only on `lm_s` (the maximal-horoball end ruled out in Section Three of `B1927`) and leave `l2_s` (the canonical length-two end selected by the arc) completely unused. Any covariance defect in `L_2` passes `test_covariance`.

#### `R82-05` — `B1922` lock leaves the third kept window unbounded and tests only the mirror-degenerate height
- **File and line (`86930f574`):** `frontier/B1922_the_frame_is_periodic_along_the_thread_exactly_at_the_threads_own_line/verification/test_b1922_periodic.py`, line `19` (with lines `1` and `14`)
- **Verbatim quotation:** `"r = P.deviations(-P.ell / 2, (0.4, 0.8)); q = P.deviations(-P.ell / 2, (0.2, 0.6))"`
- **What is wrong:** First, on line `14`, `sorted(v['S, St'] for v in own)[1] < 1e-8` checks only the two smallest of the three kept windows and places no upper bound at all on `sorted(...)[2]` (`7.83e-5` in `periodic.json`, cited on `FINDINGS.md` lines `23` and `25`). Second, despite docstring line `1` saying the lock checks what the page says, `test_b1922_periodic.py` never opens `FINDINGS.md`. Third, line `19` recomputes only `s0 = -P.ell / 2`, where `Im tau == Im(gamma tau)` by mirror symmetry, so even the non-fixed, non-periodic order-two line `(0, 1/2)` passes `S, St < 1e-8` there (`4.43e-11`), whereas in the shifted window `-P.ell / 2 + 0.15` it fails by two point zero two.

#### `R82-06` — `test_b1461_governance_delta.py` wraps its waiver assertions in an `if` with no `else` branch
- **File and line (`86930f574`):** `tests/test_b1461_governance_delta.py`, line `114`
- **Verbatim quotation:** `"    if gates.review_waiver_covers(40, w, since=since):"`
- **What is wrong:** Comment lines `111–112` state that without a live waiver the test holds as before, yet all assertions on `review_waiver_covers` sit inside the `if` block on lines `114–118` with no `else` branch. Once the waiver expires (or if `review_waiver_covers` were broken to return `False` unconditionally), zero assertions execute on `review_waiver_covers`.

---

### B. Numbers Differing From Their Source

#### `R82-07` — `B1927` reports the maximal-horoball arc-corner ratio as one point seven nine (`1.79`) instead of one point nine nine (`1.99`)
- **File and line (`86930f574`):** `frontier/B1927_the_canonical_end_is_covariant_the_read_out_needs_no_chosen_end_and_analyticity_picks_the_length_two_horocycle/FINDINGS.md`, line `73`
- **Verbatim quotation:** `"| L_max, the maximal horoball | **1.79** (both angles) | 1.98 |"`
- **What is wrong:** `verification/arc_corner_run.txt` lines `1` and `3` report `1.99` (one point nine nine, NOT one point seven nine) at both eighty degrees and seventy degrees for the `0.01` to `0.02` step.
- **Evidence (`verify_r82_checks.py` check three):** Recomputing `(vals['0.02'][0] - vals['0.0'][0]) / (vals['0.01'][0] - vals['0.0'][0])` from `verification/arc_corner.json` gives `1.9924` at eighty degrees and `1.9918` at seventy degrees; `B1927/arc_verdict.json` line `19` states `ratio 1.99`, and `test_b1927_canonical_end.py` line `77` asserts `abs(rmax - 2) < 0.2`, which `1.79` fails (`0.21 > 0.20`).

#### `R82-08` — `B1928` reports the fine grid size as one thousand and thirty-four (`1 034`) instead of one thousand and forty-six (`1 046`)
- **Files and lines (`86930f574`):**
  1. `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/FINDINGS.md`, line `27`: `"(1 034 points, the finer of two grids) and averaged along 3 000 unconstrained random words of 40 letters. The"`
  2. `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/arc_verdict.json`, line `19`: `"the numerical test on a grid of 1 034 points, interpolation median error 4.5e-4 on ratios and 3e-3 on mixing moduli"`
- **What is wrong:** Both `FINDINGS.md` and `arc_verdict.json` state `1 034` points, whereas `verification/fiber_grid_fine_run.txt` line `42` prints `grid: 1046 points` and `verification/fiber_grid_fine.json` contains exactly one thousand and forty-six (`1046`) entries (`verify_r82_checks.py` check four).

#### `R82-09` — `B1923` reports twenty-six (`26`) negative-scan rows instead of thirty (`30`)
- **Files and lines (`86930f574`):**
  1. `frontier/B1923_the_load_bearing_negatives_reexamined_and_the_twin_chooses_the_icosahedral_triplet/FINDINGS.md`, line `10` (and lines `23`, `91`): `"- **26 load-bearing negatives** of the last two weeks, found by a read-only reader's scan"`
  2. `frontier/B1923_the_load_bearing_negatives_reexamined_and_the_twin_chooses_the_icosahedral_triplet/arc_verdict.json`, line `32`: `"26 negatives of two weeks with their second-computation status (three done, one assigned, the rest assigned) and main's reading of what each wall teaches;"`
- **What is wrong:** `verification/LOAD_BEARING_NEGATIVES.md` contains thirty (`30`) negative rows across sections `A` through `D`: `A1..A9` (nine), `B1..B6` (six), `C1..C6` (six), and `D1..D9` (nine), summing to thirty (`31` if section `E`'s `B1918` entry is counted), not twenty-six (`verify_r82_checks.py` check five).

#### `R82-10` — `B1924` reports per-column spreads over forty-eight grid points as the spread across `B1667`'s fifty-four points
- **File and line (`86930f574`):** `frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/FINDINGS.md`, line `134` (echoed on `docs/POINT_REGISTER.md` line `1056`)
- **Verbatim quotation:** `"- neither is constant in L̃: across B1667's 54 points the spread is 0.41 to 0.65 for L_max and 0.16 to 0.27 for L_2."`
- **What is wrong:** Across all fifty-four points of `B1667/verification/the_canonical_cusp.json`, `L + (1/2) log Im tau` has a single global spread of zero point seven two (`0.7160`, from `0.6202` to `1.3362`) for `L_max` and zero point two seven (`0.2708`, from `2.7146` to `2.9854`) for `L_2`. The intervals `0.41 to 0.65` and `0.16 to 0.27` are the ranges of within-column spreads across the five fixed-`Re tau` grid columns, which contain only forty-eight points (`verify_r82_checks.py` check six).

#### `R82-11` — `B1917` miscounts `hecke_s2` accuracy across seventeen characters (`16` vs `17`, `4.5e-8` vs `4e-8`, uncommitted `1.6e-7`)
- **Files and lines (`86930f574`):**
  1. `frontier/B1917_the_slope_and_the_kronecker_function_one_l_function_on_the_threads_geodesic/FINDINGS.md`, line `26`: `"against H(2)·Z_tot(2, χ) summed over orbit representatives, on 17 characters at four levels, to 4 × 10⁻⁸; one"`
  2. `frontier/B1917_the_slope_and_the_kronecker_function_one_l_function_on_the_threads_geodesic/FINDINGS.md`, line `27` (also `arc_verdict.json` lines `22` and `24`): `"character whose series has no phase in n converges to 1.6 × 10⁻⁷ as the m-range grows (`hecke_s2.py`). Main's"`
- **What is wrong:** In `verification/hecke_s2.json` and `hecke_s2_run.txt`, only sixteen of the seventeen characters are near `1e-8`, while the seventeenth (`+LR 3 (1, 0)`, `hecke_s2_run.txt` line `12`) has relative discrepancy two point zero times ten to the minus four (`2.03e-4`), omitted altogether in `arc_verdict.json` lines `22` and `24`. Among the sixteen, three entries have `4.55e-8` (rounding to five times ten to the minus eight, exceeding `4e-8`). Finally, `hecke_s2.py` runs only `Mmax = 60` and never computes `1.6e-7` (`verify_r82_checks.py` check two). (In `kronecker_s1_run.txt` lines `4` and `6`, two of six characters also differ by `5.0e-4` abs / `3.7e-4` rel against `arc_verdict.json`'s `about 1e-4`.)

#### `R82-12` — `B1919` states rotated-shift failure `0.3 to 7` instead of `0.051 to 17.8` on its twenty-four kept cases
- **File and line (`86930f574`):** `frontier/B1919_the_channel_norm_is_the_shifted_lattices_kronecker_limit_at_the_kernels_shift/FINDINGS.md`, line `20`
- **Verbatim quotation:** `"truncation; the seat reports 10⁻¹¹ with its own code. The rotated placement of u fails by 0.3 to 7, as it must."`
- **What is wrong:** `0.3 to 7` came from `seat_formula.py`'s four ad-hoc characteristics at a single point (with no committed `_run.txt`). Across the twenty-four kept rows in `seat_formula_check.json`, the rotated shift actually fails by zero point zero five one to seventeen point eight (`0.0511` to `17.80`, `verify_r82_checks.py` check ten). Moreover, no script in `B1919/verification/` generates `seat_formula_check.json`, and sixteen of its twenty-four rows use four-decimal truncated moduli `[-0.1004, 0.9431]` and `[1.1004, 0.9431]` lying `4.4e-5` off the golden geodesic.

#### `R82-13` — `B1927` reports paired `L_max` vs `L_2` median `|z|` near twenty (`92 %` above two) without qualifying `n = 16`, omitting `n = 22`
- **File and line (`86930f574`):** `frontier/B1927_the_canonical_end_is_covariant_the_read_out_needs_no_chosen_end_and_analyticity_picks_the_length_two_horocycle/FINDINGS.md`, line `32` (with line `31`)
- **Verbatim quotation:** `"20, with 92 % of the numbers above 2, at the mark and at the twin."`
- **What is wrong:** Neither `canon_compare.py` nor `canon_compare_run.txt` prints this comparison. Recomputing from `canon_readout.json` (`verify_r82_checks.py` check three) shows `20.56` (`91.7 %`) and `19.98` (`91.7 %`) hold at `n = 16`, whereas at `n = 22` the paired medians are twenty-five point three nine (`100 %` above two, all twenty-four components) at the mark and twenty-six point six seven (`91.7 %`) at the twin.

#### `R82-14` — `docs/POINT_REGISTER.md` skips rank forty-five (`44` jumps to `46`), propagating ninety-three debts numbered to ninety-four into `MAP.md` and `NODES.json`
- **File and lines (`86930f574`):** `docs/POINT_REGISTER.md`, lines `99` and `103` (propagated into `frontier/B1858_the_closure_map/MAP.md` lines `28`, `345–346`, `394` and `NODES.json` lines `5073`, `6921`)
- **Verbatim quotations:**
  1. Line `99`: `"44. P-540 — B940's instrument is used by C10's seal on m004 (P-330)."`
  2. Line `103`: `"46. P-156 — B1606/B1652's D2 ±3 index rests on the end condition and dim Λ+ - 3."`
- **What is wrong:** Removing rank forty-five without renumbering left ninety-three open debts numbered `1..44, 46..94` (`verify_r82_checks.py` check eleven), so `MAP.md` simultaneously reports `93` open debts in its summary table and rank `94` at the bottom of its ranked list.

---

### C. Claims Wider Than Proved or Mathematically False Against Their Evidence

#### `R82-15` — `B1925`'s `2026-11-14` correction claims the tick's structure picks **every** metallic act (dropping `odd`)
- **File and line (`86930f574`):** `frontier/B1925_the_selection_tested_by_changing_it_the_metallic_rivals_bronze_keeps_the_tick_structure_only_nothing_left_over_picks_golden/FINDINGS.md`, line `126`
- **Verbatim quotation:** `"So the tick's structure picks **every metallic act**, not"`
- **What is wrong:** Line `14` defines metallic acts `G_m = L^m R^m` for every positive integer `m` (odd and even). Omitting `odd` on line `126` makes the claim false for every even `m` (`m = 2, 4, 6, ...`), where `G_m + I = [[m^2 + 2, m], [m, 2]]` has entrywise gcd two, Smith invariants `(2, (m^2 + 4)/2)`, no single cyclic frustrated line (`one_cyclic_line: false` in `metallic_rivals.json`), and no tick-parity law (`verify_r82_checks.py` check seven; `B1925/arc_verdict.json` line `28` explicitly notes it fails for even `m`).

#### `R82-16` — `B1928`'s top banner claims every hypothesis is checked while the arc and json leave hypotheses unchecked
- **File and line (`86930f574`):** `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/FINDINGS.md`, line `3`
- **Verbatim quotation:** `"**Verdict: OPEN** (a proof from standard ergodic theory, every hypothesis checked; its numerical prediction"`
- **What is wrong:** Line `3` asserts `every hypothesis checked`, directly contradicting `FINDINGS.md` lines `52–58` (`Not proved: H1 ... H2 ... H3`), `FINDINGS.md` lines `123–124` (`H2` and `H3` sent out as an open check), and `B1928/arc_verdict.json` lines `19` and `21` (`a proof sketch with three hypotheses unchecked`).

#### `R82-17` — `B1925` falsely states `1` has more square roots than `±1` modulo `m^2 + 4` at `m = 11` and `m = 13`, with no committed check
- **File and line (`86930f574`):** `frontier/B1925_the_selection_tested_by_changing_it_the_metallic_rivals_bronze_keeps_the_tick_structure_only_nothing_left_over_picks_golden/FINDINGS.md`, line `123` (with line `124`; echoed on `docs/HARVEST_LEDGER.md` line `1807`)
- **Verbatim quotation:** `"- **The parity law therefore holds at every odd m.** Main checked it directly at m = 9, 11 and 13, where 1 has more"`
- **What is wrong:** Modulo `N = m^2 + 4`, `1` has four square roots (`1, 16, 69, 84`) at `m = 9` (`N = 85 = 5 * 17`), but at `m = 11` (`N = 125 = 5^3`, an odd prime power) and `m = 13` (`N = 173`, which is prime) the unit group `(Z/NZ)^x` is cyclic, so `1` has **only two** square roots (`±1`) (`verify_r82_checks.py` check seven). In addition, no script or output in `B1925/verification/` runs `m = 9, 11, 13` (`metallic_rivals.py` stops at `m = 7`).

#### `R82-18` — `B1925` claims positive-trace equivalence on all three hundred and sixty hyperbolic acts when only one hundred and eighty have positive trace, and `smith_order` computes `|det|`
- **Files and lines (`86930f574`):**
  1. `frontier/B1925_the_selection_tested_by_changing_it_the_metallic_rivals_bronze_keeps_the_tick_structure_only_nothing_left_over_picks_golden/FINDINGS.md`, line `40` (with line `38`): `"- For a positive-trace hyperbolic act, **torsion-free ⟺ tr A = 3 ⟺ the frustrated level is 5**, on all 360. By"`
  2. `frontier/B1925_the_selection_tested_by_changing_it_the_metallic_rivals_bronze_keeps_the_tick_structure_only_nothing_left_over_picks_golden/verification/selection_equivalence_run.txt`, line `1`: `"for tr > 0, torsion-free <=> tr = 3 <=> level 5: 360 agree; -A exchanges the two orders: 360 agree"`
- **What is wrong:** Of the three hundred and sixty hyperbolic `SL(2, Z)` matrices with entries in `[-7, 7]`, exactly one hundred and eighty (`180`) have positive trace and one hundred and eighty (`180`) have negative trace (`verify_r82_checks.py` check seven). In `selection_equivalence.py` lines `53–56`, `else: ok_equiv += 1` unconditionally increments the counter on all one hundred and eighty negative-trace matrices (where the equivalence fails, e.g. `-LR` has trace `-3` and `|det(-LR + I)| = 1`). Furthermore, contrary to `FINDINGS.md` line `38`, `smith_order` on lines `16–18` returns `abs(a * d - b * c)` directly rather than computing Smith normal form (`smith` on lines `21–23` is never called on line `51`).

#### `R82-19` — `B1920` (and `B1919`, `P-384`) misstates the `s = 1` Laurent constant term (`8.9068` vs `32.5023`), drops `+ (1/2) #(-I)` on `167` characters, and omits `21` undefined zero-residue entries
- **Files and lines (`86930f574`):**
  1. `frontier/B1920_the_channel_norms_line_part_averaged_along_the_thread_is_the_shifted_partial_zetas_kronecker_limit/FINDINGS.md`, line `16` (also line `27`, `arc_verdict.json` line `25`, `B1919/FINDINGS.md` line `27`, `POINT_REGISTER.md` line `595`): `"3. **The line part's average along the thread is the Kronecker limit at s = 1 of the thread's shifted partial"`
  2. `frontier/B1920_the_channel_norms_line_part_averaged_along_the_thread_is_the_shifted_partial_zetas_kronecker_limit/FINDINGS.md`, line `18`: `"L-function whose odd value at s = 1 is 4π² times the slope (B1917). **So the slope and the channel norm are two"`
  3. `frontier/B1920_the_channel_norms_line_part_averaged_along_the_thread_is_the_shifted_partial_zetas_kronecker_limit/FINDINGS.md`, line `10`: `"with their reasons, nothing adjusted after the run). On all 601 lines and four channels of B1737's population:"`
- **What is wrong (`verify_r82_checks.py` check nine):**
  1. **Laurent constant-term error:** Expanding `int_0^ell E^{(u)}(z, s) ds = H(s) zeta_shift(s, u)` around `s = 1`, `zeta_shift(s, u) = 2 ell / (s - 1) + kappa_0(u) + O(s - 1)` has a simple pole while `H(s) = (pi / 2)(1 - 2 ln 2 (s - 1) + ...)`. Matching constant terms gives `<F_u> = (pi / (2 ell)) kappa_0(u) - 2 pi ln 2`, NOT `kappa_0(u)`: on `+LR 2` (`ell = 8 ln phi = 3.8497`), `<F_u> = 8.9068` whereas `kappa_0(u) = 32.5023` (and under `M -> M^2`, `<F_u>` is period-invariant while `kappa_0(u)` doubles).
  2. **Omitted `#(-I)` term:** Per `B1917/FINDINGS.md` line `16`, the odd value at `s = 1` is `4 pi^2 (slope + (1/2) #(-I))`; `#(-I)` is nonzero on one hundred and sixty-seven (`167`) of the six hundred and one characters across the nine negative-sign levels.
  3. **Omitted `R_s = 0` poles:** Of the `601 * 4 = 2 404` channel entries, twenty-one have `u_s = (0, 0) mod Z^2` (`R_s = 0`) where `B1656`'s normalised channel norm has a pole and was excluded (`2 383` evaluated in `d687a9180:relays/SM_C7_ONE_L_FUNCTION.md` lines `141` and `197`).

#### `R82-20` — `B1922` falsely claims periodicity holds *not at any other line* (false on `(1/5, 2/5)` and `(0, 0)` even on the golden thread)
- **File and line (`86930f574`):** `frontier/B1922_the_frame_is_periodic_along_the_thread_exactly_at_the_threads_own_line/FINDINGS.md`, line `28` (also line `1`, `arc_verdict.json` line `24`, and `docs/POINT_REGISTER.md` line `987`)
- **Verbatim quotation:** `"thread's own line, and not at any other line.** The average of the frame over one period is then canonical (it does"`
- **What is wrong:** `periodic.py` tested only one thread (`TR`) and two lines (`(2/5, 4/5)` and `(1/5, 3/5)`). Even on the golden thread, at least two other lines satisfy `(gamma_line ± I) v = 0 (mod 1)` and repeat across the period to ten to the minus ten: the distinct order-five twin `(1/5, 2/5)` (`7.74e-11` symmetric, `8.24e-10` shifted) and `(0, 0)` (`7.36e-11` and `1.22e-9`); general hyperbolic acts fix every torsion point in `ker(gamma_line ± I mod 1)`. (Also `POINT_REGISTER.md` line `987` writes `to 3e-10` when the second clean window in `periodic.json` is `9.79e-10`.)

#### `R82-21` — `B1928`'s `PROOF_DRAFT.md` and `FINDINGS.md` invert the single-letter return-time asymptotics near `L^inf, R^inf`, contradict themselves on Hölder/boundedness, and report unrecorded interpolation medians
- **Files and lines (`86930f574`):**
  1. `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/verification/PROOF_DRAFT.md`, line `38` (and line `63`): `"cross-section, and the return time r(x) is the hyperbolic length between successive crossings, Hölder in x. The"`
  2. `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/verification/PROOF_DRAFT.md`, line `44`: `"converges weak-* to ν. f is bounded, because the outputs are ratios of singular values and moduli of unitary"`
  3. `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/verification/PROOF_DRAFT.md`, line `76` (identical on `FINDINGS.md` line `107`): `"shift space. The suspension is not compact, because the roof r is unbounded near L^∞ and R^∞. But r grows only like"`
  4. `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/FINDINGS.md`, line `43`: `"error 4.5 × 10⁻⁴ (90 % below 2.3 × 10⁻³). The mixing moduli have median error 3 × 10⁻³ (90 % below 2 × 10⁻²). The"`
- **What is wrong:**
  1. On the single-letter shift `{L, R}^Z`, a cusp syllable `L^m R` has total hyperbolic length `2 arccosh((m + 2)/2) ~ 2 ln m` across `m + 1` letters, so approaching `L^inf` or `R^inf` sends the per-letter hyperbolic return time `r` to **zero** (`r(L^inf) = r(R^inf) = 0`, matching parabolic `tr(L^n) = 2`), whereas `r(x)` is unbounded logarithmically (`~ ln k + ln m`) at **letter-switch crossings** `... L^k . R L^m ...` (`verify_r82_checks.py` check four).
  2. Calling `r(x)` Hölder on compact `{L, R}^Z` (lines `38`, `63`) contradicts `r` being unbounded (line `76`); calling `f(x) = int_0^{r(x)} F dt` bounded (line `44`) is false wherever `r(x)` is unbounded; and Parry–Pollicott Chapter Eight orders prime orbits by hyperbolic flow period `ell <= T` (which equidistributes to Liouville measure, reading `(b)` of `P-845`), whereas combinatorial word-length ordering `n` equidistributes to the Bernoulli shift measure via spectral gap of the finite `SL(2, F_5)` transfer operator plus uniform-integrability truncation.
  3. No script or output in `B1928/verification/` computes the median/percentile errors `4.5e-4` (`2.3e-3`) or `3e-3` (`2e-2`) (`fiber_ergodic.py` computes only `worst`); and `h1_check.py` line `33` checks `H1` only for `L_2` while `canon` in `fiber_ergodic.py` averages `L_max` as well.

#### `R82-22` — `B1918` (`the numbers stand`) multiplies its geodesic average by period `ell = 1.92485` (`29` on `177` instead of `15.2` on `92.2`) and cites four uncommitted numbers
- **Files and lines (`86930f574`):**
  1. `frontier/B1918_the_channel_norm_is_not_the_l_functions_coefficient_at_a_point_or_on_average/verification/step3_average.py`, line `27`: `"avgN.append(ell / 2 * sum(wi * S.norm(c, z) for wi, z in zip(w, zs)))"`
  2. `frontier/B1918_the_channel_norm_is_not_the_l_functions_coefficient_at_a_point_or_on_average/FINDINGS.md`, line `25` (with lines `4`, `24–29`, `33`, `73` and `arc_verdict.json` line `26`): `"22 to 26. A planted norm that is exactly of the Kronecker form is recovered to 5 × 10⁻¹⁵ with its coefficients"`
- **What is wrong:** `B1918`'s retraction explicitly retains its numbers (`The computations below stand` / `the numbers stand`). Yet `step3_average.py` line `27` multiplies Gauss-Legendre weights on `[-1, 1]` (sum two) by `ell / 2` instead of `1 / 2`, computing the unnormalised period **integral** (`ell = 4 ln phi = 1.92485`) rather than the geodesic **average** — inflating the true average residual `15.21` on spread `92.16` to `29.28` on `177.39` (`verify_r82_checks.py` check nine). In addition, none of `22 to 26` (actually `22 to 25` on `c + 1/2`), `5e-15`, `4e-10`, or `0.8 on 107` appears in any committed script or output of `B1918`.

#### `R82-23` — Scope overstatements in `B1926/arc_verdict.json` (level `7` twisted not run; `W-C8 part 2a` scope), `B1923` (unassigned/uncontemplated scan rows), and `B1927` (`arc_gap_run.txt` orphan output)
- **File and line (`86930f574`):** `frontier/B1926_at_odd_ticks_the_frames_matter_exists_only_twisted_by_the_orientation_the_tick_inverts_the_scar/arc_verdict.json`, line `29`
- **Verbatim quotation:** `"Proved; recomputed by main's own Fox calculus on the golden tick's levels 1 to 8 (odd levels: 3, 10, 28 characters, none with a class on the scar; twisted: all; even levels: 4, 15, 44, all), the web seat's sealed W-C8 part 2a agreeing on every count."`
- **What is wrong:** First, in `B1926`, `odd_ticks_no_modules.py` line `176` ran the twisted (`keep_mu=False`) Fox-calculus check only at levels `3` and `5`, skipping level `7` (`28` characters, shown as `—` on `FINDINGS.md` line `44`; `verify_r82_checks.py` check eight), and `W-C8 part 2a` (`web_seat_part2a_out_e37753fd7.txt`) did not compute twisted counts. Second, in `B1923` (`FINDINGS.md` lines `13`, `25` and `arc_verdict.json` line `32`, quoted in `R82-09`), ten scan rows in Section One's table have no seat assignment (`next: contemplation` / `none` / `mended`) and Section Two contemplates only seven scan entries (leaving `A8, A9` and `C2, C3` with neither). Third, in `B1927/FINDINGS.md` line `66`, `verification/arc_gap_run.txt` has no generating `.py` script anywhere in `B1927/verification/`.

---

### D. Session Written as Authority, Stronger Section Twelve Labels, and Session Crediting

#### `R82-24` — `B1926` writes a helper session's `RECEIVED` relay as settling an open stated choice (plus `accepted` and `approved` in cited harvest rows)
- **Files and lines (`86930f574`):**
  1. `frontier/B1926_at_odd_ticks_the_frames_matter_exists_only_twisted_by_the_orientation_the_tick_inverts_the_scar/FINDINGS.md`, line `125`: `"- **The web seat's W-F4** (harvest row 1773), whose reading settles it. It recomputes this page's addendum independently and completes it: the"`
  2. `docs/HARVEST_LEDGER.md`, line `1812` (row `1759`): `"| **RECEIVED**: the amendments accepted and SM-C9 approved (M25); B1919 stays the record's own content | B1919, WP-1.9 | 2026-11-14 |"`
  3. `docs/HARVEST_LEDGER.md`, line `1817` (row `1764`): `"The post hoc identity (the twisted eta equals -L_odd(1, chi_c)/pi^2 on all 601 characters) goes to the seat's sealed SM-C9b, approved"`
- **What is wrong:** `docs/seats/README.md` Section Twelve (`line 179`) and Section Thirteen item eight forbid writing any session as an authority or using `accepts`, `approves`, or `settles`. Moreover, `B1926/FINDINGS.md` lines `56` and `118` state that whether orientation-twisted classes count as matter is an open stated choice (`not proved to be the only reading`), and `HARVEST_LEDGER.md` line `1826` grades row `1773` (`W-F4`) only `RECEIVED`.

#### `R82-25` — Stronger Section Twelve labels and unverified general claims banked with `rests_on_seat: []` in `B1929`, `B1920`, and `HARVEST_LEDGER.md`, plus session names in `claim_one_line`
- **Files and lines (`86930f574`):**
  1. `frontier/B1929_the_records_odd_l_value_is_the_twisted_eta_invariant_of_the_closed_torus_bundle/FINDINGS.md`, line `43` (and line `3`): `"- **Main's independent check of Bohn's side** is the end-to-end comparison through the seat's transcription. agy-exp's"`
  2. `docs/HARVEST_LEDGER.md`, line `1841` (row `1788`): `"through the transformation law of Siegel functions. Main's own check of the proof is owed | P-842, P-846 | 2026-11-14 |"`
  3. `frontier/B1920_the_channel_norms_line_part_averaged_along_the_thread_is_the_shifted_partial_zetas_kronecker_limit/arc_verdict.json`, line `25` (with line `12`): `"(shifted Hecke at s = 2 on main's code to 1.8e-6; the golden average 8.9068 reproduced); at the apex the line part differs from its average on all 1,476 closed entries."`
  4. `docs/HARVEST_LEDGER.md`, line `1830` (row `1777`): `"**VERIFIED, read through the mask**: SM-C6 E1, E2, E5 and E6, the M22 answer on W31, and the closed-join duality all reproduced"`
  5. `frontier/B1929_the_records_odd_l_value_is_the_twisted_eta_invariant_of_the_closed_torus_bundle/arc_verdict.json`, line `27` (and `B1917`, `B1918`, `B1919`, `B1920` `claim_one_line` / `# B19xx` titles): `"(found post hoc by the SM seat, proved by agy-exp through the Siegel functions' transformation law)"`
- **What is wrong:**
  1. In `B1929`, `end_to_end.py` imports `verification/received_sm/run_c9.py` unchanged (`FINDINGS.md` line `44`: `Main did not transcribe Bohn itself`), which under Section Twelve is `reproduced`, NOT a third independent computation or an independent check of Bohn's side; and `B1929` is banked as proved with `reach: general` and `rests_on_seat: []` while `HARVEST_LEDGER.md` row `1788` (line `1841`) explicitly records `Main's own check of the proof is owed` (dropped from `P-846`'s final bracket on `POINT_REGISTER.md` line `1057`).
  2. In `B1920`, `reproduced` is misused for an independent script (`golden_average.py`), while `at the apex the line part differs from its average on all 1,476 closed entries` was never computed on `main` despite `rests_on_seat: []`.
  3. Twelve non-`agy-002` rows in `HARVEST_LEDGER.md` (`1742, 1743, 1747, 1756, 1757, 1758, 1760, 1762, 1765, 1776, 1777, 1788`) carry `VERIFIED` without `main`'s own code or a banked `main` arc (row `1777` retroactively marks six `SM` rows `VERIFIED` via another seat's masked read with zero `main` code).
  4. `B1917`, `B1918`, `B1919`, `B1920`, and `B1929` name sessions (`the SM seat`, `agy-exp`, `main`) inside `claim_one_line` and arc titles (`TERMINOLOGY.md` lines `1113–1115`, `docs/seats/README.md` line `181`).

---

### E. Corrections That Did Not Travel, Unregistered Owed Leads, and Gate / Ledger Gaps

#### `R82-26` — `B1928/FINDINGS.md` states `PROOF_DRAFT.md` was corrected for `X-NEG`'s `L^2` density, but `PROOF_DRAFT.md` still says `mu` is singular
- **Files and lines (`86930f574`):**
  1. `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/FINDINGS.md`, line `61`: `"surface has an L² density, which agy-exp proved unconditionally (harvest row 1776). The draft is corrected."`
  2. `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/verification/PROOF_DRAFT.md`, line `59` (and lines `40–41`): `"values coincide. That set must be μ-null; μ is singular, so this is not automatic."`
- **What is wrong:** `PROOF_DRAFT.md` was never updated: lines `40–41` and `59` still state verbatim that `mu` is singular with respect to Liouville, with zero mention of row `1776` or the `L^2` projection density (and `PROOF_DRAFT.md` line `14`, `fiber_grid.py` line `4`, and `fiber_ergodic.py` lines `8` and `109` reference non-existent `audit/canonical_end/...` and `DRAFT.md`).

#### `R82-27` — Unpropagated corrections and window-currency omissions across `B1924`, `B1925`/`P-831`/`CAMPAIGN_STATUS.md`, `B1926`, `README.md`, `OPEN_LEADS.md`, `CHANGELOG.md`, and `POINT_REGISTER.md`
- **Files and lines (`86930f574`):**
  1. `frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/arc_verdict.json`, line `27`: `"20 to 60 words per n, n = 8 to 22; the trapezoid rule over one period, ratios averaged;"` (`main`'s own `2026-11-14` addendum extended `B1924` to `n = 28` and `120` pooled words at `n = 22`, and `thread_average.py` line `21` still calls `1.3, 0.9` `B1724's two ends` after `B1924`'s same-day correction withdrew that attribution).
  2. `docs/POINT_REGISTER.md`, line `1042` (`P-831`, and `docs/CAMPAIGN_STATUS.md` line `11`, `B1925/FINDINGS.md` lines `22–34, 53, 74`): `"every selection rule on record picks the golden; the tick's structure does not (odd metallic acts with a prime level keep it);"` (retains the refuted `with a prime level` qualifier corrected on `2026-11-14`).
  3. `frontier/B1926_at_odd_ticks_the_frames_matter_exists_only_twisted_by_the_orientation_the_tick_inverts_the_scar/FINDINGS.md`, line `64`: `"1 and the SM seat's SM-C10, both pending."` (`post hoc 1` and `SM-C10` are already delivered and cited in Sections One and Four of the same page, while `cites_seat` in `arc_verdict.json` omits `SM-C10` and `W-F4`).
  4. `README.md`, line `27`: `"| the last landing | S306p A NEGATIVE WITHOUT A SECOND COMPUTATION IS PROVISIONAL, HELD BY A GATE (the builder's card C19; P-842 DONE) (2026-11-13) |"` (`CHANGELOG.md` and `PROGRESS_LOG.md` also omit all `2026-11-14` landings).
  5. `docs/OPEN_LEADS.md`, line `4566`: `"## Currency — 2026-11-14 (B1917 to B1928, for Review 82 to read)"` (`OPEN_LEADS.md` omits `B1929`; `POINT_REGISTER.md` stops at `P-847` with `P-848` absent at `86930f574`, and leaves `P-310`, `P-319`, `P-334` awaiting `card C20` after `C20` already landed).

#### `R82-28` — Four explicitly promised leads missing from `POINT_REGISTER.md`, all fifty new harvest rows (`1742..1791`) missing `@ <commit>` pins, and `negative-second-computation` gate bypasses
- **Files and lines (`86930f574`):**
  1. `frontier/B1925_the_selection_tested_by_changing_it_the_metallic_rivals_bronze_keeps_the_tick_structure_only_nothing_left_over_picks_golden/FINDINGS.md`, line `77`: `"- **Clue, entered as a lead and not used:** the record's three quaternion groups nest."`
  2. `frontier/B1923_the_load_bearing_negatives_reexamined_and_the_twin_chooses_the_icosahedral_triplet/FINDINGS.md`, line `52` (with lines `68`, `78`, `82`): `"## 2. What the walls teach (main's contemplations; each clue a lead in the register)"`
  3. `docs/HARVEST_LEDGER.md`, line `1799` (representative of all fifty rows `1742..1791`, lines `1795–1844`): `"| 1746 | SM-derivation seat | ITS CARD SM-C7, STEPS 0 TO 4: the slope and the channel norm as coefficients of one L-function along the thread's geodesic"`
  4. `WORKING_RULES.md`, line `377`: `"   `audit/negatives/2026-11-13/` until it lands as an arc."`
  5. `tests/test_negative_second_computation.py`, line `60` (testing `scripts/gates/gates.py` lines `3136–3163`): `"### 7. What the wall teaches: the assumption it rests on"`
- **What is wrong:**
  1. **Four unregistered leads:** Neither `B1925`'s quaternion-nesting clue (`Q_8 subset 2T subset 2I`, line `77`) nor three of `B1923` Section Two's explicit clues/leads (Selberg's bound for `Gamma_0(5)` on line `68`, `B1838` thread-averaged exact end on line `78`, `B1855` failure-set structure on line `82`) appears anywhere in `docs/POINT_REGISTER.md` or `docs/OPEN_LEADS.md` (violating Clause Five of the `2026-11-13` rule).
  2. **Unpinned harvest rows:** All fifty rows `1742..1791` in `docs/HARVEST_LEDGER.md` omit `@ <commit>` in Column Five (`path @ pin`) while the top `## Pins` table (`lines 19, 30, 37, 39, 40`) remains frozen at `2026-11-12` (row `1741`).
  3. **Rule-to-gate enforcement gaps:** `WORKING_RULES.md` line `377` points to non-existent `audit/negatives/2026-11-13/` (landed at `B1923/verification/LOAD_BEARING_NEGATIVES.md`). In `scripts/gates/gates.py` lines `3150–3162`, `negative_without_second` filters strictly on exact uppercase `NEGATIVE` (`0` live arcs `>= B1923` match; `NO SUPPORT`, `OPEN`, and seat negatives in `HARVEST_LEDGER.md` are skipped), accepts negated or same-code strings such as `no second computation` or `second computation on the same code` in `cites_seat`, and accepts an empty bodyless `What the wall teaches` heading at EOF (`test_negative_second_computation.py` line `60`).

---

## 2. Arc-by-Arc Accounting (`B1917` to `B1929`, Rules/Gate, Register, Harvests)

- **`B1917` (11 files read in full):** `hecke_value` (`601` characters across sixteen levels, `< 2.5e-13`) and `kronecker_s1` Siegel integrals verified clean against `e47c5ee9f` and `ae5f6d7d1`. Findings: `R82-02`, `R82-11`, `R82-25`.
- **`B1918` (9 files read in full, retracted):** `step3_norm` three-point table verified; retraction header present. Findings: `R82-22`, `R82-25`.
- **`B1919` (6 files read in full):** Shifted Kronecker identity `N(c, tau) = F_u(tau) + pi log Im tau - 2 pi (gamma + log pi)` verified to `4.9e-7` on all twenty-four rows (`verify_r82_checks.py` check ten). Findings: `R82-12`, `R82-19`, `R82-25`.
- **`B1920` (10 files read in full):** `hecke_shifted_s2` (`s = 2` to `1.8e-6`) and `golden_average` (`8.9068`) verified clean against `d687a9180`. Findings: `R82-19`, `R82-25`.
- **`B1921` (7 files read in full):** Exact analytical derivation of `N(c', -1/tau) = N(c, tau) - 2 pi log|tau|`, all nine rows of `s_shift.json` (`1.9e-9`), and `test_b1921_the_s_shift.py` verified clean. *(Minor note: `0.33 to 1.27` on `FINDINGS.md` line `16` states `|n_S - n|` for signed `-1.274` to `+0.331`.)*
- **`B1922` (6 files read in full):** Golden-thread transport algebra and `periodic.json` three-window numbers verified. Findings: `R82-05`, `R82-20`. *(Minor note: `periodic.py` line `18` labels `LS0` as `L~` when `C.frame` treats it as `L(tau)`.)*
- **`B1923` (6 files read in full; own-work lines excluded per Section Zero):** `SL(2, F_5)` Weil representation on `C^5`, eigenvalue exponents `{0, 2, 3}` vs `{0, 1, 4}`, and `test_b1923_the_twin_and_the_triplet.py` verified clean. Findings: `R82-09`, `R82-23`, `R82-28`.
- **`B1924` (30 files read in full; own-work lines `167–195` excluded per Section Zero):** Closed-form channel norm (`1.95e-12`), quadrature and jackknife tables (`whole_average*.json`), and `B1667` fifty-four-point dataset checked directly. Findings: `R82-10`, `R82-27` (plus neutral boundary handoff in Section Zero).
- **`B1925` (8 files read in full):** Smith forms, metallic rivals `m = 1..14`, SnapPy manifold names and volumes (`m004, m000`, `m136, m001`, `s464, m005`, `t03910, m014`, `o10_029743, m024`), `360` hyperbolic matrices in `[-7, 7]`, and `m = 9, 11, 13` square roots recomputed independently. Findings: `R82-03`, `R82-15`, `R82-17`, `R82-18`, `R82-27`, `R82-28`.
- **`B1926` (9 files read in full):** Group-cohomology proof (`(l(mu) + 1) c(lambda) = 0` at odd `n`), Fox-calculus runs over `F_19141` (`n = 1..8`), double-cover pullback (`n = 3, 5, 7`), `test_b1926_odd_ticks.py`, and pinned `chat1`/`SM` outputs verified. Findings: `R82-23`, `R82-24`, `R82-27`.
- **`B1927` (23 files read in full):** `grid.py` (`53` points, mirror `2.9e-13`, S-covariance `4.0e-12`), `canon_readout.json`, `canon_compare_run.txt`, `positivity.py` (`22 767` nodes, zero cuts), `arc_corner.json`, and `test_b1927_canonical_end.py` verified. Findings: `R82-04`, `R82-07`, `R82-13`, `R82-23`.
- **`B1928` (15 files read in full):** `SL(2, F_5)` perfection and transitivity on the twenty-four order-five points, `fiber_grid_fine.json` (`1 046` points), `fiber_ergodic_fine.json` (`P2`/`P3` tables), `h1_check`, `h2_h3_check`, `PROOF_DRAFT.md`, and `test_b1928_one_average.py` checked. Findings: `R82-08`, `R82-16`, `R82-21`, `R82-26`.
- **`B1929` (12 files read in full):** `601`-character Siegel windings (`max |Re Delta| = 2.6e-14`, `561` nonzero ratio `-2.0000000000`, `40` zero-winding characters verified identically zero on rational `eta_A`, end-to-end difference `3.14e-14`), negative-trace/asymmetric controls, and `test_b1929_twisted_eta.py` checked. Findings: `R82-01`, `R82-25`.
- **Rules, gate, register `P-839..P-848`, and cited harvest rows:** Audited `WORKING_RULES.md` (`2026-11-13`), `scripts/gates/gates.py` (`negative-second-computation`), `tests/test_negative_second_computation.py`, `tests/test_c20_record_keeping.py` (`65` P9 lines verified), `tests/test_b1461_governance_delta.py`, `docs/POINT_REGISTER.md`, and `docs/HARVEST_LEDGER.md` (own-work rows excluded per Section Zero). Findings: `R82-06`, `R82-14`, `R82-24`, `R82-25`, `R82-27`, `R82-28`.

### What Could Not Be Checked In-Session
1. **Unpinned seat relays in `HARVEST_LEDGER.md` rows `1742..1791` not cited by commit hash inside an arc** (e.g. row `1743` `W-C6 part 2`, row `1776` `X-NEG`, row `1788` `X-C9`): because those harvest rows omit `@ <commit>` pins and `## Pins` stops at `2026-11-12`, unpinned seat branches were not browsed (`M28` cold-read boundary).
2. **External copy of M. Bohn's `2009` Bonn dissertation equation `(4.67)`:** `received_sm/run_c9.py` was audited algebraically and checked against `main_siegel.py` to `3.1e-14` across all `601` characters, without an external copy of Bohn's printed thesis in the repository.
3. **Full from-scratch forty-minute re-execution of `B1927/canon_readout.py` and `B1928/fiber_grid.py --fine`:** stored JSONs and lock spot-recomputations were verified in `A2-R82`, and `agy-002`'s independent from-scratch canonical-end computation follows immediately in card `A2-CANON`.

0 of 19.
