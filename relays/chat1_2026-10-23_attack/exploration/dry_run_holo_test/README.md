# Dry run of the holomorphic reading test's draft script (before its rule was sealed)

chat1, 2026-10-24. A code-path test, labelled; disclosed in `HOLO_TEST_RULE.md`. Every row here is a row of TWO_HIGGS's
grid (`channel_store_two_higgs.npz`), compared with the data before (TWO_HIGGS; THE_NEXT_ATTACK §2); no row of the
holomorphic test's grid was computed. It ran in a scratch folder holding links to this folder's `channel_store.py`,
`inverse_higgs.py`, `sm_search.py`, `one_higgs_search.py` and the TWO_HIGGS store.

- `driver.py` builds a stand-in store from TWO_HIGGS's stored rows (the ten α = 2/5 lines; Re τ 0.0625 and its mirror
  0.9375; Im τ 2.0 and 2.1: 40 points, 80 rows), cuts the random targets to 30, and runs the draft's modes C0, scan,
  C2, calibration and cells.
- A first attempt stopped in C0 (it asked for 40 random targets after the driver had cut them to 30); fixed, rerun.
- `holo_test_draft.py` is the draft as run (the committed `holo_test.py` adds cell H4 and its D read-out; the cells
  were re-read with it on the same outputs). `holo_cells.json` here reads C3 False only because the stand-in has 40
  mirror pairs, not the rule's 100.
