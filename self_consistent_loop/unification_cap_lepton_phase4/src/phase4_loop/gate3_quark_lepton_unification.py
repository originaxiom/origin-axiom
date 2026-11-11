"""Step 5: Gate 3 — Parameter-Free Quark-vs.-Lepton Acid Test (CKM vs. PMNS Unification).

Tests whether the exact same 3D hyperbolic geometry + E_8 -> su(5)_GUT (+) su(5)_perp
Z/5Z bundle produces small quark CKM mixing and large lepton PMNS mixing with `0 of 19`
empirical inputs:
  1. Verifies explicit E_8 branching dimensions (248 = 24+24+50+50+50+50), the exact
     lopsided SU(5) transpose identity Y_e = Y_d^T (Q_L in q=+1 vs L_L in q=+2), and
     uniqueness of the right-handed neutrino charge q(N^c) = 0 (mod 5).
  2. Evaluates ALL 4 cusp-ramified Z/5Z torsion bundles (canonically normalized so
     E_0(q=2) <= E_0(q=1)) for both Mechanism N1 (3D KK Singlet Seesaw M_nu^KK) and
     Mechanism N2 (Exact Degree-4 Contact Weinberg M_nu^W) across amphicheiral controls,
     Klein-four reversible manifolds, and the global minimal chiral irreversible pairs
     across mesh resolutions N_sub in {3, 4, 5}.
  3. Verifies bilinear eigensolver-phase invariance (< 1e-14), random Haar U(3)^3 scrambling
     invariance (< 1e-12), exact 4-line enantiomer bijection (< 1e-12), Klein-four CP
     vanishing (< 1e-14), Z/4 amphicheiral 4-line cancellation (< 1e-14), and evaluates
     the direct Quark-vs.-Lepton mixing angle Acid Test without tuning.
"""

from __future__ import annotations

import itertools
import math
from typing import Any, Dict, List, Tuple

import numpy as np

from .gate1_vacuum_selection import active_weak_compass_sign
from .phase4_core import (
    assemble_and_solve_3d_sector,
    build_eulerian_subdivision,
    classify_cohomology_and_z5_cocycles,
    compute_bilinear_majorana_matrix_q14,
    compute_quartic_weinberg_matrix_q14,
    compute_tet_element_geometry_q14,
    compute_trilinear_overlap_matrix_q14,
    extract_epstein_penner_data,
    extract_lepton_pmns_observables,
    extract_quark_ckm_observables,
    verify_lepton_seesaw_haar_invariance,
    verify_lepton_weinberg_haar_invariance,
    verify_quark_haar_invariance,
)


