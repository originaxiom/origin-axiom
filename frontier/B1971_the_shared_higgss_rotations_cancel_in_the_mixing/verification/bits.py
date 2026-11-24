"""B1971 (main, 2026-11-24; data-free): the two-bit picture of the all-S mixing, tested over points.
At height Y (default 30), column 0.13, for every point (a, b) of the given orders:
  h's dominant null-basis direction; each sector's channel u's dominant direction; down's w/u_e (when u_e dominates);
  each sector's left singular vectors' dominant directions (light, middle, heavy), and whether each is clean
  (dominant |coord| >= 0.99); the mixing's least diagonal |V|.
Prediction to test: every mass state lies along n, nb or e; the mixing is aligned iff the two assignments agree."""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import nullbasis as NB
from fractions import Fraction as Fr
mp = NB.mp
LAB = ("n", "nb", "e")

def dom(c):
    m = [abs(x) for x in c]; k = max(range(3), key=lambda i: m[i]); return LAB[k], float(m[k] / mp.sqrt(sum(x ** 2 for x in m)))

if __name__ == "__main__":
    Y = float(sys.argv[1]); orders = [int(o) for o in sys.argv[2:]] or [5]
    rows = []
    for N in orders:
        pts = sorted({(Fr(i, N), Fr(j, N)) for i in range(N) for j in range(N) if (i, j) != (0, 0)})
        pts = [p for p in pts if max(p[0].denominator, p[1].denominator) == N or N == 5]
        for (a, b) in pts:
            try:
                S = NB.snap(Y, a, b)
            except Exception as ex:
                rows.append(dict(N=N, a=str(a), b=str(b), err=str(ex)[:80])); continue
            r = dict(N=N, a=str(a), b=str(b), h=dom(S["up"]["h"]))
            for sec in ("up", "down"):
                r[sec + "_u"] = dom(S[sec]["u"]) if any(abs(x) > 0 for x in S[sec]["u"]) else ("0", 0)
                r[sec + "_assign"] = [dom([S[sec]["Ub"][k][c] for k in range(3)]) for c in range(3)]
                ue = S[sec]["u"][2]; w = S[sec]["w"]
                r[sec + "_w_over_ue"] = None if (ue == 0 or w == 0) else mp.nstr(w / ue, 4)
            V = S["V"]; r["diag"] = float(min(abs(V[k, k]) for k in range(3)))
            perm = [[float(abs(V[i, j])) for j in range(3)] for i in range(3)]
            r["Vpat"] = [[round(x) for x in row] for row in perm]
            rows.append(r)
            ua = "/".join(x[0] for x in r["up_assign"]); da = "/".join(x[0] for x in r["down_assign"])
            clean = min(x[1] for x in r["up_assign"] + r["down_assign"])
            print("N=%d (%s, %s): h~%s | u_up~%s u_dn~%s w/ue %s | up %s down %s (clean %.3f) | diag %.3f %s" % (
                N, a, b, r["h"][0], r["up_u"][0], r["down_u"][0], r["down_w_over_ue"], ua, da, clean, r["diag"],
                "AGREE" if ua == da else "differ"), flush=True)
    json.dump(rows, open(pathlib.Path(__file__).with_name("bits_run_%d_%s.json" % (int(Y), "_".join(map(str, orders)))), "w"), indent=1, default=str)
    ag = [r for r in rows if "err" not in r]
    agree = [r for r in ag if [x[0] for x in r["up_assign"]] == [x[0] for x in r["down_assign"]]]
    clean = lambda r: min(x[1] for x in r["up_assign"] + r["down_assign"])
    print("SUMMARY: %d points (%d errors); assignments agree at %d; of those aligned (diag >= 0.9): %d; of the others aligned: %d" % (
        len(ag), len(rows) - len(ag), len(agree), sum(r["diag"] >= 0.9 for r in agree), sum(r["diag"] >= 0.9 for r in ag if r not in agree)))
    print("SUMMARY: every state clean (dominant coordinate >= 0.99) at %d points; of the rest, %d aligned" % (
        sum(clean(r) >= 0.99 for r in ag), sum(r["diag"] >= 0.9 for r in ag if clean(r) < 0.99)))
    print("SUMMARY: the points not aligned:", [(r["N"], r["a"], r["b"], round(r["diag"], 3)) for r in ag if r["diag"] < 0.9])
    print("SUMMARY: the points not aligned all have a = 1/2: %s; the points with a = 1/2: %d" % (
        all(r["a"] == "1/2" for r in ag if r["diag"] < 0.9), sum(r["a"] == "1/2" for r in ag)))
