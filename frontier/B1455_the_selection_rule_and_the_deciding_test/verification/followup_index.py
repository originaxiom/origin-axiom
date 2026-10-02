#!/usr/bin/env python3
"""B1455, C3 (sealed) -- the count at the exceptional point, its pullbacks, and its count-odd image.

L1: the index is unchanged by pulling back along a symmetry of the manifold (rotation or mirror).
L2: it changes sign under dualising.   So Theta_sigma(W) = (sigma^* W)^* carries the opposite count.
Instrument: B1446's index_num through B1453's wrapper (the fibred presentation, the meridian checked), 60 digits.

    python3 followup_index.py      # prints, writes followup_index.json
"""
import json, os, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1453_the_sm_seats_join_arcs_harvested" / "verification"))
import join_own as J
from mpmath import mpf, mpc, sqrt, inverse, matrix, nstr
ix = J.ix


def index(W):
    h, T = J.fibred(W)
    I, a, b = ix.index(J.PHI, h, T)
    return I, a, b


def is_rep(W):
    R = J.word(J.REL, W); n = R.rows
    return max(abs(R[i, j] - (1 if i == j else 0)) for i in range(n) for j in range(n)) < mpf(10) ** (-40)


def pull(W, a, b):
    """sigma^* W for sigma(m) = a, sigma(n) = b (words)"""
    return {"m": J.word(a, W), "n": J.word(b, W)}


SIGMAS = {"iota (rotation, inverts the longitude)": ("M", "N"),
          "swap (rotation, keeps the longitude)": ("n", "m"),
          "tau (MIRROR, keeps the longitude)": ("M", "NMn")}


def main():
    out = {}; ok = True
    for label, q, mu in (("q0 = 17 + 12 sqrt 2, twist -1", 17 + 12 * sqrt(mpf(2)), mpc(-1)), ("q0' = 17 - 12 sqrt 2, twist -1", 17 - 12 * sqrt(mpf(2)), mpc(-1)),
                         ("control q = 3, twist -1", mpf(3), mpc(-1))):
        g = J.ballas(q, mu); reps, z, rb = J.cocycles(g)
        row = {"h1(A)": len(reps)}
        I, a, b = index(g); row["I(A)"] = int(I)
        Ia = {}
        for name, (x, y) in SIGMAS.items():
            P = pull(g, x, y); assert is_rep(P), name
            Ia[name] = int(index(P)[0]); Ia["Theta: " + name] = int(index(J.dualrep(P))[0])
        row["I on the pullbacks of A"] = Ia
        if reps:
            c = {"m": matrix([reps[0][i] for i in range(4)]), "n": matrix([reps[0][4 + i] for i in range(4)])}
            W = J.ext(g, c); assert is_rep(W)
            I, a, b = index(W); row["I(W1)"] = int(I); row["interior classes (W1, W1*)"] = [int(a["interior"]), int(b["interior"])]
            row["gap"] = {k: nstr(v, 5) for k, v in a.items() if "kept" in k or "dropped" in k or "gap" in k}
            row["I(W1*)"] = int(index(J.dualrep(W))[0])
            for name, (x, y) in SIGMAS.items():
                P = pull(W, x, y); assert is_rep(P), name
                row["I(%s^* W1)" % name.split(" ")[0]] = int(index(P)[0])
                row["I(Theta_%s W1)" % name.split(" ")[0]] = int(index(J.dualrep(P))[0])
        out[label] = row
        print(label); [print("    %-34s %s" % (k, v)) for k, v in row.items()]
    e = out["q0 = 17 + 12 sqrt 2, twist -1"]
    ok = (e["I(A)"] == 0 and e["I(W1)"] == -1 and e["I(W1*)"] == 1 and all(e["I(%s^* W1)" % s] == -1 for s in ("iota", "swap", "tau"))
          and all(e["I(Theta_%s W1)" % s] == 1 for s in ("iota", "swap", "tau")) and out["control q = 3, twist -1"]["h1(A)"] == 0)
    json.dump(out, open(HERE / "followup_index.json", "w"), indent=1)
    print("VERDICT followup-index: %s (P5: I(A) = 0, I(W1) = -1, unchanged by every pullback, +1 on every count-odd image)" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
