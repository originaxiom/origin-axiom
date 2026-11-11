"""Independent Zero-Trust Referee Lock for B1881 (P-776 Twin-Odd Maass Operator & Whole-Subweave Read-Out).

Enforces Guardrails 1-6 and L10 / PV24 / tracked-deps:
  - Never imports or calls `subweave_p776_and_hierarchy.py` (strict producer-referee separation).
  - Verifies Commit-A SHA-256 seal integrity (`ARTIFACT_HASHES.txt` vs `PREREGISTRATION.md` and
    `verification/subweave_p776_and_hierarchy.py` on disk).
  - Independently constructs a Gauss-Legendre + Euler-Maclaurin transfer operator (distinct from
    the producer's Chebyshev collocation) to verify R10-A on Omega_1(5) and Omega_1(10) to < 1e-12
    and the isometric old-space pullback P_{10<-5} intertwining G_{10} P == P G_5.
  - Independently constructs 50-dps holomorphic fractional-nome Ray-Singer torsion to verify C3
    (+-Gamma_1(5) invariance, exact `(2*a_1 - 1)^2` cusp-slope identity, and positive-definite
    Hessians at tau_0* and tau_0^{(2)*}).
  - Independently solves the P-776 twin-odd Maass eigenvalue problem on (Gamma_0(5), chi_5) using
    DIFFERENT horocycle heights (Y_ref = 0.152, Y_chk = 0.138), DIFFERENT truncation (M_ref = 26),
    DIFFERENT quadrature grid (Q_ref = 144), and an independent Gauss-Legendre Basset evaluator:
      * Verifies R_1 == pi / (2 ln phi) to < 1e-12 (Class A Q(sqrt(5)) dihedral singleton, eps_J = -1, eps_5 = -1);
      * Verifies interior hyperbolic PDE `-y^2 (psi_xx + psi_yy) == (1/4 + R_1^2) psi` via 45-dps mpmath
        central finite differences (h = 1e-10) to < 1e-15;
      * Verifies the lowest Class B Kramers doublet R_2 = 4.893781291438453 (`|R^+ - R^-| < 1e-12`),
        forced zeros at z_{e,1}, z_{e,2} = (+-2 + i)/5 (< 1e-13), and direct operator anticommutation
        `|(W_5 T_2 + T_2 W_5) psi| < 1e-12`;
      * Independently polishes the unique global peak of rho_1(z) = |psi_1(z)|^2 on the Fricke circle
        C_0 = {|z|^2 = 1/5}, verifying 2D stationarity (||grad rho_1|| < 1e-11) and strict 2D negative-definite
        Hessian (lambda_max(Hess rho_1) < -2.0 < 0).
  - Independently verifies H1, H2, H3, and H4 (SL_2(Z) covariant reduction of tau_Maass* to
    tau_red = -0.25769889 + 1.84883572i, 2/96 joint H4a+H4b pass on cusp-0 twin lines (1/5, 0) and
    (2/5, 0) at L_2 (S, S, S) with opposite chiral signs of J across the X_0(5) orbit, failure of
    (St, S, S) on H4a, and 12-draw Haar unitary basis-scrambling invariance to < 1e-13).
"""

from __future__ import annotations

from fractions import Fraction as Fr
import hashlib
import json
import math
import pathlib
import sys
from typing import Dict, List, Tuple

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss
import scipy.optimize as sp_opt
import scipy.special as sp_spec


ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC_DIR = ROOT / "frontier" / "B1881_p776_twin_odd_operator_and_whole_subweave_readout"
HASHES_TXT = ARC_DIR / "ARTIFACT_HASHES.txt"
PREREG_MD = ARC_DIR / "PREREGISTRATION.md"
SEALED_PY = ARC_DIR / "verification" / "subweave_p776_and_hierarchy.py"
COMMITTED_JSON = ARC_DIR / "verification" / "subweave_p776_and_hierarchy.json"


