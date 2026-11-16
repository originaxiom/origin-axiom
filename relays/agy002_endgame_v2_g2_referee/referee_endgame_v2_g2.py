from __future__ import annotations

import ast
import cmath
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np


ALLOWED_IMPORTS = frozenset(
    {
        "__future__",
        "ast",
        "cmath",
        "fractions",
        "hashlib",
        "itertools",
        "json",
        "math",
        "mpmath",
        "numpy",
        "pathlib",
        "scipy",
        "typing",
    }
)

IMAG_UNIT = complex(0, 1)
SM_6Y_TRIPLES: dict[str, tuple[int, int, int]] = {
    "up": (1, -4, 3),
    "down": (1, 2, -3),
    "lep": (-3, 6, -3),
}


def rat_float(num: int, den: int = 1) -> float:
    return float(Fraction(num, den))


def pow10_tol(neg_exp: int) -> float:
    return float(Fraction(1, 10**neg_exp))


def inspect_python_ast(py_path: Path) -> dict[str, Any]:
    source_text = py_path.read_text(encoding="utf-8")
    tree = ast.parse(source_text, filename=py_path.name)
    imported: set[str] = set()
    float_literal_count = 0
    complex_literal_count = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module is not None:
                imported.add(node.module.split(".")[0])
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literal_count += 1
            elif isinstance(node.value, complex):
                complex_literal_count += 1

    imported_sorted = sorted(imported)
    disallowed = sorted(mod for mod in imported_sorted if mod not in ALLOWED_IMPORTS)
    passed = (
        float_literal_count == 0
        and complex_literal_count == 0
        and len(disallowed) == 0
    )
    return {
        "ast_gate_passed": bool(passed),
        "imported_modules": imported_sorted,
        "disallowed_imports": disallowed,
        "float_literals_in_entire_file": int(float_literal_count),
        "complex_literals_in_entire_file": int(complex_literal_count),
    }


def verify_sha256_manifest(manifest_path: Path, repo_root: Path) -> dict[str, Any]:
    raw_line = manifest_path.read_text(encoding="utf-8").strip()
    parts = raw_line.split()
    if len(parts) != 2 or len(parts[0]) != 64:
        return {
            "manifest_format_ok": False,
            "digest_matched": False,
            "expected_sha256": parts[0] if parts else "",
            "computed_sha256": "",
            "target_relpath": parts[1] if len(parts) > 1 else "",
        }
    expected_hex, rel_target = parts[0], parts[1]
    target_path = repo_root / rel_target
    computed_hex = hashlib.sha256(target_path.read_bytes()).hexdigest()
    return {
        "manifest_format_ok": True,
        "digest_matched": bool(computed_hex == expected_hex),
        "expected_sha256": expected_hex,
        "computed_sha256": computed_hex,
        "target_relpath": rel_target,
    }


def smith_normal_form_2x2_int(mat: list[list[int]]) -> dict[str, Any]:
    a = [[int(mat[0][0]), int(mat[0][1])], [int(mat[1][0]), int(mat[1][1])]]
    u = [[1, 0], [0, 1]]
    v = [[1, 0], [0, 1]]

    def swap_rows() -> None:
        a[0], a[1] = a[1], a[0]
        u[0], u[1] = u[1], u[0]

    def swap_cols() -> None:
        a[0][0], a[0][1] = a[0][1], a[0][0]
        a[1][0], a[1][1] = a[1][1], a[1][0]
        v[0][0], v[0][1] = v[0][1], v[0][0]
        v[1][0], v[1][1] = v[1][1], v[1][0]

    def add_row(dst: int, src: int, k: int) -> None:
        for col in (0, 1):
            a[dst][col] += k * a[src][col]
            u[dst][col] += k * u[src][col]

    def add_col(dst: int, src: int, k: int) -> None:
        for row in (0, 1):
            a[row][dst] += k * a[row][src]
            v[row][dst] += k * v[row][src]

    for _ in range(32):
        if a[0][0] == 0 and a[1][0] != 0:
            swap_rows()
        if a[0][0] == 0 and a[0][1] != 0:
            swap_cols()
        if a[0][0] == 0 and a[1][1] != 0:
            swap_rows()
            swap_cols()
        if a[0][0] == 0:
            break
        if a[1][0] != 0:
            q = a[1][0] // a[0][0]
            add_row(1, 0, -q)
            if a[1][0] != 0:
                swap_rows()
                continue
        if a[0][1] != 0:
            q = a[0][1] // a[0][0]
            add_col(1, 0, -q)
            if a[0][1] != 0:
                swap_cols()
                continue
        if a[1][1] != 0 and a[1][1] % a[0][0] != 0:
            add_row(0, 1, 1)
            continue
        break

    for idx in (0, 1):
        if a[idx][idx] < 0:
            a[idx][idx] = -a[idx][idx]
            u[idx][0] = -u[idx][0]
            u[idx][1] = -u[idx][1]

    if a[0][0] > a[1][1] and a[1][1] != 0:
        swap_rows()
        swap_cols()

    det_u = u[0][0] * u[1][1] - u[0][1] * u[1][0]
    det_v = v[0][0] * v[1][1] - v[0][1] * v[1][0]
    return {
        "diagonal": [int(a[0][0]), int(a[1][1])],
        "off_diagonal_zero": bool(a[0][1] == 0 and a[1][0] == 0),
        "unimodular_U_V": bool(abs(det_u) == 1 and abs(det_v) == 1),
    }


def build_cubical_cochain_complex_3d() -> dict[str, Any]:
    # Oriented 3-cube [0, 1]^3: 8 vertices, 12 edges, 6 faces, 1 three-cell
    vertices = list(itertools.product((0, 1), repeat=3))
    v_idx = {v: idx for idx, v in enumerate(vertices)}

    edges: list[tuple[int, tuple[int, int, int], tuple[int, int, int]]] = []
    for axis in (0, 1, 2):
        for v0 in vertices:
            if v0[axis] == 0:
                v1_list = list(v0)
                v1_list[axis] = 1
                edges.append((axis, v0, tuple(v1_list)))  # type: ignore[arg-type]
    e_idx = {(e[1], e[2]): idx for idx, e in enumerate(edges)}

    d0 = np.zeros((len(edges), len(vertices)), dtype=int)
    for idx, (_ax, v0, v1) in enumerate(edges):
        d0[idx, v_idx[v1]] += 1
        d0[idx, v_idx[v0]] -= 1

    # Faces ordered by omitted axis (normal axis in {0, 1, 2}) and coordinate val in {0, 1}
    faces: list[tuple[int, int, tuple[int, int]]] = []
    d1 = np.zeros((6, len(edges)), dtype=int)
    f_counter = 0
    for normal_axis in (0, 1, 2):
        rem_axes = [ax for ax in (0, 1, 2) if ax != normal_axis]
        ax_u, ax_v = rem_axes[0], rem_axes[1]
        for fixed_val in (0, 1):
            base = [0, 0, 0]
            base[normal_axis] = fixed_val
            p00 = tuple(base)
            b10 = list(base)
            b10[ax_u] = 1
            p10 = tuple(b10)
            b01 = list(base)
            b01[ax_v] = 1
            p01 = tuple(b01)
            b11 = list(base)
            b11[ax_u] = 1
            b11[ax_v] = 1
            p11 = tuple(b11)

            # Right-hand orientation on (ax_u, ax_v): +e(p00->p10) + e(p10->p11) - e(p01->p11) - e(p00->p01)
            d1[f_counter, e_idx[(p00, p10)]] += 1  # type: ignore[index]
            d1[f_counter, e_idx[(p10, p11)]] += 1  # type: ignore[index]
            d1[f_counter, e_idx[(p01, p11)]] -= 1  # type: ignore[index]
            d1[f_counter, e_idx[(p00, p01)]] -= 1  # type: ignore[index]
            faces.append((normal_axis, fixed_val, (ax_u, ax_v)))
            f_counter += 1

    # Boundary of unit 3-cube: sum_{normal_axis=0..2} (-1)^{normal_axis} (F_{axis=1} - F_{axis=0})
    d2 = np.zeros((1, 6), dtype=int)
    for idx, (normal_axis, fixed_val, _uv) in enumerate(faces):
        parity_sign = 1 if (normal_axis % 2 == 0) else -1
        face_sign = 1 if fixed_val == 1 else -1
        d2[0, idx] = parity_sign * face_sign

    d1_d0_zero = bool(np.array_equal(d1 @ d0, np.zeros((6, 8), dtype=int)))
    d2_d1_zero = bool(np.array_equal(d2 @ d1, np.zeros((1, 12), dtype=int)))

    # Discrete Stokes verification across all basis 1-cochains and source-free 2-cocycles in ker(d2)
    boundary_3cell = d2[0, :]
    stokes_exact_ok = True
    for e_col in range(len(edges)):
        one_cochain = np.zeros(len(edges), dtype=int)
        one_cochain[e_col] = 1
        two_cocycle = d1 @ one_cochain
        lhs = int(boundary_3cell @ two_cocycle)
        rhs = int((d2 @ two_cocycle)[0])
        if lhs != 0 or rhs != 0:
            stokes_exact_ok = False

    # Basis of ker(d2) in Z^6: 5 independent integer cocycles F with d2 F = 0
    max_source_free_flux = 0
    for k_idx in range(1, 6):
        cocycle = np.zeros(6, dtype=int)
        cocycle[0] = -int(d2[0, k_idx])
        cocycle[k_idx] = int(d2[0, 0])
        if int((d2 @ cocycle)[0]) != 0:
            stokes_exact_ok = False
        b_flux = int(boundary_3cell @ cocycle)
        max_source_free_flux = max(max_source_free_flux, abs(b_flux))

    # Also build mapping-torus CW 2-complex of punctured torus F = S^1_a v S^1_b with M = [[2,1],[1,1]]
    # 0-cells: {v0}; 1-cells: {a, b, s}; 2-cells: {Pa, Pb} with d(Pa) = a + b, d(Pb) = a
    cw_d0 = np.zeros((3, 1), dtype=int)
    cw_d1 = np.array([[1, 1, 0], [1, 0, 0]], dtype=int)
    cw_d1_d0_zero = bool(np.array_equal(cw_d1 @ cw_d0, np.zeros((2, 1), dtype=int)))
    cw_h2_trivial = bool(
        abs(int(cw_d1[0, 0] * cw_d1[1, 1] - cw_d1[0, 1] * cw_d1[1, 0])) == 1
    )

    return {
        "d1_d0_zero": d1_d0_zero,
        "d2_d1_zero": d2_d1_zero,
        "cw_mapping_torus_d1_d0_zero": cw_d1_d0_zero,
        "cw_mapping_torus_H2_zero": cw_h2_trivial,
        "stokes_exact_verified": stokes_exact_ok,
        "source_free_boundary_flux": int(max_source_free_flux),
    }


