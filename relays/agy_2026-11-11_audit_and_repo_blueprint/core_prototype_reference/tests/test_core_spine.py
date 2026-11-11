"""Zero-Trust Verification Suite for `origin-axiom-core` (`THM-CORE-01` .. `THM-CORE-06`).

Every test pairs the package's `@producer` routines against an independent `@referee`
countercheck enforced by `guardrail_dsl` (`< 1e-12` precision, zero literal flags,
Haar unitary basis-scrambling invariance, and strict producer-referee isolation).
"""

from __future__ import annotations

from fractions import Fraction as Fr
import math
from typing import Any, Dict, List, Tuple

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss
import pytest

from origin_axiom_core import (
    FramedMatrix,
    GatedRGEIntegrator,
    Guardrail1PostInspectionError,
    Guardrail1UnpricedScanError,
    Guardrail2LiteralClaimError,
    Guardrail3BasisDependenceError,
    Guardrail3IllegalLeftRightOverlapError,
    Guardrail4BenchmarkGateError,
    Guardrail5UnpricedScaleError,
    Guardrail6ProducerEchoError,
    LedgerContext,
    TrackedValue,
    adjoint_settling_spectrum,
    analytic_jtheta,
    mayer_selberg_subweave_spectrum,
    nonorientable_pin_pullback_census,
    observable,
    projective_modular_tick_orders,
    ray_singer_x1_sheet_potential_mp,
    referee,
    schreier_closure_pm_gamma1_5,
    stabilization_potential,
    stern_brocot_axis_correlation,
    theorem,
    theta_triplet_weight_minus_half,
    twin_odd_maass_golden_and_kramers,
    two_tick_bijection_census,
    weave_6d_commutant_fusion,
    zero_bit_prediction,
)


# ---------------------------------------------------------------------------
# THM-CORE-01: Guardrail 1-6 Static & Dynamic Enforcement
# ---------------------------------------------------------------------------


