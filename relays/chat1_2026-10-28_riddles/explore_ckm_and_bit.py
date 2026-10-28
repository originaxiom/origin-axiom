"""Exploratory, data-free read-outs for the web seat's riddle notes (not a sealed test; no chi2; no data values used).
A. The frame's CKM pattern on the six's 30 slope-2/5 lines (orders 25, 30) at two strip points (0.3 + 3.03i,
   0.6 + 3.03i), L_max, every (up, down) reading pair: the full |V|, the permutation that best matches it, and which
   generation block carries each sector's heaviest left-handed state.
B. B1733's order-5 bit and CP: at each B1720 class's apex with one order-5 pair, J on v, on 2v, and on the
   mirror-invariant control line (0, 1/5); whether the apex lies on a mirror line (Re tau in {0, 1/2} mod 1).
Run:  python3 -B explore_ckm_and_bit.py <main_checkout>"""
import sys, json, math, pathlib, itertools
from fractions import Fraction as Fr
from multiprocessing import Pool
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
import census as K
import numpy as np
import mpmath as mp
PERMS = list(itertools.permutations(range(3)))

def Ys(re_t, im_t, a, b, h="L_max"):
    M = K._modules(); B, te, col = M["B"], M["te"], M["col"]
    t = complex(re_t, im_t); w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    reading = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T}
    L = float(np.interp(im_t, [q[0] for q in col], [q[1] if h == "L_max" else q[2] for q in col]))
    Y = {}
    for sec, (lf, rf) in K.SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
        Mw = B.weighted_M(u)
        for rn in ("S", "St"): Y[(sec, rn)] = B.coupling(reading[rn], Mw)
    return Y

def taskA(arg):
    a, b, re_t, im_t = arg
    Y = Ys(re_t, im_t, a, b); rec = {"line": [str(a), str(b)], "tau": [re_t, im_t], "pairs": {}, "heavy_block": {}}
    for key, Ym in Y.items():
        U = np.linalg.svd(Ym)[0]; rec["heavy_block"]["%s|%s" % key] = int(np.argmax(np.abs(U[:, 0])))
    for ru in ("S", "St"):
        for rd in ("S", "St"):
            Uu = np.linalg.svd(Y[("up", ru)])[0][:, ::-1]; Ud = np.linalg.svd(Y[("down", rd)])[0][:, ::-1]
            V = np.abs(np.conj(Uu.T) @ Ud)
            best = max(PERMS, key=lambda p: sum(V[i, p[i]] for i in range(3)))
            rec["pairs"]["%s|%s" % (ru, rd)] = {"absV": V.round(4).tolist(), "best_perm": list(best),
                                               "identity": best == (0, 1, 2), "Vus": float(V[0, 1]), "Vcb": float(V[1, 2]), "Vub": float(V[0, 2])}
    return rec

def lines_2_5():
    out = []
    for N in (25, 30):
        for k in range(N):
            if math.gcd(math.gcd(2 * N // 5, k), N) != 1: continue
            out.append((Fr(2, 5), Fr(k, N)))
    return out

def taskB(c):
    ls = [(Fr(a), Fr(b)) for a, b in c["lines"] if (Fr(a) * 5).denominator == 1 and (Fr(b) * 5).denominator == 1
          and max(Fr(a).denominator, Fr(b).denominator) == 5]
    re_t, im_t = c["tau"]
    on_mirror = min(abs((re_t % 1) - x) for x in (0.0, 0.5, 1.0)) < 1e-9
    rec = {"word": c["word"], "tau": [re_t, im_t], "on_mirror_line": on_mirror, "lines": [[str(x), str(y)] for x, y in ls]}
    for tag, (a, b) in (("v", ls[0]), ("2v", ls[1]), ("control_0_1/5", (Fr(0), Fr(1, 5)))):
        r = K.compute(re_t, im_t, a, b)
        rec[tag] = {k: r[k][3] for k in r if k.startswith("ckm|")}
    return rec

if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parent
    d = json.loads((ROOT / "frontier" / "B1720_the_thread_fixes_the_point" / "verification" / "the_thread_census.json").read_text())
    clsB = [c for c in d["classes"] if len([1 for a, b in c["lines"] if (Fr(a) * 5).denominator == 1 and (Fr(b) * 5).denominator == 1
                                             and max(Fr(a).denominator, Fr(b).denominator) == 5]) == 2]
    argsA = [(a, b, r, 3.03) for a, b in lines_2_5() for r in (0.3, 0.6)]
    print("tasks: A", len(argsA), "B", len(clsB), flush=True)
    with Pool(2) as P:
        A = P.map(taskA, argsA, chunksize=1)
        Bres = P.map(taskB, clsB, chunksize=1)
    (here / "explore_ckm_and_bit.json").write_text(json.dumps({"A": A, "B": Bres}, indent=1, default=str))
    for pr in ("S|S", "St|S", "S|St", "St|St"):
        ids = sum(r["pairs"][pr]["identity"] for r in A)
        perms = {}
        for r in A: perms[str(r["pairs"][pr]["best_perm"])] = perms.get(str(r["pairs"][pr]["best_perm"]), 0) + 1
        vub_vus = [r["pairs"][pr]["Vub"] / max(r["pairs"][pr]["Vus"], 1e-300) for r in A]
        print("A reading (up|down) %-6s identity %2d of %d; best perms %s; median Vus %.3f Vcb %.3f Vub %.3f; median Vub/Vus %.3g" % (
            pr, ids, len(A), perms, np.median([r["pairs"][pr]["Vus"] for r in A]), np.median([r["pairs"][pr]["Vcb"] for r in A]),
            np.median([r["pairs"][pr]["Vub"] for r in A]), np.median(vub_vus)))
    hb = {}
    for r in A:
        for k, v in r["heavy_block"].items(): hb.setdefault(k, {}).setdefault(v, 0); hb[k][v] += 1
    print("A heaviest left-handed state's block, counts over rows:", hb)
    for r in Bres:
        print("B", r["word"], "tau=%.4f+%.4fi" % tuple(r["tau"]), "mirror" if r["on_mirror_line"] else "off", r["lines"],
              "J(Lmax,St|S): v %.3e 2v %.3e ctl %.3e" % (r["v"]["ckm|L_max|St|S"], r["2v"]["ckm|L_max|St|S"], r["control_0_1/5"]["ckm|L_max|St|S"]),
              "| max|J| all keys: v %.2e 2v %.2e ctl %.2e" % tuple(max(abs(x) for x in r[t].values()) for t in ("v", "2v", "control_0_1/5")), flush=True)
    print("explore exit 0")
