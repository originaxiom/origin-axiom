#!/usr/bin/env python3
"""SM SEARCH (a module; data enter only through the targets passed in).  The search over Higgs directions for the
Standard Model's one-Higgs reading (up sees conj h, down and leptons see h; c = 3 on the leptons), on stored channel
weights with B1736's closed form; the objective is B1720 compare.py's chi2_nine (sigma^2 = the pinned relative error^2 +
0.10^2 on the natural logs of the six ratios and |V_us|, |V_cb|, |V_ub|), as in inverse_higgs.py.

Directions: the null conic's tube coordinates h = h0(t) + s conj h0(t), h0(t) = (2t, 1 - t^2, i(1 + t^2)) unit, which
satisfy |h.h| = 2|s| / (1 + |s|^2) for unit h (|s| = 1 is the real locus; |s| <= 1 covers CP^2): t on a 400-point
Fibonacci lattice of the Riemann sphere, |s| = 10^(-4 + k/4) (k = 0..16), arg s in 16 steps (108 800 directions), plus
4 000 random directions (seed 2610).  Then least squares (scipy trf, at most 400 evaluations, Jacobian by forward
differences evaluated as one batch) from the best eight grid directions that are pairwise more than 0.05 rad apart
(Fubini-Study) and from given extra starts (the record's directions, each as stored and conjugated)."""
import math
import numpy as np
from scipy.optimize import least_squares

F1 = np.array([0, 1, -1j]) / math.sqrt(2); F2 = np.array([1, 0, 0], dtype=complex); F3 = np.array([0, 1, 1j]) / math.sqrt(2)
LC = math.log(3.0)


def Ybatch(u4, H):
    w, u = u4[0], u4[1:]
    uh = H @ u
    Y = u[None, :, None] * H[:, None, :] + H[:, :, None] * u[None, None, :] - uh[:, None, None] * np.eye(3)[None]
    cr = np.zeros((len(H), 3, 3), dtype=complex)
    cr[:, 0, 1], cr[:, 0, 2], cr[:, 1, 2] = -H[:, 2], H[:, 1], -H[:, 0]
    cr[:, 1, 0], cr[:, 2, 0], cr[:, 2, 1] = H[:, 2], -H[:, 1], H[:, 0]
    return Y + w * cr


def nine_batch(Uh, H, T, SIG):
    """Uh: (3 sectors, 4) weights at one row; H: (N, 3) directions (any norm).  Returns the nine logs (N, 9), chi2 (N,)
    and the CKM moduli (N, 3, 3) under the Standard Model's reading."""
    H = H / np.linalg.norm(H, axis=1)[:, None]
    Uu, su, _ = np.linalg.svd(Ybatch(Uh[0], np.conj(H))); Ud, sd, _ = np.linalg.svd(Ybatch(Uh[1], H))
    se = np.linalg.svd(Ybatch(Uh[2], H), compute_uv=False)
    L = np.empty((len(H), 9))
    for j, sv in enumerate((su, sd, se)):
        L[:, 2 * j] = np.log(np.maximum(sv[:, 1] / sv[:, 0], 1e-300)); L[:, 2 * j + 1] = np.log(np.maximum(sv[:, 2] / sv[:, 0], 1e-300))
    L[:, 4] += LC; L[:, 5] -= LC
    V = np.abs(np.einsum("nji,njk->nik", np.conj(Uu[:, :, ::-1]), Ud[:, :, ::-1]))
    L[:, 6] = np.log(np.maximum(V[:, 0, 1], 1e-300)); L[:, 7] = np.log(np.maximum(V[:, 1, 2], 1e-300)); L[:, 8] = np.log(np.maximum(V[:, 0, 2], 1e-300))
    return L, np.sum(((L - T) / SIG) ** 2, axis=1), V


def tube(nt=400, nr=17, nphi=16, nrand=4000, seed=2610):
    i = np.arange(nt) + 0.5
    th = np.arccos(1 - 2 * i / nt); ph = math.pi * (1 + 5 ** 0.5) * i
    c, sn = np.cos(th / 2), np.sin(th / 2) * np.exp(1j * ph)          # t = sn / c, homogeneous
    h0 = np.stack([2 * sn * c, c ** 2 - sn ** 2, 1j * (c ** 2 + sn ** 2)], axis=1)
    h0 /= np.linalg.norm(h0, axis=1)[:, None]
    out = []
    for k in range(nr):
        r = 10 ** (-4 + k / 4)
        for j in range(nphi):
            out.append(h0 + r * np.exp(2j * math.pi * j / nphi) * np.conj(h0))
    z = np.random.default_rng(seed).normal(size=(nrand, 6)); z = z[:, :3] + 1j * z[:, 3:]
    H = np.concatenate(out + [z]); return H / np.linalg.norm(H, axis=1)[:, None]


HS = tube()


def vec(x):
    z = x[:3] + 1j * x[3:]; n = np.linalg.norm(z)
    return z / n if n > 0 else F3


def refine(Uh, x0, T, SIG):
    def res(x):
        L, _, _ = nine_batch(Uh, vec(x)[None], T, SIG); return (L[0] - T) / SIG

    def jac(x):
        e = 1e-7 * max(1.0, float(np.linalg.norm(x)))
        X = np.repeat(x[None], 7, axis=0); X[1:] += e * np.eye(6)
        L, _, _ = nine_batch(Uh, X[:, :3] + 1j * X[:, 3:], T, SIG); R = (L - T) / SIG
        return ((R[1:] - R[0]) / e).T
    try:
        r = least_squares(res, x0, jac=jac, method="trf", max_nfev=400, xtol=1e-10, ftol=1e-10)
        return float(np.sum(r.fun ** 2)), r.x
    except Exception:
        return None


def search(Uh, extra, T, SIG, H=None):
    """Returns (the grid's minimum chi2, (the refined minimum chi2, its 6-vector x))."""
    H = HS if H is None else H
    chis = np.empty(len(H))
    for a in range(0, len(H), 28200):
        chis[a:a + 28200] = nine_batch(Uh, H[a:a + 28200], T, SIG)[1]
    order = np.argsort(chis); keep = []
    for idx in order:
        if all(abs(np.vdot(H[j], H[idx])) < math.cos(0.05) for j in keep):
            keep.append(int(idx))
        if len(keep) == 8:
            break
    starts = [H[j] for j in keep] + [q for q in extra] + [np.conj(q) for q in extra]
    best = (float(chis[order[0]]), np.concatenate([H[order[0]].real, H[order[0]].imag]))
    for h in starts:
        o = refine(Uh, np.concatenate([h.real, h.imag]), T, SIG)
        if o is not None and o[0] < best[0]:
            best = o
    return float(chis[order[0]]), best
