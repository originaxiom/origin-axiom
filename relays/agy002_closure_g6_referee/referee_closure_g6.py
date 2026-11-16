#!/usr/bin/env python3
"""Independent Cold-Room Zero-Trust Referee for Gate 6 (CLOSURE-G6 + ERRATUM).

Enforces Guardrails 1-6:
  - Zero repository imports (stdlib + numpy + scipy only).
  - Zero float literals and zero complex literals in source (AST-enforced).
  - Literature Benchmark Gates (Buttazzo et al. arXiv:1307.3536; Antusch et al. hep-ph/0108005)
    verified before running model UV boundary conditions.
  - Independent construction from primary literature:
      * Cremades-Ibanez-Marchesano (JHEP 0405 (2004) 079, hep-th/0404229)
      * Weinberg (Phys. Rev. Lett. 43 (1979) 1566); Antusch et al. (hep-ph/0108005)
      * Machacek-Vaughn (Nucl. Phys. B 222, 236, 249 (1983-1985))
      * Luo-Xiao (Phys. Rev. Lett. 90 (2003) 011601, hep-ph/0207271)
      * Bednyakov-Pikelner-Velizhanin (arXiv:1212.6829, 1303.4364, 1406.7171)
  - Verifies Sections 1, 2, 3, the Bergman rank-1 reproducing-kernel erratum diagnosis,
    all 5 Planted Fault Controls (PF6.1..PF6.5), and byte-for-byte SHA256 manifests.
"""

from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import spence

IMAG_I = complex(0, 1)
ALLOWED_TOP_IMPORTS = frozenset({
    "__future__",
    "ast",
    "fractions",
    "hashlib",
    "json",
    "math",
    "numpy",
    "pathlib",
    "scipy",
    "sys",
    "time",
})


def rat(num: int, den: int = 1) -> float:
    """Convert exact integer ratio to IEEE-754 binary64 without float literals."""
    return float(Fraction(num, den))


def pow10_neg(exp_pos: int) -> float:
    """Return 10**(-exp_pos) from integer arithmetic without float literals."""
    return float(Fraction(1, 10 ** exp_pos))


def audit_own_ast_and_manifests(script_path: Path, repo_root: Path) -> dict:
    """Enforce zero float/complex literals, zero repo imports, and verify producer SHA256 manifests."""
    source_bytes = script_path.read_bytes()
    own_sha256 = hashlib.sha256(source_bytes).hexdigest()
    tree = ast.parse(source_bytes.decode("utf-8"), filename=str(script_path))

    float_literals = []
    complex_literals = []
    disallowed_imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals.append((node.lineno, repr(node.value)))
            elif isinstance(node.value, complex):
                complex_literals.append((node.lineno, repr(node.value)))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                top = alias.name.split(".")[0]
                if top not in ALLOWED_TOP_IMPORTS:
                    disallowed_imports.append((node.lineno, alias.name))
        elif isinstance(node, ast.ImportFrom):
            top = (node.module or "").split(".")[0]
            if node.level != 0 or top not in ALLOWED_TOP_IMPORTS:
                disallowed_imports.append((node.lineno, f"{'.' * node.level}{node.module}"))

    manifest_relpaths = [
        "relays/agy002_closure_g6/SCRIPT_SHA256.txt",
        "relays/agy002_closure_g6/OUTPUT_SHA256.txt",
        "relays/agy002_closure_g6_fixed/SCRIPT_SHA256.txt",
        "relays/agy002_closure_g6_fixed/OUTPUT_SHA256.txt",
    ]
    manifest_checks = {}
    all_manifests_ok = True
    for m_rel in manifest_relpaths:
        m_path = repo_root / m_rel
        line = m_path.read_text(encoding="utf-8").strip()
        expected_hex, target_rel = line.split()
        actual_hex = hashlib.sha256((repo_root / target_rel).read_bytes()).hexdigest()
        matched = (expected_hex == actual_hex)
        all_manifests_ok = all_manifests_ok and matched
        manifest_checks[m_rel] = {
            "target": target_rel,
            "expected_sha256": expected_hex,
            "actual_sha256": actual_hex,
            "byte_for_byte_match": matched,
        }

    ast_clean = (len(float_literals) == 0) and (len(complex_literals) == 0) and (len(disallowed_imports) == 0)
    return {
        "referee_script_sha256": own_sha256,
        "float_literal_count": len(float_literals),
        "complex_literal_count": len(complex_literals),
        "disallowed_import_count": len(disallowed_imports),
        "ast_zero_float_zero_complex_zero_repo_import": ast_clean,
        "producer_manifests_verified_count": len(manifest_checks),
        "all_producer_manifests_match": all_manifests_ok,
        "producer_manifests": manifest_checks,
        "passed": bool(ast_clean and all_manifests_ok),
    }


# ============================================================================
# SECTION 1: Magnetized Torus CIM Overlaps, (J_0, J_1, J_2), Seesaw & PF6.1
# ============================================================================

def jacobi_theta_point(a_char: float, b_char: float, nu: complex, tau_tilde: complex, n_trunc: int = 18) -> complex:
    """Mumford/CIM theta with characteristics sum_n exp(pi i (n+a)^2 tau_tilde + 2 pi i (n+a)(nu + b))."""
    ns = np.arange(-n_trunc, n_trunc + 1, dtype=np.int64)
    na = ns + a_char
    expo = IMAG_I * math.pi * (na * na) * tau_tilde + (2 * math.pi * IMAG_I) * na * (nu + b_char)
    return complex(np.sum(np.exp(expo)))


def cim_psi_point(flux_m: int, alpha: float, beta: float, z: complex, tau: complex, n_trunc: int = 18) -> np.ndarray:
    """CIM hep-th/0404229 eq. (3.13) normalized magnetized torus wavefunctions at point z (Wilson line 0)."""
    im_tau = tau.imag
    norm = (2 * flux_m * im_tau) ** Fraction(1, 4)
    pref = norm * np.exp(IMAG_I * math.pi * flux_m * z * (z.imag / im_tau))
    vals = np.zeros(flux_m, dtype=np.complex128)
    for j in range(flux_m):
        a_char = (j + alpha) / flux_m
        vals[j] = pref * jacobi_theta_point(a_char, -beta, flux_m * z, flux_m * tau, n_trunc=n_trunc)
    return vals


def cim_yukawa_analytic(tau: complex, n_trunc: int = 18) -> np.ndarray:
    """Exact CIM hep-th/0404229 Sec. 5.1 analytic overlap Y_cim(tau; 0, 0) for flux (3, 3, -6)
    with spin structures ((1/2, 1/2), (1/2, 1/2), (0, 0)).
    """
    pref = (3 * tau.imag) ** Fraction(1, 4)
    y0 = np.zeros((3, 3, 6), dtype=np.complex128)
    six_tau = 6 * tau
    for i in range(3):
        for j in range(3):
            for k in range(6):
                if (k - i - j - 1) % 3 == 0:
                    a_char = rat(k - 2 * j - 1, 6)
                    phase = np.exp(-IMAG_I * math.pi * rat(k, 3))
                    y0[i, j, k] = pref * phase * jacobi_theta_point(a_char, 0, complex(0, 0), six_tau, n_trunc=n_trunc)
    return y0


def cim_yukawa_quadrature_check(tau: complex, n_grid: int = 48, n_trunc: int = 16) -> dict:
    """Independent 2D spectral torus quadrature on T^2 = C / (Z + tau Z) to cross-check Y_cim(tau; 0, 0)."""
    half = rat(1, 2)
    im_tau = tau.imag
    coords = np.arange(n_grid, dtype=np.int64) / n_grid
    z_grid = coords[:, None] + tau * coords[None, :]
    ns = np.arange(-n_trunc, n_trunc + 1, dtype=np.int64)

    def eval_grid(flux_m: int, alpha: float, beta: float) -> np.ndarray:
        norm = (2 * flux_m * im_tau) ** Fraction(1, 4)
        pref = norm * np.exp(IMAG_I * math.pi * flux_m * z_grid * coords[None, :])
        mz = flux_m * z_grid
        mtau = flux_m * tau
        out = np.zeros((flux_m, n_grid, n_grid), dtype=np.complex128)
        for j in range(flux_m):
            a_c = (j + alpha) / flux_m
            na = ns[:, None, None] + a_c
            expo = IMAG_I * math.pi * (na * na) * mtau + (2 * math.pi * IMAG_I) * na * (mz - beta)
            out[j] = pref * np.sum(np.exp(expo), axis=0)
        return out

    psi3 = eval_grid(3, half, half)
    psi6 = eval_grid(6, 0, 0)
    w_cell = rat(1, n_grid * n_grid)
    gram3 = np.einsum("ixy,jxy->ij", np.conj(psi3), psi3) * w_cell
    gram6 = np.einsum("kxy,lxy->kl", np.conj(psi6), psi6) * w_cell
    y0_quad = np.einsum("ixy,jxy,kxy->ijk", psi3, psi3, np.conj(psi6)) * w_cell
    return {
        "Y0_quad": y0_quad,
        "orthonorm_err_3": float(np.linalg.norm(gram3 - np.eye(3))),
        "orthonorm_err_6": float(np.linalg.norm(gram6 - np.eye(6))),
    }


