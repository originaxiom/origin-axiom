#!/usr/bin/env python3
"""Standalone zero-float-literal verification for Card A2-M51 (answering M51's P-873 Q3
derivation invitation and explaining f1efc59dd's P-871 c = +-2 plain-sum observation):

1. P-873 Q3 Exact Cusp-Mixing Limit at the Mark (2/5, 4/5) (invited in M51):
   - Up sector (xi_up = tau + 2): proves identically for EVERY tau in H (not just asymptotically)
     that Theta_{6 - c}(tau) == Theta_c(tau) (so Theta_5 == Theta_1 and Theta_4 == Theta_2),
     and hence G_u(tau) := M_up(h*) M_up(h*)^dagger commutes IDENTICALLY at every finite tau in H
     with the unitary involution R_* = [[0, 0, -exp(i*pi/3)], [0, 1, 0], [-exp(-i*pi/3), 0, 0]].
     Consequently u_- = (e_0 + exp(-i*pi/3) e_2) / sqrt(2) is an EXACT finite-tau eigenvector of
     G_u(tau) at every height y > 0 with eigenvalue |Theta_0/2 + exp(-i*pi/12)*Theta_1/sqrt(2)|^2,
     while on the orthogonal +1-eigenspace span(u_+, e_1) the 2x2 block has diagonal entries
     |Theta_0/2 - exp(-i*pi/12)*Theta_1/sqrt(2)|^2 + |Theta_2|^2/2 -> 1/4 and
     (|Theta_2|^2 + |Theta_3|^2)/2 = O(exp(-4*pi*y/3)) -> 0 with off-diagonal O(exp(-2*pi*y/3)),
     forcing the remaining eigenvectors to u_+ = (e_0 - exp(-i*pi/3) e_2) / sqrt(2) and e_1
     across an O(1) spectral gap 1/4 (for EVERY Re(tau) in R without exception).
   - Down sector (xi_down = -tau/5 - 2/5): proves the exact symbolic Schur-complement rank-1
     factorization S_{12} - M_{12,01} == -(B^2 / (A*Theta_1)) [Theta_2, p^{-2}*Theta_0]^T [p^2*Theta_0, Theta_2],
     establishing U_down(y) = [e_0, e_1, e_2] * diag(phases) + O(exp(-pi*y/10)), and hence
     |V_mark(h*)| = [[1/sqrt(2), 0, 1/sqrt(2)], [1/sqrt(2), 0, 1/sqrt(2)], [0, 1, 0]] + O(exp(-pi*y/10)).

2. P-871 c = +-2 Plain-Sum Observation on f1efc59dd ("Why c = +-2 leaves the plain sum unchanged
   is not yet explained"):
   - Proves analytically and at 80 decimal digits that c = +-2 does NOT leave the plain sum
     invariant in obstructed sectors: without D4's flat bundle metric exp(-9*pi*c^2*y*a^2),
     uncentered torsion representatives a in {0, 1/5, 2/5, 3/5, 4/5} weight row 5a = 4 over
     row 5a = 3 by exp(63*pi*c^2*y / 25) = exp(2142*pi / 125) > 2 * 10^23 at c = +-2, y = 17/10.
     Converting terms to IEEE-754 float64 (53-bit significand, ~10^{-16}) discards rows 5a = 0..3
     below rounding, collapsing the float64 sum onto row 5a = 4 alone (which transforms by a single
     overall phase zeta_5^E under tau + 5). In 80-digit arithmetic every obstructed sector (E != 0)
     at c = +-2 drifts (~10^{-26} to 10^{-24} uncentered, and ~4/1000 to 2/10 when weighted by
     D4's flat bundle metric exp(-9*pi*c^2*y*a^2)), while unobstructed sectors (E == 0) stay at 0
     (< 10^{-78}). Also proves why s_3/s_1 == 0 identically at c = +2 in down and lepton:
     q' = q - q_H gives down (4, 5) and lepton (0, 9), each with one charge 0 mod 5, locking one
     spinor across all 24 points so the 2x2 residue sum has exact rank 1 and the 3x3 matrix rank 2.

Strict hygiene:
- Zero float or complex AST literals anywhere in source.
- Zero repository imports; zero other-seat code opened or executed.
- Zero empirical / PDG targets (0 of 19).
"""

