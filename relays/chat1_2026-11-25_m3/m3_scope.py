#!/usr/bin/env python3
"""CLAIM CARD script: agy-002's two-sector floor M3 (A2-P879-INTERIOR) holds under the one-doublet rule it states,
and fails when one Higgs is read alike in both sectors. Sealed and dependency-free: standard library and numpy only;
reads no file. Data-free.

    python3 -I m3_scope.py

The statement, as agy-002's producer v3 tests it (run_G3_M3, F_three_regime_mp, S_req_mp):
  Y_f[a, b] = Tr(sigma_a H_f sigma_b M_f) / 2 (B1736's coupling); rho = max over f of m_2/m_3 of Y_f;
  t = r / (1 + sqrt(1 - r^2)), r = |h . h| / |h|^2; s_L = |r_u ^ r_d| for the top right singular vectors of M_u, M_d;
  a = |V_33| = |<u_3^u | u_3^d>| for the top left singular vectors of Y_u, Y_d;
  F = S^2 / (2 (1 + 2 S)) for t <= S / (2 (1 + S)); S t / (1 + 2 t) for t <= S; t^2 / (1 + 2 t) otherwise, with
  S = sin(max(0, arccos((1 + s_L)/(3 - s_L)) - arccos a) / 2).
  Claim: rho >= F.
Two readings of the Higgs:
  (i)  H_u = conj(h) . sigma, H_d = h . sigma, as M3 states it (the one-doublet charge rule);
  (ii) H_u = H_d = h . sigma (one Higgs read alike in both sectors, the all-S world).
Sampling: general complex 2 x 2 channels and a complex Higgs, in six modes (generic; nearly null and nearly real
Higgs; nearly rank-one channels; equal and orthogonal top right vectors of the channels), seed 20261125.

Expectations (from this seat's runs of 2026-11-24, chk_a2_m3.py and chk_a2_m3_scope.py, which this script restates):
  (i)  no violation (rho < F - 1e-9) in 120 000 trials;
  (ii) violations in more than 10 of 120 000 trials.
"""
import numpy as np

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


def evaluate(h, Mu, Md, same):
    Hd = sum(h[k] * SIG[k] for k in range(3))
    Hu = Hd if same else sum(np.conj(h[k]) * SIG[k] for k in range(3))
    Uu, su, _ = np.linalg.svd(Ymat(Hu, Mu))
    Ud, sd, _ = np.linalg.svd(Ymat(Hd, Md))
    rho = max(su[1] / su[0], sd[1] / sd[0])
    a = abs(np.vdot(Uu[:, 0], Ud[:, 0]))
    r = abs(h @ h) / np.vdot(h, h).real
    t = r / (1 + np.sqrt(max(0.0, 1 - r * r)))
    _, _, Vhu = np.linalg.svd(Mu)
    _, _, Vhd = np.linalg.svd(Md)
    ru, rd = Vhu[0].conj(), Vhd[0].conj()
    return rho, Ffloor(t, abs(ru[0] * rd[1] - ru[1] * rd[0]), a), t, a


def cgauss(*shape):
    return rng.normal(size=shape) + 1j * rng.normal(size=shape)


def sample(mode):
    h = cgauss(3)
    Mu, Md = cgauss(2, 2), cgauss(2, 2)
    if mode == 1:
        e1 = rng.normal(size=3); e1 /= np.linalg.norm(e1)
        e2 = rng.normal(size=3); e2 -= e2 @ e1 * e1; e2 /= np.linalg.norm(e2)
        h = e1 + 1j * e2 + 10 ** rng.uniform(-6, -1) * cgauss(3)
    elif mode == 2:
        h = rng.normal(size=3) + 1j * 10 ** rng.uniform(-6, -1) * rng.normal(size=3)
    elif mode == 3:
        for M in (Mu, Md):
            u, s, vh = np.linalg.svd(M)
            M[:] = u @ np.diag([1.0, 10 ** rng.uniform(-6, -1)]) @ vh
    elif mode == 4:
        u, _, vh = np.linalg.svd(Mu)
        Mu = u @ np.diag([1.0, rng.uniform(0, 0.3)]) @ vh
        u2, _, _ = np.linalg.svd(Md)
        Md = u2 @ np.diag([1.0, rng.uniform(0, 0.3)]) @ vh
    elif mode == 5:
        u, _, vh = np.linalg.svd(Mu)
        Mu = u @ np.diag([1.0, rng.uniform(0, 0.3)]) @ vh
        u2, _, _ = np.linalg.svd(Md)
        Md = u2 @ np.diag([1.0, rng.uniform(0, 0.3)]) @ vh[::-1]
    return h, Mu, Md


N = 120000
res = {False: [0, np.inf, None], True: [0, np.inf, None]}
for n in range(N):
    h, Mu, Md = sample(n % 6)
    for same in (False, True):
        rho, F, t, a = evaluate(h, Mu, Md, same)
        R = res[same]
        if rho < F - 1e-9:
            R[0] += 1
        if rho - F < R[1]:
            R[1], R[2] = rho - F, (rho, F, t, a)
for same, name in ((False, "(i)  H_u = conj(h).sigma, as M3 states"), (True, "(ii) H_u = H_d = h.sigma")):
    v, m, rec = res[same]
    print("%s: trials %d, violations %d, least margin %.3e at (rho, F, t, |V33|) = %s"
          % (name, N, v, m, tuple(round(float(x), 6) for x in rec)))
print("(i) holds: %s; (ii) fails: %s" % (res[False][0] == 0, res[True][0] > 10))