def test_guardrail_dsl_blocks_all_adversarial_cheats_and_passes_honest() -> None:
    # Guardrail 1a: Embedded target shift in potential rejected at compile time
    with pytest.raises(Guardrail1PostInspectionError):
        @stabilization_potential()
        def _bad_pot(x: float) -> float:
            return (x - 1.6180339887) ** 2

    # Honest target-free potential: f(x) = x^4 - 4*x^2 has genuine minima at x = +-sqrt(2)
    @stabilization_potential(grad_tol=1e-7, eps=1e-5)
    def _honest_pot(x: float) -> float:
        return x ** 4 - 4.0 * (x ** 2)

    cert = _honest_pot.verify_minimum(math.sqrt(2.0))
    assert cert["grad_norm"] < 1e-8
    assert abs(cert["min_hessian_eigval"] - 16.0) < 1e-4

    # Guardrail 1b: Hidden discrete scan inside @zero_bit_prediction rejected
    ledger = LedgerContext("g1_scan")

    @zero_bit_prediction
    def _sneaky_scan() -> TrackedValue:
        _ = ledger.select_from([1.0, 2.0, 3.0, 4.0], lambda z: abs(z - 2.9))
        return TrackedValue(3.0)

    with pytest.raises(Guardrail1UnpricedScanError):
        _sneaky_scan()

    # Guardrail 2: Literal boolean or zero return rejected at AST compile time
    with pytest.raises(Guardrail2LiteralClaimError):
        @theorem()
        def _fake_thm() -> Dict[str, Any]:
            return {"bar_theta_qcd": 0.0}

    @theorem(tol=1e-12)
    def _honest_thm(theta_angle: float) -> Dict[str, float]:
        rot = np.array(
            [[math.cos(theta_angle), -math.sin(theta_angle)], [math.sin(theta_angle), math.cos(theta_angle)]],
            dtype=np.float64,
        )
        residual = float(np.linalg.norm(rot.T @ rot - np.eye(2), ord="fro"))
        return {"orthogonality_residual": residual}

    res_thm = _honest_thm(0.73)
    assert res_thm["orthogonality_residual"] < 1e-14

    # Guardrail 3a: Dirac left-right SVD overlap rejected at AST compile time
    with pytest.raises(Guardrail3IllegalLeftRightOverlapError):
        @observable()
        def _bad_lr(ym: FramedMatrix) -> float:
            u, _, vh = np.linalg.svd(ym.matrix)
            return float(np.abs((u.conj().T @ vh.conj().T)[0, 1]))

    # Guardrail 3b: Basis-dependent raw matrix entry rejected dynamically under Haar scrambling
    @observable(haar_samples=8)
    def _bad_entry(ym: FramedMatrix) -> float:
        return float(np.abs(ym.matrix[0, 0]))

    rng = np.random.default_rng(42)
    yu_m = FramedMatrix(rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3)), "Q_L", "u_R")
    yd_m = FramedMatrix(rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3)), "Q_L", "d_R")
    with pytest.raises(Guardrail3BasisDependenceError):
        _bad_entry(yu_m)

    # Honest physical CKM Jarlskog + singular-value ratio observable passes 16 Haar draws (< 1e-12)
    @observable(haar_samples=16, tol=1e-12)
    def _honest_ckm(yu: FramedMatrix, yd: FramedMatrix) -> np.ndarray:
        uu, su, _ = np.linalg.svd(yu.matrix)
        ud, sd, _ = np.linalg.svd(yd.matrix)
        v = uu[:, ::-1].conj().T @ ud[:, ::-1]
        j = np.imag(v[0, 1] * v[1, 2] * np.conj(v[0, 2]) * np.conj(v[1, 1]))
        return np.array([su[1] / su[0], sd[1] / sd[0], abs(v[0, 1]), j], dtype=np.float64)

    obs_val = _honest_ckm(yu_m, yd_m)
    assert obs_val.shape == (4,)

    # Guardrail 4: Unbenchmarked RGE integration blocked; benchmarked 1-loop QCD passes
    b0 = 7.0 / (2.0 * math.pi)
    rge = GatedRGEIntegrator(lambda _t, a: np.array([-b0 * (a[0] ** 2)]), log_variable="ln_mu")
    with pytest.raises(Guardrail4BenchmarkGateError):
        rge.integrate_model(np.array([0.118]), 91.1876, 1000.0)

    a0 = 0.118
    t_span = math.log(1000.0 / 91.1876)
    exact_a1 = a0 / (1.0 + b0 * a0 * t_span)
    receipt = rge.verify_literature_benchmark(
        np.array([a0]),
        91.1876,
        1000.0,
        np.array([exact_a1]),
        rtol=1e-3,
        citation="1-loop QCD asymptotic freedom",
    )
    assert receipt["relative_error"] < 1e-10
    y_final = rge.integrate_model(np.array([a0]), 91.1876, 1000.0)
    assert abs(float(y_final[0]) - exact_a1) < 1e-10

    # Guardrail 5: Second dimensionful anchor rejected; single anchor dimensionless ratio passes
    led5 = LedgerContext("g5")
    v_ew = led5.declare_anchor("v_EW", 246.21965, "GeV")
    with pytest.raises(Guardrail5UnpricedScaleError):
        led5.declare_anchor("M_Z", 91.1876, "GeV")
    with pytest.raises(Guardrail5UnpricedScaleError):
        led5.finalize_prediction(v_ew * 0.5)
    summary = led5.finalize_prediction((v_ew * 0.5) / v_ew)
    assert abs(summary["dimensionless_value"] - 0.5) < 1e-15

    # Guardrail 6: Referee referencing a @producer symbol rejected at AST compile time
    with pytest.raises(Guardrail6ProducerEchoError):
        @referee
        def _cheating_ref() -> Any:
            return analytic_jtheta(3, 0.0, 1j)


# ---------------------------------------------------------------------------
# THM-CORE-02: Holomorphic Quarter-Nome Jacobi Theta (P-670)
# ---------------------------------------------------------------------------


@referee
def _referee_jacobi_product_theta(n_idx: int, z_c: complex, tau_c: complex) -> complex:
    """Independent Jacobi triple-product evaluation (never uses series of producer)."""
    old_dps = mp.mp.dps
    mp.mp.dps = 40
    try:
        t = mp.mpc(tau_c.real, tau_c.imag)
        z = mp.mpc(z_c.real, z_c.imag)
        q4 = mp.exp(1j * mp.pi * t / 4)
        q = q4 ** 4
        q2 = q * q
        w2 = mp.exp(2j * z)
        wm2 = mp.exp(-2j * z)
        prod = mp.mpc(1, 0)
        qm2 = q2
        q_odd = q
        for _ in range(45):
            if n_idx == 1:
                prod *= (1 - qm2) * (1 - qm2 * w2) * (1 - qm2 * wm2)
            elif n_idx == 2:
                prod *= (1 - qm2) * (1 + qm2 * w2) * (1 + qm2 * wm2)
            elif n_idx == 3:
                prod *= (1 - qm2) * (1 + q_odd * w2) * (1 + q_odd * wm2)
            else:
                prod *= (1 - qm2) * (1 - q_odd * w2) * (1 - q_odd * wm2)
            qm2 *= q2
            q_odd *= q2
        if n_idx == 1:
            return complex(2 * q4 * mp.sin(z) * prod)
        if n_idx == 2:
            return complex(2 * q4 * mp.cos(z) * prod)
        return complex(prod)
    finally:
        mp.mp.dps = old_dps