def build_cim_majorana_triple(tau: complex) -> dict:
    """Construct cutoff-free Y_0(tau), v_0(tau), G_6(tau), v_1(tau), and (J_0, J_1, J_2) at modulus tau."""
    half = rat(1, 2)
    y0_tensor = cim_yukawa_analytic(tau)
    v0_vec = cim_psi_point(6, 0, 0, complex(0, 0), tau)
    u3_zero = cim_psi_point(3, half, half, complex(0, 0), tau)

    y0_mat = y0_tensor.reshape(9, 6)
    g6_gram = y0_mat.conj().T @ y0_mat
    v1_vec = g6_gram @ v0_vec

    j0 = np.einsum("ijk,k->ij", y0_tensor, v0_vec)
    j1 = np.einsum("ijk,k->ij", y0_tensor, v1_vec)
    j2 = j1 @ j1.conj().T @ j1

    return {
        "Y0": y0_tensor,
        "v0": v0_vec,
        "v1": v1_vec,
        "G6": g6_gram,
        "J0": j0,
        "J1": j1,
        "J2": j2,
        "u3_zero": u3_zero,
    }


def modular_u3_T() -> np.ndarray:
    """Exact unitary representation U_3(T) on psi^{(3)} with spin (1/2, 1/2)."""
    half = rat(1, 2)
    js = np.arange(3, dtype=np.int64)
    return np.diag(np.exp(IMAG_I * math.pi * ((js + half) ** 2) / 3))


def modular_u3_S(tau: complex) -> np.ndarray:
    """Exact unitary representation U_3(S; tau) on psi^{(3)} with spin (1/2, 1/2) (CIM -beta convention)."""
    half = rat(1, 2)
    phi_s = ((-IMAG_I * tau) / abs(tau)) ** half
    s_mat = np.zeros((3, 3), dtype=np.complex128)
    inv_rt3 = 1 / math.sqrt(3)
    for j in range(3):
        for k in range(3):
            ang = (math.pi / 3) * (-2 * j * k - 2 * j - half)
            s_mat[j, k] = np.exp(IMAG_I * ang) * inv_rt3
    return phi_s * s_mat


