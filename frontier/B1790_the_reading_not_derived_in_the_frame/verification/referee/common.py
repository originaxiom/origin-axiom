"""Referee's own driver (S226 reading-rule note). Uses only the frame's primitives (b1656_funcs, B1691 q-series);
the Higgs, readings, coupling sum, SVD and comparisons are written here."""
import sys, io, contextlib, importlib.util, pathlib, json, math
import numpy as np
ROOT = next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier/B1723_the_golden_valley/verification"))
_argv = sys.argv; sys.argv = ["x"]
import b1656_funcs as B
sys.argv = _argv
P1691 = ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification"
sys.path.insert(0, str(P1691))
spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import mpmath as mp
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ
BLK = [QJ, QI, QK]
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}

def comps(tau):
    return np.array([complex(te.ev(c, mp.mpc(tau.real, tau.imag))) for c in te.B[1]])

def quat(a): return a[0] * QI + a[1] * QJ + a[2] * QK

def tilde(S): return EPS @ np.conj(S) @ EPS.T

def Lval(im, which):
    k = 1 if which == "L_max" else 2
    return float(np.interp(im, [q[0] for q in col], [q[k] for q in col]))

def matter(tau, w, sec, which="L_max"):
    """the sector's weighted M (frame primitives)"""
    lf, rf = SECT[sec]
    x, y = B.sector_twists(w, tau, SIXY[lf], SIXY[rf]); R = B.residues(x, y, tau); c = B.cA(x, y, tau, R)
    L = Lval(tau.imag, which)
    u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
    return B.weighted_M(u)

def yuk(S, M):
    # my own coupling sum: Y_ab = sum_mn (C_a^T eps S C_b)_mn M_mn
    Y = np.zeros((3, 3), dtype=complex)
    for a, Ca in enumerate(BLK):
        for b, Cb in enumerate(BLK):
            Y[a, b] = np.sum((Ca.T @ EPS @ S @ Cb) * M)
    return Y

def ratios(Y):
    sv = np.linalg.svd(Y, compute_uv=False); return np.array([sv[1] / sv[0], sv[2] / sv[0]])

def spectra(tau, a, b, which="L_max", Shiggs=None):
    """{(sec, reading): (m2/m3, m1/m3)} at tau on the line w = a tau + b"""
    w = float(a) * tau + float(b)
    S = quat(comps(tau)) if Shiggs is None else Shiggs
    St = tilde(S); out = {}
    for sec in SECT:
        M = matter(tau, w, sec, which)
        out[(sec, "S")] = ratios(yuk(S, M)); out[(sec, "St")] = ratios(yuk(St, M))
    return out

def dln(x, y): return float(np.max(np.abs(np.log(x / y))))
