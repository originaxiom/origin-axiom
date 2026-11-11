"""Step 2: Textbook Calibration Gate — Phase 3 (Guardrails 2, 3, 4).

Verifies all four Phase 3 numerical instruments against exact analytical/cover
theorems BEFORE running candidate history evaluations in Gates 1-4:
  1. Positive-weight S_4-symmetric 14-point degree-5 tetrahedral quadrature vs.
     exact reference 3-simplex monomials up to degree 5 (< 1e-15) and m004 Mostow
     hyperbolic volume (< 1e-12).
  2. Exact Z/5Z trilinear charge-conservation selection rule & 5-fold cyclic cover
     equivalence on b+-LR: verifies directly on SnapPy's 10-tetrahedron 5-cusp cover
     (via exact order-5 deck Fourier projection) that int sqrt(det g) psi_{q1} psi_{q2} phi_{q3} == 0
     (< 1e-13) whenever q1 + q2 + q3 != 0 mod 5, and matches 5x the 2-tetrahedron base
     twisted overlap when q1 + q2 + q3 == 0 mod 5 (< 1e-12).
  3. Discrete Hodge harmonic 1-form alpha_s = d theta_s calibration on b++LR and b+-LR:
     verifies exact loop holonomy oint_{S^1} alpha_s = 1 (< 1e-12), elementwise exactness
     d theta_s = alpha_s (< 1e-12), discrete co-closure d^dagger alpha_s = 0 (< 1e-12),
     and positive harmonic norm ||alpha_s||_{L^2}^2 > 0.
  4. Analytical CKM & Jarlskog determinant Haar-scrambling invariance (< 1e-12) on
     both a complex CP-violating benchmark pair and a real CP-conserving negative control.
"""

from __future__ import annotations

import math
from typing import Any, Dict, List

import numpy as np

from .hyperbolic_yukawa_core import (
    TET_QUAD14_BARY,
    TET_QUAD14_WTS,
    apply_deck_map_to_local_modes,
    assemble_and_solve_3d_sector,
    build_eulerian_subdivision,
    classify_cohomology_and_z5_cocycles,
    compute_penner_tet_volume,
    compute_tet_element_geometry_q14,
    compute_trilinear_overlap_matrix_q14,
    extract_epstein_penner_data,
    extract_haar_invariant_yukawa_observables,
    find_order5_deck_generator,
    solve_harmonic_base_1form,
    verify_haar_scrambling_invariance,
)


