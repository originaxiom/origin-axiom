#!/usr/bin/env python3
"""POST HOC, labelled: chat1's three exploratory scans of main's fibre frame, re-run from a committed script so that
§5 of THE_SELECTION_MAP.md can be reproduced.  They were first run in a scratch directory against a worktree of main at
3412bf09d; this version uses two_ingredients_census.py's own set-up (main's B1720 instrument at 3412bf09d, extracted
and hash-checked) and its evaluate() function, which C1 checks against main's own ratios_at.
  fine_scan:     6 lines with alpha = 2/5, Re tau in {0, 1/4, 1/2}, Im tau 2.80..3.40 (step 0.02)
  allst_scan:   10 lines, Re tau in {0, 1/4, 1/2}, Im tau 2.30..3.50 (step 0.05)
  readings_scan: 3 points
Every sector with every Higgs reading, both horocycles, and the CKM for every (up, down) reading pair.  Model values only.
    python3 -B posthoc_scans.py [--workers 2]     # writes posthoc_scans.json"""
import json, sys, time, pathlib, importlib.util

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("tic", HERE / "two_ingredients_census.py")
tic = importlib.util.module_from_spec(spec); spec.loader.exec_module(tic)


def run(task):
    re_t, im_t, a, b = task
    r = tic.evaluate(re_t, im_t, a, b)
    r.update({"tau": [re_t, im_t], "line": [a, b]})
    return r


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    fine_lines = [(2/5, 1/5), (2/5, 2/5), (2/5, 3/5), (2/5, 4/5), (2/5, 1/2), (2/5, 1/10)]
    allst_lines = fine_lines + [(1/5, 2/5), (1/5, 3/5), (0, 1/5), (0, 2/5)]
    sets = {
        "fine_scan": [(r, round(2.80 + 0.02 * j, 2), a, b) for (a, b) in fine_lines for r in (0.0, 0.25, 0.5) for j in range(31)],
        "allst_scan": [(r, round(2.30 + 0.05 * j, 2), a, b) for (a, b) in allst_lines for r in (0.0, 0.25, 0.5) for j in range(25)],
        "readings_scan": [(0.5, 3.1, 2/5, 1/2), (0.0, 3.1, 2/5, 4/5), (0.0, 3.1, 2/5, 3/5)],
    }
    out = {"note": "POST HOC exploration, re-run from this committed script; model values only", "rev": tic.REV}
    t0 = time.time()
    with Pool(nw) as P:
        for name, tasks in sets.items():
            out[name] = P.map(run, tasks, chunksize=4)
            print(name, len(tasks), "points;", round(time.time() - t0), "s", flush=True)
    (HERE / "posthoc_scans.json").write_text(json.dumps(out) + "\n")
