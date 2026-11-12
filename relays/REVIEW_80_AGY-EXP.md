# Review 80 — Independent Reading (`agy-exp`, Card `X-R80`)

- **Seat / Session:** `agy-exp`
- **Branch:** `agy/self-consistent-loop-2026-11-11`
- **Card:** `relays/cards/AGY-EXP_X-R80_review-80-reading.md` (`17aa8ae48`)
- **Sealed Verification Script:** `relays/x_r80_verify/verify_x_r80.py` (`b1c5cf085`, SHA-256 `aa7b6dd740a50673b67548eb33c6a4f145304f729ce897cc3643fb2a76fe9cc4` in `relays/x_r80_verify/SCRIPT_SHA256.txt`)
- **Raw Unread Output Commit:** `relays/x_r80_verify/verify_x_r80_out.json` (`5e3f7a79b`, SHA-256 `c8618384acf9f1a2010f75ce86cf3a597533b3a638a1ced1c0ff393e1064cd57` in `relays/x_r80_verify/OUTPUT_SHA256.txt`)
- **Commits Read on `main`:**
  - Group A (four full arcs at `c40446392`): `B1891`, `B1894`, `B1895`, `B1897`
  - Group B (eleven post-second-round arc differences on `896cae025..c40446392`): `B862`, `B874`, `B1632`, `B1641`, `B1861`, `B1862`, `B1881`, `B1882`, `B1885`, `B1886`, `B1889`
  - Group C (seven instrument and test differences on `0dda7b472..c40446392`): scripts/seats/listen.py, scripts/atlas/query.py, scripts/checks/point_debt.py, tests/test_seat_listener.py, tests/test_b1641_w46_on_main_and_the_two_objects.py, tests/test_b874_ladder.py, tests/test_b1221_the_adjoint_control.py
  - Group D (four Review-79 window differences from `M12` on `38d2a36dc..0dda7b472`, read at `0dda7b472`): `B734`, `B1028`, `B1222`, `B1643`
- **Isolation:** No other seat's or session's Review-80 file or branch was opened or listed prior to pushing this file.
- **Empirical Firewall:** `0 of 19.`

---

## 1. Recusals and Pre-Output Script Disclosure

### 1a. Mandatory Recusals (`M10`, docs/seats/README.md § 13)

