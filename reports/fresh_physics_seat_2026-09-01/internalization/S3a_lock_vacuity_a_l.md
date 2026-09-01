# S3a — LOCK-CODE VACUITY AUDIT, tests/test_[a-l]*.py (digest, 2026-09-01)

Sweep seat digest. I flag; the evaluating seat adjudicates. All paths repo-relative to
`/home/user/origin-axiom`.

## COVERAGE MODULUS (read this first)

Population: **1066 files** match `tests/test_[a-l]*.py`, **~57,279 lines total**. A full
line-by-line read of all 1066 was NOT performed. What was actually done:

- **Full-population static pattern scans over all 1066 files** (ripgrep, patterns listed per
  section below): literal-constant asserts, bare-string asserts, silent except-fallbacks,
  module-level `mp.mp.dps`, ALL-CAPS module-flag asserts, doc-string pins over `.md` files,
  subprocess+stdout string pins, `results.json`/`json.load` cache reads. Pattern scans can miss
  obfuscated instances (e.g. flags not in ALL-CAPS, paths built by concatenation — my literal-path
  regex caught only 22 of the ~201 files that mention `results.json`).
- **Close-read of ~50 files**: a systematic every-35th sample of 31 files (list in §7) plus ~19
  targeted reads of scan hits (b710, b545, b428, b509, b791, b313, b1117, b1120, b598_p0,
  b1009, b1017, b1034, b1036, b1040, b1060 header, b1144, b1176, cc2_r5_adopted, e21,
  instrument_freshness, block_vacuity, flagship).
- **Cross-read of the enforcement layer**: `tests/conftest.py`, `scripts/checks/check_test_vacuity.py`,
  `scripts/checks/instrument_freshness.py`, `scripts/gates/gates.py:515-541` (`gate_test_vacuity`),
  `docs/ERROR_LEDGER.md` rows E12/E27/E40/E52/E53.
- **Spot-executions** (small, per remit): `pytest tests/test_b1117_adelic.py tests/test_b1120_L180.py`
  (5 passed); two standalone mpmath bite probes; one dps-15 reproduction.
- **NOT done**: the full suite; reading the ~1016 files outside the sample/hits line-by-line;
  executing any frontier `verify.py`/`compute.py`; mutation-testing any cache. Frontier modules
  were only opened where a lock's assert traced into them (B281, B279, B289, B313, B278, B244,
  B104, B384-dir listing).

## 1. E27 — verdicts wired to constants

### 1a. THE BIG ONE: ~60 lock files assert hand-written literal `True` flags from frontier modules

Scan: `assert <mod>.<ALL_CAPS_NAME>` with no comparison operator → **60 files** (full list at end
of §1a). Concentrated in the B252–B325 stratum (2026-06 era) plus test_audit_sample, b452, b807,
b811, b822, b977. Three spot-checks confirm the flags are **literals with comments, not computed**:

- `frontier/B281_crux_scoping/crux_verdict.py:8` — `EVERY_TYPE_GIVES_RANK = True  # ...`
  asserted at `tests/test_b281_crux_scoping.py:15`.
- `frontier/B279_spin_structure_bit/spin_bit_verdict.py:11` — `HOMOLOGICAL_ACTION_TRIVIAL = True`
  asserted at `tests/test_b279_spin_structure_bit.py:19`.
- `frontier/B289_cp_sign_law/verdict.py:32` — `HANDEDNESS_IS_GALOIS_CONJUGATION = True`
  asserted at `tests/test_b289_cp_sign_law.py:30`.
- Worked example: `tests/test_b313_fibonacci_bridge_and_no_forced_choice.py:23,27,31-37` asserts
  EIGHT such flags (`frontier/B313_.../fibonacci_bridge_and_no_forced_choice.py:66-68` shows
  `BRIDGE_IS_GENERIC = True` etc.), and its `verdict()` (line 81) is an AND over the same literals.
  `test_bridge_generic_object_part_is_b261` (line 26-27) contains NO computed assert at all.

