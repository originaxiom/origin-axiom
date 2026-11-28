#!/usr/bin/env python3
"""P-644, second half: FL-04's object-against-rival null. Frame C (the read-out on the whole, P-845, B1924, B1928)
run on the object and on rival objects, data-free. Nothing is compared with a measured number; the read-outs' values
are written to the json only, and the printout is differences in units of their sampling error.

    python3 -B p644_rival.py <a checkout of main at 88a1e9474>      # writes p644_rival.json beside itself

It imports main's frame from that checkout (B1724's covariance.frame with B1919's closed-form channel norm, as B1924's
whole_average.py does) and refuses to run if the checkout's HEAD is not 88a1e9474.

Where the object enters frame C (read from thread_average.py and B1872): the level and the mark. LR (m004) is
[[2, 1], [1, 1]], whose trace 3 gives tr^2 - 4 = 5; mod 5 it has the single eigenline v = (1, 2) (eigenvalue -1), and
the frame's line is v/5 = (2/5, 4/5). The allowed words are those that keep +-v mod 5. Nothing else in the read-out
depends on the monodromy: the letters L, R, the measure (each move equally likely, threads weighted by length), the
invariant end L~ (B1921, SL(2, Z)-invariant) and the frame's coupling are the same for every once-punctured torus
bundle.

A rival object w is read the same way: for each prime p dividing tr(w)^2 - 4 at which w is not +-I mod p, the mark is
w's single eigenline v_p mod p, the line is v_p / p, and the allowed words keep +-v_p mod p. The rivals are P-578's
comparable objects: m003 (monodromy -LR) and +-LLLR = +-[[4, 3], [1, 1]] (trace +-5, tr^2 - 4 = 21, so p = 3 and 7).
-LR and -LLLR have the eigenlines of LR and LLLR, so they are read as LR and LLLR are.

The read-out: R_n = the length-weighted average, over 20 distinct allowed words of n moves (L or R, each equally
likely, both letters present; fixed seeds), of each word's thread average of the log ratios over one period of its
closed geodesic, at the line with the invariant end (L~ = 1.3 and 0.9, the two ends of thread_average.py); trapezoid
nodes max(64, 30 * length). n = 12 and 16 are pooled (40 words). The sampling error of each component is a
jackknife over the words. A component whose ratio falls below 1e-10 at any node, for either object of a pair (an exact
zero, B1716), is left out of that pair's comparison, and the count is printed.

Cells and expectations, written before the run (probabilities are this seat's):
  X1 instrument: LR has the single eigenline (1, 2) mod 5; LLLR has a single eigenline mod 3 and mod 7; -LR and -LLLR
     have the same eigenlines; and m003's read-out equals m004's exactly, word by word (99 %).
  X2 seed control: m004's read-out with a second seed differs from the first in more than 3 sampling errors on fewer
     than 10 % of the compared components (85 %).
  X3 the null: LLLR's read-outs at p = 7 and at p = 3 each differ from m004's in more than 3 sampling errors on more
     than half of the compared components (80 %).
Reading, fixed here. If X1 and X3 hold, frame C's values see the object only through its level and mark: it tells
m004 from +-LLLR and cannot tell m004 from m003. If X3 fails, frame C's values are blind to the object at the
resolution of this sample.
"""
import contextlib
import io
import json
import math
import pathlib
import random
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
REV = "88a1e9474"
LM = np.array([[1, 1], [0, 1]], dtype=np.int64)
RM = np.array([[1, 0], [1, 1]], dtype=np.int64)
LT = {"L_max": 1.3, "L_2": 0.9}
OBJECTS = {"m004 (LR)": "LR", "m003 (-LR)": "-LR", "+-LLLR": "LLLR"}


def load(main_dir):
    pass  # [copy: loader replaced, see MANIFEST.md]
    with contextlib.redirect_stdout(io.StringIO()):
        import thread_average as T
        import fast_norm as FN
        import covariance as C
    C._modules()["B"].cA = lambda x, yy, t, R, **kw: FN.cA_fast(x, yy, t, R)
    return T, C


def monodromy(spec):
    sign = -1 if spec.startswith("-") else 1
    M = np.eye(2, dtype=np.int64)
    for ch in spec.lstrip("-"):
        M = M @ (LM if ch == "L" else RM)
    return sign * M


def eigenline(M, p):
    """The eigenlines of M mod p, as normalised vectors (first nonzero entry 1)."""
    lines = set()
    for x in range(p):
        for y in range(p):
            if (x, y) == (0, 0):
                continue
            u = (M @ np.array([x, y])) % p
            if any(((lam * x - u[0]) % p, (lam * y - u[1]) % p) == (0, 0) for lam in range(1, p)):
                k = pow(int(x if x else y), -1, p)
                lines.add(((x * k) % p, (y * k) % p))
    return sorted(lines)


def word_matrix(w):
    M = np.eye(2, dtype=np.int64)
    for ch in w:
        M = M @ (LM if ch == "L" else RM)
    return M


def keeps(w, v, p):
    u = tuple(int(x) for x in (word_matrix(w) @ np.array(v)) % p)
    return u in (tuple(v), tuple((-np.array(v)) % p))


def outputs(T, C, t, line):
    Lend = {h: LT[h] - 0.5 * math.log(t.imag) for h in LT}
    tr, a, b, Lr = T.reduce(complex(t), line[0], line[1], Lend)
    out = C.frame(tr, a, b, Lr)
    return {k: np.array(v, float) for k, v in out.items() if "conjS" not in k}


