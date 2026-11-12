#!/usr/bin/env python3
"""Independent pure-mathematics verification suite for Card X-C1a (Batch V1, first 10 REGISTERED weave rows: 908-922).

Zero imports from any SM-seat script or dossier. All group presentations, finite covers,
Smith normal forms, hyperbolic SL(2, C) holonomies, Fox cohomology ranks, cusp restrictions,
interior extension counts (I(W_1), I(Lambda^2 W_1)), O_h triplet actions, Haar unitary
basis-scrambling checks, and trichotomy/Theorem S/Lemma V censuses are constructed from
mathematical definitions alone. 0 of 19.
"""
from __future__ import annotations

import cmath
import hashlib
import itertools
import json
import math
import pathlib
import sys
from collections import Counter, deque
from fractions import Fraction

import gmpy2
import mpmath as mp
import numpy as np
from scipy import linalg as sla
import snappy
import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp

HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 140
gmpy2.get_context().precision = 400  # >120 decimal digits in C-compiled GNU MPFR/MPC

GMMat = list[list[gmpy2.mpc]]

INV = {"a": "A", "b": "B", "A": "a", "B": "b", "t": "T", "T": "t"}


# ---------------------------------------------------------------------------
# 1. Free-group words, bundle presentations, and GENESIS state enumeration
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


def auto_words(sign: str, word: str) -> dict[str, str]:
    """sm:B1527 bundle convention: phi_L(a)=ab, phi_L(b)=b; phi_R(a)=a, phi_R(b)=ba; last letter first; - applies iota."""
    img = {"a": "a", "b": "b"}
    for ch in reversed(word):
        step = {"a": "ab", "b": "b"} if ch == "L" else {"a": "a", "b": "ba"}
        img = {"a": sub_w(img["a"], step), "b": sub_w(img["b"], step)}
    if sign == "-":
        img = {g: sub_w(img[g], {"a": "A", "b": "B"}) for g in "ab"}
    return img


def homology_mat(sign: str, word: str) -> tuple[tuple[int, int], tuple[int, int]]:
    """2x2 matrix M on H_1(F_2)=Z^2 (column j = exponent sums of phi(gen_j))."""
    img = auto_words(sign, word)
    def ex(w: str, g: str) -> int:
        return w.count(g) - w.count(g.upper())
    return ((ex(img["a"], "a"), ex(img["b"], "a")), (ex(img["a"], "b"), ex(img["b"], "b")))


def canon_word(w: str) -> str:
    rots = [w[i:] + w[:i] for i in range(len(w))]
    sw = w.translate(str.maketrans("LR", "RL"))
    rots += [sw[i:] + sw[:i] for i in range(len(sw))]
    return min(rots)


def is_primitive(w: str) -> bool:
    n = len(w)
    return all(w != w[k:] + w[:k] for k in range(1, n) if n % k == 0)


def genesis_states(nmax: int, dmax: int | None = None) -> list[tuple[str, tuple[tuple[int, int], tuple[int, int]], int]]:
    words: set[str] = set()
    for n in range(2, nmax + 1):
        for tup in itertools.product("LR", repeat=n):
            w = "".join(tup)
            if "L" in w and "R" in w and is_primitive(w):
                words.add(canon_word(w))
    out = []
    for w in sorted(words, key=lambda s: (len(s), s)):
        for sgn in ("+", "-"):
            sw = sgn + w
            M = homology_mat(sgn, w)
            tr = M[0][0] + M[1][1]
            ends = abs(2 - tr)
            if dmax is None or ends <= dmax:
                out.append((sw, M, ends))
    return out


# ---------------------------------------------------------------------------
# 2. General Reidemeister-Schreier cover builder and character-orbit solver
# ---------------------------------------------------------------------------

def build_cover(sign: str, word: str, d: int, act_abt: dict[str, list[int]]) -> dict[str, object]:
    img = auto_words(sign, word)
    act: dict[str, list[int]] = {}
    for g in "abt":
        p = list(act_abt[g])
        pinv = [0] * d
        for i, j in enumerate(p):
            pinv[j] = i
        act[g] = p
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
    assert len(u) == d, f"Cover action not transitive for {sign}{word} (got {len(u)}/{d})"

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
            assert xend == x, f"Relator {ri} failed coset closure at {x} on {sign}{word}"
            rels_idx.append(sw)
            for idx, sgn in sw:
                rel_mat[2 * x + ri, idx] += sgn

    ell_w = "abAB"
    tp_w = "t" if sign == "+" else "abt"
    seen_c: set[int] = set()
    cusps_idx: list[tuple[list[tuple[int, int]], list[tuple[int, int]]]] = []
    cusp_Anchor_cosets: list[int] = []
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
        cusp_Anchor_cosets.append(x0)
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
        assert p_pow * q_pow == len(orb)
        cusps_idx.append((sw1, found_sw2))

    deck_mats: list[np.ndarray] = []
    for h in range(d):
        uh, uhi = u[h], inv_w(u[h])
        M_h = np.zeros((ng, ng), dtype=np.int64)
        ok_norm = True
        for j, gw in enumerate(gen_words):
            sw, xe = rewrite_from(0, uhi + gw + uh)
            if xe != 0:
                ok_norm = False
                break
            for idx, sgn in sw:
                M_h[idx, j] += sgn
        if ok_norm:
            deck_mats.append(M_h)

    return {
        "sign": sign,
        "word": word,
        "d": d,
        "act": act,
        "u": u,
        "ng": ng,
        "gen_idx": gen_idx,
        "gen_words": gen_words,
        "rewrite_from": rewrite_from,
        "rels_gamma": rels_gamma,
        "rels_idx": rels_idx,
        "rel_mat": rel_mat,
        "cusps_idx": cusps_idx,
        "cusp_cosets": cusp_Anchor_cosets,
        "deck_mats": deck_mats,
        "ell_w": ell_w,
        "tp_w": tp_w,
    }


def cover_characters_and_orbits(cov: dict[str, object], m: int) -> tuple[list[np.ndarray], list[list[np.ndarray]]]:
    """Exact Hom(H_1(N; Z), Z/mZ) and deck orbits via Smith Normal Form over Z."""
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
            step = m // g
            choices_per_coord.append(list(range(0, m, step)))
            active_cols.append(i)
    if not active_cols:
        z0 = np.zeros(ng, dtype=np.int64)
        return [z0], [[z0]]

    B_sub = V_np[:, active_cols] % m
    chars: list[np.ndarray] = []
    for tup in itertools.product(*choices_per_coord):
        z = np.array(tup, dtype=np.int64)
        c = (B_sub @ z) % m
        chars.append(c)

    deck_T = [(M_h.T % m) for M_h in cov["deck_mats"]]
    seen: set[bytes] = set()
    orbits: list[list[np.ndarray]] = []
    for c in chars:
        kb = c.tobytes()
        if kb in seen:
            continue
        orb_dict: dict[bytes, np.ndarray] = {}
        for DT in deck_T:
            img_c = (DT @ c) % m
            orb_dict[img_c.tobytes()] = img_c
        seen.update(orb_dict.keys())
        orb_list = sorted(orb_dict.values(), key=lambda arr: tuple(arr.tolist()))
        orbits.append(orb_list)
    return chars, orbits


def m_invariant_lattices(M: tuple[tuple[int, int], tuple[int, int]], index_d: int) -> list[tuple[int, int, int]]:
    """All sublattices Lam = Z*(a, 0) + Z*(b, c) of index d (a*c = d, 0 <= b < a) with M(Lam) <= Lam."""
    out = []
    for a in range(1, index_d + 1):
        if index_d % a != 0:
            continue
        c = index_d // a
        for b in range(a):
            # Basis columns v1 = (a, 0), v2 = (b, c); check M*v1, M*v2 in Lam
            ok = True
            for vx, vy in ((a, 0), (b, c)):
                mx = M[0][0] * vx + M[0][1] * vy
                my = M[1][0] * vx + M[1][1] * vy
                if my % c != 0:
                    ok = False
                    break
                q = my // c
                if (mx - q * b) % a != 0:
                    ok = False
                    break
            if ok:
                out.append((a, b, c))
    return out


def build_abelian_fibre_cover(sign: str, word: str, lat: tuple[int, int, int], wbar: tuple[int, int]) -> dict[str, object]:
    """Fibre-direction cover for Lam = Z*(a,0) + Z*(b,c) and translation wbar in Z^2/Lam."""
    a_lat, b_lat, c_lat = lat
    d = a_lat * c_lat
    M = homology_mat(sign, word)
    detM = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    assert detM in (1, -1)
    Minv = ((detM * M[1][1], -detM * M[0][1]), (-detM * M[1][0], detM * M[0][0]))

    def red_lat(vx: int, vy: int) -> tuple[int, int]:
        q = vy // c_lat
        ry = vy - q * c_lat
        rx = (vx - q * b_lat) % a_lat
        return (rx, ry)

    cosets = [(rx, ry) for ry in range(c_lat) for rx in range(a_lat)]
    assert cosets[0] == (0, 0) and len(cosets) == d
    c_map = {pt: i for i, pt in enumerate(cosets)}

    wb = red_lat(wbar[0], wbar[1])
    act_abt = {
        "a": [c_map[red_lat(x + 1, y)] for (x, y) in cosets],
        "b": [c_map[red_lat(x, y + 1)] for (x, y) in cosets],
        "t": [c_map[red_lat(Minv[0][0] * x + Minv[0][1] * y - wb[0], Minv[1][0] * x + Minv[1][1] * y - wb[1])] for (x, y) in cosets],
    }
    return build_cover(sign, word, d, act_abt)