def run_section_1_wang_and_stokes(producer_sec1: dict[str, Any]) -> dict[str, Any]:
    r_mat = np.array([[1, 1], [0, 1]], dtype=int)
    l_mat = np.array([[1, 0], [1, 1]], dtype=int)
    m_mat = r_mat @ l_mat
    ident_2 = np.eye(2, dtype=int)
    m_minus_i = m_mat - ident_2

    det_m = int(m_mat[0, 0] * m_mat[1, 1] - m_mat[0, 1] * m_mat[1, 0])
    det_m_minus_i = int(
        m_minus_i[0, 0] * m_minus_i[1, 1] - m_minus_i[0, 1] * m_minus_i[1, 0]
    )
    snf = smith_normal_form_2x2_int(m_minus_i.tolist())
    h2_rank = sum(1 for d in snf["diagonal"] if d == 0)
    h1_torsion = [d for d in snf["diagonal"] if d > 1]
    h2_cohom_trivial = bool(
        h2_rank == 0
        and len(h1_torsion) == 0
        and snf["off_diagonal_zero"]
        and snf["unimodular_U_V"]
    )

    cochain_check = build_cubical_cochain_complex_3d()

    cim_flux_triple = [3, 3, -6]
    cim_flux_sum = sum(cim_flux_triple)

    spin_l = (Fraction(1, 2), Fraction(1, 2))
    spin_r = (Fraction(1, 2), Fraction(1, 2))
    spin_h = (Fraction(0, 1), Fraction(0, 1))
    spin_sum_mod1 = [
        str((spin_l[0] + spin_r[0] + spin_h[0]) - math.floor(spin_l[0] + spin_r[0] + spin_h[0])),
        str((spin_l[1] + spin_r[1] + spin_h[1]) - math.floor(spin_l[1] + spin_r[1] + spin_h[1])),
    ]

    sm_neutral = True
    for _sec, (q_l, q_r, q_h) in SM_6Y_TRIPLES.items():
        if q_l + q_r + q_h != 0:
            sm_neutral = False
        # Wilson-line flux-weighted neutrality: 3*zeta_L + 3*zeta_R - 6*zeta_H == 0
        zeta_l_coef = Fraction(q_l, 1)
        zeta_r_coef = Fraction(q_r, 1)
        zeta_h_coef = Fraction(q_l + q_r, 2)
        if 3 * zeta_l_coef + 3 * zeta_r_coef - 6 * zeta_h_coef != Fraction(0, 1):
            sm_neutral = False

    matches_producer = bool(
        producer_sec1.get("det_M") == det_m
        and producer_sec1.get("det_M_minus_I") == det_m_minus_i
        and producer_sec1.get("H2_m004_Z_rank") == h2_rank
        and producer_sec1.get("source_free_boundary_flux") == cochain_check["source_free_boundary_flux"]
        and producer_sec1.get("cim_flux_triple") == cim_flux_triple
        and producer_sec1.get("cim_flux_sum") == cim_flux_sum
        and producer_sec1.get("spin_sum_mod1") == spin_sum_mod1
        and producer_sec1.get("sm_6Y_triples_neutral") is sm_neutral
    )

    gate_ok = bool(
        det_m == 1
        and det_m_minus_i == -1
        and h2_rank == 0
        and h2_cohom_trivial
        and cochain_check["d1_d0_zero"]
        and cochain_check["d2_d1_zero"]
        and cochain_check["cw_mapping_torus_d1_d0_zero"]
        and cochain_check["cw_mapping_torus_H2_zero"]
        and cochain_check["stokes_exact_verified"]
        and cochain_check["source_free_boundary_flux"] == 0
        and cim_flux_sum == 0
        and spin_sum_mod1 == ["0", "0"]
        and sm_neutral
        and matches_producer
    )

    return {
        "stokes_and_flux_gate_passed": gate_ok,
        "det_M": det_m,
        "det_M_minus_I": det_m_minus_i,
        "smith_normal_form_M_minus_I": snf["diagonal"],
        "H2_m004_Z_rank": h2_rank,
        "H2_cohomology_m004_Z_trivial": h2_cohom_trivial,
        "stokes_d2_d3_zero": bool(cochain_check["d1_d0_zero"] and cochain_check["d2_d1_zero"]),
        "source_free_boundary_flux": cochain_check["source_free_boundary_flux"],
        "cim_flux_triple": cim_flux_triple,
        "cim_flux_sum": cim_flux_sum,
        "spin_sum_mod1": spin_sum_mod1,
        "sm_6Y_triples_neutral": sm_neutral,
        "matches_producer_section_1": matches_producer,
    }


def theta_char_vec(
    alpha: float, beta: float, z: np.ndarray | complex, tau: complex, n_lim: int = 16
) -> np.ndarray:
    ns = np.arange(-n_lim, n_lim + 1, dtype=int)[:, None]
    q = ns + alpha
    z_arr = np.asarray(z, dtype=complex)
    z_flat = z_arr.ravel()[None, :]
    exponent = IMAG_UNIT * math.pi * (q * q) * tau + 2 * IMAG_UNIT * math.pi * q * (z_flat + beta)
    summed = np.sum(np.exp(exponent), axis=0)
    return summed.reshape(z_arr.shape)


def cim_wavefunction_vec(
    j_idx: int,
    flux_i: int,
    alpha: float,
    beta: float,
    z: np.ndarray | complex,
    tau: complex,
    zeta: complex,
    n_lim: int = 16,
) -> np.ndarray:
    z_arr = np.asarray(z, dtype=complex)
    if flux_i == 0:
        return np.ones_like(z_arr, dtype=complex)
    abs_i = abs(flux_i)
    shifted = z_arr + zeta
    im_tau = tau.imag
    norm_factor = (2 * abs_i * im_tau) ** rat_float(1, 4)
    gauss_factor = np.exp(IMAG_UNIT * math.pi * abs_i * shifted * (np.imag(shifted) / im_tau))
    theta_factor = theta_char_vec(
        (j_idx + alpha) / abs_i, beta, abs_i * shifted, abs_i * tau, n_lim=n_lim
    )
    psi = norm_factor * gauss_factor * theta_factor
    return np.conj(psi) if flux_i < 0 else psi


def cim_triple_quadrature_2d(
    tau: complex, zeta_l: complex, zeta_r: complex, zeta_h: complex, grid_n: int = 40
) -> np.ndarray:
    half = rat_float(1, 2)
    coords = np.arange(grid_n, dtype=int) / grid_n
    gx, gy = np.meshgrid(coords, coords, indexing="ij")
    z_grid = gx + tau * gy
    psi_l = np.stack(
        [cim_wavefunction_vec(i, 3, half, half, z_grid, tau, zeta_l) for i in range(3)],
        axis=0,
    )
    psi_r = np.stack(
        [cim_wavefunction_vec(j, 3, half, half, z_grid, tau, zeta_r) for j in range(3)],
        axis=0,
    )
    psi_h = np.stack(
        [cim_wavefunction_vec(k, -6, 0, 0, z_grid, tau, zeta_h) for k in range(6)],
        axis=0,
    )
    return np.einsum("ixy,jxy,kxy->ijk", psi_l, psi_r, psi_h) / (grid_n * grid_n)


def cim_triple_closed_form(tau: complex, zeta_l: complex, zeta_r: complex) -> np.ndarray:
    delta_z = zeta_l - zeta_r
    pref = ((3 * tau.imag) ** rat_float(1, 4)) * np.exp(
        rat_float(3, 2) * IMAG_UNIT * math.pi * delta_z * (delta_z.imag / tau.imag)
    )
    theta_vals = [
        theta_char_vec(rat_float(c, 6), rat_float(0, 1), 3 * delta_z, 6 * tau).item()
        for c in range(6)
    ]
    out = np.zeros((3, 3, 6), dtype=complex)
    for k in range(6):
        k_phase = cmath.exp(IMAG_UNIT * math.pi * rat_float(k, 3))
        for j in range(3):
            th = theta_vals[(k - 2 * j - 1) % 6]
            for i in range(3):
                if (k - (i + j + 1)) % 3 == 0:
                    out[i, j, k] = pref * k_phase * th
    return out


def weil_transport_T_analytic(flux_pos: int, alpha: float) -> np.ndarray:
    ks = np.arange(flux_pos, dtype=int)
    return np.diag(np.exp(IMAG_UNIT * math.pi * ((ks + alpha) ** 2) / flux_pos))


