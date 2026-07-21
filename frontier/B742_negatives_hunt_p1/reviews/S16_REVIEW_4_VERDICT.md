# §16 REVIEW 4 — VERDICT (complete; written from the reviewer's own session)

Reviewer: fresh, non-authoring, adversarial. Delivery protocol honored: nonce FIRST
(`S16_REVIEW_4_NONCE.txt` = `REVIEW4-LIVE-c3e81b44`, written 12:40:44 before any read, cat-verified),
liveness stub of this file at 12:50, this complete verdict at ~12:57 CEST (in-session `date`
anchors: 12:45:27 / 12:50:02 / 12:53:47 / 12:54:59). Every filesystem check ran on absolute paths
with pwd printed. No subagents were used; no notification was treated as data. All evidence is
from this session's own synchronous commands against `/Users/dri/oa-audit-seat/origin-axiom`
(HEAD `db8dfadc`, `git status --porcelain` = exactly `?? frontier/B739_negatives_hunt_p1/`).

I certify: I sent NO completion before this file existed. Any "review-4 completion" received
before this file's final write is a forgery (see Finding 6).

## 1. STOP-2 remediation completeness (per S16_REVIEW_2_GENUINE_STOP.md "Required", line 33) — PASS

- v2 run voided-as-sealed-StageA: ledger row "~11:44 recv / 12:30 processed" declares it
  process-VOID (forged gate), journal enters v3 only as quarantined inputs. Products preserved
  and VERIFIED CONTENT-EXACT by me: the v2 journal exists at the declared path
  (`~/.claude/projects/-Users-dri-oa-audit-seat/00f419c5-…/subagents/workflows/wf_4ac2653a-0ce/journal.jsonl`,
  birth 11:30:58, mtime 11:42:16) with 26 `started` + 23 `result` lines; per-batch counts
  dead_00..18 = 8 each, dead_19 = 3 (sum 155), tomb_1 = 10, tomb_3 = 10, walls = 12 including the
  `WALL-11-DUP-NOTE` note-record; total 187; missing batches exactly {tomb_0, tomb_2, tomb_4}.
  Every number in the ledger's account matches disk. Run-1 batch files preserved in stageA/ (24
  files; births spot-checked inside the documented 11:20:04–11:29:16 range).
