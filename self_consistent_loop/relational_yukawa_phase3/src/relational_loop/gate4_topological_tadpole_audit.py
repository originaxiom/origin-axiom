"""Step 6: Gate 4 — Unrigged Topological Tadpole & E_8 Flux Quantization Audit.

1. Builds all 240 explicit roots of Phi(E_8) and canonically decomposes
     E_8 -> su(5)_GUT (+) su(5)_perp (+) (10, 5) (+) (10bar, 5bar) (+) (5, 10bar) (+) (5bar, 10)
   purely by root-addition graph components (zero hand-picked slot signs).
2. Exhaustively enumerates ALL su(5)_GUT-commuting coroots H in Lambda_R(E_8) with
   ||H||^2 <= 32 (k_inst <= 16), verifying to < 1e-13 that
     k_inst(H) := (1/120) sum_{alpha in Phi(E_8)} <alpha, H>^2 == (1/2) ||H||^2
   and determining the exact minimal instanton thresholds k_{inst,min}(N) for
   N in {1, 2, 3, 4} chiral families in a Z/5Z-projected 5_perp slot.
3. Audits three unrigged topological quantization candidates (zero adjustable multipliers):
   - Rule T1: 2D punctured-torus fiber Euler characteristic |chi(Sigma_{1,1})| = 1,
   - Rule T2: 3D Rademacher-Dedekind monodromy framing defect |Phi_Dedekind(M_W)| = |#L - #R|
     (cross-checked via Rademacher's exact Dedekind-sum formula on SL(2, Z)),
   - Rule T3: 4D rational-elliptic surface (dP_9 = 1/2 K3) cusp-cap Bianchi identity
     k_vis + k_hid = chi(dP_9) = 12 (symmetric E_8 x E_8 split 6 + 6 = 12).
"""

from __future__ import annotations

import itertools
import math
from typing import Any, Dict, List, Tuple

import numpy as np

from .gate1_relational_quotient import check_golden_bundle_extension, word_to_sl2z


