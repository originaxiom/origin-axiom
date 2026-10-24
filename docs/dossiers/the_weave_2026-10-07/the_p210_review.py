#!/usr/bin/env python3
"""W148 — a non-authoring review on own code of the audit lane's two P-210 notes, the symmetric state's Green response
and grading (82c772eb5) and the exterior gap and thresholds (3ee8f33d0) (the rule: W148_RULE.md, committed and pushed
before this script).

  G1  the Green form G = u^dag v' + v^dag u' = a^dag a' - b^dag b' (sympy); unitary graphs b = U a are null; null planes
      from a non-orthonormal basis (P; Q) with P^dag P = Q^dag Q are unitary graphs; each is its own G-complement
  G2  the commutant of I3 x i and I3 x j in M6(C) is M3(C) x I2 (dimension 9, exact), in two quaternion bases
  G3  the grading Gamma(u, v) = (u, -v) exchanges a and b; graphs of C x I2 are Gamma-invariant iff C^2 = I; the plus
      trace of a Hermitian involution of rank r has dimension 2r, and 2r - 3 runs over {-3, -1, 1, 3}
  G4  the Cayley chart v = i H u, U = (I - iH)(I + iH)^-1; Q8-covariant H = A x I2; U = -I outside the chart
  G5  H2(S_t) = t n.sigma (sympy); the projectors for n and -n; the planes (8) as t -> 0; covariance under S -> gS and
      S -> g S g^dag; off S = I2 their Cayley U has U^2 != I
  G6  C_a^T eps = -eps C_a, (eps^-1)^T = eps, Y_ab = tr(C_a C_b) = -2 delta_ab with (C1, C2, C3) = (j, i, k), exact
  E1  D_K = -i sigma1 d_t - sigma2 x K in block form; Gamma anticommutes; the boundary current by Gauss-Legendre
  E2  the zero modes; the decaying ones; L_ext = E+ (+) E- six-dimensional, G-null, Gamma-invariant
  E3  K* = A x I2 has even positive rank; Weyl's bound; the positive count is constant on gapped paths
  E4  K(S_s) = s I3 x n.sigma; its positive space is the rank-3 projector's range; threshold s^2, decay lengths 1/s
  E5  the far-tail sequence f_L: |f_L| = 1 and |D0 f_L|^2 = L^-2 int |chi'|^2 (mpmath quadrature)
  E6  K = +-m I6 and the two extremes; the controls (a wrong Green sign, a reversed decay, an omitted MINUS slot)

  Noticed after the rule was pushed and before this script was committed (disclosed): E6's wrong-sign control is
  predicted to fail as worded. L_ext = E+ (+) E- has its u-part orthogonal to its v-part, so it is null for
  u^dag v' - v^dag u' too; only G1's graphs (with U not Hermitian) stop being null. The cell is computed as the rule
  words it.

    python3 -B the_p210_review.py      # writes the_p210_review.json beside itself
"""
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_p210_review.json"
RNG = np.random.default_rng(148)
I2, I3, I6 = np.eye(2), np.eye(3), np.eye(6)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
# W144's quaternions as 2 x 2 matrices, and a second basis
QI = np.array([[1j, 0], [0, -1j]])
QJ = np.array([[0, 1], [-1, 0]], dtype=complex)
BASES = {"W144 (i = diag(i, -i), j = [[0, 1], [-1, 0]], k = ij)": (QI, QJ, QI @ QJ),
         "-i sigma (i = -i sx, j = -i sy, k = -i sz)": (-1j * SX, -1j * SY, -1j * SZ)}
TOL = 1e-12


def haar(n):
    z = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / abs(np.diag(r)))


def herm(n):
    z = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
    return (z + z.conj().T) / 2


def proj(B):
    """orthogonal projector on the column span of B"""
    q, _ = np.linalg.qr(B)
    return q @ q.conj().T


def gram_G(X, Y, sign=1):
    """G(x, y) = u^dag v' + sign v^dag u' for columns of X, Y in (u, v) coordinates (12 rows)"""
    return X[:6].conj().T @ Y[6:] + sign * X[6:].conj().T @ Y[:6]


def to_uv(A, B):
    """(a, b) -> (u, v): u = (a + b)/sqrt2, v = (a - b)/sqrt2"""
    return np.vstack([(A + B) / np.sqrt(2), (A - B) / np.sqrt(2)])


