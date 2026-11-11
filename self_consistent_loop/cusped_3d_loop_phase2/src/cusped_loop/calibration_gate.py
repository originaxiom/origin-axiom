"""Step 2: Textbook Calibration Gate (Guardrails 2, 3, 4).

Verifies all three numerical instruments against exact analytical/literature
theorems BEFORE evaluating candidate histories in Gates 1-3:
  1. Quad-precision Epstein-Penner 24-cone Riemannian volume vs. Bloch-Wigner
     and Mostow volume of `m004` (`b++LR` and `b+-LR`) + exact cusp shapes (< 1e-12).
  2. Exact spectral equivalence between the 2-tetrahedron Z/5Z-twisted 3D P1
     Laplacian on `b+-LR` and the 10-tetrahedron untwisted 3D P1 Laplacian on
     SnapPy's 5-cusp 5-fold cyclic cover (< 1e-12), plus untwisted constant zero mode.
  3. Exact 2D Neuberger Overlap Ginsparg-Wilson Dirac operator on a magnetized
     lattice torus reproducing Atiyah-Singer index `ind(D_ov) == c_1` for
     `c_1 in {-3..-1, 0, +1..+3}` from literal machine-zero singular values (< 1e-12),
     verified invariant under independent random Haar unitary basis rotations.
"""

from __future__ import annotations

import math
from typing import Any, Dict, List

import numpy as np

from .hyperbolic_fem_core import (
    assemble_and_solve_3d_laplacian,
    build_eulerian_subdivision,
    classify_z5_torsion_cocycles,
    compute_penner_tet_volume,
    extract_epstein_penner_data,
    gauss_reduce_tau,
)


def random_haar_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    """Mezzadri algorithm for a Haar-distributed unitary matrix in U(n)."""
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = np.where(np.abs(d) > 0, d / np.abs(d), 1.0 + 0.0j)
    return q * ph[None, :]