def test_holomorphic_theta_branch_cut_freedom_and_modular_identities() -> None:
    # Test across Re(tau) = 3.0 (where naive mpmath.jtheta(1, z, exp(i*pi*tau)) jumps by i!)
    z_test = 0.37 - 0.19j
    tau_left = 3.0 - 1e-9 + 0.85j
    tau_right = 3.0 + 1e-9 + 0.85j

    for n_i in (1, 2, 3, 4):
        v_left = complex(analytic_jtheta(n_i, z_test, tau_left))
        v_right = complex(analytic_jtheta(n_i, z_test, tau_right))
        v_ref = _referee_jacobi_product_theta(n_i, z_test, 3.0 + 0.85j)
        assert abs(v_left - v_right) < 1e-7  # smooth O(1e-9) continuity across Re(tau) = 3
        v_exact = complex(analytic_jtheta(n_i, z_test, 3.0 + 0.85j))
        assert abs(v_exact - v_ref) < 1e-14

    # Modular T-identities across tau -> tau + 1 on wide Re(tau) = 2.63 + 0.91j
    tau_wide = 2.63 + 0.91j
    zeta8 = cmath_exp_ipi4 = complex(math.cos(math.pi / 4.0), math.sin(math.pi / 4.0))
    assert abs(complex(analytic_jtheta(1, z_test, tau_wide + 1.0)) - cmath_exp_ipi4 * complex(analytic_jtheta(1, z_test, tau_wide))) < 1e-14
    assert abs(complex(analytic_jtheta(2, z_test, tau_wide + 1.0)) - cmath_exp_ipi4 * complex(analytic_jtheta(2, z_test, tau_wide))) < 1e-14
    assert abs(complex(analytic_jtheta(3, z_test, tau_wide + 1.0)) - complex(analytic_jtheta(4, z_test, tau_wide))) < 1e-14

    # Verify weight-(-1/2) triplet T-action: (th2^2, th3^2, th4^2)/eta^3(tau + 1)
    trip0 = [complex(c) for c in theta_triplet_weight_minus_half(tau_wide)]
    trip1 = [complex(c) for c in theta_triplet_weight_minus_half(tau_wide + 1.0)]
    phase_eta_m3 = complex(math.cos(-math.pi / 4.0), math.sin(-math.pi / 4.0))
    assert abs(trip1[0] - (1j * phase_eta_m3) * trip0[0]) < 1e-13
    assert abs(trip1[1] - phase_eta_m3 * trip0[2]) < 1e-13
    assert abs(trip1[2] - phase_eta_m3 * trip0[1]) < 1e-13


# ---------------------------------------------------------------------------
# THM-CORE-03: Tick Pin+- Obstruction, Modular Orders & G_96 -> G_192 Fusion
# ---------------------------------------------------------------------------


