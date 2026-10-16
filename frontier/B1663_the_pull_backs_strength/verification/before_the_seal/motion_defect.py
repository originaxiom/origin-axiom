"""EXPLORATION (P-177: 'sizes from motion'; the owner's push/push-back reading). f(tau) = |D(tau)| / ||R(tau)||^2, the
matter's isotropy defect relative to its norm (W87's closed form, as B1657 implements it): zero exactly on omega's orbit
and vanishing toward the cusp (found: 0.21 at 2i, 9.5e-4 at 4i; largest near i). Step 1: f's invariance under the moves L, R (so a thread's closed
geodesic average is defined and points can be reduced to the fundamental domain). Step 2: <f>_thread = (1/l) int f ds
along each primitive thread's closed geodesic (l = 2 arccosh(tr/2)), for every Lyndon word in L, R to length N."""
import math, sys, itertools
import mpmath as mp
mp.mp.dps = 20
def f(t):
    t = mp.mpc(t); q = mp.exp(1j*mp.pi*t)
    t2, t3, t4 = (mp.jtheta(j, 0, q) for j in (2, 3, 4)); eta = mp.exp(1j*mp.pi*t/12)*mp.qp(mp.exp(2j*mp.pi*t))
    lam = t2**4/t3**4; h = lam*mp.log(abs(lam)) + (1 - lam)*mp.log(abs(1 - lam))
    D = -t3**4*h/(4*mp.pi*eta**6); Rn = (abs(t2)**4 + abs(t3)**4 + abs(t4)**4)/abs(2*mp.pi*eta**3)**2
    return float(abs(D)/Rn)
import numpy as _np
_N = _np.arange(-12, 13); _K = _np.arange(1, 60)
def f_fast(t):
    """f by plain series (valid after reduction to the fundamental domain, Im t >= sqrt3/2: |q| <= e^{-pi sqrt3/2})"""
    q = _np.exp(1j*_np.pi*t)
    t3 = _np.sum(q**(_N**2)); t4 = _np.sum((-1.0)**_N*q**(_N**2)); t2 = _np.sum(_np.exp(1j*_np.pi*t*(_N + 0.5)**2))
    eta = _np.exp(1j*_np.pi*t/12)*_np.prod(1 - _np.exp(2j*_np.pi*t*_K))
    lam = t2**4/t3**4; h = lam*_np.log(abs(lam)) + (1 - lam)*_np.log(abs(1 - lam))
    D = -t3**4*h/(4*_np.pi*eta**6); Rn = (abs(t2)**4 + abs(t3)**4 + abs(t4)**4)/abs(2*_np.pi*eta**3)**2
    return float(abs(D)/Rn)
def mob(M, t): a, b, c, d = M; return (a*t + b)/(c*t + d)
def reduce(t):
    """to the standard fundamental domain by T and S (the full modular group)"""
    for _ in range(200):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-15: t = -1/t
        else: return t
    return t
if __name__ == "__main__":
    import random; random.seed(1)
    pts = [complex(random.uniform(-0.5, 0.5), random.uniform(0.6, 2.0)) for _ in range(6)]
    for name, M in (("L", (1, 1, 0, 1)), ("R", (1, 0, 1, 1)), ("S", (0, -1, 1, 0))):
        dev = max(abs(f(mob(M, t))/f(t) - 1) for t in pts)
        print(f"invariance under {name}: max |f(M t)/f(t) - 1| = {dev:.2e}")
    import random as _r; _r.seed(5)
    chk = [reduce(complex(_r.uniform(-3, 3), _r.uniform(0.05, 3))) for _ in range(40)]
    print("f_fast vs mpmath f on 40 reduced points: max rel", max(abs(f_fast(t)/f(t) - 1) for t in chk if f(t) > 1e-12))
    print("f at omega:", f(complex(-0.5, math.sqrt(3)/2)), " at i:", f(1j), " at 2i:", f(2j), " at 4i:", f(4j))
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    def lyndon(n):
        out = []
        for w in itertools.product("LR", repeat=n):
            w = "".join(w)
            if "L" in w and "R" in w and all(w < w[i:] + w[:i] for i in range(1, n)): out.append(w)
        return out
    MAT = {"L": (1, 1, 0, 1), "R": (1, 0, 1, 1)}
    def mul(A, B): a, b, c, d = A; e, g, h, k = B; return (a*e + b*h, a*g + b*k, c*e + d*h, c*g + d*k)
    rows = []
    for n in range(2, NMAX + 1):
        for w in lyndon(n):
            M = (1, 0, 0, 1)
            for ch in w: M = mul(M, MAT[ch])
            a, b, c, d = M; tr = a + d; ell = 2*math.acosh(tr/2)
            disc = math.sqrt(tr*tr - 4); xp, xm = ((a - d) + disc)/(2*c), ((a - d) - disc)/(2*c)
            cen, rad = (xp + xm)/2, abs(xp - xm)/2
            K = max(64, int(40*ell))
            # arc length s along the semicircle: theta = 2 atan(e^s); one period = ell; Gauss-Legendre on [0, ell]
            import numpy as np
            gx, gw = np.polynomial.legendre.leggauss(K)
            tot = 0.0; ymax = 0.0
            for x, wgt in zip(gx, gw):
                s_ = (x + 1)/2*ell; th_ = 2*math.atan(math.exp(s_ - ell/2))
                z = complex(cen + rad*math.cos(th_), rad*math.sin(th_)); zr = reduce(z); ymax = max(ymax, zr.imag)
                tot += wgt*ell/2*f_fast(zr)
            rows.append((w, tr, ell, tot/ell, ymax))
    import json, pathlib
    json.dump(rows, open(pathlib.Path(__file__).with_name(f"motion_defect_N{NMAX}.json"), "w"), indent=0)
    rows.sort(key=lambda r: r[3])
    print(f"{len(rows)} primitive threads to length {NMAX}; <f> from {rows[0][3]:.3e} ({rows[0][0]}, y_max {rows[0][4]:.2f}) to {rows[-1][3]:.3e} ({rows[-1][0]})")
    for r in rows[:6] + rows[-4:]: print(f"  {r[0]:>14s} tr {r[1]:6d} l {r[2]:7.3f} <f> {r[3]:.4e} y_max {r[4]:.2f}")
    import statistics
    print("median <f>:", statistics.median(r[3] for r in rows))
