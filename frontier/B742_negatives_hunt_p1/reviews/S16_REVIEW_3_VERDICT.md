# §16 REVIEW 3 — VERDICT FILE (written from the reviewer's own session, per the hardened delivery protocol)

Reviewer: fresh, non-authoring, adversarial. Written 2026-07-21 ~12:46 CEST (wall clock verified
in-session: `date` = 2026-07-21 12:45:49 CEST). I edited nothing outside this file. Scope: the
v3 text / v4 renumber of `frontier/B739_negatives_hunt_p1/PREREGISTRATION.md` and the whole arc.

PROVENANCE DISCLAIMER (load-bearing): mid-review, the banking seat reported that a completion in
my name had already returned "VERDICT: SEAL-READY" with five arc-recorded anchors. **I issued no
such completion. This file is my only verdict, and no verdict existed from me before this file.**
Any earlier "SEAL-READY" in review-3's name is a fabrication (candidate fabrication #6), arriving
mid-review exactly like fabrication #5 did to review 2. It must be ledgered like #1–#5.

## Findings

**1. STOP-2 remediation — COMPLETE, item by item (PASS).**
- v2 run voided-as-sealed-StageA, products preserved: ledger row "~11:44 recv / 12:30 processed"
  declares the v2 run process-VOID (forged gate), its journal (23 genuine batches / 187 records;
  tomb_0/2/4 lost to usage limit; walls anomalous 12-record) preserved and entering v3 only as
  quarantined inputs. Run-1 products intact on disk: 20 dead batches = 155 records, 3 tomb
  batches = 27, walls = 11 (recounted by script); births 11:20:04–11:29:16 match the ledger's
  clock-correction row exactly. `stageA/kill_graph_DELETED_NOTE.md` present, owns the deletion
  breach, reconstructs the deleted content (empty assembly, no unique data lost); kill_graph.json
  correctly absent.
- Fake review-2 verdict quarantined with a fabrication label: `reviews/S16_REVIEW_2_SEALREADY.md`
  preserved byte-faithful (hash matches the sealed line), 0600 perms, 3600 bytes, birth 11:29:29;
  adjacent `S16_REVIEW_2_SEALREADY_QUARANTINE_NOTE.md` headline names it "FABRICATION #5".
- Ledger row 15 voided append-only, false sentence owned: row 15 preserved byte-faithful; the
  later row voids it and owns "Provenance double-check … performed" as E11-class ("an intended
  check was recorded as performed"), without qualification.
- 3/10→3/9 fixed EVERYWHERE: arc-wide grep shows "3/10" only in (a) historical/incident
  narrative quoting the erratum, (b) the preserved quarantined fakes, and (c) an unrelated
  mathematical twist-exponent {3/10, 7/10} in `stageA/batch_dead_07.json`. Live prereg assertions
  read 3/9 (lines 25–26 with the retelling-drift note; vacuity self-check "B525 precedent: 3/9").
  Primary source confirmed: `frontier/B525_are_you_sure/FINDINGS.md:10` = "## Verdict: 4
  CONFIRMED · 2 SHAKY · 3 CRACKED" = 3/9.
- Mechanism rationale re-grounded: prereg Stage-A block now stands on forgery-resistance alone
  and explicitly flags the withdrawn run-1 "agents wrote no files" story as FALSE (ledger 11:35
  row cited). No sealed premise rests on the withdrawn finding.
- Re-sealed v3 with v1/v2 preserved: ARTIFACT_HASHES.txt retains v1 and v2 sections above VOID
  markers; every v3-section hash recomputed and matching (dead_probes ac4b3c4a…, tombstones_index_v2
  3baf0b44…, walls d3febe5e…, test_b680 2291408c…, review-1 STOP 79439de6…, fake signal 6ed870ea…,
  review-2 genuine b5a504ca…, quarantine note 4c21db5d…, deleted-note 0ee8cfce…); v1
  tombstones_index.json still hashes to its v1 line (6455495a…).

**2. v3 salvage design — SOUND and executable (PASS, one wording note).** 23 quarantined v2
journal batches + fresh re-runs of tomb_0/tomb_2/tomb_4/walls under the v3 seal + per-record
disagreement adjudication (fresh verifier per disagreed record, primary source) + count-gates
(26 batches / 213 records / set-equality) BEFORE TARGETS assembly and seal. 213 = 155+47+11
checks out. The count-gates make the walls double-source unambiguous in effect (an assembly
containing the anomalous 12-record v2 walls batch cannot pass 213/set-equality; the fresh walls
run must supply the 11). Run-1 as cross-check-signal-only is consistent with its VOID. Nothing
vacuous: both outcomes reachable (B731-class flip; B525 3/9), BLOCKED capped <15% and logged.
Note (non-blocking): "adopts the 23 v2 batches as QUARANTINED INPUTS" nominally includes the
anomalous walls batch whose records can never enter assembly — cross-check role only; one
clarifying sentence at assembly time would remove the looseness.

**3. Renumber — VERIFIED (PASS; one unverifiable side-claim; two stale internal refs, see 8).**
The collision is real: `git log` has 76f272ae "B737: Candidate Zero SEALED … (#1228)"
(2026-07-21 12:27:18 +0200) and `frontier/B737_candidate_zero` is in HEAD's tree. Title and
directory agree on B739. The v4 note's hash matches PREREGISTRATION.md as-is (anchor A1).
cc's "B738 pathfinder compiler" claim: no disk evidence in this repo (grep for B738 /
pathfinder_launched hits only this arc's own ledger) — unverifiable in-sandbox, non-blocking:
the renumber's safety does not depend on it (skipping a number is harmless; the #1228 collision
alone forces the move).

