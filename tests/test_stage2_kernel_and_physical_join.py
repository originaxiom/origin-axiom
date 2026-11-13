"""Zero-Trust Adversarial Verification Suite for Stage 2 (WP-3.1, WP-3.2, B1866 Open Physical Question).

Strictly data-free (0 of 19). Independently constructs Q8-equivariant Koszul homotopies, curved spin-connection
operators on concrete manifolds, mpmath cusp pole quadratures, exact 8x8 integer companion-matrix cyclotomic rings
for Z[zeta_24] (without calling producer cyclotomic helpers), and direct q-series Jacobi theta / Szego pushforwards
(without mp.jtheta) paired with Haar unitary basis-scrambling tests (Guardrails 1-6 and Locks F1-F6).
"""
from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
import pytest
import sympy as sp

from origin_axiom.stage1_curved_action_cusp_orbit import (
    audit_source_zero_empirical_constants,
    check_guardrail2_ast_no_literal_bool_verdicts,
    haar_unitary,
    joint_commutant_dim_num,
)
from origin_axiom.stage2_kernel_and_physical_join import run_stage2_complete_verification

TOL = 1e-12
REPO_ROOT = Path(__file__).resolve().parents[1]
STAGE2_SRC = REPO_ROOT / "src" / "origin_axiom" / "stage2_kernel_and_physical_join.py"
TEST2_SRC = Path(__file__).resolve()


@pytest.fixture(scope="module")
def stage2_results() -> dict[str, Any]:
    return run_stage2_complete_verification()


def test_stage2_firewall_and_guardrail2_ast_locks(stage2_results: dict[str, Any]) -> None:
    assert audit_source_zero_empirical_constants(STAGE2_SRC) is True
    assert audit_source_zero_empirical_constants(TEST2_SRC) is True
    assert check_guardrail2_ast_no_literal_bool_verdicts(STAGE2_SRC.read_text(encoding="utf-8")) is True
    assert check_guardrail2_ast_no_literal_bool_verdicts(TEST2_SRC.read_text(encoding="utf-8")) is True
    assert stage2_results["zero_sm_empirical_constants_ast_verified"] is True
    assert stage2_results["all_verifications_passed"] is True


