#!/usr/bin/env python3
"""POST HOC (written after p644_rival_out.txt was read): two follow-ups to FL-04's rival null. Uses p644_rival.py's
functions; imports main's frame from a checkout at 88a1e9474, as that script does. Data-free; values to the json only.

    python3 -B p644_rival_posthoc.py <a checkout of main at 88a1e9474>      # writes p644_rival_posthoc.json

Why. (1) p644_rival.py's docstring names m004's line as v/5 = (2/5, 4/5), the record's mark; the code used v/5 with
v = (1, 2), which is (1/5, 2/5), the mark's twin. B1928 proves the read-out the same at every point of order 5 in the
limit; at finite length B1924 found the mark and the twin not told apart at n = 16. (2) X3 failed at p = 7: 8 of 43
components beyond 3 sampling errors (median 1.5), against a seed control at median 0.37. Whether that difference is
real or a fluctuation is decided by the sample size: a real difference grows like the square root of the number of
words; a fluctuation does not.

What it runs, with the same measure, nodes and ends as p644_rival.py:
  F1 m004 at the mark (2/5, 4/5) against m004 at the twin (1/5, 2/5), 40 words each (the twin's are p644_rival.py's
     first seed, recomputed);
  F2 LLLR at p = 7, line (1/7, 3/7), against m004 at the mark, with 120 words each (n = 12, 14 and 16, 40 words per n;
     new seeds), and the same comparison on the first 40 of the 120 words;
  F3 the seed control at 120 words: m004 at the mark with a second set of 120 words.
Reading rule, stated before the run: F2's difference is real if its median z at 120 words exceeds F3's by more than
a factor 2 and is at least 1.5 times F2's median z on 40 words; otherwise the p = 7 rival is not told apart from m004
at this resolution.
"""
pass  # [copy: loader replaced, see MANIFEST.md]
import json
import math
import pathlib
import random
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
import p644_rival as RV  # [copy: loader replaced, see MANIFEST.md]


def words3(v, p, seed, per=40):
    rng = random.Random(seed)
    out = []
    for n in (12, 14, 16):
        got = []
        while len(got) < per:
            w = "".join(rng.choice("LR") for _ in range(n))
            if "L" in w and "R" in w and RV.keeps(w, v, p) and w not in got:
                got.append(w)
        out += got
    return out


def readout_words(T, C, line, ws):
    rows = [(w,) + RV.thread(T, C, w, line) for w in ws]
    wts = np.array([r[3] for r in rows])
    keys = rows[0][1].keys()
    R = {k: sum(wt * r[1][k] for wt, r in zip(wts, rows)) / wts.sum() for k in keys}
    jk = []
    for i in range(len(rows)):
        m = np.ones(len(rows), bool)
        m[i] = False
        jk.append({k: sum(wt * r[1][k] for wt, r, keep in zip(wts, rows, m) if keep) / wts[m].sum() for k in keys})
    se = {k: np.sqrt((len(rows) - 1) * np.mean([(j[k] - R[k]) ** 2 for j in jk], 0)) for k in keys}
    low = {k: np.min([r[2][k] for r in rows], 0) for k in keys}
    return {"line": line, "words": ws, "R": R, "se": se, "low": low, "rows": rows}


def first(r, n):
    rows = r["rows"][:n]
    wts = np.array([x[3] for x in rows])
    keys = rows[0][1].keys()
    R = {k: sum(wt * x[1][k] for wt, x in zip(wts, rows)) / wts.sum() for k in keys}
    jk = []
    for i in range(len(rows)):
        m = np.ones(len(rows), bool)
        m[i] = False
        jk.append({k: sum(wt * x[1][k] for wt, x, keep in zip(wts, rows, m) if keep) / wts[m].sum() for k in keys})
    se = {k: np.sqrt((len(rows) - 1) * np.mean([(j[k] - R[k]) ** 2 for j in jk], 0)) for k in keys}
    low = {k: np.min([x[2][k] for x in rows], 0) for k in keys}
    return {"R": R, "se": se, "low": low}


def main():
    T, C = RV.load(sys.argv[1])
    mark, twin = (0.4, 0.8), (0.2, 0.4)
    w40 = RV.words((1, 2), 5, 20261125 + 5)
    A_mark = readout_words(T, C, mark, w40)
    A_twin = readout_words(T, C, twin, w40)
    f1 = RV.compare(A_mark, A_twin)
    print("F1 m004 at the mark (2/5, 4/5) against the twin (1/5, 2/5), the same 40 words: %s" % f1, flush=True)
    M120 = readout_words(T, C, mark, words3((1, 2), 5, 3105))
    L120 = readout_words(T, C, (1 / 7, 3 / 7), words3((1, 3), 7, 3107))
    S120 = readout_words(T, C, mark, words3((1, 2), 5, 9105))
    f2_120 = RV.compare(L120, M120)
    f2_40 = RV.compare(first(L120, 40), first(M120, 40))
    f3 = RV.compare(S120, M120)
    print("F2 LLLR at p = 7 against m004 at the mark, 120 words: %s" % f2_120)
    print("F2 the same, first 40 of the 120 words: %s" % f2_40)
    print("F3 m004 at the mark, a second 120 words against the first: %s" % f3)
    real = f2_120["median_z"] > 2 * f3["median_z"] and f2_120["median_z"] >= 1.5 * f2_40["median_z"]
    print("reading: the p = 7 difference is %s" % ("real" if real else "not told apart at this resolution"))
    out = {}
    for name, r in (("m004_mark_40", A_mark), ("m004_twin_40", A_twin), ("m004_mark_120", M120),
                    ("LLLR_p7_120", L120), ("m004_mark_120_second", S120)):
        out[name] = {"line": r["line"], "words": r["words"], "R": {k: v.tolist() for k, v in r["R"].items()},
                     "se": {k: v.tolist() for k, v in r["se"].items()}}
    (HERE / "p644_rival_posthoc.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