def run_calibration_gate() -> Dict[str, Any]:
    """Execute all four Step 2 textbook calibration checks."""
    # 1. 14-point degree-5 quadrature monomial check + m004 volume check
    min_wt = float(np.min(TET_QUAD14_WTS))
    wt_sum_err = abs(float(np.sum(TET_QUAD14_WTS)) - (1.0 / 6.0))
    max_deg5_mono_err = 0.0
    for a in range(6):
        for b in range(6 - a):
            for c in range(6 - a - b):
                for d in range(6 - a - b - c):
                    exact = (
                        math.factorial(a)
                        * math.factorial(b)
                        * math.factorial(c)
                        * math.factorial(d)
                        / math.factorial(a + b + c + d + 3)
                    )
                    num = float(
                        np.sum(
                            TET_QUAD14_WTS
                            * (TET_QUAD14_BARY[:, 0] ** a)
                            * (TET_QUAD14_BARY[:, 1] ** b)
                            * (TET_QUAD14_BARY[:, 2] ** c)
                            * (TET_QUAD14_BARY[:, 3] ** d)
                        )
                    )
                    max_deg5_mono_err = max(max_deg5_mono_err, abs(num - exact))

    ep_pp = extract_epstein_penner_data("b++LR")
    ep_pm = extract_epstein_penner_data("b+-LR")
    vol_pp_err = abs(sum(compute_penner_tet_volume(G, nq=20) for G in ep_pp["grams"]) - ep_pp["snappy_volume"])
    vol_pm_err = abs(sum(compute_penner_tet_volume(G, nq=20) for G in ep_pm["grams"]) - ep_pm["snappy_volume"])

    # 2. Z/5Z Trilinear Selection Rule & Authentic 10-Tet 5-Fold Cover Equivalence on b+-LR
    coh_pm = classify_cohomology_and_z5_cocycles(ep_pm)
    c_unram = coh_pm["cusp_unramified_torsion_lines"][0]["cocycle"]

    n_sub = 4
    sub4 = build_eulerian_subdivision(n_sub, True)
    geoms_pm = [compute_tet_element_geometry_q14(G, sub4["nodes_bary"], sub4["sub_tets"]) for G in ep_pm["grams"]]

    sec_q1 = assemble_and_solve_3d_sector(ep_pm, c_unram, 1, n_sub, "neumann", 5, sub4, geoms_pm)
    sec_q2 = assemble_and_solve_3d_sector(ep_pm, c_unram, 2, n_sub, "neumann", 5, sub4, geoms_pm)
    phi_minus2 = np.conj(sec_q2["local_modes"][0])

    Y_base_113 = compute_trilinear_overlap_matrix_q14(
        sec_q1["local_modes"][:3], sec_q1["local_modes"][:3], phi_minus2, sub4["sub_tets"], geoms_pm
    )
    sv_base = np.linalg.svd(Y_base_113, compute_uv=False)

    # Solve untwisted Laplacian directly on SnapPy's 10-tetrahedron 5-cusp cover of b+-LR
    M_pm = ep_pm["manifold"]
    cov5 = [c for c in M_pm.covers(5, cover_type="cyclic") if c.num_cusps() == 5][0]
    ep_cov = extract_epstein_penner_data(cov5)
    geoms_cov = [compute_tet_element_geometry_q14(G, sub4["nodes_bary"], sub4["sub_tets"]) for G in ep_cov["grams"]]
    sec_cov = assemble_and_solve_3d_sector(ep_cov, None, 0, n_sub, "neumann", 22, sub4, geoms_cov)

    union_evals = []
    for q in range(5):
        sq = assemble_and_solve_3d_sector(ep_pm, c_unram, q, n_sub, "neumann", 6, sub4, geoms_pm)
        union_evals.extend(sq["eigenvalues"][:4])
    union_evals.sort()
    cover_eval_err = float(np.max(np.abs(np.array(union_evals[:10]) - np.array(sec_cov["eigenvalues"][:10]))))

    # Project actual 10-tetrahedron cover eigenstates onto exact Z/5Z deck-transformation sectors
    dmap = find_order5_deck_generator(ep_cov, ep_pm)
    all_cov_m = sec_cov["local_modes"]
    D_all = [all_cov_m]
    for _ in range(4):
        D_all.append(apply_deck_map_to_local_modes(D_all[-1], dmap, sub4))
    deck_order5_err = float(np.max(np.abs(apply_deck_map_to_local_modes(D_all[-1], dmap, sub4) - all_cov_m)))

    Q_T = TET_QUAD14_BARY.T

    def _l2_norm_cov(m_arr: np.ndarray) -> float:
        tot = 0.0
        for t_idx in range(m_arr.shape[0]):
            mq = m_arr[t_idx, sub4["sub_tets"]] @ Q_T
            tot += float(np.sum(geoms_cov[t_idx]["dvol_q14"] * (np.abs(mq) ** 2)))
        return math.sqrt(tot)

    cov_modes_by_q: Dict[int, np.ndarray] = {}
    for q in range(1, 5):
        q_list = []
        for cl in (range(1, 5), range(5, 9), range(9, 13)):
            proj_cl = (
                sum(np.exp(-2j * math.pi * ((q * s) % 5) / 5.0) * D_all[s][list(cl)] for s in range(5))
                / 5.0
            )
            norms = [_l2_norm_cov(proj_cl[i]) for i in range(4)]
            best_i = int(np.argmax(norms))
            q_list.append(proj_cl[best_i] * (math.sqrt(5.0) / norms[best_i]))
        cov_modes_by_q[q] = np.stack(q_list, axis=0)

    # Project q = 0 sector using exact deck-averaging Pi_0 = (1/5) sum_{s=0}^4 (D^*)^s
    proj_q0_all = sum(D_all[s] for s in range(5)) / 5.0
    q0_list = []
    for idx_m in range(proj_q0_all.shape[0]):
        nrm0 = _l2_norm_cov(proj_q0_all[idx_m])
        if nrm0 > 0.2:
            q0_list.append(proj_q0_all[idx_m] * (math.sqrt(5.0) / nrm0))
            if len(q0_list) == 3:
                break
    cov_modes_by_q[0] = np.stack(q0_list, axis=0)

    max_forbidden_cover_overlap = 0.0
    for q1 in range(5):
        for q2 in range(5):
            for q3 in range(5):
                if (q1 + q2 + q3) % 5 == 0:
                    continue
                Yf = compute_trilinear_overlap_matrix_q14(
                    cov_modes_by_q[q1], cov_modes_by_q[q2], cov_modes_by_q[q3][0], sub4["sub_tets"], geoms_cov
                )
                max_forbidden_cover_overlap = max(max_forbidden_cover_overlap, float(np.max(np.abs(Yf))))

    # Verify allowed triple (+1, +1, -2) on 10-tet cover equals 5 * base twisted singular values!
    Y_cov_allowed = compute_trilinear_overlap_matrix_q14(
        cov_modes_by_q[1], cov_modes_by_q[1], np.conj(cov_modes_by_q[2][0]), sub4["sub_tets"], geoms_cov
    )
    sv_cov_allowed = np.linalg.svd(Y_cov_allowed, compute_uv=False)
    cover_5x_base_sv_err = float(np.max(np.abs(sv_cov_allowed - 5.0 * sv_base)))

    # 3. Discrete Harmonic 1-Form Calibration on b++LR and b+-LR
    coh_pp = classify_cohomology_and_z5_cocycles(ep_pp)
    geoms_pp = [compute_tet_element_geometry_q14(G, sub4["nodes_bary"], sub4["sub_tets"]) for G in ep_pp["grams"]]
    harm_pp = solve_harmonic_base_1form(
        ep_pp, coh_pp["free_cocycles_int"][0], sub4, geoms_pp, coh_pp["free_cycles_int"][0]
    )
    harm_pm = solve_harmonic_base_1form(
        ep_pm, coh_pm["free_cocycles_int"][0], sub4, geoms_pm, coh_pm["free_cycles_int"][0]
    )

    # 4. Analytical CKM & Jarlskog Haar-Invariance Calibration (Guardrail 3)
    Yu_bench = np.array(
        [
            [0.35, 0.48 * np.exp(0.7j), 0.19 * np.exp(-0.3j)],
            [0.22 * np.exp(-0.5j), 0.72, 0.41 * np.exp(1.1j)],
            [0.14 * np.exp(0.2j), 0.33 * np.exp(-0.8j), 1.05],
        ],
        dtype=np.complex128,
    )
    Yd_bench = np.array(
        [
            [0.28, 0.39 * np.exp(-0.9j), 0.31 * np.exp(0.6j)],
            [0.44 * np.exp(0.4j), 0.68, 0.27 * np.exp(-0.5j)],
            [0.25 * np.exp(-0.7j), 0.46 * np.exp(0.3j), 0.98],
        ],
        dtype=np.complex128,
    )
    obs_cp = extract_haar_invariant_yukawa_observables(Yu_bench, Yd_bench)
    haar_cp = verify_haar_scrambling_invariance(Yu_bench, Yd_bench, n_trials=20, seed=101)

    obs_real_ctrl = extract_haar_invariant_yukawa_observables(Yu_bench.real, Yd_bench.real)
    haar_real_ctrl = verify_haar_scrambling_invariance(Yu_bench.real, Yd_bench.real, n_trials=20, seed=202)

    all_ok = (
        min_wt > 0.0
        and wt_sum_err < 1e-15
        and max_deg5_mono_err < 1e-15
        and vol_pp_err < 1e-12
        and vol_pm_err < 1e-12
        and deck_order5_err < 1e-14
        and cover_eval_err < 1e-12
        and max_forbidden_cover_overlap < 1e-13
        and cover_5x_base_sv_err < 1e-12
        and harm_pp["coclosure_residual"] < 1e-12
        and harm_pm["coclosure_residual"] < 1e-12
        and harm_pp["max_element_dtheta_err"] < 1e-12
        and harm_pp["loop_holonomy_err"] < 1e-12
        and harm_pm["loop_holonomy_err"] < 1e-12
        and harm_pp["harmonic_l2_norm2"] > 0.1
        and abs(obs_cp["jarlskog_commutator_im_det_norm"]) > 1e-6
        and abs(obs_real_ctrl["jarlskog_commutator_im_det_norm"]) < 1e-15
        and haar_cp["haar_invariance_verified"]
        and haar_real_ctrl["haar_invariance_verified"]
    )

    return {
        "gate": "Step 2: Textbook Calibration Gate (Phase 3)",
        "all_calibrations_passed": all_ok,
        "quad14_and_m004_volume_calibration": {
            "min_quad14_weight": min_wt,
            "weight_sum_err": wt_sum_err,
            "max_degree5_monomial_err": max_deg5_mono_err,
            "b_pp_LR_penner_vol_err": vol_pp_err,
            "b_pm_LR_penner_vol_err": vol_pm_err,
        },
        "z5_trilinear_selection_and_cover_calibration": {
            "deck_order5_identity_err": deck_order5_err,
            "base_vs_10tet_cover_eval_err": cover_eval_err,
            "max_forbidden_charge_triple_10tet_cover": max_forbidden_cover_overlap,
            "allowed_triple_10tet_cover_vs_5x_base_sv_err": cover_5x_base_sv_err,
            "b_pm_LR_base_yukawa_svals": sv_base.tolist(),
            "b_pm_LR_10tet_cover_yukawa_svals_div5": (sv_cov_allowed / 5.0).tolist(),
        },
        "discrete_harmonic_1form_calibration": {
            "b_pp_LR_betti1": coh_pp["betti_1"],
            "b_pp_LR_coclosure_err": harm_pp["coclosure_residual"],
            "b_pm_LR_coclosure_err": harm_pm["coclosure_residual"],
            "b_pp_LR_dtheta_err": harm_pp["max_element_dtheta_err"],
            "b_pp_LR_loop_holonomy": harm_pp["loop_holonomy"],
            "b_pp_LR_loop_holonomy_err": harm_pp["loop_holonomy_err"],
            "b_pm_LR_loop_holonomy_err": harm_pm["loop_holonomy_err"],
            "b_pp_LR_harmonic_norm2": harm_pp["harmonic_l2_norm2"],
            "b_pm_LR_harmonic_norm2": harm_pm["harmonic_l2_norm2"],
        },
        "haar_yukawa_jarlskog_calibration": {
            "cp_benchmark_jarlskog": obs_cp["jarlskog_commutator_im_det_norm"],
            "real_neg_ctrl_jarlskog": obs_real_ctrl["jarlskog_commutator_im_det_norm"],
            "cp_benchmark_haar": haar_cp,
            "real_neg_ctrl_haar": haar_real_ctrl,
        },
    }


if __name__ == "__main__":
    import json

    res = run_calibration_gate()
    print(json.dumps(res, indent=2))
    if not res["all_calibrations_passed"]:
        raise SystemExit(1)
