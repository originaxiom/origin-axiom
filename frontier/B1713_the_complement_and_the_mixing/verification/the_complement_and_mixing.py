"""B1713 (P-261, P-129, P-164, P-258): the census's complement and the mixing.  Every flat line w = alpha tau + b of exact
order N, 1 <= N <= 12, up to sign (w and -w give the same spectra in every sector: B1703's law): orders 1-7 first (the
complement, 62 lines), then B1712's 204 lines of orders 8-12 in B1712's order.  With the weight-3/2 section DR (one unit
on v+, B1700), B1667's canonical end and B1656's four-channel coupling, at Re tau in {0, 1/2}, Im tau = 1.5..3.5 (step
0.1), both horocycles and B1660's three up readings: the six charged-fermion ratios (as B1712) and the quark mixing.
The mixing: Y's rows are the doublet Q's generations (bil's row index is the left field's; B1653's U4), so
V = U_u^H U_d with U the left singular vectors in ascending mass; |V_us| = |V[0,1]|, |V_cb| = |V[1,2]|, |V_ub| = |V[0,2]|,
J = Im(V_us V_cb V_ub* V_cs*); and, as a read-out of the open convention (B1659's I-33), the same from the right
singular vectors.  No data.
    python3 -B the_complement_and_mixing.py [--workers 8]      # writes the_complement_and_mixing.json beside itself"""
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
def _lines(lo, hi):
    seen, out = set(), []
    for N in range(lo, hi + 1):
        for j in range(N):
            for k in range(N):
                if math.gcd(math.gcd(j, k), N) != 1: continue
                a, b = Fr(j, N), Fr(k, N); na, nb = (-a) % 1, (-b) % 1
                key = min((a, b), (na, nb))
                if key in seen: continue
                seen.add(key); out.append(("N=%d" % N, key[0], key[1]))
    return out
LINES = _lines(1, 7) + _lines(8, 12)                    # the second block is B1712's LINES, in B1712's order
N_COMPLEMENT = len(_lines(1, 7))
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.load(open(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
def L_of(y, which): return float(np.interp(y, [c[0] for c in col], [c[1] if which == "L_max" else c[2] for c in col]))
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
def ckm(Yu, Yd, side):
    """V in ascending mass from the left (side 0) or right (side 1) singular vectors; returns |V_us|, |V_cb|, |V_ub|, J
    and the unitarity defect"""
    Uu, _, Wu = np.linalg.svd(Yu); Ud, _, Wd = np.linalg.svd(Yd)
    if side == 0: Au, Ad = Uu[:, ::-1], Ud[:, ::-1]
    else: Au, Ad = np.conj(Wu.T)[:, ::-1], np.conj(Wd.T)[:, ::-1]
    V = np.conj(Au.T) @ Ad
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2])), J, float(np.max(np.abs(V @ np.conj(V.T) - np.eye(3))))]
def point(task):
    k, re_t, y = task
    tag, a, b = LINES[k]
    t = complex(re_t, y); w = float(a) * t + float(b)                     # w = alpha tau + b
    av = [complex(te.ev(cc, mp.mpc(re_t, y))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    readings = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    res = {"line": k, "Re_tau": re_t, "Im_tau": y}
    Y = {}
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        for which in ("L_max", "L_2"):
            L = L_of(y, which)
            u = {kk: (math.sqrt(2 * math.pi * L + c[kk]) * R[kk] if c[kk] is not None and 2 * math.pi * L + c[kk] > 0 else 0) for kk in B.UNITS}
            M = B.weighted_M(u)
            for rn, SS in (readings.items() if sec == "up" else [("S", S)]):
                Ym = B.coupling(SS, M); Y[(sec, which, rn)] = Ym
                sv = np.linalg.svd(Ym, compute_uv=False)
                res["%s|%s|%s" % (sec, which, rn)] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    for which in ("L_max", "L_2"):
        for rn in readings:
            res["ckm|%s|%s" % (which, rn)] = ckm(Y[("up", which, rn)], Y[("down", which, "S")], 0)
            res["ckm_right|%s|%s" % (which, rn)] = ckm(Y[("up", which, rn)], Y[("down", which, "S")], 1)
    return res
if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    tasks = [(k, r, round(1.5 + 0.1 * j, 2)) for k in range(len(LINES)) for r in (0.0, 0.5) for j in range(21)]
    with Pool(nw) as P: out = P.map(point, tasks, chunksize=4)
    json.dump({"lines": [[tg, str(a), str(b)] for tg, a, b in LINES], "n_complement": N_COMPLEMENT, "rows": out},
              open(HERE / "the_complement_and_mixing.json", "w"))
    print(len(out), "points;", len(LINES), "lines,", N_COMPLEMENT, "of order 1-7")
