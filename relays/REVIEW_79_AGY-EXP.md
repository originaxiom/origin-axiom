# REVIEW 79 READING — `AGY-EXP` (`X-R79` AT `0dda7b472`)

- **Address:** `agy-exp` (branch `origin/agy/self-consistent-loop-2026-11-11`)
- **Card:** `X-R79` (`relays/cards/AGY-EXP_X-R79_review-79-reading.md`)
- **Date:** `2026-11-11`
- **Pinned `main` commit read:** `0dda7b472` (`0dda7b4725f613dbef273edafcd3fca73ccb245c`), with Review-79 window diff base `38d2a36dc` (`git diff 38d2a36dc 0dda7b472 -- PATH`)
- **Committed check script and raw output:** `relays/x_r79_verify/verify_x_r79.py` (sealed before first run at `723f436b1`, pre-output adjustments recorded through `291550fa2`) and `relays/x_r79_verify/verify_x_r79_out.json` (committed before reading at `c4e1b24a6`, digest in `relays/x_r79_verify/OUTPUT_SHA256.txt`)
- **Environment and isolation:** read directly from the local git object store on a clean checkout with no review-gate override environment variables set; zero Review-79 files or branches of any other session were opened prior to pushing this file.
- **Firewall:** pure mathematics and governance/audit checks only (`0 of 19`); zero measured values opened or compared; zero judgment rendered on `agy-exp`'s own work.

---

## Section 1 — Explicit Answers on the Two Assigned Corrections and Their Locks (`M4`)

### 1 — `B1221` (frontier/B1221_global_form_path_independence/FINDINGS.md and tests/test_b1221_the_adjoint_control.py)

- **Is the `2026-11-11` mathematical note right?** **Yes** (`recomputed independently` in `relays/x_r79_verify/verify_x_r79.py`). Every component of adjoint-only content carries `(t, s, y) = (0, 0, 0)`, so every element of the product of the cyclic three-group, the cyclic two-group, and the full circle acts trivially on it: its kernel is infinite, and `72` is six times twelve from sampling the circle at `12` rational grid points (`144` at `24`, `360` at `60`, `720` at `120`), whereas the twenty-seven, the sixteen, and the ten each have exact finite kernel order `6` and the integer-charge control has exact finite kernel order `18`. Two governance/propagation faults remain on the arc: the correction was not carried to `B1221`'s claim line (`F-01`), and the post-`7b89eda8a` correction heading names a session inside a statement of the mathematics (`F-02`).
- **Can tests/test_b1221_the_adjoint_control.py fail?** **Yes** (`tested against planted errors, with the count`: `3` of `3` planted mutations caught in `relays/x_r79_verify/verify_x_r79.py`). Freezing the adjoint return count at `72` across grid sizes `12, 24, 60`, perturbing the twenty-seven's kernel order away from `6`, or removing the correction text from `FINDINGS.md` each causes the lock to fail.

### 2 — `B1641` (frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md and the last test of tests/test_b1641_w46_on_main_and_the_two_objects.py)

