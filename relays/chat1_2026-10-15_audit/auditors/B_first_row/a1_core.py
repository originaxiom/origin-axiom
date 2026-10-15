#!/usr/bin/env python3
"""Audit B, part 1: independent re-derivation of the first-row folder's core mathematics.
Own theta series (no repo code). Checks: R isotropic; the bound (random, adversarial, sharp); the cap;
F5's kernel identity (closed form with the s0 cross term); F6 (Reading B); the data line."""
import math, numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(777)

def thetas(t, K=60):
    n = np.arange(-K, K + 1)
    q = lambda x: np.exp(1j * np.pi * t * x)
    th2 = np.sum(q((n + 0.5) ** 2)); th3 = np.sum(q(n * n)); th4 = np.sum((-1.0) ** n * q(n * n))
    return th2, th3, th4

def R_of(t):
    th2, th3, th4 = thetas(t)
    return np.array([-th2 ** 2, -th4 ** 2, 1j * th3 ** 2]) / (np.pi * th2 * th3 * th4)

def sig(w): w = np.asarray(w, complex); return abs(w @ w) / np.vdot(w, w).real
def ov2(u, v): return abs(np.vdot(u, v)) ** 2 / (np.vdot(u, u).real * np.vdot(v, v).real)
def bound(su, sv): return 0.5 * (1 + su * sv + math.sqrt(max(0, 1 - su * su) * max(0, 1 - sv * sv)))

taus = [1j, 1.5j, 2j, 4j, complex(-.5, math.sqrt(3) / 2), .3 + 1.1j, -.2 + .9j, .45 + 2.5j, .5 + .5j, 1.5 + math.sqrt(3) / 2 * 1j]
print("1. R isotropy |R.R|/|R|^2 max over 10 tau:", max(sig(R_of(t)) for t in taus))

# 2. the bound: random families incl. C^5, adversarial with a different optimiser (BFGS on angles), sharpness
worst = -1
for n in (2, 3, 5):
    for _ in range(40000):
        u = rng.normal(size=n) + 1j * rng.normal(size=n)
        v = rng.normal(size=n) * rng.uniform(0, 1) + 1j * rng.normal(size=n) * rng.uniform(0, 1) ** 3
        worst = max(worst, ov2(u, v) - bound(sig(u), sig(v)))
print("2a. random max excess (C^2, C^3, C^5):", worst)
def neg(p):
    u = p[:3] + 1j * p[3:6]; v = p[6:9] + 1j * p[9:12]
    return -(ov2(u, v) - bound(sig(u), sig(v)))
adv = max(-minimize(neg, rng.normal(size=12), method="BFGS").fun for _ in range(150))
print("2b. adversarial (BFGS, 150 starts) max excess:", adv)
# sharpness on a grid and the isotropic-vs-real cap
gap = 0
for su in np.linspace(0, 1, 11):
    for sv in np.linspace(0, 1, 11):
        au, av = .5 * math.acos(su), .5 * math.acos(sv)
        x, y = np.eye(3)[0], np.eye(3)[1]
        u = math.cos(au) * x + 1j * math.sin(au) * y; v = math.cos(av) * x + 1j * math.sin(av) * y
        gap = max(gap, abs(ov2(u, v) - bound(sig(u), sig(v))))
print("2c. sharp family max |ratio - bound| on 11x11 grid:", gap)
# the cap: max over real unit v of |<Rhat, v>|^2 = top eigenvalue of Re(Rhat Rhat^dag)
print("2d. cap per tau (should be 1/2):", [round(float(np.linalg.eigvalsh(np.real(np.outer(r := R_of(t) / np.linalg.norm(R_of(t)), r.conj()))).max()), 15) for t in taus])

# 3. F5: closed form with the s0 cross term (B1649's Y_closed); every operator built on it kills R on both sides
def Y_closed(s, R):
    a = np.array(s[1:]); Y = np.outer(a, R) + np.outer(R, a) - (a @ R) * np.eye(3)
    X = np.array([[0, -R[2], R[1]], [R[2], 0, -R[0]], [-R[1], R[0], 0]])
    return Y + s[0] * X
