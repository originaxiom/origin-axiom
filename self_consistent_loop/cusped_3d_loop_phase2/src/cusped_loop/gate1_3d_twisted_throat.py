"""Gate 1: True 3D Hyperbolic Pinched Throat vs. Uniform-Area Sol Mirror Split.

Tests whether solving the Z/5Z-twisted 3D Laplace-Beltrami operator on the true
cusped hyperbolic 3-manifold M_H (where long L^6 stretches pinch into an ultra-short
Margulis throat) resolves the uniform-area Sol 2-peak mirror split on `(6)` into a
unique ground state or leaves a genuine degeneracy, across:
  - `(6)` (`LLLLLLRLR`), enantiomer `(1,6)` (`LRRRRRRLR`), `(2,1,2,1,2)`,
    `(2,1,1,1,2)`, `(2,1^8,2)`, golden background `LR`,
  - planted negative control `L^2 R L R` (`LLRLR`, must be rejected by bundle gate),
  - all 18 bundle-extending histories in the bounded family `A6` (<=5 runs, sum<=8, k=1),
under both `b++` and `b+-` punctured-torus sign conventions, both cusp-unramified
(`5 cusps` in cover, Neumann & Dirichlet BCs) and cusp-ramified (`1 cusp`, Dirichlet BC)
torsion characters, charges q=1 and q=2, and mesh refinements n_sub in {3, 4, 5}.
"""

from __future__ import annotations

import itertools
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from .hyperbolic_fem_core import (
    assemble_and_solve_3d_laplacian,
    build_eulerian_subdivision,
    classify_z5_torsion_cocycles,
    extract_epstein_penner_data,
)


L_MAT = np.array([[1, 1], [0, 1]], dtype=int)
R_MAT = np.array([[1, 0], [1, 1]], dtype=int)
GOLDEN_V5 = np.array([1, 2], dtype=int)  # Golden K^-(LR) generator mod 5


def word_to_matrix(word: str) -> np.ndarray:
    """Evaluate an L/R word in SL(2, Z)."""
    M = np.eye(2, dtype=int)
    for ch in word:
        if ch == "L":
            M = M @ L_MAT
        elif ch == "R":
            M = M @ R_MAT
        else:
            raise ValueError(f"Unknown letter {ch!r}")
    return M


def runs_to_departure_word(runs: Tuple[int, ...]) -> str:
    """Convert run-length tuple (r_1, r_2, ...) into alternating L/R departure word ending with R."""
    # Convention matching Phase 1: odd number of runs starts with L and ends with R;
    # even number of runs starts with L and ends with R (e.g. (1, 6) -> L R^6).
    if len(runs) == 0:
        return ""
    start_L = True if (len(runs) % 2 == 0) else True
    # Wait: if len(runs) is odd: L^{r0} R^{r1} ... L^{r_{2k}} ends in L unless appended R!
    # Check Phase 1 convention:
    #   (6,) -> "LLLLLLR" (L^6 R, closed by LR -> LLLLLLRLR)
    #   (1, 6) -> "LRRRRRR" (L^1 R^6, closed by LR -> LRRRRRRLR)
    #   (2, 1, 2, 1, 2) -> "LLRLLRLLR" (L^2 R^1 L^2 R^1 L^2 R, closed by LR -> LLRLLRLLRLR)
    letters = []
    use_L = True
    for r in runs:
        letters.append(("L" if use_L else "R") * r)
        use_L = not use_L
    if letters[-1].endswith("L"):
        letters.append("R")
    return "".join(letters)


def check_golden_bundle_extension(word: str) -> Dict[str, Any]:
    """Check whether W_H^T (1,2) == +-(1,2) mod 5 (algebraic bundle extension gate)."""
    W = word_to_matrix(word)
    img = (W.T @ GOLDEN_V5) % 5
    pos = np.array_equal(img, GOLDEN_V5 % 5)
    neg = np.array_equal(img, (-GOLDEN_V5) % 5)
    extends = bool(pos or neg)
    sign = 1 if pos else (-1 if neg else 0)
    return {
        "word": word,
        "matrix": W.tolist(),
        "trace": int(W[0, 0] + W[1, 1]),
        "extends_golden_v5": extends,
        "extension_sign_on_b_pp": sign,
        "direct_rank1_prefix": ("b++" if sign == 1 else ("b+-" if sign == -1 else None)),
    }


