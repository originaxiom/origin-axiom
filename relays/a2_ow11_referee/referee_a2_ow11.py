"""Independent Cold-Room Zero-Trust Referee for AGY-002 Card A2-OW11 (+ Erratum 1).

Strictly disjoint verification methods constructed solely from:
  - relays/cards/AGY-002_A2-OW11_spin10-orbifold-uv-stitch-unification-and-dark-matter-collision.md
  - relays/cards/AGY-002_A2-OW11-ERRATUM-1_ps1013-slope-mechanism-clarification.md

Guardrails enforced:
  - 0 float/complex AST literals
  - 0 frontier/ imports (strict 0 of 19 empirical firewall)
  - 0 dict-literal boolean proof flags (every verdict computed directly)
  - Strictly disjoint algorithms:
      OW11-A: so(10) root system (5 Cartans + 40 roots) AND explicit 32x32 Cl(10)
              Jordan-Wigner Pauli tensor-product representation projected to 16x16
              positive-chirality 16_+ spinor generators Sigma_{ij} = (1/(4i))[Gamma_i, Gamma_j];
              exact projector traces for orbifold centralizers; direct 16x16 matrix
              multiplication (M^2, M^4, exact trace) for tr_16(F^2) and tr_16(F^4);
              exact 55-dps Chowla-Selberg E_3(tau) + Hessian for 6D Casimir stability.
      OW11-B: 55-dps d=4 harmonic-gauge Litim FRG solved via manual exact-QQ Sturm chain
              + Sturm-guided dyadic bisection + direct 55-dps 2D Newton-Raphson +
              4th-order Richardson FD Jacobian (ZERO polyroots/nroots/real_roots);
              exact sympy.Rational 1-loop beta functions computed directly from explicit
              real representation generator traces Tr_R(T_a^2)/6 (both 1x(1,2,2)_C
              matching N_S=(24,39,68) & SU(2)_L continuity AND diagnostic 2x(1,2,2)_C).
      OW11-C: Explicit 4x4 Walsh-Hadamard character matrix on E[2], {0}, E[2]\\{0};
              pure dimensionless prompt LKP decay rate; explicit Spin(10) Z_4 center
              matter parity P_M = (-1)^{3(B-L)} and c^2 = (-1)^{Q_X} on all 45 adjoint
              and 16 spinor states.
      OW11-D: Independent verification of all 4/4 planted faults PF-OW11-1..4.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp


# =============================================================================
# Exact Gaussian-Rational Matrix Arithmetic (ZERO floats, ZERO complex literals)
# Each entry is a tuple (re, im) of exact Fractions.
# =============================================================================

GZero = (Fraction(0, 1), Fraction(0, 1))
GOne = (Fraction(1, 1), Fraction(0, 1))
GMOne = (Fraction(-1, 1), Fraction(0, 1))
GI = (Fraction(0, 1), Fraction(1, 1))
GMI = (Fraction(0, 1), Fraction(-1, 1))


def g_add(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (a[0] + b[0], a[1] + b[1])


def g_sub(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (a[0] - b[0], a[1] - b[1])


def g_mul(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def g_conj(a: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (a[0], -a[1])


def g_scale(c: tuple[Fraction, Fraction], m: list[list[tuple[Fraction, Fraction]]]) -> list[list[tuple[Fraction, Fraction]]]:
    return [[g_mul(c, x) for x in row] for row in m]


def mat_zero(n: int) -> list[list[tuple[Fraction, Fraction]]]:
    return [[GZero for _ in range(n)] for _ in range(n)]


def mat_id(n: int) -> list[list[tuple[Fraction, Fraction]]]:
    return [[GOne if i == j else GZero for j in range(n)] for i in range(n)]


def mat_add(a: list[list[tuple[Fraction, Fraction]]], b: list[list[tuple[Fraction, Fraction]]]) -> list[list[tuple[Fraction, Fraction]]]:
    n = len(a)
    return [[g_add(a[i][j], b[i][j]) for j in range(n)] for i in range(n)]


def mat_sub(a: list[list[tuple[Fraction, Fraction]]], b: list[list[tuple[Fraction, Fraction]]]) -> list[list[tuple[Fraction, Fraction]]]:
    n = len(a)
    return [[g_sub(a[i][j], b[i][j]) for j in range(n)] for i in range(n)]


def mat_mul(a: list[list[tuple[Fraction, Fraction]]], b: list[list[tuple[Fraction, Fraction]]]) -> list[list[tuple[Fraction, Fraction]]]:
    n = len(a)
    # Exploit sparsity for fast exact 32x32 and 16x16 multiplies
    out = mat_zero(n)
    for i in range(n):
        row_a = a[i]
        row_nz = [(k, row_a[k]) for k in range(n) if row_a[k] != GZero]
        if not row_nz:
            continue
        for j in range(n):
            acc_r = Fraction(0, 1)
            acc_i = Fraction(0, 1)
            for k, av in row_nz:
                bv = b[k][j]
                if bv != GZero:
                    acc_r += av[0] * bv[0] - av[1] * bv[1]
                    acc_i += av[0] * bv[1] + av[1] * bv[0]
            out[i][j] = (acc_r, acc_i)
    return out


def mat_dagger(a: list[list[tuple[Fraction, Fraction]]]) -> list[list[tuple[Fraction, Fraction]]]:
    n = len(a)
    return [[g_conj(a[j][i]) for j in range(n)] for i in range(n)]


def mat_trace(a: list[list[tuple[Fraction, Fraction]]]) -> tuple[Fraction, Fraction]:
    acc_r = Fraction(0, 1)
    acc_i = Fraction(0, 1)
    for i in range(len(a)):
        acc_r += a[i][i][0]
        acc_i += a[i][i][1]
    return (acc_r, acc_i)


def mat_eq(a: list[list[tuple[Fraction, Fraction]]], b: list[list[tuple[Fraction, Fraction]]]) -> bool:
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] != b[i][j]:
                return False
    return True


def mat_kron(a: list[list[tuple[Fraction, Fraction]]], b: list[list[tuple[Fraction, Fraction]]]) -> list[list[tuple[Fraction, Fraction]]]:
    na, nb = len(a), len(b)
    out = mat_zero(na * nb)
    for ia in range(na):
        for ja in range(na):
            av = a[ia][ja]
            if av == GZero:
                continue
            for ib in range(nb):
                for jb in range(nb):
                    bv = b[ib][jb]
                    if bv != GZero:
                        out[ia * nb + ib][ja * nb + jb] = g_mul(av, bv)
    return out


def kron_list(mats: list[list[list[tuple[Fraction, Fraction]]]]) -> list[list[tuple[Fraction, Fraction]]]:
    res = mats[0]
    for m in mats[1:]:
        res = mat_kron(res, m)
    return res


def frac_str(f: Fraction | sp.Rational) -> str:
    if isinstance(f, Fraction):
        return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else str(f.numerator)
    r = sp.Rational(f)
    return f"{r.p}/{r.q}" if r.q != 1 else str(r.p)


# =============================================================================
# OW11-A: so(10) Root System + Explicit 32x32 Cl(10) -> 16x16 16_+ Spinor
#         + 6D I_8 Anomaly + 6D Bulk Supertraces & Chowla-Selberg E_3(tau)
# =============================================================================

def build_cl10_and_16plus() -> dict[str, Any]:
    """Build explicit 32x32 Cl(10) Jordan-Wigner Gammas and 16x16 16_+ Sigma_{ab}."""
    pauli_i = [[GOne, GZero], [GZero, GOne]]
    pauli_x = [[GZero, GOne], [GOne, GZero]]
    pauli_y = [[GZero, GMI], [GI, GZero]]
    pauli_z = [[GOne, GZero], [GZero, GMOne]]

    gammas: list[list[list[tuple[Fraction, Fraction]]]] = []
    for k in range(5):
        factors_x = [pauli_z] * k + [pauli_x] + [pauli_i] * (4 - k)
        factors_y = [pauli_z] * k + [pauli_y] + [pauli_i] * (4 - k)
        gammas.append(kron_list(factors_x))
        gammas.append(kron_list(factors_y))

    # Verify Clifford algebra {Gamma_a, Gamma_b} = 2 delta_{ab} I_32
    id32 = mat_id(32)
    two_id32 = g_scale((Fraction(2, 1), Fraction(0, 1)), id32)
    zero32 = mat_zero(32)
    clifford_ok = True
    for a in range(10):
        for b in range(a, 10):
            anticomm = mat_add(mat_mul(gammas[a], gammas[b]), mat_mul(gammas[b], gammas[a]))
            target = two_id32 if a == b else zero32
            if not mat_eq(anticomm, target):
                clifford_ok = False

    # Chirality Gamma_11 = (-i)^5 Gamma_1 ... Gamma_10 = (-i) Gamma_1 ... Gamma_10
    prod_g = mat_id(32)
    for g in gammas:
        prod_g = mat_mul(prod_g, g)
    # (-i)^5 = -i
    gamma11 = g_scale(GMI, prod_g)

    # Verify Gamma_11 is diagonal with 16 (+1) and 16 (-1) states
    pos_indices = [idx for idx in range(32) if gamma11[idx][idx] == GOne]
    neg_indices = [idx for idx in range(32) if gamma11[idx][idx] == GMOne]
    gamma11_diag_ok = (len(pos_indices) == 16) and (len(neg_indices) == 16)
    for i in range(32):
        for j in range(32):
            if i != j and gamma11[i][j] != GZero:
                gamma11_diag_ok = False

    # Build 45 generators Sigma_{ab} = (1 / (4i)) [Gamma_a, Gamma_b] projected to 16_+
    # Note 1 / (4i) = -i / 4
    inv_4i = (Fraction(0, 1), Fraction(-1, 4))
    pairs: list[tuple[int, int]] = []
    sigmas16: dict[tuple[int, int], list[list[tuple[Fraction, Fraction]]]] = {}
    hermitian_ok = True
    commutes_g11_ok = True
    for a in range(10):
        for b in range(a + 1, 10):
            pairs.append((a, b))
            comm = mat_sub(mat_mul(gammas[a], gammas[b]), mat_mul(gammas[b], gammas[a]))
            sig32 = g_scale(inv_4i, comm)
            # Check [sig32, gamma11] = 0 directly on off-diagonal chirality blocks
            for p_idx in pos_indices:
                for n_idx in neg_indices:
                    if sig32[p_idx][n_idx] != GZero or sig32[n_idx][p_idx] != GZero:
                        commutes_g11_ok = False
            sig16 = [[sig32[i][j] for j in pos_indices] for i in pos_indices]
            if not mat_eq(sig16, mat_dagger(sig16)):
                hermitian_ok = False
            sigmas16[(a, b)] = sig16

    # Verify so(10) Lie-algebra commutation relation [Sigma_{ab}, Sigma_{bc}] = -i Sigma_{ac}
    # for all distinct triples (a < b < c)
    lie_bracket_ok = True
    for a in range(10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                lhs = mat_sub(
                    mat_mul(sigmas16[(a, b)], sigmas16[(b, c)]),
                    mat_mul(sigmas16[(b, c)], sigmas16[(a, b)]),
                )
                rhs = g_scale(GMI, sigmas16[(a, c)])
                if not mat_eq(lhs, rhs):
                    lie_bracket_ok = False

    # Verify orthogonality & Dynkin normalization tr_16(Sigma_{ab} Sigma_{cd}) = 4 delta_{ac} delta_{bd}
    # Compare with vector 10: (T_{ab}^{vec})_{mn} = -i (delta_{am} delta_{bn} - delta_{an} delta_{bm})
    # which has tr_10(T_{ab}^2) = 2, so tr_16 / tr_10 = 4 / 2 = 2!
    ortho_ok = True
    for idx1, p1 in enumerate(pairs):
        for idx2, p2 in enumerate(pairs):
            tr_val = mat_trace(mat_mul(sigmas16[p1], sigmas16[p2]))
            expected = (Fraction(4, 1), Fraction(0, 1)) if idx1 == idx2 else GZero
            if tr_val != expected:
                ortho_ok = False

    return {
        "gammas": gammas,
        "gamma11": gamma11,
        "pos_indices": pos_indices,
        "pairs": pairs,
        "sigmas16": sigmas16,
        "clifford_ok": clifford_ok,
        "gamma11_diag_ok": gamma11_diag_ok,
        "hermitian_ok": hermitian_ok,
        "commutes_g11_ok": commutes_g11_ok,
        "lie_bracket_ok": lie_bracket_ok,
        "ortho_ok": ortho_ok,
    }


def compute_ow11_a(cl: dict[str, Any]) -> dict[str, Any]:
    """Run OW11-A via disjoint root system + 16x16 Cl(10) spinor algebra + Chowla-Selberg E_3."""
    gammas = cl["gammas"]
    pos_indices = cl["pos_indices"]
    pairs = cl["pairs"]
    sigmas16 = cl["sigmas16"]

    # -------------------------------------------------------------------------
    # A1a. Disjoint Method 1: so(10) Root System (5 Cartans + 40 roots +-e_i +- e_j)
    # -------------------------------------------------------------------------
    # Parity vector p_k for P_PS = diag(+1^6, -1^4): +1 on 2-planes 0,1,2; -1 on 2-planes 3,4
    p_ps_planes = [1, 1, 1, -1, -1]
    roots: list[tuple[int, int, int, int]] = []  # (i, j, si, sj) representing si*e_i + sj*e_j
    for i in range(5):
        for j in range(i + 1, 5):
            for si in (-1, 1):
                for sj in (-1, 1):
                    roots.append((i, j, si, sj))

    # Action of P_PS: eigenvalue on root (i, j, si, sj) is p_i * p_j; +1 on all 5 Cartans
    ps_even_roots = [r for r in roots if p_ps_planes[r[0]] * p_ps_planes[r[1]] == 1]
    ps_odd_roots = [r for r in roots if p_ps_planes[r[0]] * p_ps_planes[r[1]] == -1]
    dim_c_ps_root = 5 + len(ps_even_roots)

    # Action of J_5 (Q_X = sum H_k): eigenvalue of ad(Q_X) on root is si + sj; commutes iff si + sj == 0
    j5_even_roots = [r for r in roots if r[2] + r[3] == 0]
    dim_c_j5_root = 5 + len(j5_even_roots)

    # Simultaneous centralizer C(P_PS, J_5)
    both_even_roots = [
        r for r in roots if (p_ps_planes[r[0]] * p_ps_planes[r[1]] == 1) and (r[2] + r[3] == 0)
    ]
    dim_c_both_root = 5 + len(both_even_roots)

    # Check Lie-bracket closure of surviving root subsets:
    # Two roots alpha, beta have alpha + beta in roots iff alpha . beta == -1
    def root_vec(r: tuple[int, int, int, int]) -> tuple[int, ...]:
        v = [0, 0, 0, 0, 0]
        v[r[0]] = r[2]
        v[r[1]] = r[3]
        return tuple(v)

    all_root_vecs = {root_vec(r) for r in roots}

    def is_root_subset_closed(sub: list[tuple[int, int, int, int]]) -> bool:
        svecs = {root_vec(r) for r in sub}
        for a in svecs:
            for b in svecs:
                s = tuple(a[k] + b[k] for k in range(5))
                if s in all_root_vecs and s not in svecs:
                    return False
        return True

    closures_ok = (
        is_root_subset_closed(ps_even_roots)
        and is_root_subset_closed(j5_even_roots)
        and is_root_subset_closed(both_even_roots)
    )

    # Sub-decomposition of G_SM + U(1)_X and 33 broken Proca vectors = 24 + 8 + 1
    su3_roots = [r for r in both_even_roots if r[0] < 3 and r[1] < 3]
    su2L_roots = [r for r in both_even_roots if r[0] >= 3 and r[1] >= 3]
    # 5 Cartans: 2 in su(3)_C, 1 in su(2)_L, 1 in u(1)_Y, 1 in u(1)_X (broken at M_R)
    dim_g_sm_root = len(su3_roots) + 2 + len(su2L_roots) + 1 + 1
    n_broken_ps_coset = len(ps_odd_roots)  # 24
    n_broken_ps_to_smx = len(ps_even_roots) - len(both_even_roots)  # 8 (6 leptoquarks + 2 W_R)
    n_broken_u1x = dim_c_both_root - dim_g_sm_root  # 1
    n_broken_proca_root = n_broken_ps_coset + n_broken_ps_to_smx + n_broken_u1x

    # -------------------------------------------------------------------------
    # A1b. Disjoint Method 2: Explicit 16x16 Cl(10) Spinor Lifts & Projector Traces
    # -------------------------------------------------------------------------
    # Lift P_PS = diag(+1^6, -1^4) to S_PS = Gamma_7 Gamma_8 Gamma_9 Gamma_10 on 16_+
    # (S_PS^2 = +I_16 since (G7 G8)^2 = -I, (G9 G10)^2 = -I, they commute -> (-1)(-1) = +1)
    s_ps_32 = mat_mul(mat_mul(gammas[6], gammas[7]), mat_mul(gammas[8], gammas[9]))
    s_ps_16 = [[s_ps_32[i][j] for j in pos_indices] for i in pos_indices]
    s_ps_sq_ok = mat_eq(mat_mul(s_ps_16, s_ps_16), mat_id(16))

    # Lift J_5 = diag([[0,-1],[1,0]] x 5) to unnormalized S_J5 = prod_{k=0..4} (I - Gamma_{2k} Gamma_{2k+1})
    # Note (I - G_{2k} G_{2k+1}) (I + G_{2k} G_{2k+1}) = I - (-I) = 2 I, so S_J5 * S_J5^dagger = 32 I_32!
    id32 = mat_id(32)
    s_j5_32 = mat_id(32)
    for k in range(5):
        fac = mat_sub(id32, mat_mul(gammas[2 * k], gammas[2 * k + 1]))
        s_j5_32 = mat_mul(s_j5_32, fac)
    s_j5_16 = [[s_j5_32[i][j] for j in pos_indices] for i in pos_indices]
    s_j5_16_dag = mat_dagger(s_j5_16)
    s_j5_unitary_ok = mat_eq(
        mat_mul(s_j5_16, s_j5_16_dag),
        g_scale((Fraction(32, 1), Fraction(0, 1)), mat_id(16)),
    )
    # Check spinor lifts commute on 16_+ (equivalently P_PS J_5 == J_5 P_PS)
    lifts_commute_ok = mat_eq(mat_mul(s_ps_16, s_j5_16), mat_mul(s_j5_16, s_ps_16))

    # Compute exact 45x45 adjoint conjugation matrices A_PS and A_J5 directly via 16x16 traces:
    #   (A)_{cd, ab} = (1/4) tr_16( Sigma_{cd} * S * Sigma_{ab} * S^{-1} )
    inv_4 = Fraction(1, 4)
    inv_32 = (Fraction(1, 32), Fraction(0, 1))
    s_j5_16_inv = g_scale(inv_32, s_j5_16_dag)

    a_ps = [[Fraction(0, 1) for _ in range(45)] for _ in range(45)]
    a_j5 = [[Fraction(0, 1) for _ in range(45)] for _ in range(45)]
    adj_real_ok = True

    for idx_ab, p_ab in enumerate(pairs):
        sig = sigmas16[p_ab]
        conj_ps = mat_mul(mat_mul(s_ps_16, sig), s_ps_16)
        conj_j5 = mat_mul(mat_mul(s_j5_16, sig), s_j5_16_inv)
        for idx_cd, p_cd in enumerate(pairs):
            sig_cd = sigmas16[p_cd]
            t_ps = mat_trace(mat_mul(sig_cd, conj_ps))
            t_j5 = mat_trace(mat_mul(sig_cd, conj_j5))
            if t_ps[1] != 0 or t_j5[1] != 0:
                adj_real_ok = False
            a_ps[idx_cd][idx_ab] = t_ps[0] * inv_4
            a_j5[idx_cd][idx_ab] = t_j5[0] * inv_4

    # Verify A_PS^2 = I_45, A_J5^2 = I_45 (since J_5^2 = -I_10 acts trivially on adjoint), [A_PS, A_J5] = 0
    m_aps = sp.Matrix(a_ps)
    m_aj5 = sp.Matrix(a_j5)
    id45 = sp.eye(45)
    aps_invol_ok = (m_aps * m_aps == id45)
    aj5_invol_ok = (m_aj5 * m_aj5 == id45)
    adj_comm_ok = (m_aps * m_aj5 == m_aj5 * m_aps)

    # Exact centralizer dimensions via projector traces (ZERO Gaussian elimination!)
    proj_ps = (id45 + m_aps) * sp.Rational(1, 2)
    proj_j5 = (id45 + m_aj5) * sp.Rational(1, 2)
    proj_both = proj_ps * proj_j5
    dim_c_ps_spin = int(proj_ps.trace())
    dim_c_j5_spin = int(proj_j5.trace())
    dim_c_both_spin = int(proj_both.trace())

    # Vector 10 doublet-triplet split under -P_PS = diag(-1^6, +1^4)
    p_ps_10 = sp.diag(1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
    j5_block = sp.Matrix([[0, -1], [1, 0]])
    j5_10 = sp.diag(j5_block, j5_block, j5_block, j5_block, j5_block)
    vec10_ops_ok = (p_ps_10 * j5_10 == j5_10 * p_ps_10) and (j5_10 * j5_10 == -sp.eye(10))
    proj_2h = (sp.eye(10) - p_ps_10) * sp.Rational(1, 2)
    proj_trip = (sp.eye(10) + p_ps_10) * sp.Rational(1, 2)
    dt_even_2h = int(proj_2h.trace())
    dt_odd_triplets = int(proj_trip.trace())

    # -------------------------------------------------------------------------
    # A2. Direct 16x16 Matrix Multiplication for tr_16(F^2) & tr_16(F^4) -> 6D I_8
    # -------------------------------------------------------------------------
    # Build the 5 Cartan 16x16 matrices H_k = Sigma_{2k, 2k+1} and vector-10 Cartan matrices
    cartans16 = [sigmas16[(2 * k, 2 * k + 1)] for k in range(5)]

    def build_vec10_gen(a: int, b: int) -> list[list[tuple[Fraction, Fraction]]]:
        m = mat_zero(10)
        # (T_{ab}^{vec})_{ab} = -i, (T_{ab}^{vec})_{ba} = +i (Hermitian, eigenvalues +-1)
        m[a][b] = GMI
        m[b][a] = GI
        return m

    cartan_tests = [
        (1, 0, 0, 0, 0),
        (1, 1, 0, 0, 0),
        (1, 1, 1, 0, 0),
        (1, 2, 3, 4, 5),
    ]

    trace_records = []
    for vec in cartan_tests:
        # Build explicit 16x16 M16 and 10x10 M10
        m16 = mat_zero(16)
        m10 = mat_zero(10)
        for k, coeff in enumerate(vec):
            if coeff != 0:
                c = (Fraction(coeff, 1), Fraction(0, 1))
                m16 = mat_add(m16, g_scale(c, cartans16[k]))
                m10 = mat_add(m10, g_scale(c, build_vec10_gen(2 * k, 2 * k + 1)))
        m16_2 = mat_mul(m16, m16)
        m16_4 = mat_mul(m16_2, m16_2)
        m10_2 = mat_mul(m10, m10)
        m10_4 = mat_mul(m10_2, m10_2)

        t16_2 = mat_trace(m16_2)
        t16_4 = mat_trace(m16_4)
        t10_2 = mat_trace(m10_2)
        t10_4 = mat_trace(m10_4)

        trace_records.append({
            "cartan": list(vec),
            "tr10_F2": frac_str(t10_2[0]),
            "tr16_F2": frac_str(t16_2[0]),
            "tr10_F4": frac_str(t10_4[0]),
            "tr16_F4": frac_str(t16_4[0]),
            "imag_zero": (t16_2[1] == 0 and t16_4[1] == 0 and t10_2[1] == 0 and t10_4[1] == 0),
            "f2_ratio_exact": (t16_2[0] == Fraction(2, 1) * t10_2[0]),
            "f4_identity_exact": (
                t16_4[0] == -t10_4[0] + Fraction(3, 4) * t10_2[0] * t10_2[0]
            ),
            "_num": (t10_2[0], t10_4[0], t16_2[0], t16_4[0]),
        })

    # Solve linear system A * tr10(F^4) + B * (tr10(F^2))^2 = tr16(F^4) from first two independent vectors
    r0 = trace_records[0]["_num"]
    r1 = trace_records[1]["_num"]
    mat_lin = sp.Matrix([
        [sp.Rational(r0[1]), sp.Rational(r0[0] ** 2)],
        [sp.Rational(r1[1]), sp.Rational(r1[0] ** 2)],
    ])
    rhs_lin = sp.Matrix([sp.Rational(r0[3]), sp.Rational(r1[3])])
    sol_ab = mat_lin.LUsolve(rhs_lin)
    coeff_a = Fraction(int(sol_ab[0].p), int(sol_ab[0].q))
    coeff_b = Fraction(int(sol_ab[1].p), int(sol_ab[1].q))

    # Also test a genuinely NON-CARTAN (off-diagonal root-mixed) so(10) matrix F16 & F10
    # AND apply an exact orthogonal/unitary basis scramble U M16 U^dagger (Guardrail 3)
    non_cartan_spec = [((0, 1), 1), ((1, 2), 2), ((3, 6), -1), ((4, 9), 1), ((7, 8), 3)]
    nc16 = mat_zero(16)
    nc10 = mat_zero(10)
    for (a_i, b_i), coeff in non_cartan_spec:
        c = (Fraction(coeff, 1), Fraction(0, 1))
        nc16 = mat_add(nc16, g_scale(c, sigmas16[(a_i, b_i)]))
        nc10 = mat_add(nc10, g_scale(c, build_vec10_gen(a_i, b_i)))
    # Exact unitary basis scramble U on 16_+ using Cayley/Hadamard block (3/5, 4/5) + cyclic shift
    u_scr = mat_zero(16)
    c35 = (Fraction(3, 5), Fraction(0, 1))
    c45 = (Fraction(4, 5), Fraction(0, 1))
    cm45 = (Fraction(-4, 5), Fraction(0, 1))
    for blk in range(8):
        i0, i1 = (2 * blk + 1) % 16, (2 * blk + 2) % 16
        u_scr[i0][2 * blk] = c35
        u_scr[i0][2 * blk + 1] = c45
        u_scr[i1][2 * blk] = cm45
        u_scr[i1][2 * blk + 1] = c35
    u_scr_dag = mat_dagger(u_scr)
    u_scr_unitary_ok = mat_eq(mat_mul(u_scr, u_scr_dag), mat_id(16))
    nc16_scr = mat_mul(mat_mul(u_scr, nc16), u_scr_dag)

    nc16_2 = mat_mul(nc16_scr, nc16_scr)
    nc16_4 = mat_mul(nc16_2, nc16_2)
    nc10_2 = mat_mul(nc10, nc10)
    nc10_4 = mat_mul(nc10_2, nc10_2)
    nc_t16_2 = mat_trace(nc16_2)
    nc_t16_4 = mat_trace(nc16_4)
    nc_t10_2 = mat_trace(nc10_2)
    nc_t10_4 = mat_trace(nc10_4)
    non_cartan_ok = (
        u_scr_unitary_ok
        and nc_t16_2[1] == 0
        and nc_t16_4[1] == 0
        and nc_t16_2[0] == Fraction(2, 1) * nc_t10_2[0]
        and nc_t16_4[0] == coeff_a * nc_t10_4[0] + coeff_b * nc_t10_2[0] * nc_t10_2[0]
    )

    # Strip private _num helper before JSON output
    for rec in trace_records:
        del rec["_num"]

    # 6D I_8 anomaly polynomial for 3 x 16_+ (48 6D positive-chirality Weyl fermions)
    # I_8 = [A_hat(R) ch(F)]_8 = 3 * [tr_16(F^4)/24 - (1/48) tr(R^2) tr_16(F^2) + 16*(tr(R^4)/5760 + (tr R^2)^2/4608)]
    n_gen = 3
    n_weyl_6d = n_gen * 16
    c_tr10_f4 = Fraction(n_gen, 24) * coeff_a
    c_tr10_f2_sq = Fraction(n_gen, 24) * coeff_b
    c_tr_r4 = Fraction(n_weyl_6d, 5760)
    c_tr_r2_sq = Fraction(n_weyl_6d, 4608)
    c_tr_r2_tr10_f2 = Fraction(-n_gen, 48) * Fraction(2, 1)

    # Directly verify 0 mixed U(1) anomaly from explicit 16x16 matrices:
    # Every generator Sigma_{ab} is traceless, and Q_Y, Q_X have tr(Q)=0, tr(Q^3)=0, tr(Q Sigma^2)=0
    max_abs_tr_gen = max(
        max(abs(mat_trace(sigmas16[p])[0]), abs(mat_trace(sigmas16[p])[1])) for p in pairs
    )
    # Q_X = 2 sum_{k=0..4} H_k, Q_Y = (1/3)(H_0+H_1+H_2) - (1/2)(H_3+H_4)
    q_x16 = mat_zero(16)
    q_y16 = mat_zero(16)
    for k in range(5):
        q_x16 = mat_add(q_x16, g_scale((Fraction(2, 1), Fraction(0, 1)), cartans16[k]))
        wy = Fraction(1, 3) if k < 3 else Fraction(-1, 2)
        q_y16 = mat_add(q_y16, g_scale((wy, Fraction(0, 1)), cartans16[k]))

    tr_qy = mat_trace(q_y16)
    tr_qx = mat_trace(q_x16)
    tr_qy3 = mat_trace(mat_mul(mat_mul(q_y16, q_y16), q_y16))
    tr_qx3 = mat_trace(mat_mul(mat_mul(q_x16, q_x16), q_x16))
    # Mixed U(1)_Y - G^2 traces over all 12 SM generators (Cartan + roots -> check all 45!)
    max_mixed_qy_g2 = Fraction(0, 1)
    for p in pairs:
        sig = sigmas16[p]
        val = mat_trace(mat_mul(q_y16, mat_mul(sig, sig)))
        max_mixed_qy_g2 = max(max_mixed_qy_g2, abs(val[0]), abs(val[1]))

    mixed_u1_zero = (
        max_abs_tr_gen == 0
        and tr_qy == GZero
        and tr_qx == GZero
        and tr_qy3 == GZero
        and tr_qx3 == GZero
        and max_mixed_qy_g2 == 0
    )

    # -------------------------------------------------------------------------
    # A3. 6D Bulk Spin(10) Supertraces & 55-dps Chowla-Selberg E_3(tau) Stability
    # -------------------------------------------------------------------------
    mp.mp.dps = 55

    def e3_chowla_selberg(tau1: mp.mpf, tau2: mp.mpf, n_max: int = 25) -> mp.mpf:
        half = mp.mpf(1) / mp.mpf(2)
        five_halves = mp.mpf(5) / mp.mpf(2)
        t0 = mp.zeta(6) * (tau2 ** 3)
        t1 = mp.sqrt(mp.pi) * mp.gamma(five_halves) / mp.gamma(3) * mp.zeta(5) * (tau2 ** (-2))
        pref = mp.mpf(2) * (mp.pi ** 3) * mp.sqrt(tau2) / mp.gamma(3)
        acc = mp.mpf(0)
        two_pi = mp.mpf(2) * mp.pi
        for n in range(1, n_max + 1):
            sig = mp.mpf(0)
            for d in range(1, n + 1):
                if n % d == 0:
                    sig += mp.mpf(d) ** (-5)
            bess = mp.besselk(five_halves, two_pi * mp.mpf(n) * tau2)
            acc += (mp.mpf(n) ** five_halves) * sig * bess * mp.mpf(2) * mp.cos(two_pi * mp.mpf(n) * tau1)
        return t0 + t1 + pref * acc

    def e3_direct_lattice(tau1: mp.mpf, tau2: mp.mpf, m_lim: int = 35) -> mp.mpf:
        tot = mp.mpf(0)
        t2_cub = tau2 ** 3
        for m in range(-m_lim, m_lim + 1):
            for n in range(-m_lim, m_lim + 1):
                if m == 0 and n == 0:
                    continue
                r2 = (mp.mpf(m) + mp.mpf(n) * tau1) ** 2 + (mp.mpf(n) * tau2) ** 2
                tot += t2_cub / (r2 ** 3)
        return tot / mp.mpf(2)

    t1_hex = mp.mpf(1) / mp.mpf(2)
    t2_hex = mp.sqrt(mp.mpf(3)) / mp.mpf(2)
    e3_hex = e3_chowla_selberg(t1_hex, t2_hex, 28)
    e3_hex_lat = e3_direct_lattice(t1_hex, t2_hex, 35)
    e3_sq = e3_chowla_selberg(mp.mpf(0), mp.mpf(1), 28)

    # 4th-order Richardson gradient and 2nd-order Hessian at tau_hex
    h_fd = mp.mpf(10) ** (-11)
    h2_fd = h_fd / mp.mpf(2)

    def grad_rich(f_fn, x0: mp.mpf, y0: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        dx1 = (f_fn(x0 + h_fd, y0) - f_fn(x0 - h_fd, y0)) / (mp.mpf(2) * h_fd)
        dx2 = (f_fn(x0 + h2_fd, y0) - f_fn(x0 - h2_fd, y0)) / (mp.mpf(2) * h2_fd)
        gx = (mp.mpf(4) * dx2 - dx1) / mp.mpf(3)
        dy1 = (f_fn(x0, y0 + h_fd) - f_fn(x0, y0 - h_fd)) / (mp.mpf(2) * h_fd)
        dy2 = (f_fn(x0, y0 + h2_fd) - f_fn(x0, y0 - h2_fd)) / (mp.mpf(2) * h2_fd)
        gy = (mp.mpf(4) * dy2 - dy1) / mp.mpf(3)
        return gx, gy

    gx_hex, gy_hex = grad_rich(e3_chowla_selberg, t1_hex, t2_hex)
    h_hess = mp.mpf(10) ** (-9)
    h11 = (e3_chowla_selberg(t1_hex + h_hess, t2_hex) - mp.mpf(2) * e3_hex + e3_chowla_selberg(t1_hex - h_hess, t2_hex)) / (h_hess ** 2)
    h22 = (e3_chowla_selberg(t1_hex, t2_hex + h_hess) - mp.mpf(2) * e3_hex + e3_chowla_selberg(t1_hex, t2_hex - h_hess)) / (h_hess ** 2)
    h12 = (
        e3_chowla_selberg(t1_hex + h_hess, t2_hex + h_hess)
        - e3_chowla_selberg(t1_hex + h_hess, t2_hex - h_hess)
        - e3_chowla_selberg(t1_hex - h_hess, t2_hex + h_hess)
        + e3_chowla_selberg(t1_hex - h_hess, t2_hex - h_hess)
    ) / (mp.mpf(4) * h_hess ** 2)
    # Exact analytic Laplacian identity: at tau_hex, h11 == h22 == 4 * E_3(tau_hex)
    hess_laplacian_err = max(abs(h11 - mp.mpf(4) * e3_hex), abs(h22 - mp.mpf(4) * e3_hex), abs(h12))
    e3_min_ok = (
        e3_hex > mp.mpf(0)
        and e3_hex < e3_sq
        and abs(e3_hex - e3_hex_lat) < mp.mpf(10) ** (-5)
        and max(abs(gx_hex), abs(gy_hex)) < mp.mpf(10) ** (-35)
        and h11 > mp.mpf(0)
        and h22 > mp.mpf(0)
        and (h11 * h22 - h12 * h12) > mp.mpf(0)
        and hess_laplacian_err < mp.mpf(10) ** (-14)
    )

    n_b_gauge = 45 * 2  # 90 real gauge B per T^2 lattice point
    n_f_weyl = 48 * 2   # 96 real Weyl F per T^2 lattice point
    gsm_brane_2h = 12 * 2 - 48 * 2      # -72
    gsm_bulk_2h = 12 * 2 + 4 - 48 * 2   # -68

    casimir_configs = [
        ("brane_2H", 0, gsm_brane_2h),
        ("bulk_2H", 4, gsm_bulk_2h),
        ("bulk_real_10", 5, gsm_bulk_2h),
        ("bulk_complex_10", 10, gsm_bulk_2h),
    ]
    casimir_results = {}
    for label, s_b, gsm_ref in casimir_configs:
        str_val = n_b_gauge + s_b - n_f_weyl
        v_coeff = -str_val  # V_Cas(tau) = (v_coeff / pi^3) * E_3(tau)
        v_at_hex = (mp.mpf(v_coeff) / (mp.pi ** 3)) * e3_hex
        hess_eig = (mp.mpf(v_coeff) / (mp.pi ** 3)) * h11
        casimir_results[label] = {
            "scalar_B_per_pt": s_b,
            "supertrace_nB_minus_nF": str_val,
            "casimir_E3_pi3_coeff": v_coeff,
            "V_Cas_at_tau_hex": mp.nstr(v_at_hex, 25),
            "hessian_eig_at_tau_hex": mp.nstr(hess_eig, 25),
            "is_positive_dS": (v_at_hex > mp.mpf(0)),
            "stabilizes_tau_hex": (hess_eig > mp.mpf(0) and e3_min_ok),
            "slash_factor_vs_GSM": frac_str(Fraction(gsm_ref, str_val)) if str_val < 0 else "N/A_AdS_sign_flip",
        }

    gates_a = {
        "cl10_and_16plus_algebra_exact": (
            cl["clifford_ok"]
            and cl["gamma11_diag_ok"]
            and cl["hermitian_ok"]
            and cl["commutes_g11_ok"]
            and cl["lie_bracket_ok"]
            and cl["ortho_ok"]
        ),
        "orbifold_centralizers_root_and_spinor_agree": (
            dim_c_ps_root == 21
            and dim_c_ps_spin == 21
            and dim_c_j5_root == 25
            and dim_c_j5_spin == 25
            and dim_c_both_root == 13
            and dim_c_both_spin == 13
            and dim_g_sm_root == 12
            and n_broken_proca_root == 33
            and closures_ok
            and s_ps_sq_ok
            and s_j5_unitary_ok
            and lifts_commute_ok
            and adj_real_ok
            and aps_invol_ok
            and aj5_invol_ok
            and adj_comm_ok
            and vec10_ops_ok
        ),
        "doublet_triplet_split_4_plus_6": (dt_even_2h == 4 and dt_odd_triplets == 6),
        "tr16_F2_and_F4_identities_explicit_16x16": (
            all(r["f2_ratio_exact"] and r["f4_identity_exact"] and r["imag_zero"] for r in trace_records)
            and coeff_a == Fraction(-1, 1)
            and coeff_b == Fraction(3, 4)
            and non_cartan_ok
        ),
        "i8_anomaly_forces_7d_inflow": (
            c_tr10_f4 == Fraction(-1, 8)
            and c_tr_r4 == Fraction(1, 120)
            and mixed_u1_zero
        ),
        "casimir_6d_supertraces_and_dS_vs_AdS_selection": (
            e3_min_ok
            and casimir_results["brane_2H"]["supertrace_nB_minus_nF"] == -6
            and casimir_results["brane_2H"]["stabilizes_tau_hex"]
            and casimir_results["brane_2H"]["slash_factor_vs_GSM"] == "12"
            and casimir_results["bulk_2H"]["supertrace_nB_minus_nF"] == -2
            and casimir_results["bulk_2H"]["stabilizes_tau_hex"]
            and casimir_results["bulk_2H"]["slash_factor_vs_GSM"] == "34"
            and casimir_results["bulk_real_10"]["supertrace_nB_minus_nF"] == -1
            and casimir_results["bulk_real_10"]["stabilizes_tau_hex"]
            and casimir_results["bulk_real_10"]["slash_factor_vs_GSM"] == "68"
            and casimir_results["bulk_complex_10"]["supertrace_nB_minus_nF"] == 4
            and (not casimir_results["bulk_complex_10"]["is_positive_dS"])
            and (not casimir_results["bulk_complex_10"]["stabilizes_tau_hex"])
        ),
    }

    return {
        "orbifold_centralizers": {
            "root_system": {
                "n_cartans": 5,
                "n_roots": len(roots),
                "dim_so10": 5 + len(roots),
                "dim_C_P_PS": dim_c_ps_root,
                "dim_C_J_5": dim_c_j5_root,
                "dim_C_P_PS_J_5": dim_c_both_root,
                "dim_G_SM": dim_g_sm_root,
                "n_broken_proca": n_broken_proca_root,
                "broken_split": [n_broken_ps_coset, n_broken_ps_to_smx, n_broken_u1x],
                "subalgebras_bracket_closed": closures_ok,
            },
            "spinor_16plus_projector_traces": {
                "dim_C_P_PS": dim_c_ps_spin,
                "dim_C_J_5": dim_c_j5_spin,
                "dim_C_P_PS_J_5": dim_c_both_spin,
            },
            "doublet_triplet_10": {
                "even_2H_dim": dt_even_2h,
                "odd_triplets_dim": dt_odd_triplets,
            },
        },
        "trace_identities_and_i8": {
            "cartan_16x16_tests": trace_records,
            "extracted_A_tr10_F4": frac_str(coeff_a),
            "extracted_B_tr10_F2_sq": frac_str(coeff_b),
            "non_cartan_unitary_scrambled_verified": non_cartan_ok,
            "non_cartan_tr10_F2": frac_str(nc_t10_2[0]),
            "non_cartan_tr16_F2": frac_str(nc_t16_2[0]),
            "non_cartan_tr10_F4": frac_str(nc_t10_4[0]),
            "non_cartan_tr16_F4": frac_str(nc_t16_4[0]),
            "n_weyl_6d": n_weyl_6d,
            "c_tr10_F4": frac_str(c_tr10_f4),
            "c_tr10_F2_sq": frac_str(c_tr10_f2_sq),
            "c_tr_R4": frac_str(c_tr_r4),
            "c_tr_R2_sq": frac_str(c_tr_r2_sq),
            "c_tr_R2_tr10_F2": frac_str(c_tr_r2_tr10_f2),
            "mixed_u1_zero": mixed_u1_zero,
            "max_abs_tr16_gen": frac_str(max_abs_tr_gen),
            "max_mixed_QY_G2": frac_str(max_mixed_qy_g2),
        },
        "casimir_6d_supertraces": {
            "E3_tau_hex_chowla_selberg": mp.nstr(e3_hex, 35),
            "E3_tau_hex_direct_lattice_M35": mp.nstr(e3_hex_lat, 20),
            "E3_tau_i_chowla_selberg": mp.nstr(e3_sq, 35),
            "grad_E3_tau_hex_norm": mp.nstr(max(abs(gx_hex), abs(gy_hex)), 10),
            "hess_E3_tau_hex_diag": mp.nstr(h11, 25),
            "hess_laplacian_identity_err": mp.nstr(hess_laplacian_err, 10),
            "configs": casimir_results,
        },
        "gates": gates_a,
    }


# =============================================================================
# OW11-B: 55-dps Manual-Sturm + Bisection + 2D Newton + Richardson FD FRG
#         + Exact Matrix-Trace 1-Loop Gauge Unification & Pati-Salam Closure
#         + Dimensionless Proton Lifetime Enhancement
# =============================================================================

def manual_sturm_chain_qq(coeffs: list[int]) -> list[sp.Poly]:
    """Construct exact Sturm remainder sequence over QQ (ZERO polyroots/nroots/real_roots)."""
    x = sp.Symbol("x")
    p0 = sp.Poly([sp.Rational(c) for c in coeffs], x, domain="QQ")
    g = sp.gcd(p0, p0.diff())
    p0 = sp.quo(p0, g, x, domain="QQ")
    chain = [p0, p0.diff()]
    while chain[-1].degree() > 0:
        rem = sp.rem(chain[-2], chain[-1], x, domain="QQ")
        if rem.is_zero:
            break
        chain.append(-rem)
    return chain


def count_sign_variations(vals: list[sp.Rational]) -> int:
    nz = [1 if v > 0 else -1 for v in vals if v != 0]
    return sum(1 for i in range(len(nz) - 1) if nz[i] * nz[i + 1] < 0)


def sturm_roots_in_half_open(chain: list[sp.Poly], lo: sp.Rational, hi: sp.Rational | None) -> int:
    """Exact real root count in (lo, hi] (or (lo, +inf) when hi is None)."""
    v_lo = [p.eval(lo) for p in chain]
    if hi is None:
        v_hi = [p.LC() for p in chain]
    else:
        v_hi = [p.eval(hi) for p in chain]
    return count_sign_variations(v_lo) - count_sign_variations(v_hi)


def frg_beta_55(g: mp.mpf, lam: mp.mpf, ns: int, nw: int, nv: int, fw: int) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    """d=4 harmonic-gauge Litim FRG beta functions at 55 dps (ZERO float literals)."""
    mg = mp.mpf(ns + fw * nw - 4 * nv)
    ml = mp.mpf(ns + 2 * nv - 2 * nw) / mp.mpf(2)
    x = mp.mpf(1) - mp.mpf(2) * lam
    b1 = (mp.mpf(10) / x - mp.mpf(18) / (x * x) - mp.mpf(14) + mg) / (mp.mpf(6) * mp.pi)
    b2 = (-mp.mpf(5) / x + mp.mpf(6) / (x * x)) / (mp.mpf(12) * mp.pi)
    denom = mp.mpf(1) - g * b2
    eta = g * b1 / denom
    bg = (mp.mpf(2) + eta) * g
    bl = (eta - mp.mpf(2)) * lam + (g / (mp.mpf(2) * mp.pi)) * (
        mp.mpf(5) * (mp.mpf(1) - eta / mp.mpf(6)) / x - mp.mpf(4) + ml
    )
    return bg, bl, eta, denom


def richardson_jacobian_55(g: mp.mpf, lam: mp.mpf, ns: int, nw: int, nv: int, fw: int) -> tuple[list[list[mp.mpf]], mp.mpc, mp.mpc]:
    """4th-order Richardson-extrapolated central FD Jacobian at 55 dps."""
    h = mp.mpf(10) ** (-11)
    h2 = h / mp.mpf(2)

    def eval_pair(gv: mp.mpf, lv: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        bg, bl, _, _ = frg_beta_55(gv, lv, ns, nw, nv, fw)
        return bg, bl

    def deriv_col(step_g: mp.mpf, step_l: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        step = step_g + step_l
        fp1 = eval_pair(g + step_g, lam + step_l)
        fm1 = eval_pair(g - step_g, lam - step_l)
        d1_0 = (fp1[0] - fm1[0]) / (mp.mpf(2) * step)
        d1_1 = (fp1[1] - fm1[1]) / (mp.mpf(2) * step)
        fp2 = eval_pair(g + step_g / mp.mpf(2), lam + step_l / mp.mpf(2))
        fm2 = eval_pair(g - step_g / mp.mpf(2), lam - step_l / mp.mpf(2))
        d2_0 = (fp2[0] - fm2[0]) / step
        d2_1 = (fp2[1] - fm2[1]) / step
        r0 = (mp.mpf(4) * d2_0 - d1_0) / mp.mpf(3)
        r1 = (mp.mpf(4) * d2_1 - d1_1) / mp.mpf(3)
        return r0, r1

    c1 = deriv_col(h, mp.mpf(0))
    c2 = deriv_col(mp.mpf(0), h)
    jac = [[c1[0], c2[0]], [c1[1], c2[1]]]
    # Stability matrix B = -J; eigenvalues theta_1, theta_2 (UV-attractive iff Re(theta) > 0)
    b11, b12, b21, b22 = -c1[0], -c2[0], -c1[1], -c2[1]
    tr = b11 + b22
    det = b11 * b22 - b12 * b21
    disc = tr * tr - mp.mpf(4) * det
    if disc >= mp.mpf(0):
        sq = mp.sqrt(disc)
        t1 = mp.mpc((tr + sq) / mp.mpf(2), mp.mpf(0))
        t2 = mp.mpc((tr - sq) / mp.mpf(2), mp.mpf(0))
    else:
        sq = mp.sqrt(-disc)
        t1 = mp.mpc(tr / mp.mpf(2), sq / mp.mpf(2))
        t2 = mp.mpc(tr / mp.mpf(2), -sq / mp.mpf(2))
    return jac, t1, t2


def solve_frg_model_sturm_newton(ns: int, nw: int, nv: int, fw: int) -> dict[str, Any]:
    """Solve (beta_g, beta_lam) = (0, 0) via exact Sturm chain + bisection + 55-dps 2D Newton."""
    mp.mp.dps = 55
    mg = ns + fw * nw - 4 * nv
    ml2 = ns + 2 * nv - 2 * nw

    # Exact integer cubic Q(x) = 2(14 - Mg) x^3 + (2 Mg + 3(2 Ml) - 82) x^2 + 118 x - 48, x = 1 - 2 lam > 0
    coeffs = [2 * (14 - mg), 2 * mg + 3 * ml2 - 82, 118, -48]
    chain = manual_sturm_chain_qq(coeffs)
    n_pos_roots = sturm_roots_in_half_open(chain, sp.Rational(0), None)

    # Cauchy upper bound for positive roots
    lc = abs(sp.Rational(coeffs[0]))
    r_bound = sp.Rational(1) + max(abs(sp.Rational(c)) / lc for c in coeffs[1:])

    # Sturm-guided dyadic root isolation on (0, r_bound]
    work: list[tuple[sp.Rational, sp.Rational]] = [(sp.Rational(0), r_bound)]
    brackets: list[tuple[sp.Rational, sp.Rational]] = []
    exact_roots: list[sp.Rational] = []
    while work:
        lo, hi = work.pop()
        cnt = sturm_roots_in_half_open(chain, lo, hi)
        if cnt == 0:
            continue
        if cnt == 1:
            brackets.append((lo, hi))
        else:
            mid = (lo + hi) * sp.Rational(1, 2)
            if chain[0].eval(mid) == 0:
                exact_roots.append(mid)
                # Shift strictly off mid to isolate remaining roots cleanly
                eps = (hi - lo) * sp.Rational(1, 1024)
                while chain[0].eval(mid - eps) == 0 or chain[0].eval(mid + eps) == 0:
                    eps = eps * sp.Rational(1, 2)
                work.append((lo, mid - eps))
                work.append((mid + eps, hi))
            else:
                work.append((lo, mid))
                work.append((mid, hi))

    # Bisect each bracket to rational width < 2^-45, then polish in 55-dps 2D Newton-Raphson
    candidate_xs: list[mp.mpf] = [mp.mpf(r.p) / mp.mpf(r.q) for r in exact_roots]
    for lo, hi in brackets:
        flo = chain[0].eval(lo)
        for _ in range(50):
            mid = (lo + hi) * sp.Rational(1, 2)
            fmid = chain[0].eval(mid)
            if fmid == 0:
                lo = mid
                hi = mid
                break
            if (flo > 0 and fmid > 0) or (flo < 0 and fmid < 0):
                lo, flo = mid, fmid
            else:
                hi = mid
        xm = (lo + hi) * sp.Rational(1, 2)
        candidate_xs.append(mp.mpf(xm.p) / mp.mpf(xm.q))

    fps = []
    tol_newton = mp.mpf(10) ** (-50)
    h_n = mp.mpf(10) ** (-15)
    for x0 in sorted(candidate_xs):
        dx = mp.mpf(14 - mg) * x0 * x0 - mp.mpf(15) * x0 + mp.mpf(24)
        if dx <= mp.mpf(0):
            continue
        g = mp.mpf(12) * mp.pi * x0 * x0 / dx
        lam = (mp.mpf(1) - x0) / mp.mpf(2)
        if g <= mp.mpf(0) or lam >= mp.mpf(1) / mp.mpf(2):
            continue
        # Direct 55-dps 2D Newton-Raphson on (beta_g, beta_lam) = (0, 0)
        for _ in range(30):
            bg, bl, _, _ = frg_beta_55(g, lam, ns, nw, nv, fw)
            if max(abs(bg), abs(bl)) < tol_newton:
                break
            bg_g, bl_g, _, _ = frg_beta_55(g + h_n, lam, ns, nw, nv, fw)
            bg_l, bl_l, _, _ = frg_beta_55(g, lam + h_n, ns, nw, nv, fw)
            j11 = (bg_g - bg) / h_n
            j21 = (bl_g - bl) / h_n
            j12 = (bg_l - bg) / h_n
            j22 = (bl_l - bl) / h_n
            det = j11 * j22 - j12 * j21
            dg = -(j22 * bg - j12 * bl) / det
            dl = -(-j21 * bg + j11 * bl) / det
            g += dg
            lam += dl
            if max(abs(dg), abs(dl)) < tol_newton:
                break
        bg, bl, eta, denom = frg_beta_55(g, lam, ns, nw, nv, fw)
        _, t1, t2 = richardson_jacobian_55(g, lam, ns, nw, nv, fw)
        if g > mp.mpf(0) and lam < mp.mpf(1) / mp.mpf(2) and denom > mp.mpf(0):
            fps.append({
                "g_star": mp.nstr(g, 35),
                "lam_star": mp.nstr(lam, 35),
                "eta_N": mp.nstr(eta, 25),
                "one_minus_g_B2": mp.nstr(denom, 25),
                "theta_1_re": mp.nstr(mp.re(t1), 25),
                "theta_1_im": mp.nstr(mp.im(t1), 25),
                "theta_2_re": mp.nstr(mp.re(t2), 25),
                "theta_2_im": mp.nstr(mp.im(t2), 25),
                "uv_attractive": (mp.re(t1) > mp.mpf(0) and mp.re(t2) > mp.mpf(0)),
                "max_residual": mp.nstr(max(abs(bg), abs(bl)), 8),
                "_g": g,
                "_lam": lam,
                "_res": max(abs(bg), abs(bl)),
            })

    return {
        "spectrum": [ns, nw, nv],
        "f_W": fw,
        "M_g": mg,
        "two_M_l": ml2,
        "cubic_coeffs": coeffs,
        "sturm_positive_x_root_count": n_pos_roots,
        "n_physical_fps": len(fps),
        "fixed_points": fps,
    }


def compute_exact_scalar_db_from_real_trace() -> dict[str, Any]:
    """Compute exact 1-loop scalar beta-function shifts directly via Tr_real(T_a^2) / 6.

    For any complex representation R of dimension d_C, its realification has dimension 2*d_C
    and for any Hermitian diagonal Cartan generator T = diag(w_1, ..., w_{d_C}):
      Tr_real(T^2) = 2 * sum_{j=1}^{d_C} w_j^2,
    so Delta b = (1/6) Tr_real(T^2) = (1/3) sum w_j^2.
    For a real representation R with Cartan weights (w_1, ..., w_{d_R}):
      Tr_real(T^2) = sum w_j^2,
    so Delta b = (1/6) Tr_real(T^2).
    """
    # Explicit Cartan weight lists (exact sympy.Rational) for fundamental representations:
    # SU(2): T_3 on 2 is (+1/2, -1/2); on 3 (adj) is (+1, 0, -1)
    w_su2_2 = [sp.Rational(1, 2), sp.Rational(-1, 2)]
    w_su2_3 = [sp.Rational(1, 1), sp.Rational(0, 1), sp.Rational(-1, 1)]
    # SU(4): T_3 = diag(+1/2, -1/2, 0, 0) on 4
    w_su4_4 = [sp.Rational(1, 2), sp.Rational(-1, 2), sp.Rational(0, 1), sp.Rational(0, 1)]
    # Symmetric 2-tensor 10 of SU(4): pairs (i <= j) -> weight w_i + w_j
    w_su4_10 = [w_su4_4[i] + w_su4_4[j] for i in range(4) for j in range(i, 4)]
    # Adjoint 15 of SU(4): pairs (i != j) -> w_i - w_j (12 roots) + 3 Cartans (weight 0)
    w_su4_15 = [w_su4_4[i] - w_su4_4[j] for i in range(4) for j in range(4) if i != j] + [sp.Rational(0, 1)] * 3

    def tensor_weights(w_a: list[sp.Rational], w_b: list[sp.Rational], w_c: list[sp.Rational]) -> tuple[list[sp.Rational], list[sp.Rational], list[sp.Rational]]:
        # Returns weight lists for (T_4, T_2L, T_2R) across all dim(a)*dim(b)*dim(c) basis states
        t4, t2l, t2r = [], [], []
        for wa in w_a:
            for wb in w_b:
                for wc in w_c:
                    t4.append(wa)
                    t2l.append(wb)
                    t2r.append(wc)
        return t4, t2l, t2r

    w1 = [sp.Rational(0, 1)]

    def rep_contrib(w_a: list[sp.Rational], w_b: list[sp.Rational], w_c: list[sp.Rational], is_complex: bool) -> dict[str, Any]:
        t4, t2l, t2r = tensor_weights(w_a, w_b, w_c)
        mult = 2 if is_complex else 1
        n_real = mult * len(t4)
        tr4 = mult * sum(w * w for w in t4)
        tr2l = mult * sum(w * w for w in t2l)
        tr2r = mult * sum(w * w for w in t2r)
        return {
            "n_real_scalars": n_real,
            "db4": tr4 * sp.Rational(1, 6),
            "db2L": tr2l * sp.Rational(1, 6),
            "db2R": tr2r * sp.Rational(1, 6),
        }

    # Explicit representations:
    r_122_c = rep_contrib(w1, w_su2_2, w_su2_2, True)          # 1 complex (1,2,2) = 8 real scalars (= 2H)
    r_412_c = rep_contrib(w_su4_4, w1, w_su2_2, True)          # 1 complex (4,1,2) = 16 real scalars
    r_1511_r = rep_contrib(w_su4_15, w1, w1, False)            # 1 real (15,1,1) = 15 real scalars
    r_1013_c = rep_contrib(w_su4_10, w1, w_su2_3, True)        # 1 complex (10,1,3) = 60 real scalars

    # Also SM 2H (2 complex SU(2)_L doublets with Y = +-1/2, Q_1 = sqrt(3/5) Y -> Q_1^2 = (3/5) Y^2)
    # 2 complex doublets = 4 complex states = 8 real scalars, each with |T_3L| = 1/2 and |Y| = 1/2
    n_real_2h = 8
    db1_2h = sp.Rational(n_real_2h, 6) * sp.Rational(3, 5) * sp.Rational(1, 4)
    db2_2h = sp.Rational(n_real_2h, 6) * sp.Rational(1, 4)
    db3_2h = sp.Rational(0, 1)

    return {
        "SM_2H": {"n_real_scalars": n_real_2h, "db1": db1_2h, "db2": db2_2h, "db3": db3_2h},
        "PS_122_complex": r_122_c,
        "PS_412_complex": r_412_c,
        "PS_1511_real": r_1511_r,
        "PS_1013_complex": r_1013_c,
    }


def solve_ps_closure(
    b4: sp.Rational, b2l: sp.Rational, b2r: sp.Rational,
    b1_sm: sp.Rational, b2_sm: sp.Rational, b3_sm: sp.Rational,
    b_target: sp.Rational,
) -> dict[str, Any]:
    """Compute exact rational Pati-Salam unification scale ratio r = ln(M_PS/M_Z)/ln(M_GUT/M_Z)."""
    # Exact SO(10) -> PS -> SM hypercharge matching: alpha_1^{-1} = (3/5) alpha_{2R}^{-1} + (2/5) alpha_4^{-1}
    b1_eff = sp.Rational(3, 5) * b2r + sp.Rational(2, 5) * b4
    d23_sm = b2_sm - b3_sm
    d12_sm = b1_sm - b2_sm
    d23_ps = b2l - b4
    d12_ps = b1_eff - b2l
    b_ps = d23_ps / d12_ps
    # Solve [r * d23_sm + (1 - r) * d23_ps] / [r * d12_sm + (1 - r) * d12_ps] = b_target
    r_num = b_target * d12_ps - d23_ps
    r_den = (d23_sm - d23_ps) - b_target * (d12_sm - d12_ps)
    r_val = sp.Rational(r_num / r_den)
    # Independent reconstruction check
    b1_bar = r_val * b1_sm + (1 - r_val) * b1_eff
    b2_bar = r_val * b2_sm + (1 - r_val) * b2l
    b3_bar = r_val * b3_sm + (1 - r_val) * b4
    b_reconstructed = sp.Rational((b2_bar - b3_bar) / (b1_bar - b2_bar))
    return {
        "b4": frac_str(b4),
        "b2L": frac_str(b2l),
        "b2R": frac_str(b2r),
        "b1_eff": frac_str(b1_eff),
        "B_PS": frac_str(b_ps),
        "b1_eff_lt_b2L": bool(b1_eff < b2l),
        "B_PS_gt_target": bool(b_ps > b_target),
        "r": frac_str(r_val),
        "r_in_0_1": bool(sp.Rational(0) < r_val and r_val < sp.Rational(1)),
        "B_reconstructed": frac_str(b_reconstructed),
        "B_closure_exact": bool(b_reconstructed == b_target),
        "_r": r_val,
        "_b2L": b2l,
        "_b1_eff": b1_eff,
        "_B_PS": b_ps,
    }


def compute_ow11_b() -> dict[str, Any]:
    """Run OW11-B: 55-dps Sturm+Newton+Richardson FRG + exact 1-loop unification + proton lifetime."""
    mp.mp.dps = 55

    # 1. Solve all 6 card spectra x 2 cutoffs (Type-II f_W=1, Type-I f_W=2)
    models = [
        ("G_SM_2H", 8, 48, 12),
        ("Spin10_real_10", 10, 48, 45),
        ("Spin10_complex_10", 20, 48, 45),
        ("PS_122_412", 24, 48, 21),
        ("PS_122_412_1511", 39, 48, 21),
        ("PS_122_1013", 68, 48, 21),
    ]
    frg_table: dict[str, dict[str, Any]] = {}
    for name, ns, nw, nv in models:
        frg_table[name] = {
            "Type_II_fW1": solve_frg_model_sturm_newton(ns, nw, nv, 1),
            "Type_I_fW2": solve_frg_model_sturm_newton(ns, nw, nv, 2),
        }

    # Diagnostic FRG for 2x(1,2,2)_C (N_S = 32, 47, 76) to verify inconsistency if 2 bidoublets were present
    diag_2bidoublet_models = [
        ("PS_2x122_412", 32, 48, 21),
        ("PS_2x122_412_1511", 47, 48, 21),
        ("PS_2x122_1013", 76, 48, 21),
    ]
    frg_diag_2bidoublet: dict[str, dict[str, Any]] = {}
    for name, ns, nw, nv in diag_2bidoublet_models:
        frg_diag_2bidoublet[name] = {
            "Type_II_fW1": solve_frg_model_sturm_newton(ns, nw, nv, 1),
            "Type_I_fW2": solve_frg_model_sturm_newton(ns, nw, nv, 2),
        }

    # Extract key FRG values for gate checks
    g_gsm_t2 = frg_table["G_SM_2H"]["Type_II_fW1"]["fixed_points"][0]["_g"]
    g_s10r_t2 = frg_table["Spin10_real_10"]["Type_II_fW1"]["fixed_points"][0]["_g"]
    l_s10r_t2 = frg_table["Spin10_real_10"]["Type_II_fW1"]["fixed_points"][0]["_lam"]
    g_s10r_t1 = frg_table["Spin10_real_10"]["Type_I_fW2"]["fixed_points"][0]["_g"]
    l_s10r_t1 = frg_table["Spin10_real_10"]["Type_I_fW2"]["fixed_points"][0]["_lam"]

    g_s10c_t2 = frg_table["Spin10_complex_10"]["Type_II_fW1"]["fixed_points"][0]["_g"]
    l_s10c_t2 = frg_table["Spin10_complex_10"]["Type_II_fW1"]["fixed_points"][0]["_lam"]
    g_s10c_t1 = frg_table["Spin10_complex_10"]["Type_I_fW2"]["fixed_points"][0]["_g"]
    l_s10c_t1 = frg_table["Spin10_complex_10"]["Type_I_fW2"]["fixed_points"][0]["_lam"]

    g_ps68_t2 = frg_table["PS_122_1013"]["Type_II_fW1"]["fixed_points"][0]["_g"]
    l_ps68_t2 = frg_table["PS_122_1013"]["Type_II_fW1"]["fixed_points"][0]["_lam"]
    g_ps68_t1 = frg_table["PS_122_1013"]["Type_I_fW2"]["fixed_points"][0]["_g"]
    l_ps68_t1 = frg_table["PS_122_1013"]["Type_I_fW2"]["fixed_points"][0]["_lam"]

    weaker_ratio = g_gsm_t2 / g_s10r_t2

    max_frg_res = mp.mpf(0)
    all_fps_uv_attractive = True
    for m_dict in frg_table.values():
        for t_dict in m_dict.values():
            for fp in t_dict["fixed_points"]:
                if fp["_res"] > max_frg_res:
                    max_frg_res = fp["_res"]
                if not fp["uv_attractive"]:
                    all_fps_uv_attractive = False

    # Strip private _g, _lam, _res fields before JSON output
    for tbl in (frg_table, frg_diag_2bidoublet):
        for m_dict in tbl.values():
            for t_dict in m_dict.values():
                for fp in t_dict["fixed_points"]:
                    del fp["_g"]
                    del fp["_lam"]
                    del fp["_res"]

    # 2. Exact 1-loop gauge unification & Pati-Salam closure from explicit real traces
    reps = compute_exact_scalar_db_from_real_trace()
    b_target = sp.Rational(5, 7)

    # 4D G_SM + 2H (3 generations: +4 universal)
    b1_sm = sp.Rational(4, 1) + reps["SM_2H"]["db1"]
    b2_sm = sp.Rational(-22, 3) + sp.Rational(4, 1) + reps["SM_2H"]["db2"]
    b3_sm = sp.Rational(-11, 1) + sp.Rational(4, 1) + reps["SM_2H"]["db3"]
    B_sm_2h = sp.Rational((b2_sm - b3_sm) / (b1_sm - b2_sm))

    # 6D KK brane 2H: -10/3 C_2 (+ universal fermions)
    b1_kk_brane = sp.Rational(0, 1)
    b2_kk_brane = sp.Rational(-20, 3)
    b3_kk_brane = sp.Rational(-10, 1)
    B_kk_brane = sp.Rational((b2_kk_brane - b3_kk_brane) / (b1_kk_brane - b2_kk_brane))

    # 6D KK bulk 2H: FIRST-PRINCIPLES (-10/3 C_2 + 2H with exact db(2H) = (1/5, 1/3, 0))
    b1_kk_bulk_fp = b1_kk_brane + reps["SM_2H"]["db1"]
    b2_kk_bulk_fp = b2_kk_brane + reps["SM_2H"]["db2"]
    b3_kk_bulk_fp = b3_kk_brane + reps["SM_2H"]["db3"]
    B_kk_bulk_fp = sp.Rational((b2_kk_bulk_fp - b3_kk_bulk_fp) / (b1_kk_bulk_fp - b2_kk_bulk_fp))

    # Diagnostic check for card's B = 5/8 (requires 2x scalar = 4H = (2/5, 2/3, 0) per KK pair)
    b1_kk_bulk_2x = b1_kk_brane + 2 * reps["SM_2H"]["db1"]
    b2_kk_bulk_2x = b2_kk_brane + 2 * reps["SM_2H"]["db2"]
    b3_kk_bulk_2x = b3_kk_brane + 2 * reps["SM_2H"]["db3"]
    B_kk_bulk_2x = sp.Rational((b2_kk_bulk_2x - b3_kk_bulk_2x) / (b1_kk_bulk_2x - b2_kk_bulk_2x))

    # Pati-Salam base (gauge + 3 generations of (4,2,1) + (4bar,1,2))
    b4_base = sp.Rational(-11, 3) * 4 + sp.Rational(4, 1)
    b2l_base = sp.Rational(-11, 3) * 2 + sp.Rational(4, 1)
    b2r_base = sp.Rational(-11, 3) * 2 + sp.Rational(4, 1)

    r122 = reps["PS_122_complex"]
    r412 = reps["PS_412_complex"]
    r1511 = reps["PS_1511_real"]
    r1013 = reps["PS_1013_complex"]

    # AUTHORITATIVE FIRST-PRINCIPLES Pati-Salam closures (1 complex (1,2,2) = 8 real scalars -> N_S = 24, 39, 68, b2L = -3 == b2_SM)
    ps_fp = {
        "PS_122_412": solve_ps_closure(
            b4_base + r122["db4"] + r412["db4"],
            b2l_base + r122["db2L"] + r412["db2L"],
            b2r_base + r122["db2R"] + r412["db2R"],
            b1_sm, b2_sm, b3_sm, b_target,
        ),
        "PS_122_412_1511": solve_ps_closure(
            b4_base + r122["db4"] + r412["db4"] + r1511["db4"],
            b2l_base + r122["db2L"] + r412["db2L"] + r1511["db2L"],
            b2r_base + r122["db2R"] + r412["db2R"] + r1511["db2R"],
            b1_sm, b2_sm, b3_sm, b_target,
        ),
        "PS_122_1013": solve_ps_closure(
            b4_base + r122["db4"] + r1013["db4"],
            b2l_base + r122["db2L"] + r1013["db2L"],
            b2r_base + r122["db2R"] + r1013["db2R"],
            b1_sm, b2_sm, b3_sm, b_target,
        ),
    }
    ps_fp_ns = {
        "PS_122_412": r122["n_real_scalars"] + r412["n_real_scalars"],
        "PS_122_412_1511": r122["n_real_scalars"] + r412["n_real_scalars"] + r1511["n_real_scalars"],
        "PS_122_1013": r122["n_real_scalars"] + r1013["n_real_scalars"],
    }

    # DIAGNOSTIC Pati-Salam closures with 2x complex (1,2,2) (16 real scalars -> db2L=db2R=+2/3, b2L=-8/3)
    # Reproduces the exact numbers quoted in Card A2-OW11 & Erratum 1 (67/75, 61/69, 25/33)
    ps_diag_2x = {
        "PS_122_412": solve_ps_closure(
            b4_base + 2 * r122["db4"] + r412["db4"],
            b2l_base + 2 * r122["db2L"] + r412["db2L"],
            b2r_base + 2 * r122["db2R"] + r412["db2R"],
            b1_sm, b2_sm, b3_sm, b_target,
        ),
        "PS_122_412_1511": solve_ps_closure(
            b4_base + 2 * r122["db4"] + r412["db4"] + r1511["db4"],
            b2l_base + 2 * r122["db2L"] + r412["db2L"] + r1511["db2L"],
            b2r_base + 2 * r122["db2R"] + r412["db2R"] + r1511["db2R"],
            b1_sm, b2_sm, b3_sm, b_target,
        ),
        "PS_122_1013": solve_ps_closure(
            b4_base + 2 * r122["db4"] + r1013["db4"],
            b2l_base + 2 * r122["db2L"] + r1013["db2L"],
            b2r_base + 2 * r122["db2R"] + r1013["db2R"],
            b1_sm, b2_sm, b3_sm, b_target,
        ),
    }
    ps_diag_2x_ns = {
        "PS_122_412": 2 * r122["n_real_scalars"] + r412["n_real_scalars"],
        "PS_122_412_1511": 2 * r122["n_real_scalars"] + r412["n_real_scalars"] + r1511["n_real_scalars"],
        "PS_122_1013": 2 * r122["n_real_scalars"] + r1013["n_real_scalars"],
    }

    # Check SU(2)_L continuity across M_PS
    su2L_continuous_fp = all(v["_b2L"] == b2_sm for v in ps_fp.values())
    su2L_continuous_2x = all(v["_b2L"] == b2_sm for v in ps_diag_2x.values())

    # 3. Dimensionless proton lifetime enhancement: (M_X / M_GUT)^4 = (250 * sqrt(pi))^4 = 250^4 * pi^2
    mx_over_mpl = mp.sqrt(mp.pi) / mp.mpf(4)
    mgut_over_mpl = mp.mpf(1) / mp.mpf(1000)
    mx_over_mgut = mx_over_mpl / mgut_over_mpl
    tau_p_enhancement = mx_over_mgut ** 4
    tau_p_exact_formula = (mp.mpf(250) ** 4) * (mp.pi ** 2)
    tau_p_formula_diff = abs(tau_p_enhancement - tau_p_exact_formula)
    tau_p_threshold = mp.mpf(3) * (mp.mpf(10) ** 10)

    # Gates for OW11-B (strictly honest: separate FRG, first-principles unification, and card-number audit)
    gates_b = {
        "frg_all_12_cases_sturm_newton_verified": (
            max_frg_res < mp.mpf(10) ** (-48)
            and all_fps_uv_attractive
            and frg_table["G_SM_2H"]["Type_II_fW1"]["n_physical_fps"] == 1
            and frg_table["G_SM_2H"]["Type_I_fW2"]["n_physical_fps"] == 0
            and abs(g_gsm_t2 - mp.mpf(7058) / mp.mpf(1000)) < mp.mpf(1) / mp.mpf(1000)
            and frg_table["Spin10_real_10"]["Type_II_fW1"]["n_physical_fps"] == 1
            and frg_table["Spin10_real_10"]["Type_I_fW2"]["n_physical_fps"] == 1
            and (mp.mpf(2) / mp.mpf(10) < g_s10r_t2 < mp.mpf(3) / mp.mpf(10))
            and (mp.mpf(0) < l_s10r_t2 < mp.mpf(1) / mp.mpf(10))
            and (mp.mpf(3) / mp.mpf(10) < g_s10r_t1 < mp.mpf(4) / mp.mpf(10))
            and (mp.mpf(0) < l_s10r_t1 < mp.mpf(1) / mp.mpf(10))
            and (weaker_ratio > mp.mpf(27))
            and frg_table["Spin10_complex_10"]["Type_II_fW1"]["n_physical_fps"] == 1
            and frg_table["Spin10_complex_10"]["Type_I_fW2"]["n_physical_fps"] == 1
            and (mp.mpf(2) / mp.mpf(10) < g_s10c_t2 < mp.mpf(3) / mp.mpf(10))
            and (mp.mpf(1) / mp.mpf(10) < l_s10c_t2 < mp.mpf(2) / mp.mpf(10))
            and (mp.mpf(3) / mp.mpf(10) < g_s10c_t1 < mp.mpf(4) / mp.mpf(10))
            and (mp.mpf(1) / mp.mpf(10) < l_s10c_t1 < mp.mpf(2) / mp.mpf(10))
            and frg_table["PS_122_412"]["Type_II_fW1"]["M_g"] == -12
            and frg_table["PS_122_412"]["Type_II_fW1"]["two_M_l"] == -30
            and frg_table["PS_122_412"]["Type_II_fW1"]["n_physical_fps"] == 1
            and frg_table["PS_122_412"]["Type_I_fW2"]["n_physical_fps"] == 0
            and frg_table["PS_122_412_1511"]["Type_II_fW1"]["M_g"] == 3
            and frg_table["PS_122_412_1511"]["Type_II_fW1"]["two_M_l"] == -15
            and frg_table["PS_122_412_1511"]["Type_II_fW1"]["n_physical_fps"] == 1
            and frg_table["PS_122_412_1511"]["Type_I_fW2"]["n_physical_fps"] == 0
            and frg_table["PS_122_1013"]["Type_II_fW1"]["two_M_l"] == 14
            and frg_table["PS_122_1013"]["Type_II_fW1"]["n_physical_fps"] == 1
            and frg_table["PS_122_1013"]["Type_I_fW2"]["n_physical_fps"] == 1
            and (mp.mpf(3) / mp.mpf(10) < g_ps68_t2 < mp.mpf(4) / mp.mpf(10))
            and (mp.mpf(3) / mp.mpf(10) < l_ps68_t2 < mp.mpf(4) / mp.mpf(10))
            and (mp.mpf(3) / mp.mpf(10) < g_ps68_t1 < mp.mpf(4) / mp.mpf(10))
            and (mp.mpf(3) / mp.mpf(10) < l_ps68_t1 < mp.mpf(4) / mp.mpf(10))
        ),
        "unification_sm2h_and_kk_brane_match_card": bool(
            B_sm_2h == sp.Rational(5, 9) and B_kk_brane == sp.Rational(1, 2)
        ),
        "unification_kk_bulk_2h_first_principles_lt_5_over_7": bool(
            B_kk_bulk_fp == sp.Rational(55, 98) and B_kk_bulk_fp < b_target
        ),
        "unification_kk_bulk_2h_matches_card_5_over_8": bool(
            B_kk_bulk_fp == sp.Rational(5, 8)
        ),
        "pati_salam_first_principles_1x122_closes_5_over_7_and_su2L_continuous": bool(
            su2L_continuous_fp
            and ps_fp_ns["PS_122_412"] == 24
            and ps_fp_ns["PS_122_412_1511"] == 39
            and ps_fp_ns["PS_122_1013"] == 68
            and ps_fp["PS_122_412"]["_r"] == sp.Rational(8, 9)
            and ps_fp["PS_122_412"]["b1_eff_lt_b2L"]
            and ps_fp["PS_122_412"]["B_closure_exact"]
            and ps_fp["PS_122_412_1511"]["_r"] == sp.Rational(29, 33)
            and ps_fp["PS_122_412_1511"]["b1_eff_lt_b2L"]
            and ps_fp["PS_122_412_1511"]["B_closure_exact"]
            and ps_fp["PS_122_1013"]["_r"] == sp.Rational(11, 15)
            and ps_fp["PS_122_1013"]["B_PS_gt_target"]
            and ps_fp["PS_122_1013"]["B_closure_exact"]
        ),
        "pati_salam_first_principles_matches_card_r_values": bool(
            ps_fp["PS_122_412"]["_r"] == sp.Rational(67, 75)
            and ps_fp["PS_122_412_1511"]["_r"] == sp.Rational(61, 69)
            and ps_fp["PS_122_1013"]["_r"] == sp.Rational(25, 33)
        ),
        "pati_salam_diagnostic_2x122_reproduces_card_and_erratum_exact": bool(
            (not su2L_continuous_2x)
            and ps_diag_2x_ns["PS_122_412"] == 32
            and ps_diag_2x_ns["PS_122_412_1511"] == 47
            and ps_diag_2x_ns["PS_122_1013"] == 76
            and ps_diag_2x["PS_122_412"]["_r"] == sp.Rational(67, 75)
            and ps_diag_2x["PS_122_412"]["_b1_eff"] == sp.Rational(-16, 3)
            and ps_diag_2x["PS_122_412"]["_b2L"] == sp.Rational(-8, 3)
            and ps_diag_2x["PS_122_412_1511"]["_r"] == sp.Rational(61, 69)
            and ps_diag_2x["PS_122_412_1511"]["_b1_eff"] == sp.Rational(-76, 15)
            and ps_diag_2x["PS_122_1013"]["_r"] == sp.Rational(25, 33)
            and ps_diag_2x["PS_122_1013"]["_b1_eff"] == sp.Rational(-2, 3)
            and ps_diag_2x["PS_122_1013"]["_B_PS"] == sp.Rational(5, 2)
        ),
        "proton_lifetime_enhancement_gt_3e10": bool(
            tau_p_formula_diff < mp.mpf(10) ** (-42)
            and tau_p_enhancement > tau_p_threshold
        ),
    }

    # Strip private rational helpers
    for d in (ps_fp, ps_diag_2x):
        for v in d.values():
            del v["_r"]
            del v["_b2L"]
            del v["_b1_eff"]
            del v["_B_PS"]

    return {
        "frg_harmonic_litim_55dps": frg_table,
        "frg_spin10_real10_weaker_factor_vs_GSM": mp.nstr(weaker_ratio, 20),
        "frg_max_newton_residual": mp.nstr(max_frg_res, 8),
        "frg_diagnostic_2x122_spectra": frg_diag_2bidoublet,
        "gauge_unification_1loop": {
            "scalar_db_from_explicit_real_traces": {
                k: {
                    "n_real_scalars": v["n_real_scalars"],
                    **{fk: frac_str(fv) for fk, fv in v.items() if fk != "n_real_scalars"},
                }
                for k, v in reps.items()
            },
            "SM_2H": {"b": [frac_str(b1_sm), frac_str(b2_sm), frac_str(b3_sm)], "B": frac_str(B_sm_2h)},
            "KK_6D_brane_2H": {"b_nonuniv": [frac_str(b1_kk_brane), frac_str(b2_kk_brane), frac_str(b3_kk_brane)], "B": frac_str(B_kk_brane)},
            "KK_6D_bulk_2H_first_principles": {
                "b_nonuniv": [frac_str(b1_kk_bulk_fp), frac_str(b2_kk_bulk_fp), frac_str(b3_kk_bulk_fp)],
                "B": frac_str(B_kk_bulk_fp),
                "note": "Exact T^2/Z_2 bulk 2H (8 real scalars per pair) gives db=(1/5,1/3,0) -> B=55/98 != 5/8.",
            },
            "KK_6D_bulk_2H_diagnostic_2x_scalar": {
                "b_nonuniv": [frac_str(b1_kk_bulk_2x), frac_str(b2_kk_bulk_2x), frac_str(b3_kk_bulk_2x)],
                "B": frac_str(B_kk_bulk_2x),
                "note": "Doubling 2H scalar contribution to (2/5,2/3,0) reproduces card B=5/8.",
            },
            "pati_salam_first_principles_1x122_complex": {
                "N_S_real_scalars": ps_fp_ns,
                "su2L_continuous_across_M_PS": su2L_continuous_fp,
                "models": ps_fp,
            },
            "pati_salam_diagnostic_2x122_complex": {
                "N_S_real_scalars": ps_diag_2x_ns,
                "su2L_continuous_across_M_PS": su2L_continuous_2x,
                "models": ps_diag_2x,
            },
        },
        "proton_lifetime_enhancement": {
            "M_X_over_M_Pl": mp.nstr(mx_over_mpl, 30),
            "M_GUT_over_M_Pl": frac_str(Fraction(1, 1000)),
            "M_X_over_M_GUT": mp.nstr(mx_over_mgut, 30),
            "enhancement_fourth_power": mp.nstr(tau_p_enhancement, 30),
            "exact_250pow4_pi2": mp.nstr(tau_p_exact_formula, 30),
            "formula_diff": mp.nstr(tau_p_formula_diff, 8),
        },
        "gates": gates_b,
    }


# =============================================================================
# OW11-C: 4x4 Walsh-Hadamard Z_2 x Z_2 Character Matrix, Prompt Decay,
#         & Spin(10) Z_4 Center Matter Parity P_M = (-1)^{3(B-L)}
# =============================================================================

def compute_ow11_c(cl: dict[str, Any]) -> dict[str, Any]:
    """Run OW11-C via exact 4x4 Walsh-Hadamard matrix + explicit Spin(10) weights & 16x16 matrices."""
    mp.mp.dps = 55
    grades = [(0, 0), (1, 0), (0, 1), (1, 1)]
    points = [(0, 0), (1, 0), (0, 1), (1, 1)]

    # Build exact 4x4 Walsh-Hadamard character matrix W_{g, p} = (-1)^{g_1 p_1 + g_2 p_2}
    w_mat = sp.Matrix([
        [(-1) ** (g[0] * p[0] + g[1] * p[1]) for p in points]
        for g in grades
    ])
    wh_ortho_ok = (w_mat * w_mat.T == 4 * sp.eye(4)) and (int(w_mat.det()) == 16)

    v_e2 = sp.Matrix([1, 1, 1, 1])
    v_cusp = sp.Matrix([1, 0, 0, 0])
    v_gen3 = sp.Matrix([0, 1, 1, 1])

    c4 = [int(x) for x in (w_mat * v_e2)]
    c1 = [int(x) for x in (w_mat * v_cusp)]
    c3 = [int(x) for x in (w_mat * v_gen3)]
    c4_minus_c1 = [c4[i] - c1[i] for i in range(4)]

    # Prompt tree-level LKP decay width Gamma / M_KK = g^2 / (16 pi) at dimensionless rational benchmarks (0 of 19)
    g_benchmarks = [Fraction(1, 4), Fraction(1, 2), Fraction(1, 1)]
    decay_rates = {}
    for gb in g_benchmarks:
        gv = mp.mpf(gb.numerator) / mp.mpf(gb.denominator)
        rate = (gv * gv) / (mp.mpf(16) * mp.pi)
        decay_rates[f"g={frac_str(gb)}"] = {
            "Gamma_over_M_KK": mp.nstr(rate, 20),
            "exceeds_1e_minus_3": (rate > mp.mpf(10) ** (-3)),
        }
    g_crit = mp.sqrt(mp.mpf(16) * mp.pi / mp.mpf(1000))

    # Spin(10) Z_4 center parity P_M = (-1)^{3(B-L)} and c^2 = (-1)^{Q_X}
    # 1) On all 45 adjoint states (5 Cartans + 40 roots +-e_i +- e_j):
    #    3(B - L) = 2 (H_1 + H_2 + H_3), Q_X = 2 (H_1 + H_2 + H_3 + H_4 + H_5)
    p_ps_planes = [1, 1, 1, -1, -1]
    adj_states = []
    # 5 Cartans: 4 in G_SM (su(3)_C x su(2)_L x u(1)_Y) + 1 broken u(1)_X
    for k in range(5):
        sector = "G_SM" if k < 4 else "broken_Proca"
        three_bl = 0
        qx_adj = 0
        adj_states.append((sector, three_bl, (-1) ** three_bl, (-1) ** qx_adj))
    for i in range(5):
        for j in range(i + 1, 5):
            for si in (-1, 1):
                for sj in (-1, 1):
                    in_gsm = (p_ps_planes[i] * p_ps_planes[j] == 1) and (si + sj == 0)
                    sector = "G_SM" if in_gsm else "broken_Proca"
                    three_bl = 2 * ((si if i < 3 else 0) + (sj if j < 3 else 0))
                    qx_adj = 2 * (si + sj)
                    adj_states.append((sector, three_bl, (-1) ** three_bl, (-1) ** qx_adj))

    gsm_states = [s for s in adj_states if s[0] == "G_SM"]
    proca_states = [s for s in adj_states if s[0] == "broken_Proca"]
    all_45_pm_plus1 = all(s[2] == 1 for s in adj_states)
    all_45_c2_plus1 = all(s[3] == 1 for s in adj_states)

    # 2) On all 16 spinor states of 16_+ directly from explicit 16x16 matrices H_k = Sigma_{2k, 2k+1}
    sigmas16 = cl["sigmas16"]
    cartans16 = [sigmas16[(2 * k, 2 * k + 1)] for k in range(5)]
    op_3bl = mat_zero(16)
    op_qx = mat_zero(16)
    for k in range(5):
        if k < 3:
            op_3bl = mat_add(op_3bl, g_scale((Fraction(2, 1), Fraction(0, 1)), cartans16[k]))
        op_qx = mat_add(op_qx, g_scale((Fraction(2, 1), Fraction(0, 1)), cartans16[k]))

    # Verify op_3bl and op_qx are diagonal integer matrices on the 16_+ basis
    spinor_diag_ok = True
    spinor_3bl_eigs = []
    spinor_qx_eigs = []
    for i in range(16):
        for j in range(16):
            if i != j and (op_3bl[i][j] != GZero or op_qx[i][j] != GZero):
                spinor_diag_ok = False
        e_3bl = op_3bl[i][i]
        e_qx = op_qx[i][i]
        if e_3bl[1] != 0 or e_qx[1] != 0 or e_3bl[0].denominator != 1 or e_qx[0].denominator != 1:
            spinor_diag_ok = False
        spinor_3bl_eigs.append(int(e_3bl[0]))
        spinor_qx_eigs.append(int(e_qx[0]))

    spinor_pm_vals = [(-1) ** e for e in spinor_3bl_eigs]
    spinor_c2_vals = [(-1) ** e for e in spinor_qx_eigs]
    # Also verify Z_4 center eigenvalue c = exp(i pi Q_X / 2): since Q_X = +5,+1,-3 (all == 1 mod 4), c == +i on all 16 states!
    spinor_z4_mod4_ok = all((e % 4) == 1 for e in spinor_qx_eigs)
    all_16_pm_minus1 = all(v == -1 for v in spinor_pm_vals)
    all_16_c2_minus1 = all(v == -1 for v in spinor_c2_vals)

    gates_c = {
        "walsh_hadamard_exact_and_C3_eq_C4_minus_C1": (
            wh_ortho_ok
            and c4 == [4, 0, 0, 0]
            and c1 == [1, 1, 1, 1]
            and c3 == [3, -1, -1, -1]
            and c3 == c4_minus_c1
            and all(x == -1 for x in c3[1:])
        ),
        "prompt_lkp_decay_exceeds_1e_minus_3": (
            all(d["exceeds_1e_minus_3"] for d in decay_rates.values())
            and g_crit < mp.mpf(1) / mp.mpf(4)
        ),
        "spin10_z4_matter_parity_exact_45_and_16": (
            len(adj_states) == 45
            and len(gsm_states) == 12
            and len(proca_states) == 33
            and all_45_pm_plus1
            and all_45_c2_plus1
            and spinor_diag_ok
            and len(spinor_pm_vals) == 16
            and all_16_pm_minus1
            and all_16_c2_minus1
            and spinor_z4_mod4_ok
        ),
    }

    return {
        "walsh_hadamard_fourier": {
            "grades": [list(g) for g in grades],
            "C_4_full_E2": c4,
            "C_1_cusp_00": c1,
            "C_3_gen_E2_minus_0": c3,
            "C_4_minus_C_1": c4_minus_c1,
            "W_orthogonal_det16": wh_ortho_ok,
        },
        "prompt_decay_dimensionless": {
            "g_critical_for_1e_minus_3": mp.nstr(g_crit, 20),
            "benchmarks": decay_rates,
        },
        "spin10_z4_center_matter_parity": {
            "n_adjoint_total": len(adj_states),
            "n_G_SM": len(gsm_states),
            "n_broken_proca": len(proca_states),
            "all_45_P_M_plus1": all_45_pm_plus1,
            "all_45_c2_plus1": all_45_c2_plus1,
            "spinor_16_3BL_eigenvalues_sorted": sorted(spinor_3bl_eigs),
            "spinor_16_QX_eigenvalues_sorted": sorted(spinor_qx_eigs),
            "all_16_P_M_minus1": all_16_pm_minus1,
            "all_16_c2_minus1": all_16_c2_minus1,
            "all_16_QX_eq_1_mod_4_Z4_center": spinor_z4_mod4_ok,
        },
        "gates": gates_c,
    }


# =============================================================================
# OW11-D: Independent Verification of All 4/4 Planted Faults (PF-OW11-1..4)
# =============================================================================

def compute_ow11_d(cl: dict[str, Any], ow11_a: dict[str, Any], ow11_c: dict[str, Any]) -> dict[str, Any]:
    """Independently construct and verify all 4 planted faults catch cleanly."""
    gammas = cl["gammas"]
    pos_indices = cl["pos_indices"]
    pairs = cl["pairs"]
    sigmas16 = cl["sigmas16"]

    # PF-OW11-1: Replace P_PS = diag(+1^6, -1^4) with P_fault = diag(+1^8, -1^2) -> so(8)+so(2) (dim=29 != 21)
    # Verify BOTH via root system AND via 16x16 spinor lift S_fault = Gamma_9 Gamma_10 (note (G9 G10)^2 = -I, so S^{-1} = -S)
    p_fault_planes = [1, 1, 1, 1, -1]
    fault_even_roots = [
        (i, j, si, sj)
        for i in range(5) for j in range(i + 1, 5)
        for si in (-1, 1) for sj in (-1, 1)
        if p_fault_planes[i] * p_fault_planes[j] == 1
    ]
    dim_pf1_root = 5 + len(fault_even_roots)

    s_f_32 = mat_mul(gammas[8], gammas[9])
    s_f_16 = [[s_f_32[i][j] for j in pos_indices] for i in pos_indices]
    s_f_16_inv = g_scale(GMOne, s_f_16)
    inv_4 = Fraction(1, 4)
    tr_proj_pf1 = Fraction(0, 1)
    for p_ab in pairs:
        sig = sigmas16[p_ab]
        conj_f = mat_mul(mat_mul(s_f_16, sig), s_f_16_inv)
        diag_entry = mat_trace(mat_mul(sig, conj_f))[0] * inv_4
        tr_proj_pf1 += (Fraction(1, 1) + diag_entry) * Fraction(1, 2)
    dim_pf1_spin = int(tr_proj_pf1)
    pf1_caught = (dim_pf1_root == 29) and (dim_pf1_spin == 29) and (dim_pf1_root != 21)

    # PF-OW11-2: Bulk complex 10 (+10/pt) shifts supertrace to +4 > 0 -> AdS negative V_Cas, unstable local maximum
    cplx10 = ow11_a["casimir_6d_supertraces"]["configs"]["bulk_complex_10"]
    pf2_caught = (
        cplx10["supertrace_nB_minus_nF"] == 4
        and (not cplx10["is_positive_dS"])
        and (not cplx10["stabilizes_tau_hex"])
    )

    # PF-OW11-3: Omitting (3/4)(tr_10 F^2)^2 in tr_16(F^4) on Cartan (1, 1, 0, 0, 0)
    # Compute directly via 16x16 matrix multiplication M^4
    m16_11 = mat_add(sigmas16[(0, 1)], sigmas16[(2, 3)])
    m16_11_2 = mat_mul(m16_11, m16_11)
    m16_11_4 = mat_mul(m16_11_2, m16_11_2)
    true_tr16_f4 = mat_trace(m16_11_4)[0]
    # Vector-10 M10 for (1, 1, 0, 0, 0): eigenvalues (+1,-1,+1,-1,0^6) -> tr_10(F^4) = 4
    m10_11 = mat_zero(10)
    m10_11[0][1], m10_11[1][0] = GMI, GI
    m10_11[2][3], m10_11[3][2] = GMI, GI
    m10_11_2 = mat_mul(m10_11, m10_11)
    m10_11_4 = mat_mul(m10_11_2, m10_11_2)
    faulty_tr16_f4 = -mat_trace(m10_11_4)[0]
    pf3_residual = true_tr16_f4 - faulty_tr16_f4
    pf3_caught = (pf3_residual != 0) and (true_tr16_f4 == Fraction(8, 1)) and (faulty_tr16_f4 == Fraction(-4, 1))

    # PF-OW11-4: Treating E[2] \ {0} as Z_2 x Z_2 conserving (C_3 == 0 on non-trivial grades) fails vs -1
    c3_nontrivial = ow11_c["walsh_hadamard_fourier"]["C_3_gen_E2_minus_0"][1:]
    pf4_max_abs = max(abs(x) for x in c3_nontrivial)
    pf4_caught = (pf4_max_abs == 1) and all(x == -1 for x in c3_nontrivial)

    gates_d = {
        "PF_OW11_1_caught": pf1_caught,
        "PF_OW11_2_caught": pf2_caught,
        "PF_OW11_3_caught": pf3_caught,
        "PF_OW11_4_caught": pf4_caught,
    }
    return {
        "PF_OW11_1": {"dim_root": dim_pf1_root, "dim_spinor": dim_pf1_spin, "expected_ps_dim": 21, "caught": pf1_caught},
        "PF_OW11_2": {"supertrace": cplx10["supertrace_nB_minus_nF"], "V_Cas_at_hex": cplx10["V_Cas_at_tau_hex"], "caught": pf2_caught},
        "PF_OW11_3": {
            "cartan": [1, 1, 0, 0, 0],
            "true_tr16_F4": frac_str(true_tr16_f4),
            "faulty_minus_tr10_F4": frac_str(faulty_tr16_f4),
            "residual": frac_str(pf3_residual),
            "caught": pf3_caught,
        },
        "PF_OW11_4": {"C_3_nontrivial": c3_nontrivial, "max_abs_violation": pf4_max_abs, "caught": pf4_caught},
        "n_caught": sum(1 for v in gates_d.values() if v),
        "gates": gates_d,
    }


def main() -> None:
    cl = build_cl10_and_16plus()
    ow11_a = compute_ow11_a(cl)
    ow11_b = compute_ow11_b()
    ow11_c = compute_ow11_c(cl)
    ow11_d = compute_ow11_d(cl, ow11_a, ow11_c)

    first_principles_gates = {
        **ow11_a["gates"],
        "frg_all_12_cases_sturm_newton_verified": ow11_b["gates"]["frg_all_12_cases_sturm_newton_verified"],
        "unification_sm2h_and_kk_brane_match_card": ow11_b["gates"]["unification_sm2h_and_kk_brane_match_card"],
        "unification_kk_bulk_2h_first_principles_lt_5_over_7": ow11_b["gates"]["unification_kk_bulk_2h_first_principles_lt_5_over_7"],
        "pati_salam_first_principles_1x122_closes_5_over_7_and_su2L_continuous": ow11_b["gates"]["pati_salam_first_principles_1x122_closes_5_over_7_and_su2L_continuous"],
        "proton_lifetime_enhancement_gt_3e10": ow11_b["gates"]["proton_lifetime_enhancement_gt_3e10"],
        **ow11_c["gates"],
        **ow11_d["gates"],
    }

    card_literal_match_gates = {
        **ow11_a["gates"],
        **ow11_b["gates"],
        **ow11_c["gates"],
        **ow11_d["gates"],
    }

    out = {
        "card_id": "AGY-002_A2-OW11",
        "role": "independent_cold_room_zero_trust_referee",
        "empirical_firewall": "0_of_19",
        "OW11_A": ow11_a,
        "OW11_B": ow11_b,
        "OW11_C": ow11_c,
        "OW11_D": ow11_d,
        "summary": {
            "all_first_principles_physics_gates_passed": all(first_principles_gates.values()),
            "all_card_literal_number_gates_passed": all(card_literal_match_gates.values()),
            "failed_card_literal_gates": [k for k, v in card_literal_match_gates.items() if not v],
            "n_first_principles_gates_passed": sum(1 for v in first_principles_gates.values() if v),
            "n_first_principles_gates_total": len(first_principles_gates),
            "n_card_literal_gates_passed": sum(1 for v in card_literal_match_gates.values() if v),
            "n_card_literal_gates_total": len(card_literal_match_gates),
        },
    }

    out_path = Path(__file__).resolve().parent / "referee_a2_ow11_out.json"
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
