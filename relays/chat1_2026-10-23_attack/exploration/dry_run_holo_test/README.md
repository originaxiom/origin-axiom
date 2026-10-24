# Dry runs of the holomorphic reading test's drafts (before its rule was sealed)

chat1, 2026-10-24. Code-path tests, labelled; disclosed in `HOLO_TEST_RULE.md`. Every row here is a row of TWO_HIGGS's
grid (`channel_store_two_higgs.npz`), compared with the data before (TWO_HIGGS; THE_NEXT_ATTACK §2); no row of the
holomorphic test's grid was computed. They ran in a scratch folder holding links to this folder's `channel_store.py`,
`inverse_higgs.py`, `sm_search.py`, `one_higgs_search.py` and the TWO_HIGGS store.

- **Run 1** (`driver.py`, outputs at the top of this folder): the first draft, with a stand-in store from TWO_HIGGS's
  rows (the ten α = 2/5 lines; Re τ 0.0625 and its mirror 0.9375; Im τ 2.0 and 2.1: 40 points, 80 rows) and 30 random
  targets from main's generator; modes C0, scan, C2, calibration (three best rows per target) and cells. A first attempt
  stopped in C0 (it asked for 40 targets after the driver had cut them to 30); fixed, rerun. `holo_test_draft.py` is
  that draft **with cell H4 added after the run** (copied in afterwards; the run itself had no H4, and its best rows all
  had D = 9).
- **Run 2** (`run2/`): the revised script after the referee (`holo_test_draft_v2.py`, which is the script committed after
  the rule): the same stand-in, 10 targets of main's generator and 20 lepton-tied; modes C0, scan, calibration (one best
  row per target) and cells. C3 reads False there only because the stand-in has 40 mirror pairs, not the rule's 100.
