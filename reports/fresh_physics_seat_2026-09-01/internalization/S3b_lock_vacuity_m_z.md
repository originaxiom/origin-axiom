# S3b — LOCK-CODE VACUITY AUDIT, tests/test_[m-z]*.py + conftest + scripts/gates (digest, 2026-09-01)

Sweep seat digest. I flag; the evaluating seat adjudicates. All paths repo-relative to
`/home/user/origin-axiom`.

## COVERAGE MODULUS (read this first)

Population: **51 files** match `tests/test_[m-z]*.py` (~4,400 lines), plus `tests/conftest.py`
(53 lines) and `scripts/gates/gates.py` (1,106 lines). Unlike S3a's 1066-file range, this range is
small enough that **every one of the 53 files was close-read line-by-line in full**. Supplementary:

- **Frontier modules opened where a lock's verdict traced into them**: `frontier/physics_probes/
  metallic_spectra.py` (flag provenance), `frontier/B48_sl3_metallic_trace_maps/probe.py`
  (read lines 1–250 as the representative of the seven B48–B60 `probe.run_checks()` locks; the
  other six probes were NOT opened — pattern inferred from B48, stated as such below).
- **Spot-executions**: `pytest tests/test_w2_molien_cell.py tests/test_r28_10_stabilizations.py::
  TestTombL310` (4 passed); `scripts/checks/check_test_vacuity.py` run over the whole suite
  (4,662 tests: 0 NO-ASSERT, 0 TAUTOLOGY, 86 BOTH-LITERAL); a small script verifying the three
  wave-lock jsons all trivially contain `"0"`; flat-text check of `docs/THE_ROAD.md` phrase pins.
- **Cross-reads for board currency**: `docs/CAMPAIGN_STATUS.md` top 5 entries (B1228–B1232),
  `docs/THE_ROAD.md` (grep-level, not full), S3a digest (for continuity of E-code framing).
- **NOT done**: running the full suite; executing the snappy-dependent locks (snappy availability
  not tested); opening B49/B51/B52/B58/B59/B60 probes, `frontier/B765_p3_depth/compute.py`,
  `frontier/B932_chain_selection/chain_select.py`, or the B674 w2 cell generator; mutation-testing
  any cache; reading `scripts/checks/check_test_vacuity.py`'s own source (behavior inferred from
  its scan output only).

## 1. E27 — verdicts wired to constants / tautologies

**The a-l range's dominant class (hand-written `True` flags in frontier modules) is ABSENT here**:
a pattern scan for bare `assert <mod>.<ALLCAPS>` finds zero hits in m-z, and the two dict-flag
locks I traced (`test_metallic_spectra.py:25,30-31` asserting `g["confirmed"] is True` etc.)
resolve to genuinely computed values (`metallic_spectra.py:99` computes `confirmed: hits >= 4`;
`:127-139` computes all three distinctness flags). The m-z stratum is a different era and it shows.

What IS here:

- **`tests/test_w2_molien_cell.py:22`** — `assert sp.expand(1/(2 - phi) - phi**2) != 0 or True`.
  Vacuous by construction: the `or True` makes the assert unfailable. (Line 23 then does the real
  two-branch check, so the identity IS locked one line later — but line 22 is a dead assert
  wearing a lock's clothes, and the enforced vacuity gate does not see it; see §5.)
- **`tests/test_r28_10_stabilizations.py:95-104`** (`test_golden_seed_eigenvalues_rank1`) — the
  entire eigenvalue-field check ends `... ) or True  # eigenvalues are in Q(sqrt5)`. The whole
  test is unfailable. The file's own header (line 3) says "Recompute mathematics in-test; never
  read artifacts" — this one recomputes and then discards the answer.
- **`tests/test_r28_10_stabilizations.py:126-131`** (`TestTombL310.test_drift_decelerates`) —
  `drifts = [0.62, 0.58, 0.35, 0.31]` is a hand-typed literal list; the lock asserts a
  transcription is monotone. No drift is computed anywhere in the file. Pure E27 (the CL-LATIN
  shape with the constant inline rather than imported). Spot-executed: passes, and no edit to any
  computation anywhere can fail it.
