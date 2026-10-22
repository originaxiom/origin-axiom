"""B1720: the thread fixes the point.  For every primitive positive class w of length 2-9 (both letters) whose closed
geodesic's highest point on the modular surface lies at Im tau <= 4 (B1667's tabulated range): tau = that apex
(Im tau = Lagrange(w)/2, the thread's height), and every flat line the class's monodromy fixes up to sign (A^T v = +-v,
B1698's moves).  With the weight-3/2 section DR (one unit on v+, B1700), B1667's canonical end (both horocycles) and
B1656's four-channel coupling, B1660's three up readings: the six charged-fermion ratios and the quark mixing (as B1713).
No free continuous number.  No data.
    python3 -B the_thread_census.py [--workers 8]      # writes the_thread_census.json beside itself"""
import sys, io, json, math, contextlib, importlib.util, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(HERE)); _argv = sys.argv; sys.argv = ['x']
import b1656_funcs as B
import thread_geometry as TG
sys.argv = _argv
P1691 = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(P1691))
spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import mpmath as mp
CENSUS = TG.census(2, 9, 4.0)
TASKS = [(k, j) for k, r in enumerate(CENSUS) for j in range(len(r["lines"]))]
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.load(open(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
def L_of(y, which): return float(np.interp(y, [c[0] for c in col], [c[1] if which == "L_max" else c[2] for c in col]))
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
def ckm(Yu, Yd):
    Uu = np.linalg.svd(Yu)[0][:, ::-1]; Ud = np.linalg.svd(Yd)[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2])), J, float(np.max(np.abs(V @ np.conj(V.T) - np.eye(3))))]
def point(task):
    k, j = task; r = CENSUS[k]; a, b = r["lines"][j]
    t = complex(*r["tau"]); w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    readings = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    res = {"class": k, "line": j}; Y = {}
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        for which in ("L_max", "L_2"):
            L = L_of(t.imag, which)
            u = {kk: (math.sqrt(2 * math.pi * L + c[kk]) * R[kk] if c[kk] is not None and 2 * math.pi * L + c[kk] > 0 else 0) for kk in B.UNITS}
            M = B.weighted_M(u)
            for rn, SS in (readings.items() if sec == "up" else [("S", S)]):
                Ym = B.coupling(SS, M); Y[(sec, which, rn)] = Ym
                sv = np.linalg.svd(Ym, compute_uv=False)
                res["%s|%s|%s" % (sec, which, rn)] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    for which in ("L_max", "L_2"):
        for rn in readings:
            res["ckm|%s|%s" % (which, rn)] = ckm(Y[("up", which, rn)], Y[("down", which, "S")])
    return res
def ratios_at(t, a, b, L=None):
    """the six ratios at (tau, line (a, b)), at the maximal horocycle (L given, or read at Im tau), reading S"""
    w = a * t + b
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK; out = []
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        LL = L_of(t.imag, "L_max") if L is None else L
        u = {kk: (math.sqrt(2 * math.pi * LL + c[kk]) * R[kk] if c[kk] is not None and 2 * math.pi * LL + c[kk] > 0 else 0) for kk in B.UNITS}
        sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False); out += [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    return out
def _dev(x, y): return max((abs(math.log(p / q)) for p, q in zip(x, y) if p > 1e-10 and q > 1e-10), default=0.0)
def _order(a, b): return math.lcm(a.denominator, b.denominator)
def control(task):
    """C1: the same physical configuration in another basis gives the same ratios.  (i) T-moves, tau -> tau + n with
    (a, b) -> (a, b - n a), n = 1, -1: bar 1e-6.  (ii) the R-move tau -> tau/(tau + 1) with (a, b) -> (a - b, b), from the
    apex translated to |Re tau| <= 1/2, only where Im of the image is >= 0.3 (the Higgs's q-series is exact there), with
    the end transformed as L' = L + log|tau + 1| (B1667's L = log(1/eps) in the flat coordinate): bar 1e-5.  Lines of
    order 4 (and 12, the leptons' zero) are not used; ratios below 1e-10 are not compared."""
    k, j = task; r = CENSUS[k]; a, b = r["lines"][j]; t = complex(*r["tau"])
    base = ratios_at(t, float(a), float(b)); dT = 0.0
    for n in (1, -1):
        dT = max(dT, _dev(base, ratios_at(t + n, float(a), float(b - n * a))))
    n0 = round(t.real); t0 = t - n0; a0, b0 = a, b + n0 * a                   # translate the apex to |Re| <= 1/2
    t1 = t0 / (t0 + 1); dR = None
    if t1.imag >= 0.3:
        L1 = L_of(t0.imag, "L_max") + math.log(abs(t0 + 1))
        dR = _dev(ratios_at(t0, float(a0), float(b0)), ratios_at(t1, float(a0 - b0), float(b0), L=L1))
    return {"class": k, "line": j, "T": dT, "R": dR}
def control_tasks(n=8):
    out = []
    for k, r in enumerate(CENSUS):
        h = r["height"]
        if not (1.1 <= h <= 2.4): continue
        for j, (a, b) in enumerate(r["lines"]):
            if _order(a, b) not in (4, 12):
                out.append((k, j)); break
        if len(out) >= n: break
    return out
if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    with Pool(nw) as P:
        out = P.map(point, TASKS, chunksize=8)
        ctrl = P.map(control, control_tasks(8))
    json.dump({"classes": [{"word": r["word"], "height": r["height"], "A": r["A"], "tau": r["tau"], "lines": [[str(a), str(b)] for a, b in r["lines"]]} for r in CENSUS],
               "rows": out, "C1_control": ctrl}, open(HERE / "the_thread_census.json", "w"))
    print(len(CENSUS), "classes;", len(out), "points; C1 T %.2e, R %s" % (max(c["T"] for c in ctrl), [c["R"] for c in ctrl]))