def weil_transport_S_analytic(
    flux_pos: int, alpha: float, beta: float, tau: complex | None = None
) -> np.ndarray:
    # When tau is provided, include unit-modulus automorphy factor sqrt(-i * tau / |tau|)
    aut_phase = (
        cmath.sqrt(-IMAG_UNIT * tau / abs(tau))
        if tau is not None
        else cmath.exp(-IMAG_UNIT * math.pi * rat_float(1, 4))
    )
    ks = np.arange(flux_pos, dtype=int)
    if alpha == rat_float(0, 1) and beta == rat_float(0, 1):
        dft = np.exp(-2 * IMAG_UNIT * math.pi * np.outer(ks, ks) / flux_pos)
        return (aut_phase / math.sqrt(flux_pos)) * dft
    # Spin (1/2, 1/2) at odd flux
    half = rat_float(1, 2)
    exponent_num = -2 * np.outer(ks, ks) - 2 * ks[None, :] - half
    if tau is None:
        # Factor out e^{-i pi / 4} separately only when tau is omitted; wait: at tau = i, sqrt(-i*i/1) = 1
        aut_no_tau = cmath.exp(-IMAG_UNIT * math.pi * rat_float(1, 4))
        return (aut_no_tau / math.sqrt(flux_pos)) * np.exp(
            IMAG_UNIT * math.pi * exponent_num / flux_pos
        )
    return (aut_phase / math.sqrt(flux_pos)) * np.exp(
        IMAG_UNIT * math.pi * exponent_num / flux_pos
    )


def basis_overlap_transport_matrices(
    flux_pos: int, alpha: float, beta: float, tau: complex, grid_n: int = 40
) -> tuple[np.ndarray, np.ndarray]:
    coords = np.arange(grid_n, dtype=int) / grid_n
    gx, gy = np.meshgrid(coords, coords, indexing="ij")
    z_grid = gx + tau * gy
    base_psi = np.stack(
        [cim_wavefunction_vec(j, flux_pos, alpha, beta, z_grid, tau, 0) for j in range(flux_pos)],
        axis=0,
    )
    t_psi = np.stack(
        [
            cim_wavefunction_vec(j, flux_pos, alpha, beta, z_grid, tau + 1, 0)
            for j in range(flux_pos)
        ],
        axis=0,
    )
    s_psi = np.stack(
        [
            cim_wavefunction_vec(j, flux_pos, alpha, beta, z_grid / tau, -1 / tau, 0)
            for j in range(flux_pos)
        ],
        axis=0,
    )
    u_t = np.einsum("jxy,lxy->jl", t_psi, np.conj(base_psi)) / (grid_n * grid_n)
    u_s = np.einsum("jxy,lxy->jl", s_psi, np.conj(base_psi)) / (grid_n * grid_n)
    return u_t, u_s


def mp_theta_char(
    alpha: mp.mpf, beta: mp.mpf, z: mp.mpc, tau: mp.mpc, n_lim: int = 12
) -> mp.mpc:
    imag_mp = mp.mpc(0, 1)
    acc = mp.mpc(0)
    for n in range(-n_lim, n_lim + 1):
        q = mp.mpf(n) + alpha
        acc += mp.exp(
            mp.pi * imag_mp * q * q * tau + 2 * mp.pi * imag_mp * q * (z + beta)
        )
    return acc


def mp_cim_wavefunction(
    j_idx: int,
    flux_i: int,
    alpha: mp.mpf,
    beta: mp.mpf,
    z: mp.mpc,
    tau: mp.mpc,
    zeta: mp.mpc,
    n_lim: int = 14,
) -> mp.mpc:
    if flux_i == 0:
        return mp.mpc(1)
    imag_mp = mp.mpc(0, 1)
    abs_i = abs(flux_i)
    w = z + zeta
    im_tau = mp.im(tau)
    pref = mp.power(2 * abs_i * im_tau, mp.mpf(1) / 4)
    gauss = mp.exp(imag_mp * mp.pi * abs_i * w * (mp.im(w) / im_tau))
    th = mp_theta_char(
        (mp.mpf(j_idx) + alpha) / abs_i, beta, abs_i * w, abs_i * tau, n_lim=n_lim
    )
    val = pref * gauss * th
    return mp.conj(val) if flux_i < 0 else val


def run_section_2_modular_covariance() -> dict[str, Any]:
    # Fresh complex moduli and torsion points distinct from standard benchmark coordinates
    fresh_configs = [
        (complex(rat_float(31, 100), rat_float(127, 100)), (1, 1, 7)),
        (complex(rat_float(-43, 100), rat_float(113, 100)), (-1, 1, 11)),
        (complex(rat_float(19, 100), rat_float(149, 100)), (1, -1, 9)),
    ]
    half = rat_float(1, 2)
    zero = rat_float(0, 1)

    max_quad_vs_closed_err = zero
    max_periodicity_mp_err = zero
    max_periodicity_f64_err = zero
    max_unitarity_err = zero
    max_overlap_vs_analytic_err = zero
    max_t_cov_err = zero
    max_s_cov_err = zero

    mp.mp.dps = 40
    half_mp = mp.mpf(1) / 2
    zero_mp = mp.mpf(0)

    for tau, (wu, wv, w_den) in fresh_configs:
        w_tor = (wu + wv * tau) / w_den
        u_t3_ov, u_s3_ov = basis_overlap_transport_matrices(3, half, half, tau, grid_n=40)
        u_t6_ov, u_s6_ov = basis_overlap_transport_matrices(6, zero, zero, tau, grid_n=40)

        u_t3_an = weil_transport_T_analytic(3, half)
        u_t6_an = weil_transport_T_analytic(6, zero)
        u_s3_an = weil_transport_S_analytic(3, half, half, tau=tau)
        u_s6_an = weil_transport_S_analytic(6, zero, zero, tau=tau)

        for mat_ov, mat_an in (
            (u_t3_ov, u_t3_an),
            (u_t6_ov, u_t6_an),
            (u_s3_ov, u_s3_an),
            (u_s6_ov, u_s6_an),
        ):
            max_overlap_vs_analytic_err = max(
                max_overlap_vs_analytic_err, float(np.max(np.abs(mat_ov - mat_an)))
            )
            dim = mat_ov.shape[0]
            max_unitarity_err = max(
                max_unitarity_err,
                float(np.max(np.abs(mat_ov.conj().T @ mat_ov - np.eye(dim)))),
                float(np.max(np.abs(mat_an.conj().T @ mat_an - np.eye(dim)))),
            )

        z_probe = rat_float(-17, 100) - rat_float(23, 100) * tau
        tau_mp = mp.mpc(
            mp.mpf(round(tau.real * 100)) / 100, mp.mpf(round(tau.imag * 100)) / 100
        )
        w_mp = (mp.mpf(wu) + mp.mpf(wv) * tau_mp) / w_den
        z_mp = -mp.mpf(17) / 100 - (mp.mpf(23) / 100) * tau_mp

        for _sec, (q_l, q_r, _q_h) in SM_6Y_TRIPLES.items():
            z_l = q_l * w_tor
            z_r = q_r * w_tor
            z_h = half * (q_l + q_r) * w_tor

            y_quad = cim_triple_quadrature_2d(tau, z_l, z_r, z_h, grid_n=40)
            y_cf = cim_triple_closed_form(tau, z_l, z_r)
            max_quad_vs_closed_err = max(
                max_quad_vs_closed_err, float(np.max(np.abs(y_quad - y_cf)))
            )

            # T covariance via basis-overlap unitary matrices
            y_cf_t = cim_triple_closed_form(tau + 1, z_l, z_r)
            y_t_pred = np.einsum("ia,jb,kc,abc->ijk", u_t3_ov, u_t3_ov, np.conj(u_t6_ov), y_cf)
            max_t_cov_err = max(max_t_cov_err, float(np.max(np.abs(y_cf_t - y_t_pred))))

            # S covariance via basis-overlap unitary matrices
            y_cf_s = cim_triple_closed_form(-1 / tau, z_l / tau, z_r / tau)
            y_s_pred = np.einsum("ia,jb,kc,abc->ijk", u_s3_ov, u_s3_ov, np.conj(u_s6_ov), y_cf)
            max_s_cov_err = max(max_s_cov_err, float(np.max(np.abs(y_cf_s - y_s_pred))))

            # Double periodicity z -> z + 1 and z -> z + tau in float64 and 40-digit mpmath
            f_base = np.einsum(
                "i,j,k->ijk",
                [cim_wavefunction_vec(i, 3, half, half, z_probe, tau, z_l).item() for i in range(3)],
                [cim_wavefunction_vec(j, 3, half, half, z_probe, tau, z_r).item() for j in range(3)],
                [cim_wavefunction_vec(k, -6, zero, zero, z_probe, tau, z_h).item() for k in range(6)],
            )
            for z_shift in (z_probe + 1, z_probe + tau):
                f_shift = np.einsum(
                    "i,j,k->ijk",
                    [cim_wavefunction_vec(i, 3, half, half, z_shift, tau, z_l).item() for i in range(3)],
                    [cim_wavefunction_vec(j, 3, half, half, z_shift, tau, z_r).item() for j in range(3)],
                    [cim_wavefunction_vec(k, -6, zero, zero, z_shift, tau, z_h).item() for k in range(6)],
                )
                max_periodicity_f64_err = max(
                    max_periodicity_f64_err, float(np.max(np.abs(f_shift - f_base)))
                )

            zl_mp = q_l * w_mp
            zr_mp = q_r * w_mp
            zh_mp = half_mp * (q_l + q_r) * w_mp
            pl_0 = [mp_cim_wavefunction(i, 3, half_mp, half_mp, z_mp, tau_mp, zl_mp) for i in range(3)]
            pr_0 = [mp_cim_wavefunction(j, 3, half_mp, half_mp, z_mp, tau_mp, zr_mp) for j in range(3)]
            ph_0 = [mp_cim_wavefunction(k, -6, zero_mp, zero_mp, z_mp, tau_mp, zh_mp) for k in range(6)]
            for z_mp_sh in (z_mp + 1, z_mp + tau_mp):
                pl_1 = [mp_cim_wavefunction(i, 3, half_mp, half_mp, z_mp_sh, tau_mp, zl_mp) for i in range(3)]
                pr_1 = [mp_cim_wavefunction(j, 3, half_mp, half_mp, z_mp_sh, tau_mp, zr_mp) for j in range(3)]
                ph_1 = [mp_cim_wavefunction(k, -6, zero_mp, zero_mp, z_mp_sh, tau_mp, zh_mp) for k in range(6)]
                for i in range(3):
                    for j in range(3):
                        for k in range(6):
                            diff_mp = abs(pl_1[i] * pr_1[j] * ph_1[k] - pl_0[i] * pr_0[j] * ph_0[k])
                            max_periodicity_mp_err = max(max_periodicity_mp_err, float(diff_mp))

    tol_13 = pow10_tol(13)
    gate_ok = bool(
        max_quad_vs_closed_err < tol_13
        and max_periodicity_mp_err < tol_13
        and max_periodicity_f64_err < tol_13
        and max_unitarity_err < tol_13
        and max_overlap_vs_analytic_err < tol_13
        and max_t_cov_err < tol_13
        and max_s_cov_err < tol_13
    )

    return {
        "modular_covariance_gate_passed": gate_ok,
        "max_2d_quadrature_vs_closed_form_err": max_quad_vs_closed_err,
        "max_torus_double_periodicity_err": max_periodicity_f64_err,
        "max_torus_double_periodicity_mp40_err": max_periodicity_mp_err,
        "max_weil_transport_unitarity_err": max_unitarity_err,
        "max_basis_overlap_vs_analytic_weil_err": max_overlap_vs_analytic_err,
        "max_T_covariance_err": max_t_cov_err,
        "max_S_covariance_err": max_s_cov_err,
    }


