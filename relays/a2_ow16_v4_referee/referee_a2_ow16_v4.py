#!/usr/bin/env python3
"""
Cold-Room Zero-Trust Referee for Card A2-OW16 Erratum 1 (a2_ow16_v4).

Strict Zero-Trust Rules:
- Zero imports from producer scripts (verify_a2_ow16*) or frontier/.
- Zero Python float or complex AST literals (exact int, Fraction,
  and integer-constructed mpmath at dps = 55).
- 0 of 19 empirical inputs (zero PDG, NuFIT, Planck, or lattice data).
- Independent recomputation from raw disk bytes, sealed A2-OW1..A2-OW15
  JSON outputs, and first-principles linear algebra / group theory.
"""

from __future__ import annotations

import ast
import hashlib
import json
import os
import sys
from fractions import Fraction
from typing import Any, Dict, List, Tuple

import mpmath as mp

mp.mp.dps = 55

REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
)
RELAYS_DIR = os.path.join(REPO_ROOT, "relays")
OUT_JSON_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "a2_ow16_v4_referee_results.json",
)
PRODUCER_JSON_PATH = os.path.join(
    RELAYS_DIR, "a2_ow16_v4", "a2_ow16_v4_results.json"
)

HISTORICAL_MANIFEST_DIRS: List[str] = [
    "a2_ow1_v3", "a2_ow1_referee",
    "a2_ow2_v4", "a2_ow2_referee",
    "a2_ow3_v2", "a2_ow3_referee",
    "a2_ow4_v2", "a2_ow4_referee",
    "a2_ow5", "a2_ow5_referee",
    "a2_ow6_v2", "a2_ow6_referee",
    "a2_ow7_v2", "a2_ow7_referee",
    "a2_ow8", "a2_ow8_referee",
    "a2_ow9", "a2_ow9_referee",
    "a2_ow10_v2", "a2_ow10_referee",
    "a2_ow11_v3", "a2_ow11_referee",
    "a2_ow12_v3", "a2_ow12_referee",
    "a2_ow13_v2", "a2_ow13_referee",
    "a2_ow14_v2", "a2_ow14_referee",
    "a2_ow15", "a2_ow15_referee",
    "a2_ow16_v2", "a2_ow16_referee",
]

V4_PRODUCER_MANIFEST_DIRS: List[str] = [
    "a2_ow16_v4",
]

OW_PRODUCER_JSON_RELPATHS: Dict[str, str] = {
    "OW1": "relays/a2_ow1_v3/verify_a2_ow1_v3_out.json",
    "OW2": "relays/a2_ow2_v4/verify_a2_ow2_v4_out.json",
    "OW3": "relays/a2_ow3_v2/verify_a2_ow3_v2_out.json",
    "OW4": "relays/a2_ow4_v2/verify_a2_ow4_v2_out.json",
    "OW5": "relays/a2_ow5/verify_a2_ow5_out.json",
    "OW6": "relays/a2_ow6_v2/verify_a2_ow6_v2_out.json",
    "OW7": "relays/a2_ow7_v2/verify_a2_ow7_v2_out.json",
    "OW8": "relays/a2_ow8/verify_a2_ow8_out.json",
    "OW9": "relays/a2_ow9/verify_a2_ow9_out.json",
    "OW10": "relays/a2_ow10_v2/verify_a2_ow10_v2_out.json",
    "OW11": "relays/a2_ow11_v3/verify_a2_ow11_v3_out.json",
    "OW12": "relays/a2_ow12_v3/verify_a2_ow12_v3_out.json",
    "OW13": "relays/a2_ow13_v2/a2_ow13_v2_results.json",
    "OW14": "relays/a2_ow14_v2/a2_ow14_v2_results.json",
    "OW15": "relays/a2_ow15/a2_ow15_results.json",
}


# ---------------------------------------------------------------------------
# Exact arithmetic & parsing helpers (zero float/complex literals)
# ---------------------------------------------------------------------------

def parse_frac(val: Any) -> Fraction:
    if isinstance(val, Fraction):
        return val
    if isinstance(val, int) and not isinstance(val, bool):
        return Fraction(val, 1)
    s = str(val).strip()
    return Fraction(s)


def parse_mpf(val: Any) -> mp.mpf:
    if isinstance(val, mp.mpf):
        return val
    if isinstance(val, Fraction):
        return mp.mpf(val.numerator) / mp.mpf(val.denominator)
    if isinstance(val, int) and not isinstance(val, bool):
        return mp.mpf(val)
    s = str(val).strip()
    if "/" in s:
        f = Fraction(s)
        return mp.mpf(f.numerator) / mp.mpf(f.denominator)
    return mp.mpf(s)


def load_json_exact(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh, parse_float=str)


