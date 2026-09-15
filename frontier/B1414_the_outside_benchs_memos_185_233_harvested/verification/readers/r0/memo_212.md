# Memo 212 — THE_ARTIFACT_PAIR_SWEEP.md

## 1. HEADLINE

"THREE CELLS IN SEVENTY-FIVE, AND THE STALENESS RUNS BOTH WAYS." Banked per INDEX.md row 212:
"1B, banked 2026-09-12."

## 2. CLAIMS

1. Census over `frontier/`: 228 `results.json` files, 114 with an `output.txt` beside them, 113
   with a `compute.py` too, 75 carrying a verdict on both sides, 29 with a verdict on only one
   side (formatting gap, not contradiction), **3 (4.0%) where output.txt's verdict appears
   NOWHERE in results.json.** Grade: computed census.
2. "Three, not thirty" — the defect memo 211 found (one cell) is real but NOT endemic; a reading
   of memos 207-211 as "the record is broadly untrustworthy" is explicitly REFUSED. Grade:
   interpretive, stated as a correction of an over-generalization risk.
3. The three cells and which side is stale: **P2W5-L72** (output RESOLVED-A, json UNRESOLVED —
   the JSON is stale, 51 fields differ, records a failed h1=0 relator check from an old code
   version); **W2-270** (output UNRESOLVED, json RESOLVED-B — **the direction is reversed**: the
   text says depth 9-11 recomputation "did not complete," but the JSON already contains
   `r_seq_depths_7_11` with 5 entries plus an Aitken extrapolation — the text is the stale one,
   and both files were committed in the SAME commit, already inconsistent); **W4-017r** (output
   RESOLVED-A after "total runtime 598.6s", json PENDING_PART_B with only a `part_A` key — a
   mid-run snapshot never rewritten, CONFIRMED by re-running the unmodified `compute.py`
   (469.9s, RESOLVED-A, full six-key results.json)). Grade: each computed / settled by re-running
   the cell's own code (two of three) or by reading (one of three).
4. "No mathematics is wrong in any of the three" — P2W5-L72's splitting independently reproduced
   in memo 211; W2-270's structural obstruction untouched by which verdict string is right;
   W4-017r's part A and part B both ran and are both in its text. Grade: fenced, explicit.
5. **INTERPRETIVE**: staleness runs BOTH WAYS — no privileged artifact ("always trust the JSON"
   or "always trust the text" would each be wrong 1-in-3 times); a cell's two outputs are only as
   trustworthy as the run that wrote them, and nothing in the tree records whether that happened.
   Grade: labelled INTERPRETIVE.
6. Proposed fix (not applied by this bench): write `results.json`/`output.txt` in the same
   process exit path, and gate that every cell with a verdict on both sides carries the SAME one
   — "that check IS this certificate." Three named files to regenerate:
   `P2W5-L72/results.json`, `W2-270/output.txt`, `W4-017r/results.json`. Grade: recommendation,
   not an action ("not this bench's to apply").
7. Fence: the census tests ONLY whether a verdict string in output.txt appears in results.json —
   it does not compare numeric content, does not re-run the 113 cells with a compute.py, and says
   nothing about the 29 one-sided or 114 no-output.txt cells. "A cell passing this check is not
   thereby verified." Grade: explicit scope limit.

## 3. CERTIFICATE

`outside_bench/certificates/the_artifact_pair_sweep.py` and
`outside_bench/outputs/the_artifact_pair_sweep.txt` both EXIST. No seal declared (a census over
tracked files at HEAD). Output tail:
```
[OK ] results.json says RESOLVED-B, depth 7-11 sequence: 5 entries
  => REGENERATED (860.0s, depths 7..11 all completed). Pair agrees.
  ...
[OK ] results.json NOW says RESOLVED-A, keys [...]
  => REGENERATED from the committed compute.py (474.8s). Pair agrees.
==============================================================================
ALL ASSERTIONS HOLD AT THIS HEAD.
==============================================================================
```
Note: like memo 208, the committed output file reflects the POST-FIX state ("NOW says...",
"REGENERATED") — i.e., this output was (re-)run after the three files were already corrected. It
agrees with the memo's narrative of what was found and then fixed; final verdict line ("ALL
ASSERTIONS HOLD") is consistent with the headline once the fix is applied — it does not
contradict the "three defects existed" claim, it confirms they no longer do.

## 4. ON MAIN ALREADY?

**(b) Applied via the merge — directly regenerated on main.** `git log -1` on each of the three
named files shows all three last touched by the SAME commit:
```
e15eaada  memo 216 -- the corrections applied: 15 status supersessions in place, 3 artifacts regenerated
  frontier/B775_phase2_wave1/cells/P2W5-L72/results.json
  frontier/B771_phase1_wave1/cells/W2-270/output.txt
  frontier/B771_phase1_wave1/cells/W4-017r/results.json
```
Additionally the *systemic* fix (the proposed gate, explicitly declined by this memo as "not this
bench's to apply") **was also built**: `scripts/checks/artifact_pair_gate.py` and
`tests/test_artifact_pair_gate.py` both exist on main (installed per INDEX.md row 217, "THE GATE
IS INSTALLED: A CELL'S TWO ARTIFACTS CAN NO LONGER CONTRADICT EACH OTHER SILENTLY. Owner-
authorized.").

## 5. NEEDS COMPUTATION HERE

- **Claim 1 (the census)**: DOCUMENTARY in nature but has a concrete recipe — walk `frontier/**`
  for `results.json`, pair each with an adjacent `output.txt`, and check whether the output's
  verdict token (e.g. `RESOLVED-A`, `UNRESOLVED`) appears anywhere in the JSON's text
  representation. Recipe: `python3 outside_bench/certificates/the_artifact_pair_sweep.py`,
  expect `228 / 114 / 113 / 75 / 29 / 3` unless new cells were added or the three fixed cells
  regressed.
- **Claim 3, W4-017r**: the one claim with a real numeric computation behind it — rerun
  `frontier/B771_phase1_wave1/cells/W4-017r/compute.py` against its one dependency
  (`B461_relation_r2_borromean/ptolemy_systems.json`) in an isolated copy and confirm it reaches
  `VERDICT: RESOLVED-A` with a six-key results.json in well under 600s (memo reports 469.9s /
  474.8s on two separate runs).
- **The gate (claim 6's fix)**: run `tests/test_artifact_pair_gate.py` to confirm the installed
  gate actually fires on a synthetic mismatched pair (not exercised by this reader per the
  ≤2-minute-computation rule, but a fast, obvious check for a verifier).

## 6. SUPERSESSION

Not superseded. It is itself a follow-up to memo 211 (which found the first cell) and is
followed by memo 216 (applies the three fixes) and memo 217 (installs the permanent gate) — both
strict *confirmations/extensions*, not reversals. INDEX.md rows after 212 through 233 name no
memo disputing the 3-in-75 count.

## 7. GRADE PROPOSAL

**ALREADY-ON-MAIN.** All three flagged artifact pairs were regenerated on main in the same commit
(`e15eaada`) and a permanent structural gate against recurrence was installed and lives at
`scripts/checks/artifact_pair_gate.py` — nothing here is left open for a verifier to bank; the
useful residual action is periodic re-running of the sweep/gate, which is now automated.
