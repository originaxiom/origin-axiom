"""B1703 (P-250): the line census in the newest frame.  No data.  Every flat line w = alpha tau + b of exact order
N <= 16 ((alpha, b) in (Z/N)^2 of exact order N), at two generic tau (off the CP lines), with the end-data Higgs DR, B1667's
canonical end (L_max) and B1656's four-channel coupling: each sector's (m2/m3, m1/m3); which sectors coincide (d = e,
u = d, u = e); which first generations vanish at leading order (P-170's protection: the sector's "1"-channel residue
R_1 = theta_1(delta w) vanishes, delta = q_L - q_R in 6Y units).  The arithmetic predicted, written
before the loop: d = e iff N | 4 or N | 5; u = d iff N | 6; u = e iff N | 2; protection: up iff N | 5, leptons iff N | 9,
down never.
    python3 -B the_line_census.py [--workers 8]      # writes the_line_census.json beside itself"""
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
TAUS = [complex(0.31, 2.4), complex(0.13, 1.9)]
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.load(open(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
def L_of(y): return float(np.interp(y, [c[0] for c in col], [c[1] for c in col]))
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
NMAX = 16
LINES = [(Fr(j, N), Fr(k, N), N) for N in range(1, NMAX + 1) for j in range(N) for k in range(N) if math.gcd(math.gcd(j, k), N) == 1]
def point(task):
    k, ti = task
    a, b, N = LINES[k]; t = TAUS[ti]; w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    res = {"line": k, "tau": ti}
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        L = L_of(t.imag)
        u = {kk: (math.sqrt(2 * math.pi * L + c[kk]) * R[kk] if c[kk] is not None and 2 * math.pi * L + c[kk] > 0 else 0) for kk in B.UNITS}
        sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False)
        res[sec] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
        res[sec + "_R1_rel"] = abs(R["1"]) / max(abs(R[kk]) for kk in B.UNITS)
    return res
def same(p, q): return abs(p[0] - q[0]) / max(p[0], q[0]) < 1e-9 and abs(p[1] - q[1]) < 1e-12 + 1e-9 * max(p[1], q[1])
if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    print("prediction: d=e iff N|4 or N|5; u=d iff N|6; u=e iff N|2; protected: up iff N|5, leptons iff N|9, down never")
    with Pool(nw) as P: rows = P.map(point, [(k, ti) for k in range(len(LINES)) for ti in range(len(TAUS))], chunksize=4)
    by = {}
    for r in rows:
        N = LINES[r["line"]][2]; e = by.setdefault(N, {"lines": 0, "d=e": 0, "u=d": 0, "u=e": 0, "all_split": 0, "protected": {"up": 0, "down": 0, "lep": 0}})
        e["lines"] += 1
        de, ud, ue = same(r["down"], r["lep"]), same(r["up"], r["down"]), same(r["up"], r["lep"])
        e["d=e"] += de; e["u=d"] += ud; e["u=e"] += ue; e["all_split"] += not (de or ud or ue)
        for s in ("up", "down", "lep"): e["protected"][s] += r[s + "_R1_rel"] < 1e-9
    pred = {N: {"d=e": (4 % N == 0 or 5 % N == 0), "u=d": 6 % N == 0, "u=e": 2 % N == 0, "up": 5 % N == 0, "lep": 9 % N == 0, "down": N == 1} for N in by}
    ok = all((by[N]["d=e"] == by[N]["lines"]) == pred[N]["d=e"] and (by[N]["d=e"] in (0, by[N]["lines"])) and
             (by[N]["u=d"] == by[N]["lines"]) == pred[N]["u=d"] and (by[N]["u=d"] in (0, by[N]["lines"])) and
             (by[N]["u=e"] == by[N]["lines"]) == pred[N]["u=e"] and (by[N]["u=e"] in (0, by[N]["lines"])) and
             all((by[N]["protected"][s] == by[N]["lines"]) == pred[N][s] and by[N]["protected"][s] in (0, by[N]["lines"]) for s in ("up", "down", "lep"))
             for N in by)
    for N in sorted(by): print(N, by[N])
    print("the arithmetic holds on every line and tau:", ok)
    json.dump({"taus": [[t.real, t.imag] for t in TAUS], "lines": [[str(a), str(b), N] for a, b, N in LINES], "rows": rows,
               "by_order": by, "prediction_holds": ok}, open(HERE / "the_line_census.json", "w"))