def sha256_file_bytes(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def sha256_raw_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


# Exact RREF over Q (Fraction)
def rref_fraction(
    matrix: List[List[Fraction]],
) -> Tuple[List[List[Fraction]], List[int]]:
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    m = [[Fraction(v) for v in r] for r in matrix]
    pivots: List[int] = []
    r = 0
    for c in range(cols):
        if r >= rows:
            break
        piv = None
        for i in range(r, rows):
            if m[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        scale = m[r][c]
        m[r] = [v / scale for v in m[r]]
        for i in range(rows):
            if i != r and m[i][c] != 0:
                fac = m[i][c]
                m[i] = [m[i][j] - fac * m[r][j] for j in range(cols)]
        pivots.append(c)
        r += 1
    return m, pivots


def nullspace_fraction(matrix: List[List[Fraction]]) -> List[List[Fraction]]:
    m, pivots = rref_fraction(matrix)
    cols = len(matrix[0]) if matrix else 0
    pivot_set = set(pivots)
    free_cols = [c for c in range(cols) if c not in pivot_set]
    basis: List[List[Fraction]] = []
    for fc in free_cols:
        vec = [Fraction(0, 1)] * cols
        vec[fc] = Fraction(1, 1)
        for row_idx, pc in enumerate(pivots):
            vec[pc] = -m[row_idx][fc]
        basis.append(vec)
    return basis


# Exact arithmetic over Q(i): each element is (re: Fraction, im: Fraction)
QI = Tuple[Fraction, Fraction]
QI_ZERO: QI = (Fraction(0, 1), Fraction(0, 1))
QI_ONE: QI = (Fraction(1, 1), Fraction(0, 1))
QI_I: QI = (Fraction(0, 1), Fraction(1, 1))


def qi_add(x: QI, y: QI) -> QI:
    return (x[0] + y[0], x[1] + y[1])


def qi_sub(x: QI, y: QI) -> QI:
    return (x[0] - y[0], x[1] - y[1])


def qi_neg(x: QI) -> QI:
    return (-x[0], -x[1])


def qi_conj(x: QI) -> QI:
    return (x[0], -x[1])


def qi_mul(x: QI, y: QI) -> QI:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qi_is_zero(x: QI) -> bool:
    return x[0] == 0 and x[1] == 0


def qi_div(x: QI, y: QI) -> QI:
    denom = y[0] * y[0] + y[1] * y[1]
    if denom == 0:
        raise ZeroDivisionError("Division by zero in Q(i)")
    return (
        (x[0] * y[0] + x[1] * y[1]) / denom,
        (x[1] * y[0] - x[0] * y[1]) / denom,
    )


def rref_qi(matrix: List[List[QI]]) -> Tuple[List[List[QI]], List[int]]:
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    m = [list(r) for r in matrix]
    pivots: List[int] = []
    r = 0
    for c in range(cols):
        if r >= rows:
            break
        piv = None
        for i in range(r, rows):
            if not qi_is_zero(m[i][c]):
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        scale = m[r][c]
        m[r] = [qi_div(v, scale) for v in m[r]]
        for i in range(rows):
            if i != r and not qi_is_zero(m[i][c]):
                fac = m[i][c]
                m[i] = [
                    qi_sub(m[i][j], qi_mul(fac, m[r][j])) for j in range(cols)
                ]
        pivots.append(c)
        r += 1
    return m, pivots


def nullspace_qi(matrix: List[List[QI]]) -> List[List[QI]]:
    m, pivots = rref_qi(matrix)
    cols = len(matrix[0]) if matrix else 0
    pivot_set = set(pivots)
    free_cols = [c for c in range(cols) if c not in pivot_set]
    basis: List[List[QI]] = []
    for fc in free_cols:
        vec = [QI_ZERO] * cols
        vec[fc] = QI_ONE
        for row_idx, pc in enumerate(pivots):
            vec[pc] = qi_neg(m[row_idx][fc])
        basis.append(vec)
    return basis


# ---------------------------------------------------------------------------
# Task 1: Independent 66 / 66 SHA-256 Custody Manifest Verification
# ---------------------------------------------------------------------------

def verify_single_manifest(
    dir_name: str,
    manifest_name: str,
    override_bytes: bytes | None = None,
) -> Dict[str, Any]:
    dir_path = os.path.join(RELAYS_DIR, dir_name)
    manifest_path = os.path.join(dir_path, manifest_name)
    with open(manifest_path, "r", encoding="utf-8") as fh:
        lines = [ln.strip() for ln in fh if ln.strip()]
    if len(lines) != 1:
        return {
            "dir": dir_name,
            "manifest": manifest_name,
            "ok": False,
            "reason": f"Expected 1 line, found {len(lines)}",
        }
    parts = lines[0].split(None, 1)
    if len(parts) != 2:
        return {
            "dir": dir_name,
            "manifest": manifest_name,
            "ok": False,
            "reason": "Malformed manifest line",
        }
    recorded_sha, raw_target = parts[0].lower(), parts[1].strip()
    is_valid_hex = (
        len(recorded_sha) == 64
        and all(ch in "0123456789abcdef" for ch in recorded_sha)
    )
    if raw_target.startswith("relays/"):
        target_path = os.path.abspath(os.path.join(REPO_ROOT, raw_target))
    else:
        target_path = os.path.abspath(os.path.join(dir_path, raw_target))
    inside_dir = (
        os.path.commonpath([os.path.abspath(dir_path), target_path])
        == os.path.abspath(dir_path)
    )
    if not (is_valid_hex and inside_dir and os.path.isfile(target_path)):
        return {
            "dir": dir_name,
            "manifest": manifest_name,
            "target": raw_target,
            "ok": False,
            "reason": "Invalid digest format or missing/escaped target",
        }
    if override_bytes is not None:
        computed_sha = sha256_raw_bytes(override_bytes)
    else:
        computed_sha = sha256_file_bytes(target_path)
    matched = computed_sha == recorded_sha
    return {
        "dir": dir_name,
        "manifest": manifest_name,
        "target": os.path.relpath(target_path, REPO_ROOT),
        "recorded_sha256": recorded_sha,
        "computed_sha256": computed_sha,
        "ok": matched,
    }


def verify_all_66_manifests() -> Dict[str, Any]:
    historical_records: List[Dict[str, Any]] = []
    for d in HISTORICAL_MANIFEST_DIRS:
        for m in ("SCRIPT_SHA256.txt", "OUTPUT_SHA256.txt"):
            historical_records.append(verify_single_manifest(d, m))

    v4_records: List[Dict[str, Any]] = []
    for d in V4_PRODUCER_MANIFEST_DIRS:
        for m in ("SCRIPT_SHA256.txt", "OUTPUT_SHA256.txt"):
            v4_records.append(verify_single_manifest(d, m))

    hist_passed = sum(1 for r in historical_records if r["ok"])
    v4_passed = sum(1 for r in v4_records if r["ok"])
    total_passed = hist_passed + v4_passed
    total_checked = len(historical_records) + len(v4_records)
    mismatches = [
        r for r in (historical_records + v4_records) if not r["ok"]
    ]
    return {
        "historical_total": len(historical_records),
        "historical_verified": hist_passed,
        "v4_producer_total": len(v4_records),
        "v4_producer_verified": v4_passed,
        "total_checked": total_checked,
        "total_verified": total_passed,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "historical_manifests": historical_records,
        "v4_producer_manifests": v4_records,
        "pass": (
            len(historical_records) == 64
            and hist_passed == 64
            and len(v4_records) == 2
            and v4_passed == 2
            and len(mismatches) == 0
        ),
    }


# ---------------------------------------------------------------------------
# Task 2: Independent 10 / 10 Cross-Card Consistency Locks (OW1..OW15)
# ---------------------------------------------------------------------------

def load_sealed_ow1_to_ow15() -> Dict[str, Any]:
    return {
        tag: load_json_exact(os.path.join(REPO_ROOT, relpath))
        for tag, relpath in OW_PRODUCER_JSON_RELPATHS.items()
    }


def check_lock_6_from_data(ow8: Any, ow15: Any) -> Dict[str, Any]:
    ow8_thr = ow8["OW8_A_conformal_finite_sakharov_gravity"][
        "spin10_threshold_at_xi_1_over_6"
    ]
    ow15_bh = ow15["ow15_b"]["conformal_bh_entropy"][
        "spin10_induced_bh_entropy"
    ]
    n_proca = int(ow8_thr["n_massive_XY_Proca"])
    n_nur = int(ow8_thr["n_heavy_nuR_Weyl"])
    ow8_clog = parse_frac(ow8_thr["c_log_equal_mass"])
    c_ent = parse_frac(ow15_bh["c_log_ent"])
    c_con = parse_frac(ow15_bh["c_log_contact"])
    ow15_tot = parse_frac(ow15_bh["c_log_total"])
    # First-principles induced-gravity c_log at xi = 1/6:
    # Massive Proca = +1/2 per Proca vector (33/2), Weyl = -1/6 per Weyl (-3/6 = -1/2)
    # Wait: check exact identity: (33 * 1/2) - (3 * 1/6) = 33/2 - 1/2 = 32/2 = 16!
    first_principles_clog = Fraction(n_proca, 2) - Fraction(n_nur, 6)
    sum_ok = (c_ent + c_con) == ow15_tot
    match_ok = (
        n_proca == 33
        and n_nur == 3
        and ow8_clog == Fraction(16, 1)
        and c_ent == Fraction(-55, 3)
        and c_con == Fraction(103, 3)
        and sum_ok
        and ow15_tot == ow8_clog
        and first_principles_clog == ow8_clog
    )
    return {
        "n_massive_XY_Proca": n_proca,
        "n_heavy_nuR_Weyl": n_nur,
        "ow8_c_log": str(ow8_clog),
        "ow15_c_log_ent": str(c_ent),
        "ow15_c_log_contact": str(c_con),
        "ow15_c_log_sum": str(c_ent + c_con),
        "ow15_c_log_total": str(ow15_tot),
        "first_principles_33_over_2_minus_3_over_6": str(first_principles_clog),
        "pass": match_ok,
    }


def verify_all_10_cross_card_locks(ow: Dict[str, Any]) -> Dict[str, Any]:
    locks: Dict[str, Dict[str, Any]] = {}

    # LOCK-1: Unique chiral anomaly-free SM hit N=5, d=5 (1 of 21) across OW1, OW4, OW10, OW14
    ow1_hits = ow["OW1"]["OW1_A_open_weave_ladder"][
        "sm_hits_across_all_rungs_d_le_12"
    ]
    ow4_a = ow["OW4"]["OW4_A_dynamic_chiral_bowl_rung_selection"]
    ow10_21 = ow["OW10"]["OW10_A_asymptotic_safety_double_pincer"][
        "all_21_open_weave_actions_audit"
    ]
    ow10_recount = [
        a for a in ow10_21["actions"] if a["all_four_gates_pass"] is True
    ]
    ow14_cen = ow["OW14"]["ow14_b"]["unimodular_and_sequestering"][
        "delta_23N_census"
    ]
    lock1_ok = (
        len(ow1_hits) == 1
        and ow1_hits[0]["N"] == 5
        and ow1_hits[0]["degree"] == 5
        and ow4_a["total_faithful_actions_d_le_12"] == 21
        and ow4_a["unique_confining_chiral_bowl_2H"] == [[5, 5, 64]]
        and ow10_21["total_actions"] == 21
        and len(ow10_21["actions"]) == 21
        and len(ow10_recount) == 1
        and ow10_recount[0]["N"] == 5
        and ow10_recount[0]["d"] == 5
        and ow10_recount[0]["M_g"] == 8
        and ow14_cen["total_actions"] == 21
        and ow14_cen["survivors_cap22"] == [[5, 5, 8]]
        and ow14_cen["survivors_cap23"] == [[5, 5, 8]]
    )
    locks["LOCK-1"] = {
        "ow1_hit": [ow1_hits[0]["N"], ow1_hits[0]["degree"]]
        if len(ow1_hits) == 1
        else None,
        "ow4_total_actions": ow4_a["total_faithful_actions_d_le_12"],
        "ow4_winner_2H": ow4_a["unique_confining_chiral_bowl_2H"],
        "ow10_recount_winners": [
            [a["N"], a["d"], a["M_g"]] for a in ow10_recount
        ],
        "ow14_survivors_cap22": ow14_cen["survivors_cap22"],
        "ow14_survivors_cap23": ow14_cen["survivors_cap23"],
        "pass": lock1_ok,
    }

    # LOCK-2: Unique N_gen = 3 across OW4, OW10, OW14
    ow4_c = ow["OW4"]["OW4_C_unique_4D_gravity_and_a0_cc_nogo"]
    ow4_d4_rows = [r for r in ow4_c["dim_gen_scan"] if r["D"] == 4]
    ow4_d4_attr = sorted(
        r["N_gen"] for r in ow4_d4_rows if r["attractive_gravity_2H_xi0"]
    )
    ow10_dp = ow["OW10"]["OW10_A_asymptotic_safety_double_pincer"][
        "double_pincer_selection"
    ]
    ow10_lb = parse_frac(ow10_dp["N_gen_lower_bound"])
    ow10_ub = parse_frac(ow10_dp["N_gen_upper_bound"])
    ow10_ints = [k for k in range(1, 10) if ow10_lb < k < ow10_ub]
    ow14_frg = ow["OW14"]["ow14_b"]["unimodular_and_sequestering"][
        "unimodular_frg"
    ]
    c23_lb = parse_frac(ow14_frg["full_lam0_cap23"]["ngen_lower_bound"])
    c23_ub = parse_frac(ow14_frg["full_lam0_cap23"]["ngen_upper_bound"])
    c23_ints = [k for k in range(1, 10) if c23_lb < k < c23_ub]
    c22_lb = parse_frac(ow14_frg["traceless_cap22"]["ngen_lower_bound"])
    c22_ub = parse_frac(ow14_frg["traceless_cap22"]["ngen_upper_bound"])
    c22_ints = [k for k in range(1, 10) if c22_lb < k < c22_ub]
    lock2_ok = (
        ow4_c["exact_fg_cancellation_hits_across_D4_6_8_10_Ngen1_4"] == [[4, 3]]
        and ow4_d4_attr == [3, 4]
        and ow10_lb == Fraction(5, 2)
        and ow10_ub == Fraction(27, 8)
        and ow10_ints == [3]
        and ow10_dp["N_gen_winners_at_2H"] == [3]
        and c23_lb == Fraction(5, 2)
        and c23_ub == Fraction(63, 16)
        and c23_ints == [3]
        and ow14_frg["full_lam0_cap23"]["ngen_integer_survivors"] == [3]
        and c22_lb == Fraction(5, 2)
        and c22_ub == Fraction(31, 8)
        and c22_ints == [3]
        and ow14_frg["traceless_cap22"]["ngen_integer_survivors"] == [3]
    )
    locks["LOCK-2"] = {
        "ow4_exact_fg_hits": ow4_c[
            "exact_fg_cancellation_hits_across_D4_6_8_10_Ngen1_4"
        ],
        "ow10_bounds": [str(ow10_lb), str(ow10_ub)],
        "ow10_int_solutions": ow10_ints,
        "ow14_cap23_bounds": [str(c23_lb), str(c23_ub)],
        "ow14_cap22_bounds": [str(c22_lb), str(c22_ub)],
        "ow14_int_solutions": [c23_ints, c22_ints],
        "pass": lock2_ok,
    }

    # LOCK-3: tau_*^{+-} = (+-2 + i)/5 across OW2, OW9, OW12
    ow2_r5 = ow["OW2"]["OW2_B_certified_global_minima_finite_rungs_1_to_5"][
        "rungs"
    ]["5"]
    ow2_mins = ow2_r5["minima"]
    ow2_im_ok = all(
        parse_frac(m["tau_im"]) == Fraction(1, 5) for m in ow2_mins
    )
    ow2_re_mod1 = sorted(parse_frac(m["tau_re"]) % 1 for m in ow2_mins)
    ow2_re_ok = ow2_re_mod1 == [Fraction(2, 5), Fraction(3, 5)]
    ow9_a2 = ow["OW9"]["OW9_A2_de_sitter_casimir_and_X05_stabilization"]
    ow9_p = ow9_a2["F3_stabilization_at_tau_plus"]
    ow9_m = ow9_a2["F3_stabilization_at_tau_minus"]
    ow9_f3_diff = abs(parse_mpf(ow9_p["F3_value"]) - parse_mpf(ow9_m["F3_value"]))
    ow9_ok = (
        ow9_f3_diff < mp.mpf(1) / mp.mpf(10) ** 18
        and parse_mpf(ow9_p["grad_norm"]) < mp.mpf(1) / mp.mpf(10) ** 12
        and parse_mpf(ow9_m["grad_norm"]) < mp.mpf(1) / mp.mpf(10) ** 12
        and parse_mpf(ow9_p["eig_1"]) > 0
        and parse_mpf(ow9_p["eig_2"]) > 0
        and parse_mpf(ow9_m["eig_1"]) > 0
        and parse_mpf(ow9_m["eig_2"]) > 0
    )
    ow12_a = ow["OW12"]["OW12_A_strong_cp_and_7D_CS_axion"]
    bt_p = parse_mpf(ow12_a["bar_theta_Q_E5_plus_E6_m8_tau_plus"])
    bt_m = parse_mpf(ow12_a["bar_theta_Q_E5_plus_E6_m8_tau_minus"])
    bt_sum = abs(bt_p + bt_m)
    ow12_lep = ow["OW12"]["OW12_B_neutrino_seesaw_pmns_and_leptogenesis"][
        "leptogenesis_fukugita_yanagida"
    ]
    ep_p = parse_mpf(ow12_lep["eps1_norm_tau_plus"])
    ep_m = parse_mpf(ow12_lep["eps1_norm_tau_minus"])
    ep_sum = abs(ep_p + ep_m)
    ow12_ok = (
        abs(bt_p) > mp.mpf(1) / mp.mpf(10) ** 3
        and bt_sum < mp.mpf(1) / mp.mpf(10) ** 12
        and abs(ep_p) > mp.mpf(1) / mp.mpf(10) ** 8
        and ep_sum < mp.mpf(1) / mp.mpf(10) ** 18
    )
    lock3_ok = (
        ow2_r5["global_certification_passed"] is True
        and ow2_r5["num_gamma0_distinct_global_minima"] == 2
        and ow2_im_ok
        and ow2_re_ok
        and ow9_ok
        and ow12_ok
    )
    locks["LOCK-3"] = {
        "ow2_tau_re_mod1": [str(x) for x in ow2_re_mod1],
        "ow2_tau_im_exact_1_over_5": ow2_im_ok,
        "ow9_F3_mirror_diff": mp.nstr(ow9_f3_diff, 12),
        "ow12_bar_theta_mirror_sum": mp.nstr(bt_sum, 12),
        "ow12_eps1_mirror_sum": mp.nstr(ep_sum, 12),
        "pass": lock3_ok,
    }

    # LOCK-4: 2H Type-II X:HOL across OW3, OW8, OW11, OW13
    ow3_xhol = ow["OW3"]["OW3_B_open_torus_yukawa_and_spin10_xhol"][
        "part2_spin10_xhol_32x32"
    ]
    ow8_split = ow["OW8"]["OW8_B_unification_and_2hdm_radiative_transmutation"][
        "conformal_2H_TypeII_automatic_split"
    ]
    ow11_dt = ow["OW11"]["OW11_A_spin10_orbifold_I8_and_casimir_selection"][
        "orbifold_centralizers_in_so10"
    ]["doublet_triplet_on_10"]
    ow13_q = ow["OW13"]["ow13_a"]["quartic_fixed_points"][
        "spin10_T2_LDW_yb_high"
    ]
    ow13_gw = ow["OW13"]["ow13_c"]["gw_ew_benchmark"]
    lock4_ok = (
        ow3_xhol["holomorphic_separation_exact"] is True
        and parse_mpf(ow3_xhol["Hu_forbidden_Qd_Le_max_entry"]) == 0
        and parse_mpf(ow3_xhol["Hd_forbidden_Qu_Lnu_max_entry"]) == 0
        and len(ow8_split) >= 3
        and all(
            r["automatic_Hu_stable_Hd_destabilized"] is True
            and parse_mpf(r["lam2_Hu_IR"]) > 0
            and parse_mpf(r["lam1_Hd_IR"]) < 0
            for r in ow8_split
        )
        and ow11_dt["kept_2H_components"] == 4
        and ow11_dt["projected_color_triplets"] == 6
        and ow13_q["all_uv_irrelevant"] is True
        and ow13_q["bfb_satisfied"] is True
        and parse_mpf(ow13_gw["mh2_over_v2"]) > 0
        and parse_mpf(ow13_gw["identity_abs_err"]) == 0
    )
    locks["LOCK-4"] = {
        "ow3_holomorphic_separation_exact": ow3_xhol[
            "holomorphic_separation_exact"
        ],
        "ow8_split_count": len(ow8_split),
        "ow11_10_decomposition": [
            ow11_dt["kept_2H_components"],
            ow11_dt["projected_color_triplets"],
        ],
        "ow13_all_uv_irrelevant": ow13_q["all_uv_irrelevant"],
        "ow13_gw_mh2_over_v2": str(ow13_gw["mh2_over_v2"]),
        "s2_caveat_10R_4_real_is_1H_not_2H": True,
        "pass": lock4_ok,
    }

    # LOCK-5: 6D 3 x 16_+ anomaly inflow across OW5, OW11, OW12, OW15
    ow5_b = ow["OW5"]["OW5_B_triple_locked_6D_I8_and_7D_CS_inflow"]
    ow5_r4 = parse_frac(ow5_b["c_R4_3gen"])
    ow5_cs7 = parse_frac(ow5_b["cs_7d_inflow_terms_3gen"]["d(CS7[omega_R])"])
    ow11_i8 = ow["OW11"]["OW11_A_spin10_orbifold_I8_and_casimir_selection"][
        "spin10_6D_I8_anomaly"
    ]
    ow11_f4 = parse_frac(ow11_i8["c_tr10_F4_for_3x16"])
    ow11_r4 = parse_frac(ow11_i8["c_tr_R4_for_3x16"])
    ow12_ax = ow["OW12"]["OW12_A_strong_cp_and_7D_CS_axion"]["spin10_7D_CS_axion"]
    ow12_en = parse_frac(ow12_ax["E_over_N"])
    ow12_e = parse_frac(ow12_ax["E_gen"])
    ow12_n = parse_frac(ow12_ax["N_gen"])
    ow15_x37 = ow["OW15"]["ow15_c"]["x1_x37_audit"]["x37_spin10_topology"]
    lock5_ok = (
        ow5_r4 == Fraction(1, 120)
        and ow5_cs7 == Fraction(1, 120)
        and ow11_f4 == Fraction(-1, 8)
        and ow11_r4 == ow5_r4
        and ow11_i8["still_forces_7D_CS_inflow"] is True
        and ow12_en == Fraction(8, 3)
        and (ow12_e / ow12_n) == ow12_en
        and ow15_x37["H3_Spin10_Z"] == "Z"
        and ow15_x37["pi_3_Spin10"] == "Z"
    )
    locks["LOCK-5"] = {
        "ow5_c_R4_3gen": str(ow5_r4),
        "ow11_c_tr10_F4": str(ow11_f4),
        "ow11_c_tr_R4": str(ow11_r4),
        "ow12_E_over_N": str(ow12_en),
        "ow15_H3_Spin10_Z": ow15_x37["H3_Spin10_Z"],
        "pass": lock5_ok,
    }

    # LOCK-6: OW8 c_log = +16 equals OW15 conical-defect sum -55/3 + 103/3 == 16
    locks["LOCK-6"] = check_lock_6_from_data(ow["OW8"], ow["OW15"])

    # LOCK-7: OW11 vs OW13 Spin(10) real-10 Type-II and Type-I FRG (g_*, lam_*)
    ow11_frg = ow["OW11"]["OW11_B_weak_frg_pati_salam_unification_and_proton_safety"][
        "uv_and_intermediate_frg"
    ]["Spin10_real_10"]
    ow13_frg = ow["OW13"]["ow13_a"]["gravity_fixed_points_and_f_lam"]
    t2_11 = ow11_frg["TypeII"]["fps"][0]
    t1_11 = ow11_frg["TypeI"]["fps"][0]
    t2_13 = ow13_frg["spin10_real10_T2"]
    t1_13 = ow13_frg["spin10_real10_T1"]

    def rel_err(a_val: Any, b_val: Any) -> mp.mpf:
        a = parse_mpf(a_val)
        b = parse_mpf(b_val)
        return abs(a - b) / abs(b)

    e_t2_g = rel_err(t2_11["g_star"], t2_13["g_star"])
    e_t2_l = rel_err(t2_11["lam_star"], t2_13["lam_star"])
    e_t1_g = rel_err(t1_11["g_star"], t1_13["g_star"])
    e_t1_l = rel_err(t1_11["lam_star"], t1_13["lam_star"])
    tol_14 = mp.mpf(1) / mp.mpf(10) ** 14
    max_lock7_err = max(e_t2_g, e_t2_l, e_t1_g, e_t1_l)
    locks["LOCK-7"] = {
        "rel_err_T2_g": mp.nstr(e_t2_g, 12),
        "rel_err_T2_lam": mp.nstr(e_t2_l, 12),
        "rel_err_T1_g": mp.nstr(e_t1_g, 12),
        "rel_err_T1_lam": mp.nstr(e_t1_l, 12),
        "max_rel_err": mp.nstr(max_lock7_err, 12),
        "pass": max_lock7_err < tol_14,
    }

    # LOCK-8: OW13 f_xi^bg(lam = 0) == 0 matches OW14 unimodular lam = 0 protection
    ow13_u = ow["OW13"]["ow13_b"]["grav_beta_xi_bg"]["unimodular_lam0_2h"]
    ow14_u = ow["OW14"]["ow14_b"]["unimodular_and_sequestering"][
        "ow13_bridges_at_lam0"
    ]
    lock8_ok = (
        parse_frac(ow13_u["f_xi_bg"]) == Fraction(0, 1)
        and parse_frac(ow13_u["beta_xi_bg_at_1_6"]) == Fraction(0, 1)
        and ow14_u["f_xi_bg_at_lam0_identically_zero"] is True
        and parse_frac(ow14_u["gsm_2h_unimod_f_lam_exact"]) == Fraction(16, 3)
    )
    locks["LOCK-8"] = {
        "ow13_f_xi_bg_lam0": str(parse_frac(ow13_u["f_xi_bg"])),
        "ow13_beta_xi_bg_at_1_6": str(parse_frac(ow13_u["beta_xi_bg_at_1_6"])),
        "ow14_f_xi_bg_zero_flag": ow14_u["f_xi_bg_at_lam0_identically_zero"],
        "ow14_gsm_2h_unimod_f_lam_exact": str(
            parse_frac(ow14_u["gsm_2h_unimod_f_lam_exact"])
        ),
        "pass": lock8_ok,
    }

    # LOCK-9: G_SM 2H Weyl anomaly c = 37/15 across OW10, OW13, OW15 + first principles
    ow10_c = parse_frac(ow["OW10"]["OW10_B_stelle_ghost_and_a_theorem"]["open_weave_2H_c"])
    ow13_c = parse_frac(ow["OW13"]["ow13_b"]["quadratic_gravity_c2_r2"]["gsm_2h"]["c_mat"])
    ow15_c = parse_frac(
        ow["OW15"]["ow15_b"]["conformal_bh_entropy"][
            "schwarzschild_log_corrections"
        ]["ir_gsm_2h_48weyl"]["c"]
    )
    c_first_principles = Fraction(8 + 3 * 48 + 12 * 12, 120)
    lock9_ok = (
        ow10_c == Fraction(37, 15)
        and ow13_c == Fraction(37, 15)
        and ow15_c == Fraction(37, 15)
        and c_first_principles == Fraction(37, 15)
    )
    locks["LOCK-9"] = {
        "ow10_c": str(ow10_c),
        "ow13_c_mat": str(ow13_c),
        "ow15_c_48weyl": str(ow15_c),
        "first_principles_c": str(c_first_principles),
        "pass": lock9_ok,
    }

    # LOCK-10: OW4 unique (D=4, N_gen=3) combines with OW15 (1,3) -> (1,5) -> (1,6)
    ow15_a = ow["OW15"]["ow15_a"]
    lock10_ok = (
        ow4_c["exact_fg_cancellation_hits_across_D4_6_8_10_Ngen1_4"] == [[4, 3]]
        and ow15_a["unique_d4_complex_chiral"] == ["D4_1_3"]
        and ow15_a["unique_tower_hyp_pos_kin"] == ["D4_1_3", "D6_1_5", "D7_1_6"]
    )
    locks["LOCK-10"] = {
        "ow4_exact_fg_hit": ow4_c[
            "exact_fg_cancellation_hits_across_D4_6_8_10_Ngen1_4"
        ],
        "ow15_unique_d4": ow15_a["unique_d4_complex_chiral"],
        "ow15_unique_tower": ow15_a["unique_tower_hyp_pos_kin"],
        "pass": lock10_ok,
    }

    passed_count = sum(1 for v in locks.values() if v["pass"])
    return {
        "locks": locks,
        "passed_count": passed_count,
        "total_count": len(locks),
        "pass": passed_count == 10 and len(locks) == 10,
    }


# ---------------------------------------------------------------------------
# Task 3: Independent First-Principles Proofs of AGY-C25 S1, S2, S3, S4, S6
# ---------------------------------------------------------------------------

def prove_s1_m004_3cycle_and_bits() -> Dict[str, Any]:
    # Monodromy matrix m004 = [[2, 1], [1, 1]] in SL(2, Z)
    M = [[2, 1], [1, 1]]
    det_M = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    tr_M = M[0][0] + M[1][1]
    e2_nonzero = [(1, 0), (0, 1), (1, 1)]
    idx_of = {pt: i for i, pt in enumerate(e2_nonzero)}

    # Action on E[2] \ {0} mod 2 -> 3x3 permutation matrix P (P_{ji} = 1 if M e_i = e_j)
    P: List[List[Fraction]] = [
        [Fraction(0, 1) for _ in range(3)] for _ in range(3)
    ]
    perm: List[int] = []
    for i, (x, y) in enumerate(e2_nonzero):
        nx = (M[0][0] * x + M[0][1] * y) % 2
        ny = (M[1][0] * x + M[1][1] * y) % 2
        j = idx_of[(nx, ny)]
        perm.append(j)
        P[j][i] = Fraction(1, 1)

    def mat_mul(a: List[List[Fraction]], b: List[List[Fraction]]) -> List[List[Fraction]]:
        n = len(a)
        return [
            [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)
        ]

    I3 = [
        [Fraction(1 if i == j else 0, 1) for j in range(3)]
        for i in range(3)
    ]
    P2 = mat_mul(P, P)
    P3 = mat_mul(P2, P)

    # Verify orbit is a single 3-cycle
    orbit = [0]
    cur = perm[0]
    while cur != 0:
        orbit.append(cur)
        cur = perm[cur]
    is_single_3cycle = (len(orbit) == 3 and set(orbit) == {0, 1, 2})

    # Solve P D - D P = 0 for D = diag(d_0, d_1, d_2) via exact Fraction nullspace
    comm_rows: List[List[Fraction]] = []
    for i in range(3):
        for j in range(3):
            # (P D - D P)_{ij} = P_{ij} d_j - d_i P_{ij}
            row = [Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)]
            row[j] += P[i][j]
            row[i] -= P[i][j]
            comm_rows.append(row)
    ker = nullspace_fraction(comm_rows)
    only_scalar_commutes = (
        len(ker) == 1
        and ker[0][0] != 0
        and ker[0][0] == ker[0][1] == ker[0][2]
    )

    # Explicit non-commutation test for hierarchical D_R = diag(eps^2, eps, 1)
    eps_test = Fraction(1, 2)
    D_hier = [
        [eps_test * eps_test, Fraction(0, 1), Fraction(0, 1)],
        [Fraction(0, 1), eps_test, Fraction(0, 1)],
        [Fraction(0, 1), Fraction(0, 1), Fraction(1, 1)],
    ]
    PD = mat_mul(P, D_hier)
    DP = mat_mul(D_hier, P)
    comm_sq_norm = sum(
        (PD[i][j] - DP[i][j]) ** 2 for i in range(3) for j in range(3)
    )

    # Discrete flavor selection state count: 6 perms x 3 cusp levels {8, 24, 40} = 18
    num_perms = 6
    cusp_levels = [8, 24, 40]
    num_states = num_perms * len(cusp_levels)
    bits_18 = mp.log(mp.mpf(num_states), 2)
    bits_sum = mp.log(mp.mpf(num_perms), 2) + mp.log(mp.mpf(len(cusp_levels)), 2)
    bits_identity_err = abs(bits_18 - bits_sum)
    old_bits_12 = mp.log(mp.mpf(12), 2)
    bits_increase = bits_18 - old_bits_12

    s1_ok = (
        det_M == 1
        and tr_M == 3
        and P != I3
        and P2 != I3
        and P3 == I3
        and is_single_3cycle
        and only_scalar_commutes
        and comm_sq_norm > 0
        and num_states == 18
        and bits_identity_err < mp.mpf(1) / mp.mpf(10) ** 50
        and bits_increase > 0
    )
    return {
        "det_m004": det_M,
        "tr_m004": tr_M,
        "perm_on_E2_nonzero": perm,
        "P_matrix": [[int(x) for x in row] for row in P],
        "P_cubed_eq_I3": P3 == I3,
        "P_ne_I3_and_P2_ne_I3": (P != I3 and P2 != I3),
        "single_3cycle_orbit": orbit,
        "commuting_diagonal_nullspace_dim": len(ker),
        "commuting_diagonal_basis": [[str(x) for x in v] for v in ker],
        "only_scalar_diagonal_commutes": only_scalar_commutes,
        "hierarchical_diag_commutator_sq_norm": str(comm_sq_norm),
        "discrete_states": num_states,
        "log2_18_bits": mp.nstr(bits_18, 25),
        "log2_6_plus_log2_3_err": mp.nstr(bits_identity_err, 12),
        "bits_delta_vs_log2_12": mp.nstr(bits_increase, 20),
        "pass": s1_ok,
    }


def prove_s2_10R_vs_10C_orbifold(ow11: Any, claimed_even_10R: int = 4) -> Dict[str, Any]:
    # Build explicit 10x10 -P_PS = diag(-1^6, +1^4) over Fraction
    diag_entries = [Fraction(-1, 1)] * 6 + [Fraction(1, 1)] * 4
    neg_P_PS = [
        [diag_entries[i] if i == j else Fraction(0, 1) for j in range(10)]
        for i in range(10)
    ]
    I10 = [
        [Fraction(1 if i == j else 0, 1) for j in range(10)]
        for i in range(10)
    ]
    # Check involution (-P_PS)^2 == I10
    sq = [
        [sum(neg_P_PS[i][k] * neg_P_PS[k][j] for k in range(10)) for j in range(10)]
        for i in range(10)
    ]
    is_involution = sq == I10
    trace_val = sum(neg_P_PS[i][i] for i in range(10))

    # Compute exact eigenspace dimensions by nullspace of (-P_PS - I) and (-P_PS + I)
    mat_even = [
        [neg_P_PS[i][j] - I10[i][j] for j in range(10)]
        for i in range(10)
    ]
    mat_odd = [
        [neg_P_PS[i][j] + I10[i][j] for j in range(10)]
        for i in range(10)
    ]
    even_10R_dim = len(nullspace_fraction(mat_even))
    odd_10R_dim = len(nullspace_fraction(mat_odd))

    # Build explicit 20x20 real representation of -P_PS (x) I_2 on 10_C = 10_R (x) C
    neg_P_10C = [
        [
            (diag_entries[i // 2] if i == j else Fraction(0, 1))
            for j in range(20)
        ]
        for i in range(20)
    ]
    I20 = [
        [Fraction(1 if i == j else 0, 1) for j in range(20)]
        for i in range(20)
    ]
    mat_even_10C = [
        [neg_P_10C[i][j] - I20[i][j] for j in range(20)]
        for i in range(20)
    ]
    even_10C_dim = len(nullspace_fraction(mat_even_10C))

    # Real bidoublet check: real 4-vector (a0, a1, a2, a3) -> Phi = a0 I + i(a1 s1 + a2 s2 + a3 s3)
    # Verify exact quaternion reality condition eps Phi^* eps^T == Phi where eps = [[0, 1], [-1, 0]]
    # Test on all 4 basis elements of R^4 over Q(i)
    basis_phi: List[List[List[QI]]] = [
        [[QI_ONE, QI_ZERO], [QI_ZERO, QI_ONE]],               # I
        [[QI_ZERO, QI_I], [QI_I, QI_ZERO]],                   # i sigma_1
        [[QI_ZERO, QI_ONE], [qi_neg(QI_ONE), QI_ZERO]],       # i sigma_2
        [[QI_I, QI_ZERO], [QI_ZERO, qi_neg(QI_I)]],           # i sigma_3
    ]
    eps_mat: List[List[QI]] = [
        [QI_ZERO, QI_ONE],
        [qi_neg(QI_ONE), QI_ZERO],
    ]
    eps_T: List[List[QI]] = [
        [QI_ZERO, qi_neg(QI_ONE)],
        [QI_ONE, QI_ZERO],
    ]

    def qi_mm(a: List[List[QI]], b: List[List[QI]]) -> List[List[QI]]:
        out: List[List[QI]] = []
        for i in range(2):
            row: List[QI] = []
            for j in range(2):
                acc = QI_ZERO
                for k in range(2):
                    acc = qi_add(acc, qi_mul(a[i][k], b[k][j]))
                row.append(acc)
            out.append(row)
        return out

    reality_holds_all4 = True
    for phi in basis_phi:
        phi_conj = [[qi_conj(phi[i][j]) for j in range(2)] for i in range(2)]
        lhs = qi_mm(qi_mm(eps_mat, phi_conj), eps_T)
        if lhs != phi:
            reality_holds_all4 = False

    # First-principles 6D T^2/Z_2 bulk supertrace per lattice point:
    # 45 vectors * 2 = 90, 3x16 Weyl * 2 = 96; 10_R adds +5 -> -1 (dS), 10_C adds +10 -> +4 (AdS)
    nB_minus_nF_10R = (45 * 2 + 10 // 2) - (48 * 2)
    nB_minus_nF_10C = (45 * 2 + 20 // 2) - (48 * 2)
    ow11_cas = ow11["OW11_A_spin10_orbifold_I8_and_casimir_selection"][
        "spin10_6D_bulk_supertraces_and_casimir"
    ]
    ow11_10R_ok = (
        ow11_cas["bulk_real_10"]["n_B_minus_n_F_per_T2_pt"] == nB_minus_nF_10R
        and ow11_cas["bulk_real_10"]["de_sitter_stabilizes_tau_star"] is True
    )
    ow11_10C_excluded = (
        ow11_cas["bulk_complex_10"]["n_B_minus_n_F_per_T2_pt"] == nB_minus_nF_10C
        and ow11_cas["bulk_complex_10"]["de_sitter_stabilizes_tau_star"] is False
    )

    s2_ok = (
        is_involution
        and trace_val == Fraction(-2, 1)
        and even_10R_dim == 4
        and odd_10R_dim == 6
        and even_10R_dim == claimed_even_10R
        and even_10C_dim == 8
        and (even_10R_dim // 4) == 1
        and (even_10C_dim // 4) == 2
        and reality_holds_all4
        and nB_minus_nF_10R == -1
        and nB_minus_nF_10C == 4
        and ow11_10R_ok
        and ow11_10C_excluded
    )
    return {
        "involution_sq_eq_I10": is_involution,
        "trace_neg_P_PS": str(trace_val),
        "real_10R_even_scalars": even_10R_dim,
        "real_10R_odd_triplets": odd_10R_dim,
        "real_10R_higgs_doublets": even_10R_dim // 4,
        "complex_10C_even_scalars": even_10C_dim,
        "complex_10C_higgs_doublets": even_10C_dim // 4,
        "quaternion_bidoublet_reality_verified": reality_holds_all4,
        "bulk_10R_nB_minus_nF": nB_minus_nF_10R,
        "bulk_10C_nB_minus_nF": nB_minus_nF_10C,
        "ow11_10C_AdS_excluded": ow11_10C_excluded,
        "claimed_even_10R_matches": (even_10R_dim == claimed_even_10R),
        "pass": s2_ok,
    }


def prove_s3_betas_and_B_ratio(
    claimed_unified_ps_continuous_count: int = 4,
) -> Dict[str, Any]:
    # First-principles 1-loop beta coefficients for G_SM = SU(3) x SU(2) x U(1)_Y (k_Y = 5/3)
    # b_a = -(11/3) C2(G_a) + (2/3) sum_Weyl S2(R_a) + (1/3) sum_cScalar S2(R_a)
    k_Y = Fraction(5, 3)
    inv_kY = Fraction(1, 1) / k_Y  # 3/5
    C2_G = (Fraction(0, 1), Fraction(2, 1), Fraction(3, 1))

    # One SM generation of Weyl fermions: (dim_SU3, dim_SU2, Y, S2_SU3_per_state, S2_SU2_per_state)
    # Using S2(fund) = 1/2, S2(singlet) = 0
    gen1_weyl = [
        # name, d3, d2, Y, T3_dynkin_mult, T2_dynkin_mult
        ("Q", 3, 2, Fraction(1, 6), Fraction(1, 2), Fraction(1, 2)),
        ("u_c", 3, 1, Fraction(-2, 3), Fraction(1, 2), Fraction(0, 1)),
        ("d_c", 3, 1, Fraction(1, 3), Fraction(1, 2), Fraction(0, 1)),
        ("L", 1, 2, Fraction(-1, 2), Fraction(0, 1), Fraction(1, 2)),
        ("e_c", 1, 1, Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)),
        ("nu_c", 1, 1, Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)),
    ]
    s2_1gen_u1 = sum(inv_kY * d3 * d2 * (y * y) for _, d3, d2, y, _, _ in gen1_weyl)
    s2_1gen_su2 = sum(d3 * t2 for _, d3, _, _, _, t2 in gen1_weyl)
    s2_1gen_su3 = sum(d2 * t3 for _, _, d2, _, t3, _ in gen1_weyl)
    spin10_16_equal_dynkin = (
        s2_1gen_u1 == Fraction(2, 1)
        and s2_1gen_su2 == Fraction(2, 1)
        and s2_1gen_su3 == Fraction(2, 1)
    )

    n_gen = 3

    def compute_betas_and_B(n_H: int) -> Tuple[Fraction, Fraction, Fraction, Fraction]:
        # Complex Higgs doublet: (1, 2, +-1/2)
        s2_H_u1 = inv_kY * 1 * 2 * Fraction(1, 4) * n_H
        s2_H_su2 = Fraction(1, 2) * n_H
        s2_H_su3 = Fraction(0, 1)
        b1 = (
            Fraction(-11, 3) * C2_G[0]
            + Fraction(2, 3) * n_gen * s2_1gen_u1
            + Fraction(1, 3) * s2_H_u1
        )
        b2 = (
            Fraction(-11, 3) * C2_G[1]
            + Fraction(2, 3) * n_gen * s2_1gen_su2
            + Fraction(1, 3) * s2_H_su2
        )
        b3 = (
            Fraction(-11, 3) * C2_G[2]
            + Fraction(2, 3) * n_gen * s2_1gen_su3
            + Fraction(1, 3) * s2_H_su3
        )
        B_ratio = (b2 - b3) / (b1 - b2)
        return b1, b2, b3, B_ratio

    b1_1H, b2_1H, b3_1H, B_1H = compute_betas_and_B(1)
    b1_2H, b2_2H, b3_2H, B_2H = compute_betas_and_B(2)
    B_target = Fraction(5, 7)

    # First-principles PS_122_412 check: SU(4)_C x SU(2)_L x SU(2)_R
    # 3 gen of (4,2,1)+(4bar,1,2) + complex (1,2,2) + extra complex (4,1,2)
    # Gauge C2: (4, 2, 2); Fermion S2 per gen: (2, 2, 2) -> 3 gen * 2/3 * 2 = 4 each
    b4_ps = Fraction(-11, 3) * 4 + 4 + Fraction(1, 3) * (2 * Fraction(1, 2))
    b2L_ps = Fraction(-11, 3) * 2 + 4 + Fraction(1, 3) * (2 * Fraction(1, 2))
    b2R_ps = (
        Fraction(-11, 3) * 2
        + 4
        + Fraction(1, 3) * (2 * Fraction(1, 2) + 4 * Fraction(1, 2))
    )
    b1eff_ps = Fraction(3, 5) * b2R_ps + Fraction(2, 5) * b4_ps
    # Solve [r_low * (b2_2H - b3_2H) + (1 - r_low) * (b2L_ps - b4_ps)] /
    #       [r_low * (b1_2H - b2_2H) + (1 - r_low) * (b1eff_ps - b2L_ps)] == 5/7
    # where r_low = ln(M_PS / M_Z) / ln(M_X / M_Z)
    num_sm = b2_2H - b3_2H
    den_sm = b1_2H - b2_2H
    num_ps = b2L_ps - b4_ps
    den_ps = b1eff_ps - b2L_ps
    # 7 * (r * num_sm + (1 - r) * num_ps) = 5 * (r * den_sm + (1 - r) * den_ps)
    lhs_r = 7 * (num_sm - num_ps) - 5 * (den_sm - den_ps)
    rhs_const = 5 * den_ps - 7 * num_ps
    r_low_exact = rhs_const / lhs_r
    B_eff_check = (
        r_low_exact * num_sm + (1 - r_low_exact) * num_ps
    ) / (
        r_low_exact * den_sm + (1 - r_low_exact) * den_ps
    )

    # Guardrail-5 continuous SM/UV dimensionless count:
    # Without PS threshold: 3 (g_UV, tan(beta), M_R/M_X)
    # With PS B=5/7 closure: 4 (g_UV, tan(beta), M_R/M_X, M_PS/M_X)
    no_ps_count = 3
    with_ps_count = 4
    ledger_ok = claimed_unified_ps_continuous_count == with_ps_count

    s3_ok = (
        spin10_16_equal_dynkin
        and (b1_1H, b2_1H, b3_1H, B_1H)
        == (Fraction(41, 10), Fraction(-19, 6), Fraction(-7, 1), Fraction(115, 218))
        and (b1_2H, b2_2H, b3_2H)
        == (Fraction(21, 5), Fraction(-3, 1), Fraction(-7, 1))
        and B_2H == Fraction(5, 9)
        and B_2H != B_target
        and (b4_ps, b2L_ps, b2R_ps, b1eff_ps)
        == (Fraction(-31, 3), Fraction(-3, 1), Fraction(-7, 3), Fraction(-83, 15))
        and r_low_exact == Fraction(8, 9)
        and B_eff_check == B_target
        and ledger_ok
    )
    return {
        "spin10_16_equal_dynkin_S2_eq_2": spin10_16_equal_dynkin,
        "1H_betas_and_B": {
            "b1": str(b1_1H),
            "b2": str(b2_1H),
            "b3": str(b3_1H),
            "B": str(B_1H),
        },
        "2H_betas_and_B": {
            "b1": str(b1_2H),
            "b2": str(b2_2H),
            "b3": str(b3_2H),
            "B": str(B_2H),
            "B_ne_5_over_7": (B_2H != B_target),
            "shortfall_5_over_7_minus_B": str(B_target - B_2H),
        },
        "ps_122_412_closure": {
            "b4": str(b4_ps),
            "b2L": str(b2L_ps),
            "b2R": str(b2R_ps),
            "b1_eff": str(b1eff_ps),
            "r_low_ln_MPS_over_MZ_div_ln_MX_over_MZ": str(r_low_exact),
            "B_eff_reconstructed": str(B_eff_check),
        },
        "guardrail5_continuous_without_ps_threshold": no_ps_count,
        "guardrail5_continuous_with_ps_threshold": with_ps_count,
        "claimed_unified_ps_count": claimed_unified_ps_continuous_count,
        "ledger_count_ok": ledger_ok,
        "pass": s3_ok,
    }


def prove_s4_weyl_clifford_all_5_ordered_signatures() -> Dict[str, Any]:
    # Independent 4x4 Weyl/chiral-basis Clifford construction for ALL 5 ordered D=4 signatures
    # t in {0, 1, 2, 3, 4}, s = 4 - t, metric eta = diag(-1^t, +1^s)
    # Build BOTH in mpmath (dps = 55) AND exact Q(i) for zero-roundoff Spin(t,s) L^* vs R proof.
    Z_mp = mp.mpc(0, 0)
    O_mp = mp.mpc(1, 0)

    def mp_zero4() -> mp.matrix:
        return mp.matrix(4, 4)

    def mp_eye4() -> mp.matrix:
        m = mp.matrix(4, 4)
        for i in range(4):
            m[i, i] = O_mp
        return m

    def mp_frob(m: mp.matrix) -> mp.mpf:
        acc = mp.mpf(0)
        for i in range(m.rows):
            for j in range(m.cols):
                acc += abs(m[i, j]) ** 2
        return mp.sqrt(acc)

    # Euclidean Weyl basis gE_a = [[0, A_a], [B_a, 0]] with {gE_a, gE_b} = 2 delta_{ab} I_4
    # A_0 = I2, B_0 = I2; A_k = -i sigma_k, B_k = +i sigma_k
    s_qi: Dict[int, List[List[QI]]] = {
        0: [[QI_ONE, QI_ZERO], [QI_ZERO, QI_ONE]],
        1: [[QI_ZERO, QI_ONE], [QI_ONE, QI_ZERO]],
        2: [[QI_ZERO, qi_neg(QI_I)], [QI_I, QI_ZERO]],
        3: [[QI_ONE, QI_ZERO], [QI_ZERO, qi_neg(QI_ONE)]],
    }

    def qi_to_mpc(z: QI) -> mp.mpc:
        return mp.mpc(
            mp.mpf(z[0].numerator) / mp.mpf(z[0].denominator),
            mp.mpf(z[1].numerator) / mp.mpf(z[1].denominator),
        )

    def build_block_offdiag_qi(
        upper_right: List[List[QI]], lower_left: List[List[QI]]
    ) -> List[List[QI]]:
        mat = [[QI_ZERO for _ in range(4)] for _ in range(4)]
        for r in range(2):
            for c in range(2):
                mat[r][c + 2] = upper_right[r][c]
                mat[r + 2][c] = lower_left[r][c]
        return mat

    gE_qi: List[List[List[QI]]] = []
    # a = 0: [[0, I2], [I2, 0]]
    gE_qi.append(build_block_offdiag_qi(s_qi[0], s_qi[0]))
    # a = 1, 2, 3: [[0, -i s_a], [i s_a, 0]]
    for k in (1, 2, 3):
        ur = [[qi_mul(qi_neg(QI_I), s_qi[k][r][c]) for c in range(2)] for r in range(2)]
        ll = [[qi_mul(QI_I, s_qi[k][r][c]) for c in range(2)] for r in range(2)]
        gE_qi.append(build_block_offdiag_qi(ur, ll))

    def qi_mat4_mul(a: List[List[QI]], b: List[List[QI]]) -> List[List[QI]]:
        out = [[QI_ZERO for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                acc = QI_ZERO
                for k in range(4):
                    acc = qi_add(acc, qi_mul(a[i][k], b[k][j]))
                out[i][j] = acc
        return out

    def qi_intertwiner_dim_and_inv(
        reps_src: List[List[List[QI]]], reps_dst: List[List[List[QI]]]
    ) -> Tuple[int, bool]:
        # Solve X * src_m - dst_m * X = 0 for 2x2 matrix X = [[x0, x1], [x2, x3]] over Q(i)
        rows: List[List[QI]] = []
        for A, B in zip(reps_src, reps_dst):
            for i in range(2):
                for j in range(2):
                    # (X A - B X)_{ij} = sum_k X_{ik} A_{kj} - sum_k B_{ik} X_{kj}
                    row = [QI_ZERO, QI_ZERO, QI_ZERO, QI_ZERO]
                    for k in range(2):
                        # X_{ik} is index 2*i + k
                        row[2 * i + k] = qi_add(row[2 * i + k], A[k][j])
                        # X_{kj} is index 2*k + j
                        row[2 * k + j] = qi_sub(row[2 * k + j], B[i][k])
                    rows.append(row)
        basis = nullspace_qi(rows)
        has_invertible = False
        for v in basis:
            det_v = qi_sub(qi_mul(v[0], v[3]), qi_mul(v[1], v[2]))
            if not qi_is_zero(det_v):
                has_invertible = True
        return len(basis), has_invertible

    tol_40 = mp.mpf(1) / mp.mpf(10) ** 40
    sig_results: Dict[str, Dict[str, Any]] = {}
    complex_chiral_sigs: List[str] = []
    hyperbolic_complex_chiral_sigs: List[str] = []
    euclidean_fiber_hits: List[str] = []

    quarter_qi: QI = (Fraction(1, 4), Fraction(0, 1))

    for t in range(5):
        s = 4 - t
        label = f"({t},{s})"
        eta = [-1 if a < t else 1 for a in range(4)]

        # Build gamma_a in Q(i) and mpmath: gamma_a = i * gE_a for a < t, else gE_a
        gammas_qi: List[List[List[QI]]] = []
        gammas_mp: List[mp.matrix] = []
        for a in range(4):
            fac = QI_I if a < t else QI_ONE
            g_q = [
                [qi_mul(fac, gE_qi[a][r][c]) for c in range(4)]
                for r in range(4)
            ]
            gammas_qi.append(g_q)
            gm = mp_zero4()
            for r in range(4):
                for c in range(4):
                    gm[r, c] = qi_to_mpc(g_q[r][c])
            gammas_mp.append(gm)

        # Verify {gamma_a, gamma_b} = 2 eta_{ab} I_4 in mpmath to < 1e-40
        I4_mp = mp_eye4()
        max_cliff_err = mp.mpf(0)
        for a in range(4):
            for b in range(4):
                anticomm = gammas_mp[a] * gammas_mp[b] + gammas_mp[b] * gammas_mp[a]
                rhs = (mp.mpf(2 * eta[a]) if a == b else Z_mp) * I4_mp
                err = mp_frob(anticomm - rhs)
                if err > max_cliff_err:
                    max_cliff_err = err

        # Compute volume element omega = g0 g1 g2 g3 and omega^2 in mpmath
        omega_mp = gammas_mp[0] * gammas_mp[1] * gammas_mp[2] * gammas_mp[3]
        omega_sq_mp = omega_mp * omega_mp
        expected_sign = -1 if (t % 2 == 1) else 1
        vol_sq_err = mp_frob(omega_sq_mp - mp.mpf(expected_sign) * I4_mp)

        # Build Spin(t, s) generators Sigma_{ab} = (1/4) [gamma_a, gamma_b] in Q(i)
        # Verify strictly block-diagonal diag(L_{ab}, R_{ab}) and solve L^* ~= L vs L^* ~= R
        L_reps: List[List[List[QI]]] = []
        L_conj_reps: List[List[List[QI]]] = []
        R_reps: List[List[List[QI]]] = []
        block_diag_exact = True
        for a in range(4):
            for b in range(a + 1, 4):
                ab = qi_mat4_mul(gammas_qi[a], gammas_qi[b])
                ba = qi_mat4_mul(gammas_qi[b], gammas_qi[a])
                sig_ab = [
                    [
                        qi_mul(quarter_qi, qi_sub(ab[r][c], ba[r][c]))
                        for c in range(4)
                    ]
                    for r in range(4)
                ]
                for r in range(2):
                    for c in range(2):
                        if not qi_is_zero(sig_ab[r][c + 2]) or not qi_is_zero(
                            sig_ab[r + 2][c]
                        ):
                            block_diag_exact = False
                L_m = [[sig_ab[r][c] for c in range(2)] for r in range(2)]
                L_c = [[qi_conj(sig_ab[r][c]) for c in range(2)] for r in range(2)]
                R_m = [[sig_ab[r + 2][c + 2] for c in range(2)] for r in range(2)]
                L_reps.append(L_m)
                L_conj_reps.append(L_c)
                R_reps.append(R_m)

        dim_L_self, inv_L_self = qi_intertwiner_dim_and_inv(L_conj_reps, L_reps)
        dim_L_to_R, inv_L_to_R = qi_intertwiner_dim_and_inv(L_conj_reps, R_reps)

        is_complex_chiral = (
            expected_sign == -1
            and vol_sq_err < tol_40
            and dim_L_to_R == 1
            and inv_L_to_R
            and dim_L_self == 0
        )
        if is_complex_chiral:
            complex_chiral_sigs.append(label)
        if is_complex_chiral and t == 1:
            hyperbolic_complex_chiral_sigs.append(label)

        # Euclidean T^2 fiber addition: (t, s) + (0, 2) = (t, s + 2)
        fiber_6d = (t, s + 2)
        fiber_7d = (t, s + 3)
        matches_1_5_fiber = (fiber_6d == (1, 5))
        if is_complex_chiral and matches_1_5_fiber:
            euclidean_fiber_hits.append(label)

        sig_results[label] = {
            "t": t,
            "s": s,
            "eta_diag": eta,
            "max_clifford_anticomm_err": mp.nstr(max_cliff_err, 12),
            "clifford_verified_lt_1e40": max_cliff_err < tol_40,
            "vol_sq_sign": expected_sign,
            "vol_sq_err": mp.nstr(vol_sq_err, 12),
            "spin_generators_block_diagonal_exact": block_diag_exact,
            "dim_Hom_Lstar_to_L": dim_L_self,
            "invertible_Lstar_to_L": inv_L_self,
            "dim_Hom_Lstar_to_R": dim_L_to_R,
            "invertible_Lstar_to_R": inv_L_to_R,
            "weyl_Lstar_eq_R": is_complex_chiral,
            "hyperbolic_t_eq_1": (t == 1),
            "euclidean_fiber_tower": [
                [t, s],
                [fiber_6d[0], fiber_6d[1]],
                [fiber_7d[0], fiber_7d[1]],
            ],
            "matches_6D_1_5_fiber": matches_1_5_fiber,
        }

    # Explicit tower counting distinction:
    # Ordered Euclidean-fibered D=4 -> 6 -> 7 towers: 5 (one for each t in 0..4)
    # Unordered Cartesian product across D=4 (3), D=6 (4), D=7 (4): 3 * 4 * 4 = 48
    ordered_fibered_towers_count = 5
    unordered_d4 = len({tuple(sorted((t, 4 - t))) for t in range(5)})
    unordered_d6 = len({tuple(sorted((t, 6 - t))) for t in range(7)})
    unordered_d7 = len({tuple(sorted((t, 7 - t))) for t in range(8)})
    cartesian_unordered_triples = unordered_d4 * unordered_d6 * unordered_d7

    all_cliff_ok = all(
        v["clifford_verified_lt_1e40"]
        and v["spin_generators_block_diagonal_exact"]
        and parse_mpf(v["vol_sq_err"]) < tol_40
        for v in sig_results.values()
    )
    s4_ok = (
        all_cliff_ok
        and complex_chiral_sigs == ["(1,3)", "(3,1)"]
        and hyperbolic_complex_chiral_sigs == ["(1,3)"]
        and euclidean_fiber_hits == ["(1,3)"]
        and ordered_fibered_towers_count == 5
        and unordered_d4 == 3
        and unordered_d6 == 4
        and unordered_d7 == 4
        and cartesian_unordered_triples == 48
    )
    return {
        "signatures": sig_results,
        "complex_chiral_Lstar_eq_R_ordered": complex_chiral_sigs,
        "selected_by_hyperbolicity_t1": hyperbolic_complex_chiral_sigs,
        "selected_by_euclidean_fiber_1_5": euclidean_fiber_hits,
        "ordered_fibered_tower_space_size": ordered_fibered_towers_count,
        "unordered_counts_D4_D6_D7": [unordered_d4, unordered_d6, unordered_d7],
        "unordered_cartesian_product_size": cartesian_unordered_triples,
        "pass": s4_ok,
    }


def prove_s6_ow14_exact_arithmetic(
    ow14: Any, claimed_cap22_theta_g: Fraction | None = None
) -> Dict[str, Any]:
    M_g = 8
    theta_cap22 = Fraction(2 * (22 - M_g), 21 - M_g)
    theta_cap23 = Fraction(2 * (23 - M_g), 22 - M_g)
    wrong_7_over_3 = Fraction(7, 3)

    ow14_frg = ow14["ow14_b"]["unimodular_and_sequestering"]["unimodular_frg"]
    ow14_cap22_str = ow14_frg["traceless_cap22"]["spectra"]["gsm_2h_Ngen3"][
        "theta_g"
    ]
    ow14_cap23_str = ow14_frg["full_lam0_cap23"]["spectra"]["gsm_2h_Ngen3"][
        "theta_g"
    ]
    diff_cap22_json = abs(parse_mpf(ow14_cap22_str) - parse_mpf(theta_cap22))
    diff_cap23_json = abs(parse_mpf(ow14_cap23_str) - parse_mpf(theta_cap23))
    tol_15 = mp.mpf(1) / mp.mpf(10) ** 15

    target_val = theta_cap22 if claimed_cap22_theta_g is None else claimed_cap22_theta_g
    claimed_ok = target_val == Fraction(28, 13)

    s6_ok = (
        theta_cap22 == Fraction(28, 13)
        and theta_cap22 != wrong_7_over_3
        and (wrong_7_over_3 - theta_cap22) == Fraction(7, 39)
        and theta_cap23 == Fraction(15, 7)
        and diff_cap22_json < tol_15
        and diff_cap23_json < tol_15
        and claimed_ok
    )
    return {
        "M_g": M_g,
        "cap22_theta_g_exact": str(theta_cap22),
        "cap22_ne_7_over_3": theta_cap22 != wrong_7_over_3,
        "difference_7_over_3_minus_28_over_13": str(wrong_7_over_3 - theta_cap22),
        "cap23_theta_g_exact": str(theta_cap23),
        "ow14_json_cap22_theta_g": ow14_cap22_str,
        "ow14_json_cap22_abs_err": mp.nstr(diff_cap22_json, 12),
        "ow14_json_cap23_theta_g": ow14_cap23_str,
        "ow14_json_cap23_abs_err": mp.nstr(diff_cap23_json, 12),
        "claimed_theta_g": str(target_val),
        "claimed_matches_28_over_13": claimed_ok,
        "pass": s6_ok,
    }


# ---------------------------------------------------------------------------
# Task 4: 24-Observable Partition Validator (used for real data & PF-3)
# ---------------------------------------------------------------------------

EXPECTED_PARTITION: Dict[str, List[str]] = {
    "DERIVED_EXACT": [
        "OBS-01", "OBS-02", "OBS-03", "OBS-04", "OBS-05",
        "OBS-06", "OBS-07", "OBS-09", "OBS-10",
    ],
    "CONDITIONAL_OR_QUALITATIVE": [
        "OBS-08", "OBS-11", "OBS-12", "OBS-13", "OBS-14", "OBS-15",
    ],
    "INTERNAL_WALL_OR_TENSION": [
        "OBS-16", "OBS-17", "OBS-18", "OBS-19", "OBS-20", "OBS-21",
    ],
    "OPEN_EXTERNAL_BOUNDARY": [
        "OBS-22", "OBS-23", "OBS-24",
    ],
}


def validate_24_partition(buckets: Dict[str, List[str]]) -> Dict[str, Any]:
    expected_counts = {
        "DERIVED_EXACT": 9,
        "CONDITIONAL_OR_QUALITATIVE": 6,
        "INTERNAL_WALL_OR_TENSION": 6,
        "OPEN_EXTERNAL_BOUNDARY": 3,
    }
    actual_counts = {k: len(buckets.get(k, [])) for k in expected_counts}
    all_ids: List[str] = []
    for k in expected_counts:
        all_ids.extend(buckets.get(k, []))
    expected_all = [f"OBS-{i:02d}" for i in range(1, 25)]
    unique_exact_24 = (
        len(all_ids) == 24
        and len(set(all_ids)) == 24
        and sorted(all_ids) == expected_all
    )
    obs08_conditional = (
        "OBS-08" in buckets.get("CONDITIONAL_OR_QUALITATIVE", [])
        and "OBS-08" not in buckets.get("DERIVED_EXACT", [])
    )
    obs11_conditional = (
        "OBS-11" in buckets.get("CONDITIONAL_OR_QUALITATIVE", [])
        and "OBS-11" not in buckets.get("DERIVED_EXACT", [])
    )
    counts_match = actual_counts == expected_counts
    exact_sets_match = all(
        sorted(buckets.get(k, [])) == sorted(EXPECTED_PARTITION[k])
        for k in expected_counts
    )
    ok = (
        unique_exact_24
        and counts_match
        and obs08_conditional
        and obs11_conditional
        and exact_sets_match
    )
    return {
        "counts": actual_counts,
        "total": len(all_ids),
        "unique_exact_24": unique_exact_24,
        "obs08_in_conditional": obs08_conditional,
        "obs11_in_conditional": obs11_conditional,
        "exact_sets_match": exact_sets_match,
        "pass": ok,
    }


# ---------------------------------------------------------------------------
# Task 5: 6 / 6 Independent Planted-Fault Controls (PF-1..PF-6)
# ---------------------------------------------------------------------------

def run_6_planted_fault_controls(ow: Dict[str, Any]) -> Dict[str, Any]:
    controls: Dict[str, Dict[str, Any]] = {}

    # PF-1: 1-byte tamper on relays/a2_ow15/a2_ow15_results.json -> manifest MUST fail
    ow15_path = os.path.join(REPO_ROOT, OW_PRODUCER_JSON_RELPATHS["OW15"])
    with open(ow15_path, "rb") as fh:
        raw_ow15 = bytearray(fh.read())
    raw_ow15[0] ^= 1
    pf1_res = verify_single_manifest(
        "a2_ow15", "OUTPUT_SHA256.txt", override_bytes=bytes(raw_ow15)
    )
    controls["PF-1"] = {
        "description": "1-byte tamper on a2_ow15_results.json",
        "manifest_ok_under_fault": pf1_res["ok"],
        "detected": (pf1_res["ok"] is False),
    }

    # PF-2: Perturb OW15 c_log_total from 16 to 15 -> LOCK-6 MUST fail
    ow15_corrupt = json.loads(json.dumps(ow["OW15"]))
    ow15_corrupt["ow15_b"]["conformal_bh_entropy"]["spin10_induced_bh_entropy"][
        "c_log_total"
    ] = "15"
    pf2_res = check_lock_6_from_data(ow["OW8"], ow15_corrupt)
    controls["PF-2"] = {
        "description": "Perturb OW15 c_log_total from 16 to 15",
        "lock6_ok_under_fault": pf2_res["pass"],
        "detected": (pf2_res["pass"] is False),
    }

    # PF-3: Keep OBS-08 or OBS-11 in DERIVED_EXACT -> S3/S5 partition check MUST fail
    bad_p_08 = {k: list(v) for k, v in EXPECTED_PARTITION.items()}
    bad_p_08["CONDITIONAL_OR_QUALITATIVE"].remove("OBS-08")
    bad_p_08["DERIVED_EXACT"].append("OBS-08")
    res_p_08 = validate_24_partition(bad_p_08)

    bad_p_11 = {k: list(v) for k, v in EXPECTED_PARTITION.items()}
    bad_p_11["CONDITIONAL_OR_QUALITATIVE"].remove("OBS-11")
    bad_p_11["DERIVED_EXACT"].append("OBS-11")
    res_p_11 = validate_24_partition(bad_p_11)

    controls["PF-3"] = {
        "description": "Keep OBS-08 or OBS-11 in DERIVED_EXACT",
        "ok_when_OBS08_derived": res_p_08["pass"],
        "ok_when_OBS11_derived": res_p_11["pass"],
        "detected": (res_p_08["pass"] is False and res_p_11["pass"] is False),
    }

    # PF-4: Omit M_PS / M_X from unified PS ratio count (3 instead of 4) -> S3 ledger MUST fail
    pf4_res = prove_s3_betas_and_B_ratio(claimed_unified_ps_continuous_count=3)
    controls["PF-4"] = {
        "description": "Omit M_PS / M_X from unified PS continuous count (3 instead of 4)",
        "s3_ok_under_fault": pf4_res["pass"],
        "detected": (pf4_res["pass"] is False),
    }

    # PF-5: Claim 10_R gives 8 even real scalars -> S2 check MUST fail
    pf5_res = prove_s2_10R_vs_10C_orbifold(ow["OW11"], claimed_even_10R=8)
    controls["PF-5"] = {
        "description": "Claim real 10_R yields 8 even real scalars under -P_PS",
        "s2_ok_under_fault": pf5_res["pass"],
        "detected": (pf5_res["pass"] is False),
    }

    # PF-6: Substitute 7/3 for 28/13 in traceless cap=22 theta_g -> S6 check MUST fail
    pf6_res = prove_s6_ow14_exact_arithmetic(
        ow["OW14"], claimed_cap22_theta_g=Fraction(7, 3)
    )
    controls["PF-6"] = {
        "description": "Substitute 7/3 for 28/13 in OW14 traceless cap=22 theta_g",
        "s6_ok_under_fault": pf6_res["pass"],
        "detected": (pf6_res["pass"] is False),
    }

    detected_count = sum(1 for c in controls.values() if c["detected"])
    return {
        "controls": controls,
        "detected_count": detected_count,
        "total_count": len(controls),
        "pass": (detected_count == 6 and len(controls) == 6),
    }


# ---------------------------------------------------------------------------
# Task 6: Self AST Hygiene Check & Cross-Comparison Against Producer JSON
# ---------------------------------------------------------------------------

def self_ast_hygiene_check() -> Dict[str, Any]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src)
    float_complex_literals = 0
    forbidden_imports: List[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(
            node.value, (float, complex)
        ):
            float_complex_literals += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if "verify_a2_ow16" in alias.name or "frontier" in alias.name:
                    forbidden_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if "verify_a2_ow16" in mod or "frontier" in mod:
                forbidden_imports.append(mod)
    return {
        "float_or_complex_ast_literals": float_complex_literals,
        "forbidden_imports": forbidden_imports,
        "pass": (float_complex_literals == 0 and len(forbidden_imports) == 0),
    }


def cross_check_producer_json(
    independent: Dict[str, Any],
) -> Dict[str, Any]:
    prod = load_json_exact(PRODUCER_JSON_PATH)
    checks: Dict[str, Dict[str, Any]] = {}
    tol_10 = mp.mpf(1) / mp.mpf(10) ** 10

    def rec(ok: bool, detail: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "verdict": "the same" if ok else "differs",
            "match": ok,
            "detail": detail,
        }

    # 1. Cross-check 64 historical manifests byte-for-byte
    ref_hist_by_path: Dict[str, Dict[str, Any]] = {
        f"relays/{r['dir']}/{r['manifest']}": r
        for r in independent["manifests_66"]["historical_manifests"]
    }
    prod_manifests = prod["ow16v3_a"]["custody_manifests"]
    hist_diffs: List[str] = []
    if len(prod_manifests) != 64:
        hist_diffs.append(f"len={len(prod_manifests)} != 64")
    for pm in prod_manifests:
        mpath = pm["manifest"]
        if mpath not in ref_hist_by_path:
            hist_diffs.append(f"unexpected:{mpath}")
            continue
        rm = ref_hist_by_path[mpath]
        if (
            pm["computed_sha256"] != rm["computed_sha256"]
            or pm["expected_sha256"] != rm["recorded_sha256"]
            or pm["target"] != rm["target"]
            or pm["match"] is not True
        ):
            hist_diffs.append(f"mismatch:{mpath}")
    m64_ok = (
        prod["ow16v3_a"]["custody_manifests_total"] == 64
        and prod["ow16v3_a"]["custody_manifests_verified"] == 64
        and len(hist_diffs) == 0
        and independent["manifests_66"]["pass"]
    )
    checks["manifests_64_historical_plus_2_v4"] = rec(
        m64_ok,
        {
            "producer_historical_verified": prod["ow16v3_a"][
                "custody_manifests_verified"
            ],
            "referee_total_verified": independent["manifests_66"][
                "total_verified"
            ],
            "referee_total_checked": independent["manifests_66"][
                "total_checked"
            ],
            "diff_count": len(hist_diffs),
            "diffs": hist_diffs,
        },
    )

    # 2. Cross-check 10 cross-card locks + LOCK-7 max relative error
    prod_locks = prod["ow16v3_a"]["cross_card_locks"]
    ref_lock7_err = parse_mpf(
        independent["cross_card_locks_10"]["locks"]["LOCK-7"]["max_rel_err"]
    )
    prod_lock7_err = parse_mpf(prod_locks["lock_7_max_rel_diff"])
    lock7_rel_diff = (
        abs(ref_lock7_err - prod_lock7_err) / abs(ref_lock7_err)
        if ref_lock7_err != 0
        else abs(ref_lock7_err - prod_lock7_err)
    )
    locks_ok = (
        prod_locks["locks_passed"] == 10
        and prod_locks["total_locks"] == 10
        and prod_locks["all_locks_passed"] is True
        and all(v is True for v in prod_locks["locks"].values())
        and len(prod_locks["locks"]) == 10
        and independent["cross_card_locks_10"]["pass"]
        and lock7_rel_diff < tol_10
    )
    checks["cross_card_locks_10"] = rec(
        locks_ok,
        {
            "producer_passed": prod_locks["locks_passed"],
            "referee_passed": independent["cross_card_locks_10"]["passed_count"],
            "producer_lock7_max_rel_diff": prod_locks["lock_7_max_rel_diff"],
            "referee_lock7_max_rel_diff": independent["cross_card_locks_10"][
                "locks"
            ]["LOCK-7"]["max_rel_err"],
            "lock7_comparison_rel_diff": mp.nstr(lock7_rel_diff, 12),
        },
    )

    # 3. Cross-check S1
    p_s1 = prod["ow16v3_b"]["c25_remediation_proofs"][
        "S1_m004_equivariance_and_bits"
    ]
    r_s1 = independent["algebraic_proofs"]["S1"]
    s1_bits_diff = abs(
        parse_mpf(p_s1["discrete_bits_before_ansatz"])
        - parse_mpf(r_s1["log2_18_bits"])
    )
    s1_ok = (
        r_s1["pass"]
        and p_s1["pass"] is True
        and p_s1["m004_is_transitive_3cycle"] is True
        and p_s1["distinct_diag_breaks_m004"] is True
        and p_s1["discrete_states_6perms_x_3mL"] == r_s1["discrete_states"]
        and s1_bits_diff < tol_10
    )
    checks["S1_m004_3cycle_and_log2_18"] = rec(
        s1_ok,
        {
            "producer_states": p_s1["discrete_states_6perms_x_3mL"],
            "referee_states": r_s1["discrete_states"],
            "producer_bits": p_s1["discrete_bits_before_ansatz"],
            "referee_bits": r_s1["log2_18_bits"],
            "bits_abs_diff": mp.nstr(s1_bits_diff, 12),
        },
    )

    # 4. Cross-check S2
    p_s2 = prod["ow16v3_b"]["c25_remediation_proofs"]["S2_real10_vs_2hdm_seam"]
    r_s2 = independent["algebraic_proofs"]["S2"]
    s2_ok = (
        r_s2["pass"]
        and p_s2["pass"] is True
        and p_s2["even_real_scalars_in_10R"] == r_s2["real_10R_even_scalars"]
        and p_s2["even_real_scalars_in_10C_2H"] == r_s2["complex_10C_even_scalars"]
        and p_s2["real_10R_yields_only_1H_not_2H"] is True
    )
    checks["S2_10R_vs_10C_even_scalars"] = rec(
        s2_ok,
        {
            "producer_10R": p_s2["even_real_scalars_in_10R"],
            "referee_10R": r_s2["real_10R_even_scalars"],
            "producer_10C": p_s2["even_real_scalars_in_10C_2H"],
            "referee_10C": r_s2["complex_10C_even_scalars"],
        },
    )

    # 5. Cross-check S3
    p_s3 = prod["ow16v3_b"]["c25_remediation_proofs"][
        "S3_unification_threshold_and_mps_ratio"
    ]
    r_s3 = independent["algebraic_proofs"]["S3"]
    s3_ok = (
        r_s3["pass"]
        and p_s3["pass"] is True
        and parse_frac(p_s3["b1_2h"]) == parse_frac(r_s3["2H_betas_and_B"]["b1"])
        and parse_frac(p_s3["b2_2h"]) == parse_frac(r_s3["2H_betas_and_B"]["b2"])
        and parse_frac(p_s3["b3_2h"]) == parse_frac(r_s3["2H_betas_and_B"]["b3"])
        and parse_frac(p_s3["B_2h_no_threshold"])
        == parse_frac(r_s3["2H_betas_and_B"]["B"])
        and parse_frac(p_s3["B_target"]) == Fraction(5, 7)
        and p_s3["no_threshold_misses_5_7"] is True
    )
    checks["S3_2H_betas_and_B_5_9"] = rec(
        s3_ok,
        {
            "producer_betas": [p_s3["b1_2h"], p_s3["b2_2h"], p_s3["b3_2h"]],
            "referee_betas": [
                r_s3["2H_betas_and_B"]["b1"],
                r_s3["2H_betas_and_B"]["b2"],
                r_s3["2H_betas_and_B"]["b3"],
            ],
            "producer_B": p_s3["B_2h_no_threshold"],
            "referee_B": r_s3["2H_betas_and_B"]["B"],
        },
    )

    # 6. Cross-check S4 across all 5 ordered D=4 signatures
    p_s4 = prod["ow16v3_b"]["c25_remediation_proofs"][
        "S4_ordered_d4_clifford_and_towers"
    ]
    r_s4 = independent["algebraic_proofs"]["S4"]
    s4_table_diffs: List[str] = []
    if len(p_s4["ordered_d4_table"]) != 5:
        s4_table_diffs.append("table_len != 5")
    for row in p_s4["ordered_d4_table"]:
        t_val, s_val = row["signature"]
        key = f"({t_val},{s_val})"
        ref_row = r_s4["signatures"].get(key)
        if ref_row is None:
            s4_table_diffs.append(f"missing:{key}")
            continue
        if (
            row["vol2_sign"] != ref_row["vol_sq_sign"]
            or row["weyl_Lstar_eq_R"] != ref_row["weyl_Lstar_eq_R"]
            or row["hyperbolic_t_eq_1"] != ref_row["hyperbolic_t_eq_1"]
            or row["euclidean_fiber_6d"] != ref_row["euclidean_fiber_tower"][1]
            or row["euclidean_fiber_7d"] != ref_row["euclidean_fiber_tower"][2]
            or row["fiber_6d_is_lorentzian_1_5"]
            != ref_row["matches_6D_1_5_fiber"]
        ):
            s4_table_diffs.append(f"row_diff:{key}")
    s4_ok = (
        r_s4["pass"]
        and p_s4["pass"] is True
        and len(s4_table_diffs) == 0
        and p_s4["weyl_Lstar_eq_R_signatures"] == [[1, 3], [3, 1]]
        and p_s4["both_13_and_31_weyl_c"] is True
        and p_s4["unique_13_after_t1_or_euclidean_fiber"] is True
        and p_s4["ordered_fiber_consistent_tower_count"]
        == r_s4["ordered_fibered_tower_space_size"]
        and p_s4["unordered_cartesian_triple_count"]
        == r_s4["unordered_cartesian_product_size"]
    )
    checks["S4_ordered_D4_clifford_and_towers"] = rec(
        s4_ok,
        {
            "table_diffs": s4_table_diffs,
            "producer_ordered_towers": p_s4[
                "ordered_fiber_consistent_tower_count"
            ],
            "referee_ordered_towers": r_s4["ordered_fibered_tower_space_size"],
            "producer_cartesian_triples": p_s4[
                "unordered_cartesian_triple_count"
            ],
            "referee_cartesian_triples": r_s4[
                "unordered_cartesian_product_size"
            ],
        },
    )

    # 7. Cross-check S6
    p_s6 = prod["ow16v3_b"]["c25_remediation_proofs"]["S6_ow14_cap22_theta_g"]
    r_s6 = independent["algebraic_proofs"]["S6"]
    s6_ok = (
        r_s6["pass"]
        and p_s6["pass"] is True
        and parse_frac(p_s6["exact_theta_g_cap22"]) == Fraction(28, 13)
        and parse_frac(p_s6["card_line58_typo"]) == Fraction(7, 3)
        and p_s6["exact_is_28_13_not_7_3"] is True
        and len(p_s6["mended_expectations_cards_section12"]) == 6
    )
    checks["S6_ow14_cap22_28_over_13"] = rec(
        s6_ok,
        {
            "producer_exact": p_s6["exact_theta_g_cap22"],
            "referee_exact": r_s6["cap22_theta_g_exact"],
            "mended_cards_count": len(
                p_s6["mended_expectations_cards_section12"]
            ),
        },
    )

    # 8. Cross-check 24-observable partition (independent recount from rows!)
    p_led = prod["ow16v3_c"]["blind_prediction_ledger_24_corrected"]
    recounted: Dict[str, List[str]] = {
        "DERIVED_EXACT": [],
        "CONDITIONAL_OR_QUALITATIVE": [],
        "INTERNAL_WALL_OR_TENSION": [],
        "OPEN_EXTERNAL_BOUNDARY": [],
    }
    row_by_id: Dict[str, Dict[str, Any]] = {}
    unknown_buckets: List[str] = []
    for row in p_led["rows"]:
        b = row["bucket"]
        rid = row["id"]
        row_by_id[rid] = row
        if b in recounted:
            recounted[b].append(rid)
        else:
            unknown_buckets.append(f"{rid}:{b}")
    part_val = validate_24_partition(recounted)
    subtags_ok = (
        row_by_id.get("OBS-08", {}).get("subtag") == "CONDITIONAL_THRESHOLD"
        and row_by_id.get("OBS-11", {}).get("subtag")
        == "CONDITIONAL_GRAVITY_POSTULATE"
        and row_by_id.get("OBS-12", {}).get("subtag") == "CONDITIONAL_ANSATZ"
    )
    part_ok = (
        part_val["pass"]
        and len(unknown_buckets) == 0
        and p_led["total_observables"] == 24
        and p_led["counts_by_bucket"] == part_val["counts"]
        and p_led["obs08_reclassified_conditional"] is True
        and p_led["obs11_reclassified_conditional"] is True
        and subtags_ok
    )
    checks["partition_24_and_OBS08_OBS11"] = rec(
        part_ok,
        {
            "recounted_counts": part_val["counts"],
            "producer_counts": p_led["counts_by_bucket"],
            "obs08_in_conditional": part_val["obs08_in_conditional"],
            "obs11_in_conditional": part_val["obs11_in_conditional"],
            "subtags_ok": subtags_ok,
            "unknown_buckets": unknown_buckets,
        },
    )

    # 9. Cross-check Guardrail-5 continuous counts (3 without PS vs 4 with PS)
    p_g5 = prod["ow16v3_c"]["guardrail5_input_ledger_corrected"]
    g5_bits_diff = abs(
        parse_mpf(
            p_g5["discrete_flavor_selection_before_ansatz"]["bits_exact_log2_18"]
        )
        - parse_mpf(r_s1["log2_18_bits"])
    )
    g5_ok = (
        p_g5["dimensionful_unit_anchors"] == 1
        and p_g5["guardrail5_anchor_limit_ok"] is True
        and p_g5["campaign1_sm_uv_count"] == 4
        and len(p_g5["campaign1_sm_uv_ratios"]) == 4
        and p_g5["campaign2_no_ps_threshold_count"] == 3
        and len(p_g5["campaign2_no_ps_threshold_ratios"]) == 3
        and "M_PS / M_X" not in p_g5["campaign2_no_ps_threshold_ratios"]
        and p_g5["campaign2_with_ps_threshold_count"] == 4
        and len(p_g5["campaign2_with_ps_threshold_ratios"]) == 4
        and "M_PS / M_X" in p_g5["campaign2_with_ps_threshold_ratios"]
        and p_g5["campaign2_with_ps_delta_vs_c1"] == 0
        and p_g5["ps_ratio_honestly_counted"] is True
        and p_g5["discrete_flavor_selection_before_ansatz"][
            "total_discrete_states"
        ]
        == 18
        and g5_bits_diff < tol_10
    )
    checks["guardrail5_continuous_3_vs_4"] = rec(
        g5_ok,
        {
            "without_ps_count": p_g5["campaign2_no_ps_threshold_count"],
            "without_ps_ratios": p_g5["campaign2_no_ps_threshold_ratios"],
            "with_ps_count": p_g5["campaign2_with_ps_threshold_count"],
            "with_ps_ratios": p_g5["campaign2_with_ps_threshold_ratios"],
            "with_ps_delta_vs_c1": p_g5["campaign2_with_ps_delta_vs_c1"],
            "discrete_states": p_g5["discrete_flavor_selection_before_ansatz"][
                "total_discrete_states"
            ],
            "discrete_bits_abs_diff": mp.nstr(g5_bits_diff, 12),
        },
    )

    # 10. Cross-check 6 / 6 planted-fault controls
    p_pf = prod["ow16v3_d"]
    pf_keys = [
        "pf_ow16v3_1_tamper_1byte_manifest",
        "pf_ow16v3_2_perturb_ow15_clog_15",
        "pf_ow16v3_3_keep_obs08_11_derived",
        "pf_ow16v3_4_omit_mps_ratio_from_ps",
        "pf_ow16v3_5_claim_10R_gives_8_real",
        "pf_ow16v3_6_cap22_typo_7_3",
    ]
    pf_ok = (
        independent["planted_faults_6"]["pass"]
        and p_pf["planted_faults_caught"] == 6
        and p_pf["planted_faults_total"] == 6
        and p_pf["gate_pass"] is True
        and all(p_pf[k]["detected"] is True for k in pf_keys)
    )
    checks["planted_faults_6_of_6"] = rec(
        pf_ok,
        {
            "producer_caught": p_pf["planted_faults_caught"],
            "referee_caught": independent["planted_faults_6"]["detected_count"],
        },
    )

    all_match = all(c["match"] for c in checks.values())
    return {
        "producer_all_gates_passed": prod["all_gates_passed"],
        "producer_empirical_inputs": prod["empirical_inputs"],
        "checks": checks,
        "discrepancy_count": sum(1 for c in checks.values() if not c["match"]),
        "overall_verdict": "the same" if all_match else "differs",
        "pass": (
            all_match
            and prod["all_gates_passed"] is True
            and prod["empirical_inputs"] == "0 of 19"
        ),
    }


def main() -> int:
    hygiene = self_ast_hygiene_check()
    manifests = verify_all_66_manifests()
    ow = load_sealed_ow1_to_ow15()
    locks = verify_all_10_cross_card_locks(ow)

    s1 = prove_s1_m004_3cycle_and_bits()
    s2 = prove_s2_10R_vs_10C_orbifold(ow["OW11"])
    s3 = prove_s3_betas_and_B_ratio()
    s4 = prove_s4_weyl_clifford_all_5_ordered_signatures()
    s6 = prove_s6_ow14_exact_arithmetic(ow["OW14"])
    planted_faults = run_6_planted_fault_controls(ow)

    independent = {
        "hygiene": hygiene,
        "manifests_66": manifests,
        "cross_card_locks_10": locks,
        "algebraic_proofs": {
            "S1": s1,
            "S2": s2,
            "S3": s3,
            "S4": s4,
            "S6": s6,
            "pass": all(x["pass"] for x in (s1, s2, s3, s4, s6)),
        },
        "planted_faults_6": planted_faults,
    }
    producer_crosscheck = cross_check_producer_json(independent)

    all_passed = (
        hygiene["pass"]
        and manifests["pass"]
        and locks["pass"]
        and independent["algebraic_proofs"]["pass"]
        and planted_faults["pass"]
        and producer_crosscheck["pass"]
    )
    report = {
        "card_id": "A2-OW16-ERRATUM-1",
        "role": "cold_room_zero_trust_referee",
        "target_producer": "relays/a2_ow16_v4/a2_ow16_v4_results.json",
        "empirical_inputs": "0 of 19",
        "mpmath_dps": mp.mp.dps,
        "independent_recomputation": independent,
        "producer_crosscheck": producer_crosscheck,
        "all_gates_passed": all_passed,
    }
    with open(OUT_JSON_PATH, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2, sort_keys=False)
        fh.write("\n")
    print(json.dumps({
        "all_gates_passed": all_passed,
        "manifests": f"{manifests['total_verified']}/{manifests['total_checked']}",
        "locks": f"{locks['passed_count']}/{locks['total_count']}",
        "algebraic_proofs_pass": independent["algebraic_proofs"]["pass"],
        "planted_faults": f"{planted_faults['detected_count']}/{planted_faults['total_count']}",
        "producer_crosscheck_pass": producer_crosscheck["pass"],
    }, indent=2))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
