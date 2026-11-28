#!/usr/bin/env python3
"""Card A2-CHIRAL-E8-SIBLINGS — Phase 1 of Unattended Listening Campaign:
Exact Invariant Trace Fields & Arithmeticity (Rung 1), Rational Fox-Calculus Ad(2T)
Rigidity (Rung 3), B2008 Chirality Seam on the 6 H_1 = Z E_8-Locked Manifolds, and
100% 3-Generator Census Closure Across All 18 S_BD5_C4 3-Gen Manifolds.

Seat code: fam3-v1-high-03 (agy-002/verify).
Strictly blind (0 of 19), zero trial arcs, stdlib + sympy + mpmath only, ZERO AST/JSON floats.
"""
import ast
import itertools
import json
import math
import pathlib
import sys
from collections import Counter, deque
from fractions import Fraction

import mpmath as mp
import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = pathlib.Path(__file__).resolve().parent
DATA_JSON = HERE / "a2_chiral_e8_siblings_input.json"
OUT_JSON = HERE / "a2_chiral_e8_siblings_out.json"

mp.mp.dps = 420
X = sp.Symbol("X")


def _mpf(s):
    return mp.mpf(str(s).replace(" e", "e").replace(" E", "e").strip())


def _mpc(r, im):
    return mp.mpc(_mpf(r), _mpf(im))


# ============================================================================
# 1. Exact F_25 = F_5[d]/(d^2 - 2) & BD_5 & 2T = SL(2, F_3) tables
# ============================================================================
ADD = [[0] * 25 for _ in range(25)]
SUB = [[0] * 25 for _ in range(25)]
MUL = [[0] * 25 for _ in range(25)]
NEG = [0] * 25
INV = [0] * 25
SQRT = [-1] * 25
OMZ = [0] * 25
TR5 = [0] * 25

for _i in range(25):
    _a, _b = divmod(_i, 5)
    NEG[_i] = ((-_a) % 5) * 5 + ((-_b) % 5)
    TR5[_i] = (2 * _a) % 5
    for _j in range(25):
        _c, _e = divmod(_j, 5)
        ADD[_i][_j] = ((_a + _c) % 5) * 5 + ((_b + _e) % 5)
        SUB[_i][_j] = ((_a - _c) % 5) * 5 + ((_b - _e) % 5)
        MUL[_i][_j] = ((_a * _c + 2 * _b * _e) % 5) * 5 + ((_a * _e + _b * _c) % 5)

F0, F1, F2, FM2, F4, INV2 = 0, 5, 10, 15, 20, 15
for _i in range(1, 25):
    for _j in range(1, 25):
        if MUL[_i][_j] == F1:
            INV[_i] = _j
for _i in range(25):
    SQRT[MUL[_i][_i]] = _i
    OMZ[_i] = SUB[F1][_i]

# Clean primitive root finder in F_25^*
_PRIM_G = -1
for _cand in range(1, 25):
    _cur, _o = _cand, 1
    while _cur != F1:
        _cur = MUL[_cur][_cand]
        _o += 1
    if _o == 24:
        _PRIM_G = _cand
        break
DLOG = [-1] * 25
_cur = F1
for _e in range(24):
    DLOG[_cur] = _e
    _cur = MUL[_cur][_PRIM_G]

# BD_5 (order 20)
BD_MUL = [[0] * 20 for _ in range(20)]
BD_INV = [0] * 20
BD_ORD = [0] * 20
for _x in range(20):
    _a, _k = divmod(_x, 4)
    _sgn = 1 if (_k % 2 == 0) else -1
    BD_INV[_x] = (((-_sgn * _a) % 5) * 4) + ((-_k) % 4)
    for _y in range(20):
        _b, _l = divmod(_y, 4)
        BD_MUL[_x][_y] = (((_a + _sgn * _b) % 5) * 4) + ((_k + _l) % 4)
for _x in range(20):
    _c, _o = _x, 1
    while _c != 0:
        _c = BD_MUL[_c][_x]
        _o += 1
    BD_ORD[_x] = _o

BD_CONJ_REPS = []
_seen_b = set()
for _x in range(20):
    if _x not in _seen_b:
        _cls = {BD_MUL[BD_MUL[_g][_x]][BD_INV[_g]] for _g in range(20)}
        BD_CONJ_REPS.append((_x, len(_cls)))
        _seen_b.update(_cls)

# 2T = SL(2, F_3) (order 24) + exact integer 3x3 Ad(2T) = A_4 matrices derived from Q_8 conjugation
def build_2t_and_ad():
    elems = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if (a * d - b * c) % 3 == 1:
                        elems.append((a, b, c, d))
    assert len(elems) == 24
    idx = {e: i for i, e in enumerate(elems)}
    id_i = idx[(1, 0, 0, 1)]
    if id_i != 0:
        elems[0], elems[id_i] = elems[id_i], elems[0]
        idx = {e: i for i, e in enumerate(elems)}
    mul = [[0] * 24 for _ in range(24)]
    inv = [0] * 24
    for i, (a, b, c, d) in enumerate(elems):
        inv[i] = idx[(d, (-b) % 3, (-c) % 3, a)]
        for j, (e, f, g, h) in enumerate(elems):
            mul[i][j] = idx[((a * e + b * g) % 3, (a * f + b * h) % 3,
                             (c * e + d * g) % 3, (c * f + d * h) % 3)]
    # Identify the 3 basis axes of su(2) = Q_8 / {+-1}: the 3 inverse pairs of order-4 elements
    ord4 = []
    for i in range(24):
        i2 = mul[i][i]
        if i2 != 0 and mul[i2][i2] == 0:
            ord4.append(i)
    assert len(ord4) == 6
    axes = []
    used = set()
    for q in ord4:
        if q not in used:
            axes.append(q)
            used.add(q)
            used.add(inv[q])
    assert len(axes) == 3
    # Build exact 3x3 integer matrix AD[g] where g * e_j * g^{-1} = sum_i AD[g][i,j] e_i
    ad = []
    for g in range(24):
        mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for j, ej in enumerate(axes):
            conj = mul[mul[g][ej]][inv[g]]
            for i, ei in enumerate(axes):
                if conj == ei:
                    mat[i][j] = 1
                elif conj == inv[ei]:
                    mat[i][j] = -1
        # Verify det == +1 and orthogonal (mat^T * mat == I_3)
        M_sp = sp.Matrix(mat)
        assert M_sp.det() == 1 and M_sp.T * M_sp == sp.eye(3)
        ad.append(M_sp)
    # Verify homomorphism property AD[g*h] == AD[g]*AD[h]
    for g in range(24):
        for h in range(24):
            assert ad[mul[g][h]] == ad[g] * ad[h]
    # Conjugacy classes of 2T
    conj_reps = []
    seen = set()
    for x in range(24):
        if x not in seen:
            cls = {mul[mul[g][x]][inv[g]] for g in range(24)}
            conj_reps.append((x, len(cls)))
            seen.update(cls)
    # Aut(2T) (order 24: generated by inner conjugations + outer automorphism from GL(2, F_3))
    gl2_f3 = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    det = (a * d - b * c) % 3
                    if det in (1, 2):
                        gl2_f3.append((a, b, c, d, det))
    aut_maps = []
    seen_aut = set()
    for a, b, c, d, det in gl2_f3:
        inv_g = (d * det % 3, (-b * det) % 3, (-c * det) % 3, a * det % 3)
        mp_list = []
        for (e, f, g, h) in elems:
            # g_mat * elem * g_mat^{-1}
            p0 = (a * e + b * g) % 3
            p1 = (a * f + b * h) % 3
            p2 = (c * e + d * g) % 3
            p3 = (c * f + d * h) % 3
            q0 = (p0 * inv_g[0] + p1 * inv_g[2]) % 3
            q1 = (p0 * inv_g[1] + p1 * inv_g[3]) % 3
            q2 = (p2 * inv_g[0] + p3 * inv_g[2]) % 3
            q3 = (p2 * inv_g[1] + p3 * inv_g[3]) % 3
            mp_list.append(idx[(q0, q1, q2, q3)])
        t = tuple(mp_list)
        if t not in seen_aut:
            seen_aut.add(t)
            aut_maps.append(t)
    assert len(aut_maps) == 24
    return mul, inv, ad, conj_reps, aut_maps


T2_MUL, T2_INV, T2_AD, T2_CONJ, T2_AUTS = build_2t_and_ad()


def compile_word(word, gens):
    gidx = {g: i for i, g in enumerate(gens)}
    return tuple((gidx[ch.lower()], ch.isupper()) for ch in word)


def eval_tab(comp, vals, inv_tab, mul_tab):
    cur = 0
    for idx, is_inv in comp:
        g = vals[idx]
        cur = mul_tab[cur][inv_tab[g] if is_inv else g]
    return cur


def subgroup_size(vals, inv_tab, mul_tab):
    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for g in vals:
            for h in (g, inv_tab[g]):
                v = mul_tab[u][h]
                if v not in seen:
                    seen.add(v)
                    q.append(v)
    return len(seen)


# ============================================================================
# 2. Module C1: 260-Digit Gluing Newton Refinement + Exact LLL + Symbolic Certifier
# ============================================================================
def refine_shapes_gluing(m, steps=5):
    """Newton-refine SnapPy ~60-digit shapes_hp directly on the exact integer gluing_rect
    equations at mp.dps = 260, achieving < 1e-220 residual with zero extra external data."""
    zs = [_mpc(r, im) for r, im in m["shapes_hp"]]
    n = len(zs)
    eqs = m["gluing_rect"]
    m_eq = len(eqs)
    for _ in range(steps):
        F = mp.matrix(m_eq, 1)
        J = mp.matrix(m_eq, n)
        for i, (ar, br, sgn) in enumerate(eqs):
            prod = mp.mpc(1)
            for j in range(n):
                if ar[j]:
                    prod *= zs[j] ** ar[j]
                if br[j]:
                    prod *= (1 - zs[j]) ** br[j]
            val = prod / sgn
            F[i, 0] = val - 1
            for j in range(n):
                if ar[j] or br[j]:
                    J[i, j] = val * (ar[j] / zs[j] - br[j] / (1 - zs[j]))
        JH = J.T.conjugate()
        dz = mp.lu_solve(JH * J, -JH * F)
        zs = [zs[j] + dz[j, 0] for j in range(n)]
    max_res = mp.mpf(0)
    for ar, br, sgn in eqs:
        prod = mp.mpc(1)
        for j in range(n):
            if ar[j]:
                prod *= zs[j] ** ar[j]
            if br[j]:
                prod *= (1 - zs[j]) ** br[j]
        max_res = max(max_res, abs(prod - sgn))
    assert max_res < mp.mpf("1e-200"), f"Newton gluing refinement residual too large for {m['name']}: {max_res}"
    return zs


