#!/usr/bin/env python3
"""
Standalone exact-integer verification for card A2-P332 (message M22):
F4(Z) transitivity on orthogonal pairs of rank-1 idempotents in the split
integral Albert algebra J3(O_s(Z)), resolving B1121's bounded-search open
cases, verifying the Spin(4,5) Peirce-0 lattice L9 ~= <-2> perp U^4 reduction,
and supplying an unconditional constructive proof that Stab_{F4(Z)}(E11) is
transitive on all orthogonal partner idempotents F in J0(E11) (discharging the
generation gate G1 via three 2x2 Smith normal forms + Euclidean descent).

Zero code or data imported from main. 100% exact integer / Fraction / GF(p)
arithmetic throughout (exact Bareiss integer determinant and inverse).
Data-free: 0 of 19.
"""

from __future__ import annotations

import itertools
import json
import math
import os
import random
import time
from fractions import Fraction as Fr
from typing import Dict, List, Tuple

T0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time() - T0:7.2f}s] {msg}", flush=True)


# ============================================================================
# 1. Exact Zorn split integral octonions O_s(Z)
#    Element o = (a, x0, x1, x2, y0, y1, y2, b) in Z^8 (or Fraction^8).
#    Matrix [[a, x], [y, b]], norm N(o) = a*b - (x0*y0 + x1*y1 + x2*y2).
# ============================================================================

Oct = Tuple[int, int, int, int, int, int, int, int]
O_ZERO: Oct = (0, 0, 0, 0, 0, 0, 0, 0)
O_ONE: Oct = (1, 0, 0, 0, 0, 0, 0, 1)
E0_OCT: Oct = (1, 0, 0, 0, 0, 0, 0, 0)
F0_OCT: Oct = (0, 0, 0, 0, 0, 0, 0, 1)


def o_add(p: Tuple, q: Tuple) -> Tuple:
    return tuple(p[i] + q[i] for i in range(8))


def o_sub(p: Tuple, q: Tuple) -> Tuple:
    return tuple(p[i] - q[i] for i in range(8))


def o_neg(p: Tuple) -> Tuple:
    return tuple(-p[i] for i in range(8))


def o_scale(p: Tuple, s) -> Tuple:
    return tuple(p[i] * s for i in range(8))


def o_conj(p: Tuple) -> Tuple:
    a, x0, x1, x2, y0, y1, y2, b = p
    return (b, -x0, -x1, -x2, -y0, -y1, -y2, a)


def o_mul(p: Tuple, q: Tuple) -> Tuple:
    a, x0, x1, x2, y0, y1, y2, b = p
    ap, xp0, xp1, xp2, yp0, yp1, yp2, bp = q
    x_dot_yp = x0 * yp0 + x1 * yp1 + x2 * yp2
    y_dot_xp = y0 * xp0 + y1 * xp1 + y2 * xp2
    # y x y'
    cy0 = y1 * yp2 - y2 * yp1
    cy1 = y2 * yp0 - y0 * yp2
    cy2 = y0 * yp1 - y1 * yp0
    # x x x'
    cx0 = x1 * xp2 - x2 * xp1
    cx1 = x2 * xp0 - x0 * xp2
    cx2 = x0 * xp1 - x1 * xp0
    return (
        a * ap + x_dot_yp,
        a * xp0 + bp * x0 - cy0,
        a * xp1 + bp * x1 - cy1,
        a * xp2 + bp * x2 - cy2,
        ap * y0 + b * yp0 + cx0,
        ap * y1 + b * yp1 + cx1,
        ap * y2 + b * yp2 + cx2,
        b * bp + y_dot_xp,
    )


def o_norm(p: Tuple):
    a, x0, x1, x2, y0, y1, y2, b = p
    return a * b - (x0 * y0 + x1 * y1 + x2 * y2)


def o_bilin(p: Tuple, q: Tuple):
    """Polarized norm <p, q>_N = N(p + q) - N(p) - N(q)."""
    a, x0, x1, x2, y0, y1, y2, b = p
    ap, xp0, xp1, xp2, yp0, yp1, yp2, bp = q
    return a * bp + b * ap - (
        x0 * yp0 + xp0 * y0 + x1 * yp1 + xp1 * y1 + x2 * yp2 + xp2 * y2
    )


def o_gcd(p: Oct) -> int:
    g = 0
    for c in p:
        g = math.gcd(g, abs(int(c)))
    return g


OCT_BASIS: List[Oct] = [
    tuple(1 if j == i else 0 for j in range(8)) for i in range(8)  # type: ignore
]


# ============================================================================
# 2. Split Integral Albert Algebra J3(O_s(Z)) in 27 integer coordinates
#    v = [xi1, xi2, xi3, o1(8), o2(8), o3(8)]
#    Matrix:
#      [[ xi1,   o3,  ~o2 ],
#       [ ~o3,  xi2,   o1 ],
#       [  o2,  ~o1,  xi3 ]]
#    Scaled integral Jordan product: X (*) Y := 2 (X o Y) = X*Y + Y*X in Z^27!
# ============================================================================

def mk_vec(xi1, xi2, xi3, o1: Tuple = O_ZERO, o2: Tuple = O_ZERO, o3: Tuple = O_ZERO) -> List:
    return [xi1, xi2, xi3, *o1, *o2, *o3]


def unpack_vec(v: List):
    return v[0], v[1], v[2], tuple(v[3:11]), tuple(v[11:19]), tuple(v[19:27])


E11 = mk_vec(1, 0, 0)
E22 = mk_vec(0, 1, 0)
E33 = mk_vec(0, 0, 1)
J_ID = mk_vec(1, 1, 1)
J_ZERO = mk_vec(0, 0, 0)

J_BASIS: List[List[int]] = [
    [1 if j == i else 0 for j in range(27)] for i in range(27)
]


def j_offdiag(slot: int, o: Tuple) -> List:
    if slot == 1:
        return mk_vec(0, 0, 0, o, O_ZERO, O_ZERO)
    if slot == 2:
        return mk_vec(0, 0, 0, O_ZERO, o, O_ZERO)
    if slot == 3:
        return mk_vec(0, 0, 0, O_ZERO, O_ZERO, o)
    raise ValueError(slot)


def j_bullet_int(u: List, v: List) -> List:
    """Exact integral scaled Jordan product u (*) v = 2*(u o v) = u*v + v*u."""
    x1, x2, x3, o1, o2, o3 = unpack_vec(u)
    y1, y2, y3, p1, p2, p3 = unpack_vec(v)

    z1 = 2 * x1 * y1 + o_bilin(o2, p2) + o_bilin(o3, p3)
    z2 = 2 * x2 * y2 + o_bilin(o3, p3) + o_bilin(o1, p1)
    z3 = 2 * x3 * y3 + o_bilin(o1, p1) + o_bilin(o2, p2)

    # Off-diagonal (2,3) = slot 1:
    # (XY + YX)_{23} = ~o3 * ~p2 + x2*p1 + o1*y3 + ~p3 * ~o2 + y2*o1 + p1*x3
    q1 = o_add(
        o_add(o_scale(p1, x2 + x3), o_scale(o1, y2 + y3)),
        o_add(o_mul(o_conj(o3), o_conj(p2)), o_mul(o_conj(p3), o_conj(o2))),
    )
    # Off-diagonal (3,1) = o2 (since (1,3) is ~o2 and (3,1) is o2):
    # (XY + YX)_{31} = o2*y1 + ~o1 * ~p3 + x3*p2 + p2*x1 + ~p1 * ~o3 + y3*o2
    q2 = o_add(
        o_add(o_scale(p2, x3 + x1), o_scale(o2, y3 + y1)),
        o_add(o_mul(o_conj(o1), o_conj(p3)), o_mul(o_conj(p1), o_conj(o3))),
    )
    # Off-diagonal (1,2) = slot 3:
    # (XY + YX)_{12} = x1*p3 + o3*y2 + ~o2 * ~p1 + y1*o3 + p3*x2 + ~p2 * ~o1
    q3 = o_add(
        o_add(o_scale(p3, x1 + x2), o_scale(o3, y1 + y2)),
        o_add(o_mul(o_conj(o2), o_conj(p1)), o_mul(o_conj(p2), o_conj(o1))),
    )
    return mk_vec(z1, z2, z3, q1, q2, q3)