def build_e8_root_system_and_su5_bifundamentals() -> Dict[str, Any]:
    """Construct all 240 E_8 roots and extract the 5 weight slots of (10_GUT, 5_perp) intrinsically."""
    roots: List[np.ndarray] = []

    # 112 integer roots: permutations of (+-1, +-1, 0^6)
    for i in range(8):
        for j in range(i + 1, 8):
            for s1 in (-1.0, 1.0):
                for s2 in (-1.0, 1.0):
                    v = np.zeros(8, dtype=float)
                    v[i] = s1
                    v[j] = s2
                    roots.append(v)

    # 128 half-integer even-spinor roots: (+-1/2)^8 with even number of minus signs
    for signs in itertools.product((-0.5, 0.5), repeat=8):
        if sum(1 for x in signs if x < 0) % 2 == 0:
            roots.append(np.array(signs, dtype=float))

    R_all = np.array(roots, dtype=float)
    assert R_all.shape == (240, 8)
    assert np.allclose(np.sum(R_all ** 2, axis=1), 2.0)

    # su(5)_GUT roots: supported on 0..4 with sum == 0 (20 roots: e_i - e_j)
    is_su5_gut = np.array(
        [
            np.all(np.abs(r[5:]) < 1e-12) and abs(np.sum(r[:5])) < 1e-12
            for r in R_all
        ],
        dtype=bool,
    )
    R_gut = R_all[is_su5_gut]
    assert R_gut.shape[0] == 20

    # su(5)_perp roots: orthogonal to all su(5)_GUT roots (first 5 coords all equal)
    is_su5_perp = np.array(
        [np.max(np.abs(r[:5] - r[0])) < 1e-12 for r in R_all],
        dtype=bool,
    )
    R_perp = R_all[is_su5_perp]
    assert R_perp.shape[0] == 20

    # Remaining 200 roots decompose into 4 connected components of size 50 under root addition by R_gut U R_perp!
    rem_indices = [idx for idx in range(240) if not is_su5_gut[idx] and not is_su5_perp[idx]]
    assert len(rem_indices) == 200

    key_to_rem = {tuple(int(round(2.0 * x)) for x in R_all[idx]): idx for idx in rem_indices}
    shifts = np.vstack([R_gut, R_perp])

    visited: set[int] = set()
    components: List[List[int]] = []
    for start in rem_indices:
        if start in visited:
            continue
        comp = []
        queue = [start]
        visited.add(start)
        while queue:
            cur = queue.pop()
            comp.append(cur)
            rc = R_all[cur]
            for sh in shifts:
                cand_k = tuple(int(round(2.0 * x)) for x in (rc + sh))
                if cand_k in key_to_rem:
                    nb = key_to_rem[cand_k]
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
                cand_m = tuple(int(round(2.0 * x)) for x in (rc - sh))
                if cand_m in key_to_rem:
                    nb = key_to_rem[cand_m]
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
        components.append(comp)

    assert sorted(len(c) for c in components) == [50, 50, 50, 50]

    # Identify (10_GUT, 5_perp): a component has 10 distinct traceless su(5)_GUT projections
    # and 5 distinct su(5)_perp projections! (Whereas (5, 10bar) has 5 GUT projections and 10 perp projections.)
    ten_five_comps: List[np.ndarray] = []
    for comp in components:
        rc = R_all[comp]
        # Project onto su(5)_perp subspace (replace first 5 coords by their mean)
        perp_proj = np.column_stack([np.full((50, 5), np.mean(rc[:, :5], axis=1)[:, None]), rc[:, 5:]])
        uniq_perp = np.unique(np.round(perp_proj, 8), axis=0)
        if uniq_perp.shape[0] == 5:
            ten_five_comps.append(uniq_perp)

    assert len(ten_five_comps) == 2  # (10, 5) and (10bar, 5bar)
    # Pick canonical (10_GUT, 5_perp) (contains spinor weight (-0.1^5, 0.5, 0.5, 0.5) or its negative; both give identical |slot_charge|)
    five_perp_weights = ten_five_comps[0]
    weight_sum_err = float(np.max(np.abs(np.sum(five_perp_weights, axis=0))))

    return {
        "roots_240": R_all,
        "su5_gut_roots": R_gut,
        "su5_perp_roots": R_perp,
        "five_perp_slot_weights": five_perp_weights,
        "five_perp_weight_sum_err": weight_sum_err,
    }


