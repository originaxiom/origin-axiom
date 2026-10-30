"""P-512 exploration helpers (labelled exploration, data-free): read-only use of main's committed modules, from a checkout of
main at 5e5e75ac4 named by the environment variable OA_MAIN. Nothing is written into that checkout."""
import sys, io, json, math, contextlib, importlib.util, pathlib, os
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"; sys.dont_write_bytecode = True
import numpy as np
import mpmath as mp
ROOT = pathlib.Path(os.environ["OA_MAIN"])  # a checkout of main at 5e5e75ac4
sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification")); _argv = sys.argv; sys.argv = ["x"]
import b1656_funcs as B
sys.argv = _argv
P1691 = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(P1691))
spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads((ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text(encoding="utf-8"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
QI, QJ, QK, EPS = B.QI, B.QJ, B.QK, B.EPS
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}

def S_of(t):
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    return av[0] * QI + av[1] * QJ + av[2] * QK, av

def Lval(im_t, h="L_max"):
    k = 1 if h == "L_max" else 2
    return float(np.interp(im_t, [q[0] for q in col], [q[k] for q in col]))

def sector_M(t, a, b, sec, h="L_max", twists=None, with_c=True):
    """the weighted M for one sector (as B1726's compute), plus the pieces"""
    w = float(a) * t + float(b)
    lf, rf = SECT[sec]
    if twists is None:
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf])
    else:
        x, yy = twists
    R = B.residues(x, yy, t)
    c = B.cA(x, yy, t, R) if with_c else {s: 0.0 for s in B.UNITS}
    L = Lval(t.imag, h)
    u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
    Mw = B.weighted_M(u)
    return dict(x=x, y=yy, R=R, c=c, L=L, u=u, M=Mw)

def Ymat(S, M):
    return B.coupling(S, M)

def ratios(Y):
    sv = np.linalg.svd(Y, compute_uv=False)
    return sv[1] / sv[0], sv[2] / sv[0], sv
