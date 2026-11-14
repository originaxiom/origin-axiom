"""P-845, second run: 60 allowed words at n = 10 and n = 16 (a fixed seed), each read at the mark (2/5, 4/5) and at its
twin (1/5, 2/5) (the same words, both keep the line: the twins are kept together, B1914). Printed: structure only (the
sampling errors, the change between n, and the difference between the twins in units of the sampling error).
Values to the json. Nothing compared with a measured number."""
import json, math, pathlib, random
import numpy as np
import thread_average as T
import whole_average as WA
HERE = pathlib.Path(__file__).resolve().parent


def run(words, mark):
    T.MARK = mark
    rows = []
    for w in words:
        A, ell, nodes = WA.thread_mean(w)
        rows.append({"word": w, "length": ell, "A": {k: v.tolist() for k, v in A.items()}})
    keys = rows[0]["A"].keys(); wts = np.array([r["length"] for r in rows])
    R = {k: np.sum([wt * np.array(r["A"][k]) for wt, r in zip(wts, rows)], 0) / wts.sum() for k in keys}
    jk = []
    for i in range(len(rows)):
        m = np.ones(len(rows), bool); m[i] = False
        jk.append({k: np.sum([wt * np.array(r["A"][k]) for wt, r, keep in zip(wts, rows, m) if keep], 0) / wts[m].sum() for k in keys})
    se = {k: np.sqrt((len(rows) - 1) * np.mean([(j[k] - R[k]) ** 2 for j in jk], 0)) for k in keys}
    return rows, R, se


if __name__ == "__main__":
    rng = random.Random(8453)
    out = {}
    res = {}
    for n in (22,):
        words = []
        while len(words) < 60:
            w = "".join(rng.choice("LR") for _ in range(n))
            if "L" in w and "R" in w and T.keeps_mark(w):
                words.append(w)
        for name, mark in (("mark", (0.4, 0.8)), ("twin", (0.2, 0.4))):
            rows, R, se = run(words, mark)
            res[(n, name)] = (R, se)
            out["%d %s" % (n, name)] = {"rows": rows, "R": {k: v.tolist() for k, v in R.items()}, "se": {k: v.tolist() for k, v in se.items()}}
            print("n = %d, %s: 60 words; largest sampling error %.1e" % (n, name, max(float(np.max(v)) for v in se.values())), flush=True)
            (HERE / "whole_average_3.json").write_text(json.dumps(out, indent=1))
    (Rm, sm), (Rt, st) = res[(22, "mark")], res[(22, "twin")]
    z = np.concatenate([np.abs(Rm[k] - Rt[k]) / np.sqrt(sm[k] ** 2 + st[k] ** 2 + 1e-30) for k in Rm])
    print("n = 22: the mark against its twin per component: median |z| %.2f, share above 2: %.0f%%" % (float(np.median(z)), 100 * float(np.mean(z > 2))), flush=True)