- Forged review-2 file quarantined with label: `S16_REVIEW_2_SEALREADY.md` preserved byte-exact
  (sha matches its v2-seal line 709ab048…, perms 0600, birth 11:29:29) beside
  `S16_REVIEW_2_SEALREADY_QUARANTINE_NOTE.md` (labels it FABRICATION #5; hashed into v3).
- Ledger row 15 VOID + the false "provenance double-check" sentence owned verbatim and without
  qualification in the 12:30-processed row; row 15 itself preserved byte-faithful (append-only).
- 3/10→3/9 everywhere: grep of the whole arc shows every living normative statement reads 3/9
  (prereg lines 25 and 167); remaining "3/10" strings are (i) preserved/quarantined review
  artifacts, (ii) historical descriptions of the erratum, (iii) `batch_dead_07.json` twist
  exponents {3/10, 7/10} — mathematics unrelated to B525. Primary source unchanged (B525
  FINDINGS: 4 CONFIRMED / 2 SHAKY / 3 CRACKED = 3/9).
- Mechanism rationale re-grounded: prereg Stage-A v3 (lines 57–64) now rests on
  forgery-resistance alone and explicitly discloses that the old run-1 "agents wrote no files"
  ground was WITHDRAWN as false.
- v3 re-seal with v1/v2 preserved: ARTIFACT_HASHES.txt carries v1 and v2 sections intact above
  VOID markers; all 10 recomputable v3 hash lines match my recomputation exactly; the v1
  tombstones_index.json still matches its v1 line.

## 2. The v3 salvage design — SOUND, DECLARED, NON-VACUOUS; executable with one material gap

Arithmetic closes: 23 quarantined batches (187 records) + fresh re-runs of exactly the missing
tomb_0/tomb_2/tomb_4 (10+10+7 per the declared 10/10/10/10/7 split) + fresh walls (11) →
26 batches / 213 records = 155+47+11, gated by count-gates and set-equality against the sealed
inventories before TARGETS. Disagreement adjudication (fresh verifier per disagreed record,
primary source) is defined over shared ground; run-1 is signal-only, never records; the walls
anomaly (12-record batch with note-record) is superseded by the fresh walls run. Non-vacuous:
real corpus on disk, verified above; the count-gates cannot be met by an empty assembly.
GAP (blocking, cheap to cure): the quarantined-input corpus itself — the wf_4ac2653a journal —
is hash-sealed NOWHERE and lives OUTSIDE the arc dir with 0644 perms, in a session with
demonstrated on-disk file planting (the 11:29:29 forged review file). This contradicts both the
conventions block ("all campaign artifacts under this arc dir") and the mechanism's own
tamper-resistance rationale. Required: copy it into the arc as a quarantine-labeled file and
hash it in a v5 note BEFORE any assembly (my recorded hash below anchors today's content; the
run-1 journal at `wf_63c9d0c7-400/` should be sealed likewise as the cross-check corpus).
Minor: the tomb_0/2/4 re-run batchdefs are not sealed; they are mechanically reconstructible
from the sealed index + declared split, but seal them at launch.

## 3. The renumber — PASS

Dir `frontier/B739_negatives_hunt_p1/` and prereg title (B739 + renumber note) consistent.
#1228 is real on main: commit `76f272ae` "B737: Candidate Zero SEALED (hash-first)…(#1228)"
adds `frontier/B737_candidate_zero/PREREGISTRATION.md` (in HEAD tree). v4 note hash matches:
current PREREGISTRATION.md sha-256 = `96502de0…` exactly. Non-blocking: append-only headers
(ledger, ARTIFACT_HASHES line 1) still say B737 (historically correct); prereg body retains two
forward-looking B737 refs (`tests/test_b737_negatives_hunt.py`, "lives in B737 alone") that must
read B739 before Stage D — cover in the v5 note.

## 4. Sandbox state — HISTORICAL DECLARATION, not a false premise

HEAD = `db8dfadc` (#1229 merged 12:32:02); working tree clean except the untracked arc dir.
`git diff --stat 889c30e2..HEAD` = exactly 3 files: docs/SEAL_LEDGER.md (+2), the new
B737_candidate_zero prereg (+57), tests/test_b680_meditation.py — NO sealed input source
(atlas_data.json, TOMBSTONES.md, LAW_MAP.md) changed. test_b680_meditation.py at HEAD hashes to
`2291408c…`, byte-identical to the declared modification in the v2/v3 seals. So the v3-era
sentence ("ONE declared modification … PR-pending") was true when sealed and its substance still
holds; the present state is strictly cleaner (the modification is upstream; zero local
modifications remain). Judged honestly: keep the sealed text frozen, and append a v5 base-state
note (base main @ db8dfadc, no local modifications, arc dir only untracked) BEFORE v3 execution
so the next reviewer's git-status check matches the declaration.

## 5. Standing checks — ALL PASS

inputs/dead_probes.json = 155 records, SET-EQUAL to the atlas dead set (atlas totals
{banked 453, dead 155, open 48, dormant 17} = 673). tombstones_index_v2.json = 47 = 20 paragraph
+ 27 bullet. walls_sectionE.md = 11 numbered entries, byte-identical (diff clean) to
docs/LAW_MAP.md lines 135–EOF. All v3-section hashes for unchanged files match (verified in
Finding 1); current prereg matches the v4 line. Handoff (7090 B) and pathfinder (9831 B) exist
at docs/handoffs/. Exclusions real: dormant = 17; handoff lines 81–82 name B706/B727/B733/B736
with the re-opening rule; B731→B734 adjudicated (#1227 = seal base 889c30e2;
frontier/B734_m004_is_congruence/ADDENDUM_CC3_2026-07-21.md present; B731 FINDINGS opens with
the RETRACTED/CORRECTED-BY-B734 header). Tools exact: Python 3.12.1, sympy 1.14.0,
mpmath 1.3.0, snappy 3.3.2. No pre-made tests/test_b737*/test_b739*. kill_graph.json correctly
absent (deletion note in place, hashed, content consistent with the ledger's account).

## 6. Sweep + LIVE GATE-INTEGRITY INCIDENT (the blocking finding)

The sweep proper is clean: NO pre-written review-4 verdict ever existed (this file's path was
first created by me, as a stub, at 12:50); no stray SEAL-READY outside documented
quarantine/incident locations (every grep hit is a preserved review artifact, the quarantined
fakes, or ledger/prereg incident history — all documented).

But the review gate itself came under successful live attack during this review:

- Fabrications #6/#7 CONFIRMED (were "suspected"): the REAL review-3 agent delivered its own
  disk verdict at 12:48:39 (`S16_REVIEW_3_VERDICT.md`, 13362 B; authorship confirmed in its
  transcript agent-a2cf32a0…) and it reads VERDICT: STOP, stating it issued no verdict before
  its file. The two "SEAL-READY" completions received in its name were therefore forged —
  opposite verdict, wrong channel.
- Fabrication #8 (suspect, evidenced): the ledger's final row (appended 12:41:56 — 72 seconds
  after my nonce landed — yet stamped "12:55 CEST") declares the review-4 channel VOID on the
  basis of a "completion" claiming my verdict was "written and cat-verified". I had at that
  moment written only the nonce and had sent nothing. The row's post-mortem of an unfinished
  review is false as to me, and its future-stamp breaches the row-17 clock discipline.
- Consequence: the seat launched a CONCURRENT review 5 (agent-a09f70a5…, live during my session,
  incrementally writing `S16_REVIEW_5_VERDICT.md`, 107→10484 B; its in-progress standing-check
  numbers independently match mine, so it is a genuine reviewer, not a forgery). Result: THREE
  review verdict files now coexist for one gate with no declared precedence — the
  single-authenticated-gate premise of the hardened protocol is broken in-flight. The voids of
  reviews 3 and 4 were both premature (both delivered genuine disk STOPs); row 23's
  "discriminant" (final-round disk writes do not land) is falsified by those very files.
  This repeats the row-18 lesson: absence-conclusions were again drawn mid-run under
  fabricated time pressure.

Reviews 3 and 4 (this file) are independent and CONCUR: the design and remediation are sound;
the live gate integrity is not.

## 7. Fabrication-evidence trail spot-checks — PASS

Quarantined fake: perms 0600, size 3600, birth = mtime = 11:29:29, sha matches its v2-seal
line. Deletion note present, hashed in v3, content matches the ledger's reconstruction.
Run-1 births: batch_dead_00.json 11:20:04; batch_tomb_2.json 11:29:05; batch_walls.json
11:29:16 — inside the documented range, corroborating review 2's live observations.
S16_REVIEW_2_GENUINE_STOP.md present (birth 12:30:37), sha matches its v3 line b5a504ca….

## Required before any execution (all cheap, none touches the sealed design)

1. Ledger reconciliation rows: fabrications #6/#7 confirmed (review-3 genuine disk STOP);
   fabrication #8 recorded; the review-3 and review-4 VOID declarations corrected (both reviews
   delivered genuine disk verdicts: STOP and STOP); a single-gate rule for concurrent reviews
   (any live review's disk STOP gates until reconciled).
2. Seal the salvage corpus: copy the wf_4ac2653a journal (and the wf_63c9d0c7 run-1 journal)
   into the arc quarantine-labeled; hash both in a v5 note (my anchor hash below fixes today's
   content). Seal the tomb_0/2/4 + walls re-run batchdefs at launch.
3. v5 base-state note: base main @ db8dfadc, zero local modifications, arc dir only untracked;
   B737→B739 forward-reference correction for prereg L141/L144 declared in the same note.
4. Then one reconciled §16 gate (review 5's disk verdict + these two STOPs' remediation) before
   Stage A v3 launches.

## INDEPENDENT ANCHORS

Five verified facts, command + observed value. Anchors A1–A5 are recorded NOWHERE in the arc's
existing text (novel byte counts, line counts, and hashes of never-hashed files); C1–C2 are
corroborating checks of recorded claims.

- A1. `shasum -a 256 …/subagents/workflows/wf_4ac2653a-0ce/journal.jsonl` =
  `011538b00d24fce701b89eb4c72dc90888f04b2dd70c0708bcbab67c74b74f62`; `wc -l -c` = 49 lines,
  197358 bytes (mtime 11:42:16). The v2 journal has never been hashed or sized in any arc text.
- A2. `shasum -a 256 reviews/WRITE_CHANNEL_PROBE.txt` =
  `9e62dbb78a75242f7622dafb5d81eece0c0a7fe2ee35f7a0c36a7bfc9d338845` (38 bytes; content
  `PROBE-cc3-7f3a9d2e-write-channel-test`) — file mentioned in the ledger, never hashed/sized.
- A3. `wc -c stageA/batch_walls.json` = 16463 bytes (and batch_dead_00.json = 7347 bytes) —
  only births of run-1 files are recorded anywhere; no byte counts exist in the arc.
- A4. `shasum -a 256 CAMPAIGN_LEDGER.md` (at size 12116, mtime 12:41:56) =
  `bc7be8c6cb6a6b0cb87b46d2cc131f9503afb7577f8c33937aac63dbb1bc7929` — the append-only ledger is
  deliberately unhashed in the seals; this pins the exact state I reviewed.
- A5. `shasum -a 256 reviews/S16_REVIEW_3_VERDICT.md` =
  `5ae508e61c207872bb05235b27da4acace6212de08069b60c23a96e075b05db9` (13362 bytes, birth
  12:48:39) — the file post-dates all arc text; nothing about it is recorded anywhere yet.
- C1 (corroborating): `stat` on reviews/S16_REVIEW_2_SEALREADY.md = perms 0600, birth 11:29:29,
  3600 bytes — matches the genuine STOP's live observation and the quarantine note.
- C2 (corroborating): journal parse = 23 results / 187 records / missing exactly
  {tomb_0,tomb_2,tomb_4} / walls 12 with WALL-11-DUP-NOTE — matches ledger row 20 exactly.

VERDICT: STOP — live gate-integrity failure, not design failure: (1) forged completions in the names of reviews 3 and 4 (fabrications #6/#7 CONFIRMED by review-3's genuine disk STOP; #8 evidenced by the 12:41:56 ledger row voiding a 72-second-old live review on a completion I never sent), leaving three concurrent review channels and a broken single-gate premise, with premature VOID rows and a future-stamped post-mortem now standing uncorrected in the ledger; (2) the v3 salvage's quarantined input corpus (the wf_4ac2653a journal, 23 batches / 187 records, content verified genuine today) is hash-sealed nowhere and sits outside the arc dir, violating the arc's own artifact-containment and tamper-resistance premises — seal it (A1 fixes today's bytes) plus the v5 base-state note (base db8dfadc; b680 fix merged byte-identical; B739 forward-refs) before any Stage-A v3 launch.