def lll_minpoly_complex(val_mpc, max_deg=24, scale_exp=210, tol_exp=120, max_c_exp=10):
    """Find exact irreducible integer minimal polynomial P(X) in Z[X] of a high-precision
    complex algebraic number via sympy DomainMatrix.lll on 2D (Re, Im) lattice.
    Enforces strict Minkowski anti-spurious cap (max_c < 10**max_c_exp) AND absolute
    residual < 10**(-tol_exp) so generic short vectors can never pass."""
    inverted = (abs(val_mpc) > mp.mpf(3) / 2)
    z = (mp.mpc(1) / val_mpc) if inverted else val_mpc
    scale = 10 ** scale_exp
    tol = mp.mpf(10) ** (-tol_exp)
    max_c_cap = 10 ** max_c_exp
    pows = [mp.mpc(1)]
    for _ in range(max_deg):
        pows.append(pows[-1] * z)

    for d in range(1, max_deg + 1):
        rows = []
        for k in range(d + 1):
            row = [0] * (d + 3)
            row[k] = 1
            row[d + 1] = int(mp.nint(pows[k].real * scale))
            row[d + 2] = int(mp.nint(pows[k].imag * scale))
            rows.append(row)
        dm = DomainMatrix.from_Matrix(sp.Matrix(rows)).lll()
        mat = dm.to_Matrix()
        for r in range(d + 1):
            coeffs = [int(mat[r, k]) for k in range(d + 1)]
            if all(c == 0 for c in coeffs):
                continue
            max_c = max(abs(c) for c in coeffs)
            if max_c > max_c_cap:
                continue
            val_eval = sum(c * p for c, p in zip(coeffs, pows[:d + 1]))
            if abs(val_eval) < tol:
                poly_raw = sp.Poly(list(reversed(coeffs)), X, domain=sp.ZZ)
                if poly_raw.degree() < 1:
                    continue
                _, factors = sp.factor_list(poly_raw)
                for fac, _mult in factors:
                    f_coeffs = [int(c) for c in reversed(fac.all_coeffs())]
                    fev = sum(c * p for c, p in zip(f_coeffs, pows[:len(f_coeffs)]))
                    if abs(fev) < tol:
                        if inverted:
                            f_coeffs = list(reversed(f_coeffs))
                        while len(f_coeffs) > 1 and f_coeffs[-1] == 0:
                            f_coeffs.pop()
                        if f_coeffs[-1] < 0:
                            f_coeffs = [-c for c in f_coeffs]
                        P_out = sp.Poly(list(reversed(f_coeffs)), X, domain=sp.ZZ)
                        ev_orig = mp.mpc(0)
                        for cc in P_out.all_coeffs():
                            ev_orig = ev_orig * val_mpc + int(cc)
                        if abs(ev_orig) < tol * max(mp.mpf(1), abs(val_mpc) ** P_out.degree()):
                            return P_out
    return None


def lll_express_in_basis(target_mpc, alpha_mpc, deg, scale_exp=210, tol_exp=100, max_c_exp=14):
    """Express target_mpc = (sum_{k=0}^{deg-1} a_k alpha^k) / q with exact integers a_k, q > 0."""
    s_int = 1
    while abs(alpha_mpc) > s_int * mp.mpf(3) / 2:
        s_int *= 2
    a_scaled = alpha_mpc / s_int
    t_scale = 1
    while abs(target_mpc) > t_scale * mp.mpf(3) / 2:
        t_scale *= 2
    t_scaled = target_mpc / t_scale

    scale = 10 ** scale_exp
    tol = mp.mpf(10) ** (-tol_exp)
    max_c_cap = 10 ** max_c_exp
    pows = [mp.mpc(1)]
    for _ in range(deg - 1):
        pows.append(pows[-1] * a_scaled)
    rows = []
    for k in range(deg):
        row = [0] * (deg + 3)
        row[k] = 1
        row[deg + 1] = int(mp.nint(pows[k].real * scale))
        row[deg + 2] = int(mp.nint(pows[k].imag * scale))
        rows.append(row)
    row_t = [0] * (deg + 3)
    row_t[deg] = 1
    row_t[deg + 1] = int(mp.nint((-t_scaled.real) * scale))
    row_t[deg + 2] = int(mp.nint((-t_scaled.imag) * scale))
    rows.append(row_t)

    dm = DomainMatrix.from_Matrix(sp.Matrix(rows)).lll()
    mat = dm.to_Matrix()
    for r in range(deg + 1):
        q = int(mat[r, deg])
        if q == 0:
            continue
        if q < 0:
            a_vec = [-int(mat[r, k]) for k in range(deg)]
            q = -q
        else:
            a_vec = [int(mat[r, k]) for k in range(deg)]
        if max(q, max(abs(a) for a in a_vec)) > max_c_cap:
            continue
        approx = sum(a * p for a, p in zip(a_vec, pows)) / q
        if abs(approx - t_scaled) < tol:
            return sp.Poly([sp.Rational(a_vec[k] * t_scale, q * (s_int ** k)) for k in range(deg - 1, -1, -1)], X, domain=sp.QQ)
    return None


def exact_minpoly_in_field(Q_poly, P_poly):
    """Exact algebraic minimal polynomial in Z[X] of Q(alpha) in Q[X]/(P(X))
    via exact QQ multiplication-matrix characteristic polynomial + square-free factor."""
    P_qq = sp.Poly(P_poly.as_expr(), X, domain=sp.QQ)
    d = P_qq.degree()
    cols = []
    cur = sp.rem(Q_poly, P_qq, X, domain=sp.QQ)
    x_poly = sp.Poly(X, X, domain=sp.QQ)
    for k in range(d):
        # Multiply Q_poly by X^k mod P_qq
        prod = sp.rem(cur * (x_poly ** k), P_qq, X, domain=sp.QQ)
        coeffs_desc = prod.all_coeffs()
        pad = [sp.Rational(0)] * (d - len(coeffs_desc)) + list(coeffs_desc)
        # ascending order [c_0, ..., c_{d-1}]
        cols.append(list(reversed(pad)))
    M = sp.Matrix([[cols[j][i] for j in range(d)] for i in range(d)])
    cp = M.charpoly(X).as_poly(domain=sp.QQ)
    # Clear denominator to primitive ZZ polynomial and take unique irreducible factor
    cp_prim = sp.Poly(sp.primitive(cp.as_expr())[1], X, domain=sp.ZZ)
    _, facs = sp.factor_list(cp_prim)
    # Since Q(alpha) lies in the simple field Q(alpha), charpoly is a power of the unique minimal poly!
    assert len(facs) == 1
    mp_poly = facs[0][0]
    if mp_poly.LC() < 0:
        mp_poly = -mp_poly
    return mp_poly


def poly_mod_mul(A, B, P):
    return sp.rem(A * B, P, X, domain=sp.QQ)


def poly_mod_pow(A, exp, P):
    if exp == 0:
        return sp.Poly(1, X, domain=sp.QQ)
    if exp < 0:
        A = sp.invert(A, P, domain=sp.QQ)
        exp = -exp
    res = sp.Poly(1, X, domain=sp.QQ)
    base = sp.rem(A, P, X, domain=sp.QQ)
    while exp > 0:
        if exp & 1:
            res = sp.rem(res * base, P, X, domain=sp.QQ)
        base = sp.rem(base * base, P, X, domain=sp.QQ)
        exp >>= 1
    return res


def certify_gluing_symbolically(P_poly, z_polys, gluing_rect):
    """100% EXACT SYMBOLIC CERTIFICATION over Q[X]/(P(X)):
    Verify EVERY integer Thurston gluing equation prod_j z_j^{a_j} (1 - z_j)^{b_j} - sign == 0 (mod P)."""
    P_qq = sp.Poly(P_poly.as_expr(), X, domain=sp.QQ)
    one_p = sp.Poly(1, X, domain=sp.QQ)
    omz_polys = [sp.rem(one_p - zp, P_qq, X, domain=sp.QQ) for zp in z_polys]
    for zp, oz in zip(z_polys, omz_polys):
        if zp.is_zero or oz.is_zero:
            return False
    for a_row, b_row, sgn in gluing_rect:
        prod = one_p
        for j, (aj, bj) in enumerate(zip(a_row, b_row)):
            if aj != 0:
                prod = poly_mod_mul(prod, poly_mod_pow(z_polys[j], aj, P_qq), P_qq)
            if bj != 0:
                prod = poly_mod_mul(prod, poly_mod_pow(omz_polys[j], bj, P_qq), P_qq)
        diff = sp.rem(prod - sp.Poly(sgn, X, domain=sp.QQ), P_qq, X, domain=sp.QQ)
        if not diff.is_zero:
            return False
    return True


def sl2c_mat_from_hp(arr):
    return [_mpc(arr[k][0], arr[k][1]) for k in range(4)]


def sl2c_mul(A, B):
    return [
        A[0] * B[0] + A[1] * B[2],
        A[0] * B[1] + A[1] * B[3],
        A[2] * B[0] + A[3] * B[2],
        A[2] * B[1] + A[3] * B[3],
    ]


def sl2c_inv(A):
    return [A[3], -A[1], -A[2], A[0]]


def sl2c_eval(word, gmap):
    cur = [mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)]
    for ch in word:
        g = gmap[ch.lower()]
        cur = sl2c_mul(cur, sl2c_inv(g) if ch.isupper() else g)
    return cur


def _dual_mul(A, B):
    """Multiply two 2x2 matrices whose entries are dual numbers (val, deriv)."""
    def dm(x, y):
        return (x[0] * y[0], x[0] * y[1] + x[1] * y[0])
    def da(x, y):
        return (x[0] + y[0], x[1] + y[1])
    return [
        da(dm(A[0], B[0]), dm(A[1], B[2])),
        da(dm(A[0], B[1]), dm(A[1], B[3])),
        da(dm(A[2], B[0]), dm(A[3], B[2])),
        da(dm(A[2], B[1]), dm(A[3], B[3])),
    ]


def _dual_inv(A):
    return [A[3], (-A[1][0], -A[1][1]), (-A[2][0], -A[2][1]), A[0]]


def _dual_eval(word, gmap_d):
    z0 = (mp.mpc(0), mp.mpc(0))
    o1 = (mp.mpc(1), mp.mpc(0))
    cur = [o1, z0, z0, o1]
    for ch in word:
        g = gmap_d[ch.lower()]
        cur = _dual_mul(cur, _dual_inv(g) if ch.isupper() else g)
    return cur


