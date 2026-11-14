"""P-845, fourth run (B1924's first owed item: longer histories and a larger sample). Written before the run.

(1) n = 28: 60 allowed words (seed 8454), each read at the mark (2/5, 4/5) and its twin (1/5, 2/5).
(2) n = 22 again: 60 NEW allowed words (seed 8455), at the mark and the twin: a second, independent sample at the length
    B1924 reported, so the two n = 22 samples can be compared with each other (they must agree within their errors if
    the sampling error is honest).
EXPECTATIONS (main, before the run): (a) the two n = 22 samples agree: per number median |z| near 0.67, few above 2;
(b) n = 22 (both samples pooled) against n = 28: no change beyond the errors (median near 0.67, share above 2 near 5 %);
(c) the mark against its twin at n = 28, paired: not told apart (median below 1, share above 2 below 5 %).
A failure of (a) means the jackknife error understates the spread; of (b), that the read-out still drifts at n = 22.
Printed: structure only. Values: the json only. Nothing compared with a measured number."""
import json, pathlib, random
import numpy as np
import thread_average as T
import whole_average as WA
from whole_average_3 import run
HERE = pathlib.Path(__file__).resolve().parent


def sample(n, seed, size=60):
    rng = random.Random(seed); words = []
    while len(words) < size:
        w = "".join(rng.choice("LR") for _ in range(n))
        if "L" in w and "R" in w and T.keeps_mark(w):
            words.append(w)
    return words


if __name__ == "__main__":
    out = {}
    for label, n, seed in (("28", 28, 8454), ("22b", 22, 8455)):
        words = sample(n, seed)
        for name, mark in (("mark", (0.4, 0.8)), ("twin", (0.2, 0.4))):
            rows, R, se = run(words, mark)
            out["%s %s" % (label, name)] = {"rows": rows, "R": {k: v.tolist() for k, v in R.items()}, "se": {k: v.tolist() for k, v in se.items()}}
            print("%s, %s: %d words; largest sampling error %.1e" % (label, name, len(rows), max(float(np.max(v)) for v in se.values())), flush=True)
            (HERE / "whole_average_4.json").write_text(json.dumps(out, indent=1))
    print("done; the comparisons are made by twin_compare_4.py", flush=True)
