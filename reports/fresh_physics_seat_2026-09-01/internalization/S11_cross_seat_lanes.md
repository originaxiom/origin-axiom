# S11 — CROSS-SEAT LANES (internalization sweep, 2026-09-01)

Reader seat: internalization sweep S11. I digest and flag; the evaluating seat adjudicates.
Nothing below grades a claim dead or proved.

## Coverage modulus

**Read/computed:**
- `git branch -a`, `git ls-remote` (full ref list), then `git fetch` of all five non-main,
  non-campaign remote branches (fetch adds refs/objects only; no working-tree file modified,
  no checkout). Also fetched `main` (local `origin/main` was stale — see flag R4).
- Full `git ls-tree -r` file listings of all 6 branches + main, saved to scratchpad; set-diffed
  against main per branch.
- `git log --oneline -15` per branch; targeted `git show`/`git grep` on branch trees (never
  checked out): `menu_width.py` (full), `menu_width_out.txt` (full), `vol_basis_probe_out.txt`
  (head+tail), `vol_basis_probe.py` (docstring), V-NEG rows of `outside_bench/INDEX.md` (3 rows,
  full), `r030_phi_cover_specialization.txt` (40 lines) + its memo (50 lines),
  `r031_sparse_toric_trace.txt` (full), 2 of the 9 recovered relay files (heads), codex unique-file
  list (full, 186 files), outside-bench unique-file list (full, 477 files), audit/paper/qor5up
  unique-file lists (top-dir summaries only).
- On main: `docs/RELAY_LEDGER.md` (all 130 rows read across two pages), `docs/CLOUD_ALIAS_TABLE.md`
  (full), `frontier/B1225_no_canonical_selector/ADDENDUM_2026-08-31...md` (full),
  R01_B1225 FINDINGS (lines 15–140), grep-level context from the campaign reports
  (BATCH1, G2_t1_unblock, T1_third_column, S4b, INDEX, SEAT_ADJUDICATION — grep hits only,
  not full re-reads).

**Skipped (stated, not silent):**
- The bulk content of each lane (audit branch: 448 files unique vs main; paper branch: 705;
  qor5up: 162; outside-bench: 477; codex: 186). I sampled what the task targeted (the four
  artifacts, ledger cross-checks); the lanes' physics content is NOT digested here.
