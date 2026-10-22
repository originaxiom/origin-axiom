"""B1723 (the completion map's C3; L254, P-069): the golden valley.  B1636's modular-invariant F = sum_p |theta_p/eta|^4,
built from the weave's own forms, takes the value 8 on the discriminant-5 geodesics, so (F - 8)^2 is a functional whose
valley is that locus.  Modulo SL(2, Z) the locus is one closed geodesic, the tick's (the axis of LR, through i); in the
fundamental domain it is the two mirror arcs from i to +-1/2 + (sqrt 5/2) i (each of hyperbolic length log phi, heights
1 to sqrt 5/2).  If no point of the valley, with any line, gives the six ratios specifically, no functional with this
valley does.
The points: 25 per arc, equally spaced in arclength (i counted once): 49.  The lines: every flat line w = alpha tau + b of
exact order N, 2 <= N <= 12, up to sign (an SL(2, Z)-invariant set, so sampling the fundamental domain suffices).  With
the weight-3/2 section DR (one unit on v+, B1700), B1667's canonical end at both horocycles (L read at Im tau from its
Re tau = 1/4 column, as B1712), B1656's four-channel coupling and B1660's three up readings: the six charged-fermion
ratios and the quark mixing (as B1713).  No free continuous number but the position along the valley.  No data.
The instrument asserts its own domain: every point has 1 <= Im tau <= 4 (B1667's tabulated range).
    python3 -B the_golden_valley.py [--workers 8]      # writes the_golden_valley.json beside itself"""
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
PHI = (1 + math.sqrt(5)) / 2
K = 25


def valley_points():
    """the two arcs, by arclength s from the apex (s = 0) to i (s = log phi): theta = 2 arctan(e^s) on |z - c| = sqrt5/2"""
    r = math.sqrt(5) / 2; out = []
    for sgn in (1, -1):
        for k in range(K):
            if sgn == -1 and k == K - 1: continue                              # i, already on the first arc
            s = k * math.log(PHI) / (K - 1); th = 2 * math.atan(math.exp(s))
            z = complex(0.5 + r * math.cos(th), r * math.sin(th))
            if sgn == -1: z = complex(-z.real, z.imag)
            out.append({"arc": sgn, "s": s, "tau": [z.real, z.imag]})
    return out


def _lines():
    seen, out = set(), []
    for N in range(2, 13):
        for j in range(N):
            for k in range(N):
                if math.gcd(math.gcd(j, k), N) != 1: continue
                a, b = Fr(j, N), Fr(k, N); key = min((a, b), ((-a) % 1, (-b) % 1))
                if key in seen: continue
                seen.add(key); out.append(key)
    return out


POINTS = valley_points()
LINES = _lines()
TASKS = [(i, j) for i in range(len(POINTS)) for j in range(len(LINES))]
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.load(open(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)


def L_of(y, which):
    assert col[0][0] - 1e-9 <= y <= col[-1][0] + 1e-9, "Im tau %.6f outside B1667's tabulated range" % y
    return float(np.interp(y, [c[0] for c in col], [c[1] if which == "L_max" else c[2] for c in col]))


SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}


def ckm(Yu, Yd):
    Uu = np.linalg.svd(Yu)[0][:, ::-1]; Ud = np.linalg.svd(Yd)[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2])), J, float(np.max(np.abs(V @ np.conj(V.T) - np.eye(3))))]


_S_CACHE = {}


def _S(t):
    key = (round(t.real, 14), round(t.imag, 14))
    if key not in _S_CACHE:
        av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
        _S_CACHE[key] = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    return _S_CACHE[key]


def point(task):
    i, j = task; a, b = LINES[j]
    t = complex(*POINTS[i]["tau"]); w = float(a) * t + float(b)
    S = _S(t)
    readings = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    res = {"point": i, "line": j}; Y = {}
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
    w = a * t + b; S = _S(t); out = []
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        LL = L_of(t.imag, "L_max") if L is None else L
        u = {kk: (math.sqrt(2 * math.pi * LL + c[kk]) * R[kk] if c[kk] is not None and 2 * math.pi * LL + c[kk] > 0 else 0) for kk in B.UNITS}
        sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False); out += [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    return out


def _dev(x, y): return max((abs(math.log(p / q)) for p, q in zip(x, y) if p > 1e-10 and q > 1e-10), default=0.0)


def control(j):
    """C1: the same configuration in another basis gives the same ratios.  (i) T: the apexes -1/2 + h i and 1/2 + h i are
    one point, tau -> tau + 1 with (a, b) -> (a, b - a): bar 1e-6.  (ii) S at i, the fixed point: tau -> -1/tau = i with
    (a, b) -> (-b, a) and the end unchanged (L' = L + log|tau| = L): bar 1e-6.  Ratios below 1e-10 are not compared."""
    a, b = LINES[j]; h = math.sqrt(5) / 2
    dT = _dev(ratios_at(complex(-0.5, h), float(a), float(b)), ratios_at(complex(0.5, h), float(a), float(b - a)))
    dS = _dev(ratios_at(1j, float(a), float(b)), ratios_at(1j, float(-b), float(a)))
    return {"line": [str(a), str(b)], "T": dT, "S": dS}


def control_lines(n=12):
    """the first n lines of order neither 4 nor 12 (the zero law's), in census order"""
    out = []
    for j, (a, b) in enumerate(LINES):
        if math.lcm(a.denominator, b.denominator) not in (4, 12): out.append(j)
        if len(out) >= n: break
    return out


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    with Pool(nw) as P:
        out = P.map(point, TASKS, chunksize=16)
        ctrl = P.map(control, control_lines(12))
    json.dump({"points": POINTS, "lines": [[str(a), str(b)] for a, b in LINES], "rows": out, "C1_control": ctrl},
              open(HERE / "the_golden_valley.json", "w"))
    print(len(POINTS), "points;", len(LINES), "lines;", len(out), "rows; C1 T %.2e, S %.2e" % (max(c["T"] for c in ctrl), max(c["S"] for c in ctrl)))
