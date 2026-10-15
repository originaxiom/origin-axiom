#!/usr/bin/env python3
"""Audit B, part 5: the one-leg placement with the SAME condensate twice (A = B, as for (LH)(LH) with one Higgs):
A^2 = alpha*beta*(E_rr + E_ss), so M = sym(Y(a) P), P = 1 - e_t e_t^T. Only a (and tau, t) are free.
(i) random a: the lightest state against R and e_t; (ii) a fit of (|U_e1|^2, |U_e3|^2, dm21/dm31);
(iii) the m1 = 0 locus (det = 0, a cubic in a)."""
import math, numpy as np
from scipy.optimize import least_squares
rng = np.random.default_rng(2718)
def thetas(t, K=60):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    return np.sum(q((n + .5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
def R_of(t):
    th2, th3, th4 = thetas(t); return np.array([-th2 ** 2, -th4 ** 2, 1j * th3 ** 2]) / (np.pi * th2 * th3 * th4)
def Yc(a, R): return np.outer(a, R) + np.outer(R, a) - (a @ R) * np.eye(3)
def ov2(u, v): return abs(np.vdot(u, v)) ** 2 / (np.vdot(u, u).real * np.vdot(v, v).real)
def svd_sorted(M):
    W, s, Vh = np.linalg.svd(M); o = np.argsort(s); return Vh.conj().T[:, o], s[o]
p_nat = (1 - 0.3092) * (1 - 0.02248); r_nat = 7.49e-5 / 2.513e-3
def M_of(a, R, ti):
    P = np.eye(3, dtype=complex); P[ti, ti] = 0; M = Yc(a, R) @ P; return (M + M.T) / 2
taus = {"i": 1j, "1.5i": 1.5j, "2i": 2j, "omega": complex(-.5, math.sqrt(3) / 2), "0.3+1.1i": .3 + 1.1j}
vsR, vsT = [], []
for t in taus.values():
    R = R_of(t)
    for ti in range(3):
        for _ in range(3000):
            V, m = svd_sorted(M_of(rng.normal(size=3) + 1j * rng.normal(size=3), R, ti))
            vsR.append(ov2(R, V[:, 0])); vsT.append(abs(V[ti, 0]) ** 2)
for name, x in (("vs R", np.array(vsR)), ("vs e_t", np.array(vsT))):
    print("(i)  %-7s min %.4f max %.4f; in (1/2,1): %.3f; within 0.0085 of 0.6753: %.4f" % (name, x.min(), x.max(), np.mean((x > .5) & (x < 1 - 1e-6)), np.mean(abs(x - p_nat) < .0085)))
for electron in ("R", "e_t"):
    for tn, t in taus.items():
        R = R_of(t); best = None
        for ti in range(3):
            e = R / np.linalg.norm(R) if electron == "R" else np.eye(3)[ti].astype(complex)
            def res(p):
                V, m = svd_sorted(M_of(p[:3] + 1j * p[3:], R, ti)); row = np.abs(e.conj() @ V) ** 2
                return [row[0] - p_nat, row[2] - 0.02248, ((m[1] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[0] ** 2) - r_nat) / .1]
            for _ in range(30):
                s = least_squares(res, rng.normal(size=6), xtol=1e-15, ftol=1e-15, gtol=1e-15)
                if best is None or s.cost < best[0]:
                    V, m = svd_sorted(M_of(s.x[:3] + 1j * s.x[3:], R, ti)); best = (s.cost, ti, np.abs(e.conj() @ V) ** 2, m / m[2])
        print("(ii) electron %-3s tau=%-8s cost %.1e t=%d row (%.4f, %.4f, %.4f) m1:m2:m3 = %.4f : %.4f : 1" % (electron, tn, best[0], best[1], *best[2], *best[3][:2]))
rows = []
for t in taus.values():
    R = R_of(t)
    for ti in range(3):
        for _ in range(300):
            a12 = rng.normal(size=2) + 1j * rng.normal(size=2); xs = np.array([0, 1, -1, 2], complex)
            coef = np.polyfit(xs, [np.linalg.det(M_of(np.array([a12[0], a12[1], x]), R, ti)) for x in xs], 3)
            for x in np.roots(coef):
                V, m = svd_sorted(M_of(np.array([a12[0], a12[1], x]), R, ti))
                if m[0] / m[2] < 1e-9 and m[1] / m[2] > 1e-6: rows.append((ov2(R, V[:, 0]), abs(V[ti, 0]) ** 2))
rows = np.array(rows)
print("(iii) m1 = 0 locus: %d solutions; |U_e1|^2 vs R in [%.3f, %.3f], fraction in gap %.3f; vs e_t in [%.3f, %.3f], in gap %.3f"
      % (len(rows), rows[:, 0].min(), rows[:, 0].max(), np.mean((rows[:, 0] > .5) & (rows[:, 0] < 1 - 1e-6)), rows[:, 1].min(), rows[:, 1].max(), np.mean((rows[:, 1] > .5) & (rows[:, 1] < 1 - 1e-6))))