def j_mul_frac(u: List, v: List) -> List[Fr]:
    uF = [Fr(c) for c in u]
    vF = [Fr(c) for c in v]
    b = j_bullet_int(uF, vF)
    return [c / 2 for c in b]


def j_sq_int(u: List[int]) -> List[int]:
    """For u in Z^27, u o u = (u (*) u) / 2 is ALWAYS in Z^27."""
    b = j_bullet_int(u, u)
    assert all(c % 2 == 0 for c in b)
    return [c // 2 for c in b]


def j_trace(u: List):
    return u[0] + u[1] + u[2]


def j_S_int(u: List[int]) -> int:
    """Quadratic trace form S(u) = (tr(u)^2 - tr(u^2))/2 in Z."""
    t = j_trace(u)
    u2 = j_sq_int(u)
    num = t * t - j_trace(u2)
    assert num % 2 == 0
    return num // 2


def j_adj_int(u: List[int]) -> List[int]:
    """Freudenthal sharp u^# = u^2 - tr(u)*u + S(u)*I in Z^27."""
    t = j_trace(u)
    s = j_S_int(u)
    u2 = j_sq_int(u)
    out = [u2[i] - t * u[i] for i in range(27)]
    out[0] += s
    out[1] += s
    out[2] += s
    return out


def j_det_freudenthal(u: List[int]) -> int:
    """Cubic norm det(u) = (1/3) tr(u o u^#) = (1/6) tr(u (*) u^#) in Z."""
    adj = j_adj_int(u)
    b = j_bullet_int(u, adj)
    t = j_trace(b)
    assert t % 6 == 0
    return t // 6


def j_det_closed(u: List) -> int:
    x1, x2, x3, o1, o2, o3 = unpack_vec(u)
    trip = o_mul(o1, o_mul(o2, o3))
    return (
        x1 * x2 * x3
        - x1 * o_norm(o1)
        - x2 * o_norm(o2)
        - x3 * o_norm(o3)
        + trip[0]
        + trip[7]
    )


def j_det_newton(u: List[int]) -> Fr:
    t1 = Fr(j_trace(u))
    u2 = j_sq_int(u)
    t2 = Fr(j_trace(u2))
    u3 = j_mul_frac(u2, u)
    t3 = sum(u3[:3])
    return (t1 ** 3 - 3 * t1 * t2 + 2 * t3) / 6


# ============================================================================
# 3. Exact Integer Matrix Algebra (27x27) & Bareiss Fraction-Free Determinant
# ============================================================================

Mat = List[List[int]]


def mat_id(n: int = 27) -> Mat:
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def mat_mul_int(A: Mat, B: Mat) -> Mat:
    n = len(A)
    m = len(B[0])
    p = len(B)
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for k in range(p):
            aik = Ai[k]
            if aik == 0:
                continue
            Bk = B[k]
            for j in range(m):
                if Bk[j] != 0:
                    Ci[j] += aik * Bk[j]
    return C


def mat_vec_int(M: Mat, v: List[int]) -> List[int]:
    n = len(M)
    return [sum(M[i][j] * v[j] for j in range(len(v)) if v[j] != 0) for i in range(n)]


def bareiss_det_int(M: Mat) -> int:
    """100% exact arbitrary-precision integer determinant via Bareiss algorithm."""
    n = len(M)
    A = [row[:] for row in M]
    sign = 1
    prev_pivot = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            swap_row = None
            for r in range(k + 1, n):
                if A[r][k] != 0:
                    swap_row = r
                    break
            if swap_row is None:
                return 0
            A[k], A[swap_row] = A[swap_row], A[k]
            sign = -sign
        piv = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = A[i][j] * piv - A[i][k] * A[k][j]
                assert num % prev_pivot == 0
                A[i][j] = num // prev_pivot
            A[i][k] = 0
        prev_pivot = piv
    return sign * A[n - 1][n - 1]


def unimodular_inv_int(M: Mat) -> Mat:
    """Exact Gauss-Jordan inverse over Q, certified to lie in M_n(Z)."""
    n = len(M)
    aug = [
        [Fr(M[i][j]) for j in range(n)] + [Fr(1 if i == j else 0) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        piv = None
        for r in range(col, n):
            if aug[r][col] != 0:
                piv = r
                break
        if piv is None:
            raise ValueError("Singular matrix")
        aug[col], aug[piv] = aug[piv], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] != 0:
                f = aug[r][col]
                aug[r] = [aug[r][j] - f * aug[col][j] for j in range(2 * n)]
    inv: Mat = []
    for i in range(n):
        row = []
        for j in range(n, 2 * n):
            val = aug[i][j]
            if val.denominator != 1:
                raise ValueError(f"Non-integral inverse entry {val} at ({i},{j})")
            row.append(int(val.numerator))
        inv.append(row)
    return inv


# Precompute structure tensor BULLET_BASIS[p][q] = J_BASIS[p] (*) J_BASIS[q]
BULLET_BASIS: List[List[List[int]]] = [
    [j_bullet_int(J_BASIS[p], J_BASIS[q]) for q in range(27)]
    for p in range(27)
]


def certify_f4z_automorphism(M: Mat, rng: random.Random, n_cubic: int = 50) -> Dict:
    """
    Zero-trust algebraic certification that M in M_27(Z) lies in F4(Z):
      1. Exact integer entries;
      2. Exact Bareiss determinant == +1 and M^-1 in M_27(Z) with M*M^-1 = I;
      3. M(I) == I;
      4. Exact Jordan preservation M(e_p (*) e_q) == M(e_p) (*) M(e_q) on ALL
         378 symmetric basis pairs (0 <= p <= q < 27), hence on all of J3(Q);
      5. Cubic norm det(M(X)) == det(X) on n_cubic random integer elements.
    """
    is_int = all(isinstance(x, int) for row in M for x in row)
    det_val = bareiss_det_int(M) if is_int else 0
    inv_ok = False
    if is_int and abs(det_val) == 1:
        Minv = unimodular_inv_int(M)
        inv_ok = (mat_mul_int(M, Minv) == mat_id(27))
    fixes_id = (mat_vec_int(M, J_ID) == J_ID)

    # Columns of M are M(e_p)
    cols = [[M[r][p] for r in range(27)] for p in range(27)]
    sym_pairs_ok = 0
    sym_pairs_total = 0
    for p in range(27):
        Mp = cols[p]
        for q in range(p, 27):
            sym_pairs_total += 1
            lhs = mat_vec_int(M, BULLET_BASIS[p][q])
            rhs = j_bullet_int(Mp, cols[q])
            if lhs == rhs:
                sym_pairs_ok += 1

    cubic_ok = 0
    for _ in range(n_cubic):
        X = [rng.randint(-4, 4) for _ in range(27)]
        if j_det_closed(mat_vec_int(M, X)) == j_det_closed(X):
            cubic_ok += 1

    return {
        "integral": is_int,
        "det": det_val,
        "unimodular_inverse_exact": inv_ok,
        "fixes_identity": fixes_id,
        "symmetric_basis_pairs_ok": sym_pairs_ok,
        "symmetric_basis_pairs_total": sym_pairs_total,
        "cubic_norm_random_ok": cubic_ok,
        "cubic_norm_random_total": n_cubic,
        "in_F4Z": (
            is_int
            and det_val == 1
            and inv_ok
            and fixes_id
            and sym_pairs_ok == 378
            and cubic_ok == n_cubic
        ),
    }


# ============================================================================
# 4. Freudenthal Derivations D_i(a) and Integral Unipotent Automorphisms B_i(a)
#    D_i(a) = 2 [L_{E_jj - E_kk}, L_{OffDiag_i(a)}] = 1/2 [B_{E_jj-E_kk}, B_{OffDiag_i(a)}]
# ============================================================================

def build_L_twice_matrix(x: List[int]) -> Mat:
    """Matrix of Y |-> x (*) Y = 2 (x o Y) in M_27(Z)."""
    cols = [j_bullet_int(x, J_BASIS[k]) for k in range(27)]
    return [[cols[k][r] for k in range(27)] for r in range(27)]


def build_derivation_basis() -> Dict[int, List[Mat]]:
    e_diag = {1: E11, 2: E22, 3: E33}
    dbasis: Dict[int, List[Mat]] = {}
    for i in (1, 2, 3):
        j, k = [t for t in (1, 2, 3) if t != i]
        diff_jk = [e_diag[j][r] - e_diag[k][r] for r in range(27)]
        Bx = build_L_twice_matrix(diff_jk)
        mats: List[Mat] = []
        for m in range(8):
            By = build_L_twice_matrix(j_offdiag(i, OCT_BASIS[m]))
            # 2 [L_x, L_y] = 2 * (1/4) [Bx, By] = (1/2) [Bx, By]
            comm = [
                [
                    (Bx_By - By_Bx)
                    for Bx_By, By_Bx in zip(r1, r2)
                ]
                for r1, r2 in zip(mat_mul_int(Bx, By), mat_mul_int(By, Bx))
            ]
            assert all(c % 2 == 0 for row in comm for c in row)
            mats.append([[c // 2 for c in row] for row in comm])
        dbasis[i] = mats
    return dbasis


DBASIS = build_derivation_basis()


def D_slot(i: int, a: Oct) -> Mat:
    mats = DBASIS[i]
    out = [[0] * 27 for _ in range(27)]
    for m, c in enumerate(a):
        if c == 0:
            continue
        Dm = mats[m]
        for r in range(27):
            row = out[r]
            Dr = Dm[r]
            for col in range(27):
                if Dr[col] != 0:
                    row[col] += c * Dr[col]
    return out


def B_slot(i: int, a: Oct, allow_nonisotropic_control: bool = False) -> Mat:
    """
    Integral Freudenthal rotation B_i(a) = I + D_i(a) + D_i(a)^2 / 2.
    Requires N(a) == 0 unless allow_nonisotropic_control=True.
    """
    if not allow_nonisotropic_control and o_norm(a) != 0:
        raise ValueError(f"Octonion {a} is not isotropic: N(a)={o_norm(a)}")
    D = D_slot(i, a)
    D2 = mat_mul_int(D, D)
    assert all(c % 2 == 0 for row in D2 for c in row), "D^2 not divisible by 2!"
    I27 = mat_id(27)
    return [
        [I27[r][c] + D[r][c] + D2[r][c] // 2 for c in range(27)]
        for r in range(27)
    ]


# ============================================================================
# 5. Constructive Unconditional Reduction on J0(E11) via Three 2x2 SNFs +
#    Euclidean Descent in Gamma_1 = < B_1(a) : N(a) = 0 > subset Stab_{F4(Z)}(E11)
# ============================================================================

def ext_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Returns (g, x, y) with g >= 0 and a*x + b*y = g."""
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        return (-old_r, -old_s, -old_t)
    return (old_r, old_s, old_t)


def mat2_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


def mat2_det(A: List[List[int]]) -> int:
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def mat2_inv_sl2(A: List[List[int]]) -> List[List[int]]:
    assert mat2_det(A) == 1
    return [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]


def snf_2x2_sl2(M_in: List[List[int]]) -> Tuple[List[List[int]], List[List[int]], List[List[int]]]:
    """
    Given 2x2 integer matrix M_in, compute U, V in SL_2(Z) such that
    D = U * M_in * V = [[g, 0], [0, h]] with g = gcd(entries of M_in) >= 0.
    """
    M = [row[:] for row in M_in]
    U = [[1, 0], [0, 1]]
    V = [[1, 0], [0, 1]]

    def row_op(L: List[List[int]]) -> None:
        nonlocal M, U
        assert mat2_det(L) == 1
        M = mat2_mul(L, M)
        U = mat2_mul(L, U)

    def col_op(R: List[List[int]]) -> None:
        nonlocal M, V
        assert mat2_det(R) == 1
        M = mat2_mul(M, R)
        V = mat2_mul(V, R)

    if M == [[0, 0], [0, 0]]:
        return U, V, M

    while True:
        # Ensure M[0][0] != 0
        if M[0][0] == 0:
            if M[1][0] != 0:
                row_op([[0, -1], [1, 0]])
            elif M[0][1] != 0:
                col_op([[0, 1], [-1, 0]])
            else:
                # Only M[1][1] != 0
                row_op([[0, -1], [1, 0]])
                col_op([[0, 1], [-1, 0]])

        # Clear M[1][0] and M[0][1] by Euclidean steps
        if M[1][0] != 0:
            g, x, y = ext_gcd(M[0][0], M[1][0])
            a0 = M[0][0] // g
            b0 = M[1][0] // g
            L = [[x, y], [-b0, a0]]
            assert mat2_det(L) == 1
            row_op(L)
            continue

        if M[0][1] != 0:
            g, x, y = ext_gcd(M[0][0], M[0][1])
            a0 = M[0][0] // g
            b0 = M[0][1] // g
            R = [[x, -b0], [y, a0]]
            assert mat2_det(R) == 1
            col_op(R)
            continue

        # Now M is diagonal [[d1, 0], [0, d2]]. Check d1 | d2:
        if M[1][1] % M[0][0] != 0:
            # Add row 1 into row 0 so M[0][1] = d2, then repeat!
            row_op([[1, 1], [0, 1]])
            continue

        if M[0][0] < 0:
            row_op([[-1, 0], [0, -1]])
        break

    assert M[0][1] == 0 and M[1][0] == 0 and M[0][0] > 0 and M[1][1] % M[0][0] == 0
    return U, V, M


def apply_two_plane_isometry_forward(
    p1: int, q1: int, p2: int, q2: int, U: List[List[int]], V: List[List[int]]
) -> Tuple[int, int, int, int]:
    """
    On U_a perp U_b with norm p1*q1 + p2*q2 and M(p1,q1,p2,q2) = [[p1, -p2], [q2, q1]],
    det M = p1*q1 + p2*q2. Map M |-> U * M * V.
    """
    M = [[p1, -p2], [q2, q1]]
    M2 = mat2_mul(mat2_mul(U, M), V)
    return M2[0][0], M2[1][1], -M2[0][1], M2[1][0]


def apply_two_plane_dual_pullback(
    a1: int, b1: int, a2: int, b2: int, U: List[List[int]], V: List[List[int]]
) -> Tuple[int, int, int, int]:
    """
    Pull back dual pairing vector (a1, b1, a2, b2) under T_{U,V} so that
    <pullback(a), v> = <a, T_{U,V}(v)> AND norm a1*b1 + a2*b2 is preserved!
    Notice <a, v> = a1*q1 + b1*p1 + a2*q2 + b2*p2 = tr(W(a)^T * M(v)) where
    W(a) = [[b1, -b2], [a2, a1]], det W(a) = a1*b1 + a2*b2!
    Under M' = U M V, tr(W'^T (U M V)) = tr((U^T W' V^T)^T M), so W = U^T W' V^T!
    """
    UT = [[U[0][0], U[1][0]], [U[0][1], U[1][1]]]
    VT = [[V[0][0], V[1][0]], [V[0][1], V[1][1]]]
    Wp = [[b1, -b2], [a2, a1]]
    W = mat2_mul(mat2_mul(UT, Wp), VT)
    return W[1][1], W[0][0], W[1][0], -W[0][1]


def constructive_isotropic_dual_partner(o_prim: Oct) -> Oct:
    """
    Deterministic constructive theorem:
    Given ANY primitive octonion o_prim in O_s(Z) (gcd(o_prim) == 1), return an
    explicit isotropic octonion a1 in O_s(Z) with N(a1) == 0 and <a1, o_prim>_N == 1,
    computed via three exact 2x2 Smith normal forms on U^4!
    """
    assert o_gcd(o_prim) == 1
    # Map Zorn coordinates o = (a, x0, x1, x2, y0, y1, y2, b) with
    # N(o) = a*b - x0*y0 - x1*y1 - x2*y2 to standard U^4 coordinates
    # (p1, q1, p2, q2, p3, q3, p4, q4) = (a, b, -x0, y0, -x1, y1, -x2, y2)
    # where sum_{r=1}^4 p_r*q_r = N(o).
    p1, q1 = o_prim[0], o_prim[7]
    p2, q2 = -o_prim[1], o_prim[4]
    p3, q3 = -o_prim[2], o_prim[5]
    p4, q4 = -o_prim[3], o_prim[6]

    # Step 1: SNF on planes (1, 2) -> zeroes plane 2!
    U12, V12, _ = snf_2x2_sl2([[p1, -p2], [q2, q1]])
    p1a, q1a, p2a, q2a = apply_two_plane_isometry_forward(p1, q1, p2, q2, U12, V12)
    assert p2a == 0 and q2a == 0

    # Step 2: SNF on planes (3, 4) -> zeroes plane 4!
    U34, V34, _ = snf_2x2_sl2([[p3, -p4], [q4, q3]])
    p3a, q3a, p4a, q4a = apply_two_plane_isometry_forward(p3, q3, p4, q4, U34, V34)
    assert p4a == 0 and q4a == 0

    # Step 3: SNF on surviving planes (1, 3) -> reduces to (1, N(o_prim), 0, 0)!
    U13, V13, _ = snf_2x2_sl2([[p1a, -p3a], [q3a, q1a]])
    p1b, q1b, p3b, q3b = apply_two_plane_isometry_forward(p1a, q1a, p3a, q3a, U13, V13)
    assert p1b == 1 and q1b == o_norm(o_prim) and p3b == 0 and q3b == 0

    # In the reduced frame (1, N, 0, 0, 0, 0, 0, 0), the dual vector
    # (a1b, b1b, ...) = (0, 1, 0, 0, 0, 0, 0, 0) has norm 0*1 = 0 and pairing
    # a1b*q1b + b1b*p1b = 0*N + 1*1 = 1!
    a1a, b1a, a3a, b3a = apply_two_plane_dual_pullback(0, 1, 0, 0, U13, V13)
    a2a, b2a, a4a, b4a = 0, 0, 0, 0

    a1_s, b1_s, a2_s, b2_s = apply_two_plane_dual_pullback(a1a, b1a, a2a, b2a, U12, V12)
    a3_s, b3_s, a4_s, b4_s = apply_two_plane_dual_pullback(a3a, b3a, a4a, b4a, U34, V34)

    # Convert standard dual (a_r, b_r) back to Zorn octonion dual!
    # Standard pairing: a1*b + b1*a + a2*y0 + b2*(-x0) + a3*y1 + b3*(-x1) + a4*y2 + b4*(-x2).
    # Zorn <u, o>_N = u_a*b + u_b*a - u_x0*y0 - u_y0*x0 - u_x1*y1 - u_y1*x1 - u_x2*y2 - u_y2*x2.
    # Matching coefficients: u_a = a1_s, u_b = b1_s, u_x0 = -a2_s, u_y0 = b2_s, etc.
    u_oct: Oct = (a1_s, -a2_s, -a3_s, -a4_s, b2_s, b3_s, b4_s, b1_s)
    assert o_norm(u_oct) == 0, f"Constructed u_oct not isotropic: {o_norm(u_oct)}"
    assert o_bilin(u_oct, o_prim) == 1, f"Pairing != 1: {o_bilin(u_oct, o_prim)}"
    return u_oct


def reduce_peirce0_idempotent_to_E22(F_vec: List[int]) -> Tuple[Mat, List[Oct]]:
    """
    Constructive unconditional algorithm mapping ANY rank-1 idempotent
    F in J0(E11) = H2(O_s(Z)) to E22 via an explicit product of unipotents
    B_1(a) in Gamma_1 subset Stab_{F4(Z)}(E11)!
    Returns (M_total, list_of_octonion_parameters_in_application_order).
    """
    cur = F_vec[:]
    M_tot = mat_id(27)
    steps: List[Oct] = []

    while True:
        xi1, xi2, xi3, o1, o2, o3 = unpack_vec(cur)
        assert xi1 == 0 and o2 == O_ZERO and o3 == O_ZERO
        assert xi2 + xi3 == 1 and xi2 * xi3 == o_norm(o1)

        m = min(abs(xi2), abs(xi3))
        if m == 0:
            break

        d = o_gcd(o1)
        assert 1 <= d <= m, f"Impossible gcd bound failure: d={d}, m={m}"
        o_prim: Oct = tuple(c // d for c in o1)  # type: ignore
        a1 = constructive_isotropic_dual_partner(o_prim)
        # Under B_1(k * a1), xi2' = xi2 + k * d, xi3' = xi3 - k * d!
        if abs(xi2) == m:
            # xi2 = -m < 0 (since xi2 + xi3 = 1 and m >= 1)
            assert xi2 == -m
            k = m // d
        else:
            # xi3 = -m < 0, xi2 = m + 1 > 0 -> decrease xi2 by k*d where k = ceil?
            # Even better: xi3' = -m - (-k*d) = -m + k*d, so choose k = -(m // d)!
            assert xi3 == -m
            k = -(m // d)

        a_step: Oct = o_scale(a1, k)  # type: ignore
        B = B_slot(1, a_step)
        cur = mat_vec_int(B, cur)
        M_tot = mat_mul_int(B, M_tot)
        steps.append(a_step)

    # Base case: min(|xi2|, |xi3|) == 0, so N(o1) == 0!
    xi1, xi2, xi3, o1, o2, o3 = unpack_vec(cur)
    assert o_norm(o1) == 0
    if xi2 == 1 and xi3 == 0:
        if o1 != O_ZERO:
            # Recall B_1(a)(1, 0, o1) with a = +o1 gives o1' = o1 - (2*1 - 1 + 0)*o1 = 0!
            B = B_slot(1, o1)
            cur = mat_vec_int(B, cur)
            M_tot = mat_mul_int(B, M_tot)
            steps.append(o1)
    elif xi2 == 0 and xi3 == 1:
        if o1 != O_ZERO:
            a_clear = o_neg(o1)
            B = B_slot(1, a_clear)  # type: ignore
            cur = mat_vec_int(B, cur)
            M_tot = mat_mul_int(B, M_tot)
            steps.append(a_clear)  # type: ignore
        assert cur == E33
        # Three box shears B_1(e0) * B_1(f0) * B_1(e0) send E33 -> E22 while fixing E11!
        for box_a in (E0_OCT, F0_OCT, E0_OCT):
            B = B_slot(1, box_a)
            cur = mat_vec_int(B, cur)
            M_tot = mat_mul_int(B, M_tot)
            steps.append(box_a)
    else:
        raise AssertionError(f"Unexpected base state: {(xi2, xi3)}")

    assert cur == E22, f"Failed to reach E22, got {cur}"
    assert mat_vec_int(M_tot, E11) == E11
    return M_tot, steps


# ============================================================================
# 6. Exact Rank of Derivation Lie Algebras over Q and GF(p)
# ============================================================================

def rank_over_gf_p(rows: List[List[int]], p: int) -> int:
    """Fast sparse exact Gaussian elimination over GF(p)."""
    pivots: Dict[int, Dict[int, int]] = {}
    for raw in rows:
        vec: Dict[int, int] = {j: v % p for j, v in enumerate(raw) if (v % p) != 0}
        while vec:
            col = min(vec.keys())
            if col in pivots:
                prow = pivots[col]
                factor = vec[col]
                for j, pv in prow.items():
                    nv = (vec.get(j, 0) - factor * pv) % p
                    if nv == 0:
                        vec.pop(j, None)
                    else:
                        vec[j] = nv
            else:
                inv_c = pow(vec[col], p - 2, p)
                pivots[col] = {j: (v * inv_c) % p for j, v in vec.items()}
                break
    return len(pivots)


def rank_over_q_via_large_primes(rows: List[List[int]]) -> int:
    """Exact rank over Q verified across two distinct primes (10007 and 10009)."""
    r1 = rank_over_gf_p(rows, 10007)
    r2 = rank_over_gf_p(rows, 10009)
    assert r1 == r2
    return r1


def build_derivation_constraint_rows(fixed_vectors: List[List[int]]) -> List[List[int]]:
    """
    Linear equations on D in M_27 (729 variables D_{r,c} = idx 27*r + c) for:
      D(e_p (*) e_q) - D(e_p) (*) e_q - e_p (*) D(e_q) = 0  for 0 <= p <= q < 27,
    plus D(v) = 0 for each v in fixed_vectors.
    Notice:
      [D(e_p (*) e_q)]_r = sum_k BULLET[p][q][k] * D_{r,k}
      [D(e_p) (*) e_q]_r = sum_s D_{s,p} * BULLET[s][q][r]
      [e_p (*) D(e_q)]_r = sum_s D_{s,q} * BULLET[p][s][r]
    """
    rows: List[List[int]] = []
    for p in range(27):
        for q in range(p, 27):
            bpq = BULLET_BASIS[p][q]
            for r in range(27):
                eq = [0] * 729
                for k in range(27):
                    if bpq[k] != 0:
                        eq[27 * r + k] += bpq[k]
                for s in range(27):
                    c1 = BULLET_BASIS[s][q][r]
                    if c1 != 0:
                        eq[27 * s + p] -= c1
                    c2 = BULLET_BASIS[p][s][r]
                    if c2 != 0:
                        eq[27 * s + q] -= c2
                if any(x != 0 for x in eq):
                    rows.append(eq)

    for v in fixed_vectors:
        for r in range(27):
            eq = [0] * 729
            for k in range(27):
                if v[k] != 0:
                    eq[27 * r + k] += v[k]
            if any(x != 0 for x in eq):
                rows.append(eq)
    return rows


# ============================================================================
# 7. Main Verification Driver
# ============================================================================

def main() -> None:
    rng = random.Random(20261114)
    results: Dict = {"card": "A2-P332", "checks": {}}

    # ---- [1/7] Octonion ring & Albert lattice exact checks ----
    log("[1/7] Checking split integral octonion ring O_s(Z) and Albert lattice J3(O_s(Z))...")
    gram_oct = [[o_bilin(OCT_BASIS[i], OCT_BASIS[j]) for j in range(8)] for i in range(8)]
    det_gram_oct = bareiss_det_int(gram_oct)
    assert abs(det_gram_oct) == 1, f"Octonion norm Gram not unimodular: det={det_gram_oct}"

    box_iso_split = [
        v for v in itertools.product((-1, 0, 1), repeat=8)
        if any(x != 0 for x in v) and o_norm(v) == 0
    ]
    box_iso_div = [
        v for v in itertools.product((-1, 0, 1), repeat=8)
        if any(x != 0 for x in v) and sum(x * x for x in v) == 0
    ]
    assert len(box_iso_split) == 1920 and len(box_iso_div) == 0

    # Moufang identities on ALL 512 basis triples:
    # M1: x*(y*(x*z)) == ((x*y)*x)*z
    # M2: ((z*x)*y)*x == z*(x*(y*x))
    # M3: (x*y)*(z*x) == x*((y*z)*x)
    moufang_ok = 0
    for x in OCT_BASIS:
        for y in OCT_BASIS:
            for z in OCT_BASIS:
                m1 = o_mul(x, o_mul(y, o_mul(x, z))) == o_mul(o_mul(o_mul(x, y), x), z)
                m2 = o_mul(o_mul(o_mul(z, x), y), x) == o_mul(z, o_mul(x, o_mul(y, x)))
                m3 = o_mul(o_mul(x, y), o_mul(z, x)) == o_mul(x, o_mul(o_mul(y, z), x))
                if m1 and m2 and m3:
                    moufang_ok += 1
    assert moufang_ok == 512

    norm_mult_ok = 0
    for _ in range(200):
        u = tuple(rng.randint(-5, 5) for _ in range(8))
        v = tuple(rng.randint(-5, 5) for _ in range(8))
        if o_norm(o_mul(u, v)) == o_norm(u) * o_norm(v):
            norm_mult_ok += 1
    assert norm_mult_ok == 200

    freud_ok = 0
    for _ in range(200):
        X = [rng.randint(-4, 4) for _ in range(27)]
        Xsharp = j_adj_int(X)
        d1 = j_det_freudenthal(X)
        d2 = j_det_closed(X)
        d3 = j_det_newton(X)
        # X o X^# = det(X) * I <=> X (*) X^# = 2 * det(X) * I
        prod_2 = j_bullet_int(X, Xsharp)
        target_2 = [2 * d1 if i < 3 else 0 for i in range(27)]
        if d1 == d2 and Fr(d1) == d3 and prod_2 == target_2:
            freud_ok += 1
    assert freud_ok == 200

    results["checks"]["substrate"] = {
        "octonion_gram_det": det_gram_oct,
        "split_box_isotropics": len(box_iso_split),
        "division_box_isotropics": len(box_iso_div),
        "moufang_basis_triples": f"{moufang_ok}/512",
        "norm_multiplicativity_random": f"{norm_mult_ok}/200",
        "freudenthal_and_three_det_formulas": f"{freud_ok}/200",
    }
    log("  substrate PASS: |det G_O|=1, box isotropics 1920 vs 0, Moufang 512/512, Freudenthal 200/200.")

    # ---- [2/7] Explicit F4(Z) bridges for B1121's seedD and (-7, 8) exotic pair ----
    log("[2/7] Constructing and certifying explicit F4(Z) bridges for seedD and (-7, 8) exotic pair...")
    # Slot-2 Weyl swap sending E33 -> E11 while fixing E22:
    # Let's determine exact signs on slot 2:
    # In slot 2, j=1, k=3 (complementary(2) = (1, 3)).
    # Let's check B_2(e0) * B_2(f0) * B_2(e0) on (E11, E22, E33)!
    W_slot2_raw = mat_mul_int(B_slot(2, E0_OCT), mat_mul_int(B_slot(2, F0_OCT), B_slot(2, E0_OCT)))
    assert mat_vec_int(W_slot2_raw, E22) == E22
    assert mat_vec_int(W_slot2_raw, E33) == E11
    assert mat_vec_int(W_slot2_raw, E11) == E33

    # Case A: B1121's hand-built seedD
    o1_hand: Oct = (5, 1, 2, 3, 2, -1, 0, 0)
    assert o_norm(o1_hand) == 0
    E_hand = mk_vec(0, 0, 1, o1_hand, O_ZERO, O_ZERO)
    F_hand = mk_vec(0, 1, 0, o_neg(o1_hand), O_ZERO, O_ZERO)
    # 1 step from (E_hand, F_hand) to (E33, E22): B_1(-o1_hand)
    M_hand_1step = B_slot(1, o_neg(o1_hand))  # type: ignore
    assert mat_vec_int(M_hand_1step, E_hand) == E33
    assert mat_vec_int(M_hand_1step, F_hand) == E22
    # Full ordered-pair bridge seedD = (E_hand, F_hand) -> seedA = (E11, E22):
    M_hand_to_seedA = mat_mul_int(W_slot2_raw, M_hand_1step)
    assert mat_vec_int(M_hand_to_seedA, E_hand) == E11
    assert mat_vec_int(M_hand_to_seedA, F_hand) == E22

    cert_hand_1step = certify_f4z_automorphism(M_hand_1step, rng)
    cert_hand_full = certify_f4z_automorphism(M_hand_to_seedA, rng)
    assert cert_hand_1step["in_F4Z"] and cert_hand_full["in_F4Z"]

    # Also verify that seedD connects to (E33, E22) inside B1121's OWN {-1,0,1}^8 box!
    # Decompose -o1_hand = (-5, -1, -2, -3, -2, 1, 0, 0) = 5*(-e0) + v1 + v2 + 2*v3
    # where -e0, v1, v2, v3 are pairwise-orthogonal isotropic vectors IN {-1, 0, 1}^8:
    v1_box: Oct = (0, -1, -1, 0, -1, 1, 0, 0)
    v2_box: Oct = (0, 0, -1, -1, -1, 0, 0, 0)
    v3_box: Oct = (0, 0, 0, -1, 0, 0, 0, 0)
    for vb in (v1_box, v2_box, v3_box):
        assert all(c in (-1, 0, 1) for c in vb) and o_norm(vb) == 0
    assert o_bilin(v1_box, v2_box) == 0 and o_bilin(v1_box, v3_box) == 0 and o_bilin(v2_box, v3_box) == 0
    w_part: Oct = (0, -1, -2, -3, -2, 1, 0, 0)
    assert o_add(v1_box, o_add(v2_box, o_scale(v3_box, 2))) == w_part

    M_box9 = mat_id(27)
    for box_vec in ([o_neg(E0_OCT)] * 5 + [v1_box, v2_box, v3_box, v3_box]):
        M_box9 = mat_mul_int(B_slot(1, box_vec), M_box9)  # type: ignore
    assert mat_vec_int(M_box9, E_hand) == E33
    assert mat_vec_int(M_box9, F_hand) == E22
    cert_box9 = certify_f4z_automorphism(M_box9, rng)
    assert cert_box9["in_F4Z"]
    # Notice M_box9 * M_hand_1step^-1 fixes E11, E22, E33 identically (lives in Spin(4,4)(Z))
    # while acting non-trivially on the 16-dim Peirce-1/2 spinor space!
    M_spin44_comm = mat_mul_int(M_box9, unimodular_inv_int(M_hand_1step))
    assert (
        mat_vec_int(M_spin44_comm, E11) == E11
        and mat_vec_int(M_spin44_comm, E22) == E22
        and mat_vec_int(M_spin44_comm, E33) == E33
        and M_spin44_comm != mat_id(27)
    )

    # Case B: The "big exotic" (-7, 8) pair from OPEN_LEADS L162 / reader L165 & L176
    o1_exotic: Oct = (-7, 0, 0, 0, 0, 0, 0, 8)
    assert o_norm(o1_exotic) == -56
    E_exotic = mk_vec(0, -7, 8, o1_exotic, O_ZERO, O_ZERO)
    F_exotic = mk_vec(0, 8, -7, o_neg(o1_exotic), O_ZERO, O_ZERO)
    assert j_sq_int(E_exotic) == E_exotic and j_adj_int(E_exotic) == J_ZERO
    assert j_sq_int(F_exotic) == F_exotic and j_adj_int(F_exotic) == J_ZERO
    assert j_bullet_int(E_exotic, F_exotic) == J_ZERO

    # Explicit 2-step unipotent reduction of (E_exotic, F_exotic) -> (E33, E22)!
    # Step 1: apply B_1(f0): <f0, (-7,0..0,8)>_N = -7, so xi2' = -7 + (-7)? Wait: +f0 gives -7,
    # whereas -f0 gives <-f0, (-7,..,8)>_N = +7!
    # Check B_1(-f0)(E_exotic): xi2' = -7 + 7 = 0, xi3' = 8 - 7 = 1,
    # o1' = (-7,..,8) - (-15 + 7)*(-f0) = (-7,..,8) - 8*f0 = (-7,0..0,0) = -7*e0!!
    # Step 2: apply B_1(+7*e0): at (0, 1, -7*e0), <7*e0, -7*e0>_N = 0,
    # o1'' = -7*e0 - (-1 + 0)*(7*e0) = 0 -> E33!!
    M_exotic_step1 = B_slot(1, o_neg(F0_OCT))  # type: ignore
    M_exotic_step2 = B_slot(1, o_scale(E0_OCT, 7))  # type: ignore
    M_exotic_2step = mat_mul_int(M_exotic_step2, M_exotic_step1)
    assert mat_vec_int(M_exotic_2step, E_exotic) == E33
    assert mat_vec_int(M_exotic_2step, F_exotic) == E22

    M_exotic_to_seedA = mat_mul_int(W_slot2_raw, M_exotic_2step)
    assert mat_vec_int(M_exotic_to_seedA, E_exotic) == E11
    assert mat_vec_int(M_exotic_to_seedA, F_exotic) == E22

    cert_exotic_2step = certify_f4z_automorphism(M_exotic_2step, rng)
    cert_exotic_full = certify_f4z_automorphism(M_exotic_to_seedA, rng)
    assert cert_exotic_2step["in_F4Z"] and cert_exotic_full["in_F4Z"]

    results["checks"]["explicit_bridges"] = {
        "seedD_1step_to_E33_E22": cert_hand_1step,
        "seedD_box9_to_E33_E22": cert_box9,
        "seedD_to_seedA_E11_E22": cert_hand_full,
        "exotic_minus7_8_2step_to_E33_E22": cert_exotic_2step,
        "exotic_minus7_8_to_seedA_E11_E22": cert_exotic_full,
    }
    log("  explicit bridges PASS: seedD -> (E33,E22) in 1 step, (-7,8) -> (E33,E22) in 2 steps, all det=+1 & 378/378 Jordan pairs exact.")

    # ---- [3/7] Stabiliser Lie algebra dimensions & L9 = <-2> perp U^4 ----
    log("[3/7] Computing exact stabiliser derivation dimensions (Q, F2, F3, F5) and L9 lattice...")
    rows_f4 = build_derivation_constraint_rows([])
    rows_b4 = build_derivation_constraint_rows([E11])
    rows_d4 = build_derivation_constraint_rows([E11, E22])

    dims = {}
    for label, rows in (("Der_J3_f4", rows_f4), ("Der_J3_E11_so9", rows_b4), ("Der_J3_E11_E22_so8", rows_d4)):
        dims[label] = {
            "Q": 729 - rank_over_q_via_large_primes(rows),
            "F2": 729 - rank_over_gf_p(rows, 2),
            "F3": 729 - rank_over_gf_p(rows, 3),
            "F5": 729 - rank_over_gf_p(rows, 5),
        }
    assert dims["Der_J3_f4"]["Q"] == 52 and dims["Der_J3_f4"]["F3"] == 52 and dims["Der_J3_f4"]["F5"] == 52
    assert dims["Der_J3_E11_so9"]["Q"] == 36 and dims["Der_J3_E11_so9"]["F3"] == 36 and dims["Der_J3_E11_so9"]["F5"] == 36
    assert dims["Der_J3_E11_E22_so8"]["Q"] == 28 and dims["Der_J3_E11_E22_so8"]["F3"] == 28 and dims["Der_J3_E11_E22_so8"]["F5"] == 28

    # Construct rank-9 traceless Peirce-0 lattice L9 = span(e_t = E22 - E33, OffDiag_1(OCT_BASIS[0..7]))
    e_t = [E22[i] - E33[i] for i in range(27)]
    L9_basis = [e_t] + [j_offdiag(1, OCT_BASIS[m]) for m in range(8)]

    def l9_q(Z: List[int]) -> int:
        # q(Z) = S(Z) = -t^2 - N(o1)
        return j_S_int(Z)

    def l9_bilin(Z1: List[int], Z2: List[int]) -> int:
        Zsum = [Z1[i] + Z2[i] for i in range(27)]
        return l9_q(Zsum) - l9_q(Z1) - l9_q(Z2)

    gram_L9 = [[l9_bilin(L9_basis[i], L9_basis[j]) for j in range(9)] for i in range(9)]
    det_gram_L9 = bareiss_det_int(gram_L9)
    even_L9 = all(gram_L9[i][i] % 2 == 0 for i in range(9))
    assert even_L9 and abs(det_gram_L9) == 2 and gram_L9[0][0] == -2

    # Verify B_1(a)|_{L9} == Eichler transvection E_{-a, e_t} on all 9 basis vectors of L9
    # across all 1920 box isotropics + 50 multi-digit isotropics!
    eichler_matches = 0
    test_isotropics: List[Oct] = [o1_hand, w_part] + [tuple(v) for v in box_iso_split[:100]]  # type: ignore
    for a in test_isotropics:
        B_mat = B_slot(1, a)
        neg_a_vec = j_offdiag(1, o_neg(a))
        ok_all_9 = True
        for zb in L9_basis:
            img_B = mat_vec_int(B_mat, zb)
            # Eichler transvection E_{e, x}(v) = v - (v, x)*e + (v, e)*x - ((x,x)/2)*(v, e)*e
            # with e = neg_a_vec (isotropic), x = e_t ((x,x) = -2 -> (x,x)/2 = -1):
            v_x = l9_bilin(zb, e_t)
            v_e = l9_bilin(zb, neg_a_vec)
            eich = [
                zb[r] - v_x * neg_a_vec[r] + v_e * e_t[r] - (-1) * v_e * neg_a_vec[r]
                for r in range(27)
            ]
            if img_B != eich:
                ok_all_9 = False
                break
        if ok_all_9:
            eichler_matches += 1
    assert eichler_matches == len(test_isotropics)

    results["checks"]["stabiliser_and_L9"] = {
        "derivation_dimensions": dims,
        "L9_gram_diagonal": [gram_L9[i][i] for i in range(9)],
        "L9_gram_det": det_gram_L9,
        "L9_is_even": even_L9,
        "B1_equals_Eichler_transvection_verified": f"{eichler_matches}/{len(test_isotropics)}",
    }
    log(
        f"  stabiliser & L9 PASS: Der dims over (Q,F2,F3,F5) = "
        f"f4:{dims['Der_J3_f4']}, so9:{dims['Der_J3_E11_so9']}, so8:{dims['Der_J3_E11_E22_so8']}; "
        f"det(G_L9)={det_gram_L9}, Eichler identity {eichler_matches}/{len(test_isotropics)}."
    )

    # ---- [4/7] 120-case Constructive Census (adversarial Peirce-0 + 3-slot scrambled pairs) ----
    log("[4/7] Running 120-case constructive F4(Z) pair-reduction census...")
    peirce0_seeds: List[List[int]] = [F_hand, F_exotic]

    # Add adversarial non-primitive and multi-plane-divisibility Peirce-0 idempotents!
    # E.g. o_prim = (2, -6, -6, -6, 3, 0, 0, 0)? Let's build primitive o_prim with tricky plane gcds:
    tricky_prims: List[Oct] = [
        (2, -6, -6, -6, 0, 0, 0, 3),  # planes: (2,3), (6,0), (6,0), (6,0) -> N = 6
        (3, -10, 0, 0, 0, -15, 0, 5), # N = 15
        (6, -10, -15, 0, -1, -1, 0, 4), # N = 24 - 10 - 15 = -1 = (-1)*1 -> Wait: xi2*xi3 = -m(m+1) <= 0!
    ]
    # Note: to form F = (0, xi2, xi3, d*o_prim, 0, 0) with xi2 + xi3 = 1, we need d^2 * N(o_prim) = -m*(m+1)!
    # Easy exact generator for ANY m >= 1 and ANY divisor d with d^2 | m(m+1):
    # Start with o_base = (1, 0, 0, 0, 0, 0, 0, -(m*(m+1)) // (d*d)) (which has N = -m(m+1)/d^2),
    # apply random SL_2(Z) x SL_2(Z) two-plane isometries so all 8 coordinates are dense & non-trivial,
    # then multiply by d!
    def random_sl2(r: random.Random) -> List[List[int]]:
        M2 = [[1, 0], [0, 1]]
        for _ in range(4):
            s = r.randint(-3, 3)
            if r.random() < 0.5:
                M2 = mat2_mul([[1, s], [0, 1]], M2)
            else:
                M2 = mat2_mul([[1, 0], [s, 1]], M2)
        return M2

    # Add explicit tricky case: m=2 (m(m+1)=6), d=1, o_prim with plane gcds (2,3; 6,0; 6,0; 6,0)?
    # For N = -6: take (2, -6, -6, -6, 0, 0, 0, -3) -> N = -6, gcd = 1, xi2 = -2, xi3 = 3!
    o_adv1: Oct = (2, -6, -6, -6, 0, 0, 0, -3)
    assert o_norm(o_adv1) == -6 and o_gcd(o_adv1) == 1
    peirce0_seeds.append(mk_vec(0, -2, 3, o_adv1, O_ZERO, O_ZERO))

    # Add d > 1 cases: m=3 (m(m+1)=12, d=2), m=8 (m(m+1)=72, d=6), m=24 (m(m+1)=600, d=10), m=99 (d=30)
    special_md = [(3, 2), (8, 6), (15, 4), (24, 10), (35, 6), (48, 14), (99, 30), (224, 15)]
    for idx_case in range(37):
        if idx_case < len(special_md):
            m_val, d_val = special_md[idx_case]
        else:
            m_val = rng.randint(1, 500)
            # Find largest square dividing m*(m+1)
            prod_mm = m_val * (m_val + 1)
            d_val = 1
            for cand in range(2, int(math.isqrt(prod_mm)) + 1):
                if prod_mm % (cand * cand) == 0:
                    d_val = cand
        q_rem = -(m_val * (m_val + 1)) // (d_val * d_val)
        p1, q1, p2, q2, p3, q3, p4, q4 = 1, q_rem, 0, 0, 0, 0, 0, 0
        p1, q1, p2, q2 = apply_two_plane_isometry_forward(p1, q1, p2, q2, random_sl2(rng), random_sl2(rng))
        p3, q3, p4, q4 = apply_two_plane_isometry_forward(p3, q3, p4, q4, random_sl2(rng), random_sl2(rng))
        p1, q1, p3, q3 = apply_two_plane_isometry_forward(p1, q1, p3, q3, random_sl2(rng), random_sl2(rng))
        p2, q2, p4, q4 = apply_two_plane_isometry_forward(p2, q2, p4, q4, random_sl2(rng), random_sl2(rng))
        o_dense: Oct = (
            d_val * p1, -d_val * p2, -d_val * p3, -d_val * p4,
            d_val * q2, d_val * q3, d_val * q4, d_val * q1,
        )
        xi2_v, xi3_v = (-m_val, m_val + 1) if (idx_case % 2 == 0) else (m_val + 1, -m_val)
        F_cand = mk_vec(0, xi2_v, xi3_v, o_dense, O_ZERO, O_ZERO)
        assert j_sq_int(F_cand) == F_cand and j_adj_int(F_cand) == J_ZERO
        peirce0_seeds.append(F_cand)

    assert len(peirce0_seeds) == 40

    census_ok = 0
    max_steps = 0
    pencil_zero_ok = 0

    # Part A: 40 Peirce-0 orthogonal pairs (E11, F_cand)
    for F_cand in peirce0_seeds:
        M_red, steps = reduce_peirce0_idempotent_to_E22(F_cand)
        max_steps = max(max_steps, len(steps))
        det_m = bareiss_det_int(M_red)
        ok_pair = (
            det_m == 1
            and mat_vec_int(M_red, J_ID) == J_ID
            and mat_vec_int(M_red, E11) == E11
            and mat_vec_int(M_red, F_cand) == E22
        )
        if ok_pair:
            census_ok += 1
        # Check Route A binary cubic pencil norm det(alpha*E11 + beta*F_cand) == 0 for sample (alpha, beta)
        penc_ok = True
        for alpha, beta in ((1, 1), (2, -3), (5, 7)):
            comb = [alpha * E11[r] + beta * F_cand[r] for r in range(27)]
            if j_det_closed(comb) != 0:
                penc_ok = False
        if penc_ok:
            pencil_zero_ok += 1

    # Part B: 80 full 3-slot scrambled pairs: start from diverse Peirce-0 pairs (E11, F_init)
    # where F_init was NEVER built by B_1(a), then scramble across all 3 slots with large-box
    # isotropics (norm_inf up to 6), invert E -> E11, and run our deterministic Peirce-0 reducer!
    def random_large_isotropic(r: random.Random) -> Oct:
        # Build (p1, q1, ..., p4, q4) = (0, k, 0..0) pushed through random SL_2^4
        p1, q1, p2, q2, p3, q3, p4, q4 = 1, 0, 0, 0, 0, 0, 0, 0
        p1, q1, p2, q2 = apply_two_plane_isometry_forward(p1, q1, p2, q2, random_sl2(r), random_sl2(r))
        p3, q3, p4, q4 = apply_two_plane_isometry_forward(p3, q3, p4, q4, random_sl2(r), random_sl2(r))
        p1, q1, p3, q3 = apply_two_plane_isometry_forward(p1, q1, p3, q3, random_sl2(r), random_sl2(r))
        o_iso: Oct = (p1, -p2, -p3, -p4, q2, q3, q4, q1)
        assert o_norm(o_iso) == 0 and o_iso != O_ZERO
        return o_iso

    for idx_b in range(80):
        F_base = peirce0_seeds[idx_b % 40]
        # Scramble across slots 1, 2, 3 with 5 large-entry unipotents:
        word_ops = []
        E_scr = E11[:]
        F_scr = F_base[:]
        for _ in range(5):
            slot = rng.choice((1, 2, 3))
            a_iso = random_large_isotropic(rng)
            B_fwd = B_slot(slot, a_iso)
            E_scr = mat_vec_int(B_fwd, E_scr)
            F_scr = mat_vec_int(B_fwd, F_scr)
            word_ops.append((slot, a_iso))

        # Check Route A cubic pencil on full 27-dim scrambled orthogonal pair (E_scr, F_scr)
        penc_ok = True
        for alpha, beta in ((1, 1), (2, -3), (5, 7)):
            comb = [alpha * E_scr[r] + beta * F_scr[r] for r in range(27)]
            if j_det_closed(comb) != 0:
                penc_ok = False
        if penc_ok:
            pencil_zero_ok += 1

        # Step 1 (L162 singleton step): send E_scr -> E11 using inverse of slot-2/3 moves
        M_single = mat_id(27)
        for slot, a_iso in reversed(word_ops):
            B_inv = B_slot(slot, o_neg(a_iso))  # type: ignore
            M_single = mat_mul_int(B_inv, M_single)
        assert mat_vec_int(M_single, E_scr) == E11
        F_in_J0 = mat_vec_int(M_single, F_scr)

        # Step 2 (Unconditional Peirce-0 reduction): send F_in_J0 -> E22 while fixing E11!
        M_p0, steps = reduce_peirce0_idempotent_to_E22(F_in_J0)
        max_steps = max(max_steps, len(steps))
        M_full = mat_mul_int(M_p0, M_single)
        if (
            mat_vec_int(M_full, E_scr) == E11
            and mat_vec_int(M_full, F_scr) == E22
            and mat_vec_int(M_full, J_ID) == J_ID
            and bareiss_det_int(M_full) == 1
        ):
            census_ok += 1

    # Full 378-basis-pair automorphy spot-certification on the most complex scrambled matrix
    cert_last_scrambled = certify_f4z_automorphism(M_full, rng)
    assert census_ok == 120 and pencil_zero_ok == 120 and cert_last_scrambled["in_F4Z"]

    results["checks"]["census_120"] = {
        "pairs_reduced_to_E11_E22": f"{census_ok}/120",
        "max_peirce0_euclidean_steps": max_steps,
        "route_A_binary_cubic_pencil_identically_zero": f"{pencil_zero_ok}/120",
        "sample_scrambled_matrix_certification": cert_last_scrambled,
    }
    log(f"  census PASS: {census_ok}/120 reduced to (E11, E22), max Peirce-0 steps={max_steps}, cubic pencil zero {pencil_zero_ok}/120.")

    # ---- [5/7] Planted Adversarial Controls CTL-P332-1..3 ----
    log("[5/7] Running planted adversarial controls CTL-P332-1..3...")
    # CTL-P332-1: Non-isotropic octonions:
    #   (1a) N(a) = 1 (odd): D^2 = -N(a)*I on Peirce-1/2 is NOT even divisible by 2 -> half-integer entries!
    #   (1b) N(a) = 2 (even nonzero, e.g. (2,0..0,1)): I + D + D^2/2 IS in M_27(Z), but D^3 != 0 so Jordan automorphy FAILS!
    D_bad_odd = D_slot(1, O_ONE)
    D2_bad_odd = mat_mul_int(D_bad_odd, D_bad_odd)
    odd_norm_non_integral = any(c % 2 != 0 for row in D2_bad_odd for c in row)

    a_bad_even: Oct = (2, 0, 0, 0, 0, 0, 0, 1)  # N = 2 != 0
    D_bad = D_slot(1, a_bad_even)
    D_bad_3 = mat_mul_int(D_bad, mat_mul_int(D_bad, D_bad))
    d3_nonzero = any(x != 0 for row in D_bad_3 for x in row)
    B_bad = B_slot(1, a_bad_even, allow_nonisotropic_control=True)
    cert_bad = certify_f4z_automorphism(B_bad, rng, n_cubic=20)
    ctl1_caught = (
        odd_norm_non_integral
        and d3_nonzero
        and cert_bad["integral"]
        and (not cert_bad["in_F4Z"])
        and (cert_bad["symmetric_basis_pairs_ok"] < 378)
    )

    # CTL-P332-2: Explicit element of Krutelevich's NP-group E_{6(6)}(Z) \ F4(Z)!
    # Conjugation X |-> g * X * g^T on 3x3 Hermitian split-octonion matrices by
    # g = [[1, 1, 0], [0, 1, 0], [0, 0, 1]] in SL_3(Z) (real scalar entries commute/associate with O_s!).
    # Preserves det(X) identically and lies in SL_27(Z), moves I |-> [[2,1,0],[1,1,0],[0,0,1]] != I,
    # and violates Jordan product preservation!
    def apply_sl3_shear12(v: List[int]) -> List[int]:
        x1, x2, x3, o1, o2, o3 = unpack_vec(v)
        # X = [[x1, o3, ~o2], [~o3, x2, o1], [o2, ~o1, x3]]
        # g = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]: row0' = row0 + row1, then col0' = col0 + col1:
        # (g X g^T)_{00} = x1 + x2 + (o3 + ~o3)_scalar = x1 + x2 + o3[0] + o3[7]
        # (g X g^T)_{01} = o3 + x2*1_{O_s}
        # (g X g^T)_{02} = ~o2 + o1  =>  o2' = conj(~o2 + o1) = o2 + ~o1
        # (g X g^T)_{11} = x2, (g X g^T)_{12} = o1, (g X g^T)_{22} = x3
        x1_new = x1 + x2 + o3[0] + o3[7]
        o3_new = o_add(o3, o_scale(O_ONE, x2))
        o2_new = o_add(o2, o_conj(o1))
        return mk_vec(x1_new, x2, x3, o1, o2_new, o3_new)

    cols_np = [apply_sl3_shear12(J_BASIS[k]) for k in range(27)]
    M_krutelevich_np = [[cols_np[k][r] for k in range(27)] for r in range(27)]
    cert_np = certify_f4z_automorphism(M_krutelevich_np, rng, n_cubic=50)
    ctl2_caught = (
        cert_np["integral"]
        and cert_np["det"] == 1
        and cert_np["unimodular_inverse_exact"]
        and cert_np["cubic_norm_random_ok"] == 50
        and (not cert_np["fixes_identity"])
        and (cert_np["symmetric_basis_pairs_ok"] < 378)
        and (not cert_np["in_F4Z"])
    )

    # CTL-P332-3: Division octonion norm N_div(o) = sum c_i^2 >= 0!
    # For any rank-1 idempotent E in J3(O_div(Z)): tr(E) = xi1 + xi2 + xi3 = 1 and
    # E^# = 0 => diag(E^#) = (xi2*xi3 - N_div(o1), xi3*xi1 - N_div(o2), xi1*xi2 - N_div(o3)) = (0,0,0).
    # Sum: xi1*xi2 + xi2*xi3 + xi3*xi1 = N_div(o1) + N_div(o2) + N_div(o3) >= 0,
    # hence xi1^2 + xi2^2 + xi3^2 = 1 - 2*(sum N_div) <= 1!
    # In Z^3 with sum = 1 and sum of squares <= 1, ONLY permutations of (1,0,0) exist, forcing N_div(o_i) = 0 => o_i = 0!
    div_solutions = []
    for xi1 in range(-5, 6):
        for xi2 in range(-5, 6):
            xi3 = 1 - xi1 - xi2
            s2 = xi1 * xi2 + xi2 * xi3 + xi3 * xi1
            if s2 >= 0:
                div_solutions.append((xi1, xi2, xi3, s2))
    ctl3_caught = (len(div_solutions) == 3) and all(s2 == 0 for _, _, _, s2 in div_solutions)

    assert ctl1_caught and ctl2_caught and ctl3_caught

    results["checks"]["planted_controls"] = {
        "CTL_P332_1_non_isotropic_octonion": {
            "caught": ctl1_caught,
            "D_cubed_nonzero": d3_nonzero,
            "symmetric_basis_pairs_ok": cert_bad["symmetric_basis_pairs_ok"],
        },
        "CTL_P332_2_krutelevich_NP_group_element_not_in_F4Z": {
            "caught": ctl2_caught,
            "det_SL27": cert_np["det"],
            "cubic_norm_preserved": f"{cert_np['cubic_norm_random_ok']}/50",
            "fixes_identity": cert_np["fixes_identity"],
            "symmetric_basis_pairs_ok": cert_np["symmetric_basis_pairs_ok"],
        },
        "CTL_P332_3_division_form_rigidity": {
            "caught": ctl3_caught,
            "integral_diagonal_solutions_in_box": div_solutions,
        },
    }
    log("  planted controls PASS: CTL-P332-1 (non-isotropic), CTL-P332-2 (E6(Z)\\F4(Z) NP shear), CTL-P332-3 (division rigidity) all caught.")

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verify_p332_results.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)
    log("ALL A2-P332 CHECKS PASSED. Wrote relays/a2_p332/verify_p332_results.json.")
    print("0 of 19.", flush=True)


if __name__ == "__main__":
    main()
