import mpmath as mp
from b1653_funcs import *
mp.mp.dps = 30
def sector_sv(alpha, beta, y, sec):
    t = mp.mpc(0, y); w = alpha * t + beta / 2
    L, Rf = SECTORS[sec]
    M = res_bil(field(w, L, t), field(w, Rf, t), t)
    s = sorted([abs(v) for v in mp.svd_c(M, compute_uv=False)], reverse=True)
    return s
for alpha in (0, mp.mpf(1)/12, mp.mpf(1)/6, mp.mpf(1)/4, mp.mpf(1)/3, mp.mpf(5)/12, mp.mpf(1)/2):
    row = []
    for sec in ('up', 'down', 'lep'):
        a = sector_sv(alpha, 0, 3, sec); b = sector_sv(alpha, 0, 4, sec)
        sl = [float(-mp.log(b[i] / a[i]) / (2 * mp.pi)) for i in range(2)]
        row.append((sec, [round(x, 3) for x in sl]))
    print('alpha', mp.nstr(alpha, 4), row, flush=True)