def enumerate_su5_commuting_e8_coroots(
    e8_data: Dict[str, Any], max_norm2: int = 32
) -> Dict[str, Any]:
    """Exhaustively enumerate all H = (a^5, b1, b2, b3) in Lambda_R(E_8) with 0 < ||H||^2 <= max_norm2."""
    R_all = e8_data["roots_240"]
    slot_w = e8_data["five_perp_slot_weights"]  # (5, 8)

    coroots: List[Dict[str, Any]] = []
    max_instanton_identity_err = 0.0
    max_slot_sum_err = 0.0

    # 1. Integer branch: a, b1, b2, b3 in Z with (5a + b1 + b2 + b3) even
    a_max_int = int(math.floor(math.sqrt(max_norm2 / 5.0)))
    for a in range(-a_max_int, a_max_int + 1):
        rem = max_norm2 - 5 * a * a
        b_lim = int(math.floor(math.sqrt(max(0, rem))))
        for b1 in range(-b_lim, b_lim + 1):
            for b2 in range(-b_lim, b_lim + 1):
                for b3 in range(-b_lim, b_lim + 1):
                    n2 = 5 * a * a + b1 * b1 + b2 * b2 + b3 * b3
                    if n2 == 0 or n2 > max_norm2:
                        continue
                    if (5 * a + b1 + b2 + b3) % 2 != 0:
                        continue
                    H = np.array([a, a, a, a, a, b1, b2, b3], dtype=float)
                    k_sum = float(np.sum((R_all @ H) ** 2)) / 120.0
                    k_exact = n2 // 2
                    max_instanton_identity_err = max(max_instanton_identity_err, abs(k_sum - k_exact))
                    slots = [int(round(float(w @ H))) for w in slot_w]
                    max_slot_sum_err = max(max_slot_sum_err, abs(sum(slots)))
                    coroots.append(
                        {
                            "H": H.tolist(),
                            "norm2": int(n2),
                            "k_inst": int(k_exact),
                            "slot_indices": slots,
                            "max_abs_slot_ngen": max(abs(x) for x in slots),
                        }
                    )

    # 2. Half-integer branch: a = m + 0.5, b_k = n_k + 0.5 with (5a + b1 + b2 + b3) even integer
    m_lim = int(math.ceil(math.sqrt(max_norm2 / 5.0))) + 1
    for ma in range(-m_lim, m_lim + 1):
        a = ma + 0.5
        if 5.0 * a * a > max_norm2 + 1e-9:
            continue
        rem = max_norm2 - 5.0 * a * a
        nb_lim = int(math.ceil(math.sqrt(max(0.0, rem)))) + 1
        for nb1 in range(-nb_lim, nb_lim + 1):
            b1 = nb1 + 0.5
            for nb2 in range(-nb_lim, nb_lim + 1):
                b2 = nb2 + 0.5
                for nb3 in range(-nb_lim, nb_lim + 1):
                    b3 = nb3 + 0.5
                    n2_f = 5.0 * a * a + b1 * b1 + b2 * b2 + b3 * b3
                    n2 = int(round(n2_f))
                    if n2 == 0 or n2 > max_norm2:
                        continue
                    tot_sum = int(round(5.0 * a + b1 + b2 + b3))
                    if tot_sum % 2 != 0:
                        continue
                    H = np.array([a, a, a, a, a, b1, b2, b3], dtype=float)
                    k_sum = float(np.sum((R_all @ H) ** 2)) / 120.0
                    k_exact = n2 // 2
                    max_instanton_identity_err = max(max_instanton_identity_err, abs(k_sum - k_exact))
                    slots = [int(round(float(w @ H))) for w in slot_w]
                    max_slot_sum_err = max(max_slot_sum_err, abs(sum(slots)))
                    coroots.append(
                        {
                            "H": H.tolist(),
                            "norm2": int(n2),
                            "k_inst": int(k_exact),
                            "slot_indices": slots,
                            "max_abs_slot_ngen": max(abs(x) for x in slots),
                        }
                    )

    thresholds: Dict[str, Any] = {}
    for n_fam in (1, 2, 3, 4):
        cands = [c for c in coroots if c["max_abs_slot_ngen"] == n_fam]
        min_k = min(c["k_inst"] for c in cands)
        min_examples = [c for c in cands if c["k_inst"] == min_k]
        thresholds[str(n_fam)] = {
            "target_ngen": n_fam,
            "minimal_k_inst": min_k,
            "minimal_norm2": 2 * min_k,
            "count_at_minimum": len(min_examples),
            "sample_coroot": min_examples[0],
        }

    # Also compute max |N_gen| achievable at or below each k_inst in 1..12
    max_ngen_up_to_k: Dict[str, int] = {}
    for k_budget in range(1, 13):
        sub_c = [c["max_abs_slot_ngen"] for c in coroots if c["k_inst"] <= k_budget]
        max_ngen_up_to_k[str(k_budget)] = max(sub_c) if sub_c else 0

    return {
        "total_enumerated_coroots": len(coroots),
        "max_norm2": max_norm2,
        "max_instanton_dynkin_identity_err": max_instanton_identity_err,
        "max_unprojected_slot_sum_err": max_slot_sum_err,
        "minimal_instanton_thresholds_by_ngen": thresholds,
        "max_achievable_ngen_by_k_inst_budget": max_ngen_up_to_k,
    }