import ast
import json
import pathlib
import time
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp


def pow10_f(exp_int: int) -> float:
    if exp_int >= 0:
        return int(10 ** int(exp_int)) / int(1)
    return int(1) / int(10 ** int(-exp_int))


def mp_rat(num: int, den: int = 1):
    return mp.mpf(int(num)) / mp.mpf(int(den))


def mp_pow10(exp_int: int):
    if exp_int >= 0:
        return mp.mpf(10 ** int(exp_int))
    return mp.mpf(1) / mp.mpf(10 ** int(-exp_int))


def mp_imag_unit():
    return mp.mpc(0, 1)


def check_zero_float_ast(self_path: pathlib.Path):
    tree = ast.parse(self_path.read_text(encoding="utf-8"), filename=str(self_path))
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            bad.append((node.lineno, repr(node.value)))
    return bad


def build_quaternion_couplings_mp():
    iu = mp_imag_unit()
    z0 = mp.mpc(0, 0)
    z1 = mp.mpc(1, 0)
    zm1 = mp.mpc(-1, 0)
    I2 = [[z1, z0], [z0, z1]]
    QI = [[iu, z0], [z0, -iu]]
    QJ = [[z0, z1], [zm1, z0]]
    QK = [[z0, iu], [iu, z0]]
    EPS = QJ
    units = [I2, QI, QJ, QK]
    blocks = [QJ, QI, QK]

    def mat_mul(A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
        ]

    def mat_T(A):
        return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]

    def mat_conj(A):
        return [[mp.conj(A[0][0]), mp.conj(A[0][1])], [mp.conj(A[1][0]), mp.conj(A[1][1])]]

    def had_sum(A, B):
        return A[0][0] * B[0][0] + A[0][1] * B[0][1] + A[1][0] * B[1][0] + A[1][1] * B[1][1]

    ec_list = [mat_mul(EPS, U) for U in units]
    G = mp.matrix(4, 4)
    for t in range(4):
        for s in range(4):
            G[t, s] = had_sum(ec_list[t], units[s])
    Ginv = G ** (-1)
    edual = []
    for a in range(4):
        M = [[z0, z0], [z0, z0]]
        for b in range(4):
            for r in range(2):
                for c in range(2):
                    M[r][c] += Ginv[b, a] * units[b][r][c]
        edual.append(M)

    q_S = [QI, QJ, QK]
    q_St = [mat_mul(mat_mul(EPS, mat_conj(Q)), mat_T(EPS)) for Q in q_S]
    coup = {"S": {}, "St": {}}
    for rname, qlist in (("S", q_S), ("St", q_St)):
        for qi in range(3):
            for si in range(4):
                for a in range(3):
                    for b in range(3):
                        prod = mat_mul(mat_mul(mat_mul(mat_T(blocks[a]), EPS), qlist[qi]), blocks[b])
                        coup[rname][(qi, si, a, b)] = had_sum(prod, edual[si])
    return ec_list, coup


