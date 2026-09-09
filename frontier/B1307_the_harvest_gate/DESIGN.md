# B1307 — THE HARVEST GATE: an instrument that makes unread seat work visible the hour it is pushed, ages it like a relay, and reconciles the harvest ledger against every seat's own index — plus the sense census's third pre-registration: DESIGN (pre-registration, sealed before any of main's computations)

**Date:** 2026-09-09 · **Seat:** cc (main) · **Plan:** MASTERPLAN v3.1 §1 (THE HARVEST-DEBT GATE), §1a rule 3 (two-sided completeness control),
§3 row B1307, §7 Phase 4 (1) "instruments first"; the decision log of 2026-09-09 ("B1307 is now the standing priority — three collisions + three relay
lags in a week"). · **Kind:** instrument arc (no physics claim). · **Read in full before this seal:** `scripts/gates/gates.py` (the `GATES` dict, `run_all`,
`review_status`, the `gate_relay_debt` wrapper), `scripts/checks/relay_debt.py` (the model: a ledger is the register, a file with no row is invisible
work, a debt ages and fails past 21 days unless escalated by name, `OA_RELAY_TODAY` for deterministic tests), `tests/test_relay_debt_gate.py`,
`tests/test_repo_gates.py` (the suite lock runs every gate in `GATES`), `docs/HARVEST_LEDGER.md` (82 rows; seat names as written; no pins table),
`docs/RELAY_LEDGER.md` (header + row grammar), the B1305 census script and both FAIL records (FINDINGS §Q1, FINDINGS_B §5), and on each seat branch its
own index and relay convention (the table in §2). **Nothing below was computed with main's own code before the seal**; the inform reads were `git
show`/`git ls-tree`/`git grep` on fetched refs.

## 0. The rule lines this DESIGN carries

- `already_banked.py "harvest debt gate seat pin items newer than pin"` → settled arcs with overlapping terms exist (B957, B1000, B1202: the already-banked
  check is main's instrument for the "finished-but-forgotten" class and is the nearest relative); none is a seat-debt gate. `absence_sweep.py "harvest_debt"`
  → PRESENT on 3 heads **as a name only** (HARVEST_LEDGER's header, B1305's FINDINGS, the path-reference exemption list announce it); the script
  `scripts/checks/harvest_debt.py` does not exist on any head. `absence_sweep.py "last-harvested commit"` → ABSENT everywhere: **no seat pin has ever been
  written down on main.** So the gate is new, and the pins table is new.
- The seat speaks first (§1a rule 2) applies to the *content* of the ledger's rows, which this arc does not write. The gate grades nothing; it counts.

## 1. The view from above — which failure this closes, which it does not

**The failure, in the record's own instances (all within eight days):** the SM-derivation seat's range-exhausted note sat unanswered on its branch while
main issued a numbering relay it never saw (collisions two and three, B1302–B1304 twice over); the cloud's 34 memos 156–189 went unrelayed for nine days
and were found by fetching, not by a relay; the audit seat's twenty-one rounds were harvested three days after its last push because nothing counted
them; the physics seat's `FC_TO_CC_2026-09-06_THE_LIFT_AND_THE_THIRD_ROOT.md` — its relay of R64–R72 — **has no RELAY_LEDGER row on main today** (the
relay-debt gate's regex names the CC/CC3/CODEX/CLOUD lanes only: `SM_TO_CC`, `FC_TO_CC`, `FAB5_TO_CC`, `CHAT1_TO_CC` are structurally invisible to it,
B1172's repair 3 recurring for the lanes that opened after it). And at this seal, two seats have already moved past main's pins: the SM seat by three
commits (a proved positive half of its tower law, a proved presentation identity, sm:B1350's obstruction stages, a prior-art reconciliation), the cloud by
memos 183–184 (a printed quantum A-polynomial that does not annihilate F⁺; the 5₂ tail a false theta) — and the codeberg mirror is behind origin on both
branches. The mechanism is the alias table's own sentence: **a request or a result that lives on a branch reaches main only at a harvest, and nothing
counts the hours in between.** The relay-debt gate ages relays that have rows; nothing ages the branch itself.

**What the instrument does:** reads the local remote-tracking refs (fetching first when asked), compares each seat branch with a pinned "last read at"
commit, maps every changed path to a seat item id by that seat's own convention, checks each id against the harvest ledger's rows, reconciles the whole
of each seat's own index against the ledger both ways, lists seat-branch relay files without a relay-ledger row, reports mirror lag, and ages unread
items exactly as `relay_debt.py` ages relays. **What it does not do:** read, verify or grade a seat result — the arcs do that (B1306 B–D next); it makes
the unread visible and makes "unread for three weeks" a failing state. **The one thing it means if it fails:** if the reconciliation cannot be made
two-sided (a planted missing id not reported, or a planted stale row not flagged), the instrument is NOT ADOPTED (MB12) and the ledger stays a
hand-kept file — and the plan's §1a rule 3 has no mechanical form.

## 2. The specification, pre-registered

### 2.1 Seats, indices, item ids, relays, pins

| seat (ledger name) | branch (canonical remote) | the seat's OWN index (rule 3) | item id in a ledger row | relay files | pin = last read at (arc) |
|---|---|---|---|---|---|
| SM-derivation seat | `origin/standard-model-derivation-0qt6ao` (codeberg mirror) | `frontier/<dir>` present on the branch and absent on main (23 dirs: B1267…B1283, B1300–B1304, B1350) + the branch-only `docs/*.md` (8) | `sm:B\d{4}` or `sB\d{4}`; a docs item by its filename | root `SM_TO_CC_*.md` | `0dffacd4` (B1306 A) |
| physics seat (fc) | `origin/physics-seat-evaluation-8dkbrl` | `INDEX_R56-R72.md` rows (17) + `recompute/R<nn>_*` dirs (56) + `H1/H2` | `R\d{1,2}` in a row whose seat cell says `fc` or `physics` | `FC_TO_CC_*`, `FAB5_TO_CC_*` under `reports/fresh_physics_seat_2026-09-01/{,relays/}` | `659487bb` (B1298/B1303) |
| codex seat | `codex/seat-r001` (origin) | `MANIFEST.md` rows R001–R044 | `R\d{3}` in a row whose seat cell says `codex` | root `CODEX_TO_CC_*.md` (47) | `f7a49536` (B1306 A inventory) |
| cc3 (paper seat) | `paper/structure-genesis-first` (origin) | `frontier/B8\d{3}_*` dirs (87) | `B8\d{3}` | `frontier/B8xxx/relays/CC3_TO_CC_*.md` (91) | `a31456d2` (B1306 A inventory) |
| hostile-review seat | `golden_gate/paper-hostile-review-alero0` (that remote only) | `session_handoff/MANIFEST.md` rows (memos 10–24, 26, 27) + `session_handoff/memos/*.md` (29) | `memo N` in a row whose seat cell says `hostile`, or the memo's filename stem | none (its relays were the owner's paste) | `6fc86147` (B1306 A inventory) |
| cloud seat | `origin/outside-bench` (codeberg mirror) | `outside_bench/INDEX.md` rows 30–184 (155) | `memo N` / `memos N–M` in a row whose seat cell says `cloud` | `outside_bench/CLOUD_TO_CC_*.md` | `792918b7` (B1305 B) |
| cc3 (braver-questions branch) | `audit/b775-braver-questions` (origin) | seat-only `frontier/` dirs (B775, B783, B784, B792, B796, tierB_opening) | `B7\d{2}` in a row whose seat cell says `braver` | none | `53da05f6` (B1306 A inventory) |
| consolidation seat (qor5up) | `origin/new-session-qor5up` | seat-only `frontier/` dirs B1025–B1054 (30) | `B10[2-5]\d` in a row whose seat cell says `qor5up` or `consolidation` | none | `3851df2a` (B1306 A inventory) |
| audit seat | `audit/physical-bridge-2026-09-05` (origin) | top-level `reports/physical_bridge_2026_09_05/*.md` minus the pre-registration/control/repair companions (`*_DESIGN`, `*_PRIOR`, `*_CONTROL*`, `*_REPAIR*`, `*_DERIVATIVE`, `README`) | the file's stem anywhere in the row's item or path cell | none | `6f862099` (B1304) |
| chat1 (the session-relay seat) | no branch | — | — | owner-pasted; rowed by hand | not pinned (no ref to pin) |

The pins live in a new `## Pins` table at the head of `docs/HARVEST_LEDGER.md` (`| seat | branch | pin | pinned at | by arc |`); **a pin advances only in a
landing that read the branch up to that commit** — it is a receipt, not a bookmark. "Newer than pin" = a path changed in `pin..head` (first-parent
history of the branch) that maps to an item id; an item changed after its row was written is debt again until the pin passes it.

### 2.2 The script — `scripts/checks/harvest_debt.py`

CLI: `harvest_debt.py [--fetch] [--strict] [--json] [--selftest]`; stdlib only, no network unless `--fetch`. Per seat it prints: head, pin, commits since
pin, **NEW** items (changed since pin) split into rowed / unrowed, the **BACKLOG** (index ids with no row), **STALE ROWS** (ledger rows whose id resolves
to no index entry), **RELAYS WITHOUT A ROW** (seat-branch relay files absent from `docs/RELAY_LEDGER.md`), and **MIRROR LAG** (origin vs codeberg heads).
A one-line summary per seat and a total close the report. Exit codes: **0** — no failure; **1** — instrument integrity (pins table missing/malformed, a
pinned ref unresolvable when it exists on the remote, the ledger unparseable) or a `--selftest` control failing, or under `--strict` any debt at all;
**2** — an unrowed NEW item whose newest change is older than **21 days** (the relay-debt constant; `OA_HARVEST_TODAY` overrides the clock for tests).
The pre-push gate runs the plain mode (integrity + ageing); `gates.py review-due` runs `--strict` and prints the debt, so a review opens with the number and
cannot close with unread seat results (the review's own checklist item, added to REVIEWS at Review 56).

### 2.3 Two-sided controls (MB12 — the instrument must be able to fail)

- **Synthetic (`--selftest`, deterministic, no git):** on a fabricated seat with an index {a, b, c}, a ledger with rows for {a, b} and a change set {c, b}:
  (i) the planted NEW unrowed item `c` is reported; (ii) the harvested unchanged item `a` is not; (iii) a planted index id `d` absent from the ledger appears
  in BACKLOG; (iv) a planted ledger row `z` resolving to no index id appears in STALE ROWS; (v) an unrowed NEW item dated 22 days ago fails with exit 2
  and the same item dated 20 days ago does not. All five, or the gate is not adopted.
- **Live (this tree, after the synthetic controls pass):** `OA_HARVEST_PIN_OVERRIDE="sm=<pin>^"` must grow the SM seat's NEW set by exactly the item ids
  touched in that one commit and nothing else; the first unmodified run must list the two movements already observed at inform (§1): the SM seat's three
  commits since `0dffacd4` and the cloud's memos 183–184 (+ the edited relay) since `792918b7`.

### 2.4 Pre-registered expectations (priors stated; each can fail)

| # | expectation on the first live run | prior | if it fails |
|---|---|---|---|
| E1 | NEW: SM seat ≥ 3 item ids (sm:B1303, sm:B1304, sm:B1350 at least); cloud memos 183, 184 + its relay | 0.90 | the path→id maps are wrong; fix and re-run, recorded |
| E2 | BACKLOG (index ids with no ledger row) ≥ 250 of ≈ 430 index ids across the nine branch seats | 0.80 | either way it is the number B1306 B–D must pay; recorded |
| E3 | seat-branch relay files with no RELAY_LEDGER row ≥ 100 (cc3 ≈ 63, codex ≈ 42, fc 3) | 0.85 | the relay ledger is more complete than its lane counts suggest — recorded as good news |
| E4 | `relay_debt.py`'s `RELAY_RE` misses the `SM_TO_CC`/`FC_TO_CC`/`FAB5_TO_CC`/`CHAT1_TO_CC` lanes (read at inform) | verified by reading | widened in this arc to `[A-Z0-9]+_TO_[A-Z0-9_]+_<date>`, lock extended |
| E5 | MIRROR LAG on `origin/outside-bench` and the SM branch (codeberg behind origin) | observed at inform | the gate must print it; if it cannot, the remote-pair logic is wrong |
| E6 | the gate's own run time < 20 s without `--fetch` (it is on the pre-push path) | 0.85 | cache the per-seat index reads or move reconciliation to `--strict` only |

**Adoption rule:** `harvest-debt` enters `GATES` and `review-due` **iff** §2.3's five synthetic controls and the live pin-override control pass. The gate count
becomes 32; `docs/CAMPAIGN_STATUS.md`'s currency line and Review 56 say so. The plan's rule that a review cannot close with undispositioned rows takes its
mechanical form here: `review-due` prints the debt and the review checklist carries it.

## 3. The sense census — third pre-registration (B1305 Q1/Q6, NOT ADOPTED twice; the DESIGN_B FAIL branch named this arc)

**The instrument** is the cloud's memo 172 census (B1305's independent implementation `b1305_sense_census.py`: seven terms, a ±130-character marker
window, FALSE COMFORT below 2 %, two-sided control = `Chern-Simons` genuine AND `logarithmic`/`non-semisimple` false comfort, plus three planted MB12
controls). It failed its negative control on main twice, both times because **its own documentation says "logarithmic CFT"** (first this arc's DESIGN and
the saved cloud table; then HINT_LEDGER's H-B1305 row and the two generated views that carry slice A's verdict text). The second FAIL record named two
new routes; both are pre-registered here and both run, in this order:

- **Route A — the self-naming exclusion (the live tree at HEAD):** exclude from the prose set every `.md`/`.tex` file whose text matches `/sense[ _-]?census/i`
  (at this seal: 12 files — CAMPAIGN_STATUS, HARVEST_LEDGER, HINT_LEDGER, RELAY_LEDGER, the two generated views, and six B1305 files; the list is computed
  at run time, not hard-coded, so a future mention excludes itself). Then the two-sided control and the three planted controls. **PASS** = two-sided
  PASSED and planted PASS. **Prior 0.45** — the exclusion removes every file that failed before, but `docs/HINT_LEDGER.md` was the carrier last time and
  any surface that discusses the instrument without naming it (a future review, an OPEN_LEADS note) re-contaminates; the run tells.
- **Route B — the fixed pre-instrument commit:** the last main commit whose prose tree does not name the instrument is **`31dd52b9`** (B1302's landing;
  computed by a first-parent walk from `1ff529f7`: 1, 1, then 0 at `31dd52b9` and every commit before it). Run the unmodified census (no exclusion) on a
  detached worktree at `31dd52b9`. **PASS** = two-sided PASSED. **Prior 0.70** — the cloud's own tree (main + `outside_bench`, excluded) passed at
  `ec15923d`; a clean main should too, and if it does not the instrument was never sound on this corpus.
- **Decision rule (fixed now):** ADOPT as `scripts/checks/sense_census.py` (research instrument, not a gate; the exclusion pattern and the meta-list carried
  as constants; `--selftest` = the three planted controls) **iff Route A passes**. If only Route B passes: **NOT ADOPTED as a live instrument**; the
  record says "sound on a frozen tree, defeated by its own documentation on the live tree", and the B1305 reading of `character` stands as it is. If both
  fail: NOT ADOPTED; the cloud's instrument remains the cloud's, the two FAIL records stand, no fourth try without a new idea. The negative control's
  terms are not changed in any branch (changing the control to pass it is the E52 shape).

## 4. Not in this arc

Reading or grading any seat item (B1306 slices B–D pay the backlog the gate counts); Review 56, which is due (20 merges since Review 55 at this seal) and
runs after this lands with the gate's first report as its opening line; the E53 surface-propagation check (Phase 4 (1), the next instrument arc); any change
to the harvest rules (§1a) — the gate implements rule 3, it does not amend it.

## 5. Landing list (fixed before the build)

`scripts/checks/harvest_debt.py` (+ `--selftest`); `scripts/gates/gates.py` (`gate_harvest_debt`, `review-due` prints `--strict`); `scripts/checks/relay_debt.py`
`RELAY_RE` widened (E4) with `tests/test_relay_debt_gate.py` extended; `tests/test_harvest_debt_gate.py` (selftest, regex/id maps, a live smoke run, the
exit-code semantics); `docs/HARVEST_LEDGER.md` `## Pins` table; `frontier/B1307_the_harvest_gate/verification/` (the first report `harvest_debt_first_run.txt`
+ `.json`, the pin-override control receipt, the census runs `sense_census_routeA.txt`/`routeB.txt` + JSON); `frontier/B1307_the_harvest_gate/FINDINGS.md`,
`arc_verdict.json` (`instrument: true`); `tests/test_b1307_the_harvest_gate.py`; WORKING_RULES currency note (one line: the branch is aged, not only the
relay); REVIEWS: nothing until Review 56; CHANGELOG + PROGRESS_LOG + CAMPAIGN_STATUS; HINT_LEDGER rows; the sense-census verdict in FRESH_EYES (registers
8 and 10 named it); `check_path_references.py` exemption for this DESIGN (it cites seat-branch paths by design).
