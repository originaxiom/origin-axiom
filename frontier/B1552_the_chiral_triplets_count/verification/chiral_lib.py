#!/usr/bin/env python3
"""sm:B1552 THE CHIRAL TRIPLET'S COUNT -- the shared library (nothing is read on import).

The frame's count (sm:B1515's F-HE dictionary, unchanged: N(10') = -I(W), N(5bar') = -I(Lambda^2 W), with
I(X) = n(X) - n(X*) the difference of interior dimensions) read at the weave's spin vacuum. The vacuum is the common
point rho_Q (a -> i, b -> j), which GENESIS PF1's reading and the joint action force (the weave dossier, W2). The rank-four
modules on a state's third tick are, for a parity p (fibre character chi_p) and a value kappa on the stable letter:
  (a) the spin four:          A = lambda (x) (rho_Q + rho_Q),
  (b) the sector and mirror:  A = lambda rho_Q + conj(lambda) rho_Q,
with lambda the character (chi_p on the fibre, kappa on the stable letter). W1 = [[A, c], [0, 1]] with c a generic
interior class of A.

Two routes, independent in presentation and in linear algebra:
  route 1  the tick's own route-P presentation (sm:B1538's degree-one cover of the state sign + w^3), the lift of the
           common point found from that presentation's relators, and sm:B1549's banked cohomology and count
           (three_lib.cohom, interior, generic, frame_mats, count_of) at mpmath precision;
  route 2  the presentation <a, b, t | t x t^-1 = phi^3(x)> with phi^3 the deck-compatible third power of the state's
           automorphism (the weave dossier's word_aut composed three times), the inherited lift g^3, the peripheral
           pair ([a, b], u^-1 t) with phi^3([a, b]) = u [a, b] u^-1, and this file's own Fox calculus and SVD ranks
           in numpy double precision (the modules are unitary, so no growth), every rank decision's gap recorded.
"""
import json
import random
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent


def _root():
    for p in HERE.parents:
        if (p / "frontier").is_dir():
            return p
    raise RuntimeError("the repository root was not found")


ROOT = _root()
DOSSIER = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
sys.path.insert(0, str(DOSSIER))
import the_parity_sectors as S  # noqa: E402  (the states, the resolving tick, sm:B1550's tetra_lib -> sm:B1549's three_lib)
import the_common_point as CP  # noqa: E402  (the moves as automorphisms of F2, 2O, quaternion products)

T = S.T
PC = S.PC
DPS = 50
T.DPS = DPS
mp.mp.dps = DPS
M8 = 8
PARITIES = [(1, 0), (0, 1), (1, 1)]
NAMES = {(1, 0): "(1/2, 0)", (0, 1): "(0, 1/2)", (1, 1): "(1/2, 1/2)"}


def odd_trace_states():
    """the population: the twelve odd-trace states of GENESIS to word length 6, in census order"""
    return [sw for sw in S.states() if S.resolving_tick(sw[1:]) == 3]


def tick_state(sw, k=3):
    w = sw[1:]
    sign = sw[0] if k % 2 else "+"
    return sign + w * k


# ------------------------------------------------------------------------------------------ quaternions, exact
def exact(x):
    for v in (0, 0.5, 1):
        if abs(abs(x) - v) < 1e-9:
            return mp.mpf(v) * (1 if x >= 0 else -1)
    assert abs(abs(x) - 2 ** -0.5) < 1e-9, x
    return mp.sqrt(2) / 2 * (1 if x >= 0 else -1)


def qmat_mp(q):
    w, x, y, z = (exact(v) for v in q)
    return mp.matrix([[w + 1j * x, y + 1j * z], [-y + 1j * z, w - 1j * x]])


def qmat_np(q):
    w, x, y, z = q
    return np.array([[w + 1j * x, y + 1j * z], [-y + 1j * z, w - 1j * x]], dtype=complex)


QI_MP, QJ_MP = mp.matrix([[1j, 0], [0, -1j]]), mp.matrix([[0, 1], [-1, 0]])
QI_NP, QJ_NP = np.array([[1j, 0], [0, -1j]]), np.array([[0, 1], [-1, 0]], dtype=complex)


# ------------------------------------------------------------------------------------------ route 1
def route1_setup(sw, k=3):
    swk = tick_state(sw, k)
    C = PC.Cover(PC.State(swk), (1, 0, 1), 0)
    Pr, P = T.presentation_P(C)
    assert [w for (_, _, w) in Pr.gens] == ["a", "b", "t"], Pr.gens
    st = PC.State(swk)
    lifts = []
    for g in CP.TWO_O.values():
        G = qmat_mp(g)
        gens = {"a": QI_MP, "b": QJ_MP, "t": G}
        ok = True
        for r in st.G.rels:
            X = mp.eye(2)
            for c in r:
                X = X * (gens[c] if c.islower() else gens[c.lower()] ** -1)
            if mp.norm(X - mp.eye(2)) > mp.mpf(10) ** -40:
                ok = False
                break
        if ok:
            lifts.append(g)
    return {"swk": swk, "C": C, "Pr": Pr, "P": P, "lifts": lifts}


