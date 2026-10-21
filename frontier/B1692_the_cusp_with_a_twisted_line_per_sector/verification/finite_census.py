import pathlib as _pl
_ROOT = next(q for q in _pl.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
_B1691 = _ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
import sys, io, contextlib, importlib.util, json
from multiprocessing import Pool
sys.path.insert(0, str(_B1691))
import mpmath as mp
from b1653_funcs import *
mp.mp.dps = 35
spec = importlib.util.spec_from_file_location("te", str(_B1691 / "the_exponents.py"))
te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
SECS = {"DR": te.B[1], "w7/2a": te.section(2, 1)[0], "w7/2b": te.section(2, 2)[0], "w15/2": te.section(4, 3)[0]}
def job(task):
    j, y, name = task
    t = mp.mpc(0, y); A = [te.ev(c, t) for c in SECS[name]]
    def m2m3(alpha, sec, N=192):
        w = alpha * t; L, Rf = SECTORS[sec]
        M = res_bil(field(w, L, t), field(w, Rf, t), t, N=N)
        Y = coupling(A[0] * QI + A[1] * QJ + A[2] * QK, M)
        s = sorted([abs(v) for v in mp.svd_c(Y, compute_uv=False)], reverse=True); return s[1] / s[0]
    v = [m2m3(mp.mpf(j) / 60, s) for s in ('up', 'down', 'lep')]
    return (j, y, name, [float(x) for x in v])
if __name__ == "__main__":
    tasks = [(j, y, n) for j in range(0, 61) for y in (1.5, 2, 3) for n in SECS]
    with Pool(4) as P: res = P.map(job, tasks)
    json.dump(res, open('finite_census.json', 'w'))
    for y in (1.5, 2, 3):
        for n in SECS:
            sp = [max(v) / min(v) for j, yy, nn, v in res if yy == y and nn == n]
            mm = [v for j, yy, nn, v in res if yy == y and nn == n]
            print('y', y, n, 'max spread %.4f' % max(sp), 'm2/m3 range %.3g..%.3g' % (min(min(v) for v in mm), max(max(v) for v in mm)), flush=True)