def thread(T, C, w, line):
    beta, betap, ell, g = T.geodesic(w)
    zt = lambda s: complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
    s0 = -ell / 2
    if abs(g(zt(s0)) - zt(s0 + ell)) > 1e-7 * (1 + abs(zt(s0))):
        ell = -ell
    nodes = max(64, int(30 * abs(ell)))
    acc, low = None, None
    for j in range(nodes):
        o = outputs(T, C, zt(s0 + ell * j / nodes), line)
        if acc is None:
            acc = {k: np.zeros(len(v)) for k, v in o.items()}
            low = {k: np.full(len(v), np.inf) for k, v in o.items()}
        for k in acc:
            acc[k] += np.log(np.maximum(o[k], 1e-300)) / nodes
            low[k] = np.minimum(low[k], o[k])
    return acc, low, abs(ell)


def words(v, p, seed):
    rng = random.Random(seed)
    out = []
    for n in (12, 16):
        got = []
        while len(got) < 20:
            w = "".join(rng.choice("LR") for _ in range(n))
            if "L" in w and "R" in w and keeps(w, v, p) and w not in got:
                got.append(w)
        out += got
    return out


def readout(T, C, v, p, seed):
    line = (v[0] / p, v[1] / p)
    rows = [(w,) + thread(T, C, w, line) for w in words(v, p, seed)]
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
    return {"line": line, "words": [r[0] for r in rows], "R": R, "se": se, "low": low}


def compare(A, B):
    zs, ds, dropped = [], [], 0
    for k in A["R"]:
        for j in range(len(A["R"][k])):
            if A["low"][k][j] < 1e-10 or B["low"][k][j] < 1e-10:
                dropped += 1
                continue
            d = A["R"][k][j] - B["R"][k][j]
            s = math.hypot(A["se"][k][j], B["se"][k][j])
            ds.append(abs(d))
            zs.append(abs(d) / s if s > 0 else (0.0 if d == 0 else math.inf))
    zs = np.array(zs)
    return {"compared": len(zs), "dropped": dropped, "frac_above_3": float(np.mean(zs > 3)),
            "median_z": float(np.median(zs)), "max_abs_diff": float(max(ds)), "exact_equal": bool(max(ds) == 0.0)}


def main():
    T, C = load(sys.argv[1])
    out, res = {}, {}
    # X1: the levels and the marks
    marks = {}
    x1 = True
    for name, spec in OBJECTS.items():
        M = monodromy(spec)
        tr = int(M[0, 0] + M[1, 1])
        disc = tr * tr - 4
        ps = [p for p in (2, 3, 5, 7, 11, 13) if disc % p == 0 and p > 2]
        for p in ps:
            ls = eigenline(M, p)
            Mneg = eigenline(-M, p)
            print("X1 %s: trace %d, tr^2 - 4 = %d; mod %d its eigenlines %s (of -w: %s)" % (name, tr, disc, p, ls, Mneg))
            x1 &= len(ls) == 1 and ls == Mneg
            marks[(name, p)] = ls[0]
    x1 &= marks[("m004 (LR)", 5)] == (1, 2) and marks[("m003 (-LR)", 5)] == (1, 2)
    runs = {}
    for (name, p), v in marks.items():
        runs[(name, p, 1)] = readout(T, C, v, p, 20261125 + p)
        print("read-out %s at p = %d, line %s: %d words, lengths %.1f to %.1f" % (
            name, p, runs[(name, p, 1)]["line"], len(runs[(name, p, 1)]["words"]),
            min(T.geodesic(w)[2] for w in runs[(name, p, 1)]["words"]),
            max(T.geodesic(w)[2] for w in runs[(name, p, 1)]["words"])), flush=True)
    runs[("m004 (LR)", 5, 2)] = readout(T, C, (1, 2), 5, 777)
    c1 = compare(runs[("m003 (-LR)", 5, 1)], runs[("m004 (LR)", 5, 1)])
    x1 &= c1["exact_equal"] and runs[("m003 (-LR)", 5, 1)]["words"] == runs[("m004 (LR)", 5, 1)]["words"]
    print("X1 m003 against m004: %s" % c1)
    res["X1"] = x1
    c2 = compare(runs[("m004 (LR)", 5, 2)], runs[("m004 (LR)", 5, 1)])
    print("X2 m004, second seed against the first: %s" % c2)
    res["X2"] = c2["frac_above_3"] < 0.10
    x3 = True
    for p in (7, 3):
        c3 = compare(runs[("+-LLLR", p, 1)], runs[("m004 (LR)", 5, 1)])
        print("X3 +-LLLR at p = %d against m004: %s" % (p, c3))
        x3 &= c3["frac_above_3"] > 0.5
    res["X3"] = x3
    for key, r in runs.items():
        out["%s|p=%d|seed%d" % key] = {"line": r["line"], "words": r["words"],
                                       "R": {k: v.tolist() for k, v in r["R"].items()},
                                       "se": {k: v.tolist() for k, v in r["se"].items()}}
    (HERE / "p644_rival.json").write_text(json.dumps(out, indent=1))
    print("\n" + ", ".join("%s %s" % (k, "holds" if v else "FAILS") for k, v in res.items()))


if __name__ == "__main__":
    main()