- **Is the `2026-11-11` mathematical note right?** **The Riemann–Roch index part is right, and one formula in the evening block is wrong (`F-03`).** Because the three-dimensional piece has three distinct cusp exponents `(1/8, 3/8, 7/8)`, twisting the three canonical cusp lines by integer orders `m = (m_1, m_2, m_3)` shifts the weight-three-halves Riemann–Roch index from `0` to `m_1 + m_2 + m_3` (`1` at `(1, 0, 0)` and `3` at the uniform triple `(1, 1, 1)`, `recomputed independently`). However, the evening addition on `FINDINGS.md` writes `with m = (m_P, m_M, m_N) units of end data on the three lines the space has dimension m_P + m_M + m_N`, omitting `max(0, ...)` — which makes the stated dimension negative on `10` of the `64` triples in `{-1, 0, 1, 2}^3` (for example `-1` instead of `0` at `(-1, 0, 0)`) — and omitting `"on every vector computed"`, thereby stating an unproved mixed positive-sum dimension formula as unconditional where `GENESIS.md` (`FK10`) and `B1796` proved only non-positive sums and uniform triples `(n, n, n)`. In addition, the uniform-unit caveat did not travel to `B1641`'s claim line (`F-04`), and the post-`7b89eda8a` note names a session (`F-05`).
- **Can the last test (`test_one_unit_means_the_same_unit_on_three_lines_and_a_unit_on_one_line_gives_one`) fail?** **Overall yes as a file-pinning check, with three internal sub-assertions that do not test their stated rule (`F-06`).** Perturbing `w50_on_main.json`, `w123_check_run.txt`, `FINDINGS.md`, or `GENESIS.md` causes the function to fail, **but** inside that function: (i) `len({1, 3, 7}) == 3` evaluates `len` on a literal Python set and **cannot fail**; (ii) `classical.get(k + 12, dim + 1)` falls back to the default `dim + 1` on `6` of the `8` even weights (`6, 8, 10, 12, 14, 16`), reducing the check to an algebraic identity of the local helper; and (iii) `index` adds `+ sum(m)` directly rather than evaluating the vector-valued Riemann–Roch formula on shifted cusp exponents.

---

## Section 2 — Findings (`15` Total, Machine-Verified Against `0dda7b472`)

### Finding `F-01` — Criterion `5` (correction that did not travel)
- **Arc:** `B1221`
- **File:** frontier/B1221_global_form_path_independence/arc_verdict.json
- **Exact quotation at `0dda7b472`:**
```text
MB12 CONTROLS PASS: adjoint-only content gives 72, integer-charge-only content gives 18, so Z6 is a DISCRIMINATING outcome and not the only thing the instrument can say.
```
- **What is wrong:** `B1221`'s `FINDINGS.md` was corrected on `2026-11-11` to explain that `72` is the twelve-point circle-grid sample of an infinite kernel (`6 * N` at grid size `N`), not a finite kernel order, yet `B1221`'s `claim_one_line` in frontier/B1221_global_form_path_independence/arc_verdict.json still states `adjoint-only content gives 72` unqualified.
- **How we know:** `recomputed independently` (`relays/x_r79_verify/verify_x_r79.py` confirms infinite kernel on adjoint content with grid counts `72, 144, 360, 720` at `N = 12, 24, 60, 120`) and inspected `git diff 38d2a36dc 0dda7b472 -- frontier/B1221_global_form_path_independence/arc_verdict.json` (unchanged).

### Finding `F-02` — Criterion `8` (session credited in a statement of mathematics after `P-797`)
- **Arc:** `B1221`
- **File:** frontier/B1221_global_form_path_independence/FINDINGS.md
- **Exact quotation at `0dda7b472`:**
```text
> **CORRECTED 2026-11-11 (found by a second derivation on another family of model, agy-002's card A2-C1; checked by
```
- **What is wrong:** Committed at `57f604898`, *after* `7b89eda8a` established the `2026-11-11` session-naming rule (`P-797`, `README.md` section `12`: `"In a summary line or a statement of the mathematics, no session is named"` and `"No session is credited in a statement of the mathematics"`).
- **How we know:** Checked commit ancestry `7b89eda8a..0dda7b472` (`57f604898`) and matched verbatim against `0dda7b472` in `relays/x_r79_verify/verify_x_r79.py`.

### Finding `F-03` — Criteria `2` and `3` (formula omits `max(0, ...)` and states an unproved mixed-triple law unconditionally)
- **Arc:** `B1641`
- **File:** frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md
- **Exact quotation at `0dda7b472`:**
```text
> with m = (m_P, m_M, m_N) units of end data on the three lines the space has dimension m_P + m_M + m_N; the least
```
- **What is wrong:** `GENESIS.md` (`FK10`) and `B1796`'s `w123_check_run.txt` state `dimension max(0, m_P + m_M + m_N)` *on every vector computed* (`64` triples in `{-1, 0, 1, 2}^3`, proved only for non-positive sum and uniform `(n, n, n)`). Omitting `max(0, ...)` gives negative dimensions on `10` of the `64` tested triples (such as `-1` instead of `0` at `m = (-1, 0, 0)`), and omitting `"on every vector computed"` states the unproved general mixed positive-sum dimension formula as unconditional.
- **How we know:** `recomputed independently` across `{-1, 0, 1, 2}^3` in `relays/x_r79_verify/verify_x_r79.py` and compared against `0dda7b472:GENESIS.md` (`FK10`) and `0dda7b472:frontier/B1796_two_debts_from_the_audit_closed/verification/w123_check_run.txt`.