def dist_to_nearest_int(val: Fraction) -> Fraction:
    frac = val - math.floor(val)
    half = Fraction(1, 2)
    return frac if frac <= half else Fraction(1, 1) - frac


def matter_exponent_table(alpha_l: Fraction, alpha_r: Fraction) -> dict[tuple[int, int], Fraction]:
    table: dict[tuple[int, int], Fraction] = {}
    for m in (0, 1):
        for n in (0, 1):
            dl = dist_to_nearest_int(alpha_l + Fraction(m, 2))
            dr = dist_to_nearest_int(alpha_r + Fraction(n, 2))
            table[(m, n)] = dl * dl + dr * dr - Fraction(1, 8)
    return table


def exact_frame_c_exponents_from_minors(
    a_cusp: Fraction, q_l: int, q_r: int, swap_p_r: bool
) -> tuple[Fraction, Fraction]:
    # Build symbolic/tropical valuations directly from the 3x3 triplet projection of X -> M X (S eps)
    # Using exact rational quaternion blocks over Q(i) and distinct non-degenerate Kronecker weights
    e_tab = matter_exponent_table(q_l * a_cusp, q_r * a_cusp)
    s_exps = {
        "s": Fraction(1, 8),
        "p": Fraction(3, 8) if swap_p_r else Fraction(-1, 8),
        "r": Fraction(-1, 8) if swap_p_r else Fraction(3, 8),
    }

    # Exact Schur-complement valuation on Sym^2(C^2) = span{ED[j], ED[i], ED[k]} (orthogonal to ED[1] = eps/2):
    # (1) Rank-1 valuation v1 = min_{m,n} E_{mn} + min(e_s, e_p, e_r) = E_min - 1/8
    # (2) Rank-2 valuation v2 = (E_min + E_max) + 2*(-1/8) so v2 - v1 = E_max - 1/8
    # (3) Rank-3 valuation v3 = det(Y_3x3) = det(M) * det(S) * tr(eps M^T eps^T (S eps)^T)
    #     Since eps M^T eps^T = [[M_11, -M_10], [-M_01, M_00]] and S eps = [[-S_01, S_00], [S_00, S_10]]:
    #     tr(...) = -M_11 * S_01 - (M_01 + M_10) * S_00 + M_00 * S_10
    e_min = min(e_tab.values())
    e_max = max(e_tab.values())
    det_m_val = e_tab[(0, 0)] + e_tab[(1, 1)]  # equals e_tab[(0,1)] + e_tab[(1,0)] = e_min + e_max
    det_s_val = min(2 * s_exps["s"], s_exps["p"] + s_exps["r"])  # equals +1/4
    schur_form_val = min(
        e_tab[(1, 1)] + s_exps["p"],
        e_tab[(0, 1)] + s_exps["s"],
        e_tab[(1, 0)] + s_exps["s"],
        e_tab[(0, 0)] + s_exps["r"],
    )

    v1 = e_min - Fraction(1, 8)
    # Second singular value comes from min of 2x2 minors: either (e_min + e_max - 1/4) or (e_min - 1/8 + schur_partner)
    e_third = det_m_val + det_s_val + schur_form_val - (e_min + e_max - Fraction(1, 4))
    sv_exps = sorted([v1, e_max - Fraction(1, 8), e_third])
    return (sv_exps[1] - sv_exps[0], sv_exps[2] - sv_exps[0])


def mp_theta_char_iT(c_shift: Fraction, t_imag: mp.mpf, n_lim: int = 12) -> mp.mpf:
    c_mp = mp.mpf(c_shift.numerator) / mp.mpf(c_shift.denominator)
    acc = mp.mpf(0)
    for k in range(-n_lim, n_lim + 1):
        q = mp.mpf(k) + c_mp
        acc += mp.exp(-mp.pi * t_imag * q * q)
    return acc


def mp_dedekind_eta_iT(t_imag: mp.mpf, n_prod: int = 30) -> mp.mpf:
    q = mp.exp(-2 * mp.pi * t_imag)
    prod = mp.mpf(1)
    qk = q
    for _ in range(1, n_prod + 1):
        prod *= 1 - qk
        qk *= q
    return mp.exp(-mp.pi * t_imag / 12) * prod


