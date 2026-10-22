"""B1711 (P-256): W59's eighteen order-9 lines at the band tau.  The lines (p1, p2) = (b + i/3, b + j/3), b in {1/9, 2/9},
i, j in {0, 1, 2}, with w = p1 tau - p2 (B1656's convention, its LINES18); each of exact order 9, so by B1703 the three
charged sectors are split and the leptons' first generation is protected at leading order.  With each line, the
weight-3/2 section DR (one unit on v+, B1700), B1667's canonical end and B1656's four-channel coupling: the six
charged-fermion ratios at Re tau in {0, 1/2}, Im tau = 1.5..3.5 (step 0.02), both horocycles, B1660's three up readings.
No data.
    python3 -B the_order9_lines.py [--workers 8]      # writes the_order9_lines.json beside itself"""
import sys, io, json, math, contextlib, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(HERE)); _argv = sys.argv; sys.argv = ['x']
import b1656_funcs as B
sys.argv = _argv
P1691 = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(P1691))
spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import mpmath as mp
LINES = [("b=%s" % b, b + Fr(i, 3), b + Fr(j, 3)) for b in (Fr(1, 9), Fr(2, 9)) for i in range(3) for j in range(3)]
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.load(open(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
def L_of(y, which): return float(np.interp(y, [c[0] for c in col], [c[1] if which == "L_max" else c[2] for c in col]))
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
def point(task):
    k, re_t, y = task
    tag, a, b = LINES[k]
    t = complex(re_t, y); w = float(a) * t - float(b)                     # w = p1 tau - p2
    av = [complex(te.ev(cc, mp.mpc(re_t, y))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    readings = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    res = {"line": k, "Re_tau": re_t, "Im_tau": y}
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        for which in ("L_max", "L_2"):
            L = L_of(y, which)
            u = {kk: (math.sqrt(2 * math.pi * L + c[kk]) * R[kk] if c[kk] is not None and 2 * math.pi * L + c[kk] > 0 else 0) for kk in B.UNITS}
            M = B.weighted_M(u)
            for rn, SS in (readings.items() if sec == "up" else [("S", S)]):
                sv = np.linalg.svd(B.coupling(SS, M), compute_uv=False)
                res["%s|%s|%s" % (sec, which, rn)] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    return res
if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    tasks = [(k, r, round(1.5 + 0.02 * j, 2)) for k in range(len(LINES)) for r in (0.0, 0.5) for j in range(101)]
    with Pool(nw) as P: out = P.map(point, tasks, chunksize=4)
    json.dump({"lines": [[tg, str(a), str(b)] for tg, a, b in LINES], "rows": out}, open(HERE / "the_order9_lines.json", "w"))
    print(len(out), "points")
