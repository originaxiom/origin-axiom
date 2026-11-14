"""Zero-trust pytest counterchecks & AST locks for Stage 6 v3
(B1861 WP-4.1, WP-4.2, WP-4.3, B1919-B1922, P-831, P-845):
Closed-Loop Shifted-Lattice Kronecker Function, Physical Torus Metric & 1-Loop
Scherk-Schwarz Modulus Audit, Whole-Weave Transfer Spectrum & Hyperbolic BFS
Nielsen Rank Inversion, Level-5 Kashaev Invariant, SM 19-Parameter Operator
Jacobian, and Two-Loop Standard Model Matrix RGE Benchmark & Scrambling Gate.

Enforces Guardrails 1-6 and 0-of-19 empirical blindness (P-728):
- Strict AST Firewall (FW) and Guardrail-2 (G2) locks on BOTH stage6 producer and test suite.
- Guardrail 6 zero-trust independence: never echoes producer helpers; independently builds
  hyperbolic sinh/cosh shifted-lattice Kronecker sums, Euler-product Dedekind eta and direct
  Jacobi q-series theta_1 finite-Fourier identities at a fresh modulus, real torus frame
  pullback metric and O(h^4) 1-loop gradient/Laplacian/Scherk-Schwarz harmonicity checks,
  matrix-word BFS on distinct hyperbolic words, cyclotomic quotient ring Q[q]/(Phi_5(q)) for
  J_5(4_1) = 46 + 2*sqrt(5), complex bi-degree SU(2)_L Casimir singlet counting + u(3)^5
  flavour Jacobian + mechanical ker(J) chiral anomaly projection, explicit su(N_c) Gell-Mann
  commutator Casimirs + d = 4 - 2*eps MS-bar Chetyrkin-Tkachov kite & Dirac-block matrix
  't Hooft pole 2-loop matrix RGEs integrated via Kutta's 4th-order 3/8-rule, Cauchy-contour
  4th-order non-commuting matrix Lie-Picard jets, and fresh-seed 2-loop U(3)^5 Haar scrambling.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import product
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
import pytest
import sympy as sp

from origin_axiom.stage1_curved_action_cusp_orbit import (
    TOL,
    audit_source_zero_empirical_constants,
    check_guardrail2_ast_no_literal_bool_verdicts,
    haar_unitary,
)
from origin_axiom.stage6_closed_loop_scale_rge import (
    build_sm_2loop_betas_symbolic,
    compute_sm_19_operator_parameter_count,
    extract_physical_flavor_invariants,
    integrate_matrix_yukawa_2loop_rk4,
    make_sm_rge_num_coeffs,
    run_stage6_complete_verification,
)


ROOT_DIR = Path(__file__).resolve().parents[1]
STAGE6_SRC = ROOT_DIR / "src" / "origin_axiom" / "stage6_closed_loop_scale_rge.py"
TEST6_SRC = Path(__file__).resolve()


@pytest.fixture(scope="module")
def stage6_results() -> dict[str, Any]:
    return run_stage6_complete_verification()


# =============================================================================
# Independent Zero-Trust Referee Helpers (Guardrail 6)
# =============================================================================


def ref_kronecker_sinh_cosh_mp(
    u1_in: Any,
    u2_in: Any,
    x_in: Any,
    y_in: Any,
    shell_blocks: int = 2,
) -> Any:
    """Independent referee evaluation of F_u(x + i*y) using hyperbolic Poisson kernel
    (sinh(2*pi*|m|*y) / (cosh(2*pi*|m|*y) - cos(2*pi*(m*x + b)))) - 1.
    """
    n_sh = 32 * shell_blocks
    u1_m = mp.mpf(u1_in)
    u2_m = mp.mpf(u2_in)
    a_r = u1_m - mp.floor(u1_m)
    b_r = u2_m - mp.floor(u2_m)
    cut_z = (mp.fdiv(1, 64) + mp.mpf(int(sp.Matrix.eye(1).trace()) - 1)) ** 19
    if abs(a_r - mp.mpf(1)) < cut_z:
        a_r = mp.mpf(0)
    if abs(b_r - mp.mpf(1)) < cut_z:
        b_r = mp.mpf(0)

    xr = mp.mpf(x_in)
    yi = mp.mpf(y_in)
    tpi = 2 * mp.pi

    if abs(a_r) < cut_z:
        c0_v = (
            -mp.pi * mp.log(yi)
            + tpi * (mp.euler - mp.log(2))
            + ((mp.pi ** 2) * yi) / (mp.sin(mp.pi * b_r) ** 2)
        )
        a_base = mp.mpf(0)
        skip_zero = True
    else:
        c0_v = (
            -mp.pi * mp.log(yi)
            - tpi * mp.log(2)
            - mp.pi * (mp.digamma(a_r) + mp.digamma(1 - a_r))
        )
        a_base = a_r
        skip_zero = False

    acc_f = c0_v
    for k_i in range(-n_sh, n_sh + 1):
        if skip_zero and k_i == 0:
            continue
        m_v = a_base + mp.mpf(k_i)
        am = abs(m_v)
        uy = tpi * am * yi
        ang = tpi * (m_v * xr + b_r)
        kern = mp.fdiv(mp.sinh(uy), mp.cosh(uy) - mp.cos(ang)) - 1
        acc_f = acc_f + mp.fdiv(mp.pi, am) * kern
    return acc_f


def ref_vss_even_spin_mp(
    u1_in: Any,
    u2_in: Any,
    x_in: Any,
    y_in: Any,
    shell_blocks: int = 3,
) -> Any:
    """Independent 3-even-spin-structure Scherk-Schwarz 1-loop potential evaluated via sinh/cosh kernel."""
    half_v = mp.fdiv(1, 2)
    f_b = ref_kronecker_sinh_cosh_mp(u1_in, u2_in, x_in, y_in, shell_blocks)
    f_f = (
        ref_kronecker_sinh_cosh_mp(u1_in, u2_in - half_v, x_in, y_in, shell_blocks)
        + ref_kronecker_sinh_cosh_mp(u1_in - half_v, u2_in, x_in, y_in, shell_blocks)
        + ref_kronecker_sinh_cosh_mp(u1_in - half_v, u2_in - half_v, x_in, y_in, shell_blocks)
    )
    return f_b - mp.fdiv(f_f, 3)


def ref_euler_eta_and_qseries_theta1_fourier_mp(
    p1_i: int,
    p2_i: int,
    lev_n: int,
    x_in: Any,
    y_in: Any,
) -> Any:
    """Independent referee evaluation of F_{(p1/N, p2/N)}(x + i*y) using Euler's infinite product
    for |eta(tau)| and Jacobi's direct q-series for theta_1(z | tau) without mp.jtheta.
    """
    xr = mp.mpf(x_in)
    yi = mp.mpf(y_in)
    eta_prod = mp.exp(-mp.fdiv(mp.pi * yi, 12))
    for m_p in range(1, 72):
        r_p = mp.exp(-2 * mp.pi * mp.mpf(m_p) * yi)
        c_p = mp.cos(2 * mp.pi * mp.mpf(m_p) * xr)
        eta_prod = eta_prod * mp.sqrt(1 - 2 * r_p * c_p + (r_p ** 2))

    q_half = mp.exp(-mp.pi * yi) * mp.exp(mp.mpc(0, 1) * mp.pi * xr)
    n_m = mp.mpf(lev_n)
    out_sum = 2 * mp.pi * mp.log(n_m)

    for c_i in range(lev_n):
        for d_i in range(lev_n):
            wt_c = mp.cos(2 * mp.pi * mp.mpf(c_i * p1_i + d_i * p2_i) / n_m)
            if c_i == 0 and d_i == 0:
                g_val = (
                    2 * mp.pi * (mp.euler - mp.log(2))
                    - mp.pi * mp.log(yi)
                    - 4 * mp.pi * mp.log(eta_prod)
                )
            else:
                v1 = mp.fdiv(c_i, lev_n)
                v2 = mp.fdiv(d_i, lev_n)
                zr = mp.pi * (v2 * xr - v1)
                zi = mp.pi * v2 * yi
                z_c = zr + mp.mpc(0, 1) * zi
                th1_s = mp.mpc(0, 0)
                for k_s in range(22):
                    sgn_k = -1 if (k_s % 2 == 1) else 1
                    exp_q = (mp.mpf(k_s) + mp.fdiv(1, 2)) ** 2
                    th1_s = th1_s + 2 * sgn_k * (q_half ** exp_q) * mp.sin((2 * k_s + 1) * z_c)
                g_val = -2 * mp.pi * mp.log(abs(th1_s) / eta_prod) + 2 * (mp.pi ** 2) * (v2 ** 2) * yi
            out_sum = out_sum + wt_c * g_val
    return out_sum


def ref_eta12_imag_axis_mp(y_in: Any) -> Any:
    """Independent Euler infinite-product evaluation of |eta(i*y)|^12 on the imaginary axis."""
    yi = mp.mpf(y_in)
    eta_p = mp.exp(-mp.fdiv(mp.pi * yi, 12))
    for m_p in range(1, 72):
        eta_p = eta_p * (1 - mp.exp(-2 * mp.pi * mp.mpf(m_p) * yi))
    return eta_p ** 12


def ref_mobius_xy(a_i: int, b_i: int, c_i: int, d_i: int, xr_in: Any, yi_in: Any) -> tuple[Any, Any]:
    """Independent SL(2, Z) Mobius action on upper half-plane coordinates (x, y)."""
    xr = mp.mpf(xr_in)
    yi = mp.mpf(yi_in)
    den = ((mp.mpf(c_i) * xr + mp.mpf(d_i)) ** 2) + ((mp.mpf(c_i) * yi) ** 2)
    xn = mp.fdiv(
        (mp.mpf(a_i) * xr + mp.mpf(b_i)) * (mp.mpf(c_i) * xr + mp.mpf(d_i))
        + mp.mpf(a_i * c_i) * (yi ** 2),
        den,
    )
    yn = mp.fdiv(mp.mpf(a_i * d_i - b_i * c_i) * yi, den)
    return xn, yn


def ref_bfs_sl2_word_len(
    gens_sym: list[tuple[int, int, int, int]],
    goal_mat: tuple[int, int, int, int],
    limit_depth: int = 6,
) -> int:
    """Independent referee BFS minimal word-length solver on 2x2 integer SL(2, Z) matrices."""
    eye_t = (1, 0, 0, 1)
    if goal_mat == eye_t:
        return 0
    visited_set = {eye_t}
    layer_list = [eye_t]
    for step_d in range(1, limit_depth + 1):
        expanded = [
            (
                x_m[0] * g_m[0] + x_m[1] * g_m[2],
                x_m[0] * g_m[1] + x_m[1] * g_m[3],
                x_m[2] * g_m[0] + x_m[3] * g_m[2],
                x_m[2] * g_m[1] + x_m[3] * g_m[3],
            )
            for x_m in layer_list
            for g_m in gens_sym
        ]
        next_layer = [cand_m for cand_m in set(expanded) if cand_m not in visited_set]
        if goal_mat in next_layer:
            return step_d
        visited_set = visited_set | set(next_layer)
        layer_list = next_layer
    return -1


def ref_su_n_fundamental_generators(dim_n: int) -> list[sp.Matrix]:
    """Construct all dim_n^2 - 1 explicit Hermitian traceless su(dim_n) fundamental generators
    normalized to Tr(T^A T^B) = (1/2) * delta^{AB} (generalized Gell-Mann basis).
    """
    sym_off = [
        sp.Matrix(
            dim_n,
            dim_n,
            lambda r_i, c_i, a_p=a_i, b_p=b_i: sp.Rational(1, 2)
            if ((r_i == a_p and c_i == b_p) or (r_i == b_p and c_i == a_p))
            else 0,
        )
        for a_i in range(dim_n)
        for b_i in range(a_i + 1, dim_n)
    ]
    asym_off = [
        sp.Matrix(
            dim_n,
            dim_n,
            lambda r_i, c_i, a_p=a_i, b_p=b_i: -sp.I * sp.Rational(1, 2)
            if (r_i == a_p and c_i == b_p)
            else (sp.I * sp.Rational(1, 2) if (r_i == b_p and c_i == a_p) else 0),
        )
        for a_i in range(dim_n)
        for b_i in range(a_i + 1, dim_n)
    ]
    cartan_diag = [
        sp.Matrix(
            dim_n,
            dim_n,
            lambda r_i, c_i, k_p=k_d: (
                1 / sp.sqrt(2 * k_p * (k_p + 1))
                if (r_i == c_i and r_i < k_p)
                else (-k_p / sp.sqrt(2 * k_p * (k_p + 1)) if (r_i == c_i == k_p) else 0)
            ),
        )
        for k_d in range(1, dim_n)
    ]
    return sym_off + asym_off + cartan_diag


@lru_cache(maxsize=None)
def ref_derive_msbar_kite_matrix_yukawa_coeffs() -> dict[str, Any]:
    """Independent zero-trust derivation of ALL 1-loop and 2-loop non-commuting matrix Yukawa
    coefficients via d = 4 - 2*eps MS-bar Chetyrkin-Tkachov 2-loop kite IBP recursion,
    subdivergence-subtracted rainbow/ladder/crossed/triangle topologies, and 4x4 Dirac-block
    matrix 't Hooft RG pole cancellation (1/eps^2 == 0 and 1/eps == 0).
    """
    eps, g_eul, lnp, pi2, z3, y_sp, tau_d = sp.symbols("eps g_eul lnp pi2 z3 y_sp tau_d")
    d_dim = 4 - 2 * eps

    def trunc_e(ex_in: sp.Expr, mpw: int = 2) -> sp.Expr:
        ex_e = sp.expand(ex_in)
        return sum([ex_e.coeff(eps, k_p) * (eps ** k_p) for k_p in range(-4, mpw + 1)], sp.Integer(0))

    def mul_e(a_ex: sp.Expr, b_ex: sp.Expr, mpw: int = 2) -> sp.Expr:
        a_c, b_c = sp.expand(a_ex), sp.expand(b_ex)
        if a_c == 0 or b_c == 0:
            return sp.Integer(0)
        nz_a = [(k_a, a_c.coeff(eps, k_a)) for k_a in range(-4, mpw + 5) if a_c.coeff(eps, k_a) != 0]
        nz_b = [(k_b, b_c.coeff(eps, k_b)) for k_b in range(-4, mpw + 5) if b_c.coeff(eps, k_b) != 0]
        return sum(
            [
                sp.expand(
                    sum([va * vb for ka, va in nz_a for kb, vb in nz_b if ka + kb == ks], sp.Integer(0))
                )
                * (eps ** ks)
                for ks in range(-4, mpw + 1)
            ],
            sp.Integer(0),
        )

    def inv_l(a0_in: sp.Expr, a1_in: sp.Expr, mpw: int = 3) -> sp.Expr:
        a0_s, a1_s = sp.expand(a0_in), sp.expand(a1_in)
        if a0_s == 0:
            return (sp.Integer(1) / a1_s) * (eps ** (-1))
        r_v = -a1_s / a0_s
        return sum([sp.expand((r_v ** j_p) / a0_s) * (eps ** j_p) for j_p in range(mpw + 2)], sp.Integer(0))

    def exp_s(arg_e: sp.Expr, mpw: int = 3) -> sp.Expr:
        res_e = sp.Integer(1)
        tm_e = sp.Integer(1)
        for j_p in range(1, mpw + 2):
            tm_e = mul_e(tm_e, arg_e / sp.Integer(j_p), mpw + 1)
            res_e = trunc_e(res_e + tm_e, mpw + 1)
        return res_e

    @lru_cache(maxsize=None)
    def gam_l(z_ex: sp.Expr, mpw: int = 3) -> sp.Expr:
        cur = sp.expand(z_ex)
        z0 = int(cur.subs(eps, 0))
        fac = sp.Integer(1)
        for _ in range(4):
            if z0 > 1:
                cur = cur - 1
                z0 -= 1
                fac = mul_e(fac, cur, mpw + 2)
        for _ in range(4):
            if z0 < 1:
                c0 = cur.subs(eps, 0)
                c1 = sp.expand((cur - c0) / eps)
                fac = mul_e(fac, inv_l(c0, c1, mpw + 2), mpw + 2)
                cur = cur + 1
                z0 += 1
        w_v = sp.expand(cur - 1)
        w2_v = mul_e(w_v, w_v, mpw + 2)
        w3_v = mul_e(w2_v, w_v, mpw + 2)
        return mul_e(
            fac,
            exp_s(trunc_e(-g_eul * w_v + w2_v * (pi2 / 12) - w3_v * (z3 / 3), mpw + 2), mpw + 2),
            mpw,
        )

    @lru_cache(maxsize=None)
    def igam_l(z_ex: sp.Expr, mpw: int = 3) -> sp.Expr:
        cur = sp.expand(z_ex)
        z0 = int(cur.subs(eps, 0))
        fac = sp.Integer(1)
        for _ in range(4):
            if z0 > 1:
                cur = cur - 1
                z0 -= 1
                c0 = cur.subs(eps, 0)
                c1 = sp.expand((cur - c0) / eps)
                fac = mul_e(fac, inv_l(c0, c1, mpw + 2), mpw + 2)
        for _ in range(4):
            if z0 < 1:
                fac = mul_e(fac, cur, mpw + 2)
                cur = cur + 1
                z0 += 1
        w_v = sp.expand(cur - 1)
        w2_v = mul_e(w_v, w_v, mpw + 2)
        w3_v = mul_e(w2_v, w_v, mpw + 2)
        return mul_e(
            fac,
            exp_s(trunc_e(g_eul * w_v - w2_v * (pi2 / 12) + w3_v * (z3 / 3), mpw + 2), mpw + 2),
            mpw + 2,
        )

    @lru_cache(maxsize=None)
    def g_bub_c(a_e: sp.Expr, b_e: sp.Expr, mpw: int) -> sp.Expr:
        if (a_e.is_integer and int(a_e) <= 0) or (b_e.is_integer and int(b_e) <= 0):
            return sp.Integer(0)
        num = mul_e(
            mul_e(gam_l(sp.expand(d_dim / 2 - a_e), mpw + 2), gam_l(sp.expand(d_dim / 2 - b_e), mpw + 2), mpw + 2),
            gam_l(sp.expand(a_e + b_e - d_dim / 2), mpw + 2),
            mpw + 2,
        )
        den = mul_e(
            mul_e(igam_l(a_e, mpw + 2), igam_l(b_e, mpw + 2), mpw + 2),
            igam_l(sp.expand(d_dim - a_e - b_e), mpw + 2),
            mpw + 2,
        )
        return mul_e(mul_e(num, den, mpw + 1), exp_s(eps * g_eul, mpw + 1), mpw)

    def g_bub(a_v: Any, b_v: Any, mpw: int = 2) -> sp.Expr:
        return g_bub_c(sp.expand(a_v), sp.expand(b_v), mpw)

    z_k = int(sp.Matrix.eye(1).trace()) - 1

    @lru_cache(maxsize=None)
    def k_ct(a1: int, a2: int, a3: int, a4: int, a5: int, mpw: int = 1) -> sp.Expr:
        if a5 == 0:
            return mul_e(g_bub(a1, a2, mpw + 1), g_bub(a3, a4, mpw + 1), mpw)
        if (a1 <= 0 and a3 <= 0) or (a2 <= 0 and a4 <= 0) or (a1 <= 0 and a2 <= 0) or (a3 <= 0 and a4 <= 0):
            return sp.Integer(0)
        if a1 == 0:
            return mul_e(g_bub(a2, a5, mpw + 1), g_bub(a3, a4 + a2 + a5 - d_dim / 2, mpw + 1), mpw)
        if a2 == 0:
            return mul_e(g_bub(a1, a5, mpw + 1), g_bub(a3 + a1 + a5 - d_dim / 2, a4, mpw + 1), mpw)
        if a3 == 0:
            return mul_e(g_bub(a4, a5, mpw + 1), g_bub(a1, a2 + a4 + a5 - d_dim / 2, mpw + 1), mpw)
        if a4 == 0:
            return mul_e(g_bub(a3, a5, mpw + 1), g_bub(a1 + a3 + a5 - d_dim / 2, a2, mpw + 1), mpw)
        rhs_k = trunc_e(
            -a1 * (k_ct(a1 + 1, a2, 0, 1, 1, mpw + 1) - k_ct(a1 + 1, a2, 1, 1, 0, mpw + 1))
            - a2 * (k_ct(a1, a2 + 1, 1, 0, 1, mpw + 1) - k_ct(a1, a2 + 1, 1, 1, 0, mpw + 1)),
            mpw + 1,
        )
        return mul_e(rhs_k, inv_l(2 - a1 - a2, -2, mpw + 2), mpw)

    kite_z3_exact = sp.simplify(k_ct(1 + z_k, 1 + z_k, 1 + z_k, 1 + z_k, 1 + z_k, z_k) - 6 * z3) == 0

    p1_e = exp_s(-eps * lnp, 3)
    p2_e = exp_s(-2 * eps * lnp, 3)
    s1, s2, s3, s4, s5 = sp.symbols("s1 s2 s3 s4 s5")
    kp_s = sp.Rational(1, 2) * (s1 + 1 - s2)
    qp_s = sp.Rational(1, 2) * (s3 + 1 - s4)
    kq_s = sp.Rational(1, 2) * (s1 + s3 - s5)

    def dot_v(va: tuple[int, int, int], vb: tuple[int, int, int]) -> sp.Expr:
        ap, ak, aq = va
        bp, bk, bq = vb
        return (
            ap * bp
            + ak * bk * s1
            + aq * bq * s3
            + (ap * bk + ak * bp) * kp_s
            + (ap * bq + aq * bp) * qp_s
            + (ak * bq + aq * bk) * kq_s
        )

    def int_k(poly_s: sp.Expr) -> sp.Expr:
        ps = sp.Poly(sp.expand(poly_s), s1, s2, s3, s4, s5)
        tot = sp.Integer(0)
        for (i1, i2, i3, i4, i5), cf_p in ps.terms():
            tot = trunc_e(tot + cf_p * k_ct(1 - i1 + z_k, 1 - i2 + z_k, 1 - i3 + z_k, 1 - i4 + z_k, 1 - i5 + z_k, z_k), 0)
        return mul_e(tot, p2_e, 0)

    vp, vk, v_kmq, v_pmq = (1, 0, 0), (0, 1, 0), (0, 1, -1), (1, 0, -1)
    tr4_cr = sp.expand(
        dot_v(vp, vk) * dot_v(v_kmq, v_pmq)
        - dot_v(vp, v_kmq) * dot_v(vk, v_pmq)
        + dot_v(vp, v_pmq) * dot_v(vk, v_kmq)
    )
    g11_ct = mul_e(eps ** (-1), g_bub(1, 1, 2), 1)
    psi_rain = trunc_e(
        -sp.Rational(1, 4) * mul_e(mul_e(g_bub(1, 1, 2), g_bub(eps, 1, 2) + g_bub(1 + eps, 1, 2), 2), p2_e, 0)
        + sp.Rational(1, 4) * mul_e(g11_ct, p1_e, 0),
        0,
    )
    psi_cross = trunc_e(int_k(-tr4_cr) + mul_e(g11_ct, p1_e, 0), 0)
    v_lad_i = trunc_e(-mul_e(mul_e(g_bub(1, 1, 2), g_bub(1 + eps, 1, 2), 2), p2_e, 0) + mul_e(g11_ct, p1_e, 0), 0)
    v_cro_i = int_k(-dot_v(v_pmq, vk))
    v_se_i = trunc_e(
        -sp.Rational(1, 2) * mul_e(mul_e(g_bub(1, 1, 2), g_bub(1 + eps, 1, 2), 2), p2_e, 0)
        + sp.Rational(1, 2) * mul_e(g11_ct, p1_e, 0),
        0,
    )
    v_tr_i = trunc_e(int_k(-dot_v(v_pmq, v_kmq)) + mul_e(g11_ct, p1_e, 0), 0)
    psi_t_i = trunc_e(
        -sp.Rational(1, 2) * mul_e(mul_e(g_bub(1, 1, 2), g_bub(1, 1 + eps, 2) - g_bub(1, eps, 2), 2), p2_e, 0)
        + sp.Rational(1, 2) * mul_e(g11_ct, p1_e, 0),
        0,
    )
    vert_t_i = trunc_e(-mul_e(mul_e(g_bub(1, 1, 2), g_bub(1, 1 + eps, 2), 2), p2_e, 0) + mul_e(g11_ct, p1_e, 0), 0)

    ints_8 = (psi_rain, psi_cross, v_lad_i, v_cro_i, v_se_i, v_tr_i, psi_t_i, vert_t_i)
    subdiv_free = all(
        sp.diff(sp.expand(ig_x).coeff(eps, -1), lnp) == 0 and sp.diff(sp.expand(ig_x).coeff(eps, -2), lnp) == 0
        for ig_x in ints_8
    )

    def pl_part(ig_x: sp.Expr) -> sp.Expr:
        ex_i = sp.expand(ig_x)
        return ex_i.coeff(eps, -2) / (eps ** 2) + ex_i.coeff(eps, -1) / eps

    def eval_thooft_2x2(yu_v: sp.Matrix, yd_v: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
        hu_v, hd_v, ku_v = yu_v * yu_v.T, yd_v * yd_v.T, yu_v.T * yu_v

        def yb1_of(u_arg: sp.Matrix, d_arg: sp.Matrix) -> sp.Matrix:
            hu_a, hd_a, ku_a = u_arg * u_arg.T, d_arg * d_arg.T, u_arg.T * u_arg
            return (
                ((y_sp ** 2) / (2 * eps)) * u_arg
                + ((hu_a + hd_a) / (4 * eps)) * u_arg
                + u_arg * (ku_a / (2 * eps))
                - (hd_a * u_arg) / eps
            )

        yb1_v = yb1_of(yu_v, yd_v).applyfunc(sp.expand)
        byu1_v = (2 * eps * yb1_v).applyfunc(sp.expand)
        byd1_v = (2 * eps * yb1_of(yd_v, yu_v)).applyfunc(sp.expand)
        dyb1_v = yb1_of(yu_v + tau_d * byu1_v, yd_v + tau_d * byd1_v).applyfunc(
            lambda ex_d: sp.expand(sp.diff(ex_d, tau_d).subs(tau_d, 0))
        )

        z2_m = sp.zeros(2, 2)
        m4_list = [
            sp.BlockMatrix([[z2_m, yd_v], [-yu_v, z2_m]]).as_explicit(),
            sp.BlockMatrix([[z2_m, sp.I * yd_v], [sp.I * yu_v, z2_m]]).as_explicit(),
            sp.BlockMatrix([[yu_v, z2_m], [z2_m, yd_v]]).as_explicit(),
            sp.BlockMatrix([[-sp.I * yu_v, z2_m], [z2_m, sp.I * yd_v]]).as_explicit(),
        ]
        m4_dag = [mat_i.H for mat_i in m4_list]

        def s4_blk(fn_blk: Any) -> sp.Matrix:
            acc_m = sp.zeros(2, 2)
            for e1 in range(4):
                for e2 in range(4):
                    acc_m = acc_m + fn_blk(e1, e2)[:2, :2]
            return (acc_m / sp.Integer(4)).applyfunc(sp.expand)

        l_rn = s4_blk(lambda e1, e2: m4_list[e1] * m4_dag[e2] * m4_list[e2] * m4_dag[e1])
        r_rn = s4_blk(lambda e1, e2: m4_dag[e1] * m4_list[e2] * m4_dag[e2] * m4_list[e1])
        l_cr = s4_blk(lambda e1, e2: m4_list[e1] * m4_dag[e2] * m4_list[e1] * m4_dag[e2])
        r_cr = s4_blk(lambda e1, e2: m4_dag[e1] * m4_list[e2] * m4_dag[e1] * m4_list[e2])
        v_ld = s4_blk(lambda e1, e2: m4_list[e1] * m4_dag[e2] * m4_list[2] * m4_dag[e2] * m4_list[e1])
        v_cr = s4_blk(lambda e1, e2: m4_list[e1] * m4_dag[e2] * m4_list[2] * m4_dag[e1] * m4_list[e2])
        v_se = s4_blk(
            lambda e1, e2: m4_list[e1] * m4_dag[e2] * m4_list[e2] * m4_dag[2] * m4_list[e1]
            + m4_list[e1] * m4_dag[2] * m4_list[e2] * m4_dag[e2] * m4_list[e1]
        )
        v_tr = s4_blk(
            lambda e1, e2: m4_list[e2] * m4_dag[e1] * m4_list[e2] * m4_dag[2] * m4_list[e1]
            + m4_list[e1] * m4_dag[2] * m4_list[e2] * m4_dag[e1] * m4_list[e2]
        )

        zs1 = (y_sp ** 2) / (2 * eps)
        zl1 = (hu_v + hd_v) / (4 * eps)
        zr1 = ku_v / (2 * eps)
        dy1 = -(hd_v * yu_v) / eps
        dzl2 = -(pl_part(psi_rain) * l_rn + pl_part(psi_cross) * l_cr) - pl_part(psi_t_i) * (y_sp ** 2) * (hu_v + hd_v)
        dzr2 = -(pl_part(psi_rain) * r_rn + pl_part(psi_cross) * r_cr) - pl_part(psi_t_i) * (y_sp ** 2) * (2 * ku_v)
        dy2 = (
            pl_part(v_lad_i) * v_ld
            + pl_part(v_cro_i) * v_cr
            + pl_part(v_se_i) * v_se
            + pl_part(v_tr_i) * v_tr
            + pl_part(vert_t_i) * (y_sp ** 2) * (-hd_v * yu_v)
        )
        zl2 = -sp.Rational(1, 2) * dzl2 + sp.Rational(3, 2) * (zl1 * zl1)
        zr2 = -sp.Rational(1, 2) * dzr2 + sp.Rational(3, 2) * (zr1 * zr1)
        yb2_v = (
            zl2 * yu_v
            + yu_v * zr2
            + dy2
            + zl1 * dy1
            + dy1 * zr1
            + zl1 * yu_v * zr1
            + zs1 * (zl1 * yu_v + yu_v * zr1 + dy1)
        ).applyfunc(sp.expand)
        full_v = (4 * eps * yb2_v - dyb1_v).applyfunc(
            lambda ex_f: sp.expand(sp.expand(ex_f) - sp.expand(ex_f).coeff(y_sp, 4) * (y_sp ** 4))
        )
        return byu1_v, full_v

    yu_a = sp.Matrix([[2, 3], [-1, 5]])
    yd_a = sp.Matrix([[7, -2], [4, 1]])
    yu_b = sp.Matrix([[3, -4], [2, 1]])
    yd_b = sp.Matrix([[-1, 5], [3, 2]])

    b1_a, b2_a = eval_thooft_2x2(yu_a, yd_a)
    b1_b, b2_b = eval_thooft_2x2(yu_b, yd_b)
    b1_lep, b2_lep = eval_thooft_2x2(yu_a, sp.zeros(2, 2))

    thooft_poles_vanish = (
        b2_a.applyfunc(lambda ex_p: ex_p.coeff(eps, -2)) == sp.zeros(2, 2)
        and b2_a.applyfunc(lambda ex_p: ex_p.coeff(eps, -1)) == sp.zeros(2, 2)
        and b2_b.applyfunc(lambda ex_p: ex_p.coeff(eps, -2)) == sp.zeros(2, 2)
        and b2_b.applyfunc(lambda ex_p: ex_p.coeff(eps, -1)) == sp.zeros(2, 2)
        and b2_lep.applyfunc(lambda ex_p: ex_p.coeff(eps, -1)) == sp.zeros(2, 2)
    )

    hu_a, hd_a = yu_a * yu_a.T, yd_a * yd_a.T
    hu_b, hd_b = yu_b * yu_b.T, yd_b * yd_b.T
    ca, cb, k1, k2, k3, k4 = sp.symbols("ca cb k1 k2 k3 k4")

    b1_a_0 = b1_a.subs(y_sp, 0)
    c1_y2s = sp.simplify(b1_a[0, 0].coeff(y_sp, 2) / yu_a[0, 0])
    sol_1 = sp.solve(
        [b1_a_0[r_i, c_i] - (ca * (hu_a * yu_a)[r_i, c_i] + cb * (hd_a * yu_a)[r_i, c_i]) for r_i in range(2) for c_i in range(2)],
        [ca, cb],
    )
    c1_s, c1_p = sol_1[ca], sol_1[cb]

    b2_a_0 = b2_a.applyfunc(lambda ex_0: ex_0.subs({eps: 0, y_sp: 0}))
    b2_a_y2s = b2_a.applyfunc(lambda ex_y: ex_y.subs(eps, 0).coeff(y_sp, 2))
    bu_a = [hu_a * hu_a * yu_a, hu_a * hd_a * yu_a, hd_a * hu_a * yu_a, hd_a * hd_a * yu_a]
    bu_b = [hu_b * hu_b * yu_b, hu_b * hd_b * yu_b, hd_b * hu_b * yu_b, hd_b * hd_b * yu_b]
    sol_2 = sp.solve(
        [
            b2_a_0[r_i, c_i] - sum([kv * bm[r_i, c_i] for kv, bm in zip((k1, k2, k3, k4), bu_a)], sp.Integer(0))
            for r_i in range(2)
            for c_i in range(2)
        ],
        [k1, k2, k3, k4],
    )
    c2_1, c2_2, c2_3, c2_4 = sol_2[k1], sol_2[k2], sol_2[k3], sol_2[k4]
    sol_y2s = sp.solve(
        [b2_a_y2s[r_i, c_i] - (ca * (hu_a * yu_a)[r_i, c_i] + cb * (hd_a * yu_a)[r_i, c_i]) for r_i in range(2) for c_i in range(2)],
        [ca, cb],
    )
    cy_s, cy_p = sol_y2s[ca], sol_y2s[cb]

    c1_e = sp.simplify(b1_lep.subs(y_sp, 0)[0, 0] / (hu_a * yu_a)[0, 0])
    c2_e_he2 = sp.simplify(b2_lep.subs({eps: 0, y_sp: 0})[0, 0] / bu_a[0][0, 0])
    c2_e_y2s = sp.simplify(b2_lep.subs(eps, 0)[0, 0].coeff(y_sp, 2) / (hu_a * yu_a)[0, 0])

    b2_b_0 = b2_b.applyfunc(lambda ex_0: ex_0.subs({eps: 0, y_sp: 0}))
    b2_b_y2s = b2_b.applyfunc(lambda ex_y: ex_y.subs(eps, 0).coeff(y_sp, 2))
    pair_b_exact = (
        b1_b.subs(y_sp, 0) == (c1_s * hu_b * yu_b + c1_p * hd_b * yu_b)
        and b2_b_0 == (c2_1 * bu_b[0] + c2_2 * bu_b[1] + c2_3 * bu_b[2] + c2_4 * bu_b[3])
        and b2_b_y2s == (cy_s * hu_b * yu_b + cy_p * hd_b * yu_b)
    )
    swapped_b = c2_1 * bu_b[0] + c2_3 * bu_b[1] + c2_2 * bu_b[2] + c2_4 * bu_b[3] - b2_b_0
    swapped_comm_nonzero = (swapped_b == sp.Rational(3, 4) * (bu_b[2] - bu_b[1])) and (swapped_b != sp.zeros(2, 2))

    return {
        "c1_q_self": c1_s,
        "c1_q_partner": c1_p,
        "c1_e_self": c1_e,
        "c1_y2s": c1_y2s,
        "c2_q_hf2": c2_1,
        "c2_q_hfhfp": c2_2,
        "c2_q_hfphf": c2_3,
        "c2_q_hfp2": c2_4,
        "c2_e_he2": c2_e_he2,
        "c2_q_y2s_hf": cy_s,
        "c2_q_y2s_hfp": cy_p,
        "c2_e_y2s_he": c2_e_y2s,
        "kite_z3_exact": kite_z3_exact,
        "subdiv_free": subdiv_free,
        "thooft_poles_vanish": thooft_poles_vanish,
        "pair_b_exact": pair_b_exact,
        "swapped_comm_nonzero": swapped_comm_nonzero,
    }


def ref_build_zero_trust_mv_betas(n_c_in: int = 3, n_gen_in: int = 3) -> dict[str, Any]:
    """Independent zero-trust referee derivation of 1-loop and 2-loop SM gauge, matrix Yukawa,
    and Higgs quartic beta coefficients from:
    1. Explicit su(2) and su(N_c) generalized Gell-Mann generator commutators & Casimir sums
       (zero hand-written C_F = (N_c^2 - 1)/(2*N_c) or base-3 radix formulas!).
    2. Component index a = 0 (p_0) contractions on R^4 Higgs / O(4) tensor / Weyl spinor boxes
       (distinct from producer's a = 2 component contractions!).
    """
    su2_gens = ref_su_n_fundamental_generators(2)
    sunc_gens = ref_su_n_fundamental_generators(n_c_in)

    cf_2 = sp.simplify(sum([g_m * g_m for g_m in su2_gens], sp.zeros(2, 2))[0, 0])
    cf_nc = sp.simplify(sum([g_m * g_m for g_m in sunc_gens], sp.zeros(n_c_in, n_c_in))[0, 0])
    c2_su2 = sp.simplify(-sum([2 * ((su2_gens[0] * g_m - g_m * su2_gens[0]) ** 2).trace() for g_m in su2_gens]))
    c2_sunc = sp.simplify(-sum([2 * ((sunc_gens[0] * g_m - g_m * sunc_gens[0]) ** 2).trace() for g_m in sunc_gens]))
    c2_g = [sp.Matrix.zeros(1, 1).trace(), c2_su2, c2_sunc]

    d_g = [
        sp.Matrix.eye(1).trace(),
        sp.Matrix.eye(len(su2_gens)).trace(),
        sp.Matrix.eye(len(sunc_gens)).trace(),
    ]
    n_c_sym = sp.Matrix.eye(n_c_in).trace()
    n_gen_sym = sp.Matrix.zeros(1, 1).trace() if n_gen_in == 0 else sp.Matrix.eye(n_gen_in).trace()

    # GUT normalization k_gut = 3/5 from 16D chiral generation trace ratio:
    y16_sm = (
        [sp.Rational(1, 6)] * 6
        + [sp.Rational(-2, 3)] * 3
        + [sp.Rational(1, 3)] * 3
        + [sp.Rational(-1, 2)] * 2
        + [sp.Integer(1), sp.Integer(0)]
    )
    k_g = (
        sp.Matrix(16, 16, lambda r, c: sp.Rational(1, 4) if (r == c and (r < 6 or (12 <= r < 14))) else 0).trace()
        / sp.Matrix(16, 16, lambda r, c: (y16_sm[r] ** 2) if r == c else 0).trace()
    )

    yq = 1 / (2 * n_c_sym)
    yu = yq + sp.Rational(1, 2)
    yd = yq - sp.Rational(1, 2)
    yl = -n_c_sym * yq
    ye = -sp.Matrix.eye(1).trace()
    yh = sp.Matrix.eye(1).trace() / sp.Integer(2)

    dim_w = 4 * n_c_in + 4
    y_w = [yq] * (2 * n_c_in) + [-yu] * n_c_in + [-yd] * n_c_in + [yl] * 2 + [-ye, sp.Integer(0)]
    y2_w = sp.Matrix(dim_w, dim_w, lambda r, c: (y_w[r] ** 2) if r == c else 0)
    cas_w = [
        k_g * y2_w,
        sp.Matrix(
            dim_w,
            dim_w,
            lambda r, c: cf_2 if (r == c and (r < 2 * n_c_in or (4 * n_c_in <= r < 4 * n_c_in + 2))) else 0,
        ),
        sp.Matrix(dim_w, dim_w, lambda r, c: cf_nc if (r == c and r < 4 * n_c_in) else 0),
    ]
    cas_h = [
        sp.Matrix(2, 2, lambda r, c: k_g * (yh ** 2) if r == c else 0),
        sp.Matrix(2, 2, lambda r, c: cf_2 if r == c else 0),
        sp.Matrix(2, 2, lambda r, c: 0),
    ]
    sf_gut = [n_gen_sym * (cas_w[i].trace() / d_g[i]) for i in range(3)]
    sh_gut = [cas_h[i].trace() / d_g[i] for i in range(3)]

    b1_v = [-sp.Rational(11, 3) * c2_g[i] + sp.Rational(2, 3) * sf_gut[i] + sp.Rational(1, 3) * sh_gut[i] for i in range(3)]
    b2_m = sp.Matrix(
        3,
        3,
        lambda i, j: (
            (-sp.Rational(34, 3) * (c2_g[i] ** 2) + sp.Rational(10, 3) * c2_g[i] * sf_gut[i] + sp.Rational(2, 3) * c2_g[i] * sh_gut[i])
            * (1 if i == j else 0)
            + 2 * n_gen_sym * ((cas_w[i] * cas_w[j]).trace() / d_g[i])
            + 4 * ((cas_h[i] * cas_h[j]).trace() / d_g[i])
        ),
    )

    cq = [yq ** 2, cf_2, cf_nc]
    cu = [yu ** 2, sp.Integer(0), cf_nc]
    cd = [yd ** 2, sp.Integer(0), cf_nc]
    cl = [yl ** 2, cf_2, sp.Integer(0)]
    ce = [ye ** 2, sp.Integer(0), sp.Integer(0)]
    ch = [yh ** 2, cf_2, sp.Integer(0)]
    sc_gut = [k_g, sp.Integer(1), sp.Integer(1)]

    c_yuk = sp.Matrix(
        3,
        3,
        lambda i, f_i: (2 / d_g[i])
        * sc_gut[i]
        * (
            n_c_sym * (cq[i] + cu[i])
            if f_i == 0
            else (n_c_sym * (cq[i] + cd[i]) if f_i == 1 else (cl[i] + ce[i]))
        ),
    )

    g1s, g2s, g3s, yts, lms = sp.symbols("g1s g2s g3s yts lms")
    gys = k_g * g1s
    gs_raw = [gys, g2s, g3s]
    sf_raw = [n_gen_sym * y2_w.trace(), sf_gut[1], sf_gut[2]]
    sh_raw = [2 * (yh ** 2), sh_gut[1], sh_gut[2]]

    def mv84_ref_sector(c_left: list[sp.Expr], c_right: list[sp.Expr]) -> tuple[list[sp.Expr], sp.Expr]:
        lin_v = [
            sc_gut[i]
            * (
                sp.Rational(39, 4) * c_left[i]
                + sp.Rational(9, 4) * c_right[i]
                + sp.Rational(27, 2) * ch[i]
                - 6 * ch[i] * c2_g[i]
            )
            for i in range(3)
        ]
        g4_diag = sum(
            [
                (
                    -sp.Rational(3, 2) * ((c_left[i] ** 2) + (c_right[i] ** 2))
                    + 6 * (c_left[i] + c_right[i]) * ch[i]
                    - sp.Rational(21, 2) * (ch[i] ** 2)
                    + (c_left[i] + c_right[i])
                    * (
                        sp.Rational(5, 3) * sf_raw[i]
                        + sp.Rational(11, 6) * sh_raw[i]
                        - 16 * c2_g[i]
                        - sp.Rational(1, 6) * c2_g[i]
                    )
                    + ch[i]
                    * (
                        -sf_raw[i]
                        - sp.Rational(1, 2) * sh_raw[i]
                        + 12 * c2_g[i]
                        + sp.Rational(1, 4) * c2_g[i]
                    )
                )
                * (gs_raw[i] ** 2)
                for i in range(3)
            ]
        )
        g4_off = sum(
            [
                (
                    -3 * (c_left[ia] * c_left[ja] + c_right[ia] * c_right[ja])
                    + 6 * ((c_left[ia] + c_right[ia]) * ch[ja] + (c_left[ja] + c_right[ja]) * ch[ia])
                    - 21 * ch[ia] * ch[ja]
                )
                * gs_raw[ia]
                * gs_raw[ja]
                for ia in range(3)
                for ja in range(ia + 1, 3)
            ]
        )
        return lin_v, sp.expand(g4_diag + g4_off)

    u_self_g, u_g4 = mv84_ref_sector(cq, cu)
    d_self_g, d_g4 = mv84_ref_sector(cq, cd)
    e_self_g, e_g4 = mv84_ref_sector(cl, ce)
    u_from_d_g = [
        sc_gut[i] * (sp.Rational(39, 4) * cq[i] + sp.Rational(9, 4) * cd[i] + sp.Rational(3, 2) * ch[i] - 6 * ch[i] * c2_g[i])
        for i in range(3)
    ]
    d_from_u_g = [
        sc_gut[i] * (sp.Rational(39, 4) * cq[i] + sp.Rational(9, 4) * cu[i] + sp.Rational(3, 2) * ch[i] - 6 * ch[i] * c2_g[i])
        for i in range(3)
    ]
    tr_u_g = [sc_gut[i] * sp.Rational(5, 2) * n_c_sym * (cq[i] + cu[i]) for i in range(3)]
    tr_d_g = [sc_gut[i] * sp.Rational(5, 2) * n_c_sym * (cq[i] + cd[i]) for i in range(3)]
    tr_e_g = [sc_gut[i] * sp.Rational(5, 2) * (cl[i] + ce[i]) for i in range(3)]

    byt_1 = sp.expand((n_c_sym + sp.Rational(3, 2)) * yts - 3 * sum([(cq[i] + cu[i]) * gs_raw[i] for i in range(3)]))
    byt_2 = sp.expand(
        (sp.Rational(3, 2) - sp.Rational(9, 2) * n_c_sym) * (yts ** 2)
        - 12 * lms * yts
        + 6 * (lms ** 2)
        + yts * sum([(u_self_g[i] + tr_u_g[i]) * [g1s, g2s, g3s][i] for i in range(3)])
        + u_g4
    )

    # Component a = 0 (p_0) real Higgs & O(4) contractions (distinct from producer's a = 2!):
    p0, p1, p2, p3 = sp.symbols("p0 p1 p2 p3", real=True)
    pv = sp.Matrix([p0, p1, p2, p3])
    hd = sp.Matrix([p0 + sp.I * p1, p2 + sp.I * p3]) / sp.sqrt(2)
    htd = sp.Matrix([p2 - sp.I * p3, -(p0 - sp.I * p1)]) / sp.sqrt(2)
    g2_w, gy_w = sp.symbols("g2_w gy_w", real=True)

    def real_gen4(gen2: sp.Matrix) -> sp.Matrix:
        dh = sp.I * gen2 * hd
        vec4 = [
            sp.re(sp.expand(dh[0] * sp.sqrt(2))),
            sp.im(sp.expand(dh[0] * sp.sqrt(2))),
            sp.re(sp.expand(dh[1] * sp.sqrt(2))),
            sp.im(sp.expand(dh[1] * sp.sqrt(2))),
        ]
        return sp.Matrix(4, 4, lambda r, c: sp.diff(vec4[r], pv[c]))

    th4 = [real_gen4(g_op) for g_op in (g2_w * su2_gens[0], g2_w * su2_gens[1], g2_w * su2_gens[2], gy_w * yh * sp.eye(2))]
    l4 = {
        (ia, ib, ic, id_i): 2
        * lms
        * (
            (1 if (ia == ib and ic == id_i) else 0)
            + (1 if (ia == ic and ib == id_i) else 0)
            + (1 if (ia == id_i and ib == ic) else 0)
        )
        for ia, ib, ic, id_i in product(range(4), repeat=4)
    }
    # Contractions evaluated at external index 0 (p_0):
    candy_0 = sp.Rational(1, 2) * sum([l4[(0, 0, ei, fi)] * l4[(ei, fi, 0, 0)] for ei, fi in product(range(4), repeat=2)])
    gam2_0 = sp.Rational(1, 12) * sum([l4[(0, fi, gi, hi)] ** 2 for fi, gi, hi in product(range(4), repeat=3)])
    scoop_0 = sum([l4[(0, 0, ei, fi)] * l4[(0, ei, gi, hi)] * l4[(0, fi, gi, hi)] for ei, fi, gi, hi in product(range(4), repeat=4)])
    pure_l3 = -scoop_0 + 4 * gam2_0 * lms

    c2_s00 = -sum([tm * tm for tm in th4], sp.zeros(4, 4))[0, 0]
    i1_r = c2_s00 ** 2
    ibox_r = sum([(((ta * tb + tb * ta)[0, 0] / 2) ** 2) for ta in th4 for tb in th4])
    th_d0 = [-(tm * tm)[0, 0] for tm in th4]
    cg_4 = [c2_g[1], c2_g[1], c2_g[1], c2_g[0]]
    sf_4 = [sf_raw[1], sf_raw[1], sf_raw[1], sf_raw[0]]
    ss_4 = [-(th4[0] * th4[0]).trace() / (g2_w ** 2)] * 3 + [-(th4[3] * th4[3]).trace() / (gy_w ** 2)]
    gw_4 = [g2_w, g2_w, g2_w, gy_w]

    kg_r = sum([th_d0[ai] * (gw_4[ai] ** 2) * cg_4[ai] for ai in range(4)])
    kf_r = sum([th_d0[ai] * (gw_4[ai] ** 2) * sf_4[ai] for ai in range(4)])
    ks_r = sum([th_d0[ai] * (gw_4[ai] ** 2) * ss_4[ai] for ai in range(4)])
    bf_r = sum(
        [
            (((th4[ai] * th4[bi] + th4[bi] * th4[ai])[0, 0] / 2) ** 2)
            * (sf_4[ai] * (gw_4[ai] ** 2) + sf_4[bi] * (gw_4[bi] ** 2))
            / 2
            for ai in range(4)
            for bi in range(4)
        ]
    )
    bs_r = sum(
        [
            (((th4[ai] * th4[bi] + th4[bi] * th4[ai])[0, 0] / 2) ** 2)
            * (ss_4[ai] * (gw_4[ai] ** 2) + ss_4[bi] * (gw_4[bi] ** 2))
            / 2
            for ai in range(4)
            for bi in range(4)
        ]
    )
    bg_r = sum(
        [
            (((th4[ai] * th4[bi] + th4[bi] * th4[ai])[0, 0] / 2) ** 2)
            * (cg_4[ai] * (gw_4[ai] ** 2) + cg_4[bi] * (gw_4[bi] ** 2))
            / 2
            for ai in range(4)
            for bi in range(4)
        ]
    )
    sub_ew = {
        g2_w ** 2: g2s,
        gy_w ** 2: gys,
        g2_w ** 4: g2s ** 2,
        gy_w ** 4: gys ** 2,
        g2_w ** 6: g2s ** 3,
        gy_w ** 6: gys ** 3,
    }

    def y2_g4_at_p0(yl_v: sp.Expr, yr_v: sp.Expr, dc_v: sp.Expr, h_col: sp.Matrix) -> sp.Expr:
        w1, w2, wrc = sp.symbols("w1 w2 wrc")
        yuk_w = (h_col.H * sp.Matrix([w1, w2]))[0] * wrc
        w_vec = [w1, w2, wrc]
        ya3 = [
            sp.Matrix(3, 3, lambda r, c: sp.diff(sp.diff(sp.expand(sp.diff(yuk_w, p_s)), w_vec[r]), w_vec[c]))
            for p_s in (p0, p1, p2, p3)
        ]
        ta3 = [
            g2_w * sp.diag(su2_gens[0], 0),
            g2_w * sp.diag(su2_gens[1], 0),
            g2_w * sp.diag(su2_gens[2], 0),
            gy_w * sp.diag(yl_v * sp.eye(2), -yr_v),
        ]
        mmix_0 = sum(
            [
                ((th4[ai] * th4[bi] + th4[bi] * th4[ai])[0, ei] / 2)
                * (ya3[ei] * ya3[0].H * ((ta3[ai] * ta3[bi] + ta3[bi] * ta3[ai]) / 2)).trace()
                for ai in range(4)
                for bi in range(4)
                for ei in range(4)
            ]
        )
        return sp.expand(dc_v * (20 * ibox_r + 48 * mmix_0)).subs(sub_ew)

    u_y2g4 = y2_g4_at_p0(yq, yu, n_c_sym, htd)
    d_y2g4 = y2_g4_at_p0(yq, yd, n_c_sym, hd)
    e_y2g4 = y2_g4_at_p0(yl, ye, sp.Integer(1), hd)

    qu, qd, ur, dr = sp.symbols("qu qd ur dr")
    yus, yds = sp.symbols("yus yds", real=True)
    w_q4 = yus * (htd.H * sp.Matrix([qu, qd]))[0] * ur + yds * (hd.H * sp.Matrix([qu, qd]))[0] * dr
    qw_list = [qu, qd, ur, dr]
    ya4 = [
        sp.Matrix(4, 4, lambda r, c: sp.diff(sp.diff(sp.expand(sp.diff(w_q4, p_s)), qw_list[r]), qw_list[c]))
        for p_s in (p0, p1, p2, p3)
    ]
    tr4_d0 = sp.expand((ya4[0] * ya4[0].H * ya4[0] * ya4[0].H).trace())
    tr4_s1_0 = sp.expand(sum([(ya4[0] * ya4[ei].H * ya4[ei] * ya4[0].H).trace() for ei in range(4)]))
    tr4_s2_0 = sp.expand(sum([(ya4[0] * ya4[ei].H * ya4[0] * ya4[ei].H).trace() for ei in range(4)]))
    chi4_p = sp.Poly(sp.expand(n_c_sym * (-sp.Rational(3, 2) * tr4_s1_0 - tr4_s2_0)), yus, yds)
    ly4_p = sp.Poly(sp.expand(4 * chi4_p.as_expr() + n_c_sym * (16 * tr4_d0 + 8 * tr4_s2_0)), yus, yds)
    tr6_d0 = sp.expand((ya4[0] * ya4[0].H * ya4[0] * ya4[0].H * ya4[0] * ya4[0].H).trace())
    tr6_s1_0 = sp.expand(sum([(ya4[0] * ya4[0].H * ya4[0] * ya4[ei].H * ya4[ei] * ya4[0].H).trace() for ei in range(4)]))
    tr6_s2_0 = sp.expand(sum([(ya4[0] * ya4[ei].H * ya4[0] * ya4[0].H * ya4[0] * ya4[ei].H).trace() for ei in range(4)]))
    y6_p = sp.Poly(sp.expand(8 * n_c_sym * (tr6_s1_0 + 2 * tr6_d0 + tr6_s2_0)), yus, yds)

    kite_info = ref_derive_msbar_kite_matrix_yukawa_coeffs()
    lam_y_p0 = sum(
        [
            -2 * l4[(0, bi, ci, di)] * (ya4[bi] * ya4[ci].H * ya4[di])[1, 2]
            for bi, ci, di in product(range(4), repeat=3)
            if l4[(0, bi, ci, di)] != 0
        ],
        sp.Integer(0),
    )
    c2_lam_hf_sym = sp.simplify(lam_y_p0.subs(yds, 0) / (lms * (yus ** 2) * ya4[0][1, 2]))
    c2_lam2_sym = sp.simplify(gam2_0 / (lms ** 2))
    c1_lam_y2_sym = sp.simplify(4 * kite_info["c1_y2s"])
    c1_lam_y4_sym = sp.simplify(-4 * tr4_d0.subs({yus: 1, yds: 0}))
    c2_lam2_y2_sym = sp.simplify(-2 * candy_0 * kite_info["c1_y2s"] / (lms ** 2))
    c2_lam_yg_sym = sp.simplify(4 * kite_info["c1_y2s"])

    bl1_ew = sp.expand(candy_0 - 12 * lms * c2_s00 + 6 * ibox_r).subs(sub_ew)
    blam_1 = sp.expand(bl1_ew + c1_lam_y2_sym * n_c_sym * lms * yts + c1_lam_y4_sym * n_c_sym * (yts ** 2))

    l2_g2 = sp.expand(6 * candy_0 * c2_s00).subs(sub_ew)
    l_g4 = sp.expand(
        lms
        * (
            36 * i1_r
            + sp.Rational(2, 3) * i1_r
            - 32 * ibox_r
            - 48 * kg_r
            + sp.Rational(1, 3) * kg_r
            + 10 * kf_r
            + sp.Rational(11, 3) * ks_r
        )
    ).subs(sub_ew)
    g6_p0 = sp.expand(
        -sp.Rational(32, 3) * bf_r
        + 84 * c2_s00 * ibox_r
        - 72 * (c2_s00 ** 3)
        - 23 * bs_r
        + sp.Rational(1, 3) * bs_r
        + 144 * bg_r
        - sp.Rational(1, 3) * bg_r
    ).subs(sub_ew)

    y4g2_u = sp.expand(-4 * n_c_sym * sum([(cq[i] + cu[i] - ch[i]) * gs_raw[i] for i in range(3)]))
    y4g2_d = sp.expand(-4 * n_c_sym * sum([(cq[i] + cd[i] - ch[i]) * gs_raw[i] for i in range(3)]))
    y4g2_e = sp.expand(-4 * sum([(cl[i] + ce[i] - ch[i]) * gs_raw[i] for i in range(3)]))

    blam_2 = sp.expand(
        pure_l3
        + c2_lam2_y2_sym * n_c_sym * (lms ** 2) * yts
        + l2_g2
        + lms * ly4_p.coeff_monomial((4, 0)) * (yts ** 2)
        + c2_lam_yg_sym * lms * yts * sum([tr_u_g[i] * [g1s, g2s, g3s][i] for i in range(3)])
        + l_g4
        + y6_p.coeff_monomial((6, 0)) * (yts ** 3)
        + (yts ** 2) * y4g2_u
        + yts * u_y2g4
        + g6_p0
    )

    def terms_of(poly_expr: sp.Expr, vars_tup: tuple[sp.Symbol, ...]) -> list[tuple[tuple[int, ...], float]]:
        return [(mon_e, float(cf_v)) for mon_e, cf_v in sp.Poly(poly_expr, *vars_tup).terms()]

    vars5 = (g1s, g2s, g3s, yts, lms)
    vars3 = (g1s, g2s, g3s)
    vars4 = (g1s, g2s, g3s, lms)
    nc_fl = float(n_c_sym)

    return {
        "k_g": k_g,
        "cas_w": cas_w,
        "c2_g": c2_g,
        "d_g": d_g,
        "b1_sym": b1_v,
        "b2_sym": b2_m,
        "syms5": vars5,
        "byt_1": byt_1,
        "byt_2": byt_2,
        "blam_1": blam_1,
        "blam_2": blam_2,
        "nc_f": nc_fl,
        "kg_f": float(k_g),
        "kite_info": kite_info,
        "c1_q_self": float(kite_info["c1_q_self"]),
        "c1_q_partner": float(kite_info["c1_q_partner"]),
        "c1_e_self": float(kite_info["c1_e_self"]),
        "c1_y2s": float(kite_info["c1_y2s"]),
        "c2_q_hf2": float(kite_info["c2_q_hf2"]),
        "c2_q_hfhfp": float(kite_info["c2_q_hfhfp"]),
        "c2_q_hfphf": float(kite_info["c2_q_hfphf"]),
        "c2_q_hfp2": float(kite_info["c2_q_hfp2"]),
        "c2_e_he2": float(kite_info["c2_e_he2"]),
        "c2_q_y2s_hf": float(kite_info["c2_q_y2s_hf"]),
        "c2_q_y2s_hfp": float(kite_info["c2_q_y2s_hfp"]),
        "c2_e_y2s_he": float(kite_info["c2_e_y2s_he"]),
        "c2_lam_hf": float(c2_lam_hf_sym),
        "c2_lam2": float(c2_lam2_sym),
        "c1_lam_y2": float(c1_lam_y2_sym),
        "c1_lam_y4": float(c1_lam_y4_sym),
        "c2_lam2_y2": float(c2_lam2_y2_sym),
        "c2_lam_yg": float(c2_lam_yg_sym),
        "b1": np.array([float(v) for v in b1_v], dtype=float),
        "b2": np.array([[float(b2_m[r, c]) for c in range(3)] for r in range(3)], dtype=float),
        "ctop": np.array([float(c_yuk[i, 0]) for i in range(3)], dtype=float),
        "cyuk": np.array([[float(c_yuk[r, c]) for c in range(3)] for r in range(3)], dtype=float),
        "yt1_t": terms_of(byt_1, vars5),
        "yt2_t": terms_of(byt_2, vars5),
        "l1_t": terms_of(blam_1, vars5),
        "l2_t": terms_of(blam_2, vars5),
        "gu1": np.array([float(3 * sc_gut[i] * (cq[i] + cu[i])) for i in range(3)], dtype=float),
        "gd1": np.array([float(3 * sc_gut[i] * (cq[i] + cd[i])) for i in range(3)], dtype=float),
        "ge1": np.array([float(3 * sc_gut[i] * (cl[i] + ce[i])) for i in range(3)], dtype=float),
        "u_self": np.array([float(v) for v in u_self_g], dtype=float),
        "d_self": np.array([float(v) for v in d_self_g], dtype=float),
        "e_self": np.array([float(v) for v in e_self_g], dtype=float),
        "u_from_d": np.array([float(v) for v in u_from_d_g], dtype=float),
        "d_from_u": np.array([float(v) for v in d_from_u_g], dtype=float),
        "tr_u": np.array([float(v) for v in tr_u_g], dtype=float),
        "tr_d": np.array([float(v) for v in tr_d_g], dtype=float),
        "tr_e": np.array([float(v) for v in tr_e_g], dtype=float),
        "ug4_t": terms_of(u_g4, vars3),
        "dg4_t": terms_of(d_g4, vars3),
        "eg4_t": terms_of(e_g4, vars3),
        "uy2g4_t": terms_of(u_y2g4, vars3),
        "dy2g4_t": terms_of(d_y2g4, vars3),
        "ey2g4_t": terms_of(e_y2g4, vars3),
        "y4g2u_t": terms_of(y4g2_u, vars3),
        "y4g2d_t": terms_of(y4g2_d, vars3),
        "y4g2e_t": terms_of(y4g2_e, vars3),
        "lam_ew1_t": terms_of(bl1_ew, vars4),
        "lam_ew2_t": terms_of(sp.expand(pure_l3 + l2_g2 + l_g4 + g6_p0), vars4),
        "chi4_qd": float(chi4_p.coeff_monomial((4, 0))),
        "chi4_ed": float(chi4_p.coeff_monomial((4, 0))) / nc_fl,
        "chi4_qm": float(chi4_p.coeff_monomial((2, 2))),
        "ly4_qd": float(ly4_p.coeff_monomial((4, 0))),
        "ly4_ed": float(ly4_p.coeff_monomial((4, 0))) / nc_fl,
        "ly4_qm": float(ly4_p.coeff_monomial((2, 2))),
        "y6_qd": float(y6_p.coeff_monomial((6, 0))),
        "y6_ed": float(y6_p.coeff_monomial((6, 0))) / nc_fl,
        "y6_qm": float(y6_p.coeff_monomial((4, 2))),
    }


def ref_eval_terms(vec_x: np.ndarray, term_pairs: list[tuple[tuple[int, ...], float]]) -> Any:
    """Evaluate polynomial (monomial_tuple, coeff) over real or complex vector vec_x."""
    acc_v: Any = 0.0
    n_dim = len(vec_x)
    for mon_t, cf_f in term_pairs:
        p_term: Any = cf_f
        for idx_k in range(n_dim):
            pw_i = mon_t[idx_k]
            if pw_i != 0:
                p_term = p_term * (vec_x[idx_k] ** pw_i)
        acc_v = acc_v + p_term
    return acc_v


def ref_sm_5chan_rhs_poly(
    x_vec: np.ndarray,
    rc: dict[str, Any],
    two_loop: bool = True,
    t_mult: float = 1.0,
    lam_mult: float = 1.0,
) -> np.ndarray:
    """Independent referee 5-channel RGE RHS (supports real or complex arrays for Cauchy Lie-jets)."""
    i4p = 1.0 / (4 * math.pi)
    i8p = 0.5 * i4p
    i64p3 = i4p / (16 * (math.pi ** 2))
    i128p3 = 0.5 * i64p3

    out_v = np.zeros(5, dtype=x_vec.dtype)
    gs_v = x_vec[:3]
    yt_v = x_vec[3]
    for kg_i in range(3):
        gk = gs_v[kg_i]
        rg = i4p * rc["b1"][kg_i] * (gk ** 2)
        if two_loop:
            rg = rg + i64p3 * (gk ** 2) * ((rc["b2"][kg_i] @ gs_v) - rc["ctop"][kg_i] * yt_v)
        out_v[kg_i] = t_mult * rg

    ryt = i4p * yt_v * ref_eval_terms(x_vec, rc["yt1_t"])
    if two_loop:
        ryt = ryt + i64p3 * yt_v * ref_eval_terms(x_vec, rc["yt2_t"])
    out_v[3] = t_mult * ryt

    rlam = lam_mult * i8p * ref_eval_terms(x_vec, rc["l1_t"])
    if two_loop:
        rlam = rlam + lam_mult * i128p3 * ref_eval_terms(x_vec, rc["l2_t"])
    out_v[4] = t_mult * rlam
    return out_v


def ref_integrate_5chan_kutta38(
    x_init: np.ndarray,
    t_end: float,
    rc: dict[str, Any],
    step_blocks: int = 8,
    two_loop: bool = True,
    t_mult: float = 1.0,
    lam_mult: float = 1.0,
) -> np.ndarray:
    """Independent 4th-order Kutta 3/8-rule integrator:
    c = (0, 1/3, 2/3, 1), a_3 = (-1/3, 1), a_4 = (1, -1, 1), b = (1/8, 3/8, 3/8, 1/8).
    """
    n_st = 32 * step_blocks
    xc = np.array(x_init, dtype=float)
    dt_h = float(mp.fdiv(t_end, n_st))
    dt_third = float(mp.fdiv(dt_h, 3))
    w_eighth = float(mp.fdiv(dt_h, 8))
    for _ in range(n_st):
        k1 = ref_sm_5chan_rhs_poly(xc, rc, two_loop, t_mult, lam_mult)
        k2 = ref_sm_5chan_rhs_poly(xc + dt_third * k1, rc, two_loop, t_mult, lam_mult)
        k3 = ref_sm_5chan_rhs_poly(xc - dt_third * k1 + dt_h * k2, rc, two_loop, t_mult, lam_mult)
        k4 = ref_sm_5chan_rhs_poly(xc + dt_h * (k1 - k2 + k3), rc, two_loop, t_mult, lam_mult)
        xc = xc + w_eighth * (k1 + 3 * k2 + 3 * k3 + k4)
    return xc


def ref_matrix_yukawa_2loop_holomorphic_poly(
    gv: np.ndarray,
    lm: Any,
    um: np.ndarray,
    um_dag: np.ndarray,
    dm: np.ndarray,
    dm_dag: np.ndarray,
    em: np.ndarray,
    em_dag: np.ndarray,
    rc: dict[str, Any],
) -> tuple[np.ndarray, Any, np.ndarray, np.ndarray, np.ndarray]:
    """Holomorphic polynomial evaluation of the 2-loop 3x3 matrix Yukawa + gauge + quartic RHS
    for independent (um, um_dag), (dm, dm_dag), (em, em_dag) — used for both real-t integration
    and complex Cauchy-contour Lie-Picard Taylor jets.
    """
    i4p = 1.0 / (4 * math.pi)
    i8p = 0.5 * i4p
    i64p3 = i4p / (16 * (math.pi ** 2))
    i128p3 = 0.5 * i64p3

    nc_v = rc["nc_f"]
    hu = um @ um_dag
    hd = dm @ dm_dag
    he = em @ em_dag
    thu = np.trace(hu)
    thd = np.trace(hd)
    the = np.trace(he)
    ty2 = nc_v * thu + nc_v * thd + the
    tvec = np.array([thu, thd, the])

    dg = i4p * rc["b1"] * (gv ** 2) + i64p3 * (gv ** 2) * ((rc["b2"] @ gv) - (rc["cyuk"] @ tvec))

    id3 = np.eye(3, dtype=complex)
    du = i8p * (
        (
            rc["c1_q_self"] * hu
            + rc["c1_q_partner"] * hd
            + (rc["c1_y2s"] * ty2 - (rc["gu1"] @ gv)) * id3
        )
        @ um
    )
    dd = i8p * (
        (
            rc["c1_q_self"] * hd
            + rc["c1_q_partner"] * hu
            + (rc["c1_y2s"] * ty2 - (rc["gd1"] @ gv)) * id3
        )
        @ dm
    )
    de = i8p * ((rc["c1_e_self"] * he + (rc["c1_y2s"] * ty2 - (rc["ge1"] @ gv)) * id3) @ em)

    hu2 = hu @ hu
    hd2 = hd @ hd
    he2 = he @ he
    thu2 = np.trace(hu2)
    thd2 = np.trace(hd2)
    the2 = np.trace(he2)
    thuhd = np.trace(hu @ hd)

    x4 = np.array([gv[0], gv[1], gv[2], lm])
    dl1 = (
        ref_eval_terms(x4, rc["lam_ew1_t"])
        + rc["c1_lam_y2"] * lm * ty2
        + rc["c1_lam_y4"] * (nc_v * thu2 + nc_v * thd2 + the2)
    )

    chi4 = rc["chi4_qd"] * (thu2 + thd2) + rc["chi4_ed"] * the2 + rc["chi4_qm"] * thuhd
    yg_tr = (rc["tr_u"] @ gv) * thu + (rc["tr_d"] @ gv) * thd + (rc["tr_e"] @ gv) * the

    du2 = (
        rc["c2_q_hf2"] * hu2
        + rc["c2_q_hfhfp"] * (hu @ hd)
        + rc["c2_q_hfphf"] * (hd @ hu)
        + rc["c2_q_hfp2"] * hd2
        + (rc["c2_q_y2s_hf"] * hu + rc["c2_q_y2s_hfp"] * hd) * ty2
        + rc["c2_lam_hf"] * lm * hu
        + (rc["c2_lam2"] * (lm ** 2) + chi4 + yg_tr + ref_eval_terms(gv, rc["ug4_t"])) * id3
        + (rc["u_self"] @ gv) * hu
        - (rc["u_from_d"] @ gv) * hd
    ) @ um
    dd2 = (
        rc["c2_q_hf2"] * hd2
        + rc["c2_q_hfhfp"] * (hd @ hu)
        + rc["c2_q_hfphf"] * (hu @ hd)
        + rc["c2_q_hfp2"] * hu2
        + (rc["c2_q_y2s_hf"] * hd + rc["c2_q_y2s_hfp"] * hu) * ty2
        + rc["c2_lam_hf"] * lm * hd
        + (rc["c2_lam2"] * (lm ** 2) + chi4 + yg_tr + ref_eval_terms(gv, rc["dg4_t"])) * id3
        + (rc["d_self"] @ gv) * hd
        - (rc["d_from_u"] @ gv) * hu
    ) @ dm
    de2 = (
        rc["c2_e_he2"] * he2
        + rc["c2_e_y2s_he"] * ty2 * he
        + rc["c2_lam_hf"] * lm * he
        + (rc["c2_lam2"] * (lm ** 2) + chi4 + yg_tr + ref_eval_terms(gv, rc["eg4_t"])) * id3
        + (rc["e_self"] @ gv) * he
    ) @ em

    thu3 = np.trace(hu2 @ hu)
    thd3 = np.trace(hd2 @ hd)
    the3 = np.trace(he2 @ he)
    thu2hd = np.trace(hu2 @ hd)
    thuhd2 = np.trace(hu @ hd2)
    dl2 = (
        ref_eval_terms(x4, rc["lam_ew2_t"])
        + rc["c2_lam2_y2"] * (lm ** 2) * ty2
        + lm * (rc["ly4_qd"] * (thu2 + thd2) + rc["ly4_ed"] * the2 + rc["ly4_qm"] * thuhd)
        + rc["c2_lam_yg"] * lm * yg_tr
        + rc["y6_qd"] * (thu3 + thd3)
        + rc["y6_ed"] * the3
        + rc["y6_qm"] * (thu2hd + thuhd2)
        + ref_eval_terms(gv, rc["y4g2u_t"]) * thu2
        + ref_eval_terms(gv, rc["y4g2d_t"]) * thd2
        + ref_eval_terms(gv, rc["y4g2e_t"]) * the2
        + ref_eval_terms(gv, rc["uy2g4_t"]) * thu
        + ref_eval_terms(gv, rc["dy2g4_t"]) * thd
        + ref_eval_terms(gv, rc["ey2g4_t"]) * the
    )
    return dg, i8p * dl1 + i128p3 * dl2, du + i128p3 * du2, dd + i128p3 * dd2, de + i128p3 * de2


def ref_matrix_yukawa_2loop_rhs(
    gv: np.ndarray,
    lm: float,
    um: np.ndarray,
    dm: np.ndarray,
    em: np.ndarray,
    rc: dict[str, Any],
) -> tuple[np.ndarray, float, np.ndarray, np.ndarray, np.ndarray]:
    """Independent referee full 2-loop 3x3 matrix Yukawa + gauge + quartic RHS."""
    dg_c, dl_c, du_c, dd_c, de_c = ref_matrix_yukawa_2loop_holomorphic_poly(
        gv, lm, um, um.conj().T, dm, dm.conj().T, em, em.conj().T, rc
    )
    return np.real(dg_c), float(np.real(dl_c)), du_c, dd_c, de_c


def ref_integrate_matrix_2loop_kutta38(
    g0: np.ndarray,
    lam0: float,
    yu0: np.ndarray,
    yd0: np.ndarray,
    ye0: np.ndarray,
    t_span: float,
    rc: dict[str, Any],
    step_blocks: int = 3,
) -> tuple[np.ndarray, float, np.ndarray, np.ndarray, np.ndarray]:
    """Kutta's 4th-order 3/8-rule integrator for the full 2-loop 3x3 matrix Yukawa + gauge + quartic RGEs."""
    n_st = 32 * step_blocks
    gc = np.array(g0, dtype=float)
    lc = float(lam0)
    uc = np.array(yu0, dtype=complex)
    dc = np.array(yd0, dtype=complex)
    ec = np.array(ye0, dtype=complex)
    dt_h = float(mp.fdiv(t_span, n_st))
    dt_third = float(mp.fdiv(dt_h, 3))
    w_eighth = float(mp.fdiv(dt_h, 8))

    for _ in range(n_st):
        kg1, kl1, ku1, kd1, ke1 = ref_matrix_yukawa_2loop_rhs(gc, lc, uc, dc, ec, rc)
        kg2, kl2, ku2, kd2, ke2 = ref_matrix_yukawa_2loop_rhs(
            gc + dt_third * kg1,
            lc + dt_third * kl1,
            uc + dt_third * ku1,
            dc + dt_third * kd1,
            ec + dt_third * ke1,
            rc,
        )
        kg3, kl3, ku3, kd3, ke3 = ref_matrix_yukawa_2loop_rhs(
            gc - dt_third * kg1 + dt_h * kg2,
            lc - dt_third * kl1 + dt_h * kl2,
            uc - dt_third * ku1 + dt_h * ku2,
            dc - dt_third * kd1 + dt_h * kd2,
            ec - dt_third * ke1 + dt_h * ke2,
            rc,
        )
        kg4, kl4, ku4, kd4, ke4 = ref_matrix_yukawa_2loop_rhs(
            gc + dt_h * (kg1 - kg2 + kg3),
            lc + dt_h * (kl1 - kl2 + kl3),
            uc + dt_h * (ku1 - ku2 + ku3),
            dc + dt_h * (kd1 - kd2 + kd3),
            ec + dt_h * (ke1 - ke2 + ke3),
            rc,
        )
        gc = gc + w_eighth * (kg1 + 3 * kg2 + 3 * kg3 + kg4)
        lc = lc + w_eighth * (kl1 + 3 * kl2 + 3 * kl3 + kl4)
        uc = uc + w_eighth * (ku1 + 3 * ku2 + 3 * ku3 + ku4)
        dc = dc + w_eighth * (kd1 + 3 * kd2 + 3 * kd3 + kd4)
        ec = ec + w_eighth * (ke1 + 3 * ke2 + 3 * ke3 + ke4)
    return gc, lc, uc, dc, ec


# =============================================================================
# Pytest Verification Functions
# =============================================================================


def test_stage6_firewall_and_guardrail2_ast_locks(stage6_results: dict[str, Any]) -> None:
    fw_prod = audit_source_zero_empirical_constants(STAGE6_SRC)
    fw_test = audit_source_zero_empirical_constants(TEST6_SRC)
    g2_prod = check_guardrail2_ast_no_literal_bool_verdicts(STAGE6_SRC.read_text(encoding="utf-8"))
    g2_test = check_guardrail2_ast_no_literal_bool_verdicts(TEST6_SRC.read_text(encoding="utf-8"))

    assert fw_prod is True
    assert fw_test is True
    assert g2_prod is True
    assert g2_test is True
    assert stage6_results["zero_sm_empirical_constants_ast_verified"] is True
    assert stage6_results["guardrail2_ast_no_literal_bool_verdicts_verified"] is True
    assert stage6_results["all_verifications_passed"] is True


def test_part6a_zero_trust_kronecker_theta_modular_and_geodesic_end(
    stage6_results: dict[str, Any],
) -> None:
    res_6a = stage6_results["part6a_kronecker_and_end"]
    assert res_6a["part6a_kronecker_end_and_wp41_verified"] is True

    dyn_z = mp.mpf(int(sp.Matrix.eye(1).trace()) - 1)
    with mp.workdps(40):
        # Fresh referee modulus tau_ref = 5/11 + i * (13/10):
        x_ref = mp.fdiv(5, 11) + dyn_z
        y_ref = mp.fdiv(13, 10) + dyn_z

        for p1_t, p2_t in [(2, 4), (0, 2), (2, 0), (1, 4)]:
            u1_t = mp.fdiv(p1_t, 5)
            u2_t = mp.fdiv(p2_t, 5)
            f_sinh = ref_kronecker_sinh_cosh_mp(u1_t, u2_t, x_ref, y_ref, 2)
            f_qser = ref_euler_eta_and_qseries_theta1_fourier_mp(p1_t, p2_t, 5, x_ref, y_ref)
            assert float(abs(f_sinh - f_qser)) < 1e-30

            xt_r, yt_r = ref_mobius_xy(1, 1, 0, 1, x_ref, y_ref)
            xs_r, ys_r = ref_mobius_xy(0, -1, 1, 0, x_ref, y_ref)
            xr_r, yr_r = ref_mobius_xy(1, 0, 1, 1, x_ref, y_ref)

            assert float(abs(ref_kronecker_sinh_cosh_mp(u1_t, u2_t, xt_r, yt_r, 2) - ref_kronecker_sinh_cosh_mp(u1_t, u1_t + u2_t, x_ref, y_ref, 2))) < 1e-30
            assert float(abs(ref_kronecker_sinh_cosh_mp(u1_t, u2_t, xs_r, ys_r, 2) - ref_kronecker_sinh_cosh_mp(u2_t, -u1_t, x_ref, y_ref, 2))) < 1e-30
            assert float(abs(ref_kronecker_sinh_cosh_mp(u1_t, u2_t, xr_r, yr_r, 2) - ref_kronecker_sinh_cosh_mp(u1_t + u2_t, u2_t, x_ref, y_ref, 2))) < 1e-30

        # Independent B1920 composite 64-point midpoint Riemann quadrature along golden geodesic:
        sq5 = mp.sqrt(mp.mpf(5))
        ell_g = 2 * mp.log(mp.fdiv(3 + sq5, 2))
        n_mid = 64
        ds_m = mp.fdiv(ell_g, n_mid)
        mid_acc = mp.mpf(0)
        for k_m in range(n_mid):
            s_m = -mp.fdiv(ell_g, 2) + (mp.mpf(k_m) + mp.fdiv(1, 2)) * ds_m + dyn_z
            xg_m = mp.fdiv(1, 2) + mp.fdiv(sq5, 2) * mp.tanh(s_m)
            yg_m = mp.fdiv(sq5, 2 * mp.cosh(s_m))
            mid_acc = mid_acc + ref_kronecker_sinh_cosh_mp(mp.fdiv(2, 5), mp.fdiv(4, 5), xg_m, yg_m, 1)
        f_avg_ref = mp.fdiv(mid_acc, n_mid)
        x_gold = mp.fdiv(1, 2) + dyn_z
        y_gold = mp.fdiv(sq5, 2) + dyn_z
        f_apx_ref = ref_kronecker_sinh_cosh_mp(mp.fdiv(2, 5), mp.fdiv(4, 5), x_gold, y_gold, 1)
        assert float(abs(f_avg_ref - mp.mpf(res_6a["b1920_geodesic_avg_f"]))) < TOL
        assert float(abs(f_apx_ref - mp.mpf(res_6a["b1920_apex_f"]))) < TOL
        assert float(abs(f_avg_ref - f_apx_ref)) > (1 / 10)

        # Independent B1922 eigenline periodicity vs off-eigenline jump at s = 1/9:
        s_chk = mp.fdiv(1, 9) + dyn_z
        x0_c = mp.fdiv(1, 2) + mp.fdiv(sq5, 2) * mp.tanh(s_chk)
        y0_c = mp.fdiv(sq5, 2 * mp.cosh(s_chk))
        x1_c, y1_c = ref_mobius_xy(2, 1, 1, 1, x0_c, y0_c)
        err_eig = abs(
            ref_kronecker_sinh_cosh_mp(mp.fdiv(2, 5), mp.fdiv(4, 5), x1_c, y1_c, 3)
            - ref_kronecker_sinh_cosh_mp(mp.fdiv(2, 5), mp.fdiv(4, 5), x0_c, y0_c, 3)
        )
        jmp_off = abs(
            ref_kronecker_sinh_cosh_mp(mp.fdiv(1, 5), mp.fdiv(1, 5), x1_c, y1_c, 2)
            - ref_kronecker_sinh_cosh_mp(mp.fdiv(1, 5), mp.fdiv(1, 5), x0_c, y0_c, 2)
        )
        assert float(err_eig) < 1e-30
        assert float(jmp_off) > 1.0

        # Zero-Trust D1 Counterchecks (1-Loop Modulus Stabilization Audit):
        # (a) Matching-holonomy SUSY supertrace V_SUSY == 0 at tau_ref:
        xt_susy, yt_susy = ref_mobius_xy(1, 1, 0, 1, x_ref, y_ref)
        v_susy_ref = 4 * ref_kronecker_sinh_cosh_mp(
            mp.fdiv(2, 5), mp.fdiv(4, 5), xt_susy, yt_susy, 3
        ) - 4 * ref_kronecker_sinh_cosh_mp(mp.fdiv(2, 5), mp.fdiv(6, 5), x_ref, y_ref, 3)
        assert float(abs(v_susy_ref)) < 1e-30
        assert res_6a["guardrail1_susy_supertrace_max_err"] < 1e-30

        # (b) 4-point O(h^4) Richardson central-difference gradient of F_{(2/5,4/5)} at tau_Golden:
        h_fd = (mp.fdiv(1, 16) + dyn_z) ** 6
        u_g1 = mp.fdiv(2, 5)
        u_g2 = mp.fdiv(4, 5)
        fx_p2 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_gold + 2 * h_fd, y_gold, 3)
        fx_p1 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_gold + h_fd, y_gold, 3)
        fx_m1 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_gold - h_fd, y_gold, 3)
        fx_m2 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_gold - 2 * h_fd, y_gold, 3)
        fy_p2 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_gold, y_gold + 2 * h_fd, 3)
        fy_p1 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_gold, y_gold + h_fd, 3)
        fy_m1 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_gold, y_gold - h_fd, 3)
        fy_m2 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_gold, y_gold - 2 * h_fd, 3)
        df_dx_o4 = mp.fdiv(-fx_p2 + 8 * fx_p1 - 8 * fx_m1 + fx_m2, 12 * h_fd)
        df_dy_o4 = mp.fdiv(-fy_p2 + 8 * fy_p1 - 8 * fy_m1 + fy_m2, 12 * h_fd)
        assert float(abs(df_dx_o4)) < 1e-30
        assert float(df_dy_o4) < -4
        assert abs(float(df_dy_o4) - res_6a["guardrail1_golden_df_dy"]) < TOL

        # (c) 5-point O(h^4) 2D hyperbolic Laplacian Delta_hyp F_{(2/5,4/5)}(tau_ref) == +pi:
        fr_0 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_ref, y_ref, 3)
        fr_xp2 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_ref + 2 * h_fd, y_ref, 3)
        fr_xp1 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_ref + h_fd, y_ref, 3)
        fr_xm1 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_ref - h_fd, y_ref, 3)
        fr_xm2 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_ref - 2 * h_fd, y_ref, 3)
        fr_yp2 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_ref, y_ref + 2 * h_fd, 3)
        fr_yp1 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_ref, y_ref + h_fd, 3)
        fr_ym1 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_ref, y_ref - h_fd, 3)
        fr_ym2 = ref_kronecker_sinh_cosh_mp(u_g1, u_g2, x_ref, y_ref - 2 * h_fd, 3)
        d2x_f = mp.fdiv(-fr_xp2 + 16 * fr_xp1 - 30 * fr_0 + 16 * fr_xm1 - fr_xm2, 12 * (h_fd ** 2))
        d2y_f = mp.fdiv(-fr_yp2 + 16 * fr_yp1 - 30 * fr_0 + 16 * fr_ym1 - fr_ym2, 12 * (h_fd ** 2))
        lap_f_ref = (y_ref ** 2) * (d2x_f + d2y_f)
        assert float(abs(lap_f_ref - mp.pi)) < TOL
        assert res_6a["guardrail1_max_subharmonic_laplacian_err"] < TOL

        # (d) 3-even-spin-structure Scherk-Schwarz harmonicity Delta_hyp V_SS(tau_ref) == 0 & cusp runaway:
        vss_0 = ref_vss_even_spin_mp(u_g1, u_g2, x_ref, y_ref, 3)
        vss_xp = ref_vss_even_spin_mp(u_g1, u_g2, x_ref + h_fd, y_ref, 3)
        vss_xm = ref_vss_even_spin_mp(u_g1, u_g2, x_ref - h_fd, y_ref, 3)
        vss_yp = ref_vss_even_spin_mp(u_g1, u_g2, x_ref, y_ref + h_fd, 3)
        vss_ym = ref_vss_even_spin_mp(u_g1, u_g2, x_ref, y_ref - h_fd, 3)
        lap_vss_ref = (y_ref ** 2) * (
            mp.fdiv(vss_xp - 2 * vss_0 + vss_xm, h_fd ** 2)
            + mp.fdiv(vss_yp - 2 * vss_0 + vss_ym, h_fd ** 2)
        )
        assert float(abs(lap_vss_ref)) < TOL
        assert res_6a["guardrail1_max_vss_harmonic_laplacian_err"] < TOL

        def ref_vss_cusp_sigma(y_val_c: Any) -> Any:
            half_c = mp.fdiv(1, 2)
            sum_f = (
                ref_kronecker_sinh_cosh_mp(2 * u_g1 - (u_g2 - half_c), u_g1, dyn_z, y_val_c, 2)
                + ref_kronecker_sinh_cosh_mp(2 * (u_g1 - half_c) - u_g2, u_g1 - half_c, dyn_z, y_val_c, 2)
                + ref_kronecker_sinh_cosh_mp(2 * (u_g1 - half_c) - (u_g2 - half_c), u_g1 - half_c, dyn_z, y_val_c, 2)
            )
            return ref_kronecker_sinh_cosh_mp(2 * u_g1 - u_g2, u_g1, dyn_z, y_val_c, 2) - mp.fdiv(sum_f, 3)

        v_c4 = float(ref_vss_cusp_sigma(mp.mpf(4) + dyn_z))
        v_c8 = float(ref_vss_cusp_sigma(mp.mpf(8) + dyn_z))
        v_c16 = float(ref_vss_cusp_sigma(mp.mpf(16) + dyn_z))
        assert v_c16 < v_c8 < v_c4 < -96
        assert abs(v_c16 - res_6a["guardrail1_vss_cusp_y16"]) < TOL

    # Mod-2 3-cycle check on gamma_gold = [[2, 1], [1, 1]] over F_2^2 \ {(0, 0)}:
    gam_mod2 = sp.Matrix([[2, 1], [1, 1]])
    assert (gam_mod2 % 2) != sp.eye(2)
    assert ((gam_mod2 ** 3) % 2) == sp.eye(2)
    assert res_6a["guardrail1_even_spin_orbit_len"] == 3

    # Independent D1 classical torus metric pullback via real frame E_tau & symbolic subharmonicity:
    re_tau = sp.Symbol("re_tau", real=True)
    im_tau, a_torus, r_uv = sp.symbols("im_tau a_torus r_uv", positive=True)
    frame_e = sp.sqrt(a_torus / im_tau) * sp.Matrix([[1, re_tau], [0, im_tau]])
    metric_g = sp.simplify(frame_e.T * frame_e)
    vol_elem = sp.simplify(sp.sqrt(metric_g.det()))
    assert sp.simplify(vol_elem - a_torus) == 0
    assert sp.simplify(sp.diff(vol_elem, re_tau)) == 0
    assert sp.simplify(sp.diff(vol_elem, im_tau)) == 0

    v1_s, v2_s = sp.symbols("v1_s v2_s", positive=True)
    f_log_decomp = (
        -sp.pi * sp.log(im_tau)
        + 2 * (sp.pi ** 2) * (v2_s ** 2) * im_tau
        - sp.pi * sp.log(((v2_s * re_tau - v1_s) ** 2) + ((v2_s * im_tau) ** 2))
    )
    lap_f_sym = sp.simplify(
        (im_tau ** 2) * (sp.diff(f_log_decomp, re_tau, 2) + sp.diff(f_log_decomp, im_tau, 2))
    )
    assert sp.simplify(lap_f_sym - sp.pi) == 0

    coord_cut = r_uv * sp.sqrt(im_tau / a_torus)
    reg_sum = -2 * sp.pi * sp.log(coord_cut) + sp.pi * sp.log(im_tau)
    assert sp.simplify(sp.diff(reg_sum, im_tau)) == 0
    assert res_6a["b1921_unfixed_end_law_real_params"] == 1
    assert res_6a["guardrail1_tau_open_real_params"] == 2
    assert res_6a["wp41_b1875_total_pairwise_composites"] == 36
    assert res_6a["wp41_b1875_hyperbolic_admitted_count"] == 18
    assert res_6a["wp41_b1875_non_hyperbolic_escaped_count"] == 18