def dedekind_sum(d: int, c: int) -> float:
    """Classical Dedekind sum s(d, c) = sum_{k=1}^{|c|-1} ((k/c)) ((kd/c))."""
    c_abs = abs(c)
    if c_abs <= 1:
        return 0.0

    def sawtooth(x_num: int, x_den: int) -> float:
        if x_num % x_den == 0:
            return 0.0
        frac = (x_num % x_den) / float(x_den)
        return frac - 0.5

    return sum(sawtooth(k, c_abs) * sawtooth(k * d, c_abs) for k in range(1, c_abs))


def rademacher_phi_sl2z(M: np.ndarray) -> int:
    """Exact Rademacher-Dedekind class invariant Phi(M) in Z for hyperbolic M in SL(2, Z) (Tr(M) > 2)."""
    a, b, c, d = int(M[0, 0]), int(M[0, 1]), int(M[1, 0]), int(M[1, 1])
    if c == 0:
        return int(round(b / float(d)))
    sgn_c = 1 if c > 0 else -1
    sgn_ca = 1 if (c * (a + d)) > 0 else (-1 if (c * (a + d)) < 0 else 0)
    val = ((a + d) / float(c)) - 12.0 * sgn_c * dedekind_sum(d, c) - 3.0 * sgn_ca
    return int(round(val))


