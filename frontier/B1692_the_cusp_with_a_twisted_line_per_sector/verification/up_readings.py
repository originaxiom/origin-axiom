"""B1692's check after the census: the up sector read through B1660's three readings of one Higgs (S, S~ = eps conj(S) eps^T, conj(S));
the largest one-Higgs spread over the lines j/24."""
import sys, io, contextlib, importlib.util
import pathlib as _pl
_ROOT = next(q for q in _pl.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
_B1691 = _ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(_B1691)); sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))
import mpmath as mp
from b1653_funcs import *
mp.mp.dps = 35
spec = importlib.util.spec_from_file_location("te", str(_B1691 / "the_exponents.py"))
te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
def m2m3_S(S, t, alpha, L, R, N=192):
    w = alpha * t
    M = res_bil(twist_of(SIXY[L] * w, t), twist_of(SIXY[R] * w, t), t, N=N)
    Y = coupling(S, M)
    s = sorted([abs(v) for v in mp.svd_c(Y, compute_uv=False)], reverse=True); return s[1] / s[0]
def conjm(S): return mp.matrix([[mp.conj(S[i, j]) for j in range(2)] for i in range(2)])
for y in (2, 3, 6):
    t = mp.mpc(0, y)
    for name, basis in (("DR", te.B[1]), ("w7/2", te.section(2, 1)[0])):
        a = [te.ev(c, t) for c in basis]; S = a[0] * QI + a[1] * QJ + a[2] * QK
        readings = {"S": S, "St": EPS * conjm(S) * EPS.T, "conjS": conjm(S)}
        worst = 0
        for j in range(0, 25):
            al = mp.mpf(j) / 24
            d = m2m3_S(S, t, al, "Q", "d"); e = m2m3_S(S, t, al, "L", "e")
            for rn, Su in readings.items():
                u = m2m3_S(Su, t, al, "Q", "u")
                sp = max(u, d, e) / min(u, d, e)
                if sp > worst: worst, arg = sp, (j, rn, float(u / d), float(e / d))
        print('y', y, name, 'max one-Higgs spread over lines and up readings: %.3f' % worst, arg, flush=True)
