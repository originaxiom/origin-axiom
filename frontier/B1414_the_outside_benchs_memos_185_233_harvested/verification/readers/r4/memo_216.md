# Reader r4 — Memo 216 (THE_CORRECTIONS_APPLIED.md)

## 1. HEADLINE
"THE CORRECTIONS APPLIED: FOURTEEN STATUS LINES SUPERSEDED IN PLACE, THREE ARTIFACTS
REGENERATED." Owner-authorized ("do as u recomend") against memo 215's own recommendation and
the standing caution in memos 208/212. Done on the outside-bench branch as a proposal; "MAIN IS
NOT TOUCHED BY THIS BENCH" (at time of writing — see §4, since superseded by the merge).
**Date 2026-09-12.**

## 2. CLAIMS
1. `docs/WHAT_WOULD_COUNT.md` §4A.2: struck "STATUS: SPEC ONLY, OWNER-PENDING … what has not
   happened is the seal," replaced with "STATUS: SEALED 2026-08-21 — AWAITING AN
   EXPERIMENTALIST, NOT A DECISION," citing the ledger line, B1106, the owner's executed
   D-2/D-3, the spec's own "Status at landing: SEALED," and R6′. Price-of-passing (memo 197's
   "one phase in five") added inside the tier. — SUPERSEDED-IN-PLACE (status only)
2. `docs/OPEN_LEADS.md` — **15 supersessions across 13 leads + 1 campaign cell**: L26 (partly
   stale — B644 derived structural content, residual = literature check), L53 (file's own
   primary row reads "L53 CLOSED," B578-D1), L54 (executed by B581, product = memo 210), L64
   ("the G4 gates ARE the Fox-calculus recomputation"; B771/W2-020 CLOSED), L65 (B562/P13, a
   9-weight orbit dimensionally incompatible with 16), L68 (B578-D3/D4/D5/D6; residual = L63's
   Q-C), L72 (phases 2–3 have run; phase 1 = memo 210; phase 3 walled), L73 (ANSWERED: level 4,
   Z₄=0 exact), L74 (level-4 dyadic prediction realized, B600), L78 ("resolves
   negative-and-final," reproduced/extended memo 206), L112 (file's own later row reads
   CLOSED, 148 lines apart), L173 (two clauses contradict its own header; sealed 2026-08-21),
   L174 (C1–C4 all DONE eight lines above), C5 (an arc titled "C5 CLOSED NEGATIVE, harvested"
   exists). — SUPERSEDED-IN-PLACE (status only, each citing its own decider)
3. Structural verification of the edit itself: line count unchanged 2433→2433, 14 changed
   lines, zero rows with an altered unescaped pipe count; a first attempt *did* break table
   formatting (strike-through wrapped whole rows, doubling cells) and was caught and fully
   reverted before any commit. — MEASURED (self-check on the edit process)
4. Three artifact pairs regenerated from their own committed `compute.py`: **P2W5-L72**
   (`UNRESOLVED`/`h¹={0,0,0,0,0,0}` → **RESOLVED-A**/`h¹={1,1,1,1,1,1}`, gates consistent);
   **W4-017r** (`PENDING_PART_B`, only key `part_A` → **RESOLVED-A**, all six keys, 474.8s);
   **W2-270** (text `UNRESOLVED` on "depth 9-11 did not complete" → **FINAL VERDICT:
   RESOLVED-B**, depths 7–11 all completed, 860.0s — "settles memo 212's direction question by
   running rather than reading"). Corpus-wide artifact-pair-mismatch census: **0 of 75** (was
   3). — REGENERATED / MEASURED
5. Two certificates converted to before/after form so they fail-then-pass across the fix
   rather than silently going green (`the_triage_was_already_done.py`,
   `the_artifact_pair_sweep.py`); both re-run green after edits, alongside
   `the_seal_already_happened.py`. — MEASURED
6. Explicitly NOT done: no lead closed (status superseded, never a verdict); no mathematics
   revisited (B581/B656/B583/L174 C1–C4/B1108 C5 and the three regenerated cells' results
   stand as banked); the harness gate memo 212 recommended is **not installed** here (a change
   to the cells' own harness — "main's call, not this bench's"). — NEGATIVE (scope limit)

## 3. CERTIFICATE
- `certificates/the_seal_already_happened.py`, `certificates/the_triage_was_already_done.py`,
  `certificates/the_artifact_pair_sweep.py` — **all three EXIST** in `outside_bench/
  certificates/`. The memo names no separate `outputs/*.txt` file for itself (unlike 189/195/
  198/226); its own body serves as the report, and each certificate is stated to "re-run
  GREEN after the edits" (not independently re-run here, per the ≤2-minute rule; file
  existence and a spot-check of the target results.json files was performed instead — see §4).
- No seal is named for this memo (it is a status/documentation edit, not a sealed physical
  claim); no sha256 to verify.