### Finding `F-04` — Criterion `5` (correction that did not travel)
- **Arc:** `B1641`
- **File:** frontier/B1641_w46_on_main_and_the_two_objects/arc_verdict.json
- **Exact quotation at `0dda7b472`:**
```text
the SM seat's W46 verified on main's lifts (L6's exponents (1,1,3,5,7,7)/8, pieces 2 + 4, every chi_1 = 0, chi_3/2(rho_T) = 0, the table n(|Lambda+| - 3))
```
- **What is wrong:** `B1641`'s `FINDINGS.md` was amended on `2026-11-11` to record that `"What lagged was this arc, which wrote one integer"` (`n` in `n(|Lambda+| - 3)` is only the uniform triple `(n, n, n)` on the three canonical lines, whereas `(1, 0, 0)` gives index `1`), but `B1641`'s `claim_one_line` in frontier/B1641_w46_on_main_and_the_two_objects/arc_verdict.json still states the single-integer table `n(|Lambda+| - 3)` with no note of the three-line vector or the uniform-unit condition.
- **How we know:** Checked `git diff 38d2a36dc 0dda7b472 -- frontier/B1641_w46_on_main_and_the_two_objects/arc_verdict.json` (unchanged) and verified verbatim in `relays/x_r79_verify/verify_x_r79.py`.

### Finding `F-05` — Criterion `8` (session credited in a statement of mathematics after `P-797`)
- **Arc:** `B1641`
- **File:** frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md
- **Exact quotation at `0dda7b472`:**
```text
*Raised by a second derivation of the chiral three from its statement alone, on another family of model (agy-002's
```
- **What is wrong:** Added at `57f604898` (after `7b89eda8a`), naming a session (`agy-002`) inside a mathematical correction note on `FINDINGS.md` contrary to `README.md` section `12` (`"No session is credited in a statement of the mathematics"`).
- **How we know:** Checked commit ancestry `7b89eda8a..0dda7b472` (`57f604898`, `f8b5e6769`) and verified verbatim in `relays/x_r79_verify/verify_x_r79.py`.

### Finding `F-06` — Criterion `4` (sub-assertion that cannot fail, and fallback tautology in lock)
- **Arc:** `B1641`
- **File:** tests/test_b1641_w46_on_main_and_the_two_objects.py
- **Exact quotation at `0dda7b472`:**
```text
assert "T's exponents (⅛, ⅜, ⅞)" in b1634 and len({1, 3, 7}) == 3   # three distinct exponents: three canonical lines
```
- **What is wrong:** `len({1, 3, 7}) == 3` calls `len` on a hardcoded literal set `{1, 3, 7}` and **cannot fail** instead of computing the three distinct cusp exponents from the representation matrices; in the same function, `classical.get(k + 12, dim + 1)` defaults to `dim + 1` on `6` of the `8` tested weights (`6, 8, 10, 12, 14, 16`), and `index` adds `+ sum(m)` directly rather than evaluating the vector-valued Riemann–Roch formula on shifted cusp exponents.
- **How we know:** AST constant-expression analysis and weight-key check in `relays/x_r79_verify/verify_x_r79.py` (`tested against planted errors`).