def rc(n): return rng.normal(size=n) + 1j * rng.normal(size=n)
def takagi_null(M):   # right singular vector of the smallest singular value
    W, s, Vh = np.linalg.svd(M); return Vh.conj().T[:, np.argmin(s)], np.sort(s)
w5 = 0; w5mix = 1
for t in taus:
    R = R_of(t); Rh = R / np.linalg.norm(R)
    for _ in range(20):
        Ye = Y_closed(rc(4), R); YD = Y_closed(rc(4), R)
        MR = rc(9).reshape(3, 3); MR = MR + MR.T
        ops = [Y_closed([0] + list(rc(3)), R), -YD.T @ np.linalg.inv(MR) @ YD,
               Y_closed([0] + list(rc(3)), R) - YD.T @ np.linalg.inv(MR) @ YD,
               Y_closed(rc(4), R) @ rc(9).reshape(3, 3) @ Y_closed(rc(4), R).T]
        ve, _ = takagi_null(Ye)
        for M in ops:
            M = (M + M.T) / 2; vn, s = takagi_null(M)
            w5 = max(w5, abs(1 - abs(np.vdot(ve, vn))))
            # the mixed convention: electron's left singular vector (Rbar) against the neutrino's right one (R)
            W, se, Vh = np.linalg.svd(Ye); ue = W[:, np.argmin(se)]
            w5mix = min(w5mix, 1 - abs(np.vdot(ue, vn)))
print("3. F5 max |1-|U_e1|| (consistent convention):", w5, "; mixed convention gives |U_e1| <=", 1 - w5mix)

# 4. F6 Reading B, one condensate per leg: null line e_t; |U_e1|^2 = |R_t|^2/|R|^2 <= 1/2; on tau = iy, t = k gives 1/2
def E(r, s): M = np.zeros((3, 3), complex); M[r, s] = 1; return M
mx = 0; dev = 0
for t in taus:
    R = R_of(t)
    for ti in range(3):
        r, s = [x for x in range(3) if x != ti]
        for _ in range(10):
            A = rc(1)[0] * E(r, s) + rc(1)[0] * E(s, r); B = rc(1)[0] * E(r, s) + rc(1)[0] * E(s, r)
            Y = Y_closed([0] + list(rc(3)), R); M = A.T @ Y @ B; M = (M + M.T) / 2
            vn, s_ = takagi_null(M); dev = max(dev, 1 - abs(vn[ti]))
            mx = max(mx, ov2(R, vn))
print("4. F6 null line = e_t to", dev, "; max |U_e1|^2 =", mx)
print("   t=k on iy: ", [round(ov2(R_of(1j * y), np.eye(3)[2]), 15) for y in (0.5, 1, 2, 5)])

# 5. the data line
p = (1 - 0.3092) * (1 - 0.02248); dp = 0.0087 * (1 - 0.02248)
print("5. p = %.5f +- %.5f; (p-1/2)/dp = %.2f; (1-p)/dp = %.2f" % (p, dp, (p - .5) / dp, (1 - p) / dp))
print("   sigma_nu max = %.4f; min electron turn (real nu1) = %.3f deg; FS distance acos(sqrt p) = %.3f deg"
      % (2 * math.sqrt(p * (1 - p)), 45 - math.degrees(.5 * math.acos(2 * p - 1)), math.degrees(math.acos(math.sqrt(p)))))
print("   TM1 2/3: min turn %.3f deg; GST sqrt(me/mmu) = %.2f deg" % (45 - math.degrees(.5 * math.acos(1 / 3)), math.degrees(math.asin(math.sqrt(0.51099895 / 105.6583755)))))
# sensitivity: any sin^2 theta12 in a generous window keeps p in the gap
for s12 in (0.27, 0.29, 0.307, 0.3092, 0.32, 0.35):
    print("   sin^2 th12 = %.4f -> |U_e1|^2 = %.4f" % (s12, (1 - s12) * (1 - 0.02248)))
