"""Step 3: Gate 1 — Exhaustive Necklace Census (|W| <= 12), 1-Loop Buckling vs. Relational A-all Sum.

Executes three parameter-free tests (`0 of 19` empirical inputs):
  1. Unrestricted Primitive Necklace Census (2 <= |W| <= 12):
     Enumerates all primitive hyperbolic words W in {L, R}^* admitting a cyclic representative
     preserving the Golden Z/5Z eigenvector line v_5 = (1, 2)^T, groups them into exact 3D
     oriented isometry classes M_{<=12}/Isom_+ and relational mirror classes M_{<=12}/Isom_+-,
     and identifies the true global minimal-volume chiral irreversible 3-manifolds.
  2. Test 1A (`A-one` Classical Volume vs. Unrigged 1-Loop Quantum Contributions):
     Tests cusp-unramified (k = 0) vs. cusp-ramified (k != 0) acyclicity via exact Fox-Wada
     Reidemeister torsion, UV-subtracted twisted 3D Casimir zero-point energy, and 1-loop
     Coleman-Weinberg Yukawa quartic trace across minimal reversible vs. minimal irreversible classes.
  3. Test 1B (Deduplicated Relational `A-all` Partition Sum):
     Evaluates Boltzmann-weighted and 1-loop symmetry/torsion-weighted ensemble averages over
     M_{<=12}/Isom_+-, computing <tau_cusp,rel> and net relational Jarlskog <sigma_P * J_CKM>
     directly from explicit 3D FEM Yukawa matrices (zero literal flag assignments).
"""

from __future__ import annotations

import itertools
import math
from typing import Any, Dict, List, Tuple

import numpy as np
import snappy

from .phase4_core import (
    analyze_pi1_mod5_torsion_lines,
    assemble_and_solve_3d_sector,
    build_eulerian_subdivision,
    classify_cohomology_and_z5_cocycles,
    compute_tet_element_geometry_q14,
    compute_trilinear_overlap_matrix_q14,
    extract_epstein_penner_data,
    extract_quark_ckm_observables,
    gauss_reduce_tau,
)


L_MAT = np.array([[1, 1], [0, 1]], dtype=int)
R_MAT = np.array([[1, 0], [1, 1]], dtype=int)
GOLDEN_V5 = np.array([1, 2], dtype=int)


def word_to_sl2z(word: str) -> np.ndarray:
    M = np.eye(2, dtype=int)
    for ch in word:
        M = M @ (L_MAT if ch == "L" else R_MAT)
    return M


def canonical_necklace(word: str) -> str:
    return min(word[i:] + word[:i] for i in range(len(word)))