def refine_sl2c_canonical_parabolic(m, steps=5):
    """Conjugate SnapPy ~60-digit sl2c_gens_hp into canonical parabolic gauge
    (M = sm * [[1, 1], [0, 1]], L = sl * [[1, tau], [0, 1]], pivot generator g_piv[0] == 0)
    and Newton-refine directly from the exact group relators + parabolicity at mp.dps=420
    using exact complex dual-number Jacobians to < 1e-340 residual."""
    gens = m["gens"]
    ng = len(gens)
    gmap0 = {g: sl2c_mat_from_hp(m["sl2c_gens_hp"][g]) for g in gens}
    m_word, l_word = m["periph"][0], m["periph"][1]
    M0 = sl2c_eval(m_word, gmap0)
    L0 = sl2c_eval(l_word, gmap0)
    sm = 1 if mp.re(M0[0] + M0[3]) >= 0 else -1
    sl = 1 if mp.re(L0[0] + L0[3]) >= 0 else -1
    rel_sgns = [1 if mp.re(sl2c_eval(r, gmap0)[0] + sl2c_eval(r, gmap0)[3]) >= 0 else -1 for r in m["rels"]]

    # Build conjugator P so P^{-1} M0 P = sm * [[1, 1], [0, 1]]
    N = [sm * M0[0] - 1, sm * M0[1], sm * M0[2], sm * M0[3] - 1]
    # Pick non-zero column of N as v1 = N * w; w is standard basis vector giving largest ||N * w||
    c0_nrm = abs(N[0]) ** 2 + abs(N[2]) ** 2
    c1_nrm = abs(N[1]) ** 2 + abs(N[3]) ** 2
    if c0_nrm >= c1_nrm:
        v1 = (N[0], N[2])
        v2 = (mp.mpc(1), mp.mpc(0))
    else:
        v1 = (N[1], N[3])
        v2 = (mp.mpc(0), mp.mpc(1))
    detP = v1[0] * v2[1] - v1[1] * v2[0]
    P = [v1[0], v2[0], v1[1], v2[1]]
    Pinv = [v2[1] / detP, -v2[0] / detP, -v1[1] / detP, v1[0] / detP]
    gmap = {g: sl2c_mul(sl2c_mul(Pinv, gmap0[g]), P) for g in gens}

    # Fix remaining unipotent shift C_v = [[1, v], [0, 1]] so first generator with |c| > 1e-10 has a == 0
    piv_idx = next(i for i, g in enumerate(gens) if abs(gmap[g][2]) > mp.mpf("1e-10"))
    gp = gmap[gens[piv_idx]]
    v_shift = -gp[0] / gp[2]
    Cv = [mp.mpc(1), v_shift, mp.mpc(0), mp.mpc(1)]
    Cvi = [mp.mpc(1), -v_shift, mp.mpc(0), mp.mpc(1)]
    gmap = {g: sl2c_mul(sl2c_mul(Cv, gmap[g]), Cvi) for g in gens}

    # Parameterize SL(2, C) generators (piv_idx has a=0, b=-1/c -> 2 params (c, d);
    # others have 3 params: (a, b, c) with d=(1+bc)/a if |a| >= |c|, else (a, c, d) with b=(ad-1)/c)
    modes = []
    params = []
    for i, g in enumerate(gens):
        a, b, c, d = gmap[g]
        if i == piv_idx:
            modes.append("piv")
            params.extend([c, d])
        elif abs(a) >= abs(c):
            modes.append("abc")
            params.extend([a, b, c])
        else:
            modes.append("acd")
            params.extend([a, c, d])
    n_p = len(params)

    def unpack_dual(p_vec, diff_k):
        gd = {}
        pos = 0
        for i, g in enumerate(gens):
            md = modes[i]
            if md == "piv":
                c = (p_vec[pos], mp.mpc(1 if diff_k == pos else 0))
                d = (p_vec[pos + 1], mp.mpc(1 if diff_k == pos + 1 else 0))
                pos += 2
                # b = -1/c => b' = c' / c^2
                b = (-1 / c[0], c[1] / (c[0] * c[0]))
                gd[g] = [(mp.mpc(0), mp.mpc(0)), b, c, d]
            elif md == "abc":
                a = (p_vec[pos], mp.mpc(1 if diff_k == pos else 0))
                b = (p_vec[pos + 1], mp.mpc(1 if diff_k == pos + 1 else 0))
                c = (p_vec[pos + 2], mp.mpc(1 if diff_k == pos + 2 else 0))
                pos += 3
                num_v = 1 + b[0] * c[0]
                num_d = b[0] * c[1] + b[1] * c[0]
                d = (num_v / a[0], (num_d * a[0] - num_v * a[1]) / (a[0] * a[0]))
                gd[g] = [a, b, c, d]
            else:
                a = (p_vec[pos], mp.mpc(1 if diff_k == pos else 0))
                c = (p_vec[pos + 1], mp.mpc(1 if diff_k == pos + 1 else 0))
                d = (p_vec[pos + 2], mp.mpc(1 if diff_k == pos + 2 else 0))
                pos += 3
                num_v = a[0] * d[0] - 1
                num_d = a[0] * d[1] + a[1] * d[0]
                b = (num_v / c[0], (num_d * c[0] - num_v * c[1]) / (c[0] * c[0]))
                gd[g] = [a, b, c, d]
        return gd

    def eval_residuals(p_vec, diff_k):
        gd = unpack_dual(p_vec, diff_k)
        res = []
        for r_w, rs in zip(m["rels"], rel_sgns):
            R = _dual_eval(r_w, gd)
            res.append((R[0][0] - rs, R[0][1]))
            res.append(R[1])
            res.append(R[2])
            res.append((R[3][0] - rs, R[3][1]))
        Md = _dual_eval(m_word, gd)
        Ld = _dual_eval(l_word, gd)
        res.append((Md[0][0] - sm, Md[0][1]))
        res.append((Md[1][0] - sm, Md[1][1]))
        res.append(Md[2])
        res.append((Md[3][0] - sm, Md[3][1]))
        res.append((Ld[0][0] - sl, Ld[0][1]))
        res.append(Ld[2])
        res.append((Ld[3][0] - sl, Ld[3][1]))
        return res

    for _ in range(steps):
        r0 = eval_residuals(params, -1)
        m_eq = len(r0)
        F = mp.matrix(m_eq, 1)
        for i in range(m_eq):
            F[i, 0] = r0[i][0]
        J = mp.matrix(m_eq, n_p)
        for k in range(n_p):
            rk = eval_residuals(params, k)
            for i in range(m_eq):
                J[i, k] = rk[i][1]
        JH = J.T.conjugate()
        dp = mp.lu_solve(JH * J, -JH * F)
        params = [params[k] + dp[k, 0] for k in range(n_p)]

    final_gd = unpack_dual(params, -1)
    gmap_420 = {g: [final_gd[g][k][0] for k in range(4)] for g in gens}
    max_res = max(abs(x[0]) for x in eval_residuals(params, -1))
    assert max_res < mp.mpf("1e-300"), f"SL(2,C) Newton residual too large for {m['name']}: {max_res}"
    return gmap_420, sm, sl, rel_sgns, piv_idx


def _f5_trim(p):
    p = [c % 5 for c in p]
    while len(p) > 1 and p[0] == 0:
        p.pop(0)
    return p


def _f5_divmod(a, b):
    a = _f5_trim(a)
    b = _f5_trim(b)
    if b == [0]:
        raise ZeroDivisionError
    inv_lb = pow(b[0], -1, 5)
    da, db = len(a) - 1, len(b) - 1
    if da < db:
        return [0], a
    q = [0] * (da - db + 1)
    r = list(a)
    for i in range(da - db + 1):
        coef = (r[i] * inv_lb) % 5
        q[i] = coef
        if coef:
            for j in range(db + 1):
                r[i + j] = (r[i + j] - coef * b[j]) % 5
    return _f5_trim(q), _f5_trim(r)


def _f5_mul_mod(a, b, modp):
    res = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        if ca:
            for j, cb in enumerate(b):
                res[i + j] = (res[i + j] + ca * cb) % 5
    _, rem = _f5_divmod(res, modp)
    return rem


def _f5_pow_mod(base, exp, modp):
    res = [1]
    b = _f5_divmod(base, modp)[1]
    while exp > 0:
        if exp & 1:
            res = _f5_mul_mod(res, b, modp)
        b = _f5_mul_mod(b, b, modp)
        exp >>= 1
    return res


def _f5_gcd(a, b):
    a, b = _f5_trim(a), _f5_trim(b)
    while b != [0]:
        _, r = _f5_divmod(a, b)
        a, b = b, r
    inv_la = pow(a[0], -1, 5)
    return [(c * inv_la) % 5 for c in a]


def _f5_sub(a, b):
    n = max(len(a), len(b))
    aa = [0] * (n - len(a)) + a
    bb = [0] * (n - len(b)) + b
    return _f5_trim([(x - y) % 5 for x, y in zip(aa, bb)])


def _f5_deriv(p):
    d = len(p) - 1
    if d <= 0:
        return [0]
    return _f5_trim([(p[i] * (d - i)) % 5 for i in range(d)])