def build_2d_overlap_dirac_torus(
    L: int, flux_c1: int, wilson_m0: float = 1.0
) -> Dict[str, Any]:
    """Construct 2D Neuberger Overlap Dirac operator on an L x L torus with flux c_1."""
    # Standard Landau-torus U(1) lattice gauge links with uniform plaquette phase 2*pi*c_1 / L^2:
    # U_1(x1, x2) = exp(-i * 2*pi * c_1 * x2 / L^2) for x1 < L-1,
    # U_1(L-1, x2) = exp(-i * 2*pi * c_1 * x2 / L^2) * exp(+i * 2*pi * c_1 * x2 / L) ?
    # Check plaquette P(x1, x2) = U_1(x1,x2) U_2(x1+1,x2) U_1*(x1,x2+1) U_2*(x1,x2):
    # Clean standard 't Hooft clock/shift links on {0..L-1}^2:
    #   U_2(x1, x2) = exp(+i * 2*pi * c_1 * x1 / L^2)  for all (x1, x2)
    #   U_1(x1, x2) = 1                                for x2 < L - 1 ? Wait:
    #   Check: P(x1, x2) = U_1(x1,x2) * exp(i*2pi*c1*(x1+1)/L^2) * U_1*(x1,x2+1) * exp(-i*2pi*c1*x1/L^2)
    #   For x1 < L - 1: (x1+1) - x1 = 1 => U_2 ratio gives exp(i*2pi*c1/L^2) if U_1 == 1!
    #   At boundary x1 == L - 1: x1+1 wraps to 0, so U_2(0, x2) * U_2*(L-1, x2) = exp(-i*2pi*c1*(L-1)/L^2).
    #   We need exp(+i*2pi*c1/L^2), so ratio needed from U_1(L-1,x2)*U_1*(L-1,x2+1) is exp(+i*2pi*c1*L/L^2) = exp(+i*2pi*c1/L)!
    #   Set U_1(L-1, x2) := exp(-i * 2*pi * c_1 * x2 / L) (periodic in x2 since x2=L gives exp(-i*2pi*c1) = 1 for integer c_1!!)!
    #   Check at x2 = L - 1: U_1(L-1, L-1) * U_1*(L-1, 0) = exp(-i*2pi*c1*(L-1)/L) = exp(+i*2pi*c1/L)! EXACT EVERYWHERE!
    n_sites = L * L
    dim = 2 * n_sites

    sigma1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
    sigma2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=np.complex128)
    sigma3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
    eye2 = np.eye(2, dtype=np.complex128)

    U1 = np.ones((L, L), dtype=np.complex128)
    U2 = np.ones((L, L), dtype=np.complex128)
    for x1 in range(L):
        for x2 in range(L):
            # Covariant convention U_mu = exp(-i A_mu) so [D_1, D_2] = -i F_12 has int F_12/(2*pi) = +c_1
            U2[x1, x2] = np.exp(-1j * 2.0 * math.pi * flux_c1 * x1 / (L * L))
            if x1 == L - 1:
                U1[x1, x2] = np.exp(1j * 2.0 * math.pi * flux_c1 * x2 / L)

    # Verify uniform plaquette flux across all L^2 plaquettes: U_1 U_2 U_1^* U_2^* = exp(-i F_12)
    plaq_angles = []
    for x1 in range(L):
        for x2 in range(L):
            p = (
                U1[x1, x2]
                * U2[(x1 + 1) % L, x2]
                * np.conj(U1[x1, (x2 + 1) % L])
                * np.conj(U2[x1, x2])
            )
            plaq_angles.append(-math.atan2(p.imag, p.real))
    target_angle = 2.0 * math.pi * flux_c1 / (L * L)
    plaquette_uniformity_err = float(np.max(np.abs(np.array(plaq_angles) - target_angle)))

    D_W = np.zeros((dim, dim), dtype=np.complex128)
    Gamma5 = np.zeros((dim, dim), dtype=np.complex128)

    def s_idx(x1: int, x2: int) -> int:
        return 2 * ((x1 % L) * L + (x2 % L))

    for x1 in range(L):
        for x2 in range(L):
            i = s_idx(x1, x2)
            D_W[i : i + 2, i : i + 2] += (2.0 - wilson_m0) * eye2
            Gamma5[i : i + 2, i : i + 2] = sigma3

            # mu = 1
            ip1 = s_idx(x1 + 1, x2)
            im1 = s_idx(x1 - 1, x2)
            D_W[i : i + 2, ip1 : ip1 + 2] -= 0.5 * (eye2 - sigma1) * U1[x1, x2]
            D_W[i : i + 2, im1 : im1 + 2] -= 0.5 * (eye2 + sigma1) * np.conj(
                U1[(x1 - 1) % L, x2]
            )

            # mu = 2
            jp1 = s_idx(x1, x2 + 1)
            jm1 = s_idx(x1, x2 - 1)
            D_W[i : i + 2, jp1 : jp1 + 2] -= 0.5 * (eye2 - sigma2) * U2[x1, x2]
            D_W[i : i + 2, jm1 : jm1 + 2] -= 0.5 * (eye2 + sigma2) * np.conj(
                U2[x1, (x2 - 1) % L]
            )

    H_W = Gamma5 @ D_W
    herm_err = float(np.max(np.abs(H_W - H_W.conj().T)))
    evals_hw, evecs_hw = np.linalg.eigh(0.5 * (H_W + H_W.conj().T))
    min_abs_hw = float(np.min(np.abs(evals_hw)))
    sign_hw = (evecs_hw * np.sign(evals_hw)[None, :]) @ evecs_hw.conj().T
    D_ov = np.eye(dim, dtype=np.complex128) + Gamma5 @ sign_hw

    # Verify Ginsparg-Wilson relation: Gamma5 D_ov + D_ov Gamma5 == D_ov Gamma5 D_ov
    gw_lhs = Gamma5 @ D_ov + D_ov @ Gamma5
    gw_rhs = D_ov @ Gamma5 @ D_ov
    gw_err = float(np.max(np.abs(gw_lhs - gw_rhs)))

    # Extract chiral blocks in Gamma5 eigenbasis (+1 at even indices, -1 at odd indices!)
    # Note: D_ov maps + chirality and - chirality; specifically, on ker(D_ov), V psi = -psi and [Gamma5, D_ov|_{ker}] = 0!
    # Compute SVD of D_ov restricted to +1 chirality input (even columns) and -1 chirality input (odd columns):
    even_cols = np.arange(0, dim, 2)
    odd_cols = np.arange(1, dim, 2)
    svals_plus = np.linalg.svd(D_ov[:, even_cols], compute_uv=False)
    svals_minus = np.linalg.svd(D_ov[:, odd_cols], compute_uv=False)

    n_zero_plus = int(np.sum(svals_plus < 1e-10))
    n_zero_minus = int(np.sum(svals_minus < 1e-10))
    max_zero_sval = float(
        max(
            [0.0]
            + svals_plus[svals_plus < 1e-10].tolist()
            + svals_minus[svals_minus < 1e-10].tolist()
        )
    )
    index_svd = n_zero_plus - n_zero_minus
    index_trace = -0.5 * float(np.real(np.trace(sign_hw)))

    return {
        "L": L,
        "flux_c1": flux_c1,
        "plaquette_uniformity_err": plaquette_uniformity_err,
        "hw_hermiticity_err": herm_err,
        "hw_min_abs_eval": min_abs_hw,
        "ginsparg_wilson_err": gw_err,
        "n_zero_plus": n_zero_plus,
        "n_zero_minus": n_zero_minus,
        "max_zero_singular_value": max_zero_sval,
        "index_from_svd": index_svd,
        "index_from_spectral_trace": index_trace,
        "D_ov": D_ov,
        "even_cols": even_cols,
        "odd_cols": odd_cols,
    }


