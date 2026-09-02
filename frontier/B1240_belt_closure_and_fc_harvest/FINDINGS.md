# B1240 — THE BELT CLOSURE: the seam-harvest era's reproduction locks now RUN — and the fc R42–R50 harvest

**Date:** 2026-09-02 · **Seat:** cc (main) · **Source:** the physics-seat evaluation branch (fc) R42–R50 + Phase C/D
synthesis @ its `synth/` state, every finding recomputed here; the belt finding is this arc's own ·
**Lead:** L197(b) (the belt's non-recomputing families), E57 (lock without tool) · **Wall:** none touched
**Verdict:** OPEN — the schema class for record/harvest arcs (as B1167/B1171/B1213): instrument + closure + six propagated corrections; no theorem claimed, no verdict of record reversed; Gate 5 untouched

## THE PRIZE FIRST

Twenty-seven arcs of the seam-harvest era (B1147–B1184) — the harvests of the cloud seat's outside-bench
certificates, the charter attack, the qualia-parity synthesis, the quine synthesis — were "locked" by tests that
assert the **string** `REPRODUCES` occurs in a committed record, with no subprocess anywhere in the test file.
Five of those runners **could not run on a fresh clone of main at all**: their certificates were to be fetched from
a seat branch by name, the fetch list omitted the sibling files the certificates load at runtime, and the run
record they cite (`reproduce.log`) is gitignored repo-wide. The lock said REPRODUCES; the tool was absent.

After this arc: **the full transitive closure is vendored into the five arcs (65 files, sha256 per file,
byte-identical to the pinned SHAs), every one of the 25 certificates prints REPRODUCES on the main bench, a
permanent instrument (`scripts/checks/reproduce_belt.py`) reports the three shapes of a non-running lock with
a 9-control selftest, and `tests/test_reproduce_runners_live.py` EXECUTES all 26 runnable belt runners on every
suite run** (the 21 fast ones in full, the five heavy ones on their fastest certificate; all under `OA_SLOW=1`).
The ratchet: string-only locks may not grow past 27; no runner may reference a file main does not track.

The programme's claim to a stranger is "clone it and run it". For this era that claim was, until today, itself a
string.

## 1. The belt — census, root cause, closure

**Census** (`verification/reproduce_belt_before_output.txt`, the instrument on main before this arc):
- string-only `REPRODUCES` locks: **27** test files (B1147, 1148, 1149, 1150, 1153, 1156–1169, 1171–1175, 1180,
  1182, 1184) — the pattern `"REPRODUCES" in <text>` with no `subprocess` in the file;
- runners scanned: **69**; runners referencing untracked or absent files: **5** — B1147 `reproduce_all.sh`
  (unpinned; source resolved to `origin/outside-bench @ dc937010`), B1148 `reproduce_new.sh` @ d3c99640,
  B1149/B1150/B1153 `reproduce.sh` @ 1544989d / 981f4c33 / 0c7f8b5a;
- runners that recompute nothing: **7** — six PINS-TEXT (grep-only: B1171, B1173, B1176, B1177, B1178, B1179, all
  printing REPRODUCES) and one INERT (B1175, which prints RECORD and says in its own header "THIS SCRIPT RE-RUNS
  NOTHING" — the honest form).

**Root cause, computed not recalled** (`verification/closure_full.json`). At each pinned SHA the certificates'
imports/`open()`/`exec()` were followed transitively: five sibling dependencies that no runner's fetch list names —
`certificates/twisted_double.py`, `certificates/paper/verify/check_charge_bracket.py`, `certificates/simul_verify.py`,
`certificates/spacetime64.py`, `certificates/theta_dump.py` (absent at dc937010, present at d3c99640;
`spacetime64.py`/`simul_verify.py` byte-identical at both) — plus B1153's `c4data/c4_zeros_{L,zeta}.txt`. Closure
sizes: B1147 15 files, B1148 11, B1149 5, B1150 5, B1153 2 (+2 data). A first vendoring that took only the named
certificates left three DIFFs (a2_glue64, one_bit, hitind: `FileNotFoundError` on the siblings) — that is the
record in `verification/closure_run.txt`, kept as the negative control.

**With the closure vendored** (`verification/closure_run_full.txt`, the edited runners in a scratch copy of the tree,
final vendoring): B1147 11/11, B1148 7/7, B1149 3/3, B1150 2/2, B1153 2/2 — 25/25 `rc=0 REPRODUCES`, every runner
rc=0. One caveat inside the 11: `c2b_ohtsuki_bridge`'s expected output was never committed at source (the first
full run printed "(no committed output)" for it); our run is deterministic (rc=0, identical tail across runs), so the
vendored `outputs/c2b_ohtsuki_bridge_out.txt` is OUR output, labelled GENERATED in `VENDORED_FROM.txt` — it pins
reproducibility of the run, not an independent expectation. Wall time: 135 s, 47 s, 20 s, 21 s, 47 s
(`verification/cert_timings.txt` per certificate; `belt_timings27.txt` all 27 runners on main before the fix:
21 print REPRODUCES in ≤ 3 s, the five print nothing or exit 2).

**Runner edits** (each carries a dated bracket): B1147 pinned to dc937010 (it carried no SHA); all five take
`CERTS=<name>` to run one certificate; B1149/B1150/B1153 gain `cd "$(dirname "$0")"` (they relied on cwd);
`VENDORED_FROM.txt` per arc (SHA, source path, sha256 per file) and `ADDENDUM_2026-09-02_B1240.md` per arc.

**The live lock** (`tests/test_reproduce_runners_live.py`): each runner executes in a temporary copy of its
`verification/` (the tree is never written — B1149's `our_trace_three.out` is tracked, an anomaly the copy
sidesteps), except B1171/B1172/B1173, which read sibling arcs and docs by relative path and run in place with a
before/after snapshot asserting nothing was written. Failure markers are verdict-shaped (`DIFF` as a whole word at
line end, `(no committed output)`, a Traceback header) — B1166's prose "DIFFERENT" tripped a substring version, the
control that shaped the regex. Two-sided: a tampered expected output (one appended line in B1149's
`trace_three_out.txt`) reds the lane; restored, it greens (both runs on record in this session).

**Default lane cost:** ~11 s for the five heavy arcs (cusp_beat 0 s, kappa_beat 0 s, trace_three 6 s,
family_yukawa 4 s, c4b_superposition 1 s) + ~20 s for the 21 fast runners.

## 2. E57 gets its true extent — and a third shape

E57 (`docs/ERROR_LEDGER.md`, filed under B1238 as "lock without tool": a committed test, an untracked checker) has:
- **instances #2–#6** = the five runners above (committed test → committed record → runner whose inputs are not on
  main → run record gitignored);
