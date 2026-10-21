import pathlib as _pl
_ROOT = next(q for q in _pl.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
_B1691 = _ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
import sys, io, contextlib, importlib.util, json
from multiprocessing import Pool
sys.path.insert(0, str(_B1691))
import mpmath as mp
from b1653_funcs import *
mp.mp.dps = 45
spec = importlib.util.spec_from_file_location("te", str(_B1691 / "the_exponents.py"))
te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
Y0 = 14; t = mp.mpc(0, Y0); A = [te.ev(c, t) for c in te.B[1]]
def m2m3(alpha, beta, sec, N=256):
    w = alpha * t + beta / 2; L, Rf = SECTORS[sec]
    M = res_bil(field(w, L, t), field(w, Rf, t), t, N=N)
    Y = coupling(A[0] * QI + A[1] * QJ + A[2] * QK, M)
    s = sorted([abs(v) for v in mp.svd_c(Y, compute_uv=False)], reverse=True); return s[1] / s[0]
BASE = None
def job(task):
    j, beta = task
    base = m2m3(0, 0, 'up')
    v = [m2m3(mp.mpf(j) / 120, beta, s) / base for s in ('up', 'down', 'lep')]
    return (j, float(beta), [float(x) for x in v])
if __name__ == "__main__":
    tasks = [(j, b) for j in range(0, 121) for b in (0, mp.mpf(1) / 2, 1, mp.mpf(3) / 2)]
    with Pool(4) as P: res = P.map(job, tasks)
    json.dump(res, open('line_census.json', 'w'))
    spreads = [max(v) / min(v) for _, _, v in res]
    print('lines', len(res), 'max spread', max(spreads), 'values range', min(min(v) for _, _, v in res), max(max(v) for _, _, v in res))