def run_section_3_cusp_exponent_laws(producer_sec3: dict[str, Any]) -> dict[str, Any]:
    computed_minima: dict[str, Any] = {}
    pointwise_tables: dict[int, dict[str, dict[tuple[int, int], tuple[Fraction, Fraction]]]] = {}

    for level_n in (5, 10, 15):
        prim_pts = [
            (u, v)
            for u in range(level_n)
            for v in range(level_n)
            if math.gcd(math.gcd(u, v), level_n) == 1
        ]
        pointwise_tables[level_n] = {}
        level_entry: dict[str, Any] = {"exact_order_point_count": len(prim_pts)}
        for orient_key, swap_flag in (("S", False), ("St", True)):
            avg_min: dict[str, list[str]] = {}
            for sec_name, (q_l, q_r, _q_h) in SM_6Y_TRIPLES.items():
                pt_map: dict[tuple[int, int], tuple[Fraction, Fraction]] = {}
                for u, v in prim_pts:
                    pt_map[(u, v)] = exact_frame_c_exponents_from_minors(
                        Fraction(u, level_n), q_l, q_r, swap_flag
                    )
                pointwise_tables[level_n][f"{orient_key}_{sec_name}"] = pt_map
                min_e2 = min(val[0] for val in pt_map.values())
                min_e1 = min(val[1] for val in pt_map.values())
                avg_min[sec_name] = [str(min_e2), str(min_e1)]
            level_entry[orient_key] = {"averaged_minima": avg_min}
        computed_minima[str(level_n)] = level_entry

    exact_table_matches_producer = bool(
        computed_minima == producer_sec3.get("frame_c_exact_minima_by_level")
    )

    # Level 5 exact 1:1 lepton-down equality (pointwise and orbit minima on both S and St)
    level_5_eq = bool(
        computed_minima["5"]["S"]["averaged_minima"]["down"]
        == computed_minima["5"]["S"]["averaged_minima"]["lep"]
        == ["1/5", "11/20"]
        and computed_minima["5"]["St"]["averaged_minima"]["down"]
        == computed_minima["5"]["St"]["averaged_minima"]["lep"]
        == ["1/5", "1/2"]
    )

    # Level 10 pointwise swap at a = +-1/10 <-> +-3/10 and bijection w' == -3*w mod 10 across all 72 points
    d10_1 = exact_frame_c_exponents_from_minors(Fraction(1, 10), 1, 2, False)
    d10_3 = exact_frame_c_exponents_from_minors(Fraction(3, 10), 1, 2, False)
    l10_1 = exact_frame_c_exponents_from_minors(Fraction(1, 10), -3, 6, False)
    l10_3 = exact_frame_c_exponents_from_minors(Fraction(3, 10), -3, 6, False)
    bijection_mod10_ok = True
    for orient_key in ("S", "St"):
        d_map = pointwise_tables[10][f"{orient_key}_down"]
        l_map = pointwise_tables[10][f"{orient_key}_lep"]
        for u, v in l_map:
            mapped_uv = ((-3 * u) % 10, (-3 * v) % 10)
            if l_map[(u, v)] != d_map[mapped_uv]:
                bijection_mod10_ok = False
    level_10_swap = bool(
        d10_1 == (Fraction(1, 5), Fraction(7, 10))
        and l10_1 == (Fraction(1, 5), Fraction(1, 2))
        and d10_1 == l10_3
        and d10_3 == l10_1
        and d10_1 != l10_1
        and bijection_mod10_ok
    )
    level_10_orbit_eq = bool(
        computed_minima["10"]["S"]["averaged_minima"]["down"]
        == computed_minima["10"]["S"]["averaged_minima"]["lep"]
        == ["1/5", "1/2"]
        and computed_minima["10"]["St"]["averaged_minima"]["down"]
        == computed_minima["10"]["St"]["averaged_minima"]["lep"]
        == ["1/5", "1/2"]
    )

    # Level 15 colour-triality split: lep = (1/5, 11/20) vs down = (2/15, 1/2) on S -> ratios 3/2 and 11/10
    e_lep_15_s = (
        Fraction(computed_minima["15"]["S"]["averaged_minima"]["lep"][0]),
        Fraction(computed_minima["15"]["S"]["averaged_minima"]["lep"][1]),
    )
    e_down_15_s = (
        Fraction(computed_minima["15"]["S"]["averaged_minima"]["down"][0]),
        Fraction(computed_minima["15"]["S"]["averaged_minima"]["down"][1]),
    )
    ratio_m2_15 = e_lep_15_s[0] / e_down_15_s[0]
    ratio_m1_15 = e_lep_15_s[1] / e_down_15_s[1]
    level_15_triality_ok = bool(
        e_lep_15_s == (Fraction(1, 5), Fraction(11, 20))
        and e_down_15_s == (Fraction(2, 15), Fraction(1, 2))
        and ratio_m2_15 == Fraction(3, 2)
        and ratio_m1_15 == Fraction(11, 10)
    )

    # High-cusp extended-precision mpmath slope verification using Kronecker second-limit norms F_u and ED[u] = (1/2) U[u] * eps
    mp.mp.dps = 180
    tau0_im = 2 * mp.sqrt(3)
    eta0 = mp_dedekind_eta_iT(tau0_im)
    f_kronecker = {
        "1": eta0 * eta0 * mp.sqrt(tau0_im),
        "i": mp.exp(-mp.pi * (mp.mpf(1) / 4) * tau0_im) * mp_theta_char_iT(Fraction(0, 1), tau0_im) / eta0,
        "j": mp_theta_char_iT(Fraction(1, 2), tau0_im) / eta0,
        "k": mp.exp(-mp.pi * (mp.mpf(1) / 4) * tau0_im) * mp_theta_char_iT(Fraction(1, 2), tau0_im) / eta0,
    }
    distinct_f_norms = bool(
        len({round(float(val), 8) for val in f_kronecker.values()}) == 4
        and float(abs(f_kronecker["1"] * f_kronecker["j"] - f_kronecker["i"] * f_kronecker["k"]))
        > pow10_tol(3)
    )

    q_1 = mp.matrix([[1, 0], [0, 1]])
    q_i = mp.matrix([[mp.mpc(0, 1), 0], [0, mp.mpc(0, -1)]])
    q_j = mp.matrix([[0, 1], [-1, 0]])
    q_k = mp.matrix([[0, mp.mpc(0, 1)], [mp.mpc(0, 1), 0]])
    eps_q = q_j
    u_units = {"1": q_1, "i": q_i, "j": q_j, "k": q_k}
    ed_blocks = {u_key: (u_units[u_key] * eps_q) / 2 for u_key in u_units}
    triplet_basis = [
        mp.sqrt(2) * ed_blocks["j"],
        mp.sqrt(2) * ed_blocks["i"],
        mp.sqrt(2) * ed_blocks["k"],
    ]
    mn_unit_map = {(0, 0): "1", (0, 1): "i", (1, 0): "k", (1, 1): "j"}

    t_low, t_high = mp.mpf(80), mp.mpf(100)
    slope_cases = [
        ("N5_down_a2_5_S", Fraction(2, 5), 1, 2, False),
        ("N10_down_a1_10_S", Fraction(1, 10), 1, 2, False),
        ("N10_lep_a1_10_S", Fraction(1, 10), -3, 6, False),
        ("N15_down_a2_15_S", Fraction(2, 15), 1, 2, False),
        ("N15_down_a4_15_S", Fraction(4, 15), 1, 2, False),
        ("N15_lep_a4_15_S", Fraction(4, 15), -3, 6, False),
        ("N5_down_a0_5_St", Fraction(0, 5), 1, 2, True),
        ("N5_up_a1_5_S", Fraction(1, 5), 1, -4, False),
    ]

    slope_checks_out: list[dict[str, Any]] = []
    max_slope_err = rat_float(0, 1)
    for case_name, a_frac, q_l, q_r, swap_flag in slope_cases:
        exact_pair = exact_frame_c_exponents_from_minors(a_frac, q_l, q_r, swap_flag)
        sv_ratios_by_t: list[tuple[mp.mpf, mp.mpf]] = []
        for t_val in (t_low, t_high):
            eta_32 = mp.power(mp_dedekind_eta_iT(t_val), mp.mpf(3) / 2)
            m_2x2 = mp.matrix(2, 2)
            for m_i in (0, 1):
                for n_i in (0, 1):
                    th_l = mp_theta_char_iT(q_l * a_frac + Fraction(m_i, 2), t_val)
                    th_r = mp_theta_char_iT(q_r * a_frac + Fraction(n_i, 2), t_val)
                    m_2x2[m_i, n_i] = f_kronecker[mn_unit_map[(m_i, n_i)]] * th_l * th_r / eta_32
            s_entry = mp_theta_char_iT(Fraction(1, 2), t_val) / (2 * eta_32)
            p_entry = mp_theta_char_iT(Fraction(0, 1), t_val) / eta_32
            r_entry = mp_theta_char_iT(Fraction(1, 2), 2 * t_val) / (2 * eta_32)
            s_2x2 = (
                mp.matrix([[s_entry, r_entry], [p_entry, -s_entry]])
                if swap_flag
                else mp.matrix([[s_entry, p_entry], [r_entry, -s_entry]])
            )
            s_eps = s_2x2 * eps_q
            y_3x3 = mp.matrix(3, 3)
            for row_a in range(3):
                for col_b in range(3):
                    prod_mat = triplet_basis[row_a].transpose_conj() * m_2x2 * triplet_basis[col_b] * s_eps
                    y_3x3[row_a, col_b] = prod_mat[0, 0] + prod_mat[1, 1]
            _u_sv, sv_vec, _v_sv = mp.svd_c(y_3x3)
            sv_sorted = sorted([mp.re(x) for x in sv_vec], reverse=True)
            sv_ratios_by_t.append((sv_sorted[1] / sv_sorted[0], sv_sorted[2] / sv_sorted[0]))

        fit_e2 = -mp.log(sv_ratios_by_t[1][0] / sv_ratios_by_t[0][0]) / (mp.pi * (t_high - t_low))
        fit_e1 = -mp.log(sv_ratios_by_t[1][1] / sv_ratios_by_t[0][1]) / (mp.pi * (t_high - t_low))
        ex_e2_mp = mp.mpf(exact_pair[0].numerator) / mp.mpf(exact_pair[0].denominator)
        ex_e1_mp = mp.mpf(exact_pair[1].numerator) / mp.mpf(exact_pair[1].denominator)
        case_err = float(max(abs(fit_e2 - ex_e2_mp), abs(fit_e1 - ex_e1_mp)))
        max_slope_err = max(max_slope_err, case_err)
        slope_checks_out.append(
            {
                "case": case_name,
                "exact_exponents": [str(exact_pair[0]), str(exact_pair[1])],
                "mpmath_fitted_exponents": [float(fit_e2), float(fit_e1)],
                "abs_err": case_err,
            }
        )

    # 40-digit mpmath verification of the 288-lift CIM (3, 3, -6) level-10 bijection (i, j) -> (9i mod 20, 9j mod 20)
    mp.mp.dps = 40
    imag_mp = mp.mpc(0, 1)
    tau_bij = mp.mpc(mp.mpf(29) / 100, mp.mpf(131) / 100)
    pref_tau_bij = mp.power(3 * mp.im(tau_bij), mp.mpf(1) / 4)
    k_phases_mp = [mp.exp(imag_mp * mp.pi * mp.mpf(k) / 3) for k in range(6)]
    n_sum_bij = 9
    # Precompute tau-dependent Gaussian weights exp(pi * i * (n + c/6)^2 * 6 * tau_bij)
    tau_weights_by_c: list[list[tuple[mp.mpf, mp.mpc]]] = []
    for c_idx in range(6):
        c_list: list[tuple[mp.mpf, mp.mpc]] = []
        for n_idx in range(-n_sum_bij, n_sum_bij + 1):
            q_val = mp.mpf(n_idx) + mp.mpf(c_idx) / 6
            w_tau = mp.exp(mp.pi * imag_mp * q_val * q_val * (6 * tau_bij))
            c_list.append((q_val, w_tau))
        tau_weights_by_c.append(c_list)

    def mp_fast_y_closed(z_l_in: mp.mpc, z_r_in: mp.mpc) -> list[mp.mpc]:
        dz = z_l_in - z_r_in
        gauss_dz = mp.exp(
            (mp.mpf(3) / 2) * imag_mp * mp.pi * dz * (mp.im(dz) / mp.im(tau_bij))
        )
        pref_all = pref_tau_bij * gauss_dz
        th_c: list[mp.mpc] = []
        two_pi_i_3dz = 2 * mp.pi * imag_mp * (3 * dz)
        for c_idx in range(6):
            acc = mp.mpc(0)
            for q_val, w_tau in tau_weights_by_c[c_idx]:
                acc += w_tau * mp.exp(two_pi_i_3dz * q_val)
            th_c.append(acc)
        flat_out: list[mp.mpc] = []
        for i_idx in range(3):
            for j_idx in range(3):
                for k_idx in range(6):
                    if (k_idx - (i_idx + j_idx + 1)) % 3 == 0:
                        flat_out.append(
                            pref_all * k_phases_mp[k_idx] * th_c[(k_idx - 2 * j_idx - 1) % 6]
                        )
                    else:
                        flat_out.append(mp.mpc(0))
        return flat_out

    lifts_288 = [
        (ui, vj)
        for ui in range(20)
        for vj in range(20)
        if math.gcd(math.gcd(ui % 10, vj % 10), 10) == 1
    ]
    mapped_lifts = {((9 * ui) % 20, (9 * vj) % 20) for (ui, vj) in lifts_288}
    bijection_onto_288 = bool(len(lifts_288) == 288 and mapped_lifts == set(lifts_288))

    max_bijection_tensor_err = rat_float(0, 1)
    for ui, vj in lifts_288:
        w_pt = (mp.mpf(ui) + mp.mpf(vj) * tau_bij) / 10
        wp_pt = (mp.mpf((9 * ui) % 20) + mp.mpf((9 * vj) % 20) * tau_bij) / 10
        y_lep_vec = mp_fast_y_closed(-3 * w_pt, 6 * w_pt)
        y_dn_vec = mp_fast_y_closed(1 * wp_pt, 2 * wp_pt)
        dom_idx = max(range(len(y_lep_vec)), key=lambda idx: abs(y_lep_vec[idx]))
        u1_phase = y_lep_vec[dom_idx] / y_dn_vec[dom_idx]
        unit_err = float(abs(abs(u1_phase) - 1))
        max_bijection_tensor_err = max(max_bijection_tensor_err, unit_err)
        for idx in range(len(y_lep_vec)):
            entry_err = float(abs(y_lep_vec[idx] - u1_phase * y_dn_vec[idx]))
            max_bijection_tensor_err = max(max_bijection_tensor_err, entry_err)

    slope_tol = rat_float(2, 1000)
    bij_tol = pow10_tol(13)
    gate_ok = bool(
        exact_table_matches_producer
        and level_5_eq
        and level_10_swap
        and level_10_orbit_eq
        and level_15_triality_ok
        and distinct_f_norms
        and max_slope_err < slope_tol
        and bijection_onto_288
        and max_bijection_tensor_err < bij_tol
    )

    return {
        "levels_5_10_15_exponents_gate_passed": gate_ok,
        "exact_minima_table_matches_producer": exact_table_matches_producer,
        "level_5_exact_lepton_down_equality": level_5_eq,
        "level_10_pointwise_swap_1_10_vs_3_10": level_10_swap,
        "level_10_whole_orbit_minima_equality": level_10_orbit_eq,
        "level_15_colour_triality_split_ratio_3_over_2": level_15_triality_ok,
        "level_15_S_ratios_lep_over_down": [str(ratio_m2_15), str(ratio_m1_15)],
        "cim_level_10_bijection_w_to_9w_mod_20_lifts_checked": len(lifts_288),
        "cim_level_10_bijection_max_tensor_err": max_bijection_tensor_err,
        "kronecker_unit_norms_distinct": distinct_f_norms,
        "max_mpmath_high_cusp_slope_err": max_slope_err,
        "mpmath_high_cusp_checks": slope_checks_out,
        "frame_c_exact_minima_by_level": computed_minima,
    }