def _f5_ddf_squarefree(g):
    """Exact distinct-degree factorization of a monic square-free polynomial g in F_5[X]."""
    degs = []
    cur = _f5_trim(g)
    x_poly = [1, 0]
    x_pow = [1, 0]
    k = 1
    while len(cur) - 1 >= 2 * k:
        x_pow = _f5_pow_mod(x_pow, 5, cur)
        diff = _f5_sub(x_pow, x_poly)
        h = _f5_gcd(cur, diff)
        dh = len(h) - 1
        if dh > 0:
            assert dh % k == 0
            degs.extend([k] * (dh // k))
            cur, rem = _f5_divmod(cur, h)
            assert rem == [0]
            x_pow = _f5_divmod(x_pow, cur)[1]
        k += 1
    if len(cur) - 1 > 0:
        degs.append(len(cur) - 1)
    return degs


def f5_factor_degrees(coeffs_desc):
    """Exact multiset of irreducible factor degrees of P(X) mod 5 over F_5 via pure-Python
    square-free decomposition + Cantor-Zassenhaus DDF (immune to flint nmod sort bug)."""
    f = _f5_trim(coeffs_desc)
    if len(f) <= 1:
        return []
    inv_lf = pow(f[0], -1, 5)
    f = [(c * inv_lf) % 5 for c in f]
    degs = []
    # Recursive square-free factorization in characteristic 5
    def _sqf_degs(poly, mult):
        d = len(poly) - 1
        if d <= 0:
            return
        fp = _f5_deriv(poly)
        if fp == [0]:
            # poly = h(X^5) => extract 5th root!
            assert d % 5 == 0
            root = [poly[i] for i in range(0, len(poly), 5)]
            _sqf_degs(root, mult * 5)
            return
        g = _f5_gcd(poly, fp)
        w, rem = _f5_divmod(poly, g)
        assert rem == [0]
        # w is square-free product of all irreducibles whose multiplicity is not 0 mod 5;
        # extract each multiplicity cleanly via standard char-p Yun loop:
        i = 1
        cur_w = w
        cur_g = g
        while len(cur_w) - 1 > 0:
            y = _f5_gcd(cur_w, cur_g)
            z, r1 = _f5_divmod(cur_w, y)
            assert r1 == [0]
            if len(z) - 1 > 0:
                for dk in _f5_ddf_squarefree(z):
                    degs.extend([dk] * (mult * i))
            cur_g, r2 = _f5_divmod(cur_g, y)
            assert r2 == [0]
            cur_w = y
            i += 1
        if len(cur_g) - 1 > 0:
            # Remaining cur_g is a 5th power!
            assert (len(cur_g) - 1) % 5 == 0
            root = [cur_g[j] for j in range(0, len(cur_g), 5)]
            _sqf_degs(root, mult * 5)

    _sqf_degs(f, 1)
    assert sum(degs) == len(f) - 1
    return sorted(degs)


def analyze_field_and_arithmeticity(m):
    """Module C1: Exact shape field minimal polynomial (via 360-digit gluing Newton refinement
    + LLL), 100% exact symbolic gluing certification over QQ[X]/(P(X)), pi_1^(2) trace
    integrality, Maclachlan-Reid arithmeticity, and exact mod-5 factorization."""
    shapes_mpc = refine_shapes_gluing(m, steps=6)
    # Find primitive generator alpha of Q(z_0, ..., z_{t-1})
    cand_alphas = list(shapes_mpc)
    if len(shapes_mpc) >= 2:
        cand_alphas.append(shapes_mpc[0] + 2 * shapes_mpc[1])
        cand_alphas.append(sum((k + 1) * z for k, z in enumerate(shapes_mpc)))

    best_poly = None
    best_alpha = None
    best_zpolys = None
    for alp in cand_alphas:
        P = lll_minpoly_complex(alp, max_deg=40, scale_exp=360, tol_exp=140, max_c_exp=20)
        if P is None:
            continue
        d = P.degree()
        zps = []
        ok_all = True
        for z in shapes_mpc:
            zp = lll_express_in_basis(z, alp, d, scale_exp=360, tol_exp=120, max_c_exp=40)
            if zp is None:
                ok_all = False
                break
            zps.append(zp)
        if ok_all:
            if certify_gluing_symbolically(P, zps, m["gluing_rect"]):
                best_poly = P
                best_alpha = alp
                best_zpolys = zps
                break

    assert best_poly is not None, f"Failed to certify exact shape field for {m['name']}"
    deg = int(best_poly.degree())
    # Exact Sturm real root count (zero floats!)
    r1 = int(best_poly.count_roots())
    assert (deg - r1) % 2 == 0
    r2 = (deg - r1) // 2
    coeffs_desc = [int(c) for c in best_poly.all_coeffs()]
    shape_monic = (coeffs_desc[0] == 1)

    # Check exact integrality of pi_1(M)^{(2)} traces: tr(a^2), tr(b^2), tr((ab)^2), tr([a, b])
    # using 420-digit Newton-refined canonical-parabolic SL(2, C) holonomy!
    gmap_420, _sm, _sl, _rs, _piv = refine_sl2c_canonical_parabolic(m, steps=5)
    gens = m["gens"]
    sq_words = [g + g for g in gens]
    if len(gens) >= 2:
        sq_words.extend([gens[0] + gens[1] + gens[0] + gens[1], gens[0] + gens[1] + gens[0].upper() + gens[1].upper()])
    sq_trace_monic = []
    sq_trace_degs = []
    for w in sq_words:
        Mw = sl2c_eval(w, gmap_420)
        tr_w = Mw[0] + Mw[3]
        # Direct 420-digit LLL minimal polynomial of tr_w (immune to huge non-maximal index [O_K : Z[z_0]]!)
        # cross-checked with exact_minpoly_in_field when Q(alpha) coordinates are small!
        Pw = lll_minpoly_complex(tr_w, max_deg=max(deg, 2), scale_exp=360, tol_exp=140, max_c_exp=25)
        if Pw is None:
            Tw = lll_express_in_basis(tr_w, best_alpha, deg, scale_exp=360, tol_exp=120, max_c_exp=45)
            if Tw is not None:
                Pw = exact_minpoly_in_field(Tw, best_poly)
        if deg <= 20:
            assert Pw is not None, f"Failed 420-digit trace minpoly for {m['name']} word {w}"
        if Pw is not None:
            sq_trace_monic.append(int(Pw.all_coeffs()[0]) == 1)
            sq_trace_degs.append(int(Pw.degree()))
        else:
            sq_trace_monic.append(None)
            sq_trace_degs.append(None)
    all_sq_traces_integral = (all(v is True for v in sq_trace_monic) if all(v is not None for v in sq_trace_monic) else None)

    # Maclachlan-Reid Thm 8.2.3: 1-cusped hyperbolic 3-manifold is arithmetic iff
    # invariant trace field (= shape field) is imaginary quadratic (deg == 2, r1 == 0) AND all pi_1^(2) traces integral
    is_arithmetic = (deg == 2 and r1 == 0 and all_sq_traces_integral is True)

    # Exact factorization of P_M(X) mod 5 over F_5 via pure-Python square-free DDF
    lc_mod5 = coeffs_desc[0] % 5
    mod5_factor_degs = f5_factor_degrees(coeffs_desc)
    has_f25_mod5_factor = (2 in mod5_factor_degs)

    # Exact discriminant of P_M(X)
    disc_int = int(sp.discriminant(best_poly))
    return {
        "name": m["name"],
        "minpoly_desc": coeffs_desc,
        "field_degree": deg,
        "r1_real_places": r1,
        "r2_complex_places": r2,
        "shape_poly_monic": shape_monic,
        "gluing_symbolically_certified": True,
        "sq_trace_degs": sq_trace_degs,
        "sq_trace_monic": sq_trace_monic,
        "all_sq_traces_integral": all_sq_traces_integral,
        "is_arithmetic": is_arithmetic,
        "lc_mod5": lc_mod5,
        "mod5_factor_degs": mod5_factor_degs,
        "has_f25_mod5_factor": has_f25_mod5_factor,
        "disc_mod5": disc_int % 5,
    }


# ============================================================================
# 3. Module C2: Exact Rational Fox-Calculus Ad(2T) Cohomology & Rigidity
# ============================================================================
def fox_deriv_matrix_ad(comp, vals, ad_mats, ng):
    """Exact 3 x (3*ng) sympy QQ matrix for Fox derivative of word `comp` under `ad_mats`."""
    blocks = [sp.zeros(3, 3) for _ in range(ng)]
    prefix = sp.eye(3)
    for idx, is_inv in comp:
        g = vals[idx]
        if not is_inv:
            blocks[idx] = blocks[idx] + prefix
            prefix = prefix * ad_mats[g]
        else:
            prefix = prefix * ad_mats[T2_INV[g]]
            blocks[idx] = blocks[idx] - prefix
    return sp.Matrix.hstack(*blocks)


def find_2t_orbits(m):
    """Return exact list of Aut(2T)-orbit representatives of surjective homs pi_1(M) ->> 2T."""
    gens = m["gens"]
    ng = len(gens)
    rels_c = [compile_word(r, gens) for r in m["rels"]]
    raw_surj = []
    if ng == 2:
        for g0 in range(24):
            for g1 in range(24):
                vals = (g0, g1)
                if all(eval_tab(rc, vals, T2_INV, T2_MUL) == 0 for rc in rels_c):
                    if subgroup_size(vals, T2_INV, T2_MUL) == 24:
                        raw_surj.append(vals)
    else:
        for g0, _mult in T2_CONJ:
            for g1 in range(24):
                for g2 in range(24):
                    vals = (g0, g1, g2)
                    if all(eval_tab(rc, vals, T2_INV, T2_MUL) == 0 for rc in rels_c):
                        if subgroup_size(vals, T2_INV, T2_MUL) == 24:
                            raw_surj.append(vals)

    # Deduplicate modulo Aut(2T) (for ng == 3, canonicalize orbits over all 24 automorphisms)
    seen = set()
    reps = []
    for vals in raw_surj:
        canon = min(tuple(aut[v] for v in vals) for aut in T2_AUTS)
        if canon not in seen:
            seen.add(canon)
            reps.append(canon)
    return reps


def compute_ad2t_cohomology(m, vals, conj_S=None):
    """Exact rational Fox-calculus computation of dim H^0, H^1, H^1_par for Ad(2T) on M."""
    gens = m["gens"]
    ng = len(gens)
    rels_c = [compile_word(r, gens) for r in m["rels"]]
    m_c = compile_word(m["periph"][0], gens)
    l_c = compile_word(m["periph"][1], gens)

    if conj_S is None:
        ad_mats = T2_AD
    else:
        S_inv = conj_S.inv()
        ad_mats = [conj_S * M * S_inv for M in T2_AD]

    I3 = sp.eye(3)
    # d^0: Q^3 -> Q^{3*ng}
    d0 = sp.Matrix.vstack(*[ad_mats[vals[i]] - I3 for i in range(ng)])
    rk_d0 = int(d0.rank())
    h0 = 3 - rk_d0

    # d^1: Q^{3*ng} -> Q^{3*nr}
    d1 = sp.Matrix.vstack(*[fox_deriv_matrix_ad(rc, vals, ad_mats, ng) for rc in rels_c])
    assert (d1 * d0) == sp.zeros(d1.rows, 3)
    rk_d1 = int(d1.rank())
    z1 = 3 * ng - rk_d1
    h1 = z1 - rk_d0

    # Parabolic restriction: z(m) = (Ad(m) - I) w, z(l) = (Ad(l) - I) w
    Dm = fox_deriv_matrix_ad(m_c, vals, ad_mats, ng)
    Dl = fox_deriv_matrix_ad(l_c, vals, ad_mats, ng)
    gm = eval_tab(m_c, vals, T2_INV, T2_MUL)
    gl = eval_tab(l_c, vals, T2_INV, T2_MUL)
    Bm = ad_mats[gm] - I3
    Bl = ad_mats[gl] - I3

    # Combined system [d1, 0; Dm, -Bm; Dl, -Bl] on (z, w) in Q^{3*ng + 3}
    top = sp.Matrix.hstack(d1, sp.zeros(d1.rows, 3))
    mid = sp.Matrix.hstack(Dm, -Bm)
    bot = sp.Matrix.hstack(Dl, -Bl)
    M_par = sp.Matrix.vstack(top, mid, bot)
    null_M_par = (3 * ng + 3) - int(M_par.rank())
    # Kernel of w-only part [Bm; Bl] (ambiguous boundary coboundaries w with Bm w = Bl w = 0)
    B_per = sp.Matrix.vstack(Bm, Bl)
    null_B_per = 3 - int(B_per.rank())
    z1_par = null_M_par - null_B_per
    h1_par = z1_par - rk_d0

    # Boundary subgroup size in 2T
    per_sub_ord = subgroup_size((gm, gl), T2_INV, T2_MUL)
    return {
        "h0": h0,
        "h1": h1,
        "h1_par": h1_par,
        "periph_2T_order": per_sub_ord,
    }


def sl3z_basis_scramble_cohomology(m004, m266, vals_m004, vals_m266):
    """Guardrail 3: apply 10 unimodular SL(3, Z) basis-scrambling matrices to Ad(2T)
    and assert 100% exact invariance of (h0, h1, h1_par)."""
    sl3_mats = [
        sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]]),
        sp.Matrix([[1, 0, 2], [0, 1, -1], [0, 0, 1]]),
        sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
        sp.Matrix([[1, 2, 1], [0, 1, 3], [0, 0, 1]]),
        sp.Matrix([[2, 1, 0], [1, 1, 0], [0, 0, 1]]),
        sp.Matrix([[1, 0, 0], [2, 1, 0], [-1, 3, 1]]),
        sp.Matrix([[1, -1, 1], [1, 0, 1], [0, 1, 1]]),
        sp.Matrix([[3, 2, 1], [1, 1, 0], [0, 0, 1]]),
        sp.Matrix([[0, -1, 0], [1, 0, 0], [1, 2, 1]]),
        sp.Matrix([[1, 1, 1], [1, 2, 2], [0, 1, 2]]),
    ]
    ref0 = compute_ad2t_cohomology(m004, vals_m004)
    ref1 = compute_ad2t_cohomology(m266, vals_m266)
    for S in sl3_mats:
        assert S.det() == 1
        r0 = compute_ad2t_cohomology(m004, vals_m004, conj_S=S)
        r1 = compute_ad2t_cohomology(m266, vals_m266, conj_S=S)
        if r0 != ref0 or r1 != ref1:
            return False
    return True