def takagi_direct_svd(sym_mat: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Direct-SVD Autonne-Takagi factorization M = U diag(s) U^T without squaring condition number.
    Returns (s_asc, U_asc) sorted in ascending singular-value order.
    """
    u_left, s_desc, _ = np.linalg.svd(sym_mat)
    proj_diag = np.diag(u_left.conj().T @ sym_mat @ u_left.conj())
    safe_s = np.maximum(s_desc, pow10_neg(30))
    half_phases = np.sqrt(proj_diag / safe_s)
    u_tak_desc = u_left * half_phases[None, :]
    order = np.argsort(s_desc)
    return s_desc[order], u_tak_desc[:, order]


def haar_unitary(rng: np.random.Generator, dim: int = 3) -> np.ndarray:
    """Sample exact Haar-distributed unitary matrix in U(dim) via Mezzadri QR algorithm."""
    z = (rng.standard_normal((dim, dim)) + IMAG_I * rng.standard_normal((dim, dim))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    diag_r = np.diag(r)
    phases = diag_r / np.abs(diag_r)
    return q * phases[None, :]


def frobenius_orthonormalize(tensors: list[np.ndarray]) -> list[np.ndarray]:
    """Gram-Schmidt orthonormalization under Frobenius inner product <A, B>_F = Tr(A^dag B)."""
    ortho = []
    for mat in tensors:
        work = mat.copy()
        for prev in ortho:
            work = work - np.vdot(prev, work) * prev
        norm = math.sqrt(float(np.vdot(work, work).real))
        ortho.append(work / norm)
    return ortho


def verify_section1() -> dict:
    """Verify Section 1, independent 2D torus quadrature cross-check, Erratum diagnosis, and PF6.1."""
    tau = rat(1, 5) + IMAG_I * rat(6, 5)
    data = build_cim_majorana_triple(tau)
    quad_check = cim_yukawa_quadrature_check(tau, n_grid=48)
    analytic_vs_quad_err = float(np.linalg.norm(data["Y0"] - quad_check["Y0_quad"]))
    j_list = [data["J0"], data["J1"], data["J2"]]

    # 1. Bergman reproducing kernel check: J_0 == psi^{(3)}(0) psi^{(3)}(0)^T (exact rank 1)
    repro_outer = np.outer(data["u3_zero"], data["u3_zero"])
    bergman_repro_err = float(np.linalg.norm(data["J0"] - repro_outer))

    sym_errs = [float(np.linalg.norm(j - j.T)) for j in j_list]
    max_sym_err = max(sym_errs)
    svs_each = [np.linalg.svd(j, compute_uv=False) for j in j_list]
    ranks = [int(np.sum(sv > pow10_neg(10))) for sv in svs_each]

    # 2. T and S modular covariance: J_a(gamma tau) = U_3(gamma) J_a(tau) U_3(gamma)^T
    data_t = build_cim_majorana_triple(tau + 1)
    data_s = build_cim_majorana_triple(-1 / tau)
    u_t = modular_u3_T()
    u_s = modular_u3_S(tau)
    unitarity_err = max(
        float(np.linalg.norm(u_t @ u_t.conj().T - np.eye(3))),
        float(np.linalg.norm(u_s @ u_s.conj().T - np.eye(3))),
    )
    t_cov_errs = [
        float(np.linalg.norm(jt - u_t @ j @ u_t.T))
        for jt, j in zip([data_t["J0"], data_t["J1"], data_t["J2"]], j_list)
    ]
    s_cov_errs = [
        float(np.linalg.norm(js - u_s @ j @ u_s.T))
        for js, j in zip([data_s["J0"], data_s["J1"], data_s["J2"]], j_list)
    ]
    max_t_cov_err = max(t_cov_errs)
    max_s_cov_err = max(s_cov_errs)

    # 3. Span rank 3 in Sym^2(C^3) (isometric 6D symmetric coordinates)
    rt2 = math.sqrt(2)
    sym6_rows = np.vstack([
        np.array([j[0, 0], j[1, 1], j[2, 2], rt2 * j[0, 1], rt2 * j[0, 2], rt2 * j[1, 2]])
        for j in j_list
    ])
    span_svs = np.linalg.svd(sym6_rows, compute_uv=False)
    span_rank_sym2 = int(np.sum(span_svs > pow10_neg(8)))

    # 4. Complex CP^2 relative-phase sensitivity of sv_2 / sv_3 (fixed |c_a| = 1, varying phases)
    e0, e1, e2 = frobenius_orthonormalize(j_list)
    gram_ortho_err = max(
        abs(np.vdot(ea, eb) - (1 if ia == ib else 0))
        for ia, ea in enumerate([e0, e1, e2])
        for ib, eb in enumerate([e0, e1, e2])
    )
    sv_real_sum = np.linalg.svd(e0 + e1 + e2, compute_uv=False)
    phase_1 = IMAG_I
    phase_2 = complex(rat(-3, 5), rat(4, 5))
    sv_phased_sum = np.linalg.svd(e0 + phase_1 * e1 + phase_2 * e2, compute_uv=False)
    cp2_shift_desc = abs(float(sv_real_sum[1] / sv_real_sum[2] - sv_phased_sum[1] / sv_phased_sum[2]))
    cp2_shift_asc = abs(float(sv_real_sum[1] / sv_real_sum[0] - sv_phased_sum[1] / sv_phased_sum[0]))
    cp2_phase_shift = min(cp2_shift_desc, cp2_shift_asc)

    # 5. PF6.1: SO(3) basis rotation on Frobenius-orthonormalized (E_0, E_1, E_2)
    rot_x = np.array([
        [1, 0, 0],
        [0, rat(3, 5), rat(-4, 5)],
        [0, rat(4, 5), rat(3, 5)],
    ], dtype=np.float64)
    rot_z = np.array([
        [rat(3, 5), rat(-4, 5), 0],
        [rat(4, 5), rat(3, 5), 0],
        [0, 0, 1],
    ], dtype=np.float64)
    so3_mat = rot_x @ rot_z
    so3_orth_err = float(np.linalg.norm(so3_mat @ so3_mat.T - np.eye(3)))
    so3_det_err = abs(float(np.linalg.det(so3_mat)) - 1)
    e_rot = [sum(so3_mat[a, b] * [e0, e1, e2][b] for b in range(3)) for a in range(3)]
    sv_rot_sum = np.linalg.svd(e_rot[0] + e_rot[1] + e_rot[2], compute_uv=False)
    pf61_shift_desc = abs(float(sv_real_sum[1] / sv_real_sum[2] - sv_rot_sum[1] / sv_rot_sum[2]))
    pf61_shift_asc = abs(float(sv_real_sum[1] / sv_real_sum[0] - sv_rot_sum[1] / sv_rot_sum[0]))

    # 6. 10-trial U(3)^6 Haar basis-scrambling invariance (Guardrail 3 + Erratum verification)
    tau_u = rat(1, 9) + IMAG_I * rat(21, 20)
    tau_d = rat(2, 9) + IMAG_I * rat(23, 20)
    tau_e = rat(1, 7) + IMAG_I * rat(11, 10)
    tau_nu = rat(2, 7) + IMAG_I * rat(13, 10)

    d_u = build_cim_majorana_triple(tau_u)
    d_d = build_cim_majorana_triple(tau_d)
    d_e = build_cim_majorana_triple(tau_e)
    d_nu = build_cim_majorana_triple(tau_nu)

    y_u = d_u["J1"]
    y_d = d_d["J1"]
    y_e = d_e["J1"]
    y_nu = d_nu["J1"]
    m_r = data["J0"] + rat(1, 2) * data["J1"] + complex(rat(3, 10), rat(2, 5)) * data["J2"]

    kap_0 = y_nu @ np.linalg.solve(m_r, y_nu.T)
    tak_err_0 = float(np.linalg.norm(kap_0 - kap_0.T))
    u_ql_0, sv_u_0, _ = np.linalg.svd(y_u)
    u_dl_0, sv_d_0, _ = np.linalg.svd(y_d)
    v_ckm_0 = u_ql_0.conj().T @ u_dl_0
    j_ckm_0 = float(np.imag(v_ckm_0[0, 1] * v_ckm_0[1, 2] * np.conj(v_ckm_0[0, 2]) * np.conj(v_ckm_0[1, 1])))

    u_el_0, sv_e_0, _ = np.linalg.svd(y_e)
    sv_kap_0, u_nu_0 = takagi_direct_svd(kap_0)
    tak_recon_err = float(np.linalg.norm(kap_0 - u_nu_0 @ np.diag(sv_kap_0) @ u_nu_0.T))
    u_pmns_0 = u_el_0.conj().T @ u_nu_0
    j_pmns_0 = float(np.imag(u_pmns_0[0, 0] * u_pmns_0[1, 1] * np.conj(u_pmns_0[0, 1]) * np.conj(u_pmns_0[1, 0])))

    rng = np.random.default_rng(20261116)
    max_haar_drift = rat(0)
    for _ in range(10):
        u_q = haar_unitary(rng)
        u_ur = haar_unitary(rng)
        u_dr = haar_unitary(rng)
        u_l = haar_unitary(rng)
        u_er = haar_unitary(rng)
        u_nr = haar_unitary(rng)

        y_u_scr = u_q @ y_u @ u_ur.conj().T
        y_d_scr = u_q @ y_d @ u_dr.conj().T
        y_e_scr = u_l @ y_e @ u_er.conj().T
        y_nu_scr = u_l @ y_nu @ u_nr.conj().T
        m_r_scr = u_nr.conj() @ m_r @ u_nr.conj().T

        u_ql_s, sv_u_s, _ = np.linalg.svd(y_u_scr)
        u_dl_s, sv_d_s, _ = np.linalg.svd(y_d_scr)
        v_ckm_s = u_ql_s.conj().T @ u_dl_s
        j_ckm_s = float(np.imag(v_ckm_s[0, 1] * v_ckm_s[1, 2] * np.conj(v_ckm_s[0, 2]) * np.conj(v_ckm_s[1, 1])))

        kap_s = y_nu_scr @ np.linalg.solve(m_r_scr, y_nu_scr.T)
        u_el_s, sv_e_s, _ = np.linalg.svd(y_e_scr)
        sv_kap_s, u_nu_s = takagi_direct_svd(kap_s)
        u_pmns_s = u_el_s.conj().T @ u_nu_s
        j_pmns_s = float(np.imag(u_pmns_s[0, 0] * u_pmns_s[1, 1] * np.conj(u_pmns_s[0, 1]) * np.conj(u_pmns_s[1, 0])))

        trial_drift = max(
            float(np.max(np.abs(sv_u_s - sv_u_0))),
            float(np.max(np.abs(sv_d_s - sv_d_0))),
            float(np.max(np.abs(np.abs(v_ckm_s) - np.abs(v_ckm_0)))),
            abs(j_ckm_s - j_ckm_0),
            float(np.max(np.abs(sv_e_s - sv_e_0))),
            float(np.max(np.abs(sv_kap_s - sv_kap_0))),
            float(np.max(np.abs(np.abs(u_pmns_s) - np.abs(u_pmns_0)))),
            abs(j_pmns_s - j_pmns_0),
        )
        max_haar_drift = max(max_haar_drift, trial_drift)

    # Erratum negative control: rank-1 v_0 contraction has 2D nullspace => |U_PMNS| drifts O(1) under U(3)
    y_e_rank1 = d_e["J0"]
    y_nu_rank1 = d_nu["J0"]
    kap_r1_0 = y_nu_rank1 @ np.linalg.solve(m_r, y_nu_rank1.T)
    u_el_r1_0, _, _ = np.linalg.svd(y_e_rank1)
    _, u_nu_r1_0 = takagi_direct_svd(kap_r1_0)
    pmns_r1_0 = np.abs(u_el_r1_0.conj().T @ u_nu_r1_0)

    u_l_test = haar_unitary(rng)
    u_er_test = haar_unitary(rng)
    u_nr_test = haar_unitary(rng)
    y_e_r1_s = u_l_test @ y_e_rank1 @ u_er_test.conj().T
    y_nu_r1_s = u_l_test @ y_nu_rank1 @ u_nr_test.conj().T
    m_r_r1_s = u_nr_test.conj() @ m_r @ u_nr_test.conj().T
    kap_r1_s = y_nu_r1_s @ np.linalg.solve(m_r_r1_s, y_nu_r1_s.T)
    u_el_r1_s, _, _ = np.linalg.svd(y_e_r1_s)
    _, u_nu_r1_s = takagi_direct_svd(kap_r1_s)
    pmns_r1_s = np.abs(u_el_r1_s.conj().T @ u_nu_r1_s)
    erratum_rank1_nullspace_drift = float(np.max(np.abs(pmns_r1_s - pmns_r1_0)))

    sec1_passed = bool(
        analytic_vs_quad_err < pow10_neg(14)
        and quad_check["orthonorm_err_3"] < pow10_neg(14)
        and quad_check["orthonorm_err_6"] < pow10_neg(14)
        and max_sym_err < pow10_neg(14)
        and bergman_repro_err < pow10_neg(14)
        and ranks == [1, 3, 3]
        and unitarity_err < pow10_neg(14)
        and max_t_cov_err < pow10_neg(12)
        and max_s_cov_err < pow10_neg(12)
        and span_rank_sym2 == 3
        and cp2_shift_desc > rat(1, 200)
        and cp2_shift_asc > rat(1, 200)
        and max_haar_drift < pow10_neg(13)
        and erratum_rank1_nullspace_drift > rat(1, 20)
    )
    pf61_passed = bool(
        so3_orth_err < pow10_neg(14)
        and so3_det_err < pow10_neg(14)
        and pf61_shift_desc > rat(1, 10)
        and pf61_shift_asc > rat(1, 10)
    )

    return {
        "modulus_tau": [tau.real, tau.imag],
        "analytic_vs_48x48_torus_quadrature_err": analytic_vs_quad_err,
        "torus_orthonormality_err_3_6": [quad_check["orthonorm_err_3"], quad_check["orthonorm_err_6"]],
        "bergman_reproducing_rank1_err": bergman_repro_err,
        "symmetry_max_err": max_sym_err,
        "ranks_J0_J1_J2": ranks,
        "modular_T_max_err": max_t_cov_err,
        "modular_S_max_err": max_s_cov_err,
        "span_rank_in_Sym2_C3": span_rank_sym2,
        "span_singular_values": [float(x) for x in span_svs],
        "frobenius_gram_ortho_err": float(gram_ortho_err),
        "cp2_phase_shift_sv2_over_sv3_desc": cp2_shift_desc,
        "cp2_phase_shift_sv2_over_sv3_asc": cp2_shift_asc,
        "cp2_phase_shift_min": cp2_phase_shift,
        "honest_majorana_parameter_ledger": {
            "general_complex_tau_real_projective_ratios": 4,
            "cp_real_Re_tau_eq_0_real_projective_ratios": 2,
            "overall_scale_M0_over_vEW": 1,
        },
        "seesaw_takagi_symmetry_and_recon_err": [tak_err_0, tak_recon_err],
        "haar_U3_pow_6_10trials_max_drift": max_haar_drift,
        "erratum_rank1_v0_nullspace_drift_confirmed": erratum_rank1_nullspace_drift,
        "PF6_1_orthonormal_so3_shift_desc": pf61_shift_desc,
        "PF6_1_orthonormal_so3_shift_asc": pf61_shift_asc,
        "PF6_1_caught": pf61_passed,
        "passed": bool(sec1_passed and pf61_passed),
    }


# ============================================================================
# SECTION 2: Z_2-TM1 Sum Rule, Weinberg + SM Downward RGE & PF6.2
# ============================================================================

def build_tm1_uv_operator(nh_masses: tuple[float, float, float], swap_tm2: bool = False) -> tuple[np.ndarray, np.ndarray]:
    """Construct Z_2-TM1 (or PF6.2 swapped TM2) Weinberg operator kappa_UV at |U_{e3}|^2 = 1/48."""
    u1 = np.array([2, -1, -1], dtype=np.complex128) / math.sqrt(6)
    u2 = np.array([1, 1, 1], dtype=np.complex128) / math.sqrt(3)
    u3 = np.array([0, 1, -1], dtype=np.complex128) / math.sqrt(2)
    base = np.column_stack([u2, u1, u3]) if swap_tm2 else np.column_stack([u1, u2, u3])

    s_th = rat(1, 4)
    c_th = math.sqrt(15) / 4
    exp_id = complex(rat(3, 5), rat(4, 5))
    rot_23 = np.array([
        [1, 0, 0],
        [0, c_th, s_th * np.conj(exp_id)],
        [0, -s_th * exp_id, c_th],
    ], dtype=np.complex128)
    u_pmns_uv = base @ rot_23
    kap_uv = u_pmns_uv @ np.diag(np.array(nh_masses, dtype=np.complex128)) @ u_pmns_uv.T
    s_z2 = 2 * np.outer(u1, u1) - np.eye(3, dtype=np.complex128)
    return kap_uv, s_z2


def verify_section2_and_weinberg_benchmark() -> dict:
    """Verify Antusch et al. analytical RGE benchmark (Guardrail 4), Section 2 TM1 corridor, and PF6.2."""
    dt_span = -30
    target_tm1 = rat(2, 3)
    target_ue3_sq = rat(1, 48)

    nh_spectra = [
        ("hierarchical_NH", (rat(1, 100), rat(9, 50), rat(1, 1))),
        ("moderate_NH", (rat(1, 20), rat(1, 5), rat(1, 1))),
    ]
    ytau_grid = [rat(1, 100), rat(1, 20), rat(1, 5)]

    kap_uv_0, s_z2 = build_tm1_uv_operator(nh_spectra[0][1], swap_tm2=False)
    z2_inv_err = float(np.linalg.norm(s_z2 @ kap_uv_0 @ s_z2.T - kap_uv_0))
    _, u_uv_0 = takagi_direct_svd(kap_uv_0)
    i_tm1_uv = float(abs(u_uv_0[0, 0]) ** 2)
    ue3_sq_uv = float(abs(u_uv_0[0, 2]) ** 2)
    j_pmns_uv = abs(float(np.imag(u_uv_0[0, 0] * u_uv_0[1, 1] * np.conj(u_uv_0[0, 1]) * np.conj(u_uv_0[1, 0]))))
    uv_tm1_err = abs(i_tm1_uv - target_tm1)
    uv_ue3_err = abs(ue3_sq_uv - target_ue3_sq)

    # Guardrail 4 Literature Benchmark: Antusch et al. (hep-ph/0108005) eq. (17) exact analytical integral
    ye_bench = np.array([rat(1, 100000), rat(1, 1000), rat(1, 5)], dtype=np.float64)
    he_bench = np.diag(ye_bench * ye_bench)
    g2_b, yt_b, lam_b = rat(3, 5), rat(7, 10), rat(1, 8)
    alpha_kap_b = -3 * (g2_b ** 2) + 4 * lam_b + 2 * (3 * (yt_b ** 2) + float(np.sum(ye_bench ** 2)))
    inv16pi2 = 1 / (16 * (math.pi ** 2))

    def rhs_static(_t: float, y_flat: np.ndarray) -> np.ndarray:
        k_mat = y_flat.view(np.complex128).reshape(3, 3)
        dk = inv16pi2 * (rat(-3, 2) * (k_mat @ he_bench + he_bench @ k_mat) + alpha_kap_b * k_mat)
        return dk.reshape(-1).view(np.float64)

    sol_bench = solve_ivp(
        rhs_static,
        (0, dt_span),
        kap_uv_0.copy().reshape(-1).view(np.float64),
        method="DOP853",
        rtol=pow10_neg(12),
        atol=pow10_neg(14),
    )
    kap_num = sol_bench.y[:, -1].view(np.complex128).reshape(3, 3)
    i_factors = np.exp(inv16pi2 * rat(-3, 2) * (ye_bench * ye_bench) * dt_span)
    kap_exact = math.exp(inv16pi2 * alpha_kap_b * dt_span) * (i_factors[:, None] * kap_uv_0 * i_factors[None, :])
    weinberg_benchmark_err = float(np.linalg.norm(kap_num - kap_exact) / np.linalg.norm(kap_exact))

    corridor_records = []
    max_excursion_all = rat(0)
    max_excursion_small_ytau = rat(0)

    for spec_name, masses in nh_spectra:
        kap_uv, _ = build_tm1_uv_operator(masses, swap_tm2=False)
        for y_tau in ytau_grid:
            g1_0 = math.sqrt(4 * math.pi / 60)
            g2_0 = g1_0
            g3_0 = g1_0
            yt_0 = rat(7, 10)
            lam_0 = rat(1, 8)
            ye_vec0 = np.array([rat(1, 100000), rat(1, 1000), y_tau], dtype=np.float64)

            state0 = np.concatenate([
                np.array([g1_0, g2_0, g3_0, yt_0, lam_0], dtype=np.float64),
                ye_vec0,
                kap_uv.reshape(-1).view(np.float64),
            ])

            def rhs_coupled(_t: float, st: np.ndarray) -> np.ndarray:
                g1, g2, g3, yt, lam = st[0], st[1], st[2], st[3], st[4]
                ye_v = st[5:8]
                k_m = st[8:26].view(np.complex128).reshape(3, 3)
                tr_y = 3 * (yt * yt) + float(np.sum(ye_v * ye_v))
                dg1 = inv16pi2 * rat(41, 10) * (g1 ** 3)
                dg2 = inv16pi2 * rat(-19, 6) * (g2 ** 3)
                dg3 = inv16pi2 * (-7) * (g3 ** 3)
                dyt = inv16pi2 * yt * (rat(3, 2) * (yt * yt) + tr_y - (rat(17, 20) * g1 * g1 + rat(9, 4) * g2 * g2 + 8 * g3 * g3))
                dye = inv16pi2 * ye_v * (rat(3, 2) * (ye_v * ye_v) + tr_y - rat(9, 4) * (g1 * g1 + g2 * g2))
                dlam = inv16pi2 * (
                    24 * lam * lam - (rat(9, 5) * g1 * g1 + 9 * g2 * g2) * lam
                    + rat(27, 200) * (g1 ** 4) + rat(9, 20) * g1 * g1 * g2 * g2 + rat(9, 8) * (g2 ** 4)
                    + 4 * tr_y * lam - 2 * (3 * (yt ** 4) + float(np.sum(ye_v ** 4)))
                )
                he_mat = np.diag(ye_v * ye_v)
                a_kap = -3 * g2 * g2 + 4 * lam + 2 * tr_y
                dk = inv16pi2 * (rat(-3, 2) * (k_m @ he_mat + he_mat @ k_m) + a_kap * k_m)
                return np.concatenate([
                    np.array([dg1, dg2, dg3, dyt, dlam], dtype=np.float64),
                    dye,
                    dk.reshape(-1).view(np.float64),
                ])

            sol_ir = solve_ivp(rhs_coupled, (0, dt_span), state0, method="DOP853", rtol=pow10_neg(12), atol=pow10_neg(14))
            kap_ir = sol_ir.y[8:26, -1].view(np.complex128).reshape(3, 3)
            _, u_ir = takagi_direct_svd(kap_ir)
            i_tm1_ir = float(abs(u_ir[0, 0]) ** 2)
            excursion = abs(i_tm1_ir - target_tm1)
            max_excursion_all = max(max_excursion_all, excursion)
            if y_tau <= rat(1, 20):
                max_excursion_small_ytau = max(max_excursion_small_ytau, excursion)
            corridor_records.append({
                "spectrum": spec_name,
                "y_tau_uv": y_tau,
                "I_TM1_IR": i_tm1_ir,
                "abs_diff_from_2_over_3": excursion,
            })

    # PF6.2: TM2 column swap falsifier (u_2 = (1,1,1)^T / sqrt(3) in column 1)
    kap_tm2_swap, _ = build_tm1_uv_operator(nh_spectra[0][1], swap_tm2=True)
    _, u_bad = takagi_direct_svd(kap_tm2_swap)
    i_tm1_bad = float(abs(u_bad[0, 0]) ** 2)
    pf62_violation = abs(i_tm1_bad - target_tm1)
    pf62_caught = bool(pf62_violation > rat(1, 4))

    sec2_passed = bool(
        weinberg_benchmark_err < pow10_neg(12)
        and z2_inv_err < pow10_neg(14)
        and uv_tm1_err < pow10_neg(14)
        and uv_ue3_err < pow10_neg(14)
        and j_pmns_uv > rat(1, 100)
        and max_excursion_all < rat(1, 200)
        and max_excursion_small_ytau < rat(1, 2000)
        and pf62_caught
    )

    return {
        "weinberg_rge_analytic_benchmark_rel_err": weinberg_benchmark_err,
        "uv_z2_invariance_err": z2_inv_err,
        "I_TM1_UV": i_tm1_uv,
        "I_TM1_UV_abs_err": uv_tm1_err,
        "Ue3_sq_UV": ue3_sq_uv,
        "Ue3_sq_UV_abs_err": uv_ue3_err,
        "abs_J_PMNS_UV": j_pmns_uv,
        "max_IR_excursion_all_ytau": max_excursion_all,
        "max_IR_excursion_ytau_le_1_over_20": max_excursion_small_ytau,
        "corridor_runs": corridor_records,
        "PF6_2_tm2_swap_I_TM1": i_tm1_bad,
        "PF6_2_abs_diff_from_2_over_3": pf62_violation,
        "PF6_2_caught": pf62_caught,
        "passed": sec2_passed,
    }


# ============================================================================
# SECTION 3: 243-History Pati-Salam x Z2^D 2-Loop IR Surfaces & PF6.3..PF6.5
# ============================================================================

def sm_2loop_rhs_batch(
    g1: np.ndarray,
    g2: np.ndarray,
    g3: np.ndarray,
    lam: np.ndarray,
    yu: np.ndarray,
    yd: np.ndarray,
    ye: np.ndarray,
    n_g: int = 3,
    c_lam2_try: int = -48,
) -> tuple[np.ndarray, ...]:
    """Full 3-family matrix 2-loop SM beta functions (Machacek-Vaughn, Luo-Xiao 0207271, BPV 2014).
    Potential convention: V = -m^2 |H|^2 + lambda |H|^4 (m_H / v_EW = sqrt(2 lambda)).
    """
    g1_2, g2_2, g3_2 = g1 * g1, g2 * g2, g3 * g3
    g1_4, g2_4, g3_4 = g1_2 * g1_2, g2_2 * g2_2, g3_2 * g3_2
    g1_6, g2_6 = g1_4 * g1_2, g2_4 * g2_2

    cu = np.conj(np.swapaxes(yu, -1, -2)) @ yu
    cd = np.conj(np.swapaxes(yd, -1, -2)) @ yd
    ce = np.conj(np.swapaxes(ye, -1, -2)) @ ye

    tu = np.trace(cu, axis1=-2, axis2=-1).real
    td = np.trace(cd, axis1=-2, axis2=-1).real
    te = np.trace(ce, axis1=-2, axis2=-1).real
    tr_y = 3 * tu + 3 * td + te

    cu2 = cu @ cu
    cd2 = cd @ cd
    ce2 = ce @ ce
    cucd = cu @ cd
    cdcu = cd @ cu

    tu2 = np.trace(cu2, axis1=-2, axis2=-1).real
    td2 = np.trace(cd2, axis1=-2, axis2=-1).real
    te2 = np.trace(ce2, axis1=-2, axis2=-1).real
    tud = np.trace(cucd, axis1=-2, axis2=-1).real

    h_s = 3 * tu2 + 3 * td2 + te2
    y4_s = (
        (rat(17, 20) * g1_2 + rat(9, 4) * g2_2 + 8 * g3_2) * tu
        + (rat(1, 4) * g1_2 + rat(9, 4) * g2_2 + 8 * g3_2) * td
        + rat(3, 4) * (g1_2 + g2_2) * te
    )
    chi4_s = rat(9, 4) * (3 * tu2 + 3 * td2 + te2 - rat(2, 3) * tud)

    k1 = 1 / (16 * (math.pi ** 2))
    k2 = k1 * k1

    b1 = rat(4, 3) * n_g + rat(1, 10)
    b2 = rat(-22, 3) + rat(4, 3) * n_g + rat(1, 6)
    b3 = -11 + rat(4, 3) * n_g

    b11, b12, b13 = rat(19, 15) * n_g + rat(9, 50), rat(3, 5) * n_g + rat(9, 10), rat(44, 15) * n_g
    b21, b22, b23 = rat(1, 5) * n_g + rat(3, 10), rat(-136, 3) + rat(49, 3) * n_g + rat(13, 6), 4 * n_g
    b31, b32, b33 = rat(11, 30) * n_g, rat(3, 2) * n_g, -102 + rat(76, 3) * n_g

    dg1 = k1 * b1 * g1 * g1_2 + k2 * g1 * g1_2 * (b11 * g1_2 + b12 * g2_2 + b13 * g3_2 - rat(17, 10) * tu - rat(1, 2) * td - rat(3, 2) * te)
    dg2 = k1 * b2 * g2 * g2_2 + k2 * g2 * g2_2 * (b21 * g1_2 + b22 * g2_2 + b23 * g3_2 - rat(3, 2) * tu - rat(3, 2) * td - rat(1, 2) * te)
    dg3 = k1 * b3 * g3 * g3_2 + k2 * g3 * g3_2 * (b31 * g1_2 + b32 * g2_2 + b33 * g3_2 - 2 * tu - 2 * td)

    i3 = np.eye(3, dtype=np.complex128)[None, :, :]
    mu1 = rat(3, 2) * (cu - cd) + (tr_y - (rat(17, 20) * g1_2 + rat(9, 4) * g2_2 + 8 * g3_2))[:, None, None] * i3
    md1 = rat(3, 2) * (cd - cu) + (tr_y - (rat(1, 4) * g1_2 + rat(9, 4) * g2_2 + 8 * g3_2))[:, None, None] * i3
    me1 = rat(3, 2) * ce + (tr_y - rat(9, 4) * (g1_2 + g2_2))[:, None, None] * i3

    su2 = (
        -chi4_s + 6 * lam * lam + rat(5, 2) * y4_s
        + (rat(9, 200) + rat(29, 45) * n_g) * g1_4 - rat(9, 20) * g1_2 * g2_2 + rat(19, 15) * g1_2 * g3_2
        - (rat(35, 4) - n_g) * g2_4 + 9 * g2_2 * g3_2 - (rat(404, 3) - rat(80, 9) * n_g) * g3_4
    )
    sd2 = (
        -chi4_s + 6 * lam * lam + rat(5, 2) * y4_s
        - (rat(29, 200) + rat(1, 45) * n_g) * g1_4 - rat(27, 20) * g1_2 * g2_2 + rat(31, 15) * g1_2 * g3_2
        - (rat(35, 4) - n_g) * g2_4 + 9 * g2_2 * g3_2 - (rat(404, 3) - rat(80, 9) * n_g) * g3_4
    )
    se2 = (
        -chi4_s + 6 * lam * lam + rat(5, 2) * y4_s
        + (rat(51, 200) + rat(11, 5) * n_g) * g1_4 + rat(27, 20) * g1_2 * g2_2 - (rat(35, 4) - n_g) * g2_4
    )

    mu2 = (
        rat(3, 2) * cu2 - cucd - rat(1, 4) * cdcu + rat(11, 4) * cd2
        + tr_y[:, None, None] * (rat(5, 4) * cd - rat(9, 4) * cu)
        - (12 * lam)[:, None, None] * cu
        + (rat(223, 80) * g1_2 + rat(135, 16) * g2_2 + 16 * g3_2)[:, None, None] * cu
        - (rat(43, 80) * g1_2 - rat(9, 16) * g2_2 + 16 * g3_2)[:, None, None] * cd
        + su2[:, None, None] * i3
    )
    md2 = (
        rat(3, 2) * cd2 - cdcu - rat(1, 4) * cucd + rat(11, 4) * cu2
        + tr_y[:, None, None] * (rat(5, 4) * cu - rat(9, 4) * cd)
        - (12 * lam)[:, None, None] * cd
        + (rat(187, 80) * g1_2 + rat(135, 16) * g2_2 + 16 * g3_2)[:, None, None] * cd
        - (rat(79, 80) * g1_2 - rat(9, 16) * g2_2 + 16 * g3_2)[:, None, None] * cu
        + sd2[:, None, None] * i3
    )
    me2 = (
        rat(3, 2) * ce2 - rat(9, 4) * tr_y[:, None, None] * ce - (12 * lam)[:, None, None] * ce
        + (rat(387, 80) * g1_2 + rat(135, 16) * g2_2)[:, None, None] * ce
        + se2[:, None, None] * i3
    )

    dyu = yu @ (k1 * mu1 + k2 * mu2)
    dyd = yd @ (k1 * md1 + k2 * md2)
    dye = ye @ (k1 * me1 + k2 * me2)

    tu3 = np.trace(cu2 @ cu, axis1=-2, axis2=-1).real
    td3 = np.trace(cd2 @ cd, axis1=-2, axis2=-1).real
    te3 = np.trace(ce2 @ ce, axis1=-2, axis2=-1).real
    tmix3 = np.trace(cu @ (cu + cd) @ cd, axis1=-2, axis2=-1).real

    blam1 = (
        24 * lam * lam - (rat(9, 5) * g1_2 + 9 * g2_2) * lam
        + rat(27, 200) * g1_4 + rat(9, 20) * g1_2 * g2_2 + rat(9, 8) * g2_4
        + 4 * tr_y * lam - 2 * h_s
    )
    blam2 = (
        -312 * (lam ** 3) + (108 * g2_2 + rat(108, 5) * g1_2) * (lam * lam)
        - ((rat(313, 8) - 10 * n_g) * g2_4 - rat(117, 20) * g2_2 * g1_2 - (rat(687, 200) + 2 * n_g) * g1_4) * lam
        + rat(1, 2) * (
            (rat(497, 8) - 8 * n_g) * g2_6
            - (rat(97, 40) + rat(8, 5) * n_g) * g2_4 * g1_2
            - (rat(717, 200) + rat(8, 5) * n_g) * g2_2 * g1_4
            - (rat(531, 1000) + rat(24, 25) * n_g) * g1_6
        )
        - 32 * g3_2 * (tu2 + td2)
        - rat(4, 5) * g1_2 * (2 * tu2 - td2 + 3 * te2)
        - rat(3, 4) * g2_4 * tr_y
        + rat(1, 2) * g1_2 * (
            (rat(63, 5) * g2_2 - rat(171, 50) * g1_2) * tu
            + (rat(27, 5) * g2_2 + rat(9, 10) * g1_2) * td
            + (rat(33, 5) * g2_2 - rat(9, 2) * g1_2) * te
        )
        + 10 * lam * y4_s + c_lam2_try * (lam * lam) * tr_y - lam * h_s - 42 * lam * tud
        + 10 * (3 * tu3 + 3 * td3 + te3) - 6 * tmix3
    )
    dlam = k1 * blam1 + k2 * blam2
    return dg1, dg2, dg3, dlam, dyu, dyd, dye


def sm_2loop_rhs_single(_t: float, y_vec: np.ndarray, n_g: int = 3, c_lam2_try: int = -48) -> np.ndarray:
    """Single-history wrapper around sm_2loop_rhs_batch for DOP853 cross-checks."""
    g1 = np.array([y_vec[0]])
    g2 = np.array([y_vec[1]])
    g3 = np.array([y_vec[2]])
    lam = np.array([y_vec[3]])
    yu = y_vec[4:22].view(np.complex128).reshape(1, 3, 3)
    yd = y_vec[22:40].view(np.complex128).reshape(1, 3, 3)
    ye = y_vec[40:58].view(np.complex128).reshape(1, 3, 3)
    dg1, dg2, dg3, dlam, dyu, dyd, dye = sm_2loop_rhs_batch(g1, g2, g3, lam, yu, yd, ye, n_g=n_g, c_lam2_try=c_lam2_try)
    out = np.empty(58, dtype=np.float64)
    out[0], out[1], out[2], out[3] = dg1[0], dg2[0], dg3[0], dlam[0]
    out[4:22] = dyu[0].reshape(-1).view(np.float64)
    out[22:40] = dyd[0].reshape(-1).view(np.float64)
    out[40:58] = dye[0].reshape(-1).view(np.float64)
    return out


def rk4_integrate_sm_batch(
    g1: np.ndarray,
    g2: np.ndarray,
    g3: np.ndarray,
    lam: np.ndarray,
    yu: np.ndarray,
    yd: np.ndarray,
    ye: np.ndarray,
    delta_spans: np.ndarray,
    n_steps: int = 300,
    n_g: int = 3,
    c_lam2_try: int = -48,
) -> tuple[np.ndarray, ...]:
    """Vectorized 4th-order Runge-Kutta downward integration over t in [0, -delta_spans]."""
    half = rat(1, 2)
    sixth = rat(1, 6)
    h = -delta_spans / n_steps
    hm = h[:, None, None]
    for _ in range(n_steps):
        k1 = sm_2loop_rhs_batch(g1, g2, g3, lam, yu, yd, ye, n_g=n_g, c_lam2_try=c_lam2_try)
        k2 = sm_2loop_rhs_batch(
            g1 + half * h * k1[0], g2 + half * h * k1[1], g3 + half * h * k1[2], lam + half * h * k1[3],
            yu + half * hm * k1[4], yd + half * hm * k1[5], ye + half * hm * k1[6], n_g=n_g, c_lam2_try=c_lam2_try,
        )
        k3 = sm_2loop_rhs_batch(
            g1 + half * h * k2[0], g2 + half * h * k2[1], g3 + half * h * k2[2], lam + half * h * k2[3],
            yu + half * hm * k2[4], yd + half * hm * k2[5], ye + half * hm * k2[6], n_g=n_g, c_lam2_try=c_lam2_try,
        )
        k4 = sm_2loop_rhs_batch(
            g1 + h * k3[0], g2 + h * k3[1], g3 + h * k3[2], lam + h * k3[3],
            yu + hm * k3[4], yd + hm * k3[5], ye + hm * k3[6], n_g=n_g, c_lam2_try=c_lam2_try,
        )
        g1 = g1 + sixth * h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        g2 = g2 + sixth * h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        g3 = g3 + sixth * h * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
        lam = lam + sixth * h * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3])
        yu = yu + sixth * hm * (k1[4] + 2 * k2[4] + 2 * k3[4] + k4[4])
        yd = yd + sixth * hm * (k1[5] + 2 * k2[5] + 2 * k3[5] + k4[5])
        ye = ye + sixth * hm * (k1[6] + 2 * k2[6] + 2 * k3[6] + k4[6])
    return g1, g2, g3, lam, yu, yd, ye


def verify_buttazzo_literature_benchmark() -> dict:
    """Guardrail 4 Gate: Reproduce Buttazzo et al. arXiv:1307.3536 Table 3 -> M_Pl trajectory."""
    lam_mt = rat(12604, 100000)
    yt_mt = rat(94018, 100000)
    g2_mt = rat(64779, 100000)
    gy_mt = rat(35830, 100000)
    g1_mt = math.sqrt(rat(5, 3)) * gy_mt
    g3_mt = rat(11666, 10000)
    t_planck = math.log((12209 * (10 ** 15)) / Fraction(1731, 10))

    y0 = np.zeros(58, dtype=np.float64)
    y0[:4] = [g1_mt, g2_mt, g3_mt, lam_mt]
    y0[4:22] = np.diag([0, 0, yt_mt]).astype(np.complex128).reshape(-1).view(np.float64)
    y0[22:40] = np.diag([0, 0, rat(16, 1000)]).astype(np.complex128).reshape(-1).view(np.float64)
    y0[40:58] = np.diag([0, 0, rat(1, 100)]).astype(np.complex128).reshape(-1).view(np.float64)

    sol = solve_ivp(sm_2loop_rhs_single, (0, t_planck), y0, method="DOP853", rtol=pow10_neg(11), atol=pow10_neg(13))
    yf = sol.y[:, -1]
    yu_pl = yf[4:22].view(np.complex128).reshape(3, 3)
    yt_pl = float(np.linalg.svd(yu_pl, compute_uv=False)[0])

    ref_g1, ref_g2, ref_g3, ref_yt = rat(6154, 10000), rat(5055, 10000), rat(4873, 10000), rat(3825, 10000)
    rel_errs_gauge = [
        abs(float(yf[0]) - ref_g1) / ref_g1,
        abs(float(yf[1]) - ref_g2) / ref_g2,
        abs(float(yf[2]) - ref_g3) / ref_g3,
    ]
    rel_err_yt = abs(yt_pl - ref_yt) / ref_yt
    passed = bool(max(rel_errs_gauge) < rat(1, 1000) and rel_err_yt < rat(1, 100) and float(yf[3]) < 0)
    return {
        "g1_MPl": float(yf[0]),
        "g2_MPl": float(yf[1]),
        "g3_MPl": float(yf[2]),
        "yt_MPl": yt_pl,
        "lambda_MPl": float(yf[3]),
        "max_gauge_rel_err_vs_1307_3536": max(rel_errs_gauge),
        "yt_rel_err_vs_1307_3536": rel_err_yt,
        "passed": passed,
    }


def pati_salam_2loop_run(alpha_u_inv: int, delta_ps: int) -> np.ndarray:
    """Integrate 2-loop Pati-Salam gauge couplings (SU(4)_C, SU(2)_L, SU(2)_R) downward by delta_ps."""
    g_u = math.sqrt(4 * math.pi / alpha_u_inv)
    g_init = np.array([g_u, g_u, g_u], dtype=np.float64)
    if delta_ps == 0:
        return g_init

    b_ps = np.array([-10, rat(-7, 3), rat(-7, 3)], dtype=np.float64)
    b2_ps = np.array([
        [rat(-117, 2), rat(15, 2), rat(15, 2)],
        [rat(75, 2), rat(50, 3), 3],
        [rat(75, 2), 3, rat(50, 3)],
    ], dtype=np.float64)
    k1 = 1 / (16 * (math.pi ** 2))
    k2 = k1 * k1

    def rhs_ps(_t: float, g: np.ndarray) -> np.ndarray:
        g_sq = g * g
        return k1 * b_ps * (g * g_sq) + k2 * (g * g_sq) * (b2_ps @ g_sq)

    sol = solve_ivp(rhs_ps, (0, -delta_ps), g_init, method="DOP853", rtol=pow10_neg(12), atol=pow10_neg(14))
    return sol.y[:, -1]


def build_d_symmetric_3family_yukawas(yt_ps: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Construct D-symmetric Hermitian positive-definite 3-family Yukawas (Y_f = Y_f^dag > 0)
    at M_PS with Pati-Salam b-tau unification and |J_CKM| > 1/1000.
    """
    s12, c12 = rat(1, 4), math.sqrt(15) / 4
    s23, c23 = rat(1, 5), math.sqrt(24) / 5
    s13, c13 = rat(1, 10), math.sqrt(99) / 10
    exp_id = complex(rat(3, 5), rat(4, 5))

    u12 = np.array([[c12, s12, 0], [-s12, c12, 0], [0, 0, 1]], dtype=np.complex128)
    u23 = np.array([[1, 0, 0], [0, c23, s23], [0, -s23, c23]], dtype=np.complex128)
    u13 = np.array([[c13, 0, s13 * np.conj(exp_id)], [0, 1, 0], [-s13 * exp_id, 0, c13]], dtype=np.complex128)
    v_ckm = u23 @ u13 @ u12

    yu_eigs = np.array([yt_ps * rat(1, 500), yt_ps * rat(1, 25), yt_ps], dtype=np.complex128)
    yd_eigs = np.array([yt_ps * rat(1, 200), yt_ps * rat(1, 25), yt_ps * rat(2, 5)], dtype=np.complex128)
    ye_eigs = np.array([yt_ps * rat(1, 500), yt_ps * rat(1, 30), yt_ps * rat(2, 5)], dtype=np.complex128)

    yu = np.diag(yu_eigs)
    yd = v_ckm @ np.diag(yd_eigs) @ v_ckm.conj().T
    ye = np.diag(ye_eigs)

    j_ckm = float(np.imag(v_ckm[0, 1] * v_ckm[1, 2] * np.conj(v_ckm[0, 2]) * np.conj(v_ckm[1, 1])))
    return yu, yd, ye, j_ckm


def bloch_wigner_quadrature(z: complex, n_leggauss: int = 64) -> float:
    """Independent 64-node Gauss-Legendre quadrature for Bloch-Wigner D(z) = Im Li_2(z) + arg(1-z) log|z|."""
    nodes, weights = np.polynomial.legendre.leggauss(n_leggauss)
    s = (nodes + 1) / 2
    w = weights / 2
    li2 = -np.sum(w * np.log(1 - z * s) / s)
    one_minus_z = 1 - z
    return float(li2.imag + math.atan2(one_minus_z.imag, one_minus_z.real) * math.log(abs(z)))


def bloch_wigner_spence(z: complex) -> float:
    """Cross-check Bloch-Wigner D(z) via scipy.special.spence(1 - z) == Li_2(z)."""
    li2 = complex(spence(1 - z))
    one_minus_z = 1 - z
    return float(li2.imag + math.atan2(one_minus_z.imag, one_minus_z.real) * math.log(abs(z)))


def verify_section3_and_faults() -> dict:
    """Verify all 243 Pati-Salam x Z2^D 2-loop histories + DOP853 cross-check + PF6.3, PF6.4, PF6.5."""
    buttazzo_gate = verify_buttazzo_literature_benchmark()

    alpha_u_inv_grid = (52, 60, 68)
    delta_ps_grid = (0, 2, 4)
    delta_sm_grid = (26, 28, 30)
    yt_ps_grid = (rat(1, 2), rat(7, 10), rat(9, 10))
    cos2_2beta_grid = (rat(0), rat(1, 2), rat(1))

    g1_list, g2_list, g3_list, lam_list = [], [], [], []
    dsm_list, dps_list = [], []
    yu_list, yd_list, ye_list = [], [], []
    uv_herm_err = rat(0)
    min_uv_eig = rat(100)
    min_abs_j_ckm = rat(100)

    for alpha_u_inv in alpha_u_inv_grid:
        for delta_ps in delta_ps_grid:
            g4_ps, g2l_ps, g2r_ps = pati_salam_2loop_run(alpha_u_inv, delta_ps)
            a4_inv = 4 * math.pi / (g4_ps * g4_ps)
            a2l_inv = 4 * math.pi / (g2l_ps * g2l_ps)
            a2r_inv = 4 * math.pi / (g2r_ps * g2r_ps)

            a1_ps_inv = rat(3, 5) * a2r_inv + rat(2, 5) * a4_inv
            g1_ps = math.sqrt(4 * math.pi / a1_ps_inv)
            g2_ps = math.sqrt(4 * math.pi / a2l_inv)
            g3_ps = math.sqrt(4 * math.pi / a4_inv)

            for delta_sm in delta_sm_grid:
                for yt_ps in yt_ps_grid:
                    yu_0, yd_0, ye_0, j_ckm = build_d_symmetric_3family_yukawas(yt_ps)
                    uv_herm_err = max(
                        uv_herm_err,
                        float(np.linalg.norm(yu_0 - yu_0.conj().T)),
                        float(np.linalg.norm(yd_0 - yd_0.conj().T)),
                    )
                    min_uv_eig = min(
                        min_uv_eig,
                        float(np.min(np.linalg.eigvalsh(yu_0))),
                        float(np.min(np.linalg.eigvalsh(yd_0))),
                    )
                    min_abs_j_ckm = min(min_abs_j_ckm, abs(j_ckm))

                    for cos2_2b in cos2_2beta_grid:
                        lam_ps = rat(1, 4) * (g2_ps * g2_ps) * cos2_2b
                        g1_list.append(g1_ps)
                        g2_list.append(g2_ps)
                        g3_list.append(g3_ps)
                        lam_list.append(lam_ps)
                        dsm_list.append(delta_sm)
                        dps_list.append(delta_ps)
                        yu_list.append(yu_0)
                        yd_list.append(yd_0)
                        ye_list.append(ye_0)

    g1_arr = np.array(g1_list, dtype=np.float64)
    g2_arr = np.array(g2_list, dtype=np.float64)
    g3_arr = np.array(g3_list, dtype=np.float64)
    lam_arr = np.array(lam_list, dtype=np.float64)
    dsm_arr = np.array(dsm_list, dtype=np.float64)
    dps_arr = np.array(dps_list, dtype=np.float64)
    yu_arr = np.array(yu_list, dtype=np.complex128)
    yd_arr = np.array(yd_list, dtype=np.complex128)
    ye_arr = np.array(ye_list, dtype=np.complex128)

    n_histories = len(g1_arr)
    g1_ir, g2_ir, g3_ir, lam_ir, yu_ir, yd_ir, _ = rk4_integrate_sm_batch(
        g1_arr, g2_arr, g3_arr, lam_arr, yu_arr, yd_arr, ye_arr, dsm_arr, n_steps=300, n_g=3, c_lam2_try=-48
    )

    check_indices = [0, 80, 121, 242]
    max_rk4_vs_dop853_err = rat(0)
    for idx in check_indices:
        y_init = np.zeros(58, dtype=np.float64)
        y_init[:4] = [g1_arr[idx], g2_arr[idx], g3_arr[idx], lam_arr[idx]]
        y_init[4:22] = yu_arr[idx].reshape(-1).view(np.float64)
        y_init[22:40] = yd_arr[idx].reshape(-1).view(np.float64)
        y_init[40:58] = ye_arr[idx].reshape(-1).view(np.float64)
        sol_dop = solve_ivp(
            lambda t, y: sm_2loop_rhs_single(t, y, n_g=3, c_lam2_try=-48),
            (0, -dsm_arr[idx]),
            y_init,
            method="DOP853",
            rtol=pow10_neg(12),
            atol=pow10_neg(14),
        )
        yf_dop = sol_dop.y[:, -1]
        yu_dop = yf_dop[4:22].view(np.complex128).reshape(3, 3)
        err_idx = max(
            abs(float(g1_ir[idx] - yf_dop[0])),
            abs(float(g2_ir[idx] - yf_dop[1])),
            abs(float(g3_ir[idx] - yf_dop[2])),
            abs(float(lam_ir[idx] - yf_dop[3])),
            float(np.linalg.norm(yu_ir[idx] - yu_dop)),
        )
        max_rk4_vs_dop853_err = max(max_rk4_vs_dop853_err, err_idx)

    # Deliverable 3.1: Strong CP bar_theta_QCD(IR) = arg det(Y_u(IR) Y_d(IR))
    det_prod = np.linalg.det(yu_ir @ yd_ir)
    bar_thetas = np.abs(np.arctan2(det_prod.imag, det_prod.real))
    max_bar_theta_ir = float(np.max(bar_thetas))
    max_ir_nonhermiticity = float(np.max(np.linalg.norm(yu_ir - np.conj(np.swapaxes(yu_ir, -1, -2)), axis=(-2, -1))))

    # Deliverable 3.2: 2-loop Pati-Salam gauge residual delta_{2-loop}
    a1_ir_inv = 4 * math.pi / (g1_ir * g1_ir)
    a2_ir_inv = 4 * math.pi / (g2_ir * g2_ir)
    a3_ir_inv = 4 * math.pi / (g3_ir * g3_ir)
    a_em_ir = 1 / (rat(5, 3) * a1_ir_inv + a2_ir_inv)
    a3_ir = 1 / a3_ir_inv
    sin2_theta_w_ir = a_em_ir * a2_ir_inv
    sin2_1loop_formula = (
        rat(23, 134)
        + rat(109, 201) * (a_em_ir / a3_ir)
        + (rat(506, 201) / math.pi) * a_em_ir * dps_arr
    )
    delta_2loop_arr = sin2_theta_w_ir - sin2_1loop_formula
    min_delta_2loop = float(np.min(delta_2loop_arr))
    max_delta_2loop = float(np.max(delta_2loop_arr))

    # Deliverable 3.3: Higgs-to-VEV ratio sqrt(2 lambda_IR) = m_H / v_EW & vacuum stability
    min_lambda_ir = float(np.min(lam_ir))
    higgs_ratios = np.sqrt(2 * lam_ir)
    min_higgs_ratio = float(np.min(higgs_ratios))
    max_higgs_ratio = float(np.max(higgs_ratios))

    # PF6.3: N_g = 6 (b_3 = -3) vs N_g = 3 (b_3 = -7) over Delta_SM = 28
    idx_pf63 = 121
    y_pf63 = np.zeros(58, dtype=np.float64)
    y_pf63[:4] = [g1_arr[idx_pf63], g2_arr[idx_pf63], g3_arr[idx_pf63], lam_arr[idx_pf63]]
    y_pf63[4:22] = yu_arr[idx_pf63].reshape(-1).view(np.float64)
    y_pf63[22:40] = yd_arr[idx_pf63].reshape(-1).view(np.float64)
    y_pf63[40:58] = ye_arr[idx_pf63].reshape(-1).view(np.float64)

    sol_ng3 = solve_ivp(lambda t, y: sm_2loop_rhs_single(t, y, n_g=3, c_lam2_try=-48), (0, -28), y_pf63, method="DOP853", rtol=pow10_neg(11), atol=pow10_neg(13))
    sol_ng6 = solve_ivp(lambda t, y: sm_2loop_rhs_single(t, y, n_g=6, c_lam2_try=-48), (0, -28), y_pf63, method="DOP853", rtol=pow10_neg(11), atol=pow10_neg(13))
    a3_inv_ng3 = 4 * math.pi / (float(sol_ng3.y[2, -1]) ** 2)
    a3_inv_ng6 = 4 * math.pi / (float(sol_ng6.y[2, -1]) ** 2)
    pf63_shift = abs(a3_inv_ng6 - a3_inv_ng3)
    pf63_caught = bool(pf63_shift > 15)

    # PF6.4: -24 vs -48 lambda^2 Tr_Y factor-of-2 bug across all 243 histories
    _, _, _, lam_ir_bug24, _, _, _ = rk4_integrate_sm_batch(
        g1_arr, g2_arr, g3_arr, lam_arr, yu_arr, yd_arr, ye_arr, dsm_arr, n_steps=300, n_g=3, c_lam2_try=-24
    )
    pf64_max_shift = float(np.max(np.abs(higgs_ratios - np.sqrt(2 * lam_ir_bug24))))
    pf64_caught = bool(pf64_max_shift > rat(1, 1000))

    # PF6.5: Tautological Bloch-Wigner conjugation D(z) + D(conj(z)) == 0 at asymmetric z = 3/5 + (4/5)i
    z_asym = complex(rat(3, 5), rat(4, 5))
    dz_quad = bloch_wigner_quadrature(z_asym)
    dzbar_quad = bloch_wigner_quadrature(np.conj(z_asym))
    dz_spence = bloch_wigner_spence(z_asym)
    quad_vs_spence_err = abs(dz_quad - dz_spence)
    pf65_sum_abs = abs(dz_quad + dzbar_quad)
    pf65_caught = bool(
        abs(dz_quad) > rat(9, 10)
        and quad_vs_spence_err < pow10_neg(15)
        and pf65_sum_abs < pow10_neg(15)
    )

    sec3_passed = bool(
        buttazzo_gate["passed"]
        and n_histories == 243
        and uv_herm_err < pow10_neg(15)
        and min_uv_eig > 0
        and min_abs_j_ckm > rat(1, 1000)
        and max_rk4_vs_dop853_err < pow10_neg(10)
        and max_ir_nonhermiticity > pow10_neg(6)
        and max_bar_theta_ir < pow10_neg(13)
        and min_delta_2loop >= rat(7, 10000)
        and max_delta_2loop <= rat(3, 1000)
        and min_lambda_ir > rat(1, 20)
        and min_higgs_ratio >= rat(35, 100)
        and max_higgs_ratio <= rat(78, 100)
        and pf63_caught
        and pf64_caught
        and pf65_caught
    )

    return {
        "buttazzo_1307_3536_benchmark_gate": buttazzo_gate,
        "history_count": n_histories,
        "uv_hermiticity_max_err": uv_herm_err,
        "uv_min_positive_eigenvalue": min_uv_eig,
        "min_abs_J_CKM_UV": min_abs_j_ckm,
        "rk4_vs_dop853_max_discrepancy": max_rk4_vs_dop853_err,
        "max_dynamical_IR_nonhermiticity_Yu": max_ir_nonhermiticity,
        "max_abs_bar_theta_QCD_IR": max_bar_theta_ir,
        "delta_2loop_envelope": [min_delta_2loop, max_delta_2loop],
        "delta_2loop_target_bounds": [rat(7, 10000), rat(3, 1000)],
        "sqrt_2lambda_IR_envelope": [min_higgs_ratio, max_higgs_ratio],
        "sqrt_2lambda_IR_target_bounds": [rat(35, 100), rat(78, 100)],
        "min_lambda_IR": min_lambda_ir,
        "PF6_3_alpha3_inv_ng3_vs_ng6": [a3_inv_ng3, a3_inv_ng6],
        "PF6_3_abs_shift_alpha3_inv": pf63_shift,
        "PF6_3_caught": pf63_caught,
        "PF6_4_max_abs_shift_sqrt_2lambda_IR": pf64_max_shift,
        "PF6_4_caught": pf64_caught,
        "PF6_5_D_z_at_3_5_plus_4_5_i": dz_quad,
        "PF6_5_quad_vs_spence_err": quad_vs_spence_err,
        "PF6_5_abs_D_z_plus_D_conj_z": pf65_sum_abs,
        "PF6_5_caught": pf65_caught,
        "passed": sec3_passed,
    }


def main() -> int:
    t_start = time.perf_counter()
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]

    sec0 = audit_own_ast_and_manifests(script_path, repo_root)
    sec1 = verify_section1()
    sec2 = verify_section2_and_weinberg_benchmark()
    sec3 = verify_section3_and_faults()
    elapsed_s = time.perf_counter() - t_start

    planted_faults = {
        "PF6_1_orthonormal_basis_so3_anisotropy": sec1["PF6_1_caught"],
        "PF6_2_tm2_column_swap_falsifier": sec2["PF6_2_caught"],
        "PF6_3_ng6_chiral_doubling_gauge_ruin": sec3["PF6_3_caught"],
        "PF6_4_minus24_vs_minus48_quartic_bug": sec3["PF6_4_caught"],
        "PF6_5_bloch_wigner_conjugation_tautology": sec3["PF6_5_caught"],
    }
    all_planted_caught = all(planted_faults.values())
    overall_passed = bool(
        sec0["passed"]
        and sec1["passed"]
        and sec2["passed"]
        and sec3["passed"]
        and all_planted_caught
        and elapsed_s < 30
    )

    report = {
        "gate": "AGY-002_CLOSURE-G6_INDEPENDENT_REFEREE",
        "firewall": "0 of 19",
        "overall_passed": overall_passed,
        "runtime_seconds": elapsed_s,
        "planted_faults_caught_count": sum(1 for v in planted_faults.values() if v),
        "planted_faults_summary": planted_faults,
        "section_0_ast_and_manifests": sec0,
        "section_1_covariant_majorana_seesaw": sec1,
        "section_2_tm1_sum_rule_and_rge": sec2,
        "section_3_pati_salam_2loop_ir_surfaces": sec3,
    }

    out_path = script_path.with_name("referee_closure_g6_out.json")
    out_path.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    return 0 if overall_passed else 1


if __name__ == "__main__":
    sys.exit(main())