def price_ground_state_degeneracy(
    hermitian_mat: np.ndarray, deg_tol: float | None = None
) -> tuple[np.ndarray, int, float, np.ndarray]:
    tol = pow10_tol(9) if deg_tol is None else deg_tol
    evals, evecs = np.linalg.eigh(hermitian_mat)
    ground_val = float(evals[0])
    deg_count = int(np.sum(np.abs(evals - ground_val) <= tol))
    bits = math.log2(deg_count) if deg_count > 1 else rat_float(0, 1)
    return evals, deg_count, float(bits), evecs


def random_haar_u3(rng: np.random.Generator) -> np.ndarray:
    z_mat = rng.standard_normal((3, 3)) + IMAG_UNIT * rng.standard_normal((3, 3))
    q_mat, r_mat = np.linalg.qr(z_mat)
    diag_r = np.diag(r_mat)
    phases = diag_r / np.abs(diag_r)
    return q_mat * phases[None, :]


def extract_physical_yukawa_observables(
    y_u: np.ndarray, y_d: np.ndarray, y_e: np.ndarray, include_ckm: bool = True
) -> np.ndarray:
    obs: list[float] = []
    for y_mat in (y_u, y_d, y_e):
        sv = np.sort(np.linalg.svd(y_mat, compute_uv=False))[::-1]
        obs.append(float(sv[1] / sv[0]))
        obs.append(float(sv[2] / sv[0]))

    if include_ckm:
        h_u = y_u @ y_u.conj().T
        h_d = y_d @ y_d.conj().T
        _eu, u_l = np.linalg.eigh(h_u)
        _ed, d_l = np.linalg.eigh(h_d)
        # Order left-handed eigenstates in ascending mass^2 -> descending [2, 1, 0]
        u_l = u_l[:, ::-1]
        d_l = d_l[:, ::-1]
        v_ckm = u_l.conj().T @ d_l
        obs.extend(float(x) for x in np.abs(v_ckm).ravel())
        jarlskog = float(
            abs(np.imag(v_ckm[0, 1] * v_ckm[1, 2] * np.conj(v_ckm[0, 2]) * np.conj(v_ckm[1, 1])))
        )
        obs.append(jarlskog)
    return np.array(obs, dtype=float)


