import mpmath as mp
from b1653_funcs import *
mp.mp.dps = 30
S = ONE * mp.mpf('0.3') + QI * mp.mpf('0.7') + QJ * mp.mpf('-0.4') + QK * mp.mpf('0.5')   # one fixed real Higgs quaternion
def masses(alpha, y, sec, N=192):
    t = mp.mpc(0, y); w = alpha * t
    L, Rf = SECTORS[sec]
    M = res_bil(field(w, L, t), field(w, Rf, t), t, N=N)
    Y = coupling(S, M)
    return sorted([abs(v) for v in mp.svd_c(Y, compute_uv=False)], reverse=True)
for alpha in (0, mp.mpf(1)/12, mp.mpf(1)/6, mp.mpf(1)/4, mp.mpf(1)/3, mp.mpf(1)/2):
    out = {}
    for sec in ('up', 'down', 'lep'):
        ms = {y: masses(alpha, y, sec) for y in (3, 4, 5)}
        sl3 = [round(float(-mp.log(ms[b][0] / ms[a][0]) / (2 * mp.pi * (b - a))), 3) for a, b in ((3, 4), (4, 5))]
        r2 = [mp.nstr(ms[y][1] / ms[y][0], 3) for y in (3, 4, 5)]
        out[sec] = (sl3, r2, mp.nstr(ms[5][2] / ms[5][0], 2))
    print('alpha', mp.nstr(alpha, 3), out, flush=True)