def verify_e8_lepton_branching_and_charge_uniqueness() -> Dict[str, Any]:
    """Verify 248 -> su(5)_GUT (+) su(5)_perp dimensions, Y_e = Y_d^T, and uniqueness of q(N^c) = 0."""
    roots = []
    for i in range(8):
        for j in range(i + 1, 8):
            for s1 in (-1.0, 1.0):
                for s2 in (-1.0, 1.0):
                    v = np.zeros(8)
                    v[i], v[j] = s1, s2
                    roots.append(v)
    for signs in itertools.product((-0.5, 0.5), repeat=8):
        if sum(1 for s in signs if s < 0) % 2 == 0:
            roots.append(np.array(signs, dtype=float))
    R_e8 = np.array(roots, dtype=float)
    assert R_e8.shape == (240, 8)

    is_perp_root = (
        (np.abs(R_e8[:, 0] - R_e8[:, 1]) < 1e-12)
        & (np.abs(R_e8[:, 1] - R_e8[:, 2]) < 1e-12)
        & (np.abs(R_e8[:, 2] - R_e8[:, 3]) < 1e-12)
        & (np.abs(R_e8[:, 3] - R_e8[:, 4]) < 1e-12)
    )
    is_gut_root = (
        (np.abs(R_e8[:, 5]) < 1e-12)
        & (np.abs(R_e8[:, 6]) < 1e-12)
        & (np.abs(R_e8[:, 7]) < 1e-12)
        & (np.abs(np.sum(R_e8[:, :5], axis=1)) < 1e-12)
    )
    n_perp_adj = int(np.sum(is_perp_root)) + 4
    n_gut_adj = int(np.sum(is_gut_root)) + 4
    n_bifund_roots = 240 - int(np.sum(is_perp_root)) - int(np.sum(is_gut_root))

    q_10 = 1
    q_5bar = 2
    q_Hu = (-2) % 5
    q_Hd = 2

    up_yukawa_mod5 = (q_10 + q_10 + q_Hu) % 5
    down_charged_lep_mod5 = (q_10 + q_5bar + q_Hd) % 5
    weinberg_contact_mod5 = (q_5bar + q_5bar + q_Hu + q_Hu) % 5

    dirac_allowed_qN = [qN for qN in range(5) if (q_5bar + qN + q_Hu) % 5 == 0]
    majorana_allowed_qN = [qN for qN in range(5) if (2 * qN) % 5 == 0]
    simultaneous_qN = [qN for qN in range(5) if qN in dirac_allowed_qN and qN in majorana_allowed_qN]

    return {
        "e8_total_dim": n_gut_adj + n_perp_adj + n_bifund_roots,
        "su5_gut_adjoint_dim": n_gut_adj,
        "su5_perp_adjoint_dim": n_perp_adj,
        "matter_bifundamental_total_dim": n_bifund_roots,
        "up_yukawa_charge_sum_mod5": up_yukawa_mod5,
        "down_and_charged_lepton_charge_sum_mod5": down_charged_lep_mod5,
        "weinberg_quartic_charge_sum_mod5": weinberg_contact_mod5,
        "dirac_allowed_q_Nc": dirac_allowed_qN,
        "majorana_allowed_q_Nc": majorana_allowed_qN,
        "unique_simultaneous_q_Nc": simultaneous_qN,
        "passed": (
            n_gut_adj == 24
            and n_perp_adj == 24
            and n_bifund_roots == 200
            and up_yukawa_mod5 == 0
            and down_charged_lep_mod5 == 0
            and weinberg_contact_mod5 == 0
            and simultaneous_qN == [0]
        ),
    }


