"""Cold-room Gate 9 standalone verification script (0 of 19 empirical inputs).

Independently verifies Cards AGY-002_FOUND-G9, AGY-002_FOUND-G9-ERRATUM, and
AGY-002_FOUND-G9-ERRATUM-2 from scratch with zero repository Python imports,
zero float AST literals, and zero complex AST literals:
  1. Parity-odd 4D Callan-Harvey / Kaplan domain-wall chiral localization
     (SymPy operator + normalization proofs, 220-mode Dirichlet Sine-Galerkin
     solver cross-checked against 200-node Chebyshev collocation, and PF9.1).
  2. SU(2)_L-invariant Pati-Salam (1, 2, 2) D-parity Strong-CP = 0 and
     |J_CKM| > 1/100 at tau_cusp = 2 sqrt(3) i with shared xi = i eta
     (2D gauge-periodic torus quadrature cross-checked against closed-form 1D
     CIM Jacobi-theta sum, Guardrail 4 BBO -11/2 and +3 slopes, 2-loop BPV
     quark Yukawa RGE over dt = -30 via DOP853 and RK4, 10-trial SU(3)^3 and
     U(3)^3 Haar invariance, PF9.2, and PF9.3).
  3. Complete P-864 canonical-end repair via left-multiplying SL(2, Z) Gauss
     reduction z_FD = (a t + b)/(c t + d) and L(t) = L(z_FD) - ln|c t + d|
     on both L_2 and L_max over B1927 grid.json + B1667 the_canonical_cusp.json,
     Delaunay chord-lens verification, multi-letter SL(2, Z) word covariance,
     PF9.4, PF9.5, B1927..B1949 JSON coordinate sweep, and 11-manifest custody.
"""

from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
import sympy as sp

I_UNIT: complex = complex(0, 1)
ZERO_C: complex = complex(0, 0)

ALLOWED_IMPORT_ROOTS: frozenset[str] = frozenset(
    {
        "__future__",
        "ast",
        "fractions",
        "hashlib",
        "json",
        "math",
        "mpmath",
        "numpy",
        "pathlib",
        "scipy",
        "sympy",
        "typing",
    }
)

EXPECTED_PRIOR_MANIFESTS: tuple[str, ...] = (
    "relays/agy002_found_g8/OUTPUT_SHA256.txt",
    "relays/agy002_found_g8/SCRIPT_SHA256.txt",
    "relays/agy002_found_g8_fixed/OUTPUT_SHA256.txt",
    "relays/agy002_found_g8_fixed/SCRIPT_SHA256.txt",
    "relays/agy002_found_g8_referee/OUTPUT_SHA256.txt",
    "relays/agy002_found_g8_referee/SCRIPT_SHA256.txt",
    "relays/agy002_found_g9/SCRIPT_SHA256.txt",
    "relays/agy002_found_g9_fixed/OUTPUT_SHA256.txt",
    "relays/agy002_found_g9_fixed/SCRIPT_SHA256.txt",
    "relays/agy002_found_g9_v2/OUTPUT_SHA256.txt",
    "relays/agy002_found_g9_v2/SCRIPT_SHA256.txt",
)