def graph(U):
    return to_uv(I6.astype(complex), U)


def nrm(M):
    return float(np.linalg.norm(M, 2))


# ---------------------------------------------------------------- the first note

def G1():
    u, v, up, vp = sp.symbols("u v up vp")
    a, b = (u + v) / sp.sqrt(2), (u - v) / sp.sqrt(2)
    ap, bp = (up + vp) / sp.sqrt(2), (up - vp) / sp.sqrt(2)
    c = sp.conjugate
    ok_sym = sp.expand(c(a) * ap - c(b) * bp - (c(u) * vp + c(v) * up)) == 0
    worst_null, rank_ok = 0.0, True
    for _ in range(200):
        L = graph(haar(6))
        worst_null = max(worst_null, nrm(gram_G(L, L)))
        A = (L[:6] + L[6:]) / np.sqrt(2)
        rank_ok &= np.linalg.matrix_rank(A, tol=1e-10) == 6
    worst_unit, worst_comp, inj = 0.0, 0.0, True
    Gm = np.block([[np.zeros((6, 6)), I6], [I6, np.zeros((6, 6))]])
    for _ in range(200):
        P = RNG.normal(size=(6, 6)) + 1j * RNG.normal(size=(6, 6))
        Q = haar(6) @ P
        inj &= np.linalg.matrix_rank(P, tol=1e-10) == 6
        W = Q @ np.linalg.inv(P)
        worst_unit = max(worst_unit, nrm(W.conj().T @ W - I6))
        L = to_uv(P, Q)
        worst_null = max(worst_null, nrm(gram_G(L, L)) / nrm(P) ** 2)
        M = L.conj().T @ Gm                                    # G(l, x) = l^dag Gm x
        _, sv, vh = np.linalg.svd(M)
        ns = vh[np.sum(sv > 1e-9 * sv[0]):].conj().T
        comp_dim = ns.shape[1]
        worst_comp = max(worst_comp, nrm(proj(ns) - proj(L)))
        inj &= comp_dim == 6
    res = {"G = a^dag a' - b^dag b' (sympy)": ok_sym, "max |G on the plane|": worst_null,
           "graphs: projection to a of rank 6": bool(rank_ok),
           "(P; Q): P invertible, complement dimension 6": bool(inj),
           "max |(QP^-1)^dag (QP^-1) - I|": worst_unit, "max |P_complement - P_plane|": worst_comp}
    return res, bool(ok_sym and worst_null < TOL and rank_ok and inj and worst_unit < TOL and worst_comp < 1e-10)