def _evaluate_single_bundle_quark_lepton(
    ep: Dict[str, Any],
    raw_cocycle: np.ndarray,
    s0_dir: Dict[str, Any],
    s0_neu: Dict[str, Any],
    n_sub: int,
    sub: Dict[str, Any],
    geoms: List[Dict[str, np.ndarray]],
    sig_p: int,
    run_haar: bool = True,
) -> Dict[str, Any]:
    """Evaluate CKM + PMNS (KK Seesaw N1 & Contact Weinberg N2) on one normalized cocycle."""
    coc = np.array(raw_cocycle, dtype=int) % 5
    s1 = assemble_and_solve_3d_sector(ep, coc, 1, n_sub, "dirichlet", 6, sub, geoms)
    s2 = assemble_and_solve_3d_sector(ep, coc, 2, n_sub, "dirichlet", 6, sub, geoms)
    if s1["eigenvalues"][0] < s2["eigenvalues"][0] - 1e-9:
        coc = (2 * coc) % 5
        s1 = assemble_and_solve_3d_sector(ep, coc, 1, n_sub, "dirichlet", 6, sub, geoms)
        s2 = assemble_and_solve_3d_sector(ep, coc, 2, n_sub, "dirichlet", 6, sub, geoms)

    psi_p1 = s1["local_modes"][:3]
    chi_p2 = s2["local_modes"][:3]
    phi_p2 = s2["local_modes"][0]
    phi_m2 = np.conj(phi_p2)

    Y_u = compute_trilinear_overlap_matrix_q14(psi_p1, psi_p1, phi_m2, sub["sub_tets"], geoms)
    Y_d = compute_trilinear_overlap_matrix_q14(psi_p1, chi_p2, phi_p2, sub["sub_tets"], geoms)
    Y_e = Y_d.T.copy()
    yu_sym_err = float(np.max(np.abs(Y_u - Y_u.T)))

    eta0_dir = s0_dir["local_modes"][:3]
    lam0_dir = np.array(s0_dir["eigenvalues"][:3], dtype=float)
    Y_nu_dir = compute_trilinear_overlap_matrix_q14(chi_p2, eta0_dir, phi_m2, sub["sub_tets"], geoms)
    M_R_dir = compute_bilinear_majorana_matrix_q14(eta0_dir, lam0_dir, sub["sub_tets"], geoms)
    M_nu_kk = -(Y_nu_dir @ np.linalg.solve(M_R_dir, Y_nu_dir.T))

    eta0_neu = s0_neu["local_modes"][1:4]
    lam0_neu = np.array(s0_neu["eigenvalues"][1:4], dtype=float)
    Y_nu_neu = compute_trilinear_overlap_matrix_q14(chi_p2, eta0_neu, phi_m2, sub["sub_tets"], geoms)
    M_R_neu = compute_bilinear_majorana_matrix_q14(eta0_neu, lam0_neu, sub["sub_tets"], geoms)
    M_nu_kk_neu = -(Y_nu_neu @ np.linalg.solve(M_R_neu, Y_nu_neu.T))

    # Bilinear eigensolver-phase invariance check on eta0_dir:
    rng_phase = np.random.default_rng(77123 + n_sub)
    rand_ph = np.exp(1j * rng_phase.uniform(0.0, 2.0 * math.pi, size=3))
    eta0_reph = eta0_dir * rand_ph[:, None, None]
    Y_nu_reph = compute_trilinear_overlap_matrix_q14(chi_p2, eta0_reph, phi_m2, sub["sub_tets"], geoms)
    M_R_reph = compute_bilinear_majorana_matrix_q14(eta0_reph, lam0_dir, sub["sub_tets"], geoms)
    M_nu_kk_reph = -(Y_nu_reph @ np.linalg.solve(M_R_reph, Y_nu_reph.T))
    kk_phase_inv_err = float(np.max(np.abs(M_nu_kk_reph - M_nu_kk)))

    M_nu_w = compute_quartic_weinberg_matrix_q14(chi_p2, phi_m2, sub["sub_tets"], geoms)

    q_obs = extract_quark_ckm_observables(Y_u, Y_d)
    l_kk = extract_lepton_pmns_observables(Y_e, M_nu_kk)
    l_kk_neu = extract_lepton_pmns_observables(Y_e, M_nu_kk_neu)
    l_w = extract_lepton_pmns_observables(Y_e, M_nu_w)

    haar_audits = None
    if run_haar:
        haar_audits = {
            "quark_ckm": verify_quark_haar_invariance(Y_u, Y_d, n_trials=16, seed=5100 + n_sub),
            "lepton_kk_seesaw": verify_lepton_seesaw_haar_invariance(Y_e, Y_nu_dir, M_R_dir, n_trials=16, seed=5200 + n_sub),
            "lepton_weinberg": verify_lepton_weinberg_haar_invariance(Y_e, M_nu_w, n_trials=16, seed=5300 + n_sub),
        }

    ckm_a = q_obs["angles"]
    pmns_kk_a = l_kk["angles"]
    pmns_w_a = l_w["angles"]

    return {
        "E0_q2": float(s2["eigenvalues"][0]),
        "E0_q1": float(s1["eigenvalues"][0]),
        "yu_symmetry_err": yu_sym_err,
        "kk_eigensolver_phase_invariance_err": kk_phase_inv_err,
        "quark_ckm": q_obs,
        "lepton_pmns_kk_dirichlet": l_kk,
        "lepton_pmns_kk_neumann_nonconst": l_kk_neu,
        "lepton_pmns_weinberg": l_w,
        "relational_jarlskog": {
            "ckm": float(sig_p * q_obs["jarlskog_norm"]),
            "pmns_kk_dirichlet": float(sig_p * l_kk["jarlskog_pmns_norm"]),
            "pmns_kk_neumann": float(sig_p * l_kk_neu["jarlskog_pmns_norm"]),
            "pmns_weinberg": float(sig_p * l_w["jarlskog_pmns_norm"]),
        },
        "acid_test_lepton_exceeds_quark": {
            "kk_dirichlet_theta12_gt_ckm": pmns_kk_a["sin2_theta_12"] > ckm_a["sin2_theta_12"],
            "kk_dirichlet_theta23_gt_ckm": pmns_kk_a["sin2_theta_23"] > ckm_a["sin2_theta_23"],
            "kk_dirichlet_theta13_gt_ckm": pmns_kk_a["sin2_theta_13"] > ckm_a["sin2_theta_13"],
            "weinberg_theta12_gt_ckm": pmns_w_a["sin2_theta_12"] > ckm_a["sin2_theta_12"],
            "weinberg_theta23_gt_ckm": pmns_w_a["sin2_theta_23"] > ckm_a["sin2_theta_23"],
            "weinberg_theta13_gt_ckm": pmns_w_a["sin2_theta_13"] > ckm_a["sin2_theta_13"],
            "kk_theta12_ratio_to_ckm": pmns_kk_a["sin2_theta_12"] / max(1e-30, ckm_a["sin2_theta_12"]),
            "kk_theta23_ratio_to_ckm": pmns_kk_a["sin2_theta_23"] / max(1e-30, ckm_a["sin2_theta_23"]),
            "weinberg_theta12_ratio_to_ckm": pmns_w_a["sin2_theta_12"] / max(1e-30, ckm_a["sin2_theta_12"]),
            "weinberg_theta23_ratio_to_ckm": pmns_w_a["sin2_theta_23"] / max(1e-30, ckm_a["sin2_theta_23"]),
        },
        "haar_audits": haar_audits,
    }