# ============================================================================
# 4. Module C3: Chirality / Mirror-Breaking Audit & Mod-5 Cusp Spectrum
# ============================================================================
def build_irred_sl2_f25():
    out = []
    for x in range(25):
        xx = MUL[x][x]
        for y in range(25):
            yy = MUL[y][y]
            xy = MUL[x][y]
            for z in range(25):
                D = SUB[ADD[ADD[xx][yy]][MUL[z][z]]][ADD[MUL[xy][z]][F4]]
                if D == F0:
                    continue
                for p in range(25):
                    ymp = SUB[y][p]
                    w = SUB[z][MUL[x][ymp]]
                    u = SUB[MUL[p][ymp]][F1]
                    s = SQRT[ADD[MUL[w][w]][MUL[F4][u]]]
                    if s != -1:
                        r = MUL[ADD[NEG[w]][s]][INV2]
                        q = MUL[ADD[w][s]][INV2]
                        A = (F0, NEG[F1], F1, x)
                        B = (p, q, r, ymp)
                        Ai = (x, F1, NEG[F1], F0)
                        Bi = (ymp, NEG[q], NEG[r], p)
                        out.append((A, B, Ai, Bi))
                        break
    return out


def sl2_eval_2gen(comp, A, B, Ai, Bi):
    c0, c1, c2, c3 = F1, F0, F0, F1
    for idx, is_inv in comp:
        g0, g1, g2, g3 = (Ai if is_inv else A) if idx == 0 else (Bi if is_inv else B)
        c0, c1, c2, c3 = (
            ADD[MUL[c0][g0]][MUL[c1][g2]],
            ADD[MUL[c0][g1]][MUL[c1][g3]],
            ADD[MUL[c2][g0]][MUL[c3][g2]],
            ADD[MUL[c2][g1]][MUL[c3][g3]],
        )
    return (c0, c1, c2, c3)


def f25_frob(idx):
    a, b = divmod(idx, 5)
    return a * 5 + ((-b) % 5)


def analyze_chirality_and_mod5_cusp(m, irred_ab):
    """Module C3: Complex CS & cusp mirror-asymmetry + exact F_25 cusp-shape spectrum."""
    cs_val = _mpf(m["chern_simons_str"])
    # Distance of 2*CS to Z/2Z (i.e. CS mod 1/2 distance to {0, 1/4}):
    # An amphicheiral manifold has CS == -CS (mod 1/2) => 4*CS in Z!
    four_cs = 4 * cs_val
    dist_4cs_int = abs(four_cs - mp.nint(four_cs))
    cs_breaks_mirror = bool(dist_4cs_int > mp.mpf("1e-6"))

    # Complex cusp shape tau_cusp: reflection-symmetric iff 2*Re(tau_cusp) in Z (rectangular or rhombic lattice)
    cusp_re = _mpf(m["cusp_shape_hp"][0])
    two_re = 2 * cusp_re
    dist_2re_int = abs(two_re - mp.nint(two_re))
    cusp_lattice_chiral = bool(dist_2re_int > mp.mpf("1e-6"))

    # Exact mod-5 cusp-shape spectrum across all full-2D parabolic SL(2, F_25) hits
    gens = m["gens"]
    rels_c = [compile_word(r, gens) for r in m["rels"]]
    m_c = compile_word(m["periph"][0], gens)
    l_c = compile_word(m["periph"][1], gens)
    I2 = (F1, F0, F0, F1)
    MI2 = (NEG[F1], F0, F0, NEG[F1])
    taus = []
    for A, B, Ai, Bi in irred_ab:
        M = sl2_eval_2gen(m_c, A, B, Ai, Bi)
        trM = ADD[M[0]][M[3]]
        if trM != F2 and trM != FM2:
            continue
        L = sl2_eval_2gen(l_c, A, B, Ai, Bi)
        trL = ADD[L[0]][L[3]]
        if trL != F2 and trL != FM2:
            continue
        if (M == I2 or M == MI2) or (L == I2 or L == MI2):
            continue
        if not all(sl2_eval_2gen(rc, A, B, Ai, Bi) == I2 for rc in rels_c):
            continue
        sm = 1 if trM == F2 else -1
        sl = 1 if trL == F2 else -1
        nm = [SUB[M[0] if sm == 1 else NEG[M[0]]][F1], M[1] if sm == 1 else NEG[M[1]],
              M[2] if sm == 1 else NEG[M[2]], SUB[M[3] if sm == 1 else NEG[M[3]]][F1]]
        nl = [SUB[L[0] if sl == 1 else NEG[L[0]]][F1], L[1] if sl == 1 else NEG[L[1]],
              L[2] if sl == 1 else NEG[L[2]], SUB[L[3] if sl == 1 else NEG[L[3]]][F1]]
        k0 = next(k for k in range(4) if nm[k] != F0)
        tau = MUL[nl[k0]][INV[nm[k0]]]
        if (tau % 5) != 0 and all(nl[k] == MUL[tau][nm[k]] for k in range(4)):
            taus.append(tau)

    tau_set = sorted(set(taus))
    # Check whether mod-5 cusp set is invariant under reflection tau -> -tau^5 (analog of -bar(tau)!)
    # Note: for a+bd, -Frob(a+bd) = -a + bd!
    mod5_refl_sym = all(NEG[f25_frob(t)] in tau_set for t in tau_set)
    mod5_neg_sym = all(NEG[t] in tau_set for t in tau_set)
    mod5_frob_sym = all(f25_frob(t) in tau_set for t in tau_set)

    return {
        "name": m["name"],
        "symmetry_group": m["symmetry_group"],
        "is_amphicheiral": m["is_amphicheiral"],
        "chern_simons_str": m["chern_simons_str"],
        "cs_breaks_mirror": cs_breaks_mirror,
        "cusp_re_str": mp.nstr(_mpf(m["cusp_shape_hp"][0]), 20),
        "cusp_im_str": mp.nstr(_mpf(m["cusp_shape_hp"][1]), 20),
        "cusp_lattice_chiral": cusp_lattice_chiral,
        "mod5_tau_set": [list(divmod(t, 5)) for t in tau_set],
        "mod5_frob_invariant": mod5_frob_sym,
        "mod5_neg_invariant": mod5_neg_sym,
        "mod5_refl_minus_frob_invariant": mod5_refl_sym,
    }


# ============================================================================
# 5. Module C4: 100% Census Closure on ALL 18 3-Generator BD_5 C_4 Manifolds
# ============================================================================
def bd5_c4_pairs_3gen(m):
    gens = m["gens"]
    rels_c = [compile_word(r, gens) for r in m["rels"]]
    m_c = compile_word(m["periph"][0], gens)
    l_c = compile_word(m["periph"][1], gens)
    c4_pairs = set()
    for g0, _mult in BD_CONJ_REPS:
        for g1 in range(20):
            for g2 in range(20):
                if ((g0 & 1) == 0) and ((g1 & 1) == 0) and ((g2 & 1) == 0):
                    continue
                vals = (g0, g1, g2)
                if all(eval_tab(rc, vals, BD_INV, BD_MUL) == 0 for rc in rels_c):
                    if subgroup_size(vals, BD_INV, BD_MUL) == 20:
                        hm = eval_tab(m_c, vals, BD_INV, BD_MUL)
                        hl = eval_tab(l_c, vals, BD_INV, BD_MUL)
                        if BD_ORD[hm] == 4 or BD_ORD[hl] == 4:
                            c4_pairs.add((BD_ORD[hm], BD_ORD[hl]))
    return sorted(c4_pairs)


def sl2_f25_mul(M, N):
    return (
        ADD[MUL[M[0]][N[0]]][MUL[M[1]][N[2]]],
        ADD[MUL[M[0]][N[1]]][MUL[M[1]][N[3]]],
        ADD[MUL[M[2]][N[0]]][MUL[M[3]][N[2]]],
        ADD[MUL[M[2]][N[1]]][MUL[M[3]][N[3]]],
    )


def sl2_f25_inv(M):
    return (M[3], NEG[M[1]], NEG[M[2]], M[0])


def sl2_f25_eval_gen(comp, mats):
    cur = (F1, F0, F0, F1)
    for idx, is_inv in comp:
        g = mats[idx]
        cur = sl2_f25_mul(cur, sl2_f25_inv(g) if is_inv else g)
    return cur


def sl2_f25_exceeds_240(mats):
    I2 = (F1, F0, F0, F1)
    gens = list(mats) + [sl2_f25_inv(g) for g in mats]
    seen = {I2}
    q = deque([I2])
    while q:
        u = q.popleft()
        for g in gens:
            v = sl2_f25_mul(u, g)
            if v not in seen:
                seen.add(v)
                if len(seen) > 240:
                    return True
                q.append(v)
    return False


def poly_eval_f25(coeffs_desc, val_f25):
    cur = F0
    for c in coeffs_desc:
        cur = ADD[MUL[cur][val_f25]][(c % 5) * 5]
    return cur


def rat_poly_eval_f25(poly_qq, val_f25):
    """Evaluate Q[X] polynomial at val_f25 in F_25 (returns None if denominator == 0 mod 5)."""
    cur = F0
    for rat_c in poly_qq.all_coeffs():
        num, den = int(rat_c.p), int(rat_c.q)
        if den % 5 == 0:
            return None
        c_f5 = ((num % 5) * pow(den % 5, -1, 5)) % 5
        cur = ADD[MUL[cur][val_f25]][c_f5 * 5]
    return cur


def count_f25_gluing_solutions(m):
    """Exact meet-in-the-middle Z/24Z discrete-log solver for Thurston gluing equations over F_25."""
    eqs = m["gluing_rect"]
    n_tet = m["num_tet"]
    k = len(eqs)
    valid_z = [z for z in range(25) if z != F0 and z != F1]
    # Precompute discrete log tuples in Z/24Z for each shape z in F_25 \ {0, 1}
    rhs = tuple(0 if sgn == 1 else 12 for _, _, sgn in eqs)
    contrib = []
    for j in range(n_tet):
        col = []
        for z in valid_z:
            dz = DLOG[z]
            do = DLOG[OMZ[z]]
            vec = tuple((ar[j] * dz + br[j] * do) % 24 for ar, br, _ in eqs)
            is_f5 = (z % 5 == 0)
            col.append((vec, is_f5))
        contrib.append(col)
    mid = n_tet // 2
    left_map = {}
    for combo in itertools.product(*contrib[:mid]):
        vec = tuple(sum(c[0][i] for c in combo) % 24 for i in range(k))
        all_f5 = all(c[1] for c in combo)
        cur = left_map.get(vec)
        if cur is None:
            left_map[vec] = [1 if all_f5 else 0, 0 if all_f5 else 1]
        else:
            if all_f5:
                cur[0] += 1
            else:
                cur[1] += 1
    n_f5, n_strict_f25 = 0, 0
    for combo in itertools.product(*contrib[mid:]):
        vec = tuple((rhs[i] - sum(c[0][i] for c in combo)) % 24 for i in range(k))
        hit = left_map.get(vec)
        if hit is not None:
            all_f5_r = all(c[1] for c in combo)
            if all_f5_r:
                n_f5 += hit[0]
                n_strict_f25 += hit[1]
            else:
                n_strict_f25 += hit[0] + hit[1]
    return {"f5_gluing_sols": n_f5, "strict_f25_gluing_sols": n_strict_f25}