def test_wp31_zero_trust_koszul_homotopy_curved_pde_and_parabolic_integrability(
    stage2_results: dict[str, Any],
) -> None:
    # 1. Independent numerical SVD Moore-Penrose Koszul homotopy + planted non-Q8-equivariant negative control:
    e5 = np.zeros((5, 5), dtype=complex)
    for idx, cv in enumerate((2, math.sqrt(6), math.sqrt(6), 2)):
        e5[idx + 1, idx] = cv
    j5 = np.zeros((5, 5), dtype=complex)
    for idx, cv in enumerate((1, -1, 1, -1, 1)):
        j5[idx, 4 - idx] = cv
    bz = np.zeros((5, 5), dtype=complex)
    bz[1, 4] = math.sqrt(2) / math.sqrt(5)
    bz[4, 1] = -bz[1, 4]
    bz[2, 3] = -math.sqrt(3) / math.sqrt(5)
    bz[3, 2] = -bz[2, 3]
    z5 = np.zeros((5, 5), dtype=complex)

    e10 = np.block([[e5, z5], [z5, -e5.T]])
    g10 = math.sqrt(10) * np.block([[z5, bz], [j5 @ bz @ j5, z5]])
    ep10, em10 = (e10 + g10) * 0.5, (e10 - g10) * 0.5
    hp10 = ep10 @ ep10.conj().T - ep10.conj().T @ ep10
    hm10 = em10 @ em10.conj().T - em10.conj().T @ em10
    h5 = np.diag([-4, -2, 0, 2, 4]).astype(complex)
    h10 = np.block([[h5, z5], [z5, -h5]])
    n10 = np.block([[np.eye(5), z5], [z5, -np.eye(5)]]).astype(complex)
    x10 = -1j * n10 @ np.diag(np.exp(-1j * math.pi * np.diag(h10) / 4))
    ev_h, vc_h = np.linalg.eigh(((hp10 - hm10) + (hp10 - hm10).conj().T) * 0.5)
    d10 = vc_h @ np.diag(np.exp(-1j * math.pi * ev_h / 4)) @ vc_h.conj().T
    y10 = d10 @ x10

    d0 = np.vstack([e10, g10])
    d1 = np.hstack([-g10, e10])
    assert float(np.max(np.abs(d1 @ d0))) < TOL

    h1_pinv = np.linalg.pinv(d0)
    h2_pinv = np.linalg.pinv(d1)
    p0_harm = np.eye(10, dtype=complex) - h1_pinv @ d0
    p1_harm = np.eye(20, dtype=complex) - (d0 @ h1_pinv + h2_pinv @ d1)
    p2_harm = np.eye(10, dtype=complex) - d1 @ h2_pinv
    assert int(round(float(np.real(np.trace(p0_harm))))) == 2
    assert int(round(float(np.real(np.trace(p1_harm))))) == 4
    assert int(round(float(np.real(np.trace(p2_harm))))) == 2
    assert float(np.max(np.abs(d0 @ p0_harm))) < TOL
    assert float(np.max(np.abs(d1 @ p1_harm))) < TOL
    assert float(np.max(np.abs(p2_harm @ d1))) < TOL

    fi = np.array([[1j, 0.0], [0.0, -1j]], dtype=complex)
    fj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    r1_x = np.kron(fi, x10)
    r1_y = np.kron(fj, y10)
    assert float(np.max(np.abs(x10 @ h1_pinv - h1_pinv @ r1_x))) < TOL
    assert float(np.max(np.abs(y10 @ h1_pinv - h1_pinv @ r1_y))) < TOL
    assert float(np.max(np.abs(r1_x @ h2_pinv - h2_pinv @ x10))) < TOL
    assert float(np.max(np.abs(r1_y @ h2_pinv - h2_pinv @ y10))) < TOL

    # Planted negative control: breaking balanced Higgs norm G_10 -> 2 * G_10 breaks Q_8 equivariance of h_1!
    h1_broken = np.linalg.pinv(np.vstack([e10, 2.0 * g10]))
    assert float(np.max(np.abs(y10 @ h1_broken - h1_broken @ r1_y))) > 1e-9

    # 2. Independent concrete curved-manifold PDE test on Fubini-Study patch Omega = (x^2 + y^2 + 1)^(-2)
    #    and Poincare half-plane Omega = y^(-2) for J = 3 (S^-3 bundle):
    xs, ys = sp.symbols("xs ys", real=True, positive=True)
    zb = xs - sp.I * ys
    phi_bar_concrete = zb**3 - 2 * sp.I * zb + 5
    for om_concrete in ((xs**2 + ys**2 + 1) ** (-2), ys ** (-2)):
        dz_fn = lambda ex: sp.Rational(1, 2) * (sp.diff(ex, xs) - sp.I * sp.diff(ex, ys))
        a_good = (om_concrete ** (-sp.Rational(3, 4))) * phi_bar_concrete
        a_wrong_no_s3 = phi_bar_concrete  # dropping Omega^(-3/4) spin connection factor!
        cov_dz_good = sp.simplify(dz_fn(a_good) + sp.Rational(3, 4) * (dz_fn(om_concrete) / om_concrete) * a_good)
        cov_dz_wrong = sp.simplify(
            dz_fn(a_wrong_no_s3) + sp.Rational(3, 4) * (dz_fn(om_concrete) / om_concrete) * a_wrong_no_s3
        )
        assert cov_dz_good == 0
        assert cov_dz_wrong != 0

    # 3. Independent mpmath quadrature of cusp S^5 pole selection (k=1, 2 converge; k=3 diverges as eps -> 0+):
    with mp.workdps(25):
        for k_pole in (1, 2):
            i_small = float(mp.quad(lambda r: (r ** (4 - 2 * k_pole)) * ((-mp.log(r)) ** 3), [mp.mpf(1) / mp.mpf(64), mp.mpf(1) / mp.mpf(2)]))
            i_zero = float(mp.quad(lambda r: (r ** (4 - 2 * k_pole)) * ((-mp.log(r)) ** 3), [0, mp.mpf(1) / mp.mpf(2)]))
            assert 0.0 < i_small < i_zero < np.inf
        # k = 3 diverges like 1/r at r -> 0+:
        k3_a = float(mp.quad(lambda r: (r ** (-2)) * ((-mp.log(r)) ** 3), [mp.mpf(1) / mp.mpf(16), mp.mpf(1) / mp.mpf(2)]))
        k3_b = float(mp.quad(lambda r: (r ** (-2)) * ((-mp.log(r)) ** 3), [mp.mpf(1) / mp.mpf(64), mp.mpf(1) / mp.mpf(2)]))
        assert k3_b > 2.0 * k3_a

    # 4. Independent elliptic parity Gram orthogonality across ALL 3 even branches b in (2, 3, 4) at tau_alt = 3/13 + 15/11 i:
    with mp.workdps(25):
        tau_alt = mp.mpc(mp.mpf(3) / mp.mpf(13), mp.mpf(15) / mp.mpf(11))
        q_alt = mp.exp(1j * mp.pi * tau_alt)
        im_alt = float(mp.im(tau_alt))
        n_g = 16
        grid_pts = (np.arange(n_g) + 0.5) / n_g - 0.5
        for b_br in (2, 3, 4):
            off_sum = 0.0 + 0.0j
            diag0 = 0.0
            diag1 = 0.0
            c_norm = mp.pi * mp.jtheta(1, 0, q_alt, 1) / mp.jtheta(b_br, 0, q_alt)
            for u_p in grid_pts:
                for v_p in grid_pts:
                    zv = mp.mpc(float(u_p)) + mp.mpc(float(v_p)) * tau_alt
                    th_b = mp.jtheta(b_br, mp.pi * zv, q_alt)
                    dth_b = mp.pi * mp.jtheta(b_br, mp.pi * zv, q_alt, 1)
                    th_1 = mp.jtheta(1, mp.pi * zv, q_alt)
                    dth_1 = mp.pi * mp.jtheta(1, mp.pi * zv, q_alt, 1)
                    sb_val = complex(c_norm * th_b / th_1)
                    dsb_val = complex(c_norm * (dth_b * th_1 - th_b * dth_1) / (th_1**2))
                    th1_abs2 = float(abs(th_1) ** 2) * math.exp(-2.0 * math.pi * float(v_p * v_p) * im_alt)
                    om_v = 1.0 / (th1_abs2 * (math.log(th1_abs2) ** 2 + 1.0))
                    wt = (1.0 / (om_v * math.sqrt(om_v))) * im_alt / float(n_g * n_g)
                    off_sum += wt * np.conj(sb_val) * dsb_val
                    diag0 += wt * (abs(sb_val) ** 2)
                    diag1 += wt * (abs(dsb_val) ** 2)
            assert abs(off_sum) < TOL
            assert diag0 > 0.0 and diag1 > 0.0

    wp31 = stage2_results["wp31_kernel_and_homotopy"]
    assert wp31["e8_cross_bracket_10_6_x_128_sym_exact"] is True
    assert wp31["max_e8_cross_bracket_err"] < TOL
    assert wp31["untwisted_spin_h0_by_eta"] == {(0, 0): 1, (1, 0): 0, (0, 1): 0, (1, 1): 0}
    assert wp31["census_248_by_bg_and_spin"]["h4"][(0, 0)]["ker_M"] == 68
    assert wp31["census_248_by_bg_and_spin"]["h4"][(0, 0)]["ker_M_dag"] == 68
    assert wp31["census_248_by_bg_and_spin"]["h4"][(0, 0)]["index"] == 0
    assert wp31["h4_even_spin_orbit_ker"] == [60, 60, 68]
    assert wp31["branch_pullback_eta00"] == [68, 68, 68]
    assert wp31["branch_pullback_eta11"] == [60, 68, 60]
    assert wp31["census_248_by_bg_and_spin"]["h1"][(0, 0)]["ker_M"] == 70
    assert wp31["census_248_by_bg_and_spin"]["h1"][(0, 0)]["ker_M_dag"] == 70
    assert wp31["census_248_by_bg_and_spin"]["h1"][(0, 0)]["index"] == 0
    assert wp31["h1_even_spin_orbit_ker"] == [62, 62, 70]
    assert wp31["comm_q8_spin_doublet_dim"] == 1
    assert wp31["comm_10_6_deg1_unsplit_dim"] == 4
    assert wp31["comm_10_6_deg1_mu_neg2_q8_dim"] == 1
    assert wp31["comm_10_6_aslot_etheta_dim"] == 1
    assert wp31["comm_10_6_aslot_bare_swap_dim"] == 2

    # 5. Independent Pauli-Clifford Spin(16) (10,6) x 128 -> 128 Lie bracket equivariance check on BOTH h_4 and h_1
    #    + planted negative control showing double-counting odd_grade on V_10 breaks e_8 bracket equivariance:
    sx_p = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy_p = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
    sz_p = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    i2_p = np.eye(2, dtype=complex)

    def kron_list(ops: list[np.ndarray]) -> np.ndarray:
        cur_m = ops[0]
        for op_m in ops[1:]:
            cur_m = np.kron(cur_m, op_m)
        return cur_m

    g10_maj = []
    for k_i in range(5):
        g10_maj.append(kron_list([sz_p] * k_i + [sx_p] + [i2_p] * (4 - k_i)))
        g10_maj.append(kron_list([sz_p] * k_i + [sy_p] + [i2_p] * (4 - k_i)))
    chir10_p = kron_list([sz_p] * 5)
    g6_maj = []
    for k_i in range(3):
        g6_maj.append(kron_list([sz_p] * k_i + [sx_p] + [i2_p] * (2 - k_i)))
        g6_maj.append(kron_list([sz_p] * k_i + [sy_p] + [i2_p] * (2 - k_i)))
    chir6_p = -1.0j * kron_list([sz_p] * 3)  # omega_6 with omega_6^2 = -I_8; chir10_p = i * omega_10 => omega_10 * omega_6 = (-i chir10_p) * chir6_p
    om16_diag = np.real(np.diag((-1.0j * chir10_p))[:, None] * np.diag(chir6_p)[None, :]).reshape(-1)
    idx_128_p = np.where(om16_diag > 0.5)[0]
    assert idx_128_p.shape[0] == 128

    # Construct an odd-chirality reflection product on Spin(10) x chir10_p (matching h_1's s32 = u32 * chir10) and s8 = g6_maj[0]:
    u32_odd_p = g10_maj[0] @ g10_maj[2] @ g10_maj[4] @ g10_maj[6] @ g10_maj[8]
    s32_p = u32_odd_p @ chir10_p
    s8_p = g6_maj[0]
    h4_8_p = (
        (( np.eye(8) - g6_maj[0] @ g6_maj[1]) / math.sqrt(2))
        @ ((np.eye(8) - g6_maj[2] @ g6_maj[3]) / math.sqrt(2))
        @ ((np.eye(8) - g6_maj[4] @ g6_maj[5]) / math.sqrt(2))
    )
    a32_p = ((np.eye(32) + g10_maj[0] @ g10_maj[1]) / math.sqrt(2)) @ ((np.eye(32) - g10_maj[2] @ g10_maj[3]) / math.sqrt(2))

    # 60 generators of (10,6) on S_16^+: B_{m,p} = (1/2) (g10_maj[m] @ chir10_p) (x) g6_maj[p] restricted to idx_128_p:
    b60_p = np.zeros((60, 128, 128), dtype=complex)
    for m_i in range(10):
        for p_i in range(6):
            full256 = 0.5 * np.kron(g10_maj[m_i] @ chir10_p, g6_maj[p_i])
            b60_p[6 * m_i + p_i] = full256[np.ix_(idx_128_p, idx_128_p)]

    rng_br = np.random.default_rng(29)
    for m32_t, m8_t, is_h1 in [(a32_p, h4_8_p, False), (a32_p @ s32_p, s8_p, True)]:
        u256_t = np.kron(m32_t, m8_t)
        u128_t = u256_t[np.ix_(idx_128_p, idx_128_p)]
        sgn_32 = float(np.real((chir10_p @ m32_t @ chir10_p @ m32_t.conj().T)[0, 0]))
        v10_t = np.array(
            [[np.trace(g10_maj[r_i] @ (m32_t @ g10_maj[c_i] @ m32_t.conj().T)) / 32 for c_i in range(10)] for r_i in range(10)],
            dtype=complex,
        )
        v6_t = np.array(
            [[sgn_32 * np.trace(g6_maj[r_i] @ (m8_t @ g6_maj[c_i] @ m8_t.conj().T)) / 8 for c_i in range(6)] for r_i in range(6)],
            dtype=complex,
        )
        ad60_t = np.kron(v10_t, v6_t)
        c_vec = rng_br.normal(size=60) + 1j * rng_br.normal(size=60)
        c_vec /= np.linalg.norm(c_vec)
        psi_v = rng_br.normal(size=128) + 1j * rng_br.normal(size=128)
        psi_v /= np.linalg.norm(psi_v)
        m_act = np.tensordot(c_vec, b60_p, axes=([0], [0]))
        m_ad_act = np.tensordot(ad60_t @ c_vec, b60_p, axes=([0], [0]))
        assert float(np.max(np.abs(u128_t @ (m_act @ psi_v) - m_ad_act @ (u128_t @ psi_v)))) < TOL
        if is_h1:
            # Planted negative control: multiplying V_10 by an extra -1 breaks (10,6) x 128 -> 128 equivariance!
            ad60_wrong = np.kron(-v10_t, v6_t)
            m_wrong_act = np.tensordot(ad60_wrong @ c_vec, b60_p, axes=([0], [0]))
            assert float(np.max(np.abs(u128_t @ (m_act @ psi_v) - m_wrong_act @ (u128_t @ psi_v)))) > (1 / 10)


