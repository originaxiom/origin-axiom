"""B1695 (P-243): one line, one tau, the unique section -- the six charged-fermion mass ratios of the weight-3/2 covariant
Higgs DR at the canonical end (B1667's horocycles) with a flat hypercharge line w = alpha tau (B1656's four-channel
coupling and per-sector twists, copied verbatim), on a grid alpha = j/96 (j = 0..48) x Im tau = 1.5..3.5 (step 0.05) x
Re tau in {0, 1/2}; the up sector in B1660's three readings of one Higgs (S, S~ = eps conj(S) eps^T, conj(S)).
Mathematics only; no data.
    python3 -B the_grid.py [--workers 8]      # writes the_grid.json beside itself"""
import sys, io, json, math, contextlib, importlib.util, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(HERE))
_argv = sys.argv; sys.argv = ['x']
import b1656_funcs as B
sys.argv = _argv
P1691 = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(P1691))
spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import mpmath as mp
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.load(open(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
def L_of(y, which):
    arr = [c[1] if which == "L_max" else c[2] for c in col]; ys = [c[0] for c in col]
    return float(np.interp(y, ys, arr))
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
def conj2(S): return np.conj(S)
def point(task):
    j, y, re_t = task
    t = complex(re_t, y); w = (j / 96.0) * t
    a = [complex(te.ev(cc, mp.mpc(re_t, y))) for cc in te.B[1]]
    S = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    readings = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    res = {"j": j, "Im_tau": y, "Re_tau": re_t}
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf])
        R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        for which in ("L_max", "L_2"):
            L = L_of(y, which)
            u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
            M = B.weighted_M(u)
            for rn, SS in (readings.items() if sec == "up" else [("S", S)]):
                sv = np.linalg.svd(B.coupling(SS, M), compute_uv=False)
                res["%s|%s|%s" % (sec, which, rn)] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    return res
if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    tasks = [(j, round(1.5 + 0.05 * k, 2), r) for r in (0.0, 0.5) for j in range(0, 49) for k in range(41)]
    with Pool(nw) as P: out = P.map(point, tasks, chunksize=4)
    json.dump({"grid": out, "L_column_Re_tau_0.25": col}, open(HERE / "the_grid.json", "w"))
    print(len(out), "points")
