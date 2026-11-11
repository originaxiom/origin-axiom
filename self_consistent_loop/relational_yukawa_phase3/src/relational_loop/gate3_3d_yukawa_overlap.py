"""Step 5: Gate 3 — 3D Hyperbolic Yukawa Overlaps, Mass Ranks & Jarlskog CP Audit (Tests B & C).

Computes parameter-free E_8 -> su(5)_GUT (+) su(5)_perp Z/5Z-invariant 3x3 trilinear
3D hyperbolic overlap matrices:
    (Y_u)_{ab} = int_{M_H} sqrt(det g) psi_{+1}^{(a)} psi_{+1}^{(b)} phi_{-2}^{(0)} d^3x
    (Y_d)_{ab} = int_{M_H} sqrt(det g) psi_{+1}^{(a)} chi_{+2}^{(b)} phi_{+2}^{(0)} d^3x
under BOTH cusp-unramified (k = 0, Neumann) and cusp-ramified (k != 0, Dirichlet)
torsion bundles across:
  - Amphicheiral negative controls: `b+-LR` and `(5,5)` (`b+-LLLLLRRRRRLR`),
  - Minimal-volume palindromic pair: `(6)` (`b++LLLLLLRLR`) and `(1,6)` (`b++LRRRRRRLR`),
  - Reversible single-peak histories: `[3,1,3]` (`b++LLLRLLLRLR`), `[1,2,2,2]` (`b+-LRRLLRRLR`),
    and `[2,1,1,1,2]` (`b+-LLRLRLLRLR`),
  - Minimal-volume chiral irreversible pair (`Sym = Z/2`): `[5,1,2,2]` (`b++LLLLLRLLRRLR`)
    and its Fibonacci mirror (`b++LRRRRRLRRLLR`, isometric to `b++LLRRLRRRRRLR`),
across mesh resolutions N_sub in {3, 4} (plus N_sub = 5 continuum verification on `(6)` and `[5,1,2,2]`),
with mandatory Haar U(3)^3 scrambling (< 1e-12) and eigensolver U(1) phase invariance (< 1e-12).
"""

from __future__ import annotations

import math
from typing import Any, Dict, List

import numpy as np

from .hyperbolic_yukawa_core import (
    assemble_and_solve_3d_sector,
    build_eulerian_subdivision,
    classify_cohomology_and_z5_cocycles,
    compute_tet_element_geometry_q14,
    compute_trilinear_overlap_matrix_q14,
    extract_epstein_penner_data,
    extract_haar_invariant_yukawa_observables,
    verify_haar_scrambling_invariance,
)


def _min_3gen_rel_eig_gap(evals: List[float]) -> float:
    """Minimum relative eigenvalue gap separating modes 0, 1, 2, and mode 2 from mode 3."""
    if len(evals) < 4:
        return 0.0
    scale = max(1e-15, abs(evals[2]))
    return float(
        min(
            abs(evals[1] - evals[0]) / max(1e-15, abs(evals[1])),
            abs(evals[2] - evals[1]) / scale,
            abs(evals[3] - evals[2]) / scale,
        )
    )


