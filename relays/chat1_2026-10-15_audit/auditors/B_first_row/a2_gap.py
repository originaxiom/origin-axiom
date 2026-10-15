#!/usr/bin/env python3
"""Audit B, part 2: leading-order configurations ON THE RECORD that lie outside the first row's premises.
E1  puncture (R) for one sector, a half-period (B1651's tau-independent isotropic triplets) for the other
E2  two moduli (B1640: one tau cannot give TM1's residual pair): R(tau_e) against R(tau_nu)
E4  Reading B with both condensates on one leg (chat1's own read-out placement): the lightest neutrino against R and e_t
E6  TM1's actual line: the minimal electron turn is d(R, nu_TM1) - acos(sqrt(2/3)), not 9.7 deg except where the cap is reached
E7  W68 G2: R(omega) on l_omega = (-w, 1, w^2), an isotropic eigenline of the three-fold rotation M"""
import math, numpy as np
from scipy.optimize import brentq, minimize
rng = np.random.default_rng(4242)

def thetas(t, K=60):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    return np.sum(q((n + .5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
def R_of(t):
    th2, th3, th4 = thetas(t); return np.array([-th2 ** 2, -th4 ** 2, 1j * th3 ** 2]) / (np.pi * th2 * th3 * th4)
def ov2(u, v): return abs(np.vdot(u, v)) ** 2 / (np.vdot(u, u).real * np.vdot(v, v).real)
def sig(w): return abs(w @ w) / np.vdot(w, w).real
V4 = [np.diag(d).astype(complex) for d in ([1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1])]
HP = {"1/2": np.array([0, -1, 1j]), "tau/2": np.array([1j, 0, 1]), "(1+tau)/2": np.array([1j, -1, 0])}
p_nat = (1 - 0.3092) * (1 - 0.02248)

print("E1. puncture R against B1651's half-period triplets (squared overlaps = |U_e1|^2 if one sector couples at each)")
tU6 = complex(-0.478912465221202676701750533539, 0.903766110064352479191995826113)
for name, v in HP.items():
    vals = sorted(set(round(ov2(R_of(tU6), D @ v), 6) for D in V4))
    print("   at B1651's U6 tau (Im 0.904): 0 |", name, "->", vals, " sqrt ->", [round(math.sqrt(x), 4) for x in vals])
for y in (0.6, 0.8, 0.9, 1.0, 1.2, 1.5, 2.0, 3.0):
    print("   tau = %.1fi:" % y, {n: sorted(set(round(ov2(R_of(1j * y), D @ v), 4) for D in V4)) for n, v in HP.items()})
f = lambda y: ov2(R_of(1j * y), HP["1/2"]) - p_nat
ys = brentq(f, 0.5, 1.0)
th2, th3, th4 = thetas(1j * ys)
print("   |U_e1|^2 = %.4f (nature) at tau = %.6f i  (hand: ((1 + th4^2/th3^2)/2)^2 = %.6f)" % (p_nat, ys, ((1 + (th4 / th3) ** 2) / 2).real ** 2))
print("   the interval reached on the imaginary axis by the + sign: (1/4, 1); by the - sign: (0, 1/4)")

print("\nE2. two moduli: |<R(tau_e), R(tau_nu)>|^2 (both isotropic, so the cap gives no bound)")
pts = {"i": 1j, "omega": complex(-.5, math.sqrt(3) / 2), "(1+i)/2": .5 + .5j, "3/2+i*sqrt3/2": complex(1.5, math.sqrt(3) / 2),
       "2i": 2j, "1.5i": 1.5j, "4i": 4j}
names = list(pts)
for a in range(len(names)):
    print("   %-15s" % names[a], " ".join("%s=%.4f" % (names[b], ov2(R_of(pts[names[a]]), R_of(pts[names[b]]))) for b in range(a + 1, len(names))))
g = lambda y: ov2(R_of(1j), R_of(1j * y)) - p_nat
try:
    y2 = brentq(g, 1.0, 6.0); print("   R(i) vs R(iy) reaches %.4f at y = %.5f" % (p_nat, y2))
except ValueError as e:
    print("   R(i) vs R(iy): no crossing on [1, 6]", [round(ov2(R_of(1j), R_of(1j * y)), 4) for y in (1.5, 2, 3, 6)])

print("\nE4. Reading B, both condensates on one leg: M = sym(Y(a) A B); the lightest state against R and e_t")
def E(r, s): M = np.zeros((3, 3), complex); M[r, s] = 1; return M
def Yc(a, R): return np.outer(a, R) + np.outer(R, a) - (a @ R) * np.eye(3)
def rc(n): return rng.normal(size=n) + 1j * rng.normal(size=n)
def lightest(M):
    W, s, Vh = np.linalg.svd(M); o = np.argsort(s); return Vh.conj().T[:, o[0]], s[o]
stats = {"vs_R": [], "vs_et": [], "m1m3": []}
for t in (1j, 1.5j, 2j, .3 + 1.1j, complex(-.5, math.sqrt(3) / 2)):
    R = R_of(t)
    for ti in range(3):
        r, s = [x for x in range(3) if x != ti]
        for _ in range(3000):
            A = rc(1)[0] * E(r, s) + rc(1)[0] * E(s, r); B = rc(1)[0] * E(r, s) + rc(1)[0] * E(s, r)
            M = Yc(rc(3), R) @ A @ B; M = (M + M.T) / 2
            v, sv = lightest(M)
            stats["vs_R"].append(ov2(R, v)); stats["vs_et"].append(abs(v[ti]) ** 2); stats["m1m3"].append(sv[0] / sv[2])
for k in ("vs_R", "vs_et"):
    x = np.array(stats[k]); print("   %-6s: min %.4f max %.4f; fraction in (1/2, 1): %.3f; fraction within 0.0085 of 0.6753: %.4f"
                                    % (k, x.min(), x.max(), np.mean((x > .5) & (x < 1 - 1e-6)), np.mean(abs(x - p_nat) < 0.0085)))
x = np.array(stats["m1m3"]); print("   m1/m3 over the draws: min %.2e median %.3f max %.3f (rank 3, as chat1 read out)" % (x.min(), np.median(x), x.max()))

print("\nE6. TM1's actual line: minimal electron turn for P10's 2/3 = d(Rhat, nu_TM1) - acos(sqrt(2/3))")
dTM1 = math.degrees(math.acos(math.sqrt(2 / 3)))
for name, o in (("y=0.6 (W49)", 0.2704059716567261), ("tau=i (W49)", 0.375), ("2i (W49)", 0.49264068711928527),
                ("omega, 1/6 classes", 1 / 6), ("omega, 1/2 classes", 0.5), ("1.5i, 24-frame max", 0.4665264681835642),
                ("1.5i, 24-frame min", 0.07973073534142427)):
    d = math.degrees(math.acos(math.sqrt(o))); print("   %-20s overlap %.4f -> d = %.2f deg, min turn %.2f deg" % (name, o, d, d - dTM1))

print("\nE7. W68 G2 by own thetas: R(omega) against l_omega = (-w, 1, w^2), w = exp(2 pi i/3)")
w = np.exp(2j * np.pi / 3); lw = np.array([-w, 1, w ** 2]); lw2 = np.array([-w ** 2, 1, w])
Rw = R_of(complex(-.5, math.sqrt(3) / 2))
print("   |<R(omega), l_omega>|^2 = %.15f ; against l_omega^2: %.3e ; against the axis (1,-1,-1): %.3e ; sigma(l_omega) = %.1e"
      % (ov2(Rw, lw), ov2(Rw, lw2), ov2(Rw, np.array([1, -1, -1])), sig(lw)))
M3 = np.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]], float)   # e_i -> -e_j, e_j -> e_k, e_k -> -e_i (columns are images)
print("   M3 R(omega) = lambda R(omega)?  residual %.2e, lambda = %s" % (np.linalg.norm(M3 @ Rw - (np.vdot(Rw, M3 @ Rw) / np.vdot(Rw, Rw)) * Rw) / np.linalg.norm(Rw), np.round(np.vdot(Rw, M3 @ Rw) / np.vdot(Rw, Rw), 6)))