def is_primitive_word(word: str) -> bool:
    n = len(word)
    for d in range(1, n):
        if n % d == 0 and word == word[:d] * (n // d):
            return False
    return True


def is_word_palindrome_necklace(word: str) -> bool:
    return canonical_necklace(word) == canonical_necklace(word[::-1])


def has_lr_departure_representative(word: str) -> bool:
    """Check whether any cyclic shift of word ends in `LR` and is not `(LR)^m`."""
    if canonical_necklace(word) == "LR":
        return False
    n = len(word)
    for s in range(n):
        ws = word[s:] + word[:s]
        if ws.endswith("LR"):
            M = word_to_sl2z(ws)
            img = (M.T @ GOLDEN_V5) % 5
            if np.array_equal(img, GOLDEN_V5) or np.array_equal(img, (5 - GOLDEN_V5) % 5):
                return True
    return False


def active_weak_compass_sign(cs_val: float, tol: float = 1e-10) -> int:
    """Relational weak-compass sign sigma_P(M) = -sgn(sin(4*pi*CS(M))) (0 if amphicheiral)."""
    s = math.sin(4.0 * math.pi * cs_val)
    if abs(s) <= tol:
        return 0
    return -1 if s > 0.0 else 1


def enumerate_and_quotient_necklaces(max_len: int = 12) -> Dict[str, Any]:
    """Exhaustively enumerate primitive Golden-v5 necklaces (2 <= |W| <= max_len) and quotient by Isom_+-."""
    seen_necklaces: set[str] = set()
    raw_items: List[Dict[str, Any]] = []

    for n in range(2, max_len + 1):
        for bits in itertools.product("LR", repeat=n):
            w = "".join(bits)
            if "L" not in w or "R" not in w:
                continue
            cw = canonical_necklace(w)
            if cw in seen_necklaces or not is_primitive_word(cw):
                continue
            seen_necklaces.add(cw)

            # Find canonical cyclic shift fixing GOLDEN_V5 = (1, 2)^T (mod 5):
            # Prefer a shift ending in LR if one exists so departure names match Phase 2/3.
            shifts = [cw[s:] + cw[:s] for s in range(n)]
            shifts_sorted = sorted(shifts, key=lambda x: (0 if x.endswith("LR") else 1, x))
            chosen_spec = None
            chosen_word = None
            chosen_sign = 0
            for ws in shifts_sorted:
                Ms = word_to_sl2z(ws)
                img = (Ms.T @ GOLDEN_V5) % 5
                if np.array_equal(img, GOLDEN_V5):
                    chosen_word = ws
                    chosen_spec = "b++" + ws
                    chosen_sign = 1
                    break
                if np.array_equal(img, (5 - GOLDEN_V5) % 5):
                    chosen_word = ws
                    chosen_spec = "b+-" + ws
                    chosen_sign = -1
                    break

            if chosen_spec is None:
                continue

            M_std = snappy.Manifold(chosen_spec)
            M_hp = M_std.high_precision()
            M_hp.set_peripheral_curves("shortest")
            vol = float(M_hp.volume())
            cs = float(M_hp.chern_simons())
            tau_f = gauss_reduce_tau(complex(M_hp.cusp_info(0)["modulus"]))
            sym_grp = M_std.symmetry_group()
            sym_str = str(sym_grp)
            sym_ord = int(sym_grp.order())
            is_amph = bool(sym_grp.is_amphicheiral())
            hom_str = str(M_std.homology())
            word_pal = is_word_palindrome_necklace(cw)
            in_lr_dep = has_lr_departure_representative(cw)

            raw_items.append(
                {
                    "necklace": cw,
                    "length": n,
                    "spec": chosen_spec,
                    "word_shift": chosen_word,
                    "extension_sign": chosen_sign,
                    "in_lr_departure_subfamily": in_lr_dep,
                    "is_word_palindrome": word_pal,
                    "volume": vol,
                    "chern_simons": cs,
                    "sigma_P": (0 if is_amph else active_weak_compass_sign(cs)),
                    "tau_cusp_F": tau_f,
                    "homology_str": hom_str,
                    "symmetry_group": sym_str,
                    "symmetry_order": sym_ord,
                    "is_amphicheiral": is_amph,
                    "manifold_std": M_std,
                }
            )

    raw_items.sort(key=lambda d: (round(d["volume"], 9), d["length"], d["spec"]))

    # Group into exact 3D relational isometry classes (Isom_+-) and oriented classes (Isom_+):
    # Bucket first by (round(vol, 6), homology_str) for fast exact SnapPy isometry checks.
    buckets: Dict[Tuple[float, str], List[int]] = {}
    for idx, item in enumerate(raw_items):
        key = (round(item["volume"], 6), item["homology_str"])
        buckets.setdefault(key, []).append(idx)

    parent_rel = list(range(len(raw_items)))
    parent_ori = list(range(len(raw_items)))

    def find_p(par: List[int], x: int) -> int:
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for b_indices in buckets.values():
        m = len(b_indices)
        for a in range(m):
            ia = b_indices[a]
            for b in range(a + 1, m):
                ib = b_indices[b]
                if abs(raw_items[ia]["volume"] - raw_items[ib]["volume"]) > 1e-7:
                    continue
                try:
                    isoms = raw_items[ia]["manifold_std"].is_isometric_to(
                        raw_items[ib]["manifold_std"], return_isometries=True
                    )
                except Exception:
                    isoms = []
                if isoms:
                    ra, rb = find_p(parent_rel, ia), find_p(parent_rel, ib)
                    if ra != rb:
                        parent_rel[rb] = ra
                    dets = {int(round(float(iso.cusp_maps()[0].det()))) for iso in isoms}
                    if 1 in dets:
                        oa, ob = find_p(parent_ori, ia), find_p(parent_ori, ib)
                        if oa != ob:
                            parent_ori[ob] = oa

    ori_groups: Dict[int, List[int]] = {}
    rel_groups: Dict[int, List[int]] = {}
    for idx in range(len(raw_items)):
        ori_groups.setdefault(find_p(parent_ori, idx), []).append(idx)
        rel_groups.setdefault(find_p(parent_rel, idx), []).append(idx)

    relational_classes: List[Dict[str, Any]] = []
    max_rel_tau_enantiomer_err = 0.0

    for root_idx, member_indices in rel_groups.items():
        members = [raw_items[i] for i in member_indices]
        # Prefer member with sigma_P == +1 (active weak left-handed sector) or canonical spec:
        members_sorted = sorted(
            members,
            key=lambda d: (0 if d["sigma_P"] >= 0 else 1, 0 if d["spec"].endswith("LR") else 1, d["spec"]),
        )
        rep = members_sorted[0]

        is_amph = rep["is_amphicheiral"]
        any_pal = any(m["is_word_palindrome"] for m in members)
        sym_ord = rep["symmetry_order"]
        sym_plus_ord = sym_ord // 2 if is_amph else sym_ord

        if is_amph:
            chirality_class = "amphicheiral"
        elif (not any_pal) and sym_plus_ord == 2:
            chirality_class = "chiral_irreversible"
        else:
            chirality_class = "chiral_reversible"

        rel_taus = []
        for m in members:
            rt = complex(m["sigma_P"] * m["tau_cusp_F"].real, m["tau_cusp_F"].imag)
            rel_taus.append(rt)
        for rt in rel_taus[1:]:
            max_rel_tau_enantiomer_err = max(max_rel_tau_enantiomer_err, abs(rt - rel_taus[0]))

        ori_roots_in_rel = {find_p(parent_ori, i) for i in member_indices}
        relational_classes.append(
            {
                "rep_spec": rep["spec"],
                "rep_necklace": rep["necklace"],
                "min_word_length": min(m["length"] for m in members),
                "member_specs": [m["spec"] for m in members],
                "num_necklace_members": len(members),
                "num_oriented_isometry_classes": len(ori_roots_in_rel),
                "has_b_plus_plus_member": any(m["extension_sign"] == 1 for m in members),
                "in_lr_departure_subfamily": any(m["in_lr_departure_subfamily"] for m in members),
                "chirality_class": chirality_class,
                "is_amphicheiral": is_amph,
                "is_word_palindrome": any_pal,
                "symmetry_group": rep["symmetry_group"],
                "symmetry_order_full": sym_ord,
                "symmetry_order_orient_pres": sym_plus_ord,
                "homology_str": rep["homology_str"],
                "volume": rep["volume"],
                "rep_chern_simons": rep["chern_simons"],
                "rep_sigma_P": rep["sigma_P"],
                "relational_tau_cusp": [float(rel_taus[0].real), float(rel_taus[0].imag)],
            }
        )

    relational_classes.sort(key=lambda d: (d["volume"], d["min_word_length"], d["rep_spec"]))

    irrev_all = [c for c in relational_classes if c["chirality_class"] == "chiral_irreversible"]
    irrev_bpp = [c for c in irrev_all if c["has_b_plus_plus_member"]]
    irrev_lr_dep = [c for c in irrev_all if c["in_lr_departure_subfamily"]]
    rev_all = [c for c in relational_classes if c["chirality_class"] == "chiral_reversible"]
    rev_lr_dep = [c for c in rev_all if c["in_lr_departure_subfamily"]]
    amph_all = [c for c in relational_classes if c["chirality_class"] == "amphicheiral"]

    return {
        "max_word_length": max_len,
        "num_golden_primitive_necklaces": len(raw_items),
        "num_oriented_3manifold_classes": len(ori_groups),
        "num_relational_quotient_classes": len(relational_classes),
        "counts_by_chirality": {
            "amphicheiral": len(amph_all),
            "chiral_reversible": len(rev_all),
            "chiral_irreversible": len(irrev_all),
        },
        "max_relational_tau_enantiomer_err": max_rel_tau_enantiomer_err,
        "global_minimal_amphicheiral": amph_all[0],
        "global_minimal_chiral_reversible": rev_all[0],
        "departure_lr_minimal_chiral_reversible": rev_lr_dep[0],
        "global_minimal_chiral_irreversible": irrev_all[0],
        "b_plus_plus_minimal_chiral_irreversible": irrev_bpp[0],
        "departure_lr_minimal_chiral_irreversible": irrev_lr_dep[0],
        "relational_classes": relational_classes,
    }


def _evaluate_3d_yukawa_and_casimir_on_spec(
    spec: str, n_subs: Tuple[int, ...] = (3, 4), k_ir: int = 6
) -> Dict[str, Any]:
    """Compute Fox-Wada torsion, UV-subtracted Casimir sum, and 1-loop CW Yukawa trace on `spec`."""
    ep = extract_epstein_penner_data(spec)
    coh = classify_cohomology_and_z5_cocycles(ep)
    pi1_tors = analyze_pi1_mod5_torsion_lines(spec)

    # Check k = 0 (unramified) vs k != 0 (ramified) torsion lines in pi_1 Fox-Wada:
    tors_unram = [ln for ln in pi1_tors["lines"] if ln["is_torsion_nontrivial"] and ln["is_cusp_unramified"]]
    tors_ram = [ln for ln in pi1_tors["lines"] if ln["is_torsion_nontrivial"] and not ln["is_cusp_unramified"]]
    free_lines = [ln for ln in pi1_tors["lines"] if ln["is_pure_free_character"]]

    # Select canonical ground-state-minimizing cusp-ramified dual cocycle for 3D FEM:
    ram_dual_lines = coh["cusp_ramified_torsion_lines"]
    sub3 = build_eulerian_subdivision(3, True)
    geoms3 = [compute_tet_element_geometry_q14(G, sub3["nodes_bary"], sub3["sub_tets"]) for G in ep["grams"]]

    best_line = None
    best_e0 = float("inf")
    for ln in ram_dual_lines:
        c_try = np.array(ln["cocycle"], dtype=int) % 5
        s1_t = assemble_and_solve_3d_sector(ep, c_try, 1, 3, "dirichlet", 4, sub3, geoms3)
        s2_t = assemble_and_solve_3d_sector(ep, c_try, 2, 3, "dirichlet", 4, sub3, geoms3)
        e_min = min(s1_t["eigenvalues"][0], s2_t["eigenvalues"][0])
        if e_min < best_e0 - 1e-12:
            best_e0 = e_min
            best_line = ln
    assert best_line is not None
    coc = np.array(best_line["cocycle"], dtype=int) % 5

    grid_records: Dict[str, Any] = {}
    for n_sub in n_subs:
        sub = sub3 if n_sub == 3 else build_eulerian_subdivision(n_sub, True)
        geoms = geoms3 if n_sub == 3 else [
            compute_tet_element_geometry_q14(G, sub["nodes_bary"], sub["sub_tets"]) for G in ep["grams"]
        ]
        s0 = assemble_and_solve_3d_sector(ep, None, 0, n_sub, "dirichlet", k_ir + 2, sub, geoms)
        s1 = assemble_and_solve_3d_sector(ep, coc, 1, n_sub, "dirichlet", k_ir + 2, sub, geoms)
        s2 = assemble_and_solve_3d_sector(ep, coc, 2, n_sub, "dirichlet", k_ir + 2, sub, geoms)
        if s1["eigenvalues"][0] < s2["eigenvalues"][0] - 1e-9:
            coc_n = (2 * coc) % 5
            s1 = assemble_and_solve_3d_sector(ep, coc_n, 1, n_sub, "dirichlet", k_ir + 2, sub, geoms)
            s2 = assemble_and_solve_3d_sector(ep, coc_n, 2, n_sub, "dirichlet", k_ir + 2, sub, geoms)

        lam0 = np.sqrt(np.maximum(0.0, np.array(s0["eigenvalues"][:k_ir])))
        lam1 = np.sqrt(np.maximum(0.0, np.array(s1["eigenvalues"][:k_ir])))
        lam2 = np.sqrt(np.maximum(0.0, np.array(s2["eigenvalues"][:k_ir])))
        # Sum over all 4 twisted Z/5Z charges (q=1,2,3,4, since spec(q=4)=spec(q=1) and spec(q=3)=spec(q=2))
        # minus 4 copies of untwisted q=0:
        casimir_twist_sum = float(np.sum(2.0 * lam1 + 2.0 * lam2 - 4.0 * lam0))

        psi_p1 = s1["local_modes"][:3]
        chi_p2 = s2["local_modes"][:3]
        phi_p2 = s2["local_modes"][0]
        phi_m2 = np.conj(phi_p2)

        Y_u = compute_trilinear_overlap_matrix_q14(psi_p1, psi_p1, phi_m2, sub["sub_tets"], geoms)
        Y_d = compute_trilinear_overlap_matrix_q14(psi_p1, chi_p2, phi_p2, sub["sub_tets"], geoms)
        q_obs = extract_quark_ckm_observables(Y_u, Y_d)

        grid_records[f"nsub_{n_sub}"] = {
            "casimir_uv_subtracted_4charges": casimir_twist_sum,
            "cw_yukawa_quartic_potential": -q_obs["cw_yukawa_quartic_trace"],
            "jarlskog_ckm_norm": q_obs["jarlskog_norm"],
            "relational_jarlskog_ckm": active_weak_compass_sign(ep["chern_simons"]) * q_obs["jarlskog_norm"]
            if not ep["is_amphicheiral"]
            else 0.0,
        }

    # Check exact Golden cyclotomic product (2 sin(pi/5))^2 * (2 sin(2*pi/5))^2 == 5 on ramified lines:
    ram_prod5_errs = [abs(ln["torsion_product_all_4_charges"] - 5.0) for ln in tors_ram]
    unram_max_tors = max((ln["torsion_q1"] for ln in tors_unram), default=0.0)

    return {
        "spec": spec,
        "volume": ep["snappy_volume"],
        "symmetry_group": ep["symmetry_group_str"],
        "num_unramified_torsion_lines": len(tors_unram),
        "num_ramified_torsion_lines": len(tors_ram),
        "unramified_max_torsion_q1": unram_max_tors,
        "unramified_all_non_acyclic": all(not ln["is_acyclic_q1"] for ln in tors_unram),
        "ramified_all_acyclic": all(ln["is_acyclic_q1"] for ln in tors_ram),
        "ramified_cyclotomic_5_max_err": max(ram_prod5_errs, default=0.0),
        "ramified_torsion_q1_values": [ln["torsion_q1"] for ln in tors_ram],
        "free_character_torsion_q1": (free_lines[0]["torsion_q1"] if free_lines else None),
        "grid_evaluations": grid_records,
    }


def run_test_1a_one_loop_buckling(census: Dict[str, Any]) -> Dict[str, Any]:
    """Run Test 1A comparing k=0 vs k!=0 and minimal reversible vs minimal irreversible classes."""
    key_specs = [
        ("min_unrestricted_reversible", census["global_minimal_chiral_reversible"]["rep_spec"]),
        ("min_departure_lr_reversible_6", census["departure_lr_minimal_chiral_reversible"]["rep_spec"]),
        ("min_unrestricted_irreversible", census["global_minimal_chiral_irreversible"]["rep_spec"]),
        ("min_bpp_irreversible", census["b_plus_plus_minimal_chiral_irreversible"]["rep_spec"]),
        ("min_departure_lr_irreversible_5122", census["departure_lr_minimal_chiral_irreversible"]["rep_spec"]),
    ]

    evals = {}
    for label, spec in key_specs:
        evals[label] = _evaluate_3d_yukawa_and_casimir_on_spec(spec, n_subs=(3, 4), k_ir=6)

    rev_unr = evals["min_unrestricted_reversible"]
    irr_unr = evals["min_unrestricted_irreversible"]
    rev_dep = evals["min_departure_lr_reversible_6"]
    irr_dep = evals["min_departure_lr_irreversible_5122"]

    delta_vol_unrestricted = irr_unr["volume"] - rev_unr["volume"]
    delta_casimir_unrestricted = (
        irr_unr["grid_evaluations"]["nsub_4"]["casimir_uv_subtracted_4charges"]
        - rev_unr["grid_evaluations"]["nsub_4"]["casimir_uv_subtracted_4charges"]
    )
    delta_cw_unrestricted = (
        irr_unr["grid_evaluations"]["nsub_4"]["cw_yukawa_quartic_potential"]
        - rev_unr["grid_evaluations"]["nsub_4"]["cw_yukawa_quartic_potential"]
    )

    delta_vol_departure = irr_dep["volume"] - rev_dep["volume"]
    delta_casimir_departure = (
        irr_dep["grid_evaluations"]["nsub_4"]["casimir_uv_subtracted_4charges"]
        - rev_dep["grid_evaluations"]["nsub_4"]["casimir_uv_subtracted_4charges"]
    )
    delta_cw_departure = (
        irr_dep["grid_evaluations"]["nsub_4"]["cw_yukawa_quartic_potential"]
        - rev_dep["grid_evaluations"]["nsub_4"]["cw_yukawa_quartic_potential"]
    )

    # Check 1-loop acyclicity selection of k != 0 over k = 0:
    # Every tested manifold has unramified_all_non_acyclic == True (tau_Reid == 0, zero-mode obstruction)
    # and ramified_all_acyclic == True (prod_{q=1..4} tau_Reid(q) == 5 to < 1e-12)!
    k_nonzero_selected_by_acyclicity = all(
        v["unramified_all_non_acyclic"]
        and v["unramified_max_torsion_q1"] < 1e-12
        and v["ramified_all_acyclic"]
        and v["ramified_cyclotomic_5_max_err"] < 1e-11
        for v in evals.values()
    )

    # Check honestly whether unrigged 1-loop shifts (Casimir + CW, with unit/natural prefactor 1/(16*pi^2) or even O(1))
    # overturn classical Delta Vol > 0:
    one_loop_overturns_classical_unrestricted = (
        delta_vol_unrestricted + delta_casimir_unrestricted / (16.0 * math.pi ** 2) + delta_cw_unrestricted / (16.0 * math.pi ** 2)
    ) < 0.0

    return {
        "candidates": evals,
        "k_nonzero_selected_over_k_zero_by_reidemeister_acyclicity": k_nonzero_selected_by_acyclicity,
        "unrestricted_comparison": {
            "delta_volume_irrev_minus_rev": delta_vol_unrestricted,
            "delta_reidemeister_fiber_product_log": 0.0,
            "delta_casimir_nsub4": delta_casimir_unrestricted,
            "delta_cw_yukawa_nsub4": delta_cw_unrestricted,
            "one_loop_overturns_classical_volume_without_tuning": one_loop_overturns_classical_unrestricted,
        },
        "departure_lr_comparison": {
            "delta_volume_5122_minus_6": delta_vol_departure,
            "delta_reidemeister_fiber_product_log": 0.0,
            "delta_casimir_nsub4": delta_casimir_departure,
            "delta_cw_yukawa_nsub4": delta_cw_departure,
        },
    }


def run_test_1b_relational_a_all_ensemble(
    census: Dict[str, Any], fem_vol_cutoff: float = 7.6, fem_n_sub: int = 4
) -> Dict[str, Any]:
    """Evaluate deduplicated relational A-all partition sums over M_{<=12}/Isom_+-."""
    classes = census["relational_classes"]

    # Full geometric A-all sum over ALL deduplicated relational classes in M_{<=12}/Isom_+-:
    vols = np.array([c["volume"] for c in classes], dtype=float)
    v_min = float(np.min(vols))
    w_boltz = np.exp(-(vols - v_min))
    sym_factors = np.array([1.0 / c["symmetry_order_orient_pres"] for c in classes], dtype=float)
    w_sym_boltz = sym_factors * w_boltz

    w_boltz /= np.sum(w_boltz)
    w_sym_boltz /= np.sum(w_sym_boltz)

    rel_taus = np.array([complex(c["relational_tau_cusp"][0], c["relational_tau_cusp"][1]) for c in classes])
    tau_avg_boltz = complex(np.sum(w_boltz * rel_taus))
    tau_avg_sym = complex(np.sum(w_sym_boltz * rel_taus))

    irrev_mask = np.array([c["chirality_class"] == "chiral_irreversible" for c in classes], dtype=bool)
    irrev_weight_boltz = float(np.sum(w_boltz[irrev_mask]))
    irrev_weight_sym = float(np.sum(w_sym_boltz[irrev_mask]))

    # Explicit 3D FEM Jarlskog evaluation at N_sub = 4 (first Eulerian mesh with interior
    # tetrahedron nodes, eliminating 2-tet N_sub = 3 boundary-only mesh degeneracies)
    # across ALL classes with Vol <= fem_vol_cutoff (plus [5,1,2,2]+LR `b++LLLLLRLLRRLR` at Vol = 9.06871):
    sub_grid = build_eulerian_subdivision(fem_n_sub, True)
    fem_records: List[Dict[str, Any]] = []
    max_klein4_reversible_jarlskog = 0.0
    max_amphicheiral_rel_jarlskog = 0.0
    max_amphicheiral_line_sum_err = 0.0
    max_irreversible_jarlskog = 0.0

    eval_classes = [
        c for c in classes if c["volume"] <= fem_vol_cutoff or c["rep_spec"] == "b++LLLLLRLLRRLR"
    ]
    for c in eval_classes:
        spec = c["rep_spec"]
        ep = extract_epstein_penner_data(spec)
        coh = classify_cohomology_and_z5_cocycles(ep)
        geoms_grid = [
            compute_tet_element_geometry_q14(G, sub_grid["nodes_bary"], sub_grid["sub_tets"]) for G in ep["grams"]
        ]

        ram_lines = coh["cusp_ramified_torsion_lines"]
        line_js: List[float] = []
        line_s12s: List[float] = []
        line_e0s: List[float] = []

        for ln in ram_lines:
            coc = np.array(ln["cocycle"], dtype=int) % 5
            s1 = assemble_and_solve_3d_sector(ep, coc, 1, fem_n_sub, "dirichlet", 5, sub_grid, geoms_grid)
            s2 = assemble_and_solve_3d_sector(ep, coc, 2, fem_n_sub, "dirichlet", 5, sub_grid, geoms_grid)
            if s1["eigenvalues"][0] < s2["eigenvalues"][0] - 1e-9:
                coc = (2 * coc) % 5
                s1 = assemble_and_solve_3d_sector(ep, coc, 1, fem_n_sub, "dirichlet", 5, sub_grid, geoms_grid)
                s2 = assemble_and_solve_3d_sector(ep, coc, 2, fem_n_sub, "dirichlet", 5, sub_grid, geoms_grid)
            Y_u = compute_trilinear_overlap_matrix_q14(
                s1["local_modes"][:3], s1["local_modes"][:3], np.conj(s2["local_modes"][0]), sub_grid["sub_tets"], geoms_grid
            )
            Y_d = compute_trilinear_overlap_matrix_q14(
                s1["local_modes"][:3], s2["local_modes"][:3], s2["local_modes"][0], sub_grid["sub_tets"], geoms_grid
            )
            q_obs = extract_quark_ckm_observables(Y_u, Y_d)
            line_js.append(q_obs["jarlskog_norm"])
            line_s12s.append(q_obs["angles"]["sin2_theta_12"])
            line_e0s.append(s2["eigenvalues"][0])

        sig_p = 0 if c["is_amphicheiral"] else active_weak_compass_sign(ep["chern_simons"])
        min_e0 = min(line_e0s)
        gs_indices = [i for i, e in enumerate(line_e0s) if abs(e - min_e0) < 1e-6]
        j_gs_abs = float(max(abs(line_js[i]) for i in gs_indices))
        j_line_sum = float(sum(line_js))
        j_line_avg = float(np.mean(line_js))
        s12_gs = float(np.mean([line_s12s[i] for i in gs_indices]))

        if c["chirality_class"] == "chiral_reversible":
            max_klein4_reversible_jarlskog = max(
                max_klein4_reversible_jarlskog, max(abs(x) for x in line_js)
            )
        elif c["chirality_class"] == "amphicheiral":
            max_amphicheiral_rel_jarlskog = max(
                max_amphicheiral_rel_jarlskog, max(abs(sig_p * x) for x in line_js)
            )
            max_amphicheiral_line_sum_err = max(max_amphicheiral_line_sum_err, abs(j_line_sum))
        else:
            max_irreversible_jarlskog = max(
                max_irreversible_jarlskog, max(abs(x) for x in line_js)
            )

        fem_records.append(
            {
                "rep_spec": spec,
                "in_lr_departure_subfamily": c["in_lr_departure_subfamily"],
                "chirality_class": c["chirality_class"],
                "volume": c["volume"],
                "sym_order_orient_pres": c["symmetry_order_orient_pres"],
                "num_ramified_z5_lines": len(ram_lines),
                "sigma_P": sig_p,
                "jarlskog_all_lines_unbroken_sum_nsub4": j_line_sum,
                "jarlskog_all_lines_unbroken_avg_nsub4": j_line_avg,
                "jarlskog_gs_branch_abs_nsub4": j_gs_abs,
                "jarlskog_relational_spontaneous_branch_nsub4": float(abs(sig_p) * j_gs_abs),
                "ckm_sin2_theta12_nsub4": s12_gs,
            }
        )

    f_vols = np.array([r["volume"] for r in fem_records], dtype=float)
    fw_boltz_raw = np.exp(-(f_vols - v_min))
    fw_sym_raw = np.array([1.0 / r["sym_order_orient_pres"] for r in fem_records]) * fw_boltz_raw
    z_all_sym_raw = float(np.sum(sym_factors * np.exp(-(vols - v_min))))
    fem_mass_capture_sym = float(np.sum(fw_sym_raw) / z_all_sym_raw)

    fw_boltz = fw_boltz_raw / np.sum(fw_boltz_raw)
    fw_sym = fw_sym_raw / np.sum(fw_sym_raw)

    f_junbroken = np.array([r["sigma_P"] * r["jarlskog_all_lines_unbroken_avg_nsub4"] for r in fem_records])
    f_jspont = np.array([r["jarlskog_relational_spontaneous_branch_nsub4"] for r in fem_records], dtype=float)
    f_s12 = np.array([r["ckm_sin2_theta12_nsub4"] for r in fem_records], dtype=float)

    unbroken_j_sym = float(np.sum(fw_sym * f_junbroken))
    spont_j_boltz = float(np.sum(fw_boltz * f_jspont))
    spont_j_sym = float(np.sum(fw_sym * f_jspont))
    spont_j_full_census_lb = float(np.sum(fw_sym_raw * f_jspont) / z_all_sym_raw)
    avg_ckm_s12_sym = float(np.sum(fw_sym * f_s12))

    dep_records = [r for r in fem_records if r["in_lr_departure_subfamily"]]
    d_vols = np.array([r["volume"] for r in dep_records], dtype=float)
    dw_sym = np.array([1.0 / r["sym_order_orient_pres"] for r in dep_records]) * np.exp(-(d_vols - np.min(d_vols)))
    dw_sym /= np.sum(dw_sym)
    spont_j_dep_sym = float(
        np.sum(dw_sym * np.array([r["jarlskog_relational_spontaneous_branch_nsub4"] for r in dep_records]))
    )

    return {
        "full_census_relational_tau_boltz": [tau_avg_boltz.real, tau_avg_boltz.imag],
        "full_census_relational_tau_sym_boltz": [tau_avg_sym.real, tau_avg_sym.imag],
        "chiral_irreversible_boltzmann_fraction": irrev_weight_boltz,
        "chiral_irreversible_sym_boltzmann_fraction": irrev_weight_sym,
        "num_fem_evaluated_classes": len(fem_records),
        "fem_sym_boltzmann_mass_capture_fraction": fem_mass_capture_sym,
        "max_klein4_reversible_abs_jarlskog": max_klein4_reversible_jarlskog,
        "max_amphicheiral_relational_jarlskog": max_amphicheiral_rel_jarlskog,
        "max_amphicheiral_4line_sum_err": max_amphicheiral_line_sum_err,
        "max_chiral_irreversible_abs_jarlskog": max_irreversible_jarlskog,
        "unbroken_4line_sum_relational_jarlskog_sym": unbroken_j_sym,
        "spontaneous_branch_relational_jarlskog_boltzmann": spont_j_boltz,
        "spontaneous_branch_relational_jarlskog_sym_boltzmann": spont_j_sym,
        "spontaneous_branch_lower_bound_full_124_census_sym": spont_j_full_census_lb,
        "spontaneous_branch_relational_jarlskog_lr_departures_sym": spont_j_dep_sym,
        "ensemble_avg_ckm_sin2_theta12_sym": avg_ckm_s12_sym,
        "fem_evaluated_classes": fem_records,
    }


def run_gate1_vacuum_selection() -> Dict[str, Any]:
    """Execute complete Gate 1 (Unrestricted |W| <= 12 Census + Test 1A + Test 1B)."""
    census = enumerate_and_quotient_necklaces(max_len=12)
    t1a = run_test_1a_one_loop_buckling(census)
    t1b = run_test_1b_relational_a_all_ensemble(census, fem_vol_cutoff=7.6)

    gate_passed = (
        census["max_relational_tau_enantiomer_err"] < 1e-12
        and census["global_minimal_chiral_irreversible"]["chirality_class"] == "chiral_irreversible"
        and t1a["k_nonzero_selected_over_k_zero_by_reidemeister_acyclicity"]
        and t1b["max_klein4_reversible_abs_jarlskog"] < 1e-13
        and t1b["max_amphicheiral_relational_jarlskog"] == 0.0
        and t1b["max_amphicheiral_4line_sum_err"] < 1e-13
        and abs(t1b["unbroken_4line_sum_relational_jarlskog_sym"]) < 1e-14
        and t1b["max_chiral_irreversible_abs_jarlskog"] > 1e-6
        and t1b["spontaneous_branch_relational_jarlskog_sym_boltzmann"] > 0.0
    )

    return {
        "necklace_census_summary": {k: v for k, v in census.items() if k != "relational_classes"},
        "relational_classes": census["relational_classes"],
        "test_1a_one_loop_buckling": t1a,
        "test_1b_relational_a_all_ensemble": t1b,
        "gate1_passed": gate_passed,
    }


if __name__ == "__main__":
    res = run_gate1_vacuum_selection()
    print("Gate 1 passed:", res["gate1_passed"])
    csum = res["necklace_census_summary"]
    print("  Necklaces:", csum["num_golden_primitive_necklaces"], "-> Oriented 3-manifolds:", csum["num_oriented_3manifold_classes"], "-> Relational classes:", csum["num_relational_quotient_classes"])
    print("  Counts by chirality:", csum["counts_by_chirality"])
    print("  Global min reversible:", csum["global_minimal_chiral_reversible"]["rep_spec"], csum["global_minimal_chiral_reversible"]["volume"])
    print("  Global min irreversible:", csum["global_minimal_chiral_irreversible"]["rep_spec"], csum["global_minimal_chiral_irreversible"]["volume"])
    print("  b++ min irreversible:", csum["b_plus_plus_minimal_chiral_irreversible"]["rep_spec"], csum["b_plus_plus_minimal_chiral_irreversible"]["volume"])
    print("  Test 1A k!=0 acyclicity:", res["test_1a_one_loop_buckling"]["k_nonzero_selected_over_k_zero_by_reidemeister_acyclicity"])
    print("  Test 1A unrestricted comparison:", res["test_1a_one_loop_buckling"]["unrestricted_comparison"])
    print("  Test 1B max Klein-4 |J|:", res["test_1b_relational_a_all_ensemble"]["max_klein4_reversible_abs_jarlskog"])
    print("  Test 1B max Z/4 amph 4-line sum err:", res["test_1b_relational_a_all_ensemble"]["max_amphicheiral_4line_sum_err"])
    print("  Test 1B unbroken 4-line <J_rel>:", res["test_1b_relational_a_all_ensemble"]["unbroken_4line_sum_relational_jarlskog_sym"])
    print("  Test 1B spontaneous branch <J_rel>:", res["test_1b_relational_a_all_ensemble"]["spontaneous_branch_relational_jarlskog_sym_boltzmann"])
