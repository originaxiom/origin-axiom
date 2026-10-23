# Dry runs of the reading test's draft script (before THE READING TEST's rule was sealed)

chat1, 2026-10-23. Code-path tests, labelled; disclosed in `READING_TEST_RULE.md`. Every row here is a row of TWO_HIGGS's
grid (`channel_store_two_higgs.npz`), compared with the data before (THE_NEXT_ATTACK §2); no row of the reading test's
grid was computed. They ran in a scratch folder holding links to this folder's `channel_store.py`, `inverse_higgs.py`,
`sm_search.py` and the TWO_HIGGS store; paths are shown relative to it.

- `driver.py` builds a stand-in store from TWO_HIGGS's stored rows (the ten α = 2/5 lines; Re τ 0.0625 and its mirror
  0.9375; Im τ 2.0 and 3.5: 40 points, 80 rows) and runs the draft's modes C0, scan, C2 and cells on it.
- `run1/`: the first draft (search called without `n_extra = 4`, a bug; C2 without noise, success at χ² ≤ 0.1). Its
  planted control reached 22 of 24; the two misses (|h·h| ≈ 3 × 10⁻⁴) stopped at 0.217 and 1.2. That draft was not
  kept; `run1/driver_out.txt` and the JSON files are its outputs.
- `exp_c2.py` → `exp_c2_out.txt`: the same planted directions with `n_extra = 4` (noiseless): 21 of 24 at χ² ≤ 0.1;
  the misses at |h·h| ≈ 3–4 × 10⁻⁴ reach 0.18–1.2 in near-degenerate alternative minima (a tube-coordinate refinement
  from them is tried and printed).
- `exp_c2b.py` → `exp_c2b_out.txt`: noisy targets (Gaussian noise of the χ²'s σ): the search met or beat the planted
  direction's χ² on 24 of 24.
- `n_extra_check.py` → `n_extra_check_out.txt`: `n_extra = 4` against `search_check.py`'s full-start minima on ten of
  its rows (equal) and the time per row. First run inline before commit 4370b2e95; rerun here to keep its log.
- `reading_test_draft_v2.py` and `run2/`: the revised draft (after the referee: Lemma A′ in C0, C2 with three strata
  and noise, the bounds' read-outs, degenerate-row handling) on the same 80 rows. C2 met 36 of 36. C3 reads False there
  only because the stand-in grid has 40 mirror pairs, not the 80 the rule requires. `run2/driver_out2.txt` ends in a
  KeyError from the driver's last print (a key the revised C2 renamed), after every file was written.
