#!/usr/bin/env python3
"""Independent pure-mathematics verification suite for Card X-C1b
(Batch V1, second ten REGISTERED weave rows: 923, 924, 925, 926, 927, 928, 929, 930, 931, 934).

Zero imports from any SM-seat script or dossier, and zero execution of any SM-seat script.
All free-group automorphisms, mapping-torus presentations, Reidemeister-Schreier finite covers,
finite-field and high-precision complex Fox cohomology spaces, hyperbolic SL(2, C) holonomies,
spin and adjoint representations, slope-law censuses, number-field trace ideals (via split-in-half
algebraic resultants and PARI local maximal orders), and projective-line gluing scans are built
from mathematical definitions alone. 0 of 19.
"""
from __future__ import annotations

import cmath
import collections
from collections import Counter, deque
from fractions import Fraction
import hashlib
import itertools
import json
import math
import pathlib
import subprocess
import sys
import time

import gmpy2
import mpmath as mp
import numpy as np
import snappy
from snappy import pari as PARI
import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp

HERE = pathlib.Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]

mp.mp.dps = 160
gmpy2.get_context().precision = 300  # ~90 decimal digits in GNU MPFR/MPC
PARI.allocatemem(512 * 1024 * 1024, silent=True)

GMMat = list[list[gmpy2.mpc]]
INV = {"a": "A", "b": "B", "A": "a", "B": "b", "t": "T", "T": "t"}


# ---------------------------------------------------------------------------
# 1. Free-group automorphisms, conjugators, and GENESIS state enumeration
# ---------------------------------------------------------------------------

def inv_w(w: str) -> str:
    return "".join(INV[c] for c in reversed(w))


def red_w(w: str) -> str:
    out: list[str] = []
    for c in w:
        if out and out[-1] == INV[c]:
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def sub_w(w: str, img: dict[str, str]) -> str:
    return red_w("".join(img[c] if c in img else inv_w(img[INV[c]]) for c in w))


def phi1_words(sign: str, word: str) -> dict[str, str]:
    """Bundle convention: phi_L(a)=ab, phi_L(b)=b; phi_R(a)=a, phi_R(b)=ba; last letter first; - applies iota."""
    img = {"a": "a", "b": "b"}
    for ch in reversed(word):
        step = {"a": "ab", "b": "b"} if ch == "L" else {"a": "a", "b": "ba"}
        img = {g: sub_w(img[g], step) for g in "ab"}
    if sign == "-":
        img = {g: sub_w(img[g], {"a": "A", "b": "B"}) for g in "ab"}
    return img


def iter_phi(sign: str, word: str, k: int) -> dict[str, str]:
    p1 = phi1_words(sign, word)
    img = {"a": "a", "b": "b"}
    for _ in range(k):
        img = {g: sub_w(img[g], p1) for g in "ab"}
    return img


def extract_u(img: dict[str, str]) -> str:
    """Find reduced word u in F_2 such that img([a, b]) = u [a, b] u^-1, so u^-1 t commutes with [a, b]."""
    target = sub_w("abAB", img)
    i, j = 0, len(target)
    while j - i > 4 and target[i] == INV[target[j - 1]]:
        i += 1
        j -= 1
    core = target[i:j]
    shifts = {"abAB": "", "bABa": "A", "ABab": "BA", "Baba": "B"}
    if core not in shifts:
        raise RuntimeError(f"Unexpected commutator core {core!r}")
    u = red_w(target[:i] + shifts[core])
    if red_w(u + "abAB" + inv_w(u)) != target:
        raise RuntimeError("Conjugator verification failed")
    return u


def steps_route1(sign: str, word: str, k: int) -> tuple[list[str], str, dict[str, str]]:
    """Route 1 presentation: state (sign * word)^k as tick_sign + (word * k)."""
    tick_sign = "+" if (sign == "+" or k % 2 == 0) else "-"
    w_k = word * k
    steps = list(reversed(w_k)) + (["-"] if tick_sign == "-" else [])
    img = phi1_words(tick_sign, w_k)
    mu_w = "t" if tick_sign == "+" else "abt"
    return steps, mu_w, img


def steps_route2(sign: str, word: str, k: int) -> tuple[list[str], str, dict[str, str]]:
    """Route 2 deck-compatible presentation: <a, b, t | t x t^-1 = phi^k(x)> with meridian u_k^-1 t."""
    steps1 = list(reversed(word)) + (["-"] if sign == "-" else [])
    steps = steps1 * k
    img = iter_phi(sign, word, k)
    u_k = extract_u(img)
    mu_w = inv_w(u_k) + "t"
    return steps, mu_w, img


def hom_mat(img: dict[str, str]) -> tuple[tuple[int, int], tuple[int, int]]:
    def ex(w: str, g: str) -> int:
        return w.count(g) - w.count(g.upper())
    return ((ex(img["a"], "a"), ex(img["b"], "a")), (ex(img["a"], "b"), ex(img["b"], "b")))


def homology_mat(sign: str, word: str) -> tuple[tuple[int, int], tuple[int, int]]:
    return hom_mat(phi1_words(sign, word))


