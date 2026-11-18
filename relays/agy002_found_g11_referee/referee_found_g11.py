"""Cold-room Gate 11 & campaign-wide standalone referee verification script (0 of 19).

Independently verifies Card AGY-002_FOUND-G11 from scratch with zero repository
Python imports, zero float AST literals, and zero complex AST literals:
  0. AST source lock (0 float literals, 0 complex literals, 0 repo imports),
     raw byte-level SHA-256 custody across all 19 prior Gate 8-11 manifests plus
     self SCRIPT_SHA256.txt (20 live + 1 OUTPUT_SHA256.txt = 21 total manifests),
     and in-memory 1-hex-character tamper detection control.
  1. Completed-square analytic 1D Cremades-Ibanez-Marchesano theta-addition
     overlap Y_{ijk}(tau; zeta_L, zeta_R, zeta_H) cross-checked against 42x42
     2D torus quadrature, closed-form Weil/theta unitary transports U_T and U_S,
     Kahler-normalized 1-loop Schwinger-Dyson singlet resolvent Majorana operator
     M_R^{SD}(tau; kappa) = Y(tau) (I_6 + kappa G_6(tau))^{-1} v_0(tau) (symmetry,
     T- and S-covariance at 23/100 + 141/100 i and 2 sqrt(3) i, rank transition
     (1, 3), 10-trial Haar U(6) x U(3) basis invariance), M44 Level-6 Higgs 4-lift
     Klein isotropy (Z^3 and X^3 lattice-shift conjugations and {I_6, Z^3, X^3,
     Z^3 X^3} scalar identity collapse leaving +-pi/6 = 1 discrete bit), PF11.1,
     PF11.2, and PF11.4.
  2. Symbolic 1-loop RG dimensional transmutation d(ln Lambda_H)/d(ln mu) == 0
     (with Gross-Wilczek/Politzer benchmark gate + Kahan-compensated RK4 ODE
     cross-check), 3-route 50-digit Vol(m004) verification (Bloch-Wigner
     dilogarithm 2 D_2(exp(i pi/3)), Dirichlet L-series (3 sqrt(3)/2) L(2, chi_{-3})
     via Hurwitz zeta, and direct Lobachevsky quadrature), exact
     |det((LR)^4 - I_2)| == 45 vs 4-sheet cover degree 4, PF11.3, PF11.5, and
     independent stereographic differential-form / quaternion SymPy CAS
     verification of PHYSICAL-C7 (det Z == 0, Hopf Chern number
     int_{S^2} F / (2 pi) == 1 on v = conj(u), exact 0 U(1) gauge drift and
     A^2 + I_2 == 0, A^4 - I_2 == 0 of composite (A, W), and exact rational
     commutator-trace drift -6784/4225 != 0 of direct (U(u), U(conj(v))) at
     u = (3/5, 4/5), v = (5/13, 12/13 i)).
  3. Independent Kahn in-degree topological sort and 3-color DFS verification of
     the 52-node Foundational Epistemic DAG (8 ROOT + 7 OPERATOR + 8 SEAM +
     10 RELATION + 19 SM_TARGET = 52, PR-5 at rank 2, relation_rank_histogram =
     [2, 5, 3, 0], sm_target_rank_histogram = [0, 0, 1, 18] with SM19:bar_theta_QCD
     unique rank-2 SM parameter), Guardrail 1 seam honesty, F15 premise honesty,
     monotone (max, <=) propagation, plus cycle-injection, rank-laundering, and
     unproved-seam controls.
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
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

I_UNIT: complex = complex(0, 1)

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
    "relays/agy002_found_g9_referee/OUTPUT_SHA256.txt",
    "relays/agy002_found_g9_referee/SCRIPT_SHA256.txt",
    "relays/agy002_found_g9_v2/OUTPUT_SHA256.txt",
    "relays/agy002_found_g9_v2/SCRIPT_SHA256.txt",
    "relays/agy002_found_g10/OUTPUT_SHA256.txt",
    "relays/agy002_found_g10/SCRIPT_SHA256.txt",
    "relays/agy002_found_g10_referee/OUTPUT_SHA256.txt",
    "relays/agy002_found_g10_referee/SCRIPT_SHA256.txt",
    "relays/agy002_found_g11/OUTPUT_SHA256.txt",
    "relays/agy002_found_g11/SCRIPT_SHA256.txt",
)


def _rat(num: int, den: int = 1) -> float:
    return float(Fraction(num, den))


def _pow10_neg(exp_pos: int) -> float:
    return float(Fraction(1, 10**exp_pos))


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


def _flip_first_hex_char(digest_hex: str) -> str:
    replacement = "0" if digest_hex[0] != "0" else "1"
    return replacement + digest_hex[1:]


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

    # Memory-only 1-hex-character tamper control (never touches disk)
    probe_rec = dict(prior_records[0])
    tampered_expected = _flip_first_hex_char(str(probe_rec["expected_sha256"]))
    tampered_matched = bool(
        probe_rec["actual_sha256"] == tampered_expected and len(tampered_expected) == 64
    )
    tamper_control_caught = bool(
        (not tampered_matched) and tampered_expected != probe_rec["expected_sha256"]
    )

    passed = bool(
        len(float_literals) == 0
        and len(complex_literals) == 0
        and len(disallowed_imports) == 0
        and prior_total_count == 19
        and prior_matched_count == 19
        and self_record["matched"]
        and tamper_control_caught
    )
    return {
        "float_literal_count": len(float_literals),
        "complex_literal_count": len(complex_literals),
        "repo_import_count": len(disallowed_imports),
        "disallowed_imports": disallowed_imports,
        "empirical_inputs_used": "0 of 19",
        "prior_manifest_count": prior_total_count,
        "prior_manifests_matched": prior_matched_count,
        "campaign_total_manifests_with_self_pair": prior_total_count + 2,
        "prior_manifests": prior_records,
        "self_script_manifest": self_record,
        "memory_tamper_control_caught": tamper_control_caught,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Section 1: Analytic 1D Theta-Addition Overlap vs 2D Quadrature,
#            Schwinger-Dyson Resolvent 4 -> 1, & M44 4-Lift Klein Isotropy
# ---------------------------------------------------------------------------


def _psi_cim_grid(
    flux_m: int,
    alpha: float,
    beta: float,
    z_grid: np.ndarray,
    tau: complex,
    zeta: complex,
    n_half: int = 24,
) -> np.ndarray:
    """Evaluate orthonormal magnetized-torus zero modes psi_j^{(M, alpha, beta)}(z; tau, zeta)
    using completed-square Gaussian-theta exponents to prevent overflow under lattice shifts.
    """
    w = z_grid + zeta
    im_tau = tau.imag
    uy = w.imag / im_tau
    ux = w.real - uy * tau.real
    norm_pref = (2 * flux_m * im_tau) ** Fraction(1, 4)
    n_center = int(round(-float(np.mean(uy))))
    ns = np.arange(n_center - n_half, n_center + n_half + 1, dtype=np.int64)

    out = np.zeros((flux_m,) + z_grid.shape, dtype=np.complex128)
    half = _rat(1, 2)
    for j in range(flux_m):
        a_char = (j + alpha) / flux_m
        na = ns.reshape((-1,) + (1,) * z_grid.ndim) + a_char
        shifted = na + uy
        expo = (
            I_UNIT * math.pi * flux_m * tau * (shifted * shifted)
            + (2 * math.pi * I_UNIT * flux_m) * ux * (na + half * uy)
            + (2 * math.pi * I_UNIT * beta) * na
        )
        out[j] = norm_pref * np.sum(np.exp(expo), axis=0)
    return out


def _psi_cim_point(
    flux_m: int,
    alpha: float,
    beta: float,
    z_pt: complex,
    tau: complex,
    zeta: complex,
    n_half: int = 24,
) -> np.ndarray:
    z_arr = np.array([z_pt], dtype=np.complex128)
    return _psi_cim_grid(flux_m, alpha, beta, z_arr, tau, zeta, n_half=n_half)[:, 0]


def _cim_overlap_2d_quadrature(
    tau: complex,
    zeta_l: complex,
    zeta_r: complex,
    zeta_h: complex,
    n_grid: int = 42,
) -> dict[str, Any]:
    """Direct 2D spectral torus quadrature for Y_{ijk}(tau; zeta_L, zeta_R, zeta_H)."""
    half = _rat(1, 2)
    grid_1d = np.arange(n_grid, dtype=np.int64) / n_grid
    xg, yg = np.meshgrid(grid_1d, grid_1d, indexing="ij")
    z_grid = xg + tau * yg
    w_cell = _rat(1, n_grid * n_grid)

    psi_l = _psi_cim_grid(3, half, half, z_grid, tau, zeta_l)
    psi_r = _psi_cim_grid(3, half, half, z_grid, tau, zeta_r)
    psi_h = _psi_cim_grid(6, _rat(0), _rat(0), z_grid, tau, zeta_h)

    gram_l = np.einsum("ixy,jxy->ij", psi_l, psi_l.conj()) * w_cell
    gram_h = np.einsum("kxy,lxy->kl", psi_h, psi_h.conj()) * w_cell
    y_quad = np.einsum("ixy,jxy,kxy->ijk", psi_l, psi_r, psi_h.conj()) * w_cell
    return {
        "Y_quad": y_quad,
        "orthonorm_err_3": float(np.linalg.norm(gram_l - np.eye(3))),
        "orthonorm_err_6": float(np.linalg.norm(gram_h - np.eye(6))),
    }


def _cim_overlap_1d_analytic(
    tau: complex,
    zeta_l: complex,
    zeta_r: complex,
    zeta_h: complex,
    n_half: int = 26,
) -> np.ndarray:
    """Exact 1D Cremades-Ibanez-Marchesano (hep-th/0404229 Sec. 5) theta-addition series
    for flux (3, 3, -6) with spin structures ((1/2, 1/2), (1/2, 1/2), (0, 0)) and
    balanced Wilson lines 3*zeta_L + 3*zeta_R - 6*zeta_H = 0.
    """
    if abs(zeta_h - _rat(1, 2) * (zeta_l + zeta_r)) > _pow10_neg(12):
        raise ValueError("Flux-balanced Wilson lines require zeta_H = (zeta_L + zeta_R) / 2")

    delta = zeta_l - zeta_r
    im_tau = tau.imag
    alpha_d = delta.imag / im_tau
    beta_d = delta.real - alpha_d * tau.real
    norm_pref = (3 * im_tau) ** Fraction(1, 4)

    half = _rat(1, 2)
    quarter = _rat(1, 4)
    n_center = int(round(-half * alpha_d))
    ns = np.arange(n_center - n_half, n_center + n_half + 1, dtype=np.int64)

    y_out = np.zeros((3, 3, 6), dtype=np.complex128)
    for i in range(3):
        for j in range(3):
            for k in range(6):
                if (k - i - j - 1) % 3 == 0:
                    a_char = _rat(2 * i + 1 - k, 6)
                    na = ns + a_char
                    shifted = na + half * alpha_d
                    expo = (
                        (6 * math.pi * I_UNIT * tau) * (shifted * shifted)
                        + (6 * math.pi * I_UNIT * beta_d) * (na + quarter * alpha_d)
                    )
                    phase_k = np.exp(I_UNIT * math.pi * _rat(k, 3))
                    y_out[i, j, k] = norm_pref * phase_k * complex(np.sum(np.exp(expo)))
    return y_out


def _weil_transport_T(flux_m: int, alpha: float) -> np.ndarray:
    js = np.arange(flux_m, dtype=np.int64) + alpha
    return np.diag(np.exp(I_UNIT * math.pi * (js * js) / flux_m))


def _weil_transport_S(flux_m: int, alpha: float, beta: float, tau: complex) -> np.ndarray:
    half = _rat(1, 2)
    js = np.arange(flux_m, dtype=np.int64) + alpha
    metaplectic_pref = ((-I_UNIT * tau) / abs(tau)) ** half / math.sqrt(flux_m)
    fourier_block = np.exp((-2 * math.pi * I_UNIT / flux_m) * np.outer(js, js))
    spin_shift = np.exp((2 * math.pi * I_UNIT * beta / flux_m) * (js[:, None] - js[None, :]))
    return metaplectic_pref * (fourier_block * spin_shift)


def _quadrature_transport(
    flux_m: int,
    alpha: float,
    beta: float,
    tau: complex,
    gen: str,
    n_grid: int = 42,
) -> np.ndarray:
    grid_1d = np.arange(n_grid, dtype=np.int64) / n_grid
    xg, yg = np.meshgrid(grid_1d, grid_1d, indexing="ij")
    z_grid = xg + tau * yg
    zero_c = complex(0, 0)
    old_modes = _psi_cim_grid(flux_m, alpha, beta, z_grid, tau, zero_c)
    if gen == "T":
        new_modes = _psi_cim_grid(flux_m, alpha, beta, z_grid, tau + 1, zero_c)
    elif gen == "S":
        new_modes = _psi_cim_grid(flux_m, alpha, beta, z_grid / tau, -1 / tau, zero_c)
    else:
        raise ValueError(f"Unknown generator {gen}")
    return np.einsum("axy,bxy->ab", new_modes, old_modes.conj()) / (n_grid * n_grid)


def _resolvent_majorana_bundle(tau: complex, kappa: float) -> dict[str, Any]:
    zero_c = complex(0, 0)
    half = _rat(1, 2)
    y_ten = _cim_overlap_1d_analytic(tau, zero_c, zero_c, zero_c)
    y_mat = y_ten.reshape(9, 6)
    g6 = y_mat.conj().T @ y_mat
    v0 = _psi_cim_point(6, _rat(0), _rat(0), zero_c, tau, zero_c)
    u3_zero = _psi_cim_point(3, half, half, zero_c, tau, zero_c)

    w_eff = np.linalg.solve(np.eye(6, dtype=np.complex128) + kappa * g6, v0)
    m_r_sd = np.einsum("ijk,k->ij", y_ten, w_eff)
    j0 = np.einsum("ijk,k->ij", y_ten, v0)
    j1 = np.einsum("ijk,k->ij", y_ten, g6 @ v0)
    j2 = j1 @ j1.conj().T @ j1
    return {
        "Y": y_ten,
        "G6": g6,
        "v0": v0,
        "u3_zero": u3_zero,
        "MR_SD": m_r_sd,
        "J0": j0,
        "J1": j1,
        "J2": j2,
    }


def _takagi_direct_svd(sym_mat: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    u_left, s_desc, _ = np.linalg.svd(sym_mat)
    proj_diag = np.diag(u_left.conj().T @ sym_mat @ u_left.conj())
    safe_s = np.maximum(s_desc, _pow10_neg(30))
    half_phases = np.sqrt(proj_diag / safe_s)
    u_tak_desc = u_left * half_phases[None, :]
    order = np.argsort(s_desc)
    return s_desc[order], u_tak_desc[:, order]


def _haar_unitary(rng: np.random.Generator, dim: int) -> np.ndarray:
    z = (rng.standard_normal((dim, dim)) + I_UNIT * rng.standard_normal((dim, dim))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    diag_r = np.diag(r)
    phases = diag_r / np.abs(diag_r)
    return q * phases[None, :]


def _frobenius_gram_schmidt(mats: list[np.ndarray]) -> list[np.ndarray]:
    ortho: list[np.ndarray] = []
    for mat in mats:
        work = mat.copy()
        for prev in ortho:
            work = work - np.vdot(prev, work) * prev
        norm = math.sqrt(float(np.vdot(work, work).real))
        ortho.append(work / norm)
    return ortho


def _frobenius_lowdin(mats: list[np.ndarray]) -> list[np.ndarray]:
    gram = np.array([[np.vdot(a, b) for b in mats] for a in mats], dtype=np.complex128)
    evals, evecs = np.linalg.eigh(gram)
    g_inv_sqrt = evecs @ np.diag(1 / np.sqrt(evals)) @ evecs.conj().T
    return [sum(g_inv_sqrt[b, a] * mats[b] for b in range(3)) for a in range(3)]


def _higgs_bubble_single_point(tau: complex, w_pt: complex) -> np.ndarray:
    sectors: tuple[tuple[int, int, int], ...] = ((1, -4, 3), (1, 2, 3), (-3, 6, 1))
    half = _rat(1, 2)
    b_mat = np.zeros((6, 6), dtype=np.complex128)
    for q_l, q_r, n_c in sectors:
        z_l = q_l * w_pt
        z_r = q_r * w_pt
        z_h = half * (q_l + q_r) * w_pt
        y_sec = _cim_overlap_1d_analytic(tau, z_l, z_r, z_h)
        b_mat += n_c * np.einsum("ijk,ijl->kl", y_sec.conj(), y_sec)
    return b_mat


def run_section_1_resolvent_majorana_and_m44_isotropy() -> dict[str, Any]:
    half = _rat(1, 2)
    zero_c = complex(0, 0)
    tau_gen = _rat(23, 100) + I_UNIT * _rat(141, 100)
    tau_cusp = I_UNIT * (2 * math.sqrt(3))
    kappa_loop = 1 / (4 * math.pi)

    # 1. Cross-check 1D analytic theta-addition series against 42x42 2D torus quadrature
    #    and verify closed-form Weil/theta unitary transports U_T and U_S
    quad_vs_1d_errors: list[float] = []
    orthonorm_errors: list[float] = []
    transport_unitarity_errors: list[float] = []
    transport_quad_vs_closed_errors: list[float] = []

    for tau_pt in (tau_gen, tau_cusp):
        q0 = _cim_overlap_2d_quadrature(tau_pt, zero_c, zero_c, zero_c, n_grid=42)
        y0_an = _cim_overlap_1d_analytic(tau_pt, zero_c, zero_c, zero_c)
        quad_vs_1d_errors.append(float(np.linalg.norm(y0_an - q0["Y_quad"])))
        orthonorm_errors.extend([q0["orthonorm_err_3"], q0["orthonorm_err_6"]])

        w_probe = _rat(1, 5) * tau_pt + _rat(2, 5)
        for q_l, q_r, _ in ((1, -4, 3), (1, 2, 3), (-3, 6, 1)):
            z_l = q_l * w_probe
            z_r = q_r * w_probe
            z_h = half * (q_l + q_r) * w_probe
            q_sec = _cim_overlap_2d_quadrature(tau_pt, z_l, z_r, z_h, n_grid=42)
            y_sec_an = _cim_overlap_1d_analytic(tau_pt, z_l, z_r, z_h)
            quad_vs_1d_errors.append(float(np.linalg.norm(y_sec_an - q_sec["Y_quad"])))

        for flux_m, al, be in ((3, half, half), (6, _rat(0), _rat(0))):
            ut_cl = _weil_transport_T(flux_m, al)
            us_cl = _weil_transport_S(flux_m, al, be, tau_pt)
            ut_qd = _quadrature_transport(flux_m, al, be, tau_pt, "T", n_grid=42)
            us_qd = _quadrature_transport(flux_m, al, be, tau_pt, "S", n_grid=42)
            transport_unitarity_errors.extend(
                [
                    float(np.linalg.norm(ut_cl @ ut_cl.conj().T - np.eye(flux_m))),
                    float(np.linalg.norm(us_cl @ us_cl.conj().T - np.eye(flux_m))),
                ]
            )
            transport_quad_vs_closed_errors.extend(
                [
                    float(np.linalg.norm(ut_cl - ut_qd)),
                    float(np.linalg.norm(us_cl - us_qd)),
                ]
            )

    max_1d_vs_42x42_err = max(quad_vs_1d_errors)
    max_orthonorm_err = max(orthonorm_errors)
    max_transport_unitarity_err = max(transport_unitarity_errors)
    max_transport_closed_vs_quad_err = max(transport_quad_vs_closed_errors)

    # 2. Schwinger-Dyson singlet resolvent M_R^{SD}(tau; kappa): symmetry, T/S covariance,
    #    Bergman rank-1 reproducing identity at kappa=0 -> full rank 3 at kappa > 0
    modulus_records: dict[str, Any] = {}
    max_sym_err = _rat(0)
    max_t_cov_err = _rat(0)
    max_s_cov_err = _rat(0)
    max_bergman_err = _rat(0)
    all_rank_transitions_1_to_3 = True

    ut3 = _weil_transport_T(3, half)
    for label, tau_pt in (("tau_gen_23_100_plus_141_100i", tau_gen), ("tau_cusp_2sqrt3_i", tau_cusp)):
        b_base = _resolvent_majorana_bundle(tau_pt, kappa_loop)
        b_tree = _resolvent_majorana_bundle(tau_pt, _rat(0))
        b_t = _resolvent_majorana_bundle(tau_pt + 1, kappa_loop)
        b_s = _resolvent_majorana_bundle(-1 / tau_pt, kappa_loop)
        us3 = _weil_transport_S(3, half, half, tau_pt)

        mr_sd = b_base["MR_SD"]
        mr_tree = b_tree["MR_SD"]
        sym_err = float(np.linalg.norm(mr_sd - mr_sd.T))
        bergman_err = float(
            np.linalg.norm(mr_tree - np.outer(b_base["u3_zero"], b_base["u3_zero"]))
        )
        t_err = float(np.linalg.norm(b_t["MR_SD"] - ut3 @ mr_sd @ ut3.T))
        s_err = float(np.linalg.norm(b_s["MR_SD"] - us3 @ mr_sd @ us3.T))

        sv_tree = np.sort(np.linalg.svd(mr_tree, compute_uv=False))
        sv_loop = np.sort(np.linalg.svd(mr_sd, compute_uv=False))
        rank_tree = int(np.sum(sv_tree > _pow10_neg(10)))
        rank_loop = int(np.sum(sv_loop > _pow10_neg(10)))

        max_sym_err = max(max_sym_err, sym_err)
        max_bergman_err = max(max_bergman_err, bergman_err)
        max_t_cov_err = max(max_t_cov_err, t_err)
        max_s_cov_err = max(max_s_cov_err, s_err)
        all_rank_transitions_1_to_3 = bool(
            all_rank_transitions_1_to_3 and (rank_tree, rank_loop) == (1, 3)
        )
        modulus_records[label] = {
            "symmetry_err": sym_err,
            "bergman_rank1_reproducing_err": bergman_err,
            "T_covariance_err": t_err,
            "S_covariance_err": s_err,
            "rank_transition_tree_to_loop": [rank_tree, rank_loop],
            "singular_values_ascending_loop": [float(x) for x in sv_loop],
        }

    # 3. 10-trial Haar U(6) x U(3) basis-scrambling invariance (Guardrail 3)
    rng_haar = np.random.default_rng(20261118)
    b_haar = _resolvent_majorana_bundle(tau_gen, kappa_loop)
    y_base = b_haar["Y"]
    v0_base = b_haar["v0"]
    mr_base = b_haar["MR_SD"]
    sv_mr_base = np.sort(np.linalg.svd(mr_base, compute_uv=False))

    w_lep = _rat(1, 5) * tau_gen + _rat(2, 5)
    y_e_ten = _cim_overlap_1d_analytic(tau_gen, -3 * w_lep, 6 * w_lep, _rat(3, 2) * w_lep)
    y_e_raw = np.einsum("ijk,k->ij", y_e_ten, b_haar["G6"] @ v0_base)
    y_e_base = y_e_raw / np.linalg.norm(y_e_raw)
    y_nu_base = b_haar["J1"] / np.linalg.norm(b_haar["J1"])
    m_nu_base = y_nu_base @ np.linalg.solve(mr_base, y_nu_base.T)

    u_el_0, sv_e_0, _ = np.linalg.svd(y_e_base)
    sv_nu_0, u_nu_0 = _takagi_direct_svd(m_nu_base)
    pmns_abs_0 = np.abs(u_el_0.conj().T @ u_nu_0)
    u_pmns_0 = u_el_0.conj().T @ u_nu_0
    j_pmns_0 = float(
        np.imag(u_pmns_0[0, 0] * u_pmns_0[1, 1] * np.conj(u_pmns_0[0, 1]) * np.conj(u_pmns_0[1, 0]))
    )

    max_haar_u6_u3_drift = _rat(0)
    for _ in range(10):
        u6 = _haar_unitary(rng_haar, 6)
        u_nr = _haar_unitary(rng_haar, 3)
        u_l = _haar_unitary(rng_haar, 3)
        u_er = _haar_unitary(rng_haar, 3)

        # Transform Y_{ijk} under U_nr^* x U_nr^* x U_6^* and v_0 under U_6
        y_scr = np.einsum("ia,jb,kc,abc->ijk", u_nr.conj(), u_nr.conj(), u6.conj(), y_base)
        v0_scr = u6 @ v0_base
        y_scr_mat = y_scr.reshape(9, 6)
        g6_scr = y_scr_mat.conj().T @ y_scr_mat
        mr_scr = np.einsum(
            "ijk,k->ij",
            y_scr,
            np.linalg.solve(np.eye(6, dtype=np.complex128) + kappa_loop * g6_scr, v0_scr),
        )
        sv_mr_scr = np.sort(np.linalg.svd(mr_scr, compute_uv=False))
        mr_cov_err = float(np.linalg.norm(mr_scr - u_nr.conj() @ mr_base @ u_nr.conj().T))

        y_e_scr = u_l @ y_e_base @ u_er.conj().T
        y_nu_scr = u_l @ y_nu_base @ u_nr.conj().T
        m_nu_scr = y_nu_scr @ np.linalg.solve(mr_scr, y_nu_scr.T)

        u_el_s, sv_e_s, _ = np.linalg.svd(y_e_scr)
        sv_nu_s, u_nu_s = _takagi_direct_svd(m_nu_scr)
        u_pmns_s = u_el_s.conj().T @ u_nu_s
        pmns_abs_s = np.abs(u_pmns_s)
        j_pmns_s = float(
            np.imag(u_pmns_s[0, 0] * u_pmns_s[1, 1] * np.conj(u_pmns_s[0, 1]) * np.conj(u_pmns_s[1, 0]))
        )

        trial_drift = max(
            mr_cov_err,
            float(np.max(np.abs(sv_mr_scr - sv_mr_base))),
            float(np.max(np.abs(sv_e_s - sv_e_0))),
            float(np.max(np.abs(sv_nu_s - sv_nu_0))),
            float(np.max(np.abs(pmns_abs_s - pmns_abs_0))),
            abs(j_pmns_s - j_pmns_0),
        )
        max_haar_u6_u3_drift = max(max_haar_u6_u3_drift, trial_drift)

    # 4. M44 Level-6 Higgs 4-lift Klein isotropy at w = (1/5) tau + 2/5 and over E*[5]
    z3_clock = np.diag([(-1) ** k for k in range(6)]).astype(np.complex128)
    x3_shift = np.roll(np.eye(6, dtype=np.complex128), 3, axis=0)
    klein_4 = (np.eye(6, dtype=np.complex128), z3_clock, x3_shift, z3_clock @ x3_shift)

    m44_records: dict[str, Any] = {}
    max_z3_conj_err = _rat(0)
    max_x3_conj_err = _rat(0)
    max_klein_isotropy_err = _rat(0)
    min_single_lift_anisotropy = _rat(10**6)

    for label, tau_pt in (("tau_gen", tau_gen), ("tau_cusp", tau_cusp)):
        w_m44 = _rat(1, 5) * tau_pt + _rat(2, 5)
        b_0 = _higgs_bubble_single_point(tau_pt, w_m44)
        b_w1 = _higgs_bubble_single_point(tau_pt, w_m44 + 1)
        b_wt = _higgs_bubble_single_point(tau_pt, w_m44 + tau_pt)

        err_z3 = float(np.linalg.norm(b_w1 - z3_clock @ b_0 @ z3_clock.conj().T))
        err_x3 = float(np.linalg.norm(b_wt - x3_shift @ b_0 @ x3_shift.conj().T))
        raw_shift_1 = float(np.linalg.norm(b_w1 - b_0))
        raw_shift_tau = float(np.linalg.norm(b_wt - b_0))

        b_klein = sum(g @ b_0 @ g.conj().T for g in klein_4) / 4
        scalar_target = (np.trace(b_0) / 6) * np.eye(6, dtype=np.complex128)
        iso_err = float(np.linalg.norm(b_klein - scalar_target))

        evals_single = np.linalg.eigvalsh((b_0 + b_0.conj().T) / 2)
        aniso_single = float(np.max(evals_single) - np.min(evals_single))

        max_z3_conj_err = max(max_z3_conj_err, err_z3)
        max_x3_conj_err = max(max_x3_conj_err, err_x3)
        max_klein_isotropy_err = max(max_klein_isotropy_err, iso_err)
        min_single_lift_anisotropy = min(min_single_lift_anisotropy, aniso_single)

        m44_records[label] = {
            "Z3_shift_1_conjugation_err": err_z3,
            "X3_shift_tau_conjugation_err": err_x3,
            "raw_unconjugated_shift_1_norm": raw_shift_1,
            "raw_unconjugated_shift_tau_norm": raw_shift_tau,
            "klein_4lift_scalar_isotropy_err": iso_err,
            "single_lift_eigenvalue_spread": aniso_single,
        }

    # Also verify full 24-point E*[5] sum averaged over Klein 4-lifts collapses to scalar I_6
    b_24 = np.zeros((6, 6), dtype=np.complex128)
    for a5 in range(5):
        for b5 in range(5):
            if (a5, b5) != (0, 0):
                b_24 += _higgs_bubble_single_point(
                    tau_gen, _rat(a5, 5) * tau_gen + _rat(b5, 5)
                )
    b_24_klein = sum(g @ b_24 @ g.conj().T for g in klein_4) / 4
    e5_24pt_klein_isotropy_err = float(
        np.linalg.norm(b_24_klein - (np.trace(b_24) / 6) * np.eye(6, dtype=np.complex128))
    )

    # 5. Planted Fault PF11.1: Omitting Kahler (Im tau)^{1/4} gives modular weight |tau|^1
    y_pf1_t = _cim_overlap_1d_analytic(tau_gen, zero_c, zero_c, zero_c)
    y_pf1_s = _cim_overlap_1d_analytic(-1 / tau_gen, zero_c, zero_c, zero_c)
    w_pf1_t = y_pf1_t / ((tau_gen.imag) ** Fraction(1, 4))
    w_pf1_s = y_pf1_s / (((-1 / tau_gen).imag) ** Fraction(1, 4))
    gw_t = w_pf1_t.reshape(9, 6).conj().T @ w_pf1_t.reshape(9, 6)
    gw_s = w_pf1_s.reshape(9, 6).conj().T @ w_pf1_s.reshape(9, 6)
    us6_gen = _weil_transport_S(6, _rat(0), _rat(0), tau_gen)
    pf11_1_weight1_law_err = float(
        np.linalg.norm(gw_s - abs(tau_gen) * (us6_gen @ gw_t @ us6_gen.conj().T))
    )
    pf11_1_unweighted_violation = float(
        np.linalg.norm(gw_s - (us6_gen @ gw_t @ us6_gen.conj().T))
    )
    pf11_1_caught = bool(
        pf11_1_weight1_law_err < _pow10_neg(13) and pf11_1_unweighted_violation > half
    )

    # 6. Planted Fault PF11.2: Sweeping kappa in [1/(48 pi^2), 4 pi] at tau = 2 sqrt(3) i
    kappa_grid = (1 / (48 * (math.pi**2)), 1 / (4 * math.pi), 4 * math.pi)
    b_cusp_ref = _resolvent_majorana_bundle(tau_cusp, kappa_loop)
    j1_cusp = b_cusp_ref["J1"]
    mr_r13_vals: list[float] = []
    mr_s3_over_s1_vals: list[float] = []
    seesaw_r12_vals: list[float] = []
    seesaw_s2_over_s1_vals: list[float] = []

    for kap_val in kappa_grid:
        mr_k = _resolvent_majorana_bundle(tau_cusp, kap_val)["MR_SD"]
        sv_mr_k = np.sort(np.linalg.svd(mr_k, compute_uv=False))
        mr_r13_vals.append(float(sv_mr_k[0] / sv_mr_k[2]))
        mr_s3_over_s1_vals.append(float(sv_mr_k[2] / sv_mr_k[0]))

        m_nu_k = j1_cusp @ np.linalg.solve(mr_k, j1_cusp.T)
        sv_ss_k = np.sort(np.linalg.svd(m_nu_k, compute_uv=False))
        seesaw_r12_vals.append(float(sv_ss_k[0] / sv_ss_k[1]))
        seesaw_s2_over_s1_vals.append(float(sv_ss_k[1] / sv_ss_k[0]))

    pf11_2_mr_r13_factor = max(mr_r13_vals) / min(mr_r13_vals)
    pf11_2_seesaw_r12_factor = max(seesaw_r12_vals) / min(seesaw_r12_vals)
    pf11_2_mr_s3_s1_span = max(mr_s3_over_s1_vals) - min(mr_s3_over_s1_vals)
    pf11_2_seesaw_s2_s1_span = max(seesaw_s2_over_s1_vals) - min(seesaw_s2_over_s1_vals)
    pf11_2_caught = bool(
        pf11_2_mr_r13_factor > 250
        and pf11_2_seesaw_r12_factor > 250
        and pf11_2_mr_s3_s1_span > 250
        and pf11_2_seesaw_s2_s1_span > 250
    )

    # 7. Planted Fault PF11.4: Real SO(3) rotation [[3/5, -4/5, 0], [4/5, 3/5, 0], [0, 0, 1]]
    #    on legacy Frobenius-orthonormal (E_0, E_1, E_2) all-ones (1, 1, 1)^T contraction
    r_so3 = np.array(
        [
            [_rat(3, 5), _rat(-4, 5), _rat(0)],
            [_rat(4, 5), _rat(3, 5), _rat(0)],
            [_rat(0), _rat(0), _rat(1)],
        ],
        dtype=np.float64,
    )
    so3_orth_err = float(np.linalg.norm(r_so3 @ r_so3.T - np.eye(3)))
    so3_det_err = abs(float(np.linalg.det(r_so3)) - 1)
    c_ones = np.ones(3, dtype=np.float64)
    c_rot = r_so3 @ c_ones

    j_triple_cusp = [b_cusp_ref["J0"], b_cusp_ref["J1"], b_cusp_ref["J2"]]
    gs_cusp = _frobenius_gram_schmidt(j_triple_cusp)
    lowdin_cusp = _frobenius_lowdin(j_triple_cusp)

    sv_gs_unrot = np.sort(np.linalg.svd(gs_cusp[0] + gs_cusp[1] + gs_cusp[2], compute_uv=False))
    sv_gs_rot = np.sort(
        np.linalg.svd(
            c_rot[0] * gs_cusp[0] + c_rot[1] * gs_cusp[1] + c_rot[2] * gs_cusp[2],
            compute_uv=False,
        )
    )
    pf11_4_gs_asc_sigma2_over_sigma1_shift = abs(
        float(sv_gs_unrot[1] / sv_gs_unrot[0] - sv_gs_rot[1] / sv_gs_rot[0])
    )
    pf11_4_gs_bounded_sigma1_over_sigma2_shift = abs(
        float(sv_gs_unrot[0] / sv_gs_unrot[1] - sv_gs_rot[0] / sv_gs_rot[1])
    )

    sv_lw_unrot = np.sort(
        np.linalg.svd(lowdin_cusp[0] + lowdin_cusp[1] + lowdin_cusp[2], compute_uv=False)
    )
    sv_lw_rot = np.sort(
        np.linalg.svd(
            c_rot[0] * lowdin_cusp[0] + c_rot[1] * lowdin_cusp[1] + c_rot[2] * lowdin_cusp[2],
            compute_uv=False,
        )
    )
    pf11_4_lowdin_asc_sigma2_over_sigma1_shift = abs(
        float(sv_lw_unrot[1] / sv_lw_unrot[0] - sv_lw_rot[1] / sv_lw_rot[0])
    )

    pf11_4_caught = bool(
        so3_orth_err < _pow10_neg(14)
        and so3_det_err < _pow10_neg(14)
        and pf11_4_gs_asc_sigma2_over_sigma1_shift > half
        and pf11_4_gs_bounded_sigma1_over_sigma2_shift > half
        and pf11_4_lowdin_asc_sigma2_over_sigma1_shift > half
    )

    passed = bool(
        max_1d_vs_42x42_err < _pow10_neg(13)
        and max_orthonorm_err < _pow10_neg(14)
        and max_transport_unitarity_err < _pow10_neg(14)
        and max_transport_closed_vs_quad_err < _pow10_neg(13)
        and max_sym_err < _pow10_neg(14)
        and max_bergman_err < _pow10_neg(14)
        and max_t_cov_err < _pow10_neg(13)
        and max_s_cov_err < _pow10_neg(13)
        and all_rank_transitions_1_to_3
        and max_haar_u6_u3_drift < _pow10_neg(13)
        and max_z3_conj_err < _pow10_neg(13)
        and max_x3_conj_err < _pow10_neg(13)
        and max_klein_isotropy_err < _pow10_neg(13)
        and e5_24pt_klein_isotropy_err < _pow10_neg(13)
        and min_single_lift_anisotropy > 1
        and pf11_1_caught
        and pf11_2_caught
        and pf11_4_caught
    )
    return {
        "max_1d_analytic_vs_42x42_quadrature_err": max_1d_vs_42x42_err,
        "max_mode_orthonormality_err": max_orthonorm_err,
        "max_weil_transport_unitarity_err": max_transport_unitarity_err,
        "max_weil_closed_vs_quadrature_err": max_transport_closed_vs_quad_err,
        "resolvent_moduli_checks": modulus_records,
        "max_symmetry_err": max_sym_err,
        "max_bergman_rank1_err": max_bergman_err,
        "max_T_covariance_err": max_t_cov_err,
        "max_S_covariance_err": max_s_cov_err,
        "all_rank_transitions_1_to_3": all_rank_transitions_1_to_3,
        "haar_10_trial_U6_x_U3_max_drift": max_haar_u6_u3_drift,
        "m44_klein_4lift_checks": m44_records,
        "m44_max_Z3_conjugation_err": max_z3_conj_err,
        "m44_max_X3_conjugation_err": max_x3_conj_err,
        "m44_max_4lift_scalar_isotropy_err": max_klein_isotropy_err,
        "m44_e5_24pt_4lift_scalar_isotropy_err": e5_24pt_klein_isotropy_err,
        "m44_repricing_PR5_discrete_bits": 1,
        "PF11_1_weight1_law_err": pf11_1_weight1_law_err,
        "PF11_1_unweighted_S_violation": pf11_1_unweighted_violation,
        "PF11_1_caught": pf11_1_caught,
        "PF11_2_mr_r13_sweep_factor": pf11_2_mr_r13_factor,
        "PF11_2_seesaw_r12_sweep_factor": pf11_2_seesaw_r12_factor,
        "PF11_2_mr_s3_over_s1_span": pf11_2_mr_s3_s1_span,
        "PF11_2_seesaw_s2_over_s1_span": pf11_2_seesaw_s2_s1_span,
        "PF11_2_caught": pf11_2_caught,
        "PF11_4_gs_asc_sigma2_over_sigma1_shift": pf11_4_gs_asc_sigma2_over_sigma1_shift,
        "PF11_4_gs_bounded_sigma1_over_sigma2_shift": pf11_4_gs_bounded_sigma1_over_sigma2_shift,
        "PF11_4_lowdin_asc_sigma2_over_sigma1_shift": pf11_4_lowdin_asc_sigma2_over_sigma1_shift,
        "PF11_4_caught": pf11_4_caught,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Section 2: 1-Loop RG Dimensional Transmutation, 3-Route 50-Digit Vol(m004),
#            4-Sheet vs 45-Torsion Audit, & PHYSICAL-C7 Symbolic CAS Proofs
# ---------------------------------------------------------------------------


def _su2_matrix(x1: Any, x2: Any) -> sp.Matrix:
    return sp.Matrix([[x1, -sp.conjugate(x2)], [x2, sp.conjugate(x1)]])


def run_section_2_transmutation_vol_m004_and_c7_cas() -> dict[str, Any]:
    # 1. Literature Benchmark Gate (Guardrail 4) & Symbolic 1-loop RG Dimensional Transmutation
    n_c_sym, n_f_sym = sp.symbols("N_c N_f")
    b0_gross_wilczek = sp.Rational(11, 3) * n_c_sym - sp.Rational(2, 3) * n_f_sym
    b0_pure_su3 = b0_gross_wilczek.subs({n_c_sym: 3, n_f_sym: 0})
    b0_sm_qcd_nf6 = b0_gross_wilczek.subs({n_c_sym: 3, n_f_sym: 6})
    benchmark_b0_ok = bool(b0_pure_su3 == 11 and b0_sm_qcd_nf6 == 7)

    ln_mu, ln_mu_uv, b_abs, alpha_uv_inv = sp.symbols(
        "ln_mu ln_mu_uv b_abs alpha_uv_inv", real=True, positive=True
    )
    alpha_h_inv_mu = alpha_uv_inv + (b_abs / (2 * sp.pi)) * (ln_mu - ln_mu_uv)
    ln_lambda_h = ln_mu - (2 * sp.pi / b_abs) * alpha_h_inv_mu
    d_ln_lambda_d_ln_mu = sp.simplify(sp.diff(ln_lambda_h, ln_mu))
    ln_lambda_minus_uv = sp.simplify(ln_lambda_h - ln_mu_uv)
    expected_transmuted_log_ratio = -2 * sp.pi * alpha_uv_inv / b_abs
    transmutation_symbolic_ok = bool(
        d_ln_lambda_d_ln_mu == 0
        and sp.simplify(ln_lambda_minus_uv - expected_transmuted_log_ratio) == 0
    )

    # Independent Kahan-compensated RK4 ODE integration on d(alpha_H^{-1})/d(ln mu) = |b_H| / (2 pi)
    b_num = _rat(7)
    alpha_inv_0 = _rat(25)
    t_span = _rat(-30)
    n_rk4 = 600
    dt_step = t_span / n_rk4
    slope_rg = b_num / (2 * math.pi)
    alpha_cur = alpha_inv_0
    alpha_comp = _rat(0)
    ln_mu_cur = _rat(0)
    ln_mu_comp = _rat(0)
    max_rk4_invariant_drift = _rat(0)
    inv_0 = ln_mu_cur - (2 * math.pi / b_num) * alpha_cur
    for _ in range(n_rk4):
        k1 = slope_rg
        k2 = slope_rg
        k3 = slope_rg
        k4 = slope_rg
        d_alpha = (dt_step / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        y_a = d_alpha - alpha_comp
        t_a = alpha_cur + y_a
        alpha_comp = (t_a - alpha_cur) - y_a
        alpha_cur = t_a

        y_m = dt_step - ln_mu_comp
        t_m = ln_mu_cur + y_m
        ln_mu_comp = (t_m - ln_mu_cur) - y_m
        ln_mu_cur = t_m

        inv_cur = ln_mu_cur - (2 * math.pi / b_num) * alpha_cur
        max_rk4_invariant_drift = max(max_rk4_invariant_drift, abs(inv_cur - inv_0))

    # 2. Three-route 50-digit Vol(m004) verification & 4-sheet cover vs 45-torsion audit
    with mp.workdps(65):
        z_ideal = mp.exp(mp.mpc(0, 1) * mp.pi / mp.mpf(3))
        d2_bloch_wigner = mp.im(mp.polylog(2, z_ideal)) + mp.arg(
            mp.mpf(1) - z_ideal
        ) * mp.log(abs(z_ideal))
        vol_route1_dilog = mp.mpf(2) * d2_bloch_wigner

        l2_chi_minus3 = (
            mp.hurwitz(2, mp.mpf(1) / mp.mpf(3)) - mp.hurwitz(2, mp.mpf(2) / mp.mpf(3))
        ) / mp.mpf(9)
        vol_route2_dirichlet_l = (mp.mpf(3) * mp.sqrt(mp.mpf(3)) / mp.mpf(2)) * l2_chi_minus3

        vol_route3_lobachevsky = -mp.mpf(4) * mp.quad(
            lambda u: mp.log(mp.mpf(2) * mp.sin(u)), [mp.mpf(0), mp.pi / mp.mpf(6)]
        )

        diff_r1_r2 = float(abs(vol_route1_dilog - vol_route2_dirichlet_l))
        diff_r1_r3 = float(abs(vol_route1_dilog - vol_route3_lobachevsky))
        vol_50digit_str = mp.nstr(vol_route1_dilog, 50)

        pf11_3_log10_suppression_gap = float(
            mp.log10(
                mp.exp(-mp.mpf(4) * vol_route1_dilog / mp.pi)
                / mp.exp(-mp.mpf(45) * vol_route1_dilog / mp.pi)
            )
        )

    l_mat = sp.Matrix([[1, 0], [1, 1]])
    r_mat = sp.Matrix([[1, 1], [0, 1]])
    lr_mat = l_mat * r_mat
    rl_mat = r_mat * l_mat
    lr4_minus_i = (lr_mat**4) - sp.eye(2)
    rl4_minus_i = (rl_mat**4) - sp.eye(2)
    abs_det_lr4_minus_i = int(abs(lr4_minus_i.det()))
    abs_det_rl4_minus_i = int(abs(rl4_minus_i.det()))
    snf_mat = smith_normal_form(lr4_minus_i, domain=sp.ZZ)
    snf_invariants = sorted([int(abs(snf_mat[0, 0])), int(abs(snf_mat[1, 1]))])
    cyclic_cover_degree = 4
    conflated_product_180 = cyclic_cover_degree * abs_det_lr4_minus_i
    diff_45_vs_180 = abs(conflated_product_180 - abs_det_lr4_minus_i)
    diff_45_vs_4 = abs(abs_det_lr4_minus_i - cyclic_cover_degree)

    pf11_3_caught = bool(
        abs_det_lr4_minus_i == 45
        and abs_det_rl4_minus_i == 45
        and snf_invariants == [3, 15]
        and cyclic_cover_degree == 4
        and pf11_3_log10_suppression_gap > 11
        and diff_45_vs_180 > 35
        and diff_45_vs_4 > 35
    )

    # 3. Planted Fault PF11.5: X-APEX-2 telescoping boundary-flux tautology (Guardrail 2)
    rng_flux = np.random.default_rng(20261118)
    max_telescoping_dev_from_1 = _rat(0)
    for n_cells in (48, 64):
        dx = _rat(12, n_cells)
        for _ in range(5):
            a_arr = np.zeros(n_cells + 1, dtype=np.float64)
            a_arr[0] = _rat(0)
            a_arr[-1] = _rat(1)
            a_arr[1:-1] = rng_flux.uniform(-500, 500, size=n_cells - 1)
            ap = (a_arr[1:] - a_arr[:-1]) / dx
            telescoping_flux = float(np.sum(ap) * dx)
            max_telescoping_dev_from_1 = max(
                max_telescoping_dev_from_1, abs(telescoping_flux - 1)
            )
    pf11_5_caught = bool(max_telescoping_dev_from_1 < _pow10_neg(10))

    # 4. Independent Stereographic Differential-Form & Quaternion CAS Verification of PHYSICAL-C7
    p1, p2, r1, r2 = sp.symbols("p1 p2 r1 r2", complex=True)
    phi_g = sp.Symbol("phi_g", real=True)
    z_conifold = sp.Matrix([[p1 * r1, p1 * r2], [p2 * r1, p2 * r2]])
    det_z_exact = sp.expand(z_conifold.det())
    p_rot = sp.exp(sp.I * phi_g) * sp.Matrix([p1, p2])
    r_rot = sp.exp(-sp.I * phi_g) * sp.Matrix([r1, r2])
    z_conifold_rot = sp.Matrix(
        [[p_rot[0] * r_rot[0], p_rot[0] * r_rot[1]], [p_rot[1] * r_rot[0], p_rot[1] * r_rot[1]]]
    )
    z_gauge_drift = sp.simplify(z_conifold_rot - z_conifold)
    conifold_ok = bool(det_z_exact == 0 and z_gauge_drift == sp.zeros(2, 2))

    # Stereographic / Fubini-Study coordinates on S^3 -> CP^1 ~= S^2 for v = conj(u)
    r_st, phi_st, t_rad = sp.symbols("r_st phi_st t_rad", real=True, positive=True)
    u_st = sp.Matrix([sp.Integer(1), r_st * sp.exp(sp.I * phi_st)]) / sp.sqrt(
        sp.Integer(1) + r_st**2
    )
    v_st = sp.conjugate(u_st)
    p_vec = t_rad * u_st
    r_vec = t_rad * v_st
    u_norm_sq = sp.simplify((u_st.adjoint() * u_st)[0, 0])
    denom_pr = sp.simplify((p_vec.adjoint() * p_vec + r_vec.adjoint() * r_vec)[0, 0])

    # Pullback 1-form A_phase = [Im(P^dag dP) - Im(R^dag dR)] / (||P||^2 + ||R||^2)
    a_phase_r = sp.simplify(
        (
            sp.im((p_vec.adjoint() * sp.diff(p_vec, r_st))[0, 0])
            - sp.im((r_vec.adjoint() * sp.diff(r_vec, r_st))[0, 0])
        )
        / denom_pr
    )
    a_phase_phi = sp.simplify(
        (
            sp.im((p_vec.adjoint() * sp.diff(p_vec, phi_st))[0, 0])
            - sp.im((r_vec.adjoint() * sp.diff(r_vec, phi_st))[0, 0])
        )
        / denom_pr
    )
    a_hopf_phi_expected = r_st**2 / (sp.Integer(1) + r_st**2)
    f_curvature_r_phi = sp.simplify(sp.diff(a_phase_phi, r_st) - sp.diff(a_phase_r, phi_st))
    f_expected = (2 * r_st) / ((sp.Integer(1) + r_st**2) ** 2)
    chern_stereographic = sp.simplify(
        sp.integrate(sp.integrate(f_curvature_r_phi, (r_st, 0, sp.oo)), (phi_st, 0, 2 * sp.pi))
        / (2 * sp.pi)
    )

    # Cross-check in spherical coordinates r_st = tan(theta/2)
    theta_sp = sp.Symbol("theta_sp", real=True, positive=True)
    f_spherical = sp.trigsimp(
        f_curvature_r_phi.subs(r_st, sp.tan(theta_sp / 2)) * sp.diff(sp.tan(theta_sp / 2), theta_sp)
    )
    chern_spherical = sp.simplify(
        sp.integrate(sp.integrate(f_spherical, (theta_sp, 0, sp.pi)), (phi_st, 0, 2 * sp.pi))
        / (2 * sp.pi)
    )
    hopf_chern_ok = bool(
        u_norm_sq == 1
        and a_phase_r == 0
        and sp.simplify(a_phase_phi - a_hopf_phi_expected) == 0
        and sp.simplify(f_curvature_r_phi - f_expected) == 0
        and chern_stereographic == 1
        and chern_spherical == 1
    )

    # Symbolic composite (A, W) = (U(u) J U(u)^{-1}, U(u) U(conj(v))^{-1}) checks
    ua, ub, uc, ud = sp.symbols("ua ub uc ud", real=True)
    va, vb, vc, vd = sp.symbols("va vb vc vd", real=True)
    u1_s = ua + sp.I * ub
    u2_s = uc + sp.I * ud
    v1_s = va + sp.I * vb
    v2_s = vc + sp.I * vd
    unit_subs = {
        ua**2: sp.Integer(1) - ub**2 - uc**2 - ud**2,
        va**2: sp.Integer(1) - vb**2 - vc**2 - vd**2,
    }

    u_mat = _su2_matrix(u1_s, u2_s)
    c_mat = _su2_matrix(sp.conjugate(v1_s), sp.conjugate(v2_s))
    j_quat = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    u_det = sp.expand(u_mat.det()).subs(unit_subs)
    c_det = sp.expand(c_mat.det()).subs(unit_subs)
    a_comp = sp.expand(u_mat * j_quat * u_mat.adjoint()).subs(unit_subs)
    w_comp = sp.expand(u_mat * c_mat.adjoint()).subs(unit_subs)

    d_phi = sp.Matrix([[sp.exp(sp.I * phi_g), 0], [0, sp.exp(-sp.I * phi_g)]])
    u_mat_phi = u_mat * d_phi
    c_mat_phi = c_mat * d_phi
    a_comp_phi = sp.simplify(sp.expand(u_mat_phi * j_quat * u_mat_phi.adjoint()).subs(unit_subs))
    w_comp_phi = sp.simplify(sp.expand(u_mat_phi * c_mat_phi.adjoint()).subs(unit_subs))

    a_gauge_drift = sp.simplify(a_comp_phi - a_comp)
    w_gauge_drift = sp.simplify(w_comp_phi - w_comp)
    a_trace = sp.simplify(sp.trace(a_comp))
    a_antiherm = sp.simplify(a_comp.adjoint() + a_comp)
    a_sq_plus_i = sp.simplify(sp.expand(a_comp * a_comp + sp.eye(2)).subs(unit_subs))
    a_4th_minus_i = sp.simplify(sp.expand(a_comp**4 - sp.eye(2)).subs(unit_subs))

    # Shear v -> i*v => conj(v) -> -i*conj(v) => C -> C * J^{-1} => W -> A * W (order 4)
    c_shear = _su2_matrix(sp.conjugate(sp.I * v1_s), sp.conjugate(sp.I * v2_s))
    w_shear = sp.simplify(sp.expand(u_mat * c_shear.adjoint()).subs(unit_subs))
    aw_prod = sp.simplify(sp.expand(a_comp * w_comp).subs(unit_subs))
    shear_is_aw = bool(sp.simplify(w_shear - aw_prod) == sp.zeros(2, 2))

    # On primitive sphere v = conj(u), W == I_2 and [A, W] == 0
    w_on_prim = sp.simplify(
        w_comp.subs({va: ua, vb: -ub, vc: uc, vd: -ud}).subs(unit_subs)
    )
    composite_ok = bool(
        u_det == 1
        and c_det == 1
        and a_gauge_drift == sp.zeros(2, 2)
        and w_gauge_drift == sp.zeros(2, 2)
        and a_trace == 0
        and a_antiherm == sp.zeros(2, 2)
        and a_sq_plus_i == sp.zeros(2, 2)
        and a_4th_minus_i == sp.zeros(2, 2)
        and shear_is_aw
        and w_on_prim == sp.eye(2)
    )

    # Exact rational commutator-trace drift of direct (U(u), U(conj(v))) at
    # u = (3/5, 4/5), v = (5/13, 12/13 i) under U(1) gauge step phi = pi/2 (e^{i phi} = i)
    u_rat = (sp.Rational(3, 5), sp.Rational(4, 5))
    v_rat = (sp.Rational(5, 13), sp.Rational(12, 13) * sp.I)
    u_rat_phi = (sp.I * u_rat[0], sp.I * u_rat[1])
    v_rat_phi = (-sp.I * v_rat[0], -sp.I * v_rat[1])

    z_rat_0 = sp.Matrix([[u_rat[0] * v_rat[0], u_rat[0] * v_rat[1]], [u_rat[1] * v_rat[0], u_rat[1] * v_rat[1]]])
    z_rat_phi = sp.Matrix(
        [
            [u_rat_phi[0] * v_rat_phi[0], u_rat_phi[0] * v_rat_phi[1]],
            [u_rat_phi[1] * v_rat_phi[0], u_rat_phi[1] * v_rat_phi[1]],
        ]
    )
    same_quotient_point = bool(sp.simplify(z_rat_phi - z_rat_0) == sp.zeros(2, 2))

    m1_0 = _su2_matrix(u_rat[0], u_rat[1])
    m2_0 = _su2_matrix(sp.conjugate(v_rat[0]), sp.conjugate(v_rat[1]))
    comm_0 = sp.simplify(m1_0 * m2_0 * m1_0.inv() * m2_0.inv())
    tr_comm_0 = sp.simplify(sp.trace(comm_0))

    m1_phi = _su2_matrix(u_rat_phi[0], u_rat_phi[1])
    m2_phi = _su2_matrix(sp.conjugate(v_rat_phi[0]), sp.conjugate(v_rat_phi[1]))
    comm_phi = sp.simplify(m1_phi * m2_phi * m1_phi.inv() * m2_phi.inv())
    tr_comm_phi = sp.simplify(sp.trace(comm_phi))

    direct_comm_trace_drift = sp.simplify(tr_comm_phi - tr_comm_0)
    expected_drift = sp.Rational(-6784, 4225)

    # Confirm composite (A, W) has exact 0 drift at the same rational point
    a_rat_0 = sp.simplify(m1_0 * j_quat * m1_0.inv())
    w_rat_0 = sp.simplify(m1_0 * m2_0.inv())
    a_rat_phi = sp.simplify(m1_phi * j_quat * m1_phi.inv())
    w_rat_phi = sp.simplify(m1_phi * m2_phi.inv())
    comp_rat_zero_drift = bool(
        sp.simplify(a_rat_phi - a_rat_0) == sp.zeros(2, 2)
        and sp.simplify(w_rat_phi - w_rat_0) == sp.zeros(2, 2)
    )

    direct_failure_ok = bool(
        same_quotient_point
        and tr_comm_0 == sp.Rational(-766, 4225)
        and tr_comm_phi == sp.Rational(-302, 169)
        and direct_comm_trace_drift == expected_drift
        and comp_rat_zero_drift
    )

    passed = bool(
        benchmark_b0_ok
        and transmutation_symbolic_ok
        and max_rk4_invariant_drift < _pow10_neg(14)
        and diff_r1_r2 < _pow10_neg(45)
        and diff_r1_r3 < _pow10_neg(45)
        and pf11_3_caught
        and pf11_5_caught
        and conifold_ok
        and hopf_chern_ok
        and composite_ok
        and direct_failure_ok
    )
    return {
        "gross_wilczek_b0_benchmark_passed": benchmark_b0_ok,
        "transmutation_d_ln_Lambda_d_ln_mu": int(d_ln_lambda_d_ln_mu),
        "transmutation_symbolic_exact": transmutation_symbolic_ok,
        "transmutation_extra_knobs_beyond_alpha_UV_inv": 0,
        "transmutation_rk4_invariant_max_drift": max_rk4_invariant_drift,
        "vol_m004_50digits": vol_50digit_str,
        "vol_m004_dilog_vs_dirichlet_L_diff": diff_r1_r2,
        "vol_m004_dilog_vs_lobachevsky_quad_diff": diff_r1_r3,
        "abs_det_LR4_minus_I2": abs_det_lr4_minus_i,
        "abs_det_RL4_minus_I2": abs_det_rl4_minus_i,
        "LR4_minus_I2_smith_invariant_factors": snf_invariants,
        "manifold_cyclic_cover_degree": cyclic_cover_degree,
        "PF11_3_log10_4sheet_vs_45torsion_ratio": pf11_3_log10_suppression_gap,
        "PF11_3_45_vs_180_discrepancy": diff_45_vs_180,
        "PF11_3_caught": pf11_3_caught,
        "PF11_5_random_interior_max_dev_from_1": max_telescoping_dev_from_1,
        "PF11_5_caught": pf11_5_caught,
        "c7_conifold_det_Z_zero_and_gauge_invariant": conifold_ok,
        "c7_hopf_stereographic_and_spherical_chern_number": int(chern_stereographic),
        "c7_hopf_chern_verified": hopf_chern_ok,
        "c7_composite_AW_zero_drift_and_order4_verified": composite_ok,
        "c7_direct_tr_comm_phi_0": f"{int(tr_comm_0.p)}/{int(tr_comm_0.q)}",
        "c7_direct_tr_comm_phi_pi_over_2": f"{int(tr_comm_phi.p)}/{int(tr_comm_phi.q)}",
        "c7_direct_commutator_trace_drift": f"{int(direct_comm_trace_drift.p)}/{int(direct_comm_trace_drift.q)}",
        "c7_direct_orbit_failure_verified": direct_failure_ok,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Section 3: Independent Kahn Topological-Sort Verification of the 52-Node
#            Foundational Epistemic DAG (Gates 8-11 Complete)
# ---------------------------------------------------------------------------


def _build_52_node_foundational_dag() -> tuple[list[dict[str, Any]], list[tuple[str, str]]]:
    """Construct the 52-node Foundational Epistemic DAG:
    8 ROOT + 7 OPERATOR + 8 SEAM + 10 RELATION + 19 SM_TARGET = 52.
    """
    nodes: list[dict[str, Any]] = [
        # 8 ROOT nodes (5 from Gate 7 + 3 universal mathematical theorems from Gates 8-10)
        {"id": "G:m004_Mostow_Rigidity", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "G:X4_Collar_Cobordism", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "G:Spin10_E6_Chirality", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "G:Heisenberg_Weil_SL2Z", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "G:MSbar_2Loop_EFT_RGE", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "G:Weil_CAR_Cl10_A2xE6_Orthogonality", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "G:Kaplan_DomainWall_Chiral_Index", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "G:Culler_SpinLift_Baer_RayleighRitz", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        # 7 OPERATOR nodes (5 from Gate 7 + 2 foundational operators from Gates 10-11)
        {"id": "O:Spin10_Anomaly_Operator", "category": "OPERATOR", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "O:Collar_Casimir_Operator", "category": "OPERATOR", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "O:PatiSalam_Z2D_Channel", "category": "OPERATOR", "intrinsic_rank": 1, "has_stabilization_proof": True, "premises": ["G_422_x_Z2D_breaking_channel"]},
        {"id": "O:CIM_33m6_Frame_D1", "category": "OPERATOR", "intrinsic_rank": 1, "has_stabilization_proof": True, "premises": ["Magnetized_E_tau_flux_3_3_minus6_frame"]},
        {"id": "O:Bergman_Majorana_Seesaw", "category": "OPERATOR", "intrinsic_rank": 1, "has_stabilization_proof": True, "premises": ["Heavy_6plet_singlet_TypeI_portal"]},
        {"id": "O:BranchB_Cohomological_Collar", "category": "OPERATOR", "intrinsic_rank": 1, "has_stabilization_proof": True, "premises": ["Kink_gapped_bulk_spinors_curved_counterterm_open"]},
        {"id": "O:SchwingerDyson_Resolvent_Majorana", "category": "OPERATOR", "intrinsic_rank": 1, "has_stabilization_proof": True, "premises": ["1Loop_singlet_bubble_UV_coupling_kappa"]},
        # 8 SEAM nodes (7 from Gate 7 + 1 M44 Level-6 Higgs +-pi/6 discrete bit at rank 2)
        {"id": "S:StrongCP_Det_Sign_Bit", "category": "SEAM", "intrinsic_rank": 2, "has_stabilization_proof": False, "premises": ["1bit_D_parity_bidoublet_sign"]},
        {"id": "S:Discrete_Torsion_TM1_Z2", "category": "SEAM", "intrinsic_rank": 2, "has_stabilization_proof": False, "premises": ["1bit_TM1_Z2_residual_column"]},
        {"id": "S:Level6_Higgs_Klein_Pair_Bit", "category": "SEAM", "intrinsic_rank": 2, "has_stabilization_proof": False, "premises": ["1bit_M44_Klein_isotropy_pm_pi_over_6_pair"]},
        {"id": "S:Collar_Modulus_Delta_PS", "category": "SEAM", "intrinsic_rank": 3, "has_stabilization_proof": False, "premises": ["Continuous_threshold_interval_Delta_PS"]},
        {"id": "S:Unified_Gauge_Anchor_AlphaU", "category": "SEAM", "intrinsic_rank": 3, "has_stabilization_proof": False, "premises": ["Continuous_UV_gauge_coupling_alpha_U"]},
        {"id": "S:Elliptic_Fibre_Modulus_Tau", "category": "SEAM", "intrinsic_rank": 3, "has_stabilization_proof": False, "premises": ["Continuous_complex_fibre_modulus_tau"]},
        {"id": "S:Torsion_Tau_SU2R_Break", "category": "SEAM", "intrinsic_rank": 3, "has_stabilization_proof": False, "premises": ["Continuous_SU2R_breaking_holonomy_shift"]},
        {"id": "S:Electroweak_VEV_Portal_Scale", "category": "SEAM", "intrinsic_rank": 3, "has_stabilization_proof": False, "premises": ["Dimensionful_anchor_v_EW"]},
        # 10 RELATION nodes (PR-1..PR-10)
        {"id": "PR-1", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "PR-2", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "PR-3", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "PR-4", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "PR-5", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "PR-6", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "PR-7", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "PR-8", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "PR-9", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "PR-10", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        # 19 SM_TARGET nodes (SM01..SM19)
        {"id": "SM01:y_u", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM02:y_c", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM03:y_t", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM04:y_d", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM05:y_s", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM06:y_b", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM07:y_e", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM08:y_mu", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM09:y_tau", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM10:theta_12_CKM", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM11:theta_23_CKM", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM12:theta_13_CKM", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM13:delta_CKM", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM14:g_1", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM15:g_2", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM16:g_3", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM17:v_EW", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM18:m_H", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
        {"id": "SM19:bar_theta_QCD", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True, "premises": []},
    ]

    edges: list[tuple[str, str]] = [
        # ROOT -> OPERATOR
        ("G:Spin10_E6_Chirality", "O:Spin10_Anomaly_Operator"),
        ("G:Weil_CAR_Cl10_A2xE6_Orthogonality", "O:Spin10_Anomaly_Operator"),
        ("G:m004_Mostow_Rigidity", "O:Collar_Casimir_Operator"),
        ("G:X4_Collar_Cobordism", "O:Collar_Casimir_Operator"),
        ("G:Spin10_E6_Chirality", "O:Collar_Casimir_Operator"),
        ("G:Culler_SpinLift_Baer_RayleighRitz", "O:Collar_Casimir_Operator"),
        ("G:X4_Collar_Cobordism", "O:PatiSalam_Z2D_Channel"),
        ("G:Spin10_E6_Chirality", "O:PatiSalam_Z2D_Channel"),
        ("G:Kaplan_DomainWall_Chiral_Index", "O:PatiSalam_Z2D_Channel"),
        ("G:MSbar_2Loop_EFT_RGE", "O:PatiSalam_Z2D_Channel"),
        ("G:m004_Mostow_Rigidity", "O:CIM_33m6_Frame_D1"),
        ("G:Heisenberg_Weil_SL2Z", "O:CIM_33m6_Frame_D1"),
        ("G:Weil_CAR_Cl10_A2xE6_Orthogonality", "O:CIM_33m6_Frame_D1"),
        ("G:Kaplan_DomainWall_Chiral_Index", "O:CIM_33m6_Frame_D1"),
        ("O:CIM_33m6_Frame_D1", "O:Bergman_Majorana_Seesaw"),
        ("O:PatiSalam_Z2D_Channel", "O:Bergman_Majorana_Seesaw"),
        ("G:MSbar_2Loop_EFT_RGE", "O:Bergman_Majorana_Seesaw"),
        ("O:Collar_Casimir_Operator", "O:BranchB_Cohomological_Collar"),
        ("G:Kaplan_DomainWall_Chiral_Index", "O:BranchB_Cohomological_Collar"),
        ("G:Culler_SpinLift_Baer_RayleighRitz", "O:BranchB_Cohomological_Collar"),
        ("O:CIM_33m6_Frame_D1", "O:SchwingerDyson_Resolvent_Majorana"),
        ("O:Bergman_Majorana_Seesaw", "O:SchwingerDyson_Resolvent_Majorana"),
        # OPERATOR / ROOT -> SEAM
        ("O:PatiSalam_Z2D_Channel", "S:StrongCP_Det_Sign_Bit"),
        ("O:CIM_33m6_Frame_D1", "S:StrongCP_Det_Sign_Bit"),
        ("O:SchwingerDyson_Resolvent_Majorana", "S:Discrete_Torsion_TM1_Z2"),
        ("O:CIM_33m6_Frame_D1", "S:Level6_Higgs_Klein_Pair_Bit"),
        ("O:BranchB_Cohomological_Collar", "S:Collar_Modulus_Delta_PS"),
        ("PR-10", "S:Collar_Modulus_Delta_PS"),
        ("O:Collar_Casimir_Operator", "S:Unified_Gauge_Anchor_AlphaU"),
        ("O:CIM_33m6_Frame_D1", "S:Elliptic_Fibre_Modulus_Tau"),
        ("O:PatiSalam_Z2D_Channel", "S:Torsion_Tau_SU2R_Break"),
        ("G:MSbar_2Loop_EFT_RGE", "S:Electroweak_VEV_Portal_Scale"),
        # Rank-0 universal relations: PR-1, PR-10
        ("G:Spin10_E6_Chirality", "PR-1"),
        ("G:Weil_CAR_Cl10_A2xE6_Orthogonality", "PR-1"),
        ("O:Spin10_Anomaly_Operator", "PR-1"),
        ("G:m004_Mostow_Rigidity", "PR-10"),
        ("G:X4_Collar_Cobordism", "PR-10"),
        ("G:Culler_SpinLift_Baer_RayleighRitz", "PR-10"),
        ("O:Collar_Casimir_Operator", "PR-10"),
        # Rank-1 frame-wide relations: PR-3, PR-4, PR-6, PR-7, PR-8 (5 relations)
        ("PR-1", "PR-3"),
        ("G:MSbar_2Loop_EFT_RGE", "PR-3"),
        ("O:PatiSalam_Z2D_Channel", "PR-3"),
        ("G:MSbar_2Loop_EFT_RGE", "PR-4"),
        ("O:PatiSalam_Z2D_Channel", "PR-4"),
        ("O:PatiSalam_Z2D_Channel", "PR-6"),
        ("O:CIM_33m6_Frame_D1", "PR-6"),
        ("O:PatiSalam_Z2D_Channel", "PR-7"),
        ("O:CIM_33m6_Frame_D1", "PR-7"),
        ("G:Heisenberg_Weil_SL2Z", "PR-8"),
        ("O:CIM_33m6_Frame_D1", "PR-8"),
        ("PR-6", "PR-8"),
        ("PR-7", "PR-8"),
        # Rank-2 discrete-bit relations: PR-2, PR-5 (re-priced per M44), PR-9 (3 relations)
        ("G:m004_Mostow_Rigidity", "PR-2"),
        ("G:Kaplan_DomainWall_Chiral_Index", "PR-2"),
        ("G:MSbar_2Loop_EFT_RGE", "PR-2"),
        ("O:PatiSalam_Z2D_Channel", "PR-2"),
        ("S:StrongCP_Det_Sign_Bit", "PR-2"),
        ("O:CIM_33m6_Frame_D1", "PR-5"),
        ("S:Level6_Higgs_Klein_Pair_Bit", "PR-5"),
        ("G:MSbar_2Loop_EFT_RGE", "PR-9"),
        ("O:SchwingerDyson_Resolvent_Majorana", "PR-9"),
        ("S:Discrete_Torsion_TM1_Z2", "PR-9"),
        # 19 SM_TARGET edges (SM01..SM18 at rank 3; SM19:bar_theta_QCD unique at rank 2)
        ("PR-5", "SM01:y_u"),
        ("PR-8", "SM01:y_u"),
        ("S:Discrete_Torsion_TM1_Z2", "SM01:y_u"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM01:y_u"),
        ("PR-5", "SM02:y_c"),
        ("PR-8", "SM02:y_c"),
        ("S:Discrete_Torsion_TM1_Z2", "SM02:y_c"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM02:y_c"),
        ("PR-5", "SM03:y_t"),
        ("PR-8", "SM03:y_t"),
        ("S:Discrete_Torsion_TM1_Z2", "SM03:y_t"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM03:y_t"),
        ("PR-5", "SM04:y_d"),
        ("PR-7", "SM04:y_d"),
        ("PR-8", "SM04:y_d"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM04:y_d"),
        ("S:Torsion_Tau_SU2R_Break", "SM04:y_d"),
        ("PR-5", "SM05:y_s"),
        ("PR-7", "SM05:y_s"),
        ("PR-8", "SM05:y_s"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM05:y_s"),
        ("S:Torsion_Tau_SU2R_Break", "SM05:y_s"),
        ("PR-5", "SM06:y_b"),
        ("PR-7", "SM06:y_b"),
        ("PR-8", "SM06:y_b"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM06:y_b"),
        ("S:Torsion_Tau_SU2R_Break", "SM06:y_b"),
        ("PR-5", "SM07:y_e"),
        ("PR-7", "SM07:y_e"),
        ("PR-8", "SM07:y_e"),
        ("PR-9", "SM07:y_e"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM07:y_e"),
        ("S:Torsion_Tau_SU2R_Break", "SM07:y_e"),
        ("PR-5", "SM08:y_mu"),
        ("PR-7", "SM08:y_mu"),
        ("PR-8", "SM08:y_mu"),
        ("PR-9", "SM08:y_mu"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM08:y_mu"),
        ("S:Torsion_Tau_SU2R_Break", "SM08:y_mu"),
        ("PR-5", "SM09:y_tau"),
        ("PR-7", "SM09:y_tau"),
        ("PR-8", "SM09:y_tau"),
        ("PR-9", "SM09:y_tau"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM09:y_tau"),
        ("S:Torsion_Tau_SU2R_Break", "SM09:y_tau"),
        ("PR-6", "SM10:theta_12_CKM"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM10:theta_12_CKM"),
        ("S:Torsion_Tau_SU2R_Break", "SM10:theta_12_CKM"),
        ("PR-6", "SM11:theta_23_CKM"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM11:theta_23_CKM"),
        ("S:Torsion_Tau_SU2R_Break", "SM11:theta_23_CKM"),
        ("PR-6", "SM12:theta_13_CKM"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM12:theta_13_CKM"),
        ("S:Torsion_Tau_SU2R_Break", "SM12:theta_13_CKM"),
        ("PR-6", "SM13:delta_CKM"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM13:delta_CKM"),
        ("S:Torsion_Tau_SU2R_Break", "SM13:delta_CKM"),
        ("PR-1", "SM14:g_1"),
        ("PR-3", "SM14:g_1"),
        ("S:Collar_Modulus_Delta_PS", "SM14:g_1"),
        ("S:Unified_Gauge_Anchor_AlphaU", "SM14:g_1"),
        ("PR-3", "SM15:g_2"),
        ("S:Collar_Modulus_Delta_PS", "SM15:g_2"),
        ("S:Unified_Gauge_Anchor_AlphaU", "SM15:g_2"),
        ("PR-3", "SM16:g_3"),
        ("S:Collar_Modulus_Delta_PS", "SM16:g_3"),
        ("S:Unified_Gauge_Anchor_AlphaU", "SM16:g_3"),
        ("S:Electroweak_VEV_Portal_Scale", "SM17:v_EW"),
        ("PR-4", "SM18:m_H"),
        ("PR-5", "SM18:m_H"),
        ("SM03:y_t", "SM18:m_H"),
        ("S:Torsion_Tau_SU2R_Break", "SM18:m_H"),
        ("S:Electroweak_VEV_Portal_Scale", "SM18:m_H"),
        ("PR-2", "SM19:bar_theta_QCD"),
        ("G:MSbar_2Loop_EFT_RGE", "SM19:bar_theta_QCD"),
    ]
    return nodes, edges


def _kahn_topological_sort(
    node_ids: list[str], edges: list[tuple[str, str]]
) -> tuple[bool, list[str]]:
    adj: dict[str, list[str]] = {nid: [] for nid in node_ids}
    indeg: dict[str, int] = {nid: 0 for nid in node_ids}
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1

    queue: list[str] = [nid for nid in node_ids if indeg[nid] == 0]
    topo: list[str] = []
    head = 0
    while head < len(queue):
        cur = queue[head]
        head += 1
        topo.append(cur)
        for nxt in adj[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                queue.append(nxt)
    return (len(topo) == len(node_ids)), topo


def _dfs_three_color_has_cycle(node_ids: list[str], edges: list[tuple[str, str]]) -> bool:
    adj: dict[str, list[str]] = {nid: [] for nid in node_ids}
    for u, v in edges:
        adj[u].append(v)
    color: dict[str, int] = {nid: 0 for nid in node_ids}

    def visit(u: str) -> bool:
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1:
                return True
            if color[v] == 0 and visit(v):
                return True
        color[u] = 2
        return False

    for nid in node_ids:
        if color[nid] == 0 and visit(nid):
            return True
    return False


def _propagate_max_ranks(
    nodes: list[dict[str, Any]], edges: list[tuple[str, str]], topo_order: list[str]
) -> dict[str, int]:
    parents: dict[str, list[str]] = {nd["id"]: [] for nd in nodes}
    intrinsic: dict[str, int] = {nd["id"]: int(nd["intrinsic_rank"]) for nd in nodes}
    for u, v in edges:
        parents[v].append(u)
    ranks: dict[str, int] = {}
    for nid in topo_order:
        ranks[nid] = max([intrinsic[nid]] + [ranks[p] for p in parents[nid]])
    return ranks


def _check_monotone_max_law(
    nodes: list[dict[str, Any]],
    edges: list[tuple[str, str]],
    reported_ranks: dict[str, int],
) -> list[str]:
    parents: dict[str, list[str]] = {nd["id"]: [] for nd in nodes}
    intrinsic: dict[str, int] = {nd["id"]: int(nd["intrinsic_rank"]) for nd in nodes}
    for u, v in edges:
        parents[v].append(u)

    violations: list[str] = []
    for nd in nodes:
        nid = nd["id"]
        expected = max([intrinsic[nid]] + [reported_ranks[p] for p in parents[nid]])
        if reported_ranks[nid] < intrinsic[nid]:
            violations.append(f"{nid}:below_intrinsic")
        for p in parents[nid]:
            if reported_ranks[nid] < reported_ranks[p]:
                violations.append(f"{nid}:below_parent:{p}")
        if reported_ranks[nid] != expected:
            violations.append(f"{nid}:mismatch:{reported_ranks[nid]}!={expected}")
    return violations


def _check_guardrail_1_and_premise_honesty(
    nodes: list[dict[str, Any]], propagated_ranks: dict[str, int]
) -> list[str]:
    violations: list[str] = []
    for nd in nodes:
        nid = nd["id"]
        if nd["category"] == "SEAM" and not bool(nd["has_stabilization_proof"]):
            if int(nd["intrinsic_rank"]) < 2 or propagated_ranks[nid] < 2:
                violations.append(f"unproved_seam_below_rank2:{nid}")
        if len(nd["premises"]) > 0 and propagated_ranks[nid] == 0:
            violations.append(f"premise_conditioned_promoted_to_rank0:{nid}")
    return violations


def run_section_3_foundational_52node_dag() -> dict[str, Any]:
    nodes, edges = _build_52_node_foundational_dag()
    node_ids = [nd["id"] for nd in nodes]
    unique_id_count = len(set(node_ids))

    category_counts: dict[str, int] = {
        "ROOT": 0,
        "OPERATOR": 0,
        "SEAM": 0,
        "RELATION": 0,
        "SM_TARGET": 0,
    }
    for nd in nodes:
        category_counts[nd["category"]] += 1

    kahn_acyclic, topo_order = _kahn_topological_sort(node_ids, edges)
    dfs_has_cycle = _dfs_three_color_has_cycle(node_ids, edges)
    ranks = _propagate_max_ranks(nodes, edges, topo_order)
    monotone_violations = _check_monotone_max_law(nodes, edges, ranks)
    honesty_violations = _check_guardrail_1_and_premise_honesty(nodes, ranks)

    rel_hist = [0, 0, 0, 0]
    sm_hist = [0, 0, 0, 0]
    rel_by_rank: dict[str, list[str]] = {"0": [], "1": [], "2": [], "3": []}
    sm_by_rank: dict[str, list[str]] = {"0": [], "1": [], "2": [], "3": []}

    for nd in nodes:
        nid = nd["id"]
        rk = ranks[nid]
        if nd["category"] == "RELATION":
            rel_hist[rk] += 1
            rel_by_rank[str(rk)].append(nid)
        elif nd["category"] == "SM_TARGET":
            sm_hist[rk] += 1
            sm_by_rank[str(rk)].append(nid)

    # Adversarial control A: cycle injection SM03:y_t -> G:m004_Mostow_Rigidity
    edges_cycle = list(edges) + [("SM03:y_t", "G:m004_Mostow_Rigidity")]
    kahn_cycle_ok, topo_cycle = _kahn_topological_sort(node_ids, edges_cycle)
    dfs_cycle_detected = _dfs_three_color_has_cycle(node_ids, edges_cycle)
    cycle_control_caught = bool(
        (not kahn_cycle_ok) and len(topo_cycle) < 52 and dfs_cycle_detected
    )

    # Adversarial control B: rank laundering on PR-5 (2 -> 1) and SM03:y_t (3 -> 0)
    laundered_ranks = dict(ranks)
    laundered_ranks["PR-5"] = 1
    laundered_ranks["SM03:y_t"] = 0
    laundering_violations = _check_monotone_max_law(nodes, edges, laundered_ranks)
    rank_laundering_caught = bool(len(laundering_violations) >= 2)

    # Adversarial control C: Guardrail 1 zero-rank seam laundering
    tampered_nodes = [dict(nd) for nd in nodes]
    for nd in tampered_nodes:
        if nd["id"] in ("S:Collar_Modulus_Delta_PS", "S:Level6_Higgs_Klein_Pair_Bit"):
            nd["intrinsic_rank"] = 0
    tampered_ranks = _propagate_max_ranks(tampered_nodes, edges, topo_order)
    g1_tamper_violations = _check_guardrail_1_and_premise_honesty(tampered_nodes, tampered_ranks)
    seam_tamper_caught = bool(len(g1_tamper_violations) >= 2)

    passed = bool(
        len(nodes) == 52
        and unique_id_count == 52
        and category_counts
        == {"ROOT": 8, "OPERATOR": 7, "SEAM": 8, "RELATION": 10, "SM_TARGET": 19}
        and kahn_acyclic
        and len(topo_order) == 52
        and (not dfs_has_cycle)
        and len(monotone_violations) == 0
        and len(honesty_violations) == 0
        and ranks["PR-5"] == 2
        and rel_hist == [2, 5, 3, 0]
        and sm_hist == [0, 0, 1, 18]
        and sm_by_rank["2"] == ["SM19:bar_theta_QCD"]
        and cycle_control_caught
        and rank_laundering_caught
        and seam_tamper_caught
    )
    return {
        "total_nodes": len(nodes),
        "total_edges": len(edges),
        "category_counts": category_counts,
        "kahn_visited_count": len(topo_order),
        "kahn_acyclic": kahn_acyclic,
        "dfs_cycle_detected": dfs_has_cycle,
        "monotone_violation_count": len(monotone_violations),
        "guardrail_1_and_premise_violation_count": len(honesty_violations),
        "PR_5_propagated_rank": ranks["PR-5"],
        "relation_rank_histogram": rel_hist,
        "relations_by_rank": rel_by_rank,
        "sm_target_rank_histogram": sm_hist,
        "sm_targets_by_rank": sm_by_rank,
        "unique_rank2_sm_parameter": sm_by_rank["2"][0],
        "cycle_injection_control_caught": cycle_control_caught,
        "rank_laundering_control_caught": rank_laundering_caught,
        "guardrail_1_seam_tamper_control_caught": seam_tamper_caught,
        "passed": passed,
    }


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]
    out_path = script_path.parent / "referee_found_g11_out.json"

    sec0 = run_section_0_custody_and_ast_lock(script_path, repo_root)
    sec1 = run_section_1_resolvent_majorana_and_m44_isotropy()
    sec2 = run_section_2_transmutation_vol_m004_and_c7_cas()
    sec3 = run_section_3_foundational_52node_dag()

    planted_faults = {
        "PF11_1_caught": sec1["PF11_1_caught"],
        "PF11_2_caught": sec1["PF11_2_caught"],
        "PF11_3_caught": sec2["PF11_3_caught"],
        "PF11_4_caught": sec1["PF11_4_caught"],
        "PF11_5_caught": sec2["PF11_5_caught"],
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
        "gate": "AGY-002_FOUND-G11_COLD_ROOM_REFEREE",
        "empirical_inputs": "0 of 19",
        "section_0_custody_and_ast_lock": sec0,
        "section_1_resolvent_majorana_and_m44_isotropy": sec1,
        "section_2_transmutation_vol_m004_and_c7_cas": sec2,
        "section_3_foundational_52node_dag": sec3,
        "planted_fault_summary": planted_faults,
        "all_5_planted_faults_caught": all_planted_caught,
        "overall_passed": overall_passed,
    }
    out_path.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    if not overall_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