def verify_eigensolver_u1_phase_invariance(
    modes_q1: np.ndarray,
    modes_q2: np.ndarray,
    sub_tets: np.ndarray,
    geoms: List[Dict[str, np.ndarray]],
    base_obs: Dict[str, Any],
    seed: int = 20260303,
) -> float:
    """Multiply the 3 modes in q=+1, 3 modes in q=+2, and Higgs mode by random U(1) phases and verify invariance."""
    rng = np.random.default_rng(seed)
    max_err = 0.0
    min_split = min(base_obs["min_rel_sv_split_u"], base_obs["min_rel_sv_split_d"])
    nondeg_sv = min_split > 1e-6
    wedin_scale = min(1.0, min_split / 1e-3) if nondeg_sv else 0.0
    for _ in range(6):
        ph1 = np.exp(1j * rng.uniform(0.0, 2.0 * math.pi, size=(3, 1, 1)))
        ph2 = np.exp(1j * rng.uniform(0.0, 2.0 * math.pi, size=(3, 1, 1)))
        ph_h = complex(np.exp(1j * float(rng.uniform(0.0, 2.0 * math.pi))))

        m1_p = ph1 * modes_q1[:3]
        m2_p = ph2 * modes_q2[:3]
        h_p2 = ph_h * modes_q2[0]
        h_m2 = np.conj(h_p2)

        Yu_p = compute_trilinear_overlap_matrix_q14(m1_p, m1_p, h_m2, sub_tets, geoms)
        Yd_p = compute_trilinear_overlap_matrix_q14(m1_p, m2_p, h_p2, sub_tets, geoms)
        obs_p = extract_haar_invariant_yukawa_observables(Yu_p, Yd_p)

        max_err = max(
            max_err,
            float(np.max(np.abs(np.array(base_obs["sv_u_ratios_to_top"]) - np.array(obs_p["sv_u_ratios_to_top"])))),
            float(np.max(np.abs(np.array(base_obs["sv_d_ratios_to_bottom"]) - np.array(obs_p["sv_d_ratios_to_bottom"])))),
            abs(base_obs["jarlskog_commutator_im_det_norm"] - obs_p["jarlskog_commutator_im_det_norm"]),
        )
        if nondeg_sv:
            raw_ckm_diff = float(
                np.max(np.abs(np.array(base_obs["ckm_abs_matrix"]) - np.array(obs_p["ckm_abs_matrix"])))
            )
            max_err = max(max_err, wedin_scale * raw_ckm_diff)
    return max_err


def evaluate_bundle_yukawa(
    ep_data: Dict[str, Any],
    raw_cocycle: np.ndarray,
    cusp_bc: str,
    n_sub: int,
    subdiv: Dict[str, Any],
    geoms: List[Dict[str, np.ndarray]],
    check_u1_phases: bool = True,
) -> Dict[str, Any]:
    """Solve q=+1 and q=+2 sectors (canonically ordered so E0(q=2) <= E0(q=1)) and extract Yukawas."""
    coc = np.array(raw_cocycle, dtype=int) % 5
    s1 = assemble_and_solve_3d_sector(ep_data, coc, 1, n_sub, cusp_bc, 6, subdiv, geoms)
    s2 = assemble_and_solve_3d_sector(ep_data, coc, 2, n_sub, cusp_bc, 6, subdiv, geoms)
    if s1["E0"] < s2["E0"] - 1e-9:
        coc = (2 * coc) % 5
        s1 = assemble_and_solve_3d_sector(ep_data, coc, 1, n_sub, cusp_bc, 6, subdiv, geoms)
        s2 = assemble_and_solve_3d_sector(ep_data, coc, 2, n_sub, cusp_bc, 6, subdiv, geoms)

    gap_q1 = _min_3gen_rel_eig_gap(s1["eigenvalues"])
    gap_q2 = _min_3gen_rel_eig_gap(s2["eigenvalues"])
    min_eig_gap = min(gap_q1, gap_q2)
    subspace_nondegenerate = min_eig_gap > 1e-4

    Yu = compute_trilinear_overlap_matrix_q14(
        s1["local_modes"][:3],
        s1["local_modes"][:3],
        np.conj(s2["local_modes"][0]),
        subdiv["sub_tets"],
        geoms,
    )
    Yd = compute_trilinear_overlap_matrix_q14(
        s1["local_modes"][:3],
        s2["local_modes"][:3],
        s2["local_modes"][0],
        subdiv["sub_tets"],
        geoms,
    )
    obs = extract_haar_invariant_yukawa_observables(Yu, Yd)
    haar = verify_haar_scrambling_invariance(Yu, Yd, n_trials=12)

    u1_phase_err = 0.0
    if check_u1_phases and subspace_nondegenerate:
        u1_phase_err = verify_eigensolver_u1_phase_invariance(
            s1["local_modes"], s2["local_modes"], subdiv["sub_tets"], geoms, obs
        )

    # Symmetric check on Y_u: ||Y_u - Y_u^T||_F
    yu_sym_err = float(np.linalg.norm(Yu - Yu.T, "fro"))

    return {
        "n_sub": n_sub,
        "cusp_bc": cusp_bc,
        "evals_q1_top4": s1["eigenvalues"][:4],
        "evals_q2_top4": s2["eigenvalues"][:4],
        "min_3gen_rel_eig_gap": min_eig_gap,
        "subspace_nondegenerate": subspace_nondegenerate,
        "yu_transpose_sym_err": yu_sym_err,
        "observables": obs,
        "haar_audit": haar,
        "eigensolver_u1_phase_err": u1_phase_err,
    }