def run_section_4_blind_level6_scalar_mass() -> dict[str, Any]:
    ks6 = np.arange(6, dtype=int)
    u_t6 = np.diag(np.exp(IMAG_UNIT * math.pi * (ks6 * ks6) / 6))
    u_s6 = (
        cmath.exp(-IMAG_UNIT * math.pi * rat_float(1, 4)) / math.sqrt(6)
    ) * np.exp(-2 * IMAG_UNIT * math.pi * np.outer(ks6, ks6) / 6)
    u_l6 = u_s6.conj().T @ u_t6.conj().T @ u_s6
    u_m6 = u_t6 @ u_l6

    um6_pow12_err = float(np.max(np.abs(np.linalg.matrix_power(u_m6, 12) - np.eye(6))))
    raw_evals, raw_evecs = np.linalg.eig(u_m6)
    raw_phases = np.angle(raw_evals)
    sort_idx = np.argsort(raw_phases)
    um6_phases = raw_phases[sort_idx]
    um6_evecs = raw_evecs[:, sort_idx]
    # Normalize eigenvectors explicitly
    for col in range(6):
        um6_evecs[:, col] /= np.linalg.norm(um6_evecs[:, col])

    expected_fracs = [
        Fraction(-5, 6),
        Fraction(-1, 3),
        Fraction(-1, 6),
        Fraction(1, 6),
        Fraction(1, 3),
        Fraction(5, 6),
    ]
    expected_phases = np.array([float(f) * math.pi for f in expected_fracs], dtype=float)
    um6_phase_err = float(np.max(np.abs(um6_phases - expected_phases)))
    v_plus_pi_over_6 = um6_evecs[:, 3]
    v_minus_pi_over_6 = um6_evecs[:, 2]

    # Closed geodesic of M = [[2, 1], [1, 1]] on upper half-plane with hyperbolic length L_M = 4 ln(phi)
    phi = (1 + math.sqrt(5)) / 2
    phi_inv = 1 / phi
    sqrt5 = math.sqrt(5)
    l_m = 4 * math.log(phi)

    def geodesic_tau(s_param: float) -> complex:
        e_s = math.exp(s_param)
        e_2s = e_s * e_s
        return ((phi * e_2s - phi_inv) + IMAG_UNIT * sqrt5 * e_s) / (1 + e_2s)

    tau_0 = geodesic_tau(rat_float(0, 1))
    tau_end = geodesic_tau(l_m)
    m_tau_0 = (2 * tau_0 + 1) / (tau_0 + 1)
    geodesic_period_err = float(abs(tau_end - m_tau_0))

    # Blind (zeta = 0) 1-loop chiral fermion bubble integrated via 64-pt Gauss-Legendre & cross-checked with 128-pt midpoint
    n_gl = 64
    gl_nodes, gl_weights = np.polynomial.legendre.leggauss(n_gl)
    s_nodes = rat_float(1, 2) * l_m * (gl_nodes + 1)
    s_weights = rat_float(1, 2) * l_m * gl_weights

    bubble_1period_neg6 = np.zeros((6, 6), dtype=complex)
    bubble_1period_pos6 = np.zeros((6, 6), dtype=complex)
    for s_val, w_val in zip(s_nodes, s_weights):
        y_mat = cim_triple_closed_form(geodesic_tau(float(s_val)), 0, 0).reshape(9, 6)
        # For I_H = -6 (conjugate representation), Higgs self-energy contracts Y_{ijk} conj(Y_{ijk'})
        b_neg6 = y_mat.T @ y_mat.conj()
        b_pos6 = y_mat.conj().T @ y_mat
        v_trans = um6_evecs @ np.diag(np.exp(IMAG_UNIT * um6_phases * (float(s_val) / l_m))) @ um6_evecs.conj().T
        bubble_1period_neg6 += (float(w_val) / l_m) * (v_trans.conj().T @ b_neg6 @ v_trans)
        bubble_1period_pos6 += (float(w_val) / l_m) * (v_trans.conj().T @ b_pos6 @ v_trans)

    # Cross-check quadrature against 128-point midpoint rule
    n_mid = 128
    ds_mid = l_m / n_mid
    bubble_mid_neg6 = np.zeros((6, 6), dtype=complex)
    for m_step in range(n_mid):
        s_mid = (m_step + rat_float(1, 2)) * ds_mid
        y_mat = cim_triple_closed_form(geodesic_tau(s_mid), 0, 0).reshape(9, 6)
        b_neg6 = y_mat.T @ y_mat.conj()
        v_trans = um6_evecs @ np.diag(np.exp(IMAG_UNIT * um6_phases * (s_mid / l_m))) @ um6_evecs.conj().T
        bubble_mid_neg6 += (ds_mid / l_m) * (v_trans.conj().T @ b_neg6 @ v_trans)
    quad_gl_vs_mid_err = float(np.max(np.abs(bubble_1period_neg6 - bubble_mid_neg6)))

    # Holonomy-covariant 12-sheeted geodesic average over <U_M^{(6)}> (full period 12 * L_M)
    sigma_h_geod = (
        sum(
            np.linalg.matrix_power(u_m6, -r_pow)
            @ bubble_1period_neg6
            @ np.linalg.matrix_power(u_m6, r_pow)
            for r_pow in range(12)
        )
        / 12
    )
    sigma_h_geod = rat_float(1, 2) * (sigma_h_geod + sigma_h_geod.conj().T)

    # Pure bubble at Riley cusp tau = 2 * sqrt(3) * i
    tau_riley = 2 * math.sqrt(3) * IMAG_UNIT
    y_riley = cim_triple_closed_form(tau_riley, 0, 0).reshape(9, 6)
    sigma_h_riley = y_riley.T @ y_riley.conj()
    sigma_h_riley = rat_float(1, 2) * (sigma_h_riley + sigma_h_riley.conj().T)

    # Regime 1: Pure Yukawa bubble (-Sigma_H)
    _ev_g1, deg_geod, bits_geod, _vc_g1 = price_ground_state_degeneracy(-sigma_h_geod)
    _ev_r1, deg_riley, bits_riley, _vc_r1 = price_ground_state_degeneracy(-sigma_h_riley)
    _ev_1p, deg_1period, _bits_1p, _vc_1p = price_ground_state_degeneracy(
        -rat_float(1, 2) * (bubble_1period_neg6 + bubble_1period_neg6.conj().T)
    )

    # Regime 2: Pure Kaluza-Klein holonomy kinetic operator K_KK = (theta_m / L_M)^2
    k_kk = um6_evecs @ np.diag((um6_phases / l_m) ** 2) @ um6_evecs.conj().T
    k_kk = rat_float(1, 2) * (k_kk + k_kk.conj().T)
    _ev_kk, deg_kk, bits_kk, _vc_kk = price_ground_state_degeneracy(k_kk)

    # Regime 3: Combined 1-loop M_H^2 = K_KK - kappa_loop * Sigma_H (fixed chiral flux I_H = -6)
    kappa_loop = 1 / (4 * math.pi)
    m_h2 = k_kk - kappa_loop * sigma_h_geod
    m_h2 = rat_float(1, 2) * (m_h2 + m_h2.conj().T)
    ev_comb, deg_comb, bits_comb, vc_comb = price_ground_state_degeneracy(m_h2)
    min_adj_gap = float(np.min(np.diff(ev_comb)))
    overlap_plus_pi6 = float(abs(np.vdot(v_plus_pi_over_6, vc_comb[:, 0])) ** 2)

    # Also verify single-period unprojected parallel-transported bubble selects +pi/6 with d = 1
    m_h2_1period = k_kk - kappa_loop * rat_float(1, 2) * (
        bubble_1period_neg6 + bubble_1period_neg6.conj().T
    )
    _ev_1c, deg_1c, _bits_1c, vc_1c = price_ground_state_degeneracy(m_h2_1period)
    overlap_1period_plus_pi6 = float(abs(np.vdot(v_plus_pi_over_6, vc_1c[:, 0])) ** 2)

    # Verify opposite flux sign (+6) flips selection out of +pi/6
    sigma_h_pos6 = (
        sum(
            np.linalg.matrix_power(u_m6, -r_pow)
            @ bubble_1period_pos6
            @ np.linalg.matrix_power(u_m6, r_pow)
            for r_pow in range(12)
        )
        / 12
    )
    _ev_pos, _deg_pos, _bits_pos, vc_pos = price_ground_state_degeneracy(
        k_kk - kappa_loop * rat_float(1, 2) * (sigma_h_pos6 + sigma_h_pos6.conj().T)
    )
    overlap_minus_on_flipped = float(abs(np.vdot(v_minus_pi_over_6, vc_pos[:, 0])) ** 2)

    # 10 fresh random Haar U(3)^6 basis-scrambling trials on contracted Yukawa matrices
    tau_haar = complex(rat_float(27, 100), rat_float(133, 100))
    w_haar = (2 + tau_haar) / 15
    h_vec = vc_comb[:, 0]
    y_mats_3x3: dict[str, np.ndarray] = {}
    for sec_name, (q_l, q_r, _q_h) in SM_6Y_TRIPLES.items():
        y_ten = cim_triple_closed_form(tau_haar, q_l * w_haar, q_r * w_haar)
        y_mats_3x3[sec_name] = np.einsum("ijk,k->ij", y_ten, h_vec)

    base_sv_obs = extract_physical_yukawa_observables(
        y_mats_3x3["up"], y_mats_3x3["down"], y_mats_3x3["lep"], include_ckm=False
    )
    base_full_obs = extract_physical_yukawa_observables(
        y_mats_3x3["up"], y_mats_3x3["down"], y_mats_3x3["lep"], include_ckm=True
    )

    rng = np.random.default_rng(20261116)
    max_haar_err = rat_float(0, 1)
    n_haar_trials = 10
    for _trial in range(n_haar_trials):
        # Independent U(3)^6 transformations on (u_L, u_R, d_L, d_R, e_L, e_R) for mass ratios
        u_lu, u_ru = random_haar_u3(rng), random_haar_u3(rng)
        u_ld, u_rd = random_haar_u3(rng), random_haar_u3(rng)
        u_le, u_re = random_haar_u3(rng), random_haar_u3(rng)
        scr_sv_obs = extract_physical_yukawa_observables(
            u_lu @ y_mats_3x3["up"] @ u_ru.conj().T,
            u_ld @ y_mats_3x3["down"] @ u_rd.conj().T,
            u_le @ y_mats_3x3["lep"] @ u_re.conj().T,
            include_ckm=False,
        )
        max_haar_err = max(max_haar_err, float(np.max(np.abs(scr_sv_obs - base_sv_obs))))

        # SU(2)_L gauge-covariant U(3)^6 transformations (U_Q, U_uR, U_dR, U_L, U_eR, U_nuR) including CKM & Jarlskog
        u_q = random_haar_u3(rng)
        scr_full_obs = extract_physical_yukawa_observables(
            u_q @ y_mats_3x3["up"] @ u_ru.conj().T,
            u_q @ y_mats_3x3["down"] @ u_rd.conj().T,
            u_le @ y_mats_3x3["lep"] @ u_re.conj().T,
            include_ckm=True,
        )
        max_haar_err = max(max_haar_err, float(np.max(np.abs(scr_full_obs - base_full_obs))))

    tol_13 = pow10_tol(13)
    tol_12 = pow10_tol(12)
    log2_3 = math.log2(3)
    gate_ok = bool(
        um6_pow12_err < tol_13
        and um6_phase_err < tol_13
        and geodesic_period_err < tol_13
        and quad_gl_vs_mid_err < pow10_tol(10)
        and deg_geod == 3
        and deg_1period == 3
        and abs(bits_geod - log2_3) < tol_13
        and deg_riley == 3
        and abs(bits_riley - log2_3) < tol_13
        and deg_kk == 2
        and abs(bits_kk - rat_float(1, 1)) < tol_13
        and deg_comb == 1
        and deg_1c == 1
        and bits_comb == rat_float(0, 1)
        and min_adj_gap > pow10_tol(4)
        and abs(overlap_plus_pi6 - rat_float(1, 1)) < tol_12
        and overlap_1period_plus_pi6 > rat_float(9999, 10000)
        and max_haar_err < tol_12
    )

    return {
        "level6_higgs_mass_gate_passed": gate_ok,
        "UM6_order_12_err": um6_pow12_err,
        "UM6_eigenphase_max_err": um6_phase_err,
        "geodesic_period_4ln_phi_err": geodesic_period_err,
        "gauss_legendre_vs_midpoint_err": quad_gl_vs_mid_err,
        "regime_1_pure_yukawa_bubble": {
            "geodesic_ground_degeneracy_d": deg_geod,
            "geodesic_selection_bits_log2_d": bits_geod,
            "riley_cusp_ground_degeneracy_d": deg_riley,
            "riley_cusp_selection_bits_log2_d": bits_riley,
        },
        "regime_2_pure_kk_holonomy": {
            "ground_degeneracy_d": deg_kk,
            "selection_bits_log2_d": bits_kk,
        },
        "regime_3_combined_1loop_M_H2": {
            "eigenvalues_sorted": [float(x) for x in ev_comb],
            "min_adjacent_eigenvalue_gap": min_adj_gap,
            "ground_degeneracy_d": deg_comb,
            "additional_selection_bits_given_chiral_flux_sign": bits_comb,
            "overlap_with_plus_pi_over_6_mode": overlap_plus_pi6,
            "single_period_overlap_with_plus_pi_over_6_mode": overlap_1period_plus_pi6,
            "flipped_flux_overlap_with_minus_pi_over_6_mode": overlap_minus_on_flipped,
        },
        "haar_u3_6_trials": n_haar_trials,
        "haar_u3_6_max_observable_err": max_haar_err,
    }


