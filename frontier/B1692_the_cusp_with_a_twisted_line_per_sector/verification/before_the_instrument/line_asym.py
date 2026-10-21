import pathlib as _pl
_ROOT = next(q for q in _pl.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
_B1691 = _ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
import sys, io, contextlib, importlib.util
sys.path.insert(0, str(_B1691))
import mpmath as mp
sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1])) if "sys" in dir() else None
from b1653_funcs import *
mp.mp.dps = 45
spec = importlib.util.spec_from_file_location("te", str(_B1691 / "the_exponents.py"))
te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
def m2m3(a, t, alpha, sec, N=256):
    w = alpha * t; L, Rf = SECTORS[sec]
    M = res_bil(field(w, L, t), field(w, Rf, t), t, N=N)
    Y = coupling(a[0] * QI + a[1] * QJ + a[2] * QK, M)
    s = sorted([abs(v) for v in mp.svd_c(Y, compute_uv=False)], reverse=True); return s[1] / s[0]
for k in (5, 7, 13, 17, 19, 23):
    alpha = mp.mpf(k) / 48
    out = []
    for y in (6, 10, 14):
        t = mp.mpc(0, y); a = [te.ev(c, t) for c in te.B[1]]; base = m2m3(a, t, 0, 'up')
        out.append((y, [mp.nstr(m2m3(a, t, alpha, s) / base, 7) for s in ('up', 'down', 'lep')]))
    print('alpha', k, '/48', out, flush=True)