def enumerate_bounded_extending_family_A6(
    max_runs: int = 5, max_sum: int = 8
) -> Dict[str, Any]:
    """Enumerate all non-trivial departure run tuples with <= max_runs, sum <= max_sum (k=1)."""
    seen_words = set()
    tested = 0
    extending: List[Dict[str, Any]] = []

    for n_runs in range(1, max_runs + 1):
        for runs in itertools.product(range(1, max_sum + 1), repeat=n_runs):
            if sum(runs) > max_sum:
                continue
            dep = runs_to_departure_word(runs)
            full_word = dep + "LR"
            if full_word in seen_words or full_word == "LR":
                continue
            seen_words.add(full_word)
            tested += 1
            ext = check_golden_bundle_extension(full_word)
            if ext["extends_golden_v5"]:
                extending.append({"runs": list(runs), **ext})

    return {
        "tested_unique_words": tested,
        "extending_count": len(extending),
        "extending_members": extending,
    }


def check_margulis_geodesic_holonomy(ep_data: Dict[str, Any]) -> Dict[str, Any]:
    """Check shortest closed geodesic length l_1 in M_H and its lift in 5-fold torsion covers."""
    M = ep_data["manifold"]
    try:
        ls_base = M.length_spectrum(2.6)
        if len(ls_base) == 0:
            ls_base = M.length_spectrum(4.0)
    except Exception:
        ls_base = []

    if not ls_base:
        return {"found_shortest_geodesic": False}

    g0 = ls_base[0]
    l1_complex = complex(g0["length"])
    l1_real = float(l1_complex.real)
    l1_mult = int(g0["multiplicity"])

    # Check lift in the 5-cusp torsion cover (if available)
    M_std = M.low_precision() if hasattr(M, "low_precision") else M
    covs_5cusp = [c for c in M_std.covers(5, cover_type="cyclic") if c.num_cusps() == 5]
    cover_lift_info: Optional[Dict[str, Any]] = None
    if covs_5cusp:
        cov = covs_5cusp[0]
        # Look up to max(2.0, 5 * l1_real + 0.15) if 5 * l1_real <= 3.0
        cutoff = min(3.2, max(1.5, 5.0 * l1_real + 0.15))
        try:
            ls_cov = cov.length_spectrum(cutoff)
            if len(ls_cov) > 0:
                gc0 = ls_cov[0]
                lc_real = float(complex(gc0["length"]).real)
                lc_mult = int(gc0["multiplicity"])
                # Uncharged geodesic lifts to 5 copies of length l1_real;
                # Z/5Z-charged geodesic lifts to 1 single tube of length 5 * l1_real!
                charged_lift = abs(lc_real - 5.0 * l1_real) < 1e-4 and lc_mult == l1_mult
                uncharged_lift = abs(lc_real - l1_real) < 1e-4 and lc_mult == 5 * l1_mult
                cover_lift_info = {
                    "cover_shortest_real_len": lc_real,
                    "cover_shortest_mult": lc_mult,
                    "ratio_to_base_l1": lc_real / l1_real,
                    "shortest_throat_is_z5_charged": charged_lift,
                    "shortest_throat_is_z5_trivial": uncharged_lift,
                }
        except Exception:
            cover_lift_info = None

    return {
        "found_shortest_geodesic": True,
        "shortest_real_length": l1_real,
        "shortest_torsion_angle": float(l1_complex.imag),
        "shortest_multiplicity": l1_mult,
        "cover_5cusp_lift": cover_lift_info,
    }