This is exactly the CL-LATIN "hardcoded T3/T4 booleans" mechanism from the E27 ledger row, one
level of indirection down (the literal lives in the imported module, not the test body). Caveats
for the adjudicator: (i) most of these files ALSO contain genuinely computed asserts — the flag
asserts are the vacuous fraction, not the whole file; (ii) some ALL-CAPS asserts may trace to
computed module values (I spot-checked 3 of 60 modules; all 3 were literals); (iii) many of these
flags encode ADJUDICATION statements ("DERIVES_SM_VALUES is False") for which a constant may be
the honest representation of a sealed reading — but then they are records, not locks, and the
repo's own E53 row #8 says such a cell "must never be re-run as one".

**Bite test**: flip `EVERY_TYPE_GIVES_RANK` to `False` in crux_verdict.py — the suite should go
red via the lock. It will (the assert is wired to the file), but flip the underlying MATH (edit
the computation the comment cites, where one exists) and nothing moves: the flag is not wired to
any computed quantity. The mutation harness of the 2026-07-25 E27 sweep (aggregate-json mutation)
structurally cannot see this class, and that sweep's "0 genuine E27 remaining" claim was scoped to
"the session's lock layer" (B7xx era) — it never covered B252–B325.

**The instrument is blind to this class**: `scripts/checks/check_test_vacuity.py` (enforced at
`scripts/gates/gates.py:515` for NO-ASSERT/TAUTOLOGY only) scans the TEST file's AST; a literal in
an imported frontier module appears as an attribute access, not a literal, so all 60 files pass the
vacuity gate. BOTH-LITERAL is report-only by design.