def route1_module(Pr, p, kappa_exp, g, variant):
    G = qmat_mp(g)
    gens = {"a": QI_MP, "b": QJ_MP, "t": G}
    chi = {"a": mp.mpf((-1) ** p[0]), "b": mp.mpf((-1) ** p[1]), "t": mp.expjpi(mp.mpf(2 * kappa_exp) / M8)}
    mats = []
    for (_, _, word) in Pr.gens:
        R, lam = mp.eye(2), mp.mpc(1)
        for c in word:
            R = R * (gens[c] if c.islower() else gens[c.lower()] ** -1)
            lam *= chi[c] if c.islower() else 1 / chi[c.lower()]
        lam2 = lam if variant == "a" else mp.conj(lam)
        A = [[mp.mpc(0)] * 4 for _ in range(4)]
        for i in range(2):
            for j in range(2):
                A[i][j] = lam * R[i, j]
                A[2 + i][2 + j] = lam2 * R[i, j]
        mats.append(A)
    return mats


def route1_structure(setup, A):
    s = T.cohom(T.Mod(A), setup["P"])
    return {k: s[k] for k in ("h0", "h1", "r1", "n")}


def route1_count(setup, A, seed):
    """the count at a generic interior class, exactly as sm:B1549's read_P draws it"""
    P = setup["P"]
    s = T.cohom(T.Mod(A), P, want_interior=True)
    if not s["interior"]:
        return None
    z = T.generic(s["interior"], random.Random(seed))
    cvals = [z[4 * j:4 * j + 4] for j in range(P.ngen)]
    cnt, reads = T.count_of(T.frame_mats(A, cvals), P)
    gaps = [g for r in reads.values() for g in r["gaps"]]
    return {"count": [int(cnt[0]), int(cnt[1])], "reads": {k: {kk: v[kk] for kk in ("h0", "h1", "r1", "n")}
                                                          for k, v in reads.items()},
            "gaps": [[float(x) if x is not None else None for x in g] if isinstance(g, (list, tuple)) else g
                     for g in gaps]}