def evaluate_3d_history_both_conventions(
    label: str,
    word: str,
    subdiv_cache: Dict[int, Dict[str, Any]],
    n_subs: Tuple[int, ...] = (3, 4),
) -> Dict[str, Any]:
    """Evaluate 3D cusped hyperbolic twisted Laplacian under both b++ and b+-."""
    ext = check_golden_bundle_extension(word)
    if not ext["extends_golden_v5"]:
        return {
            "label": label,
            "word": word,
            "extends_golden_v5": False,
            "rejected_by_bundle_gate": True,
        }

    sign_pp = ext["extension_sign_on_b_pp"]  # +1 => direct rank-1 on b++, -1 => direct rank-1 on b+-
    direct_prefix = "b++" if sign_pp == 1 else "b+-"
    rank2_prefix = "b+-" if sign_pp == 1 else "b++"

    # 1. Direct rank-1 manifold (has 5 | |H_1(M)_tors| directly on N_let tetrahedra!)
    ep_direct = extract_epstein_penner_data(direct_prefix + word)
    cocycles_dir = classify_z5_torsion_cocycles(ep_direct)
    assert cocycles_dir["has_5_torsion"], f"Expected 5-torsion on {direct_prefix + word}"

    # Pick canonical cusp-unramified torsion line (if t5_rank==2, test all and select lowest E0)
    unram_lines = cocycles_dir["cusp_unramified_torsion_lines"]
    ram_lines = cocycles_dir["cusp_ramified_torsion_lines"]

    # Mesh convergence scan on cusp-unramified q=1 (Neumann and Dirichlet) and q=2 (Neumann)
    mesh_scan: Dict[str, Any] = {}
    best_unram_line_idx = 0
    if len(unram_lines) > 1:
        # Evaluate all cusp-unramified lines at n_sub = n_subs[0] to inspect full spectrum
        trial_e0s = []
        for idx_l, ln in enumerate(unram_lines):
            r_try = assemble_and_solve_3d_laplacian(
                ep_direct,
                cocycle_mod5=ln["cocycle"],
                charge_q=1,
                n_sub=n_subs[0],
                cusp_bc="neumann",
                n_eigs=6,
                subdiv_cache=subdiv_cache[n_subs[0]],
            )
            trial_e0s.append((r_try["E0"], idx_l, r_try))
        trial_e0s.sort(key=lambda x: x[0])
        best_unram_line_idx = trial_e0s[0][1]

    c_unram = unram_lines[best_unram_line_idx]["cocycle"]

    for ns in n_subs:
        r_q1_neu = assemble_and_solve_3d_laplacian(
            ep_direct,
            cocycle_mod5=c_unram,
            charge_q=1,
            n_sub=ns,
            cusp_bc="neumann",
            n_eigs=6,
            subdiv_cache=subdiv_cache[ns],
        )
        r_q1_dir = assemble_and_solve_3d_laplacian(
            ep_direct,
            cocycle_mod5=c_unram,
            charge_q=1,
            n_sub=ns,
            cusp_bc="dirichlet",
            n_eigs=6,
            subdiv_cache=subdiv_cache[ns],
        )
        r_q2_neu = assemble_and_solve_3d_laplacian(
            ep_direct,
            cocycle_mod5=c_unram,
            charge_q=2,
            n_sub=ns,
            cusp_bc="neumann",
            n_eigs=6,
            subdiv_cache=subdiv_cache[ns],
        )
        r_untw = assemble_and_solve_3d_laplacian(
            ep_direct,
            cocycle_mod5=None,
            charge_q=0,
            n_sub=ns,
            cusp_bc="neumann",
            n_eigs=6,
            subdiv_cache=subdiv_cache[ns],
        )
        mesh_scan[f"n_sub={ns}"] = {
            "untwisted_S1_neumann": {
                "E0": r_untw["E0"],
                "rel_gap": r_untw["rel_gap"],
                "mult": r_untw["ground_multiplicity"],
                "prob_peaks": r_untw["dominant_prob_peak_layers"],
                "dens_peaks": r_untw["dominant_density_peak_layers"],
                "layer_probs": r_untw["layer_probs"],
            },
            "twisted_q1_cusp_unram_neumann": {
                "E0": r_q1_neu["E0"],
                "E1_next": r_q1_neu["E1_next_distinct"],
                "rel_gap": r_q1_neu["rel_gap"],
                "mult": r_q1_neu["ground_multiplicity"],
                "prob_peaks": r_q1_neu["dominant_prob_peak_layers"],
                "dens_peaks": r_q1_neu["dominant_density_peak_layers"],
                "single_prob_peak": r_q1_neu["is_unique_single_layer_prob_peak"],
                "single_dens_peak": r_q1_neu["is_unique_single_layer_density_peak"],
                "layer_probs": r_q1_neu["layer_probs"],
                "layer_density_ratio": r_q1_neu["layer_density_ratio"],
                "tau_expectation": r_q1_neu["tau_pleated_expectation"],
            },
            "twisted_q1_cusp_unram_dirichlet": {
                "E0": r_q1_dir["E0"],
                "rel_gap": r_q1_dir["rel_gap"],
                "mult": r_q1_dir["ground_multiplicity"],
                "prob_peaks": r_q1_dir["dominant_prob_peak_layers"],
                "dens_peaks": r_q1_dir["dominant_density_peak_layers"],
                "single_prob_peak": r_q1_dir["is_unique_single_layer_prob_peak"],
                "layer_probs": r_q1_dir["layer_probs"],
            },
            "twisted_q2_cusp_unram_neumann": {
                "E0": r_q2_neu["E0"],
                "rel_gap": r_q2_neu["rel_gap"],
                "mult": r_q2_neu["ground_multiplicity"],
                "prob_peaks": r_q2_neu["dominant_prob_peak_layers"],
                "dens_peaks": r_q2_neu["dominant_density_peak_layers"],
                "single_prob_peak": r_q2_neu["is_unique_single_layer_prob_peak"],
                "layer_probs": r_q2_neu["layer_probs"],
            },
        }

    # Also evaluate cusp-ramified torsion lines (1 cusp in 5-fold cover, exact Dirichlet BC at cusp)
    ramified_summary = []
    ns_top = n_subs[-1]
    for r_idx, r_ln in enumerate(ram_lines[:4]):
        rr = assemble_and_solve_3d_laplacian(
            ep_direct,
            cocycle_mod5=r_ln["cocycle"],
            charge_q=1,
            n_sub=ns_top,
            cusp_bc="dirichlet",
            n_eigs=5,
            subdiv_cache=subdiv_cache[ns_top],
        )
        ramified_summary.append(
            {
                "line_idx": r_idx,
                "E0": rr["E0"],
                "rel_gap": rr["rel_gap"],
                "mult": rr["ground_multiplicity"],
                "prob_peaks": rr["dominant_prob_peak_layers"],
                "dens_peaks": rr["dominant_density_peak_layers"],
                "single_prob_peak": rr["is_unique_single_layer_prob_peak"],
            }
        )

    # 2. Opposite convention (rank-2 D_5 bundle via base-circle 2-fold cover b++(word + word))
    word_double = word + word
    ep_double = extract_epstein_penner_data("b++" + word_double)
    coc_double = classify_z5_torsion_cocycles(ep_double)
    double_summary: Optional[Dict[str, Any]] = None
    if coc_double["cusp_unramified_torsion_lines"]:
        c_dbl = coc_double["cusp_unramified_torsion_lines"][0]["cocycle"]
        ns_d = n_subs[0]
        r_dbl = assemble_and_solve_3d_laplacian(
            ep_double,
            cocycle_mod5=c_dbl,
            charge_q=1,
            n_sub=ns_d,
            cusp_bc="neumann",
            n_eigs=6,
            subdiv_cache=subdiv_cache[ns_d],
        )
        n_let = len(word)
        folded_probs = (
            np.array(r_dbl["layer_probs"][:n_let]) + np.array(r_dbl["layer_probs"][n_let:])
        )
        double_summary = {
            "cover_manifold": "b++" + word_double,
            "n_sub": ns_d,
            "E0": r_dbl["E0"],
            "rel_gap": r_dbl["rel_gap"],
            "mult": r_dbl["ground_multiplicity"],
            "folded_base_layer_probs": folded_probs.tolist(),
            "argmax_folded_layer": int(np.argmax(folded_probs)),
        }

    # Shortest closed geodesic & Margulis throat holonomy check
    geod_info = check_margulis_geodesic_holonomy(ep_direct)

    # Identify which tetrahedron layers have minimal horotriangle edge (pinched throat layers)
    # and maximal tetrahedral Bloch-Wigner volume (thick anti-apex layers)
    min_horo_val = min(ep_direct["horo_min_edge"])
    throat_layers = [
        i for i, v in enumerate(ep_direct["horo_min_edge"]) if abs(v - min_horo_val) <= 1e-6
    ]
    max_bw_val = max(ep_direct["tet_bw_volumes"])
    thick_layers = [
        i for i, v in enumerate(ep_direct["tet_bw_volumes"]) if abs(v - max_bw_val) <= 1e-6
    ]

    finest = mesh_scan[f"n_sub={n_subs[-1]}"]["twisted_q1_cusp_unram_neumann"]
    return {
        "label": label,
        "word": word,
        "num_letters_tets": ep_direct["num_tets"],
        "extends_golden_v5": True,
        "direct_rank1_manifold": direct_prefix + word,
        "opposite_rank2_manifold": rank2_prefix + word,
        "homology_direct": ep_direct["homology_str"],
        "torsion_5_rank": cocycles_dir["torsion_5_rank"],
        "snappy_volume": ep_direct["snappy_volume"],
        "tet_bw_volumes": ep_direct["tet_bw_volumes"],
        "horo_min_edge_by_layer": ep_direct["horo_min_edge"],
        "pinched_throat_layers": throat_layers,
        "thickest_volume_layers": thick_layers,
        "margulis_geodesic_check": geod_info,
        "mesh_convergence": mesh_scan,
        "cusp_ramified_q1_dirichlet": ramified_summary,
        "opposite_convention_2fold_cover": double_summary,
        "headline_finest_q1": {
            "n_sub": n_subs[-1],
            "E0": finest["E0"],
            "rel_gap": finest["rel_gap"],
            "ground_multiplicity": finest["mult"],
            "prob_peak_layers": finest["prob_peaks"],
            "density_peak_layers": finest["dens_peaks"],
            "single_prob_peak": finest["single_prob_peak"],
            "single_density_peak": finest["single_dens_peak"],
            "tau_pleated_expectation": finest["tau_expectation"],
        },
    }