- a **gate scope hole**: `gate_tracked_deps` (B1238's 30th gate) reads tracked `.py` under `tests/` and `scripts/`
  and is blind to shell runners under `frontier/` and to files that are simply absent. `reproduce_belt.py --runners`
  covers exactly that hole (and `test_belt_ratchet_string_locks_do_not_grow` runs it on every suite run);
- a **third shape**: a runner that recomputes nothing and prints REPRODUCES (PINS-TEXT). B1171/1173/1176–1179 are
  record-surface arcs where the sentence is defensible ("the record reproduces"), so they are CENSUSED here, not
  edited — the honest form is B1175's (prints RECORD). Turning the six into RECORD-printers is a one-line change
  each and is left to the arcs' next touch; the instrument names them on every run.

## 3. The fc harvest, R42–R50 — every finding recomputed here

| cell | fc's finding | recomputed here | disposition |
|---|---|---|---|
| **R42** m=12 class count | B92's companion table needs h(148) | own SL₂(ℤ) reduction: **3 proper / 2 improper (GL₂ℤ)**; PARI `qfbclassno(148)` = 3; independent PARI-ρ route: 14 reduced primitive forms, 3 ρ-cycles (two 6-cycles + {(−1,12,1),(1,12,−1)}), GL 2, no form left unvisited; theory: 6+√37 has norm −1 so h⁺ = h = 3 for the conductor-2 order. Own table m=1..11 equals PARI throughout (1,1,1,1,1,2,1,1,2,2,1) — which also confirms fc R45's B92 row | VERIFIED + SHARPENED (the SL/GL split); relayed to codex as the R040-adjacent datum |
| **R43** asserted batch | Vol(4₁) digits; B955 surjections asserted | Vol(4₁) at 35 dps = 2.02988321281930725004240510854904**06**; `frontier/B980_k3_conflation/FINDINGS.md:81` prints "…0424051081…" — a digit slip, inline-corrected. B955's A4/D5/S5 surjections brute-forced over Sₙ² (`fast_checks.py`): all True | B980 addendum; B955 addendum (asserted → computed) |
| **R44** Lie batch | B549's seven numbers labelled "Perron spectrum of the E7 Cartan matrix" | the seven are the **Perron eigenvector of the E7 Dynkin ADJACENCY matrix, normalised by its minimum** [1, 1.285575, 1.879385, 1.969616, 2.532089, 2.879385, 3.701666]; match exact to 6 dp | B549 addendum (mislabel, numbers stand) |
| **R45** misc arithmetic | 4 MATCH rows (B554 class numbers, B407 φ⁴+φ⁻⁴=7, B92 table, B1067 regulator) | B92 row independently confirmed by the R42 table above | nothing to propagate |
| **R46** codex certificates | 11 codex certs pass on fc's bench; only `r024_lepton_character_datum.py` is tracked on main | read; the ten untracked certs are the codex-side instance of exactly this arc's class | → L198 (ship-the-generator, codex side) |
| **R47** outside-bench certificates | 17 certs pass on fc's bench; an "up-Yukawa disagreement" | the disagreement is the layered reading already banked in B1185 INV-1 (heterotic dressing: zero; object channel: 6 nonzero kinematic components). The live surface `docs/SM_SPECIFICATION_LEDGER.md:19` states only the dressing half | dated bracket added at the ledger line |
| **R48** B511 wild access | D3.3's banked percentiles "2.0, 2.0, 2.0" are a double-precision collapse; dps60 gives classical 0.927/0.967/0.850 | **independent 200-bit re-implementation on trace coordinates** (`b511_d3_tracemap.py`; maps verified against explicit SU(2) matrices to 1e−15 first): M10/D10/F80 classical 0.927/0.920, wild 0.028/0.035; M20/F80 0.863/0.858, 0.085/0.087; D20/F80 0.943/0.940, 0.020/0.020; F-only control classical 0.022/0.028, wild 0.782/0.762 (κ drift ≤ 1.3e−58 — the detector bites); all prec200 escaped = 0. The SAME code at 53 bits escapes 112–171 of 400 per run with classical 0.52–0.64 | CONCURS; B511 D3.3 **REBANKED on the trace map**, `d3_results.json` percentiles marked ARTIFACT (B511 addendum) |
| **R49** spacetime64 room | the cloud certificate prints "(0,0) content in the complement: 2 (0 = NO hypercharge room)" | reproduced verbatim (`spacetime64_output.txt`): the parenthetical contradicts its own count. The sentence is NOT on main — it lives on the outside-bench branch only | relay to cloud; nothing to correct here |
| **R50** B775 V4 table | 8/8 rows | `symmetry_group()` (orientation-aware, B1235's detector): m004/m003 order 8 amphicheiral, m025 6 T, b++RRLL 8 T, m009/m010/b++RRL/b++RLL 4 F — 8/8 | CONFIRMED |

**Phase C/D synthesis, read:** 59 packets / 398 claims; 8 DIFFERS all judged; 52 PARTIAL; 139 CANNOT_RUN (the
class this arc's instrument targets); Phase D 187/205. fc's `SUMMARY.md` tallies **`SUPERSEDED_UNMARKED` 128**
(128 distinct arcs) — L197 quotes **48** from the earlier 605-arc partial digest; the full candidate list ships here
as `verification/superseded_unmarked_candidates.tsv` (candidates, never verdicts — the identification audit's rule;
one row's quoted worktree directory name is written `[seat]_…` per the attribution rule, otherwise fc's text verbatim).

## 4. Corrections propagated (the E53 rule: reach the source, not just the log)

- `frontier/B511_*/ADDENDUM_2026-09-02_B1240.md` + inline brackets on `D3_FINDINGS.md` D3.1/D3.3 rows and the
  reproducer line (D3.3 REBANKED on trace coordinates; the committed `d3_measure.py`/`d3_wild_access.py` NaN on
  numpy 2.4.6 per fc; the percentiles are an artifact of 53-bit escapes).
- `frontier/B549_*/ADDENDUM_2026-09-02_B1240.md` + inline bracket at FINDINGS.md:5 (adjacency Perron vector, not
  "Cartan matrix spectrum"; generator `fast_checks.py` R44).
- `frontier/B980_*/FINDINGS.md:81` inline digit correction + addendum.
- `frontier/B955_*/ADDENDUM_2026-09-02_B1240.md` (surjections computed True).
- `docs/SM_SPECIFICATION_LEDGER.md:19` dated bracket (layered reading, B1185 INV-1).
- `docs/OPEN_LEADS.md` L197 inline update: 128 not 48; string locks 27 (the lead said 29); instrument + candidate
  list shipped; PINS-TEXT census.
- `docs/ERROR_LEDGER.md` E57 row extended (instances #2–#6, scope hole, third shape, instrument).

## 5. Self-caught slips in this arc (recorded because the class is E53-shaped)

1. **R42 first draft counted imprimitive forms** (2·(disc 37) forms at D=148) and reported 4 proper / 3 improper;
   the primitivity test was added and own ρ was checked against PARI's on all 14 reduced forms before the count
   was written anywhere.
2. **A stale JSON**: after fix 1 the script was correct but `fast_checks.json` had not been regenerated; the carried
   note (3/2) and the file (4/3) disagreed. Rule adopted: *a verification JSON is regenerated by its script in the
   same edit that changes the script* — this arc's three scripts each end in a verdict block and were rerun after
   that block was added.
3. **131 vs 128**: my carried `SUPERSEDED_UNMARKED` count was a substring grep over the TSV; three `OTHER` rows
   mention the term in prose. The column-parsed count is 128, which is also fc's own headline.
4. **The instrument flagged my own fix** (caught in the dry run against an archive of the staged tree, before landing):
   the runner edit `CERTS="${CERTS:-a b c}"` was tokenised by the closure extractor as garbage paths (all five runners
   "missing" again), and the instrument read its own selftest fixture string `"frontier/X/.../present.py"` as a
   dependency of any runner that calls it. Fix: shell defaults `${VAR:-default}` are expanded before extraction (a
   ninth selftest control pins the form) and the fixture paths are built from components. Both directions of the
   instrument's error are conservative (false MISSING, never false PRESENT), which is why the dry run — not the suite
   on main — is what found them: the instrument on main had nothing of that shape to read.

## 6. Leads

- **L198 — SHIP THE GENERATOR.** Phase C's PARTIAL shape 1 ("hardcoded record, live code absent or guarded") and
  the 139 CANNOT_RUN claims are this arc's class at corpus scale. Codex side first: B1175's R020–R022 certificates
  and the ten untracked codex certs of R46 need the same vendoring (source: `origin/codex/seat-r001`). Then the six
  PINS-TEXT runners → RECORD-printers. Instrument exists; the walk is single-seat (B1216's lesson).

## 7. Gate 5

No measured physical value enters or is compared. Class numbers, volumes, Perron vectors, trace-map statistics and
symmetry orders are properties of the object and of the record.

## Reproduction

`bash verification/reproduce.sh` → fast_checks (R42/R43/R44/B955/R50) + r42_pari_cycles + the instrument's
selftest and ratchet on this tree → `REPRODUCES` (~30 s); `OA_SLOW=1` adds the 200-bit B511 rerun (~2 min).
The belt itself: `python3 -m pytest tests/test_reproduce_runners_live.py` (~40 s default; `OA_SLOW=1` ~4.5 min).