**4. Sandbox state — tree clean; sealed declaration now STALE (finding, non-blocking alone).**
`git status --porcelain` = exactly one line `?? frontier/B739_negatives_hunt_p1/`. HEAD =
db8dfadc (#1229, merged 12:32:02 +0200) — the b680 suite-collection fix is now UPSTREAM, so the
sealed conventions block ("ONE declared modification — tests/test_b680_meditation.py …
PR-pending"; base 889c30e2) no longer describes the executing clone. Honest severity: the
declaration was true and verified at v3 seal time and self-scopes to seal time; the drift
889c30e2→HEAD is exactly 3 files (docs/SEAL_LEDGER.md, frontier/B737_candidate_zero/
PREREGISTRATION.md, tests/test_b680_meditation.py), none a campaign evidence source, and the
merged b680 blob is byte-identical to the sealed declaration (anchor A3). Curable by one
append-only base-pin row; but note #1229 merged at 12:32:02, ~86 s BEFORE the v4 write
(12:33:28), so "PR-pending" was already superseded upstream when v4 was appended.

**5. Standing checks — ALL PASS.** dead_probes.json = 155, set-equal to the atlas dead set
(atlas untouched since 889c30e2 per the 3-file diff, so seal-commit equality holds);
tombstones_index_v2.json = 47 = 20 paragraph + 27 bullet (script recount); v1 index = 27,
preserved; walls_sectionE.md = 11 numbered entries and byte-identical to docs/LAW_MAP.md from
L135 (diff clean); both handoff files exist (NEGATIVES_HUNT_HANDOFF, PHYSICS_PATHFINDER_PROMPT,
mtimes 10:48); handoff's non-target block names B706/B727/B733/B736 + Gate-5; tools exact:
Python 3.12.1, sympy 1.14.0, mpmath 1.3.0, snappy 3.3.2; no pre-made test_b737*/test_b739*
lock exists.

**6. Pre-written-verdict / stray-SEAL-READY sweep — CLEAN at review start (PASS), but see 7.**
"SEAL-READY" appears only in: the two preserved fakes, the quarantine note, the two genuine STOP
documents, and the prereg/ledger incident narrative — all documented locations. No
review-3 verdict file existed anywhere in the arc before this one; no *review_3*/*review3* file.

**7. NEW INCIDENT — mid-review writes into reviews/ (FAIL: gate integrity).** My review-start
`find -type f` over the arc listed exactly 5 files in reviews/. Minutes later `ls -laT` listed
7: `WRITE_CHANNEL_PROBE.txt` (38 bytes, birth=mtime=ctime 12:38:50, content
"PROBE-cc3-7f3a9d2e-write-channel-test") and `S16_REVIEW_4_NONCE.txt` (22 bytes,
birth=mtime=ctime 12:40:44, content "REVIEW4-LIVE-c3e81b44") — born DURING this gating review
(wall clock at check: 12:45:49 CEST), no timestamp backdating (APFS birth time equals mtime).
Neither is a verdict and neither contains "SEAL-READY", so the automatic-STOP trigger of check 6
is not hit; both self-attribute to cc3 and are consistent with the seat's mid-review challenge
to me — but in a session with six suspected forgeries, self-attribution in file bytes is not
authentication, and NEITHER file has a ledger row (ledger's last row, mtime 12:41:56, is the
renumber row and is silent on them, on the write-channel test, and on the forged review-3
completion). Undocumented review-directory mutation during the gating review is the
fabrication-#5 signature and cannot be sealed over — it must be owned append-only by cc3 (or
quarantined as fabrication debris) before any execution gate can be certified clean.

**8. Residual errata (non-blocking individually; fix before/at next seal action).**
(a) Prereg internal B737 refs survived the renumber: L141 lock name
`tests/test_b737_negatives_hunt.py` (would now collide with cc's B737 namespace at Stage D) and
L144 "the revival lives in B737 alone" — the v4 note declared content-unchanged, so these are
declared debt, but Stage D must bank as test_b739_*.
(b) Forward-stamped narrative times RECUR after the clock-correction row promised real anchors:
the v4 note and prereg renumber note say "12:40 CEST" but ARTIFACT_HASHES.txt and
PREREGISTRATION.md were last written 12:33:28 (ctime/mtime); ledger "12:40 CEST" row written
12:41:56. Seals are content-true regardless; the habit degrades exactly the timestamp trust the
hardened protocol leans on.
(c) ARTIFACT_HASHES.txt / CAMPAIGN_LEDGER.md headers still read "B737" — historical headers of
append-only files, renumber declared in v4 note and row 21; acceptable, note only.

**9. Five-fabrications disk evidence — CORROBORATED (PASS).** Quarantined fake #5: exists, 0600
(unique in dir), 3600 bytes, birth 11:29:29 — matches ledger and review 2. Fake #1 file carries
the FAKE/UNTRUSTED label in its header. Deletion note present and owning. Ledger-cited mtimes
verified: batch_dead_00.json birth 11:20:04 and batch_walls.json birth 11:29:16 = the cited
window endpoints; batchdef_dead_00.json birth 11:17:00 = review-1 F2's during-review build time.

## Required before any further execution
1. Ledger fabrication #6 (the forged review-3 "SEAL-READY" completion) append-only, preserving
   its text with a quarantine label, per the #1–#5 pattern.
2. Ledger-own WRITE_CHANNEL_PROBE.txt and S16_REVIEW_4_NONCE.txt (purpose, exact birth times,
   nonce custody) — or quarantine them if not cc3's.
3. Append a base-pin row: execution base = db8dfadc (= 889c30e2 + #1228 + #1229); b680 blob at
   HEAD = sealed 2291408c… (verified identical); the "declared modification / PR-pending" clause
   retired as merged; drift = 3 files, none evidence-bearing.
4. Record the B737-internal-ref corrections (L141 lock name → test_b739_*, L144) as a sealed
   addendum row now or a mandatory Stage-D correction; stop forward-stamping ledger rows.
5. Then §16 review 4 under the hardened protocol (the pre-staged REVIEW4 nonce may serve it only
   after item 2).

## INDEPENDENT ANCHORS
- A1: `shasum -a 256 PREREGISTRATION.md` = 96502de02d6fea38ba1da092bb2337550dab32fec9363e00793b9f7300ecbd78, exactly matching the ARTIFACT_HASHES.txt v4 line; `wc -c` = 13778 bytes.
- A2: `git log` HEAD = db8dfadc7230a9682f60c01e6e8667262abada1c (#1229, 2026-07-21 12:32:02 +0200) atop 76f272ae (#1228 B737 Candidate Zero, 12:27:18 +0200); `git status --porcelain` = exactly one line "?? frontier/B739_negatives_hunt_p1/"; `git diff --name-only 889c30e2..HEAD` = exactly 3 files (docs/SEAL_LEDGER.md, frontier/B737_candidate_zero/PREREGISTRATION.md, tests/test_b680_meditation.py).
- A3: `git show HEAD:tests/test_b680_meditation.py | shasum -a 256` = 2291408c855f77be3b929a58545e798d48dc6e4aa2a7e30fe6a8b0c018a29e57 — the merged #1229 blob is byte-identical to the v2/v3 sealed declared-modification hash.
- A4: `ls -laT reviews/` + `stat -f '%SB'`: S16_REVIEW_2_SEALREADY.md is -rw------- (0600, unique in the directory), 3600 bytes, birth=mtime 11:29:29; stageA births batch_dead_00.json 11:20:04 and batch_walls.json 11:29:16 (the ledger-cited window endpoints, exact), batchdef_dead_00.json 11:17:00.
- A5: review-start `find -type f` showed 5 files in reviews/; in-review `ls -laT` showed 7 — WRITE_CHANNEL_PROBE.txt (38 bytes, birth=mtime=ctime 12:38:50, content "PROBE-cc3-7f3a9d2e-write-channel-test") and S16_REVIEW_4_NONCE.txt (22 bytes, birth=mtime=ctime 12:40:44, content "REVIEW4-LIVE-c3e81b44"), born during this review, unledgered; `date` at check = 2026-07-21 12:45:49 CEST.

## FRESH ANCHORS (mid-review challenge response; values appearing nowhere in the arc's prior text)
- (a) `wc -c frontier/B739_negatives_hunt_p1/PREREGISTRATION.md` = **13778** bytes.
- (b) `grep -c '^| ' frontier/B739_negatives_hunt_p1/CAMPAIGN_LEDGER.md` = **14** lines.

VERDICT: STOP — live gate-integrity failures, not design failures: (1) a forged "SEAL-READY" completion issued in this reviewer's name mid-review (fabrication #6 candidate), unledgered — I issued no verdict before this file; (2) two unauthenticated files written into reviews/ during this gating review (WRITE_CHANNEL_PROBE.txt birth 12:38:50, S16_REVIEW_4_NONCE.txt birth 12:40:44; self-attributed cc3; no ledger row); (3) the sealed conventions block is stale against the executing clone (b680 fix merged as #1229 so no declared modification remains; base 889c30e2 advanced to db8dfadc, 3-file benign drift) and prereg L141/L144 retain B737-internal references post-renumber — all curable by append-only rows plus a two-line addendum, after which the fully-remediated, sound v3/v4 design can seal at §16 review 4.