- **`tests/test_qp3_integration.py`** — subtler and worth the adjudicator's attention because it
  is a physics-facing lock (theta-sector coupling, the 15/32 fraction). Line 32
  (`assert complex(-1).imag == 0`) is a literal tautology whose docstring claims it checks
  "d(tr AB)/du = -1"; the derivative is asserted in a comment, never computed. The same pattern
  runs through the file: lines 37, 44, 51-58, 71 all hand-transcribe closed-form derivatives
  (`deriv = -2 * (2 - w)`, `4 * w**3 + 8 * w`, the seven-word list) and then verify arithmetic
  ON the transcription. The load-bearing step — that these ARE the derivatives of the Sym^2
  trace maps of the actual Riley matrices — is cited from comments, not differentiated in-test.
  Contrast `test_adjoint_off_block` (lines 77-91) and `test_theta_fixed_locus_zero`, which DO
  build Ad_B from matrices; and `tests/test_qp4_closure.py`, which builds its weld block from
  `frontier/B238_su32_levelrank/su32_wrt.py` live — the repair pattern exists in the same wave.
  Bite: corrupt the trace-map algebra upstream and `test_coupling_fraction` still passes;
  the 15/32 lock certifies the transcription, not the map.
- Literal-arithmetic data-locks (the checker's documented deliberate category, listed for base
  rate): `tests/test_wave_b931_b933.py:12-14` (lc == 2304^2·5^2·7^3·11 over a hand-typed lc);
  `tests/test_sweep2_facts.py:23` (`ours = {1: 2, 2: 8, 3: 32}` hand-typed census data checked
  against a formula — the formula side is real, the data side is transcription);
  `tests/test_t2_golden_cm.py:8` (the H_-48 Hilbert polynomial is a "banked" literal the whole
  resultant computation hinges on — cited, not recomputed).

## 2. E40 — locks over committed caches nothing re-runs

Only **2 of 51** files are pure cache-read locks (vs the a-l range's much larger exposure):

- **`tests/test_p3_depth_exposure.py`** — all 13 tests read `frontier/B765_p3_depth/results.json`
  plus the B742 stageA jsons. The arc ships `compute.py`, but nothing re-runs it. The
  partition/consistency tests (lines 34-37, 99-109) are cross-cache arithmetic — wired to the
  cache, blind to the mathematics. Counts pinned: 21/8/6/7 and the exact 7-member exposed set
  (line 95). Note `P3_depth_exposure` is also the one BY-NAME grandfathered entry in
  `gates.py:187` (verdict convention) — this arc is doubly exempted, once per layer.
- **`tests/test_wave_b931_b933.py`** — three arcs' `results.json` read; `chain_select.py` et al.
  un-re-run. Worse, the asserts are substring membership over `json.dumps` of the whole file,
  with disjunctions that collapse: **line 28** — `assert "singlet" in t.lower() or "no lepton"
  in t.lower() or "0" in t` — I verified all three jsons trivially contain `"0"` (they contain
  numbers), so the documented claim "no color singlets in the conformal 27" is UNENFORCED; the
  assert cannot fail on any json that contains a zero digit. Line 20's
  `("1/2" in t or "one-half" in t or "degener" in t.lower())` is the same disjunction-weakening
  shape, one notch less degenerate. This is E40 (cache) compounded with E27 (vacuous clause).

Hybrid/OK: `test_w2_molien_cell.py` checks five artifact files EXIST plus `"LOCKED"`/`"2/5"`
strings in status docs (presence-pin, not content lock) — the actual identities are computed at
lines 23-28. `test_verdict_body_agreement.py` reads every B1060+ `arc_verdict.json` but as gate
SUBJECT (a scan), with an explicit MB12 non-vacuity floor (line 36-39) — the healthy shape.
One mild fail-open there: the DIVERGENT regex (line 15) has `re.M` but not `re.S`, so a FINDINGS
whose "## Verdict" heading and its STALLED word sit on different lines is invisible to the scan.

## 3. E12 — precision

**Clean in this range.** No module-level `mp.mp.dps` in any m-z file; the two assignments
(`test_snapdata.py:29`, `test_w3_support_stop.py:12`) are function-scoped and restored by
`tests/conftest.py`'s autouse fixture (read in full: the collection-time guard at lines 42-46 and
the per-test save/restore at 49-53 are both present and coherent). The a-l B1117/B1120 neutralized-
dps failure has no m-z counterpart.