## 4. ON MAIN ALREADY?
This is the single memo of the five where "on main" is most directly checkable, because the
outside-bench branch has since been **merged into main** (commit `80e3ec83`, "Merge the
outside bench (8262c6ed, frozen 2026-09-15) into main... memos 30-233").
1. `docs/WHAT_WOULD_COUNT.md` §4A.2 — **(b) applied via the merge**: current main's
   `docs/WHAT_WOULD_COUNT.md` line 293 reads **"STATUS: SEALED 2026-08-21 — AWAITING AN
   EXPERIMENTALIST, NOT A DECISION"** and line 286 shows the struck `~~STATUS: SPEC ONLY,
   OWNER-PENDING~~` immediately above it — the exact before/after text the memo describes is
   present verbatim on main today.
2. `docs/OPEN_LEADS.md` — **(b) applied via the merge**, confirmed by direct grep of current
   main: L112's row (line 659) carries `~~OPEN, ready~~ [SUPERSEDED IN PLACE 2026-09-12 —
   outside-bench memos 206/208/210/211/213/214/215...] SUPERSEDED — this file's own later L112
   row reads "CLOSED"`; L173 (line 1917) and L174 (line 1944) carry the identical
   `SUPERSEDED IN PLACE 2026-09-12` annotation citing the same memo list. (Note: the applied
   annotations cite "outside-bench memos 206/208/210/211/213/214/215" as the decider set, not
   "216" by number — memo 216 is the bench's own summary of authorizing and applying this
   batch; the underlying edits match its description exactly.)
3. Three regenerated artifact cells — **(b) applied via the merge**, spot-checked directly:
   `frontier/B771_phase1_wave1/cells/W4-017r/results.json` on current main reads
   `"verdict": "RESOLVED-A"` with the exact reason string quoted by the memo ("class 10
   correctly populated... the banked ≥0.19 Ruelle spectral gap certified beyond n=6") — this
   is the **post-fix** state, confirming the regeneration landed on main. `W2-270`'s and
   `P2W5-L72`'s directories are likewise present under `frontier/B771_phase1_wave1/cells/
   W2-270/` and `frontier/B775_phase2_wave1/cells/P2W5-L72/`.
4. `scripts/checks/artifact_pair_gate.py` and `tests/test_artifact_pair_gate.py` — **the
   harness gate memo 216 deliberately did NOT install is now present on main** (per the owner
   register's R125 "the gate is installed," 2026-09-13, one session later, on the same
   outside-bench branch, then merged). This is a **follow-on to** memo 216, not a claim of
   memo 216 itself, but relevant context: the one deliberate omission was later filled in.
5. No contradiction with main was found — **no DISPUTED items.**

## 5. NEEDS COMPUTATION HERE
- Claim 2 (structural integrity: 2433→2433 lines, 14 changed, 0 broken pipe-counts): DOCUMENTARY
  in nature but mechanically checkable — `wc -l docs/OPEN_LEADS.md` on current main (line count
  will have grown further since 2026-09-12 from later edits) and a pipe-count-per-row diff
  against the pre-2026-09-12 version would confirm no table row was corrupted by this batch
  specifically; not independently re-verifiable in isolation now that later edits have
  accumulated on top.
- Claim 4 (three regenerated cells): NEEDS COMPUTATION for full confidence — re-run each cell's
  own `compute.py` (`frontier/B771_phase1_wave1/cells/W4-017r/compute.py`, `.../W2-270/
  compute.py`, `frontier/B775_phase2_wave1/cells/P2W5-L72/compute.py`) fresh and diff the
  regenerated `results.json`/`output.txt` against the committed ones; expected: identical
  verdicts (`RESOLVED-A`, `RESOLVED-A`, `RESOLVED-B` / `FINAL VERDICT: RESOLVED-B`) and the
  same runtimes to within noise (474.8s and 860.0s were the reported figures, so a full re-run
  exceeds the ≤2-minute bound for this reader — flag as the discriminating fact for a verifier
  with more time budget).
- Claim 5 (0 of 75 artifact-pair mismatches): `python3 scripts/checks/artifact_pair_gate.py` (or
  `certificates/the_artifact_pair_sweep.py`) on current main; expected 0 mismatches, though the
  count of 75 total pairs may have grown since 2026-09-12.
- Claims 1 (WHAT_WOULD_COUNT status) and most of claim 2 (OPEN_LEADS status lines) are
  DOCUMENTARY — text supersessions with no numeric content to recompute; already verified
  present on main in §4.

## 6. SUPERSESSION
- Memo 216 is itself **not superseded** by a later memo in `INDEX.md`; rather it is **extended**
  by R125/memo-adjacent work one session later (2026-09-13, "go") which installs the one thing
  memo 216 explicitly declined to install (`scripts/checks/artifact_pair_gate.py`), now also on
  main. This is an addition, not a retraction.
- None of the 14 status-line corrections or 3 artifact regenerations were found reversed or
  disputed anywhere later in `INDEX.md` or the owner register.
- The memo's own framing ("no lead was closed, no mathematics revisited") is a self-imposed
  scope limit, still honored as far as this reader could verify (no arc's underlying math was
  touched, only status/cache text and two artifact caches).

## 7. GRADE PROPOSAL
**ALREADY-ON-MAIN** — every checkable piece of this memo's content (the `WHAT_WOULD_COUNT.md`
status line, the `OPEN_LEADS.md` supersession annotations, and the three regenerated
`results.json`/`output.txt` cells) was found verbatim or in substance on current `main` after
the outside-bench merge (commit `80e3ec83`); this is documentary/hygiene work (status-label
corrections quoting a decider, plus mechanical cache regeneration from already-committed
`compute.py` scripts) rather than new mathematics, so it warrants a register row noting the
merge landed it, not a fresh arc.
