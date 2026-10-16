"""EXPLORATION (P-183 step 3, design only; disclosed): (a) f's mirror invariance f(-conj t) = f(t); (b) the ray instrument --
the time average of f along the geodesic ray to xi, approximated by the closed geodesic of the word built from xi's first
continued-fraction digits (<= NL letters), against the Liouville average 0.31500491 for Lebesgue-random xi (a control)."""
import sys, math, random, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
from motion_defect import f_fast, f, reduce
rng = random.Random(3)
pts = [complex(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 2.5)) for _ in range(5)]
print("mirror: max |f(-conj t)/f(t) - 1| =", max(abs(f(-t.conjugate())/f(t) - 1) for t in pts))
def word_avg(digits, K=None):
    """closed geodesic of L^a1 R^a2 ... (even number of blocks), <f> over one period (motion_defect's method)"""
    M = (1, 0, 0, 1)
    def mul(A, B): a, b, c, d = A; e, g, h, k = B; return (a*e + b*h, a*g + b*k, c*e + d*h, c*g + d*k)
    for j, a in enumerate(digits):
        G = (1, 1, 0, 1) if j % 2 == 0 else (1, 0, 1, 1)
        for _ in range(a): M = mul(M, G)
    a, b, c, d = M; tr = a + d; ell = 2*math.acosh(tr/2); disc = math.sqrt(tr*tr - 4)
    xp, xm = ((a - d) + disc)/(2*c), ((a - d) - disc)/(2*c); cen, rad = (xp + xm)/2, abs(xp - xm)/2
    K = K or max(64, int(25*ell)); gx, gw = np.polynomial.legendre.leggauss(K); tot = 0.0
    for x, w in zip(gx, gw):
        s = (x + 1)/2*ell; th = 2*math.atan(math.exp(s - ell/2))
        tot += w*ell/2*f_fast(reduce(complex(cen + rad*math.cos(th), rad*math.sin(th))))
    return tot/ell, ell
def cf_digits(num, den, nmax):
    out = []
    while den and len(out) < nmax:
        q, r = divmod(num, den); out.append(q); num, den = den, r
    return out
def ray_avg(x_num, x_den, NL=60):
    d = [a for a in cf_digits(x_num, x_den, 400)[1:] if a > 0]
    blocks, tot = [], 0
    for a in d:
        if tot + a > NL: break
        blocks.append(a); tot += a
    if len(blocks) % 2: blocks = blocks[:-1]
    return word_avg(blocks) if len(blocks) >= 2 else (float("nan"), 0)
# control: Lebesgue-random xi in (0,1) as an exact fraction with 60 digits
vals = []
for _ in range(60):
    num = rng.getrandbits(200); den = 1 << 200
    v, ell = ray_avg(num, den); vals.append(v)
vals = [v for v in vals if v == v]
print(f"Lebesgue control: mean <f> = {np.mean(vals):.4f} +- {np.std(vals)/math.sqrt(len(vals)):.4f} over {len(vals)} rays (Liouville 0.3150)")
