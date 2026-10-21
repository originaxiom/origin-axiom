"""B1701 (P-246): the SM seat's W63 on main, and the Higgs's direction tied to the line at the canonical end.  No data.
(a) W63's cells on main's own R (B1691's theta triplet) and B1645's coupling Y(a) = a R^T + R a^T - (a.R) 1: the half
    bound over 2000 real directions (a Fibonacci sphere), m(e_u) for each unit at W63's tau set, m(e_k) = 1/2 on the
    imaginary axis, the isotropic cone.
(b) W63's tie: at a line w, the Higgs's parity copy p is untwisted when p + 3w = 0 (mod the lattice); on a line with 6w
    in the lattice and p* = -3w a half-period, the Higgs is the unit C_{p*} (W61's blocks: (1/2, 0) -> j, (0, 1/2) -> i,
    (1/2, 1/2) -> k in B1656's w = p1 tau - p2).  For every such line (alpha, b) in (1/6)Z^2 mod 1 (27 lines; w = alpha
    tau + b, so p = (alpha, -b)) the six ratios in B1656's four-channel frame at B1667's canonical end, both horocycles,
    B1660's three up readings, Re tau in {0, 1/2}, Im tau = 1.0..4.0 (step 0.2): the smallest m2/m3 per sector.
    python3 -B w63_on_main.py [--workers 8]      # writes w63_on_main.json beside itself"""
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
def Rvec(t): return np.array([complex(te.ev(c, mp.mpc(t.real, t.imag))) for c in te.B[0]])
def Y(a, R): return np.outer(a, R) + np.outer(R, a) - (a @ R) * np.eye(3)
def m_of(a, R): s = np.linalg.svd(Y(a, R), compute_uv=False); return s[1] / s[0]
UNIT = {(Fr(1, 2), Fr(0)): "j", (Fr(0), Fr(1, 2)): "i", (Fr(1, 2), Fr(1, 2)): "k"}
AX = {"i": 0, "j": 1, "k": 2}
def tied(alpha, b):
    p = ((-3 * alpha) % 1, (3 * b) % 1)                      # p* = -3w, w = alpha tau + b  <->  (p1, p2) = (alpha, -b)
    return UNIT.get(p)
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.load(open(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
def L_of(y, which): return float(np.interp(y, [c[0] for c in col], [c[1] if which == "L_max" else c[2] for c in col]))
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
LINES = [(Fr(j, 6), Fr(k, 6)) for j in range(6) for k in range(6) if tied(Fr(j, 6), Fr(k, 6))]
def point(task):
    k, re_t, y = task[:3]
    a, b = LINES[k]; u = task[3] if len(task) > 3 else tied(a, b); t = complex(re_t, y); w = float(a) * t + float(b)
    av = [0, 0, 0]; av[AX[u]] = 1
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    readings = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    res = {"line": k, "Re_tau": re_t, "Im_tau": y}
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        for which in ("L_max", "L_2"):
            L = L_of(y, which)
            uu = {kk: (math.sqrt(2 * math.pi * L + c[kk]) * R[kk] if c[kk] is not None and 2 * math.pi * L + c[kk] > 0 else 0) for kk in B.UNITS}
            M = B.weighted_M(uu)
            for rn, SS in (readings.items() if sec == "up" else [("S", S)]):
                sv = np.linalg.svd(B.coupling(SS, M), compute_uv=False)
                res["%s|%s|%s" % (sec, which, rn)] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    return res
if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    out = {"a": {}, "b": {}}
    taus = {"i": 1j, "1.5i": 1.5j, "2.0207i": 2.0207j, "4i": 4j, "omega": complex(-0.5, math.sqrt(3) / 2)}
    rng = np.random.default_rng(63)
    for _ in range(6):
        x = rng.uniform(-0.5, 0.5); y = rng.uniform(max(0.8, math.sqrt(1 - x * x)), 2.0); taus["%.3f%+.3fi" % (x, y)] = complex(x, y)
    n = 2000; g = math.pi * (3 - math.sqrt(5)); fib = [np.array([math.cos(g * i) * math.sqrt(1 - (1 - 2 * (i + .5) / n) ** 2), 1 - 2 * (i + .5) / n, math.sin(g * i) * math.sqrt(1 - (1 - 2 * (i + .5) / n) ** 2)]) for i in range(n)]
    for name, t in taus.items():
        R = Rvec(t); ms = [m_of(a.astype(complex), R) for a in fib]
        iso = []
        for _ in range(50):                                   # isotropic: a.a = 1 - cos^2 s - sin^2 s = 0
            s = rng.uniform(0, 2 * math.pi); iso.append(m_of(np.array([1, 1j * math.cos(s), 1j * math.sin(s)]), R))
        out["a"][name] = {"min_m_real": min(ms), "max_m_real": max(ms), "m_units": {u: m_of(np.eye(3)[AX[u]].astype(complex), R) for u in AX},
                          "max_m_isotropic": max(iso), "RR_over_R2": abs(R @ R) / np.vdot(R, R).real}
    out["b"]["lines"] = [[str(a), str(b), tied(a, b)] for a, b in LINES]
    tasks = [(k, r, round(1.0 + 0.2 * j, 2)) for k in range(len(LINES)) for r in (0.0, 0.5) for j in range(16)]
    with Pool(nw) as P: rows = P.map(point, tasks, chunksize=4)
    out["b"]["rows"] = rows
    mins = {}
    for sec in ("up", "down", "lep"):
        vals = [(r[key][0], r["line"], r["Re_tau"], r["Im_tau"], key) for r in rows for key in r if key.startswith(sec + "|")]
        v = min(vals); mins[sec] = {"min_m2/m3": v[0], "line": out["b"]["lines"][v[1]], "Re_tau": v[2], "Im_tau": v[3], "choice": v[4]}
    out["b"]["min_m2_over_m3"] = mins
    out["b"]["max_abs_m2_over_m3_minus_1"] = max(abs(r[k][0] - 1) for r in rows for k in r if "|" in k)
    out["b"]["max_m1_over_m3"] = max(r[k][1] for r in rows for k in r if "|" in k)
    # (c) the control: the two untied units on the same lines at two taus
    ctasks = [(k, r, y, u) for k in range(len(LINES)) for r, y in ((0.5, 2.0), (0.0, 2.0)) for u in AX if u != tied(*LINES[k])]
    with Pool(nw) as P: crows = P.map(point, ctasks, chunksize=4)
    out["c"] = {"points": len(crows), "min_abs_m2_over_m3_minus_1": min(abs(r[k][0] - 1) for r in crows for k in r if "|" in k),
                "min_m1_over_m3": min(r[k][1] for r in crows for k in r if "|" in k)}
    json.dump(out, open(HERE / "w63_on_main.json", "w"), indent=1)
    for k, v in out["a"].items(): print(k, {kk: (round(vv, 6) if isinstance(vv, float) else {a: round(b, 6) for a, b in vv.items()}) for kk, vv in v.items()})
    print(len(LINES), "tied lines;", mins, "max |m2/m3 - 1| %.2e, max m1/m3 %.2e" % (out["b"]["max_abs_m2_over_m3_minus_1"], out["b"]["max_m1_over_m3"]))
    print("control (untied units):", out["c"])
