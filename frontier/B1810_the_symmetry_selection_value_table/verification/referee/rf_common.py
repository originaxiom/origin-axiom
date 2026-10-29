"""Referee B1810 (P-432 table), common driver.  Read-only use of the record's machinery (b1656_funcs, B1691's
the_exponents), written independently of the draft's script (same machinery, own code).  Data-free."""
import contextlib, glob, importlib.util, io, json, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
V = pathlib.Path(glob.glob(str(ROOT / "frontier" / "B1691_*" / "verification"))[0]); C = V / "correction"
sys.path.insert(0, str(C)); sys.path.insert(0, str(V)); sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("te", V / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import b1656_funcs as B
mp.mp.dps = 30

I = 1j; W = complex(0.5, math.sqrt(3) / 2)
RADII = {I: (0.688385709056232, 2.7192576281085956), W: (0.6920800405023999, 2.7864751428899948)}
SECT = {"up": (1, -4), "down": (1, 2), "lepton": (-3, 6)}
S_ = te.S
QSECS = {"DR": te.B[1], "a0": [te.B[2][j] + S_.c(F(-1, 48)) * te.e4 * te.B[0][j] for j in range(3)], "R": te.B[0],
         "t": [te.B[2][j] + S_.c(F(-5, 288)) * te.e4 * te.B[0][j] for j in range(3)]}


def theta_dir(a_, tau):
    """B1730's F_a without its eta power: (eps th2^a, eps th4^a, i th3^a), eps = i^((a+2)/2) (as c6)"""
    q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag)); eps = 1j ** ((a_ + 2) // 2)
    th2, th3, th4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    return np.array([complex(eps * th2 ** a_), complex(eps * th4 ** a_), complex(1j * th3 ** a_)])


def direction(name, tau):
    if name in QSECS: return np.array([complex(te.ev(c, mp.mpc(tau.real, tau.imag))) for c in QSECS[name]])
    return theta_dir(int(name[2:]), tau)


_cache = {}


def channels(tau, p, ql, qr):
    key = (complex(tau), tuple(p), ql, qr)
    if key not in _cache:
        w = B.line_w(p[0], p[1], tau); x, y = B.sector_twists(w, tau, ql, qr)
        R = B.residues(x, y, tau); c = B.cA(x, y, tau, R)
        _cache[key] = (R, c)
    return _cache[key]


def weights(tau, p, ql, qr, L):
    R, c = channels(tau, p, ql, qr)
    out = {}
    for k in B.UNITS:
        if c[k] is None: out[k] = 0
        else:
            wt = 2 * math.pi * L + c[k]
            out[k] = math.sqrt(wt) * R[k] if wt > 0 else 0
    return out


def Ymat(a, tau, p, ql, qr, L, tilde=False):
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    if tilde: Sm = B.EPS @ Sm.conj() @ B.EPS.T
    return B.coupling(Sm, B.weighted_M(weights(tau, p, ql, qr, L)))


def svd_sorted(Y):
    u, s, vh = np.linalg.svd(Y); o = np.argsort(s)
    return u[:, o], s[o], vh[o, :]
