import random, mpmath as mp
from fractions import Fraction as F
from series import *
mp.mp.dps = 30
exec(open('census_probe.py').read().split('def exps(a):')[0])        # R, B0, B1, B2, M, dot
def ev(s, tau):
    x = mp.exp(2j * mp.pi * tau / 8)
    return mp.fsum(mp.mpc(a.numerator / mp.mpf(a.denominator), b.numerator / mp.mpf(b.denominator)) * x ** k for k, (a, b) in s.d.items())
OM = mp.mpc(-0.5, mp.sqrt(3) / 2)
def masses(a, tau):
    av = [ev(c, tau) for c in a]; Rv = [ev(c, tau) for c in R]
    aa = sum(u * u for u in av); aR = sum(u * v for u, v in zip(av, Rv)); aRb = sum(u * mp.conj(v) for u, v in zip(av, Rv))
    na = sum(abs(u) ** 2 for u in av); nR = sum(abs(v) ** 2 for v in Rv)
    s1sq = 2 * nR * na + 2 * abs(aRb) ** 2 - abs(aR) ** 2
    return float(nR * abs(aa) / s1sq), float(abs(aR) / mp.sqrt(s1sq) / nR), float(abs(aa) / na)   # m2/m3, m1/m3 without |D|/(2 pi L), |a.a|/|a|^2
for n in range(0, 7):
    k = F(4 * n - 1, 2)
    fs = [(0, M(2 * n)), (1, M(2 * n - 2) if n >= 1 else []), (2, M(2 * n - 4) if n >= 2 else [])]
    rng = random.Random(7 + n); a = [S(), S(), S()]
    for j, basis in fs:
        for f in basis:
            c = S.c(F(rng.randint(-9, 9) or 1, rng.randint(1, 5)), F(rng.randint(-9, 9), rng.randint(1, 5)))
            for i in range(3): a[i] = a[i] + c * f * (B0, B1, B2)[j][i]
    rows = []
    for eps in (mp.mpf('1e-3'), mp.mpf('1e-4')):
        rows.append(masses(a, OM + eps * mp.exp(0.7j)))
    sl = [mp.log(rows[0][i] / rows[1][i]) / mp.log(10) if rows[1][i] > 0 else None for i in range(3)]
    print('k', k, 'at eps 1e-3:', ['%.3e' % v for v in rows[0]], 'slopes in eps:', [mp.nstr(s, 4) if s is not None else None for s in sl])