def run_gate4() -> Dict[str, Any]:
    """Execute Gate 4 unrigged topological tadpole & flux quantization audit."""
    e8_data = build_e8_root_system_and_su5_bifundamentals()
    enum_res = enumerate_su5_commuting_e8_coroots(e8_data, max_norm2=32)

    k_min_1 = enum_res["minimal_instanton_thresholds_by_ngen"]["1"]["minimal_k_inst"]
    k_min_2 = enum_res["minimal_instanton_thresholds_by_ngen"]["2"]["minimal_k_inst"]
    k_min_3 = enum_res["minimal_instanton_thresholds_by_ngen"]["3"]["minimal_k_inst"]
    k_min_4 = enum_res["minimal_instanton_thresholds_by_ngen"]["4"]["minimal_k_inst"]
    max_by_k = enum_res["max_achievable_ngen_by_k_inst_budget"]

    # Audit Rule T1: 2D punctured-torus fiber Euler characteristic |chi(Sigma_{1,1})| = |2 - 2*1 - 1| = 1
    chi_punctured_torus = 2 - 2 * 1 - 1
    k_rule_t1 = abs(chi_punctured_torus)
    rule_t1_audit = {
        "rule": "T1: 2D Punctured-Fiber Euler Characteristic |chi(Sigma_{1,1})|",
        "chi_sigma_1_1": chi_punctured_torus,
        "k_inst_budget": k_rule_t1,
        "max_ngen_without_multiplier": max_by_k[str(k_rule_t1)],
        "reaches_3_generations_unrigged": max_by_k[str(k_rule_t1)] >= 3,
    }

    # Audit Rule T2: 3D Rademacher-Dedekind Monodromy Framing Defect |Phi_Dedekind(M_W)| = |#L - #R|
    candidate_words = [
        ("golden_bg_LR", "LR"),
        ("palindromic_run6", "LLLLLLRLR"),
        ("palindromic_mirror_1_6", "LRRRRRRLR"),
        ("reversible_3_1_3", "LLLRLLLRLR"),
        ("reversible_1_2_2_2", "LRRLLRRLR"),
        ("reversible_2_1_1_1_2", "LLRLRLLRLR"),
        ("irreversible_5_1_2_2", "LLLLLRLLRRLR"),
        ("amphicheiral_5_5", "LLLLLRRRRRLR"),
        ("non_extending_run7_ctrl", "LLLLLLLRLR"),
        ("higher_twist_run11", "LLLLLLLLLLLRLR"),
    ]
    t2_records: List[Dict[str, Any]] = []
    max_rademacher_word_err = 0
    for label, w in candidate_words:
        M = word_to_sl2z(w)
        phi_rad = rademacher_phi_sl2z(M)
        word_diff = w.count("L") - w.count("R")
        max_rademacher_word_err = max(max_rademacher_word_err, abs(phi_rad - word_diff))
        ext = check_golden_bundle_extension(w)
        k_b = abs(phi_rad)
        max_n = max_by_k[str(min(12, k_b))] if k_b > 0 else 0
        t2_records.append(
            {
                "label": label,
                "word": w,
                "extends_golden_v5": ext["extends_golden_v5"],
                "rademacher_phi": phi_rad,
                "L_minus_R": word_diff,
                "abs_phi_budget": k_b,
                "max_ngen_at_budget": max_n,
                "reaches_3_generations_and_extends": bool(ext["extends_golden_v5"] and max_n >= 3),
            }
        )

    rule_t2_audit = {
        "rule": "T2: 3D Rademacher-Dedekind Monodromy Framing Defect |Phi(M_W)|",
        "max_rademacher_vs_L_minus_R_err": max_rademacher_word_err,
        "run6_reaches_3_generations": next(
            r["reaches_3_generations_and_extends"] for r in t2_records if r["label"] == "palindromic_run6"
        ),
        "irrev_5_1_2_2_reaches_3_generations": next(
            r["reaches_3_generations_and_extends"] for r in t2_records if r["label"] == "irreversible_5_1_2_2"
        ),
        "records": t2_records,
    }

    # Audit Rule T3: 4D Rational Elliptic Surface (dP_9 = 1/2 K3) Cusp-Cap Bianchi Identity
    # chi(K3) = 24 => chi(dP_9) = c_2(T_{dP_9}) = 12; symmetric E_8 x E_8 split gives k_vis = k_hid = 6!
    chi_k3 = 24
    chi_dp9 = chi_k3 // 2
    k_vis_symmetric = chi_dp9 // 2
    rule_t3_audit = {
        "rule": "T3: 4D Rational-Elliptic Cusp-Cap Bianchi Identity (dP_9 = 1/2 K3)",
        "chi_K3": chi_k3,
        "chi_dP9_c2": chi_dp9,
        "symmetric_e8_x_e8_visible_k_inst": k_vis_symmetric,
        "exact_match_to_3gen_threshold": (k_vis_symmetric == k_min_3),
        "max_ngen_at_symmetric_split": max_by_k[str(k_vis_symmetric)],
    }

    gate4_passed = (
        e8_data["five_perp_weight_sum_err"] < 1e-13
        and enum_res["max_instanton_dynkin_identity_err"] < 1e-13
        and enum_res["max_unprojected_slot_sum_err"] == 0.0
        and k_min_3 == 6
        and max_rademacher_word_err == 0
        and (not rule_t1_audit["reaches_3_generations_unrigged"])
        and (not rule_t2_audit["run6_reaches_3_generations"])
        and (not rule_t2_audit["irrev_5_1_2_2_reaches_3_generations"])
        and rule_t3_audit["exact_match_to_3gen_threshold"]
        and rule_t3_audit["max_ngen_at_symmetric_split"] == 3
    )

    return {
        "gate": "Gate 4: Unrigged Topological Tadpole & E_8 Flux Quantization Audit",
        "gate4_passed": gate4_passed,
        "e8_instanton_quantization_theorem": enum_res,
        "rule_t1_2d_fiber_audit": rule_t1_audit,
        "rule_t2_3d_dedekind_audit": rule_t2_audit,
        "rule_t3_4d_dp9_cusp_cap_audit": rule_t3_audit,
    }


if __name__ == "__main__":
    import json

    out = run_gate4()
    print(json.dumps(out, indent=2))
    if not out["gate4_passed"]:
        raise SystemExit(1)