One skip-shape flag: `tests/test_r28_10_stabilizations.py:47-50` decorates with
`@pytest.mark.skipif(not pytest.importorskip("snappy", ...), ...)` — `importorskip` called at
class-body evaluation raises `Skipped` at module IMPORT if snappy is absent, which would skip the
ENTIRE module (Binet, torsion, functoriality — locks with no snappy dependency), not just the one
snappy test. On a snappy-less runner the R28-10 prereg locks silently vanish from the suite. I did
not execute a snappy-less run to confirm; flagged as PLAUSIBLE, mechanism from pytest semantics.

## 4. E6 / string-pins of counts and statuses (E53 sub-mechanism)

The m-z doc-lock stratum is large (9 of 51 files) but notably better-armed than the a-l one:
`test_paper_citations.py` and `test_paper_provenance.py` carry planted-defect selftests (MB12);
`test_relay_debt_gate.py` proves its checker's failure path against the real ledger at a
far-future date (line 75-81); `test_review_carry_gate.py` unit-tests the gate on synthetic leaks.
These are the repaired pattern and useful positive controls for the adjudicator.

Live string-pin exposures:

- **`tests/test_the_road.py:39`** pins `"nine genuine open nodes (one carrying"` — currently
  matches THE_ROAD (verified flat-joined). The test's own comment records the B1218 lesson: the
  previous "ten" pin HELD THE STALE COUNT IN PLACE, and the repair added a fact-shaped L175 check
  (lines 40-42). The repair is real, but the count itself is still a string-pin, and the live
  board's B1231 rule ("the parameter count is a LOWER BOUND"; counts must state what decides
  them) makes any future legitimate count change fail the corrector again. Same mechanism as
  S3a's test_b1017 flag, one repair-generation later.
- **`tests/test_stale_absence_lock.py`** — the range's largest pin battery (~45 anchors + 16
  currency-stamp floors + 6 forbidden phrases). Direction matters: pinning CORRECTIONS landed and
  OVERCLAIMS dead (lines 99-138) is the right-way-round use of this mechanism. The risky half is
  `STAMP_COUNTS` (lines 32-44) + `test_total_stamp_floor`: it requires >= 16 copies of the exact
  string "stamp 2026-08-19: still CURRENT as of B1082" to survive **forever**. The board is now
  ~150 arcs past B1082 (B1216-B1232 era). If any of those 16 stamped absences has since been
  overtaken, the honest fix (replace the stamp with an OVERTAKEN note) REMOVES a counted stamp
  and fails `test_currency_stamps_survive` — the lock would fight the corrector. I did not
  adjudicate whether any of the 16 is in fact stale; the structure is the flag.