def commutant(mats):
    """exact basis of {X in M6 : X A = A X for A in mats} (sympy), as 6 x 6 matrices"""
    rows = []
    for A in mats:
        As = sp.Matrix(A)
        X = sp.Matrix(6, 6, lambda i, j: sp.Symbol("x%d_%d" % (i, j)))
        E = X * As - As * X
        rows += [[sp.expand(E[i, j]).coeff(sp.Symbol("x%d_%d" % (k // 6, k % 6))) for k in range(36)]
                 for i in range(6) for j in range(6)]
    return sp.Matrix(rows).nullspace()


def exact(M):
    return [[sp.nsimplify(complex(x).real) + sp.I * sp.nsimplify(complex(x).imag) for x in r] for r in M]


def G2():
    res, ok = {}, True
    for name, (qi, qj, _) in BASES.items():
        ns = commutant([exact(np.kron(I3, qi)), exact(np.kron(I3, qj))])
        span = sp.Matrix.hstack(*ns)
        target = sp.Matrix.hstack(*[sp.Matrix(np.kron(np.outer(I3[a], I3[b]), I2).reshape(36).astype(int))
                                    for a in range(3) for b in range(3)])
        both = sp.Matrix.hstack(span, target)
        r_ns, r_both = len(ns), both.rank()
        res[name] = {"commutant dimension": r_ns, "rank with M3 x I2": r_both}
        ok &= r_ns == 9 and r_both == 9
    worst = 0.0
    for _ in range(50):
        U = np.kron(haar(3), I2)
        for qi, qj, _ in BASES.values():
            worst = max(worst, nrm(U @ np.kron(I3, qi) - np.kron(I3, qi) @ U),
                        nrm(U @ np.kron(I3, qj) - np.kron(I3, qj) @ U))
    res["max commutator of C x I2 with the generators"] = worst
    return res, bool(ok and worst < TOL)


def gamma_uv():
    return np.block([[I6, np.zeros((6, 6))], [np.zeros((6, 6)), -I6]])


def G3():
    R = np.block([[I6, I6], [I6, -I6]]) / np.sqrt(2)                       # (a, b) -> (u, v), an involution
    Gab = R @ gamma_uv() @ R
    swap = np.block([[np.zeros((6, 6)), I6], [I6, np.zeros((6, 6))]])
    ok_swap = nrm(Gab - swap) < TOL
    least = np.inf
    for _ in range(200):
        L = graph(np.kron(haar(3), I2))
        least = min(least, nrm(proj(gamma_uv() @ L) - proj(L)))
    ranks, worst_inv = {}, 0.0
    for r in range(4):
        for _ in range(20):
            V = haar(3)
            C = V @ np.diag([1] * r + [-1] * (3 - r)) @ V.conj().T
            U = np.kron(C, I2)
            L = graph(U)
            worst_inv = max(worst_inv, nrm(proj(gamma_uv() @ L) - proj(L)))
            w, _ = np.linalg.eigh((U + U.conj().T) / 2)
            plus = int(np.sum(abs(w - 1) < 1e-9))
            ranks.setdefault(str(r), set()).add(plus)
    ranks = {k: sorted(v) for k, v in ranks.items()}
    indices = sorted(2 * int(k) - 3 for k in ranks)
    res = {"Gamma exchanges a and b": bool(ok_swap), "least |P_Gamma L - P_L| over 200 non-involutions": least,
           "max |P_Gamma L - P_L| over Hermitian involutions": worst_inv, "plus-trace dimension by r": ranks,
           "indices 2r - 3": indices}
    ok = (ok_swap and least >= 1e-3 and worst_inv < 1e-10 and all(ranks[str(r)] == [2 * r] for r in range(4))
          and indices == [-3, -1, 1, 3])
    return res, bool(ok)


def G4():
    worst_null, worst_unit, worst_same = 0.0, 0.0, 0.0
    for _ in range(200):
        H = herm(6)
        L = np.vstack([I6, 1j * H])
        worst_null = max(worst_null, nrm(gram_G(L, L)))
        U = (I6 - 1j * H) @ np.linalg.inv(I6 + 1j * H)
        worst_unit = max(worst_unit, nrm(U.conj().T @ U - I6))
        worst_same = max(worst_same, nrm(proj(graph(U)) - proj(L)))
    worst_cov = 0.0
    for qi, qj, _ in BASES.values():
        H = np.kron(herm(3), I2)
        worst_cov = max(worst_cov, nrm(H @ np.kron(I3, qi) - np.kron(I3, qi) @ H),
                        nrm(H @ np.kron(I3, qj) - np.kron(I3, qj) @ H))
    h0 = np.vstack([I6, 0 * I6])
    ok_v0 = nrm(proj(np.vstack([I6, 1j * 0.0 * I6])) - proj(h0)) < TOL
    det_minus = abs(np.linalg.det(-I6 + I6))
    u0_plane = graph(-I6)
    ok_u0 = nrm(proj(u0_plane) - proj(np.vstack([0 * I6, I6]))) < 1e-10
    res = {"max |G on v = iHu|": worst_null, "max |U^dag U - I|": worst_unit, "max |P_graph(U) - P_plane|": worst_same,
           "A x I2 commutes with both generators (max commutator)": worst_cov,
           "h = 0 gives v = 0": bool(ok_v0),
           "U = -I is u = 0, and det(U + I) = 0 there": bool(ok_u0 and det_minus == 0)}
    ok = worst_null < TOL and worst_unit < 1e-10 and worst_same < 1e-10 and worst_cov < TOL and ok_v0 and ok_u0
    return res, bool(ok and det_minus == 0)


def H2(S):
    M = S @ S.conj().T
    return M - np.trace(M) / 2 * I2


def sqrtm_pos(M):
    w, V = np.linalg.eigh(M)
    return V @ np.diag(np.sqrt(w)) @ V.conj().T


def plane8(K, eta, which):
    return np.vstack([I6, 1j * eta * K]) if which == 1 else np.vstack([1j * eta * K, I6])


def G5():
    t = sp.Symbol("t", positive=True)
    n1, n2, n3 = sp.symbols("n1 n2 n3", real=True)
    ns = (n1 * sp.Matrix([[0, 1], [1, 0]]) + n2 * sp.Matrix([[0, -sp.I], [sp.I, 0]])
          + n3 * sp.Matrix([[1, 0], [0, -1]]))
    M = sp.eye(2) + t * ns
    ok_sym = sp.simplify(M - M.trace() / 2 * sp.eye(2) - t * ns) == sp.zeros(2, 2)
    worst_h2, worst_orth, dist_ok, worst_cov, least_u2 = 0.0, 0.0, True, 0.0, np.inf
    for _ in range(50):
        n = RNG.normal(size=3)
        n /= np.linalg.norm(n)
        nsig = n[0] * SX + n[1] * SY + n[2] * SZ
        Pp, Pm = np.kron(I3, (I2 + nsig) / 2), np.kron(I3, (I2 - nsig) / 2)
        worst_orth = max(worst_orth, nrm(Pp @ Pm), abs(nrm(Pp - Pm) - 1))
        for tt in (0.9, 0.3, 1e-3, 1e-6):
            S = sqrtm_pos(I2 + tt * nsig)
            worst_h2 = max(worst_h2, nrm(H2(S) - tt * nsig) / max(tt, 1e-300) * tt)
            K = np.kron(I3, H2(S))
            if tt == 1e-6:
                dist_ok &= nrm(proj(plane8(K, 1.0, 1)) - proj(np.vstack([I6, 0 * I6]))) < 1e-5
                dist_ok &= nrm(proj(plane8(K, 1.0, 2)) - proj(np.vstack([0 * I6, I6]))) < 1e-5
            if tt == 0.3:
                g = haar(2)
                G6 = np.kron(I3, g)
                for S2 in (g @ S, g @ S @ g.conj().T):
                    K2 = np.kron(I3, H2(S2))
                    for which in (1, 2):
                        moved = np.vstack([G6 @ plane8(K, 1.0, which)[:6], G6 @ plane8(K, 1.0, which)[6:]])
                        worst_cov = max(worst_cov, nrm(proj(plane8(K2, 1.0, which)) - proj(moved)))
                U = (I6 - 1j * K) @ np.linalg.inv(I6 + 1j * K)
                least_u2 = min(least_u2, nrm(U @ U - I6))
    res = {"H2(S_t) = t n.sigma (sympy, through S S^dag = I + t n.sigma)": bool(ok_sym),
           "max |H2(S_t) - t n.sigma| (numerics)": worst_h2,
           "max of |P+ P-| and ||P+ - P-| - 1|": worst_orth,
           "planes (8) within 1e-5 of v = 0, u = 0 at t = 1e-6": bool(dist_ok),
           "max covariance defect (S -> gS, S -> gSg^dag)": worst_cov, "least |U^2 - I| at t = 0.3, eta = 1": least_u2}
    ok = ok_sym and worst_h2 < 1e-10 and worst_orth < 1e-12 and dist_ok and worst_cov < 1e-10 and least_u2 > 1e-3
    return res, bool(ok)


def G6():
    eps = sp.Matrix([[0, 1], [-1, 0]])
    res, ok = {}, True
    sym_bases = {"W144": (sp.Matrix([[sp.I, 0], [0, -sp.I]]), sp.Matrix([[0, 1], [-1, 0]])),
                 "-i sigma": (sp.Matrix([[0, -sp.I], [-sp.I, 0]]), sp.Matrix([[0, -1], [1, 0]]))}
    for name, (qi, qj) in sym_bases.items():
        qk = qi * qj
        C = (qj, qi, qk)
        anti = all(sp.simplify(c.T * eps + eps * c) == sp.zeros(2, 2) for c in C)
        einv_t = eps.inv().T == eps
        Y = sp.Matrix(3, 3, lambda a, b: sum((C[a].T * eps * C[b])[m, n] * eps.inv()[m, n]
                                             for m in range(2) for n in range(2)))
        tr = sp.Matrix(3, 3, lambda a, b: (C[a] * C[b]).trace())
        okY = sp.simplify(Y - tr) == sp.zeros(3, 3) and sp.simplify(Y + 2 * sp.eye(3)) == sp.zeros(3, 3)
        res[name] = {"C^T eps = -eps C": bool(anti), "(eps^-1)^T = eps": bool(einv_t),
                     "Y = tr(C_a C_b) = -2 delta": bool(okY)}
        ok &= anti and einv_t and okY
    return res, bool(ok)


# ---------------------------------------------------------------- the second note

def D_of(K, p):
    return -1j * p * np.kron(SX, I6) - np.kron(SY, K)


def gauss(n, T):
    x, w = np.polynomial.legendre.leggauss(n)
    return T * (x + 1) / 2, w * T / 2


def E1():
    p, k = sp.symbols("p k")
    D = -sp.I * p * sp.Matrix([[0, 1], [1, 0]]) - sp.Matrix([[0, -sp.I], [sp.I, 0]]) * k
    ok_block = sp.simplify(D - sp.Matrix([[0, sp.I * (-p + k)], [-sp.I * (p + k), 0]])) == sp.zeros(2, 2)
    worst_blk, worst_anti, worst_bdry = 0.0, 0.0, 0.0
    Gam = gamma_uv()
    T = 1.7
    ts, ws = gauss(24, T)
    for _ in range(50):
        K = herm(6)
        pp = RNG.normal()
        blk = np.block([[np.zeros((6, 6)), 1j * (-pp * I6 + K)], [-1j * (pp * I6 + K), np.zeros((6, 6))]])
        worst_blk = max(worst_blk, nrm(D_of(K, pp) - blk))
        worst_anti = max(worst_anti, nrm(Gam @ D_of(K, pp) + D_of(K, pp) @ Gam))
        c1 = RNG.normal(size=(5, 12)) + 1j * RNG.normal(size=(5, 12))
        c2 = RNG.normal(size=(5, 12)) + 1j * RNG.normal(size=(5, 12))
        psi = lambda c, t: sum(c[j] * t ** j for j in range(5))
        dpsi = lambda c, t: sum(j * c[j] * t ** (j - 1) for j in range(1, 5))
        Dpsi = lambda c, t: -1j * np.kron(SX, I6) @ dpsi(c, t) - np.kron(SY, K) @ psi(c, t)
        lhs = sum(w * (np.vdot(psi(c1, t), Dpsi(c2, t)) - np.vdot(Dpsi(c1, t), psi(c2, t))) for t, w in zip(ts, ws))
        cur = lambda t: np.vdot(psi(c1, t), np.kron(SX, I6) @ psi(c2, t))
        rhs = 1j * cur(0.0) - 1j * cur(T)
        worst_bdry = max(worst_bdry, abs(lhs - rhs) / max(1.0, abs(rhs)))
    res = {"block form (sympy, d_t -> p)": bool(ok_block), "max |D_K - block|": worst_blk,
           "max |Gamma D + D Gamma|": worst_anti, "max relative boundary-identity defect": worst_bdry}
    return res, bool(ok_block and worst_blk < TOL and worst_anti < TOL and worst_bdry < 1e-10)


def decaying_plane(K, reverse=False):
    w, V = np.linalg.eigh(K)
    Ep, Em = V[:, w > 0], V[:, w < 0]
    if reverse:
        Ep, Em = Em, Ep
    top = np.hstack([Ep, np.zeros((6, Em.shape[1]))])
    bot = np.hstack([np.zeros((6, Ep.shape[1])), Em])
    return np.vstack([top, bot]), Ep.shape[1], Em.shape[1]


def E2():
    worst_eq, worst_null, dims_ok, gam_ok, decay_ok = 0.0, 0.0, True, True, True
    for _ in range(200):
        K = herm(6)
        w, V = np.linalg.eigh(K)
        if min(abs(w)) < 1e-3:
            continue
        u0, v0 = RNG.normal(size=6) + 1j * RNG.normal(size=6), RNG.normal(size=6) + 1j * RNG.normal(size=6)
        with mp.workdps(30):                                      # mpmath's expm, differentiated numerically
            Km, t, h = mp.matrix(K.tolist()), mp.mpf("0.7"), mp.mpf(10) ** -12
            um, vm = mp.matrix(u0.tolist()), mp.matrix(v0.tolist())
            uf = lambda x: mp.expm(-x * Km) * um
            vf = lambda x: mp.expm(x * Km) * vm
            du = (uf(t + h) - uf(t - h)) / (2 * h)
            dv = (vf(t + h) - vf(t - h)) / (2 * h)
            ru = mp.norm(du + Km * uf(t)) / mp.norm(uf(t))
            rv = mp.norm(-dv + Km * vf(t)) / mp.norm(vf(t))
            worst_eq = max(worst_eq, float(ru), float(rv))
        far = 40.0 / min(abs(w))
        for k in range(6):
            uk = np.exp(-far * w[k]) * np.linalg.norm(V[:, k])
            vk = np.exp(far * w[k]) * np.linalg.norm(V[:, k])
            decay_ok &= (uk < 1e-10) == (w[k] > 0) and (vk < 1e-10) == (w[k] < 0)
        L, dp, dm = decaying_plane(K)
        dims_ok &= dp + dm == 6
        worst_null = max(worst_null, nrm(gram_G(L, L)))
        gam_ok &= nrm(proj(gamma_uv() @ L) - proj(L)) < 1e-10
    res = {"max relative |(d_t + K) u|, |(-d_t + K) v| (expm, 30 digits)": float(worst_eq),
           "decay exactly on E+ (u) and E- (v)": bool(decay_ok),
           "L_ext six-dimensional": bool(dims_ok), "max |G on L_ext|": worst_null,
           "L_ext Gamma-invariant": bool(gam_ok)}
    return res, bool(worst_eq < 1e-10 and decay_ok and dims_ok and worst_null < TOL and gam_ok)


def E3():
    even = True
    for _ in range(200):
        A = herm(3)
        Ks = np.kron(A, I2)
        even &= int(np.sum(np.linalg.eigvalsh(Ks) > 0)) % 2 == 0
    worst_weyl = -np.inf
    for _ in range(2000):
        K, K2 = herm(6), herm(6)
        d = np.max(abs(np.linalg.eigvalsh(K2) - np.linalg.eigvalsh(K)))
        worst_weyl = max(worst_weyl, d - nrm(K2 - K))
    const = True
    for _ in range(200):
        Ks = np.kron(herm(3), I2)
        delta = min(abs(np.linalg.eigvalsh(Ks)))
        Dl = herm(6)
        Dl *= 0.49 * delta / nrm(Dl)
        counts = {int(np.sum(np.linalg.eigvalsh(Ks + s * Dl) > 0)) for s in np.linspace(0, 1, 101)}
        const &= len(counts) == 1
    res = {"positive rank of A x I2 even (200)": bool(even), "max (Weyl defect - |K' - K|) (2 000)": float(worst_weyl),
           "positive count constant on 200 gapped paths": bool(const)}
    return res, bool(even and worst_weyl <= TOL and const)


def E4():
    worst, ok = 0.0, True
    for _ in range(20):
        n = RNG.normal(size=3)
        n /= np.linalg.norm(n)
        nsig = n[0] * SX + n[1] * SY + n[2] * SZ
        for s in (0.5, 0.1, 0.01):
            K = np.kron(I3, H2(sqrtm_pos(I2 + s * nsig)))
            worst = max(worst, nrm(K - s * np.kron(I3, nsig)))
            w, V = np.linalg.eigh(K)
            Ep = V[:, w > 0]
            ok &= Ep.shape[1] == 3 and nrm(proj(Ep) - np.kron(I3, (I2 + nsig) / 2)) < 1e-10
            ok &= abs(min(abs(w)) ** 2 - s * s) < 1e-12 and np.allclose(1 / abs(w), 1 / s)
    res = {"max |K(S_s) - s I3 x n.sigma|": worst, "positive space rank 3, the projector's range; s^2; 1/s": bool(ok)}
    return res, bool(worst < 1e-12 and ok)


def E5():
    with mp.workdps(30):
        bump = lambda x: mp.exp(-1 / (x * (1 - x))) if 0 < x < 1 else mp.mpf(0)
        dbump = lambda x: bump(x) * (-(2 * x - 1) / (x * (1 - x)) ** 2) if 0 < x < 1 else mp.mpf(0)
        c = 1 / mp.sqrt(mp.quad(lambda x: bump(x) ** 2, [0, 0.5, 1]))
        chi2_int = mp.quad(lambda x: (c * dbump(x)) ** 2, [0, 0.5, 1])
        rows, worst = {}, mp.mpf(0)
        for L in (1, 10, 100):
            T = 10 * L
            f2 = mp.quad(lambda t: (c * bump((t - T) / L)) ** 2 / L, [T, T + L / 2, T + L])
            d2 = mp.quad(lambda t: (c * dbump((t - T) / L) / L) ** 2 / L, [T, T + L / 2, T + L])
            dev = max(abs(f2 - 1), abs(d2 - chi2_int / L ** 2) / (chi2_int / L ** 2))
            worst = max(worst, dev)
            rows[str(L)] = {"|f_L|^2": mp.nstr(f2, 12), "|D0 f_L|^2": mp.nstr(d2, 12),
                            "L^-2 int |chi'|^2": mp.nstr(chi2_int / L ** 2, 12)}
    return {"rows": rows, "max deviation": mp.nstr(worst, 3)}, bool(worst < 1e-8)


def E6():
    res = {}
    Lp, dp, _ = decaying_plane(2.0 * I6)
    Lm, dm, _ = decaying_plane(-2.0 * I6)
    ok_ext = (dp == 6 and nrm(proj(Lp) - proj(np.vstack([I6, 0 * I6]))) < 1e-12 and dm == 0
              and nrm(proj(Lm) - proj(np.vstack([0 * I6, I6]))) < 1e-12)
    res["m > 0: v = 0, plus rank 6, index +3; m < 0: u = 0, rank 0, index -3"] = bool(ok_ext)
    least_g1, max_e2 = np.inf, 0.0
    for _ in range(200):
        L = graph(haar(6))
        least_g1 = min(least_g1, nrm(gram_G(L, L, sign=-1)))
    rev_ok, omit_ok = True, True
    for _ in range(200):
        K = herm(6)
        L, dpos, dneg = decaying_plane(K)
        max_e2 = max(max_e2, nrm(gram_G(L, L, sign=-1)))
        Lr, a, b = decaying_plane(K, reverse=True)
        rev_ok &= a + b == 6 and nrm(gram_G(Lr, Lr)) < TOL
        omit_ok &= dpos < 6 or dneg == 0
    res["wrong sign: least |G' on G1's graphs|"] = least_g1
    res["wrong sign: largest |G' on E2's L_ext|"] = max_e2
    res["reversed decay: E- (+) E+, six-dimensional and null"] = bool(rev_ok)
    res["MINUS slot omitted: E+ (+) 0 below 6 on every K drawn"] = bool(omit_ok)
    wrong_sign_as_worded = least_g1 >= 1e-3 and max_e2 >= 1e-3              # "the planes of G1 and E2 are not null"
    res["the rule's wrong-sign control as worded (G1's and E2's planes not null)"] = bool(wrong_sign_as_worded)
    return res, bool(ok_ext and wrong_sign_as_worded and rev_ok and omit_ok)


def main():
    t0 = time.time()
    out = {"arc": "W148", "rule": "W148_RULE.md", "status": "one run", "python": sys.version.split()[0],
           "numpy": np.__version__, "sympy": sp.__version__, "mpmath": mp.__version__}
    cells, secs = {}, {}
    for name, fn in (("G1", G1), ("G2", G2), ("G3", G3), ("G4", G4), ("G5", G5), ("G6", G6),
                     ("E1", E1), ("E2", E2), ("E3", E3), ("E4", E4), ("E5", E5), ("E6", E6)):
        t = time.time()
        try:
            out[name], cells[name] = fn()
        except Exception as exc:  # a failed part is kept and disclosed
            out[name + "_failed"] = repr(exc)
            cells[name] = False
        secs[name] = round(time.time() - t, 1)
    out["cells"] = {k: bool(v) for k, v in cells.items()}
    out["every predicted cell holds"] = bool(all(out["cells"].values()))
    out["part_seconds"] = secs
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])
    failed = [k for k in out if k.endswith("_failed")]
    if failed:
        print("failed parts:", failed)


if __name__ == "__main__":
    main()