# ------------------------------------------------------------------------------------------ route 2
def fr_reduce(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def power(phi, k):
    out = {1: [1], 2: [2]}
    for _ in range(k):
        out = CP.compose(out, phi)
    return out


def apply(phi, w):
    out = []
    for x in w:
        out += phi[x] if x > 0 else CP.inv(phi[-x])
    return fr_reduce(out)


ELL = [1, 2, -1, -2]                    # [a, b] = a b a^-1 b^-1


def peripheral_u(phi):
    """u with phi([a, b]) = u [a, b] u^-1 (phi orientation-preserving on the fibre)"""
    w = apply(phi, ELL)
    k = 0
    while k < len(w) // 2 and w[k] == -w[-1 - k]:
        k += 1
    u0, core = w[:k], w[k:len(w) - k]
    assert len(core) == 4, ("not conjugate to a commutator of length 4", w)
    for r in range(4):
        if core == ELL[r:] + ELL[:r]:
            return fr_reduce(u0 + CP.inv(ELL[:r]))
    raise AssertionError(("the core is not a rotation of [a, b]", core))


def route2_setup(sw, k=3):
    sign = 1 if sw[0] == "+" else -1
    phi1 = CP.word_aut(sw[1:], sign)
    phik = power(phi1, k)
    lifts = []
    for g in CP.extend(phi1):
        q = (1.0, 0.0, 0.0, 0.0)
        for _ in range(k):
            q = CP.qmul(q, g)
        lifts.append(q)
    rels = [[3, x, -3] + CP.inv(phik[x]) for x in (1, 2)]   # t x t^-1 phi^k(x)^-1, generators 1 = a, 2 = b, 3 = t
    u = peripheral_u(phik)
    periph = [ELL, CP.inv(u) + [3]]
    return {"phik": phik, "lifts": lifts, "rels": rels, "periph": periph}


def route2_module(p, kappa_exp, g, variant):
    kap = np.exp(2j * np.pi * kappa_exp / M8)
    G = qmat_np(g)
    base = {1: (QI_NP, (-1) ** p[0]), 2: (QJ_NP, (-1) ** p[1]), 3: (G, kap)}
    mats = {}
    for gen, (R, lam) in base.items():
        lam2 = lam if variant == "a" else np.conj(lam)
        A = np.zeros((4, 4), dtype=complex)
        A[0:2, 0:2] = lam * R
        A[2:4, 2:4] = lam2 * R
        mats[gen] = A
    return mats


def _word(mats, w, e):
    X = np.eye(e, dtype=complex)
    for x in w:
        X = X @ (mats[x] if x > 0 else np.linalg.inv(mats[-x]))
    return X


def _fox(mats, w, e):
    """the e x 3e block of z -> z(w) for left cocycles"""
    out = np.zeros((e, 3 * e), dtype=complex)
    pre = np.eye(e, dtype=complex)
    for x in w:
        j = abs(x) - 1
        if x > 0:
            out[:, j * e:(j + 1) * e] += pre
            pre = pre @ mats[x]
        else:
            pre = pre @ np.linalg.inv(mats[-x])
            out[:, j * e:(j + 1) * e] -= pre
    return out


def _rank(A, gaps, tol=1e-8):
    if A.size == 0:
        return 0
    s = np.linalg.svd(A, compute_uv=False)
    if s.size == 0 or s[0] == 0:
        return 0
    r = int(np.sum(s > tol * s[0]))
    kept = s[r - 1] / s[0] if r > 0 else None
    dropped = s[r] / s[0] if r < len(s) else None
    gaps.append([kept, dropped])
    return r


def _null(A, tol=1e-8):
    u, s, vh = np.linalg.svd(A)
    r = int(np.sum(s > tol * s[0])) if s.size and s[0] > 0 else 0
    return vh[r:].conj().T                                   # columns span the kernel


def route2_cohom(setup, mats, want_interior=False):
    e = mats[1].shape[0]
    gaps = []
    for r in setup["rels"]:
        assert np.allclose(_word(mats, r, e), np.eye(e), atol=1e-9), "a relator is not 1 in the module"
    F = np.vstack([_fox(mats, r, e) for r in setup["rels"]])           # (2e) x (3e)
    Z = _null(F) if F.size else np.eye(3 * e)
    dg = np.vstack([mats[j] - np.eye(e) for j in (1, 2, 3)])           # (3e) x e: v -> ((X_j - 1) v)_j
    r0 = _rank(dg, gaps)
    h0 = e - r0
    h1 = Z.shape[1] - r0
    # the restriction to the cusp
    rowsR, BPb = [], []
    for w in setup["periph"]:
        rowsR.append(_fox(mats, w, e))
        BPb.append(_word(mats, w, e) - np.eye(e))
    R = np.vstack(rowsR)                                                # (2e) x (3e)
    BP = np.vstack(BPb)                                                 # (2e) x e
    RZ = R @ Z
    rBP = _rank(BP, gaps)
    rboth = _rank(np.hstack([BP, RZ]), gaps)
    r1 = rboth - rBP
    out = {"h0": h0, "h1": h1, "r1": r1, "n": h1 - r1, "gaps": gaps}
    if want_interior:
        K = _null(np.hstack([RZ, -BP]))
        alpha = K[:Z.shape[1], :]
        Icoc = Z @ alpha                                                # cocycles whose restriction is a coboundary
        # a complement of the coboundaries inside them
        Bcol = dg                                                       # (3e) x e, the coboundary directions
        basis, cur = [], Bcol.copy()
        rk = np.linalg.matrix_rank(cur, tol=1e-8)
        for j in range(Icoc.shape[1]):
            cand = np.hstack([cur, Icoc[:, j:j + 1]])
            rk2 = np.linalg.matrix_rank(cand, tol=1e-8)
            if rk2 > rk:
                basis.append(Icoc[:, j])
                cur, rk = cand, rk2
        out["interior"] = basis
    return out


def _wedge2(X):
    n = X.shape[0]
    idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return np.array([[X[i, k] * X[j, l] - X[i, l] * X[j, k] for (k, l) in idx] for (i, j) in idx])


def route2_count(setup, mats, seed):
    s = route2_cohom(setup, mats, want_interior=True)
    if not s["interior"]:
        return None
    rng = np.random.default_rng(seed)
    coef = rng.uniform(-1, 1, len(s["interior"])) + 1j * rng.uniform(-1, 1, len(s["interior"]))
    z = sum(c * v for c, v in zip(coef, s["interior"]))
    e = mats[1].shape[0]
    W1 = {}
    for j in (1, 2, 3):
        X = np.zeros((e + 1, e + 1), dtype=complex)
        X[:e, :e] = mats[j]
        X[:e, e] = z[(j - 1) * e:j * e]
        X[e, e] = 1
        W1[j] = X
    dual = lambda M: {j: np.linalg.inv(M[j]).T for j in M}       # noqa: E731
    L2 = {j: _wedge2(W1[j]) for j in W1}
    reads = {"W1": route2_cohom(setup, W1), "W1*": route2_cohom(setup, dual(W1)),
             "L2": route2_cohom(setup, L2), "L2*": route2_cohom(setup, dual(L2))}
    cnt = (reads["W1"]["n"] - reads["W1*"]["n"], reads["L2"]["n"] - reads["L2*"]["n"])
    return {"count": [int(cnt[0]), int(cnt[1])],
            "reads": {k: {kk: v[kk] for kk in ("h0", "h1", "r1", "n")} for k, v in reads.items()},
            "worst gap": min([g[0] / g[1] for v in reads.values() for g in v["gaps"]
                              if g[0] is not None and g[1] is not None and g[1] > 0] or [float("inf")])}
