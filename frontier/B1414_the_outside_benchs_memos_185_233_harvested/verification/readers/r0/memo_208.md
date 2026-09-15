# Memo 208 — THE_TRIAGE_WAS_ALREADY_DONE.md

## 1. HEADLINE

"THE TRIAGE WAS ALREADY DONE, IN 2026, AND SEVEN OF ITS VERDICTS NEVER LANDED." No date header
on the memo itself; banked per `outside_bench/INDEX.md` row 208 as "1B, banked 2026-09-12".
Addendum 1, same session (2026-09-12), corrects one sentence but not the headline.

## 2. CLAIMS

1. A triage of `docs/OPEN_LEADS.md` L-numbered leads below L91 was already run on 2026-07-17 at
   `frontier/B666_leads_campaign/cellT/TRIAGE_TABLE.md` (38 rows, 17 SUPERSEDED). Grade:
   documentary fact, verified.
2. Applying an 18-word "did it land?" test: **17 SUPERSEDED, 10 applied, 7 NOT APPLIED, 0 rows
   missing.** Grade: computed count.
3. Seven specific leads (L54, L64, L65, L73, L74, L78, L26) carry NO resolution word in their own
   row despite the 2026-07-17 triage having adjudicated them SUPERSEDED with a cited decider.
   Grade: computed, table given.
4. Instrument limitation named: the word-test scans every row naming a lead, not just its own —
   L77 is falsely counted "applied" by this artifact; excluded from the count of seven. Grade:
   self-reported instrument caveat.
5. L26 is only PARTLY stale (structural half derived in-repo by B644; residual is external
   novelty attribution) — the other six are stale outright. Grade: qualified finding.
6. Five MORE leads (L53, L72, L112, L174, and L174's C5) are internally contradicted — the row
   says OPEN while another row in the SAME FILE (or the arc itself) says CLOSED/DONE. Grade:
   computed, quoted (e.g. L112: ":659 OPEN, ready" vs ":807 CLOSED", "same file 148 lines apart").
7. **THE COUNT: eleven leads read as live work and are not.** Grade: headline sub-claim, PROVED
   by direct quotation.
8. **INTERPRETIVE**: the failure is not analysis/effort but a missing write-back-owner; nothing
   here touches the leads' underlying mathematics (all cited math — B581 torsions, B656 clock
   law, B583 rank 6, L174 C1-C4, B1108 C5 — stands as correct). Grade: labelled INTERPRETIVE,
   fenced explicitly.
9. Not claimed: that eleven is the complete set (one file tested against one triage + five hand
   reads; `open_claim_sweep.py` flags 52 claims across twelve surfaces, 28 unexamined). Grade:
   explicit scope limit.
10. **ADDENDUM 1 (2026-09-12, same session): §4's "the write-back step has no owner" is
    CORRECTED — too broad.** `docs/HARVEST_LEDGER.md` and `docs/OPEN_PROBLEMS.md` gate D DO work
    as write-back loops (found by memo 209). Grade: **WITHDRAWN (partial)** — the memo's own
    ownership sentence in §4 is retracted; the eleven-lead count, the 17/10/7 split, and every
    quoted decider are explicitly held UNCHANGED.

## 3. CERTIFICATE

`outside_bench/certificates/the_triage_was_already_done.py` and
`outside_bench/outputs/the_triage_was_already_done.txt` both EXIST. "No seal" is declared in the
memo itself (substring/table tests on tracked files at HEAD) — nothing to hash-check.

Output's final section reads:
```
[OK ] L174 C5 read needs-specialist (now STRUCK)  (docs/OPEN_LEADS.md:1919)
[OK ] an arc titled C5 CLOSED NEGATIVE  (frontier/B1108_c5_archimedean/FINDINGS.md:1)
==============================================================================
ALL ASSERTIONS HOLD AT THIS HEAD.
==============================================================================
```
This is the certificate re-run AFTER the fix (memo 216) was applied — the output file on disk
already shows rows "now STRUCK", i.e. it reflects the post-correction state, not the
pre-correction state the memo's prose describes. The memo's prose verdict ("eleven leads read as
live and are not") agrees with the *original* run; the output file agrees with the fix having
landed. No disagreement — both are consistent with "the defect existed, then was fixed."

## 4. ON MAIN ALREADY?

**(b) Applied via the merge, directly in `docs/OPEN_LEADS.md`.** Every one of the seven
"NOT APPLIED" leads plus the four "contradicts itself" leads now carries an explicit
supersession stamp on main:

- `docs/OPEN_LEADS.md:71` (L26), `:270-271` (L54, and the merged-into-L53 row at `:521`),
  `:524` (L64), `:525` (L65), `:542` (L73), `:543` (L74), `:552` (L78), `:659`+`:807-808` (L112)
  all read: **"[SUPERSEDED IN PLACE 2026-09-12 — outside-bench memos 206/208/210/211/213/214/215;
  certificates `the_triage_was_already_done.py`, `the_seal_already_happened.py`. Struck text
  kept for provenance, not deleted.]"** with the struck original text kept via `~~...~~`.
- This was landed by `outside_bench` memo 216 ("THE CORRECTIONS APPLIED: FOURTEEN STATUS LINES
  SUPERSEDED IN PLACE"), confirmed by `git log -1 -- docs/OPEN_LEADS.md`-style provenance: commit
  `e15eaada` ("memo 216 -- the corrections applied: 15 status supersessions in place, 3 artifacts
  regenerated").

So memo 208's finding is not merely cited — it was **acted on**, the same week, on the exact file
it audited.

## 5. NEEDS COMPUTATION HERE

DOCUMENTARY for the core claim (it is a substring/cross-reference test on tracked markdown, not a
mathematical computation). The one thing worth independently re-running: **re-execute
`the_triage_was_already_done.py` against current HEAD** and confirm it still reports
"ALL ASSERTIONS HOLD" (i.e., that nobody has silently reverted the `docs/OPEN_LEADS.md` strikes
since 2026-09-12). Recipe: `python3 outside_bench/certificates/the_triage_was_already_done.py`
and diff its tail against the committed `outputs/the_triage_was_already_done.txt`; expected:
identical "ALL ASSERTIONS HOLD AT THIS HEAD."

## 6. SUPERSESSION

The headline is NOT superseded — it stands, and is furthermore CONFIRMED CLOSED (the recommended
fix was applied). §4's one interpretive sentence ("the write-back step has no owner") IS
superseded IN THE SAME MEMO by its own Addendum 1 (memo 209's finding that `HARVEST_LEDGER.md`
and `OPEN_PROBLEMS.md` gate D are working write-back loops). INDEX.md rows after 208 (through
233) name no further memo revisiting this one.

## 7. GRADE PROPOSAL

**ALREADY-ON-MAIN.** The audit's finding was converted into an actual fix on `docs/OPEN_LEADS.md`
within the same week (commit `e15eaada`, memo 216) — there is nothing left to bank; a verifier
should only spot-check that the strikes are still in place and the certificate still passes.