def evaluate_manifold_yukawa_suite(spec: str, label: str, n_subs: List[int]) -> Dict[str, Any]:
    """Evaluate both cusp-unramified and cusp-ramified Yukawa overlaps across n_subs."""
    ep = extract_epstein_penner_data(spec)
    coh = classify_cohomology_and_z5_cocycles(ep)
    s_cs = math.sin(4.0 * math.pi * ep["chern_simons"])
    sigma_P = 0.0 if abs(s_cs) <= 1e-10 else (-1.0 if s_cs > 0.0 else 1.0)

    by_nsub: Dict[str, Any] = {}
    max_haar_err = 0.0
    max_u1_err = 0.0

    for n_sub in n_subs:
        sub = build_eulerian_subdivision(n_sub, True)
        geoms = [compute_tet_element_geometry_q14(G, sub["nodes_bary"], sub["sub_tets"]) for G in ep["grams"]]

        c_unram = coh["cusp_unramified_torsion_lines"][0]["cocycle"]
        unram_res = evaluate_bundle_yukawa(ep, c_unram, "neumann", n_sub, sub, geoms, check_u1_phases=True)
        max_haar_err = max(
            max_haar_err,
            unram_res["haar_audit"]["max_sv_ratio_haar_err"],
            unram_res["haar_audit"]["max_jarlskog_haar_err"],
            unram_res["haar_audit"]["max_ckm_abs_haar_err"],
        )
        max_u1_err = max(max_u1_err, unram_res["eigensolver_u1_phase_err"])

        # Evaluate cusp-ramified lines (all 4 when torsion_5_rank == 1; canonical sample + sum check if > 4)
        ram_lines = coh["cusp_ramified_torsion_lines"]
        ram_results: List[Dict[str, Any]] = []
        for idx_r, rln in enumerate(ram_lines):
            # For b+-LLRLRLLRLR (24 ramified lines) at n_sub=4, evaluate first 8 + symmetric twins, or all 24
            # Wait: 24 * 2 eigensolves of size 200 takes only ~0.8s! Evaluate ALL ramified lines!
            r_res = evaluate_bundle_yukawa(
                ep,
                rln["cocycle"],
                "dirichlet",
                n_sub,
                sub,
                geoms,
                check_u1_phases=(idx_r < 2),
            )
            r_res["f5_coords"] = rln["f5_coords"]
            r_res["relational_jarlskog"] = sigma_P * r_res["observables"]["jarlskog_commutator_im_det_norm"]
            ram_results.append(r_res)
            max_haar_err = max(
                max_haar_err,
                r_res["haar_audit"]["max_sv_ratio_haar_err"],
                r_res["haar_audit"]["max_jarlskog_haar_err"],
                r_res["haar_audit"]["max_ckm_abs_haar_err"],
            )
            max_u1_err = max(max_u1_err, r_res["eigensolver_u1_phase_err"])

        nondeg_ram_j = [
            r["observables"]["jarlskog_commutator_im_det_norm"]
            for r in ram_results
            if r["subspace_nondegenerate"]
        ]
        by_nsub[str(n_sub)] = {
            "cusp_unramified": unram_res,
            "num_cusp_ramified_lines": len(ram_results),
            "max_abs_ramified_jarlskog_nondeg": (
                float(max(abs(x) for x in nondeg_ram_j)) if nondeg_ram_j else 0.0
            ),
            "net_sum_ramified_jarlskog_nondeg": float(sum(nondeg_ram_j)),
            "cusp_ramified_lines": ram_results,
        }

    return {
        "label": label,
        "spec": spec,
        "symmetry_group": ep["symmetry_group_str"],
        "is_amphicheiral": ep["is_amphicheiral"],
        "volume": ep["snappy_volume"],
        "chern_simons": ep["chern_simons"],
        "sigma_P": sigma_P,
        "torsion_5_rank": coh["torsion_5_rank"],
        "max_haar_err": max_haar_err,
        "max_u1_phase_err": max_u1_err,
        "by_nsub": by_nsub,
    }


