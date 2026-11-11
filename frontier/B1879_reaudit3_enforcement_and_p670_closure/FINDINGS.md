# B1879 — RE-AUDIT 2 AND RE-AUDIT 3 ENFORCEMENT CLOSURE, REVIEW 78 APPEND-ONLY FIXES, THE JTHETA SWEEP COMPLETED, AND SUITE REPAIRS

**Date:** `2026-11-11`  
**Verdict:** `PROVED` (process and instrument arc; `0 of 19`)  
**Rows closed or advanced:** `P-154` (`DONE`), `P-670` (`DONE`), `P-772` (`(b)(c)(d)(f)` + `Re-Audit 3` `t3, t4, t7, j4` + `Review 78` `append-only` reader items paid on `main`), `P-757` (`G1, G2, G4, G5–G10, G13, G14, L4, L6, L7, L10, X3` first half paid on `main`)

---

## 1. What was open at `015be0cc7`, and what this arc closes

Three adversarial harnesses from the advisor seat (`planted_violations.py` with leaf `PV14` at `6ab743907`; `further_plants.py` at `d59e36d8`; and `reaudit3/plants.py` at `6ab743907`, harvested as row `1671`), together with the `Review 78` reader notes on `append-only` (`P-772(d)`), `P-154` (`retraction-sweep`), `X3`/`L6`/`L10`, and `P-670` (`jtheta` outside the fundamental strip), stood open on `main` after `B1878`.

### 1.1 `Re-Audit 3` residuals (`t3, t4, t7, j4`, `E2, L6, V4`) and leaf `PV14`

1. **`t3` (decoy shadowing on `artifact-hashes`):** Previously, `_resolve_hash_entry` checked `os.path.join(list_dir, name)` before `os.path.join(repo, name)`, allowing a decoy tracked file at `frontier/B.../verification/frontier/...` to mask edits to a top-level `frontier/...` script. `_resolve_hash_entry` now resolves paths starting with top-level repository roots (`frontier/`, `scripts/`, `tests/`, `docs/`, `papers/`, `outside_bench/`) strictly from `ROOT`, and fails closed with `AMBIGUOUS` whenever a bare or relative entry matches more than one distinct tracked path across `list_dir`, `list_dir/verification`, and `ROOT`.
2. **`t4` (re-editing a frozen broken script):** Pre-existing `MISMATCH` entries frozen by key in `ARTIFACT_HASHES_BROKEN` are now also pinned by their exact disk SHA-256 at `015be0cc7` (`ARTIFACT_HASHES_BROKEN_DISK`), so any second edit or deletion fails `artifact-hashes` with `MODIFIED AFTER FREEZE`.
3. **`t7` (secondary seal hash lists such as `SEAL_SHA256.txt`):** `verification/measure_other_hash_lists.py` inventories every tracked `<sha256>  <path>` file outside `ARTIFACT_HASHES*.txt` (`docs/OTHER_HASH_LISTS.md`: `79` matched secondary seal lists with `266` entries — `126` verifying, `140` historical mismatches frozen by key and `65` present-file mismatches pinned by disk SHA-256 — plus `71` heuristic/intake files documented apart). `gate_artifact_hashes` now checks all `79` secondary seal lists and enforces history immutability from `015be0cc7` (`OTHER_HASH_LISTS_IMMUTABLE_FROM`).
4. **`j4` and `BEARS_ON` (`B1861` closure programme):** `build_programme.py` adds **Rule 21**, reading `REAUDIT_2_2026-11-10.md` at `S.ADVISOR[0]` (`e7703f2ec`) when present in the clone and refusing any `ACCEPTED` entry incompatible with the advisor seat's table verdict. `programme_source.py` adds `B734` and `tests/test_b734_m004_congruence.py` to `BEARS_ON["E2"]`, `B1849` and `B1850` to `BEARS_ON["L6"]`, and `B1840` and `B1841` to `BEARS_ON["V4"]`.
5. **Leaf `PV14` (`arc_verdict.json` JSON corruption on an unreferenced leaf arc):** Both `gate_arc_verdicts` in `scripts/gates/gates.py` and `scripts/checks/arc_data.py` parse every `frontier/B*/arc_verdict.json` unconditionally (including leaf arcs that no downstream `depends_on` names) and fail closed on invalid JSON or non-dict payloads.

### 1.2 `P-772(b)(c)(d)(f)`, `Review 78` reader additions, and `P-757` gates (`PV9..PV24, p2`)

