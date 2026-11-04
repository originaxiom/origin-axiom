"""S304 checks for Theorems 77, 81 (the e^-2L term), 82 and 83 (value-free; main's code + first principles; no lane code run).
  D1  the flat-disc cut's O(eps^2) coefficient on main's cA: int_{P minus D_eps} |K_s|^2 - (2 pi log 1/eps + c_s) = -pi eps^2 |a0_s|^2 + O(eps^4)
      (main's cA adds pi eps^2 |a0|^2 back, so cA(eps) - cA(1e-5) must be O(eps^4)); Theorem 81 uses pi |wp(v)| e^{-2L} instead.
  D2  Theorem 82: F(u,v) F(u,-v) = wp(u) - wp(v) (Kronecker); the finite-disc integral I_eps = I_PV + pi eps^2 wp(v) (exact, eps < 1/2);
      S-covariance of I_eps when the cut radius transforms with the coordinate (eps -> eps/|tau|), and its failure with a fixed number.
  D3  Theorem 83 / P-670: mp.jtheta(2, 0, e^{i pi tau}) / (2 sum e^{i pi tau (n+1/2)^2}) against (-i)^floor((Re tau + 1)/2).
  D4  Theorem 77: the lane's abstract encoding of the spinor group, (u,v) in Z8 x Z4, (u1,v1)(u2,v2) = (u1+u2, (-1)^u2 v1 + v2);
      quotient by the lane's kernel <(2,0)> = <a^2> vs by <(2,2)> = <a^2 d^-2> (main's c4: the lift of -I10 is x_i^2 x_k^-2).
  D5  Theorem 83's Bernoulli sums (exact rationals) and the c29b large-y slope 2 pi N_gen |sum| against main's c29b table.
    OPENBLAS_NUM_THREADS=1 nice -n 10 python3 -B p3_misc.py"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(v, "1")
import sys, io, math, contextlib, pathlib, itertools
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification"))
_argv = sys.argv; sys.argv = ["x"]
with contextlib.redirect_stdout(io.StringIO()):
    import b1656_funcs as B
sys.argv = _argv

# ---------------- D1
print("D1  the flat disc's O(eps^2) term (main's cA, which adds +pi eps^2 |a0|^2 back):")
for t, (a, b), (lf, rf) in ((complex(0.31, 2.05), (1 / 7, 3 / 7), ("Q", "d")), (complex(0.13, 1.30), (5 / 12, 1 / 4), ("Q", "u"))):
    w = a * t + b; x, y = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, y, t)
    c0 = B.cA(x, y, t, R, eps=1e-5); A0 = B.a0_of(x, y, t, R)
    for e in (0.05, 0.1, 0.2):
        ce = B.cA(x, y, t, R, eps=e)
        r = max(abs(ce[s] - c0[s]) for s in B.UNITS if c0[s] is not None)
        a0m = max(abs(A0[s]) ** 2 for s in B.UNITS if A0[s] is not None)
        print("    tau=%s eps=%.2f: max_s |cA(eps) - cA(1e-5)| = %.2e (O(eps^4) residue) ; pi eps^2 max|a0|^2 = %.2e (the term it carries)"
              % (t, e, r, math.pi * e * e * a0m))

# ---------------- D2
mp.mp.dps = 30
def th1(z, tau): return mp.jtheta(1, mp.pi * z, mp.exp(1j * mp.pi * tau))
def th1d(z, tau, k): return mp.pi ** k * mp.jtheta(1, mp.pi * z, mp.exp(1j * mp.pi * tau), derivative=k)
def G2(tau): return -th1d(0, tau, 3) / (3 * th1d(0, tau, 1))
def wp(z, tau):
    t0, t1, t2 = th1(z, tau), th1d(z, tau, 1), th1d(z, tau, 2)
    return -(t2 / t0 - (t1 / t0) ** 2) - G2(tau)
def F(u, v, tau): return th1d(0, tau, 1) * th1(u + v, tau) / (th1(u, tau) * th1(v, tau))
tau = mp.mpc("0.21", "1.37"); v = mp.mpc("0.3", "0") - mp.mpf(1) / 5 * tau
err_kron = max(abs(F(u, v, tau) * F(u, -v, tau) - (wp(u, tau) - wp(v, tau))) for u in (mp.mpc("0.11", "0.07"), mp.mpc("-0.2", "0.15"), mp.mpc("0.05", "-0.31")))
# Weierstrass check of wp: Laurent 1/u^2 + O(u^2) and wp' ^2 = 4 wp^3 - g2 wp - g3 at a point (consistency of the evaluator)
u0 = mp.mpc("0.013", "0.007"); lau = abs(wp(u0, tau) - 1 / u0 ** 2)
print("\nD2  Kronecker product F(u,v)F(u,-v) = wp(u) - wp(v): max dev %.1e ; wp(u) - 1/u^2 at |u| = 0.015: %.1e (O(u^2))" % (err_kron, lau))
def I_pv(v, tau): y = mp.im(tau); return -y * (wp(v, tau) + G2(tau) - mp.pi / y)
def I_eps(v, tau, eps): return I_pv(v, tau) + mp.pi * eps ** 2 * wp(v, tau)
# direct numerical check of I_eps on a moderate disc (eps = 0.2), integrating wp(u) - wp(v) over the Dirichlet-like parallelogram minus the disc
def direct(v, tau, eps, n=48):
    xs, ws = np.polynomial.legendre.leggauss(n)
    tot = mp.mpf(0)
    # polar around 0 over the parallelogram P = {s + t tau, |s|,|t| <= 1/2}: integrate in (theta, r) from eps to the boundary
    tc = complex(tau)
    verts = [0.5 + 0.5 * tc, -0.5 + 0.5 * tc, -0.5 - 0.5 * tc, 0.5 - 0.5 * tc]
    angs = sorted(float(np.mod(np.angle(z), 2 * np.pi)) for z in verts); angs = angs + [angs[0] + 2 * np.pi]
    wv = complex(wp(v, tau))
    def rmax(th):
        d = np.exp(1j * th); y1 = d.imag / tc.imag; x1 = d.real - y1 * tc.real; return 0.5 / max(abs(x1), abs(y1))
    for a, b in zip(angs[:-1], angs[1:]):
        for xi, wi in zip(xs, ws):
            th = 0.5 * (b - a) * xi + 0.5 * (b + a); wt = 0.5 * (b - a) * wi
            hi = math.log(rmax(th)); lo = math.log(eps)
            for xj, wj in zip(xs, ws):
                sg = 0.5 * (hi - lo) * xj + 0.5 * (hi + lo); rr = math.exp(sg)
                z = rr * np.exp(1j * th)
                tot += wt * 0.5 * (hi - lo) * wj * (complex(wp(mp.mpc(z.real, z.imag), tau)) - wv) * rr * rr
    return tot
mp.mp.dps = 20
d_direct = direct(v, tau, 0.2, n=32)
print("    I_eps by direct quadrature (eps = 0.2) vs I_PV + pi eps^2 wp(v): |diff| = %.1e" % abs(d_direct - I_eps(v, tau, mp.mpf("0.2"))))
mp.mp.dps = 30
tS = -1 / tau; vS = v / tau; ph = (tau / abs(tau)) ** 2
print("    S-covariance, I(v/tau, -1/tau) vs (tau/|tau|)^2 I(v, tau):")
print("      PV (eps -> 0):                         %.1e" % abs(I_pv(vS, tS) - ph * I_pv(v, tau)))
for e in (mp.mpf("0.05"), mp.mpf("0.2")):
    print("      finite disc, radius transformed eps/|tau|: %.1e ; same number eps in both frames: %.1e   (eps = %s)"
          % (abs(I_eps(vS, tS, e / abs(tau)) - ph * I_eps(v, tau, e)), abs(I_eps(vS, tS, e) - ph * I_eps(v, tau, e)), e))
cconst = mp.mpf("2.0")
print("      a fixed constant added in both frames (the lane's construction): %.1e" % abs((I_pv(vS, tS) + cconst) - ph * (I_pv(v, tau) + cconst)))

# ---------------- D3
print("\nD3  mp.jtheta(2, 0, e^{i pi tau}) / series, against (-i)^floor((Re tau + 1)/2), Im tau = 0.9:")
mp.mp.dps = 30
worst = 0.0
for re in (-3.3, -2.5, -1.5, -1.0, -0.999, -0.7, 0.0, 0.5, 0.999, 1.0, 1.001, 1.3, 2.5, 2.999, 3.0, 3.4, 5.2):
    t = mp.mpc(re, 0.9)
    ser = 2 * mp.nsum(lambda n: mp.exp(1j * mp.pi * t * (n + mp.mpf(1) / 2) ** 2), [0, mp.inf])
    lib = mp.jtheta(2, 0, mp.exp(1j * mp.pi * t))
    k = math.floor((re + 1) / 2); pred = mp.mpc(0, -1) ** k
    dv = abs(lib / ser - pred); worst = max(worst, float(dv)) if abs(abs(re) - 1) > 1e-9 and abs(re - 3) > 1e-9 else worst
    print("    Re tau = %+6.3f: ratio = %s ; predicted (-i)^%d ; |dev| = %.1e" % (re, mp.nstr(lib / ser, 6), k, float(dv)))
print("    max dev off the cut lines Re tau = +-1, 3: %.1e" % worst)

# ---------------- D4
def mul(g, h, U=8, V=4): return ((g[0] + h[0]) % U, (g[1] * (1 if h[0] % 2 == 0 else -1) + h[1]) % V)
G = [(u, v) for u in range(8) for v in range(4)]
def gorder(g, m):
    c, n = g, 1
    while c != (0, 0): c = m(c, g); n += 1
    return n
center = [g for g in G if all(mul(g, h) == mul(h, g) for h in G)]
print("\nD4  the lane's abstract spinor group: |G| = %d, orders %s, |Z| = %d" % (len(G), dict(Counter(gorder(g, mul) for g in G)), len(center)))
def quotient(kgen):
    K = {(0, 0)}; c = kgen
    while c != (0, 0): K.add(c); c = mul(c, kgen)
    assert all(mul(k, g) == mul(g, k) for k in K for g in G)
    cos = {}
    for g in G:
        key = min(mul(g, k) for k in K); cos[g] = key
    reps = sorted(set(cos.values()))
    def qm(a, b): return cos[mul(a, b)]
    ords = Counter()
    for r in reps:
        c, n = r, 1
        while cos[c] != cos[(0, 0)]: c = qm(c, r); n += 1
        ords[n] += 1
    return len(K), len(reps), dict(ords)
for name, kg in (("<(2,0)> = <a^2> (the lane's C_hat)", (2, 0)), ("<(2,2)> = <a^2 d^-2> (main's c4 lift of -I10)", (2, 2))):
    k, n, o = quotient(kg)
    typ = "Q8" if o.get(2, 0) == 1 and o.get(4, 0) == 6 else "D4" if o.get(2, 0) == 5 else "other"
    print("    G / %s: |K| = %d, quotient order %d, element orders %s -> %s" % (name, k, n, o, typ))

# ---------------- D5
def B2(x): return x * x - x + Fr(1, 6)
def dist(x): r = x % 1; return min(r, 1 - r)
reps = [("Q", 6, 1), ("u^c", 3, -4), ("d^c", 3, 2), ("L", 2, -3), ("e^c", 1, 6)]
for al in (Fr(2, 5), Fr(1, 5)):
    s = sum(m * B2(dist(q * al)) for _, m, q in reps)
    print("\nD5  sum_f mult_f B2(||q_f alpha||) at alpha = %s: %s ; 2 pi * 3 * |sum| = %.4f" % (al, s, 2 * math.pi * 3 * abs(float(s))), end="")
print("\n    main's c29b at Im tau = 12: lane's sign +12.65, fermion-loop sign -13.74 -> half-difference %.3f, half-sum %.3f (a 1/y^3 flux term)"
      % ((12.65 + 13.74) / 2, (12.65 - 13.74) / 2))