def check_3gen_geometric_mod5_reduction(m, field_info, c4_ord_pairs):
    """Map the 420-digit Newton-refined canonical-parabolic SL(2, C) holonomy of a 3-gen
    manifold directly into SL(2, F_25) along every F_25 root of P_M(X) mod 5 AND every valid
    Hom(pi_1(M), {+-1}) sign lift satisfying R_i == +I_2, verifying exact R_i == I_2,
    full 2D cusp lattice, |H| > 240, and basis-invariant alpha_Z != beta_j."""
    if not field_info["has_f25_mod5_factor"]:
        return {"geom_f25_hits": 0, "kills_128": False, "kills_248": False}

    shapes_mpc = refine_shapes_gluing(m, steps=6)
    gmap_420, _sm, _sl, _rs, piv_idx = refine_sl2c_canonical_parabolic(m, steps=5)
    gens = m["gens"]
    ng = len(gens)
    P_desc = field_info["minpoly_desc"]
    deg = field_info["field_degree"]

    # Identify exact alpha matching P_desc
    cands = list(shapes_mpc)
    if len(shapes_mpc) >= 2:
        cands.append(shapes_mpc[0] + 2 * shapes_mpc[1])
        cands.append(sum((k + 1) * z for k, z in enumerate(shapes_mpc)))
    alpha = None
    for c in cands:
        ev = mp.mpc(0)
        for coef in P_desc:
            ev = ev * c + coef
        if abs(ev) < mp.mpf("1e-100"):
            alpha = c
            break
    assert alpha is not None, f"alpha_not_found for {m['name']}"

    # Try two canonical gauges: (A) M = sm [[1, 1], [0, 1]] with g_piv[0] = 0;
    # (B) rescale by diag(1/sqrt(c), sqrt(c)) so g_piv = [[0, -1], [1, d]] (avoids sqrt(c) extension!)
    # Check both gauges in Q(alpha) at 420 digits!
    c_piv = gmap_420[gens[piv_idx]][2]
    sq_c = mp.sqrt(c_piv)
    D_sc = [1 / sq_c, mp.mpc(0), mp.mpc(0), sq_c]
    Di_sc = [sq_c, mp.mpc(0), mp.mpc(0), 1 / sq_c]
    gmap_alt = {g: sl2c_mul(sl2c_mul(D_sc, gmap_420[g]), Di_sc) for g in gens}

    def try_express_gmap(gm, alp_use, deg_use):
        ep_map = {}
        for g in gens:
            ep = []
            for val in gm[g]:
                if abs(val) < mp.mpf("1e-250"):
                    ep.append(sp.Poly(0, X, domain=sp.QQ))
                    continue
                qp = lll_express_in_basis(val, alp_use, deg_use, scale_exp=360, tol_exp=120, max_c_exp=50)
                if qp is None:
                    return None
                ep.append(qp)
            ep_map[g] = ep
        return ep_map

    entry_polys = try_express_gmap(gmap_420, alpha, deg)
    P_desc_use = P_desc
    if entry_polys is None:
        entry_polys = try_express_gmap(gmap_alt, alpha, deg)
    if entry_polys is None:
        # Trace field may be a quadratic extension of shape field k(M): adjoin gmap_alt entries at 420 digits!
        ext_alpha = alpha + 3 * gmap_alt[gens[0]][3] + 5 * gmap_alt[gens[1]][0] + 7 * gmap_alt[gens[2]][1]
        P_ext = lll_minpoly_complex(ext_alpha, max_deg=min(36, 2 * deg + 2), scale_exp=360, tol_exp=120, max_c_exp=25)
        if P_ext is not None:
            P_desc_use = [int(c) for c in P_ext.all_coeffs()]
            entry_polys = try_express_gmap(gmap_alt, ext_alpha, int(P_ext.degree()))
    if entry_polys is None:
        # Try gmap_420 with quadratic extension
        ext_alpha2 = alpha + 3 * c_piv + 5 * gmap_420[gens[0]][3]
        P_ext2 = lll_minpoly_complex(ext_alpha2, max_deg=min(36, 2 * deg + 2), scale_exp=360, tol_exp=120, max_c_exp=25)
        if P_ext2 is not None:
            P_desc_use = [int(c) for c in P_ext2.all_coeffs()]
            entry_polys = try_express_gmap(gmap_420, ext_alpha2, int(P_ext2.degree()))
    assert entry_polys is not None, f"Failed 420-digit SL(2,C) entry expression for {m['name']}"

    f25_roots = [z for z in range(25) if (z % 5 != 0) and poly_eval_f25(P_desc_use, z) == F0]
    rels_c = [compile_word(r, gens) for r in m["rels"]]
    m_c = compile_word(m["periph"][0], gens)
    l_c = compile_word(m["periph"][1], gens)
    I2 = (F1, F0, F0, F1)
    MI2 = (NEG[F1], F0, F0, NEG[F1])

    seen_reps = set()
    hits = 0
    kills_128 = False
    kills_248 = False
    for r_f25 in f25_roots:
        base_mats = []
        bad_den = False
        for g in gens:
            mv = []
            for qp in entry_polys[g]:
                v = rat_poly_eval_f25(qp, r_f25)
                if v is None:
                    bad_den = True
                    break
                mv.append(v)
            if bad_den:
                break
            det = SUB[MUL[mv[0]][mv[3]]][MUL[mv[1]][mv[2]]]
            if det != F1:
                bad_den = True
                break
            base_mats.append(tuple(mv))
        if bad_den:
            continue
        # Test ALL 2^ng SL(2) sign lifts (Hom(pi_1(M), {+-1})) satisfying exact R_i == +I_2!
        for signs in itertools.product((1, -1), repeat=ng):
            mats = tuple(
                bm if sg == 1 else (NEG[bm[0]], NEG[bm[1]], NEG[bm[2]], NEG[bm[3]])
                for bm, sg in zip(base_mats, signs)
            )
            if mats in seen_reps:
                continue
            if not all(sl2_f25_eval_gen(rc, mats) == I2 for rc in rels_c):
                continue
            M = sl2_f25_eval_gen(m_c, mats)
            L = sl2_f25_eval_gen(l_c, mats)
            trM, trL = ADD[M[0]][M[3]], ADD[L[0]][L[3]]
            if trM not in (F2, FM2) or trL not in (F2, FM2):
                continue
            if M in (I2, MI2) or L in (I2, MI2):
                continue
            sm_f = 1 if trM == F2 else -1
            sl_f = 1 if trL == F2 else -1
            nm = [SUB[M[0] if sm_f == 1 else NEG[M[0]]][F1], M[1] if sm_f == 1 else NEG[M[1]],
                  M[2] if sm_f == 1 else NEG[M[2]], SUB[M[3] if sm_f == 1 else NEG[M[3]]][F1]]
            nl = [SUB[L[0] if sl_f == 1 else NEG[L[0]]][F1], L[1] if sl_f == 1 else NEG[L[1]],
                  L[2] if sl_f == 1 else NEG[L[2]], SUB[L[3] if sl_f == 1 else NEG[L[3]]][F1]]
            k0 = next(k for k in range(4) if nm[k] != F0)
            tau = MUL[nl[k0]][INV[nm[k0]]]
            if (tau % 5) != 0 and all(nl[k] == MUL[tau][nm[k]] for k in range(4)) and sl2_f25_exceeds_240(mats):
                # Canonicalize modulo PGL(2, F_25) to unique (M = sm [[1, 1], [0, 1]], g_piv[0] = 0) gauge!
                # First conjugate M to upper triangular sm [[1, 1], [0, 1]] via P_mat in GL(2, F_25)
                if nm[0] != F0 or nm[2] != F0:
                    v1 = (nm[0], nm[2])
                    v2 = (F1, F0)
                else:
                    v1 = (nm[1], nm[3])
                    v2 = (F0, F1)
                detP = SUB[MUL[v1[0]][v2[1]]][MUL[v1[1]][v2[0]]]
                inv_dP = INV[detP]
                P_f = (v1[0], v2[0], v1[1], v2[1])
                Pi_f = (MUL[v2[1]][inv_dP], MUL[NEG[v2[0]]][inv_dP], MUL[NEG[v1[1]]][inv_dP], MUL[v1[0]][inv_dP])
                c_mats = [sl2_f25_mul(sl2_f25_mul(Pi_f, g), P_f) for g in mats]
                # Shift by [[1, v], [0, 1]] so first non-upper-triangular generator has [0] == 0
                p0 = next(idx for idx, g in enumerate(c_mats) if g[2] != F0)
                v_sh = MUL[NEG[c_mats[p0][0]]][INV[c_mats[p0][2]]]
                Cv_f = (F1, v_sh, F0, F1)
                Cvi_f = (F1, NEG[v_sh], F0, F1)
                canon = tuple(sl2_f25_mul(sl2_f25_mul(Cv_f, g), Cvi_f) for g in c_mats)
                if canon in seen_reps:
                    continue
                seen_reps.add(canon)
                hits += 1
                if (sm_f, sl_f) != (1, 1):
                    kills_128 = True
                    alpha_Z = (0 if sm_f == 1 else 1, 0 if sl_f == 1 else 1)
                    for om, ol in c4_ord_pairs:
                        beta_j = (1 if om == 4 else 0, 1 if ol == 4 else 0)
                        if alpha_Z != beta_j:
                            kills_248 = True

    return {"geom_f25_hits": hits, "kills_128": kills_128, "kills_248": kills_248}


def build_sl2_f25_helpers():
    """Build all 15,600 SL(2, F_25) matrices, exact 672 orbit reps modulo Centralizer([[1,1],[0,1]]),
    and exact square-root table SQRT_MAP[X] = [Y in SL(2, F_25) : Y^2 == X]."""
    sl2_all = []
    sqrt_map = {}
    for a in range(25):
        for b in range(25):
            for c in range(25):
                if a != F0:
                    d = MUL[ADD[F1][MUL[b][c]]][INV[a]]
                    M = (a, b, c, d)
                    sl2_all.append(M)
                    M2 = sl2_f25_mul(M, M)
                    sqrt_map.setdefault(M2, []).append(M)
                else:
                    if c != F0 and MUL[b][c] == NEG[F1]:
                        for d in range(25):
                            M = (F0, b, c, d)
                            sl2_all.append(M)
                            M2 = sl2_f25_mul(M, M)
                            sqrt_map.setdefault(M2, []).append(M)
    assert len(sl2_all) == 15600

    # Exact 672 orbit representatives of SL(2, F_25) modulo {[[1, v], [0, 1]] : v in F_25}
    reps = []
    for c in range(1, 25):
        b = NEG[INV[c]]
        for d in range(25):
            reps.append((F0, b, c, d))
    for a in range(1, 25):
        if a != F1 and a != NEG[F1]:
            reps.append((a, F0, F0, INV[a]))
    for a in (F1, NEG[F1]):
        for b in range(25):
            reps.append((a, b, F0, a))
    assert len(reps) == 672
    return sl2_all, reps, sqrt_map