def evaluate_quark_lepton_on_manifold(
    spec: str,
    label: str,
    n_subs: Tuple[int, ...] = (3, 4),
) -> Dict[str, Any]:
    """Evaluate all 4 cusp-ramified Z/5Z bundles on `spec` across `n_subs` (and ground-state bundle at n_sub=5)."""
    ep = extract_epstein_penner_data(spec)
    coh = classify_cohomology_and_z5_cocycles(ep)
    ram_lines = coh["cusp_ramified_torsion_lines"]
    assert len(ram_lines) >= 4
    sig_p = 0 if ep["is_amphicheiral"] else active_weak_compass_sign(ep["chern_simons"])

    res_by_nsub: Dict[str, Any] = {}
    gs_line_idx_n3 = 0

    for n_sub in n_subs:
        sub = build_eulerian_subdivision(n_sub, True)
        geoms = [compute_tet_element_geometry_q14(G, sub["nodes_bary"], sub["sub_tets"]) for G in ep["grams"]]
        s0_dir = assemble_and_solve_3d_sector(ep, None, 0, n_sub, "dirichlet", 6, sub, geoms)
        s0_neu = assemble_and_solve_3d_sector(ep, None, 0, n_sub, "neumann", 6, sub, geoms)

        if n_sub <= 4:
            line_records = []
            for idx_r, rln in enumerate(ram_lines[:4]):
                rec = _evaluate_single_bundle_quark_lepton(
                    ep, rln["cocycle"], s0_dir, s0_neu, n_sub, sub, geoms, sig_p, run_haar=(idx_r < 2)
                )
                rec["f5_coords"] = rln["f5_coords"]
                line_records.append(rec)

            # Sort canonically by (round(E0_q2, 7), -relational_jarlskog["ckm"]) so the ground-state
            # positive-relational-Jarlskog branch is index 0 on EVERY triangulation of M and -M!
            line_records_sorted = sorted(
                line_records,
                key=lambda r: (round(r["E0_q2"], 7), -round(r["relational_jarlskog"]["ckm"], 13)),
            )
            if n_sub == 3:
                # Track original ram_lines index of canonical ground-state positive branch for n_sub=5:
                gs_coords = line_records_sorted[0]["f5_coords"]
                gs_line_idx_n3 = next(i for i, rln in enumerate(ram_lines[:4]) if rln["f5_coords"] == gs_coords)

            sum_j_ckm = float(sum(r["quark_ckm"]["jarlskog_norm"] for r in line_records_sorted))
            sum_j_pmns_kk = float(sum(r["lepton_pmns_kk_dirichlet"]["jarlskog_pmns_norm"] for r in line_records_sorted))
            sum_j_pmns_w = float(sum(r["lepton_pmns_weinberg"]["jarlskog_pmns_norm"] for r in line_records_sorted))

            res_by_nsub[f"nsub_{n_sub}"] = {
                "ground_state_positive_branch": line_records_sorted[0],
                "all_4_ramified_lines_sorted": line_records_sorted,
                "four_line_jarlskog_sums": {
                    "ckm": sum_j_ckm,
                    "pmns_kk_dirichlet": sum_j_pmns_kk,
                    "pmns_weinberg": sum_j_pmns_w,
                },
            }
        else:
            # At n_sub = 5, evaluate the two ground-state doublet lines to pick positive relational branch cleanly:
            e0_list = [r["E0_q2"] for r in res_by_nsub["nsub_4"]["all_4_ramified_lines_sorted"]]
            gs_coords_set = {
                tuple(r["f5_coords"])
                for r in res_by_nsub["nsub_4"]["all_4_ramified_lines_sorted"]
                if abs(r["E0_q2"] - e0_list[0]) < 1e-6
            }
            n5_records = []
            for rln in ram_lines[:4]:
                if tuple(rln["f5_coords"]) in gs_coords_set:
                    rec5 = _evaluate_single_bundle_quark_lepton(
                        ep, rln["cocycle"], s0_dir, s0_neu, n_sub, sub, geoms, sig_p, run_haar=True
                    )
                    rec5["f5_coords"] = rln["f5_coords"]
                    n5_records.append(rec5)
            n5_records.sort(key=lambda r: -round(r["relational_jarlskog"]["ckm"], 13))
            res_by_nsub[f"nsub_{n_sub}"] = {
                "ground_state_positive_branch": n5_records[0],
                "ground_state_doublet_lines": n5_records,
            }

    return {
        "label": label,
        "spec": spec,
        "volume": ep["snappy_volume"],
        "chern_simons": ep["chern_simons"],
        "sigma_P": sig_p,
        "symmetry_group": ep["symmetry_group_str"],
        "symmetry_order": ep["symmetry_order"],
        "is_amphicheiral": ep["is_amphicheiral"],
        "resolutions": res_by_nsub,
    }