1. **`B1894` (`2X1` through `2X8`):** Recused in full on the eight `agy-exp` second-round items `2X1` through `2X8` (`B1894` records answers to `agy-exp`'s own `REVIEW_79B_AGY-EXP.md`). Only the twenty-seven non-`2X` rows and `B1894`'s shared verification machinery were read for defects.
2. **`B1889` (`agy` / `agy-002` / `agy-exp` section and clause):** Recused in full on the `agy`-family section, table rows, and summary clause in `B1889` (`SEATS.md`, `SEATS.json`, `FINDINGS.md`, `arc_verdict.json`). Only the non-`agy` seat counts and global totals were checked.
3. **`B1885` (`agy`-lane point):** Recused on the `agy`-lane provenance and comparison clause; only the standalone arithmetic and `mpmath` working-precision alignment in golden_state_on_main.py were checked.
4. **Measured / physical quantities:** Recused across all targets (`0 of 19`).

### 1b. Pre-Output Script Amendments Disclosed (docs/seats/README.md § 8)

Before any output file (`relays/x_r80_verify/verify_x_r80_out.json`) was created, three source-spelling assertions inside `relays/x_r80_verify/verify_x_r80.py` aborted early during pre-output execution and were fixed in disclosed commits without rewriting history:
- `686556faf` -> `c3461a951` (Commit 2b): in `m_bypass_5`, matched Python source `"W": list(W)` rather than the JSON-evaluated `[[0, -1], [5, 0]]`.
- `c3461a951` -> `6c7b74afd` (Commit 2c): in the `B1885` source check, matched `mp.mp.dps = 18` rather than `mp.workdps(18)`.
- `6c7b74afd` -> `b1c5cf085` (Commit 2d): in `image_order_riley(2)` (`B734` at characteristic two), guarded `minus_I != I_mat` when halving `len(seen)` (`-I = I` modulo `2`), matching `psl_amb` on the adjacent line.
The single run that produced `relays/x_r80_verify/verify_x_r80_out.json` ran cleanly from `b1c5cf085` and was committed unread at `5e3f7a79b`. All three negative controls (`C-R80-1`, `C-R80-2`, `C-R80-3`) fired as designed.

---

## 2. Hard Question 1 — `B1895` Derived from Statements Alone (No Producer Code Run)

Both mathematical claims added in `B1895` hold in full, and the second extends to resolve `B1895` § 4's open remark on the strict second-least reading across all cyclic run sequences.

### 2a. Coordinate-Swap Conjugation vs Transpose on `SL(2, F_5)` (`120` of `120` Agreement at Isotropic Marks, `88` of `120` at Non-Isotropic Marks)

1. **The two conventions:**
   - The seat's convention acts on row vectors on the right with odd-position step $L = \begin{pmatrix}1 & 0\\ 1 & 1\end{pmatrix}$, even-position step $R = \begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$, and row mark $v = (1, 3) \in \mathbb{F}_5^2$. Its ground word is $G = L R = \begin{pmatrix}1 & 1\\ 1 & 2\end{pmatrix}$, which is symmetric ($G^T = G$) and satisfies $v G = (4, 2) = -v \pmod 5$.
   - Let $J = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ be the coordinate swap ($J^2 = I$, $\det J = -1$). Conjugation by $J$ swaps the two steps: $J L J = R$ and $J R J = L$. Therefore any run sequence $(r_1, r_2, \dots, r_n)$ whose row-convention matrix is $W = L^{r_1} R^{r_2} \cdots$ evaluates under `B1881`'s column convention (which places $R^{r_1}$ first, $L^{r_2}$ second, and acts on columns on the left) to $W_{\text{col}} = R^{r_1} L^{r_2} \cdots = J W J$, with column mark $u_{\text{mark}} = (1, 2)^T = J(2, 1)^T$. On the ground $(1, 1)$, $W_{\text{col}} = J G J = \begin{pmatrix}2 & 1\\ 1 & 1\end{pmatrix} \neq G^T$, refuting any identification of the second convention with the transpose.
2. **Exact bilinear duality on every invertible matrix over $\mathbb{F}_5$:**
   - Under the standard dot product $v \cdot u = v_1 u_1 + v_2 u_2 \pmod 5$, each nonzero row $v \in \mathbb{F}_5^2$ annihilates a unique projective column line $[u] = v^\perp \in \mathbb{P}^1(\mathbb{F}_5)$.
   - For any $W \in \mathrm{GL}(2, \mathbb{F}_5)$, $(v W) \cdot u = v (W u)$. Because $W$ is invertible, the one-dimensional row subspace $\mathbb{F}_5 v$ is stabilized by right multiplication ($v W \in \mathbb{F}_5^\times v$) if and only if $(v W) \cdot u = 0$, if and only if $v \cdot (W u) = 0$, if and only if the orthogonal column line $\mathbb{F}_5 u$ is stabilized by left multiplication ($W u \in \mathbb{F}_5^\times u$).
   - Since $J^2 = I$, $W u = \lambda u \iff (J W J)(J u) = \lambda (J u)$. Thus for **every** $W \in \mathrm{SL}(2, \mathbb{F}_5)$ (all `120` matrices) and **every** $W \in \mathrm{GL}(2, \mathbb{F}_5)$ (all `480` matrices), and for **each of the six** projective lines $[v] \in \mathbb{P}^1(\mathbb{F}_5)$:
     $$v W \in \mathbb{F}_5^\times v \iff (J W J)(J u) \in \mathbb{F}_5^\times (J u), \qquad [u] = v^\perp.$$
3. **Why the swapped-mark recipe agrees on `120` of `120` for $(1, 3)$ and $(1, 2)$ and on `88` of `120` for the other four lines:**
   - The recipe that compares `row c kept by W` against `column J c^T kept by J W J` substitutes $[c^T]$ for $c^\perp = [u]$. Those two lines coincide if and only if $c$ is **self-orthogonal (isotropic)**, $c_1^2 + c_2^2 \equiv 0 \pmod 5$. Since $-1 \equiv 4 = (\pm 2)^2 \pmod 5$, $\mathbb{P}^1(\mathbb{F}_5)$ has exactly **two** isotropic lines: $[(1, 2)]$ and $[(1, 3)]$ ($1^2 + 3^2 = 10 \equiv 0 \pmod 5$, with $[(1, 3)^T] = [2 \cdot (1, 3)^T] = [(2, 1)^T]$, whose swap is $J(2, 1)^T = (1, 2)^T$). On both isotropic lines, $[c^T] = c^\perp$, so the recipe agrees on **all `120` of `120` matrices** in $\mathrm{SL}(2, \mathbb{F}_5)$.
   - On each of the **four non-isotropic lines** $(0, 1)$, $(1, 0)$, $(1, 1)$, and $(1, 4)$, the two lines $\ell_1 = c^\perp$ and $\ell_2 = [c^T]$ are distinct lines in $\mathbb{P}^1(\mathbb{F}_5)$. In $\mathrm{SL}(2, \mathbb{F}_5)$ (order `120`, transitive on the `6` projective lines), the stabilizer $B_i$ of a single line has order $120 / 6 = 20$, and the simultaneous stabilizer $B_1 \cap B_2$ of two distinct lines (choosing bases along $\ell_1, \ell_2$, diagonal matrices $\operatorname{diag}(a, a^{-1})$ with $a \in \mathbb{F}_5^\times$) has order `4`. By inclusion–exclusion, both predicates hold on $|B_1 \cap B_2| = 4$ matrices and both fail on $120 - (20 + 20 - 4) = 84$ matrices, giving $4 + 84 = 88$ agreements and $32$ disagreements out of `120` for **every** non-isotropic line (including $(1, 1)$).
4. **Word-level counts and the reversed-sequence transpose identity:**
   - Across the $6^2 + 6^4 = 1,332$ even-length words of lengths `2` and `4` with runs `1` through `6`: the words surject onto all `120` matrices of $\mathrm{SL}(2, \mathbb{F}_5)$; $J W J \neq W^T$ on `989` of the `1,332` words; and the column test at $(1, 2)^T$ on $J W J$ disagrees with the same column test on $W^T$ on `342` words.
   - Reversing an even-length word $(r_1, \dots, r_{2k}) \mapsto (r_{2k}, \dots, r_1)$ sends $W = L^{r_1} R^{r_2} \cdots L^{r_{2k-1}} R^{r_{2k}}$ under the column convention to $R^{r_{2k}} L^{r_{2k-1}} \cdots R^{r_2} L^{r_1}$. Since $L^T = R$ and $R^T = L$, we have $W^T = L^{r_{2k}} R^{r_{2k-1}} \cdots L^{r_2} R^{r_1}$, and conjugating by $J$ swaps $L \leftrightarrow R$, yielding $W_{\text{col}}(\text{rev}) = J W^T J$. Because $v W \in \mathbb{F}_5^\times v \iff W^T v^T \in \mathbb{F}_5^\times v^T \iff (J W^T J)(J v^T) \in \mathbb{F}_5^\times (J v^T)$, the reversed even-length word satisfies the swapped-mark identity on **all six** lines.

### 2b. Uniqueness of the Least Reading $\sqrt{5}/2$ Below $4/3$, and Uniqueness of $\sqrt{2}$ as Strict Second-Least Across All Cyclic Sequences

1. **Exact continued-fraction tail enclosure:**
   - At step $i$ of any periodic positive-integer run sequence $(r_1, \dots, r_n)$ ($r_j \in \mathbb{Z}_{\ge 1}$), the reading is $H_i = (r_i + x_i + y_i)/2$, where $x_i = 1 / (a_1 + 1/t)$ and $y_i = 1 / (b_1 + 1/s)$ have positive-integer first partial quotients $a_1, b_1 \in \mathbb{Z}_{\ge 1}$ (the two neighbors of $r_i$ on the cycle) and infinite periodic tails $t = 1 + u > 1$, $s = 1 + w > 1$ ($u, w > 0$, because every subsequent partial quotient is at least `1` and the tail is strictly greater than its own integer floor when continued infinitely).
   - Over exact rational algebra (verified symbolically in `verify_x_r80.py`):
     $$x_i - \frac{1}{a_1 + 1} = \frac{u}{(a_1 + 1)\bigl(a_1(u + 1) + 1\bigr)} > 0, \qquad \frac{1}{a_1} - x_i = \frac{1}{a_1\bigl(a_1(u + 1) + 1\bigr)} > 0.$$
     Hence $\frac{1}{a_1 + 1} < x_i < \frac{1}{a_1}$ and $\frac{1}{b_1 + 1} < y_i < \frac{1}{b_1}$ hold **strictly** at every position of every sequence.
2. **Three-way exhaustive case split on $M = \max_j r_j$:**
   - **Case 1 ($M \ge 3$):** Pick $i$ with $r_i = M \ge 3$. Since $x_i > 0$ and $y_i > 0$, the cycle's maximum reading satisfies $\max_j H_j \ge H_i > 3/2 > 4/3$.
   - **Case 2 ($M = 2$):** Pick $i$ with $r_i = 2$. Every entry of the sequence lies in $\{1, 2\}$, so both neighbors satisfy $a_1 \le 2$ and $b_1 \le 2$, whence $x_i > 1/(2 + 1) = 1/3$ and $y_i > 1/(2 + 1) = 1/3$. Therefore:
     $$\max_j H_j \ge H_i > \frac{2 + 1/3 + 1/3}{2} = \frac{4}{3}.$$
   - **Case 3 ($M = 1$, all ones):** Every $r_j = 1$, so $x_i = y_i = (\sqrt{5} - 1)/2$ and $H_i = \sqrt{5}/2$ at every position. Since $(\sqrt{5}/2)^2 = 5/4$ and $(4/3)^2 = 16/9$ with $5 \times 9 = 45 < 64 = 4 \times 16$, we have $\sqrt{5}/2 < 4/3$. Thus all-ones is the **unique** cyclic sequence (for any length and any run bound) below $4/3$.
3. **Resolution of `B1895` § 4's remark on the strict second-least reading $\sqrt{2}$:**
   - Within Case 2 ($M = 2$), either every entry equals `2` — giving $x_i = y_i = \sqrt{2} - 1$ and $H_i = \sqrt{2}$ — or the sequence contains both `2` and `1`. In any cyclic sequence containing both `2` and `1`, at least one `2` sits adjacent to a `1`, so at that index $r_i = 2$, one neighbor is $a_1 = 1$ ($x_i > 1/(1 + 1) = 1/2$) and the other satisfies $b_1 \le 2$ ($y_i > 1/3$). That single step gives:
     $$\max_j H_j \ge H_i > \frac{2 + 1/2 + 1/3}{2} = \frac{17}{12}.$$
   - Squaring compares $(17/12)^2 = 289/144$ against $(\sqrt{2})^2 = 2 = 288/144$ (and in Case 1, $(3/2)^2 = 9/4 = 324/144$). Because $5/4 < 16/9 < 2 < 289/144 < 9/4$, all-twos ($\sqrt{2}$) is strictly the **second-least** apex across **all** positive-integer cyclic sequences of any length, separated from every mixed $\{1, 2\}$ sequence by at least the gap $17/12 - \sqrt{2} > 0$.

---

## 3. Hard Question 2 (`B1897` & `B1881` Diff) and Findings Across the Review-80 Scope

All `14` findings below (`F-R80-1` through `F-R80-14`) carry character-for-character verbatim quotations verified against `c40446392` (`F-R80-1` through `F-R80-12`) or `0dda7b472` (`F-R80-13` and `F-R80-14`) by `verify_exact_quotes()` in `relays/x_r80_verify/verify_x_r80_out.json`. Findings `F-R80-1` through `F-R80-5` answer Hard Question 2 directly: each was executed in an isolated sandbox against `B1881`'s twice-rebuilt lock at `c40446392` and passed all `15` of `15` `pytest` tests (`returncode == 0`), while the planted literal-`True` control failed (`3` failed, `12` passed).

### Finding F-R80-1 — `test_b1881` lets vacuous `all([])` replace both Review-79-mended `mirror_ok` and `single_ok` computations (`15` of `15` pass)

- **Arc:** `B1881`
- **File:** frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py
- **Commit read:** `c40446392`
- **Criterion:** 4 (lock strength — a test that passes when the mended computation is emptied)

```text
assert len(binds) == 1 and "all(" in ast.get_source_segment(src, binds[0].value), name
```

- **Defect and live plant:** `test_the_conditions_of_the_mended_checks_are_the_ones_that_were_mended` pins `mirror_ok` and `single_ok` in `_PINNED_CONDITIONS` and then checks only that `"all("` appears as a substring of each variable's RHS. Replacing `mirror_ok = all(...)` with `mirror_ok = all([])` and `single_ok = all(...)` with `single_ok = all([])` in whole_and_value_on_main.py makes both Review-79-mended checks vacuously `True` without evaluating a single matrix or run, is not flagged by `_constant_checks` (`ast.Call` is not a constant), emits byte-identical run and JSON outputs, and passes all `15` tests (`F-R80-1_vacuous_all_on_mirror_and_single` in `relays/x_r80_verify/verify_x_r80_out.json`).
- **Concrete mend:** Inspect the AST of `binds[0].value` to require a non-empty generator/comprehension over `box` (for `mirror_ok`) and `zip(range(1, 6), single)` with the monotonicity conjunction (for `single_ok`), or import the helper and assert it returns `False` on a corrupted `box` / `single` list.

### Finding F-R80-2 — `test_b1881` never tests that `whole_and_value_on_main.check()` honors its boolean argument (`15` of `15` pass when `64` of `65` checks are forced to `True`)

- **Arc:** `B1881`
- **File:** frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py
- **Commit read:** `c40446392`
- **Criterion:** 4 (lock strength — `check()` itself is never exercised on a `False` input)

```text
"""lines of a script where check() is passed a constant, or a name bound once to a constant, or RES[...] is assigned one"""
```

- **Defect and live plant:** Every AST scan in `test_b1881` inspects the call sites `check(label, cond, detail)` while assuming `def check(...)` faithfully records its second positional argument. Changing `def check(name, ok, detail=""):` in whole_and_value_on_main.py to `def check(name, _ignored_ok, detail="", ok=True):` causes all `64` call-site checks to record `True` and print `[ok]` regardless of whether their second argument evaluates to `False`, emits byte-identical outputs on the committed script, and passes all `15` tests (`F-R80-2_neutralized_check_function`).
- **Concrete mend:** In `test_b1881`, import `mod = _the_script()`, call `mod.check("probe", False)` in an isolated state, and assert `mod.RES["probe"] is False` and `"probe" in mod.FAILS` (plus pin the AST / signature of `def check`).

### Finding F-R80-3 — `test_b1881`'s `or`-tautology guard checks only comparisons against `0` and `-1`, letting `or len(OUT) >= 1` bypass any unpinned check (`15` of `15` pass)

- **Arc:** `B1881`
- **File:** frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py
- **Commit read:** `c40446392`
- **Criterion:** 4 (lock strength — narrow regex against one planted spelling of an always-true disjunct)

```text
assert not re.search(r"len\([^)]*\)\s*(>=\s*0|>\s*-1|>\s*0)\b", seg), seg[:120]
```

- **Defect and live plant:** Only `3` of the `65` checks are in `_PINNED_CONDITIONS`. On any of the other `61` `check(...)` calls (for example, the central least-apex check comparing `floor` against `mp.sqrt(5) / 2`), replacing `cond` with `(False and cond) or len(OUT) >= 1` makes the check unable to fail (`OUT` already holds dozens of header lines), avoids `_constant_checks`, misses the `>=\s*0|>\s*-1|>\s*0` regex, emits byte-identical outputs, and passes all `15` tests (`F-R80-3_always_true_or_len_ge_1`).
- **Concrete mend:** Forbid top-level `ast.Or` in `check(...)` conditions altogether unless explicitly whitelisted for a mathematical disjunction, or require every `check(...)` condition to depend solely on the mathematical variables of its section (forbidding globals `OUT`, `RES`, `FAILS` inside `check` arguments).

### Finding F-R80-4 — `test_b1881` checks `by_all` and `by_even` by `.startswith(...)`, allowing all three sequence counts and `floor` to be typed without evaluating a single sequence (`15` of `15` pass)

- **Arc:** `B1881`
- **File:** frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py
- **Commit read:** `c40446392`
- **Criterion:** 4 (lock strength — prefix string match instead of full expression check)

```text
assert len(binds) == 1 and ast.get_source_segment(src, binds[0].value).startswith("len({min(seq[i:] + seq[:i] for i in range("), name
```

- **Defect and live plant:** Replacing the `16,275`-sequence loop `lows.append(max(heights(list(seq))))` with `lows.extend([mp.sqrt(5) / 2] * 16275)` and replacing `by_all` and `by_even` with `len({min(seq[i:] + seq[:i] for i in range(0)) for seq in []}) or 2815` and `... or 5575` skips all `16,275` continued-fraction evaluations (finishing roughly seven seconds faster), satisfies `names == ["len(lows)", "by_all", "by_even"]`, satisfies `.startswith("len({min(seq[i:] + seq[:i] for i in range(")`, bypasses `_constant_checks`, emits byte-identical outputs, and passes all `15` tests (`F-R80-4_typed_counts_behind_startswith`).
- **Concrete mend:** Pin the exact full source segments of `by_all`, `by_even`, and the `lows` comprehension (using `==` rather than `.startswith(...)`), and factor the orbit counter / floor finder into a callable helper tested on a non-`5` alphabet size (such as runs `1..3` of length `2, 4`).

### Finding F-R80-5 — `test_b1881` trusts `whole_and_value_on_main_made_with.json` without comparing it to the fresh run's sidecar, and `_held_under_another_version` ignores `A_numbers` and `B_numbers` (`15` of `15` pass with `"W"` corrupted)

- **Arc:** `B1881`
- **File:** frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py
- **Commit read:** `c40446392`
- **Criterion:** 4 (lock strength — version-fallback branch drops two numerical dictionaries and never verifies the sidecar written by the run)

```text
assert all(new[k] == old[k] for k in old if isinstance(old[k], bool)) and new["B_counts"] == old["B_counts"]
```

- **Defect and live plant:** `whole_and_value_on_main.py` writes `whole_and_value_on_main_made_with.json` on every run, yet `_run_the_script_in_a_copy` discards `work / "whole_and_value_on_main_made_with.json"` and `test_what_is_held_under_another_version...` checks only `set(made) == {"python", "mpmath", "sympy"}`. Meanwhile `_held_under_another_version` checks boolean entries and `B_counts`, omitting `A_numbers` and `B_numbers` completely. Setting `"python"` to `"zero-dot-zero"` (`"0" + "." + "0"`) in committed `whole_and_value_on_main_made_with.json` while corrupting `"W": list(W)` to `[[999 + len(OUT), 999], [999, 999]]` in `whole_and_value_on_main.py` forces `same == False` and passes all `15` tests (`F-R80-5_version_sidecar_unheeded_A_numbers`).
- **Concrete mend:** When `same` is `True` on the host environment, assert the fresh run's `whole_and_value_on_main_made_with.json` equals `_made_with()`; and in `_held_under_another_version`, compare `new["A_numbers"]` and `new["B_numbers"]` (exact on integers/rationals and to eight significant digits on formatted strings).

### Finding F-R80-6 — `test_b1891` omits the fourth corrected sentence from its unbracketed-old-form guard and omits `set(now_tab) == set(snap["status_table_rows"])` from its no-added-item check

- **Arc:** `B1891`
- **File:** frontier/B1891_the_foundation_at_version_1_66/verification/test_b1891_the_foundation_at_version_1_66.py
- **Commit read:** `c40446392`
- **Criterion:** 4 (lock strength — docstring promises all four old sentences and no added item, while code checks three of four sentences and one of two row maps)

```text
for old in ("Eleven entries", "every statement the record holds about the weave is unchanged except the hand"):
```

- **Defect and live plant:** `test_b1891`'s module docstring states *"What could fail: a status cell differing from version 1_65 as committed; one of the four corrected sentences standing in its old form outside the bracket that quotes it"*, and `FINDINGS.md` claims *"No item is added"*. However:
  1. `test_the_four_sentences_stand_corrected_and_the_old_forms_only_where_they_are_quoted` forbids the third old sentence via `not in FLAT` and checks bracket context for only the first two (`"Eleven entries"` and `"every statement..."`), omitting the fourth old sentence (`"it is the only history of at most five letters that does"`) altogether. Appending that fourth old sentence unbracketed as a fresh paragraph in `GENESIS.md` passes `test_b1891` (`fourth_old_sentence_unbracketed_passes_b1891 == True`).
  2. `test_no_status_cell_changed_from_version_1_65` asserts `set(now_id) == set(snap["identifier_rows"])` (`# and no item is added`) while omitting `set(now_tab) == set(snap["status_table_rows"])` (and omitting `bs.unspaced_table_lines(G) == []`). Inserting an untracked `DERIVED` row into a `Status`-headed table in `GENESIS.md` passes `test_b1891` (`added_status_table_row_passes_b1891 == True`).
- **Concrete mend:** Add `"it is the only history of at most five letters that does"` to the `for old in (...)` bracket-context loop, and add `assert set(now_tab) == set(snap["status_table_rows"]) and bs.unspaced_table_lines(G) == []`.

### Finding F-R80-7 — `B1894`'s `quote_check.py` widens `pool` across the entire arc folder and `WIDE` even when a specific file is named, and `test_b1894` passes `r is None` without re-running on synthetic inputs

- **Arc:** `B1894`
- **File:** frontier/B1894_review_79_the_second_round/verification/quote_check.py
- **Commit read:** `c40446392`
- **Criterion:** 4 (lock strength — quotation checker reports a quotation found in the file it names when the named file does not contain it)

```text
pool = ([named] if named in fs else []) + ([f for f in fs if f.startswith("frontier/%s_" % arc)] if arc else []) + [f for f in WIDE if f in fs]
```

- **Defect and live plant:** `quote_check.py`'s docstring states *"every quotation of the four readers' second files, looked for in the file it names at the commit of main the reader read"*. Yet `found(q, arc, named)` unconditionally unions `[named]` with **every** file in `frontier/<arc>_*` and all ten files in `WIDE` (and for `"the SM seat"`, `quotations()` emits `(None, None, q)`, ignoring arc and file attribution altogether). Calling `qc.found("Version 1" + "." + "65", "B1886", "ROADMAP.md")` — naming `ROADMAP.md` for text that sits in `GENESIS.md` — returns `True` (`b1894_wrong_named_file_accepted == True`). In addition, `test_b1894` asserts `r is None or r == q[reader]` (passing vacuously whenever seat branch commits are absent from a clone of `main`) and locks only `2A3`/`2A4` among the prose mends in `ANSWERS.md`.
- **Concrete mend:** When `named` is provided and present in `fs`, check `[named]` alone (falling back to the arc folder only when `named` is omitted), and add a synthetic unit test in `test_b1894` asserting `found(...)` rejects a quotation attributed to the wrong file.

### Finding F-R80-8 — `B1895` (`"instrument": false`) and `B1897` carry session identifier `agy-002` inside `claim_one_line`, publishing a session key onto `VERDICT_LEDGER.md`

- **Arc:** `B1895`
- **File:** frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/arc_verdict.json
- **Commit read:** `c40446392`
- **Criterion:** 8 (hygiene — `P-797` and docs/seats/README.md § 12 forbid session keys in published claim lines and living ledgers)

```text
THE MENDS OF B1881 READ BY A SESSION THAT DID NOT WRITE THEM: FOUR FINDINGS, ALL HELD, AND WHAT THE ARC'S SECOND CONVENTION IS (agy-002's reading of main at 87bfa1f05, 4 of 4 quotations found by machine;
```

- **Defect:** docs/seats/README.md § 12 and `P-797` state that seat/session names belong in relays, commit trailers, and provenance notes rather than published claim lines (`VERDICT_LEDGER.md` is rebuilt directly from `claim_one_line` of every `arc_verdict.json`). Both `B1895/arc_verdict.json` (which sets `"instrument": false` and `"verdict": "PROVED"`) and `B1897/arc_verdict.json` (`"agy-002 then planted 23 of its own..."`) write the session key `agy-002` directly into `claim_one_line`, whereas `B1895`'s and `B1897`'s titles already express the provenance cleanly (`"a session that did not write them"` / `"a session that did not write it"`).
- **Concrete mend:** Replace the session key in `B1895/arc_verdict.json` and `B1897/arc_verdict.json` `claim_one_line` with `"an independent session's reading"` / `"that session then planted 23 of its own"` (keeping the commit hashes in `FINDINGS.md` provenance), and rebuild `docs/views/VERDICT_LEDGER.md`.

### Finding F-R80-9 — `test_b1895` treats an entire `.json` file as a single block in its old-transpose sweep, allowing an uncorrected `"transpose"` claim anywhere else in `B1881/arc_verdict.json`

- **Arc:** `B1895`
- **File:** frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/verification/test_b1895_the_mends_of_b1881_read.py
- **Commit read:** `c40446392`
- **Criterion:** 4 (lock strength — file-level rather than field-level masking on `.json`, plus unexecuted verification scripts in `B1895` and `B1897`)

```text
blocks = [text] if f.endswith(".json") else text.split("\n\n")
```

- **Defect and live plant:** `test_the_old_word_stands_nowhere_on_main_without_its_correction` splits Markdown files on `"\n\n"` so a correction in one paragraph cannot mask an uncorrected statement in another, yet wraps an entire `.json` file into a single one-element list `[text]`. Because `B1881/arc_verdict.json` already contains `"not the transpose"` inside `claim_one_line`, planting `"Unamended plant: the columns are the transpose that B1881 used."` inside `scope["hypotheses"]` (or `note`) of `B1881/arc_verdict.json` yields `hits == []` and passes `test_b1895` (`b1895_json_whole_file_block_plant_passes == True`). Furthermore, `"this label read"` in `marks` is a generic substring rather than a transpose-specific retraction, and neither `test_b1895` nor `test_b1897` executes `B1895`'s `quote_check.py` or `B1897`'s `plant_23_errors.py` (checking only saved `.json` artifacts).
- **Concrete mend:** Split `.json` files per leaf string value (such as `claim_one_line`, each key of `scope`, and `note`) rather than `[text]`, tighten `"this label read"` to the specific retraction phrase, and invoke a lightweight self-test of `quote_check.py` / `plant_23_errors.py` from `pytest`.

### Finding F-R80-10 — `B1861` removed two owner chat quotes from `NOT_CONFIRMED` per `P-796`, yet left `CONFIRMATION` verbatim in `programme_source.py` and rendered into living page `PROGRAMME.md`

- **Arc:** `B1861`
- **File:** frontier/B1861_the_closure_programme/verification/programme_source.py
- **Commit read:** `c40446392`
- **Criterion:** 5 and Criterion 8 (internal consistency of the `896cae025..c40446392` mend and `P-796` hygiene on a rebuilt living page)

```text
# the owner's answer to main, verbatim (spelling as written), and the rulings it covers: the eleven main had named in its question
```

- **Defect:** In `896cae025..c40446392`, `B1861` replaced two `2026-11-10` owner chat quotations in `NOT_CONFIRMED` with plain-prose descriptions because `PROGRAMME.md` is a living page rebuilt at every landing rather than frozen history (`P-796`). Five lines above `NOT_CONFIRMED` in `programme_source.py`, however, `CONFIRMATION` (`2026-11-10`) still holds the owner's verbatim chat message (not reproduced here per `P-796`), and `build_programme.py` still emits `"> \"%s\"" % S.CONFIRMATION[1]` straight into `frontier/B1861_the_closure_programme/PROGRAMME.md` (`b1861_confirmation_verbatim_quote_in_living_page == True`). In addition, `build_programme.short(",;: " + "y" * 200, 110)` strips the empty prefix before the first space and returns `" […]"` (`b1861_short_punct_prefix_returns_mark_alone == True`).
- **Concrete mend:** Paraphrase `CONFIRMATION[1]` in plain indirect prose in `programme_source.py` and `build_programme.py` (matching `NOT_CONFIRMED` and `DIRECT_RULINGS`), and guard `if not cut.rstrip(",;:")` before substituting `cut` in `short()`.

### Finding F-R80-11 — `B862`'s `kernel_exact(grid=0)` and `kernel_exact(grid=-6)` pass `if grid % need:` and silently return `[]` instead of raising `ValueError`

- **Arc:** `B862`
- **File:** frontier/B862_global_form/global_form.py
- **Commit read:** `c40446392`
- **Criterion:** 3 and Criterion 4 (domain guard completeness — incomplete grid returns part of the kernel without a word)

```text
need = math.gcd(3 * abs(c1), 2 * abs(c2))
    if grid % need:
```

- **Defect and live plant:** `kernel_exact`'s docstring states *"A grid that is not a multiple of g would return a part of the kernel without a word. It is refused now"*. Because `0 % need == 0` and `(-6) % 6 == 0` in Python while `range(grid)` is empty for `grid <= 0`, calling `kernel_exact(0, charges=(-2, 3))` or `kernel_exact(-6, charges=(-2, 3))` raises nothing and silently returns `[]`, missing all `6` kernel elements (`b862_grid_zero_returns_empty_without_raising == True`, `b862_grid_negative_returns_empty_without_raising == True`).
- **Concrete mend:** Guard `if grid <= 0 or grid % need:` so every non-positive `grid` raises `ValueError`, and add `grid=0` and `grid=-6` to `test_b862_global_form.py`.

### Finding F-R80-12 — scripts/seats/listen.py silently drops in-place amendments on legacy memory whenever a new message arrives on the same push, and swallows non-message `###` headings

- **Arc:** `window`
- **File:** scripts/seats/listen.py
- **Commit read:** `c40446392`
- **Criterion:** 3 and Criterion 4 (edge case in the `0dda7b472..c40446392` legacy-memory mend + docstring/code mismatch)

```text
if not new and not amended and read and not sums:
```

- **Defect and live reproduction:** The `0dda7b472..c40446392` mend added a warning for legacy state files (`read > 0` with no `"sums"` dictionary) so an in-place amendment to `M1..Mk` is not silently overwritten by `remember()`. Because the condition requires `not new`, whenever `main` in the same window **both** posts a new message `M(k+1)` **and** amends an earlier message `M1..Mk` in place, `new` is non-empty, `amended` is empty (`str(n) in sums` is `False`), the legacy-memory warning is skipped, and `remember()` immediately writes `"sums"` with the amended hash of `M1..Mk`. Subsequent runs return status `3`, losing the in-place amendment to `M1..Mk` permanently without warning (`listen_legacy_memory_new_plus_amended_silently_lost == True`). Secondarily, `messages()`'s docstring states each message runs *"to the next heading of its level or above"* (`###` is level `3`), whereas line `108` matches `r"^#{1,2} "`, swallowing any trailing non-`M<n>` level-`3` heading into the preceding message (`listen_non_message_h3_swallowed == True`).
- **Concrete mend:** Change line `158` to emit the legacy-memory notice whenever `read and not sums` (even when `new` is non-empty: append `"Note: legacy memory held no text hashes for M1..M%d; re-check those messages once for in-place edits."`), and change `r"^#{1,2} "` in `messages()` to `r"^#{1,3} "`.

### Finding F-R80-13 — In `M12` (`0dda7b472`), `B1222/FINDINGS.md` inserts its `E7` correction as a separate list bullet, and `test_b1028`'s `_units()` masks bare zero claims across unrelated bullets of any Markdown list

- **Arc:** `B1222`
- **File:** frontier/B1222_symmetry_vanishing_thesis/FINDINGS.md
- **Commit read:** `0dda7b472`
- **Criterion:** 4 and Criterion 5 (list-item structure in `B1222` and paragraph-joining gap in `tests/test_b1028_freedom_ledger.py`)

```text
- [CORRECTED 2026-11-11 (the audit's finding E7): the freedom ledger's zero is not a computed quantity.
```

- **Defect and live plant:** In `38d2a36dc..0dda7b472`, `frontier/B1222_symmetry_vanishing_thesis/FINDINGS.md` lies in a bulleted list of **ten** counterexamples (`"7 of 10"`). Inserting `- [CORRECTED 2026-11-11 ...]` as a separate standalone bullet above `- **designer freedom ...**` turns the ten-bullet list into eleven bullets (where the correction bullet is formatted as if it were one of the counterexamples rather than attached inside the `designer freedom` bullet). Worse, `tests/test_b1028_freedom_ledger.py`'s `_units()` joins every non-table line between blank lines into a single `prose` string (`prose = " ".join(...)`), so a `[CORRECTED ...]` tag in bullet `1` of any tight Markdown list masks an unamended `B1028` zero claim in bullet `3` (`b1028_bullet_list_join_plant_passes == True`). Also in `test_b1028`, `frontier/B1028_freedom_ledger/FINDINGS.md` is listed in `OWN_RECORD` (exempt from `_bare_statements`) while `CARRIED` checks only `MARK.lower() in text.lower()` anywhere in the file, so moving `B1028/FINDINGS.md`'s leading correction banner to a footnote at the bottom of the file would still pass `test_b1028`.
- **Concrete mend:** Fold the `[CORRECTED 2026-11-11 ...]` note into the `- **designer freedom ...**` bullet in `B1222/FINDINGS.md`, split Markdown bullet items (`^\s*[-*+]\s+`) into separate units in `test_b1028._units()`, and assert `MARK.lower()` appears before the first `##` heading of `B1028/FINDINGS.md`.

### Finding F-R80-14 — In `M12` (`0dda7b472`), `tests/test_b734_m004_congruence.py` sweeps only `claim_one_line` on `.json` files, omitting `scope` and `note`

- **Arc:** `B734`
- **File:** tests/test_b734_m004_congruence.py
- **Commit read:** `0dda7b472`
- **Criterion:** 4 (lock parity between `test_b734` and `test_b1028` on `arc_verdict.json` fields)

```text
text = json.loads(text).get("claim_one_line", "")
```

- **Defect:** Whereas `tests/test_b1028_freedom_ledger.py` at the same commit (`0dda7b472`) sweeps `("claim_one_line", "scope", "note")` of every `arc_verdict.json`, `tests/test_b734_m004_congruence.py` replaces the `.json` file content with `.get("claim_one_line", "")` alone (`b734_json_sweep_reads_claim_one_line_only == True`). Any unamended `"congruence at level 8"` / `"level (2)^3 = (8)"` statement inside `scope` or `note` of any `arc_verdict.json` passes `test_b734` unseen. (Also noted with date context: `B734/FINDINGS.md`'s `2026-11-11` banner uses pre-`P-795` authority phrasing `"accepted"` / `"verdict"` from the day before `P-795` was registered.)
- **Concrete mend:** Join `str(d[k]) for k in ("claim_one_line", "scope", "note") if d.get(k)` in `tests/test_b734_m004_congruence.py`, matching `test_b1028`.

---

## 4. Clean Targets Verified Across Groups B, C, and D (One-Line Check Summary Each)

Every remaining target in `X-R80` was read in full and checked; none carried an unreported defect:

1. **`B874` (`896cae025..c40446392`) and `tests/test_b874_ladder.py` (`0dda7b472..c40446392`):** Verified the added scope disclosure (`E_8 -> E_7 -> E_6 -> D_5 -> A_4` uniqueness holds within rank-by-one simple Dynkin-node deletions, while maximal non-simple centralized subgroups such as `A_8`, `D_8`, `A_4 + A_4` are distinct ambient-group reductions) and confirmed `test_b874_ladder.py` locks both phrases.
2. **`B1632` (`896cae025..c40446392`):** Verified the `[READ THIS FIRST, ADDED 2026-11-12 ...]` scope notice in `B1632/arc_verdict.json` `claim_one_line` (`VERDICT_LEDGER.md` truncates at `150` characters) and confirmed `B1896`'s lock (`test_b1896_scope_before_the_cut.py`) pins the leading prefix.
3. **`B1641` (`896cae025..c40446392`) and `tests/test_b1641_w46_on_main_and_the_two_objects.py` (`0dda7b472..c40446392`):** Independently recomputed the exact unitary eigenvalues of $r_T$ (turns $1/8, 3/8, 7/8$), $\exp(i\pi k/2) r_S$, and $(\exp(i\pi k/3) r_S r_T)^{-1}$ at $k = 3/2$ in SymPy (`b1641_chi3_and_minus_chi3_verified == True`), confirming $\chi_{3/2}(m) = m_1 + m_2 + m_3$ ($0$ at $(0, 0, 0)$, $1$ at $(1, 0, 0)$, $3$ at $(1, 1, 1)$), four-dimensional index $-\chi_{3/2}(n, n, n) = -3n$ across both identifications in `w46_on_main.json`, and dimension $\max(0, m_1 + m_2 + m_3)$ differing from $\chi_{3/2}$ on `10` of `64` vectors in `{-1, 0, 1, 2}^3`.
4. **`B1862` (`896cae025..c40446392`):** Verified the `B862` charge-dependent grid guard note in `B1862/FINDINGS.md` and `test_b1862_the_audits_first_corrections.py` matches `B862`'s diff (modulo the `grid <= 0` domain edge reported on `B862` in `F-R80-11`).
5. **`B1882` (`896cae025..c40446392`):** Checked `v1_null.json` across all `9` `(null, menu)` cells (the `20%` top-edge clustering figure holds, bottom-end proportions sit near eighteen-hundredths against three-tenths, and top-layer covariant count `130` vs `123` is within null dispersion) and verified `_inside_a_correction` in `test_b1882` narrows bracket exemptions from whole paragraphs to bracket spans.
6. **`B1885` (`896cae025..c40446392`, recused on `agy`-lane point):** Confirmed `mp.mp.dps = 30` and `mp.mp.dps = 18` alignment in `golden_state_on_main.py` (`b1885_dps_30_and_18_verified == True`) and verified `test_b1885` checks exact agreement without importing recused lane prose.
7. **`B1886` (`896cae025..c40446392`):** Tested `build_status_cells.py`'s new duplicate-key `ValueError` guards on both `identifier_rows` and `status_table_rows` (`b1886_duplicate_identifier_raises == True`, `b1886_duplicate_table_row_raises == True`) and confirmed `test_b1886` exercises both plus `unspaced_table_lines`.
8. **`B1889` (`896cae025..c40446392`, recused on `agy` / `agy-002` / `agy-exp` section and clause):** Verified non-recused `SEATS.json` counts (`rows == 1699`; `chat1`: `240` rows, `74` recomputed, `63` verified; `audit`: `314` rows; and `46 + 15 = 61` unread items across ended seats plus quiet `sm`, `b1889_non_recused_counts_verified == True`).
9. **`scripts/atlas/query.py` (`0dda7b472..c40446392`):** Verified the query-surface update matches the current ledger / registry layout cleanly with no silent fallback.
10. **`scripts/checks/point_debt.py` (`0dda7b472..c40446392`):** Verified `FLOOR = 823` matches the exact row count `P-001` through `P-823` of `docs/POINT_REGISTER.md` at `c40446392` (`point_debt_floor_matches_823_rows == True`).
11. **tests/test_seat_listener.py (`0dda7b472..c40446392`):** Verified the added tests exercise `look_main` `git for-each-ref` non-zero exit preservation and the `not new` legacy-memory path (leaving only the `new` + `amended` legacy-memory combination reported in `F-R80-12`).
12. **tests/test_b1221_the_adjoint_control.py (`0dda7b472..c40446392`):** Verified the strengthened adjoint-control lock computes the comparison directly rather than reading a typed flag.
13. **`B734` mathematics (`38d2a36dc..0dda7b472`, `M12`):** Independently enumerated $|\mathrm{SL}(2, \mathcal{O}_3/(m))|$ and the true Riley generator image $\langle A, B_{\text{Riley}}\rangle$ ($B_{\text{Riley}} = \begin{pmatrix}1 & 0\\ -\omega & 1\end{pmatrix}$) at all three levels $m = 2, 4, 8$ without assuming $|\mathrm{SL}(2, \mathcal{O}_3/(8))| = 245,760$: obtained $(60, 10, 6, 6)$ at $(2)$, $(3840, 320, 12, 6)$ at $(4)$, and $(245760, 20480, 12, 12)$ at $(8)$, plus norm-$2$ inertness modulo `4` (`b734_two_inert_mod_4 == True`), confirming standard $\mathrm{PSL}(2, \mathcal{O}_3)$ congruence level `(4)` (lock gap on `.json` fields reported in `F-R80-14`).
14. **`B1643` (`38d2a36dc..0dda7b472`, `M12`):** Verified the `[CORRECTED 2026-11-11 (the audit's finding E7): ...]` bracket sits directly inside the paragraph citing `B1028` in `frontier/B1643_the_crossings_census/FINDINGS.md` and matches `B1028`'s `OPEN` status at `0dda7b472`, while `tests/test_b1643_the_crossings_census.py` requires `B1028` to be absent from `proved`.

`0 of 19.`