- The ~2,900-commit histories per branch (shallow clone; only head-15 logs read).
- All refs/pull/* (thousands); not enumerated beyond confirming they exist.
- B1233 (`b122d854`, remote main head) — not read; it is not in this clone's tree (flag R4).
- `git merge-base` is unreliable here: **the clone is shallow** (`--is-shallow-repository` =
  true), so most branch↔main merge-bases return empty and ahead/behind counts are untrustworthy.
  Only outside-bench yielded a merge-base (`cb96cb7e`).

## 1. The branch inventory (all reachable after fetch)

Remote `origin` = github.com/originaxiom/origin-axiom. Heads (refs/heads/* only):

| branch | head | head date | lane identity |
|---|---|---|---|
| `main` | `b122d854` (B1233) | 2026-09-01 | main bench. **NOTE: this clone's tree is at `680be7a` on the campaign branch, forked from `864c6b75` — one commit behind remote main (B1233 "THE Z-AI AUDIT")** |
| `claude/physics-seat-evaluation-8dkbrl` | `680be7a` | 2026-09-01 | THIS campaign's branch |
| `claude/outside-bench` | `d52bf025` | 2026-09-01 06:04 | **cloud's outside bench** (the RELAY_LEDGER's "origin/outside-bench": hashes dc937010, d3c99640, 7ff41915, 3debbec8, 60bcf01d all verified ancestors of this head). Carries `outside_bench/` (memos ≥151, certificates, seals, outputs; 477 files beyond main, all under `outside_bench/`). Recent heads: Q11 SENT to Dimofte (`2e4f11f6`), then Q1–Q8 composed as drafts-only, head = "Rewrite all seven drafts as letters rather than reports" |
| `codex/seat-r001` | `9c2c2c9a` (R034) | 2026-09-01 | **codex seat**. 186 files beyond main: the full R-series (R006–R034) certificates/memos/outputs incl. the yukawa-308 chain (R017, R023–R031), CODEX_TO_CC relays, the program-question-map |
| `paper/structure-genesis-first` | `a31456d2` (B8154 Paper IV) | 2026-08-29 | **cc3's live lane** (B8xxx band). 705 files beyond main: `papers/structure_paper` + `papers/series` (the four-paper series), frontier/B8068–B8154 |
| `audit/b775-braver-questions` | `53da05f6` | 2026-08-14 | **cc3's earlier audit lane** (pre-B8xxx-remap era; B775–B796 frontier work). 448 files beyond main — **including the nine "E51-unrecoverable" relay files (see §3)** |
| `claude/new-session-qor5up` | `3851df2a` | 2026-08-14 | **cloud consolidation seat** (the qB1025–qB1054 band). Dormant since 08-14; head = green-suite pin (4006 passed). Matches CLOUD_ALIAS_TABLE: fork `3524b889` verified ancestor; `be87a51` pin in its log; `docs/handoffs/CONSOLIDATION_REFRESH_HANDOFF_2026-08-12.md` present |

So: **all cross-seat lanes named by the ledgers are reachable in this clone after a fetch** — none
was reachable before fetching (the clone shipped with only main + the campaign branch), which is
the mechanical reason the campaign's own branch searches (batches 1–3) could see only main.

## 2. THE FOUR MISSING SINGLE-HOMED ARTIFACTS — branch-by-branch verdicts

### 2a. The 17-atom list — **FOUND on `claude/outside-bench`** (highest-value find)

> *Corrected 2026-09-01 (banking seat's correction, adopted):* the list is **present on main** in B1203's cert
> (`frontier/B1203_two_probes/verification/reproduce.sh`, 89affd5b, 2026-08-30) — the search that missed it looked
> at branches instead of the arc's own verification directory. The outside-bench file is a second, provenanced copy
> plus the tier-rule enumerator; only the enumerator was single-homed. R2 below is re-typed accordingly: the
> "on NO branch" claim was wrong on main first, on outside-bench second.

`outside_bench/certificates/menu_width.py` (committed `a1d99957`, **2026-08-28**, "MENU-1 run —
W1 = 11720") contains the explicit list, twice: in the frozen-protocol docstring with per-atom
provenance ("1, 2, 3 (grammar constants); 11 (the sum rule, B928); 12 (Vol = 12 Vol_orb, B1188;
the Coxeter number); 27, 64, 72, 78; 112 (B1188); 953, 2304 (B931/B910-928); 151/64, 553/64;
3/8; phi; 2+sqrt3") and as the executable `ATOMS` array. It matches exactly the 17-atom dict
R01 found hard-coded in main's `frontier/B1203_two_probes/verification/reproduce.sh`. Complex
atoms (ω, 2−ω) are declared excluded at tier 1; transcendental atoms (Vol, π²/6, 2 log φ)
declared tier 2 — the exact structure B1225/B1227 argue over.

**Contradiction of record (adjudicator's call):** the B1225 ADDENDUM (2026-08-31) states
*"Searched: main, `outside-bench`, `codex/seat-r001`, `paper/structure-genesis-first`. The list
does not exist on any of them"*, and RELAY_LEDGER row `CC_TO_CLOUD_2026-08-31_SEND_THE_SEVENTEEN_ATOMS`
repeats "enumerated on NO branch". The file had been on outside-bench for **three days** when
that was written. What the branch does NOT carry is the addendum's full ask (per-atom β-parity
and dimension annotations) — but the *list with provenance notes* is there, and the relay row's
literal claim does not hold against the branch tree. (R01 had already flagged the main-side half
of this — the hard-coded dict in B1203's reproduce.sh; the branch-side half is new here.)

### 2b. The W1 = 11720 enumerator — **FOUND, same file**

`menu_width.py` IS the enumerator (depth-≤3 ordered-operand grammar over the 17 atoms, one
optional root-sqrt, (0,1) filter, 40-digit dedup at 60 dps), and
`outside_bench/outputs/menu_width_out.txt` carries the banked run: "value pool: 17 atoms, 731 at
size 2, 38769 at size 3 … W1 (THE TIER-1 MENU WIDTH) = 11720", the decile histogram, median gap
3.53287e-5, min gap 1.63157e-9 — the exact numbers main banked. R01's line "W1 = 11720 itself:
NOT reproducible from committed files (enumerator is [not committed])" is true of *main's* tree
and of this clone as the campaign found it; it is not true of the reachable remote as a whole.
Committed 2026-08-28 — before B1225 (08-31) and before the campaign.

### 2c. B1217's V-NEG certificate — **FOUND on `claude/outside-bench`**, post-dating B1217's charge

- The charge (B1217, 2026-08-30; upheld by cloud as "bench error #15"): the extended-run
  V-NEG headline was reported but never committed; `vol_basis_extended.py` held only the basis
  builder; no committed cert carried the `involves_regulator` gate. True at their head `7ff41915`.
- The repair is now on the branch: `outside_bench/certificates/vol_basis_probe.py` (committed
  `a4759c6d`, **2026-08-29 23:18 UTC**, "Bench error #15: the extended regulator probe was
  reported and never committed"; its own docstring quotes and upholds B1217's charge) plus
  `outside_bench/outputs/vol_basis_probe_out.txt`: sealed 18 targets at sha256 `e93efeaa…`,
  Vol(m004) computed from Li₂, **CONTROL 216 cells → 117 raw / 117 involves_V / 0
  involves_regulator; EXTENDED (28-entry basis) → 108 / 108 / 0**. `outside_bench/INDEX.md`
  row 151 (banked 2026-08-30): "BENCH ERROR #15 CLOSED — … OUTCOME V-NEG STANDS UNCHANGED …
  from COMMITTED CODE — an error of BANKING not of COMPUTATION."
- **Staleness flag:** campaign S4b ("cloud's V-NEG headline run is not reproducible as
  committed — typed CITED, artifact missing") and INDEX item 22 describe the pre-08-29 state.
  The committed certificate has existed on the reachable remote since 08-29/30; whether main's
  CITED typing should upgrade is the evaluating seat's (and main's verify-don't-trust) call —
  the artifact-gap half of the claim is no longer current.

### 2d. The 27-value evaluator `.sage` files — **NOT on any branch (campaign verdict CONFIRMED)**

Grepped all six branch trees for `cech_308` / `marked_pseudoinverse`: **zero hits**. So
`certify_yukawa_down_tail_cech_308.sage`, `certify_yukawa_down_obstruction_308.sage`,
`attempt_yukawa_cech_308.sage`, `verify_marked_pseudoinverse_cech.sage` are absent everywhere
reachable — G1's "in-any-branch-tree=False" and the E51 .sage debt stand, now verified against
the actually-fetched branches (the campaign clone could not see them; the conclusion survives).

What codex/seat-r001 DOES carry near this hole (adjudicator may care):
- `documents/program-question-map/evidence/audit_yukawa_tail_record_consistency.sage` — a
  committed .sage in the 308 chain (an audit, not the evaluator);
- `certificates/r030_phi_cover_specialization/r030_mod1009_cover_all36.json.gz` + memo: exact
  GF(1009) unit identities on all 36 toric charts with pinned hashes — but the memo says
  explicitly: "R030 pays coverage and existence only. It does not emit a characteristic-zero
  contracting homotopy … evaluate the normalized residue trace, or construct either Serre tail";
- `r031_sparse_toric_trace` output: "SCOPE computation shrinks 384 trace simplices to 96;
  **no Yukawa entry or rank is evaluated**."

So the 27 values T[i,j,conn_k] remain uncomputed/uncommitted on every reachable ref — consistent
with T1/G2's missing-datum typing and with B1232's "codex runs still in flight."

## 3. E51 — the nine "unrecoverable" relay files ARE on a reachable branch

RELAY_LEDGER (rows 38–45, 102) and CAMPAIGN_STATUS (2026-08-28 seat-change entry) close E51
FINAL: the nine 2026-08-09 relay files are "lost from the working tree … **not on any reachable
branch** … checked at their local dir at retirement … **UNRECOVERABLE — E51 closes FINAL; these
ledger rows are the permanent sole record**."

**All nine named files exist at the ROOT of `origin/audit/b775-braver-questions`**, committed
2026-08-09 (08:48–11:28 +0200, i.e. the day they were written), verified real content by
sampling (FRAMEWORK_DELTA opens with the six-delta plan; HARVEST_MANIFEST with "29 relays…";
L114_DISCHARGE is 5.3 KB): `CC3_TO_CC_2026-08-09_FRAMEWORK_DELTA.md`, `_HARVEST_MANIFEST.md`,
`_DAY_LOG.md`, `_PROGRAMME_ASSEMBLY.md`, `_REVIVABLE_rationale.md`, `_L114_DISCHARGE.md`,
`_CORNERSTONE_PLAN.md`, `README_ARC_PROPOSAL.md`, `_PATH_BEYOND_THE_WALL.md` — plus four more
same-day relays already dispositioned from other copies (`_STEPPING_BACK`, `_UNEXPLORED_LEADS`,
`_CORNERSTONE`, `_COVER_four_relays`, `_GENESIS_STRATUM`). The branch head (2026-08-14) predates
the 08-27 escalation and 08-28 closure by two weeks; the files were on origin the entire time.
I do not adjudicate why the searches missed it (the branch is cc3's *older* lane, superseded by
`paper/structure-genesis-first`, and may have fallen out of whatever "reachable branch" meant
operationally) — but "not on any reachable branch" is false against today's remote, and E51's
CLOSED-UNRECOVERABLE status appears reversible by a fetch.

## 4. RELAY_LEDGER + CLOUD_ALIAS_TABLE cross-checks (rows claiming branch residence)

Verified TRUE:
- Alias table: qor5up fork point `3524b889` is an ancestor of `claude/new-session-qor5up`;
  the pinned green `be87a51` is in its log; `docs/handoffs/CONSOLIDATION_REFRESH_HANDOFF_2026-08-12.md`
  exists on that branch (the table says "not a main path" — correct); its frontier carries the
  colliding B1025–B1054 dirs exactly as the table maps them.
- All five "origin/outside-bench @ <hash>" ledger citations checked (dc937010, d3c99640,
  7ff41915, 3debbec8, 60bcf01d): ancestors of `claude/outside-bench` — one lane, continuous.
- codex rows: `codex/seat-r001` carries the cited R-series and CODEX_TO_CC relays (R017, R022,
  R024, R030/R031 all present as certificates + outputs).
- cc3 rows: `paper/structure-genesis-first` carries B8068–B8154 and the four-paper series
  (`papers/series`, `papers/structure_paper`); B8154's cited commit `a4cc762b` is its second-to-head.
- B1217/B1203/B1225 main artifacts are identical (same blob hashes) on main and outside-bench
  where shared; outside-bench's extra content is entirely under `outside_bench/`.

Contradicted (see §2a, §3): the SEND_THE_SEVENTEEN_ATOMS row's "on NO branch"; E51's
"not on any reachable branch / unrecoverable".

## 5. Red flags (typed per the sweep's rubric)

- **R1 [class (b), contradiction with live board — E51]**: the nine relay files declared
  UNRECOVERABLE-FINAL (RELAY_LEDGER, CAMPAIGN_STATUS 08-28) sit on `origin/audit/b775-braver-questions`,
  committed 2026-08-09. The ledger rows are NOT the sole surviving record.
- **R2 [class (b) — atom list]**: B1225's ADDENDUM and the 08-31 relay row claim the 17-atom
  list is "enumerated on NO branch" including outside-bench; `outside_bench/certificates/menu_width.py`
  (on that branch since 08-28) enumerates it with per-atom provenance, and is also the W1=11720
  enumerator whose absence R01 typed. Two of the four campaign-typed missing artifacts are one
  committed file.
- **R3 [class (b)/(c) — V-NEG]**: the campaign's "B1217 V-NEG artifact missing / typed CITED"
  (S4b, INDEX 22, SEAT_ADJUDICATION) describes the branch state at 08-30 head `7ff41915`; the
  committed certificate + output landed on outside-bench 08-29/30 (bench error #15 CLOSED,
  INDEX row 151, both arms reproduced 117/117/0 and 108/108/0). Any live surface still reading
  the artifact-gap as current is stale; the CITED→verified upgrade decision is main's.
- **R4 [class (b) — board currency]**: remote main is at `b122d854` (B1233, "THE Z-AI AUDIT:
  15 confirmed, 7 refuted, one real defect in our own record"), one commit past this clone's
  fork point `864c6b75`. The campaign's entire batch-1..3 record was written without B1233;
  its content (unread here) may bear on batch verdicts.
- **R5 [coverage caveat, not a defect]**: the clone is shallow; branch/main merge-bases and
  ahead/behind counts are not computable locally, and the campaign's earlier "git history +
  all four branches" search claims (G1 FINDINGS row B) could not have been executed against
  these branch trees from this clone as shipped. The specific .sage conclusion nevertheless
  verifies TRUE now (§2d); other history-quantified campaign claims inherit this caveat.
- **R6 [note for the board]**: outside-bench's last commits show Q11 was SENT (to Dimofte,
  `2e4f11f6`) and Q1–Q8 exist as unsent letter drafts — the specialist-contact queue has one
  transmission on record from the cloud lane.

## 6. What each lane carries beyond main (one line each, for the map)

- **claude/outside-bench**: the cloud's whole memo-numbered bench (INDEX ≥151 rows), incl. the
  MENU-1 instrument (atoms + W1), the V-NEG committed repair, the vol-hygiene cert, the frame
  census / grand-table / weld-book dossiers, the Q1–Q11 letter queue.
- **codex/seat-r001**: the full R-series (R006–R034) with dependency-free certs + outputs; the
  yukawa-308 chain up to (not including) the 27-value evaluation; the program-question-map.
- **paper/structure-genesis-first**: cc3's B8xxx band (B8068–B8154) + the four-paper series
  sources; head = Paper IV escape-(i) vacuity.
- **audit/b775-braver-questions**: cc3's pre-remap audit lane (B775–B796 arcs, SEALS/, THE_AUDIT_MANUAL)
  — and the nine E51 relays.
- **claude/new-session-qor5up**: the frozen cloud-consolidation record (qB1025–qB1054 dirs,
  consolidation docs, handoffs) — released FROZEN-RECORD-CLOSED by B1173; matches that typing.