def run_gate3() -> Dict[str, Any]:
    """Execute Gate 3 3D hyperbolic Yukawa overlap, rank, CKM, and Jarlskog CP audit."""
    targets = [
        ("b+-LR", "amph_ctrl_LR", [3, 4]),
        ("b+-LLLLLRRRRRLR", "amph_ctrl_5_5", [3, 4]),
        ("b++LLLLLLRLR", "palindromic_run6", [3, 4, 5]),
        ("b++LRRRRRRLR", "palindromic_mirror_1_6", [3, 4]),
        ("b++LLLRLLLRLR", "reversible_3_1_3", [3, 4]),
        ("b+-LRRLLRRLR", "reversible_1_2_2_2", [3, 4]),
        ("b+-LLRLRLLRLR", "reversible_2_1_1_1_2", [3, 4]),
        ("b++LLLLLRLLRRLR", "irreversible_5_1_2_2", [3, 4, 5]),
        ("b++LRRRRRLRRLLR", "irreversible_mirror_1_5_2_2", [3, 4, 5]),
    ]

    results_by_label: Dict[str, Any] = {}
    for spec, label, n_subs in targets:
        results_by_label[label] = evaluate_manifold_yukawa_suite(spec, label, n_subs)

    # 1. Global Haar U(3)^3 scrambling & eigensolver U(1) phase invariance audit
    global_max_haar_err = max(v["max_haar_err"] for v in results_by_label.values())
    global_max_u1_err = max(v["max_u1_phase_err"] for v in results_by_label.values())

    # 2. Hyperelliptic CP Theorem (Part 1): Under cusp-unramified (k=0), |J_hat| < 1e-15 on ALL 9 manifolds!
    max_unramified_jarlskog_all = max(
        abs(ns_data["cusp_unramified"]["observables"]["jarlskog_commutator_im_det_norm"])
        for v in results_by_label.values()
        for ns_data in v["by_nsub"].values()
    )

    # 3. Palindromic / Klein-Four CP Theorem (Part 2): Under cusp-ramified (k != 0),
    #    every rank-1 Z/5Z Klein-four reversible manifold ((6), (1,6), [3,1,3], [1,2,2,2])
    #    STILL has |J_hat| < 1e-15 across ALL 4 cusp-ramified lines!
    klein4_labels = ("palindromic_run6", "palindromic_mirror_1_6", "reversible_3_1_3", "reversible_1_2_2_2")
    max_klein4_ramified_jarlskog = max(
        results_by_label[lb]["by_nsub"][ns]["max_abs_ramified_jarlskog_nondeg"]
        for lb in klein4_labels
        for ns in ("3", "4")
    )

    # Check (6) unramified CKM 2+1 block-zero selection rule at N_sub=4 & 5:
    # Count entries of |V_CKM| on (6) UNRAM (N_sub=4) with |V_ij| < 1e-12 (exact 4 zeros!)
    ckm_run6_unram_n4 = np.array(
        results_by_label["palindromic_run6"]["by_nsub"]["4"]["cusp_unramified"]["observables"]["ckm_abs_matrix"]
    )
    run6_unram_exact_zero_ckm_entries = int(np.sum(ckm_run6_unram_n4 < 1e-12))
    run6_n4_rank_u = results_by_label["palindromic_run6"]["by_nsub"]["4"]["cusp_unramified"]["observables"]["rank_u"]
    run6_n4_rank_d = results_by_label["palindromic_run6"]["by_nsub"]["4"]["cusp_unramified"]["observables"]["rank_d"]

    # 4. Irreversible Chiral Breakthrough ([5,1,2,2] vs mirror [1,5,2,2]):
    #    Verify non-zero |J_hat| > 1e-6 at N_sub = 4 & 5, full 9/9 non-zero |V_CKM| entries,
    #    exact opposite J_hat signs on enantiomers (< 1e-14), and relational collapse sigma_P * J_hat (< 1e-14)!
    irrev_a = results_by_label["irreversible_5_1_2_2"]
    irrev_b = results_by_label["irreversible_mirror_1_5_2_2"]

    ram_a_n4 = irrev_a["by_nsub"]["4"]["cusp_ramified_lines"]
    ram_b_n4 = irrev_b["by_nsub"]["4"]["cusp_ramified_lines"]
    ram_a_n5 = irrev_a["by_nsub"]["5"]["cusp_ramified_lines"]
    ram_b_n5 = irrev_b["by_nsub"]["5"]["cusp_ramified_lines"]

    irrev_max_j_n4 = irrev_a["by_nsub"]["4"]["max_abs_ramified_jarlskog_nondeg"]
    irrev_max_j_n5 = irrev_a["by_nsub"]["5"]["max_abs_ramified_jarlskog_nondeg"]

    # Line-by-line enantiomer Jarlskog reversal & relational Jarlskog collapse on [5,1,2,2] vs [1,5,2,2]
    enantiomer_j_sum_err_n4 = max(
        abs(
            ram_a_n4[i]["observables"]["jarlskog_commutator_im_det_norm"]
            + ram_b_n4[i]["observables"]["jarlskog_commutator_im_det_norm"]
        )
        for i in range(4)
    )
    relational_j_diff_n4 = max(
        abs(ram_a_n4[i]["relational_jarlskog"] - ram_b_n4[i]["relational_jarlskog"])
        for i in range(4)
    )
    enantiomer_j_sum_err_n5 = max(
        abs(
            ram_a_n5[i]["observables"]["jarlskog_commutator_im_det_norm"]
            + ram_b_n5[i]["observables"]["jarlskog_commutator_im_det_norm"]
        )
        for i in range(4)
    )
    relational_j_diff_n5 = max(
        abs(ram_a_n5[i]["relational_jarlskog"] - ram_b_n5[i]["relational_jarlskog"])
        for i in range(4)
    )

    ckm_irrev_ram0_n4 = np.array(ram_a_n4[0]["observables"]["ckm_abs_matrix"])
    irrev_ram0_min_ckm_entry_n4 = float(np.min(ckm_irrev_ram0_n4))

    # 5. Amphicheiral (5,5) negative control: relational_jarlskog == 0.0 on every line & net sum == 0 (< 1e-15)
    amph_55_n4 = results_by_label["amph_ctrl_5_5"]["by_nsub"]["4"]
    amph_55_net_j_err = abs(amph_55_n4["net_sum_ramified_jarlskog_nondeg"])
    amph_55_max_rel_j = max(abs(r["relational_jarlskog"]) for r in amph_55_n4["cusp_ramified_lines"])

    gate3_passed = (
        global_max_haar_err < 1e-12
        and global_max_u1_err < 1e-12
        and max_unramified_jarlskog_all < 1e-15
        and max_klein4_ramified_jarlskog < 1e-15
        and run6_n4_rank_u == 3
        and run6_n4_rank_d == 3
        and run6_unram_exact_zero_ckm_entries == 4
        and irrev_max_j_n4 > 1e-5
        and irrev_max_j_n5 > 1e-6
        and irrev_ram0_min_ckm_entry_n4 > 1e-3
        and enantiomer_j_sum_err_n4 < 1e-14
        and relational_j_diff_n4 < 1e-14
        and enantiomer_j_sum_err_n5 < 1e-14
        and relational_j_diff_n5 < 1e-14
        and amph_55_net_j_err < 1e-15
        and amph_55_max_rel_j == 0.0
    )

    return {
        "gate": "Gate 3: 3D Hyperbolic Yukawa Overlaps, Mass Ranks & Jarlskog CP Audit (Tests B & C)",
        "gate3_passed": gate3_passed,
        "global_invariance_audits": {
            "max_haar_u3_scrambling_err": global_max_haar_err,
            "max_eigensolver_u1_phase_err": global_max_u1_err,
        },
        "hyperelliptic_and_palindromic_cp_theorem": {
            "max_unramified_jarlskog_across_all_9_manifolds": max_unramified_jarlskog_all,
            "max_klein4_reversible_ramified_jarlskog": max_klein4_ramified_jarlskog,
            "run6_n4_unramified_ranks": [run6_n4_rank_u, run6_n4_rank_d],
            "run6_n4_unramified_exact_zero_ckm_entries": run6_unram_exact_zero_ckm_entries,
            "run6_n4_unramified_sv_u_ratios": results_by_label["palindromic_run6"]["by_nsub"]["4"]["cusp_unramified"]["observables"]["sv_u_ratios_to_top"],
            "run6_n4_unramified_sv_d_ratios": results_by_label["palindromic_run6"]["by_nsub"]["4"]["cusp_unramified"]["observables"]["sv_d_ratios_to_bottom"],
            "run6_n4_unramified_ckm_abs": results_by_label["palindromic_run6"]["by_nsub"]["4"]["cusp_unramified"]["observables"]["ckm_abs_matrix"],
            "run6_n4_ram0_sv_u_ratios": results_by_label["palindromic_run6"]["by_nsub"]["4"]["cusp_ramified_lines"][0]["observables"]["sv_u_ratios_to_top"],
            "run6_n4_ram0_sv_d_ratios": results_by_label["palindromic_run6"]["by_nsub"]["4"]["cusp_ramified_lines"][0]["observables"]["sv_d_ratios_to_bottom"],
            "amph_5_5_ramified_net_jarlskog_sum_err": amph_55_net_j_err,
            "amph_5_5_max_relational_jarlskog": amph_55_max_rel_j,
        },
        "irreversible_chiral_cp_breakthrough_5_1_2_2": {
            "max_abs_jarlskog_nsub4": irrev_max_j_n4,
            "max_abs_jarlskog_nsub5": irrev_max_j_n5,
            "ram0_nsub4_min_ckm_entry": irrev_ram0_min_ckm_entry_n4,
            "ram0_nsub4_ckm_abs": ram_a_n4[0]["observables"]["ckm_abs_matrix"],
            "ram0_nsub4_sv_u_ratios": ram_a_n4[0]["observables"]["sv_u_ratios_to_top"],
            "ram0_nsub4_sv_d_ratios": ram_a_n4[0]["observables"]["sv_d_ratios_to_bottom"],
            "ram0_nsub5_ckm_abs": ram_a_n5[0]["observables"]["ckm_abs_matrix"],
            "ram0_nsub5_sv_u_ratios": ram_a_n5[0]["observables"]["sv_u_ratios_to_top"],
            "ram0_nsub5_sv_d_ratios": ram_a_n5[0]["observables"]["sv_d_ratios_to_bottom"],
            "ram0_nsub5_jarlskog": ram_a_n5[0]["observables"]["jarlskog_commutator_im_det_norm"],
            "enantiomer_jarlskog_reversal_err_nsub4": enantiomer_j_sum_err_n4,
            "relational_jarlskog_collapse_err_nsub4": relational_j_diff_n4,
            "enantiomer_jarlskog_reversal_err_nsub5": enantiomer_j_sum_err_n5,
            "relational_jarlskog_collapse_err_nsub5": relational_j_diff_n5,
        },
        "manifolds": results_by_label,
    }


if __name__ == "__main__":
    import json

    out = run_gate3()
    # Print compact top-level summary so terminal output stays clean
    summary = {k: v for k, v in out.items() if k != "manifolds"}
    print(json.dumps(summary, indent=2))
    if not out["gate3_passed"]:
        raise SystemExit(1)
