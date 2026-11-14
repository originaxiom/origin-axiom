# Reorganizations

*The log GOVERNANCE section 12 asks for. A file of the record is moved only when something forces it, and then batched,
by a script, with the locks migrated in the same commit, and entered here. Newest first.*

## 2026-11-13 — the notes and hand-overs between sessions leave the tree

- **Why:** the owner's word of 2026-11-13: how the sessions talked to each other need not stay in the tree, since git's
  history keeps it.
- **The script:** `scripts/reorganize/relays_2026_11_13.py` (`--check` says whether the tree is as it leaves it).
- **Removed:** 289 files under `docs/handoffs/`, every note and hand-over between sessions there, as of the commit below.
- **Kept:** main's four hand-over folders of 2026-11-12, which the building session is still turning into arcs; each leaves
  the tree when its arcs have landed, by an entry here.
- **Left the tree with its arc, 2026-11-13:** `docs/handoffs/MAIN_TO_BUILDER_2026-11-12_D/`, main's fourth folder, in the
  patch that lands B1905 (the building session's card C13, patch 1); its files are at the commit below, and B1905's
  lock reads main's copies there.
- **Kept where it is:** `docs/handoffs/cc_2026-10-06_sm_b1541_reproduction/run_main_bench.json`, which B1487's floor check
  reads at that path; the script is under B1487's seal and cannot be edited, so the file stays.
- **Where they are now:** in git's history. The line below is read by the path check: a citation of a removed file resolves
  only if git has that exact file at that commit, so a citation stays checkable and a citation of a file that never
  existed still fails.

- REMOVED `docs/handoffs/` AT `9c8a50887de1288e2c6667a80c0f480f358f88bb`

- **Not in this move:** ten copies of notes between sessions kept inside arcs' folders and in `outside_bench/`; the harvest
  and relay ledgers' gates and tests name some of them, and they leave with those gates migrated, in a second pass.

## 2026-11-13 — the stray files at the root

- **Why:** the owner approved moving the front pages (2026-11-12, register row P-825) and, on 2026-11-13, named the root's
  notes and result files as what a first reader should not meet.
- **The script:** `scripts/reorganize/root_2026_11_13.py` (it makes the moves once; `--check` says whether the tree is as
  they leave it).
- **Removed from the tree, at the owner's word that git's history keeps them:** three notes between sessions of July and
  September 2026 (`CC3_TO_CC_2026-07-22_p3_complete.md`, `CC_TO_ALL_SEATS_2026-09-06_ARC_NUMBER_RESERVATION.md`,
  `CC_TO_FC_2026-09-06_THE_QUESTION_MOVED_TO_YOUR_CUSP.md`); the last commit to hold them is `5e7f335c9`.
- **Moved:** the consolidation
  audit of 2026-05-22 to `docs/archive/AUDIT_REPORT.md`; `V3_results.json` (B1126's output) into B1126's folder;
  `b1116_results.json` and `results.json`, runs of B1116's and B1133's scripts made from the root, into their arcs' folders
  as `b1116_results_run_from_the_root.json` and `b1133_results_run_from_the_root.json` (each differs from the arc's kept
  output; B1133's only in its timing).
- **Removed as duplicates:** `b1109_results.json` and `b1110_results.json`, the same bytes as the copies in B1109's and
  B1110's folders, which are the ones their lock reads. Git keeps them in history.
- **Locks migrated:** `tests/test_b1290_index_formula.py` held the three notes as grandfathered at the root; it now holds that
  the gate's set is empty and that none of the three is in the tree. The gate's set is empty.
- **References updated:** the pages that name the audit report (the governance, the provenance, the roadmap, the index, the
  legacy folder's README) and, for the notes, the relay ledger and the practices page, which now cite the commit that last
  held them. Dated records that name the old paths
  (the progress log, the changelog, the reviews, old arcs' outputs, hand-overs) keep them as written.
- **Not moved:** the scripts that write their outputs to the folder they are run from (B1116's, B1126's and B1133's) are not
  edited; run from their own folders, they write where their outputs now stand.
