"""B1702 (P-249): the six charged-fermion ratios at the other cusp shapes on record -- the silver word state's 2i (B675,
B485) and the golden word's spin end curve 1/2 + sqrt3 i (B1483; -1/2 + sqrt3 i up to tau -> tau + 1) -- for every flat
line w = alpha tau + b with (alpha, b) = (j/24, k/24), j, k = 0..23 (576 lines), the end-data Higgs DR, B1667's canonical
end (both horocycles), B1656's four-channel coupling and B1660's three up readings.  No data.
    python3 -B the_cusp_shapes.py [--workers 8]      # writes the_cusp_shapes.json beside itself"""
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
TAUS = {"silver 2i": (0.0, 2.0), "spin curve 1/2 + sqrt3 i": (0.5, math.sqrt(3))}
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.load(open(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
def L_of(y, which): return float(np.interp(y, [c[0] for c in col], [c[1] if which == "L_max" else c[2] for c in col]))
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
LINES = [(Fr(j, 24), Fr(k, 24)) for j in range(24) for k in range(24)]
def point(task):
    k, name = task
    a, b = LINES[k]; re_t, y = TAUS[name]
    t = complex(re_t, y); w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(re_t, y))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    readings = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    res = {"line": k, "tau": name}
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
    with Pool(nw) as P: out = P.map(point, [(k, n) for n in TAUS for k in range(len(LINES))], chunksize=4)
    json.dump({"taus": TAUS, "lines": [[str(a), str(b)] for a, b in LINES], "rows": out}, open(HERE / "the_cusp_shapes.json", "w"))
    print(len(out), "rows at", list(TAUS))