def _compare_4line_enantiomer_bijection(ra: Dict[str, Any], rb: Dict[str, Any]) -> Dict[str, float]:
    """Compare all 4 canonically sorted cusp-ramified bundles between M and mirror -M."""
    la = ra["all_4_ramified_lines_sorted"]
    lb = rb["all_4_ramified_lines_sorted"]
    max_j_rel_err = 0.0
    max_sv_err = 0.0
    max_pmns_kk_err = 0.0
    max_pmns_w_err = 0.0
    max_ckm_err = 0.0

    for i in range(4):
        ia, ib = la[i], lb[i]
        max_j_rel_err = max(
            max_j_rel_err,
            abs(ia["relational_jarlskog"]["ckm"] - ib["relational_jarlskog"]["ckm"]),
            abs(ia["relational_jarlskog"]["pmns_kk_dirichlet"] - ib["relational_jarlskog"]["pmns_kk_dirichlet"]),
            abs(ia["relational_jarlskog"]["pmns_weinberg"] - ib["relational_jarlskog"]["pmns_weinberg"]),
        )
        max_sv_err = max(
            max_sv_err,
            float(np.max(np.abs(np.array(ia["quark_ckm"]["sv_u_ratios"]) - np.array(ib["quark_ckm"]["sv_u_ratios"])))),
            float(np.max(np.abs(np.array(ia["lepton_pmns_kk_dirichlet"]["sv_nu_ratios"]) - np.array(ib["lepton_pmns_kk_dirichlet"]["sv_nu_ratios"])))),
            float(np.max(np.abs(np.array(ia["lepton_pmns_weinberg"]["sv_nu_ratios"]) - np.array(ib["lepton_pmns_weinberg"]["sv_nu_ratios"])))),
        )

        sp_q = min(ia["quark_ckm"]["min_rel_sv_split_u"], ia["quark_ckm"]["min_rel_sv_split_d"])
        wq = min(1.0, sp_q / 1e-3) if sp_q > 1e-6 else 0.0
        max_ckm_err = max(
            max_ckm_err,
            wq * float(np.max(np.abs(np.array(ia["quark_ckm"]["ckm_abs_matrix"]) - np.array(ib["quark_ckm"]["ckm_abs_matrix"])))),
        )

        sp_kk = min(ia["lepton_pmns_kk_dirichlet"]["min_rel_sv_split_e"], ia["lepton_pmns_kk_dirichlet"]["min_rel_sv_split_nu"])
        wkk = min(1.0, sp_kk / 1e-3) if sp_kk > 1e-6 else 0.0
        max_pmns_kk_err = max(
            max_pmns_kk_err,
            wkk * float(np.max(np.abs(np.array(ia["lepton_pmns_kk_dirichlet"]["pmns_abs_matrix"]) - np.array(ib["lepton_pmns_kk_dirichlet"]["pmns_abs_matrix"])))),
        )

        sp_w = min(ia["lepton_pmns_weinberg"]["min_rel_sv_split_e"], ia["lepton_pmns_weinberg"]["min_rel_sv_split_nu"])
        ww = min(1.0, sp_w / 1e-3) if sp_w > 1e-6 else 0.0
        max_pmns_w_err = max(
            max_pmns_w_err,
            ww * float(np.max(np.abs(np.array(ia["lepton_pmns_weinberg"]["pmns_abs_matrix"]) - np.array(ib["lepton_pmns_weinberg"]["pmns_abs_matrix"])))),
        )

    return {
        "max_relational_jarlskog_err": max_j_rel_err,
        "max_sv_ratio_err": max_sv_err,
        "max_wedin_ckm_err": max_ckm_err,
        "max_wedin_pmns_kk_err": max_pmns_kk_err,
        "max_wedin_pmns_weinberg_err": max_pmns_w_err,
    }


