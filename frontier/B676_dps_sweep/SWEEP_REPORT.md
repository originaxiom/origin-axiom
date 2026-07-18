# B676 — the module-level-dps sweep (R22-4, the E12 class-wide fix)

**Seat:** R22-4 (sanctioned tracked-file exception, B666-cell-5 precedent).
**Date:** 2026-07-18. **Mechanism repaired:** ERROR_LEDGER E12, collection-time
variant — pytest imports every test module in sorted order before any test
runs, so a module-level `mp.mp.dps` assignment leaks into every later import,
and the LAST one in sorted order becomes the global precision every runtime
test sees (cell 5's b353 localization).

## The transform (per file, two halves)

1. **Import wrap** — `_saved = mp.mp.dps` before the import that executes a
   module-level dps assignment, restore after. Safe because every module that
   computes import-time constants sets its own dps FIRST (verified per file
   below), so the constants are unchanged; only the leak dies.
2. **Per-file autouse fixture** (the b204 pattern) pinning the runtime dps the
   tests need, since after the sweep no test can inherit a useful global.

## Scope note — the list grew beyond cell 5's 12 (tasking anticipated this)

Cell 5's ordered scan records dps TRANSITIONS only: a module that sets the
value already in force is invisible ("masked"). Repairing the visible 12
unmasked 5 more in successive ordered rescans (b246, b265, b353-import,
b357-import, then b250), and an isolated-import rescan (fresh dps per module;
`scratchpad` tool, method recorded below) found the final 2 (b258; b570_c1,
masked in-suite by the e6_tangent_gradings sys.modules cache hit). All are the
same E12 class, so all were repaired under the same sanction. **Final tally:
19 test files + tests/conftest.py.**

## Per-file changes

Original 12 (cell 5's enumeration):

| file | import wrap | fixture | rationale |
|---|---|---|---|
| test_b204_metallic_wrt_period.py | around `from gauss_proof import` (gauss_proof sets 30) | pre-existing `_mp_dps`=25 kept | proof locks already pinned; only the leak repaired |
| test_b261_golden_root_aj.py | around exec_module (golden_root_aj sets 50) | new, 50 | golden_root_sequence computes colored Jones at runtime, rounds to ints |
| test_b264_e6_character_variety.py | around exec_module (module sets 80) | new, 80 | 1e-50 rank tolerances; H1_sym self-guards, adjoint_tangent_dim did not |
| test_b269_t41_rungs_2_3.py | around exec_module (module sets 30) | new, 30 | runtime saddle volume + 1e-25 GEOMETRIC_SHAPE compare |
| test_b270_integrability_cup_product.py | around exec_module (its embedded B264 import sets 80) | new, 80 | calls b264.symn/SVD ranks at runtime |
| test_b276_zeta3_probe.py | around exec_module (module sets 60, then its nested B261 import sets 50 — the module's OWN import-time state was already 50; its entry points self-guard to 60, so no behavior change) | new, 60 | belt on the self-guards |
| test_b347_e6_tangent_gradings.py | around `from e6_tangent_gradings import` (sets 70) | new, 70 | entry points _guard() internally; fixture removes the dependence anyway |
| test_b352_cup_product_obstruction.py | around exec_module (`_guard()` sets 100 at module level) | new, 100 | h1_line/h2_functional cliff asserts at runtime |
| test_b355_weil_layer_independent.py | around `from weil_layer import` (sets 60) | new, 60 | 1e-25/1e-30 runtime comparisons |
| test_b462.py | around the 4-module import block (phi_scan sets 40) | none — every mpmath test already pins its own dps inline (40/30/30), order-independent | deliberate: no redundant fixture |
| test_b598_p0.py | the VOL literal wrapped `saved; dps=30; VOL; restore` (the file's OWN import-time constant) | new, 30 | Kashaev sums at runtime, 1e-25 tolerance |
| test_cc2_r5_adopted.py | `_SAVED_DPS` at top, restored after the final print — all 20 locks run at import; each mpmath section sets its dps inline (80/50/40) BEFORE computing | none — the runtime test only reads PASS | see the LOCK 2 finding below |

Unmasked by the rescans (same class, same transform):

| file | import wrap | fixture | rationale |
|---|---|---|---|
| test_b246_quantum_volume.py | around exec_module (quantum_volume sets 30) | new, 30 | vc_growth/fixedA_volume runtime mpmath |
| test_b250_volume_profile.py | around exec_module (volume_profile sets 30) | new, 30 | volume/CS runtime comparisons |
| test_b258_two_ended_unification.py | around exec_module (two_ended_unification sets 30) | new, 30 | runtime mpmath |
| test_b265_e6_integrability.py | around exec_module (embedded B264 import sets 80) | new, 80 | H2_sym self-guards; fixture removes residual dependence |
| test_b353_geometric_theta_identification.py | around `from geometric_theta import` (sets 100) | pre-existing `_dps_100` (cell 5) kept | only the import leak repaired |
| test_b357_e6_boundary_restriction.py | around `from boundary_restriction import` (sets 60) | pre-existing `_dps_module` kept | only the import leak repaired |
| test_b570_c1.py | around `from e6_tangent_gradings import` (sets 70; cache-hit in full suite, executes in single-file runs) | new, 70 | most tests _guard(); the tautology test did not |

tests/conftest.py: added `pytest_collection_finish` restoring `mp.mp.dps` to
its pre-collection value — the class-wide guard so a FUTURE module-level
assignment cannot silently become the suite-wide runtime precision (it does
not repair such a file's own tests; detector remains the import scan).

No banked lock's tolerance or verdict was changed anywhere. Comments +
save/restore + fixtures only; zero assertion edits.

## The LOCK 2 question (tasking premise corrected)

The tasking said cc2_r5_adopted "self-clobbers, LOCK 2 runs at 40". Verified
empirically (instrumented import recording `mp.mp.dps` at every `report()`
call, entry dps forced to the pre-fix leaked 30): LOCK 1 runs at 30 (exact
Fraction arithmetic, dps-irrelevant), **LOCKs 2–3 at 80** (the section's own
`mp.mp.dps = 80` precedes them), LOCK 4 at 50, LOCKs 5–8 at 50
(integer/sympy/json, dps-irrelevant), LOCK 9 at 40. There is NO self-clobber
of lock precision — each mpmath section sets its dps inline before computing;
the file's only E12 defect was leaking its final 40 out of the import (and,
being last in sorted order, suite-wide). All 20 locks PASS at their intended
precisions; no tolerance touched.

## Verification

1. **Each edited file alone:** all pass — b204 11p/43s, b261 2p, b264 3p,
   b269 3p, b270 2p, b276 3p, b347 6p/51s, b352 3p+1skip, b355 6p/63s,
   b462 7p, b598_p0 2p, cc2 1p, b246 3p, b250 4p, b258+b570_c1 11p,
   b265 3p, b353 3p, b357 2p+1skip (skips = OA_SLOW gates, unchanged).
2. **Ordered import scan (cell 5's instrument):** zero `DPS CHANGE` lines;
   final dps after the full 650-module collection sweep = 15 (= entry).
3. **Isolated-import rescan** (each module imported with dps reset to 15 and
   its newly loaded sys.modules purged, catching masked setters): **0
   module-level dps setters remain.** Method: scratchpad script
   `isolated_scan.py` (session scratchpad; logic described above so it can be
   re-created — candidate for adoption next to cell 5's import_scan.py).
4. **Sorted-prefix victim simulation (the cell 5 pattern):** all 19 repaired
   files + the victims test_b353, test_b357, test_b629 (test_e62's hearing
   locks live there) collected together in sorted order: 81 passed, 2 skipped.
5. **Full suite:** `python3 -m pytest tests/ -q`, tail captured to
   `frontier/B676_dps_sweep/full_suite_log.txt` — result: (see log; recorded
   below when complete).

## Full-suite result

PENDING at report-write time; the run's tail is appended to
full_suite_log.txt. This section is updated from that file.
