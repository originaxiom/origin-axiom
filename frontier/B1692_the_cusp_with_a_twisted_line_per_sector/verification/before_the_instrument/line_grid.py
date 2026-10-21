import pathlib as _pl
_ROOT = next(q for q in _pl.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
_B1691 = _ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
import sys, io, contextlib, importlib.util, json
sys.path.insert(0, str(_B1691))
import mpmath as mp
sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1])) if "sys" in dir() else None
from b1653_funcs import *
mp.mp.dps = 30
spec = importlib.util.spec_from_file_location("te", str(_B1691 / "the_exponents.py"))
te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
Y0 = 6
t = mp.mpc(0, Y0); q12 = mp.exp(-mp.pi * Y0)
secs = [te.B[1], te.section(2, 1)[0], te.section(4, 2)[0]]
aval = [[te.ev(c, t) for c in b] for b in secs]
def m2m3(a, alpha, beta, sec, N=192):
    w = alpha * t + beta / 2; L, Rf = SECTORS[sec]
    M = res_bil(field(w, L, t), field(w, Rf, t), t, N=N)
    Y = coupling(a[0] * QI + a[1] * QJ + a[2] * QK, M)
    s = sorted([abs(v) for v in mp.svd_c(Y, compute_uv=False)], reverse=True); return s[1] / s[0]
rows = []
for k in range(0, 13):
    alpha = mp.mpf(k) / 24
    for beta in (0, 1):
        vals = []
        for a in aval:
            base = m2m3(a, 0, 0, 'up')
            vals.append([m2m3(a, alpha, beta, s) / base for s in ('up', 'down', 'lep')])
        spread = max(abs(vals[i][j] - vals[0][j]) / vals[0][j] for i in range(1, 3) for j in range(3))
        rows.append((k, beta, [mp.nstr(v, 8) for v in vals[0]], float(spread)))
        print(k, '/24  beta', beta, [mp.nstr(v, 8) for v in vals[0]], 'section spread %.1e' % spread, flush=True)
json.dump(rows, open('line_grid.json', 'w'), indent=0)