def _sha256_hex(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _verify_manifest_file(manifest_path: Path, repo_root: Path) -> dict[str, Any]:
    raw_line = manifest_path.read_bytes().decode("utf-8").strip()
    parts = raw_line.split()
    expected_digest = parts[0]
    rel_target = parts[1]
    target_path = repo_root / rel_target
    actual_digest = _sha256_hex(target_path)
    return {
        "manifest": str(manifest_path.relative_to(repo_root)),
        "target": rel_target,
        "expected_sha256": expected_digest,
        "actual_sha256": actual_digest,
        "matched": bool(actual_digest == expected_digest and len(expected_digest) == 64),
    }


def run_section_0_custody_and_ast_lock(script_path: Path, repo_root: Path) -> dict[str, Any]:
    source_text = script_path.read_text(encoding="utf-8")
    tree = ast.parse(source_text, filename=str(script_path))

    float_literals: list[int] = []
    complex_literals: list[int] = []
    disallowed_imports: list[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals.append(int(getattr(node, "lineno", 0)))
            elif isinstance(node.value, complex):
                complex_literals.append(int(getattr(node, "lineno", 0)))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                mod_root = alias.name.split(".")[0]
                if mod_root not in ALLOWED_IMPORT_ROOTS:
                    disallowed_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if int(node.level or 0) > 0:
                disallowed_imports.append(f"relative:{node.module}")
            elif node.module is not None:
                mod_root = node.module.split(".")[0]
                if mod_root not in ALLOWED_IMPORT_ROOTS:
                    disallowed_imports.append(node.module)

    prior_records: list[dict[str, Any]] = []
    for rel_mf in EXPECTED_PRIOR_MANIFESTS:
        mf_path = repo_root / rel_mf
        prior_records.append(_verify_manifest_file(mf_path, repo_root))

    prior_matched_count = sum(1 for rec in prior_records if rec["matched"])
    prior_total_count = len(prior_records)

    self_mf_path = script_path.parent / "SCRIPT_SHA256.txt"
    self_record = _verify_manifest_file(self_mf_path, repo_root)

    passed = bool(
        len(float_literals) == 0
        and len(complex_literals) == 0
        and len(disallowed_imports) == 0
        and prior_total_count == 11
        and prior_matched_count == 11
        and self_record["matched"]
    )
    return {
        "float_literal_count": len(float_literals),
        "complex_literal_count": len(complex_literals),
        "repo_import_count": len(disallowed_imports),
        "disallowed_imports": disallowed_imports,
        "empirical_inputs_used": "0 of 19",
        "prior_manifest_count": prior_total_count,
        "prior_manifests_matched": prior_matched_count,
        "prior_manifests": prior_records,
        "self_script_manifest": self_record,
        "passed": passed,
    }


def _sine_galerkin_domain_wall(
    box_half_width: int,
    mass_amp: int,
    n_modes: int,
    n_quad: int,
    constant_mass_fault: bool,
) -> tuple[np.ndarray, np.ndarray, float]:
    half_L = float(Fraction(box_half_width, 1))
    m0 = float(Fraction(mass_amp, 1))
    two_L = float(Fraction(2 * box_half_width, 1))
    du = two_L / n_quad
    u_grid = (np.arange(n_quad, dtype=np.float64) + (1 / 2)) * du - half_L

    mode_idx = np.arange(1, n_modes + 1, dtype=np.float64)[:, None]
    phi_basis = math.sqrt(1 / half_L) * np.sin(
        mode_idx * math.pi * (u_grid[None, :] + half_L) / two_L
    )
    kinetic = np.diag(((np.arange(1, n_modes + 1, dtype=np.float64) * math.pi) / two_L) ** 2)

    if constant_mass_fault:
        pot_L = np.full_like(u_grid, m0 ** 2)
    else:
        pot_L = (m0 ** 2) - 2 * (m0 ** 2) / (np.cosh(m0 * u_grid) ** 2)

    H_L = kinetic + (phi_basis * (pot_L * du)) @ phi_basis.T
    H_R = kinetic + np.diag(np.full(n_modes, m0 ** 2, dtype=np.float64))

    evals_L, evecs_L = np.linalg.eigh(H_L)
    evals_R, _ = np.linalg.eigh(H_R)

    psi_ground = evecs_L[:, 0] @ phi_basis
    psi_sech_exact = math.sqrt(m0 / 2) / np.cosh(m0 * u_grid)
    overlap = float(abs(np.sum(psi_ground * psi_sech_exact) * du))
    return evals_L, evals_R, overlap


def _chebyshev_collocation_domain_wall(
    box_half_width: int,
    mass_amp: int,
    n_cheb: int,
) -> tuple[np.ndarray, np.ndarray]:
    half_L = float(Fraction(box_half_width, 1))
    m0 = float(Fraction(mass_amp, 1))
    k_idx = np.arange(n_cheb + 1, dtype=np.float64)
    x_nodes = np.cos(math.pi * k_idx / n_cheb)
    weights = np.ones(n_cheb + 1, dtype=np.float64)
    weights[0] = 2
    weights[-1] = 2
    weights = weights * ((-1) ** np.arange(n_cheb + 1))

    X_mat = np.tile(x_nodes, (n_cheb + 1, 1))
    dX = X_mat - X_mat.T
    D1 = (weights[:, None] / weights[None, :]) / (dX + np.eye(n_cheb + 1))
    D1 = D1 - np.diag(np.sum(D1, axis=1))
    D1_s = D1 / half_L
    D2_s = D1_s @ D1_s

    s_interior = half_L * x_nodes[1:-1]
    pot_L = (m0 ** 2) - 2 * (m0 ** 2) / (np.cosh(m0 * s_interior) ** 2)
    pot_R = np.full_like(s_interior, m0 ** 2)

    H_L_cheb = -D2_s[1:-1, 1:-1] + np.diag(pot_L)
    H_R_cheb = -D2_s[1:-1, 1:-1] + np.diag(pot_R)
    evals_L_c = np.sort(np.linalg.eigvals(H_L_cheb).real)
    evals_R_c = np.sort(np.linalg.eigvals(H_R_cheb).real)
    return evals_L_c, evals_R_c


def run_section_1_domain_wall_localization() -> dict[str, Any]:
    s_sym = sp.Symbol("s", real=True)
    M0_sym = sp.Symbol("M_0", positive=True)
    f_sym = sp.Function("f")(s_sym)

    kink_mass = M0_sym * sp.tanh(M0_sym * s_sym)
    parity_odd_res = sp.simplify(kink_mass.subs(s_sym, -s_sym) + kink_mass)

    psi0_sym = sp.sech(M0_sym * s_sym)
    annihilator_res = sp.simplify(sp.diff(psi0_sym, s_sym) + kink_mass * psi0_sym)

    A_f = sp.diff(f_sym, s_sym) + kink_mass * f_sym
    Adag_A_f = -sp.diff(A_f, s_sym) + kink_mass * A_f
    expected_HL_f = (
        -sp.diff(f_sym, s_sym, 2)
        + (M0_sym ** 2) * f_sym
        - 2 * (M0_sym ** 2) * (sp.sech(M0_sym * s_sym) ** 2) * f_sym
    )
    hl_factor_res = sp.simplify(Adag_A_f - expected_HL_f)

    Adag_f = -sp.diff(f_sym, s_sym) + kink_mass * f_sym
    A_Adag_f = sp.diff(Adag_f, s_sym) + kink_mass * Adag_f
    expected_HR_f = -sp.diff(f_sym, s_sym, 2) + (M0_sym ** 2) * f_sym
    hr_factor_res = sp.simplify(A_Adag_f - expected_HR_f)

    sech_sq_int = sp.integrate(sp.sech(M0_sym * s_sym).rewrite(sp.exp) ** 2, (s_sym, -sp.oo, sp.oo))
    norm_int_res = sp.simplify(sech_sq_int - sp.Rational(2, 1) / M0_sym)

    symbolic_ok = bool(
        parity_odd_res == 0
        and annihilator_res == 0
        and hl_factor_res == 0
        and hr_factor_res == 0
        and norm_int_res == 0
    )

    evals_L_sg, evals_R_sg, overlap_sg = _sine_galerkin_domain_wall(
        box_half_width=8,
        mass_amp=3,
        n_modes=220,
        n_quad=640,
        constant_mass_fault=False,
    )
    evals_L_ch, evals_R_ch = _chebyshev_collocation_domain_wall(
        box_half_width=8,
        mass_amp=3,
        n_cheb=200,
    )
    evals_L_const, _, overlap_const = _sine_galerkin_domain_wall(
        box_half_width=8,
        mass_amp=3,
        n_modes=220,
        n_quad=640,
        constant_mass_fault=True,
    )

    lam_L0 = float(evals_L_sg[0])
    lam_L1 = float(evals_L_sg[1])
    lam_R0 = float(evals_R_sg[0])
    lam_L0_cheb = float(evals_L_ch[0])
    lam_L1_cheb = float(evals_L_ch[1])
    lam_R0_cheb = float(evals_R_ch[0])
    lam_L0_pf91 = float(evals_L_const[0])

    tol_zero = (1 / 10) ** 4
    min_overlap = 99999 / 100000
    gap_threshold = 9

    pf9_1_caught = bool(lam_L0_pf91 > gap_threshold)
    spectral_ok = bool(
        abs(lam_L0) < tol_zero
        and abs(lam_L0_cheb) < tol_zero
        and lam_L1 > gap_threshold
        and lam_L1_cheb > gap_threshold
        and lam_R0 > gap_threshold
        and lam_R0_cheb > gap_threshold
        and overlap_sg > min_overlap
        and abs(lam_L1 - lam_L1_cheb) < (1 / 10) ** 6
        and abs(lam_R0 - lam_R0_cheb) < (1 / 10) ** 10
    )

    left_zero_modes = int(np.sum(np.abs(evals_L_sg) < tol_zero))
    right_zero_modes = int(np.sum(np.abs(evals_R_sg) < tol_zero))
    cim_internal_generations = 3
    chiral_generations_4d = (left_zero_modes - right_zero_modes) * cim_internal_generations

    passed = bool(symbolic_ok and spectral_ok and pf9_1_caught and chiral_generations_4d == 3)
    return {
        "symbolic_parity_odd_zero": bool(parity_odd_res == 0),
        "symbolic_plus_dds_annihilates_sech": bool(annihilator_res == 0),
        "symbolic_AdagA_poschl_teller_exact": bool(hl_factor_res == 0),
        "symbolic_AAdag_free_gap_exact": bool(hr_factor_res == 0),
        "symbolic_sech_sq_integral_2_over_M0": bool(norm_int_res == 0),
        "sine_galerkin_modes": 220,
        "chebyshev_nodes": 200,
        "box_half_width": 8,
        "M_0": 3,
        "lambda_L0_sine_galerkin": lam_L0,
        "lambda_L1_sine_galerkin": lam_L1,
        "lambda_R0_sine_galerkin": lam_R0,
        "lambda_L0_chebyshev": lam_L0_cheb,
        "lambda_L1_chebyshev": lam_L1_cheb,
        "lambda_R0_chebyshev": lam_R0_cheb,
        "overlap_abs_psiL0_sech": overlap_sg,
        "left_zero_modes": left_zero_modes,
        "right_zero_modes": right_zero_modes,
        "chiral_generations_tensored_with_CIM_3_3_minus6": chiral_generations_4d,
        "PF9_1_constant_mass_lambda_L0": lam_L0_pf91,
        "PF9_1_constant_mass_overlap": overlap_const,
        "PF9_1_caught": pf9_1_caught,
        "passed": passed,
    }


def _psi_cim_torus(
    z_grid: np.ndarray,
    j_idx: int,
    flux_M: int,
    alpha_char: float,
    beta_char: float,
    zeta_shift: complex,
    tau_mod: complex,
    n_sum: int = 12,
) -> np.ndarray:
    w_val = np.asarray(z_grid + zeta_shift, dtype=np.complex128)
    w_re = np.real(w_val)
    w_im = np.imag(w_val)
    t_re = float(tau_mod.real)
    t_im = float(tau_mod.imag)
    norm_factor = (2 * flux_M * t_im) ** (1 / 4)

    n_vec = np.arange(-n_sum, n_sum + 1, dtype=np.float64)[:, None]
    na_vec = n_vec + (j_idx + alpha_char) / flux_M
    w1_flat = w_re.ravel()[None, :]
    w2_flat = w_im.ravel()[None, :]

    re_part = -math.pi * flux_M * t_im * ((na_vec + w2_flat / t_im) ** 2)
    im_part = (
        math.pi * flux_M * (w1_flat * w2_flat / t_im)
        + math.pi * flux_M * t_re * (na_vec ** 2)
        + 2 * math.pi * na_vec * (flux_M * w1_flat + beta_char)
    )
    series_sum = np.sum(np.exp(re_part + I_UNIT * im_part), axis=0)
    return float(norm_factor) * series_sum.reshape(w_val.shape)


def _build_cim_overlap_quadrature(
    n_grid: int,
    tau_mod: complex,
    zeta_L: complex,
    zeta_R: complex,
    zeta_H: complex,
) -> tuple[np.ndarray, np.ndarray, float, float, float]:
    axis = (np.arange(n_grid, dtype=np.float64) + (1 / 2)) / n_grid - (1 / 2)
    X_g, Y_g = np.meshgrid(axis, axis, indexing="ij")
    Z_g = np.asarray(X_g + tau_mod * Y_g, dtype=np.complex128)
    d_area = 1 / (n_grid * n_grid)

    half = float(Fraction(1, 2))
    zero_f = float(Fraction(0, 1))
    psi_L = np.array([_psi_cim_torus(Z_g, i, 3, half, half, zeta_L, tau_mod) for i in range(3)])
    psi_R = np.array([_psi_cim_torus(Z_g, j, 3, half, half, zeta_R, tau_mod) for j in range(3)])
    psi_H = np.array([_psi_cim_torus(Z_g, k, 6, zero_f, zero_f, zeta_H, tau_mod) for k in range(6)])

    gram_L = np.einsum("ixy,jxy->ij", psi_L.conj(), psi_L) * d_area
    gram_H = np.einsum("kxy,lxy->kl", psi_H.conj(), psi_H) * d_area
    ortho_err_L = float(np.max(np.abs(gram_L - np.eye(3))))
    ortho_err_H = float(np.max(np.abs(gram_H - np.eye(6))))

    Y_tensor = np.einsum("ixy,jxy,kxy->ijk", psi_L, psi_R, psi_H.conj()) * d_area
    return Y_tensor, psi_L, d_area, ortho_err_L, ortho_err_H


def _build_cim_overlap_theta_series(tau_im: float, eta_val: float) -> np.ndarray:
    Y_th = np.zeros((3, 3, 6), dtype=np.complex128)
    pref = (3 * tau_im) ** float(Fraction(1, 4))
    m_idx = np.arange(-14, 15, dtype=np.float64)
    for i in range(3):
        for j in range(3):
            for k in range(6):
                if (i + j + 1 - k) % 3 == 0:
                    delta_m = m_idx + (k - 2 * j - 1) / 6
                    phase = np.exp(I_UNIT * math.pi * k / 3)
                    Y_th[i, j, k] = pref * phase * np.sum(
                        np.exp(-6 * math.pi * tau_im * ((delta_m + eta_val / tau_im) ** 2))
                    )
    return Y_th


def _jarlskog_and_ckm_from_svd(Y_u: np.ndarray, Y_d: np.ndarray) -> tuple[float, float, np.ndarray]:
    U_u, _, _ = np.linalg.svd(Y_u)
    U_d, _, _ = np.linalg.svd(Y_d)
    U_u_asc = U_u[:, ::-1]
    U_d_asc = U_d[:, ::-1]
    V_ckm = U_u_asc.conj().T @ U_d_asc
    J_quartet = float(np.imag(V_ckm[0, 0] * V_ckm[1, 1] * np.conj(V_ckm[0, 1]) * np.conj(V_ckm[1, 0])))

    H_u = Y_u @ Y_u.conj().T
    H_d = Y_d @ Y_d.conj().T
    ev_u = np.sort(np.linalg.eigvalsh(H_u))
    ev_d = np.sort(np.linalg.eigvalsh(H_d))
    comm_num = float(np.imag(np.trace(H_u @ H_u @ H_d @ H_d @ H_u @ H_d)))
    comm_den = float(
        (ev_u[2] - ev_u[1])
        * (ev_u[2] - ev_u[0])
        * (ev_u[1] - ev_u[0])
        * (ev_d[2] - ev_d[1])
        * (ev_d[2] - ev_d[0])
        * (ev_d[1] - ev_d[0])
    )
    J_comm = comm_num / comm_den
    return J_quartet, J_comm, np.abs(V_ckm)


def _beta_bpv_quark_2loop(
    Y_u: np.ndarray,
    Y_d: np.ndarray,
    include_1loop: bool = True,
    include_2loop: bool = True,
    include_traces: bool = True,
    unrescaled_loop_factors: bool = True,
) -> tuple[np.ndarray, np.ndarray]:
    H_u = Y_u @ Y_u.conj().T
    H_d = Y_d @ Y_d.conj().T
    I_3 = np.eye(3, dtype=np.complex128)

    Y2_S = (3 * np.trace(H_u + H_d)) if include_traces else ZERO_C
    chi4_S = (
        ((9 / 4) * np.trace(3 * (H_u @ H_u) + 3 * (H_d @ H_d) - (1 / 3) * (H_u @ H_d + H_d @ H_u)))
        if include_traces
        else ZERO_C
    )

    loop1 = (1 / (16 * (math.pi ** 2))) if unrescaled_loop_factors else 1
    loop2 = (loop1 ** 2) if unrescaled_loop_factors else 1

    M_u = np.zeros((3, 3), dtype=np.complex128)
    M_d = np.zeros((3, 3), dtype=np.complex128)

    if include_1loop:
        M_u = M_u + loop1 * ((3 / 2) * (H_u - H_d) + Y2_S * I_3)
        M_d = M_d + loop1 * ((3 / 2) * (H_d - H_u) + Y2_S * I_3)

    if include_2loop:
        M_u2 = (
            (3 / 2) * (H_u @ H_u)
            - (H_d @ H_u)
            - (1 / 4) * (H_u @ H_d)
            + (11 / 4) * (H_d @ H_d)
            + Y2_S * ((5 / 4) * H_d - (9 / 4) * H_u)
            - chi4_S * I_3
        )
        M_d2 = (
            (3 / 2) * (H_d @ H_d)
            - (H_u @ H_d)
            - (1 / 4) * (H_d @ H_u)
            + (11 / 4) * (H_u @ H_u)
            + Y2_S * ((5 / 4) * H_u - (9 / 4) * H_d)
            - chi4_S * I_3
        )
        M_u = M_u + loop2 * M_u2
        M_d = M_d + loop2 * M_d2

    return M_u @ Y_u, M_d @ Y_d


def _verify_bbo_benchmark_gate() -> dict[str, Any]:
    a_d_sym = sp.Rational(-3, 2)
    c_d_sym = sp.Rational(11, 4)
    b_d_trace_sym = sp.Rational(5, 4) * 3
    sym_1loop = -2 * a_d_sym
    sym_2loop_cd = -2 * c_d_sym
    sym_2loop_full = -2 * (b_d_trace_sym + c_d_sym)

    s12 = 1 / 100
    s23 = (1 / 10) ** 4
    s13 = (1 / 10) ** 5
    c12 = math.sqrt(1 - s12 ** 2)
    c23 = math.sqrt(1 - s23 ** 2)
    c13 = math.sqrt(1 - s13 ** 2)
    ph = complex(math.cos(1), math.sin(1))
    ph_c = np.conj(ph)

    V_hier = np.array(
        [
            [c12 * c13, s12 * c13, s13 * ph_c],
            [-s12 * c23 - c12 * s23 * s13 * ph, c12 * c23 - s12 * s23 * s13 * ph, s23 * c13],
            [s12 * s23 - c12 * c23 * s13 * ph, -c12 * s23 - s12 * c23 * s13 * ph, c23 * c13],
        ],
        dtype=np.complex128,
    )
    Yu_b = np.diag([(1 / 10) ** 6, (1 / 10) ** 4, 1]).astype(np.complex128)
    Yd_b = V_hier @ np.diag([(1 / 10) ** 8, (1 / 10) ** 6, (1 / 10) ** 4]).astype(np.complex128)

    J_base, _, _ = _jarlskog_and_ckm_from_svd(Yu_b, Yd_b)
    eps_step = (1 / 10) ** 5

    dYu_1, dYd_1 = _beta_bpv_quark_2loop(Yu_b, Yd_b, True, False, False, False)
    J1_p, _, _ = _jarlskog_and_ckm_from_svd(Yu_b + eps_step * dYu_1, Yd_b + eps_step * dYd_1)
    J1_m, _, _ = _jarlskog_and_ckm_from_svd(Yu_b - eps_step * dYu_1, Yd_b - eps_step * dYd_1)
    num_1loop = (J1_p - J1_m) / (2 * eps_step * J_base)

    dYu_2c, dYd_2c = _beta_bpv_quark_2loop(Yu_b, Yd_b, False, True, False, False)
    J2c_p, _, _ = _jarlskog_and_ckm_from_svd(Yu_b + eps_step * dYu_2c, Yd_b + eps_step * dYd_2c)
    J2c_m, _, _ = _jarlskog_and_ckm_from_svd(Yu_b - eps_step * dYu_2c, Yd_b - eps_step * dYd_2c)
    num_2loop_cd = (J2c_p - J2c_m) / (2 * eps_step * J_base)

    dYu_2f, dYd_2f = _beta_bpv_quark_2loop(Yu_b, Yd_b, False, True, True, False)
    J2f_p, _, _ = _jarlskog_and_ckm_from_svd(Yu_b + eps_step * dYu_2f, Yd_b + eps_step * dYd_2f)
    J2f_m, _, _ = _jarlskog_and_ckm_from_svd(Yu_b - eps_step * dYu_2f, Yd_b - eps_step * dYd_2f)
    num_2loop_full = (J2f_p - J2f_m) / (2 * eps_step * J_base)

    passed = bool(
        sym_1loop == sp.Integer(3)
        and sym_2loop_cd == sp.Rational(-11, 2)
        and sym_2loop_full == sp.Integer(-13)
        and abs(num_1loop - 3) < 2 / 1000
        and abs(num_2loop_cd - (-11 / 2)) < 2 / 1000
        and abs(num_2loop_full - (-13)) < 3 / 1000
    )
    return {
        "symbolic_1loop_slope": str(sym_1loop),
        "symbolic_2loop_cd_matrix_slope": str(sym_2loop_cd),
        "symbolic_2loop_with_Y2S_slope": str(sym_2loop_full),
        "numerical_1loop_slope": float(num_1loop),
        "numerical_2loop_cd_matrix_slope": float(num_2loop_cd),
        "numerical_2loop_with_Y2S_slope": float(num_2loop_full),
        "passed": passed,
    }


def _random_haar_unitary(rng: np.random.Generator, special: bool) -> np.ndarray:
    raw = (rng.standard_normal((3, 3)) + I_UNIT * rng.standard_normal((3, 3))) / math.sqrt(2)
    q_mat, r_mat = np.linalg.qr(raw)
    diag_r = np.diag(r_mat)
    phases = diag_r / np.abs(diag_r)
    u_mat = q_mat * phases[None, :]
    if special:
        det_u = np.linalg.det(u_mat)
        angle_det = math.atan2(float(det_u.imag), float(det_u.real))
        u_mat = u_mat * complex(math.cos(-angle_det / 3), math.sin(-angle_det / 3))
    return u_mat


def _rk4_integrate_yukawas(
    Yu_0: np.ndarray,
    Yd_0: np.ndarray,
    dt_total: int,
    n_steps: int,
) -> tuple[np.ndarray, np.ndarray]:
    h_step = float(Fraction(dt_total, n_steps))
    Yu = Yu_0.copy()
    Yd = Yd_0.copy()
    for _ in range(n_steps):
        k1_u, k1_d = _beta_bpv_quark_2loop(Yu, Yd)
        k2_u, k2_d = _beta_bpv_quark_2loop(Yu + (h_step / 2) * k1_u, Yd + (h_step / 2) * k1_d)
        k3_u, k3_d = _beta_bpv_quark_2loop(Yu + (h_step / 2) * k2_u, Yd + (h_step / 2) * k2_d)
        k4_u, k4_d = _beta_bpv_quark_2loop(Yu + h_step * k3_u, Yd + h_step * k3_d)
        Yu = Yu + (h_step / 6) * (k1_u + 2 * k2_u + 2 * k3_u + k4_u)
        Yd = Yd + (h_step / 6) * (k1_d + 2 * k2_d + 2 * k3_d + k4_d)
    return Yu, Yd


def run_section_2_su2l_strong_cp_and_ckm() -> dict[str, Any]:
    tau_im = 2 * math.sqrt(3)
    tau_cusp = I_UNIT * tau_im
    eta_val = 23 / 100
    xi_shared = I_UNIT * eta_val
    zeta_R = np.conj(xi_shared)

    Y_quad42, psi_L_shared, d_area, ortho_L, ortho_H = _build_cim_overlap_quadrature(
        42, tau_cusp, xi_shared, zeta_R, ZERO_C
    )
    Y_quad54, _, _, _, _ = _build_cim_overlap_quadrature(
        54, tau_cusp, xi_shared, zeta_R, ZERO_C
    )
    Y_theta = _build_cim_overlap_theta_series(tau_im, eta_val)

    quad_conv_err = float(np.max(np.abs(Y_quad54 - Y_quad42)))
    quad_vs_theta_err = float(np.max(np.abs(Y_quad42 - Y_theta)))

    z_probe = np.array([[17 / 100 + tau_cusp * (41 / 100)]], dtype=np.complex128)
    half = float(Fraction(1, 2))
    zero_f = float(Fraction(0, 1))
    torus_period_err = float(Fraction(0, 1))
    for i in range(3):
        for j in range(3):
            for k in range(6):
                val_0 = (
                    _psi_cim_torus(z_probe, i, 3, half, half, xi_shared, tau_cusp)
                    * _psi_cim_torus(z_probe, j, 3, half, half, zeta_R, tau_cusp)
                    * np.conj(_psi_cim_torus(z_probe, k, 6, zero_f, zero_f, ZERO_C, tau_cusp))
                )
                val_1 = (
                    _psi_cim_torus(z_probe + 1, i, 3, half, half, xi_shared, tau_cusp)
                    * _psi_cim_torus(z_probe + 1, j, 3, half, half, zeta_R, tau_cusp)
                    * np.conj(_psi_cim_torus(z_probe + 1, k, 6, zero_f, zero_f, ZERO_C, tau_cusp))
                )
                val_t = (
                    _psi_cim_torus(z_probe + tau_cusp, i, 3, half, half, xi_shared, tau_cusp)
                    * _psi_cim_torus(z_probe + tau_cusp, j, 3, half, half, zeta_R, tau_cusp)
                    * np.conj(_psi_cim_torus(z_probe + tau_cusp, k, 6, zero_f, zero_f, ZERO_C, tau_cusp))
                )
                torus_period_err = max(
                    torus_period_err,
                    float(np.abs(val_1 - val_0)[0, 0]),
                    float(np.abs(val_t - val_0)[0, 0]),
                )

    d_parity_tensor_err = max(
        float(abs(Y_quad42[2 - i, 2 - j, (-k) % 6] - np.conj(Y_quad42[j, i, k])))
        for i in range(3)
        for j in range(3)
        for k in range(6)
    )

    P_flip = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=np.complex128)
    v_u = np.array(
        [
            1 / 2,
            (2 + 3 * I_UNIT) / 5,
            (-1 + 2 * I_UNIT) / 5,
            1 / 4,
            (-1 - 2 * I_UNIT) / 5,
            (2 - 3 * I_UNIT) / 5,
        ],
        dtype=np.complex128,
    )
    v_d = np.array(
        [
            1 / 2,
            (-3 + 4 * I_UNIT) / 10,
            (2 + I_UNIT) / 5,
            -3 / 10,
            (2 - I_UNIT) / 5,
            (-3 - 4 * I_UNIT) / 10,
        ],
        dtype=np.complex128,
    )

    v_d_parity_err = max(
        max(float(abs(v_u[(-k) % 6] - np.conj(v_u[k]))), float(abs(v_d[(-k) % 6] - np.conj(v_d[k]))))
        for k in range(6)
    )

    Yu_uv = np.einsum("ijk,k->ij", Y_quad42, v_u) @ P_flip
    Yd_uv = np.einsum("ijk,k->ij", Y_quad42, v_d) @ P_flip
    if float(np.linalg.det(Yu_uv @ Yd_uv).real) < 0:
        v_d = -v_d
        Yd_uv = -Yd_uv

    herm_err_u = float(np.linalg.norm(Yu_uv - Yu_uv.conj().T, ord="fro"))
    herm_err_d = float(np.linalg.norm(Yd_uv - Yd_uv.conj().T, ord="fro"))

    det_uv = complex(np.linalg.det(Yu_uv @ Yd_uv))
    bar_theta_uv = math.atan2(det_uv.imag, det_uv.real)
    J_uv_svd, J_uv_comm, _ = _jarlskog_and_ckm_from_svd(Yu_uv, Yd_uv)

    bbo_gate = _verify_bbo_benchmark_gate()

    def _pack(Yu: np.ndarray, Yd: np.ndarray) -> np.ndarray:
        flat = np.concatenate([Yu.ravel(), Yd.ravel()])
        return np.concatenate([flat.real, flat.imag])

    def _unpack(state: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        comp = state[:18] + I_UNIT * state[18:]
        return comp[:9].reshape(3, 3), comp[9:].reshape(3, 3)

    def _ode_rhs(_t: float, state: np.ndarray) -> np.ndarray:
        Yu_cur, Yd_cur = _unpack(state)
        dYu_cur, dYd_cur = _beta_bpv_quark_2loop(Yu_cur, Yd_cur)
        return _pack(dYu_cur, dYd_cur)

    sol = solve_ivp(
        _ode_rhs,
        (0, -30),
        _pack(Yu_uv, Yd_uv),
        method="DOP853",
        rtol=3 * ((1 / 10) ** 14),
        atol=(1 / 10) ** 15,
    )
    Yu_ir, Yd_ir = _unpack(sol.y[:, -1])
    Yu_rk4, Yd_rk4 = _rk4_integrate_yukawas(Yu_uv, Yd_uv, dt_total=-30, n_steps=1600)
    ode_cross_err = float(
        max(np.linalg.norm(Yu_ir - Yu_rk4, ord="fro"), np.linalg.norm(Yd_ir - Yd_rk4, ord="fro"))
    )

    det_ir = complex(np.linalg.det(Yu_ir @ Yd_ir))
    bar_theta_ir = math.atan2(det_ir.imag, det_ir.real)
    J_ir_svd, J_ir_comm, V_ir_abs = _jarlskog_and_ckm_from_svd(Yu_ir, Yd_ir)
    ir_nonherm_norm = float(np.linalg.norm(Yu_ir - Yu_ir.conj().T, ord="fro"))

    rng = np.random.default_rng(20260909)
    max_haar_j_diff = float(Fraction(0, 1))
    max_haar_v_diff = float(Fraction(0, 1))
    max_haar_theta_su3_diff = float(Fraction(0, 1))
    for _ in range(10):
        U_Q = _random_haar_unitary(rng, special=True)
        U_uR = _random_haar_unitary(rng, special=True)
        U_dR = _random_haar_unitary(rng, special=True)
        Yu_scr = U_Q @ Yu_ir @ U_uR.conj().T
        Yd_scr = U_Q @ Yd_ir @ U_dR.conj().T
        J_scr, _, V_scr_abs = _jarlskog_and_ckm_from_svd(Yu_scr, Yd_scr)
        det_scr = complex(np.linalg.det(Yu_scr @ Yd_scr))
        theta_scr = math.atan2(det_scr.imag, det_scr.real)
        max_haar_j_diff = max(max_haar_j_diff, abs(abs(J_scr) - abs(J_ir_svd)), abs(J_scr - J_ir_svd))
        max_haar_v_diff = max(max_haar_v_diff, float(np.max(np.abs(V_scr_abs - V_ir_abs))))
        max_haar_theta_su3_diff = max(max_haar_theta_su3_diff, abs(theta_scr - bar_theta_ir))

        U_Q_gen = _random_haar_unitary(rng, special=False)
        U_uR_gen = _random_haar_unitary(rng, special=False)
        U_dR_gen = _random_haar_unitary(rng, special=False)
        J_u3, _, V_u3_abs = _jarlskog_and_ckm_from_svd(
            U_Q_gen @ Yu_ir @ U_uR_gen.conj().T,
            U_Q_gen @ Yd_ir @ U_dR_gen.conj().T,
        )
        max_haar_j_diff = max(max_haar_j_diff, abs(abs(J_u3) - abs(J_ir_svd)))
        max_haar_v_diff = max(max_haar_v_diff, float(np.max(np.abs(V_u3_abs - V_ir_abs))))

    # PF9.2: Splitting z_{u_L} != z_{d_L} inside Q_L breaks SU(2)_L doublet covariance
    U_su2_flip = np.array([[0, 1], [-1, 0]], dtype=np.complex128)
    _, psi_L_split_d, _, _, _ = _build_cim_overlap_quadrature(
        42, tau_cusp, I_UNIT * (47 / 100), zeta_R, ZERO_C
    )

    def _su2l_profile_commutator_l2(p_u: np.ndarray, p_d: np.ndarray) -> float:
        zeros_p = np.zeros_like(p_u)
        prof_op = np.array([[p_u, zeros_p], [zeros_p, p_d]], dtype=np.complex128)
        comm = np.einsum("ab,bcixy->acixy", U_su2_flip, prof_op) - np.einsum(
            "abixy,bc->acixy", prof_op, U_su2_flip
        )
        return float(math.sqrt(float(np.sum(np.abs(comm) ** 2) * d_area)))

    su2_shared_defect = _su2l_profile_commutator_l2(psi_L_shared, psi_L_shared)
    su2_split_l2_defect = _su2l_profile_commutator_l2(psi_L_shared, psi_L_split_d)
    pf9_2_caught = bool(su2_shared_defect < (1 / 10) ** 14 and su2_split_l2_defect > 1 / 10)

    # PF9.3: Opposite D-parity determinant-sign branch v_d -> -v_d on odd N_g = 3
    det_opp = complex(np.linalg.det(Yu_uv @ (-Yd_uv)))
    bar_theta_pf93 = abs(math.atan2(det_opp.imag, det_opp.real))
    pf9_3_caught = bool(det_opp.real < 0 and bar_theta_pf93 > 3 and abs(bar_theta_pf93 - math.pi) < (1 / 10) ** 14)

    tol_14 = (1 / 10) ** 14
    tol_13 = (1 / 10) ** 13
    passed = bool(
        ortho_L < tol_14
        and ortho_H < tol_14
        and quad_conv_err < tol_14
        and quad_vs_theta_err < tol_14
        and torus_period_err < tol_13
        and d_parity_tensor_err < tol_14
        and v_d_parity_err == 0
        and det_uv.real > 0
        and herm_err_u < tol_14
        and herm_err_d < tol_14
        and abs(bar_theta_uv) < tol_14
        and abs(J_uv_svd) > 1 / 50
        and abs(J_uv_svd - J_uv_comm) < tol_14
        and bbo_gate["passed"]
        and ode_cross_err < (1 / 10) ** 12
        and abs(bar_theta_ir) < tol_13
        and abs(J_ir_svd) > 1 / 100
        and abs(J_ir_svd - J_ir_comm) < tol_13
        and max_haar_j_diff < tol_13
        and max_haar_v_diff < tol_13
        and max_haar_theta_su3_diff < tol_13
        and pf9_2_caught
        and pf9_3_caught
    )
    return {
        "tau_cusp": "2*sqrt(3)*i",
        "shared_xi": "23*i/100",
        "orthonormality_err_L": ortho_L,
        "orthonormality_err_H": ortho_H,
        "quadrature_42_vs_54_err": quad_conv_err,
        "quadrature_vs_1d_theta_err": quad_vs_theta_err,
        "torus_gauge_periodicity_err": torus_period_err,
        "d_parity_tensor_conjugation_err": d_parity_tensor_err,
        "hermiticity_err_Yu_uv": herm_err_u,
        "hermiticity_err_Yd_uv": herm_err_d,
        "det_YuYd_uv": float(det_uv.real),
        "abs_bar_theta_QCD_uv": abs(bar_theta_uv),
        "abs_J_CKM_uv": abs(J_uv_svd),
        "J_svd_vs_commutator_uv_diff": abs(J_uv_svd - J_uv_comm),
        "bbo_guardrail_4_benchmark": bbo_gate,
        "rge_dt": -30,
        "dop853_vs_rk4_err": ode_cross_err,
        "ir_Yu_nonhermiticity_fro": ir_nonherm_norm,
        "abs_bar_theta_QCD_ir": abs(bar_theta_ir),
        "abs_J_CKM_ir": abs(J_ir_svd),
        "J_svd_vs_commutator_ir_diff": abs(J_ir_svd - J_ir_comm),
        "haar_10_trials_max_J_diff": max_haar_j_diff,
        "haar_10_trials_max_V_diff": max_haar_v_diff,
        "haar_10_trials_max_theta_su3_diff": max_haar_theta_su3_diff,
        "PF9_2_su2l_shared_defect": su2_shared_defect,
        "PF9_2_su2l_split_defect": su2_split_l2_defect,
        "PF9_2_caught": pf9_2_caught,
        "PF9_3_opposite_branch_abs_theta": bar_theta_pf93,
        "PF9_3_caught": pf9_3_caught,
        "passed": passed,
    }


def _mp_sl2z_gauss_reduce(t_mp: mp.mpc) -> tuple[mp.mpc, tuple[int, int, int, int]]:
    with mp.workdps(50):
        a, b, c, d = 1, 0, 0, 1
        half_mp = mp.mpf(1) / mp.mpf(2)
        one_mp = mp.mpf(1)
        eps_mp = mp.mpf(10) ** (-35)
        for _ in range(200):
            z_cur = (a * t_mp + b) / (c * t_mp + d)
            k_shift = int(mp.floor(mp.re(z_cur) + half_mp))
            if k_shift != 0:
                a = a - k_shift * c
                b = b - k_shift * d
                z_cur = (a * t_mp + b) / (c * t_mp + d)
            norm_sq = mp.re(z_cur) ** 2 + mp.im(z_cur) ** 2
            if norm_sq < one_mp - eps_mp:
                # Left-multiplication by S = [[0, -1], [1, 0]]
                a, b, c, d = -c, -d, a, b
            else:
                if abs(norm_sq - one_mp) <= eps_mp and mp.re(z_cur) < 0:
                    a, b, c, d = -c, -d, a, b
                    z_cur = (a * t_mp + b) / (c * t_mp + d)
                return z_cur, (a, b, c, d)
        raise RuntimeError("SL(2, Z) Gauss reduction exceeded iteration bound")


def _sl2z_matmul(g1: tuple[int, int, int, int], g2: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    a1, b1, c1, d1 = g1
    a2, b2, c2, d2 = g2
    return (
        a1 * a2 + b1 * c2,
        a1 * b2 + b1 * d2,
        c1 * a2 + d1 * c2,
        c1 * b2 + d1 * d2,
    )


def run_section_3_p864_repair_and_sweep(repo_root: Path) -> dict[str, Any]:
    grid_path = next((repo_root / "frontier").glob("B1927_*/verification/grid.json"))
    cusp_path = next((repo_root / "frontier").glob("B1667_*/verification/the_canonical_cusp.json"))
    grid_json = json.loads(grid_path.read_bytes().decode("utf-8"))
    cusp_json = json.loads(cusp_path.read_bytes().decode("utf-8"))

    dedup_pts: dict[tuple[int, int], tuple[float, float, float, float]] = {}
    scale_key = 10 ** 9
    for pt in grid_json["grid"]:
        tx, ty = float(pt["tau"][0]), float(pt["tau"][1])
        dedup_pts[(round(tx * scale_key), round(ty * scale_key))] = (
            tx,
            ty,
            float(pt["L_2"]),
            float(pt["L_max"]),
        )
    for pt in cusp_json["points"]:
        tx, ty = float(pt["tau"][0]), float(pt["tau"][1])
        dedup_pts[(round(tx * scale_key), round(ty * scale_key))] = (
            tx,
            ty,
            float(pt["L_2"]),
            float(pt["L_max"]),
        )

    y_max_val = max(row[1] for row in dedup_pts.values())

    # 1. Unreduced mirrored table (reproducing main's P-864 behavior on [-1/2, +1/2])
    xy_unred: list[list[float]] = []
    v_l2_unred: list[float] = []
    v_lmax_unred: list[float] = []
    tiny = (1 / 10) ** 14
    for tx, ty, l2_v, lmax_v in dedup_pts.values():
        xy_unred.append([tx, ty])
        v_l2_unred.append(l2_v)
        v_lmax_unred.append(lmax_v)
        if abs(tx) > tiny:
            xy_unred.append([-tx, ty])
            v_l2_unred.append(l2_v)
            v_lmax_unred.append(lmax_v)

    xy_unred_arr = np.asarray(xy_unred, dtype=np.float64)
    lin_l2_unred = LinearNDInterpolator(xy_unred_arr, np.asarray(v_l2_unred, dtype=np.float64))
    near_l2_unred = NearestNDInterpolator(xy_unred_arr, np.asarray(v_l2_unred, dtype=np.float64))

    def _canon_unreduced_l2(z_c: complex) -> tuple[float, bool]:
        q_pt = np.array([[z_c.real, z_c.imag]], dtype=np.float64)
        lin_v = float(lin_l2_unred(q_pt)[0])
        used_nearest = bool(math.isnan(lin_v))
        if used_nearest:
            return float(near_l2_unred(q_pt)[0]), True
        return lin_v, False

    # 2. Repaired periodic + mirrored fundamental-domain table with Gauss reduction
    xy_fd: list[list[float]] = []
    v_l2_fd: list[float] = []
    v_lmax_fd: list[float] = []
    bound_x = 13 / 20
    for tx, ty, l2_v, lmax_v in dedup_pts.values():
        signs = [tx, -tx] if abs(tx) > tiny else [float(Fraction(0, 1))]
        for sx in signs:
            for shift_n in (-1, 0, 1):
                x_sh = sx + shift_n
                if -bound_x <= x_sh <= bound_x:
                    xy_fd.append([x_sh, ty])
                    v_l2_fd.append(l2_v)
                    v_lmax_fd.append(lmax_v)

    xy_fd_arr = np.asarray(xy_fd, dtype=np.float64)
    lin_l2_fd = LinearNDInterpolator(xy_fd_arr, np.asarray(v_l2_fd, dtype=np.float64))
    near_l2_fd = NearestNDInterpolator(xy_fd_arr, np.asarray(v_l2_fd, dtype=np.float64))
    lin_lmax_fd = LinearNDInterpolator(xy_fd_arr, np.asarray(v_lmax_fd, dtype=np.float64))
    near_lmax_fd = NearestNDInterpolator(xy_fd_arr, np.asarray(v_lmax_fd, dtype=np.float64))

    def canon_gauss_reduced(t_mp: mp.mpc) -> dict[str, Any]:
        with mp.workdps(50):
            z_fd, (a, b, c, d) = _mp_sl2z_gauss_reduce(t_mp)
            det_ok = bool(a * d - b * c == 1)
            in_fd_ok = bool(
                abs(mp.re(z_fd)) <= mp.mpf(1) / mp.mpf(2) + mp.mpf(10) ** (-30)
                and mp.re(z_fd) ** 2 + mp.im(z_fd) ** 2 >= mp.mpf(1) - mp.mpf(10) ** (-30)
            )
            x_fd = abs(float(mp.re(z_fd)))
            y_fd = float(mp.im(z_fd))
            above_ymax = bool(y_fd > y_max_val)
            y_eval = min(y_fd, y_max_val)
            q_pt = np.array([[x_fd, y_eval]], dtype=np.float64)

            val_l2 = float(lin_l2_fd(q_pt)[0])
            if math.isnan(val_l2):
                val_l2 = float(near_l2_fd(q_pt)[0])
            val_lmax = float(lin_lmax_fd(q_pt)[0])
            if math.isnan(val_lmax):
                val_lmax = float(near_lmax_fd(q_pt)[0])

            log_aut = float(mp.log(abs(c * t_mp + d)))
            return {
                "L_2": val_l2 - log_aut,
                "L_max": val_lmax - log_aut,
                "z_FD": [float(mp.re(z_fd)), y_fd],
                "sl2z_matrix": [a, b, c, d],
                "det_is_1": det_ok,
                "in_fundamental_domain": in_fd_ok,
                "above_ymax": above_ymax,
            }

    S_mat = (0, -1, 1, 0)
    T_mat = (1, 1, 0, 1)
    Tinv_mat = (1, -1, 0, 1)
    words: list[tuple[str, tuple[int, int, int, int]]] = [
        ("S", S_mat),
        ("T", T_mat),
        ("T^-1", Tinv_mat),
        ("S*T", _sl2z_matmul(S_mat, T_mat)),
        ("T*S", _sl2z_matmul(T_mat, S_mat)),
        ("S*T^2*S", _sl2z_matmul(S_mat, _sl2z_matmul(T_mat, _sl2z_matmul(T_mat, S_mat)))),
        ("T^-2*S*T*S", _sl2z_matmul(Tinv_mat, _sl2z_matmul(Tinv_mat, _sl2z_matmul(S_mat, _sl2z_matmul(T_mat, S_mat))))),
        (
            "S*T^-3*S*T^2*S",
            _sl2z_matmul(
                S_mat,
                _sl2z_matmul(
                    Tinv_mat,
                    _sl2z_matmul(
                        Tinv_mat,
                        _sl2z_matmul(
                            Tinv_mat,
                            _sl2z_matmul(S_mat, _sl2z_matmul(T_mat, _sl2z_matmul(T_mat, S_mat))),
                        ),
                    ),
                ),
            ),
        ),
    ]

    with mp.workdps(50):
        base_points: list[tuple[str, mp.mpc]] = [
            ("13/100 + 17/10 i", mp.mpc(mp.mpf(13) / 100, mp.mpf(17) / 10)),
            ("9/10 i", mp.mpc(0, mp.mpf(9) / 10)),
            ("3/10 + 96/100 i", mp.mpc(mp.mpf(3) / 10, mp.mpf(96) / 100)),
        ]

        max_cov_defect_l2 = float(Fraction(0, 1))
        max_cov_defect_lmax = float(Fraction(0, 1))
        det_fd_checks: list[bool] = []

        for _, t_pt in base_points:
            base_eval = canon_gauss_reduced(t_pt)
            det_fd_checks.append(
                bool(
                    base_eval["det_is_1"]
                    and base_eval["in_fundamental_domain"]
                    and (not base_eval["above_ymax"])
                )
            )
            for _, (ga, gb, gc, gd) in words:
                det_w = ga * gd - gb * gc
                gamma_t = (ga * t_pt + gb) / (gc * t_pt + gd)
                w_eval = canon_gauss_reduced(gamma_t)
                log_factor = float(mp.log(abs(gc * t_pt + gd)))
                def_l2 = abs(w_eval["L_2"] - base_eval["L_2"] - log_factor)
                def_lmax = abs(w_eval["L_max"] - base_eval["L_max"] - log_factor)
                max_cov_defect_l2 = max(max_cov_defect_l2, def_l2)
                max_cov_defect_lmax = max(max_cov_defect_lmax, def_lmax)
                det_fd_checks.append(
                    bool(
                        det_w == 1
                        and w_eval["det_is_1"]
                        and w_eval["in_fundamental_domain"]
                        and (not w_eval["above_ymax"])
                    )
                )
        all_dets_and_fd_ok = bool(len(det_fd_checks) > 0 and all(det_fd_checks))

    # Chord-lens geometric proof and PF9.4 unreduced defect verification
    t1_c = (13 / 100) + I_UNIT * (17 / 10)
    t2_c = I_UNIT * (9 / 10)
    t3_c = (3 / 10) + I_UNIT * (96 / 100)
    minus_inv_t1 = -1 / t1_c
    minus_inv_t2 = -1 / t2_c
    minus_inv_t3 = -1 / t3_c

    sqrt3_half = math.sqrt(3) / 2
    t2_in_chord_lens = bool(sqrt3_half <= t2_c.imag < math.sqrt(1 - t2_c.real ** 2))
    minv_t3_in_chord_lens = bool(
        sqrt3_half <= minus_inv_t3.imag < math.sqrt(1 - minus_inv_t3.real ** 2)
    )

    val_t1_u, _ = _canon_unreduced_l2(t1_c)
    val_minv_t1_u, nearest_used_t1 = _canon_unreduced_l2(minus_inv_t1)
    pf9_4_defect_t1 = abs(val_minv_t1_u - (val_t1_u + math.log(abs(t1_c))))

    val_t2_u, nearest_used_t2 = _canon_unreduced_l2(t2_c)
    val_minv_t2_u, _ = _canon_unreduced_l2(minus_inv_t2)
    pf9_4_defect_09i = abs(val_minv_t2_u - (val_t2_u + math.log(abs(t2_c))))

    val_t3_u, _ = _canon_unreduced_l2(t3_c)
    val_minv_t3_u, nearest_used_minv_t3 = _canon_unreduced_l2(minus_inv_t3)
    pf9_4_defect_t3 = abs(val_minv_t3_u - (val_t3_u + math.log(abs(t3_c))))

    pf9_4_caught = bool(
        nearest_used_t1
        and pf9_4_defect_t1 > 1 / 4
        and t2_in_chord_lens
        and (not nearest_used_t2)
        and pf9_4_defect_09i > 1 / 1000
        and minv_t3_in_chord_lens
        and (not nearest_used_minv_t3)
        and pf9_4_defect_t3 > 1 / 10000
    )

    # PF9.5: Explicit above_ymax flag when Im(z_FD) = 10 > Y_max = 6
    with mp.workdps(50):
        high_eval_direct = canon_gauss_reduced(mp.mpc(0, 10))
        high_eval_inverted = canon_gauss_reduced(mp.mpc(0, mp.mpf(1) / 10))
    pf9_5_caught = bool(
        high_eval_direct["above_ymax"]
        and high_eval_inverted["above_ymax"]
        and y_max_val == 6
    )

    # Read-only coordinate sweep across tracked JSON files in B1927..B1949
    target_prefixes = (
        "B1927_",
        "B1928_",
        "B1940_",
        "B1941_",
        "B1944_",
        "B1945_",
        "B1946_",
        "B1949_",
    )
    json_paths = sorted(
        p
        for d in (repo_root / "frontier").iterdir()
        if d.is_dir() and d.name.startswith(target_prefixes)
        for p in d.rglob("*.json")
    )

    explicit_tau_count = 0
    below_unit_circle_entries: list[dict[str, Any]] = []
    min_abs_tau = float(10 ** 6)
    max_im_tau = float(0)
    b1945_defect_keys_found: list[dict[str, Any]] = []

    for jp in json_paths:
        rel_jp = str(jp.relative_to(repo_root))
        payload = json.loads(jp.read_bytes().decode("utf-8"))

        def _walk_json(node: Any, jpath: str) -> None:
            nonlocal explicit_tau_count, min_abs_tau, max_im_tau
            if isinstance(node, dict):
                for k_str, val in node.items():
                    if "table_law_defect" in k_str:
                        b1945_defect_keys_found.append({"file": rel_jp, "key": k_str, "value": val})
                    if (
                        k_str == "tau"
                        and isinstance(val, list)
                        and len(val) == 2
                        and all(isinstance(coord, (int, float)) for coord in val)
                    ):
                        re_v, im_v = float(val[0]), float(val[1])
                        mod_v = math.hypot(re_v, im_v)
                        explicit_tau_count += 1
                        min_abs_tau = min(min_abs_tau, mod_v)
                        max_im_tau = max(max_im_tau, im_v)
                        if mod_v < 1 - (1 / 10) ** 12:
                            below_unit_circle_entries.append(
                                {"file": rel_jp, "path": f"{jpath}.tau", "tau": [re_v, im_v], "abs_tau": mod_v}
                            )
                    _walk_json(val, f"{jpath}.{k_str}")
            elif isinstance(node, list):
                for idx, item in enumerate(node):
                    _walk_json(item, f"{jpath}[{idx}]")

        _walk_json(payload, "")

    tol_14 = (1 / 10) ** 14
    passed = bool(
        all_dets_and_fd_ok
        and max_cov_defect_l2 < tol_14
        and max_cov_defect_lmax < tol_14
        and pf9_4_caught
        and pf9_5_caught
        and len(json_paths) == 24
        and explicit_tau_count == 1175
        and len(below_unit_circle_entries) == 0
        and min_abs_tau >= 1
    )
    return {
        "interpolator_unique_right_half_points": len(dedup_pts),
        "Y_max": y_max_val,
        "sl2z_words_tested_per_point": len(words),
        "all_sl2z_dets_and_fd_bounds_ok": all_dets_and_fd_ok,
        "max_sl2z_covariance_defect_L_2": max_cov_defect_l2,
        "max_sl2z_covariance_defect_L_max": max_cov_defect_lmax,
        "chord_lens_verified_at_9_over_10_i": t2_in_chord_lens,
        "chord_lens_verified_at_minus_inv_3_10_plus_96_100_i": minv_t3_in_chord_lens,
        "PF9_4_unreduced_defect_at_minus_inv_t1": pf9_4_defect_t1,
        "PF9_4_unreduced_defect_at_9_over_10_i": pf9_4_defect_09i,
        "PF9_4_unreduced_defect_at_3_10_plus_96_100_i": pf9_4_defect_t3,
        "PF9_4_caught": pf9_4_caught,
        "PF9_5_above_ymax_at_10i": high_eval_direct["above_ymax"],
        "PF9_5_above_ymax_at_inv_10i": high_eval_inverted["above_ymax"],
        "PF9_5_caught": pf9_5_caught,
        "sweep_json_file_count": len(json_paths),
        "sweep_explicit_tau_count": explicit_tau_count,
        "sweep_explicit_tau_below_unit_circle_count": len(below_unit_circle_entries),
        "sweep_min_abs_tau": min_abs_tau,
        "sweep_max_im_tau": max_im_tau,
        "b1945_diagnostic_defect_keys": b1945_defect_keys_found,
        "passed": passed,
    }


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]
    out_path = script_path.parent / "referee_found_g9_out.json"

    sec0 = run_section_0_custody_and_ast_lock(script_path, repo_root)
    sec1 = run_section_1_domain_wall_localization()
    sec2 = run_section_2_su2l_strong_cp_and_ckm()
    sec3 = run_section_3_p864_repair_and_sweep(repo_root)

    planted_faults = {
        "PF9_1_caught": sec1["PF9_1_caught"],
        "PF9_2_caught": sec2["PF9_2_caught"],
        "PF9_3_caught": sec2["PF9_3_caught"],
        "PF9_4_caught": sec3["PF9_4_caught"],
        "PF9_5_caught": sec3["PF9_5_caught"],
    }
    all_planted_caught = all(planted_faults.values())
    overall_passed = bool(
        sec0["passed"]
        and sec1["passed"]
        and sec2["passed"]
        and sec3["passed"]
        and all_planted_caught
    )

    report = {
        "gate": "AGY-002_FOUND-G9_COLD_ROOM_REFEREE",
        "empirical_inputs": "0 of 19",
        "section_0_custody_and_ast_lock": sec0,
        "section_1_domain_wall_localization": sec1,
        "section_2_su2l_strong_cp_and_ckm": sec2,
        "section_3_p864_repair_and_sweep": sec3,
        "planted_fault_summary": planted_faults,
        "all_5_planted_faults_caught": all_planted_caught,
        "overall_passed": overall_passed,
    }
    out_path.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    if not overall_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