def test_wp32_zero_trust_cyclotomic_s4_nogo_and_g192_exchange(stage2_results: dict[str, Any]) -> None:
    # Independent 8x8 integer/rational companion-matrix representation of Q(zeta_24) = Q[x]/(x^8 - x^4 + 1)
    # (zero use of SymPy Poly or producer cyc24_* functions!):
    comp_z = np.zeros((8, 8), dtype=int)
    for k in range(7):
        comp_z[k + 1, k] = 1
    comp_z[0, 7] = -1
    comp_z[4, 7] = 1

    z_pows = [np.eye(8, dtype=int)]
    for _ in range(23):
        z_pows.append(z_pows[-1] @ comp_z)
    assert np.array_equal(z_pows[12], -np.eye(8, dtype=int))
    assert np.array_equal(z_pows[8] - z_pows[4] + z_pows[0], np.zeros((8, 8), dtype=int))

    # Every element M of Sym^2(Weil_2), T, T_bar, and G_192 satisfies 2*M in M_{8n}(Z) (exact integer matrices!).
    i8 = z_pows[6]
    rt2_8 = z_pows[3] - z_pows[9]  # rt2_8^2 == 2 * I_8!
    assert np.array_equal(rt2_8 @ rt2_8, 2 * z_pows[0])

    def blk_mat(blocks_2d: list[list[np.ndarray]]) -> np.ndarray:
        return np.block(blocks_2d)

    def mul_scaled2(a_2m: np.ndarray, b_2m: np.ndarray) -> np.ndarray:
        """Given (2*A) and (2*B) in M_{8n}(Z), return (2 * A * B) = ((2*A) @ (2*B)) // 2 with exact divisibility assertion!"""
        prod4 = a_2m @ b_2m
        assert np.all(prod4 % 2 == 0), "Denominator exceeded 2!"
        return prod4 // 2

    def close_exact_int_group(gens_2m: list[np.ndarray], dim_n: int) -> list[np.ndarray]:
        id_2m = 2 * np.eye(8 * dim_n, dtype=int)
        seen_keys = {id_2m.tobytes(): id_2m}
        queue = [id_2m]
        for _ in range(24):
            if not queue:
                break
            nxt_q = []
            for cur in queue:
                for g_m in gens_2m:
                    p_m = mul_scaled2(cur, g_m)
                    kb = p_m.tobytes()
                    if kb not in seen_keys:
                        seen_keys[kb] = p_m
                        nxt_q.append(p_m)
            queue = nxt_q
        assert not queue
        return list(seen_keys.values())

    z8 = np.zeros((8, 8), dtype=int)
    # 2 * L_sym2 and 2 * S0_sym2 in M_{24}(Z):
    two_l_sym2 = blk_mat(
        [
            [2 * z_pows[0], z8, z8],
            [z8, 2 * i8, z8],
            [z8, z8, -2 * z_pows[0]],
        ]
    )
    two_l_inv_sym2 = blk_mat(
        [
            [2 * z_pows[0], z8, z8],
            [z8, -2 * i8, z8],
            [z8, z8, -2 * z_pows[0]],
        ]
    )
    two_s0_sym2 = blk_mat(
        [
            [z_pows[0], rt2_8, z_pows[0]],
            [rt2_8, z8, -rt2_8],
            [z_pows[0], -rt2_8, z_pows[0]],
        ]
    )
    assert np.array_equal(mul_scaled2(two_s0_sym2, two_s0_sym2), 2 * np.eye(24, dtype=int))
    two_r_sym2 = mul_scaled2(two_s0_sym2, mul_scaled2(two_l_inv_sym2, two_s0_sym2))

    def scalar_24(k_mod: int) -> np.ndarray:
        return np.kron(np.eye(3, dtype=int), 2 * z_pows[k_mod % 24])

    even_ord_set: set[int] = set()
    odd_96_list: list[int] = []
    for m_k in range(24):
        lm = mul_scaled2(scalar_24(m_k), two_l_sym2)
        rm = mul_scaled2(scalar_24(-m_k), two_r_sym2)
        grp_m = close_exact_int_group([lm, rm], 3)
        if m_k % 2 == 0:
            even_ord_set.add(len(grp_m))
        elif len(grp_m) == 96:
            odd_96_list.append(m_k)
    assert even_ord_set == {24, 48, 72, 144}
    assert odd_96_list == [3, 9, 15, 21]

    # Exact B1879 G_96 -> G_192 doubling under exchange P on T (+) T_bar (48x48 exact integer matrices!):
    two_tl = mul_scaled2(scalar_24(15), two_l_sym2)
    two_tr = mul_scaled2(scalar_24(-15), two_r_sym2)
    two_tbar_l = mul_scaled2(scalar_24(-15), two_l_inv_sym2)
    two_r_bar_sym2 = mul_scaled2(two_s0_sym2, mul_scaled2(two_l_sym2, two_s0_sym2))
    two_tbar_r = mul_scaled2(scalar_24(15), two_r_bar_sym2)

    z24_blk = np.zeros((24, 24), dtype=int)
    two_l6 = np.block([[two_tl, z24_blk], [z24_blk, two_tbar_l]])
    two_r6 = np.block([[two_tr, z24_blk], [z24_blk, two_tbar_r]])
    two_p6 = np.block([[z24_blk, two_s0_sym2], [two_s0_sym2, z24_blk]])

    assert len(close_exact_int_group([two_l6, two_r6], 6)) == 96
    assert len(close_exact_int_group([two_l6, two_r6, two_p6], 6)) == 192

    # Independent Haar U(2) universal central-S^4 symmetric-square No-Go test:
    rng = np.random.default_rng(107)
    inv_rt2 = 1.0 / math.sqrt(2.0)
    for e1 in (-1.0, 1.0):
        for e2 in (-1.0, 1.0):
            for _ in range(4):
                u2 = haar_unitary(2, rng)
                m_s4 = u2 @ np.diag([e1, e2]) @ u2.conj().T
                a, b = m_s4[0, 0], m_s4[0, 1]
                c, d = m_s4[1, 0], m_s4[1, 1]
                sym2_m = np.array(
                    [
                        [a * a, math.sqrt(2) * a * b, b * b],
                        [math.sqrt(2) * a * c, a * d + b * c, math.sqrt(2) * b * d],
                        [c * c, math.sqrt(2) * c * d, inv_rt2 * math.sqrt(2) * d * d],
                    ],
                    dtype=complex,
                )
                assert float(np.linalg.norm(sym2_m - (-np.eye(3, dtype=complex)), ord=2)) + TOL >= 2.0

    wp32 = stage2_results["wp32_cyclotomic_algebra"]
    assert wp32["b1879_exchange_doubles_96_to_192_exact"] is True