### Finding `F-07` — Criterion `4` (two `check(..., True, ...)` calls counted in `"65 checks, none failing"` cannot fail)
- **Arc:** `B1881`
- **File:** frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py
- **Exact quotation at `0dda7b472`:**
```text
check("E3 (Q5) the mirror normalises the group: [[a,b],[5c,d]] -> [[a,-b],[-5c,d]]", True, "an identity of matrices")
```
- **What is wrong:** Two of the `65` boolean checks counted in `B1881`'s `FINDINGS.md` (`65 checks, none failing`), `arc_verdict.json`, and `test_b1881_the_whole_and_the_value_verified.py` (`assert len(checks) == 65 and all(checks.values())`) pass the literal boolean `True` as their condition argument — line `230` (quoted above) and line `591` (`check("the own values of the allowed single runs increase without bound: 5m/2 + sqrt5/2 for the run of 5m + 1", True, ...)`). Neither check can fail.
- **How we know:** AST scan of `whole_and_value_on_main.py` in `relays/x_r79_verify/verify_x_r79.py` (which also verified both mathematical statements independently by symbolic matrix conjugation and exact formula).

### Finding `F-08` — Criterion `4` (genus assertion in lock evaluates hardcoded `Fraction` literals and cannot fail)
- **Arc:** `B1881`
- **File:** frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py
- **Exact quotation at `0dda7b472`:**
```text
assert Fr(1) + Fr(12, 12) - 0 - 0 - Fr(4, 2) == 0 and Fr(1) + Fr(6, 12) - Fr(2, 4) - 0 - Fr(2, 2) == 0     # both of genus 0
```
- **What is wrong:** In `test_the_two_quotients_recomputed`, the genus-zero check performs arithmetic solely on hardcoded `Fraction` and integer literals (`1 + 12/12 - 4/2 == 0` and `1 + 6/12 - 2/4 - 2/2 == 0`): it **cannot fail**, because neither the cusp count nor the elliptic fixed-point counts are computed from the two mod-`5` subgroup coset actions constructed earlier in that test.
- **How we know:** AST literal-expression detector in `relays/x_r79_verify/verify_x_r79.py`, alongside an independent coset-action computation of index, cusp widths (`[1, 1, 5, 5]` and `[1, 5]`), elliptic counts (`(0, 0)` and `(2, 0)`), and genus `0`.

