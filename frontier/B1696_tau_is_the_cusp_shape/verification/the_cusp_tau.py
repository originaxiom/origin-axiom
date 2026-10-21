"""B1696 (P-244): tau = the state's own cusp shape. For the tick LR (m004) the cusp torus's shape is 2 sqrt(-3), in the
fundamental domain tau_c = 2 sqrt(3) i (B712, B762; B357: one universal tau = the cusp shape governs every E6 block). With
tau = tau_c, the unique section DR, B1667's canonical end at Im tau_c (L_max, L_2 interpolated from its stored column) and
B1656's four-channel coupling with a flat hypercharge line w = alpha tau (alpha = j/192, j = 0..96; beta = 0): the six
charged-fermion ratios for each alpha, each horocycle and each of B1660's three readings of the up sector.  No data.
    python3 -B the_cusp_tau.py [--workers 8]      # writes the_cusp_tau.json beside itself"""
import sys, io, json, math, contextlib, importlib.util, pathlib
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
Y_C = 2 * math.sqrt(3)
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.load(open(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
L_C = {"L_max": float(np.interp(Y_C, [c[0] for c in col], [c[1] for c in col])), "L_2": float(np.interp(Y_C, [c[0] for c in col], [c[2] for c in col]))}
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
def point(j):
    t = complex(0, Y_C); w = (j / 192.0) * t
    a = [complex(te.ev(cc, mp.mpc(0, Y_C))) for cc in te.B[1]]
    S = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    readings = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    res = {"j": j}
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        for which, L in L_C.items():
            u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
            M = B.weighted_M(u)
            for rn, SS in (readings.items() if sec == "up" else [("S", S)]):
                sv = np.linalg.svd(B.coupling(SS, M), compute_uv=False)
                res["%s|%s|%s" % (sec, which, rn)] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    return res
if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    with Pool(nw) as P: out = P.map(point, range(0, 97))
    json.dump({"tau": [0.0, Y_C], "L": L_C, "rows": out}, open(HERE / "the_cusp_tau.json", "w"))
    print(len(out), "lines")
