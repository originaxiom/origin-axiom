import pathlib as _pl
_ROOT = next(q for q in _pl.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
_B1691 = _ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
import sys, io, contextlib, importlib.util
sys.path.insert(0, str(_B1691))
import mpmath as mp
sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1])) if "sys" in dir() else None
from b1653_funcs import *
mp.mp.dps = 30
spec = importlib.util.spec_from_file_location("te", str(_B1691 / "the_exponents.py"))
te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
S_ = None
def section_value(sec_basis, tau):                     # a in M on (e_i, e_j, e_k)
    return [te.ev(c, tau) for c in sec_basis]
def masses_cov(a_vec, alpha, y, sec, N=192):
    t = mp.mpc(0, y); w = alpha * t
    L, Rf = SECTORS[sec]
    M = res_bil(field(w, L, t), field(w, Rf, t), t, N=N)
    S = a_vec[0] * QI + a_vec[1] * QJ + a_vec[2] * QK
    Y = coupling(S, M)
    return sorted([abs(v) for v in mp.svd_c(Y, compute_uv=False)], reverse=True)
DR = te.B[1]
for y in (3, 4, 5):
    t = mp.mpc(0, y); a = section_value(DR, t)
    m = masses_cov(a, 0, y, 'up')
    print('alpha 0, a = DR, y', y, 'm2/m3 / |q|^(1/2) =', mp.nstr(m[1] / m[0] / mp.exp(-mp.pi * y), 8), ' m1/m3', mp.nstr(m[2] / m[0], 3))
print('--- twisted lines, a = DR (weight 3/2) and a generic weight-7/2 section')
a72, _ = te.section(2, 1)
for alpha in (mp.mpf(1)/12, mp.mpf(1)/6, mp.mpf(1)/4, mp.mpf(1)/3, mp.mpf(1)/2):
    row = {}
    for name, basis in (('DR', DR), ('w7/2', a72)):
        for sec in ('up', 'down', 'lep'):
            r = {}
            for y in (3, 4, 5):
                t = mp.mpc(0, y); m = masses_cov(section_value(basis, t), alpha, y, sec); r[y] = (m[1] / m[0], m[2] / m[0])
            sl = [round(float(-mp.log(r[b][0] / r[a][0]) / (2 * mp.pi * (b - a))), 3) for a, b in ((3, 4), (4, 5))]
            row[(name, sec)] = (sl, mp.nstr(r[5][0], 3))
    print('alpha', mp.nstr(alpha, 3), row, flush=True)