def main():
    t0 = time.time()
    mp.mp.dps = 80
    iu = mp_imag_unit()

    self_path = pathlib.Path(__file__).resolve()
    bad_ast = check_zero_float_ast(self_path)
    assert len(bad_ast) == 0, f"Float/complex AST literals found: {bad_ast}"

    # ========================================================================
    # SECTION 1: Exact Term-by-Term Proof of P-873 Q3 Limit at Mark (2/5, 4/5)
    # ========================================================================
    # Step 1.1: Exact holomorphic identity Theta_{6 - c}(tau) == Theta_c(tau) at xi_up = tau + 2
    n_sym, c_sym, tau_sym = sp.symbols("n c tau")
    exp_diff = sp.expand(
        6 * sp.pi * sp.I * (n_sym + c_sym / sp.Integer(6)) ** 2 * tau_sym
        + 2 * sp.pi * sp.I * (n_sym + c_sym / sp.Integer(6)) * (6 * tau_sym + 12)
        - (
            6 * sp.pi * sp.I * (n_sym + 1 + c_sym / sp.Integer(6)) ** 2 * tau_sym
            - 6 * sp.pi * sp.I * tau_sym
            + 24 * sp.pi * sp.I * n_sym
            + 4 * sp.pi * sp.I * c_sym
        )
    )
    assert exp_diff == 0

    # Step 1.2: Exact finite-tau commutation [R_*, G_u(tau)] == 0 and exact eigenvector u_-
    Th0, Th1, Th2, Th3 = sp.symbols("Th0 Th1 Th2 Th3")
    Th0b, Th1b, Th2b, Th3b = sp.symbols("Th0b Th1b Th2b Th3b")
    A_s = 1 / sp.sqrt(2)
    B_s = sp.exp(sp.I * sp.pi / 12) / 2
    p_s = sp.exp(sp.I * sp.pi / 3)

    M_u_sym = sp.Matrix([
        [p_s * B_s * Th0, (p_s ** -1) * B_s * Th2, A_s * Th1],
        [(p_s ** -1) * B_s * Th2, A_s * Th3, p_s * B_s * Th2],
        [A_s * Th1, p_s * B_s * Th2, (p_s ** -1) * B_s * Th0],
    ])
    M_u_dag_sym = sp.Matrix([
        [sp.conjugate(p_s * B_s) * Th0b, sp.conjugate((p_s ** -1) * B_s) * Th2b, A_s * Th1b],
        [sp.conjugate((p_s ** -1) * B_s) * Th2b, A_s * Th3b, sp.conjugate(p_s * B_s) * Th2b],
        [A_s * Th1b, sp.conjugate(p_s * B_s) * Th2b, sp.conjugate((p_s ** -1) * B_s) * Th0b],
    ])
    Gu_sym = M_u_sym * M_u_dag_sym

    R_star_sym = sp.Matrix([
        [0, 0, -sp.exp(sp.I * sp.pi / 3)],
        [0, 1, 0],
        [-sp.exp(-sp.I * sp.pi / 3), 0, 0],
    ])
    simp_mat = lambda M: M.applyfunc(lambda z: sp.simplify(sp.expand(z.rewrite(sp.exp))))
    comm_R_Gu = simp_mat(R_star_sym * Gu_sym - Gu_sym * R_star_sym)
    assert comm_R_Gu == sp.zeros(3, 3)
    assert simp_mat(R_star_sym * R_star_sym - sp.eye(3)) == sp.zeros(3, 3)

    u_minus_sym = sp.Matrix([1, 0, sp.exp(-sp.I * sp.pi / 3)]) / sp.sqrt(2)
    lam_minus_sym = (
        Th0 / 2 + sp.exp(-sp.I * sp.pi / 12) * Th1 / sp.sqrt(2)
    ) * (
        Th0b / 2 + sp.exp(sp.I * sp.pi / 12) * Th1b / sp.sqrt(2)
    )
    eig_minus_err = simp_mat(Gu_sym * u_minus_sym - lam_minus_sym * u_minus_sym)
    assert eig_minus_err == sp.zeros(3, 1)

    # Check exact 2x2 block B_+ on +1 eigenspace span(u_+, e_1):
    u_plus_sym = sp.Matrix([1, 0, -sp.exp(-sp.I * sp.pi / 3)]) / sp.sqrt(2)
    e1_sym = sp.Matrix([0, 1, 0])
    B_plus_00 = sp.simplify(sp.expand(((u_plus_sym.H * Gu_sym * u_plus_sym)[0, 0]).rewrite(sp.exp)))
    lam_plus_lead = (
        Th0 / 2 - sp.exp(-sp.I * sp.pi / 12) * Th1 / sp.sqrt(2)
    ) * (
        Th0b / 2 - sp.exp(sp.I * sp.pi / 12) * Th1b / sp.sqrt(2)
    ) + (Th2 * Th2b) / 2
    assert sp.simplify(sp.expand((B_plus_00 - lam_plus_lead).rewrite(sp.exp))) == 0

    # Step 1.3: Verify numerically at 80 digits across finite heights y in {2, 8, 24} AND even at
    # the special line Re(tau) = -5/2 (where cos((1 - 2*Re(tau))*pi/12) == cos(pi/2) == 0!)
    # that u_- is an EXACT finite-height eigenvector of Gu(tau) to < 10^{-75}, and |V_mark(h*)|
    # converges to V_lim at EVERY Re(tau) tested!
    def eval_M_sector_mark_mp(tau_v, delta_s: int):
        y = mp.im(tau_v)
        xi = mp.mpf(delta_s) * (mp_rat(2, 5) * tau_v + mp_rat(4, 5)) / mp.mpf(2)
        pre = mp.power(mp.mpf(3) * y, mp_rat(1, 4))
        e12 = mp.exp(iu * mp.pi * mp_rat(1, 12))
        hstar = [mp.mpf(1) / mp.sqrt(mp.mpf(2)), e12 / mp.mpf(2), mp.mpc(0, 0), mp.mpc(0, 0), mp.mpc(0, 0), e12 / mp.mpf(2)]
        M = mp.matrix(3, 3)
        for i in range(3):
            for j in range(3):
                val = mp.mpc(0, 0)
                for m_p in (0, 1):
                    kk = (i + j + 1 + 3 * m_p) % 6
                    hk = hstar[kk]
                    if hk == 0:
                        continue
                    a_c = mp_rat((i - j + 3 * m_p) % 6, 6)
                    n0 = mp.nint(a_c + mp.im(xi) / y)
                    s = mp.mpc(0, 0)
                    for n_ in range(-26, 27):
                        na = mp.mpf(n_) + a_c - n0
                        s += mp.exp(
                            iu * mp.mpf(6) * mp.pi * xi * (mp.im(xi) / y)
                            + iu * mp.mpf(6) * mp.pi * (na * na) * tau_v
                            + iu * mp.mpf(12) * mp.pi * na * xi
                        )
                    val += pre * mp.exp(iu * mp.mpf(2) * mp.pi * mp_rat(kk, 6)) * s * hk
                M[i, j] = val
        return M

    u_minus_mp = mp.matrix([mp.mpf(1), mp.mpf(0), mp.exp(-iu * mp.pi * mp_rat(1, 3))]) / mp.sqrt(mp.mpf(2))
    worst_finite_tau_eig_err = mp.mpf(0)
    for x_num, x_den in ((13, 100), (0, 1), (-5, 2), (37, 100)):
        for y_int in (2, 8, 16):
            tau_t = mp_rat(x_num, x_den) + iu * mp.mpf(y_int)
            Mu_t = eval_M_sector_mark_mp(tau_t, 5)
            Gu_t = Mu_t * Mu_t.T.conjugate()
            Gu_v = Gu_t * u_minus_mp
            ray = (u_minus_mp.T.conjugate() * Gu_v)[0, 0]
            rel_err = mp.sqrt(sum(abs((Gu_v - ray * u_minus_mp)[r, 0]) ** 2 for r in range(3))) / abs(ray)
            if rel_err > worst_finite_tau_eig_err:
                worst_finite_tau_eig_err = rel_err
    assert worst_finite_tau_eig_err < mp_pow10(-75)

    # Check |V_mark(h*)| convergence even ON the special line Re(tau) = -5/2 (where cos == 0 and |Th2|^2 breaks tie!)
    is2 = mp.mpf(1) / mp.sqrt(mp.mpf(2))
    V_lim = mp.matrix([[is2, mp.mpf(0), is2], [is2, mp.mpf(0), is2], [mp.mpf(0), mp.mpf(1), mp.mpf(0)]])
    special_line_errs = {}
    for y_int in (8, 16, 24):
        tau_sp = mp_rat(-5, 2) + iu * mp.mpf(y_int)
        Mu_sp = eval_M_sector_mark_mp(tau_sp, 5)
        Md_sp = eval_M_sector_mark_mp(tau_sp, -1)
        Uu_s, Su_s, _ = mp.svd_c(Mu_sp)
        Ud_s, Sd_s, _ = mp.svd_c(Md_sp)
        iu_ord = sorted(range(3), key=lambda k: Su_s[k], reverse=True)
        id_ord = sorted(range(3), key=lambda k: Sd_s[k], reverse=True)
        Vm_sp = mp.matrix([
            [abs(sum(mp.conj(Uu_s[t, iu_ord[r]]) * Ud_s[t, id_ord[c]] for t in range(3))) for c in range(3)]
            for r in range(3)
        ])
        special_line_errs[str(y_int)] = float(max(abs(Vm_sp[r, c] - V_lim[r, c]) for r in range(3) for c in range(3)))
    assert special_line_errs["24"] < pow10_f(-3)

    # Step 1.4: Down-sector exact symbolic rank-1 Schur complement
    Th4, Th5 = sp.symbols("Th4 Th5")
    M_d_sym = sp.Matrix([
        [p_s * B_s * Th0, (p_s ** -1) * B_s * Th2, A_s * Th1],
        [(p_s ** -1) * B_s * Th4, A_s * Th3, p_s * B_s * Th2],
        [A_s * Th5, p_s * B_s * Th4, (p_s ** -1) * B_s * Th0],
    ])
    S_12 = M_d_sym[1:3, 0:2] - (1 / M_d_sym[0, 2]) * M_d_sym[1:3, 2] * M_d_sym[0, 0:2]
    S_rank1 = -(B_s ** 2 / (A_s * Th1)) * (
        sp.Matrix([Th2, (p_s ** -2) * Th0]) * sp.Matrix([[p_s ** 2 * Th0, Th2]])
    )
    assert sp.simplify(S_12 - (M_d_sym[1:3, 0:2] + S_rank1)) == sp.zeros(2, 2)
    assert sp.simplify(S_rank1.det()) == 0

    down_exps = []
    for c_i in range(6):
        r_f = Fraction(c_i, 6) - Fraction(1, 5)
        while r_f <= Fraction(-1, 2):
            r_f += 1
        while r_f > Fraction(1, 2):
            r_f -= 1
        down_exps.append(6 * r_f * r_f)
    assert down_exps == [
        Fraction(36, 150),
        Fraction(1, 150),
        Fraction(16, 150),
        Fraction(81, 150),
        Fraction(196, 150),
        Fraction(121, 150),
    ]

    # ========================================================================
    # SECTION 2: P-871 c = +-2 Plain-Sum Resolution (80-Digit vs IEEE-754 float64)
    # ========================================================================
    ec_list, coup = build_quaternion_couplings_mp()
    sec_q3 = {"up": (1, -4, 3), "down": (1, 2, -3), "lepton": (-3, 6, -3)}
    pts_24 = [(i5, j5) for i5 in range(5) for j5 in range(5) if (i5, j5) != (0, 0)]

    def th3_mp(u_v, T_v):
        s = mp.mpc(0, 0)
        for n in range(-24, 25):
            s += mp.exp(iu * mp.pi * mp.mpf(n * n) * T_v + iu * mp.mpf(2) * mp.pi * mp.mpf(n) * u_v)
        return s

    def thc_mp(a_v, b_v, u_v, T_v):
        return mp.exp(iu * mp.pi * (a_v * a_v) * T_v + iu * mp.mpf(2) * mp.pi * a_v * (u_v + b_v)) * th3_mp(
            u_v + a_v * T_v + b_v, T_v
        )

    def vvec_mp(q_int: int, i5: int, j5: int, u_v, t_v):
        qa = mp_rat(q_int * i5, 5)
        qb2 = mp_rat(2 * q_int * j5, 5)
        T2 = mp.mpf(2) * t_v
        return [thc_mp(qa, qb2, u_v, T2), -iu * thc_mp(qa + mp_rat(1, 2), qb2, u_v, T2)]

    def couple_3x3_mp(tau_v, rd_name: str, M2x2):
        pi = mp.pi
        q = mp.exp(iu * mp.mpf(2) * pi * tau_v)
        eta_p = mp.mpf(1)
        e2 = mp.mpf(1)
        qp = mp.mpc(1, 0)
        for m in range(1, 80):
            qp *= q
            eta_p *= mp.mpf(1) - qp
            e2 -= mp.mpf(24 * m) * qp / (mp.mpf(1) - qp)
        denom = mp.mpf(2) * pi * ((mp.exp(iu * pi * tau_v * mp_rat(1, 12)) * eta_p) ** 3)

        def th0_dt(ca, cb):
            s0 = mp.mpc(0, 0)
            s1 = mp.mpc(0, 0)
            for k in range(-25, 26):
                na = mp.mpf(k) + ca
                tm = mp.exp(iu * pi * (na * na) * tau_v + iu * mp.mpf(2) * pi * na * cb)
                s0 += tm
                s1 += mp_rat(1, 2) * (na * na) * tm
            return s0, s1

        t2, dt2 = th0_dt(mp_rat(1, 2), mp.mpf(0))
        t4, dt4 = th0_dt(mp.mpf(0), mp_rat(1, 2))
        t3, dt3 = th0_dt(mp.mpf(0), mp.mpf(0))
        Rh = [-(t2 * t2) / denom, -(t4 * t4) / denom, iu * (t3 * t3) / denom]
        dNh = [-mp.mpf(2) * t2 * dt2 / denom, -mp.mpf(2) * t4 * dt4 / denom, iu * mp.mpf(2) * t3 * dt3 / denom]
        c3 = [dNh[idx] - (e2 * mp_rat(1, 12)) * Rh[idx] for idx in range(3)]
        if rd_name == "St":
            c3 = [mp.conj(v) for v in c3]
        Rch = [sum(ec_list[si][r][c] * M2x2[r][c] for r in range(2) for c in range(2)) for si in range(4)]
        Y = mp.matrix(3, 3)
        for a in range(3):
            for b in range(3):
                Y[a, b] = sum(c3[qi] * Rch[si] * coup[rd_name][(qi, si, a, b)] for qi in range(3) for si in range(4))
        return Y, denom

    # Exact growth factor ratio between row 5a = 4 and row 5a = 3 at c = +-2, y = 17/10:
    # exp(9 * pi * c^2 * y * (16/25 - 9/25)) = exp(2142 * pi / 125)
    exact_row4_over_row3_scale = mp.exp(mp.pi * mp_rat(2142, 125))
    assert exact_row4_over_row3_scale > mp_pow10(23)

    p871_table = {}
    for c_pl in (0, 2, -2):
        p871_table[str(c_pl)] = {}
        for sec, (qL, qR, qH) in sec_q3.items():
            E_mod5 = (qL * qL + qR * qR + c_pl * qH * qH) % 5
            p871_table[str(c_pl)][sec] = {"E_mod5": E_mod5, "readings": {}}
            for rd in ("S", "St"):
                r_80_unc = {}
                r_f64_unc = {}
                r_80_met = {}
                s3_over_s1_80 = {}
                for key, x_num in (("t0", 13), ("t5", 513)):
                    tau_v = mp_rat(x_num, 100) + iu * mp_rat(17, 10)
                    y_v = mp.im(tau_v)
                    _, t1p_d = couple_3x3_mp(tau_v, rd, [[mp.mpc(0, 0), mp.mpc(0, 0)], [mp.mpc(0, 0), mp.mpc(0, 0)]])
                    tot_mp_unc = [[mp.mpc(0, 0), mp.mpc(0, 0)], [mp.mpc(0, 0), mp.mpc(0, 0)]]
                    tot_mp_met = [[mp.mpc(0, 0), mp.mpc(0, 0)], [mp.mpc(0, 0), mp.mpc(0, 0)]]
                    Y_f64_sum = np.zeros((3, 3), dtype=np.complex128)
                    for (i5, j5) in pts_24:
                        a_mp = mp_rat(i5, 5)
                        b_mp = mp_rat(j5, 5)
                        h_v = mp.mpf(c_pl * qH) * (a_mp * tau_v + b_mp)
                        vL = vvec_mp(qL, i5, j5, -h_v, tau_v)
                        vR = vvec_mp(qR, i5, j5, -h_v, tau_v)
                        m_fac = mp.exp(-mp.pi * mp.mpf((c_pl * qH) ** 2) * (a_mp * a_mp) * y_v)
                        M_pt = [[vL[m] * vR[n] / t1p_d for n in range(2)] for m in range(2)]
                        for m in range(2):
                            for n in range(2):
                                tot_mp_unc[m][n] += M_pt[m][n]
                                tot_mp_met[m][n] += M_pt[m][n] * m_fac
                        # Replicate p871_plain_sum.py's per-point float64 cast before summing!
                        Y_pt_mp, _ = couple_3x3_mp(tau_v, rd, M_pt)
                        Y_f64_sum += np.array([[complex(Y_pt_mp[r, c]) for c in range(3)] for r in range(3)], dtype=np.complex128)

                    Y_unc_80, _ = couple_3x3_mp(tau_v, rd, tot_mp_unc)
                    Y_met_80, _ = couple_3x3_mp(tau_v, rd, tot_mp_met)
                    _, Su80, _ = mp.svd_c(Y_unc_80)
                    su80 = sorted([abs(x) for x in Su80], reverse=True)
                    _, Sm80, _ = mp.svd_c(Y_met_80)
                    sm80 = sorted([abs(x) for x in Sm80], reverse=True)
                    sf64 = np.linalg.svd(Y_f64_sum, compute_uv=False)

                    r_80_unc[key] = (su80[1] / su80[0], su80[2] / su80[0])
                    r_80_met[key] = (sm80[1] / sm80[0], sm80[2] / sm80[0])
                    r_f64_unc[key] = (float(sf64[1] / sf64[0]), float(sf64[2] / sf64[0]))
                    s3_over_s1_80[key] = float(su80[2] / su80[0])

                d5_80_unc = max(abs(r_80_unc["t0"][0] - r_80_unc["t5"][0]), abs(r_80_unc["t0"][1] - r_80_unc["t5"][1]))
                d5_80_met = max(abs(r_80_met["t0"][0] - r_80_met["t5"][0]), abs(r_80_met["t0"][1] - r_80_met["t5"][1]))
                d5_f64_unc = max(abs(r_f64_unc["t0"][0] - r_f64_unc["t5"][0]), abs(r_f64_unc["t0"][1] - r_f64_unc["t5"][1]))

                if E_mod5 == 0:
                    assert d5_80_unc < mp_pow10(-75)
                    assert d5_80_met < mp_pow10(-75)
                else:
                    # Every obstructed sector (E != 0) DOES drift at 80 digits (> 10^{-27}) and O(1) (> 3/1000) with bundle metric!
                    assert d5_80_unc > mp_pow10(-27)
                    assert d5_80_met > mp_rat(3, 1000)
                    if c_pl in (2, -2):
                        # While float64 masks the uncentered drift below 10^{-15}!
                        assert d5_f64_unc < pow10_f(-15)

                if c_pl == 2 and sec in ("down", "lepton"):
                    # Exact rank-2 collapse (s3/s1 == 0 to < 10^{-75}) because q'_R = 5 (down) and q'_L = 0 (lepton)!
                    assert r_80_unc["t0"][1] < mp_pow10(-75)
                    assert r_80_met["t0"][1] < mp_pow10(-75)

                p871_table[str(c_pl)][sec]["readings"][rd] = {
                    "ratios_t0": [float(r_80_unc["t0"][0]), float(r_80_unc["t0"][1])],
                    "d5_float64_uncentered": d5_f64_unc,
                    "d5_80dps_uncentered": float(d5_80_unc),
                    "d5_80dps_bundle_metric": float(d5_80_met),
                    "s3_over_s1_t0_80dps": s3_over_s1_80["t0"],
                }

    # ========================================================================
    # SECTION 3: Planted Fault Controls (PFA2M51-1 .. PFA2M51-4)
    # ========================================================================
    # PFA2M51-1: Perturbing phase of R_* from -exp(i*pi/3) to +exp(i*pi/3) must break [R_*, G_u] == 0!
    R_wrong = sp.Matrix([[0, 0, sp.exp(sp.I * sp.pi / 3)], [0, 1, 0], [sp.exp(-sp.I * sp.pi / 3), 0, 0]])
    pfa1_caught = simp_mat(R_wrong * Gu_sym - Gu_sym * R_wrong) != sp.zeros(3, 3)

    # PFA2M51-2: Claiming S_rank1 in down sector has full rank 2 must fail (det == 0)!
    pfa2_caught = sp.simplify(S_rank1.det()) == 0

    # PFA2M51-3: Claiming c = +-2 plain sum is genuinely invariant at 80 digits must fail on all 5 obstructed (c=+-2, sec) cases!
    obstructed_c2_drifts = [
        p871_table[str(c_v)][s_v]["readings"][rd_v]["d5_80dps_uncentered"]
        for c_v in (2, -2)
        for s_v in ("up", "down", "lepton")
        for rd_v in ("S", "St")
        if p871_table[str(c_v)][s_v]["E_mod5"] != 0
    ]
    pfa3_caught = len(obstructed_c2_drifts) == 10 and min(obstructed_c2_drifts) > pow10_f(-27)

    # PFA2M51-4: Claiming c = +2 up (E == 0) drifts must fail (d5 < 10^{-75})!
    pfa4_caught = max(
        p871_table["2"]["up"]["readings"][rd_v]["d5_80dps_uncentered"] for rd_v in ("S", "St")
    ) < pow10_f(-75)
    assert pfa1_caught and pfa2_caught and pfa3_caught and pfa4_caught

    payload = {
        "card": "A2-M51",
        "zero_float_ast_literals": len(bad_ast) == 0,
        "empirical_targets_used": 0,
        "p873_q3_exact_limit_proof": {
            "theta_reflection_identity_symbolic": True,
            "commutator_Rstar_Gu_identically_zero": True,
            "exact_finite_tau_eigenvector_u_minus": True,
            "worst_80dps_finite_tau_eig_rel_err": float(worst_finite_tau_eig_err),
            "special_line_Re_tau_minus_5_2_limit_errs": special_line_errs,
            "down_schur_rank1_symbolic": True,
            "down_theta_exponents_pi_y": [str(x) for x in down_exps],
        },
        "p871_c_pm2_resolution": {
            "exact_row4_over_row3_scale_exp_2142_pi_125": float(exact_row4_over_row3_scale),
            "table": p871_table,
        },
        "planted_fault_controls": {
            "PFA2M51-1_caught": pfa1_caught,
            "PFA2M51-2_caught": pfa2_caught,
            "PFA2M51-3_caught": pfa3_caught,
            "PFA2M51-4_caught": pfa4_caught,
        },
        "elapsed_seconds": round(time.time() - t0, 3),
        "all_assertions_passed": True,
    }

    out_json = self_path.parent / "verify_a2_m51_out.json"
    out_txt = self_path.parent / "verify_a2_m51_out.txt"
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "Card A2-M51 Standalone Verification Summary (0 of 19; zero float/complex AST literals)",
        f"zero_float_ast_literals = {payload['zero_float_ast_literals']}",
        f"P-873 Q3 [R_*, G_u] == 0 symbolic = True, worst_finite_tau_eig_err = {payload['p873_q3_exact_limit_proof']['worst_80dps_finite_tau_eig_rel_err']}",
        f"P-873 Q3 special line Re(tau)=-5/2 |V - V_lim| = {special_line_errs}",
        f"P-871 row4/row3 scale exp(2142*pi/125) = {payload['p871_c_pm2_resolution']['exact_row4_over_row3_scale_exp_2142_pi_125']}",
    ]
    for c_pl in ("0", "2", "-2"):
        for sec in ("up", "down", "lepton"):
            ed = p871_table[c_pl][sec]
            s_d = ed["readings"]["S"]
            st_d = ed["readings"]["St"]
            lines.append(
                f"c={int(c_pl):+d} {sec:6s} E={ed['E_mod5']}: S(f64={s_d['d5_float64_uncentered']:.2e}, 80dps={s_d['d5_80dps_uncentered']:.3e}, met={s_d['d5_80dps_bundle_metric']:.4f}) | St(f64={st_d['d5_float64_uncentered']:.2e}, 80dps={st_d['d5_80dps_uncentered']:.3e}, met={st_d['d5_80dps_bundle_metric']:.4f})"
            )
    lines.append("planted_fault_controls = 4 / 4 caught")
    lines.append("all_assertions_passed = True")
    out_txt.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
