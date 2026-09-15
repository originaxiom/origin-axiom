# memo_217 — THE_GATE_IS_INSTALLED.md

## 1. HEADLINE
"**THE GATE IS INSTALLED: A CELL'S TWO ARTIFACTS CAN NO LONGER CONTRADICT EACH OTHER SILENTLY.**" Owner-authorized; banked 2026-09-13 per INDEX.md. Memo states "done on `<remote>/outside-bench` as a proposal, main not touched" — this framing is now stale (see §4).

## 2. CLAIMS
1. `scripts/checks/instrument_freshness.py` (B1054, Review 1) already exists and re-runs `verify.py`/`results.json` pairs, but never reads `output.txt` — DOCUMENTARY, cites prior main content correctly.
2. The new gate is the "cheap complementary half": a MISMATCH fires when both artifacts carry a verdict and the text's verdict appears in none of the JSON's; a one-sided verdict is a "formatting gap," reported not failed — graded design specification, not a numeric claim per se.
3. Extraction rule: from `output.txt`, last match of `(FINAL )?VERDICT:\s*(\S+)`; from `results.json`, every string-valued `verdict` key at any depth (nested keys included; `verdict_under_universal_reading`-style keys excluded) — DOCUMENTARY/specification.
4. Census at HEAD: **83 cells** agree on both sides, **22** carry a verdict on one side only (0 contradictions) — graded MEASURED, "the population is larger than memo 212's 75... the extractor improving, not the corpus drifting."
5. `--selftest` (MB12 bite control): 3 must-fire cases, 5 must-be-quiet cases, 4 extractor-format tests, 1 nested-JSON test — all PASS.
6. Historical regression: run against three REAL contradictions as they stood at the commit before repair (P2W5-L72, W2-270, W4-017r) — **all three fire True** — graded the memo's strongest verification claim ("the part that matters most... transcribed into the lock so it cannot go vacuous").
7. `tests/test_artifact_pair_gate.py`: 5 tests, 0.38s — graded MEASURED.
8. Explicit fence: does NOT re-run anything (drifted numbers with a held verdict string pass silently — `instrument_freshness`'s job); does NOT fix root cause (results.json/output.txt still written by separate code paths, 113 cells still need harness unification — "main's call"); reads verdict strings not meaning (agreeing `RESOLVED-A` on different underlying resolutions would pass) — graded EXPLICIT LIMITATIONS, not claims of completeness.

## 3. CERTIFICATE
The memo names the artifacts as `scripts/checks/artifact_pair_gate.py` + `tests/test_artifact_pair_gate.py` + output `outside_bench/outputs/artifact_pair_gate.txt`. All three EXIST: `scripts/checks/artifact_pair_gate.py` (163 lines), `tests/test_artifact_pair_gate.py` (73 lines), `outside_bench/outputs/artifact_pair_gate.txt` (16 lines, full file read). The output's final line is "selftest: PASS", and the body shows "artifact-pair-gate: ok (83 cells carry a verdict on both sides and agree; 22 carry one on a single side -- a formatting gap, not a contradiction)" — **agrees exactly** with the memo's census numbers (83/22) and verdict. No seal is claimed for this memo.

## 4. ON MAIN ALREADY?
1. The gate script and its lock — **(a) already on main, directly**: `scripts/checks/artifact_pair_gate.py` and `tests/test_artifact_pair_gate.py` are tracked files in the current repo tree (which is `main`, per the session's git status). `git log --oneline -- scripts/checks/artifact_pair_gate.py` shows commit `8b3f1924` "memo 217 -- install the artifact-pair gate, with a historical regression in its lock" — i.e. this IS a main commit, contradicting the memo's own framing ("main not touched by this bench... as a proposal"). The memo's self-description is now out of date relative to its own subsequent landing.
2. It is referenced in `docs/views/THE_SPINE.md:1489` ("— `test_artifact_pair_gate.py`") alongside `test_instrument_freshness.py` at line 1176 — i.e. it is listed in the spine's test inventory, confirming integration.
3. It is NOT wired into any master gate-runner script found (no `run_all_gates.py` or similar found at repo root referencing it), and it is not found referenced from a pre-commit/pre-push hook in `.git/hooks/` — so it is installed but its enforcement is currently opt-in/manual (`python3 scripts/checks/artifact_pair_gate.py`), same as `instrument_freshness.py` appears to be. This matches the memo's own honest fencing (it does not claim to be wired into CI).
4. `frontier/B1413_the_audit_lanes_r21_r31/verification/readers/DOC_CHIRALITY_REFRESH.md:39-42` independently references `instrument_freshness.py`'s timeout-handling bug (a separate, adjacent finding, not from this memo) — confirms the neighboring instrument is under live audit scrutiny on main, consistent with this gate being a recent, active addition to the same family of checks.

## 5. NEEDS COMPUTATION HERE
1. Discriminating fact: re-run `python3 scripts/checks/artifact_pair_gate.py` at current HEAD and confirm it still reports 0 contradictions (the 83/22 split may have shifted as new arcs have landed since 2026-09-13 — e.g. B1413 and others). Expected: still "ok", counts may have grown but contradictions should remain 0 unless a genuine new artifact-pair mismatch has appeared.
2. Re-run `python3 scripts/checks/artifact_pair_gate.py --selftest` and `pytest tests/test_artifact_pair_gate.py -q` — expected PASS / 5 passed in <1s, per the memo's own numbers. Both are well under the 2-minute compute budget for this harvest.
3. The historical-regression claim (P2W5-L72/W2-270/W4-017r all fire at the pre-repair commit) is DOCUMENTARY in the sense that it's a fixed test fixture already transcribed into the lock (per the memo) — a verifier need only confirm those three cases are present as literal test cases in `tests/test_artifact_pair_gate.py` and pass, rather than re-deriving them from git blobs.

## 6. SUPERSESSION
Not superseded by any later assigned memo. It is the last-numbered memo among the six assigned to this reader (217), and per INDEX.md rows after 217 were not reviewed here (out of scope), but nothing among 191/196/199/202/215 supersedes it. Its own self-description ("main not touched... as a proposal") is superseded by its own subsequent commit to main (8b3f1924) — this is a **stale self-description inside an otherwise-accurate memo**, not a substantive retraction.

## 7. GRADE PROPOSAL
**ALREADY-ON-MAIN.** The gate, its test, and its output are all committed to main and cross-referenced in `docs/views/THE_SPINE.md`. The one thing worth flagging to a verifier: the memo's own text says "main is not touched by this bench... as a proposal," which is no longer true — it should be read as describing the memo's state *at authorization time*, before the same-session commit landed it. Not DISPUTED (no contradiction), just a wording lag between the memo prose and its own outcome.