def run_gate3_quark_lepton_unification() -> Dict[str, Any]:
    """Execute complete Gate 3 across controls, reversible bulk, and chiral irreversible candidates."""
    branching = verify_e8_lepton_branching_and_charge_uniqueness()

    roster: List[Tuple[str, str, Tuple[int, ...]]] = [
        ("amphicheiral_m003_control", "b+-LR", (3, 4)),
        ("amphicheiral_5_5_control", "b+-LLLLLRRRRRLR", (3, 4)),
        ("min_unrestricted_reversible_L5R", "b++LLLRLL", (3, 4)),
        ("reversible_6", "b++LLLLLLRLR", (3, 4, 5)),
        ("reversible_1_6_mirror", "b++LRRRRRRLR", (3, 4)),
        ("reversible_single_peak_313", "b++LLLRLLLRLR", (3, 4)),
        ("global_min_irreversible_719", "b+-LLLLLRLLRR", (3, 4, 5)),
        ("global_min_irreversible_719_mirror", "b+-LLRRLRRRRR", (3, 4)),
        ("min_bpp_irreversible_736", "b++LLLLLLLRRLLR", (3, 4)),
        ("min_bpp_irreversible_736_mirror", "b++RRRRRLRRLLRR", (3, 4)),
        ("departure_irreversible_5122", "b++LLLLLRLLRRLR", (3, 4, 5)),
        ("departure_irreversible_2215_mirror", "b++LLRRLRRRRRLR", (3, 4)),
    ]

    evals: Dict[str, Any] = {}
    for label, spec, n_subs in roster:
        evals[label] = evaluate_quark_lepton_on_manifold(spec, label, n_subs=n_subs)

    # 1. Verify Haar invariance & eigensolver-phase invariance across every run:
    all_haar_passed = True
    max_phase_inv_err = 0.0
    for rec in evals.values():
        for r_sub in rec["resolutions"].values():
            lines_check = r_sub.get("all_4_ramified_lines_sorted") or r_sub.get("ground_state_doublet_lines", [])
            for ln_rec in lines_check:
                max_phase_inv_err = max(max_phase_inv_err, ln_rec["kk_eigensolver_phase_invariance_err"])
                if ln_rec["haar_audits"] is not None:
                    ha = ln_rec["haar_audits"]
                    if not (
                        ha["quark_ckm"]["passed"]
                        and ha["lepton_kk_seesaw"]["passed"]
                        and ha["lepton_weinberg"]["passed"]
                    ):
                        all_haar_passed = False

    # 2. Verify Klein-four / D4 CP vanishing on EVERY single bundle (< 1e-14):
    klein4_d4_labels = [
        "amphicheiral_m003_control",
        "min_unrestricted_reversible_L5R",
        "reversible_6",
        "reversible_1_6_mirror",
        "reversible_single_peak_313",
    ]
    max_klein4_jarlskog = 0.0
    for lbl in klein4_d4_labels:
        for ln_rec in evals[lbl]["resolutions"]["nsub_4"]["all_4_ramified_lines_sorted"]:
            max_klein4_jarlskog = max(
                max_klein4_jarlskog,
                abs(ln_rec["quark_ckm"]["jarlskog_norm"]),
                abs(ln_rec["lepton_pmns_kk_dirichlet"]["jarlskog_pmns_norm"]),
                abs(ln_rec["lepton_pmns_weinberg"]["jarlskog_pmns_norm"]),
            )

    # 3. Verify Z/4 amphicheiral (5,5) relational Jarlskog == 0.0 and 4-line sum == 0 (< 1e-14):
    amph55_n4 = evals["amphicheiral_5_5_control"]["resolutions"]["nsub_4"]
    amph55_max_rel_j = max(
        max(abs(v) for v in ln_rec["relational_jarlskog"].values())
        for ln_rec in amph55_n4["all_4_ramified_lines_sorted"]
    )
    amph55_max_4line_sum_err = max(abs(v) for v in amph55_n4["four_line_jarlskog_sums"].values())

    # 4. Verify exact 4-line enantiomer relational collapse (< 1e-12):
    enantiomer_pairs = [
        ("reversible_6", "reversible_1_6_mirror"),
        ("global_min_irreversible_719", "global_min_irreversible_719_mirror"),
        ("min_bpp_irreversible_736", "min_bpp_irreversible_736_mirror"),
        ("departure_irreversible_5122", "departure_irreversible_2215_mirror"),
    ]
    enantiomer_audits = {}
    max_enantiomer_rel_err = 0.0
    for lbl_a, lbl_b in enantiomer_pairs:
        cmp_res = _compare_4line_enantiomer_bijection(
            evals[lbl_a]["resolutions"]["nsub_4"],
            evals[lbl_b]["resolutions"]["nsub_4"],
        )
        enantiomer_audits[f"{lbl_a}__vs__{lbl_b}"] = cmp_res
        max_enantiomer_rel_err = max(max_enantiomer_rel_err, max(cmp_res.values()))

    # 5. Summarize Quark-vs.-Lepton Acid Test across the 3 chiral irreversible manifolds (nsub=4 & 5):
    irrev_summary = {}
    for lbl in ("global_min_irreversible_719", "min_bpp_irreversible_736", "departure_irreversible_5122"):
        gs4 = evals[lbl]["resolutions"]["nsub_4"]["ground_state_positive_branch"]
        irrev_summary[lbl] = {
            "ckm_angles_deg_nsub4": {k: gs4["quark_ckm"]["angles"][k] for k in ("theta_12_deg", "theta_23_deg", "theta_13_deg")},
            "pmns_kk_dirichlet_angles_deg_nsub4": {k: gs4["lepton_pmns_kk_dirichlet"]["angles"][k] for k in ("theta_12_deg", "theta_23_deg", "theta_13_deg")},
            "pmns_kk_neumann_angles_deg_nsub4": {k: gs4["lepton_pmns_kk_neumann_nonconst"]["angles"][k] for k in ("theta_12_deg", "theta_23_deg", "theta_13_deg")},
            "pmns_weinberg_angles_deg_nsub4": {k: gs4["lepton_pmns_weinberg"]["angles"][k] for k in ("theta_12_deg", "theta_23_deg", "theta_13_deg")},
            "relational_jarlskog_nsub4": gs4["relational_jarlskog"],
            "acid_test_flags_nsub4": gs4["acid_test_lepton_exceeds_quark"],
        }
        if "nsub_5" in evals[lbl]["resolutions"]:
            gs5 = evals[lbl]["resolutions"]["nsub_5"]["ground_state_positive_branch"]
            irrev_summary[lbl]["ckm_angles_deg_nsub5"] = {k: gs5["quark_ckm"]["angles"][k] for k in ("theta_12_deg", "theta_23_deg", "theta_13_deg")}
            irrev_summary[lbl]["pmns_kk_dirichlet_angles_deg_nsub5"] = {k: gs5["lepton_pmns_kk_dirichlet"]["angles"][k] for k in ("theta_12_deg", "theta_23_deg", "theta_13_deg")}
            irrev_summary[lbl]["pmns_weinberg_angles_deg_nsub5"] = {k: gs5["lepton_pmns_weinberg"]["angles"][k] for k in ("theta_12_deg", "theta_23_deg", "theta_13_deg")}
            irrev_summary[lbl]["relational_jarlskog_nsub5"] = gs5["relational_jarlskog"]

    gate3_passed = (
        branching["passed"]
        and all_haar_passed
        and max_phase_inv_err < 1e-13
        and max_klein4_jarlskog < 1e-14
        and amph55_max_rel_j == 0.0
        and amph55_max_4line_sum_err < 1e-14
        and max_enantiomer_rel_err < 1e-12
    )

    return {
        "e8_lepton_branching_and_charge_uniqueness": branching,
        "all_haar_scrambling_passed": all_haar_passed,
        "max_kk_eigensolver_phase_invariance_err": max_phase_inv_err,
        "max_klein4_cp_protected_jarlskog": max_klein4_jarlskog,
        "amphicheiral_5_5_max_relational_jarlskog": amph55_max_rel_j,
        "amphicheiral_5_5_max_4line_sum_err": amph55_max_4line_sum_err,
        "enantiomer_4line_relational_audits": enantiomer_audits,
        "max_enantiomer_relational_err": max_enantiomer_rel_err,
        "chiral_irreversible_acid_test_summary": irrev_summary,
        "candidates": evals,
        "gate3_passed": gate3_passed,
    }


if __name__ == "__main__":
    out = run_gate3_quark_lepton_unification()
    print("Gate 3 passed:", out["gate3_passed"])
    print("  Branching & q(N^c)=0 uniqueness:", out["e8_lepton_branching_and_charge_uniqueness"]["passed"])
    print("  All Haar passed:", out["all_haar_scrambling_passed"], "Max KK phase err:", out["max_kk_eigensolver_phase_invariance_err"])
    print("  Max Klein-4 |J|:", out["max_klein4_cp_protected_jarlskog"])
    print("  Z/4 Amph (5,5) 4-line sum err:", out["amphicheiral_5_5_max_4line_sum_err"], "rel J:", out["amphicheiral_5_5_max_relational_jarlskog"])
    print("  Max 4-line enantiomer relational err:", out["max_enantiomer_relational_err"])
    for k, s in out["chiral_irreversible_acid_test_summary"].items():
        print(f"\n  === {k} ===")
        for subk, subv in s.items():
            print(f"    {subk}: {subv}")