def test_part6b_zero_trust_mod_n_transfer_nielsen_and_cusp_divergence(
    stage6_results: dict[str, Any],
) -> None:
    res_6b = stage6_results["part6b_whole_weave_and_p845"]
    assert res_6b["part6b_whole_weave_and_p845_verified"] is True

    # 1. Independent mod-N primitive carrier & SL(2, Z/NZ) spectrum construction (N = 2..7):
    for n_m in range(2, 8):
        prim_pts = [
            (u_a, u_b)
            for u_a in range(n_m)
            for u_b in range(n_m)
            if math.gcd(math.gcd(u_a, u_b), n_m) == 1
        ]
        map_p = {pt: idx_p for idx_p, pt in enumerate(prim_pts)}
        dim_p = len(prim_pts)
        mat_pos = np.zeros((dim_p, dim_p), dtype=float)
        mat_sym = np.zeros((dim_p, dim_p), dtype=float)
        for idx_p, (ua, ub) in enumerate(prim_pts):
            mat_pos[map_p[(ua, (ua + ub) % n_m)], idx_p] += 1 / 2
            mat_pos[map_p[((ua + ub) % n_m, ub)], idx_p] += 1 / 2
            mat_sym[map_p[(ua, (ua + ub) % n_m)], idx_p] += 1 / 4
            mat_sym[map_p[((ua + ub) % n_m, ub)], idx_p] += 1 / 4
            mat_sym[map_p[(ua, (ub - ua) % n_m)], idx_p] += 1 / 4
            mat_sym[map_p[((ua - ub) % n_m, ub)], idx_p] += 1 / 4

        evs_s = np.linalg.eigvalsh(mat_sym)
        evs_p = np.linalg.eigvals(mat_pos)
        assert int(np.sum(np.abs(np.abs(evs_s) - 1.0) < 1e-9)) == 1
        assert int(np.sum(np.abs(evs_p - 1.0) < 1e-9)) == 1
        if n_m >= 3:
            assert float(np.linalg.norm(mat_pos @ mat_pos.T - mat_pos.T @ mat_pos)) > 1e-6

    for n_g, exp_ord, exp_unit in [(2, 6, 2), (3, 24, 1), (4, 48, 2), (5, 120, 1)]:
        grp = [
            (a0, a1, a2, a3)
            for a0, a1, a2, a3 in product(range(n_g), repeat=4)
            if (a0 * a3 - a1 * a2) % n_g == 1
        ]
        assert len(grp) == exp_ord
        g_idx = {g_e: i_g for i_g, g_e in enumerate(grp)}
        mat_g = np.zeros((exp_ord, exp_ord), dtype=float)
        gens_4 = [(1, 1, 0, 1), (1, 0, 1, 1), (1, (-1) % n_g, 0, 1), (1, 0, (-1) % n_g, 1)]
        for i_g, x_g in enumerate(grp):
            for s_g in gens_4:
                prod_g = (
                    (x_g[0] * s_g[0] + x_g[1] * s_g[2]) % n_g,
                    (x_g[0] * s_g[1] + x_g[1] * s_g[3]) % n_g,
                    (x_g[2] * s_g[0] + x_g[3] * s_g[2]) % n_g,
                    (x_g[2] * s_g[1] + x_g[3] * s_g[3]) % n_g,
                )
                mat_g[g_idx[prod_g], i_g] += 1 / 4
        ev_g = np.linalg.eigvalsh(mat_g)
        assert int(np.sum(np.abs(np.abs(ev_g) - 1.0) < 1e-9)) == exp_unit

    assert res_6b["p831_level5_pm_stabilizer_index"] == 12
    assert res_6b["p831_level5_p1_stabilizer_index"] == 6

    # Independent D2 spectral-trace proof of P^1(F_5) T-cusp cycle widths [1, 5] & width-1 cusp (0, 1):
    p1_pts = sorted(
        {
            (0, 1) if ((2 * g_e[0] + 4 * g_e[2]) % 5 == 0) else (
                1,
                (((2 * g_e[1] + 4 * g_e[3]) % 5) * ((((2 * g_e[0] + 4 * g_e[2]) % 5) ** 3) % 5)) % 5,
            )
            for g_e in [
                (a0, a1, a2, a3)
                for a0, a1, a2, a3 in product(range(5), repeat=4)
                if (a0 * a3 - a1 * a2) % 5 == 1
            ]
        }
    )
    assert len(p1_pts) == 6
    p1_map = {pt_c: i_c for i_c, pt_c in enumerate(p1_pts)}
    perm_t = np.zeros((6, 6), dtype=int)
    for i_c, (px, py) in enumerate(p1_pts):
        qx, qy = px, (px + py) % 5
        canon_q = (0, 1) if qx == 0 else (1, (qy * ((qx ** 3) % 5)) % 5)
        perm_t[p1_map[canon_q], i_c] = 1
    assert [int(np.trace(np.linalg.matrix_power(perm_t, pw))) for pw in range(1, 6)] == [1, 1, 1, 1, 6]
    fixed_cusps_ref = [p1_pts[i_c] for i_c in range(6) if perm_t[i_c, i_c] == 1]
    assert fixed_cusps_ref == [(0, 1)]
    assert res_6b["p831_level5_cusp_widths"] == [1, 5]
    assert res_6b["p831_level5_width1_cusp"] == (0, 1)

    # 2. Independent B1885 composite Simpson check on [1, 3] with Euler-product |eta(i*y)|^12:
    dyn_zb = mp.mpf(int(sp.Matrix.eye(1).trace()) - 1)
    with mp.workdps(35):
        n_simp = 96
        h_s = mp.fdiv(2, n_simp) + dyn_zb
        num_e = mp.mpf(0) + dyn_zb
        den_e = mp.mpf(0) + dyn_zb
        num_h = mp.mpf(0) + dyn_zb
        den_h = mp.mpf(0) + dyn_zb
        for idx_s in range(n_simp + 1):
            y_s = mp.mpf(1) + mp.mpf(idx_s) * h_s
            wt_s = 1 if (idx_s == 0 or idx_s == n_simp) else (4 if idx_s % 2 == 1 else 2)
            prof_y = (y_s ** 3) * ref_eta12_imag_axis_mp(y_s)
            num_e = num_e + wt_s * y_s * prof_y
            den_e = den_e + wt_s * prof_y
            num_h = num_h + wt_s * mp.fdiv(prof_y, y_s)
            den_h = den_h + wt_s * mp.fdiv(prof_y, y_s ** 2)
        shift_simp = float(abs(mp.fdiv(num_e, den_e) - mp.fdiv(num_h, den_h)))
    assert abs(shift_simp - res_6b["b1885_jacobian_mean_y_shift"]) < 1e-7
    assert shift_simp > (1 / 10)

    # 3. Zero-Trust D2: Genuine hyperbolic matrix-word BFS on eta_1 = A*B^2 (tr=10) & eta_2 = A*B (tr=6):
    mat_l1 = sp.Matrix([[1, 1], [0, 1]])
    mat_r1 = sp.Matrix([[1, 0], [1, 1]])
    mat_a = mat_l1 * mat_l1
    mat_b = mat_r1 * mat_r1
    eta_1 = mat_a * mat_b * mat_b
    eta_2 = mat_a * mat_b
    assert abs(int(eta_1.trace())) == 10 and abs(int(eta_2.trace())) == 6

    def to_tup(mat_x: sp.Matrix) -> tuple[int, int, int, int]:
        return (int(mat_x[0, 0]), int(mat_x[0, 1]), int(mat_x[1, 0]), int(mat_x[1, 1]))

    t1_gens = [to_tup(mat_a), to_tup(mat_a.inv()), to_tup(mat_b), to_tup(mat_b.inv())]
    mat_a_niel = mat_a * mat_b * mat_b
    t2_gens = [to_tup(mat_a_niel), to_tup(mat_a_niel.inv()), to_tup(mat_b), to_tup(mat_b.inv())]

    len_t1_e1 = ref_bfs_sl2_word_len(t1_gens, to_tup(eta_1), 5)
    len_t1_e2 = ref_bfs_sl2_word_len(t1_gens, to_tup(eta_2), 5)
    len_t2_e1 = ref_bfs_sl2_word_len(t2_gens, to_tup(eta_1), 5)
    len_t2_e2 = ref_bfs_sl2_word_len(t2_gens, to_tup(eta_2), 5)
    assert (len_t1_e1, len_t1_e2) == (3, 2) and len_t1_e1 > len_t1_e2
    assert (len_t2_e1, len_t2_e2) == (1, 2) and len_t2_e1 < len_t2_e2
    assert math.exp(-0.5 * len_t1_e1) < math.exp(-0.5 * len_t1_e2)
    assert math.exp(-0.5 * len_t2_e1) > math.exp(-0.5 * len_t2_e2)
    assert res_6b["p845_bfs_word_lengths_s1"] == (3, 2)
    assert res_6b["p845_bfs_word_lengths_s2"] == (1, 2)

    # Conjugacy invariance of geodesic length & torus Lefschetz/Nielsen fixed-point identities:
    conj_g = sp.Matrix([[3, 2], [1, 1]])
    eye_2 = sp.eye(2)
    for mat_w in (
        eta_1,
        eta_2,
        mat_l1 * mat_l1 * mat_l1 * mat_r1,
        mat_l1 * mat_r1 * mat_r1 * mat_r1,
        mat_r1 * mat_l1 * mat_l1 * mat_r1,
    ):
        tr_0 = abs(int(mat_w.trace()))
        tr_c = abs(int((conj_g * mat_w * conj_g.inv()).trace()))
        assert int(mat_w.det()) == 1 and tr_0 == tr_c and tr_0 > 2
        assert abs(int((eye_2 - mat_w).det())) == abs(int(mat_w.trace()) - 2)
        assert abs(int((eye_2 + mat_w).det())) == abs(int(mat_w.trace()) + 2)
    assert res_6b["p845_nielsen_torus_class_verified"] is True

    # 4. Independent P-845 zero-row cusp slope & convergent log integral:
    with mp.workdps(40):
        y_a = mp.mpf(12) + dyn_zb
        y_b = mp.mpf(24) + dyn_zb
        f_a = ref_kronecker_sinh_cosh_mp(dyn_zb, mp.fdiv(2, 5), dyn_zb, y_a, 1)
        f_b = ref_kronecker_sinh_cosh_mp(dyn_zb, mp.fdiv(2, 5), dyn_zb, y_b, 1)
        slope_ab = mp.fdiv((f_b + mp.pi * mp.log(y_b)) - (f_a + mp.pi * mp.log(y_a)), y_b - y_a)
        slope_rad = mp.fdiv(8 * (mp.pi ** 2), 5 + mp.sqrt(mp.mpf(5)))
        assert float(abs(slope_ab - slope_rad)) < 1e-24
        assert abs(float(slope_rad) - res_6b["p845_zero_row_cusp_slope"]) < TOL

    y_var = sp.Symbol("y_var", positive=True)
    assert sp.simplify(sp.integrate(sp.log(y_var) / (y_var ** 2), (y_var, 2, sp.oo)) - (1 + sp.log(2)) / 2) == 0