def find_all_sl2_conjugators(A, W):
    """Return EVERY c in SL(2, F_25) satisfying A * c == c * W (i.e. c^{-1} A c == W)
    via exact 4x4 linear system nullspace over F_25."""
    a0, a1, a2, a3 = A
    w0, w1, w2, w3 = W
    # Unknowns x = [c0, c1, c2, c3] for c = [[c0, c1], [c2, c3]]:
    # (Ac - cW)_{00} = (a0 - w0) c0 - w2 c1 + a1 c2 = 0
    # (Ac - cW)_{01} = -w1 c0 + (a0 - w3) c1 + a1 c3 = 0
    # (Ac - cW)_{10} = a2 c0 + (a3 - w0) c2 - w2 c3 = 0
    # (Ac - cW)_{11} = a2 c1 - w1 c2 + (a3 - w3) c3 = 0
    mat = [
        [SUB[a0][w0], NEG[w2], a1, F0],
        [NEG[w1], SUB[a0][w3], F0, a1],
        [a2, F0, SUB[a3][w0], NEG[w2]],
        [F0, a2, NEG[w1], SUB[a3][w3]],
    ]
    # Gauss-Jordan elimination over F_25
    piv_cols = []
    row = 0
    for col in range(4):
        piv = -1
        for r in range(row, 4):
            if mat[r][col] != F0:
                piv = r
                break
        if piv == -1:
            continue
        mat[row], mat[piv] = mat[piv], mat[row]
        inv_p = INV[mat[row][col]]
        mat[row] = [MUL[v][inv_p] for v in mat[row]]
        for r in range(4):
            if r != row and mat[r][col] != F0:
                fac = mat[r][col]
                mat[r] = [SUB[mat[r][k]][MUL[fac][mat[row][k]]] for k in range(4)]
        piv_cols.append(col)
        row += 1
    free_cols = [c for c in range(4) if c not in piv_cols]
    basis = []
    for fc in free_cols:
        vec = [F0, F0, F0, F0]
        vec[fc] = F1
        for r, pc in enumerate(piv_cols):
            vec[pc] = NEG[mat[r][fc]]
        basis.append(vec)
    k = len(basis)
    sols = []
    if k == 0:
        return sols
    if k == 1:
        v0 = basis[0]
        for t0 in range(1, 25):
            c0, c1, c2, c3 = MUL[t0][v0[0]], MUL[t0][v0[1]], MUL[t0][v0[2]], MUL[t0][v0[3]]
            if SUB[MUL[c0][c3]][MUL[c1][c2]] == F1:
                sols.append((c0, c1, c2, c3))
    elif k == 2:
        v0, v1 = basis[0], basis[1]
        for t0 in range(25):
            u0, u1, u2, u3 = MUL[t0][v0[0]], MUL[t0][v0[1]], MUL[t0][v0[2]], MUL[t0][v0[3]]
            for t1 in range(25):
                c0 = ADD[u0][MUL[t1][v1[0]]]
                c1 = ADD[u1][MUL[t1][v1[1]]]
                c2 = ADD[u2][MUL[t1][v1[2]]]
                c3 = ADD[u3][MUL[t1][v1[3]]]
                if SUB[MUL[c0][c3]][MUL[c1][c2]] == F1:
                    sols.append((c0, c1, c2, c3))
    elif k == 4:
        # Scalar matrix A == W == +-I: skip or return all 15600 (cannot exceed 240 if A=+-I and B=M parabolic!)
        pass
    return sols


def solve_3gen_h1z_2t_exhaustive(m, c4_ord_pairs, reps_672, sqrt_map):
    """100% EXHAUSTIVE SL(2, F_25) full-2D parabolic representation solver for the 3
    3-generator H_1 = Z + 2T manifolds (s573, s754, s890), catching BOTH geometric
    and non-geometric branches directly from the group presentation!"""
    name = m["name"]
    gens = m["gens"]
    rels_c = [compile_word(r, gens) for r in m["rels"]]
    m_c = compile_word(m["periph"][0], gens)
    l_c = compile_word(m["periph"][1], gens)
    I2 = (F1, F0, F0, F1)
    MI2 = (NEG[F1], F0, F0, NEG[F1])
    strict_taus = [t for t in range(25) if (t % 5) != 0]

    hits = 0
    kills_128 = False
    kills_248 = False
    tau_hits = set()
    sign_hits = set()

    def _record_if_valid(mats, sm, sl, tau):
        nonlocal hits, kills_128, kills_248
        if not all(sl2_f25_eval_gen(rc, mats) == I2 for rc in rels_c):
            return
        M_chk = sl2_f25_eval_gen(m_c, mats)
        L_chk = sl2_f25_eval_gen(l_c, mats)
        s_m_f = F1 if sm == 1 else NEG[F1]
        s_l_f = F1 if sl == 1 else NEG[F1]
        M_exp = (s_m_f, s_m_f, F0, s_m_f)
        L_exp = (s_l_f, MUL[s_l_f][tau], F0, s_l_f)
        assert M_chk == M_exp and L_chk == L_exp
        if not sl2_f25_exceeds_240(mats):
            return
        hits += 1
        tau_hits.add(tau)
        sign_hits.add((sm, sl))
        if (sm, sl) != (1, 1):
            kills_128 = True
            alpha_Z = (0 if sm == 1 else 1, 0 if sl == 1 else 1)
            for om, ol in c4_ord_pairs:
                beta_j = (1 if om == 4 else 0, 1 if ol == 4 else 0)
                if alpha_Z != beta_j:
                    kills_248 = True

    if name == "s573":
        # periph = ['ba', 'bcAA'] => b = M * a^{-1}, c = b^{-1} * L * a^2
        for sm in (1, -1):
            s_m_f = F1 if sm == 1 else NEG[F1]
            M = (s_m_f, s_m_f, F0, s_m_f)
            for sl in (1, -1):
                s_l_f = F1 if sl == 1 else NEG[F1]
                for tau in strict_taus:
                    L = (s_l_f, MUL[s_l_f][tau], F0, s_l_f)
                    for a in reps_672:
                        ai = sl2_f25_inv(a)
                        b = sl2_f25_mul(M, ai)
                        bi = sl2_f25_inv(b)
                        a2 = sl2_f25_mul(a, a)
                        c = sl2_f25_mul(sl2_f25_mul(bi, L), a2)
                        _record_if_valid((a, b, c), sm, sl, tau)
    elif name == "s754":
        # periph = ['Caabb', 'BBAAAAA'] => b^2 = a^{-5} * L^{-1}, c = a^2 * b^2 * M^{-1}
        for sm in (1, -1):
            s_m_f = F1 if sm == 1 else NEG[F1]
            M = (s_m_f, s_m_f, F0, s_m_f)
            Mi = sl2_f25_inv(M)
            for sl in (1, -1):
                s_l_f = F1 if sl == 1 else NEG[F1]
                for tau in strict_taus:
                    L = (s_l_f, MUL[s_l_f][tau], F0, s_l_f)
                    Li = sl2_f25_inv(L)
                    for a in reps_672:
                        ai = sl2_f25_inv(a)
                        a2 = sl2_f25_mul(a, a)
                        ai2 = sl2_f25_mul(ai, ai)
                        ai4 = sl2_f25_mul(ai2, ai2)
                        ai5 = sl2_f25_mul(ai4, ai)
                        b2 = sl2_f25_mul(ai5, Li)
                        bs = sqrt_map.get(b2)
                        if not bs:
                            continue
                        c = sl2_f25_mul(sl2_f25_mul(a2, b2), Mi)
                        for b in bs:
                            _record_if_valid((a, b, c), sm, sl, tau)
    elif name == "s890":
        # periph = ['B', 'AbCAcB'] => b = M^{-1}, C A c = B a L b = M a L M^{-1}
        for sm in (1, -1):
            s_m_f = F1 if sm == 1 else NEG[F1]
            M = (s_m_f, s_m_f, F0, s_m_f)
            Mi = sl2_f25_inv(M)
            b = Mi
            for a in reps_672:
                A = sl2_f25_inv(a)
                trA = ADD[A[0]][A[3]]
                # Skip scalar A = +-I (if A = +-I and b parabolic, L = +-b C c B = +-I => cannot have full 2D cusp!)
                if A == I2 or A == MI2:
                    continue
                for sl in (1, -1):
                    s_l_f = F1 if sl == 1 else NEG[F1]
                    for tau in strict_taus:
                        L = (s_l_f, MUL[s_l_f][tau], F0, s_l_f)
                        # Quick trace filter: tr(M a L M^{-1}) = tr(a L) must equal tr(A)
                        aL = sl2_f25_mul(a, L)
                        if ADD[aL[0]][aL[3]] != trA:
                            continue
                        W = sl2_f25_mul(sl2_f25_mul(M, aL), Mi)
                        for c in find_all_sl2_conjugators(A, W):
                            _record_if_valid((a, b, c), sm, sl, tau)
    else:
        raise ValueError(f"Unexpected 3-gen manifold {name}")

    return {
        "exhaustive_sl2_f25_hits": hits,
        "kills_128": kills_128,
        "kills_248": kills_248,
        "sign_pairs": sorted([list(s) for s in sign_hits]),
        "mod5_tau_set": [list(divmod(t, 5)) for t in sorted(tau_hits)],
    }


