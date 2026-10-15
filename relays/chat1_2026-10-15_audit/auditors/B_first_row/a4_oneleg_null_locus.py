#!/usr/bin/env python3
"""Audit B, part 4. chat1's read-out: 'both condensates on one leg, sym(Y(a) AB) ... rank 3. There is no massless neutrino,
so the hook does not survive that placement.' det(sym(Y(a) D)) is a homogeneous cubic in a, so it vanishes on a complex
surface of Higgs directions. On that surface the hook survives with a null vector that is neither R nor e_t.
Here: solve det = 0 for a_3 given random (a_1, a_2), and read the null vector's overlap with R and e_t, and its sigma."""
import math, numpy as np
rng = np.random.default_rng(31415)

def thetas(t, K=60):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    return np.sum(q((n + .5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
def R_of(t):
    th2, th3, th4 = thetas(t); return np.array([-th2 ** 2, -th4 ** 2, 1j * th3 ** 2]) / (np.pi * th2 * th3 * th4)
def Yc(a, R): return np.outer(a, R) + np.outer(R, a) - (a @ R) * np.eye(3)
def sig(w): return abs(w @ w) / np.vdot(w, w).real
def ov2(u, v): return abs(np.vdot(u, v)) ** 2 / (np.vdot(u, u).real * np.vdot(v, v).real)
p_nat = (1 - 0.3092) * (1 - 0.02248)

def M_of(a, R, D): M = Yc(a, R) @ D; return (M + M.T) / 2
rows = []
for t in (1j, 1.5j, 2j, complex(-.5, math.sqrt(3) / 2), .3 + 1.1j):
    R = R_of(t)
    for ti in range(3):
        r, s = [x for x in range(3) if x != ti]
        for _ in range(400):
            D = np.zeros((3, 3), complex); D[r, r] = complex(*rng.normal(size=2)); D[s, s] = complex(*rng.normal(size=2))
            a12 = rng.normal(size=2) + 1j * rng.normal(size=2)
            # det(M(a1, a2, x)) is a cubic in x: sample at 4 points and fit exactly
            xs = np.array([0, 1, -1, 2], complex)
            ds = [np.linalg.det(M_of(np.array([a12[0], a12[1], x]), R, D)) for x in xs]
            coef = np.polyfit(xs, ds, 3)
            for x in np.roots(coef):
                a = np.array([a12[0], a12[1], x]); M = M_of(a, R, D)
                W, sv, Vh = np.linalg.svd(M); o = np.argsort(sv)
                if sv[o[0]] / sv[o[2]] > 1e-9 or sv[o[1]] / sv[o[2]] < 1e-6: continue   # rank exactly 2
                u = Vh.conj().T[:, o[0]]
                rows.append((ov2(R, u), abs(u[ti]) ** 2, sig(u), sv[o[1]] / sv[o[2]]))
rows = np.array(rows)
print("solutions with rank exactly 2 (m1/m3 < 1e-9):", len(rows))
for k, name in enumerate(("|<R, nu1>|^2  (electron along R)", "|<e_t, nu1>|^2 (electron along e_t)")):
    x = rows[:, k]
    print("  %-38s min %.4f max %.4f; in (1/2, 1): %.3f; within 0.0085 of 0.6753: %.4f" % (name, x.min(), x.max(), np.mean((x > .5) & (x < 1 - 1e-6)), np.mean(abs(x - p_nat) < .0085)))
print("  sigma of the null vector: min %.3f median %.3f max %.3f (0 = isotropic, 1 = real)" % (rows[:, 2].min(), np.median(rows[:, 2]), rows[:, 2].max()))
print("  m2/m3 on the locus: min %.2e median %.3f" % (rows[:, 3].min(), np.median(rows[:, 3])))