Files (60): test_audit_sample, b252, b253, b257, b258, b262, b263, b271, b273, b275, b276, b279,
b281, b284, b285, b286, b287, b288, b289, b290, b291, b292, b293, b294, b295, b296, b298, b299,
b300, b301, b302, b303, b304, b305, b306, b307, b308, b309, b310, b311, b312, b313, b314, b315,
b316, b317, b318, b319, b320, b321, b322, b323, b324, b325, b351, b452, b807, b811, b822, b977.
(b811's is a seal-pin against hand-copied thresholds — arguably legitimate tamper detection.)

### 1b. Literal-arithmetic tautology asserts (small, mostly the documented "data-lock" category)

Scan `^\s*assert (True|1)\b` → 18 hits, most inside real computed tests. Standouts:

- `tests/test_b710_thimbles.py:26` — `def test_orbit_counts_differ(): assert 1 != 2`. The ENTIRE
  test is a tautology; the docstring claims it locks "mod-conjugation orbit count 1 (fig-8) vs 2
  (FRW)" but neither count is computed. Bite: no edit anywhere can fail this test. Pure E27.
- `tests/test_b710_thimbles.py:23` — `assert all(...) or any(...)`: the `or any` clause makes the
  documented claim ("all off the real axis") unenforced — if 3 of 4 roots were real the assert
  still passes. Semi-vacuous disjunction.
- `tests/test_b545.py:6` — `def test_c1_class_on_level(): assert 1*1 + 0 + 0 - 0 == 1`. Whole
  test tautological (file's other two tests compute genuinely via sympy).
- `tests/test_b509.py:26` — `assert 148176*5 != 55296*25`: the j-invariants are hand-typed
  literals; "NOT quadratic twists" is decided by transcription, nothing recomputes j.
- `tests/test_b791_weyl.py:24` — `assert 1 + 5 + 6 == 12` is labeled "THE load-bearing step" but
  is a constant; the adjacent line 25 (12·W vs Vol/6π², 1e-25) is the real lock. Label overstates.
- `tests/test_b428_spin_walls.py:29-37` — a block of pure dimension-arithmetic identities
  (52+26==78 etc.). This is the checker's documented deliberate-data-lock category; note the
  precedent that test_b780_gate's universal identity was DEMOTED to a comment — these were not.

### 1c. Silent except-fallbacks

Scan `except ...:` + `pass/continue` → 4 sites, all read and all defensible-to-mild:
- `tests/test_b1009_verification.py:43,69` — `except (OSError, ValueError): continue` inside a
  negative scan over all `frontier/*/arc_verdict.json`. Mild: if the jsons became systematically
  unreadable the negative lock (`assert not hits`) would pass vacuously. Not a constant verdict,
  but a fail-open scan.
- `tests/test_cc2_r5_adopted.py:260` — `except FileNotFoundError: pass` over 6 data files, but
  guarded by `len(primes_1215) >= 3` and every `report()` asserts (line 45). Wired.
- `tests/test_e21_group_naming_guard.py:37` — skip unreadable files in a repo scan. Benign.

## 2. E40 — locks over committed caches nothing re-runs

Numbers first (all computed this sweep, full population):

- **201 of 1066** a-l lock files mention `results.json`; **372** call `json.load`.
- **119** `frontier/B*` dirs carry a committed `results.json`; **only 2** (B943, B946) also carry
  a file literally named `verify.py`.
- `scripts/checks/instrument_freshness.py:instruments()` discovers instruments by the EXACT
  filename `verify.py` → **the freshness sweep covers 2 of 119 cached-results arcs**.
- At least **7 more** arcs have verify-style instruments under other names, invisible to the sweep:
  B791 (`verify_bank_structure.py`), B794 (`verify_congruence.py`), B848 (`verify_handoff.py`),
  B875, B878, B879, B907 — plus newer arcs using `bNNNN_verify.py` (B1107 `b1107_verify.py`,
  B1120 `b1120_verify.py`, B1122 `b1122_verify.py`).
- **22 lock-read cache jsons** (literal-path scan; undercount, see coverage) live in arcs with no
  sweep-visible instrument; three of those arcs contain **no .py at all** next to the cache:
  `frontier/B1099_route_a_counter/` (read by test_b1099_route_a_counter and 9 other lock files),
  `frontier/B1108_c5_archimedean/`, `frontier/B738_pathfinder_compiler/kill_graph.json`.

Red flag on the enforcement layer itself: `tests/test_instrument_freshness.py` (in this sweep's
range) says *"main has 2 cache-shape instruments today; the sweep discovers them, so growth is
covered"* — **false for the corpus's actual naming conventions**; growth has NOT been covered
(every post-B946 arc names its instrument `bNNNN_verify.py` or `verify_*.py` and is skipped). Its
non-vacuity companion (`test_the_sweep_is_not_vacuous`) only asserts the output does not say
"0 instruments", which 2-of-119 satisfies. This is the same shape as the E53 row's doc_currency
finding (a staleness detector green at 11% coverage), now at the lock layer.

Representative pure cache-read locks (lock reads flags/values; suite re-runs nothing):
- `tests/test_b420_tw6.py:5-6` — asserts `R["entropy_eq_4Reg"] is True` etc. straight from
  `track_lfunctions.json`. Verdict-flag-over-cache, the exact B1054 shape.
- `tests/test_b384_kashaev.py` — all four tests read `kashaev.json` fields; the generators
  (`kashaev_smalls.py` etc.) exist in-dir but nothing re-runs them.
- `tests/test_b1112_projective_hatch.py` — all asserts over `parity_sweep.json`
  (`parity_sweep.py` un-re-run); honest cross-link to independently-locked B1100 noted.
- `tests/test_b886_matter_pencil.py` — structure asserts over results_stage1/2.json.
- `tests/test_b1120_L180.py:29-30` — `r["verdict"] == "EULER-STRUCTURE-CONFIRMED"` and
  `precision_sufficient_by_k` flags read from cache (lines 21-27 do recompute the closed forms
  against cached best_values — hybrid).
Hybrids that read caches but compute over the values (defensible, still cache-anchored): b663,
b771 (explicitly documents the split), b958, b1208, b1009.

**Bite test for the class**: corrupt one non-verdict value in any of the above jsons (e.g. flip
`"sqrt5_part"` for N=5 in kashaev.json) — the lock goes red (they are wired to the cache, per the
2026-07-25 mutation sweep's sense). But edit what the INSTRUMENT measures and re-run nothing —
no surface moves. That second bite is E40's definition, and for 117/119 arcs no committed
machinery performs it.

## 3. E12 — module-level precision, with a demonstrated weakening

- `tests/test_b1117_adelic.py:6` (`mp.mp.dps = 40`) and `tests/test_b1120_L180.py:7`
  (`mp.mp.dps = 50`): module-level assignments with **no per-file autouse fixture** (grep
  confirms none), unlike the ~18 repaired files using the `_saved_dps` + fixture pattern
  (b204, b246, b250, ..., b598_p0 is the model repair). `tests/conftest.py`'s
  `pytest_collection_finish` restores entry precision after collection — so these two modules'
  intended precision NEVER APPLIES AT RUNTIME. They no longer leak (the guard works); instead
  they silently run at dps 15.
- **Demonstrated bite** (spot-executed): at dps 15, B1117's anchor-B assert computes
  `abs(vol_pred - vol_true) == 0.0` (both operands round to the same 15-digit value), so the
  stated 1e-25 tolerance is theater; a vol_true corrupted in its 17th significant digit STILL
  PASSES at dps 15 and correctly FAILS at dps 40. The lock certifies ~15 digits while its
  docstring claims "to 1e-25". `pytest tests/test_b1117_adelic.py tests/test_b1120_L180.py`
  → 5 passed, consistent with runtime dps 15.
- b1120's 1e-15 tolerances (lines 21,23) sit at the edge of dps-15 representability — passing,
  but with no precision margin and its cached `best_value` strings truncated on conversion.
- These are the only 2 unrepaired module-level dps files found in the a-l range (scan:
  column-0 `mp.mp.dps =` without `_saved_dps` context).

## 4. E6 — output-string asserts

- **58 files** in range run a subprocess/script and assert exact stdout lines (e.g.
  `tests/test_b459.py` — six pinned lines like `"Law 2 (...): PASS"`;
  `tests/test_b565_triality.py:14-15`, `test_b598_step7.py:36-38`, `test_b604_rosetta.py:32`,
  `test_b605_door2.py:35-36`, `test_b612_pairing_chirality.py:20`, `test_b620_conductor_mechanism.py:16-24`).
  These DO recompute fresh (unlike E40) but lock the print format, not the quantities: a script
  edit that reworded a line while breaking the math's meaning, or that computed the right number
  and printed a stale label, is invisible. Lower severity than 1a/2; listed for the base rate.
- Variant: `tests/test_b1036_mirror_double.py:15` asserts the string `"V1 CONTROL FAILED -- HALT"`
  is present in a script's SOURCE (`b1036_final.py`) — that the gate text exists, not that the
  gate runs.

## 5. String-pins of counts/statuses (E53 sub-mechanism)

The E53 ledger row (Review 53) names the exact mechanism: "a lock pinning a count or status must
also pin what DECIDES it". Live instances found in range:

- **`tests/test_b1017_recount.py:30-32`** — pins `"five typed external data"` AND `"is open"`
  (the fold-into-ℝ⁺ question) as literal strings in `docs/THE_CLAIM.md` (which still carries
  both, line 11/15). Against the live board this is the highest-tension pin in the range:
  B1230 C-1 rules every continuous-parameter count must state its field (σ over-counted), B1231
  makes counts LOWER BOUNDS, and B1232 re-types the observer inputs into THREE columns and
  resolves C-2 to OUTCOME A. If/when THE_CLAIM's five-count or the open-status is corrected to
  the B1230–B1232 typing, THIS LOCK FAILS THE CORRECTOR — the "ten genuine open nodes" mechanism
  verbatim. I do not adjudicate whether the five-count is already stale; I flag that the pin is a
  string, not a fact-plus-decider.
- `tests/test_b1040_battery.py:14` — pins `"ω-essential steps = 0 of 11 decidable"` (a count
  string in the arc's own ledger.md), plus a sha256 seal pin (line 9, legitimate).
- `tests/test_b1032_type_law.py:50` (`"unopened"`), `tests/test_b1034_l154.py:105`
  (`"NOT derived"`), `tests/test_b1013_wall_resort.py:25` (`"DISCHARGED 2026-08-10"`),
  `tests/test_b1144_adoption_audit.py` (six correction-string pins incl.
  `verdict == "PROVED"` from arc_verdict.json), `tests/test_b1176_record_surface_wave.py`
  (portfolio/OPEN_LEADS pins incl. an exact `count(...) == 2`), `tests/test_b1060_digest.py:32`
  (digest row pins). Status-pin density is high across the B10xx doc-lock stratum (40+ files
  read `.md` and assert phrases — see the doc-reading list in my scan; I read ~10 of them).
  Note the two-sided variant done RIGHT: test_b1009 pins the withdrawal note present AND scans
  computationally for a fact that would reopen the question.
- Positive control for the adjudicator: the board (B1230) credits `test_b1034_l154.py`'s
  allowlist lock with catching B1229 pairing Brown–Henneaux with (E₆)₁ unstated — read here,
  its v2 lock does scan computationally (regex over the repo with a named allowlist,
  lines 28-40+). String-pin locks CAN bite; the class risk is they bite the corrector, not
  the error.

## 6. Base rate (honest)

Systematic every-35th sample, 31 files, all close-read (§7 list). Classification (a file can
carry more than one character; primary character used):

- **Clean recompute-style** (imports/spawns the computation and asserts mathematics):
  b104, b137, b172, b209, b350, b523, b556_campaign3, b570_c3_level2, b595, b700, b733, b853,
  b918, b1208 → **14/31 (~45%)**.
- **Subprocess-recompute but stdout-string asserts** (E6 form): b459, b620 → 2/31.
- **Hybrid cache+compute**: b663, b771, b958, b1009 → 4/31.
- **Pure cache-read (E40 exposure)**: b384, b420, b886, b1112 → 4/31.
- **Doc/string-pin locks**: b1144, b1176, flagship → 3/31.
- **Literal-flag (E27 class of §1a)**: b313 → 1/31 (population figure is the honest one: 60/1066
  files ≈ 5.6% carry at least one such assert).
- **Data-structure self-consistency / seal-pins (BOTH-LITERAL kin)**: b244, b278, b811 → 3/31.

Extrapolation caution: the sample is by filename order, and the failure classes cluster by era
(literal-flag in B252–B325; doc-pins in B10xx+), so per-class population greps above are more
trustworthy than sample fractions for any single class.

## 7. Sample list (all close-read)

b1009, b104, b1112, b1144, b1176, b1208, b137, b172, b209, b244, b278, b313, b350, b384, b420,
b459, b523, b556_campaign3, b570_c3_level2, b595, b620, b663, b700, b733, b771, b811, b853, b886,
b918, b958, flagship_paper.

## RED FLAGS FOR THE EVALUATING SEAT (ranked)

1. **E40 coverage collapse**: instrument_freshness discovers instruments by exact filename
   `verify.py` → 2/119 cached-results arcs covered; ≥10 differently-named verify scripts
   invisible; `tests/test_instrument_freshness.py`'s own docstring asserts growth is covered.
   The corpus's E40 defence is ~2% deployed while its lock says it is systemic.
2. **60-file literal-flag stratum (E27)**: hand-written `True` flags in frontier modules
   asserted as locks, invisible by construction to check_test_vacuity and to the 2026-07-25
   mutation sweep's scope. The "0 genuine E27 remaining" ledger sentence does not cover it.
3. **test_b1017_recount's "five typed external data" + "is open" string-pins** vs the
   B1230–B1232 re-typing: primed to enforce a stale count exactly as `test_the_road.py` did.
4. **B1117/B1120 precision theater (E12→E27 hybrid)**: module-level dps neutralized by the
   conftest guard; B1117's 1e-25 anchor lock demonstrated (executed) to pass a corrupted
   17th-digit anchor at the dps it actually runs at.
5. **test_b710_thimbles.py:26** `assert 1 != 2` — a fully vacuous named lock
   (test_orbit_counts_differ), plus the line-23 `all(...) or any(...)` weakening; kin
   test_b545.py:6.