@referee
def _referee_psl2_closed_formula_and_haar_commutant() -> Dict[str, Any]:
    """Independently computes |PSL_2(Z/NZ)| by prime-power Jordan-Holder formula and scrambles G_96/G_192."""
    formula_orders: Dict[int, int] = {}
    for n_val in range(2, 14):
        # |SL_2(Z/NZ)| = N^3 * prod_{p | N} (1 - 1/p^2)
        temp = n_val
        primes: List[int] = []
        d = 2
        while d * d <= temp:
            if temp % d == 0:
                primes.append(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            primes.append(temp)
        sl2_ord = n_val ** 3
        for p in primes:
            sl2_ord = (sl2_ord // (p * p)) * (p * p - 1)
        psl2_ord = sl2_ord if n_val == 2 else sl2_ord // 2
        formula_orders[n_val] = psl2_ord

    # Independent Haar-scrambled Reynolds commutant trace Tr(P_comm) = (1/|G|) sum_{g in G} |Tr(g)|^2
    zeta8 = np.exp(2j * math.pi / 8.0)
    t_mat = np.array(
        [[1j * (zeta8 ** (-3)), 0, 0], [0, 0, zeta8 ** (-3)], [0, zeta8 ** (-3), 0]],
        dtype=complex,
    )
    s_mat = np.array([[0, 0, -1], [0, -1, 0], [-1, 0, 0]], dtype=complex)
    l3 = s_mat @ np.linalg.inv(t_mat) @ np.linalg.inv(s_mat)
    r3 = t_mat
    z3 = np.zeros((3, 3), dtype=complex)
    l6 = np.block([[l3, z3], [z3, np.conj(l3)]])
    r6 = np.block([[r3, z3], [z3, np.conj(r3)]])
    p6 = np.block([[z3, s_mat], [np.conj(s_mat), z3]])

    rng = np.random.default_rng(20261111)
    g_rand = (rng.standard_normal((6, 6)) + 1j * rng.standard_normal((6, 6))) / math.sqrt(2.0)
    u6, r_qr = np.linalg.qr(g_rand)
    diag_r = np.diag(r_qr)
    u6 = u6 * (diag_r / np.abs(diag_r))[None, :]

    def _burnside_commutant_trace(gens: List[np.ndarray]) -> Tuple[int, float]:
        scr_gens = [u6 @ g @ u6.conj().T for g in gens]
        elts = [np.eye(6, dtype=complex)]
        idx = 0
        while idx < len(elts):
            cur = elts[idx]
            idx += 1
            for g in scr_gens:
                nxt = cur @ g
                if not any(float(np.max(np.abs(nxt - e))) < 1e-10 for e in elts):
                    elts.append(nxt)
        tr_sq_sum = float(np.sum([abs(np.trace(e)) ** 2 for e in elts]))
        return len(elts), tr_sq_sum / float(len(elts))

    ord96, comm96 = _burnside_commutant_trace([l6, r6])
    ord192, comm192 = _burnside_commutant_trace([l6, r6, p6])
    return {
        "formula_psl2": formula_orders,
        "ord96": ord96,
        "comm96": comm96,
        "ord192": ord192,
        "comm192": comm192,
    }


def test_tick_pin_modular_orders_and_weave_commutant_fusion() -> None:
    pin_rows = nonorientable_pin_pullback_census(max_len=6)
    assert len(pin_rows) == 10
    assert all(r["det"] == -1 for r in pin_rows)
    m000_rows = [r for r in pin_rows if r["length"] == 1]
    assert len(m000_rows) == 2
    assert all(r["cover_pullback_image_size"] == 1 for r in m000_rows)
    # Over F_2, LP and RP have order 3 (generate A_3 <= SL_2(F_2)), so pullback sizes are in {1, 4}
    assert {r["cover_pullback_image_size"] for r in pin_rows} == {1, 4}

    mod_rows = projective_modular_tick_orders()
    ref_check = _referee_psl2_closed_formula_and_haar_commutant()
    unchanged_levels = [r["N"] for r in mod_rows if r["ratio"] == 1]
    assert unchanged_levels == [2, 5, 10, 13]
    for r in mod_rows:
        assert r["psl2_order"] == ref_check["formula_psl2"][r["N"]]
        assert (r["ratio"] == 1) == r["minus1_is_square_mod_N"]

    fus = weave_6d_commutant_fusion()
    assert fus["order_g96"] == 96 and ref_check["ord96"] == 96
    assert fus["order_g192"] == 192 and ref_check["ord192"] == 192
    assert fus["commutant_dim_g96"] == 2 and abs(ref_check["comm96"] - 2.0) < 1e-13
    assert fus["commutant_dim_g192"] == 1 and abs(ref_check["comm192"] - 1.0) < 1e-13


# ---------------------------------------------------------------------------
# THM-CORE-04: Stern-Brocot Minkowski S-Duality & Adjoint Trace Law
# ---------------------------------------------------------------------------


@referee
def _referee_exact_metallic_and_chiral_polynomial_check(
    tau_lr: complex,
    lam_silver: complex,
    tau_bronze: complex,
    tau_chiral: complex,
) -> Dict[str, float]:
    """Independently solves the exact algebraic polynomials in 40-dps mpmath and measures root error."""
    old_dps = mp.mp.dps
    mp.mp.dps = 40
    try:
        phi = 0.5 * (mp.mpf(1) + mp.sqrt(5))
        err_lr = abs(tau_lr - 5.0)
        err_silver = abs(lam_silver - complex(phi ** 6))
        # Exact largest real root of tau^4 - 114*tau^3 + 4264*tau^2 - 58910*tau + 192359 = 0
        bronze_exact = mp.findroot(
            lambda t: t ** 4 - 114 * (t ** 3) + 4264 * (t ** 2) - 58910 * t + 192359,
            mp.mpf("54.08"),
        )
        err_bronze_root = abs(tau_bronze - complex(bronze_exact))
        err_chiral_quad = min(
            abs(tau_chiral - complex(9.0, math.sqrt(7.0))),
            abs(tau_chiral - complex(9.0, -math.sqrt(7.0))),
        )
        return {
            "err_lr": float(err_lr),
            "err_silver": float(err_silver),
            "err_bronze_root": float(err_bronze_root),
            "err_chiral_quad": float(err_chiral_quad),
        }
    finally:
        mp.mp.dps = old_dps


def test_minkowski_s_duality_and_punctured_torus_adjoint_polynomials() -> None:
    for y_val in (math.sqrt(2.0), math.sqrt(1.5), 0.5 * (1.0 + math.sqrt(5.0)), 2.37):
        c_pos = stern_brocot_axis_correlation(y_val, 0.25, depth=12)
        c_inv = stern_brocot_axis_correlation(1.0 / y_val, 0.25, depth=12)
        assert abs(c_pos - c_inv) < 1e-14

    spec_lr = adjoint_settling_spectrum("LR")
    spec_silver = adjoint_settling_spectrum("LLRR")
    spec_bronze = adjoint_settling_spectrum("LLLRRR")
    spec_chiral = adjoint_settling_spectrum("LLR")

    for sp in (spec_lr, spec_silver, spec_bronze, spec_chiral):
        assert sp["symplectic_det_prod_minus_1_err"] < 1e-12

    errs = _referee_exact_metallic_and_chiral_polynomial_check(
        complex(*spec_lr["tau_adj"]),
        complex(*spec_silver["lambda_1"]),
        complex(*spec_bronze["tau_adj"]),
        complex(*spec_chiral["tau_adj"]),
    )
    assert errs["err_lr"] < 1e-12
    assert errs["err_silver"] < 1e-12
    assert errs["err_bronze_root"] < 1e-12
    assert errs["err_chiral_quad"] < 1e-12


# ---------------------------------------------------------------------------
# THM-CORE-05: Whole-Subweave Schreier, Old-Space Pullback & Ray-Singer Coercivity
# ---------------------------------------------------------------------------


@referee
def _referee_gauss_legendre_oldspace_and_coercivity() -> Dict[str, float]:
    """Independently constructs Gauss-Legendre + Euler-Maclaurin R10-A and verifies P_{10<-5} intertwining."""
    def _lines(n_lv: int) -> List[Tuple[int, int]]:
        s = set()
        for a in range(n_lv):
            for b in range(n_lv):
                if math.gcd(math.gcd(a, b), n_lv) == 1:
                    s.add(min((a, b), ((-a) % n_lv, (-b) % n_lv)))
        return sorted(s)

    def _vand(xs: np.ndarray, k_d: int) -> Tuple[np.ndarray, np.ndarray]:
        u = 2.0 * xs - 1.0
        p = np.zeros((len(xs), k_d), dtype=np.float64)
        dp = np.zeros((len(xs), k_d), dtype=np.float64)
        p[:, 0] = 1.0
        if k_d > 1:
            p[:, 1] = u
            dp[:, 1] = 1.0
        for k in range(2, k_d):
            p[:, k] = ((2 * k - 1) * u * p[:, k - 1] - (k - 1) * p[:, k - 2]) / float(k)
            dp[:, k] = (2 * k - 1) * p[:, k - 1] + dp[:, k - 2]
        return p, 2.0 * dp

    def _op(n_lv: int, k_d: int = 18, q_cut: int = 240) -> Tuple[np.ndarray, List[Tuple[int, int]]]:
        nd, _ = leggauss(k_d)
        xs = 0.5 * (nd + 1.0)
        vm, _ = _vand(xs, k_d)
        vinv = np.linalg.inv(vm)
        qn, qw = leggauss(20)
        sq = 0.5 * (qn + 1.0)
        wq = 0.5 * qw
        cs = _lines(n_lv)
        imap = {c: i for i, c in enumerate(cs)}
        blks: List[np.ndarray] = []
        for r in range(1, n_lv + 1):
            ns = (np.arange(q_cut, dtype=np.float64) * n_lv + r)[:, None]
            den = ns + xs[None, :]
            pe, _ = _vand((1.0 / den).ravel(), k_d)
            direct = np.einsum("qi,qik->ik", den ** (-2.0), pe.reshape(q_cut, k_d, k_d))
            uq = 1.0 / (float(q_cut * n_lv + r) + xs)
            pi_m, _ = _vand((uq[:, None] * sq[None, :]).ravel(), k_d)
            iterm = (uq[:, None] / float(n_lv)) * np.einsum("m,imk->ik", wq, pi_m.reshape(k_d, len(sq), k_d))
            pq, dpq = _vand(uq, k_d)
            fq = (uq[:, None] ** 2) * pq
            dfq = -float(n_lv) * (2.0 * (uq[:, None] ** 3) * pq + (uq[:, None] ** 4) * dpq)
            blks.append((direct + iterm + 0.5 * fq - dfq / 12.0) @ vinv)
        gop = np.zeros((len(cs) * k_d, len(cs) * k_d), dtype=np.float64)
        for ri, r in enumerate(range(1, n_lv + 1)):
            for ci, (cx, cy) in enumerate(cs):
                nx, ny = cy % n_lv, (cx + r * cy) % n_lv
                cj = imap[min((nx, ny), ((-nx) % n_lv, (-ny) % n_lv))]
                gop[ci * k_d : (ci + 1) * k_d, cj * k_d : (cj + 1) * k_d] += blks[ri]
        return gop, cs

    g5, c5 = _op(5, 18)
    g10, c10 = _op(10, 18)
    i5 = {c: i for i, c in enumerate(c5)}
    p_cos = np.zeros((len(c10), len(c5)), dtype=np.float64)
    for i10, (a, b) in enumerate(c10):
        p_cos[i10, i5[min((a % 5, b % 5), ((-a) % 5, (-b) % 5))]] = 1.0 / math.sqrt(3.0)
    p_full = np.kron(p_cos, np.eye(18))
    inter_err = float(np.linalg.norm(g10 @ p_full - p_full @ g5, ord=2))

    ones5 = np.ones((len(c5), 1)) / math.sqrt(len(c5))
    q5, _ = np.linalg.qr(np.hstack([ones5, np.eye(len(c5), len(c5) - 1)]), mode="complete")
    ps5 = np.kron(q5[:, 1:], np.eye(18))
    m5_sub = ps5.T @ (g5 @ g5) @ ps5
    rho5 = float(np.max(np.abs(np.linalg.eigvals(m5_sub))))

    coercivity_err = float(
        sum(
            abs(float((Fr(1, 3) + 4 * (Fr(r, n) ** 2 - Fr(r, n) + Fr(1, 6))) - (2 * Fr(r, n) - 1) ** 2))
            for n in range(2, 12)
            for r in range(n)
        )
    )
    return {
        "rho5": rho5,
        "intertwine_err": inter_err,
        "coercivity_identity_err": coercivity_err,
    }


def test_subweave_schreier_mayer_oldspace_and_raysinger_coercivity() -> None:
    sch = schreier_closure_pm_gamma1_5()
    assert sch["index_in_psl2z"] == 12
    assert sch["unfactored_count"] == 0
    assert sch["max_word_depth"] <= 4

    sp5 = mayer_selberg_subweave_spectrum(5, k_nodes=16)
    sp10 = mayer_selberg_subweave_spectrum(10, k_nodes=16)
    ref = _referee_gauss_legendre_oldspace_and_coercivity()

    assert abs(sp5["subweave_mayer_rho0"] - ref["rho5"]) < 1e-12
    assert abs(sp5["subweave_mayer_rho0"] - sp10["subweave_mayer_rho0"]) < 1e-12
    assert sp5["subweave_fredholm_det"] < sp10["subweave_fredholm_det"] - 0.8
    assert ref["intertwine_err"] < 1e-13
    assert ref["coercivity_identity_err"] < 1e-15

    # Verify +-Gamma_1(5) T-invariance of holomorphic Ray-Singer sheet (0, 1) potential across Re(tau)=0.5
    old_dps = mp.mp.dps
    mp.mp.dps = 40
    try:
        v_a = ray_singer_x1_sheet_potential_mp(mp.mpc("0.42", "1.15"), 0, 1, 5, kappa=2, n_terms=60)
        v_b = ray_singer_x1_sheet_potential_mp(mp.mpc("1.42", "1.15"), 0, 1, 5, kappa=2, n_terms=60)
        assert float(abs(v_a - v_b)) < 1e-30
    finally:
        mp.mp.dps = old_dps



# ---------------------------------------------------------------------------
# THM-CORE-06: Two-Tick Bijection & Twin-Odd Level-5 Maass Golden-Regulator Law
# ---------------------------------------------------------------------------


@referee
def _referee_maass_1949_grossencharacter_and_two_tick_check() -> Dict[str, Any]:
    """Independently constructs the 45-dps Maass (1949) Q(sqrt 5) Euler series (zero pullback) & 2-tick words."""
    # 1. Independent string-rewriting verification of {FF, FF', F'F, F'F'} == {LR, L^2, R^2, RL}
    l_m = np.array([[1, 1], [0, 1]], dtype=np.int64)
    r_m = np.array([[1, 0], [1, 1]], dtype=np.int64)
    p_m = np.array([[0, 1], [1, 0]], dtype=np.int64)
    f_a = l_m @ p_m
    f_b = r_m @ p_m
    pair_diff = (
        int(np.max(np.abs(f_a @ f_a - l_m @ r_m)))
        + int(np.max(np.abs(f_a @ f_b - l_m @ l_m)))
        + int(np.max(np.abs(f_b @ f_a - r_m @ r_m)))
        + int(np.max(np.abs(f_b @ f_b - r_m @ l_m)))
    )

    # 2. Exact 45-dps Maass (1949) Q(sqrt 5) Grossencharacter Euler product (zero producer calls, zero pullback)
    old_dps = mp.mp.dps
    mp.mp.dps = 45
    try:
        phi = (1 + mp.sqrt(5)) / 2
        r1 = mp.pi / (2 * mp.log(phi))
        lam1 = mp.mpf("0.25") + r1 * r1
        sc = mp.exp(mp.pi * r1 / 2)
        split_pairs = {
            11: ((7 + mp.sqrt(5)) / 2, (7 - mp.sqrt(5)) / 2),
            19: ((9 + mp.sqrt(5)) / 2, (9 - mp.sqrt(5)) / 2),
            29: ((11 + mp.sqrt(5)) / 2, (11 - mp.sqrt(5)) / 2),
            31: (6 + mp.sqrt(5), 6 - mp.sqrt(5)),
            41: ((13 + mp.sqrt(5)) / 2, (13 - mp.sqrt(5)) / 2),
        }

        def _cn(n_v: int) -> mp.mpf:
            acc = mp.mpf(1)
            rem = n_v
            for p_d in range(2, n_v + 1):
                if rem % p_d == 0:
                    k_e = 0
                    while rem % p_d == 0:
                        rem //= p_d
                        k_e += 1
                    if p_d == 5:
                        acc *= mp.mpf(-1) ** k_e
                    elif p_d % 5 in (2, 3):
                        if k_e % 2 == 1:
                            return mp.mpf(0)
                    else:
                        ap, bp = split_pairs[p_d]
                        th = r1 * mp.log(ap / bp)
                        acc *= mp.sin((k_e + 1) * th) / mp.sin(th)
            return acc

        cs = [_cn(k) for k in range(1, 43)]

        def _psi1(xv: mp.mpf, yv: mp.mpf) -> mp.mpf:
            sy = mp.sqrt(yv)
            tot = mp.mpf(0)
            for idx, c_v in enumerate(cs, start=1):
                if c_v == 0:
                    continue
                tot += c_v * sy * mp.re(mp.besselk(1j * r1, 2 * mp.pi * idx * yv)) * sc * mp.sin(2 * mp.pi * idx * xv)
            return tot

        # Direct Fricke functional identity psi_1(-1 / (5 z)) + psi_1(z) == 0 without pullback
        z_t = mp.mpc("0.27", "0.41")
        w5_t = -1 / (5 * z_t)
        fricke_err = float(abs(_psi1(mp.re(w5_t), mp.im(w5_t)) + _psi1(mp.re(z_t), mp.im(z_t))))

        # Direct interior PDE check -y^2 (psi_xx + psi_yy) == (1/4 + R_1^2) psi_1
        h_p = mp.mpf("1e-10")
        xm, ym = mp.mpf("0.23"), mp.mpf("0.46")
        f0 = _psi1(xm, ym)
        dxx = (_psi1(xm + h_p, ym) - 2 * f0 + _psi1(xm - h_p, ym)) / (h_p * h_p)
        dyy = (_psi1(xm, ym + h_p) - 2 * f0 + _psi1(xm, ym - h_p)) / (h_p * h_p)
        pde_err = float(abs(-(ym * ym) * (dxx + dyy) - lam1 * f0))

        # Locate exact Fricke-circle peak theta* and measure full 2D gradient
        h_g = mp.mpf("1e-11")

        def _d_th(th_v: mp.mpf) -> mp.mpf:
            fp = _psi1(mp.cos(th_v + h_g) / mp.sqrt(5), mp.sin(th_v + h_g) / mp.sqrt(5)) ** 2
            fm = _psi1(mp.cos(th_v - h_g) / mp.sqrt(5), mp.sin(th_v - h_g) / mp.sqrt(5)) ** 2
            return (fp - fm) / (2 * h_g)

        th_s = mp.findroot(_d_th, mp.mpf("0.97339"))
        xs = mp.cos(th_s) / mp.sqrt(5)
        ys = mp.sin(th_s) / mp.sqrt(5)
        gx = (_psi1(xs + h_g, ys) ** 2 - _psi1(xs - h_g, ys) ** 2) / (2 * h_g)
        gy = (_psi1(xs, ys + h_g) ** 2 - _psi1(xs, ys - h_g) ** 2) / (2 * h_g)
        grad_2d = float(mp.hypot(gx, gy))

        return {
            "pair_diff_plus_one": int(pair_diff + 1),
            "r1_exact": float(r1),
            "c11_exact": float(cs[10]),
            "fricke_err": fricke_err,
            "pde_err": pde_err,
            "tau_star_exact": [float(xs), float(ys)],
            "grad_2d": grad_2d,
        }
    finally:
        mp.mp.dps = old_dps


def test_two_tick_bijection_and_twin_odd_maass_p776() -> None:
    bij = two_tick_bijection_census(max_ticks=8)
    assert bij["mismatch_depths"] == 0
    for k_ev, cnt in bij["even_counts"].items():
        assert cnt == 2 ** k_ev
    for k_od, cnt in bij["odd_counts"].items():
        assert cnt == 2 ** k_od

    maass = twin_odd_maass_golden_and_kramers()
    ref = _referee_maass_1949_grossencharacter_and_two_tick_check()
    assert ref["pair_diff_plus_one"] == 1

    # Guardrail 4 benchmark: SL_2(Z) odd ground state R_1^- (Hejhal 1983)
    assert abs(maass["sl2z_r1_odd"] - 9.533695261353558) < 1e-11
    assert maass["sl2z_ychk_err"] < 1e-12

    # Level-5 twin-odd ground state R_1 = pi / (2 ln phi) & Maass (1949) Q(sqrt 5) identities
    assert abs(maass["r1_level5"] - ref["r1_exact"]) < 1e-13
    assert maass["r1_golden_diff"] < 1e-13
    assert maass["r1_ychk_err"] < 1e-12
    assert abs(maass["c2_c3_c4_c5"][0]) < 1e-13
    assert abs(maass["c2_c3_c4_c5"][1]) < 1e-13
    assert abs(maass["c2_c3_c4_c5"][2] - 1.0) < 1e-13
    assert abs(maass["c2_c3_c4_c5"][3] + 1.0) < 1e-13
    assert abs(maass["c11"] - ref["c11_exact"]) < 1e-12
    assert maass["elliptic_zero_abs"] < 1e-13
    assert ref["fricke_err"] < 1e-35
    assert ref["pde_err"] < 1e-15
    assert ref["grad_2d"] < 1e-18
    assert math.hypot(
        maass["tau_maass_star"][0] - ref["tau_star_exact"][0],
        maass["tau_maass_star"][1] - ref["tau_star_exact"][1],
    ) < 5e-9

    # Lowest Class B Kramers doublet R_2^+ == R_2^- & direct operator anticommutation (W_5 T_2 + T_2 W_5) = 0
    assert abs(maass["r2_plus"] - 4.893781291438453) < 1e-12
    assert maass["r2_kramers_split"] < 1e-13
    assert maass["r2_ychk_max"] < 1e-12
    assert maass["w5_t2_anticomm_abs"] < 1e-13