def run_gate1() -> Dict[str, Any]:
    """Execute Gate 1 across headline candidates, negative control, and full A6 family."""
    subdiv_cache = {
        ns: build_eulerian_subdivision(ns, truncate_cusp_corners=True) for ns in (3, 4, 5)
    }

    # 1. Planted negative control: L^2 R L R ("LLRLR") must be rejected by bundle extension
    neg_ctrl = evaluate_3d_history_both_conventions("neg_ctrl_L2RLR", "LLRLR", subdiv_cache, (3,))

    # 2. Primary catalog histories evaluated up to n_sub = 5 (for <=10 tets) or (3, 4)
    primary_specs = [
        ("golden_bg_LR", "LR", (3, 4, 5)),
        ("(6)_LLLLLLRLR", runs_to_departure_word((6,)) + "LR", (3, 4, 5)),
        ("(1,6)_LRRRRRRLR", runs_to_departure_word((1, 6)) + "LR", (3, 4, 5)),
        ("(2,1,2,1,2)", runs_to_departure_word((2, 1, 2, 1, 2)) + "LR", (3, 4)),
        ("(2,1,1,1,2)", runs_to_departure_word((2, 1, 1, 1, 2)) + "LR", (3, 4)),
        ("(2,1^8,2)", runs_to_departure_word((2, 1, 1, 1, 1, 1, 1, 1, 1, 2)) + "LR", (3, 4)),
    ]

    primary_results: Dict[str, Any] = {}
    for label, word, n_subs in primary_specs:
        primary_results[label] = evaluate_3d_history_both_conventions(
            label, word, subdiv_cache, n_subs=n_subs
        )

    # 3. Full bounded family A6 scan (all 18 extending words at n_sub = 3, 4)
    a6_enum = enumerate_bounded_extending_family_A6(max_runs=5, max_sum=8)
    a6_results: List[Dict[str, Any]] = []
    for member in a6_enum["extending_members"]:
        w = member["word"]
        lbl = f"runs_{tuple(member['runs'])}"
        res_m = evaluate_3d_history_both_conventions(lbl, w, subdiv_cache, n_subs=(3, 4))
        a6_results.append(
            {
                "runs": member["runs"],
                "word": w,
                "letters": len(w),
                "volume": res_m["snappy_volume"],
                "direct_manifold": res_m["direct_rank1_manifold"],
                "E0_q1": res_m["headline_finest_q1"]["E0"],
                "rel_gap_q1": res_m["headline_finest_q1"]["rel_gap"],
                "mult_q1": res_m["headline_finest_q1"]["ground_multiplicity"],
                "prob_peaks_q1": res_m["headline_finest_q1"]["prob_peak_layers"],
                "dens_peaks_q1": res_m["headline_finest_q1"]["density_peak_layers"],
                "single_prob_peak": res_m["headline_finest_q1"]["single_prob_peak"],
                "single_dens_peak": res_m["headline_finest_q1"]["single_density_peak"],
                "tau_pleated_expectation": res_m["headline_finest_q1"]["tau_pleated_expectation"],
            }
        )

    a6_results.sort(key=lambda x: (x["volume"], x["letters"], x["word"]))
    single_prob_count = sum(1 for x in a6_results if x["single_prob_peak"])
    single_dens_count = sum(1 for x in a6_results if x["single_dens_peak"])
    nondeg_e0_count = sum(1 for x in a6_results if x["mult_q1"] == 1)

    r6 = primary_results["(6)_LLLLLLRLR"]
    r16 = primary_results["(1,6)_LRRRRRRLR"]
    enantiomer_e0_diff = abs(
        r6["headline_finest_q1"]["E0"] - r16["headline_finest_q1"]["E0"]
    )
    r6_n5_q1 = r6["mesh_convergence"]["n_sub=5"]["twisted_q1_cusp_unram_neumann"]
    r6_n5_q2 = r6["mesh_convergence"]["n_sub=5"]["twisted_q2_cusp_unram_neumann"]
    p_q2 = r6_n5_q2["layer_probs"]
    p_q1 = r6_n5_q1["layer_probs"]
    palindromic_isometry_err = max(
        abs(p_q2[0] - p_q2[6]),
        abs(p_q2[1] - p_q2[5]),
        abs(p_q2[2] - p_q2[4]),
        abs(p_q2[7] - p_q2[8]),
        abs(p_q1[0] - p_q1[6]),
        abs(p_q1[7] - p_q1[8]),
    )

    return {
        "gate": "Gate 1: True 3D Hyperbolic Pinched Throat vs. Sol Split",
        "negative_control_L2RLR": neg_ctrl,
        "primary_catalog": primary_results,
        "enantiomer_6_vs_1_6_E0_diff": enantiomer_e0_diff,
        "run6_3d_verdict": {
            "ground_eigenvalue_nondegenerate_mult_eq_1": (
                r6_n5_q2["mult"] == 1 and r6_n5_q1["mult"] == 1
            ),
            "lowest_twisted_orbit_q2": {
                "E0_n5": r6_n5_q2["E0"],
                "rel_gap_n5": r6_n5_q2["rel_gap"],
                "mult": r6_n5_q2["mult"],
                "prob_peak_layers": r6_n5_q2["prob_peaks"],
                "density_peak_layers": r6_n5_q2["dens_peaks"],
                "throat_center_prob_P3": p_q2[3],
                "shoulder_probs_P0_P6": [p_q2[0], p_q2[6]],
            },
            "secondary_twisted_orbit_q1": {
                "E0_n5": r6_n5_q1["E0"],
                "rel_gap_n5": r6_n5_q1["rel_gap"],
                "mult": r6_n5_q1["mult"],
                "merged_plateau_peak": r6_n5_q1["prob_peaks"],
                "anti_apex_pair_probs_P7_P8": [p_q1[7], p_q1[8]],
                "throat_center_prob_P3": p_q1[3],
            },
            "palindromic_Z2_isometry_prob_symmetry_err": palindromic_isometry_err,
            "E0_n5": r6["headline_finest_q1"]["E0"],
            "rel_gap_n5": r6["headline_finest_q1"]["rel_gap"],
            "prob_peak_layers": r6["headline_finest_q1"]["prob_peak_layers"],
            "density_peak_layers": r6["headline_finest_q1"]["density_peak_layers"],
            "pinched_throat_layers": r6["pinched_throat_layers"],
            "thickest_volume_layers": r6["thickest_volume_layers"],
            "single_prob_peak": r6["headline_finest_q1"]["single_prob_peak"],
            "single_density_peak": r6["headline_finest_q1"]["single_density_peak"],
            "margulis_throat_is_z5_charged": (
                r6["margulis_geodesic_check"]
                .get("cover_5cusp_lift", {})
                .get("shortest_throat_is_z5_charged", None)
                if r6["margulis_geodesic_check"].get("cover_5cusp_lift")
                else None
            ),
        },
        "bounded_family_A6_3d_summary": {
            "tested_unique_words": a6_enum["tested_unique_words"],
            "bundle_extending_count": a6_enum["extending_count"],
            "nondegenerate_ground_eigenvalue_count": nondeg_e0_count,
            "single_prob_peak_count": single_prob_count,
            "single_density_peak_count": single_dens_count,
            "sorted_by_volume": a6_results,
        },
    }


if __name__ == "__main__":
    import json

    out = run_gate1()
    print(json.dumps(out["run6_3d_verdict"], indent=2))