### Finding `F-09` — Criteria `1` and `4` (second discriminant-`-20` point `w2` is constructed and never evaluated, yet reported as checked)
- **Arc:** `B1885`
- **File:** frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main.py
- **Exact quotation at `0dda7b472`:**
```text
check("so f vanishes at i/sqrt5 if s = -1; and it vanishes at 1/2 + i/(2 sqrt5), which lies on x = 1/2", abs(f(w1)) ** 2 / top
```
- **What is wrong:** Line `230` defines `w2` as the second discriminant-`-20` point (`1/2 + i/(2 sqrt 5)`), and the check's own label, `FINDINGS.md`, and `arc_verdict.json` (`vanishes at both elliptic points, at both points of discriminant -20`) report both points as checked, **but `w2` is never passed to `f(...)` or read anywhere in the script** (`Name('w2', Store) = 1`, `Name('w2', Load) = 0`), and `golden_state_on_main.json` records no evaluation at `w2`. In addition, the ternary fallback `... if s1 < 0 else True` passes `True` if `s1 >= 0`.
- **How we know:** Python AST symbol-load audit and `recomputed independently` evaluation of the Maass wave form at both `w1` and `w2` in `relays/x_r79_verify/verify_x_r79.py` (confirming mathematically that `f(w2)` does vanish, while the arc's script omitted the call).

### Finding `F-10` — Criterion `4` (vacuous `all([])` check at level `17`, hidden zero count, and two non-failing literal `Fraction` assertions in lock)
- **Arc:** `B1885`
- **File:** frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main.py
- **Exact quotation at `0dda7b472`:**
```text
check("level %d: f vanishes at every elliptic point where the character forces it" % p, all(r[3] < mp.mpf(10) ** -15 for r in forced), len(forced))
```
- **What is wrong:** At level `p = 17`, `(-1 / 17) = +1` on the two order-`2` elliptic points and there are zero order-`3` elliptic points, so `forced` is empty (`len(forced) == 0`): `all(... for r in forced)` evaluates `all([]) == True` vacuously (counted among the `32` checks), and `check(..., detail=len(forced))` tests `if detail:` so integer `0` is treated as falsy and omitted from `golden_state_on_main_run.txt` (`[ok] level 17: f vanishes at every elliptic point where the character forces it`). In addition, `test_b1885_the_golden_state_on_the_whole_verified.py` lines `76` and `77` (`assert Fraction(1, 5) + Fraction(1, 20) == Fraction(1, 2) ** 2` and the following `Fraction` equality) assert pure arithmetic on hardcoded literals and **cannot fail**.
- **How we know:** `recomputed independently` Legendre obstructions on elliptic points at `p = 5, 13, 17`, checked `golden_state_on_main_run.txt`, and ran AST literal-assertion scan on `test_b1885` in `relays/x_r79_verify/verify_x_r79.py`.

### Finding `F-11` — Criterion `2` (number `50` in `FINDINGS.md` and `arc_verdict.json` differs from the arc's own output `51`)
- **Arc:** `B1888`
- **File:** frontier/B1888_the_public_form_scrutinised/FINDINGS.md
- **Exact quotation at `0dda7b472`:**
```text
which opens the one file of measured masses. One Python file of the chain names that file. In the whole tree 50 do.
```
- **What is wrong:** `B1888`'s `FINDINGS.md` (lines `50` and `62`: `in the archive 50 scripts name the file`) and `arc_verdict.json` (`the one file of measured masses that 50 scripts of the whole tree name`) state **`50`**, whereas `B1888`'s own committed outputs `verification/candidate_chain.json` (`"namers_in_tree": 51`) and `verification/candidate_chain_run.txt` (`in the whole tree: 51`) record **`51`** (`test_b1888` only asserted `>= 40`).
- **How we know:** Compared against `0dda7b472:frontier/B1888_the_public_form_scrutinised/verification/candidate_chain.json` and `recomputed independently` across all tracked Python scripts at `0dda7b472` (`51` scripts) in `relays/x_r79_verify/verify_x_r79.py` without opening any measured data file.

### Finding `F-12` — Criterion `1` (`"14 pass"` on `main`'s head is not supported by the arc's committed outputs)
- **Arc:** `B1890`
- **File:** frontier/B1890_the_first_enforcement_series_verified_and_landed/FINDINGS.md
- **Exact quotation at `0dda7b472`:**
```text
| the series' own lock on main's head | 14 pass |
```
- **What is wrong:** `B1890`'s `FINDINGS.md` (line `50`) and `arc_verdict.json` (`the series' lock passes (14);`) report `14` passing tests for tests/test_gates_are_a_function_of_the_commit.py on `main`'s head, **but neither `verification/other_checks_run.txt` nor `verification/unseen_cases_run.json` contains any post-landing run of that test file** (`other_checks_run.txt` records only the four pre-patch runs ending at `2 failed, 12 passed`, then the `47`-file run `2 failed, 366 passed, 5 skipped`, then the `2`-file rerun `8 passed`; `test_b1890` asserts `53 passed` and `8 passed` in `other_checks_run.txt` and never asserts `14 passed`).
- **How we know:** Inspected `other_checks_run.txt`, `unseen_cases_run.json`, and `test_b1890` at `0dda7b472` in `relays/x_r79_verify/verify_x_r79.py`.

### Finding `F-13` — Criterion `1` (`## Reproduce` omits the fourth stage `clock` and does not assemble `unseen_cases_run.json`)
- **Arc:** `B1890`
- **File:** frontier/B1890_the_first_enforcement_series_verified_and_landed/FINDINGS.md
- **Exact quotation at `0dda7b472`:**
```text
python3 -B run_unseen.py dates
```
- **What is wrong:** `B1890`'s `## Reproduce` block lists only `export`, `shallow`, and `dates`, omitting `python3 -B run_unseen.py clock` — yet `verification/unseen_cases_run.json` contains four top-level stages (`clock`, `dates`, `export`, `shallow`), and `clock` is the stage where the `time.strftime` stub took effect (`dates` recorded `'2027-12-16 2027-12-16 2026-11-11'` whereas `clock` recorded `'2027-12-16 2027-12-16 2027-12-16'`). Moreover, `run_unseen.py` writes per-stage files `"unseen_%s.json" % stage` into a scratch directory and never writes `verification/unseen_cases_run.json`. (Note: `test_b1890` line `26` also pins `len(g.READS_TRACKED) == 6 and len(g.READS_HISTORY) == 14`, which register row `P-808` item `(8)` already carries.)
- **How we know:** Checked `FINDINGS.md`, `run_unseen.py`, and `unseen_cases_run.json` at `0dda7b472` in `relays/x_r79_verify/verify_x_r79.py`.

### Finding `F-14` — Criterion `5` (`2026-11-11` window correction in `B874/FINDINGS.md` did not travel to `B874/arc_verdict.json`)
- **Arc:** `B874`
- **File:** frontier/B874_measurement_ladder/arc_verdict.json
- **Exact quotation at `0dda7b472`:**
```text
adding x14 or x22 collapses 46 -> 12 directly -- NO 26 stratum exists; the step-2 question closes NEGATIVELY: the complete ladder is {78, 46, 30, 12}
```
- **What is wrong:** In the Review-79 window, `B874/FINDINGS.md` received a `2026-11-11` dated note on the `14`-dimensional wall mechanism (`B892` found complex lines in `(x14, x22)` with centraliser dimensions `18` and `14`, so `{78, 46, 30, 12}` holds over real pairs rather than over complex combinations), while `B874`'s `claim_one_line` in frontier/B874_measurement_ladder/arc_verdict.json remained unchanged and still states unqualified `the complete ladder is {78, 46, 30, 12}`.
- **How we know:** Checked `git diff 38d2a36dc 0dda7b472 -- frontier/B874_measurement_ladder` (`arc_verdict.json` untouched) in `relays/x_r79_verify/verify_x_r79.py`.

### Finding `F-15` — Criteria `2` and `5` (`PROGRAMME.md` table truncates the `2026-11-11` `W:INDEX3` uniform-unit caveat mid-word)
- **Arc:** `B1861`
- **File:** frontier/B1861_the_closure_programme/PROGRAMME.md
- **Exact quotation at `0dda7b472`:**
```text
| W:INDEX3 | Given Λ and the uniform unit, the chiral three is a four-dimensional index (±3) on the weave's own surface; th |
```
- **What is wrong:** When `B1861` regenerated `PROGRAMME.md` in the window to carry `B1641`'s uniform-unit caveat onto `W:INDEX3`, the table builder's fixed character-width slice truncated the sentence mid-word at `; th`, dropping the caveat clause (`the three lines carry a vector...`) from the rendered Markdown table in section `6`.
- **How we know:** Checked `git diff 38d2a36dc 0dda7b472 -- frontier/B1861_the_closure_programme/PROGRAMME.md` and verified verbatim in `relays/x_r79_verify/verify_x_r79.py`.

---

## Section 3 — Arc-by-Arc Coverage and Unchecked Boundaries (`5` Full Arcs + `15` Window-Changed Arcs)

### Five Full Review-79 Arcs (`M4`)
- **`B1879` (frontier/B1879_the_weaves_theorems_with_the_exchange):** Read `FINDINGS.md`, `arc_verdict.json`, `weave_with_the_exchange.py`, `weave_with_the_exchange_run.txt`, and `test_b1879_the_weaves_theorems_with_the_exchange.py` in full; `recomputed independently` in `verify_x_r79.py` the Groebner fixed characters `(0, 0, 0)` and `(2, 2, 2)` of `(M1, M2)` and of the single tick `F`, the six-dimensional Fox cohomology representation (`96` to `192`, commutant dimensions `2` and `1`, plain Frobenius–Schur indicators `-1` and `+1` on the two lifts, twisted Frobenius–Schur indicator `+1` on the triplet, all verified invariant under a random six-by-six Haar unitary basis rotation), the `165` run-law triples in `12` letters, the `22` non-orientable `1`-cusped punctured-torus bundles up to `7` letters (`snappy`), and the upper-half-plane reflection loci. Nothing wrong found (`W:INDEX3` row properly discloses that the four-dimensional index is argued rather than recomputed there).
- **`B1881` (frontier/B1881_the_whole_and_the_value_verified):** Read all arc files in full; `recomputed independently` in `verify_x_r79.py` the two mod-`5` subgroup quotients (indices `12` and `6`, cusp widths `[1, 1, 5, 5]` and `[1, 5]`, elliptic counts `(0, 0)` and `(2, 0)`, both genus `0`), symbolic mirror normalisation, golden-period fixed-point derivative, and exact agreement across all `47,988` two-convention sequences under sequence reversal. Two findings reported (`F-07`, `F-08`).
- **`B1885` (frontier/B1885_the_golden_state_on_the_whole_verified):** Read all arc files in full; `recomputed independently` in `verify_x_r79.py` the real-quadratic Maass wave form at level `5`, its automorphy under `Gamma_0(5)` with quadratic character, its vanishing at both discriminant-`-20` points `w1` and `w2`, and the Legendre elliptic obstructions at `5, 13, 17`. Two findings reported (`F-09`, `F-10`). **Unchecked and why:** spectral simplicity and rank as lowest twin-odd state are explicitly unproved in the arc and tracked on `P-783`; the comparison clause naming a branch point from `origin/agy/stage4-sync-2026-11-11` (`agy-002`) is another session's branch, not `agy-exp`'s.
- **`B1888` (frontier/B1888_the_public_form_scrutinised):** Read all arc files in full; verified `276` nodes at `ea41e6fc9`, `17` Python files / `3,032` lines / `14` arcs (`13` files / `2,252` lines / `11` arcs in the census half), and `recomputed independently` the tree-wide count of Python scripts naming the measured-mass filename (`51`, versus `50` in `FINDINGS.md` and `arc_verdict.json` — Finding `F-11`). **Unchecked and why:** `0 of 19` firewall bars opening any measured mass file (`compare.py`'s numerical comparisons left untouched); `B1888`'s `cites_seat` note mentioning `"through the lane's note read earlier through the mask"` touches `agy-exp`'s `P-781` note and is left without self-judgment per section `13` (whereas the `"seven reports"` belong to `agy-002`'s `stage4-sync` branch).
- **`B1890` (frontier/B1890_the_first_enforcement_series_verified_and_landed):** Read all arc files in full; checked `unseen_cases_run.json`, `other_checks_run.txt`, `run_unseen.py`, `test_b1890`, and verified that `P-757` carries the ninth unseen case (`a repository with no commit, is the seat's to close`) and `P-808` item `(8)` carries the pinned table sizes `6` and `14`. Two findings reported (`F-12`, `F-13`). **Unchecked and why:** running the whole suite on a fresh clone and running the advisor seat's twenty-one-case planted suite were explicitly marked not run in `B1890` (`P-810` subsequently ran the fresh-clone suite).

### Fifteen Window-Changed Arcs (`M5`, Read via `git diff 38d2a36dc 0dda7b472 -- frontier/<ARC>`)
- **`B874` (frontier/B874_measurement_ladder):** Read window diff (`2026-11-11` note on `14`-locus mechanism added to `FINDINGS.md`); reported Finding `F-14` (`arc_verdict.json` still states unqualified `{78, 46, 30, 12}`).
- **`B892` (frontier/B892_second_measurement):** Read window diff (`FINDINGS.md`, `walls_on_the_line.py`, `walls_on_the_line_run.txt`, and tests/test_b892_walls_on_the_line.py); `recomputed independently` in `verify_x_r79.py` irreducibility, positive discriminant, and `3` distinct real roots (`2` positive, `1` negative) of `u^3 - 28224 u^2 - 159667200 u + 500716339200` and weight decomposition `12 + (2 + 2 + 6 + 6 + 6 + 6 + 6) = 46`, and checked that `test_b892_walls_on_the_line.py` calls real computations and can fail. Nothing wrong found (committed at `af542158d`, prior to `7b89eda8a`).
- **`B1221` (frontier/B1221_global_form_path_independence):** Covered in Section `1` and Findings `F-01`, `F-02`.
- **`B1486` (frontier/B1486_the_two_orders_at_the_silver_members):** Read window diff (`2026-11-11` disclosure note on `FINDINGS.md` recording the post-seal lower-left cocycle sign fix caught by its own control, committed prior to `7b89eda8a` and recorded on `P-772`). Nothing wrong found in the window diff.
- **`B1494` (frontier/B1494_no_room_on_any_companion):** Read window diff (`2026-11-11` disclosure note on `FINDINGS.md` recording the one-folder import-path fix after the sealed hash list, recorded on `P-772`). Nothing wrong found in the window diff.
- **`B1499` (frontier/B1499_the_fusion_on_the_first_room):** Read window diff (`FINDINGS.md` and `arc_verdict.json` marking cells `F2` and `F3` post hoc after loosening the convergence threshold after the sealed run stalled, with unsettled regrade question explicitly carried on `P-772`). Nothing wrong found in the window diff.
- **`B1641` (frontier/B1641_w46_on_main_and_the_two_objects):** Covered in Section `1` and Findings `F-03`, `F-04`, `F-05`, `F-06`.
- **`B1675` (frontier/B1675_no_thread_keeps_a_record_verified):** Read window diff (`FINDINGS.md` correction from `718 of 758` to all `758`, `718` keeping a line and `40` keeping all three, plus tests/test_b1675_no_thread_keeps_a_record_verified.py); checked against `v2_w34_independent_run.txt` (`718 + 40 = 758`) and confirmed the lock parses the output file and can fail. Nothing wrong found.
- **`B1726` (frontier/B1726_the_two_ingredients_replicated):** Read window diff (`2026-11-11` `B1882` / `V1` note on random-target specificity null windows for the six-ratio value comparison). **Left unchecked under the `0 of 19` firewall (`M5`, section `9`):** this change concerns specificity nulls of measured-value comparisons.
- **`B1753` (frontier/B1753_the_six_on_the_five_ality_lines):** Read window diff (`2026-11-11` `B1882` / `V1` note on random-target specificity null windows for the six-ratio value comparison). **Left unchecked under the `0 of 19` firewall (`M5`, section `9`):** this change concerns specificity nulls of measured-value comparisons.
- **`B1853` (frontier/B1853_the_departures_depth_premises_verified):** Read window diff (`2026-11-11` cross-reference note to `B1881` on single-run depth `(n - 1)/2 + (sqrt 5)/2` for `n = 1 mod 5`, committed prior to `7b89eda8a`); verified consistent with `B1881`'s recomputed mathematics. Nothing wrong found.
- **`B1861` (frontier/B1861_the_closure_programme):** Read window diff across `PROGRAMME.md`, `PROGRAMME.json`, `build_run.txt`, `programme_source.py`, and `test_b1861`; verified that `test_b1861`'s amended debt-count assertion checks cross-surface consistency (`debts_in_md == debts_in_json == debts_in_run`) rather than a hardcoded integer, and reported Finding `F-15` (`W:INDEX3` mid-word table truncation). **Left unchecked per section `13`:** the addition of `P-781` (which includes `agy-exp`'s loop branch) to the unverified-seat-results debt list is left without self-judgment.
- **`B1872` (frontier/B1872_all_histories_together_the_exact_facts_verified):** Read window diff (`2026-11-11` cross-reference note to `B1881` on three symmetry pairs vs the arc between discriminant-`-20` points, committed prior to `7b89eda8a`); verified consistent with `B1881`'s recomputed level-`5` quotients. Nothing wrong found.
- **`B1874` (frontier/B1874_the_scripts_a_seal_hashed):** Read window diff (`2026-11-11` item-by-item reading of the `11` post-seal edits across six arcs in `FINDINGS.md`, committed prior to `7b89eda8a`); verified consistent with `B1486`, `B1494`, `B1499`, and `P-772` (`NOT SETTLED, and noted here: whether B1499's negative should be regraded`). Nothing wrong found.
- **`B1877` (frontier/B1877_review_78_the_decadal_review):** Read window diff (`2026-11-11` dated note on `"even ticks observed"` vs `"the tick is an act"` and string-piece path literal in `test_b1877_review_78.py`, committed at `7480c2426` prior to `7b89eda8a`). Nothing wrong found.

`0 of 19.`