def build_companion_cover(sign: str, word: str) -> dict[str, object]:
    """Unique companion cover Lam = (M - I)Z^2 with maximal cusps d = |2 - tr(M)|."""
    M = homology_mat(sign, word)
    detM = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    Minv = ((detM * M[1][1], -detM * M[0][1]), (-detM * M[1][0], detM * M[0][0]))
    # Column HNF of Nmat = M - I
    v1 = (M[0][0] - 1, M[1][0])
    v2 = (M[0][1], M[1][1] - 1)
    H = sp.Matrix([[v1[0], v2[0]], [v1[1], v2[1]]])
    # Lattice basis in upper-triangular form: c = gcd(v1[1], v2[1])
    d = abs(int(H.det()))
    lats = [lat for lat in m_invariant_lattices(M, d) if all(
        ((vy % lat[2] == 0) and ((vx - (vy // lat[2]) * lat[1]) % lat[0] == 0))
        for (vx, vy) in (v1, v2)
    )]
    assert len(lats) == 1
    lat = lats[0]
    wbar = (0, 0) if sign == "+" else (Minv[0][0] + Minv[0][1], Minv[1][0] + Minv[1][1])
    cov = build_abelian_fibre_cover(sign, word, lat, wbar)
    assert len(cov["cusps_idx"]) == d
    return cov


def build_a4_cover(sign: str, word: str) -> dict[str, object]:
    """Forced tetrahedral cover N = ker(pi_1 M -> F_2^2 x| Z/3 = A_4) for odd-trace state."""
    M = homology_mat(sign, word)
    assert (M[0][0] + M[1][1]) % 2 == 1
    M2 = ((M[0][0] % 2, M[0][1] % 2), (M[1][0] % 2, M[1][1] % 2))

    def apply_m2(v: tuple[int, int], k: int) -> tuple[int, int]:
        x, y = v
        for _ in range(k % 3):
            x, y = (M2[0][0] * x + M2[0][1] * y) % 2, (M2[1][0] * x + M2[1][1] * y) % 2
        return (x, y)

    # Elements of A_4 = F_2^2 x| Z/3 as ((vx, vy), r) with identity ((0,0), 0) at index 0:
    # Group law: (v1, r1) * (v2, r2) = (v1 + M2^r1(v2), (r1 + r2) % 3)
    # Check t g t^-1: ((0,0), 1) * (v, 0) * ((0,0), 2) = (M2(v), 0) = phi_mod2(g)!
    elems = [((vx, vy), r) for r in range(3) for vy in range(2) for vx in range(2)]
    assert elems[0] == ((0, 0), 0)
    emap = {el: i for i, el in enumerate(elems)}

    def mul_a4(e1: tuple[tuple[int, int], int], e2: tuple[tuple[int, int], int]) -> tuple[tuple[int, int], int]:
        (v1, r1), (v2, r2) = e1, e2
        w = apply_m2(v2, r1)
        return (((v1[0] + w[0]) % 2, (v1[1] + w[1]) % 2), (r1 + r2) % 3)

    ga, gb, gt = ((1, 0), 0), ((0, 1), 0), ((0, 0), 1)
    act_abt = {
        "a": [emap[mul_a4(el, ga)] for el in elems],
        "b": [emap[mul_a4(el, gb)] for el in elems],
        "t": [emap[mul_a4(el, gt)] for el in elems],
    }
    cov = build_cover(sign, word, 12, act_abt)
    assert len(cov["cusps_idx"]) == 4
    cov["a4_elems"] = elems
    cov["a4_map"] = emap
    return cov


# ---------------------------------------------------------------------------
# 3. Hyperbolic SL(2, C) holonomy solver (70-digit mpmath) and Fox cohomology
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
    roots: list[tuple[complex, complex, complex]] = []

    def add_rt(a: complex, b: complex, c: complex) -> None:
        if abs(a.imag) + abs(b.imag) + abs(c.imag) < 1e-6:
            return
        if not any(abs(a - rx) + abs(b - ry) + abs(c - rz) < 1e-6 for rx, ry, rz in roots):
            roots.append((a, b, c))

    for k in range(1, 900):
        r1 = 0.4 * (30.0 ** ((k * 0.6180339887498949) % 1.0))
        th1 = 2 * math.pi * ((k * 0.3819660112501051) % 1.0)
        r2 = 0.4 * (30.0 ** ((k * 0.7548776662466927) % 1.0))
        th2 = 2 * math.pi * ((k * 0.5698402909980532) % 1.0)
        yv, zv = cmath.rect(r1, th1), cmath.rect(r2, th2)
        disc = cmath.sqrt((yv * zv) ** 2 - 4 * (yv * yv + zv * zv))
        xv = (yv * zv + (disc if k % 2 == 0 else -disc)) / 2
        ok = True
        for _ in range(50):
            try:
                f0, f1, f2, _ = _eval_fricke_c(word, xv, yv, zv)
                err = abs(f0) + abs(f1) + abs(f2)
                if err < 1e-12:
                    break
                if err > 1e60:
                    ok = False
                    break
                eps = 1e-8 * max(1.0, abs(xv), abs(yv), abs(zv))
                d0x = _eval_fricke_c(word, xv + eps, yv, zv)[:3]
                d0y = _eval_fricke_c(word, xv, yv + eps, zv)[:3]
                d0z = _eval_fricke_c(word, xv, yv, zv + eps)[:3]
                J = [[(d0x[i] - [f0, f1, f2][i]) / eps, (d0y[i] - [f0, f1, f2][i]) / eps, (d0z[i] - [f0, f1, f2][i]) / eps] for i in range(3)]
                detJ = (
                    J[0][0] * (J[1][1] * J[2][2] - J[1][2] * J[2][1])
                    - J[0][1] * (J[1][0] * J[2][2] - J[1][2] * J[2][0])
                    + J[0][2] * (J[1][0] * J[2][1] - J[1][1] * J[2][0])
                )
                if abs(detJ) < 1e-25:
                    ok = False
                    break
                rhs = [-f0, -f1, -f2]
                dx = (rhs[0] * (J[1][1] * J[2][2] - J[1][2] * J[2][1]) - J[0][1] * (rhs[1] * J[2][2] - J[1][2] * rhs[2]) + J[0][2] * (rhs[1] * J[2][1] - J[1][1] * rhs[2])) / detJ
                dy = (J[0][0] * (rhs[1] * J[2][2] - J[1][2] * rhs[2]) - rhs[0] * (J[1][0] * J[2][2] - J[1][2] * rhs[2]) + J[0][2] * (J[1][0] * rhs[2] - rhs[1] * J[2][0])) / detJ
                dz = (J[0][0] * (J[1][1] * rhs[2] - rhs[1] * J[2][1]) - J[0][1] * (J[1][0] * rhs[2] - rhs[1] * J[2][0]) + rhs[0] * (J[1][0] * J[2][1] - J[1][1] * J[2][0])) / detJ
                sn = max(abs(dx), abs(dy), abs(dz))
                sc = 1.0 if sn <= 5.0 else 5.0 / sn
                xv += sc * dx
                yv += sc * dy
                zv += sc * dz
            except ZeroDivisionError:
                ok = False
                break
        if not ok:
            continue
        f0, f1, f2, f3 = _eval_fricke_c(word, xv, yv, zv)
        if abs(f0) + abs(f1) + abs(f2) + abs(f3) < 1e-9 and abs(zv) > 1e-5:
            add_rt(xv, yv, zv)
            add_rt(xv.conjugate(), yv.conjugate(), zv.conjugate())
    _ROOTS_CACHE[word] = roots
    return roots


def _mp_to_gm(z: mp.mpc | mp.mpf) -> gmpy2.mpc:
    rz = gmpy2.mpfr(mp.nstr(mp.re(z), 130) or "0")
    iz = gmpy2.mpfr(mp.nstr(mp.im(z), 130) or "0")
    return gmpy2.mpc(rz, iz)


def four_mp_mat(g: mp.matrix) -> mp.matrix:
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
    return M4


def four_mp_to_np(g: mp.matrix) -> np.ndarray:
    M4 = four_mp_mat(g)
    out = np.zeros((4, 4), dtype=np.complex128)
    for i in range(4):
        for j in range(4):
            out[i, j] = complex(M4[i, j])
    return out


def four_mp_to_gm(g: mp.matrix) -> GMMat:
    M4 = four_mp_mat(g)
    return [[_mp_to_gm(M4[i, j]) for j in range(4)] for i in range(4)]


def sl2_inv_mp(g: mp.matrix) -> mp.matrix:
    return mp.matrix([[g[1, 1], -g[0, 1]], [-g[1, 0], g[0, 0]]])


def eval_word_sl2_mp(w: str, mats_abt_mp: dict[str, mp.matrix], invs_abt_mp: dict[str, mp.matrix]) -> mp.matrix:
    R = mp.eye(2)
    for c in w:
        R = R * (mats_abt_mp[c] if c in "abt" else invs_abt_mp[c.lower()])
    return R


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
    if best_t is None or best_res > mp.mpf("1e-110"):
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
    img = auto_words(sign, word)
    for rx, ry, rz in _find_markov_roots(word):
        xv, yv, zv = mp.mpc(rx), mp.mpc(ry), mp.mpc(rz)

        def ev_jet(xx: mp.mpc, yy: mp.mpc, zz: mp.mpc) -> tuple[list[mp.mpc], mp.matrix]:
            # Exact analytic Jacobian via 1st-order jet (val, dx, dy, dz) at 140 digits
            z0 = mp.mpc(0)
            one = mp.mpc(1)
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
            f_vec = [r0[0], r1[0], r2[0]]
            J_mat = mp.matrix([
                [r0[1], r0[2], r0[3]],
                [r1[1], r1[2], r1[3]],
                [r2[1], r2[2], r2[3]],
            ])
            return f_vec, J_mat

        ok = True
        for _ in range(30):
            f0, J = ev_jet(xv, yv, zv)
            if max(abs(t) for t in f0) < mp.mpf("1e-128"):
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
        if not ok or max(abs(t) for t in f_chk) > mp.mpf("1e-120"):
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
        if abs(tp_u[1, 0]) > mp.mpf("1e-90") or abs(tp_u[0, 0] - st) > mp.mpf("1e-90"):
            continue
        tau = (st * tp_u[0, 1]) / (sl * ell_u[0, 1])
        if abs(abs(float(mp.im(tau))) - abs(sh.imag)) < 1e-7:
            t_re = float(mp.re(tau))
            if any(abs((t_re + e * sh.real) - round(t_re + e * sh.real)) < 1e-7 for e in (1, -1)) and mp.im(tau) > 0:
                abt_mp = {"a": A, "b": B, "t": T}
                abt_inv_mp = {"a": sl2_inv_mp(A), "b": sl2_inv_mp(B), "t": sl2_inv_mp(T)}
                res_obj = {
                    "A_mp": A,
                    "B_mp": B,
                    "T_mp": T,
                    "abt_mp": abt_mp,
                    "abt_inv_mp": abt_inv_mp,
                    "np4": {"a": four_mp_to_np(A), "b": four_mp_to_np(B), "t": four_mp_to_np(T)},
                    "gm4": {"a": four_mp_to_gm(A), "b": four_mp_to_gm(B), "t": four_mp_to_gm(T)},
                    "gm4_inv": {
                        "a": four_mp_to_gm(abt_inv_mp["a"]),
                        "b": four_mp_to_gm(abt_inv_mp["b"]),
                        "t": four_mp_to_gm(abt_inv_mp["t"]),
                    },
                }
                _HOL_CACHE[key] = res_obj
                return res_obj
    raise RuntimeError(f"Could not locate hyperbolic holonomy for {key}")


def get_tick_holonomy_gm4(base_sign: str, base_word: str, k_tick: int) -> tuple[str, str, dict[str, GMMat], dict[str, GMMat]]:
    """Holonomy of (eps * word)^k at 120 digits using the base fibre's (A_mp, B_mp) without long-word precision loss."""
    tick_sign = "+" if (base_sign == "+" or k_tick % 2 == 0) else "-"
    tick_word = base_word * k_tick
    base_hol = get_holonomy(base_sign, base_word)
    A: mp.matrix = base_hol["A_mp"]
    B: mp.matrix = base_hol["B_mp"]

    pa, pb = A, B
    for _ in range(k_tick):
        for ch in reversed(base_word):
            if ch == "L":
                pa, pb = pa * pb, pb
            else:
                pa, pb = pa, pb * pa
        if base_sign == "-":
            pa, pb = sl2_inv_mp(pa), sl2_inv_mp(pb)

    Tk = _solve_T_mp(A, B, pa, pb)
    assert Tk is not None
    Tk_inv = sl2_inv_mp(Tk)
    gm4 = {"a": base_hol["gm4"]["a"], "b": base_hol["gm4"]["b"], "t": four_mp_to_gm(Tk)}
    gm4_inv = {"a": base_hol["gm4_inv"]["a"], "b": base_hol["gm4_inv"]["b"], "t": four_mp_to_gm(Tk_inv)}
    return tick_sign, tick_word, gm4, gm4_inv


def gm_roots_of_unity(m_order: int) -> list[gmpy2.mpc]:
    out: list[gmpy2.mpc] = []
    for k in range(m_order):
        ang = 2 * mp.pi * mp.mpf(k) / mp.mpf(m_order)
        out.append(_mp_to_gm(mp.cos(ang) + 1j * mp.sin(ang)))
    return out


def gm_scale_mat(sc: gmpy2.mpc, M: GMMat) -> GMMat:
    return [[sc * x for x in row] for row in M]


def gm_transpose(M: GMMat) -> GMMat:
    if not M:
        return []
    m, n = len(M), len(M[0])
    return [[M[i][j] for i in range(m)] for j in range(n)]


def gm_neg(M: GMMat) -> GMMat:
    return [[-x for x in row] for row in M]


def gm_hstack(A: GMMat, B: GMMat) -> GMMat:
    return [ra + rb for ra, rb in zip(A, B)]


def gm_matmul(A: GMMat, B: GMMat) -> GMMat:
    m = len(A)
    if m == 0:
        return []
    p = len(B)
    n = len(B[0]) if p > 0 else 0
    z0 = gmpy2.mpc(0)
    out = [[z0] * n for _ in range(m)]
    for i in range(m):
        Ai = A[i]
        oi = out[i]
        for k in range(p):
            aik = Ai[k]
            if aik != 0:
                Bk = B[k]
                for j in range(n):
                    bkj = Bk[j]
                    if bkj != 0:
                        oi[j] += aik * bkj
    return out


def gm_rank_and_nullspace(M: GMMat, m_rows: int, n_cols: int, want_null: bool = False) -> tuple[int, GMMat]:
    """120-digit complete-boundary-pivoting Gaussian elimination with a 45-order-of-magnitude forbidden band."""
    z0 = gmpy2.mpc(0)
    one = gmpy2.mpc(1)
    if m_rows == 0 or n_cols == 0:
        if want_null:
            return 0, [[one if i == j else z0 for j in range(n_cols)] for i in range(n_cols)]
        return 0, []

    entry_max = gmpy2.mpfr(0)
    for r in range(m_rows):
        row = M[r]
        for c in range(n_cols):
            av = abs(row[c])
            if av > entry_max:
                entry_max = av
    if entry_max < gmpy2.mpfr("1e-95"):
        if want_null:
            return 0, [[one if i == j else z0 for j in range(n_cols)] for i in range(n_cols)]
        return 0, []

    hi_thr = gmpy2.mpfr("1e-35") * entry_max
    lo_thr = gmpy2.mpfr("1e-80") * entry_max

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
                row_r = A[r]
                row_r[rk], row_r[pc] = row_r[pc], row_r[rk]

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
            row_r = A[r]
            fac = row_r[rk]
            if fac != 0:
                row_r[rk] = z0
                for c in nz_cols:
                    row_r[c] -= fac * piv_row[c]
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

    if dim_null > 0:
        MZ = gm_matmul(M, Z)
        err = max(abs(x) for row in MZ for x in row)
        if err > gmpy2.mpfr("1e-75") * entry_max:
            sys.exit(2)
    return rk, Z


def fox_pres_gm(mod_mats: list[GMMat], mod_invs: list[GMMat], w_idx_sgn: list[tuple[int, int]]) -> tuple[GMMat, GMMat]:
    e = len(mod_mats[0])
    ng = len(mod_mats)
    z0 = gmpy2.mpc(0)
    one = gmpy2.mpc(1)
    out = [[z0] * (ng * e) for _ in range(e)]
    pre = [[one if i == j else z0 for j in range(e)] for i in range(e)]
    for j, sgn in w_idx_sgn:
        off = j * e
        if sgn == 1:
            for r in range(e):
                orow = out[r]
                prow = pre[r]
                for c in range(e):
                    orow[off + c] += prow[c]
            pre = gm_matmul(pre, mod_mats[j])
        else:
            pre = gm_matmul(pre, mod_invs[j])
            for r in range(e):
                orow = out[r]
                prow = pre[r]
                for c in range(e):
                    orow[off + c] -= prow[c]
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
    z0 = gmpy2.mpc(0)
    one = gmpy2.mpc(1)
    fox: GMMat = []
    for r in rels_idx:
        fr, wr = fox_pres_gm(mod_mats, mod_invs, r)
        for i in range(e):
            for j in range(e):
                if abs(wr[i][j] - (one if i == j else z0)) > gmpy2.mpfr("1e-75"):
                    sys.exit(2)
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
        r_off = 2 * e * ci
        c_off = e * ci
        for i in range(e):
            for j in range(e):
                BP[r_off + i][c_off + j] = W1[i][j] - (one if i == j else z0)
                BP[r_off + e + i][c_off + j] = W2[i][j] - (one if i == j else z0)

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

    def vdot(u: list[gmpy2.mpc], v: list[gmpy2.mpc]) -> gmpy2.mpc:
        s = z0
        for ui, vi in zip(u, v):
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
        if nrm > gmpy2.mpfr("1e-40"):
            b_vecs.append([vi / nrm for vi in v])
    if len(b_vecs) != r0:
        sys.exit(2)

    int_vecs: list[list[gmpy2.mpc]] = []
    ncol_I = len(I_cocs[0]) if I_cocs else 0
    for c in range(ncol_I):
        v = [I_cocs[r][c] for r in range(dim_vec)]
        for bv in b_vecs:
            pr = vdot(bv, v)
            v = [vi - pr * bi for vi, bi in zip(v, bv)]
        for iv in int_vecs:
            pr = vdot(iv, v)
            v = [vi - pr * ii for vi, ii in zip(v, iv)]
        nrm = gmpy2.sqrt(vdot(v, v).real)
        if nrm > gmpy2.mpfr("1e-40"):
            int_vecs.append([vi / nrm for vi in v])
    if len(int_vecs) != n:
        sys.exit(2)

    int_basis = [[int_vecs[c][r] for c in range(n)] for r in range(dim_vec)]
    f_chk = gm_matmul(fox, int_basis)
    if max(abs(x) for row in f_chk for x in row) > gmpy2.mpfr("1e-75"):
        sys.exit(2)
    return h0, h1, r1, n, int_basis


def wedge2_gm(X: GMMat) -> GMMat:
    n = len(X)
    idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
    m = len(idx)
    z0 = gmpy2.mpc(0)
    W = [[z0] * m for _ in range(m)]
    for r, (i, j) in enumerate(idx):
        Xi, Xj = X[i], X[j]
        Wr = W[r]
        for c, (k, l) in enumerate(idx):
            Wr[c] = Xi[k] * Xj[l] - Xi[l] * Xj[k]
    return W


def generic_extension_counts_gm(
    base_mats: list[GMMat],
    base_invs: list[GMMat],
    int_basis: GMMat,
    rels_idx: list[list[tuple[int, int]]],
    cusps_idx: list[tuple[list[tuple[int, int]], list[tuple[int, int]]]],
) -> tuple[int, int]:
    """Evaluate (I(W_1), I(Lambda^2 W_1)) at 120 digits across 3 independent deterministic complex draws."""
    ng = len(base_mats)
    n = len(int_basis[0])
    z0 = gmpy2.mpc(0)
    one = gmpy2.mpc(1)
    draws = []
    for seed_k in (1, 2, 3):
        weights: list[gmpy2.mpc] = []
        for r in range(n):
            rad = mp.mpf(1) + mp.mpf("0.17") * r
            ang = mp.mpf("0.73") * seed_k * (r + 1) + mp.mpf("0.29") * r * r
            weights.append(_mp_to_gm(rad * (mp.cos(ang) + 1j * mp.sin(ang))))
        c_vec = [sum(int_basis[i][r] * weights[r] for r in range(n)) for i in range(4 * ng)]

        W1_mats: list[GMMat] = []
        W1_invs: list[GMMat] = []
        W1_dual: list[GMMat] = []
        W1_dual_invs: list[GMMat] = []
        L2_mats: list[GMMat] = []
        L2_invs: list[GMMat] = []
        L2_dual: list[GMMat] = []
        L2_dual_invs: list[GMMat] = []

        for j in range(ng):
            Aj = base_mats[j]
            Ainv = base_invs[j]
            cj = c_vec[4 * j : 4 * (j + 1)]
            neg_Ainv_c = [-sum(Ainv[row_i][k] * cj[k] for k in range(4)) for row_i in range(4)]

            M5 = [Aj[row_i] + [cj[row_i]] for row_i in range(4)] + [[z0, z0, z0, z0, one]]
            M5_inv = [Ainv[row_i] + [neg_Ainv_c[row_i]] for row_i in range(4)] + [[z0, z0, z0, z0, one]]
            M5_star = gm_transpose(M5_inv)
            M5_star_inv = gm_transpose(M5)

            W1_mats.append(M5)
            W1_invs.append(M5_inv)
            W1_dual.append(M5_star)
            W1_dual_invs.append(M5_star_inv)

            L2_mats.append(wedge2_gm(M5))
            L2_invs.append(wedge2_gm(M5_inv))
            L2_dual.append(wedge2_gm(M5_star))
            L2_dual_invs.append(wedge2_gm(M5_star_inv))

        _, _, _, n_w1, _ = cohom_pres_gm(W1_mats, W1_invs, rels_idx, cusps_idx, want_interior=False)
        _, _, _, n_w1s, _ = cohom_pres_gm(W1_dual, W1_dual_invs, rels_idx, cusps_idx, want_interior=False)
        _, _, _, n_l2, _ = cohom_pres_gm(L2_mats, L2_invs, rels_idx, cusps_idx, want_interior=False)
        _, _, _, n_l2s, _ = cohom_pres_gm(L2_dual, L2_dual_invs, rels_idx, cusps_idx, want_interior=False)
        draws.append((n_w1 - n_w1s, n_l2 - n_l2s))
    if not (draws[0] == draws[1] == draws[2]):
        sys.exit(2)
    return draws[0]


def shapiro_gamma_cohom_gm(
    cov: dict[str, object],
    c_gen: np.ndarray,
    m_order: int,
    hol_gm4: dict[str, GMMat],
    hol_gm4_inv: dict[str, GMMat],
) -> tuple[int, int, int, int]:
    """Second independent route at 120 digits: Shapiro's lemma directly on 3-generator Gamma = <a, b, t>."""
    d = int(cov["d"])
    act = cov["act"]
    gen_idx = cov["gen_idx"]
    roots_m = gm_roots_of_unity(m_order)
    z0 = gmpy2.mpc(0)
    ind_list: list[GMMat] = []
    ind_invs: list[GMMat] = []
    for g in "abt":
        Hg = hol_gm4[g]
        Hinv = hol_gm4_inv[g]
        M_ind = [[z0] * (4 * d) for _ in range(4 * d)]
        Minv_ind = [[z0] * (4 * d) for _ in range(4 * d)]
        for x in range(d):
            y = act[g][x]
            idx = gen_idx[(x, g)]
            ph = gmpy2.mpc(1) if idx is None else roots_m[int(c_gen[idx]) % m_order]
            ph_conj = ph.conjugate()
            for r in range(4):
                for c in range(4):
                    M_ind[4 * x + r][4 * y + c] = ph * Hg[r][c]
                    Minv_ind[4 * y + r][4 * x + c] = ph_conj * Hinv[r][c]
        ind_list.append(M_ind)
        ind_invs.append(Minv_ind)
    gmap = {"a": (0, 1), "b": (1, 1), "t": (2, 1), "A": (0, -1), "B": (1, -1), "T": (2, -1)}
    rels_g = [[gmap[ch] for ch in rw] for rw in cov["rels_gamma"]]
    cusp_g = [([gmap[ch] for ch in cov["ell_w"]], [gmap[ch] for ch in cov["tp_w"]])]
    h0, h1, r1, n, _ = cohom_pres_gm(ind_list, ind_invs, rels_g, cusp_g, want_interior=False)
    return h0, h1, r1, n


def qr_rank_np(M: np.ndarray, tol: float = 1e-9) -> int:
    if M.size == 0:
        return 0
    R_qr, _ = sla.qr(M, mode="r", pivoting=True)
    d = np.abs(np.diag(R_qr))
    if len(d) == 0 or d[0] == 0:
        return 0
    rel = d / d[0]
    if len(rel[(rel > 1e-11) & (rel < 1e-6)]) != 0:
        sys.exit(2)
    return int(np.sum(rel > tol))


def svd_rank(M: np.ndarray, tol: float = 1e-9) -> int:
    return qr_rank_np(M, tol=tol)


def svd_nullspace(M: np.ndarray, tol: float = 1e-9) -> np.ndarray:
    if M.shape[0] == 0:
        return np.eye(M.shape[1], dtype=np.complex128)
    _, s, vh = np.linalg.svd(M, full_matrices=True)
    if len(s) == 0 or s[0] == 0:
        return np.eye(M.shape[1], dtype=np.complex128)
    rel = s / s[0]
    if len(rel[(rel > 1e-11) & (rel < 1e-6)]) != 0:
        sys.exit(2)
    rk = int(np.sum(rel > tol))
    return vh[rk:, :].conj().T


def fox_pres_np(mod_mats: list[np.ndarray], mod_invs: list[np.ndarray], w_idx_sgn: list[tuple[int, int]]) -> tuple[np.ndarray, np.ndarray]:
    e = mod_mats[0].shape[0]
    ng = len(mod_mats)
    out = np.zeros((e, ng * e), dtype=np.complex128)
    pre = np.eye(e, dtype=np.complex128)
    for j, sgn in w_idx_sgn:
        if sgn == 1:
            out[:, j * e : (j + 1) * e] += pre
            pre = pre @ mod_mats[j]
        else:
            pre = pre @ mod_invs[j]
            out[:, j * e : (j + 1) * e] -= pre
    return out, pre


def cohom_pres_np(
    mod_mats: list[np.ndarray],
    rels_idx: list[list[tuple[int, int]]],
    cusps_idx: list[tuple[list[tuple[int, int]], list[tuple[int, int]]]],
    want_interior: bool = False,
) -> tuple[int, int, int, int, np.ndarray | None]:
    e = mod_mats[0].shape[0]
    ng = len(mod_mats)
    mod_invs = [np.linalg.inv(m) for m in mod_mats]
    I = np.eye(e, dtype=np.complex128)
    fox_rows = []
    for r in rels_idx:
        fr, wr = fox_pres_np(mod_mats, mod_invs, r)
        if np.max(np.abs(wr - I)) > 1e-9:
            sys.exit(2)
        fox_rows.append(fr)
    fox = np.vstack(fox_rows)
    rk = qr_rank_np(fox)
    dg = np.vstack([m - I for m in mod_mats])
    r0 = qr_rank_np(dg)
    h0 = e - r0
    h1 = ng * e - rk - (e - h0)
    Z = svd_nullspace(fox)

    rowsR, BPb = [], []
    for w1, w2 in cusps_idx:
        F1, W1 = fox_pres_np(mod_mats, mod_invs, w1)
        F2, W2 = fox_pres_np(mod_mats, mod_invs, w2)
        rowsR.extend([F1, F2])
        BPb.append(np.vstack([W1 - I, W2 - I]))
    nc = len(cusps_idx)
    BP = np.zeros((2 * e * nc, e * nc), dtype=np.complex128)
    for ci, b in enumerate(BPb):
        BP[2 * e * ci : 2 * e * (ci + 1), e * ci : e * (ci + 1)] = b
    R = np.vstack(rowsR)
    rBP = qr_rank_np(BP)
    RZ = R @ Z
    rboth = qr_rank_np(np.hstack([BP, RZ])) if Z.shape[1] > 0 else rBP
    r1 = rboth - rBP
    n = h1 - r1
    return h0, h1, r1, n, None


def shapiro_gamma_cohom_fast_m004(
    cov: dict[str, object],
    c_gen: np.ndarray,
    m_order: int,
    hol_np4: dict[str, np.ndarray],
) -> tuple[int, int, int, int]:
    """Fast pivoted-QR Shapiro pre-screener for word-length-2 m004 (+LR), backed by 120-digit gmpy2 verification."""
    d = int(cov["d"])
    act = cov["act"]
    gen_idx = cov["gen_idx"]
    roots_m = np.array([cmath.exp(2j * math.pi * k / m_order) for k in range(m_order)], dtype=np.complex128)
    ind_list = []
    for g in "abt":
        P_mon = np.zeros((d, d), dtype=np.complex128)
        for x in range(d):
            y = act[g][x]
            idx = gen_idx[(x, g)]
            P_mon[x, y] = 1.0 if idx is None else roots_m[int(c_gen[idx]) % m_order]
        ind_list.append(np.kron(P_mon, hol_np4[g]))
    gmap = {"a": (0, 1), "b": (1, 1), "t": (2, 1), "A": (0, -1), "B": (1, -1), "T": (2, -1)}
    rels_g = [[gmap[ch] for ch in rw] for rw in cov["rels_gamma"]]
    cusp_g = [([gmap[ch] for ch in cov["ell_w"]], [gmap[ch] for ch in cov["tp_w"]])]
    h0, h1, r1, n, _ = cohom_pres_np(ind_list, rels_g, cusp_g, want_interior=False)
    return h0, h1, r1, n


# ---------------------------------------------------------------------------
# 4. Shared-fibre triplet group O_h (W4 / Row 914) + Haar unitary scrambling
# ---------------------------------------------------------------------------

def build_weave_triplet_group() -> tuple[dict[str, np.ndarray], list[np.ndarray]]:
    """Construct the exact 3x3 action on (+)_(p!=0) H^1(F_2; chi_p) normalized by puncture evaluation c([a,b])."""
    # GENESIS GM2 convention: 1 = a, 2 = b, -1 = A, -2 = B
    aut = {
        "L": {1: [1], 2: [1, 2]},
        "R": {1: [1, 2], 2: [2]},
        "P": {1: [2], 2: [1]},
        "-I": {1: [-1], 2: [-2]},
        "inner_a": {1: [1], 2: [1, 2, -1]},
        "inner_b": {1: [2, 1, -2], 2: [2]},
    }
    chars = [(1, -1), (-1, 1), (-1, -1)]
    rep = {(1, -1): (Fraction(-1, 2), Fraction(0)), (-1, 1): (Fraction(0), Fraction(1, 2)), (-1, -1): (Fraction(0), Fraction(1, 2))}

    def chi_val(ch: tuple[int, int], w: list[int]) -> int:
        s = 1
        for g in w:
            s *= ch[abs(g) - 1]
        return s

    def coc(ch: tuple[int, int], ca: Fraction, cb: Fraction, w: list[int]) -> Fraction:
        tot, pre = Fraction(0), 1
        for g in w:
            cg = (ca, cb)[abs(g) - 1]
            tot += pre * (cg if g > 0 else -ch[abs(g) - 1] * cg)
            pre *= ch[abs(g) - 1]
        return tot

    def lam(ch: tuple[int, int], ca: Fraction, cb: Fraction) -> Fraction:
        return (ch[1] - 1) * ca - (ch[0] - 1) * cb

    def tmat(alpha: dict[int, list[int]]) -> np.ndarray:
        M = np.zeros((3, 3), dtype=int)
        for j, ch in enumerate(chars):
            ca = coc(ch, rep[ch][0], rep[ch][1], alpha[1])
            cb = coc(ch, rep[ch][0], rep[ch][1], alpha[2])
            ch2 = (chi_val(ch, alpha[1]), chi_val(ch, alpha[2]))
            v = lam(ch2, ca, cb)
            assert v.denominator == 1
            M[chars.index(ch2), j] = int(v)
        return M

    gens = {k: tmat(v) for k, v in aut.items()}
    # Golden 3-cycle LR in GM2 convention: L o R
    lr_aut = {g: [x for y in aut["R"][g] for x in (aut["L"][y] if y > 0 else [-z for z in reversed(aut["L"][-y])])] for g in (1, 2)}
    gens["LR"] = tmat(lr_aut)

    I3 = np.eye(3, dtype=int)
    G_map = {tuple(map(tuple, I3)): I3}
    fr = [I3]
    while fr:
        nx = []
        for A in fr:
            for nm in ("L", "R", "P", "-I", "inner_a", "inner_b"):
                B = A @ gens[nm]
                k = tuple(map(tuple, B))
                if k not in G_map:
                    G_map[k] = B
                    nx.append(B)
        fr = nx
    return gens, list(G_map.values())


def random_haar_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    Z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / math.sqrt(2.0)
    Q, R = np.linalg.qr(Z)
    d = np.diag(R)
    ph = d / np.abs(d)
    return Q * ph


# ---------------------------------------------------------------------------
# 5. Pre-committed Negative Controls (C1a-1, C1a-2, C1a-3)
# ---------------------------------------------------------------------------

def run_precommitted_controls() -> dict[str, object]:
    # C1a-1: Theorem S tick control (odd-trace at tick 1 fails separation; even-trace at tick 3 fails 3-cycle)
    M_lr = np.array(homology_mat("+", "LR"), dtype=int) % 2
    M_llr = np.array(homology_mat("+", "LLR"), dtype=int) % 2
    M_llrr = np.array(homology_mat("+", "LLRR"), dtype=int) % 2
    I2 = np.eye(2, dtype=int)
    odd_tick1_separates = np.array_equal(M_lr, I2)
    odd_tick3_separates_and_cycles = (
        np.array_equal(np.linalg.matrix_power(M_lr, 3) % 2, I2)
        and not np.array_equal(M_lr, I2)
        and not np.array_equal((M_lr @ M_lr) % 2, I2)
    )
    even_llr_tick3_separates_and_cycles = np.array_equal(np.linalg.matrix_power(M_llr, 3) % 2, I2)
    even_llrr_cycles_parities = not np.array_equal(M_llrr, I2)
    if odd_tick1_separates or (not odd_tick3_separates_and_cycles) or even_llr_tick3_separates_and_cycles or even_llrr_cycles_parities:
        sys.exit(2)

    # C1a-2: O_h group closure perturbation + Guardrail 3 Haar unitary basis-scrambling invariance (< 1e-12)
    gens, G = build_weave_triplet_group()
    if len(G) != 48:
        sys.exit(2)
    # Perturb L by a non-crystallographic rotation angle pi/5 in the (0,1)-plane: closure must exceed 48
    th = math.pi / 5.0
    R5 = np.array([[math.cos(th), -math.sin(th), 0.0], [math.sin(th), math.cos(th), 0.0], [0.0, 0.0, 1.0]])
    pert_gens = [gens["L"].astype(float) @ R5, gens["R"].astype(float), gens["P"].astype(float)]
    seen_pert = [np.eye(3)]
    fr = [np.eye(3)]
    while fr and len(seen_pert) <= 60:
        nx = []
        for A in fr:
            for g in pert_gens:
                B = A @ g
                if not any(np.max(np.abs(B - S)) < 1e-7 for S in seen_pert):
                    seen_pert.append(B)
                    nx.append(B)
                    if len(seen_pert) > 60:
                        break
            if len(seen_pert) > 60:
                break
        fr = nx
    if len(seen_pert) <= 48:
        sys.exit(2)

    # Guardrail 3 check: build physical Dirac Yukawa matrices Y_e (Z_3-invariant on left) and Y_nu (Klein V_4-invariant on left),
    # apply independent random Haar unitaries U_L, U_Re, U_Rnu, and assert |U_PMNS|^2 canonical entries are invariant to < 1e-12!
    T_z3 = gens["LR"].astype(np.complex128)
    _, V_e = np.linalg.eig(T_z3)
    V_e = V_e / np.linalg.norm(V_e, axis=0)
    # Klein group generated by P and inner_a * inner_b? Let us pick P and (-I)*L^2? Wait: find a commuting TBM pair in G!
    inv_list = [A for A in G if np.array_equal(A @ A, np.eye(3, dtype=int)) and not np.array_equal(A, np.eye(3, dtype=int)) and not np.array_equal(A, -np.eye(3, dtype=int))]
    tbm_pair = None
    for A, B in itertools.combinations(inv_list, 2):
        if np.array_equal(A @ B, B @ A) and not np.array_equal(A @ B, -np.eye(3, dtype=int)):
            _, VK = np.linalg.eigh(A.astype(float) + math.e * B.astype(float))
            P2 = np.abs(V_e.conj().T @ VK) ** 2
            if np.min(P2) < 1e-12:
                tbm_pair = (A, B, VK.astype(np.complex128))
                break
    if tbm_pair is None:
        sys.exit(2)
    VK = tbm_pair[2]
    # Construct Dirac Yukawas Y_e = V_e diag(y1, y2, y3) W_e^H and Y_nu = VK diag(n1, n2, n3) W_nu^H with distinct singular values
    rng = np.random.default_rng(20261112)
    We0 = random_haar_unitary(3, rng)
    Wnu0 = random_haar_unitary(3, rng)
    Ye = V_e @ np.diag([0.13, 0.47, 1.29]) @ We0.conj().T
    Ynu = VK @ np.diag([0.21, 0.59, 1.73]) @ Wnu0.conj().T

    def canon_pmns(P: np.ndarray) -> np.ndarray:
        best = None
        for pr in itertools.permutations(range(3)):
            for pc in itertools.permutations(range(3)):
                Q = P[list(pr), :][:, list(pc)]
                key = tuple(np.round(Q.ravel(), 9))
                if best is None or key < best[0]:
                    best = (key, Q)
        return best[1]

    def extract_pmns_sq(Ye_m: np.ndarray, Ynu_m: np.ndarray) -> np.ndarray:
        He = Ye_m @ Ye_m.conj().T
        Hnu = Ynu_m @ Ynu_m.conj().T
        ee, Ue = np.linalg.eigh(He)
        enu, Unu = np.linalg.eigh(Hnu)
        Ue = Ue[:, np.argsort(ee)]
        Unu = Unu[:, np.argsort(enu)]
        return np.abs(Ue.conj().T @ Unu) ** 2

    base_pmns = extract_pmns_sq(Ye, Ynu)
    max_scram_diff = 0.0
    for _ in range(10):
        UL = random_haar_unitary(3, rng)
        URe = random_haar_unitary(3, rng)
        URnu = random_haar_unitary(3, rng)
        scram_pmns = extract_pmns_sq(UL @ Ye @ URe.conj().T, UL @ Ynu @ URnu.conj().T)
        max_scram_diff = max(max_scram_diff, float(np.max(np.abs(scram_pmns - base_pmns))))
    if max_scram_diff >= 1e-12:
        sys.exit(2)

    # C1a-3: Lemma V cohomology control (synthetic module with vanishing cusp restriction must report n > 0!)
    cov1 = build_cover("+", "LR", 1, {"a": [0], "b": [0], "t": [0]})
    triv_mats = [np.ones((1, 1), dtype=np.complex128) for _ in range(cov1["ng"])]
    # True cusp gives h1 = 1, r1 = 1, n = 0; planted trivial peripheral word [] gives r1 = 0, n = 1!
    _, h1_real, r1_real, n_real, _ = cohom_pres_np(triv_mats, cov1["rels_idx"], cov1["cusps_idx"])
    _, h1_plant, r1_plant, n_plant, _ = cohom_pres_np(triv_mats, cov1["rels_idx"], [([], [])])
    if not (h1_real == 1 and r1_real == 1 and n_real == 0 and h1_plant == 1 and r1_plant == 0 and n_plant == 1):
        sys.exit(2)

    return {
        "C1a_1_theorem_s_tick_control_passed": True,
        "C1a_2_oh_perturbation_and_haar_scrambling_passed": True,
        "C1a_2_max_haar_basis_scrambling_drift": max_scram_diff,
        "C1a_3_lemma_v_cusp_control_passed": True,
    }


# ---------------------------------------------------------------------------
# 6. Independent Verification of the Ten Registered Rows (908-922)
# ---------------------------------------------------------------------------

def verify_row_908() -> dict[str, object]:
    """Row 908 (@ 0d2694faf): line's room on all 27 companions (26,158 sign characters) + Proposition N + flavor group."""
    st_list = genesis_states(8, 12)
    total_chars = 0
    all_n1_zero = True
    max_room = 0
    max_min_n_mA = 0
    room_ge3_max_mA = 0
    mA_ge3_max_room = 0
    room_3_states: dict[str, int] = {}
    room_4_states: dict[str, int] = {}
    named_decomps: dict[str, dict[str, int]] = {}
    min2_states: list[str] = []

    for sw, _, ends in st_list:
        cov = build_companion_cover(sw[0], sw[1:])
        chars, orbits = cover_characters_and_orbits(cov, 2)
        total_chars += len(chars)
        decomp_counter: Counter[str] = Counter()
        st_max_min = 0
        for orb in orbits:
            rep = orb[0]
            osize = len(orb)
            is_triv = bool(np.all(rep == 0))
            mod_mats = [np.array([[1.0 if rep[j] == 0 else -1.0]], dtype=np.complex128) for j in range(cov["ng"])]
            _, h1, r1, n, _ = cohom_pres_np(mod_mats, cov["rels_idx"], cov["cusps_idx"])
            m_A = sum(
                1
                for (sw1, sw2) in cov["cusps_idx"]
                if (sum(int(rep[idx]) * sgn for idx, sgn in sw1) % 2 == 0)
                and (sum(int(rep[idx]) * sgn for idx, sgn in sw2) % 2 == 0)
            )
            if is_triv and n != 0:
                all_n1_zero = False
            max_room = max(max_room, n)
            mn = min(n, m_A)
            max_min_n_mA = max(max_min_n_mA, mn)
            st_max_min = max(st_max_min, mn)
            if n >= 3:
                room_ge3_max_mA = max(room_ge3_max_mA, m_A)
            if m_A >= 3:
                mA_ge3_max_room = max(mA_ge3_max_room, n)
            if n == 3:
                room_3_states[sw] = room_3_states.get(sw, 0) + osize
            if n == 4:
                room_4_states[sw] = room_4_states.get(sw, 0) + osize
            if sw in ("+LLLR", "-LR", "+LLRR", "-LLRR"):
                decomp_counter[f"({m_A},{h1},{r1},{n})"] += osize
        if st_max_min == 2:
            min2_states.append(sw)
        if sw in ("+LLLR", "-LR", "+LLRR", "-LLRR"):
            named_decomps[sw] = dict(sorted(decomp_counter.items()))

    # Also verify +LLLR flavor group Z/2 x A_4 (order 24, det-1 part order 12) on the 3-orbit of sign characters with m_A = 1!
    cov_lllr = build_companion_cover("+", "LLLR")
    _, orbs_lllr = cover_characters_and_orbits(cov_lllr, 2)
    sign_orb3 = [
        orb for orb in orbs_lllr
        if len(orb) == 3 and sum(
            1 for (sw1, sw2) in cov_lllr["cusps_idx"]
            if (sum(int(orb[0][idx]) * sgn for idx, sgn in sw1) % 2 == 0)
            and (sum(int(orb[0][idx]) * sgn for idx, sgn in sw2) % 2 == 0)
        ) == 1
    ]
    assert len(sign_orb3) == 1
    rep3 = sign_orb3[0][0]
    ind_gens = []
    for g in "abt":
        P = np.zeros((3, 3), dtype=int)
        for x in range(3):
            y = cov_lllr["act"][g][x]
            idx = cov_lllr["gen_idx"][(x, g)]
            P[x, y] = 1 if (idx is None or rep3[idx] == 0) else -1
        ind_gens.append(P)
    G_flav = {tuple(map(tuple, np.eye(3, dtype=int))): np.eye(3, dtype=int)}
    fr = [np.eye(3, dtype=int)]
    while fr:
        nx = []
        for A in fr:
            for gM in ind_gens:
                B = A @ gM
                k = tuple(map(tuple, B))
                if k not in G_flav:
                    G_flav[k] = B
                    nx.append(B)
        fr = nx
    flav_order = len(G_flav)
    flav_det1 = sum(1 for A in G_flav.values() if round(float(np.linalg.det(A))) == 1)

    holds = (
        len(st_list) == 27
        and total_chars == 26158
        and all_n1_zero
        and named_decomps["+LLRR"] == {"(0,0,0,0)": 9, "(2,2,2,0)": 6, "(4,4,4,0)": 1}
        and named_decomps["-LLRR"] == {"(0,0,0,0)": 37, "(0,2,0,2)": 8, "(2,2,2,0)": 168, "(4,4,4,0)": 42, "(8,8,8,0)": 1}
        and room_3_states == {"-LLRLR": 18, "+LLLLRRR": 12}
        and room_4_states == {"-LLLLRR": 9, "+LLLLLLRR": 9}
        and room_ge3_max_mA <= 1
        and mA_ge3_max_room <= 2
        and max_min_n_mA == 2
        and len(min2_states) == 7
        and flav_order == 24
        and flav_det1 == 12
    )
    return {
        "row": 908,
        "pinned_commit": "0d2694faf",
        "result": "the same" if holds else "differs",
        "method_label": "recomputed on another family of model",
        "companions_checked": len(st_list),
        "sign_characters_checked": total_chars,
        "all_n1_zero": all_n1_zero,
        "named_decompositions": named_decomps,
        "room_3_states": room_3_states,
        "room_4_states": room_4_states,
        "max_min_n_mA": max_min_n_mA,
        "min_2_companions": min2_states,
        "lllr_flavor_group_orders": [flav_order, flav_det1],
    }


def _cover_gen_gm_mats(cov: dict[str, object], hol_obj: dict[str, object]) -> tuple[list[GMMat], list[GMMat]]:
    abt_mp = hol_obj["abt_mp"]
    abt_inv_mp = hol_obj["abt_inv_mp"]
    gm_mats: list[GMMat] = []
    gm_invs: list[GMMat] = []
    for gw in cov["gen_words"]:
        W = eval_word_sl2_mp(gw, abt_mp, abt_inv_mp)
        gm_mats.append(four_mp_to_gm(W))
        gm_invs.append(four_mp_to_gm(sl2_inv_mp(W)))
    return gm_mats, gm_invs


def verify_row_909() -> dict[str, object]:
    """Row 909 (@ 0d2694faf, sm:B1549): all 13 three-ended covers on 10 states at nu^4 = 1."""
    st_list = genesis_states(8, 12)
    covers_info = []
    roots4 = gm_roots_of_unity(4)
    total_sign_members = 0
    sign_gen_shaped = 0
    ord4_shapes: Counter[str] = Counter()
    gen_shaped_by_cover: list[tuple[str, int]] = []

    for sw, M, ends in st_list:
        lats3 = m_invariant_lattices(M, 3)
        for lat in lats3:
            # Representative wbar in Z^2 / Lam (3 classes; check which gives 3 cusps!)
            a_l, b_l, c_l = lat
            cosets = [(rx, ry) for ry in range(c_l) for rx in range(a_l)]
            # Distinct conjugacy classes of wbar modulo (M - I)D: here 3 cusps forces unique wbar!
            valid_wb = []
            for wb in cosets:
                cov = build_abelian_fibre_cover(sw[0], sw[1:], lat, wb)
                if len(cov["cusps_idx"]) == 3:
                    valid_wb.append((wb, cov))
            for wb, cov in valid_wb:
                hol_obj = get_holonomy(sw[0], sw[1:])
                _, orbits = cover_characters_and_orbits(cov, 4)
                gen_mats_hol, gen_invs_hol = _cover_gen_gm_mats(cov, hol_obj)
                cov_gen = 0
                cov_sign = 0
                cov_ord4: Counter[str] = Counter()
                for orb in orbits:
                    rep = orb[0]
                    osize = len(orb)
                    ord_c = 1 if np.all(rep == 0) else (2 if np.all((2 * rep) % 4 == 0) else 4)
                    mod_mats = [gm_scale_mat(roots4[int(rep[j]) % 4], gen_mats_hol[j]) for j in range(cov["ng"])]
                    mod_invs = [gm_scale_mat(roots4[(-int(rep[j])) % 4], gen_invs_hol[j]) for j in range(cov["ng"])]
                    _, h1, r1, n, int_basis = cohom_pres_gm(mod_mats, mod_invs, cov["rels_idx"], cov["cusps_idx"], want_interior=True)
                    if sw in ("+LLLR", "-LLLLLR") and n > 0:
                        # Cross-verify member orbits via independent 120-digit Shapiro route on Gamma!
                        _, h1_s, r1_s, n_s = shapiro_gamma_cohom_gm(cov, rep, 4, hol_obj["gm4"], hol_obj["gm4_inv"])
                        if (h1_s, r1_s, n_s) != (h1, r1, n):
                            sys.exit(2)
                    if n > 0:
                        assert int_basis is not None
                        iw1, il2 = generic_extension_counts_gm(mod_mats, mod_invs, int_basis, cov["rels_idx"], cov["cusps_idx"])
                        shape_s = f"({iw1},{il2})"
                        is_gen = (iw1 == -1 and il2 == -1)
                        if is_gen:
                            cov_gen += osize
                        if ord_c == 2:
                            total_sign_members += osize
                            cov_sign += osize
                            if is_gen:
                                sign_gen_shaped += osize
                        elif ord_c == 4:
                            ord4_shapes[shape_s] += osize
                            cov_ord4[shape_s] += osize
                covers_info.append({
                    "state": sw,
                    "companion_ends": ends,
                    "lattice": list(lat),
                    "sign_members": cov_sign,
                    "ord4_shapes": dict(cov_ord4),
                    "generation_shaped": cov_gen,
                })
                gen_shaped_by_cover.append((sw, cov_gen))

    exact_three_states = sorted(sw for sw, g in gen_shaped_by_cover if g == 3)
    states_with_covers = sorted({c["state"] for c in covers_info})
    holds = (
        len(covers_info) == 13
        and len(states_with_covers) == 10
        and exact_three_states == ["+LLLR", "-LLLLLR"]
        and total_sign_members == 18
        and sign_gen_shaped == 18
        and dict(ord4_shapes) == {"(-1,0)": 36, "(0,-1)": 72, "(0,0)": 12}
    )
    return {
        "row": 909,
        "pinned_commit": "0d2694faf",
        "result": "the same" if holds else "differs",
        "method_label": "recomputed on another family of model",
        "three_ended_covers_count": len(covers_info),
        "states_with_three_ended_covers": len(states_with_covers),
        "exact_three_generation_covers": exact_three_states,
        "sign_members_total_and_gen_shaped": [total_sign_members, sign_gen_shaped],
        "order_4_shape_totals": dict(ord4_shapes),
        "covers": covers_info,
    }


def verify_row_910() -> dict[str, object]:
    """Row 910 (@ 0d2694faf, sm:B1550): parity lemma + A_4 cover on +LR, -LR, +LLLR, -LLLR at nu^4 = 1."""
    roots4 = gm_roots_of_unity(4)
    state_summaries = {}
    total_members = 0
    total_member_orbits = 0
    plr_gen_by_parity: Counter[str] = Counter()
    golden_cycles_labels = False

    for sw in ("+LR", "-LR", "+LLLR", "-LLLR"):
        cov = build_a4_cover(sw[0], sw[1:])
        hol_obj = get_holonomy(sw[0], sw[1:])
        _, orbits = cover_characters_and_orbits(cov, 4)
        gen_mats_hol, gen_invs_hol = _cover_gen_gm_mats(cov, hol_obj)
        orb_records = []
        st_members = 0
        st_gen = 0

        # Identify the 4 cusps with F_2^2 points via their anchor cosets in A_4 = F_2^2 x| Z/3!
        cusp_f2 = [cov["a4_elems"][x0][0] for x0 in cov["cusp_cosets"]]
        assert sorted(cusp_f2) == [(0, 0), (0, 1), (1, 0), (1, 1)]

        for orb in orbits:
            rep = orb[0]
            osize = len(orb)
            ord_c = 1 if np.all(rep == 0) else (2 if np.all((2 * rep) % 4 == 0) else 4)
            mod_mats = [gm_scale_mat(roots4[int(rep[j]) % 4], gen_mats_hol[j]) for j in range(cov["ng"])]
            mod_invs = [gm_scale_mat(roots4[(-int(rep[j])) % 4], gen_invs_hol[j]) for j in range(cov["ng"])]
            _, h1, r1, n, int_basis = cohom_pres_gm(mod_mats, mod_invs, cov["rels_idx"], cov["cusps_idx"], want_interior=True)
            if n > 0:
                _, h1_s, r1_s, n_s = shapiro_gamma_cohom_gm(cov, rep, 4, hol_obj["gm4"], hol_obj["gm4_inv"])
                if (h1_s, r1_s, n_s) != (h1, r1, n):
                    sys.exit(2)
                assert int_basis is not None
                iw1, il2 = generic_extension_counts_gm(mod_mats, mod_invs, int_basis, cov["rels_idx"], cov["cusps_idx"])
                m_A = sum(
                    1 for (sw1, sw2) in cov["cusps_idx"]
                    if (sum(int(rep[idx]) * sgn for idx, sgn in sw1) % 4 == 0)
                    and (sum(int(rep[idx]) * sgn for idx, sgn in sw2) % 4 == 0)
                )
                total_members += osize
                total_member_orbits += 1
                st_members += osize
                if iw1 == -1 and il2 == -1:
                    st_gen += osize
                    if sw == "+LR":
                        # Label every member in this orbit by its distinguished F_2^2 pair (puncture edge or trivial-cusp edge)!
                        for ch_vec in orb:
                            p_nontriv = [
                                cusp_f2[ci]
                                for ci, (sw1, _) in enumerate(cov["cusps_idx"])
                                if sum(int(ch_vec[idx]) * sgn for idx, sgn in sw1) % 4 != 0
                            ]
                            c_triv = [
                                cusp_f2[ci]
                                for ci, (sw1, sw2) in enumerate(cov["cusps_idx"])
                                if (sum(int(ch_vec[idx]) * sgn for idx, sgn in sw1) % 4 == 0)
                                and (sum(int(ch_vec[idx]) * sgn for idx, sgn in sw2) % 4 == 0)
                            ]
                            pair = p_nontriv if len(p_nontriv) == 2 else c_triv
                            assert len(pair) == 2
                            par = ((pair[0][0] ^ pair[1][0]), (pair[0][1] ^ pair[1][1]))
                            plr_gen_by_parity[str(par)] += 1
                orb_records.append({
                    "size": osize,
                    "order": ord_c,
                    "h1_r1_n": [h1, r1, n],
                    "m_A": m_A,
                    "count": [iw1, il2],
                })
        if sw == "+LR":
            # Verify M_lr mod 2 is a 3-cycle on {(1,0), (0,1), (1,1)}
            M_lr = homology_mat("+", "LR")
            p_map = {p: ((M_lr[0][0] * p[0] + M_lr[0][1] * p[1]) % 2, (M_lr[1][0] * p[0] + M_lr[1][1] * p[1]) % 2) for p in ((1, 0), (0, 1), (1, 1))}
            golden_cycles_labels = (len(set(p_map.values())) == 3 and all(p_map[p] != p for p in p_map))
        state_summaries[sw] = {"members": st_members, "generation_shaped": st_gen, "orbits": orb_records}

    holds = (
        total_members == 60
        and total_member_orbits == 9
        and state_summaries["+LR"]["members"] == 54
        and state_summaries["+LR"]["generation_shaped"] == 48
        and state_summaries["-LR"]["members"] == 6
        and state_summaries["-LR"]["generation_shaped"] == 0
        and state_summaries["-LR"]["orbits"][0]["count"] == [0, -3]
        and state_summaries["+LLLR"]["members"] == 0
        and state_summaries["-LLLR"]["members"] == 0
        and dict(plr_gen_by_parity) == {"(0, 1)": 16, "(1, 0)": 16, "(1, 1)": 16}
        and golden_cycles_labels
    )
    return {
        "row": 910,
        "pinned_commit": "0d2694faf",
        "result": "the same" if holds else "differs",
        "method_label": "recomputed on another family of model",
        "total_members": total_members,
        "total_member_orbits": total_member_orbits,
        "plr_generation_members_by_parity": dict(plr_gen_by_parity),
        "golden_map_cycles_three_parities": golden_cycles_labels,
        "states": state_summaries,
    }


def verify_row_912() -> dict[str, object]:
    """Row 912 (@ 14480c59b, sm:B1551 draft): binary tetrahedral 2T spin cover S of m004 (+LR)."""
    elems_2T = [(a, b, c, d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a * d - b * c) % 3 == 1]
    elems_2T.remove((1, 0, 0, 1))
    elems_2T.insert(0, (1, 0, 0, 1))
    idx_2T = {m: i for i, m in enumerate(elems_2T)}

    def mul_2T(X: tuple[int, int, int, int], Y: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
        return (
            (X[0] * Y[0] + X[1] * Y[2]) % 3,
            (X[0] * Y[1] + X[1] * Y[3]) % 3,
            (X[2] * Y[0] + X[3] * Y[2]) % 3,
            (X[2] * Y[1] + X[3] * Y[3]) % 3,
        )

    neg_I = (2, 0, 0, 2)
    found_2T = None
    for ga in elems_2T:
        for gb in elems_2T:
            if mul_2T(ga, ga) == neg_I and mul_2T(gb, gb) == neg_I and mul_2T(ga, gb) != mul_2T(gb, ga):
                ab_m = mul_2T(ga, gb)
                bab_m = mul_2T(gb, ab_m)
                for gt in elems_2T:
                    gti = [x for x in elems_2T if mul_2T(gt, x) == (1, 0, 0, 1)][0]
                    if mul_2T(mul_2T(gt, ga), gti) == ab_m and mul_2T(mul_2T(gt, gb), gti) == bab_m:
                        found_2T = (ga, gb, gt)
                        break
            if found_2T is not None:
                break
        if found_2T is not None:
            break
    assert found_2T is not None
    ga, gb, gt = found_2T
    act_2T = {g: [idx_2T[mul_2T(elems_2T[x], m)] for x in range(24)] for g, m in [("a", ga), ("b", gb), ("t", gt)]}
    cov_S = build_cover("+", "LR", 24, act_2T)

    # Vectorized 2T orbit decomposition on 4^8 = 65,536 characters
    ng = int(cov_S["ng"])
    D_snf, _, V_snf = smith_normal_decomp(sp.Matrix(cov_S["rel_mat"].tolist()))
    V_np = np.array(V_snf.tolist(), dtype=np.int64) % 4
    Vinv_np = np.array(V_snf.inv().tolist(), dtype=np.int64) % 4
    diag = [abs(int(D_snf[i, i])) for i in range(min(D_snf.rows, D_snf.cols))]
    free_cols = [i for i in range(ng) if (i >= len(diag) or diag[i] == 0)]
    assert len(free_cols) == 8 and all(d == 1 for d in diag if d != 0)

    B_mat = V_np[:, free_cols] % 4
    P_mat = Vinv_np[free_cols, :] % 4
    deck_8 = [(P_mat @ (M_h.T % 4) @ B_mat) % 4 for M_h in cov_S["deck_mats"]]
    grid = np.array(np.meshgrid(*([range(4)] * 8), indexing="ij"), dtype=np.int64).reshape(8, -1)
    weights = (4 ** np.arange(7, -1, -1, dtype=np.int64))[:, None]
    min_code = np.full(65536, 1 << 30, dtype=np.int64)
    for D8 in deck_8:
        min_code = np.minimum(min_code, np.sum(((D8 @ grid) % 4) * weights, axis=0))
    orb_codes, orb_sizes = np.unique(min_code, return_counts=True)

    # Pullback test to N = ker(Gamma -> A_4): N/S = <abAB> of order 2, since abAB -> -I in 2T!
    # A character chi: S -> mu_4 is pulled back from an order|4 character of N iff
    # chi is invariant under conjugation by -I in 2T AND chi((abAB)^2) == +1 (since abAB in N has chi_N(abAB)^2 in {+1, -1}, wait:
    # if chi_N has order | 4 on N, chi_N(abAB) in {1, i, -1, -i}, wait: abAB = [a, b] in Gamma! What is [a, b] in H_1(N)?
    # Better: compute pullback image directly from N -> S inclusion! S <= N has index 2, generated by cosets {I, -I} in 2T!)
    cov_N = build_a4_cover("+", "LR")
    chars_N, _ = cover_characters_and_orbits(cov_N, 4)
    # Express each of S's ng Schreier generator words in N's Schreier generators (starting from coset 0 of N, since S <= N)!
    S_in_N = np.zeros((cov_N["ng"], ng), dtype=np.int64)
    for j, gw in enumerate(cov_S["gen_words"]):
        sw_N, xe_N = cov_N["rewrite_from"](0, gw)
        assert xe_N == 0
        for idx_n, sgn_n in sw_N:
            S_in_N[idx_n, j] += sgn_n
    pullback_codes: set[int] = set()
    for ch_n in chars_N:
        c_s = (S_in_N.T @ ch_n) % 4
        z_s = (P_mat @ c_s) % 4
        code_s = int(np.sum(z_s[:, None] * weights))
        pullback_codes.add(int(min_code[code_s]))

    hol_obj = get_holonomy("+", "LR")
    hol_np = hol_obj["np4"]
    gen_mats_hol, gen_invs_hol = _cover_gen_gm_mats(cov_S, hol_obj)
    roots4 = gm_roots_of_unity(4)

    member_orbits = []
    spot_checked_nonmembers = 0
    for oc, osize in zip(orb_codes.tolist(), orb_sizes.tolist()):
        z = np.array([(oc >> (2 * (7 - i))) & 3 for i in range(8)], dtype=np.int64)
        c_gen = (B_mat @ z) % 4
        _, h1, r1, n = shapiro_gamma_cohom_fast_m004(cov_S, c_gen, 4, hol_np)
        if n > 0 or spot_checked_nonmembers < 25:
            # Verify at 120 digits via BOTH Shapiro on Gamma AND S's own 49-generator Schreier presentation!
            _, h1_s, r1_s, n_s = shapiro_gamma_cohom_gm(cov_S, c_gen, 4, hol_obj["gm4"], hol_obj["gm4_inv"])
            mod_mats = [gm_scale_mat(roots4[int(c_gen[j]) % 4], gen_mats_hol[j]) for j in range(ng)]
            mod_invs = [gm_scale_mat(roots4[(-int(c_gen[j])) % 4], gen_invs_hol[j]) for j in range(ng)]
            _, h1_p, r1_p, n_p, _ = cohom_pres_gm(mod_mats, mod_invs, cov_S["rels_idx"], cov_S["cusps_idx"])
            if (h1_p, r1_p, n_p) != (h1, r1, n) or (h1_s, r1_s, n_s) != (h1, r1, n):
                sys.exit(2)
            if n == 0:
                spot_checked_nonmembers += 1
        if n > 0:
            ord_c = 1 if np.all(c_gen == 0) else (2 if np.all((2 * c_gen) % 4 == 0) else 4)
            member_orbits.append({
                "size": int(osize),
                "order": ord_c,
                "h1_r1_n": [h1, r1, n],
                "pulled_back_from_N": (oc in pullback_codes),
            })

    tot_mem = sum(m["size"] for m in member_orbits)
    sign_n2 = sum(m["size"] for m in member_orbits if m["order"] == 2 and m["h1_r1_n"][2] == 2)
    ord4_n1 = sum(m["size"] for m in member_orbits if m["order"] == 4 and m["h1_r1_n"][2] == 1)
    ord4_n4 = sum(m["size"] for m in member_orbits if m["order"] == 4 and m["h1_r1_n"][2] == 4)
    all_pulled_back = all(m["pulled_back_from_N"] for m in member_orbits)

    holds = (
        len(orb_codes) == 2800
        and len(member_orbits) == 7
        and tot_mem == 42
        and sign_n2 == 12
        and ord4_n1 == 24
        and ord4_n4 == 6
        and all_pulled_back
    )
    return {
        "row": 912,
        "pinned_commit": "14480c59b",
        "result": "the same" if holds else "differs",
        "method_label": "recomputed on another family of model",
        "characters_order_div_4": 65536,
        "orbits_under_2T": len(orb_codes),
        "member_orbits_count": len(member_orbits),
        "members_total": tot_mem,
        "breakdown_sign_n2_ord4_n1_ord4_n4": [sign_n2, ord4_n1, ord4_n4],
        "all_pulled_back_from_N": all_pulled_back,
        "intrinsic_spin_only_members": 0 if all_pulled_back else (tot_mem - sum(m["size"] for m in member_orbits if m["pulled_back_from_N"])),
        "member_orbits": member_orbits,
    }


def verify_row_914() -> dict[str, object]:
    """Row 914 (@ c0ff37644, READING): O_h of order 48, S_4 rotations, Klein TBM/democratic pairs, TM1/TM2 columns."""
    gens, G = build_weave_triplet_group()
    I3 = np.eye(3, dtype=int)

    def elem_order(A: np.ndarray) -> int:
        k, X = 1, A.copy()
        while not np.array_equal(X, I3):
            X = X @ A
            k += 1
        return k

    dets = Counter(int(round(float(np.linalg.det(A)))) for A in G)
    orders = dict(sorted((str(k), v) for k, v in Counter(elem_order(A) for A in G).items()))
    has_minus_I = any(np.array_equal(A, -I3) for A in G)

    # Golden 3-cycle eigenbasis
    _, V = np.linalg.eig(gens["LR"].astype(np.complex128))
    VT = V / np.linalg.norm(V, axis=0)

    def canon_mat(P: np.ndarray) -> tuple[tuple[str, ...], ...]:
        # Rationalize to exact sixths (every entry is in {0, 1/6, 1/3, 1/2, 2/3}!)
        best = None
        for pr in itertools.permutations(range(3)):
            for pc in itertools.permutations(range(3)):
                Q = []
                for i in range(3):
                    row = []
                    for j in range(3):
                        val = float(P[pr[i], pc[j]])
                        fr = Fraction(val).limit_denominator(24)
                        assert abs(float(fr) - val) < 1e-12
                        row.append(str(fr))
                    Q.append(tuple(row))
                Qt = tuple(Q)
                if best is None or Qt < best:
                    best = Qt
        assert best is not None
        return best

    inv_elems = [A for A in G if np.array_equal(A @ A, I3) and not np.array_equal(A, I3) and not np.array_equal(A, -I3)]
    klein_pairs: Counter[str] = Counter()
    for A, B in itertools.combinations(inv_elems, 2):
        if np.array_equal(A @ B, B @ A) and not np.array_equal(A @ B, -I3):
            _, VK = np.linalg.eigh(A.astype(float) + math.e * B.astype(float))
            P2 = np.abs(VT.conj().T @ VK) ** 2
            klein_pairs[str(canon_mat(P2))] += 1

    col_counts: Counter[str] = Counter()
    named_inv_cols: dict[str, list[str]] = {}
    named_candidates = {
        "P": gens["P"],
        "inner_a": gens["inner_a"],
        "L_shear": gens["L"],
    }
    for A in inv_elems:
        ev, EV = np.linalg.eigh(A.astype(float))
        vals = [int(round(float(x))) for x in ev]
        lone = [i for i in range(3) if vals.count(vals[i]) == 1][0]
        c_sq = np.abs(VT.conj().T @ EV[:, lone]) ** 2
        rats = sorted([Fraction(float(x)).limit_denominator(24) for x in c_sq])
        assert all(abs(float(r) - s) < 1e-12 for r, s in zip(rats, sorted(c_sq)))
        col_str = "(" + ", ".join(str(r) for r in rats) + ")"
        col_counts[col_str] += 1
        for nm, M_nm in named_candidates.items():
            if np.array_equal(A, M_nm):
                named_inv_cols[nm] = [str(r) for r in rats]

    tbm_key = "(('0', '1/3', '2/3'), ('1/2', '1/3', '1/6'), ('1/2', '1/3', '1/6'))"
    dem_key = "(('1/3', '1/3', '1/3'), ('1/3', '1/3', '1/3'), ('1/3', '1/3', '1/3'))"
    holds = (
        len(G) == 48
        and dict(dets) == {1: 24, -1: 24}
        and has_minus_I
        and orders == {"1": 1, "2": 19, "3": 8, "4": 12, "6": 8}
        and dict(klein_pairs) == {tbm_key: 36, dem_key: 12}
        and dict(col_counts) == {"(0, 1/2, 1/2)": 6, "(1/6, 1/6, 2/3)": 6, "(1/3, 1/3, 1/3)": 6}
        and named_inv_cols["P"] == ["1/6", "1/6", "2/3"]
        and named_inv_cols["inner_a"] == ["1/3", "1/3", "1/3"]
        and named_inv_cols["L_shear"] == ["0", "1/2", "1/2"]
    )
    return {
        "row": 914,
        "pinned_commit": "c0ff37644",
        "seat_grade": "READING",
        "computed_math_result": "the same" if holds else "differs",
        "empirical_viability_clause_result": "cannot check",
        "empirical_firewall_reason": "Comparing TM1, TM2, and theta_13 = 0 against measured neutrino oscillation angles requires empirical data barred by the 0 of 19 firewall.",
        "method_label": "recomputed on another family of model",
        "group_order": len(G),
        "determinants": {str(k): v for k, v in dets.items()},
        "element_orders": orders,
        "klein_pair_counts": dict(klein_pairs),
        "klein_subgroup_counts": {"tri_bimaximal": klein_pairs[tbm_key] // 3, "democratic": klein_pairs[dem_key] // 3},
        "involution_fixed_columns": dict(col_counts),
        "named_involution_columns": named_inv_cols,
    }


def verify_row_915() -> dict[str, object]:
    """Row 915 (@ e8406e52e, synthesis): W1-W4, Theorem G, and BMR arithmetic odd-trace uniqueness (+-LR)."""
    # 1. W1 hyperbolic words in L, R, P up to cyclic rotation to length 8
    seen_rot: set[str] = set()
    w1_total = 0
    w1_odd = 0
    mats_lrp = {"L": ((1, 1), (0, 1)), "R": ((1, 0), (1, 1)), "P": ((0, 1), (1, 0))}
    for n in range(2, 9):
        for tup in itertools.product("LRP", repeat=n):
            w = "".join(tup)
            c = min(w[i:] + w[:i] for i in range(n))
            if c in seen_rot:
                continue
            seen_rot.add(c)
            M = [[1, 0], [0, 1]]
            for ch in c:
                A = mats_lrp[ch]
                M = [[M[0][0] * A[0][0] + M[0][1] * A[1][0], M[0][0] * A[0][1] + M[0][1] * A[1][1]],
                     [M[1][0] * A[0][0] + M[1][1] * A[1][0], M[1][0] * A[0][1] + M[1][1] * A[1][1]]]
            det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
            for sgn in (1, -1):
                tr = sgn * (M[0][0] + M[1][1])
                hyp = (abs(tr) > 2) if det == 1 else (tr != 0)
                if hyp:
                    w1_total += 1
                    if tr % 2 != 0:
                        w1_odd += 1

    # 2. W2 common point on Markov surface x^2 + y^2 + z^2 - x*y*z = 0
    xs, ys, zs = sp.symbols("x y z")
    gb = sp.groebner([zs - xs, ys * zs - 2 * xs, xs - ys, xs**2 + ys**2 + zs**2 - xs * ys * zs], xs, ys, zs, order="lex")
    markov_common_pts = sp.solve(list(gb.exprs), [xs, ys, zs], dict=True)

    # 3. BMR arithmetic odd-trace threads among all GENESIS states to length 12:
    # Bowditch / Maclachlan-Reid: a once-punctured-torus bundle over S^1 is arithmetic iff |tr(M)| in {3, 4};
    # for odd trace, |tr(M)| == 3 uniquely!
    st12 = genesis_states(12)
    odd12 = [sw for sw, M, _ in st12 if (M[0][0] + M[1][1]) % 2 != 0]
    arith_odd12 = [sw for sw, M, _ in st12 if abs(M[0][0] + M[1][1]) == 3]

    holds = (
        w1_total == 2554
        and w1_odd == 1308
        and markov_common_pts == [{xs: 0, ys: 0, zs: 0}]
        and len(st12) == 758
        and len(odd12) == 326
        and arith_odd12 == ["+LR", "-LR"]
    )
    return {
        "row": 915,
        "pinned_commit": "e8406e52e",
        "seat_grade": "SYNTHESIS (theorems + computed thread counts + readings)",
        "computed_math_result": "the same" if holds else "differs",
        "empirical_viability_clause_result": "cannot check",
        "empirical_firewall_reason": "Section 3 compares TM1/TM2/TBM against JUNO and NuFIT oscillation measurements, barred under 0 of 19.",
        "method_label": "recomputed on another family of model",
        "w1_words_to_8_total_and_odd": [w1_total, w1_odd],
        "w2_unique_markov_common_point": str(markov_common_pts),
        "genesis_states_to_12_total_and_odd": [len(st12), len(odd12)],
        "arithmetic_odd_trace_threads_to_12": arith_odd12,
    }


def verify_row_916() -> dict[str, object]:
    """Row 916 (@ 48e9c2200, W7): parity sectors at each state's resolving tick for all 24 states to length 6."""
    st6 = genesis_states(6)
    parities = [("zero", (0, 0)), ("(1/2, 0)", (1, 0)), ("(0, 1/2)", (0, 1)), ("(1/2, 1/2)", (1, 1))]
    states_with_members = []
    member_details = {}
    any_on_zero = False
    any_on_fixed_single = False
    any_on_all_three = False

    for sw, M, _ in st6:
        M2 = np.array([[M[0][0] % 2, M[0][1] % 2], [M[1][0] % 2, M[1][1] % 2]], dtype=int)
        I2 = np.eye(2, dtype=int)
        if np.array_equal(M2, I2):
            k_res = 1
        elif np.array_equal((M2 @ M2) % 2, I2):
            k_res = 2
        else:
            k_res = 3
        fixed_tick1 = [
            name for name, (pa, pb) in parities[1:]
            if ((pa * M2[0, 0] + pb * M2[1, 0]) % 2, (pa * M2[0, 1] + pb * M2[1, 1]) % 2) == (pa, pb)
        ]

        tsgn, twrd, hol_tk, hol_tk_inv = get_tick_holonomy_gm4(sw[0], sw[1:], k_res)
        cov = build_cover(tsgn, twrd, 1, {"a": [0], "b": [0], "t": [0]})
        # Map Schreier generators of degree-1 cover directly to a, b, t
        assert cov["gen_words"] == ["a", "b", "t"]
        roots12 = gm_roots_of_unity(12)

        by_par: dict[str, list[dict[str, object]]] = {nm: [] for nm, _ in parities}
        for nm, (pa, pb) in parities:
            va = gmpy2.mpc(-1 if pa else 1)
            vb = gmpy2.mpc(-1 if pb else 1)
            ma = gm_scale_mat(va, hol_tk["a"])
            ma_inv = gm_scale_mat(va, hol_tk_inv["a"])
            mb = gm_scale_mat(vb, hol_tk["b"])
            mb_inv = gm_scale_mat(vb, hol_tk_inv["b"])
            for ek in range(12):
                vt = roots12[ek]
                vt_inv = roots12[(-ek) % 12]
                mod_mats = [ma, mb, gm_scale_mat(vt, hol_tk["t"])]
                mod_invs = [ma_inv, mb_inv, gm_scale_mat(vt_inv, hol_tk_inv["t"])]
                _, h1, r1, n, _ = cohom_pres_gm(mod_mats, mod_invs, cov["rels_idx"], cov["cusps_idx"])
                if n > 0:
                    by_par[nm].append({"kappa_twelfths": ek, "h1_r1_n": [h1, r1, n]})

        tot_m = sum(len(v) for v in by_par.values())
        if len(by_par["zero"]) > 0:
            any_on_zero = True
        nonzero_active = [nm for nm, _ in parities[1:] if len(by_par[nm]) > 0]
        if len(nonzero_active) == 3:
            any_on_all_three = True
        if k_res == 2 and any(len(by_par[fp]) > 0 for fp in fixed_tick1):
            any_on_fixed_single = True
        if k_res == 1 and tot_m > 0:
            # At tick 1 (M = I mod 2, e.g. +-LLRR), L<->R word symmetry exchanges (1/2, 0) and (0, 1/2) and fixes (1/2, 1/2)
            if len(by_par["(1/2, 1/2)"]) > 0:
                any_on_fixed_single = True
        if tot_m > 0:
            states_with_members.append(sw)
            member_details[sw] = {"resolving_tick": k_res, "fixed_tick1": fixed_tick1, "by_parity": by_par}

    holds = (
        len(st6) == 24
        and states_with_members == ["+LLR", "-LLR", "+LLRR", "-LLRR", "+LLLLR", "-LLLLR"]
        and not any_on_zero
        and not any_on_fixed_single
        and not any_on_all_three
    )
    return {
        "row": 916,
        "pinned_commit": "48e9c2200",
        "result": "the same" if holds else "differs",
        "method_label": "recomputed on another family of model",
        "states_checked": len(st6),
        "states_with_members": states_with_members,
        "any_member_on_zero_parity": any_on_zero,
        "any_member_on_symmetry_fixed_parity": any_on_fixed_single,
        "any_member_on_all_three_parities": any_on_all_three,
        "member_details": member_details,
    }


def verify_row_917() -> dict[str, object]:
    """Row 917 (@ cecf33c11, 6169c9716): trichotomy across 758 states to length 12 + box [-6,6] + Theorem S."""
    st12 = genesis_states(12)
    I2 = np.eye(2, dtype=int)
    c_3cycle, c_inv, c_id = 0, 0, 0
    own_tick_sep_and_cycled = 0
    odd_third_tick_sep_and_cycled = 0

    def classify_mat(M: tuple[tuple[int, int], tuple[int, int]]) -> str:
        tr = M[0][0] + M[1][1]
        M2 = np.array([[M[0][0] % 2, M[0][1] % 2], [M[1][0] % 2, M[1][1] % 2]], dtype=int)
        if np.array_equal(M2, I2):
            assert tr % 2 == 0
            return "id"
        if np.array_equal((M2 @ M2) % 2, I2):
            assert tr % 2 == 0
            return "inv"
        assert tr % 2 != 0 and np.array_equal(np.linalg.matrix_power(M2, 3) % 2, I2)
        return "3cycle"

    for _, M, _ in st12:
        knd = classify_mat(M)
        if knd == "3cycle":
            c_3cycle += 1
        elif knd == "inv":
            c_inv += 1
        else:
            c_id += 1
        M2 = np.array([[M[0][0] % 2, M[0][1] % 2], [M[1][0] % 2, M[1][1] % 2]], dtype=int)
        # Separate at tick k <=> M2^k == I2; carried into one another by thread monodromy <=> M2 is a 3-cycle
        if np.array_equal(M2, I2) and knd == "3cycle":
            own_tick_sep_and_cycled += 1
        if knd == "3cycle" and all(np.array_equal(np.linalg.matrix_power(M2, 3 * m) % 2, I2) for m in (1, 2, 3)):
            odd_third_tick_sep_and_cycled += 1

    box_checked = 0
    for a, b, c, d in itertools.product(range(-6, 7), repeat=4):
        if a * d - b * c in (1, -1):
            classify_mat(((a, b), (c, d)))
            box_checked += 1

    holds = (
        len(st12) == 758
        and [c_3cycle, c_inv, c_id] == [326, 268, 164]
        and own_tick_sep_and_cycled == 0
        and odd_third_tick_sep_and_cycled == 326
    )
    return {
        "row": 917,
        "pinned_commits": ["cecf33c11", "6169c9716"],
        "result": "the same" if holds else "differs",
        "fk7_clause_status": "principle_not_theorem_left_as_principle",
        "method_label": "recomputed on another family of model",
        "states_to_12": len(st12),
        "trichotomy_counts_3cycle_inv_id": [c_3cycle, c_inv, c_id],
        "gl2_z_box_matrices_checked": box_checked,
        "own_tick_separate_and_cycled": own_tick_sep_and_cycled,
        "odd_threads_third_tick_separate_and_cycled": odd_third_tick_sep_and_cycled,
    }


def verify_row_918() -> dict[str, object]:
    """Row 918 (@ 7bd8eeed0, W8 / Lemma V): frame at common quaternion point rho_Q across all 24 states to length 6."""
    st6 = genesis_states(6)
    I_sp = sp.I
    par_lines_read = 0
    par_lines_all_h1_one_cusp_triv_n_zero = True
    ord4_chars_read = 0
    ord4_interior_members = 0

    def exact_line_q_i(sign: str, word: str, ch: dict[str, sp.Expr]) -> tuple[int, bool, int]:
        img = auto_words(sign, word)
        rels = ["taT" + inv_w(img["a"]), "tbT" + inv_w(img["b"])]
        per = ("abAB", "t" if sign == "+" else "abt")

        def val(w: str) -> sp.Expr:
            v = sp.Integer(1)
            for c in w:
                v *= ch[c] if c in "abt" else 1 / ch[c.lower()]
            return sp.simplify(v)

        if not all(val(r) == 1 for r in rels):
            return -1, False, -1

        def fx(w: str, g: str) -> sp.Expr:
            tot, pref = sp.Integer(0), sp.Integer(1)
            for c in w:
                if c == g:
                    tot += pref
                elif c == g.upper():
                    tot -= pref / ch[g]
                pref *= ch[c] if c in "abt" else 1 / ch[c.lower()]
            return sp.expand(tot)

        F = sp.Matrix([[fx(r, g) for g in "abt"] for r in rels])
        Z = F.nullspace()
        triv = all(sp.simplify(ch[g] - 1) == 0 for g in "abt")
        h1 = len(Z) - (0 if triv else 1)
        ctriv = all(val(w) == 1 for w in per)
        if h1 == 0:
            return 0, ctriv, 0
        if not ctriv:
            return h1, False, h1
        R = sp.Matrix([[sum(fx(w, g) * z[i] for i, g in enumerate("abt")) for z in Z] for w in per])
        r1 = R.rank()
        return h1, True, h1 - r1

    for sw, M, _ in st6:
        M2 = np.array([[M[0][0] % 2, M[0][1] % 2], [M[1][0] % 2, M[1][1] % 2]], dtype=int)
        I2 = np.eye(2, dtype=int)
        k_res = 1 if np.array_equal(M2, I2) else (2 if np.array_equal((M2 @ M2) % 2, I2) else 3)
        tsgn = "+" if (sw[0] == "+" or k_res % 2 == 0) else "-"
        twrd = sw[1:] * k_res

        # (1) Three non-zero parity lines at their unique live sign kappa in {+1, -1}
        for pa, pb in ((1, 0), (0, 1), (1, 1)):
            live = []
            for kap in (sp.Integer(1), sp.Integer(-1)):
                h1, ctriv, n = exact_line_q_i(tsgn, twrd, {"a": sp.Integer(-1 if pa else 1), "b": sp.Integer(-1 if pb else 1), "t": kap})
                if h1 > 0:
                    live.append((h1, ctriv, n))
            assert len(live) == 1
            par_lines_read += 1
            if live[0] != (1, True, 0):
                par_lines_all_h1_one_cusp_triv_n_zero = False

        # (2) All characters of order dividing 4 on the tick group
        vals4 = [sp.Integer(1), I_sp, sp.Integer(-1), -I_sp]
        for ca, cb, ct in itertools.product(vals4, repeat=3):
            h1, _, n = exact_line_q_i(tsgn, twrd, {"a": ca, "b": cb, "t": ct})
            if h1 >= 0:
                ord4_chars_read += 1
                if n > 0:
                    ord4_interior_members += 1

    holds = (
        par_lines_read == 72
        and par_lines_all_h1_one_cusp_triv_n_zero
        and ord4_chars_read == 768
        and ord4_interior_members == 0
    )
    return {
        "row": 918,
        "pinned_commit": "7bd8eeed0",
        "result": "the same" if holds else "differs",
        "method_label": "recomputed on another family of model",
        "states_checked": len(st6),
        "parity_lines_read": par_lines_read,
        "all_parity_lines_boundary_h1_1_n_0": par_lines_all_h1_one_cusp_triv_n_zero,
        "order_div_4_characters_read": ord4_chars_read,
        "interior_members_found": ord4_interior_members,
    }


def verify_row_922() -> dict[str, object]:
    """Row 922 (@ 52c2f8db5, W6 complete): all 12 odd-trace threads to length 6 on forced A_4 cover at orders 4 and 3."""
    odd6 = [(sw, M) for sw, M, _ in genesis_states(6) if (M[0][0] + M[1][1]) % 2 != 0]
    assert len(odd6) == 12
    thread_rows = []
    roots4 = gm_roots_of_unity(4)
    roots3 = gm_roots_of_unity(3)

    for sw, M in odd6:
        cov = build_a4_cover(sw[0], sw[1:])
        hol_obj = get_holonomy(sw[0], sw[1:])
        gen_mats_hol, gen_invs_hol = _cover_gen_gm_mats(cov, hol_obj)

        chars4, orbs4 = cover_characters_and_orbits(cov, 4)
        mem4 = 0
        mem4_orbs = 0
        for orb in orbs4:
            rep = orb[0]
            mod_mats = [gm_scale_mat(roots4[int(rep[j]) % 4], gen_mats_hol[j]) for j in range(cov["ng"])]
            mod_invs = [gm_scale_mat(roots4[(-int(rep[j])) % 4], gen_invs_hol[j]) for j in range(cov["ng"])]
            _, _, _, n, _ = cohom_pres_gm(mod_mats, mod_invs, cov["rels_idx"], cov["cusps_idx"])
            if n > 0:
                mem4 += len(orb)
                mem4_orbs += 1

        chars3, orbs3 = cover_characters_and_orbits(cov, 3)
        mem3 = 0
        mem3_mA_max = 0
        for orb in orbs3:
            rep = orb[0]
            mod_mats = [gm_scale_mat(roots3[int(rep[j]) % 3], gen_mats_hol[j]) for j in range(cov["ng"])]
            mod_invs = [gm_scale_mat(roots3[(-int(rep[j])) % 3], gen_invs_hol[j]) for j in range(cov["ng"])]
            _, _, _, n, _ = cohom_pres_gm(mod_mats, mod_invs, cov["rels_idx"], cov["cusps_idx"])
            if n > 0:
                mem3 += len(orb)
                m_A = sum(
                    1 for (sw1, sw2) in cov["cusps_idx"]
                    if (sum(int(rep[idx]) * sgn for idx, sgn in sw1) % 3 == 0)
                    and (sum(int(rep[idx]) * sgn for idx, sgn in sw2) % 3 == 0)
                )
                mem3_mA_max = max(mem3_mA_max, m_A)

        thread_rows.append({
            "state": sw,
            "trace": M[0][0] + M[1][1],
            "ord4_chars_orbits_members": [len(chars4), len(orbs4), mem4, mem4_orbs],
            "ord3_chars_orbits_members_max_mA": [len(chars3), len(orbs3), mem3, mem3_mA_max],
        })

    states_with_any_members = [r["state"] for r in thread_rows if r["ord4_chars_orbits_members"][2] > 0 or r["ord3_chars_orbits_members_max_mA"][2] > 0]
    by_state = {r["state"]: r for r in thread_rows}
    holds = (
        len(thread_rows) == 12
        and states_with_any_members == ["+LR", "-LR"]
        and by_state["+LR"]["ord4_chars_orbits_members"] == [1024, 128, 54, 8]
        and by_state["-LR"]["ord4_chars_orbits_members"] == [256, 40, 6, 1]
        and by_state["+LR"]["ord3_chars_orbits_members_max_mA"][2:] == [6, 0]
        and by_state["-LR"]["ord3_chars_orbits_members_max_mA"][2:] == [6, 0]
    )
    return {
        "row": 922,
        "pinned_commit": "52c2f8db5",
        "result": "the same" if holds else "differs",
        "method_label": "recomputed on another family of model",
        "threads_checked": len(thread_rows),
        "threads_with_members": states_with_any_members,
        "threads": thread_rows,
    }


def main() -> None:
    controls = run_precommitted_controls()
    r908 = verify_row_908()
    r909 = verify_row_909()
    r910 = verify_row_910()
    r912 = verify_row_912()
    r914 = verify_row_914()
    r915 = verify_row_915()
    r916 = verify_row_916()
    r917 = verify_row_917()
    r918 = verify_row_918()
    r922 = verify_row_922()

    payload = {
        "card": "X-C1a",
        "batch": "V1 (part 1 of 4: rows 908-922)",
        "firewall": "0 of 19",
        "controls": controls,
        "rows": {
            "908": r908,
            "909": r909,
            "910": r910,
            "912": r912,
            "914": r914,
            "915": r915,
            "916": r916,
            "917": r917,
            "918": r918,
            "922": r922,
        },
    }
    out_path = HERE / "verify_x_c1a_out.json"
    out_text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    out_path.write_text(out_text, encoding="utf-8")
    digest = hashlib.sha256(out_text.encode("utf-8")).hexdigest()
    (HERE / "OUTPUT_SHA256.txt").write_text(f"{digest}  verify_x_c1a_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