def test_b1866_zero_trust_jacobi_theta_qseries_and_3branch_pde_join(stage2_results: dict[str, Any]) -> None:
    # Independent direct q-series theta_1..theta_4 and Dedekind eta (zero use of mp.jtheta!) at a 3rd test point:
    with mp.workdps(40):
        def qseries_theta1(z_v: mp.mpc, tau_v: mp.mpc) -> mp.mpc:
            q_v = mp.exp(1j * mp.pi * tau_v)
            tot = mp.mpc(0)
            for n_k in range(28):
                sgn = -1 if (n_k % 2 == 1) else 1
                tot += sgn * (q_v ** ((n_k + mp.mpf(1) / mp.mpf(2)) ** 2)) * mp.sin((2 * n_k + 1) * mp.pi * z_v)
            return 2 * tot

        def qseries_dtheta1_zero(tau_v: mp.mpc) -> mp.mpc:
            q_v = mp.exp(1j * mp.pi * tau_v)
            tot = mp.mpc(0)
            for n_k in range(28):
                sgn = -1 if (n_k % 2 == 1) else 1
                tot += sgn * (2 * n_k + 1) * (q_v ** ((n_k + mp.mpf(1) / mp.mpf(2)) ** 2))
            return 2 * mp.pi * tot

        def qseries_theta_even(b_br: int, z_v: mp.mpc, tau_v: mp.mpc) -> mp.mpc:
            q_v = mp.exp(1j * mp.pi * tau_v)
            if b_br == 2:
                tot = mp.mpc(0)
                for n_k in range(28):
                    tot += (q_v ** ((n_k + mp.mpf(1) / mp.mpf(2)) ** 2)) * mp.cos((2 * n_k + 1) * mp.pi * z_v)
                return 2 * tot
            tot = mp.mpc(1)
            for n_k in range(1, 28):
                sgn = (-1 if (n_k % 2 == 1) else 1) if b_br == 4 else 1
                tot += 2 * sgn * (q_v ** (n_k * n_k)) * mp.cos(2 * n_k * mp.pi * z_v)
            return tot

        def qseries_eta(tau_v: mp.mpc) -> mp.mpc:
            q2 = mp.exp(2j * mp.pi * tau_v)
            prod = mp.mpf(1)
            for n_k in range(1, 70):
                prod *= 1 - q2**n_k
            return mp.exp(1j * mp.pi * tau_v / 12) * prod

        def indep_szego(b_br: int, z_v: mp.mpc, tau_v: mp.mpc) -> mp.mpc:
            return (qseries_dtheta1_zero(tau_v) * qseries_theta_even(b_br, z_v, tau_v)) / (
                qseries_theta_even(b_br, mp.mpc(0), tau_v) * qseries_theta1(z_v, tau_v)
            )

        # Verify Jacobi's derivative identity dtheta1(0|tau)/dz == 2*pi * eta(tau)^3 from raw q-series!
        tau3 = mp.mpc(mp.mpf(2) / mp.mpf(11), mp.mpf(16) / mp.mpf(13))
        z3 = mp.mpc(mp.mpf(3) / mp.mpf(19), -mp.mpf(4) / mp.mpf(15))
        assert float(abs(qseries_dtheta1_zero(tau3) - 2 * mp.pi * (qseries_eta(tau3) ** 3))) < TOL

        # Verify pure elliptic half-form transformation of eta(tau)^3 * S_b(z|tau) * (dz)^{5/2} under L and R
        # BEFORE multiplying by E8 fiber compensator phases, and check its exact permutation + eighth-root phases:
        branch_ord = [2, 3, 4]
        ell_mats: dict[str, np.ndarray] = {}
        for gk in ("L", "R"):
            if gk == "L":
                z_old, tau_old, eps = z3, tau3 - 1, mp.mpc(1)
            else:
                tau_old = tau3 / (1 - tau3)
                eps = mp.sqrt(tau_old + 1)
                z_old = (eps**2) * z3
            m_ell = np.zeros((3, 3), dtype=complex)
            for col_i, b_src in enumerate(branch_ord):
                pushed = (qseries_eta(tau_old) ** 3) * indep_szego(b_src, z_old, tau_old) * (eps**5)
                for row_i, b_dst in enumerate(branch_ord):
                    dst_v = (qseries_eta(tau3) ** 3) * indep_szego(b_dst, z3, tau3)
                    ratio = complex(pushed / dst_v)
                    if abs(abs(ratio) - 1.0) < 1e-9:
                        m_ell[row_i, col_i] = ratio
            assert float(np.max(np.abs(m_ell @ m_ell.conj().T - np.eye(3, dtype=complex)))) < TOL
            ell_mats[gk] = m_ell

        # Check braid relation and S^4 == -I_3 on the pure half-form Szego triplet (eta^3 * S_b * dz^{5/2}):
        s_ell = ell_mats["L"] @ np.linalg.inv(ell_mats["R"]) @ ell_mats["L"]
        s_ell_rhs = np.linalg.inv(ell_mats["R"]) @ ell_mats["L"] @ np.linalg.inv(ell_mats["R"])
        assert float(np.max(np.abs(s_ell - s_ell_rhs))) < TOL
        assert float(np.max(np.abs(np.linalg.matrix_power(s_ell, 4) + np.eye(3, dtype=complex)))) < TOL

    b1866 = stage2_results["b1866_zero_handtyped_3branch_join"]
    th_p = b1866["thread_h4_plus"]
    assert th_p["proxy_1form_b3_stabilizer_L2_S"] == (-1, -1)
    assert th_p["mode_center_and_pg_orders"]["proxy_1form_no_S3"] == (1, 24)
    assert th_p["mode_center_and_pg_orders"]["phi_sp_conj_weyl"] == (4, 24)
    assert th_p["mode_center_and_pg_orders"]["a_sp_left_weyl"] == (4, 24)
    assert th_p["mode_center_and_pg_orders"]["a_dp_left_weyl"] == (12, 24)
    assert th_p["mode_center_and_pg_orders"]["psi_spin_left_weyl"] == (12, 6)
    assert th_p["mode_s4_signs"] == {
        "proxy_1form_no_S3": 1,
        "phi_sp_conj_weyl": -1,
        "a_sp_left_weyl": -1,
        "a_dp_left_weyl": -1,
        "psi_spin_left_weyl": -1,
    }
    assert th_p["pairwise_hom_dims"] == {
        "a_sp_vs_a_dp": 0,
        "a_sp_vs_psi_spin": 0,
        "a_dp_vs_psi_spin": 0,
    }
    assert th_p["end_9d_commutant_dim"] == 4
    assert th_p["reducible_neg_ctrl_hom_dim"] == 2
    assert th_p["hom_weave_to_a_sp"] == 0
    assert th_p["hom_weave_conj_to_a_sp"] == 1
    assert th_p["hom_weave_to_phi_sp"] == 1
    assert th_p["exact_cyc24_intertwiners_verified"] is True
    assert b1866["eta3_supplies_odd_metaplectic_char_exact"] is True
    assert b1866["b1866_physical_join_resolved_and_verified"] is True

    # Independent mechanical SL(2, Z) / Gamma_theta coset transport + Haar U(3) scrambling check (F1 + F3 + Guardrail 6):
    # (a) Pure elliptic half-form triplet WITHOUT E8 gauge compensator X has projective image S_3 => reducible 1 (+) 2 (commutant dim 2).
    # (b) Mechanically close Gamma_theta mod 4 generated by (L^2 -> -1, S -> -1, -I_2 -> +1) and transport cosets (R, I_2, L)
    #     under L and R: the induced sign character lifts S_3 -> S_4 and yields comp ~ T, conj(comp) ~ T_bar (not T)!
    sl_l = np.array([[1, 1], [0, 1]], dtype=int)
    sl_r = np.array([[1, 0], [1, 1]], dtype=int)
    sl_linv = np.array([[1, -1], [0, 1]], dtype=int)
    sl_rinv = np.array([[1, 0], [-1, 1]], dtype=int)
    sl_l2 = sl_l @ sl_l
    sl_s = sl_l @ sl_rinv @ sl_l

    def key_mod4(mat_i: np.ndarray) -> tuple[int, ...]:
        return tuple(int(v_x % 4) for v_x in mat_i.ravel())

    chi_gt4: dict[tuple[int, ...], int] = {key_mod4(np.eye(2, dtype=int)): 1}
    q_gt = [np.eye(2, dtype=int)]
    gens_gt = [(sl_l2, -1), (sl_linv @ sl_linv, -1), (sl_s, -1), (-sl_s, -1), (-np.eye(2, dtype=int), 1)]
    while q_gt:
        cur_g = q_gt.pop(0)
        cur_s = chi_gt4[key_mod4(cur_g)]
        for gm_s, sg_v in gens_gt:
            nxt_g = cur_g @ gm_s
            km = key_mod4(nxt_g)
            if km in chi_gt4:
                assert chi_gt4[km] == cur_s * sg_v
            else:
                chi_gt4[km] = cur_s * sg_v
                q_gt.append(nxt_g)
    assert len(chi_gt4) == 16

    cosets_3 = [sl_r, np.eye(2, dtype=int), sl_l]
    cosets_3_inv = [sl_rinv, np.eye(2, dtype=int), sl_linv]
    ind_sign_mats: dict[str, np.ndarray] = {}
    for gk_c, gm_c in (("L", sl_l), ("R", sl_r)):
        m_ind = np.zeros((3, 3), dtype=complex)
        for col_j in range(3):
            hit_c = 0
            for row_i in range(3):
                gam_ij = cosets_3_inv[row_i] @ gm_c @ cosets_3[col_j]
                km_ij = key_mod4(gam_ij)
                if km_ij in chi_gt4:
                    m_ind[row_i, col_j] = float(chi_gt4[km_ij])
                    hit_c += 1
            assert hit_c == 1
        ind_sign_mats[gk_c] = m_ind

    comp_l = np.where(np.abs(ind_sign_mats["L"]) > 0.5, ind_sign_mats["L"] * ell_mats["L"], 0.0j)
    comp_r = np.where(np.abs(ind_sign_mats["R"]) > 0.5, ind_sign_mats["R"] * ell_mats["R"], 0.0j)
    # Verify exact braid relation on mechanically compensated half-form representation:
    s_comp_lhs = comp_l @ np.linalg.inv(comp_r) @ comp_l
    s_comp_rhs = np.linalg.inv(comp_r) @ comp_l @ np.linalg.inv(comp_r)
    assert float(np.max(np.abs(s_comp_lhs - s_comp_rhs))) < TOL

    # Necessary-and-sufficient Sylvester Hom & unitary intertwiner countercheck against independent T and T_bar (F3):
    rt2_inv = 1.0 / np.sqrt(2.0)
    l_w2 = np.diag([1.0, 1.0j])
    s0_w2 = np.array([[rt2_inv, rt2_inv], [rt2_inv, -rt2_inv]], dtype=complex)
    r_w2 = s0_w2 @ np.linalg.inv(l_w2) @ s0_w2

    def sym2_u2(u2: np.ndarray) -> np.ndarray:
        a_u, b_u, c_u, d_u = u2[0, 0], u2[0, 1], u2[1, 0], u2[1, 1]
        s2 = np.sqrt(2.0)
        return np.array(
            [
                [a_u * a_u, s2 * a_u * b_u, b_u * b_u],
                [s2 * a_u * c_u, a_u * d_u + b_u * c_u, s2 * b_u * d_u],
                [c_u * c_u, s2 * c_u * d_u, d_u * d_u],
            ],
            dtype=complex,
        )

    z15_ph = np.exp(2.0j * np.pi * 15 / 24)
    t_l_ind = z15_ph * sym2_u2(l_w2)
    t_r_ind = np.conj(z15_ph) * sym2_u2(r_w2)
    tbar_l_ind = np.conj(t_l_ind)
    tbar_r_ind = np.conj(t_r_ind)

    def indep_hom_and_err(pa: tuple[np.ndarray, np.ndarray], pb: tuple[np.ndarray, np.ndarray]) -> tuple[int, float]:
        i3_n = np.eye(3, dtype=complex)
        sys_h = np.vstack(
            [
                np.kron(pa[0].T, i3_n) - np.kron(i3_n, pb[0]),
                np.kron(pa[1].T, i3_n) - np.kron(i3_n, pb[1]),
            ]
        )
        _, sv_h, vh_h = np.linalg.svd(sys_h)
        h_dim = int(np.sum(sv_h < 1e-9))
        if h_dim != 1:
            return h_dim, 1.0
        u_cand = vh_h[-1].conj().reshape((3, 3), order="F")
        uu, _, vhu = np.linalg.svd(u_cand)
        u_iso = uu @ vhu
        res = max(
            float(np.max(np.abs(u_iso @ pa[0] @ u_iso.conj().T - pb[0]))),
            float(np.max(np.abs(u_iso @ pa[1] @ u_iso.conj().T - pb[1]))),
        )
        return h_dim, res

    hd_comp_t, err_comp_t = indep_hom_and_err((comp_l, comp_r), (t_l_ind, t_r_ind))
    hd_comp_tb, _ = indep_hom_and_err((comp_l, comp_r), (tbar_l_ind, tbar_r_ind))
    hd_conj_tb, err_conj_tb = indep_hom_and_err((comp_l.conj(), comp_r.conj()), (tbar_l_ind, tbar_r_ind))
    hd_conj_t, _ = indep_hom_and_err((comp_l.conj(), comp_r.conj()), (t_l_ind, t_r_ind))
    assert hd_comp_t == 1 and err_comp_t < TOL
    assert hd_comp_tb == 0
    assert hd_conj_tb == 1 and err_conj_tb < TOL
    assert hd_conj_t == 0

    rng = np.random.default_rng(149)
    for _ in range(6):
        u3 = haar_unitary(3, rng)
        assert joint_commutant_dim_num([u3 @ ell_mats["L"] @ u3.conj().T, u3 @ ell_mats["R"] @ u3.conj().T], tol=1e-10) == 2
        assert joint_commutant_dim_num([u3 @ comp_l @ u3.conj().T, u3 @ comp_r @ u3.conj().T], tol=1e-10) == 1