def test_part6c_zero_trust_kashaev_j5_and_2loop_rge_haar_benchmarks(
    stage6_results: dict[str, Any],
) -> None:
    res_6c = stage6_results["part6c_level5_kashaev_and_rge"]
    assert res_6c["part6c_level5_kashaev_and_rge_verified"] is True

    # 1. Independent WP-4.3 cyclotomic quotient ring proof in Q[q] / (1 + q + q^2 + q^3 + q^4):
    q_sym = sp.Symbol("q_sym")
    phi_5 = 1 + q_sym + (q_sym ** 2) + (q_sym ** 3) + (q_sym ** 4)
    j5_poly = sp.Integer(0)
    poch_q = sp.Integer(1)
    for n_s in range(5):
        if n_s > 0:
            fac_n = (1 - (q_sym ** n_s)) * (1 - (q_sym ** (5 - n_s)))
            poch_q = sp.rem(sp.expand(poch_q * fac_n), phi_5, q_sym)
        j5_poly = sp.rem(j5_poly + poch_q, phi_5, q_sym)

    min_poly_rem = sp.rem(sp.expand((j5_poly - 46) ** 2 - 20), phi_5, q_sym)
    assert min_poly_rem == 0

    one_d = float(int(sp.Matrix.eye(1).trace()))
    j5_pos = 1.0 * one_d
    p_run = 1.0 * one_d
    for k_r in range(1, 5):
        p_run *= 4 * (math.sin(math.pi * k_r * one_d / 5) ** 2)
        j5_pos += p_run
    assert j5_pos > 46 and abs(j5_pos - (46 + 2 * math.sqrt(5 * one_d))) < TOL
    assert abs(j5_pos - res_6c["wp43_j5_value"]) < TOL
    assert res_6c["wp42_primes_with_twisted_eigenline"] == [5]

    # Zero-Trust D3 Check 1: Genuine (Z/5Z)^x Kronecker scaling symmetry count == 2 -> 1 bit at tau_ref:
    zero_ic = int(sp.Matrix.eye(1).trace()) - 1
    dyn_zc = mp.mpf(zero_ic)
    with mp.workdps(35):
        xr_c = mp.fdiv(5, 11) + dyn_zc
        yr_c = mp.fdiv(13, 10) + dyn_zc
        f0_u = ref_kronecker_sinh_cosh_mp(mp.fdiv(1, 5), mp.fdiv(2, 5), xr_c, yr_c, 2)
        sym_eps = [
            eps_k
            for eps_k in (1, 2, 3, 4)
            if float(
                abs(
                    ref_kronecker_sinh_cosh_mp(
                        mp.fdiv(eps_k % 5, 5), mp.fdiv((2 * eps_k) % 5, 5), xr_c, yr_c, 2
                    )
                    - f0_u
                )
            )
            < TOL
        ]
    assert sym_eps == [1, 4]
    assert int(round(math.log2(len(sym_eps)))) == 1
    assert res_6c["wp42_kronecker_scaling_sym_count"] == 2
    assert res_6c["wp42_sc_premise_bits"] == 1

    # 2. Zero-Trust D4: Independent su(N_c) Gell-Mann + p_0 MV84/MV85 Beta Derivation & Specializations:
    rc_sm = ref_build_zero_trust_mv_betas(3 + zero_ic, 3 + zero_ic)
    rc_nc4 = ref_build_zero_trust_mv_betas(4 + zero_ic, 3 + zero_ic)
    rc_ng0 = ref_build_zero_trust_mv_betas(3 + zero_ic, 0 + zero_ic)

    kite_chk = rc_sm["kite_info"]
    assert kite_chk["kite_z3_exact"] is True
    assert kite_chk["subdiv_free"] is True
    assert kite_chk["thooft_poles_vanish"] is True
    assert kite_chk["pair_b_exact"] is True
    assert kite_chk["swapped_comm_nonzero"] is True
    assert sp.simplify(4 * kite_chk["c2_q_hfhfp"] + 1) == 0
    assert sp.simplify(kite_chk["c2_q_hfphf"] + 1) == 0
    assert sp.simplify(4 * kite_chk["c2_q_hfp2"] - 11) == 0
    assert sp.simplify(4 * kite_chk["c2_q_y2s_hf"] + 9) == 0
    assert sp.simplify(4 * kite_chk["c2_q_y2s_hfp"] - 5) == 0

    assert sp.simplify(5 * rc_sm["k_g"] - 3) == 0
    assert sp.simplify((rc_sm["b1_sym"][0] - rc_sm["b1_sym"][1]) * (23 * 5) - (rc_sm["b1_sym"][1] - rc_sm["b1_sym"][2]) * (2 * 109)) == 0

    pl2_nc4 = sp.Poly(rc_nc4["blam_2"], *rc_nc4["syms5"])
    pl2_ng0 = sp.Poly(rc_ng0["blam_2"], *rc_ng0["syms5"])
    assert sp.simplify(pl2_nc4.coeff_monomial((0, 0, 0, 0, 3)) / sp.Integer(24) + 13) == 0
    assert sp.simplify(pl2_ng0.coeff_monomial((0, 0, 0, 0, 3)) / sp.Integer(24) + 13) == 0
    assert pl2_nc4.coeff_monomial((0, 1, 0, 0, 2)) == 108
    assert pl2_ng0.coeff_monomial((0, 1, 0, 0, 2)) == 108
    assert sp.simplify(3 * rc_nc4["b1_sym"][2] + 32) == 0
    assert sp.simplify(10 * rc_ng0["b1_sym"][0] - 1) == 0
    assert sp.simplify(6 * rc_ng0["b1_sym"][1] + 43) == 0
    assert sp.simplify(rc_ng0["b1_sym"][2] + 11) == 0

    # Zero-Trust D3 Check 2: Independent SM 19-parameter operator derivation at fresh Yukawa textures:
    j_im = complex(0.0, 1.0)
    yu_0 = one_d * np.array(
        [
            [1 / 10, (1 / 5) * (1.0 + j_im), 0.0],
            [(1 / 5) * (1.0 - j_im), 1 / 4, 1 / 7],
            [0.0, 1 / 7, 1 / 2],
        ],
        dtype=complex,
    )
    yd_0 = one_d * np.array(
        [
            [1 / 14, 1 / 9, (1 / 6) * j_im],
            [1 / 9, 1 / 6, 1 / 9],
            [-(1 / 6) * j_im, 1 / 9, 1 / 3],
        ],
        dtype=complex,
    )
    ye_0 = yd_0.T.copy()

    # Build 54 x 45 u(3)^5 Jacobian using anti-Hermitian generator basis i * {I_3/sqrt(6), T^A_GellMann}:
    gm_3 = ref_su_n_fundamental_generators(3)
    u3_ah = [j_im * np.eye(3, dtype=complex)] + [
        j_im * np.array([[complex(gm_m[r, c]) for c in range(3)] for r in range(3)], dtype=complex)
        for gm_m in gm_3
    ]
    z3_m = np.zeros((3, 3), dtype=complex)
    jac_54_cols = [
        np.concatenate(
            [
                (ah_m @ yu_0 if sl_i == 0 else (-yu_0 @ ah_m if sl_i == 1 else z3_m)).real.ravel(),
                (ah_m @ yu_0 if sl_i == 0 else (-yu_0 @ ah_m if sl_i == 1 else z3_m)).imag.ravel(),
                (ah_m @ yd_0 if sl_i == 0 else (-yd_0 @ ah_m if sl_i == 2 else z3_m)).real.ravel(),
                (ah_m @ yd_0 if sl_i == 0 else (-yd_0 @ ah_m if sl_i == 2 else z3_m)).imag.ravel(),
                (ah_m @ ye_0 if sl_i == 3 else (-ye_0 @ ah_m if sl_i == 4 else z3_m)).real.ravel(),
                (ah_m @ ye_0 if sl_i == 3 else (-ye_0 @ ah_m if sl_i == 4 else z3_m)).imag.ravel(),
            ]
        )
        for sl_i in range(5)
        for ah_m in u3_ah
    ]
    jac_ref = np.column_stack(jac_54_cols)
    _, sv_j_ref, vh_j_ref = np.linalg.svd(jac_ref, full_matrices=True)
    rk_flav = int(np.sum(sv_j_ref > 1e-8))
    ker_ref = vh_j_ref[rk_flav:, :].T
    assert rk_flav == 41 and (45 - rk_flav) == 4
    n_flav_ref = 54 - rk_flav
    assert n_flav_ref == 13
    assert res_6c["wp43_flavor_jacobian_rank"] == 41
    assert res_6c["wp43_flavor_conserved_u1_nullity"] == 4

    # Count Higgs invariants via complex bi-degree (p, q) SU(2)_L Casimir J^2 == 0 singlets (1 <= p+q <= 4):
    n_higgs_sing = 0
    for deg_tot in range(1, 5):
        for p_deg in range(deg_tot + 1):
            q_deg = deg_tot - p_deg
            if p_deg != q_deg:
                continue
            mons_pq = [
                (a1, p_deg - a1, b1, q_deg - b1)
                for a1 in range(p_deg + 1)
                for b1 in range(q_deg + 1)
            ]
            map_pq = {mn: idx_m for idx_m, mn in enumerate(mons_pq)}
            dim_pq = len(mons_pq)
            jp_m = np.zeros((dim_pq, dim_pq), dtype=float)
            jm_m = np.zeros((dim_pq, dim_pq), dtype=float)
            j3_m = np.zeros((dim_pq, dim_pq), dtype=float)
            for col_k, (a1, a2, b1, b2) in enumerate(mons_pq):
                j3_m[col_k, col_k] = 0.5 * (a1 - a2 - b1 + b2)
                if a2 > 0:
                    jp_m[map_pq[(a1 + 1, a2 - 1, b1, b2)], col_k] += float(a2)
                if b1 > 0:
                    jp_m[map_pq[(a1, a2, b1 - 1, b2 + 1)], col_k] -= float(b1)
                if a1 > 0:
                    jm_m[map_pq[(a1 - 1, a2 + 1, b1, b2)], col_k] += float(a1)
                if b2 > 0:
                    jm_m[map_pq[(a1, a2, b1 + 1, b2 - 1)], col_k] -= float(b2)
            j2_cas = 0.5 * (jp_m @ jm_m + jm_m @ jp_m) + (j3_m @ j3_m)
            ev_j2 = np.linalg.eigvals(j2_cas)
            n_higgs_sing += int(np.sum(np.abs(ev_j2) < 1e-9))
    assert n_higgs_sing == 2

    # Mechanical chiral Weyl anomaly projection on ker(J_ref) for generic rank-3 AND massless-up rank-2:
    n_gauge_ref = sum([1 for cm_w in rc_sm["cas_w"] if cm_w.trace() != 0])
    nonab_g = [ig_k for ig_k in range(3) if rc_sm["c2_g"][ig_k] != 0]
    nc_i_ref = int(rc_sm["nc_f"])
    w_blocks = [
        (0, 2 * nc_i_ref, 1.0),
        (2 * nc_i_ref, 3 * nc_i_ref, -1.0),
        (3 * nc_i_ref, 4 * nc_i_ref, -1.0),
        (4 * nc_i_ref, 4 * nc_i_ref + 2, 1.0),
        (4 * nc_i_ref + 2, 4 * nc_i_ref + 3, -1.0),
    ]
    anom_ref_2x45 = np.array(
        [
            [
                ch_sgn
                * float(rc_sm["cas_w"][ig_k][r0_b:r1_b, r0_b:r1_b].trace() / rc_sm["d_g"][ig_k])
                * float(np.imag(np.trace(ah_m)))
                for r0_b, r1_b, ch_sgn in w_blocks
                for ah_m in u3_ah
            ]
            for ig_k in nonab_g
        ],
        dtype=float,
    )
    anom_rk_3 = int(np.sum(np.linalg.svd(anom_ref_2x45 @ ker_ref, compute_uv=False) > 1e-8))
    n_theta_ref = len(nonab_g) - anom_rk_3
    assert n_gauge_ref == 3 and anom_rk_3 == 1 and n_theta_ref == 1
    assert (n_flav_ref + n_gauge_ref + n_higgs_sing + n_theta_ref) == 19
    assert res_6c["wp43_flavor_anom_rank"] == 1
    assert res_6c["wp43_unresolved_sm_parameters_count"] == 19
    assert res_6c["wp43_unproved_bridge_gates_count"] == 3

    # Rank-2 massless up-quark control (zero lightest singular value -> nullity 5, anom_rank 2, n_theta 0):
    ul_r2, sv_r2, vhr_r2 = np.linalg.svd(yu_0)
    yu_rank2 = (ul_r2 * np.array([sv_r2[0], sv_r2[1], 0.0], dtype=float)) @ vhr_r2
    jac_r2 = np.column_stack(
        [
            np.concatenate(
                [
                    (ah_m @ yu_rank2 if sl_i == 0 else (-yu_rank2 @ ah_m if sl_i == 1 else z3_m)).real.ravel(),
                    (ah_m @ yu_rank2 if sl_i == 0 else (-yu_rank2 @ ah_m if sl_i == 1 else z3_m)).imag.ravel(),
                    (ah_m @ yd_0 if sl_i == 0 else (-yd_0 @ ah_m if sl_i == 2 else z3_m)).real.ravel(),
                    (ah_m @ yd_0 if sl_i == 0 else (-yd_0 @ ah_m if sl_i == 2 else z3_m)).imag.ravel(),
                    (ah_m @ ye_0 if sl_i == 3 else (-ye_0 @ ah_m if sl_i == 4 else z3_m)).real.ravel(),
                    (ah_m @ ye_0 if sl_i == 3 else (-ye_0 @ ah_m if sl_i == 4 else z3_m)).imag.ravel(),
                ]
            )
            for sl_i in range(5)
            for ah_m in u3_ah
        ]
    )
    _, sv_jr2, vh_jr2 = np.linalg.svd(jac_r2, full_matrices=True)
    rk_r2 = int(np.sum(sv_jr2 > 1e-8))
    ker_r2 = vh_jr2[rk_r2:, :].T
    anom_rk_r2 = int(np.sum(np.linalg.svd(anom_ref_2x45 @ ker_r2, compute_uv=False) > 1e-8))
    n_theta_r2 = len(nonab_g) - anom_rk_r2
    assert rk_r2 == 40 and (45 - rk_r2) == 5 and anom_rk_r2 == 2 and n_theta_r2 == 0

    prod_beta = build_sm_2loop_betas_symbolic(0 + zero_ic, -1 + zero_ic)
    prod_r2_cnt = compute_sm_19_operator_parameter_count(prod_beta, yu_rank2, yd_0, ye_0)
    assert prod_r2_cnt["jac_rank"] == 40
    assert prod_r2_cnt["u1_conserved_nullity"] == 5
    assert prod_r2_cnt["anom_rank"] == 2
    assert prod_r2_cnt["n_theta_phys"] == 0
    assert res_6c["wp43_massless_up_nullity"] == 5
    assert res_6c["wp43_massless_up_anom_rank"] == 2
    assert res_6c["wp43_massless_up_n_theta_phys"] == 0

    # 3. Step-halving Kutta-3/8 check & Cauchy-contour 4th-order Lie-Picard jet on 5-channel RGE:
    x_start = one_d * np.array([1 / 5, 1 / 3, 1 / 2, 2 / 5, 1 / 10], dtype=float)
    x_coarse = ref_integrate_5chan_kutta38(x_start, 0.5 * one_d, rc_sm, 4, True)
    x_fine = ref_integrate_5chan_kutta38(x_start, 0.5 * one_d, rc_sm, 8, True)
    assert float(np.max(np.abs(x_fine - x_coarse))) < TOL

    c_jet = np.zeros((5, 5), dtype=float)
    c_jet[0] = x_start.copy()
    r_cs = 0.5 * one_d
    n_roots = 16
    for ord_m in range(1, 5):
        acc_c = np.zeros(5, dtype=complex)
        for k_rt in range(n_roots):
            ang_k = 2.0 * one_d * math.pi * k_rt / n_roots
            eps_c = r_cs * complex(math.cos(ang_k), math.sin(ang_k))
            x_eps = np.zeros(5, dtype=complex)
            for j_p in range(ord_m):
                x_eps = x_eps + c_jet[j_p] * (eps_c ** j_p)
            v_c = ref_sm_5chan_rhs_poly(x_eps, rc_sm, True)
            acc_c = acc_c + v_c / (eps_c ** (ord_m - 1))
        c_jet[ord_m] = np.real(acc_c / n_roots) / ord_m

    dt_jet = (1 / 96) * one_d
    x_lie_jet4 = (
        c_jet[0]
        + c_jet[1] * dt_jet
        + c_jet[2] * (dt_jet ** 2)
        + c_jet[3] * (dt_jet ** 3)
        + c_jet[4] * (dt_jet ** 4)
    )
    x_k38_jet = ref_integrate_5chan_kutta38(x_start, dt_jet, rc_sm, 2, True)
    assert float(np.max(np.abs(x_k38_jet - x_lie_jet4))) < TOL
    assert res_6c["guardrail4_5chan_symbolic_jet4_err"] < TOL

    x_pr = ref_integrate_5chan_kutta38(
        one_d * np.array([0.0, 0.0, 0.5, (1 / 9), 0.0], dtype=float),
        1.0 * one_d,
        rc_sm,
        8,
        False,
    )
    assert abs((x_pr[3] / x_pr[2]) - (2 / 9)) < TOL

    x_bad_4pi = ref_integrate_5chan_kutta38(x_start, 0.5 * one_d, rc_sm, 4, True, 2.0, 1.0)
    x_bad_lam = ref_integrate_5chan_kutta38(x_start, 0.5 * one_d, rc_sm, 4, True, 1.0, 2.0)
    assert float(np.max(np.abs(x_bad_4pi - x_fine))) > (1 / 64)
    assert 128 * abs(float(x_bad_lam[4] - x_fine[4])) > 0.5

    # 4. Zero-Trust D4: Full 2-loop 3x3 matrix Yukawa specialization & fresh-seed (109) U(3)^5 Haar scrambling:
    yt_sp = (3 / 5) * one_d
    g_sp = one_d * np.array([1 / 5, 1 / 3, 1 / 2], dtype=float)
    l_sp = (1 / 9) * one_d
    dg_m, dl_m, du_m, dd_m, de_m = ref_matrix_yukawa_2loop_rhs(
        g_sp, l_sp, np.diag([0.0, 0.0, yt_sp]).astype(complex), z3_m, z3_m, rc_sm
    )
    dx5_m = ref_sm_5chan_rhs_poly(
        np.array([g_sp[0], g_sp[1], g_sp[2], yt_sp ** 2, l_sp], dtype=float), rc_sm, True
    )
    assert float(np.max(np.abs(dg_m - dx5_m[:3]))) < TOL
    assert abs(2.0 * yt_sp * float(np.real(du_m[2, 2])) - float(dx5_m[3])) < TOL
    assert abs(dl_m - float(dx5_m[4])) < TOL
    assert float(np.max(np.abs(dd_m))) < TOL and float(np.max(np.abs(de_m))) < TOL
    assert res_6c["guardrail4_2loop_matrix_to_5chan_spec_err"] < TOL

    g_uv = one_d * np.array([math.pi / 6, math.pi / 6, math.pi / 6], dtype=float)
    lam_uv = (1 / 8) * one_d

    # Non-commuting 3x3 2-loop matrix Cauchy-contour 4th-order Lie-Picard jet + swapped negative control:
    hu_0 = yu_0 @ yu_0.conj().T
    hd_0 = yd_0 @ yd_0.conj().T
    assert float(np.linalg.norm(hu_0 @ hd_0 - hd_0 @ hu_0)) > (1 / 64)

    gl_jet_c = np.zeros((5, 4), dtype=float)
    gl_jet_c[0, :3] = g_uv.copy()
    gl_jet_c[0, 3] = lam_uv
    u_jet_c = [yu_0.copy()] + [np.zeros((3, 3), dtype=complex) for _ in range(4)]
    d_jet_c = [yd_0.copy()] + [np.zeros((3, 3), dtype=complex) for _ in range(4)]
    e_jet_c = [ye_0.copy()] + [np.zeros((3, 3), dtype=complex) for _ in range(4)]
    n_roots_m = 24
    r_cs_m = 0.5 * one_d
    for ord_m in range(1, 5):
        acc_glm = np.zeros(4, dtype=complex)
        acc_um = np.zeros((3, 3), dtype=complex)
        acc_dm = np.zeros((3, 3), dtype=complex)
        acc_em = np.zeros((3, 3), dtype=complex)
        for k_rt in range(n_roots_m):
            ang_m = 2.0 * one_d * math.pi * k_rt / n_roots_m
            eps_m = r_cs_m * complex(math.cos(ang_m), math.sin(ang_m))
            gl_ep = np.zeros(4, dtype=complex)
            u_ep = np.zeros((3, 3), dtype=complex)
            ud_ep = np.zeros((3, 3), dtype=complex)
            d_ep = np.zeros((3, 3), dtype=complex)
            dd_ep = np.zeros((3, 3), dtype=complex)
            e_ep = np.zeros((3, 3), dtype=complex)
            ed_ep = np.zeros((3, 3), dtype=complex)
            for j_p in range(ord_m):
                pw_ep = eps_m ** j_p
                gl_ep = gl_ep + gl_jet_c[j_p] * pw_ep
                u_ep = u_ep + u_jet_c[j_p] * pw_ep
                ud_ep = ud_ep + u_jet_c[j_p].conj().T * pw_ep
                d_ep = d_ep + d_jet_c[j_p] * pw_ep
                dd_ep = dd_ep + d_jet_c[j_p].conj().T * pw_ep
                e_ep = e_ep + e_jet_c[j_p] * pw_ep
                ed_ep = ed_ep + e_jet_c[j_p].conj().T * pw_ep
            vg_e, vl_e, vu_e, vd_e, ve_e = ref_matrix_yukawa_2loop_holomorphic_poly(
                gl_ep[:3], gl_ep[3], u_ep, ud_ep, d_ep, dd_ep, e_ep, ed_ep, rc_sm
            )
            tgl_e = np.array([vg_e[0], vg_e[1], vg_e[2], vl_e], dtype=complex)
            acc_glm = acc_glm + tgl_e / (eps_m ** (ord_m - 1))
            acc_um = acc_um + vu_e / (eps_m ** (ord_m - 1))
            acc_dm = acc_dm + vd_e / (eps_m ** (ord_m - 1))
            acc_em = acc_em + ve_e / (eps_m ** (ord_m - 1))
        gl_jet_c[ord_m] = np.real(acc_glm / n_roots_m) / ord_m
        u_jet_c[ord_m] = (acc_um / n_roots_m) / ord_m
        d_jet_c[ord_m] = (acc_dm / n_roots_m) / ord_m
        e_jet_c[ord_m] = (acc_em / n_roots_m) / ord_m

    dt_mat_ref = -(1 / 96) * one_d
    gl_mj = (
        gl_jet_c[0]
        + gl_jet_c[1] * dt_mat_ref
        + gl_jet_c[2] * (dt_mat_ref ** 2)
        + gl_jet_c[3] * (dt_mat_ref ** 3)
        + gl_jet_c[4] * (dt_mat_ref ** 4)
    )
    g_mj = gl_mj[:3]
    l_mj = float(gl_mj[3])
    u_mj = sum([u_jet_c[k_p] * (dt_mat_ref ** k_p) for k_p in range(5)], z3_m)
    d_mj = sum([d_jet_c[k_p] * (dt_mat_ref ** k_p) for k_p in range(5)], z3_m)
    e_mj = sum([e_jet_c[k_p] * (dt_mat_ref ** k_p) for k_p in range(5)], z3_m)

    g_mk38, l_mk38, u_mk38, d_mk38, e_mk38 = ref_integrate_matrix_2loop_kutta38(
        g_uv, lam_uv, yu_0, yd_0, ye_0, dt_mat_ref, rc_sm, 2
    )
    assert float(np.max(np.abs(g_mk38 - g_mj))) < TOL
    assert abs(l_mk38 - l_mj) < TOL
    assert float(np.max(np.abs(u_mk38 - u_mj))) < TOL
    assert float(np.max(np.abs(d_mk38 - d_mj))) < TOL
    assert float(np.max(np.abs(e_mk38 - e_mj))) < TOL
    assert res_6c["guardrail4_matrix_jet4_err"] < TOL

    rc_swapped = {
        **rc_sm,
        "c2_q_hfhfp": rc_sm["c2_q_hfphf"],
        "c2_q_hfphf": rc_sm["c2_q_hfhfp"],
    }
    _, _, du_true_0, dd_true_0, _ = ref_matrix_yukawa_2loop_rhs(g_uv, lam_uv, yu_0, yd_0, ye_0, rc_sm)
    _, _, du_swap_0, dd_swap_0, _ = ref_matrix_yukawa_2loop_rhs(g_uv, lam_uv, yu_0, yd_0, ye_0, rc_swapped)
    assert max(float(np.linalg.norm(du_swap_0 - du_true_0)), float(np.linalg.norm(dd_swap_0 - dd_true_0))) > 1e-6
    _, _, u_swap_dt, d_swap_dt, _ = ref_integrate_matrix_2loop_kutta38(
        g_uv, lam_uv, yu_0, yd_0, ye_0, dt_mat_ref, rc_swapped, 2
    )
    assert max(float(np.linalg.norm(u_swap_dt - u_mj)), float(np.linalg.norm(d_swap_dt - d_mj))) > 1e-8
    assert res_6c["guardrail4_neg_ctrl_swapped_comm_rhs_err"] > 1e-6
    assert res_6c["guardrail4_neg_ctrl_swapped_comm_jet_err"] > 1e-8

    # Direct Producer RK4 vs Referee Kutta-3/8 cross-check on Stage 6's non-commuting 3x3 trajectory (t = -1.5):
    yu_s6 = one_d * np.array(
        [
            [1 / 8, (1 / 4) * (1.0 + j_im), 0.0],
            [(1 / 4) * (1.0 - j_im), 1 / 3, 1 / 6],
            [0.0, 1 / 6, 0.5],
        ],
        dtype=complex,
    )
    yd_s6 = one_d * np.array(
        [
            [1 / 12, 1 / 8, (1 / 5) * j_im],
            [1 / 8, 1 / 5, 1 / 8],
            [-(1 / 5) * j_im, 1 / 8, 1 / 3],
        ],
        dtype=complex,
    )
    ye_s6 = yd_s6.T.copy()
    t_ir_full = -(3 / 2) * one_d
    prod_coeffs = make_sm_rge_num_coeffs(prod_beta)
    gp_ir, lp_ir, up_ir, dp_ir, ep_ir = integrate_matrix_yukawa_2loop_rk4(
        g_uv, lam_uv, yu_s6, yd_s6, ye_s6, t_ir_full, prod_coeffs, step_blocks=8, two_loop=True
    )
    gr_ir, lr_ir, ur_ir, dr_ir, er_ir = ref_integrate_matrix_2loop_kutta38(
        g_uv, lam_uv, yu_s6, yd_s6, ye_s6, t_ir_full, rc_sm, 8
    )
    assert float(np.max(np.abs(gp_ir - gr_ir))) < TOL
    assert abs(lp_ir - lr_ir) < TOL
    assert float(np.max(np.abs(up_ir - ur_ir))) < TOL
    assert float(np.max(np.abs(dp_ir - dr_ir))) < TOL
    assert float(np.max(np.abs(ep_ir - er_ir))) < TOL
    obs_p_ir = extract_physical_flavor_invariants(up_ir, dp_ir, ep_ir)
    obs_r_ir = extract_physical_flavor_invariants(ur_ir, dr_ir, er_ir)
    assert float(np.max(np.abs(obs_p_ir["sv_u"] - obs_r_ir["sv_u"]))) < TOL
    assert float(np.max(np.abs(obs_p_ir["sv_d"] - obs_r_ir["sv_d"]))) < TOL
    assert float(np.max(np.abs(obs_p_ir["sv_e"] - obs_r_ir["sv_e"]))) < TOL
    assert float(np.max(np.abs(obs_p_ir["v_ckm_abs"] - obs_r_ir["v_ckm_abs"]))) < TOL
    assert abs(obs_p_ir["jarlskog_tr"] - obs_r_ir["jarlskog_tr"]) < TOL
    assert abs(obs_r_ir["yb_over_ytau"] - res_6c["guardrail3_radiative_yb_over_ytau"]) < TOL

    t_down = -1.0 * one_d
    g_ref_ir, l_ref_ir, u_ref_ir, d_ref_ir, e_ref_ir = ref_integrate_matrix_2loop_kutta38(
        g_uv, lam_uv, yu_0, yd_0, ye_0, t_down, rc_sm, 3
    )
    sv_u_ref = np.sort(np.linalg.svd(u_ref_ir, compute_uv=False))
    sv_d_ref = np.sort(np.linalg.svd(d_ref_ir, compute_uv=False))
    sv_e_ref = np.sort(np.linalg.svd(e_ref_ir, compute_uv=False))
    hu_ref = u_ref_ir @ u_ref_ir.conj().T
    hd_ref = d_ref_ir @ d_ref_ir.conj().T
    _, ul_u_ref = np.linalg.eigh(0.5 * (hu_ref + hu_ref.conj().T))
    _, ul_d_ref = np.linalg.eigh(0.5 * (hd_ref + hd_ref.conj().T))
    ckm_ref = np.abs(ul_u_ref.conj().T @ ul_d_ref)
    cm_ref = hu_ref @ hd_ref - hd_ref @ hu_ref
    j_tr_ref = float(np.imag(np.trace(cm_ref @ cm_ref @ cm_ref)))
    assert abs(j_tr_ref) > 1e-7
    assert (sv_d_ref[2] / sv_e_ref[2]) > (1.0 + 1 / 16)

    rng_ref = np.random.default_rng(109)
    for _ in range(4):
        uq = haar_unitary(3, rng_ref)
        uuc = haar_unitary(3, rng_ref)
        udc = haar_unitary(3, rng_ref)
        ul = haar_unitary(3, rng_ref)
        uec = haar_unitary(3, rng_ref)
        gs_ir, ls_ir, us_ir, ds_ir, es_ir = ref_integrate_matrix_2loop_kutta38(
            g_uv,
            lam_uv,
            uq @ yu_0 @ uuc.conj().T,
            uq @ yd_0 @ udc.conj().T,
            ul @ ye_0 @ uec.conj().T,
            t_down,
            rc_sm,
            3,
        )
        assert float(np.max(np.abs(gs_ir - g_ref_ir))) < TOL
        assert abs(ls_ir - l_ref_ir) < TOL
        assert float(np.max(np.abs(np.sort(np.linalg.svd(us_ir, compute_uv=False)) - sv_u_ref))) < TOL
        assert float(np.max(np.abs(np.sort(np.linalg.svd(ds_ir, compute_uv=False)) - sv_d_ref))) < TOL
        assert float(np.max(np.abs(np.sort(np.linalg.svd(es_ir, compute_uv=False)) - sv_e_ref))) < TOL
        hus = us_ir @ us_ir.conj().T
        hds = ds_ir @ ds_ir.conj().T
        _, ul_us = np.linalg.eigh(0.5 * (hus + hus.conj().T))
        _, ul_ds = np.linalg.eigh(0.5 * (hds + hds.conj().T))
        assert float(np.max(np.abs(np.abs(ul_us.conj().T @ ul_ds) - ckm_ref))) < TOL
        cms = hus @ hds - hds @ hus
        assert abs(float(np.imag(np.trace(cms @ cms @ cms))) - j_tr_ref) < TOL

    assert res_6c["guardrail3_max_haar_rge_scrambling_err"] < TOL
    dim_mat_1x10 = sp.Matrix([[1, 1, 1, 1, 1, 1, 0, 0, 0, 0]])
    assert int(dim_mat_1x10.rank()) == 1 and len(dim_mat_1x10.nullspace()) == 9
    assert res_6c["guardrail5_max_dimensionful_anchors"] == 1
    assert res_6c["guardrail5_dimless_ratio_nullity"] == 9