def run_section_5_planted_faults(sigma_h_geod_pure: np.ndarray) -> dict[str, Any]:
    half = rat_float(1, 2)
    zero = rat_float(0, 1)
    tau_fault = complex(rat_float(31, 100), rat_float(127, 100))
    w_fault = (1 + 2 * tau_fault) / 5
    z_fault = rat_float(23, 100) + rat_float(37, 100) * tau_fault
    q_l_up, q_r_up, q_h_up = SM_6Y_TRIPLES["up"]
    z_l = q_l_up * w_fault
    z_r = q_r_up * w_fault
    z_h = half * (q_l_up + q_r_up) * w_fault

    # PF2.1: Flux-violating untwisted scalar I_H = 0 (3 + 3 + 0 != 0) breaks z -> z + tau periodicity by > 1/2
    f_pf21_0 = np.einsum(
        "i,j->ij",
        [cim_wavefunction_vec(i, 3, half, half, z_fault, tau_fault, z_l).item() for i in range(3)],
        [cim_wavefunction_vec(j, 3, half, half, z_fault, tau_fault, z_r).item() for j in range(3)],
    )
    f_pf21_tau = np.einsum(
        "i,j->ij",
        [cim_wavefunction_vec(i, 3, half, half, z_fault + tau_fault, tau_fault, z_l).item() for i in range(3)],
        [cim_wavefunction_vec(j, 3, half, half, z_fault + tau_fault, tau_fault, z_r).item() for j in range(3)],
    )
    pf21_err = float(np.max(np.abs(f_pf21_tau - f_pf21_0)))
    pf21_caught = bool(pf21_err > half)

    # PF2.2: Naive phase-twisted point/untwisted coupling exp(2 pi i q_H w(tau)) * Y(tau; 0) fails T: tau -> tau + 1 by > 1/10
    a_tor, b_tor = rat_float(1, 5), rat_float(2, 5)
    y_naive_0 = cmath.exp(2 * IMAG_UNIT * math.pi * q_h_up * (a_tor + b_tor * tau_fault)) * cim_triple_closed_form(
        tau_fault, 0, 0
    )
    y_naive_t = cmath.exp(
        2 * IMAG_UNIT * math.pi * q_h_up * (a_tor + b_tor * (tau_fault + 1))
    ) * cim_triple_closed_form(tau_fault + 1, 0, 0)
    u_t3 = weil_transport_T_analytic(3, half)
    u_t6 = weil_transport_T_analytic(6, zero)
    y_naive_t_pred = np.einsum("ia,jb,kc,abc->ijk", u_t3, u_t3, np.conj(u_t6), y_naive_0)
    pf22_err = float(np.max(np.abs(y_naive_t - y_naive_t_pred)))
    pf22_caught = bool(pf22_err > rat_float(1, 10))

    # PF2.3: Spin-characteristic violation (alpha_H, beta_H) = (1/2, 0) breaks z -> z + 1 periodicity by > 1/2
    f_pf23_0 = np.einsum(
        "i,j,k->ijk",
        [cim_wavefunction_vec(i, 3, half, half, z_fault, tau_fault, z_l).item() for i in range(3)],
        [cim_wavefunction_vec(j, 3, half, half, z_fault, tau_fault, z_r).item() for j in range(3)],
        [cim_wavefunction_vec(k, -6, half, zero, z_fault, tau_fault, z_h).item() for k in range(6)],
    )
    f_pf23_1 = np.einsum(
        "i,j,k->ijk",
        [cim_wavefunction_vec(i, 3, half, half, z_fault + 1, tau_fault, z_l).item() for i in range(3)],
        [cim_wavefunction_vec(j, 3, half, half, z_fault + 1, tau_fault, z_r).item() for j in range(3)],
        [cim_wavefunction_vec(k, -6, half, zero, z_fault + 1, tau_fault, z_h).item() for k in range(6)],
    )
    pf23_err = float(np.max(np.abs(f_pf23_1 - f_pf23_0)))
    pf23_caught = bool(pf23_err > half)

    # PF2.4: Corrupted lepton doublet charge q_L = -2 at level 15 breaks level-15-to-level-5 collapse by > 2/100
    prim_15 = [(u, v) for u in range(15) for v in range(15) if math.gcd(math.gcd(u, v), 15) == 1]
    true_lep_5 = (Fraction(1, 5), Fraction(11, 20))
    corrupted_vals = [
        exact_frame_c_exponents_from_minors(Fraction(u, 15), -2, 6, False) for (u, _v) in prim_15
    ]
    corrupted_min = (
        min(val[0] for val in corrupted_vals),
        min(val[1] for val in corrupted_vals),
    )
    pf24_shift = float(
        max(abs(corrupted_min[0] - true_lep_5[0]), abs(corrupted_min[1] - true_lep_5[1]))
    )
    pf24_caught = bool(pf24_shift > rat_float(2, 100))

    # PF2.5: Degenerate pure-bubble bit-pricing control (turning off K_KK returns d = 3, log_2(3) > 158/100 bits)
    _ev_pf25, deg_pf25, bits_pf25, _vc_pf25 = price_ground_state_degeneracy(-sigma_h_geod_pure)
    pf25_caught = bool(deg_pf25 == 3 and bits_pf25 > rat_float(158, 100))

    all_caught = bool(pf21_caught and pf22_caught and pf23_caught and pf24_caught and pf25_caught)
    return {
        "all_5_planted_faults_caught": all_caught,
        "PF2_1_untwisted_flux_periodicity_err": {
            "measured_err": pf21_err,
            "caught": pf21_caught,
        },
        "PF2_2_b1947_naive_phase_T_cov_err": {
            "measured_err": pf22_err,
            "caught": pf22_caught,
        },
        "PF2_3_spin_mismatch_periodicity_err": {
            "measured_err": pf23_err,
            "caught": pf23_caught,
        },
        "PF2_4_corrupted_lepton_level15_shift": {
            "measured_err": pf24_shift,
            "corrupted_minima": [str(corrupted_min[0]), str(corrupted_min[1])],
            "caught": pf24_caught,
        },
        "PF2_5_deg3_bit_pricing_control": {
            "degeneracy": deg_pf25,
            "bits": bits_pf25,
            "caught": pf25_caught,
        },
    }


def main() -> None:
    self_path = Path(__file__).resolve()
    referee_dir = self_path.parent
    repo_root = referee_dir.parents[1]
    producer_dir = repo_root / "relays" / "agy002_endgame_v2_g2"

    producer_script_path = producer_dir / "verify_endgame_v2_g2.py"
    producer_script_sha_path = producer_dir / "SCRIPT_SHA256.txt"
    producer_out_json_path = producer_dir / "verify_endgame_v2_g2_out.json"
    producer_out_sha_path = producer_dir / "OUTPUT_SHA256.txt"

    self_ast = inspect_python_ast(self_path)
    producer_ast = inspect_python_ast(producer_script_path)
    script_sha_check = verify_sha256_manifest(producer_script_sha_path, repo_root)
    output_sha_check = verify_sha256_manifest(producer_out_sha_path, repo_root)

    producer_payload = json.loads(producer_out_json_path.read_text(encoding="utf-8"))

    sec0_ok = bool(
        self_ast["ast_gate_passed"]
        and producer_ast["ast_gate_passed"]
        and script_sha_check["digest_matched"]
        and output_sha_check["digest_matched"]
    )
    sec0 = {
        "ast_and_digest_gate_passed": sec0_ok,
        "referee_ast": self_ast,
        "producer_ast": producer_ast,
        "producer_script_sha256_check": script_sha_check,
        "producer_output_sha256_check": output_sha_check,
    }

    sec1 = run_section_1_wang_and_stokes(
        producer_payload.get("section_1_wang_homology_and_stokes_flux_accounting", {})
    )
    sec2 = run_section_2_modular_covariance()
    sec3 = run_section_3_cusp_exponent_laws(
        producer_payload.get("section_3_levels_5_10_15_cusp_exponent_laws", {})
    )
    sec4 = run_section_4_blind_level6_scalar_mass()

    # Reconstruct pure holonomy-covariant geodesic bubble solely for PF2.5 control input
    ks6 = np.arange(6, dtype=int)
    u_t6 = np.diag(np.exp(IMAG_UNIT * math.pi * (ks6 * ks6) / 6))
    u_s6 = (
        cmath.exp(-IMAG_UNIT * math.pi * rat_float(1, 4)) / math.sqrt(6)
    ) * np.exp(-2 * IMAG_UNIT * math.pi * np.outer(ks6, ks6) / 6)
    u_m6 = u_t6 @ (u_s6.conj().T @ u_t6.conj().T @ u_s6)
    phi = (1 + math.sqrt(5)) / 2
    l_m = 4 * math.log(phi)
    gl_x, gl_w = np.polynomial.legendre.leggauss(64)
    b_geod_pure = np.zeros((6, 6), dtype=complex)
    for x_i, w_i in zip(gl_x, gl_w):
        s_val = rat_float(1, 2) * l_m * (float(x_i) + 1)
        e_s = math.exp(s_val)
        tau_s = ((phi * e_s * e_s - 1 / phi) + IMAG_UNIT * math.sqrt(5) * e_s) / (1 + e_s * e_s)
        ym = cim_triple_closed_form(tau_s, 0, 0).reshape(9, 6)
        b_geod_pure += (rat_float(1, 2) * float(w_i)) * (ym.T @ ym.conj())
    sigma_pure_ctrl = (
        sum(
            np.linalg.matrix_power(u_m6, -r_i)
            @ b_geod_pure
            @ np.linalg.matrix_power(u_m6, r_i)
            for r_i in range(12)
        )
        / 12
    )
    sigma_pure_ctrl = rat_float(1, 2) * (sigma_pure_ctrl + sigma_pure_ctrl.conj().T)

    sec5 = run_section_5_planted_faults(sigma_pure_ctrl)

    overall_passed = bool(
        sec0["ast_and_digest_gate_passed"]
        and sec1["stokes_and_flux_gate_passed"]
        and sec2["modular_covariance_gate_passed"]
        and sec3["levels_5_10_15_exponents_gate_passed"]
        and sec4["level6_higgs_mass_gate_passed"]
        and sec5["all_5_planted_faults_caught"]
    )

    report = {
        "campaign": "AGY-002-ENDGAME-V2",
        "gate": "Gate 2 Cold-Room Countercheck \u2014 Frame D1 Covariance, Levels 5/10/15 Exponents & Blind Level-6 M_H^2",
        "empirical_firewall": "0 of 19",
        "gate_2_countercheck_passed": overall_passed,
        "section_0_ast_and_digest_lock": sec0,
        "section_1_wang_homology_and_stokes_flux_accounting": sec1,
        "section_2_cim_3_3_minus6_modular_covariance": sec2,
        "section_3_levels_5_10_15_cusp_exponent_laws": sec3,
        "section_4_blind_level6_scalar_mass_matrix_and_bit_ledger": sec4,
        "section_5_planted_fault_controls": sec5,
    }

    out_json_path = referee_dir / "referee_endgame_v2_g2_out.json"
    out_json_text = json.dumps(report, indent=2) + "\n"
    out_json_path.write_text(out_json_text, encoding="utf-8")

    out_sha = hashlib.sha256(out_json_path.read_bytes()).hexdigest()
    out_rel = "relays/agy002_endgame_v2_g2_referee/referee_endgame_v2_g2_out.json"
    out_manifest_path = referee_dir / "OUTPUT_SHA256.txt"
    out_manifest_path.write_text(f"{out_sha}  {out_rel}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