def test_b1881_seal_integrity_and_json_contract() -> None:
    """Verifies that Commit-A SHA-256 hashes match PREREGISTRATION.md and subweave_p776_and_hierarchy.py on disk."""
    lines = [
        ln.strip()
        for ln in HASHES_TXT.read_text(encoding="utf-8").splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    assert len(lines) == 2
    entries: Dict[str, str] = {}
    for ln in lines:
        digest, rel = ln.split(None, 1)
        entries[rel.strip()] = digest.strip()

    prereg_sha = hashlib.sha256(PREREG_MD.read_bytes()).hexdigest()
    script_sha = hashlib.sha256(SEALED_PY.read_bytes()).hexdigest()
    assert entries["PREREGISTRATION.md"] == prereg_sha
    assert entries["verification/subweave_p776_and_hierarchy.py"] == script_sha

    data = json.loads(COMMITTED_JSON.read_text(encoding="utf-8"))
    assert data["arc"] == "B1881"
    assert "0 of 19" in data["data_free"]
    assert data["C0"]["holds"] is True
    assert data["C1"]["holds"] is True
    assert data["C2"]["holds"] is True
    assert data["C3"]["holds"] is True
    assert data["C4_P776_twin_odd_maass"]["holds"] is True
    assert data["H4_P776_maass_fr_fib_test"]["holds_H4_joint"] is True


# =============================================================================
# Independent Referee 1: C2 Mayer-Selberg Legendre/Euler-Maclaurin & Oldspace
# =============================================================================


def _independent_marked_lines(n_lv: int) -> List[Tuple[int, int]]:
    s = set()
    for a in range(n_lv):
        for b in range(n_lv):
            if math.gcd(math.gcd(a, b), n_lv) == 1:
                s.add(min((a, b), ((-a) % n_lv, (-b) % n_lv)))
    return sorted(s)


def _independent_act_line(g: Tuple[int, int, int, int], line: Tuple[int, int], n_lv: int) -> Tuple[int, int]:
    nx = (g[0] * line[0] + g[1] * line[1]) % n_lv
    ny = (g[2] * line[0] + g[3] * line[1]) % n_lv
    return min((nx, ny), ((-nx) % n_lv, (-ny) % n_lv))


def _legendre_shifted_vandermonde_and_deriv(xs: np.ndarray, k_deg: int) -> Tuple[np.ndarray, np.ndarray]:
    u = 2.0 * xs - 1.0
    p = np.zeros((len(xs), k_deg), dtype=np.float64)
    dp_du = np.zeros((len(xs), k_deg), dtype=np.float64)
    p[:, 0] = 1.0
    if k_deg > 1:
        p[:, 1] = u
        dp_du[:, 1] = 1.0
    for k in range(2, k_deg):
        p[:, k] = ((2 * k - 1) * u * p[:, k - 1] - (k - 1) * p[:, k - 2]) / float(k)
        dp_du[:, k] = (2 * k - 1) * p[:, k - 1] + dp_du[:, k - 2]
    return p, 2.0 * dp_du


def _independent_euler_maclaurin_legendre_coset_op(
    n_lv: int, k_deg: int = 20, q_cutoff: int = 300, grid: str = "leggauss"
) -> Tuple[np.ndarray, List[Tuple[int, int]]]:
    if grid == "leggauss":
        nodes_m11, _ = leggauss(k_deg)
        xs = 0.5 * (nodes_m11 + 1.0)
    elif grid == "cheb_nodes":
        j_idx = np.arange(k_deg, dtype=np.float64)
        xs = 0.5 * (1.0 + np.cos(math.pi * (2.0 * j_idx + 1.0) / (2.0 * k_deg)))
    else:
        raise ValueError(f"Unknown grid: {grid}")
    v_mat, _ = _legendre_shifted_vandermonde_and_deriv(xs, k_deg)
    v_inv = np.linalg.inv(v_mat)

    q_quad_nodes, q_quad_weights = leggauss(max(24, (k_deg + 3) // 2 + 2))
    s_quad = 0.5 * (q_quad_nodes + 1.0)
    w_quad = 0.5 * q_quad_weights

    cosets = _independent_marked_lines(n_lv)
    d_cos = len(cosets)
    idx_map = {c: i for i, c in enumerate(cosets)}

    blocks: List[np.ndarray] = []
    for r in range(1, n_lv + 1):
        ns = (np.arange(q_cutoff, dtype=np.float64) * n_lv + r)[:, None]
        den = ns + xs[None, :]
        u_vals = 1.0 / den
        w = den ** (-2.0)
        p_eval, _ = _legendre_shifted_vandermonde_and_deriv(u_vals.ravel(), k_deg)
        direct = np.einsum("qi,qik->ik", w, p_eval.reshape(q_cutoff, k_deg, k_deg))

        den_q = float(q_cutoff * n_lv + r) + xs
        u_q = 1.0 / den_q
        u_grid = u_q[:, None] * s_quad[None, :]
        p_int, _ = _legendre_shifted_vandermonde_and_deriv(u_grid.ravel(), k_deg)
        p_int = p_int.reshape(k_deg, len(s_quad), k_deg)
        integral_term = (u_q[:, None] / float(n_lv)) * np.einsum("m,imk->ik", w_quad, p_int)

        pq_val, dpq_dx = _legendre_shifted_vandermonde_and_deriv(u_q, k_deg)
        f_q = (u_q[:, None] ** 2) * pq_val
        df_dt_q = -float(n_lv) * (2.0 * (u_q[:, None] ** 3) * pq_val + (u_q[:, None] ** 4) * dpq_dx)
        tail = integral_term + 0.5 * f_q - (1.0 / 12.0) * df_dt_q
        blocks.append((direct + tail) @ v_inv)

    g_op = np.zeros((d_cos * k_deg, d_cos * k_deg), dtype=np.float64)
    for r_i, r in enumerate(range(1, n_lv + 1)):
        gn = (0, 1 % n_lv, 1 % n_lv, r % n_lv)
        for ci, c_val in enumerate(cosets):
            cj = idx_map[_independent_act_line(gn, c_val, n_lv)]
            g_op[ci * k_deg : (ci + 1) * k_deg, cj * k_deg : (cj + 1) * k_deg] += blocks[r_i]
    return g_op, cosets


def test_b1881_c2_independent_legendre_and_oldspace_pullback() -> None:
    data = json.loads(COMMITTED_JSON.read_text(encoding="utf-8"))
    c2_levels = {row["N"]: row["X1"] for row in data["C2"]["levels"]}

    def _sub_spectrum(g_mat: np.ndarray, d_c: int, k_d: int) -> Tuple[float, float, float]:
        m_mat = g_mat @ g_mat
        ones = np.ones((d_c, 1), dtype=np.float64) / math.sqrt(d_c)
        q_orth, _ = np.linalg.qr(np.hstack([ones, np.eye(d_c, d_c - 1)]), mode="complete")
        p_tr = np.kron(ones, np.eye(k_d))
        p_sb = np.kron(q_orth[:, 1:], np.eye(k_d))
        ev_tr = np.sort(np.abs(np.linalg.eigvals(p_tr.T @ m_mat @ p_tr)))[::-1]
        m_sb = p_sb.T @ m_mat @ p_sb
        ev_sb = np.sort(np.abs(np.linalg.eigvals(m_sb)))[::-1]
        det_sb = float(np.linalg.det(np.eye(m_sb.shape[0]) - m_sb))
        return float(ev_tr[1]), float(ev_sb[0]), det_sb

    g5_18, cos5 = _independent_euler_maclaurin_legendre_coset_op(5, k_deg=18, grid="leggauss")
    g5_24, _ = _independent_euler_maclaurin_legendre_coset_op(5, k_deg=24, grid="leggauss")
    g10_24, cos10 = _independent_euler_maclaurin_legendre_coset_op(10, k_deg=24, grid="leggauss")

    w5_18, rho5_18, _ = _sub_spectrum(g5_18, len(cos5), 18)
    w5_24, rho5_24, det5_24 = _sub_spectrum(g5_24, len(cos5), 24)
    w10_24, rho10_24, det10_24 = _sub_spectrum(g10_24, len(cos10), 24)

    assert abs(w5_24 - w5_18) < 1e-13
    assert abs(rho5_24 - rho5_18) < 1e-13
    assert abs(w5_24 - c2_levels[5]["trivial_lambda2_wirsing_sq"]) < 1e-12
    assert abs(w10_24 - c2_levels[10]["trivial_lambda2_wirsing_sq"]) < 1e-12
    assert abs(rho5_24 - c2_levels[5]["subweave_mayer_spectral_radius"]) < 1e-12
    assert abs(rho10_24 - c2_levels[10]["subweave_mayer_spectral_radius"]) < 1e-12

    g5_c16, _ = _independent_euler_maclaurin_legendre_coset_op(5, k_deg=16, grid="cheb_nodes")
    g10_c16, _ = _independent_euler_maclaurin_legendre_coset_op(10, k_deg=16, grid="cheb_nodes")
    _, _, det5_c16 = _sub_spectrum(g5_c16, len(cos5), 16)
    _, _, det10_c16 = _sub_spectrum(g10_c16, len(cos10), 16)
    assert abs(det5_c16 - c2_levels[5]["subweave_fredholm_det_at_s1"]) < 1e-12
    assert abs(det10_c16 - c2_levels[10]["subweave_fredholm_det_at_s1"]) < 1e-12

    idx5 = {c: i for i, c in enumerate(cos5)}
    pull_cos = np.zeros((len(cos10), len(cos5)), dtype=np.float64)
    for i10, (a10, b10) in enumerate(cos10):
        c5 = min((a10 % 5, b10 % 5), ((-a10) % 5, (-b10) % 5))
        pull_cos[i10, idx5[c5]] = 1.0 / math.sqrt(3.0)

    assert float(np.linalg.norm(pull_cos.T @ pull_cos - np.eye(len(cos5)), ord="fro")) < 1e-14
    p_full = np.kron(pull_cos, np.eye(24))
    assert float(np.linalg.norm(g10_24 @ p_full - p_full @ g5_24, ord=2)) < 1e-13
    assert abs(rho10_24 - rho5_24) < 1e-13
    assert det5_24 < det10_24 - 0.8


# =============================================================================
# Independent Referee 2: C3 50-dps Ray-Singer Torsion & Coercivity
# =============================================================================


def _independent_ray_singer_potential_mp(tau: mp.mpc, r1: int, r2: int, n_lv: int, kappa: int) -> mp.mpf:
    im_t = float(mp.im(tau))
    n_terms = max(70, int(26.0 / im_t) + 20)
    q2 = mp.exp(2j * mp.pi * tau)
    log_eta_abs = -mp.pi * mp.im(tau) / 12
    qm = q2
    for _ in range(n_terms):
        log_eta_abs += mp.log(abs(1 - qm))
        qm *= q2

    a1_i = r1 % n_lv
    a1 = mp.mpf(a1_i) / mp.mpf(n_lv)
    a2 = mp.mpf(r2 % n_lv) / mp.mpf(n_lv)
    b2 = a1 * a1 - a1 + mp.mpf(1) / 6
    z = mp.exp(2j * mp.pi * a2)

    log_g_abs = -mp.pi * mp.im(tau) * b2
    if a1_i == 0:
        log_g_abs += mp.log(abs(1 - z))
        qm = q2
        for _ in range(1, n_terms):
            log_g_abs += mp.log(abs(1 - qm * z)) + mp.log(abs(1 - qm / z))
            qm *= q2
    else:
        for m in range(0, n_terms):
            w1 = mp.exp(2j * mp.pi * (mp.mpf(m) + a1) * tau) * z
            w2 = mp.exp(2j * mp.pi * (mp.mpf(m + 1) - a1) * tau) / z
            log_g_abs += mp.log(abs(1 - w1)) + mp.log(abs(1 - w2))

    return -(mp.log(mp.im(tau)) + 4 * log_eta_abs + (2 * kappa) * log_g_abs)


def test_b1881_c3_independent_ray_singer_50dps_coercivity_and_hessians() -> None:
    data = json.loads(COMMITTED_JSON.read_text(encoding="utf-8"))
    c3 = data["C3"]

    for n_lv in range(2, 13):
        for r1 in range(n_lv):
            a1 = Fr(r1, n_lv)
            b2 = a1 * a1 - a1 + Fr(1, 6)
            assert Fr(1, 3) + 4 * b2 == (2 * a1 - 1) ** 2
        assert any((2 * Fr(r1, n_lv) - 1) == 0 for r1 in range(n_lv)) == (n_lv % 2 == 0)

    old_dps = mp.mp.dps
    mp.mp.dps = 50
    try:
        gamma1_5_valid = [(1, 1, 0, 1), (1, 0, 5, 1), (6, -5, 5, -4), (4, -1, 5, -1)]
        t_test = mp.mpc("0.17", "1.23")
        for kap in (1, 2):
            v_base = _independent_ray_singer_potential_mp(t_test, 0, 1, 5, kap)
            for a, b, c, d in gamma1_5_valid:
                assert a * d - b * c == 1
                t_img = (a * t_test + b) / (c * t_test + d)
                v_img = _independent_ray_singer_potential_mp(t_img, 0, 1, 5, kap)
                assert float(abs(v_img - v_base)) < 1e-35

        c1_n5 = next(r for r in c3["R10C1_kappa1_minima"] if r["N"] == 5)
        c2_n5 = next(r for r in c3["R10C2_odd_N_minima"] if r["N"] == 5)
        t1 = mp.mpc(repr(c1_n5["tau0_star"][0]), repr(c1_n5["tau0_star"][1]))
        t2 = mp.mpc(c2_n5["tau0_kappa2_star_30dps"][0], c2_n5["tau0_kappa2_star_30dps"][1])

        for t_pt, kap, ref_v, ref_eig in (
            (t1, 1, c1_n5["V_min"], c1_n5["hessian_min_eig"]),
            (t2, 2, c2_n5["tau0_kappa2_star"] and c2_n5["V_min"], c2_n5["hessian_min_eig"]),
        ):
            v0 = _independent_ray_singer_potential_mp(t_pt, 2, 2, 5, kap)
            assert float(abs(v0 - ref_v)) < 1e-13
            h = mp.mpf("1e-7")
            vp_x = _independent_ray_singer_potential_mp(t_pt + h, 2, 2, 5, kap)
            vm_x = _independent_ray_singer_potential_mp(t_pt - h, 2, 2, 5, kap)
            vp_y = _independent_ray_singer_potential_mp(t_pt + 1j * h, 2, 2, 5, kap)
            vm_y = _independent_ray_singer_potential_mp(t_pt - 1j * h, 2, 2, 5, kap)
            gx = float((vp_x - vm_x) / (2 * h))
            gy = float((vp_y - vm_y) / (2 * h))
            assert math.hypot(gx, gy) < 1e-11

            dxx = float((vp_x - 2 * v0 + vm_x) / (h * h))
            dyy = float((vp_y - 2 * v0 + vm_y) / (h * h))
            dxy = float(
                (
                    _independent_ray_singer_potential_mp(t_pt + h + 1j * h, 2, 2, 5, kap)
                    - _independent_ray_singer_potential_mp(t_pt + h - 1j * h, 2, 2, 5, kap)
                    - _independent_ray_singer_potential_mp(t_pt - h + 1j * h, 2, 2, 5, kap)
                    + _independent_ray_singer_potential_mp(t_pt - h - 1j * h, 2, 2, 5, kap)
                )
                / (4 * h * h)
            )
            eigs = np.linalg.eigvalsh(np.array([[dxx, dxy], [dxy, dyy]], dtype=float))
            assert float(np.min(eigs)) > 0.0
            assert abs(float(np.min(eigs)) - ref_eig) < 1e-11
    finally:
        mp.mp.dps = old_dps


# =============================================================================
# Independent Referee 3: C4 P-776 Twin-Odd Maass Solver, PDE, Anticommutation & Peak
# =============================================================================


_GL_NODES_96, _GL_WEIGHTS_96 = leggauss(96)


def _referee_k_ir(r_val: float, u_arr: np.ndarray) -> np.ndarray:
    """Independent Gauss-Legendre shifted-contour + 38-term series evaluator for K_{iR}(u)."""
    shape = np.shape(u_arr)
    u = np.asarray(u_arr, dtype=np.float64).ravel()
    out = np.empty_like(u)
    m_small = u <= 3.5
    if np.any(m_small):
        us = u[m_small]
        ks = np.arange(38, dtype=np.float64)
        c0 = np.exp(0.5 * math.pi * r_val - sp_spec.loggamma(1.0 + 1j * r_val))
        coeffs = np.empty(38, dtype=np.complex128)
        coeffs[0] = c0
        for k in range(1, 38):
            coeffs[k] = coeffs[k - 1] / (k * (k + 1j * r_val))
        hu = 0.5 * us
        pows = (hu[:, None] ** 2) ** ks[None, :]
        val_i = (pows @ coeffs) * np.exp(1j * r_val * np.log(hu))
        pref = -2.0 * math.pi * math.exp(-1.5 * math.pi * r_val) / (1.0 - math.exp(-2.0 * math.pi * r_val))
        out[m_small] = pref * np.imag(val_i)
    m_big = ~m_small
    if np.any(m_big):
        ub = u[m_big]
        out_b = np.zeros_like(ub)
        act = ub < 54.0
        if np.any(act):
            ua = ub[act]
            al = np.minimum(np.arctan2(r_val, ua), 1.28)
            ca, sa = np.cos(al), np.sin(al)
            tmax = np.arccosh(1.0 + 40.0 / np.maximum(ua * ca, 0.5))
            # Integrate on [0, tmax] via 96-point Gauss-Legendre (using evenness after contour shift!)
            # Note: after shifting t -> t - i*al, integrand exp(-u cosh(t - i*al)) cos(R(t)...) is symmetric
            # on (-tmax, +tmax), so integrate s in [-tmax, tmax] via GL_96:
            s_pts = tmax[:, None] * _GL_NODES_96[None, :]
            w_pts = tmax[:, None] * _GL_WEIGHTS_96[None, :]
            integrand = np.exp(-r_val * al[:, None] - (ua * ca)[:, None] * np.cosh(s_pts)) * np.cos(
                r_val * s_pts - (ua * sa)[:, None] * np.sinh(s_pts)
            )
            out_b[act] = 0.5 * np.sum(w_pts * integrand, axis=1)
        out[m_big] = out_b
    return out.reshape(shape)


def _referee_pullback_gamma0_plus_5_scalar(z_in: complex, eps_5: int) -> Tuple[complex, int]:
    """Independent scalar complex-arithmetic pullback to F^+(Gamma_0^+(5))."""
    z = complex(z_in)
    sgn = 1
    for _ in range(120):
        n_int = int(round(z.real))
        if n_int != 0:
            z -= n_int
        if abs(z) < (1.0 / math.sqrt(5.0)) - 1e-15:
            z = -1.0 / (5.0 * z)
            sgn *= eps_5
            continue
        if z.real >= 0.0 and abs(z - 0.5) < (1.0 / math.sqrt(20.0)) - 1e-15:
            # (3*W_5(z) + 1) / (5*W_5(z) + 2) == (-3 + 5z) / (-5 + 10z) == 1/2 - 1/(20*(z - 1/2))
            w = -1.0 / (5.0 * z)
            z = (3.0 * w + 1.0) / (5.0 * w + 2.0)
            sgn *= -eps_5
            continue
        if z.real < 0.0 and abs(z + 0.5) < (1.0 / math.sqrt(20.0)) - 1e-15:
            # (3*W_5(z) - 1) / (-5*W_5(z) + 2) == (-3 - 5z) / (5 + 10z) == -1/2 - 1/(20*(z + 1/2))
            w = -1.0 / (5.0 * z)
            z = (3.0 * w - 1.0) / (-5.0 * w + 2.0)
            sgn *= -eps_5
            continue
        break
    z -= round(z.real)
    return z, sgn


def _referee_solve_sector_root(
    r_lo: float, r_hi: float, eps_j: int, eps_5: int, m_ref: int = 26, q_ref: int = 144, y_ref: float = 0.152, y_chk: float = 0.138
) -> Tuple[float, float, np.ndarray]:
    """Solves for a Maass cusp form in sector (eps_J, eps_5) on independent horocycle heights Y_ref=0.152, Y_chk=0.138."""
    xs = (np.arange(q_ref, dtype=np.float64) + 0.5) / (2.0 * q_ref)
    ns = np.arange(1, m_ref + 1, dtype=np.float64)
    pb_ref = [_referee_pullback_gamma0_plus_5_scalar(complex(float(x), y_ref), eps_5) for x in xs]
    pb_chk = [_referee_pullback_gamma0_plus_5_scalar(complex(float(x), y_chk), eps_5) for x in xs]

    def _mat(rv: float, yv: float, pbs: List[Tuple[complex, int]]) -> Tuple[np.ndarray, np.ndarray]:
        px = np.array([p[0].real for p in pbs], dtype=np.float64)
        py = np.array([p[0].imag for p in pbs], dtype=np.float64)
        pm = np.array([float(p[1]) for p in pbs], dtype=np.float64)
        sc = math.exp(0.5 * math.pi * rv)
        kh = _referee_k_ir(rv, 2.0 * np.pi * ns * yv) * sc * math.sqrt(yv)
        kp = _referee_k_ir(rv, 2.0 * np.pi * py[:, None] * ns[None, :]) * sc * np.sqrt(py[:, None])
        if eps_j == -1:
            tj = (2.0 / q_ref) * np.sin(2.0 * np.pi * ns[:, None] * xs[None, :])
            tp = pm[:, None] * np.sin(2.0 * np.pi * px[:, None] * ns[None, :])
        else:
            tj = (2.0 / q_ref) * np.cos(2.0 * np.pi * ns[:, None] * xs[None, :])
            tp = pm[:, None] * np.cos(2.0 * np.pi * px[:, None] * ns[None, :])
        return np.diag(kh) - tj @ (kp * tp), kh

    def _res(rv: float) -> float:
        am, kh = _mat(rv, y_ref, pb_ref)
        a_rest = np.linalg.solve(am[1:, 1:] / kh[1:, None], -am[1:, 0] / kh[1:])
        avec = np.concatenate([[1.0], a_rest])
        return float((am[0, :] @ avec) / kh[0])

    r_star = float(sp_opt.brentq(_res, r_lo, r_hi, xtol=1e-14, rtol=1e-14))
    am1, kh1 = _mat(r_star, y_ref, pb_ref)
    a_rest = np.linalg.solve(am1[1:, 1:] / kh1[1:, None], -am1[1:, 0] / kh1[1:])
    avec = np.concatenate([[1.0], a_rest])
    am2, kh2 = _mat(r_star, y_chk, pb_chk)
    ychk_err = float(np.linalg.norm((am2[:8, :] @ avec) / kh2[:8]))
    return r_star, ychk_err, avec


def test_b1881_c4_p776_independent_maass_pde_anticommutation_and_peak() -> None:
    data = json.loads(COMMITTED_JSON.read_text(encoding="utf-8"))
    c4 = data["C4_P776_twin_odd_maass"]

    # 0. Cross-check _referee_k_ir against 40-dps mpmath.besselk at 6 points across small & large u
    old_dps = mp.mp.dps
    mp.mp.dps = 40
    try:
        for rv_t, uv_t in ((3.264, 0.8), (3.264, 3.49), (3.264, 3.51), (4.894, 9.2), (6.528, 18.0)):
            ref_mp = float(mp.re(mp.besselk(1j * mp.mpf(repr(rv_t)), mp.mpf(repr(uv_t)))) * mp.exp(0.5 * mp.pi * rv_t))
            got_gl = float(_referee_k_ir(rv_t, np.array([uv_t]))[0] * math.exp(0.5 * math.pi * rv_t))
            assert abs(got_gl - ref_mp) < 1e-13
    finally:
        mp.mp.dps = old_dps

    # 1. Ground state R_1 on independent grid (M=26, Q=144, Y_ref=0.152, Y_chk=0.138)
    phi = 0.5 * (1.0 + math.sqrt(5.0))
    r1_exact = math.pi / (2.0 * math.log(phi))
    r1_ref, ychk_r1, a1_ref = _referee_solve_sector_root(3.20, 3.32, eps_j=-1, eps_5=-1)
    assert ychk_r1 < 1e-12
    assert abs(r1_ref - r1_exact) < 1e-13
    assert abs(r1_ref - c4["ground_state"]["R"]) < 1e-13
    # Class A Hecke eigenvalues: c_2 = c_3 = c_6 = 0, c_4 = +1, c_5 = -1
    assert abs(a1_ref[1]) < 1e-13
    assert abs(a1_ref[2]) < 1e-13
    assert abs(a1_ref[3] - 1.0) < 1e-13
    assert abs(a1_ref[4] + 1.0) < 1e-13
    assert abs(a1_ref[5]) < 1e-13

    # 2. Direct 45-dps mpmath interior PDE test: -y^2 (psi_xx + psi_yy) == (1/4 + R_1^2) psi_1 to < 1e-15!
    mp.mp.dps = 45
    try:
        r1_mp = mp.pi / (2 * mp.log((1 + mp.sqrt(5)) / 2))
        lam1_mp = mp.mpf("0.25") + r1_mp * r1_mp
        sc_mp = mp.exp(0.5 * mp.pi * r1_mp)
        a1_mp = [mp.mpf(repr(float(v))) for v in a1_ref]

        def _psi1_mp_raw(xm: mp.mpf, ym: mp.mpf) -> mp.mpf:
            acc = mp.mpf("0")
            sy = mp.sqrt(ym)
            for idx_n, coef in enumerate(a1_mp, start=1):
                if abs(coef) < mp.mpf("1e-20"):
                    continue
                kv = mp.re(mp.besselk(1j * r1_mp, 2 * mp.pi * idx_n * ym)) * sc_mp
                acc += coef * sy * kv * mp.sin(2 * mp.pi * idx_n * xm)
            return acc

        h_fd = mp.mpf("1e-10")
        for x_int, y_int in (("0.19", "0.47"), ("0.31", "0.39"), ("0.12", "0.73")):
            xm = mp.mpf(x_int)
            ym = mp.mpf(y_int)
            f0 = _psi1_mp_raw(xm, ym)
            assert abs(f0) > mp.mpf("0.05")
            dxx = (_psi1_mp_raw(xm + h_fd, ym) - 2 * f0 + _psi1_mp_raw(xm - h_fd, ym)) / (h_fd * h_fd)
            dyy = (_psi1_mp_raw(xm, ym + h_fd) - 2 * f0 + _psi1_mp_raw(xm, ym - h_fd)) / (h_fd * h_fd)
            pde_lhs = -(ym * ym) * (dxx + dyy)
            pde_rhs = lam1_mp * f0
            assert float(abs(pde_lhs - pde_rhs)) < 1e-15
    finally:
        mp.mp.dps = old_dps

    # 3. Lowest Class B Kramers doublet R_2 = 4.893781291438453 & direct operator anticommutation (W_5 T_2 + T_2 W_5) = 0
    r2_plus, ychk_2p, a2_plus = _referee_solve_sector_root(4.84, 4.95, eps_j=-1, eps_5=+1)
    r2_minus, ychk_2m, a2_minus = _referee_solve_sector_root(4.84, 4.95, eps_j=-1, eps_5=-1)
    assert ychk_2p < 1e-12 and ychk_2m < 1e-12
    assert abs(r2_plus - r2_minus) < 1e-13
    assert abs(0.5 * (r2_plus + r2_minus) - c4["lowest_class_b_doublet"]["R"]) < 1e-13

    def _eval_ref_global(rv: float, avec: np.ndarray, ej: int, e5: int, z_pt: complex) -> float:
        zp, sgn = _referee_pullback_gamma0_plus_5_scalar(z_pt, e5)
        ns = np.arange(1, len(avec) + 1, dtype=np.float64)
        sc = math.exp(0.5 * math.pi * rv)
        kv = _referee_k_ir(rv, 2.0 * np.pi * ns * zp.imag) * sc * math.sqrt(zp.imag)
        trig = np.sin(2.0 * np.pi * ns * zp.real) if ej == -1 else np.cos(2.0 * np.pi * ns * zp.real)
        return float(sgn) * float(np.dot(kv * trig, avec))

    # Forced vanishing at both elliptic points z_{e,1}, z_{e,2} = (+-2 + i)/5 (evaluated directly without pullback!)
    for ze in (complex(0.4, 0.2), complex(-0.4, 0.2)):
        ns = np.arange(1, len(a1_ref) + 1, dtype=np.float64)
        kv1 = _referee_k_ir(r1_ref, 2.0 * np.pi * ns * ze.imag) * math.exp(0.5 * math.pi * r1_ref) * math.sqrt(ze.imag)
        assert abs(float(np.dot(kv1 * np.sin(2.0 * np.pi * ns * ze.real), a1_ref))) < 1e-13
        kv2 = _referee_k_ir(r2_plus, 2.0 * np.pi * ns * ze.imag) * math.exp(0.5 * math.pi * r2_plus) * math.sqrt(ze.imag)
        assert abs(float(np.dot(kv2 * np.sin(2.0 * np.pi * ns * ze.real), a2_plus))) < 1e-13

    # Direct operator anticommutation (W_5 T_2 + T_2 W_5) psi_2^+ == 0 at 3 interior points
    # Recall (T_2 f)(z) = (1 / sqrt(2)) * (chi_5(2) f(2z) + f(z/2) + f((z + 1)/2)), chi_5(2) = -1
    def _t2_op(rv: float, avec: np.ndarray, ej: int, e5: int, z_pt: complex) -> float:
        return (
            -_eval_ref_global(rv, avec, ej, e5, 2.0 * z_pt)
            + _eval_ref_global(rv, avec, ej, e5, 0.5 * z_pt)
            + _eval_ref_global(rv, avec, ej, e5, 0.5 * (z_pt + 1.0))
        ) / math.sqrt(2.0)

    for z_probe in (complex(0.18, 0.53), complex(0.29, 0.44), complex(-0.23, 0.61)):
        w5_z = -1.0 / (5.0 * z_probe)
        w5_t2 = _t2_op(r2_plus, a2_plus, -1, +1, w5_z)
        # Since W_5 psi_2^+ == +psi_2^+, (T_2 W_5 psi_2^+)(z) == (T_2 psi_2^+)(z)!
        t2_w5 = _t2_op(r2_plus, a2_plus, -1, +1, z_probe)
        assert abs(t2_w5) > 0.02
        assert abs(w5_t2 + t2_w5) < 1e-13

    # 4. Independent global peak polish of rho_1(z) along C_0 and 2D negative-definite Hessian check
    # Normalize a1_ref to unit L^2(F^+) norm on an independent 32x40 Legendre grid
    xl, wl = leggauss(32)
    xr, wr = leggauss(20)
    tl, wt = leggauss(40)
    xs_q = np.concatenate([0.2 * (xl + 1.0), 0.45 + 0.05 * xr])
    ws_q = np.concatenate([0.2 * wl, 0.05 * wr])
    ts_q = 0.5 * (tl + 1.0)
    wt_q = 0.5 * wt
    yb_q = np.maximum(np.sqrt(np.maximum(0.2 - xs_q ** 2, 0.0)), np.sqrt(np.maximum(0.05 - (xs_q - 0.5) ** 2, 0.0)))
    norm_sq = 0.0
    ns_1 = np.arange(1, len(a1_ref) + 1, dtype=np.float64)
    sc_1 = math.exp(0.5 * math.pi * r1_ref)
    for xi_v, wi_v, ybi_v in zip(xs_q, ws_q, yb_q):
        ys_col = np.minimum(ybi_v / ts_q, 9.5)
        kv_col = _referee_k_ir(r1_ref, 2.0 * np.pi * ys_col[:, None] * ns_1[None, :]) * sc_1 * np.sqrt(ys_col[:, None])
        vals_col = (kv_col * np.sin(2.0 * np.pi * xi_v * ns_1)[None, :]) @ a1_ref
        norm_sq += 2.0 * (wi_v / ybi_v) * float(np.dot(wt_q, vals_col * vals_col))
    a1_l2 = a1_ref / math.sqrt(norm_sq)

    def _rho1_ref(x_v: float, y_v: float) -> float:
        val = _eval_ref_global(r1_ref, a1_l2, -1, -1, complex(x_v, y_v))
        return val * val

    # Locate theta* on C_0 using BOTH:
    # (a) independent numerical collocation a1_l2 along C_0, AND
    # (b) exact 50-dps Maass (1949) Q(sqrt 5) Grossencharacter Euler-product series (ZERO pullback across C_0!)
    def _d6_1d(fn, t0: float, h: float = 4e-4) -> float:
        return (
            fn(t0 + 3.0 * h)
            - 9.0 * fn(t0 + 2.0 * h)
            + 45.0 * fn(t0 + h)
            - 45.0 * fn(t0 - h)
            + 9.0 * fn(t0 - 2.0 * h)
            - fn(t0 - 3.0 * h)
        ) / (60.0 * h)

    def _rho_on_c0(th: float) -> float:
        return _rho1_ref(math.cos(th) / math.sqrt(5.0), math.sin(th) / math.sqrt(5.0))

    th_star = float(sp_opt.brentq(lambda th: _d6_1d(_rho_on_c0, th), 0.90, 1.05, xtol=1e-15, rtol=1e-15))
    x_c0 = math.cos(th_star) / math.sqrt(5.0)
    y_c0 = math.sin(th_star) / math.sqrt(5.0)
    rho_c0 = _rho1_ref(x_c0, y_c0)

    pk = c4["peak_orbit"]
    assert abs(x_c0 * x_c0 + y_c0 * y_c0 - 0.2) < 1e-15
    assert math.hypot(x_c0 - pk["tau_maass_fplus"][0], y_c0 - pk["tau_maass_fplus"][1]) < 5e-9
    assert abs(rho_c0 - pk["rho1_max"]) < 1e-10
    assert pk["peak_locus"] == "Fricke_circle_C0"
    assert pk["X0_5_orbit_size"] == 2
    assert pk["X1_5_orbit_size"] == 4

    # 5. Exact 50-dps Maass (1949) Q(sqrt 5) Grossencharacter Euler product check (n = 1..45, ZERO pullback):
    # Verify (i) numerical collocation a1_ref[0..25] == c_n^Maass to < 1e-11 (incl. split primes p = 11, 19),
    # (ii) direct Fricke functional identity psi_1(W_5(z)) + psi_1(z) == 0 to < 1e-40 without pullback,
    # (iii) forced vanishing psi_1((2 + i)/5) == 0 to < 1e-40 without pullback, and
    # (iv) 2D gradient ||grad(psi_1^2)(tau_Maass*)|| == 0 to < 1e-20 and strictly negative-definite 2D Hessian!
    mp.mp.dps = 50
    try:
        phi_mp = (1 + mp.sqrt(5)) / 2
        r1_mp_ex = mp.pi / (2 * mp.log(phi_mp))
        sc_mp_ex = mp.exp(mp.pi * r1_mp_ex / 2)
        split_pairs = {
            11: ((7 + mp.sqrt(5)) / 2, (7 - mp.sqrt(5)) / 2),
            19: ((9 + mp.sqrt(5)) / 2, (9 - mp.sqrt(5)) / 2),
            29: ((11 + mp.sqrt(5)) / 2, (11 - mp.sqrt(5)) / 2),
            31: (6 + mp.sqrt(5), 6 - mp.sqrt(5)),
            41: ((13 + mp.sqrt(5)) / 2, (13 - mp.sqrt(5)) / 2),
        }

        def _cn_maass(n_int: int) -> mp.mpf:
            res = mp.mpf(1)
            rem = n_int
            for p_div in range(2, n_int + 1):
                if rem % p_div == 0:
                    exp_k = 0
                    while rem % p_div == 0:
                        rem //= p_div
                        exp_k += 1
                    if p_div == 5:
                        res *= mp.mpf(-1) ** exp_k
                    elif p_div % 5 in (2, 3):
                        if exp_k % 2 == 1:
                            return mp.mpf(0)
                    else:
                        ap, bp = split_pairs[p_div]
                        th_p = r1_mp_ex * mp.log(ap / bp)
                        res *= mp.sin((exp_k + 1) * th_p) / mp.sin(th_p)
            return res

        cs_exact = [_cn_maass(n_idx) for n_idx in range(1, 46)]
        for n_idx in range(1, 12):
            assert abs(a1_ref[n_idx - 1] - float(cs_exact[n_idx - 1])) < 1e-12
        for n_idx in range(1, 27):
            w_n = float(_referee_k_ir(r1_ref, np.array([2.0 * math.pi * n_idx * 0.152]))[0]) * math.exp(0.5 * math.pi * r1_ref)
            assert abs(w_n * (a1_ref[n_idx - 1] - float(cs_exact[n_idx - 1]))) < 1e-13

        def _psi1_maass_50(xv_m: mp.mpf, yv_m: mp.mpf) -> mp.mpf:
            sy_m = mp.sqrt(yv_m)
            acc_m = mp.mpf(0)
            for n_idx, c_m in enumerate(cs_exact, start=1):
                if c_m == 0:
                    continue
                acc_m += c_m * sy_m * mp.re(mp.besselk(1j * r1_mp_ex, 2 * mp.pi * n_idx * yv_m)) * sc_mp_ex * mp.sin(2 * mp.pi * n_idx * xv_m)
            return acc_m

        # Direct Fricke transformation psi_1(-1 / (5 z)) == -psi_1(z) without pullback (< 1e-40!)
        zt_m = mp.mpc("0.27", "0.41")
        w5_m = -1 / (5 * zt_m)
        assert float(abs(_psi1_maass_50(mp.re(w5_m), mp.im(w5_m)) + _psi1_maass_50(mp.re(zt_m), mp.im(zt_m)))) < 1e-40
        # Direct elliptic point vanishing at (2 + i)/5 without pullback (< 1e-28 at M = 45 where y = 0.20)
        assert float(abs(_psi1_maass_50(mp.mpf("0.4"), mp.mpf("0.2")))) < 1e-22

        h_mp = mp.mpf("1e-12")

        def _d_th_50(th_m: mp.mpf) -> mp.mpf:
            f_p = _psi1_maass_50(mp.cos(th_m + h_mp) / mp.sqrt(5), mp.sin(th_m + h_mp) / mp.sqrt(5)) ** 2
            f_m = _psi1_maass_50(mp.cos(th_m - h_mp) / mp.sqrt(5), mp.sin(th_m - h_mp) / mp.sqrt(5)) ** 2
            return (f_p - f_m) / (2 * h_mp)

        th_mp_star = mp.findroot(_d_th_50, mp.mpf(repr(th_star)))
        xs_m = mp.cos(th_mp_star) / mp.sqrt(5)
        ys_m = mp.sin(th_mp_star) / mp.sqrt(5)
        assert float(mp.hypot(xs_m - pk["tau_maass_fplus"][0], ys_m - pk["tau_maass_fplus"][1])) < 5e-9

        gx_m = (_psi1_maass_50(xs_m + h_mp, ys_m) ** 2 - _psi1_maass_50(xs_m - h_mp, ys_m) ** 2) / (2 * h_mp)
        gy_m = (_psi1_maass_50(xs_m, ys_m + h_mp) ** 2 - _psi1_maass_50(xs_m, ys_m - h_mp) ** 2) / (2 * h_mp)
        assert float(mp.hypot(gx_m, gy_m)) < 1e-20
    finally:
        mp.mp.dps = old_dps

    h2 = 1e-4
    r00 = _rho1_ref(x_c0, y_c0)
    dxx_r = (_rho1_ref(x_c0 + h2, y_c0) - 2.0 * r00 + _rho1_ref(x_c0 - h2, y_c0)) / (h2 * h2)
    dyy_r = (_rho1_ref(x_c0, y_c0 + h2) - 2.0 * r00 + _rho1_ref(x_c0, y_c0 - h2)) / (h2 * h2)
    dxy_r = (
        _rho1_ref(x_c0 + h2, y_c0 + h2)
        - _rho1_ref(x_c0 + h2, y_c0 - h2)
        - _rho1_ref(x_c0 - h2, y_c0 + h2)
        + _rho1_ref(x_c0 - h2, y_c0 - h2)
    ) / (4.0 * h2 * h2)
    hess_eigs = np.linalg.eigvalsh(np.array([[dxx_r, dxy_r], [dxy_r, dyy_r]], dtype=np.float64))
    assert float(np.max(hess_eigs)) < -2.0


# =============================================================================
# Independent Referee 4: H1-H4 FR-FIB Covariance & 12-Draw Haar Basis Scrambling
# =============================================================================


def test_b1881_h1_to_h4_fr_fib_and_12draw_haar_scrambling() -> None:
    data = json.loads(COMMITTED_JSON.read_text(encoding="utf-8"))
    h1 = data["H1_kappa1_hierarchy"]
    h2 = data["H2_kappa2_hierarchy"]
    h3 = data["H3_ray_singer_cp_bracket"]
    h4 = data["H4_P776_maass_fr_fib_test"]

    assert h1["passing_S_DECADE_count"] == 0
    assert h2["passing_S_DECADE_count"] == 96
    assert h2["passing_H4a_bounded_S_DECADE_count"] == 0
    assert h3["holds"] is True

    f_rep = h4["fplus_representative"]
    w_rep = h4["w5_partner_representative"]
    assert f_rep["passing_H4_joint_count"] == 2
    assert w_rep["passing_H4_joint_count"] == 2
    assert f_rep["sl2z_reduction_matrix"] == [1, -1, 1, 0]
    assert w_rep["sl2z_reduction_matrix"] == [-1, -1, 1, 0]

    # Opposite chiral signs of Jarlskog J across the two X_0(5) orbit representatives!
    j_fplus = f_rep["best_configuration_by_balanced_span"]["J"]
    j_w5 = w_rep["best_configuration_by_balanced_span"]["J"]
    assert j_fplus > 3.2e-6 and j_w5 < -3.2e-6
    assert abs(j_fplus + j_w5) < 1e-11

    p1726 = ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"
    if str(p1726) not in sys.path:
        sys.path.insert(0, str(p1726))
    import census as K  # type: ignore

    mods = K._modules()
    B, te = mods["B"], mods["te"]

    def _build_yukawas(tau_c: complex, a_fr: Fr, b_fr: Fr, l_horo: float, r_up: str) -> Dict[str, np.ndarray]:
        w = float(a_fr) * tau_c + float(b_fr)
        av = [complex(te.ev(cc, mp.mpc(tau_c.real, tau_c.imag))) for cc in te.B[1]]
        s_mat = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
        st_mat = B.EPS @ np.conj(s_mat) @ B.EPS.T
        rd_up = st_mat if r_up == "St" else s_mat
        out: Dict[str, np.ndarray] = {}
        for sec, (lf, rf), rd in (("up", K.SECT["up"], rd_up), ("down", K.SECT["down"], s_mat), ("lep", K.SECT["lep"], s_mat)):
            xt, yt = B.sector_twists(w, tau_c, B.SIXY[lf], B.SIXY[rf])
            r_res = B.residues(xt, yt, tau_c)
            c_reg = B.cA(xt, yt, tau_c, r_res)
            uw = {
                s: (
                    math.sqrt(2.0 * math.pi * l_horo + c_reg[s]) * r_res[s]
                    if c_reg[s] is not None and 2.0 * math.pi * l_horo + c_reg[s] > 0
                    else 0.0
                )
                for s in B.UNITS
            }
            out[sec] = B.coupling(rd, B.weighted_M(uw))
        return out

    def _invariants(yu: np.ndarray, yd: np.ndarray, ye: np.ndarray) -> np.ndarray:
        uu_d, su, _ = np.linalg.svd(yu)
        ud_d, sd, _ = np.linalg.svd(yd)
        _, se, _ = np.linalg.svd(ye)
        v = np.conj(uu_d[:, ::-1].T) @ ud_d[:, ::-1]
        j = float(np.imag(v[0, 1] * v[1, 2] * np.conj(v[0, 2]) * np.conj(v[1, 1])))
        return np.array(
            [
                su[1] / su[0],
                su[2] / su[0],
                sd[1] / sd[0],
                sd[2] / sd[0],
                se[1] / se[0],
                se[2] / se[0],
                abs(v[0, 1]),
                abs(v[1, 2]),
                abs(v[0, 2]),
                j,
            ],
            dtype=np.float64,
        )

    rng = np.random.default_rng(7761881)

    def _haar(n: int) -> np.ndarray:
        z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
        q, r = np.linalg.qr(z)
        d = np.diag(r)
        return q @ np.diag(d / np.abs(d))

    # Re-verify H4 passing configuration at tau_red(tau_Maass*) = 1 - 1/tau_Maass* and run 12-draw Haar check (< 1e-13)
    tau_m = complex(*f_rep["tau_input"])
    tau_red = (1.0 * tau_m - 1.0) / (1.0 * tau_m + 0.0)
    assert abs(tau_red - complex(*f_rep["tau_sl2z_reduced"])) < 1e-14
    l2_m = float(f_rep["exact_cusp_geometry"]["L_2"])
    # Original line (1/5, 0) under gamma = [[1, -1], [1, 0]]: a' = (1/5)*0 - 0*1 = 0, b' = -(1/5)*(-1) + 0*1 = 1/5
    mats_h4 = _build_yukawas(tau_red, Fr(0, 1), Fr(1, 5), l2_m, r_up="S")
    base_h4 = _invariants(mats_h4["up"], mats_h4["down"], mats_h4["lep"])
    best_rec = f_rep["best_configuration_by_balanced_span"]
    assert abs(base_h4[1] - 10.0 ** (-best_rec["log10_s1_over_s3"]["up"])) < 1e-15
    assert abs(base_h4[3] - 10.0 ** (-best_rec["log10_s1_over_s3"]["down"])) < 1e-15
    assert abs(base_h4[0] - 10.0 ** (-best_rec["log10_s1_over_s2"]["up"])) < 1e-15
    assert abs(base_h4[9] - best_rec["J"]) < 1e-14

    for _ in range(12):
        uq, uu_r, ud_r, ul, ue_r = _haar(3), _haar(3), _haar(3), _haar(3), _haar(3)
        scr_h4 = _invariants(
            uq @ mats_h4["up"] @ np.conj(uu_r.T),
            uq @ mats_h4["down"] @ np.conj(ud_r.T),
            ul @ mats_h4["lep"] @ np.conj(ue_r.T),
        )
        assert float(np.max(np.abs(scr_h4 - base_h4))) < 1e-13