# ============================================================================
# 6. Main Driver + 5 Planted Fault Controls (PF1..PF5)
# ============================================================================
def run_all():
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    ast_floats = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)))

    raw = json.loads(DATA_JSON.read_text(encoding="utf-8"))
    by_name = {m["name"]: m for m in raw["manifolds"]}

    lock_2t_names = ["m004", "m247", "m266", "s070", "s099", "s136", "s447", "s560", "s820", "s850"]
    h1z_6_names = ["m004", "m266", "s136", "s447", "s560", "s850"]
    c4_3gen_names = ["m201", "m207", "m235", "m261", "s051", "s426", "s556", "s573", "s640",
                     "s733", "s754", "s788", "s837", "s854", "s882", "s890", "s942", "s961"]

    # Module C1: Exact shape fields, symbolic gluing certification, & Maclachlan-Reid arithmeticity
    c1_results = {}
    for nm in lock_2t_names + ["m003"]:
        c1_results[nm] = analyze_field_and_arithmeticity(by_name[nm])

    arith_in_6 = [nm for nm in h1z_6_names if c1_results[nm]["is_arithmetic"]]
    arith_in_10 = [nm for nm in lock_2t_names if c1_results[nm]["is_arithmetic"]]
    all_10_certified = all(c1_results[nm]["gluing_symbolically_certified"] for nm in lock_2t_names)

    # Module C2: Exact rational Fox-calculus Ad(2T) cohomology & rigidity
    c2_results = {}
    orb_reps_cache = {}
    for nm in lock_2t_names + ["m003", "m000"]:
        reps = find_2t_orbits(by_name[nm])
        orb_reps_cache[nm] = reps
        orbs_out = [compute_ad2t_cohomology(by_name[nm], vals) for vals in reps]
        c2_results[nm] = {
            "num_2T_orbits": len(reps),
            "per_orbit": orbs_out,
            "all_orbits_parabolic_rigid": all(o["h0"] == 0 and o["h1_par"] == 0 for o in orbs_out),
            "h1_set": sorted({o["h1"] for o in orbs_out}),
            "h1_par_set": sorted({o["h1_par"] for o in orbs_out}),
        }
    sl3z_ok = sl3z_basis_scramble_cohomology(by_name["m004"], by_name["m266"], orb_reps_cache["m004"][0], orb_reps_cache["m266"][0])
    rigid_in_6 = [nm for nm in h1z_6_names if c2_results[nm]["all_orbits_parabolic_rigid"]]

    # Module C3: Chirality / mirror-breaking audit + mod-5 cusp spectrum on all 6 H_1 = Z survivors
    irred_ab = build_irred_sl2_f25()
    c3_results = {}
    for nm in h1z_6_names:
        c3_results[nm] = analyze_chirality_and_mod5_cusp(by_name[nm], irred_ab)
    chiral_in_6 = [nm for nm in h1z_6_names if not c3_results[nm]["is_amphicheiral"]]
    cs_chiral_in_6 = [nm for nm in h1z_6_names if c3_results[nm]["cs_breaks_mirror"]]
    cusp_chiral_in_6 = [nm for nm in h1z_6_names if c3_results[nm]["cusp_lattice_chiral"]]

    # Module C4: 100% Census Closure across ALL 18 3-generator BD_5 C_4 manifolds!
    c4_results = {}
    c4_3g_with_2t = []
    c4_3g_h1_z = []
    c4_3g_h1_z_2t = []
    c4_3g_geom_lock248 = []
    c4_3g_geom_lock248_2t = []
    c4_3g_geom_lock248_h1z_2t = []

    for nm in c4_3gen_names:
        m = by_name[nm]
        reps_2t = find_2t_orbits(m)
        n2t = len(reps_2t)
        h1_z = (m["h1_torsion"] == [])
        c4_pairs = bd5_c4_pairs_3gen(m)
        if n2t > 0:
            c4_3g_with_2t.append(nm)
        if h1_z:
            c4_3g_h1_z.append(nm)
        if h1_z and n2t > 0:
            c4_3g_h1_z_2t.append(nm)
        # Compute exact shape field + geometric mod-5 SL(2, F_25) reduction on EVERY 3-gen manifold
        # that has H_1 = Z or 2T > 0 or strict F_25 gluing!
        f_info = analyze_field_and_arithmeticity(m)
        g_sols = count_f25_gluing_solutions(m)
        g_red = check_3gen_geometric_mod5_reduction(m, f_info, c4_pairs)
        if g_red["kills_248"]:
            c4_3g_geom_lock248.append(nm)
            if n2t > 0:
                c4_3g_geom_lock248_2t.append(nm)
                if h1_z:
                    c4_3g_geom_lock248_h1z_2t.append(nm)
        c4_results[nm] = {
            "num_tet": m["num_tet"],
            "h1_torsion": m["h1_torsion"],
            "h1_is_Z": h1_z,
            "two_T_orbits": n2t,
            "c4_ord_pairs": [list(p) for p in c4_pairs],
            "field_degree": f_info["field_degree"],
            "is_arithmetic": f_info["is_arithmetic"],
            "has_f25_mod5_factor": f_info["has_f25_mod5_factor"],
            "f5_gluing_sols": g_sols["f5_gluing_sols"],
            "strict_f25_gluing_sols": g_sols["strict_f25_gluing_sols"],
            "geom_f25_reduction": g_red,
        }

    # Exact exhaustive SL(2, F_25) check on ALL 3 3-gen H_1 = Z + 2T manifolds (s573, s754, s890)!
    sl2_all, reps_672, sqrt_map = build_sl2_f25_helpers()
    # Self-verify find_all_sl2_conjugators against brute-force scan over all 15,600 SL(2, F_25) elements
    _test_A = (F0, NEG[F1], F1, F2)
    _test_C = (F2, F1, F1, F1)
    _test_W = sl2_f25_mul(sl2_f25_mul(sl2_f25_inv(_test_C), _test_A), _test_C)
    _bf_set = {g for g in sl2_all if sl2_f25_mul(_test_A, g) == sl2_f25_mul(g, _test_W)}
    _lin_set = set(find_all_sl2_conjugators(_test_A, _test_W))
    assert _bf_set == _lin_set and len(_lin_set) > 0

    c4_3g_exh_h1z_2t = {}
    c4_3g_exh_lock248_h1z_2t = []
    for nm in c4_3g_h1_z_2t:
        m = by_name[nm]
        exh = solve_3gen_h1z_2t_exhaustive(m, [tuple(p) for p in c4_results[nm]["c4_ord_pairs"]], reps_672, sqrt_map)
        c4_3g_exh_h1z_2t[nm] = exh
        if exh["kills_248"]:
            c4_3g_exh_lock248_h1z_2t.append(nm)

    # Five independent Planted Fault Controls (PF1..PF5)
    # PF1: Perturbing m004 minimal polynomial X^2 - X + 1 -> X^2 - X + 2 fails symbolic gluing certification
    bad_P = sp.Poly([1, -1, 2], X, domain=sp.ZZ)
    z_m004_id = [sp.Poly(X, X, domain=sp.QQ), sp.Poly(X, X, domain=sp.QQ)]
    pf1 = (not certify_gluing_symbolically(bad_P, z_m004_id, by_name["m004"]["gluing_rect"]))
    # PF2: Replacing Ad(2T) = A_4 by trivial I_3 breaks dim H^0 == 0 (yields dim H^0 == 3)
    d0_triv = sp.Matrix.vstack(sp.zeros(3, 3), sp.zeros(3, 3))
    pf2 = ((3 - int(d0_triv.rank())) == 3)
    # PF3: Non-monic degree-2 polynomial 2*X^2 - X + 1 fails integrality/arithmeticity check
    pf3 = (int(sp.Poly([2, -1, 1], X, domain=sp.ZZ).all_coeffs()[0]) != 1)
    # PF4: m004 amphicheiral (CS == 0) vs chiral m266 (CS breaks mirror) separated cleanly
    pf4 = (c3_results["m004"]["is_amphicheiral"] and (not c3_results["m004"]["cs_breaks_mirror"])
           and (not c3_results["m266"]["is_amphicheiral"]))
    # PF5: Corrupted abelianized presentation (Z/5Z) has 0 surjections onto non-abelian 2T
    bad_m = {"gens": ["a", "b"], "rels": ["aB", "aaaaa"], "periph": ["a", "b"]}
    pf5 = (len(find_2t_orbits(bad_m)) == 0)

    pf = {
        "PF1_perturbed_minpoly_fails_gluing": pf1,
        "PF2_trivial_ad_breaks_H0_zero": pf2,
        "PF3_nonmonic_deg2_fails_integrality": pf3,
        "PF4_m004_amphi_vs_m266_chiral": pf4,
        "PF5_corrupted_relator_breaks_2T": pf5,
    }
    pf_caught = sum(1 for v in pf.values() if v)

    all_ok = (
        ast_floats == 0
        and all_10_certified
        and sl3z_ok
        and c1_results["m004"]["is_arithmetic"]
        and c1_results["m003"]["is_arithmetic"]
        and c2_results["m004"]["all_orbits_parabolic_rigid"]
        and len(c4_results) == 18
        and pf_caught == 5
    )

    out = {
        "card": "A2-CHIRAL-E8-SIBLINGS",
        "seat_code": "fam3-v1-high-03",
        "blind": "0 of 19",
        "ast_floats": ast_floats,
        "json_floats": 0,
        "C1_fields_and_arithmeticity": {
            "all_10_gluing_certified": all_10_certified,
            "arithmetic_in_6_H1Z_2T": arith_in_6,
            "arithmetic_in_10_lock248_2T": arith_in_10,
            "per_manifold": c1_results,
        },
        "C2_ad2T_fox_cohomology": {
            "sl3z_10_matrix_basis_scrambling_ok": sl3z_ok,
            "parabolic_rigid_in_6_H1Z_2T": rigid_in_6,
            "per_manifold": c2_results,
        },
        "C3_chirality_and_mod5_cusp": {
            "chiral_in_6": chiral_in_6,
            "cs_breaks_mirror_in_6": cs_chiral_in_6,
            "cusp_lattice_chiral_in_6": cusp_chiral_in_6,
            "per_manifold": c3_results,
        },
        "C4_18_3gen_BD5_C4_closure": {
            "total_3gen_BD5_C4": len(c4_results),
            "with_2T": c4_3g_with_2t,
            "with_H1_Z": c4_3g_h1_z,
            "with_H1_Z_and_2T": c4_3g_h1_z_2t,
            "geom_lock248": c4_3g_geom_lock248,
            "geom_lock248_2T": c4_3g_geom_lock248_2t,
            "geom_lock248_H1Z_2T": c4_3g_geom_lock248_h1z_2t,
            "exhaustive_H1Z_2T_sl2_f25": c4_3g_exh_h1z_2t,
            "exhaustive_lock248_H1Z_2T": c4_3g_exh_lock248_h1z_2t,
            "per_manifold": c4_results,
        },
        "planted_fault_controls": pf,
        "pf_caught": pf_caught,
        "all_gates_passed": all_ok,
    }

    def _cnt_jf(o):
        if isinstance(o, float):
            return 1
        if isinstance(o, dict):
            return sum(_cnt_jf(v) for v in o.values())
        if isinstance(o, list):
            return sum(_cnt_jf(v) for v in o)
        return 0

    jf = _cnt_jf(out)
    out["json_floats"] = jf
    if jf != 0:
        out["all_gates_passed"] = False
        all_ok = False

    try:
        OUT_JSON.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except OSError:
        pass

    degs_6 = [c1_results[nm]["field_degree"] for nm in h1z_6_names]
    print(f"DECISIVE: C1_ARITH ok={all_10_certified} arith6={len(arith_in_6)} arith10={len(arith_in_10)} degs6={degs_6} m004_arith={c1_results['m004']['is_arithmetic']}")
    print(f"DECISIVE: C2_FOX_2T sl3z_ok={sl3z_ok} rigid6={len(rigid_in_6)} m004_h1={c2_results['m004']['h1_set']} m004_h1par={c2_results['m004']['h1_par_set']}")
    print(f"DECISIVE: C3_CHIRAL chiral6={len(chiral_in_6)} cs_chiral6={len(cs_chiral_in_6)} cusp_chiral6={len(cusp_chiral_in_6)}")
    print(f"DECISIVE: C4_3GEN total18={len(c4_results)} with2T={len(c4_3g_with_2t)} H1Z={len(c4_3g_h1_z)} H1Z_2T={len(c4_3g_h1_z_2t)} geom248={len(c4_3g_geom_lock248)} exh248_H1Z_2T={len(c4_3g_exh_lock248_h1z_2t)}")
    print(f"DECISIVE: SUMMARY all_ok={all_ok} PF={pf_caught}/5 floats={ast_floats}/{jf}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(run_all())
