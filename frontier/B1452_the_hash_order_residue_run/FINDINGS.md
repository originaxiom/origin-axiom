# B1452 — THE HASH-ORDER RESIDUE, RUN: the 24 order-sensitive sites in banked verification scripts, each script re-run under four hash seeds — no banked number depends on the order; one script prints a dictionary in a seed-dependent order, and one no longer runs on this bench for an unrelated reason

cc, 2026-10-02. B1425 minted error class E83 (a script that hands a set where order matters returns a differently
normalised answer per `PYTHONHASHSEED`) and its sweep left lead L226: 24 unsorted sites in 16 banked verification
scripts that no lock re-runs. "The open question is not whether they are order-sensitive — they are — but whether
any of them feeds a banked NUMBER." The lead ages on 2026-10-09. **Verdict: NEGATIVE** — none does.

## What was run

Each of the 16 scripts under `PYTHONHASHSEED` = 0, 1, 2, 3 in a scratch checkout of main, what it prints and what
it writes compared across seeds after removing timings (`verification/pass1…pass4`, record `seed_runs.json`). Four
passes were needed: five scripts address their inputs from the repository root and failed from their own directory;
two take over two hours a seed; one needs another's untracked product.

| | scripts | sites |
|---|---|---|
| identical output on four seeds | 14 | 21 |
| identical up to the printed order of one dictionary | 1 (B904) | 1 |
| does not run on this bench; settled by reading | 1 (B675) | 2 |

- **Fourteen scripts print the same thing on four seeds.** Three of them also write a file that is the tracked
  file again: `b1100_exact_table.py` (one hash on four seeds, the tracked `b1100_exact_table.json` byte for byte,
  after 2.4 hours a seed), `b1100_hypercharge.py` (likewise the tracked `b1100_hypercharge.json`) and
  `b1102_adapted_basis.py` (equal to the tracked JSON apart from the times in its embedded log).
- **B904 `stage2c_final.py`:** the line `fitted: {…}` and the JSON written list three keys of equal value
  (`lam0`, `lam1`, `lam2`) in a seed-dependent order. Equal as dictionaries. Cosmetic.
- **B675 `bronze_certification.py` does not run here.** It stops on every seed with `TypeError: nmods cannot be
  ordered` inside the polynomial library's factor sort (python-flint 0.9.0), after printing its quartic and octic
  checks. That is not a hash-order effect. Its two sites (lines 439, 524) each build a mapping from symbols to
  values for an evaluator, which no iteration order can change. **The script's failure to run is registered as
  lead L238**; this arc does not claim B675's certification re-runs.

## What it means

- **No banked verdict is at risk from E83 at these 24 sites.** With B1425's five locks (28 tests on five seeds),
  all 34 sites of the sweep are now settled. Most of the sites build a substitution mapping, where order cannot
  matter; the ones that hand a list of symbols to a solver or take "the first symbol" did not change their output.
- **The fence.** Four seeds, not all; the sweep's patterns, not every way a set's order can leak; the W5 cell's
  results file was not compared field by field (it records run times); B675's sites were read, not run.

## Lead

L226 is closed by this arc. L238 registered.