6. **`G1 / a1` + `Review 78` reader additions (`P-772(d)` — `append-only`):** `archive_append_only_problems` checks `docs/progress/PROGRESS_*.md` across history after `015be0cc7` (`ARCHIVE_IMMUTABLE_FROM`). On roll-ups, `_rollup_ok` verifies that any header text before the first `## 20` dated heading is preserved verbatim, and `append_only_problems` restricts the roll-up archive check to `docs/progress/*.md` files added or modified (`--diff-filter=AM`) in that commit itself. Unit locks in `tests/test_b1879_reaudit3_and_enforcement.py` explicitly cover committed log deletion, committed log rename, header alteration, pre-existing archive reuse, and module-level `APPEND_ONLY_WAIVED`.
7. **`G2 / s2, s3` (`P-772(c)`) & `G4 / s4` (`P-772(b)`):** `SEAL_PATTERNS` walks `frontier/B*/**/` recursively across `PREREG*`, `*DESIGN*.md`, `SEALED*.md`, `DECLARATION.md`, `PRE_RUN_NOTE*.md`, and `*RULE.md` (`474` files; `docs/SEAL_LEDGER.md` and `docs/SEAL_ORDER_UNSHOWN.md` updated), while `seal_order_after_problems` refuses any rule committed after `FINDINGS.md` outside the frozen historical ceiling (`SEAL_ORDER_AFTER_CEILING`).
8. **Fail-closed git/baseline gates (`G5, G6, G7, G8, G9, G10, G13, G14, L4, L7`):**
   - `PV9–PV13, PV15, PV22`: git-dependent and debt/register/chain-lock gates fail closed when git is absent, in a shallow clone lacking `S306_ROOT`, or when required target ledgers/verdicts are missing; `harvest_debt.py`, `lead_debt.py`, and `relay_debt.py` pin timestamps to commit time (`git log -1 --format=%cs HEAD`) rather than wall-clock date.
   - `PV16`: `gate_gate_controls` AST-inspects `tests/GATE_CONTROLS.json` targets to refuse `@pytest.mark.skip`, `xfail`, `pytest.skip()`, or assertion-free controls.
   - `PV17` & `P-154`: `scripts/checks/retraction_sweep.py` parses Format 3 (`2026-10-07` onward 4-column unquoted `CLAIM RETRACTED` tables), raising active swept phrases to `47` with zero live unnegated hits.
   - `PV19`: `gate_attribution` freezes `ATTRIBUTION_CEILING` in code so raising `docs/ATTRIBUTION_BASELINE.json` fails.
   - `PV20, PV21`: `gate_claims` requires lock references on `## Proven` rows in `CLAIMS.md`; `gate_framing` scans `papers/**/*.tex` case-insensitively.
   - `PV24`: `check_test_vacuity.py` refuses pure both-literal test functions across all `6,400+` tests; `19` historical pure-literal tests are upgraded to compute invariants from real module data.
   - `L4 / p2`: `gate_tracked_deps` propagates local string constants and `Path` joins across AST statements so multi-step untracked reads (`name = "driver_k1" + ".log"`) fail.

---

## 2. `X3` (first half), `L6`, `L10`, and `P-670` (`WP-0.3`)