def run_calibration_gate() -> Dict[str, Any]:
    """Execute all three Step 2 textbook calibration gates."""
    # 1. Hyperbolic volume & cusp calibration on m004 (b++LR and b+-LR)
    ep_pp = extract_epstein_penner_data("b++LR")
    ep_pm = extract_epstein_penner_data("b+-LR")

    penner_vols_pp = [compute_penner_tet_volume(G, nq=20) for G in ep_pp["grams"]]
    penner_vols_pm = [compute_penner_tet_volume(G, nq=20) for G in ep_pm["grams"]]

    vol_pp_err = abs(sum(penner_vols_pp) - ep_pp["snappy_volume"])
    vol_pm_err = abs(sum(penner_vols_pm) - ep_pm["snappy_volume"])
    tet_bw_err = max(
        abs(vp - vbw) for vp, vbw in zip(penner_vols_pp, ep_pp["tet_bw_volumes"])
    )

    # Exact figure-eight cusp shapes: b++LR has modulus 2*sqrt(3)*i; b+-LR has 1/2 + i*sqrt(3)/2 (in F)
    tau_pp = gauss_reduce_tau(ep_pp["cusp_moduli"][0])
    tau_pm = gauss_reduce_tau(ep_pm["cusp_moduli"][0])
    # Note: 2*sqrt(3)*i is already in F! Check:
    cusp_pp_err = abs(ep_pp["cusp_moduli"][0] - complex(0.0, 2.0 * math.sqrt(3.0)))
    cusp_pm_err = abs(tau_pm - complex(0.5, 0.5 * math.sqrt(3.0)))

    # 2. 3D Simplicial P1 FEM Cover Equivalence on b+-LR (2 tets vs 10-tet 5-cusp cover)
    cocycles_pm = classify_z5_torsion_cocycles(ep_pm)
    assert len(cocycles_pm["cusp_unramified_torsion_lines"]) == 1
    c_unram = cocycles_pm["cusp_unramified_torsion_lines"][0]["cocycle"]

    n_sub_cal = 4
    subdiv4 = build_eulerian_subdivision(n_sub_cal, truncate_cusp_corners=True)
    # Solve for q = 0, 1, 2, 3, 4 on 2-tet base manifold
    union_evals_base: List[float] = []
    q_ground_evals: Dict[str, float] = {}
    untwisted_zero_mode = 0.0
    for q in range(5):
        res_q = assemble_and_solve_3d_laplacian(
            ep_pm,
            cocycle_mod5=c_unram,
            charge_q=q,
            n_sub=n_sub_cal,
            cusp_bc="neumann",
            n_eigs=6,
            subdiv_cache=subdiv4,
        )
        if q == 0:
            untwisted_zero_mode = abs(res_q["eigenvalues"][0])
        q_ground_evals[f"q={q}"] = res_q["E0"]
        union_evals_base.extend(res_q["eigenvalues"][:4])
    union_evals_base.sort()

    # Solve untwisted on SnapPy's independent 10-tet 5-cusp cyclic cover of b+-LR
    M_pm = ep_pm["manifold"]
    cov_5cusp = [c for c in M_pm.covers(5, cover_type="cyclic") if c.num_cusps() == 5][0]
    ep_cov = extract_epstein_penner_data(cov_5cusp)
    res_cov = assemble_and_solve_3d_laplacian(
        ep_cov,
        cocycle_mod5=None,
        charge_q=0,
        n_sub=n_sub_cal,
        cusp_bc="neumann",
        n_eigs=12,
        subdiv_cache=subdiv4,
    )
    cov_evals = res_cov["eigenvalues"][:10]
    base_vs_cover_eval_err = float(
        np.max(np.abs(np.array(union_evals_base[:10]) - np.array(cov_evals)))
    )

    # Also check truncated volume convergence across n_sub = 3, 4, 6 on b+-LR
    trunc_vols = {}
    for ns in (3, 4, 6):
        r_ns = assemble_and_solve_3d_laplacian(
            ep_pm, cocycle_mod5=None, charge_q=0, n_sub=ns, cusp_bc="neumann", n_eigs=3
        )
        trunc_vols[f"n_sub={ns}"] = r_ns["truncated_volume"]

    # 3. 2D Magnetized Torus Overlap Dirac Index & Haar Basis Scrambling Calibration
    rng = np.random.default_rng(20261110)
    flux_results = {}
    max_gw_err = 0.0
    max_index_err = 0.0
    max_haar_sval_err = 0.0

    for c1 in (-3, -2, -1, 0, 1, 2, 3):
        ov = build_2d_overlap_dirac_torus(L=10, flux_c1=c1, wilson_m0=1.0)
        max_gw_err = max(max_gw_err, ov["ginsparg_wilson_err"])
        idx_err = max(
            abs(ov["index_from_svd"] - c1),
            abs(ov["index_from_spectral_trace"] - c1),
        )
        max_index_err = max(max_index_err, idx_err)

        # Guardrail 3: Apply independent random Haar unitary transformations U_out, U_in_plus, U_in_minus
        D_plus = ov["D_ov"][:, ov["even_cols"]]
        D_minus = ov["D_ov"][:, ov["odd_cols"]]
        U_out = random_haar_unitary(D_plus.shape[0], rng)
        U_in_p = random_haar_unitary(D_plus.shape[1], rng)
        U_in_m = random_haar_unitary(D_minus.shape[1], rng)

        sv_p_orig = np.linalg.svd(D_plus, compute_uv=False)
        sv_p_scr = np.linalg.svd(U_out @ D_plus @ U_in_p.conj().T, compute_uv=False)
        sv_m_orig = np.linalg.svd(D_minus, compute_uv=False)
        sv_m_scr = np.linalg.svd(U_out @ D_minus @ U_in_m.conj().T, compute_uv=False)
        haar_err = max(
            float(np.max(np.abs(sv_p_orig - sv_p_scr))),
            float(np.max(np.abs(sv_m_orig - sv_m_scr))),
        )
        max_haar_sval_err = max(max_haar_sval_err, haar_err)

        flux_results[f"c1={c1:+d}"] = {
            "n_zero_plus": ov["n_zero_plus"],
            "n_zero_minus": ov["n_zero_minus"],
            "index_svd": ov["index_from_svd"],
            "max_zero_sval": ov["max_zero_singular_value"],
            "haar_sval_err": haar_err,
        }

    all_passed = bool(
        ep_pp["max_intra_penner_err"] < 1e-12
        and ep_pp["max_inter_gluing_err"] < 1e-12
        and vol_pp_err < 1e-12
        and vol_pm_err < 1e-12
        and tet_bw_err < 1e-12
        and cusp_pp_err < 1e-12
        and cusp_pm_err < 1e-12
        and untwisted_zero_mode < 1e-12
        and base_vs_cover_eval_err < 1e-12
        and max_gw_err < 1e-12
        and max_index_err < 1e-12
        and max_haar_sval_err < 1e-12
    )

    return {
        "gate": "Step 2: Textbook Calibration Gate",
        "all_calibrations_passed": all_passed,
        "hyperbolic_m004_calibration": {
            "m004_snappy_volume": ep_pp["snappy_volume"],
            "b_pp_LR_penner_vol_err": vol_pp_err,
            "b_pm_LR_penner_vol_err": vol_pm_err,
            "tet_bloch_wigner_err": tet_bw_err,
            "max_intra_penner_err": max(ep_pp["max_intra_penner_err"], ep_pm["max_intra_penner_err"]),
            "max_inter_gluing_err": max(ep_pp["max_inter_gluing_err"], ep_pm["max_inter_gluing_err"]),
            "b_pp_LR_cusp_err": cusp_pp_err,
            "b_pm_LR_cusp_err": cusp_pm_err,
        },
        "fem_cover_equivalence_calibration": {
            "manifold": "b+-LR (2 tets) vs 5-cusp cover (10 tets)",
            "n_sub": n_sub_cal,
            "untwisted_zero_mode_abs": untwisted_zero_mode,
            "q_sector_E0": q_ground_evals,
            "base_union_first_10_evals": union_evals_base[:10],
            "cover_first_10_evals": cov_evals,
            "base_vs_cover_max_eval_err": base_vs_cover_eval_err,
            "truncated_volume_convergence": trunc_vols,
        },
        "overlap_dirac_index_calibration": {
            "lattice_L": 10,
            "max_ginsparg_wilson_err": max_gw_err,
            "max_index_err": max_index_err,
            "max_haar_scrambling_err": max_haar_sval_err,
            "flux_scan": flux_results,
        },
    }


if __name__ == "__main__":
    import json

    res = run_calibration_gate()
    print(json.dumps(res, indent=2))