- **`tests/test_sl4_dehn_filling_paper.py:46`** — `assert "for all $n$" not in body or "no" in
  low`: `low` is the lower-cased full text of every .tex/.md/.py/.bib in the paper dir, which
  contains "no" with probability 1 (e.g. inside "not", "novelty" — and line 48 requires
  "specialist" so "no" is guaranteed). The documented guard ("the family is NOT claimed for all
  n") is therefore vacuous; the over-claim it exists to block could return silently. Lines 45/48
  (`"open" in low`, `"specialist" in low`) are near-vacuous for any long document. The honest
  parts of the file (WITHDRAWN-banner-style framing pins, figure existence, AI-label scan) work.
- Moderate/low: `test_masterplan_v3.py`, `test_roadmap_register.py` (plan-text pins — governance
  records, not physics locks; both pin binding-order by index arithmetic, which is at least
  fact-shaped); `test_pc12_draft_skeleton.py` (skeleton headings); `test_p5_draft.py` /
  `test_p5_phase3.py` (withdrawal guards — pins pointed the RIGHT way, guarding a retraction
  against un-retraction, plus genuinely computed hopf/vacuity-repair checks at
  test_p5_phase3.py:37-58; the range's best example of a records-lock done properly);
  `test_w2_step3_kill.py:11-13` ("KILLED-AT-(iii)" status pin beside real sympy arithmetic).

## 5. The enforcement layer is blind to every §1 instance (measured, not asserted)

Ran `scripts/checks/check_test_vacuity.py` over the suite: **4,662 tests, 0 NO-ASSERT,
0 TAUTOLOGY, 86 BOTH-LITERAL**. So: the two `or True` asserts (§1), the `assert complex(-1).imag
== 0` tautology, and the `or "0" in t` collapse are ALL invisible to the enforced classes — a
BoolOp containing a `True` operand is evidently not classified as TAUTOLOGY, and substring-over-
json disjunctions are structurally out of scope. In m-z the report-only BOTH-LITERAL class
catches exactly two sites (`test_wave_b931_b933.py:12`, `test_sweep2_facts.py:14`), both of the
deliberate-data-lock species. Conclusion for the adjudicator: `gate_test_vacuity`'s green
"0 vacuous" line certifies the two hard classes only; every live m-z finding sits in its blind
spot, consistent with S3a's finding that the instrument cannot see indirection or disjunction.

## 6. gates.py — per-gate exemption/allowlist audit (the B982 question: does each entry name
its discharging document?)

Read in full (1,106 lines). Overall shape is strong: most gates carry inline provenance by arc/
review number, several are deliberately FAIL-CLOSED with the near-miss documented in place
(`gate_path_refs:499-506`, `gate_test_vacuity:532`, `gate_review_actions:336-340`,
`gate_views_fresh:388-392`, `gate_knowledge_index:461-466`, `gate_id_collisions:428-431`,
`gate_retraction_sweep`, `gate_representation_sweep`), and `gate_identification_register`
(lines 989-1046) is current with the live board (B1231's ratchet, B1225 typing). Entry-by-entry
on the B982 criterion:

| Gate | Exemption/allowlist | Discharge named? |
|---|---|---|
| framing (`FRAMING_EXEMPT`, :48) | FAILURE_ATLAS.md | YES inline ("quotes what it bans") |
| framing | GOVERNANCE.md, gates.py, test_repo_gates.py | **NO** — self-evident-ish but no doc |
| framing (`FRAMING_SCOPE_DIRS`, :50) | scope excludes `tests/` entirely | **NO** — undocumented scope hole: a banned phrase in a test docstring is invisible |
| arc-verdicts (`VERDICT_GRANDFATHERED`, :182-188) | 14 entries | **PARTIAL** — blanket "frozen constants per GOVERNANCE house rule; additions require a logged amendment"; only `P3_depth_exposure` carries a per-entry note; the other 13 name no document |
| attribution (`_ATTR_BASELINE`, :219) | per-file frozen counts | **YES** — `docs/ATTRIBUTION_BASELINE.json`, B1226 ratchet documented |
| attribution (`ATTR_EXEMPT_PREFIXES`, :226) | B742 reviews/ | YES inline (hash-pinned seals) |
| attribution | `legacy/`, `.claude/`, `audit/` | **NO** document named |
| attribution (`ATTR_EXEMPT_FILES`, :230) | 3 scanner tests | rationale inline, no doc |
| tracked-forbidden (`GRANDFATHERED_RELAYS`, :270) | 1 relay file | **PARTIAL** — GOVERNANCE §12 cited as the reason it can't be removed; no ruling doc for the specific file |
| id-collisions (`GRANDFATHERED_IDS`, :418) | `{"B58"}` | **PARTIAL/CONFUSING** — the comment block (:412-417) names FIVE historical collision groups (B788, B793, B372, L108, B569-B574) but the frozen set holds only B58; a reader cannot tell from this file whether the other four were renumbered (discharged where?) or are silently passing. No per-entry ruling document. |
| log-changelog-paired (:628-630) | dir excludes incl. **`"veins"`** | **NO** — `legacy` gets a justification sentence; `veins` gets NOTHING, anywhere in the file. The one fully naked allowlist entry in the module. |
| append-only (:125-129) | quarterly roll-up exception | YES — GOVERNANCE §9, and the exception is VERIFIED (removed prefix must appear verbatim in archive) rather than trusted |
| seal-provenance (`SEAL_PROVENANCE_FROM`, :808) | pre-2026-08-08 seals | YES — B946(b) rationale + the principled "rule cannot bind text sealed before it existed" |
| lawmap-scope (:868-874) | marker list + SCOPE_HEAVY=4 | YES — calibrated on the B965 audit, calibration stated |
| atlas-lexicon (:740) | LEXICON_MIN_BYTES=2000 thin-arc cutoff | PARTIAL — B821 triage rationale inline; the 2000 number itself uncited |

Fail-open observations (not exemptions, but same species): four gates soft-skip to PASS when git
is unavailable (`gate_append_only:132`, `gate_attribution:237`, `gate_tracked_forbidden:262`,
`gate_log_changelog_paired:646,650`) — on a git-less or shallow checkout these four gates green
while checking nothing; the restart-resistance audit hardened the file-missing paths but not the
git-missing paths. `gate_framing:73-74` skips unreadable files silently. `_load_attr_baseline`'s
`except: return {}` is fail-CLOSED in effect (empty baseline reds the backlog), which is correct.

## 7. Base rate (honest — full census, no sampling)

All 51 files close-read; primary character per file:

- **Genuine recompute-style** (math computed in-test or via a traced-computed module): 30/51
  (~59%) — metallic_spectra, mobius_vector_field, multichannel_fibonacci, preserved_form, qp1,
  qp2, qp4, r28_10 (majority of its tests), ramanujan_s1, sieve, sl2_decomposition, the seven
  B48-B60 probe locks (B48 verified computed; other six pattern-inferred), snapdata,
  spectral_curve_coulomb, sweep2_facts, t2_golden_cm, thermo, torsion, trace_selector_c5,
  trifocal, uniqueness_theorem, v4_genericity, w3_support_stop, zimm_bragg.
- **Governance/meta locks with real negative controls**: 9/51 (~18%) — no_hardcoded_paths,
  paper_chain_table, paper_citations, paper_provenance, public_surface_scan, relay_debt_gate,
  repo_gates, review_carry_gate, verdict_body_agreement.
- **Doc/string-pin locks**: 8/51 (~16%) — masterplan_v3, pc12_draft_skeleton, p5_draft,
  p5_phase3 (hybrid, best-in-class), roadmap_register, stale_absence_lock, the_road,
  sl4_dehn_filling_paper.
- **Pure cache-read (E40)**: 2/51 (~4%) — p3_depth_exposure, wave_b931_b933.
- **Files carrying at least one vacuous/unfailable assert**: 5/51 (~10%) — w2_molien_cell,
  r28_10_stabilizations, qp3_integration, wave_b931_b933, sl4_dehn_filling_paper.

The m-z stratum is materially healthier than a-l: zero literal-flag files (vs 60), two cache
locks (vs ~200 mentions), zero E12 leaks, and the strongest MB12 discipline in the suite lives
here. The failures that remain are of the SUBTLE kinds the enforced checker provably cannot see.

## RED FLAGS FOR THE EVALUATING SEAT (ranked)

1. **`tests/test_qp3_integration.py` — the theta-coupling lock certifies transcriptions**: every
   "derivative" (incl. the 15/32 coupling fraction, `:49-63`) is a hand-typed closed form from a
   comment; line 32 is a literal tautology. A wrong upstream trace-map derivation would pass all
   nine tests. Physics-facing, unlike the other findings.
2. **Two unfailable asserts invisible to the enforced vacuity gate** —
   `test_r28_10_stabilizations.py:104` and `test_w2_molien_cell.py:22` (`... or True`), plus the
   hardcoded-drift lock `test_r28_10_stabilizations.py:126-131`, in a file whose header claims
   "Recompute mathematics in-test". Measured: `check_test_vacuity` reports 0 TAUTOLOGY suite-wide.
3. **`test_wave_b931_b933.py:28`** — `or "0" in t` verified trivially true for the json it scans;
   the "no color singlets in the conformal 27" clause of the B932 outcome-A lock enforces
   nothing. Kin: `test_sl4_dehn_filling_paper.py:46`'s `or "no" in low` (the for-all-n overclaim
   guard is vacuous).
4. **gates.py naked/blanket exemptions**: the `"veins"` directory exclusion (`:630`, zero
   documentation); `VERDICT_GRANDFATHERED`'s 13 undischarged entries; `GRANDFATHERED_IDS`'
   comment-vs-set mismatch (five collisions described, one entry frozen). Also: four gates
   soft-skip to PASS without git.
5. **`test_stale_absence_lock`'s 16 "still CURRENT as of B1082" stamp floors**, ~150 arcs behind
   the board: the first B1216-B1232-era correction to a stamped absence will be FAILED by the
   lock — the corrector-biting direction, structurally identical to the pre-repair
   test_the_road. (test_the_road itself now pins "nine genuine open nodes" — repaired and
   currently true, but still a count-as-string under B1231's counts-are-lower-bounds rule.)
6. Skip-shape: `test_r28_10_stabilizations.py:47-50`'s `importorskip` inside a decorator likely
   skips the whole R28-10 prereg module (not just the snappy test) on a snappy-less runner —
   PLAUSIBLE, not executed.