def mat2_mul(A: tuple[tuple[int, int], tuple[int, int]], B: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def mat2_pow(M: tuple[tuple[int, int], tuple[int, int]], k: int) -> tuple[tuple[int, int], tuple[int, int]]:
    R = ((1, 0), (0, 1))
    for _ in range(k):
        R = mat2_mul(R, M)
    return R


def resolving_tick(M: tuple[tuple[int, int], tuple[int, int]]) -> int:
    for k in (1, 2, 3):
        Mk = mat2_pow(M, k)
        if Mk[0][0] % 2 == 1 and Mk[0][1] % 2 == 0 and Mk[1][0] % 2 == 0 and Mk[1][1] % 2 == 1:
            return k
    raise RuntimeError("Monodromy mod 2 failed to resolve by tick 3")


def canon_word(w: str) -> str:
    rots = [w[i:] + w[:i] for i in range(len(w))]
    sw = w.translate(str.maketrans("LR", "RL"))
    rots += [sw[i:] + sw[:i] for i in range(len(sw))]
    return min(rots)


def is_primitive(w: str) -> bool:
    n = len(w)
    return all(w != w[k:] + w[:k] for k in range(1, n) if n % k == 0)


def unsigned_primitive_words(nmax: int) -> list[str]:
    words: set[str] = set()
    for n in range(2, nmax + 1):
        for tup in itertools.product("LR", repeat=n):
            w = "".join(tup)
            if "L" in w and "R" in w and is_primitive(w):
                words.add(canon_word(w))
    return sorted(words, key=lambda s: (len(s), s))


def genesis_states(nmax: int, odd_only: bool = False) -> list[tuple[str, str, tuple[tuple[int, int], tuple[int, int]]]]:
    out = []
    for w in unsigned_primitive_words(nmax):
        for sgn in ("+", "-"):
            M = homology_mat(sgn, w)
            tr = M[0][0] + M[1][1]
            if odd_only and (tr % 2 == 0):
                continue
            out.append((sgn, w, M))
    return out


# ---------------------------------------------------------------------------
# 2. Exact finite-field linear algebra, Fox step-chain cohomology, and spin lifts
# ---------------------------------------------------------------------------

def np_rank_gf(M: np.ndarray, p: int) -> int:
    if M.size == 0:
        return 0
    A = M.astype(np.int64, copy=True) % p
    m, n = A.shape
    r = 0
    for c in range(n):
        if r >= m:
            break
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0:
            continue
        pr = r + int(nz[0])
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        sub = A[r + 1 :, c]
        rows = np.flatnonzero(sub)
        if rows.size:
            fac = (sub[rows] * inv) % p
            A[r + 1 + rows] = (A[r + 1 + rows] - fac[:, None] * A[r]) % p
        r += 1
    return r


def np_rref_gf(M: np.ndarray, p: int) -> tuple[int, list[int], np.ndarray]:
    A = M.astype(np.int64, copy=True) % p
    m, n = A.shape
    pivs: list[int] = []
    r = 0
    for c in range(n):
        if r >= m:
            break
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0:
            continue
        pr = r + int(nz[0])
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        col = A[:, c].copy()
        col[r] = 0
        rows = np.flatnonzero(col)
        if rows.size:
            A[rows] = (A[rows] - col[rows, None] * A[r]) % p
        pivs.append(c)
        r += 1
    return r, pivs, A


def np_null_gf(M: np.ndarray, p: int) -> tuple[int, np.ndarray]:
    m, n = M.shape
    rk, pivs, R = np_rref_gf(M, p)
    piv_set = set(pivs)
    free = [c for c in range(n) if c not in piv_set]
    Z = np.zeros((n, len(free)), dtype=np.int64)
    for j, fc in enumerate(free):
        Z[fc, j] = 1
        for row_i, pc in enumerate(pivs):
            Z[pc, j] = (-R[row_i, fc]) % p
    return rk, Z


def np_inv_gf(M: np.ndarray, p: int) -> np.ndarray:
    n = M.shape[0]
    aug = np.hstack([M % p, np.eye(n, dtype=np.int64)])
    rk, _, R = np_rref_gf(aug, p)
    if rk != n:
        raise RuntimeError("Singular matrix over GF(p)")
    return R[:, n:]


_W2_IDX_CACHE: dict[int, tuple[np.ndarray, np.ndarray]] = {}


def wedge2_gf(X: np.ndarray, p: int) -> np.ndarray:
    n = X.shape[0]
    if n not in _W2_IDX_CACHE:
        _W2_IDX_CACHE[n] = np.triu_indices(n, k=1)
    ii, jj = _W2_IDX_CACHE[n]
    return (X[np.ix_(ii, ii)] * X[np.ix_(jj, jj)] - X[np.ix_(ii, jj)] * X[np.ix_(jj, ii)]) % p


def fox_word_np_gf(mats: dict[str, np.ndarray], invs: dict[str, np.ndarray], w: str, p: int) -> tuple[np.ndarray, np.ndarray]:
    e = mats["a"].shape[0]
    idx = {"a": 0, "b": 1, "t": 2}
    out = np.zeros((e, 3 * e), dtype=np.int64)
    pre = np.eye(e, dtype=np.int64)
    for ch in w:
        if ch in "abt":
            off = idx[ch] * e
            out[:, off : off + e] = (out[:, off : off + e] + pre) % p
            pre = (pre @ mats[ch]) % p
        else:
            g = ch.lower()
            off = idx[g] * e
            pre = (pre @ invs[g]) % p
            out[:, off : off + e] = (out[:, off : off + e] - pre) % p
    return out, pre


def fox_steps_np_gf(mats: dict[str, np.ndarray], steps: list[str], p: int) -> np.ndarray:
    """Exact Fox Jacobian of [t a T psi(a)^-1, t b T psi(b)^-1] in O(|steps|) matrix products."""
    e = mats["a"].shape[0]
    I = np.eye(e, dtype=np.int64)
    Z0 = np.zeros((e, e), dtype=np.int64)
    Da_a, Db_a, Ra = I.copy(), Z0.copy(), mats["a"].copy()
    Da_b, Db_b, Rb = Z0.copy(), I.copy(), mats["b"].copy()
    for st in reversed(steps):
        if st == "L":
            Da_a = (Da_a + Ra @ Da_b) % p
            Db_a = (Db_a + Ra @ Db_b) % p
            Ra = (Ra @ Rb) % p
        elif st == "R":
            Da_b = (Da_b + Rb @ Da_a) % p
            Db_b = (Db_b + Rb @ Db_a) % p
            Rb = (Rb @ Ra) % p
        else:
            Rai = np_inv_gf(Ra, p)
            Rbi = np_inv_gf(Rb, p)
            Da_a, Db_a, Ra = (-Rai @ Da_a) % p, (-Rai @ Db_a) % p, Rai
            Da_b, Db_b, Rb = (-Rbi @ Da_b) % p, (-Rbi @ Db_b) % p, Rbi
    Mt = mats["t"]
    Mti = np_inv_gf(Mt, p)
    if not (np.array_equal((Mt @ mats["a"] @ Mti) % p, Ra) and np.array_equal((Mt @ mats["b"] @ Mti) % p, Rb)):
        sys.exit(2)
    return np.block([
        [(Mt - Da_a) % p, (-Db_a) % p, (I - Ra) % p],
        [(-Da_b) % p, (Mt - Db_b) % p, (I - Rb) % p],
    ])


def cohom_steps_np_gf(
    mats: dict[str, np.ndarray],
    invs: dict[str, np.ndarray],
    steps: list[str],
    ell_w: str,
    mu_w: str,
    p: int,
    want_cocs: bool = False,
    want_interior: bool = False,
) -> tuple[int, int, int, int, list[np.ndarray]]:
    e = mats["a"].shape[0]
    I = np.eye(e, dtype=np.int64)
    fox = fox_steps_np_gf(mats, steps, p)
    _, Z = np_null_gf(fox, p)
    dg = np.vstack([(mats[g] - I) % p for g in "abt"])
    r0 = np_rank_gf(dg, p)
    h0 = e - r0
    dimZ = Z.shape[1]
    h1 = dimZ - r0

    F1, W1 = fox_word_np_gf(mats, invs, ell_w, p)
    F2, W2 = fox_word_np_gf(mats, invs, mu_w, p)
    rowsR = np.vstack([F1, F2])
    BP = np.vstack([(W1 - I) % p, (W2 - I) % p])
    rBP = np_rank_gf(BP, p)
    if dimZ == 0:
        return h0, h1, 0, h1, []
    RZ = (rowsR @ Z) % p
    rboth = np_rank_gf(np.hstack([BP, RZ]), p)
    r1 = rboth - rBP
    n = h1 - r1

    if want_interior:
        if n == 0:
            return h0, h1, r1, 0, []
        _, K = np_null_gf(np.hstack([RZ, (-BP) % p]), p)
        I_cocs = (Z @ K[:dimZ, :]) % p
        cur = dg.T.copy()
        cur_rk = r0
        int_cocs: list[np.ndarray] = []
        for c in range(I_cocs.shape[1]):
            z = I_cocs[:, c]
            nrk = np_rank_gf(np.vstack([cur, z]), p)
            if nrk > cur_rk:
                cur = np.vstack([cur, z])
                cur_rk = nrk
                int_cocs.append(z)
        if len(int_cocs) != n:
            sys.exit(2)
        return h0, h1, r1, n, int_cocs

    if want_cocs:
        if h1 == 0:
            return h0, h1, r1, n, []
        cur = dg.T.copy()
        cur_rk = r0
        cocs: list[np.ndarray] = []
        for c in range(dimZ):
            z = Z[:, c]
            nrk = np_rank_gf(np.vstack([cur, z]), p)
            if nrk > cur_rk:
                cur = np.vstack([cur, z])
                cur_rk = nrk
                cocs.append(z)
        if len(cocs) != h1:
            sys.exit(2)
        return h0, h1, r1, n, cocs

    return h0, h1, r1, n, []


def verify_b1604_e1_duality_gf(
    mats: dict[str, np.ndarray],
    invs: dict[str, np.ndarray],
    steps: list[str],
    ell_w: str,
    mu_w: str,
    p: int,
) -> tuple[tuple[int, int, int, int], tuple[int, int, int, int]]:
    """Compute (h0, h1, r1, n) on E and E^* and assert B1604's E1 / B1297 duality identity."""
    t_E = cohom_steps_np_gf(mats, invs, steps, ell_w, mu_w, p)[:4]
    mats_s = {g: invs[g].T.copy() for g in "abt"}
    invs_s = {g: mats[g].T.copy() for g in "abt"}
    t_Es = cohom_steps_np_gf(mats_s, invs_s, steps, ell_w, mu_w, p)[:4]
    # Check peripheral H^0(dM; E^*) = t0(E^*):
    e = mats["a"].shape[0]
    I = np.eye(e, dtype=np.int64)
    _, W1s = fox_word_np_gf(mats_s, invs_s, ell_w, p)
    _, W2s = fox_word_np_gf(mats_s, invs_s, mu_w, p)
    BPs = np.vstack([(W1s - I) % p, (W2s - I) % p])
    t0_Es = e - np_rank_gf(BPs, p)
    # B1604 E1: h0(E) - h1(E) + n(E^*) + t0(E^*) - h0(E^*) == 0
    if (t_E[0] - t_E[1] + t_Es[3] + t0_Es - t_Es[0]) % 1 != 0 or (t_E[0] - t_E[1] + t_Es[3] + t0_Es - t_Es[0]) != 0:
        sys.exit(2)
    return t_E, t_Es


_SPIN_SETUP_CACHE: dict[int, dict[str, object]] = {}


def setup_spin_gf(p: int) -> dict[str, object]:
    if p in _SPIN_SETUP_CACHE:
        return _SPIN_SETUP_CACHE[p]
    if (p - 1) % 24 != 0:
        raise ValueError(f"Prime {p} is not 1 mod 24")
    zeta24 = next(
        pow(g, (p - 1) // 24, p)
        for g in range(2, p)
        if pow(g, (p - 1) // 2, p) != 1 and pow(g, (p - 1) // 3, p) != 1
    )
    zeta8 = pow(zeta24, 3, p)
    ii = pow(zeta8, 2, p)
    sq2 = (zeta8 + pow(zeta8, 7, p)) % p
    inv_sq2 = pow(sq2, p - 2, p)

    QA = np.array([[ii, 0], [0, (-ii) % p]], dtype=np.int64)
    QB = np.array([[0, 1], [p - 1, 0]], dtype=np.int64)
    UL = np.array([[inv_sq2, (-inv_sq2) % p], [inv_sq2, inv_sq2]], dtype=np.int64)
    UR = np.array([[((1 - ii) * inv_sq2) % p, 0], [0, ((1 + ii) * inv_sq2) % p]], dtype=np.int64)
    UN = (QA @ QB) % p
    UP = np.array([[(ii * inv_sq2) % p, inv_sq2], [(-inv_sq2) % p, (-ii * inv_sq2) % p]], dtype=np.int64)

    B3 = [QA, QB, UN]
    inv_m2 = pow(p - 2, p - 2, p)

    def ad3(U: np.ndarray) -> np.ndarray:
        Ui = np_inv_gf(U, p)
        M3 = np.zeros((3, 3), dtype=np.int64)
        for col in range(3):
            X = (U @ B3[col] @ Ui) % p
            for row in range(3):
                M3[row, col] = (int(np.trace(B3[row] @ X)) * inv_m2) % p
        return M3

    pars = [(1, 0), (0, 1), (1, 1)]
    bases = {}
    for par in pars:
        sa = p - 1 if par[0] else 1
        sb = p - 1 if par[1] else 1
        Ap = (sa * QA) % p
        Bp = (sb * QB) % p
        inv_ApI = np.array(
            [[pow(int((Ap[0, 0] - 1) % p), p - 2, p), 0], [0, pow(int((Ap[1, 1] - 1) % p), p - 2, p)]],
            dtype=np.int64,
        )
        bases[par] = (Ap, Bp, inv_ApI)

    def act_6d_step(step: str, U: np.ndarray) -> np.ndarray:
        M6 = np.zeros((6, 6), dtype=np.int64)
        Uinv = np_inv_gf(U, p)
        I2 = np.eye(2, dtype=np.int64)
        for src_idx, p_src in enumerate(pars):
            Ap, Bp, _ = bases[p_src]
            if step == "L":
                p_dst = ((p_src[0] + p_src[1]) % 2, p_src[1])
            elif step == "R":
                p_dst = (p_src[0], (p_src[0] + p_src[1]) % 2)
            elif step == "-":
                p_dst = p_src
            elif step == "P":
                p_dst = (p_src[1], p_src[0])
            else:
                raise ValueError(step)
            dst_idx = pars.index(p_dst)
            _, Bd, inv_AdI = bases[p_dst]
            Bpinv = np_inv_gf(Bp, p)
            for col in range(2):
                cb = np.array([1 if col == 0 else 0, 1 if col == 1 else 0], dtype=np.int64)
                if step == "L":
                    raw_a = (Ap @ cb) % p
                    raw_b = cb
                elif step == "R":
                    raw_a = np.zeros(2, dtype=np.int64)
                    raw_b = cb
                elif step == "-":
                    raw_a = np.zeros(2, dtype=np.int64)
                    raw_b = (-Bpinv @ cb) % p
                else:
                    raw_a = cb
                    raw_b = np.zeros(2, dtype=np.int64)
                na = (Uinv @ raw_a) % p
                nb = (Uinv @ raw_b) % p
                v = (-inv_AdI @ na) % p
                fb = (nb + ((Bd - I2) % p) @ v) % p
                M6[2 * dst_idx : 2 * dst_idx + 2, 2 * src_idx + col] = fb
        return M6

    SL = act_6d_step("L", UL)
    SR = act_6d_step("R", UR)
    SN = act_6d_step("-", UN)
    SP = act_6d_step("P", UP)

    def lift_steps_2d(steps: list[str], lift_idx: int = 0) -> np.ndarray:
        U = np.eye(2, dtype=np.int64)
        for st in steps:
            U = ((UL if st == "L" else UR if st == "R" else UN) @ U) % p
        if lift_idx == 1:
            U = ((p - 1) * U) % p
        return U

    def act_steps_6d(steps: list[str], lift_idx: int = 0) -> np.ndarray:
        # S(f2 o f1) = S(f1) @ S(f2):
        S = np.eye(6, dtype=np.int64)
        for st in steps:
            S = (S @ (SL if st == "L" else SR if st == "R" else SN)) % p
        if lift_idx == 1:
            S = ((p - 1) * S) % p
        return S

    obj = {
        "p": p,
        "zeta24": zeta24,
        "zeta8": zeta8,
        "ii": ii,
        "QA": QA,
        "QB": QB,
        "QAi": np_inv_gf(QA, p),
        "QBi": np_inv_gf(QB, p),
        "UL": UL,
        "UR": UR,
        "UN": UN,
        "UP": UP,
        "PA": ad3(QA),
        "PB": ad3(QB),
        "PAi": np_inv_gf(ad3(QA), p),
        "PBi": np_inv_gf(ad3(QB), p),
        "ad3": ad3,
        "SL": SL,
        "SR": SR,
        "SN": SN,
        "SP": SP,
        "lift_steps_2d": lift_steps_2d,
        "act_steps_6d": act_steps_6d,
    }
    _SPIN_SETUP_CACHE[p] = obj
    return obj


# ---------------------------------------------------------------------------
# 3. High-precision hyperbolic holonomies, finite covers, and gmpy2 cohomology
# ---------------------------------------------------------------------------

_ROOTS_CACHE: dict[str, list[tuple[complex, complex, complex]]] = {}
_HOL_CACHE: dict[str, dict[str, object]] = {}


def _eval_fricke_c(word: str, xv: complex, yv: complex, zv: complex) -> tuple[complex, complex, complex, complex]:
    A_, B_, C_ = xv, yv, zv
    for ch in word:
        if ch == "L":
            A_, B_, C_ = C_, B_, B_ * C_ - A_
        else:
            A_, B_, C_ = A_, C_, A_ * C_ - B_
    return A_ - xv, B_ - yv, xv * xv + yv * yv + zv * zv - xv * yv * zv, C_ - zv


def _find_markov_roots(word: str) -> list[tuple[complex, complex, complex]]:
    if word in _ROOTS_CACHE:
        return _ROOTS_CACHE[word]
    xs, ys, zs = sp.symbols("x y z")
    A_, B_, C_ = xs, ys, zs
    for ch in word:
        if ch == "L":
            A_, B_, C_ = C_, B_, sp.expand(B_ * C_ - A_)
        else:
            A_, B_, C_ = A_, C_, sp.expand(A_ * C_ - B_)
    gb = sp.groebner([A_ - xs, B_ - ys, xs**2 + ys**2 + zs**2 - xs * ys * zs, C_ - zs], xs, ys, zs, order="lex")
    exprs = list(gb.exprs)
    pz = sp.Poly(exprs[-1], zs).sqf_part()
    y_polys = [e for e in exprs[:-1] if xs not in e.free_symbols and ys in e.free_symbols]
    roots: list[tuple[complex, complex, complex]] = []
    for zr in pz.nroots(n=35, maxsteps=300):
        if abs(complex(zr)) < 1e-7:
            continue
        y_cands = []
        for yp in y_polys:
            ev_y = yp.evalf(35, subs={zs: zr})
            if ys in ev_y.free_symbols:
                py_sub = sp.Poly(ev_y, ys)
                if abs(complex(py_sub.LC())) > 1e-7:
                    y_cands.append((py_sub.degree(), py_sub))
        y_cands.sort(key=lambda t: t[0])
        py_sub = y_cands[0][1]
        for yr in py_sub.nroots(n=35, maxsteps=300):
            yc, zc = complex(yr), complex(zr)
            disc = cmath.sqrt((yc * zc) ** 2 - 4.0 * (yc * yc + zc * zc))
            for xc in ((yc * zc + disc) / 2.0, (yc * zc - disc) / 2.0):
                if abs(xc.imag) + abs(yc.imag) + abs(zc.imag) < 1e-6:
                    continue
                f0, f1, f2, f3 = _eval_fricke_c(word, xc, yc, zc)
                scale = max(1.0, abs(xc) ** len(word), abs(yc) ** len(word), abs(zc) ** len(word))
                if (abs(f0) + abs(f1) + abs(f2) + abs(f3)) / scale < 1e-4:
                    if not any(abs(xc - rx) + abs(yc - ry) + abs(zc - rz) < 1e-4 for rx, ry, rz in roots):
                        roots.append((xc, yc, zc))
    _ROOTS_CACHE[word] = roots
    return roots


def _mp_to_gm(z: mp.mpc | mp.mpf) -> gmpy2.mpc:
    rz = gmpy2.mpfr(mp.nstr(mp.re(z), 95) or "0")
    iz = gmpy2.mpfr(mp.nstr(mp.im(z), 95) or "0")
    return gmpy2.mpc(rz, iz)


def sl2_inv_mp(g: mp.matrix) -> mp.matrix:
    return mp.matrix([[g[1, 1], -g[0, 1]], [-g[1, 0], g[0, 0]]])


def two_mp_to_gm(g: mp.matrix) -> GMMat:
    return [[_mp_to_gm(g[i, j]) for j in range(2)] for i in range(2)]


def four_mp_to_gm(g: mp.matrix) -> GMMat:
    E = [
        mp.matrix([[1, 0], [0, 0]]),
        mp.matrix([[0, 0], [0, 1]]),
        mp.matrix([[0, 1], [1, 0]]),
        mp.matrix([[0, 1j], [-1j, 0]]),
    ]
    gs = g.transpose_conj()
    M4 = mp.matrix(4, 4)
    for col_k, Ek in enumerate(E):
        X = g * Ek * gs
        vals = [mp.re(X[0, 0]), mp.re(X[1, 1]), mp.re(X[0, 1]), mp.im(X[0, 1])]
        for row_i in range(4):
            M4[row_i, col_k] = vals[row_i]
    return [[_mp_to_gm(M4[i, j]) for j in range(4)] for i in range(4)]


def _solve_T_mp(A: mp.matrix, B: mp.matrix, pa: mp.matrix, pb: mp.matrix) -> mp.matrix | None:
    Sys = mp.matrix(8, 4)
    for eq_idx, (X1, X2) in enumerate([(A, pa), (B, pb)]):
        for i in range(2):
            for j in range(2):
                r = eq_idx * 4 + i * 2 + j
                for k in range(2):
                    Sys[r, i * 2 + k] += X1[k, j]
                    Sys[r, k * 2 + j] -= X2[i, k]
    best_t, best_res = None, mp.mpf("1")
    for fix in range(4):
        cols = [c for c in range(4) if c != fix]
        Sub, rhs = mp.matrix(8, 3), mp.matrix(8, 1)
        for r in range(8):
            rhs[r, 0] = -Sys[r, fix]
            for ci, c in enumerate(cols):
                Sub[r, ci] = Sys[r, c]
        SH = Sub.transpose_conj()
        try:
            sol = mp.lu_solve(SH * Sub, SH * rhs)
        except Exception:
            continue
        vec = [mp.mpc(0)] * 4
        vec[fix] = mp.mpc(1)
        for ci, c in enumerate(cols):
            vec[c] = sol[ci, 0]
        res = max(abs(sum(Sys[r, c] * vec[c] for c in range(4))) for r in range(8))
        if res < best_res:
            best_res, best_t = res, vec
    sys_scale = max(mp.mpf(1), max(abs(Sys[r, c]) for r in range(8) for c in range(4)))
    if best_t is None or best_res > mp.mpf("1e-110") * sys_scale:
        return None
    T0 = mp.matrix([[best_t[0], best_t[1]], [best_t[2], best_t[3]]])
    detT = T0[0, 0] * T0[1, 1] - T0[0, 1] * T0[1, 0]
    if abs(detT) < mp.mpf("1e-20"):
        return None
    return T0 / mp.sqrt(detT)


def get_holonomy(sign: str, word: str) -> dict[str, object]:
    key = sign + word
    if key in _HOL_CACHE:
        return _HOL_CACHE[key]
    sh = complex(snappy.Manifold(("b++" if sign == "+" else "b+-") + word).cusp_info("shape")[0])
    img = phi1_words(sign, word)
    for rx, ry, rz in _find_markov_roots(word):
        xv, yv, zv = mp.mpc(rx), mp.mpc(ry), mp.mpc(rz)

        def ev_jet(xx: mp.mpc, yy: mp.mpc, zz: mp.mpc) -> tuple[list[mp.mpc], mp.matrix]:
            z0, one = mp.mpc(0), mp.mpc(1)
            A_ = (xx, one, z0, z0)
            B_ = (yy, z0, one, z0)
            C_ = (zz, z0, z0, one)

            def jmul(u: tuple[mp.mpc, ...], v: tuple[mp.mpc, ...]) -> tuple[mp.mpc, ...]:
                return (
                    u[0] * v[0],
                    u[1] * v[0] + u[0] * v[1],
                    u[2] * v[0] + u[0] * v[2],
                    u[3] * v[0] + u[0] * v[3],
                )

            def jsub(u: tuple[mp.mpc, ...], v: tuple[mp.mpc, ...]) -> tuple[mp.mpc, ...]:
                return (u[0] - v[0], u[1] - v[1], u[2] - v[2], u[3] - v[3])

            for ch in word:
                if ch == "L":
                    A_, B_, C_ = C_, B_, jsub(jmul(B_, C_), A_)
                else:
                    A_, B_, C_ = A_, C_, jsub(jmul(A_, C_), B_)
            r0 = (A_[0] - xx, A_[1] - one, A_[2], A_[3])
            r1 = (B_[0] - yy, B_[1], B_[2] - one, B_[3])
            r2 = (
                xx * xx + yy * yy + zz * zz - xx * yy * zz,
                2 * xx - yy * zz,
                2 * yy - xx * zz,
                2 * zz - xx * yy,
            )
            return [r0[0], r1[0], r2[0]], mp.matrix([[r0[1], r0[2], r0[3]], [r1[1], r1[2], r1[3]], [r2[1], r2[2], r2[3]]])

        ok = True
        for _ in range(30):
            f0, J = ev_jet(xv, yv, zv)
            if max(abs(t) for t in f0) < mp.mpf("1e-145"):
                break
            try:
                delta = mp.lu_solve(J, mp.matrix([[-f0[0]], [-f0[1]], [-f0[2]]]))
            except Exception:
                ok = False
                break
            xv += delta[0]
            yv += delta[1]
            zv += delta[2]
        f_chk, _ = ev_jet(xv, yv, zv)
        if not ok or max(abs(t) for t in f_chk) > mp.mpf("1e-135"):
            continue

        A = mp.matrix([[xv, 1], [-1, 0]])
        beta = (-zv + mp.sqrt(zv * zv - 4)) / 2
        B = mp.matrix([[0, beta], [-1 / beta, yv]])
        M0 = {"a": A, "b": B, "A": sl2_inv_mp(A), "B": sl2_inv_mp(B)}

        def wm(w: str) -> mp.matrix:
            R = mp.eye(2)
            for c in w:
                R = R * M0[c]
            return R

        T = _solve_T_mp(A, B, wm(img["a"]), wm(img["b"]))
        if T is None:
            continue
        ell = wm("abAB")
        tp = T if sign == "+" else A * B * T
        sl = 1 if mp.re(ell[0, 0] + ell[1, 1]) > 0 else -1
        Nl = ell - sl * mp.eye(2)
        u0, v0 = (Nl[0, 1], -Nl[0, 0]) if abs(Nl[0, 0]) + abs(Nl[0, 1]) >= abs(Nl[1, 0]) + abs(Nl[1, 1]) else (-Nl[1, 1], Nl[1, 0])
        nrm2 = abs(u0) ** 2 + abs(v0) ** 2
        Pmat = mp.matrix([[u0, -mp.conj(v0) / nrm2], [v0, mp.conj(u0) / nrm2]])
        Pinv = mp.inverse(Pmat)
        ell_u, tp_u = Pinv * ell * Pmat, Pinv * tp * Pmat
        st = 1 if mp.re(tp_u[0, 0] + tp_u[1, 1]) > 0 else -1
        if abs(tp_u[1, 0]) > mp.mpf("1e-110") or abs(tp_u[0, 0] - st) > mp.mpf("1e-110"):
            continue
        tau = (st * tp_u[0, 1]) / (sl * ell_u[0, 1])
        if abs(abs(float(mp.im(tau))) - abs(sh.imag)) < 1e-7:
            t_re = float(mp.re(tau))
            if any(abs((t_re + e * sh.real) - round(t_re + e * sh.real)) < 1e-7 for e in (1, -1)) and mp.im(tau) > 0:
                Ai, Bi, Ti = sl2_inv_mp(A), sl2_inv_mp(B), sl2_inv_mp(T)
                res_obj = {
                    "A_mp": A,
                    "B_mp": B,
                    "T_mp": T,
                    "gm2": {"a": two_mp_to_gm(A), "b": two_mp_to_gm(B), "t": two_mp_to_gm(T)},
                    "gm2_inv": {"a": two_mp_to_gm(Ai), "b": two_mp_to_gm(Bi), "t": two_mp_to_gm(Ti)},
                    "gm4": {"a": four_mp_to_gm(A), "b": four_mp_to_gm(B), "t": four_mp_to_gm(T)},
                    "gm4_inv": {"a": four_mp_to_gm(Ai), "b": four_mp_to_gm(Bi), "t": four_mp_to_gm(Ti)},
                }
                _HOL_CACHE[key] = res_obj
                return res_obj
    raise RuntimeError(f"Could not locate hyperbolic holonomy for {key}")


def gm_matmul(A: GMMat, B: GMMat) -> GMMat:
    m = len(A)
    if m == 0:
        return []
    p_dim = len(B)
    n = len(B[0]) if p_dim > 0 else 0
    z0 = gmpy2.mpc(0)
    out = [[z0] * n for _ in range(m)]
    for i in range(m):
        Ai, oi = A[i], out[i]
        for k in range(p_dim):
            aik = Ai[k]
            if aik != 0:
                Bk = B[k]
                for j in range(n):
                    bkj = Bk[j]
                    if bkj != 0:
                        oi[j] += aik * bkj
    return out


def gm_add(A: GMMat, B: GMMat) -> GMMat:
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def gm_sub(A: GMMat, B: GMMat) -> GMMat:
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def gm_neg(M: GMMat) -> GMMat:
    return [[-x for x in row] for row in M]


def gm_scale(sc: gmpy2.mpc, M: GMMat) -> GMMat:
    return [[sc * x for x in row] for row in M]


def gm_transpose(M: GMMat) -> GMMat:
    if not M:
        return []
    m, n = len(M), len(M[0])
    return [[M[i][j] for i in range(m)] for j in range(n)]


def gm_hstack(A: GMMat, B: GMMat) -> GMMat:
    return [ra + rb for ra, rb in zip(A, B)]


def gm_kron(A: GMMat, B: GMMat) -> GMMat:
    ma, na = len(A), len(A[0])
    mb, nb = len(B), len(B[0])
    z0 = gmpy2.mpc(0)
    out = [[z0] * (na * nb) for _ in range(ma * mb)]
    for i in range(ma):
        for j in range(na):
            aij = A[i][j]
            if aij != 0:
                for r in range(mb):
                    for c in range(nb):
                        out[i * mb + r][j * nb + c] = aij * B[r][c]
    return out


def gm_roots_of_unity(m_order: int) -> list[gmpy2.mpc]:
    out: list[gmpy2.mpc] = []
    for k in range(m_order):
        ang = 2 * mp.pi * mp.mpf(k) / mp.mpf(m_order)
        out.append(_mp_to_gm(mp.cos(ang) + 1j * mp.sin(ang)))
    return out


def gm_rank_and_nullspace(M: GMMat, m_rows: int, n_cols: int, want_null: bool = False) -> tuple[int, GMMat]:
    z0, one = gmpy2.mpc(0), gmpy2.mpc(1)
    if m_rows == 0 or n_cols == 0:
        if want_null:
            return 0, [[one if i == j else z0 for j in range(n_cols)] for i in range(n_cols)]
        return 0, []
    entry_max = gmpy2.mpfr(0)
    for r in range(m_rows):
        for x in M[r]:
            av = abs(x)
            if av > entry_max:
                entry_max = av
    if entry_max < gmpy2.mpfr("1e-70"):
        if want_null:
            return 0, [[one if i == j else z0 for j in range(n_cols)] for i in range(n_cols)]
        return 0, []

    hi_thr = gmpy2.mpfr("1e-25") * entry_max
    lo_thr = gmpy2.mpfr("1e-60") * entry_max
    A = [row[:] for row in M]
    col_perm = list(range(n_cols))
    rk = 0
    limit = min(m_rows, n_cols)
    while rk < limit:
        pr = max(range(rk, m_rows), key=lambda r: abs(A[r][rk]))
        pval = abs(A[pr][rk])
        pc = rk
        if pval < hi_thr:
            best_v = gmpy2.mpfr(-1)
            for r in range(rk, m_rows):
                row_r = A[r]
                for c in range(rk, n_cols):
                    av = abs(row_r[c])
                    if av > best_v:
                        best_v = av
                        pr, pc = r, c
            pval = best_v
            if pval <= lo_thr:
                break
            if pval < hi_thr:
                sys.exit(2)
        if pr != rk:
            A[rk], A[pr] = A[pr], A[rk]
        if pc != rk:
            col_perm[rk], col_perm[pc] = col_perm[pc], col_perm[rk]
            for r in range(m_rows):
                A[r][rk], A[r][pc] = A[r][pc], A[r][rk]
        inv_piv = one / A[rk][rk]
        piv_row = A[rk]
        piv_row[rk] = one
        for c in range(rk + 1, n_cols):
            if piv_row[c] != 0:
                piv_row[c] *= inv_piv
        nz_cols = [c for c in range(rk + 1, n_cols) if piv_row[c] != 0]
        r_iter = range(m_rows) if want_null else range(rk + 1, m_rows)
        for r in r_iter:
            if r == rk:
                continue
            fac = A[r][rk]
            if fac != 0:
                A[r][rk] = z0
                for c in nz_cols:
                    A[r][c] -= fac * piv_row[c]
        rk += 1
    if not want_null:
        return rk, []
    dim_null = n_cols - rk
    Z = [[z0] * dim_null for _ in range(n_cols)]
    for f_idx in range(rk, n_cols):
        col_num = f_idx - rk
        Z[col_perm[f_idx]][col_num] = one
        for i in range(rk):
            Z[col_perm[i]][col_num] = -A[i][f_idx]
    return rk, Z


def gm_inv(M: GMMat) -> GMMat:
    n = len(M)
    z0, one = gmpy2.mpc(0), gmpy2.mpc(1)
    aug = [M[i][:] + [one if i == j else z0 for j in range(n)] for i in range(n)]
    for rk in range(n):
        pr = max(range(rk, n), key=lambda r: abs(aug[r][rk]))
        aug[rk], aug[pr] = aug[pr], aug[rk]
        inv_p = one / aug[rk][rk]
        aug[rk] = [x * inv_p for x in aug[rk]]
        for r in range(n):
            if r != rk and aug[r][rk] != 0:
                fac = aug[r][rk]
                aug[r] = [aug[r][c] - fac * aug[rk][c] for c in range(2 * n)]
    return [row[n:] for row in aug]


def fox_word_gm(mats: dict[str, GMMat], invs: dict[str, GMMat], w: str) -> tuple[GMMat, GMMat]:
    e = len(mats["a"])
    z0, one = gmpy2.mpc(0), gmpy2.mpc(1)
    idx = {"a": 0, "b": 1, "t": 2}
    out = [[z0] * (3 * e) for _ in range(e)]
    pre = [[one if i == j else z0 for j in range(e)] for i in range(e)]
    for ch in w:
        if ch in "abt":
            off = idx[ch] * e
            for r in range(e):
                for c in range(e):
                    out[r][off + c] += pre[r][c]
            pre = gm_matmul(pre, mats[ch])
        else:
            g = ch.lower()
            off = idx[g] * e
            pre = gm_matmul(pre, invs[g])
            for r in range(e):
                for c in range(e):
                    out[r][off + c] -= pre[r][c]
    return out, pre


def cohom_steps_gm(mats: dict[str, GMMat], invs: dict[str, GMMat], steps: list[str], ell_w: str, mu_w: str) -> tuple[int, int, int, int, int]:
    """High-precision Fox cohomology via O(|steps|) product rule; returns (h0, h1, r1, n, h0_torus)."""
    e = len(mats["a"])
    z0, one = gmpy2.mpc(0), gmpy2.mpc(1)
    I = [[one if i == j else z0 for j in range(e)] for i in range(e)]
    Z0 = [[z0] * e for _ in range(e)]
    Da_a, Db_a, Ra = [r[:] for r in I], [r[:] for r in Z0], [r[:] for r in mats["a"]]
    Da_b, Db_b, Rb = [r[:] for r in Z0], [r[:] for r in I], [r[:] for r in mats["b"]]
    for st in reversed(steps):
        if st == "L":
            Da_a = gm_add(Da_a, gm_matmul(Ra, Da_b))
            Db_a = gm_add(Db_a, gm_matmul(Ra, Db_b))
            Ra = gm_matmul(Ra, Rb)
        elif st == "R":
            Da_b = gm_add(Da_b, gm_matmul(Rb, Da_a))
            Db_b = gm_add(Db_b, gm_matmul(Rb, Db_a))
            Rb = gm_matmul(Rb, Ra)
        else:
            Rai = gm_inv(Ra)
            Rbi = gm_inv(Rb)
            Da_a, Db_a, Ra = gm_neg(gm_matmul(Rai, Da_a)), gm_neg(gm_matmul(Rai, Db_a)), Rai
            Da_b, Db_b, Rb = gm_neg(gm_matmul(Rbi, Da_b)), gm_neg(gm_matmul(Rbi, Db_b)), Rbi

    Mt, Mti = mats["t"], invs["t"]
    chk_a = gm_sub(gm_matmul(gm_matmul(Mt, mats["a"]), Mti), Ra)
    chk_b = gm_sub(gm_matmul(gm_matmul(Mt, mats["b"]), Mti), Rb)
    if max(abs(x) for row in chk_a + chk_b for x in row) > gmpy2.mpfr("1e-55"):
        sys.exit(2)

    fox = gm_hstack(gm_hstack(gm_sub(Mt, Da_a), gm_neg(Db_a)), gm_sub(I, Ra)) + \
          gm_hstack(gm_hstack(gm_neg(Da_b), gm_sub(Mt, Db_b)), gm_sub(I, Rb))

    rk, Z = gm_rank_and_nullspace(fox, 2 * e, 3 * e, want_null=True)
    dg = gm_sub(mats["a"], I) + gm_sub(mats["b"], I) + gm_sub(mats["t"], I)
    r0, _ = gm_rank_and_nullspace(dg, 3 * e, e, want_null=False)
    h0 = e - r0
    dimZ = 3 * e - rk
    h1 = dimZ - r0

    F1, W1 = fox_word_gm(mats, invs, ell_w)
    F2, W2 = fox_word_gm(mats, invs, mu_w)
    rowsR = F1 + F2
    BP = gm_sub(W1, I) + gm_sub(W2, I)
    rBP, _ = gm_rank_and_nullspace(BP, 2 * e, e, want_null=False)
    h0_torus = e - rBP
    if dimZ == 0:
        return h0, h1, 0, h1, h0_torus
    RZ = gm_matmul(rowsR, Z)
    rboth, _ = gm_rank_and_nullspace(gm_hstack(BP, RZ), 2 * e, e + dimZ, want_null=False)
    r1 = rboth - rBP
    return h0, h1, r1, h1 - r1, h0_torus


# Finite cover helpers for Row 924 I1 (m135) and Row 925 (+LLLR A_4 cover)
def build_cover(sign: str, word: str, d: int, act_abt: dict[str, list[int]]) -> dict[str, object]:
    img = phi1_words(sign, word)
    act: dict[str, list[int]] = {}
    for g in "abt":
        p_arr = list(act_abt[g])
        pinv = [0] * d
        for i, j in enumerate(p_arr):
            pinv[j] = i
        act[g] = p_arr
        act[g.upper()] = pinv

    u: dict[int, str] = {0: ""}
    q = deque([0])
    while q:
        x = q.popleft()
        for g in "abtABT":
            y = act[g][x]
            if y not in u:
                u[y] = u[x] + g
                q.append(y)
    if len(u) != d:
        raise RuntimeError("Non-transitive cover")

    gen_idx: dict[tuple[int, str], int | None] = {}
    gen_words: list[str] = []
    for x in range(d):
        for g in "abt":
            y = act[g][x]
            w = red_w(u[x] + g + inv_w(u[y]))
            if w == "":
                gen_idx[(x, g)] = None
            else:
                gen_idx[(x, g)] = len(gen_words)
                gen_words.append(w)
    ng = len(gen_words)

    def rewrite_from(x0: int, w: str) -> tuple[list[tuple[int, int]], int]:
        x = x0
        out: list[tuple[int, int]] = []
        for c in w:
            if c in "abt":
                idx = gen_idx[(x, c)]
                if idx is not None:
                    out.append((idx, 1))
                x = act[c][x]
            else:
                y = act[c][x]
                idx = gen_idx[(y, c.lower())]
                if idx is not None:
                    out.append((idx, -1))
                x = y
        return out, x

    rels_gamma = ["taT" + inv_w(img["a"]), "tbT" + inv_w(img["b"])]
    rels_idx: list[list[tuple[int, int]]] = []
    rel_mat = np.zeros((2 * d, ng), dtype=np.int64)
    for x in range(d):
        for ri, rw in enumerate(rels_gamma):
            sw, xend = rewrite_from(x, rw)
            assert xend == x
            rels_idx.append(sw)
            for idx, sgn in sw:
                rel_mat[2 * x + ri, idx] += sgn

    ell_w = "abAB"
    tp_w = "t" if sign == "+" else "abt"
    seen_c: set[int] = set()
    cusps_idx: list[tuple[list[tuple[int, int]], list[tuple[int, int]]]] = []
    for x0 in range(d):
        if x0 in seen_c:
            continue
        orb: set[int] = set()
        stack = [x0]
        while stack:
            z = stack.pop()
            if z in orb:
                continue
            orb.add(z)
            for pw in (ell_w, tp_w):
                _, z2 = rewrite_from(z, pw)
                if z2 not in orb:
                    stack.append(z2)
        seen_c |= orb
        p_pow = 1
        while True:
            sw1, xe = rewrite_from(x0, ell_w * p_pow)
            if xe == x0:
                break
            p_pow += 1
        q_pow, found_sw2 = 1, None
        while True:
            for r_pow in range(p_pow):
                sw2, xe = rewrite_from(x0, (tp_w * q_pow) + (ell_w * r_pow))
                if xe == x0:
                    found_sw2 = sw2
                    break
            if found_sw2 is not None:
                break
            q_pow += 1
        cusps_idx.append((sw1, found_sw2))

    return {
        "ng": ng,
        "gen_words": gen_words,
        "rels_idx": rels_idx,
        "rel_mat": rel_mat,
        "cusps_idx": cusps_idx,
    }


def cover_characters(cov: dict[str, object], m: int) -> list[np.ndarray]:
    ng = int(cov["ng"])
    D_snf, _, V_snf = smith_normal_decomp(sp.Matrix(cov["rel_mat"].tolist()))
    V_np = np.array(V_snf.tolist(), dtype=np.int64) % m
    diag = [abs(int(D_snf[i, i])) for i in range(min(D_snf.rows, D_snf.cols))]
    choices_per_coord: list[list[int]] = []
    active_cols: list[int] = []
    for i in range(ng):
        di = diag[i] if i < len(diag) else 0
        g = math.gcd(di, m) if di != 0 else m
        if g > 1:
            choices_per_coord.append(list(range(0, m, m // g)))
            active_cols.append(i)
    if not active_cols:
        return [np.zeros(ng, dtype=np.int64)]
    B_sub = V_np[:, active_cols] % m
    return [(B_sub @ np.array(tup, dtype=np.int64)) % m for tup in itertools.product(*choices_per_coord)]


def fox_pres_gm(mod_mats: list[GMMat], mod_invs: list[GMMat], w_idx_sgn: list[tuple[int, int]]) -> tuple[GMMat, GMMat]:
    e = len(mod_mats[0])
    ng = len(mod_mats)
    z0, one = gmpy2.mpc(0), gmpy2.mpc(1)
    out = [[z0] * (ng * e) for _ in range(e)]
    pre = [[one if i == j else z0 for j in range(e)] for i in range(e)]
    for j, sgn in w_idx_sgn:
        off = j * e
        if sgn == 1:
            for r in range(e):
                for c in range(e):
                    out[r][off + c] += pre[r][c]
            pre = gm_matmul(pre, mod_mats[j])
        else:
            pre = gm_matmul(pre, mod_invs[j])
            for r in range(e):
                for c in range(e):
                    out[r][off + c] -= pre[r][c]
    return out, pre


def cohom_pres_gm(
    mod_mats: list[GMMat],
    mod_invs: list[GMMat],
    rels_idx: list[list[tuple[int, int]]],
    cusps_idx: list[tuple[list[tuple[int, int]], list[tuple[int, int]]]],
    want_interior: bool = False,
) -> tuple[int, int, int, int, GMMat | None]:
    e = len(mod_mats[0])
    ng = len(mod_mats)
    z0, one = gmpy2.mpc(0), gmpy2.mpc(1)
    fox: GMMat = []
    for r in rels_idx:
        fr, wr = fox_pres_gm(mod_mats, mod_invs, r)
        fox.extend(fr)
    rk, Z = gm_rank_and_nullspace(fox, len(fox), ng * e, want_null=True)
    dg: GMMat = []
    for m in mod_mats:
        for i in range(e):
            dg.append([m[i][j] - (one if i == j else z0) for j in range(e)])
    r0, _ = gm_rank_and_nullspace(dg, ng * e, e, want_null=False)
    h0 = e - r0
    dimZ = ng * e - rk
    h1 = dimZ - r0

    rowsR: GMMat = []
    nc = len(cusps_idx)
    BP = [[z0] * (e * nc) for _ in range(2 * e * nc)]
    for ci, (w1, w2) in enumerate(cusps_idx):
        F1, W1 = fox_pres_gm(mod_mats, mod_invs, w1)
        F2, W2 = fox_pres_gm(mod_mats, mod_invs, w2)
        rowsR.extend(F1)
        rowsR.extend(F2)
        for i in range(e):
            for j in range(e):
                BP[2 * e * ci + i][e * ci + j] = W1[i][j] - (one if i == j else z0)
                BP[2 * e * ci + e + i][e * ci + j] = W2[i][j] - (one if i == j else z0)
    rBP, _ = gm_rank_and_nullspace(BP, 2 * e * nc, e * nc, want_null=False)
    RZ = gm_matmul(rowsR, Z) if dimZ > 0 else [[z0] * 0 for _ in range(2 * e * nc)]
    rboth, _ = gm_rank_and_nullspace(gm_hstack(BP, RZ), 2 * e * nc, e * nc + dimZ, want_null=False) if dimZ > 0 else (rBP, [])
    r1 = rboth - rBP
    n = h1 - r1
    if not want_interior or n == 0:
        return h0, h1, r1, n, None
    _, K = gm_rank_and_nullspace(gm_hstack(RZ, gm_neg(BP)), 2 * e * nc, dimZ + e * nc, want_null=True)
    I_cocs = gm_matmul(Z, K[:dimZ])
    dim_vec = ng * e

    def vdot(u_v: list[gmpy2.mpc], v_v: list[gmpy2.mpc]) -> gmpy2.mpc:
        s = z0
        for ui, vi in zip(u_v, v_v):
            if ui != 0 and vi != 0:
                s += ui.conjugate() * vi
        return s

    b_vecs: list[list[gmpy2.mpc]] = []
    for c in range(e):
        v = [dg[r][c] for r in range(dim_vec)]
        for bv in b_vecs:
            pr = vdot(bv, v)
            v = [vi - pr * bi for vi, bi in zip(v, bv)]
        nrm = gmpy2.sqrt(vdot(v, v).real)
        if nrm > gmpy2.mpfr("1e-30"):
            b_vecs.append([vi / nrm for vi in v])
    int_vecs: list[list[gmpy2.mpc]] = []
    for c in range(len(I_cocs[0])):
        v = [I_cocs[r][c] for r in range(dim_vec)]
        for bv in b_vecs:
            pr = vdot(bv, v)
            v = [vi - pr * bi for vi, bi in zip(v, bv)]
        for iv in int_vecs:
            pr = vdot(iv, v)
            v = [vi - pr * ii for vi, ii in zip(v, iv)]
        nrm = gmpy2.sqrt(vdot(v, v).real)
        if nrm > gmpy2.mpfr("1e-30"):
            int_vecs.append([vi / nrm for vi in v])
    if len(int_vecs) != n:
        sys.exit(2)
    return h0, h1, r1, n, [[int_vecs[c][r] for c in range(n)] for r in range(dim_vec)]


def wedge2_gm(X: GMMat) -> GMMat:
    n = len(X)
    idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
    m = len(idx)
    z0 = gmpy2.mpc(0)
    W = [[z0] * m for _ in range(m)]
    for r, (i, j) in enumerate(idx):
        Xi, Xj = X[i], X[j]
        for c, (k, l) in enumerate(idx):
            W[r][c] = Xi[k] * Xj[l] - Xi[l] * Xj[k]
    return W


# ---------------------------------------------------------------------------
# 4. Shared algebraic solvers for W14 (slope law) and W16 (number-field ideals)
# ---------------------------------------------------------------------------

def slope_table_and_census(sign: str, word: str) -> dict[str, object]:
    """Exact tick-3 slope table over 3 independent primes > 10^9 and complete F-CI census."""
    img1 = phi1_words(sign, word)
    M1 = hom_mat(img1)
    tr1 = M1[0][0] + M1[1][1]
    steps3, mu3, img3 = steps_route2(sign, word, 3)
    u3 = extract_u(img3)
    M3 = hom_mat(img3)
    A_ab = sp.Matrix([[M3[0][0] - 1, M3[1][0]], [M3[0][1], M3[1][1] - 1]])
    D, _, V = smith_normal_decomp(A_ab)
    d0, d1 = abs(int(D[0, 0])), abs(int(D[1, 1]))
    ordG = d0 * d1
    if ordG != abs(tr1 - 2) * (tr1 + 1) ** 2:
        sys.exit(2)
    expG = math.lcm(d0, d1)

    primes: list[int] = []
    q_cand = ((10**9 // expG) + 1) * expG + 1
    while len(primes) < 3:
        if sp.isprime(q_cand):
            primes.append(q_cand)
        q_cand += expG

    V_mat = [[int(V[i, j]) for j in range(2)] for i in range(2)]
    chars: list[tuple[int, int]] = []
    for c0 in range(d0):
        z0 = c0 * (expG // d0)
        for c1 in range(d1):
            z1 = c1 * (expG // d1)
            ea = (V_mat[0][0] * z0 + V_mat[0][1] * z1) % expG
            eb = (V_mat[1][0] * z0 + V_mat[1][1] * z1) % expG
            chars.append((ea, eb))
    char_idx = {ch: i for i, ch in enumerate(chars)}
    zero_i = char_idx[(0, 0)]
    pfacs = list(sp.factorint(expG).keys())

    def slopes_for_prime(p: int) -> tuple[list[int | None], int, list[list[int] | None]]:
        zeta = next(
            pow(g, (p - 1) // expG, p)
            for g in range(2, p)
            if all(pow(g, (p - 1) // f, p) != 1 for f in pfacs)
        )
        s_arr: list[int | None] = [None] * ordG
        c_arr: list[list[int] | None] = [None] * ordG
        for i, (ea, eb) in enumerate(chars):
            if i == zero_i:
                continue
            va, vb = pow(zeta, ea, p), pow(zeta, eb, p)
            ca, cb = va, vb
            J00, J01, J10, J11 = 1, 0, 0, 1
            for st in reversed(steps3):
                if st == "L":
                    na, nb = (ca * cb) % p, cb
                    s00, s01, s10, s11 = 1, ca, 0, 1
                elif st == "R":
                    na, nb = ca, (cb * ca) % p
                    s00, s01, s10, s11 = 1, 0, cb, 1
                else:
                    cai, cbi = pow(ca, p - 2, p), pow(cb, p - 2, p)
                    na, nb = cai, cbi
                    s00, s01, s10, s11 = (-cai) % p, 0, 0, (-cbi) % p
                J00, J01, J10, J11 = (
                    (s00 * J00 + s01 * J10) % p,
                    (s00 * J01 + s01 * J11) % p,
                    (s10 * J00 + s11 * J10) % p,
                    (s10 * J01 + s11 * J11) % p,
                )
                ca, cb = na, nb
            vai, vbi = pow(va, p - 2, p), pow(vb, p - 2, p)
            uda = udb = 0
            vt = 1
            for ch in u3:
                if ch == "a":
                    uda = (uda + vt) % p
                    vt = (vt * va) % p
                elif ch == "b":
                    udb = (udb + vt) % p
                    vt = (vt * vb) % p
                elif ch == "A":
                    vt = (vt * vai) % p
                    uda = (uda - vt) % p
                else:
                    vt = (vt * vbi) % p
                    udb = (udb - vt) % p
            r0 = [(vt - J00) % p, (-J01) % p, (1 - va) % p]
            r1 = [(-J10) % p, (vt - J11) % p, (1 - vb) % p]
            dg = [(va - 1) % p, (vb - 1) % p, (vt - 1) % p]
            # Verify rank([r0; r1]) == 1 so h^1(M_3; chi) == 1:
            if np_rank_gf(np.array([r0, r1], dtype=np.int64), p) != 1:
                sys.exit(2)
            row = r0 if any(r0) else r1
            piv = next(k for k in range(3) if row[k] != 0)
            inv_piv = pow(row[piv], p - 2, p)
            dpiv = next(k for k in range(3) if dg[k] != 0)
            inv_dpiv = pow(dg[dpiv], p - 2, p)
            c_found = None
            for free_k in range(3):
                if free_k == piv:
                    continue
                c = [0, 0, 0]
                c[free_k] = 1
                c[piv] = (-row[free_k] * inv_piv) % p
                fac = (c[dpiv] * inv_dpiv) % p
                if any((c[k] - fac * dg[k]) % p != 0 for k in range(3)):
                    c_found = c
                    break
            if c_found is None:
                sys.exit(2)
            ce = ((1 - vb) * c_found[0] + (va - 1) * c_found[1]) % p
            if ce == 0:
                sys.exit(2)
            cm = (pow(vt, p - 2, p) * (c_found[2] - uda * c_found[0] - udb * c_found[1])) % p
            s_arr[i] = (cm * pow(ce, p - 2, p)) % p
            c_arr[i] = c_found
        return s_arr, zeta, c_arr

    prime_runs = [slopes_for_prime(p) for p in primes]
    partitions = []
    for s_arr, _, _ in prime_runs:
        buckets = collections.defaultdict(list)
        for i in range(ordG):
            if i != zero_i:
                buckets[s_arr[i]].append(i)
        partitions.append(sorted(tuple(v) for v in buckets.values()))
    if not (partitions[0] == partitions[1] == partitions[2]):
        sys.exit(2)

    slopes = prime_runs[0][0]
    zeta0 = prime_runs[0][1]
    cocs0 = prime_runs[0][2]
    slope_buckets: dict[int, list[int]] = collections.defaultdict(list)
    for i in range(ordG):
        if i != zero_i:
            slope_buckets[int(slopes[i])].append(i)  # type: ignore[arg-type]

    def add_c(i: int, j: int) -> int:
        return char_idx[((chars[i][0] + chars[j][0]) % expG, (chars[i][1] + chars[j][1]) % expG)]

    def sub_c(i: int, j: int) -> int:
        return char_idx[((chars[i][0] - chars[j][0]) % expG, (chars[i][1] - chars[j][1]) % expG)]

    def mul_k(k: int, i: int) -> int:
        return char_idx[((k * chars[i][0]) % expG, (k * chars[i][1]) % expG)]

    def deck_c(i: int) -> int:
        ea, eb = chars[i]
        return char_idx[((M1[0][0] * ea + M1[1][0] * eb) % expG, (M1[0][1] * ea + M1[1][1] * eb) % expG)]

    def idx_law(lam: int, alp: int) -> int:
        if lam == zero_i or alp == zero_i or alp == lam:
            return 0
        sl = slopes[lam]
        return (1 if slopes[alp] == sl else 0) - (1 if slopes[sub_c(alp, lam)] == sl else 0)

    # Check opposite-sign pairing (lam, alp) -> (-lam, alp - lam) across all (lam, alp):
    firing_modules = 0
    for lam in range(ordG):
        if lam == zero_i:
            continue
        nlam = mul_k(-1, lam)
        for alp in range(ordG):
            v = idx_law(lam, alp)
            if v != 0:
                firing_modules += 1
            if idx_law(nlam, sub_c(alp, lam)) != -v:
                sys.exit(2)

    five_inv: dict[int, list[int]] = collections.defaultdict(list)
    for py in range(ordG):
        five_inv[mul_k(5, py)].append(py)
    squares = {mul_k(2, x) for x in range(ordG)}
    deck_map = [deck_c(i) for i in range(ordG)]

    gen_bgs: dict[tuple[int, ...], int] = {}
    for lam in range(ordG):
        if lam == zero_i:
            continue
        sl = int(slopes[lam])  # type: ignore[arg-type]
        S_lam = slope_buckets[sl]
        S_set = set(S_lam)
        A_pos = [alp for alp in S_lam if alp != lam and sub_c(alp, lam) not in S_set]
        A_neg = [add_c(bet, lam) for bet in S_lam if add_c(bet, lam) != zero_i and add_c(bet, lam) not in S_set]
        for v0, A_list in ((1, A_pos), (-1, A_neg)):
            if not A_list:
                continue
            A_set = set(A_list)
            for ad in A_list:
                for aL in A_list:
                    for py in five_inv.get(sub_c(ad, aL), ()):
                        th = sub_c(ad, mul_k(2, py))
                        W = sub_c(mul_k(2, th), lam)
                        th_W = add_c(th, W)
                        aQ = add_c(th_W, py)
                        if aQ not in A_set:
                            continue
                        au = add_c(th_W, mul_k(-4, py))
                        if au not in A_set:
                            continue
                        ae = add_c(th_W, mul_k(6, py))
                        if ae not in A_set:
                            continue
                        an = add_c(th, mul_k(-3, W))
                        gen_bgs[(lam, aQ, au, ae, ad, aL, an)] = v0

    seen = set()
    orb_hist: Counter[int] = Counter()
    for bg in gen_bgs:
        if bg in seen:
            continue
        b1 = tuple(deck_map[x] for x in bg)
        b2 = tuple(deck_map[x] for x in b1)
        orb = {bg, b1, b2}
        seen |= orb
        orb_hist[len(orb)] += len(orb)

    half = expG // 2
    parities = [char_idx[(0, half)], char_idx[(half, 0)], char_idx[(half, half)]]
    par_slopes = {slopes[pi] for pi in parities}
    if len(par_slopes) != 1:
        sys.exit(2)
    par_class_sz = len(slope_buckets[int(slopes[parities[0]])])  # type: ignore[arg-type]
    par_module_firings = sum(1 for pi in parities for alp in range(ordG) if idx_law(pi, alp) != 0)
    par_bg_firings = sum(1 for bg in gen_bgs if bg[0] in parities)

    ua = u3.count("a") - u3.count("A")
    ub = u3.count("b") - u3.count("B")

    def direct_engine_index(lam: int, alp: int) -> int:
        if lam == zero_i:
            return 0
        p0 = primes[0]
        c_lam = cocs0[lam]
        assert c_lam is not None
        bet = sub_c(alp, lam)

        def char_vals(ci: int) -> dict[str, int]:
            ea, eb = chars[ci]
            et = (ua * ea + ub * eb) % expG
            return {"a": pow(zeta0, ea, p0), "b": pow(zeta0, eb, p0), "t": pow(zeta0, et, p0)}

        va = char_vals(alp)
        vb = char_vals(bet)
        idx_map = {"a": 0, "b": 1, "t": 2}
        mats: dict[str, np.ndarray] = {}
        invs: dict[str, np.ndarray] = {}
        for g in "abt":
            ag, bg_v = va[g], vb[g]
            dg_v = (c_lam[idx_map[g]] * bg_v) % p0
            M2 = np.array([[ag, dg_v], [0, bg_v]], dtype=np.int64)
            ai, bi = pow(ag, p0 - 2, p0), pow(bg_v, p0 - 2, p0)
            M2i = np.array([[ai, (-ai * dg_v * bi) % p0], [0, bi]], dtype=np.int64)
            mats[g], invs[g] = M2, M2i
        t_E, t_Es = verify_b1604_e1_duality_gf(mats, invs, steps3, "abAB", mu3, p0)
        return t_E[3] - t_Es[3]

    return {
        "ordG": ordG,
        "expG": expG,
        "zero_i": zero_i,
        "slopes": slopes,
        "distinct_slopes": len(slope_buckets),
        "firing_modules": firing_modules,
        "gen_count": len(gen_bgs),
        "lift_count": sum(1 for bg in gen_bgs if bg[0] in squares),
        "nuc_count": sum(1 for bg, v0 in gen_bgs.items() if idx_law(bg[0], bg[6]) == v0),
        "pos_count": sum(1 for v0 in gen_bgs.values() if v0 == 1),
        "neg_count": sum(1 for v0 in gen_bgs.values() if v0 == -1),
        "orb_hist": {str(k): int(v) for k, v in sorted(orb_hist.items())},
        "parity_slope_class_size": par_class_sz,
        "parity_module_firings": par_module_firings,
        "parity_bg_firings": par_bg_firings,
        "idx_law": idx_law,
        "add_c": add_c,
        "sub_c": sub_c,
        "direct_engine_index": direct_engine_index,
    }


_W16_VARS = (PARI("x"), PARI("y"), PARI("z"), PARI("u"))


def analyze_w16_word(w: str) -> dict[str, object]:
    """Exact number field K = Q(x, y, z) and prime-ideal factorization of (x, y, z) in O_K."""
    px, py, pz, pu = _W16_VARS

    def step_L(x, y, z):
        return (z, y, y * z - x)

    def step_R(x, y, z):
        return (x, z, x * z - y)

    def inv_L(X, Y, Z):
        return (X * Y - Z, Y, X)

    def inv_R(X, Y, Z):
        return (X, X * Y - Z, Y)

    def cross_cands(s: complex) -> list[complex]:
        out = []
        for u_c in [s, 1 / (1 - s), 1 - 1 / s, s.conjugate(), (1 / (1 - s)).conjugate(), (1 - 1 / s).conjugate()]:
            for val in [(1 - u_c) / u_c, u_c / (1 - u_c)]:
                rt = cmath.sqrt(val)
                out.extend([rt, -rt])
        return out

    M_sn = snappy.Manifold("b++" + w)
    vt = float(M_sn.volume())
    sh = [complex(s) for s in M_sn.tetrahedra_shapes("rect")]
    seed = None
    for i in range(len(sh)):
        for j in range(len(sh)):
            for r in cross_cands(sh[i]):
                for r1 in cross_cands(sh[j]):
                    if abs(r) < 1e-12 or abs(r1) < 1e-12:
                        continue
                    xz = r1 * (r * r + 1) / r if w[1] == "L" else r1 * (r * r + 1)
                    if abs(xz) < 1e-12:
                        continue
                    z = (xz * xz + r * r + 1) / (xz * r)
                    x, y = xz * z, r * z
                    if not (x.real > 0.5 and y.real > 0.5 and z.real > 0.5):
                        continue
                    qx, qy, qz = x, y, z
                    vsum = 0.0
                    for ch in w:
                        u_t = (qz * qz) / (qy * qy + qz * qz) if ch == "L" else (qx * qx) / (qx * qx + qz * qz)
                        qx, qy, qz = step_L(qx, qy, qz) if ch == "L" else step_R(qx, qy, qz)
                        vsum += abs(float(PARI(u_t).polylog(2, 2)))
                    if abs(qx - x) + abs(qy - y) + abs(qz - z) < 1e-6 and abs(vsum - vt) < 1e-5:
                        seed = (x, y, z)
                        break
                if seed is not None:
                    break
            if seed is not None:
                break
        if seed is not None:
            break
    if seed is None:
        raise RuntimeError(f"Could not locate geometric seed for {w}")

    dps = 120
    old_prec = gmpy2.get_context().precision
    gmpy2.get_context().precision = int(dps * 3.35) + 64
    try:
        x_g, y_g, z_g = gmpy2.mpc(seed[0]), gmpy2.mpc(seed[1]), gmpy2.mpc(seed[2])
        for _ in range(12):
            qx, qy, qz = x_g, y_g, z_g
            J = [[gmpy2.mpc(1 if r == c else 0) for c in range(3)] for r in range(3)]
            for ch in w:
                if ch == "L":
                    J = [J[2], J[1], [qy * J[2][c] + qz * J[1][c] - J[0][c] for c in range(3)]]
                    qx, qy, qz = qz, qy, qy * qz - qx
                else:
                    J = [J[0], J[2], [qx * J[2][c] + qz * J[0][c] - J[1][c] for c in range(3)]]
                    qx, qy, qz = qx, qz, qx * qz - qy
            f = [qx - x_g, qy - y_g, x_g * x_g + y_g * y_g + z_g * z_g - x_g * y_g * z_g]
            A = [
                [J[0][0] - 1, J[0][1], J[0][2]],
                [J[1][0], J[1][1] - 1, J[1][2]],
                [2 * x_g - y_g * z_g, 2 * y_g - x_g * z_g, 2 * z_g - x_g * y_g],
            ]
            b = [-f[0], -f[1], -f[2]]
            for k in range(3):
                piv = max(range(k, 3), key=lambda r: abs(A[r][k]))
                A[k], A[piv] = A[piv], A[k]
                b[k], b[piv] = b[piv], b[k]
                for r in range(k + 1, 3):
                    fac = A[r][k] / A[k][k]
                    for c in range(k, 3):
                        A[r][c] -= fac * A[k][c]
                    b[r] -= fac * b[k]
            dx = [gmpy2.mpc(0)] * 3
            for k in range(2, -1, -1):
                dx[k] = (b[k] - sum(A[k][c] * dx[c] for c in range(k + 1, 3))) / A[k][k]
            x_g += dx[0]
            y_g += dx[1]
            z_g += dx[2]

        PARI.default("realprecision", dps)

        def mpfr_p(r_val):
            if r_val == 0:
                return PARI("0.0")
            m_s, e_s, _ = r_val.digits(10)
            neg = m_s.startswith("-")
            if neg:
                m_s = m_s[1:]
            m_s = m_s[: dps - 5]
            return PARI(f"-0.{m_s}E{e_s}" if neg else f"0.{m_s}E{e_s}")

        xn = mpfr_p(x_g.real) + PARI("I") * mpfr_p(x_g.imag)
        yn = mpfr_p(y_g.real) + PARI("I") * mpfr_p(y_g.imag)
        zn = mpfr_p(z_g.real) + PARI("I") * mpfr_p(z_g.imag)
    finally:
        gmpy2.get_context().precision = old_prec

    mid = len(w) // 2
    w1, w2 = w[:mid], w[mid:]
    M_hom = homology_mat("+", w)
    tr_val = M_hom[0][0] + M_hom[1][1]
    odd_trace = (tr_val % 2) == 1

    for cb, cc in [(0, 0), (1, 2), (2, 3), (1, 3)]:
        px_expr = pu - cb * py - cc * pz
        th_num = xn + cb * yn + cc * zn
        a1, b1, c1 = px_expr, py, pz
        for ch in w1:
            a1, b1, c1 = step_L(a1, b1, c1) if ch == "L" else step_R(a1, b1, c1)
        a2, b2, c2 = px_expr, py, pz
        for ch in reversed(w2):
            a2, b2, c2 = inv_L(a2, b2, c2) if ch == "L" else inv_R(a2, b2, c2)
        mk = px_expr * px_expr + py * py + pz * pz - px_expr * py * pz
        eqs = [a1 - a2, b1 - b2, c1 - c2]
        r_ys = [PARI.polresultant(mk, eq, pz) for eq in eqs]
        g_u = PARI.gcd(PARI.polresultant(r_ys[0], r_ys[1], py), PARI.polresultant(r_ys[0], r_ys[2], py))
        facs = g_u.factor()
        best_P = None
        for k in range(len(facs[0])):
            P_c = facs[0][k]
            if float(PARI.abs(PARI.subst(P_c, "u", th_num))) < 1e-60:
                best_P = P_c
                break
        if best_P is None:
            continue
        one_K = PARI.Mod(1, best_P)
        gy = PARI.gcd(PARI.gcd(one_K * r_ys[0], one_K * r_ys[1]), one_K * r_ys[2])
        if int(PARI.poldegree(gy, py)) != 1:
            continue
        my = -PARI.polcoef(gy, 0, py) / PARI.polcoef(gy, 1, py)
        gz = one_K * PARI.subst(mk, "y", my.lift())
        for eq in eqs:
            gz = PARI.gcd(gz, one_K * PARI.subst(eq, "y", my.lift()))
        if int(PARI.poldegree(gz, pz)) != 1:
            continue
        mz = -PARI.polcoef(gz, 0, pz) / PARI.polcoef(gz, 1, pz)
        mx = PARI.Mod(pu, best_P) - cb * my - cc * mz

        qx, qy, qz = mx, my, mz
        for ch in w:
            qx, qy, qz = (qz, qy, qy * qz - qx) if ch == "L" else (qx, qz, qx * qz - qy)
        if not (qx == mx and qy == my and qz == mz and mx * mx + my * my + mz * mz - mx * my * mz == 0):
            sys.exit(2)

        deg = int(best_P.poldegree())
        P_x = PARI.subst(best_P, "u", px)
        mx_x = PARI.Mod(PARI.subst(mx.lift(), "u", px), P_x)
        my_x = PARI.Mod(PARI.subst(my.lift(), "u", px), P_x)
        mz_x = PARI.Mod(PARI.subst(mz.lift(), "u", px), P_x)
        norms = [abs(int(c.norm())) for c in (mx_x, my_x, mz_x)]
        g_norm = math.gcd(norms[0], math.gcd(norms[1], norms[2]))
        g_primes = [int(p_f) for p_f in PARI.factor(g_norm)[0]]
        nf = PARI.nfinit([P_x, g_primes])

        ideals: list[dict[str, object]] = []
        for p_f in g_primes:
            for pr in PARI.idealprimedec(nf, p_f):
                vals = [int(PARI.idealval(nf, c.lift(), pr)) for c in (mx_x, my_x, mz_x)]
                emin = min(vals)
                if emin > 0:
                    nm_pr = int(PARI.idealnorm(nf, pr))
                    f_deg = round(math.log(nm_pr, p_f))
                    if p_f**f_deg != nm_pr:
                        sys.exit(2)
                    ideals.append({"p": p_f, "residue_degree": f_deg, "exponent": emin, "vals": vals})
        ideal_norm = math.prod(int(d["p"]) ** (int(d["residue_degree"]) * int(d["exponent"])) for d in ideals)
        return {
            "word": w,
            "trace": tr_val,
            "odd_trace": odd_trace,
            "degree_K": deg,
            "prime_factors": ideals,
            "ideal_norm": ideal_norm,
        }
    raise RuntimeError(f"Failed algebraic field reconstruction on {w}")


# ---------------------------------------------------------------------------
# 5. Three planted negative controls (must fail and fire before any item runs)
# ---------------------------------------------------------------------------

def run_negative_controls() -> dict[str, object]:
    # Control C1b-1: Slope-law sign / difference fault on +LR at tick 3
    lr_data = slope_table_and_census("+", "LR")
    ordG = int(lr_data["ordG"])
    zero_i = int(lr_data["zero_i"])
    slopes = lr_data["slopes"]
    add_c = lr_data["add_c"]
    sub_c = lr_data["sub_c"]
    direct_eng = lr_data["direct_engine_index"]

    mismatches_true = 0
    mismatches_wrong_sign = 0
    mismatches_wrong_diff = 0
    for lam in range(ordG):
        if lam == zero_i:
            continue
        for alp in range(ordG):
            eng = direct_eng(lam, alp)
            true_v = lr_data["idx_law"](lam, alp)
            if eng != true_v:
                mismatches_true += 1
            if alp == zero_i or alp == lam:
                ws_v = 0
            else:
                sl = slopes[lam]
                ws_v = (1 if slopes[alp] == sl else 0) + (1 if slopes[sub_c(alp, lam)] == sl else 0)
            if eng != ws_v:
                mismatches_wrong_sign += 1
            ap = add_c(alp, lam)
            if alp == zero_i or ap == zero_i:
                wd_v = 0
            else:
                sl = slopes[lam]
                wd_v = (1 if slopes[alp] == sl else 0) - (1 if slopes[ap] == sl else 0)
            if eng != wd_v:
                mismatches_wrong_diff += 1

    c1b_1_fired = (mismatches_true == 0) and (mismatches_wrong_sign > 0) and (mismatches_wrong_diff > 0)
    if not c1b_1_fired:
        sys.exit(2)

    # Control C1b-2: Spin-zero T2 peripheral-acyclicity violation on +LR at tick 3
    # Replace rho_Q (rho_Q([a,b]) = -I_2, r^1 = 0) with a cusp-trivial doublet module [[alp, c_lam*bet], [0, bet]]:
    # verify r^1 > 0 on non-trivial cusp-trivial character AND non-zero class index I(E) != 0 when peripheral acyclicity is dropped.
    nonzero_indices = [direct_eng(lam, alp) for lam in range(ordG) if lam != zero_i for alp in range(ordG)]
    p_chk = 20089
    steps3, mu3, _ = steps_route2("+", "LR", 3)
    triv2 = {g: np.eye(2, dtype=np.int64) for g in "abt"}
    h0_triv, h1_triv, r1_triv, _, _ = cohom_steps_np_gf(triv2, triv2, steps3, "abAB", mu3, p_chk)
    c1b_2_fired = (h0_triv == 2 and r1_triv > 0) and any(v != 0 for v in nonzero_indices)
    if not c1b_2_fired:
        sys.exit(2)

    # Control C1b-3: Trace-ideal parity swap between LR (odd trace 3) and LLR (even trace 4)
    w_lr = analyze_w16_word("LR")
    w_llr = analyze_w16_word("LLR")

    def passes_odd_rule(rec: dict[str, object]) -> bool:
        pfs = rec["prime_factors"]
        return len(pfs) == 1 and pfs[0]["p"] == 3 and pfs[0]["residue_degree"] == 1 and pfs[0]["vals"] == [1, 1, 1]

    def passes_even_rule(rec: dict[str, object]) -> bool:
        pfs = rec["prime_factors"]
        return len(pfs) == 1 and pfs[0]["p"] == 2 and rec["ideal_norm"] >= 4

    c1b_3_fired = (
        passes_odd_rule(w_lr)
        and passes_even_rule(w_llr)
        and (not passes_even_rule(w_lr))
        and (not passes_odd_rule(w_llr))
    )
    if not c1b_3_fired:
        sys.exit(2)

    return {
        "C1b_1": {
            "fired": c1b_1_fired,
            "mismatches_true": mismatches_true,
            "mismatches_wrong_sign": mismatches_wrong_sign,
            "mismatches_wrong_diff": mismatches_wrong_diff,
        },
        "C1b_2": {
            "fired": c1b_2_fired,
            "triv_doublet_h0_r1": [h0_triv, r1_triv],
            "cusp_trivial_nonzero_index_count": sum(1 for v in nonzero_indices if v != 0),
        },
        "C1b_3": {
            "fired": c1b_3_fired,
            "LR_ideal_norm": w_lr["ideal_norm"],
            "LLR_ideal_norm": w_llr["ideal_norm"],
        },
        "all_controls_fired": bool(c1b_1_fired and c1b_2_fired and c1b_3_fired),
    }


# ---------------------------------------------------------------------------
# 6. Row verifiers (923, 924, 925, 926, 927, 928)
# ---------------------------------------------------------------------------

def verify_row_923() -> dict[str, object]:
    """Row 923 (@ 6e5f5f2e3): W2 unconstrained character variety fixed points of L and R."""
    xs, ys, zs = sp.symbols("x y z")
    eqs_lr = [zs - xs, ys * zs - xs - zs, xs * zs - ys - zs]
    gb_lr = sp.groebner(eqs_lr, xs, ys, zs, order="lex")
    sols_lr = sp.solve(list(gb_lr.exprs), (xs, ys, zs), dict=True)
    pts_lr = sorted((int(s[xs]), int(s[ys]), int(s[zs])) for s in sols_lr)

    # Include P: (x, y, z) -> (y, x, z) and -I: (x, y, z) -> (x, y, z)
    gb_full = sp.groebner(eqs_lr + [ys - xs], xs, ys, zs, order="lex")
    sols_full = sp.solve(list(gb_full.exprs), (xs, ys, zs), dict=True)
    pts_full = sorted((int(s[xs]), int(s[ys]), int(s[zs])) for s in sols_full)

    kappas = {str(pt): pt[0] ** 2 + pt[1] ** 2 + pt[2] ** 2 - pt[0] * pt[1] * pt[2] - 2 for pt in pts_lr}
    ok = (
        pts_lr == [(0, 0, 0), (2, 2, 2)]
        and pts_full == [(0, 0, 0), (2, 2, 2)]
        and kappas["(0, 0, 0)"] == -2
        and kappas["(2, 2, 2)"] == 2
    )
    return {
        "row": 923,
        "commits": ["6e5f5f2e3"],
        "fixed_points_LR": [list(pt) for pt in pts_lr],
        "fixed_points_LR_P_negI": [list(pt) for pt in pts_full],
        "puncture_traces_kappa": kappas,
        "pf1_exclusion_of_222": "reading (not independently checked)",
        "result": "the same" if ok else "differs",
    }


def _eval_b1552_state_route(sign: str, word: str, k_tick: int, route: int, p: int = 20089) -> dict[str, object]:
    sp_obj = setup_spin_gf(p)
    QA, QB = sp_obj["QA"], sp_obj["QB"]
    QAi, QBi = sp_obj["QAi"], sp_obj["QBi"]
    zeta24 = int(sp_obj["zeta24"])
    zeta8 = int(sp_obj["zeta8"])
    lift_2d = sp_obj["lift_steps_2d"]

    if route == 1:
        steps, mu_w, _ = steps_route1(sign, word, k_tick)
    else:
        steps, mu_w, _ = steps_route2(sign, word, k_tick)

    pars = [(1, 0), (0, 1), (1, 1)]
    struct_by_mod_lift: dict[str, Counter[tuple[int, int]]] = collections.defaultdict(Counter)
    counts_by_mod: dict[str, list[list[int]]] = {"a": [], "b": []}
    t2_tuples: list[dict[str, object]] = []
    n_readings = 0
    all_zero = True
    t2_ok = True

    for lift_idx in (0, 1):
        Ut = lift_2d(steps, lift_idx)
        Uti = np_inv_gf(Ut, p)
        # Note mu_w = inv(u) + t or abt: we twist by character lambda with lambda(a)=(-1)^pa, lambda(b)=(-1)^pb, lambda(mu_w)=kappa in mu_8!
        # Wait: if lambda(mu_w) = kappa, then lambda(t) = kappa * lambda(u) (where for abt, u = BA so lambda(u) = (-1)^(pa+pb))!
        u_part = mu_w[:-1]  # prefix before 't'
        for mod_name in ("a", "b"):
            for par in pars:
                sa = p - 1 if par[0] else 1
                sb = p - 1 if par[1] else 1
                lu = 1
                for ch in u_part:
                    lu = (lu * (sa if ch in "aA" else sb)) % p
                for k8 in range(8):
                    kap = pow(zeta8, k8, p)
                    kap_bar = pow(zeta8, (-k8) % 8, p)
                    lt = (kap * pow(lu, p - 2, p)) % p
                    lt_bar = (kap_bar * pow(lu, p - 2, p)) % p
                    if mod_name == "a":
                        Ma = np.block([[(sa * QA) % p, np.zeros((2, 2), dtype=np.int64)], [np.zeros((2, 2), dtype=np.int64), (sa * QA) % p]])
                        Mb = np.block([[(sb * QB) % p, np.zeros((2, 2), dtype=np.int64)], [np.zeros((2, 2), dtype=np.int64), (sb * QB) % p]])
                        Mt = np.block([[(lt * Ut) % p, np.zeros((2, 2), dtype=np.int64)], [np.zeros((2, 2), dtype=np.int64), (lt * Ut) % p]])
                    else:
                        Ma = np.block([[(sa * QA) % p, np.zeros((2, 2), dtype=np.int64)], [np.zeros((2, 2), dtype=np.int64), (sa * QA) % p]])
                        Mb = np.block([[(sb * QB) % p, np.zeros((2, 2), dtype=np.int64)], [np.zeros((2, 2), dtype=np.int64), (sb * QB) % p]])
                        Mt = np.block([[(lt * Ut) % p, np.zeros((2, 2), dtype=np.int64)], [np.zeros((2, 2), dtype=np.int64), (lt_bar * Ut) % p]])
                    A_mats = {"a": Ma, "b": Mb, "t": Mt}
                    A_invs = {"a": np_inv_gf(Ma, p), "b": np_inv_gf(Mb, p), "t": np_inv_gf(Mt, p)}
                    h0, h1, r1, n, int_cocs = cohom_steps_np_gf(A_mats, A_invs, steps, "abAB", mu_w, p, want_interior=True)
                    if n == 0:
                        continue
                    if mod_name == "a" and lift_idx == 0:
                        struct_by_mod_lift["a_lift0"][(h1, n)] += 1
                    for draw_seed in (1552, 2552):
                        c_vec = np.zeros(12, dtype=np.int64)
                        for idx_c, z_c in enumerate(int_cocs):
                            wt = pow(zeta24, (draw_seed + 7 * idx_c + 1) % 24, p) + (idx_c + 2)
                            c_vec = (c_vec + (wt % p) * z_c) % p
                        W1_m: dict[str, np.ndarray] = {}
                        W1_i: dict[str, np.ndarray] = {}
                        L2_m: dict[str, np.ndarray] = {}
                        L2_i: dict[str, np.ndarray] = {}
                        for gi, g in enumerate("abt"):
                            Ag = A_mats[g]
                            Agi = A_invs[g]
                            cg = c_vec[4 * gi : 4 * (gi + 1)].reshape(4, 1)
                            neg_Aic = ((-Agi @ cg) % p)
                            M5 = np.block([[Ag, cg], [np.zeros((1, 4), dtype=np.int64), np.ones((1, 1), dtype=np.int64)]]) % p
                            M5i = np.block([[Agi, neg_Aic], [np.zeros((1, 4), dtype=np.int64), np.ones((1, 1), dtype=np.int64)]]) % p
                            W1_m[g], W1_i[g] = M5, M5i
                            L2_m[g], L2_i[g] = wedge2_gf(M5, p), wedge2_gf(M5i, p)
                        t_W1, t_W1s = verify_b1604_e1_duality_gf(W1_m, W1_i, steps, "abAB", mu_w, p)
                        t_L2, t_L2s = verify_b1604_e1_duality_gf(L2_m, L2_i, steps, "abAB", mu_w, p)
                        iw1 = t_W1[3] - t_W1s[3]
                        il2 = t_L2[3] - t_L2s[3]
                        n_readings += 1
                        counts_by_mod[mod_name].append([iw1, il2])
                        if (iw1, il2) != (0, 0):
                            all_zero = False
                        if not (h0 == 0 and r1 == 0 and t_W1 == (0, n - 1, 0, n - 1) and t_W1s == (1, n + 1, 2, n - 1)):
                            t2_ok = False
                        if len(t2_tuples) < 8:
                            t2_tuples.append({"A": [h0, h1, r1, n], "W1": list(t_W1), "W1s": list(t_W1s), "L2": list(t_L2), "L2s": list(t_L2s)})

    return {
        "n_readings": n_readings,
        "all_zero": all_zero,
        "t2_ok": t2_ok,
        "struct_a_lift0": {str(k): int(v) for k, v in sorted(struct_by_mod_lift["a_lift0"].items())},
        "counts_by_mod": counts_by_mod,
    }


def verify_row_924() -> dict[str, object]:
    """Row 924 (@ c9d03b925, 80a263a36): sm:B1552 preregistration seal, pre-seal controls, and I1-I3."""
    prereg_bytes = subprocess.check_output(
        ["git", "-C", str(REPO_ROOT), "cat-file", "-p", "c9d03b925:frontier/B1552_the_chiral_triplets_count/PREREGISTRATION.md"]
    )
    sha_hex = hashlib.sha256(prereg_bytes).hexdigest()
    sha_ok = sha_hex.startswith("556910b6")

    # I1: m135 (-LLRR) companion cover (d = |2 - (-2)| = 4) has 2 active sign members reading [-1, -1]
    M_m135 = homology_mat("-", "LLRR")
    detM = M_m135[0][0] * M_m135[1][1] - M_m135[0][1] * M_m135[1][0]
    Minv = ((detM * M_m135[1][1], -detM * M_m135[0][1]), (-detM * M_m135[1][0], detM * M_m135[0][0]))
    # For -LLRR: M = ((-1, -2), (2, 3)) or conjugate; M - I has index 4! Find unique M-invariant lattice containing (M - I)Z^2:
    v1 = (M_m135[0][0] - 1, M_m135[1][0])
    v2 = (M_m135[0][1], M_m135[1][1] - 1)
    lat_found = None
    for a_l in (1, 2, 4):
        c_l = 4 // a_l
        for b_l in range(a_l):
            ok_lat = True
            for vx, vy in ((a_l, 0), (b_l, c_l)):
                mx = M_m135[0][0] * vx + M_m135[0][1] * vy
                my = M_m135[1][0] * vx + M_m135[1][1] * vy
                if my % c_l != 0 or (mx - (my // c_l) * b_l) % a_l != 0:
                    ok_lat = False
                    break
            if ok_lat and all(vy % c_l == 0 and (vx - (vy // c_l) * b_l) % a_l == 0 for vx, vy in (v1, v2)):
                lat_found = (a_l, b_l, c_l)
    assert lat_found is not None
    a_l, b_l, c_l = lat_found

    def red_lat(vx: int, vy: int) -> tuple[int, int]:
        q = vy // c_l
        return ((vx - q * b_l) % a_l, vy - q * c_l)

    cosets = [(rx, ry) for ry in range(c_l) for rx in range(a_l)]
    c_map = {pt: i for i, pt in enumerate(cosets)}
    wb = red_lat(Minv[0][0] + Minv[0][1], Minv[1][0] + Minv[1][1])
    cov_m135 = build_cover(
        "-",
        "LLRR",
        4,
        {
            "a": [c_map[red_lat(x + 1, y)] for x, y in cosets],
            "b": [c_map[red_lat(x, y + 1)] for x, y in cosets],
            "t": [c_map[red_lat(Minv[0][0] * x + Minv[0][1] * y - wb[0], Minv[1][0] * x + Minv[1][1] * y - wb[1])] for x, y in cosets],
        },
    )
    hol_m135 = get_holonomy("-", "LLRR")
    gm4, gm4_inv = hol_m135["gm4"], hol_m135["gm4_inv"]
    gen_mats_0: list[GMMat] = []
    gen_invs_0: list[GMMat] = []
    z0, one = gmpy2.mpc(0), gmpy2.mpc(1)
    for gw in cov_m135["gen_words"]:
        R = [[one if i == j else z0 for j in range(4)] for i in range(4)]
        for ch in gw:
            R = gm_matmul(R, gm4[ch] if ch in "abt" else gm4_inv[ch.lower()])
        gen_mats_0.append(R)
        gen_invs_0.append(gm_inv(R))

    i1_counts: list[list[int]] = []
    for c_char in cover_characters(cov_m135, 2):
        mats_c = [gm_scale(gmpy2.mpc(-1 if c_char[j] % 2 else 1), gen_mats_0[j]) for j in range(len(gen_mats_0))]
        invs_c = [gm_scale(gmpy2.mpc(-1 if c_char[j] % 2 else 1), gen_invs_0[j]) for j in range(len(gen_invs_0))]
        _, _, _, n_c, int_b = cohom_pres_gm(mats_c, invs_c, cov_m135["rels_idx"], cov_m135["cusps_idx"], want_interior=True)
        if n_c > 0 and int_b is not None:
            ng_c = len(mats_c)
            c_vec = [sum(int_b[i][r] * gmpy2.mpc(r + 1, r + 2) for r in range(n_c)) for i in range(4 * ng_c)]
            W1_m, W1_i, W1s_m, W1s_i = [], [], [], []
            L2_m, L2_i, L2s_m, L2s_i = [], [], [], []
            for j in range(ng_c):
                Aj, Aij = mats_c[j], invs_c[j]
                cj = c_vec[4 * j : 4 * (j + 1)]
                naic = [-sum(Aij[ri][k] * cj[k] for k in range(4)) for ri in range(4)]
                M5 = [Aj[ri] + [cj[ri]] for ri in range(4)] + [[z0, z0, z0, z0, one]]
                M5i = [Aij[ri] + [naic[ri]] for ri in range(4)] + [[z0, z0, z0, z0, one]]
                M5s, M5si = gm_transpose(M5i), gm_transpose(M5)
                W1_m.append(M5); W1_i.append(M5i); W1s_m.append(M5s); W1s_i.append(M5si)
                L2_m.append(wedge2_gm(M5)); L2_i.append(wedge2_gm(M5i))
                L2s_m.append(wedge2_gm(M5s)); L2s_i.append(wedge2_gm(M5si))
            nw1 = cohom_pres_gm(W1_m, W1_i, cov_m135["rels_idx"], cov_m135["cusps_idx"])[3]
            nw1s = cohom_pres_gm(W1s_m, W1s_i, cov_m135["rels_idx"], cov_m135["cusps_idx"])[3]
            nl2 = cohom_pres_gm(L2_m, L2_i, cov_m135["rels_idx"], cov_m135["cusps_idx"])[3]
            nl2s = cohom_pres_gm(L2s_m, L2s_i, cov_m135["rels_idx"], cov_m135["cusps_idx"])[3]
            i1_counts.append([nw1 - nw1s, nl2 - nl2s])
    i1_ok = i1_counts == [[-1, -1], [-1, -1]]

    # I2: Structure multisets on +LR and -LR across Routes 1 and 2
    r1_plr = _eval_b1552_state_route("+", "LR", 3, 1)
    r2_plr = _eval_b1552_state_route("+", "LR", 3, 2)
    r1_mlr = _eval_b1552_state_route("-", "LR", 3, 1)
    r2_mlr = _eval_b1552_state_route("-", "LR", 3, 2)
    i2_ok = (
        r1_plr["struct_a_lift0"] == {"(4, 4)": 3}
        and r2_plr["struct_a_lift0"] == {"(4, 4)": 3}
        and r1_mlr["struct_a_lift0"] == {"(2, 2)": 6}
        and r2_mlr["struct_a_lift0"] == {"(2, 2)": 6}
    )

    # Pre-seal controls (+LLRR tick 1, -LLRR tick 1, +LLR tick 2) and I3 (+LLRR Routes 1 & 2)
    ctrl_ok = True
    for sgn_c, w_c, tk_c in [("+", "LLRR", 1), ("-", "LLRR", 1), ("+", "LLR", 2)]:
        for rt in (1, 2):
            ev = _eval_b1552_state_route(sgn_c, w_c, tk_c, rt)
            if not ev["all_zero"] or ev["n_readings"] == 0:
                ctrl_ok = False

    # Population arithmetic check: 6 chiral * 48 + 6 vector-like * 24 = 432 per route
    odd6 = genesis_states(6, odd_only=True)
    chiral_list = []
    vec_list = []
    for sgn_s, w_s, _ in odd6:
        hand = (w_s.count("L") - w_s.count("R") + (2 if sgn_s == "-" else 0)) % 4
        if hand == 2:
            chiral_list.append(sgn_s + w_s)
        else:
            vec_list.append(sgn_s + w_s)
    pop_ok = len(odd6) == 12 and len(chiral_list) == 6 and len(vec_list) == 6 and (6 * 48 + 6 * 24 == 432)

    ok = sha_ok and i1_ok and i2_ok and ctrl_ok and pop_ok
    return {
        "row": 924,
        "commits": ["c9d03b925", "80a263a36"],
        "prereg_sha256": sha_hex,
        "population_per_route": len(chiral_list) * 48 + len(vec_list) * 24,
        "chiral_twins": chiral_list,
        "vector_like_twins": vec_list,
        "I1_m135_counts": i1_counts,
        "I2_ok": i2_ok,
        "pre_seal_controls_and_I3_all_zero": ctrl_ok,
        "result": "the same" if ok else "differs",
    }


def verify_row_925() -> dict[str, object]:
    """Row 925 (@ 94aa48ea8): relay ledger note on B1601 ((0,0,0) mod 3 -> 2T / A_4; +LLLR hyperbolic vs spin)."""
    # Over F_3, Qa = [[0, 2], [1, 0]], Qb = [[1, 1], [1, 2]] in SL(2, F_3)
    Qa = ((0, 2), (1, 0))
    Qb = ((1, 1), (1, 2))

    def m3(X, Y):
        return (
            ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0]) % 3, (X[0][0] * Y[0][1] + X[0][1] * Y[1][1]) % 3),
            ((X[1][0] * Y[0][0] + X[1][1] * Y[1][0]) % 3, (X[1][0] * Y[0][1] + X[1][1] * Y[1][1]) % 3),
        )

    Qab = m3(Qa, Qb)
    traces_f3 = ((Qa[0][0] + Qa[1][1]) % 3, (Qb[0][0] + Qb[1][1]) % 3, (Qab[0][0] + Qab[1][1]) % 3)
    I_f3 = ((1, 0), (0, 1))
    seen_sl2 = {I_f3}
    q = deque([I_f3])
    while q:
        cur = q.popleft()
        for g in (Qa, Qb):
            nxt = m3(cur, g)
            if nxt not in seen_sl2:
                seen_sl2.add(nxt)
                q.append(nxt)
    psl2 = {min(g, tuple(tuple((-x) % 3 for x in r) for r in g)) for g in seen_sl2}

    # Forced A_4 cover of +LLLR at hyperbolic holonomy (order dividing 4): verify 0 interior members
    M_lllr = homology_mat("+", "LLLR")
    M2 = ((M_lllr[0][0] % 2, M_lllr[0][1] % 2), (M_lllr[1][0] % 2, M_lllr[1][1] % 2))

    def app_m2(v, k_r):
        vx, vy = v
        for _ in range(k_r % 3):
            vx, vy = (M2[0][0] * vx + M2[0][1] * vy) % 2, (M2[1][0] * vx + M2[1][1] * vy) % 2
        return (vx, vy)

    elems_a4 = [((vx, vy), r) for r in range(3) for vy in range(2) for vx in range(2)]
    emap_a4 = {el: i for i, el in enumerate(elems_a4)}

    def mul_a4(e1, e2):
        (v1, r1), (v2, r2) = e1, e2
        w_v = app_m2(v2, r1)
        return (((v1[0] + w_v[0]) % 2, (v1[1] + w_v[1]) % 2), (r1 + r2) % 3)

    cov_a4 = build_cover(
        "+",
        "LLLR",
        12,
        {
            "a": [emap_a4[mul_a4(el, ((1, 0), 0))] for el in elems_a4],
            "b": [emap_a4[mul_a4(el, ((0, 1), 0))] for el in elems_a4],
            "t": [emap_a4[mul_a4(el, ((0, 0), 1))] for el in elems_a4],
        },
    )
    hol_lllr = get_holonomy("+", "LLLR")
    gm4, gm4_inv = hol_lllr["gm4"], hol_lllr["gm4_inv"]
    z0, one = gmpy2.mpc(0), gmpy2.mpc(1)
    gen_m0, gen_i0 = [], []
    for gw in cov_a4["gen_words"]:
        R = [[one if i == j else z0 for j in range(4)] for i in range(4)]
        for ch in gw:
            R = gm_matmul(R, gm4[ch] if ch in "abt" else gm4_inv[ch.lower()])
        gen_m0.append(R)
        gen_i0.append(gm_inv(R))
    roots4 = gm_roots_of_unity(4)
    hyp_members_lllr = 0
    for c_ch in cover_characters(cov_a4, 4):
        mc = [gm_scale(roots4[int(c_ch[j]) % 4], gen_m0[j]) for j in range(len(gen_m0))]
        ic = [gm_scale(roots4[(-int(c_ch[j])) % 4], gen_i0[j]) for j in range(len(gen_i0))]
        if cohom_pres_gm(mc, ic, cov_a4["rels_idx"], cov_a4["cusps_idx"])[3] > 0:
            hyp_members_lllr += 1

    # Spin space V at tick 3 on +LLLR: 2 active eigenvalues (+i, -i) of multiplicity 3 each
    sp_obj = setup_spin_gf(20089)
    steps3, _, _ = steps_route2("+", "LLLR", 3)
    S3 = sp_obj["act_steps_6d"](steps3, 0)
    ii = int(sp_obj["ii"])
    p = 20089
    rk_pi = 6 - np_rank_gf((S3 - ii * np.eye(6, dtype=np.int64)) % p, p)
    rk_mi = 6 - np_rank_gf((S3 - ((-ii) % p) * np.eye(6, dtype=np.int64)) % p, p)

    ok = traces_f3 == (0, 0, 0) and len(seen_sl2) == 24 and len(psl2) == 12 and hyp_members_lllr == 0 and rk_pi == 3 and rk_mi == 3
    return {
        "row": 925,
        "commits": ["94aa48ea8"],
        "traces_mod_3": list(traces_f3),
        "sl2_f3_order_2T": len(seen_sl2),
        "psl2_f3_order_A4": len(psl2),
        "plus_LLLR_a4_hyperbolic_members": hyp_members_lllr,
        "plus_LLLR_tick3_spin_eigenspace_dims": [rk_pi, rk_mi],
        "result": "the same" if ok else "differs",
    }


def verify_row_926() -> dict[str, object]:
    """Row 926 (@ 09217e78a): sm:B1552 banked (864 readings = 0,0) + W11 (T2 intermediate dims, 1516 96th powers, 144 tick powers)."""
    odd6 = genesis_states(6, odd_only=True)
    tot_r1 = 0
    tot_r2 = 0
    all_zero = True
    t2_all_ok = True
    for sgn, w, _ in odd6:
        ev1 = _eval_b1552_state_route(sgn, w, 3, 1)
        ev2 = _eval_b1552_state_route(sgn, w, 3, 2)
        tot_r1 += int(ev1["n_readings"])
        tot_r2 += int(ev2["n_readings"])
        if not (ev1["all_zero"] and ev2["all_zero"]):
            all_zero = False
        if not (ev1["t2_ok"] and ev2["t2_ok"]):
            t2_all_ok = False

    # W11 checks (2) and (3) on 6D parity-twisted spin space V:
    # Check 96th power = I_6 across all 758 x 2 = 1516 (state, lift) pairs to length 12,
    # and tick-k act == (S_1)^k across all 24 x 2 x 3 = 144 (state, lift, tick) triples to length 6.
    p = 20089
    sp_obj = setup_spin_gf(p)
    act_6d = sp_obj["act_steps_6d"]
    I6 = np.eye(6, dtype=np.int64)

    def mat6_pow(M: np.ndarray, exp_n: int) -> np.ndarray:
        R = np.eye(6, dtype=np.int64)
        B = M.copy()
        e_cur = exp_n
        while e_cur > 0:
            if e_cur & 1:
                R = (R @ B) % p
            B = (B @ B) % p
            e_cur >>= 1
        return R

    states12 = genesis_states(12, odd_only=False)
    pow96_checked = 0
    pow96_ok = True
    for sgn, w, _ in states12:
        st1 = list(reversed(w)) + (["-"] if sgn == "-" else [])
        for lift_idx in (0, 1):
            S1 = act_6d(st1, lift_idx)
            pow96_checked += 1
            if not np.array_equal(mat6_pow(S1, 96), I6):
                pow96_ok = False

    QA_6, QB_6 = sp_obj["QA"], sp_obj["QB"]
    lift_2d_6 = sp_obj["lift_steps_2d"]
    pars_6 = [(1, 0), (0, 1), (1, 1)]

    def fox2_word(Ap: np.ndarray, Bp: np.ndarray, w_f: str) -> tuple[np.ndarray, np.ndarray]:
        Api = np_inv_gf(Ap, p)
        Bpi = np_inv_gf(Bp, p)
        Db = np.zeros((2, 2), dtype=np.int64)
        pre = np.eye(2, dtype=np.int64)
        for ch_f in w_f:
            if ch_f == "a":
                pre = (pre @ Ap) % p
            elif ch_f == "b":
                Db = (Db + pre) % p
                pre = (pre @ Bp) % p
            elif ch_f == "A":
                pre = (pre @ Api) % p
            elif ch_f == "B":
                pre = (pre @ Bpi) % p
                Db = (Db - pre) % p
        return Db, pre

    def direct_word_S6(img_d: dict[str, str], U_d: np.ndarray) -> np.ndarray:
        Ui_d = np_inv_gf(U_d, p)
        ea_a = (img_d["a"].count("a") - img_d["a"].count("A")) % 2
        eb_a = (img_d["a"].count("b") - img_d["a"].count("B")) % 2
        ea_b = (img_d["b"].count("a") - img_d["b"].count("A")) % 2
        eb_b = (img_d["b"].count("b") - img_d["b"].count("B")) % 2
        M6 = np.zeros((6, 6), dtype=np.int64)
        I2 = np.eye(2, dtype=np.int64)
        for s_i, ps in enumerate(pars_6):
            sa = p - 1 if ps[0] else 1
            sb = p - 1 if ps[1] else 1
            Ap = (sa * QA_6) % p
            Bp = (sb * QB_6) % p
            pd = ((ps[0] * ea_a + ps[1] * eb_a) % 2, (ps[0] * ea_b + ps[1] * eb_b) % 2)
            d_i = pars_6.index(pd)
            dsa = p - 1 if pd[0] else 1
            dsb = p - 1 if pd[1] else 1
            Ad = (dsa * QA_6) % p
            Bd = (dsb * QB_6) % p
            inv_AdI = np.array(
                [[pow(int((Ad[0, 0] - 1) % p), p - 2, p), 0], [0, pow(int((Ad[1, 1] - 1) % p), p - 2, p)]],
                dtype=np.int64,
            )
            Db_wa, Wa = fox2_word(Ap, Bp, img_d["a"])
            Db_wb, Wb = fox2_word(Ap, Bp, img_d["b"])
            if not (np.array_equal((U_d @ Ad @ Ui_d) % p, Wa) and np.array_equal((U_d @ Bd @ Ui_d) % p, Wb)):
                sys.exit(2)
            for col in range(2):
                cb = np.array([1 if col == 0 else 0, 1 if col == 1 else 0], dtype=np.int64)
                na = (Ui_d @ ((Db_wa @ cb) % p)) % p
                nb = (Ui_d @ ((Db_wb @ cb) % p)) % p
                v = (-inv_AdI @ na) % p
                fb = (nb + ((Bd - I2) % p) @ v) % p
                M6[2 * d_i : 2 * d_i + 2, 2 * s_i + col] = fb
        return M6

    states6 = genesis_states(6, odd_only=False)
    tick_pow_checked = 0
    tick_pow_ok = True
    for sgn, w, _ in states6:
        st1 = list(reversed(w)) + (["-"] if sgn == "-" else [])
        img1 = phi1_words(sgn, w)
        for lift_idx in (0, 1):
            U1 = lift_2d_6(st1, lift_idx)
            S1 = act_6d(st1, lift_idx)
            if not np.array_equal(direct_word_S6(img1, U1), S1):
                tick_pow_ok = False
            Uk = np.eye(2, dtype=np.int64)
            for k_t in (1, 2, 3):
                Uk = (Uk @ U1) % p
                Sk = direct_word_S6(iter_phi(sgn, w, k_t), Uk)
                tick_pow_checked += 1
                if not np.array_equal(Sk, mat6_pow(S1, k_t)):
                    tick_pow_ok = False

    ok = (
        tot_r1 == 432
        and tot_r2 == 432
        and all_zero
        and t2_all_ok
        and pow96_checked == 1516
        and pow96_ok
        and tick_pow_checked == 144
        and tick_pow_ok
    )
    return {
        "row": 926,
        "commits": ["09217e78a"],
        "route_1_readings": tot_r1,
        "route_2_readings": tot_r2,
        "total_sealed_readings": tot_r1 + tot_r2,
        "all_counts_zero": all_zero,
        "t2_intermediate_cohomology_ok": t2_all_ok,
        "w11_pow96_checked": pow96_checked,
        "w11_pow96_ok": pow96_ok,
        "w11_tick_powers_checked": tick_pow_checked,
        "w11_tick_powers_ok": tick_pow_ok,
        "result": "the same" if ok else "differs",
    }


def verify_row_927() -> dict[str, object]:
    """Row 927 (@ 3a01ae3aa): W12 joined vacuum A = lambda x rho_hyp x rho_Q across 24 states to length 6."""
    states6 = genesis_states(6, odd_only=False)
    roots24 = gm_roots_of_unity(24)
    ctrl_c7 = gm_roots_of_unity(7)[1]
    ctrl_c2 = gmpy2.mpc(2)

    z0, one = gmpy2.mpc(0), gmpy2.mpc(1)
    ii_gm = gmpy2.mpc(0, 1)
    sq2_inv = one / gmpy2.sqrt(gmpy2.mpfr(2))
    QA_gm = [[ii_gm, z0], [z0, -ii_gm]]
    QB_gm = [[z0, one], [-one, z0]]
    UL_gm = [[sq2_inv, -sq2_inv], [sq2_inv, sq2_inv]]
    UR_gm = [[(one - ii_gm) * sq2_inv, z0], [z0, (one + ii_gm) * sq2_inv]]
    UN_gm = gm_matmul(QA_gm, QB_gm)

    def lift_gm(steps: list[str], lift_idx: int) -> GMMat:
        U = [[one, z0], [z0, one]]
        for st in steps:
            U = gm_matmul(UL_gm if st == "L" else UR_gm if st == "R" else UN_gm, U)
        return gm_neg(U) if lift_idx == 1 else U

    state_tick_pairs = 0
    active_readings = 0
    control_readings = 0
    active_ok = True
    controls_ok = True

    for sgn, w, M in states6:
        hol = get_holonomy(sgn, w)
        Ah, Bh, Th = hol["gm2"]["a"], hol["gm2"]["b"], hol["gm2"]["t"]
        Ahi, Bhi, Thi = hol["gm2_inv"]["a"], hol["gm2_inv"]["b"], hol["gm2_inv"]["t"]
        k_res = resolving_tick(M)
        ticks = [1] if k_res == 1 else [1, k_res]
        for k_t in ticks:
            state_tick_pairs += 1
            steps_k, mu_k, _ = steps_route2(sgn, w, k_t)
            Mk = mat2_pow(M, k_t)
            valid_pars = [
                (pa, pb)
                for pa in (0, 1)
                for pb in (0, 1)
                if (pa * Mk[0][0] + pb * Mk[1][0]) % 2 == pa and (pa * Mk[0][1] + pb * Mk[1][1]) % 2 == pb
            ]
            # Tk for rho_hyp in Route 2 (<a, b, t | t x t^-1 = phi^k(x)>): Tk = (Th)^k!
            Th_k = [[one, z0], [z0, one]]
            for _ in range(k_t):
                Th_k = gm_matmul(Th_k, Th)
            Th_ki = gm_inv(Th_k)

            u_part = mu_k[:-1]
            for sgn_T in (1, -1):
                Th_s = gm_neg(Th_k) if sgn_T == -1 else Th_k
                Th_si = gm_neg(Th_ki) if sgn_T == -1 else Th_ki
                for lift_idx in (0, 1):
                    Uq = lift_gm(steps_k, lift_idx)
                    Uqi = gm_inv(Uq)
                    base_a = gm_kron(Ah, QA_gm)
                    base_b = gm_kron(Bh, QB_gm)
                    base_t = gm_kron(Th_s, Uq)
                    base_ai = gm_kron(Ahi, gm_inv(QA_gm))
                    base_bi = gm_kron(Bhi, gm_inv(QB_gm))
                    base_ti = gm_kron(Th_si, Uqi)

                    for pa, pb in valid_pars:
                        sa = gmpy2.mpc(-1 if pa else 1)
                        sb = gmpy2.mpc(-1 if pb else 1)
                        lu = one
                        for ch in u_part:
                            lu *= sa if ch in "aA" else sb
                        Ma = gm_scale(sa, base_a)
                        Mb = gm_scale(sb, base_b)
                        Mai = gm_scale(sa, base_ai)
                        Mbi = gm_scale(sb, base_bi)
                        # Peripheral ell = abAB is independent of kappa; precompute W_mu0 at kappa = 1 (lt = lu^-1):
                        Mt0 = gm_scale(one / lu, base_t)
                        Mti0 = gm_scale(lu, base_ti)
                        _, W_ell = fox_word_gm({"a": Ma, "b": Mb, "t": Mt0}, {"a": Mai, "b": Mbi, "t": Mti0}, "abAB")
                        _, W_mu0 = fox_word_gm({"a": Ma, "b": Mb, "t": Mt0}, {"a": Mai, "b": Mbi, "t": Mti0}, mu_k)
                        I4 = [[one if i == j else z0 for j in range(4)] for i in range(4)]
                        B_ell = gm_sub(W_ell, I4)

                        for kap in roots24:
                            # Quick peripheral h0(T; A) check before full Fox solve:
                            BP_k = B_ell + gm_sub(gm_scale(kap, W_mu0), I4)
                            rBP_k, _ = gm_rank_and_nullspace(BP_k, 8, 4, want_null=False)
                            h0_tor = 4 - rBP_k
                            if h0_tor == 0:
                                continue
                            lt = kap / lu
                            mats = {"a": Ma, "b": Mb, "t": gm_scale(lt, base_t)}
                            invs = {"a": Mai, "b": Mbi, "t": gm_scale(one / lt, base_ti)}
                            h0, h1, r1, n, h0_t_chk = cohom_steps_gm(mats, invs, steps_k, "abAB", mu_k)
                            active_readings += 1
                            if not (n == 0 and h1 == r1 and r1 == h0_t_chk and h0_t_chk == h0_tor):
                                active_ok = False

                        for kap_ctrl in (ctrl_c7, ctrl_c2):
                            lt = kap_ctrl / lu
                            mats = {"a": Ma, "b": Mb, "t": gm_scale(lt, base_t)}
                            invs = {"a": Mai, "b": Mbi, "t": gm_scale(one / lt, base_ti)}
                            _, h1_c, _, _, _ = cohom_steps_gm(mats, invs, steps_k, "abAB", mu_k)
                            control_readings += 1
                            if h1_c != 0:
                                controls_ok = False

    ok = (
        state_tick_pairs == 44
        and active_readings == 736
        and control_readings == 992
        and active_ok
        and controls_ok
    )
    return {
        "row": 927,
        "commits": ["3a01ae3aa"],
        "state_tick_pairs": state_tick_pairs,
        "active_readings": active_readings,
        "control_readings": control_readings,
        "active_n_zero_and_h1_eq_r1_eq_h0T": active_ok,
        "controls_h1_zero": controls_ok,
        "result": "the same" if ok else "differs",
    }


def verify_row_928() -> dict[str, object]:
    """Row 928 (@ f92faba59): W13 and W14 slope law and F-CI tick-3 census on all 12 odd-trace states to length 6."""
    odd6 = genesis_states(6, odd_only=True)
    expected_census = {
        "+LR": (16, 3, 48, 0, 48, {"3": 48}, 3),
        "-LR": (20, 5, 96, 0, 0, {"3": 96}, 3),
        "+LLLR": (108, 13, 72, 0, 24, {"3": 72}, 3),
        "-LLLR": (112, 18, 48, 0, 48, {"3": 48}, 3),
        "+LLLLLR": (320, 35, 720, 240, 48, {"3": 720}, 3),
        "-LLLLLR": (324, 41, 360, 0, 96, {"3": 360}, 3),
        "+LLLRLR": (2156, 217, 144, 72, 0, {"3": 144}, 3),
        "-LLLRLR": (2160, 198, 2776, 1216, 1744, {"1": 16, "3": 2760}, 3),
        "+LLLRRR": (1296, 115, 1584, 288, 1296, {"3": 1584}, 67),
        "-LLLRRR": (1300, 139, 720, 408, 0, {"3": 720}, 3),
        "+LLRLRR": (3328, 553, 0, 0, 0, {}, 15),
        "-LLRLRR": (3332, 555, 0, 0, 0, {}, 3),
    }

    census_out: dict[str, object] = {}
    all_census_ok = True
    engine_mismatches: dict[str, int] = {}

    for sgn, w, _ in odd6:
        label = sgn + w
        res = slope_table_and_census(sgn, w)
        exp_t = expected_census[label]
        got_t = (
            res["ordG"],
            res["distinct_slopes"],
            res["gen_count"],
            res["lift_count"],
            res["nuc_count"],
            res["orb_hist"],
            res["parity_slope_class_size"],
        )
        signs_balanced = res["pos_count"] == res["neg_count"] and (res["pos_count"] + res["neg_count"] == res["gen_count"])
        par_silent = res["parity_module_firings"] == 0 and res["parity_bg_firings"] == 0
        if got_t != exp_t or not signs_balanced or not par_silent:
            all_census_ok = False
        census_out[label] = {
            "ordG": res["ordG"],
            "distinct_slopes": res["distinct_slopes"],
            "generation_shaped": res["gen_count"],
            "lifted": res["lift_count"],
            "nuc_same_sign": res["nuc_count"],
            "pos_neg": [res["pos_count"], res["neg_count"]],
            "orb_hist": res["orb_hist"],
            "parity_slope_class_size": res["parity_slope_class_size"],
            "parity_firings": res["parity_module_firings"],
        }

        # Direct GF(p) Fox engine check on EVERY module of +-LR and +-LLLR (256 + 400 + 11664 + 12544), plus 300 sampled modules of +LLRLRR:
        ordG = int(res["ordG"])
        zero_i = int(res["zero_i"])
        idx_law = res["idx_law"]
        direct_eng = res["direct_engine_index"]
        if label in ("+LR", "-LR", "+LLLR", "-LLLR"):
            mm = 0
            checked = 0
            for lam in range(ordG):
                for alp in range(ordG):
                    checked += 1
                    if direct_eng(lam, alp) != idx_law(lam, alp):
                        mm += 1
            engine_mismatches[label] = mm
            if mm != 0 or checked != ordG * ordG:
                all_census_ok = False
        elif label == "+LLRLRR":
            firing_pairs = []
            silent_pairs = []
            for lam in range(ordG):
                if lam == zero_i:
                    continue
                for alp in range(ordG):
                    if idx_law(lam, alp) != 0:
                        if len(firing_pairs) < 60:
                            firing_pairs.append((lam, alp))
                    else:
                        if len(silent_pairs) < 240 and (lam * 7 + alp * 13) % 19 == 0:
                            silent_pairs.append((lam, alp))
                if len(firing_pairs) >= 60 and len(silent_pairs) >= 240:
                    break
            sample = firing_pairs + silent_pairs
            mm = sum(1 for lam, alp in sample if direct_eng(lam, alp) != idx_law(lam, alp))
            engine_mismatches[label] = mm
            if mm != 0 or len(sample) != 300 or len(firing_pairs) != 60:
                all_census_ok = False

    return {
        "row": 928,
        "commits": ["f92faba59"],
        "census": census_out,
        "engine_mismatches": engine_mismatches,
        "all_census_and_law_checks_ok": all_census_ok,
        "result": "the same" if all_census_ok else "differs",
    }


# ---------------------------------------------------------------------------
# 7. Row verifiers (929, 930, 931, 934) and sealed main runner
# ---------------------------------------------------------------------------

def verify_row_929() -> dict[str, object]:
    """Row 929 (@ d2b8dc5b2): W15 Theorem H, rank-3 weave extensions, Part 2 prediction test, and rank-5 weave's five."""
    p = 20089
    sp_obj = setup_spin_gf(p)
    SL, SR, SN, SP = sp_obj["SL"], sp_obj["SR"], sp_obj["SN"], sp_obj["SP"]
    act_6d = sp_obj["act_steps_6d"]
    zeta8 = int(sp_obj["zeta8"])
    zeta24 = int(sp_obj["zeta24"])
    ii = int(sp_obj["ii"])
    negI6 = ((p - 1) * np.eye(6, dtype=np.int64)) % p

    def group_order_6d(gens: list[np.ndarray]) -> int:
        I6_b = np.eye(6, dtype=np.int64).tobytes()
        seen = {I6_b}
        q = deque([np.eye(6, dtype=np.int64)])
        while q:
            cur = q.popleft()
            for g in gens:
                nxt = (g @ cur) % p
                kb = nxt.tobytes()
                if kb not in seen:
                    seen.add(kb)
                    q.append(nxt)
        return len(seen)

    ord_moves = group_order_6d([SL, SR, SN, negI6])
    ord_with_swap = group_order_6d([SL, SR, SN, SP, negI6])

    # Split V into 3D irreps T and T_bar using (-LR)^3 eigenspaces (+i and -i):
    S_mLR3 = act_6d(["R", "L", "-"] * 3, 0)
    idx_pi = [idx for idx in range(6) if S_mLR3[idx, idx] == ii and np.count_nonzero(S_mLR3[idx]) == 1]
    idx_mi = [idx for idx in range(6) if S_mLR3[idx, idx] == ((-ii) % p) and np.count_nonzero(S_mLR3[idx]) == 1]
    if len(idx_pi) != 3 or len(idx_mi) != 3:
        sys.exit(2)

    def det3_mod(M3: np.ndarray) -> int:
        a, b, c = M3[0]
        d, e, f = M3[1]
        g, h, k = M3[2]
        return int(a * (e * k - f * h) - b * (d * k - f * g) + c * (d * h - e * g)) % p

    eighths_map = {pow(zeta8, k, p): k for k in range(8)}
    # Pick T vs T_bar so det(L|_T) in eighths is {1, 5}:
    dL_pi = eighths_map[det3_mod(SL[np.ix_(idx_pi, idx_pi)])]
    if dL_pi in (1, 5):
        T_idx, Tb_idx = idx_pi, idx_mi
    else:
        T_idx, Tb_idx = idx_mi, idx_pi

    # Check (i) one line per parity block (0..1, 2..3, 4..5), (ii) monomial on T & T_bar, (vi) SP exchanges T and T_bar:
    one_line_per_parity = sorted(i // 2 for i in T_idx) == [0, 1, 2] and sorted(i // 2 for i in Tb_idx) == [0, 1, 2]
    invariance_and_monomial_ok = True
    for G6 in (SL, SR, SN):
        if np.any(G6[np.ix_(T_idx, Tb_idx)]) or np.any(G6[np.ix_(Tb_idx, T_idx)]):
            invariance_and_monomial_ok = False
        GT = G6[np.ix_(T_idx, T_idx)]
        if any(np.count_nonzero(GT[r, :]) != 1 or np.count_nonzero(GT[:, r]) != 1 for r in range(3)):
            invariance_and_monomial_ok = False
    swap_exchanges = (not np.any(SP[np.ix_(T_idx, T_idx)])) and (not np.any(SP[np.ix_(Tb_idx, Tb_idx)]))

    # Check commutant dimension of <SL, SR, SN> on V is 2:
    # A 6x6 matrix X commutes with SL, SR, SN: build 3*36 x 36 system over GF(p)
    comm_rows = []
    for G6 in (SL, SR, SN):
        # G6 X - X G6 = 0 => (G6 (x) I - I (x) G6^T) vec(X) = 0
        I6 = np.eye(6, dtype=np.int64)
        comm_rows.append((np.kron(G6, I6) - np.kron(I6, G6.T)) % p)
    comm_dim = 36 - np_rank_gf(np.vstack(comm_rows), p)

    det_L_eighths = sorted(eighths_map[det3_mod(((1 if lf == 0 else p - 1) * SL[np.ix_(T_idx, T_idx)]) % p)] for lf in (0, 1))
    det_R_eighths = sorted(eighths_map[det3_mod(((1 if lf == 0 else p - 1) * SR[np.ix_(T_idx, T_idx)]) % p)] for lf in (0, 1))
    det_N_eighths = sorted(eighths_map[det3_mod(((1 if lf == 0 else p - 1) * SN[np.ix_(T_idx, T_idx)]) % p)] for lf in (0, 1))

    # Check (iii) direct tick-3 scalar action on all 32 odd-trace states to length 8:
    odd8 = genesis_states(8, odd_only=True)
    tick3_scalar_ok = True
    for sgn, w, _ in odd8:
        st1 = list(reversed(w)) + (["-"] if sgn == "-" else [])
        S1 = act_6d(st1, 0)
        S3 = act_6d(st1 * 3, 0)
        dT = det3_mod(S1[np.ix_(T_idx, T_idx)])
        dTb = det3_mod(S1[np.ix_(Tb_idx, Tb_idx)])
        if not (
            np.array_equal(S3[np.ix_(T_idx, T_idx)], (dT * np.eye(3, dtype=np.int64)) % p)
            and np.array_equal(S3[np.ix_(Tb_idx, Tb_idx)], (dTb * np.eye(3, dtype=np.int64)) % p)
        ):
            tick3_scalar_ok = False

    # Check (v) hand rule across all 326 odd-trace states among 758 states to length 12:
    odd12 = genesis_states(12, odd_only=True)
    hand_rule_ok = True
    chiral_by_word: Counter[str] = Counter()
    for sgn, w, _ in odd12:
        st1 = list(reversed(w)) + (["-"] if sgn == "-" else [])
        S1 = act_6d(st1, 0)
        dT = det3_mod(S1[np.ix_(T_idx, T_idx)])
        is_chiral_det = dT in (ii, (-ii) % p)
        is_chiral_rule = ((w.count("L") - w.count("R") + (2 if sgn == "-" else 0)) % 4) == 2
        if is_chiral_det != is_chiral_rule:
            hand_rule_ok = False
        if is_chiral_det:
            chiral_by_word[w] += 1
    twins_split_163 = len(odd12) == 326 and len(chiral_by_word) == 163 and all(v == 1 for v in chiral_by_word.values())

    thm_h_ok = (
        ord_moves == 96
        and ord_with_swap == 192
        and comm_dim == 2
        and one_line_per_parity
        and invariance_and_monomial_ok
        and swap_exchanges
        and det_L_eighths == [1, 5]
        and det_R_eighths == [3, 7]
        and det_N_eighths == [2, 6]
        and len(odd8) == 32
        and tick3_scalar_ok
        and hand_rule_ok
        and twins_split_163
    )

    # Rank-3 weave extensions X = [[A, c * B_p], [0, B_p]]
    def run_rank3_extensions(states_list, q_list, k24_list, prime_p: int) -> tuple[int, Counter[int], dict[str, Counter[int]]]:
        sp_p = setup_spin_gf(prime_p)
        QA_p, QB_p = sp_p["QA"], sp_p["QB"]
        QAi_p, QBi_p = sp_p["QAi"], sp_p["QBi"]
        z24_p = int(sp_p["zeta24"])
        lift_p = sp_p["lift_steps_2d"]
        pars_nz = [(1, 0), (0, 1), (1, 1)]
        tot = 0
        hist: Counter[int] = Counter()
        per_state: dict[str, Counter[int]] = {}
        for sgn, w, _ in states_list:
            lbl = sgn + w
            per_state[lbl] = Counter()
            steps3, mu3, _ = steps_route2(sgn, w, 3)
            u3_part = mu3[:-1]
            U3 = lift_p(steps3, 0)
            U3i = np_inv_gf(U3, prime_p)
            for par_p in pars_nz:
                bp_a = prime_p - 1 if par_p[0] else 1
                bp_b = prime_p - 1 if par_p[1] else 1
                bp_t = 1
                for ch in u3_part:
                    bp_t = (bp_t * (bp_a if ch in "aA" else bp_b)) % prime_p
                bp_vals = {"a": bp_a, "b": bp_b, "t": bp_t}
                for par_q in q_list:
                    qa_s = prime_p - 1 if par_q[0] else 1
                    qb_s = prime_p - 1 if par_q[1] else 1
                    qt_u = 1
                    for ch in u3_part:
                        qt_u = (qt_u * (qa_s if ch in "aA" else qb_s)) % prime_p
                    Aa = (qa_s * QA_p) % prime_p
                    Ab = (qb_s * QB_p) % prime_p
                    Aai = (qa_s * QAi_p) % prime_p
                    Abi = (qb_s * QBi_p) % prime_p
                    for k24 in k24_list:
                        kap = pow(z24_p, k24, prime_p)
                        # A(mu_3) = kap * rho_Q(mu_3)? Note kap * qt_u * U3 covers the same roots of unity:
                        At = ((kap * qt_u) % prime_p * U3) % prime_p
                        Ati = (pow((kap * qt_u) % prime_p, prime_p - 2, prime_p) * U3i) % prime_p
                        A_m = {"a": Aa, "b": Ab, "t": At}
                        A_i = {"a": Aai, "b": Abi, "t": Ati}
                        # Hom(B_p, A) = A (x) B_p^-1 (note B_p^-1 = B_p since order 2!):
                        hom_m = {g: (bp_vals[g] * A_m[g]) % prime_p for g in "abt"}
                        hom_i = {g: (bp_vals[g] * A_i[g]) % prime_p for g in "abt"}
                        _, h1_g, _, _, cocs = cohom_steps_np_gf(hom_m, hom_i, steps3, "abAB", mu3, prime_p, want_cocs=True)
                        if h1_g == 0:
                            continue
                        draws_c = list(cocs)
                        if h1_g >= 2:
                            gen_c = np.zeros_like(cocs[0])
                            for ic, zc in enumerate(cocs):
                                gen_c = (gen_c + pow(z24_p, 5 * ic + 1, prime_p) * zc) % prime_p
                            draws_c.append(gen_c)
                        for cv in draws_c:
                            X_m: dict[str, np.ndarray] = {}
                            X_i: dict[str, np.ndarray] = {}
                            for gi, g in enumerate("abt"):
                                cg = cv[2 * gi : 2 * (gi + 1)].reshape(2, 1)
                                bpg = bp_vals[g]
                                cBp = (cg * bpg) % prime_p
                                neg_Aic = ((-A_i[g] @ cg) % prime_p)
                                M3x = np.block([[A_m[g], cBp], [np.zeros((1, 2), dtype=np.int64), np.array([[bpg]], dtype=np.int64)]]) % prime_p
                                M3xi = np.block([[A_i[g], neg_Aic], [np.zeros((1, 2), dtype=np.int64), np.array([[bpg]], dtype=np.int64)]]) % prime_p
                                X_m[g], X_i[g] = M3x, M3xi
                            t_X, t_Xs = verify_b1604_e1_duality_gf(X_m, X_i, steps3, "abAB", mu3, prime_p)
                            ix = t_X[3] - t_Xs[3]
                            tot += 1
                            hist[ix] += 1
                            per_state[lbl][ix] += 1
        return tot, hist, per_state

    odd6 = genesis_states(6, odd_only=True)
    all_q = [(0, 0), (1, 0), (0, 1), (1, 1)]
    tot_a, hist_a, per_a = run_rank3_extensions(odd6, all_q, list(range(24)), 20089)
    ext_a_ok = (
        tot_a == 360
        and hist_a == Counter({1: 300, 0: 60})
        and per_a["+LLRLRR"] == Counter({0: 30})
        and per_a["-LLRLRR"] == Counter({0: 30})
    )

    # (b) Two further primes 50329 and 90073 on +-LR and +-LLRLRR
    sub_b_states = [s for s in odd6 if (s[0] + s[1]) in ("+LR", "-LR", "+LLRLRR", "-LLRLRR")]
    ext_b_ok = True
    for p_alt in (50329, 90073):
        tb, hb, pb = run_rank3_extensions(sub_b_states, all_q, list(range(24)), p_alt)
        if not (tb == 120 and hb == Counter({1: 60, 0: 60}) and pb["+LLRLRR"] == Counter({0: 30}) and pb["-LLRLRR"] == Counter({0: 30})):
            ext_b_ok = False

    # (c) Length 8 (20 states), reduced rule q = (0,0), kappa in mu_4 (k24 in 0, 6, 12, 18)
    just8 = [s for s in odd8 if len(s[1]) == 8]
    tot_c, hist_c, per_c = run_rank3_extensions(just8, [(0, 0)], [0, 6, 12, 18], 20089)
    ext_c_ok = (
        len(just8) == 20
        and tot_c == 150
        and hist_c == Counter({1: 135, 0: 15})
        and per_c["+LLLLLRRR"] + per_c["-LLLLLRRR"] == Counter({0: 15})
    )

    # Mod-16 equivalence on all 32 odd-trace states to length 8:
    mod16_states = []
    mod16_equiv_ok = True
    for sgn, w, M in odd8:
        tr = M[0][0] + M[1][1]
        M3 = mat2_pow(M, 3)
        m3_pm_I = (
            (M3[0][0] - 1) % 16 == 0 and M3[0][1] % 16 == 0 and M3[1][0] % 16 == 0 and (M3[1][1] - 1) % 16 == 0
        ) or (
            (M3[0][0] + 1) % 16 == 0 and M3[0][1] % 16 == 0 and M3[1][0] % 16 == 0 and (M3[1][1] + 1) % 16 == 0
        )
        tr_pm_1 = (tr % 16) in (1, 15)
        if m3_pm_I != tr_pm_1:
            mod16_equiv_ok = False
        if m3_pm_I:
            mod16_states.append(sgn + w)
    mod16_ok = mod16_equiv_ok and sorted(mod16_states) == ["+LLLLLRRR", "+LLRLRR", "-LLLLLRRR", "-LLRLRR"]

    # Part 2 prediction test: F-CI at tick 3 on +-LLLLLRRR and +-LLLLLLLR
    pred_p_lllrrr = slope_table_and_census("+", "LLLLLRRR")
    pred_m_lllrrr = slope_table_and_census("-", "LLLLLRRR")
    pred_p_lllllr = slope_table_and_census("+", "LLLLLLLR")
    pred_m_lllllr = slope_table_and_census("-", "LLLLLLLR")
    pred_test_ok = (
        pred_p_lllrrr["gen_count"] == 3064
        and pred_p_lllrrr["orb_hist"] == {"1": 16, "3": 3048}
        and pred_m_lllrrr["gen_count"] == 336
        and pred_p_lllllr["gen_count"] == 480
        and pred_m_lllllr["gen_count"] == 336
    )

    # Rank-5 weave's five at tick 3 across all 12 odd-trace states to length 6 over GF(20089):
    QA_0, QB_0 = sp_obj["QA"], sp_obj["QB"]
    QAi_0, QBi_0 = sp_obj["QAi"], sp_obj["QBi"]
    lift_0 = sp_obj["lift_steps_2d"]
    pars_nz = [(1, 0), (0, 1), (1, 1)]
    five_by_state: dict[str, list[list[int]]] = {}
    five_ok = True
    for sgn, w, _ in odd6:
        lbl = sgn + w
        steps3, mu3, _ = steps_route2(sgn, w, 3)
        u3_part = mu3[:-1]
        U3 = lift_0(steps3, 0)
        U3i = np_inv_gf(U3, p)
        bp_list = []
        for par_p in pars_nz:
            bpa = p - 1 if par_p[0] else 1
            bpb = p - 1 if par_p[1] else 1
            bpt = 1
            for ch in u3_part:
                bpt = (bpt * (bpa if ch in "aA" else bpb)) % p
            bp_list.append({"a": bpa, "b": bpb, "t": bpt})
        B3_m = {g: np.diag([bp_list[0][g], bp_list[1][g], bp_list[2][g]]).astype(np.int64) for g in "abt"}
        pairs_seen: set[tuple[int, int]] = set()
        for k24 in range(24):
            kap = pow(zeta24, k24, p)
            At = (kap * U3) % p
            Ati = (pow(kap, p - 2, p) * U3i) % p
            A_m = {"a": QA_0, "b": QB_0, "t": At}
            A_i = {"a": QAi_0, "b": QBi_0, "t": Ati}
            cocs_per_p = []
            ok_all3 = True
            for j_p in range(3):
                hom_m = {g: (bp_list[j_p][g] * A_m[g]) % p for g in "abt"}
                hom_i = {g: (bp_list[j_p][g] * A_i[g]) % p for g in "abt"}
                _, h1_p, _, _, cs_p = cohom_steps_np_gf(hom_m, hom_i, steps3, "abAB", mu3, p, want_cocs=True)
                if h1_p == 0:
                    ok_all3 = False
                    break
                cocs_per_p.append(cs_p)
            if not ok_all3:
                continue
            combos: list[tuple[np.ndarray, np.ndarray, np.ndarray]] = []
            for t0, t1, t2 in itertools.product(*cocs_per_p):
                combos.append((t0, t1, t2))
            if len(cocs_per_p[0]) >= 2:
                g_tri = tuple(
                    (cs_p[0] + pow(zeta24, 3 * j_p + 1, p) * cs_p[1]) % p
                    for j_p, cs_p in enumerate(cocs_per_p)
                )
                combos.append(g_tri)  # type: ignore[arg-type]
            for c1, c2, c3 in combos:
                W_m: dict[str, np.ndarray] = {}
                W_i: dict[str, np.ndarray] = {}
                L2_m: dict[str, np.ndarray] = {}
                L2_i: dict[str, np.ndarray] = {}
                for gi, g in enumerate("abt"):
                    C_blk = np.column_stack([
                        c1[2 * gi : 2 * (gi + 1)],
                        c2[2 * gi : 2 * (gi + 1)],
                        c3[2 * gi : 2 * (gi + 1)],
                    ]) % p
                    CB = (C_blk @ B3_m[g]) % p
                    neg_AiC = ((-A_i[g] @ C_blk) % p)
                    M5 = np.block([[A_m[g], CB], [np.zeros((3, 2), dtype=np.int64), B3_m[g]]]) % p
                    M5i = np.block([[A_i[g], neg_AiC], [np.zeros((3, 2), dtype=np.int64), B3_m[g]]]) % p
                    W_m[g], W_i[g] = M5, M5i
                    L2_m[g], L2_i[g] = wedge2_gf(M5, p), wedge2_gf(M5i, p)
                t_W, t_Ws = verify_b1604_e1_duality_gf(W_m, W_i, steps3, "abAB", mu3, p)
                t_L, t_Ls = verify_b1604_e1_duality_gf(L2_m, L2_i, steps3, "abAB", mu3, p)
                pairs_seen.add((t_W[3] - t_Ws[3], t_L[3] - t_Ls[3]))
        sorted_pairs = [list(pr) for pr in sorted(pairs_seen)]
        five_by_state[lbl] = sorted_pairs
        is_chiral = ((w.count("L") - w.count("R") + (2 if sgn == "-" else 0)) % 4) == 2
        if lbl in ("+LLRLRR", "-LLRLRR"):
            if sorted_pairs != [[0, 0]]:
                five_ok = False
        elif is_chiral:
            if sorted_pairs != [[1, 3]]:
                five_ok = False
        else:
            if sorted_pairs != [[1, 3], [2, 3]]:
                five_ok = False

    all_ok = thm_h_ok and ext_a_ok and ext_b_ok and ext_c_ok and mod16_ok and pred_test_ok and five_ok
    return {
        "row": 929,
        "commits": ["d2b8dc5b2"],
        "theorem_H": {
            "group_order_moves": ord_moves,
            "group_order_with_swap": ord_with_swap,
            "commutant_dim": comm_dim,
            "det_T_eighths": {"L": det_L_eighths, "R": det_R_eighths, "sign": det_N_eighths},
            "tick3_scalar_32_of_32": tick3_scalar_ok,
            "hand_rule_326_of_326": hand_rule_ok and twins_split_163,
        },
        "weave_extensions": {
            "part_a_360_readings": dict(hist_a),
            "part_b_alt_primes_ok": ext_b_ok,
            "part_c_150_readings_len8": dict(hist_c),
            "mod16_silent_states": sorted(mod16_states),
        },
        "prediction_test_F_CI": {
            "+LLLLLRRR": {"gen": pred_p_lllrrr["gen_count"], "orbits": pred_p_lllrrr["orb_hist"]},
            "-LLLLLRRR": {"gen": pred_m_lllrrr["gen_count"], "orbits": pred_m_lllrrr["orb_hist"]},
            "+LLLLLLLR": {"gen": pred_p_lllllr["gen_count"], "orbits": pred_p_lllllr["orb_hist"]},
            "-LLLLLLLR": {"gen": pred_m_lllllr["gen_count"], "orbits": pred_m_lllllr["orb_hist"]},
        },
        "weaves_five_tick3": five_by_state,
        "result": "the same" if all_ok else "differs",
    }


def verify_row_930() -> dict[str, object]:
    """Row 930 (@ ebd5f9fc4): W16 common point mod 3 across all 37 primitive unsigned words to length 8 + B1604."""
    words8 = unsigned_primitive_words(8)
    rows_out = []
    odd_count = 0
    even_count = 0
    odd_all_norm3_vals111 = True
    even_norms: Counter[int] = Counter()
    llllllrr_f3 = False
    llllrrrr_1024 = False

    for w in words8:
        rec = analyze_w16_word(w)
        rows_out.append(rec)
        if rec["odd_trace"]:
            odd_count += 1
            pfs = rec["prime_factors"]
            if not (
                len(pfs) == 1
                and pfs[0]["p"] == 3
                and pfs[0]["residue_degree"] == 1
                and pfs[0]["exponent"] == 1
                and pfs[0]["vals"] == [1, 1, 1]
                and rec["ideal_norm"] == 3
            ):
                odd_all_norm3_vals111 = False
        else:
            even_count += 1
            pfs = rec["prime_factors"]
            if not (len(pfs) == 1 and pfs[0]["p"] == 2):
                odd_all_norm3_vals111 = False
            even_norms[int(rec["ideal_norm"])] += 1
            if w == "LLLLLLRR" and pfs[0]["residue_degree"] == 3 and rec["ideal_norm"] == 64:
                llllllrr_f3 = True
            if w == "LLLLRRRR" and rec["ideal_norm"] == 1024:
                llllrrrr_1024 = True

    # Symbolic B1604 Euler characteristic & E1 / B1297 equivalence check:
    rk_sym = sp.Symbol("r", integer=True, positive=True)
    chi_pres = rk_sym * (1 - 3 + 2)
    h0_E, r1_E, n_E, t0_E = sp.symbols("h0_E r1_E n_E t0_E")
    h0_Es, r1_Es, n_Es, t0_Es = sp.symbols("h0_Es r1_Es n_Es t0_Es")
    h1_E = n_E + r1_E
    h1_Es = n_Es + r1_Es
    E1_E = h0_E - h1_E + n_Es + t0_Es - h0_Es
    E1_Es = h0_Es - h1_Es + n_E + t0_E - h0_E
    # E1_E - E1_Es == 2*(h0_E - h0_Es) - 2*(n_E - n_Es) - (r1_E - r1_Es) + (t0_Es - t0_E)
    diff_id = sp.simplify((E1_E - E1_Es) - (2 * (h0_E - h0_Es) - 2 * (n_E - n_Es) - (r1_E - r1_Es) + (t0_Es - t0_E)))
    sum_id = sp.simplify((E1_E + E1_Es) - ((t0_E + t0_Es) - (r1_E + r1_Es)))
    b1604_ok = (chi_pres == 0) and (diff_id == 0) and (sum_id == 0)

    ok = (
        len(words8) == 37
        and odd_count == 16
        and even_count == 21
        and odd_all_norm3_vals111
        and dict(even_norms) == {4: 8, 8: 7, 64: 5, 1024: 1}
        and llllllrr_f3
        and llllrrrr_1024
        and b1604_ok
    )
    return {
        "row": 930,
        "commits": ["ebd5f9fc4"],
        "total_geometries": len(words8),
        "odd_trace_count": odd_count,
        "even_trace_count": even_count,
        "odd_all_norm3_f1_e1_vals111": odd_all_norm3_vals111,
        "even_ideal_norm_histogram": {str(k): int(v) for k, v in sorted(even_norms.items())},
        "LLLLLLRR_residue_degree_3_norm_64": llllllrr_f3,
        "LLLLRRRR_norm_1024": llllrrrr_1024,
        "b1604_chi_zero_and_e1_equivalence": b1604_ok,
        "geometries": rows_out,
        "result": "the same" if ok else "differs",
    }


def verify_row_931() -> dict[str, object]:
    """Row 931 (@ 57e99a1d4): W17 (480 tick-1 rank-5 readings) and W18 (Route A vs Route B + projective-line scan at p=73, 97)."""
    p = 20089
    sp_obj = setup_spin_gf(p)
    QA, QB = sp_obj["QA"], sp_obj["QB"]
    QAi, QBi = sp_obj["QAi"], sp_obj["QBi"]
    PA, PB = sp_obj["PA"], sp_obj["PB"]
    PAi, PBi = sp_obj["PAi"], sp_obj["PBi"]
    ad3 = sp_obj["ad3"]
    lift_2d = sp_obj["lift_steps_2d"]
    zeta24 = int(sp_obj["zeta24"])
    omega = pow(zeta24, 8, p)
    omega2 = pow(zeta24, 16, p)

    odd8 = genesis_states(8, odd_only=True)
    mod16_set = {"+LLRLRR", "-LLRLRR", "+LLLLLRRR", "-LLLLLRRR"}
    w17_readings = 0
    w17_carriers_ok = True
    w17_chiral_ok = True
    w17_mod16_ok = True

    route_b_canonical_72 = 0
    route_b_total_checked = 0
    route_ab_agree = True
    w18_chiral_ok = True
    w18_mod16_ok = True
    w18_singlets_carriers_ok = True
    carriers_list: list[tuple[str, str]] = []

    for sgn, w, _ in odd8:
        lbl = sgn + w
        is_mod16 = lbl in mod16_set
        is_chiral = ((w.count("L") - w.count("R") + (2 if sgn == "-" else 0)) % 4) == 2
        if (not is_mod16) and (not is_chiral):
            carriers_list.append((sgn, w))

        steps1, mu1, _ = steps_route2(sgn, w, 1)
        u1_part = mu1[:-1]
        is_len6 = len(w) <= 6
        if is_len6:
            steps3, mu3, _ = steps_route2(sgn, w, 3)
            u3_part = mu3[:-1]

        first_nu_lift0_seen = False
        for lift_idx in (0, 1):
            Ut = lift_2d(steps1, lift_idx)
            Uti = np_inv_gf(Ut, p)
            Pt = ad3(Ut)
            Pti = np_inv_gf(Pt, p)
            P_sec = {"a": PA, "b": PB, "t": Pt}
            P_seci = {"a": PAi, "b": PBi, "t": Pti}

            for k_nu in range(24):
                nu_t = pow(zeta24, k_nu, p)
                nu5 = pow(nu_t, 5, p)
                D5 = {"a": QA, "b": QB, "t": (nu5 * Ut) % p}
                Ps = {"a": PAi.T, "b": PBi.T, "t": Pti.T}
                hom_m = {g: np.kron(D5[g], Ps[g]) % p for g in "abt"}
                hom_i = {g: np_inv_gf(hom_m[g], p) for g in "abt"}
                _, h1_g, _, _, cocs = cohom_steps_np_gf(hom_m, hom_i, steps1, "abAB", mu1, p, want_cocs=True)
                if h1_g == 0:
                    continue

                is_canonical_slice = is_len6 and (lift_idx == 0) and (not first_nu_lift0_seen)
                if lift_idx == 0 and not first_nu_lift0_seen:
                    first_nu_lift0_seen = True

                draws_c = list(cocs)
                if h1_g == 2:
                    draws_c.append((cocs[0] + zeta24 * cocs[1]) % p)
                elif h1_g != 1:
                    sys.exit(2)

                nu3 = pow(nu_t, 3, p)
                num2 = pow(nu_t, -2, p)
                D_tw = {"a": QA, "b": QB, "t": (nu3 * Ut) % p}
                D_twi = {"a": QAi, "b": QBi, "t": (pow(nu3, p - 2, p) * Uti) % p}
                P_tw = {"a": PA, "b": PB, "t": (num2 * Pt) % p}
                P_twi = {"a": PAi, "b": PBi, "t": (pow(num2, p - 2, p) * Pti) % p}

                for cv in draws_c:
                    W_m: dict[str, np.ndarray] = {}
                    W_i: dict[str, np.ndarray] = {}
                    L2_m: dict[str, np.ndarray] = {}
                    L2_i: dict[str, np.ndarray] = {}
                    for gi, g in enumerate("abt"):
                        cg = cv[6 * gi : 6 * (gi + 1)].reshape(2, 3)
                        cP = (cg @ P_tw[g]) % p
                        neg_Dic = ((-D_twi[g] @ cg) % p)
                        M5 = np.block([[D_tw[g], cP], [np.zeros((3, 2), dtype=np.int64), P_tw[g]]]) % p
                        M5i = np.block([[D_twi[g], neg_Dic], [np.zeros((3, 2), dtype=np.int64), P_twi[g]]]) % p
                        W_m[g], W_i[g] = M5, M5i
                        L2_m[g], L2_i[g] = wedge2_gf(M5, p), wedge2_gf(M5i, p)

                    t_W, t_Ws = verify_b1604_e1_duality_gf(W_m, W_i, steps1, "abAB", mu1, p)
                    t_L, t_Ls = verify_b1604_e1_duality_gf(L2_m, L2_i, steps1, "abAB", mu1, p)
                    pair_1 = (t_W[3] - t_Ws[3], t_L[3] - t_Ls[3])
                    w17_readings += 1

                    if is_mod16:
                        if pair_1 != (0, 0):
                            w17_mod16_ok = False
                    elif is_chiral:
                        if pair_1 != (0, 1):
                            w17_chiral_ok = False
                    else:
                        if pair_1 != (1, 1):
                            w17_carriers_ok = False

                    # W18 Route A: sectors 1, omega, omega^2, and P on M_1
                    singlet_pairs = [pair_1]
                    for om_t in (omega, omega2):
                        omi_t = pow(om_t, p - 2, p)
                        W_om = {"a": W_m["a"], "b": W_m["b"], "t": (om_t * W_m["t"]) % p}
                        Wi_om = {"a": W_i["a"], "b": W_i["b"], "t": (omi_t * W_i["t"]) % p}
                        L2_om = {"a": L2_m["a"], "b": L2_m["b"], "t": (om_t * L2_m["t"]) % p}
                        L2i_om = {"a": L2_i["a"], "b": L2_i["b"], "t": (omi_t * L2_i["t"]) % p}
                        tw_o, tws_o = verify_b1604_e1_duality_gf(W_om, Wi_om, steps1, "abAB", mu1, p)
                        tl_o, tls_o = verify_b1604_e1_duality_gf(L2_om, L2i_om, steps1, "abAB", mu1, p)
                        singlet_pairs.append((tw_o[3] - tws_o[3], tl_o[3] - tls_o[3]))

                    WP_m = {g: np.kron(W_m[g], P_sec[g]) % p for g in "abt"}
                    WP_i = {g: np.kron(W_i[g], P_seci[g]) % p for g in "abt"}
                    L2P_m = {g: np.kron(L2_m[g], P_sec[g]) % p for g in "abt"}
                    L2P_i = {g: np.kron(L2_i[g], P_seci[g]) % p for g in "abt"}
                    tw_p, tws_p = verify_b1604_e1_duality_gf(WP_m, WP_i, steps1, "abAB", mu1, p)
                    tl_p, tls_p = verify_b1604_e1_duality_gf(L2P_m, L2P_i, steps1, "abAB", mu1, p)
                    pair_P = (tw_p[3] - tws_p[3], tl_p[3] - tls_p[3])

                    if is_mod16:
                        if pair_P != (0, 0) or any(sp_pr != (0, 0) for sp_pr in singlet_pairs):
                            w18_mod16_ok = False
                    elif is_chiral:
                        if pair_P != (0, 2) or any(sp_pr != (0, 1) for sp_pr in singlet_pairs):
                            w18_chiral_ok = False
                    else:
                        if sorted(singlet_pairs) != [(0, 1), (0, 1), (1, 1)]:
                            w18_singlets_carriers_ok = False
                        if pair_P not in ((1, 1), (0, 1)):
                            w17_carriers_ok = False

                    # W18 Route B on all 12 length-6 states: pull back along t_tilde -> t^3 and twist by B_p
                    if is_len6:
                        Wt3 = (W_m["t"] @ W_m["t"] % p) @ W_m["t"] % p
                        Wt3i = (W_i["t"] @ W_i["t"] % p) @ W_i["t"] % p
                        L2t3 = wedge2_gf(Wt3, p)
                        L2t3i = wedge2_gf(Wt3i, p)
                        # Zero parity check (sum of 1, omega, omega^2):
                        W3_0 = {"a": W_m["a"], "b": W_m["b"], "t": Wt3}
                        W3i_0 = {"a": W_i["a"], "b": W_i["b"], "t": Wt3i}
                        L23_0 = {"a": L2_m["a"], "b": L2_m["b"], "t": L2t3}
                        L23i_0 = {"a": L2_i["a"], "b": L2_i["b"], "t": L2t3i}
                        tw0, tws0 = verify_b1604_e1_duality_gf(W3_0, W3i_0, steps3, "abAB", mu3, p)
                        tl0, tls0 = verify_b1604_e1_duality_gf(L23_0, L23i_0, steps3, "abAB", mu3, p)
                        sum_sing = (sum(x[0] for x in singlet_pairs), sum(x[1] for x in singlet_pairs))
                        if (tw0[3] - tws0[3], tl0[3] - tls0[3]) != sum_sing:
                            route_ab_agree = False

                        for par_p in [(1, 0), (0, 1), (1, 1)]:
                            bpa = p - 1 if par_p[0] else 1
                            bpb = p - 1 if par_p[1] else 1
                            bpt = 1
                            for ch in u3_part:
                                bpt = (bpt * (bpa if ch in "aA" else bpb)) % p
                            W3_p = {"a": (bpa * W_m["a"]) % p, "b": (bpb * W_m["b"]) % p, "t": (bpt * Wt3) % p}
                            W3i_p = {"a": (bpa * W_i["a"]) % p, "b": (bpb * W_i["b"]) % p, "t": (bpt * Wt3i) % p}
                            L23_p = {"a": (bpa * L2_m["a"]) % p, "b": (bpb * L2_m["b"]) % p, "t": (bpt * L2t3) % p}
                            L23i_p = {"a": (bpa * L2_i["a"]) % p, "b": (bpb * L2_i["b"]) % p, "t": (bpt * L2t3i) % p}
                            tw_b, tws_b = verify_b1604_e1_duality_gf(W3_p, W3i_p, steps3, "abAB", mu3, p)
                            tl_b, tls_b = verify_b1604_e1_duality_gf(L23_p, L23i_p, steps3, "abAB", mu3, p)
                            if (tw_b[3] - tws_b[3], tl_b[3] - tls_b[3]) != pair_P:
                                route_ab_agree = False
                            route_b_total_checked += 1
                            if is_canonical_slice:
                                route_b_canonical_72 += 1

    # Basis-independent projective-line scan at p = 73 and p = 97 across all 14 carriers:
    proj_scan_ok = len(carriers_list) == 14
    proj_summary: dict[str, dict[str, dict[str, int]]] = {}
    for p_sc in (73, 97):
        sp_sc = setup_spin_gf(p_sc)
        QA_s, QB_s = sp_sc["QA"], sp_sc["QB"]
        QAi_s, QBi_s = sp_sc["QAi"], sp_sc["QBi"]
        PA_s, PB_s = sp_sc["PA"], sp_sc["PB"]
        PAi_s, PBi_s = sp_sc["PAi"], sp_sc["PBi"]
        ad3_s = sp_sc["ad3"]
        lift_s = sp_sc["lift_steps_2d"]
        z24_s = int(sp_sc["zeta24"])
        proj_summary[str(p_sc)] = {}
        for sgn, w in carriers_list:
            steps1, mu1, _ = steps_route2(sgn, w, 1)
            Ut = lift_s(steps1, 0)
            Uti = np_inv_gf(Ut, p_sc)
            Pt = ad3_s(Ut)
            Pti = np_inv_gf(Pt, p_sc)
            P_sec = {"a": PA_s, "b": PB_s, "t": Pt}
            P_seci = {"a": PAi_s, "b": PBi_s, "t": Pti}
            found_cocs = None
            nu_t_sel = 1
            for k_nu in range(24):
                nu_t = pow(z24_s, k_nu, p_sc)
                nu5 = pow(nu_t, 5, p_sc)
                D5 = {"a": QA_s, "b": QB_s, "t": (nu5 * Ut) % p_sc}
                Ps = {"a": PAi_s.T, "b": PBi_s.T, "t": Pti.T}
                hom_m = {g: np.kron(D5[g], Ps[g]) % p_sc for g in "abt"}
                hom_i = {g: np_inv_gf(hom_m[g], p_sc) for g in "abt"}
                _, h1_s, _, _, cs_s = cohom_steps_np_gf(hom_m, hom_i, steps1, "abAB", mu1, p_sc, want_cocs=True)
                if h1_s > 0:
                    if h1_s != 2:
                        sys.exit(2)
                    found_cocs = cs_s
                    nu_t_sel = nu_t
                    break
            assert found_cocs is not None
            nu3 = pow(nu_t_sel, 3, p_sc)
            num2 = pow(nu_t_sel, -2, p_sc)
            D_tw = {"a": QA_s, "b": QB_s, "t": (nu3 * Ut) % p_sc}
            D_twi = {"a": QAi_s, "b": QBi_s, "t": (pow(nu3, p_sc - 2, p_sc) * Uti) % p_sc}
            P_tw = {"a": PA_s, "b": PB_s, "t": (num2 * Pt) % p_sc}
            P_twi = {"a": PAi_s, "b": PBi_s, "t": (pow(num2, p_sc - 2, p_sc) * Pti) % p_sc}

            hist_p: Counter[tuple[int, int]] = Counter()
            for alpha_c, beta_c in [(1, s_val) for s_val in range(p_sc)] + [(0, 1)]:
                cv = (alpha_c * found_cocs[0] + beta_c * found_cocs[1]) % p_sc
                WP_m: dict[str, np.ndarray] = {}
                WP_i: dict[str, np.ndarray] = {}
                L2P_m: dict[str, np.ndarray] = {}
                L2P_i: dict[str, np.ndarray] = {}
                for gi, g in enumerate("abt"):
                    cg = cv[6 * gi : 6 * (gi + 1)].reshape(2, 3)
                    cP = (cg @ P_tw[g]) % p_sc
                    neg_Dic = ((-D_twi[g] @ cg) % p_sc)
                    M5 = np.block([[D_tw[g], cP], [np.zeros((3, 2), dtype=np.int64), P_tw[g]]]) % p_sc
                    M5i = np.block([[D_twi[g], neg_Dic], [np.zeros((3, 2), dtype=np.int64), P_twi[g]]]) % p_sc
                    WP_m[g] = np.kron(M5, P_sec[g]) % p_sc
                    WP_i[g] = np.kron(M5i, P_seci[g]) % p_sc
                    L2P_m[g] = np.kron(wedge2_gf(M5, p_sc), P_sec[g]) % p_sc
                    L2P_i[g] = np.kron(wedge2_gf(M5i, p_sc), P_seci[g]) % p_sc
                tw_p, tws_p = verify_b1604_e1_duality_gf(WP_m, WP_i, steps1, "abAB", mu1, p_sc)
                tl_p, tls_p = verify_b1604_e1_duality_gf(L2P_m, L2P_i, steps1, "abAB", mu1, p_sc)
                hist_p[(tw_p[3] - tws_p[3], tl_p[3] - tls_p[3])] += 1

            proj_summary[str(p_sc)][sgn + w] = {str(k): int(v) for k, v in sorted(hist_p.items())}
            if hist_p != Counter({(1, 1): p_sc - 1, (0, 1): 2}):
                proj_scan_ok = False

    ok = (
        w17_readings == 480
        and w17_carriers_ok
        and w17_chiral_ok
        and w17_mod16_ok
        and route_b_canonical_72 == 72
        and route_ab_agree
        and w18_chiral_ok
        and w18_mod16_ok
        and w18_singlets_carriers_ok
        and proj_scan_ok
    )
    return {
        "row": 931,
        "commits": ["57e99a1d4"],
        "w17_total_readings": w17_readings,
        "w17_carriers_14_read_1_1": w17_carriers_ok,
        "w17_chiral_14_read_0_1": w17_chiral_ok,
        "w17_mod16_4_read_0_0": w17_mod16_ok,
        "w18_route_b_canonical_readings": route_b_canonical_72,
        "w18_route_b_all_checked_readings": route_b_total_checked,
        "w18_routes_a_and_b_agree": route_ab_agree,
        "w18_chiral_0_2_and_0_9_ok": w18_chiral_ok,
        "w18_mod16_0_0_ok": w18_mod16_ok,
        "w18_carrier_singlets_11_01_01_ok": w18_singlets_carriers_ok,
        "w18_projective_line_scan_p73_p97_all_14_have_2_special": proj_scan_ok,
        "projective_line_histograms": proj_summary,
        "result": "the same" if ok else "differs",
    }


def verify_row_934() -> dict[str, object]:
    """Row 934 (@ 240d3ddf2): finite group-theory identity inside A_4 = (Z_2 x Z_2) x| Z_3; orbifold analogy left as reading."""
    M2 = ((1, 1), (1, 0))  # order-3 golden action on F_2^2

    def app_m2(v: tuple[int, int], r: int) -> tuple[int, int]:
        x, y = v
        for _ in range(r % 3):
            x, y = (M2[0][0] * x + M2[0][1] * y) % 2, (M2[1][0] * x + M2[1][1] * y) % 2
        return (x, y)

    elems = [((vx, vy), r) for r in range(3) for vy in range(2) for vx in range(2)]

    def mul(e1, e2):
        (v1, r1), (v2, r2) = e1, e2
        w_v = app_m2(v2, r1)
        return (((v1[0] + w_v[0]) % 2, (v1[1] + w_v[1]) % 2), (r1 + r2) % 3)

    def inv_el(e):
        for f in elems:
            if mul(e, f) == ((0, 0), 0):
                return f
        raise RuntimeError

    v4 = [e for e in elems if e[1] == 0]
    v4_nontriv = [e for e in v4 if e != ((0, 0), 0)]
    is_normal = all(mul(mul(g, k), inv_el(g)) in v4 for g in elems for k in v4)
    gen_z3 = ((0, 0), 1)
    z3_orbit = {mul(mul(gen_z3 if r == 1 else mul(gen_z3, gen_z3) if r == 2 else ((0, 0), 0), v4_nontriv[0]), inv_el(gen_z3 if r == 1 else mul(gen_z3, gen_z3) if r == 2 else ((0, 0), 0))) for r in range(3)}

    ok = len(elems) == 12 and len(v4) == 4 and len(v4_nontriv) == (2**2 - 1) and is_normal and z3_orbit == set(v4_nontriv)
    return {
        "row": 934,
        "commits": ["240d3ddf2"],
        "a4_order": len(elems),
        "klein_four_order": len(v4),
        "nontrivial_twisted_elements_2_sq_minus_1": len(v4_nontriv),
        "klein_four_normal_and_cycled_transitively_by_Z3": is_normal and (z3_orbit == set(v4_nontriv)),
        "heterotic_orbifold_literature_analogy": "reading (not independently checked)",
        "result": "the same" if ok else "differs",
    }


def main() -> None:
    t0 = time.time()
    controls = run_negative_controls()
    rows = {
        "923": verify_row_923(),
        "924": verify_row_924(),
        "925": verify_row_925(),
        "926": verify_row_926(),
        "927": verify_row_927(),
        "928": verify_row_928(),
        "929": verify_row_929(),
        "930": verify_row_930(),
        "931": verify_row_931(),
        "934": verify_row_934(),
    }
    payload = {
        "card": "X-C1b",
        "seat": "agy-exp",
        "negative_controls": controls,
        "rows": rows,
        "elapsed_seconds": round(time.time() - t0, 3),
    }
    out_path = HERE / "verify_x_c1b_out.json"
    out_bytes = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    out_path.write_bytes(out_bytes)
    digest = hashlib.sha256(out_bytes).hexdigest()
    (HERE / "OUTPUT_SHA256.txt").write_text(f"{digest}  verify_x_c1b_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
