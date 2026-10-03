# B1461 — THE REVIEW FIRES, ITS CARRIED ITEMS AGE, AND EVERY GATE HAS BEEN SEEN TO FAIL

**Verdict: PROVED** (a process arc: four gates, each with a failing-path test; scope: the repository's own review
machinery, frame-independent, reach general for the record). cc (main), 2026-10-03. Pays R58-1's implementation
(the owner's "yes on all" of 2026-10-02) and R58-2; R55-6 paid on the way.

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "review fires|carried a (third|fourth) time|failing-path|gate controls|fresh clone|gate nobody"`: *VERDICT topic-sweep: 3 of 1333 arcs on main match (OPEN 1, PROVED 2)* — B1009 (an earlier verification pass), B1240 (the belt a fresh clone runs) and this arc; B1448 (the review's instrument) was read directly. Then Review 58 (`docs/progress/REVIEWS.md` §9 and its action block) for the three decisions and their reasons;
  `scripts/gates/gates.py` (`review_status`, `_carry_leaks`, `gate_review_actions`, the GATES table) and
  `scripts/review/review_tools.py` (B1448: `action_loop`, `gate_controls`, `sample_draw` already existed — the tooling
  half was built; the enforcement half was not); `scripts/checks/relay_debt.py` and `lead_debt.py` for the frozen-baseline
  ratchet and the env clock seam (the shapes copied here); `scripts/checks/reproduce_belt.py` (B1240) for the belt the
  fresh clone runs; `docs/atlas/BLIND_ARCS.md` for the triage-register shape `tests/GATE_CONTROLS.json` follows. The
  measurement before writing: by a text proxy 18 of 36 gates had no failing-path test, 13 were named by no test at all;
  by hand 7 more of the "named" ones had no real failing path (framing, claims, atlas-fresh, arc-verdicts, attribution,
  theorem-registry, retraction-debt). **Literature:** none; this is the repository's own governance.

## 1. What was built

| decision (R58-1) | gate | failing path proved by |
|---|---|---|
| 1. the review fires at 40 merges unless the owner waives it by date | `review-fires` (`REVIEW_HARD = 40`; `docs/progress/REVIEW_WAIVER.md`, grammar `- waived <date> by the owner through <N> merges: <reason>`; `OA_REVIEW_MERGES` seam) | `test_b1461_governance_delta.py::test_review_fires_past_twice_the_period_unless_waived` (fails at 40; passes waived; fails when the waiver's reach is spent) |
| 2. carried items age at the third carry | `carry-age` (`carry_age_problems`; a `[>]` at count ≥ 3 must carry "declined" with a reason or "waived by the owner"; the fifteen keys past the limit today are `CARRY_BASELINE`, exempt at Review 58 only) | `::test_carry_age_fails_on_a_third_carry_without_disposition` (a planted three-review register) |
| 3a. every gate has a test that makes it fail | `gate-controls` (`tests/GATE_CONTROLS.json`, 40 entries; the gate checks completeness and that every named function exists) | `::test_gate_controls_fails_on_an_unregistered_gate_and_a_missing_function` |
| 3b. a fresh-clone reproduction; 3c. the sample drawn by seed | `review-core` (from Review 59 the entry must carry `fresh-clone:`, `sample seed:`, `gate controls:`); `review_tools.fresh_clone` (clone, `gates.py`, `reproduce_belt.py`; `--fresh-clone`); `render` prints the three lines | `::test_review_core_fails_on_an_entry_without_its_three_lines`; `::test_review_tools_render_carries_the_core_lines` |

**The failing-path tests (R58-2):** `tests/test_gate_failing_paths.py`, 25 tests — the twelve R58-2 named (append-only,
chain-locks, firewall-oneway, id-collisions, knowledge-index, law-map-provenance, lawmap-scope, path-refs,
practices-register, seal-provenance, views-fresh, views-generated) and thirteen more (test-vacuity, seal-digests,
retraction-sweep, representation-sweep, seen-first, genesis-cited, framing, claims, atlas-fresh, arc-verdicts,
attribution, theorem-registry, retraction-debt). Each plants a bad input through the gate's own seams (`gates._read`,
`gates.ROOT`, `gates._git`, a checker's `ROOT` inside a throwaway git index) and asserts the gate returns false; the
other fifteen gates' existing failing-path tests are registered by name. Three plants were wrong on first draft and
the gate said so (a five-digit arc id the regex does not read; a checker that reads git's index, not the disk; a
roll-up branch I had not planned for) — recorded, not hidden.

**The fresh clone, run once on HEAD `5c0951b7`:** gates all PASS, belt ok. Its first run returned
`NameError: name 'os' is not defined` — the instrument's own missing import, caught by the instrument.

## 2. What it changes

GOVERNANCE §15 amended (additive; no rule weakened); four PRACTICES sections; `review_tools.render` carries the three
core lines; R58-1 implementation recorded, R58-2 paid, R58-4 updated with B1453/B1457's numbers, R55-6 paid (the
H-CUSP status column now says what its body says). **Due at Review 59, by the rule now on:** R55-1, R55-2, R55-4,
R55-7, R55-9, R55-12, R55-13, R55-14, R55-15, R56-1, R56-3 — each resolved, declined with its reason, or waived by
the owner. The counter stands at 16 merges; the review is due at 20 and fires at 40.

## 3. Errors in this arc

The missing import above; three test plants wrong on first draft. And the arc itself is a day late: the decisions were
taken on 2026-10-02 and three computation arcs ran before the owner asked how the review had gone.