- **`X3` (first half — `the_price_is_twelve.py` & `docs/THE_SM_VERDICT.md`):** `docs/THE_SM_VERDICT.md` strikes the superseded `22 ROWS OUTSTANDING` line and states the live union-find count (`4 axioms + 20 UNEARNED rows = 24 ROWS OUTSTANDING; 20 rows reduce to 9 IRREDUCIBLE SOURCES, so the free-input count is 4 + 9 = 13`). `outside_bench/certificates/the_price_is_twelve.py` exits `0` (`test_b1873` updated with a dated note; `X3` graded `"PARTLY FIXED"` in `B1861` because `B1266`'s typed `AXIOMS = 4` vs graph-computed price remains `P-773` / `WP-0.12`).
- **`L10` (`PV27` — read-only test runs):** `B1464/verification/seal_census.py` and `B1690/verification/main_w81_w83.py` write JSON only when passed `--write`, leaving tracked JSON files clean during `pytest`.
- **`L6` (`PV26` — numerical residual locks):** `B1849` and `B1850` locks parse machine-epsilon residuals and require `< 1e-12` numerically rather than exact float-string equality.
- **`P-670` (`WP-0.3` closed):** `verification/p670_variable_order_sweep.py` sweeps all `101` tracked `.py` files calling `jtheta` (`80` outside S305's literal-2 list):
  - Verifies the exact quarter-nome sheet law $\operatorname{jtheta}(k, u, e^{i\pi\tau}) / \theta_k^{\text{hol}}(u \mid \tau) = (-i)^{\lfloor(\operatorname{Re}\tau + 1)/2\rfloor}$ for both $q^{1/4}$-bearing indices $k \in \{1, 2\}$ across $\operatorname{Re}\tau \in [-5.4, 5.4]$ to `2.33e-36`, and `+1` (`7.07e-37`) for $k \in \{3, 4\}$.
  - Upgrades `B1678/verification/main_check/s5_theta.py` to explicit quarter-nome `analytic_jtheta` ($w = e^{i\pi\tau/4}$), passing quasi-periodicity to `< 1e-30` at planted controls $\tau = 0.6 + 1.1i$ ($\operatorname{Re}(2\tau) = 1.2 > 1$) and $\tau = 1.3 + 1.1i$ ($\operatorname{Re}(2\tau) = 2.6 > 1$) where naive `mp.jtheta(2, u, q)` jumps sheet. Hash-pinned `B1821/cm_zero_line.py` stays untouched per `P-670`.

---

## Seen first

- **Swept:** `VERDICT topic-sweep /planted.violations|seal.order|retraction.sweep|jtheta|P-670|P-772|P-757/ (full text): 44 of 1625 arcs on main match (NEGATIVE 3, PROVED 41); 8 register rows match (DONE 5, QUEUED 3)`. Prior arcs on `main`: `B967` (`retraction-sweep`), `B1461` and `B1464` (gate controls and seal provenance), `B1837` and `B1838` (`P-670` sheet law), and `B1861`–`B1878` (closure programme, first enforcement waves, `artifact-hashes`, `Review 78`, and `arrival-phrases`).
- **Literature:** Whittaker & Watson, *A Course of Modern Analysis*, Ch. XXI, and NIST DLMF §20.2 (`20.2.1`–`20.2.4`) for the Jacobi theta quarter-nome convention $q^{1/4} = e^{i\pi\tau/4}$ vs `mpmath.jtheta`'s principal root `(exp(i*pi*tau))**(1/4)` in `P-670`; the repository enforcement gates, seal-ledger checks, and suite repairs are internal instrument work with no further external literature.
- **Outside inputs:** the advisor seat's `planted_violations.py` (`701d12ff7` and leaf-`PV14` update `6ab743907`), `further_plants.py` (`REAUDIT_2_2026-11-10.md`), and `reaudit3/plants.py` (`REAUDIT_3_2026-11-11.md @ 6ab743907`); per Rule 20 (`B1874`), changes to findings already read by `REAUDIT_2` are recorded in `SINCE_REAUDIT` and left for the seat's re-read.

## Disclosed

- No physical observable, held-out target (`D11` / `P-709`), or Standard Model parameter is touched (`0 of 19`).
- Historical pre-`015be0cc7` ceiling sets (`SEAL_ORDER_UNSHOWN_CEILING`, `SEAL_ORDER_AFTER_CEILING`, `ATTRIBUTION_CEILING`, `ARTIFACT_HASHES_BROKEN_DISK`, `OTHER_HASH_LISTS_BROKEN`, `OTHER_HASH_LISTS_BROKEN_DISK`) freeze pre-existing repository history by explicit key and SHA-256 so new commits cannot add violations or re-edit frozen files.

## Files

- `frontier/B1879_reaudit3_enforcement_and_p670_closure/FINDINGS.md`
- `frontier/B1879_reaudit3_enforcement_and_p670_closure/arc_verdict.json`
- `frontier/B1879_reaudit3_enforcement_and_p670_closure/verification/measure_other_hash_lists.py`
- `frontier/B1879_reaudit3_enforcement_and_p670_closure/verification/other_hash_lists_census.json`
- `frontier/B1879_reaudit3_enforcement_and_p670_closure/verification/p670_variable_order_sweep.py`
- `frontier/B1879_reaudit3_enforcement_and_p670_closure/verification/p670_variable_order_sweep.json`
- `docs/OTHER_HASH_LISTS.md`
- `tests/test_b1879_reaudit3_and_enforcement.py`
