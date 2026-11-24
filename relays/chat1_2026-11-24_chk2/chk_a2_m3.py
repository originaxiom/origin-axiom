#!/usr/bin/env python3
"""CHK-2b: a test of agy-002's two-sector trade-off M3 (A2-P879-INTERIOR). Data-free.

    python3 -I -u chk_a2_m3.py

The statement tested, as agy-002's producer v3 checks it (run_G3_M3, F_three_regime_mp, S_req_mp):
  one Higgs h in C^3; H_d = h . sigma and H_u = conj(h) . sigma; channels M_u, M_d in C^{2x2};
  Y_f[a, b] = Tr(sigma_a H_f sigma_b M_f) / 2; rho_f = m_2 / m_3 of Y_f; rho = max(rho_u, rho_d);
  t = r / (1 + sqrt(1 - r^2)), r = |h . h| / |h|^2; s_L = |r_u ^ r_d| for the top right singular vectors of M_u, M_d;
  a = |V_33| = |<u_3^u | u_3^d>| for the top left singular vectors of Y_u, Y_d.
  Claim: rho >= F(t; s_L, a), with S = sin(max(0, arccos((1 + s_L)/(3 - s_L)) - arccos a) / 2) and
  F = S^2 / (2 (1 + 2 S)) for t <= S / (2 (1 + S)); S t / (1 + 2 t) for t <= S; t^2 / (1 + 2 t) otherwise.

This code is this seat's own (numpy), sharing nothing with agy-002's but the statement. Its sampling differs from
agy-002's: general complex channels (not fixed singular values 1 and kappa), six modes, and an adversarial search that
minimises rho - F from random starts.

Expectations, written before the run:
  M3-a  No violation (rho < F - 1e-9) in 240 000 random trials.                               80 %
  M3-b  No violation found by the adversarial search (400 starts).                             70 %
  M3-c  The least margin rho - F found is below 1e-2 (the bound is close to sharp somewhere).   60 %
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(20261125)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def Ymat(H, M):
    return np.array([[0.5 * np.trace(SIG[a] @ H @ SIG[b] @ M) for b in range(3)] for a in range(3)])


def Ffloor(t, sL, a):
    th0 = np.arccos(np.clip((1 + sL) / (3 - sL), -1, 1))
    gap = th0 - np.arccos(np.clip(a, -1, 1))
    S = np.sin(gap / 2) if gap > 0 else 0.0
    t1 = S / (2 * (1 + S)) if S > 0 else 0.0
    if t <= t1:
        return S * S / (2 * (1 + 2 * S))
    if t <= S:
        return S * t / (1 + 2 * t)
    return t * t / (1 + 2 * t)


def evaluate(h, Mu, Md):
    Hd = sum(h[k] * SIG[k] for k in range(3))
    Hu = sum(np.conj(h[k]) * SIG[k] for k in range(3))
    Uu, su, _ = np.linalg.svd(Ymat(Hu, Mu))
    Ud, sd, _ = np.linalg.svd(Ymat(Hd, Md))
    rho = max(su[1] / su[0], sd[1] / sd[0])
    a = abs(np.vdot(Uu[:, 0], Ud[:, 0]))
    r = abs(h @ h) / np.vdot(h, h).real
    t = r / (1 + np.sqrt(max(0.0, 1 - r * r)))
    _, _, Vhu = np.linalg.svd(Mu)
    _, _, Vhd = np.linalg.svd(Md)
    ru, rd = Vhu[0].conj(), Vhd[0].conj()
    sL = abs(ru[0] * rd[1] - ru[1] * rd[0])
    return rho, Ffloor(t, sL, a), t, sL, a


def cgauss(*shape):
    return rng.normal(size=shape) + 1j * rng.normal(size=shape)


def sample(mode):
    h = cgauss(3)
    Mu, Md = cgauss(2, 2), cgauss(2, 2)
    if mode == 1:      # nearly null Higgs (t near 0)
        e1 = rng.normal(size=3); e1 /= np.linalg.norm(e1)
        e2 = rng.normal(size=3); e2 -= e2 @ e1 * e1; e2 /= np.linalg.norm(e2)
        h = e1 + 1j * e2 + 10 ** rng.uniform(-6, -1) * cgauss(3)
    elif mode == 2:    # nearly real Higgs (t near 1)
        h = rng.normal(size=3) + 1j * 10 ** rng.uniform(-6, -1) * rng.normal(size=3)
    elif mode == 3:    # nearly rank-one channels
        for M in (Mu, Md):
            u, s, vh = np.linalg.svd(M)
            M[:] = u @ np.diag([1.0, 10 ** rng.uniform(-6, -1)]) @ vh
    elif mode == 4:    # equal top right vectors (s_L = 0) and small kappa
        u, _, vh = np.linalg.svd(Mu)
        Mu = u @ np.diag([1.0, rng.uniform(0, 0.3)]) @ vh
        u2, _, _ = np.linalg.svd(Md)
        Md = u2 @ np.diag([1.0, rng.uniform(0, 0.3)]) @ vh
    elif mode == 5:    # orthogonal top right vectors (s_L = 1)
        u, _, vh = np.linalg.svd(Mu)
        Mu = u @ np.diag([1.0, rng.uniform(0, 0.3)]) @ vh
        u2, _, _ = np.linalg.svd(Md)
        Md = u2 @ np.diag([1.0, rng.uniform(0, 0.3)]) @ vh[::-1]
    return h, Mu, Md


N = 240000
viol, worst, worst_rec = 0, np.inf, None
for n in range(N):
    h, Mu, Md = sample(n % 6)
    rho, F, t, sL, a = evaluate(h, Mu, Md)
    if rho < F - 1e-9:
        viol += 1
    if rho - F < worst:
        worst, worst_rec = rho - F, (t, sL, a, rho, F)
print("M3-a  random trials %d, violations %d, least margin %.3e at (t, s_L, a, rho, F) = %s"
      % (N, viol, worst, tuple(round(float(v), 6) for v in worst_rec)))


def unpack(p):
    h = p[0:3] + 1j * p[3:6]
    Mu = (p[6:10] + 1j * p[10:14]).reshape(2, 2)
    Md = (p[14:18] + 1j * p[18:22]).reshape(2, 2)
    return h, Mu, Md


def obj(p):
    h, Mu, Md = unpack(p)
    if np.linalg.norm(h) < 1e-8 or np.linalg.norm(Mu) < 1e-8 or np.linalg.norm(Md) < 1e-8:
        return 1.0
    rho, F, *_ = evaluate(h, Mu, Md)
    return rho - F


best, best_p, aviol = np.inf, None, 0
for s in range(400):
    p0 = rng.normal(size=22)
    res = minimize(obj, p0, method="Nelder-Mead", options={"maxiter": 6000, "xatol": 1e-10, "fatol": 1e-12})
    if res.fun < -1e-9:
        aviol += 1
    if res.fun < best:
        best, best_p = res.fun, res.x
rec = evaluate(*unpack(best_p))
print("M3-b  adversarial starts 400, starts ending in a violation %d, least margin %.3e at (rho, F, t, s_L, a) = %s"
      % (aviol, best, tuple(round(float(v), 6) for v in rec)))
print("M3-c  least margin overall %.3e" % min(worst, best))
print("done")
