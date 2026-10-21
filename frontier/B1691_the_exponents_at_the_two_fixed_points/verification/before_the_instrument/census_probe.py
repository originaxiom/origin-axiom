import random, time
from fractions import Fraction as F
from series import *
t0 = time.time()
th2, th3, th4 = theta2(), theta3(1), theta3(-1)
di = (th2 * th3 * th4).inv()
R = [-(th2 * th2) * di, -(th4 * th4) * di, (th3 * th3) * S.c(0, 1) * di]
e2 = E2(); e4 = E4(); e6 = E6()
B0 = R
B1 = [serre(c, F(-1, 2), e2) for c in B0]
B2 = [serre(c, F(3, 2), e2) for c in B1]
def M(w):                                       # a basis of M_w(SL2Z) as monomials E4^a E6^b
    out = []
    for a in range(0, w // 4 + 1):
        for b in range(0, w // 6 + 1):
            if 4 * a + 6 * b == w:
                f = S.c(1)
                for _ in range(a): f = f * e4
                for _ in range(b): f = f * e6
                out.append(f)
    return out
dot = lambda u, v: u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
nrm = lambda u: u[0] * u[0].conj() + u[1] * u[1].conj() + u[2] * u[2].conj()
RRb = nrm(R)
def exps(a):
    aa = dot(a, a); aR = dot(a, R); aRb = dot(a, [c.conj() for c in R]); na = nrm(a)
    s1 = RRb * na * S.c(2) + aRb * aRb.conj() * S.c(2) - aR * aR.conj()
    if aa.ord() is None: d2 = None
    else: d2 = F(RRb.ord() + aa.ord() - s1.ord(), 8)
    d1 = None if aR.ord() is None else F(2 * (8 + aR.ord()) - s1.ord(), 16)
    return d2, d1, (aa.ord(), aR.ord(), na.ord(), s1.ord())
for n in range(0, 7):
    k = F(4 * n - 1, 2)
    fs = [(0, M(2 * n)), (1, M(2 * n - 2) if n >= 1 else []), (2, M(2 * n - 4) if n >= 2 else [])]
    dim = sum(len(f) for _, f in fs)
    res = []
    for seed in (1, 2):
        rng = random.Random(seed * 100 + n)
        a = [S(), S(), S()]
        for j, basis in fs:
            Bj = (B0, B1, B2)[j]
            for f in basis:
                c = S.c(F(rng.randint(-9, 9) or 1, rng.randint(1, 5)), F(rng.randint(-9, 9), rng.randint(1, 5)))
                for i in range(3): a[i] = a[i] + c * f * Bj[i]
        res.append(exps(a))
    print('k', k, 'dim', dim, res, round(time.time() - t0, 1), flush=True)
