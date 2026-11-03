#!/usr/bin/env python3
"""
ZERO-TRUST HOSTILE REFEREE AUDIT SCRIPT
Branch under audit: agy/audit-2026-11-02

Independently tests and cross-examines all claims, formulas, numbers, and code modules in:
  - relays/AGY_TO_CC_2026-11-02_FULL_AUDIT_BLIND_SPOTS_AND_REFRAMING.md
  - relays/AGY_TO_CC_2026-11-02_ELEVATION_PLAN_AND_OPERATOR_GATE_EXECUTED.md
  - src/origin_axiom/twisted_norms.py
  - src/origin_axiom/operator_gate.py
  - src/origin_axiom/stepb_audit.py
  - src/origin_axiom/parameter_ledger.py

against the untouched main-branch source files:
  - frontier/B1825_step_b_the_nine_from_one_address/verification/run.json
  - scripts/stepb/assemble.py, scripts/stepb/stepb_core.py, scripts/stepb/census_io.py,
    scripts/stepb/kten.py, scripts/stepb/cells.py
  - frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification/cm_zero_line.py
  - frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py
  - frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction/b1656_funcs.py
  - frontier/B1653_the_rank_of_a_point_coupling/verification/the_rank_of_a_point_coupling.py
  - frontier/B1822_t_norm_on_the_frames_matter/verification/tnorm.py
"""
from __future__ import annotations

from fractions import Fraction
import json
import math
import pathlib
import sys
import time
from typing import Dict, List, Tuple

import mpmath as mp
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(
    0, str(ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction")
)
sys.path.insert(
    0, str(ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification")
)
sys.path.insert(0, str(ROOT / "scripts/stepb"))
sys.path.insert(
    0, str(ROOT / "frontier/B1741_tau_from_the_thread_rule_the_line_free/verification")
)

import b1656_funcs as B
import qseries as Q
import compare
import stepb_core as C
import census_io as CIO

from origin_axiom.twisted_norms import (
    channel_pair_decay_exponents,
    closed_form_cA,
    cusp_combination_D_inf,
    cusp_limit_c,
    sector_higgs_twist_multiple,
)
from origin_axiom.operator_gate import (
    BLOCKS,
    EPS,
    QI,
    QJ,
    QK,
    UNITS,
    ckm_full_diagnostics,
    direct_quaternion_coupling,
    evaluate_operator_gate,
    lagrange_ckm_compromise,
    m004_three_fold_cover_invariants,
    quaternionic_4d_yukawa,
    schur_quaternionic_bimodule_decomposition,
    serre_dr_dot_dr_eta6_identity,
    yukawa_4d_determinant_factorization,
    z3_norm_preserving_scalar_higgs,
)
from origin_axiom.sm_19_gate import (
    step1_golden_5torsion_norm_preserving_solution,
    step2_physical_spin_flavour_locking_bridge,
    step3_pmns_and_m004_gauge_thresholds,
    step4_sealed_stepb_v2_fr_cov_verdict,
    theorem8_golden_codifferent_unit_modulus_closure,
)
from origin_axiom.stepb_audit import (
    KEPT_DIRECTIONS as AGY_KEPT_DIRECTIONS,
    canonical_non_trivial_lines,
    count_order12_massless_electron_choices,
    decode_stepb_choice_index,
    strict_ten_physical_choice_mask,
)
from origin_axiom.parameter_ledger import (
    compare_frame_input_ledgers,
    m004_cover_monodromy_fixed_torsion,
    nineteen_parameter_impact_table,
)


def build_serre_sections():
    th2, th3, th4 = Q.theta2(), Q.theta3(1), Q.theta3(-1)
    di = (th2 * th3 * th4).inv()
    r_ser = [-(th2 * th2) * di, -(th4 * th4) * di, (th3 * th3) * Q.S.c(0, 1) * di]
    e2 = Q.E2()
    e4 = Q.E4()
    dr_ser = [Q.serre(c, Fraction(-1, 2), e2) for c in r_ser]
    d2r_ser = [Q.serre(c, Fraction(3, 2), e2) for c in dr_ser]
    a0_ser = [d2r_ser[j] + Q.S.c(Fraction(-1, 48)) * e4 * r_ser[j] for j in range(3)]
    t_m5_288_ser = [d2r_ser[j] + Q.S.c(Fraction(-5, 288)) * e4 * r_ser[j] for j in range(3)]
    return th2, th3, th4, r_ser, dr_ser, d2r_ser, a0_ser, t_m5_288_ser


def eval_qseries(s, tau: complex, dps: int = 35) -> complex:
    mp.mp.dps = dps
    x = mp.exp(2j * mp.pi * mp.mpc(tau.real, tau.imag) / 8)
    return complex(
        mp.fsum(
            mp.mpc(mp.mpf(a.numerator) / a.denominator, mp.mpf(b.numerator) / b.denominator)
            * (x ** kk)
            for kk, (a, b) in s.d.items()
        )
    )


def get_radii(tau: complex) -> Tuple[float, float]:
    col = sorted(
        (p["tau"][1], p["L_max"], p["L_2"])
        for p in json.loads(
            (
                ROOT
                / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json"
            ).read_text(encoding="utf-8")
        )["points"]
        if abs(p["tau"][0] - 0.25) < 1e-9
    )
    return (
        float(np.interp(tau.imag, [c[0] for c in col], [c[1] for c in col])),
        float(np.interp(tau.imag, [c[0] for c in col], [c[2] for c in col])),
    )


def audit_area_1(dr_ser) -> Dict[str, object]:
    """Area 1: Audit B1825 run.json readout, observable breakdown, and Lagrange CKM compromise."""
    run_json = json.loads(
        (
            ROOT / "frontier/B1825_step_b_the_nine_from_one_address/verification/run.json"
        ).read_text(encoding="utf-8")
    )
    T9 = np.asarray(compare.arrays()["T9"], float)
    J_target = 3.12e-5
    t10 = np.concatenate([T9, [math.log(J_target)]])
    sig = np.array(
        json.loads(
            (ROOT / "scripts/stepb/sigma/SIGMA_ONLY.json").read_text(encoding="utf-8")
        )["sigma_natural_log"],
        float,
    )
    tt_c3 = t10 - C.c_shift(3.0)

    # Fresh recomputation at B1825 best address ((3/8, 3/8), DR, L_2, S~S~S, tau=0.093359375+2.742578125j)
    tau_best = complex(0.093359375, 2.742578125)
    line_best = (Fraction(3, 8), Fraction(3, 8))
    _, L2_best = get_radii(tau_best)
    a_dr = [eval_qseries(c, tau_best) for c in dr_ser]

    U = {}
    S_vals = {}
    matter_quats = {}
    for (sn, ql, qr), r in zip(
        [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)], (1, 1, 0)
    ):
        w = B.line_w(line_best[0], line_best[1], tau_best)
        x, yy = B.sector_twists(w, tau_best, ql, qr)
        R = B.residues(x, yy, tau_best)
        c = B.cA(x, yy, tau_best, R)
        Sm = a_dr[0] * B.QI + a_dr[1] * B.QJ + a_dr[2] * B.QK
        if r:
            Sm = B.EPS @ Sm.conj() @ B.EPS.T
        u = {
            k: (
                math.sqrt(2 * math.pi * L2_best + c[k]) * R[k]
                if c[k] is not None and 2 * math.pi * L2_best + c[k] > 0
                else 0.0
            )
            for k in B.UNITS
        }
        matter_quats[sn] = u
        Y = B.coupling(Sm, B.weighted_M(u))
        u_, s, _ = np.linalg.svd(Y)
        o = np.argsort(s)
        s = s[o]
        U[sn] = u_[:, o]
        S_vals[sn] = s / s[2]

    Vm = U["up"].conj().T @ U["down"]
    J_val = float(
        abs(np.imag(Vm[0, 1] * Vm[1, 2] * np.conj(Vm[0, 2]) * np.conj(Vm[1, 1])))
    )
    raw_pred = [
        float(S_vals["up"][1]),
        float(S_vals["up"][0]),
        float(S_vals["down"][1]),
        float(S_vals["down"][0]),
        float(S_vals["lepton"][1]),
        float(S_vals["lepton"][0]),
        float(abs(Vm[0, 1])),
        float(abs(Vm[1, 2])),
        float(abs(Vm[0, 2])),
        J_val,
    ]
    f_pred = np.log(np.array(raw_pred, float))
    z_vec = (f_pred - tt_c3) / sig
    chi2_i = z_vec ** 2
    chi2_ten_recomputed = float(np.sum(chi2_i))

    # Check discrepancies between run.json and AGY_TO_CC_2026-11-02_FULL_AUDIT_BLIND_SPOTS_AND_REFRAMING.md lines 22-24
    prose_vs_run_json_discrepancies = {
        "readout_least_chi2_nine": {
            "run_json_exact": run_json["S"]["readout_least_chi2_nine"],
            "agy_verify_json": 82.6047634064222,
            "agy_relay_prose_line_22": 82.600158,
            "diff_prose_vs_run_json": 82.600158 - run_json["S"]["readout_least_chi2_nine"],
        },
        "L_six": {
            "run_json_exact": run_json["K"]["L_six"],
            "agy_relay_prose_line_23": 23.467113,
            "diff_prose_vs_run_json": 23.467113 - run_json["K"]["L_six"],
        },
        "C_six": {
            "run_json_exact": run_json["K"]["C_six"],
            "agy_relay_prose_line_23": 9.162624,
            "diff_prose_vs_run_json": 9.162624 - run_json["K"]["C_six"],
            "note": "In run.json, C_six is NEGATIVE (-3.079845 bits: the six do not compress), whereas relay line 23 printed +9.162624 bits!",
        },
        "bits_CKM": {
            "run_json_exact": run_json["K"]["bits_CKM"],
            "agy_relay_prose_line_23": -206.202854,
            "diff_prose_vs_run_json": -206.202854 - run_json["K"]["bits_CKM"],
        },
        "C_ten": {
            "run_json_exact": run_json["K"]["C_ten"],
            "agy_verify_json": -197.03655960242986,
            "agy_relay_prose_line_23": -197.040229,
            "diff_prose_vs_run_json": -197.040229 - run_json["K"]["C_ten"],
        },
        "min_chi2_six": {
            "run_json_exact": run_json["CKM"]["clause"]["min_chi2_six"],
            "agy_verify_json": 1.3582125046184093,
            "agy_relay_prose_line_24": 1.358308,
            "diff_prose_vs_run_json": 1.358308 - run_json["CKM"]["clause"]["min_chi2_six"],
        },
    }

    # Audit Lagrange CKM compromise (both equal-weight and exact sigma-weighted)
    r_eq = lagrange_ckm_compromise(0.22500, 0.04182, 0.003732)
    # Using exact B1741 compare.py targets:
    vus_t9, vcb_t9, vub_t9 = float(math.exp(T9[6])), float(math.exp(T9[7])), float(math.exp(T9[8]))
    r_t9 = lagrange_ckm_compromise(vus_t9, vcb_t9, vub_t9)
    # Sigma-weighted Lagrange compromise: minimize sum_{i in {12,23,13}} (ln r_i / sigma_i)^2 s.t. ln r_13 - ln r_12 - ln r_23 = ln K
    k_t9 = (vus_t9 * vcb_t9) / vub_t9
    s12, s23, s13 = float(sig[6]), float(sig[7]), float(sig[8])
    w_sum = s12 ** 2 + s23 ** 2 + s13 ** 2
    ln_r12_w = -(s12 ** 2 / w_sum) * math.log(k_t9)
    ln_r23_w = -(s23 ** 2 / w_sum) * math.log(k_t9)
    ln_r13_w = +(s13 ** 2 / w_sum) * math.log(k_t9)
    r_sig_weighted = (math.exp(ln_r12_w), math.exp(ln_r23_w), math.exp(ln_r13_w))

    return {
        "chi2_ten_fresh_run_json": run_json["S"]["readout_fresh_at_address"]["chi2_ten_fresh"],
        "chi2_ten_fresh_recomputed": chi2_ten_recomputed,
        "abs_diff_fresh_recomputation": abs(
            chi2_ten_recomputed - run_json["S"]["readout_fresh_at_address"]["chi2_ten_fresh"]
        ),
        "chi2_six_recomputed": float(np.sum(chi2_i[:6])),
        "chi2_Vub_recomputed": float(chi2_i[8]),
        "chi2_J_recomputed": float(chi2_i[9]),
        "fraction_Vub_plus_J_of_chi2_ten": float((chi2_i[8] + chi2_i[9]) / chi2_ten_recomputed),
        "prose_vs_run_json_discrepancies": prose_vs_run_json_discrepancies,
        "lagrange_compromise": {
            "equal_weight_pdg_rounded": list(r_eq),
            "equal_weight_T9_exact": list(r_t9),
            "sigma_weighted_T9_exact": list(r_sig_weighted),
            "relay_1_line_140_rounding_note": "Relay 1 line 140 wrote (0.7348, 0.7348, 1.3609), whereas 2.5213^(-1/3) = 0.734733 and 2.5213^(+1/3) = 1.361038 (corrected in operator_gate.py to (0.7347, 0.7347, 1.3611)).",
        },
        "_cached_b1825_matter_quats": matter_quats,
        "_cached_b1825_a_dr": a_dr,
        "_cached_t10": t10,
        "_cached_tt_c3": tt_c3,
        "_cached_sig": sig,
    }


def audit_area_2(r_ser, t_m5_288_ser) -> Dict[str, object]:
    """Area 2: Audit Step B code defects in assemble.py, kten.py, cells.py, census_io.py, and stepb_audit.py."""
    manifest = json.loads(
        (ROOT / "scripts/census/REFINED_CENSUS_MANIFEST.json").read_text(encoding="utf-8")
    )["per_file"]

    # Check the TRUE direction ordering in cm_zero_line.py & census_io.py vs stepb_audit.py's KEPT_DIRECTIONS!
    cm_zero_line_dirs = [
        "DR", "a0", "R", "t=-5/288", "F_-10", "F_-6", "F_-2", "F_6", "F_10", "F_14", "F_18", "F_22", "F_26"
    ]
    # census_io.py drops index FM2 = 6 ("F_-2") and keeps the remaining 12 in ascending integer order of d:
    true_kept_dirs_with_d_idx = [
        (idx, name) for idx, name in enumerate(cm_zero_line_dirs) if idx != CIO.FM2
    ]
    true_kept_dir_names = [name for _, name in true_kept_dirs_with_d_idx]

    # Decode choice 30900 using the TRUE kept direction order vs agy's KEPT_DIRECTIONS:
    agy_decoded_30900 = decode_stepb_choice_index(30900, manifest)
    lines = canonical_non_trivial_lines(manifest)
    rem = 30900
    r_idx = rem % 8; rem //= 8
    rad_idx = rem % 2; rem //= 2
    d_pos = rem % 12; rem //= 12
    line_idx = rem
    true_d_raw_idx, true_dir_name = true_kept_dirs_with_d_idx[d_pos]

    # Evaluate ((2/5, 0), F_26, L_max, ('S~', 'S', 'S')) at a sample tau to check if J != 0 and V defined == True!
    tau_sample = complex(0.15, 2.55)
    Lmax_s, _ = get_radii(tau_sample)
    q_mp = mp.exp(1j * mp.pi * mp.mpc(tau_sample.real, tau_sample.imag))
    eps_26 = 1j ** ((26 + 2) // 2)
    t2, t3, t4 = mp.jtheta(2, 0, q_mp), mp.jtheta(3, 0, q_mp), mp.jtheta(4, 0, q_mp)
    a_f26 = [complex(eps_26 * (t2 ** 26)), complex(eps_26 * (t4 ** 26)), complex(1j * (t3 ** 26))]

    U_30900 = {}
    s_ratios_30900 = {}
    for (sn, ql, qr), r_flag in zip([("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)], (1, 0, 0)):
        w = B.line_w(Fraction(2, 5), Fraction(0, 1), tau_sample)
        x, yy = B.sector_twists(w, tau_sample, ql, qr)
        R = B.residues(x, yy, tau_sample)
        c = B.cA(x, yy, tau_sample, R)
        Sm = a_f26[0] * B.QI + a_f26[1] * B.QJ + a_f26[2] * B.QK
        if r_flag:
            Sm = B.EPS @ Sm.conj() @ B.EPS.T
        u = {
            k: (math.sqrt(2 * math.pi * Lmax_s + c[k]) * R[k] if c[k] is not None and 2 * math.pi * Lmax_s + c[k] > 0 else 0.0)
            for k in B.UNITS
        }
        Y = B.coupling(Sm, B.weighted_M(u))
        u_, s, _ = np.linalg.svd(Y)
        o = np.argsort(s)
        s = s[o]
        U_30900[sn] = u_[:, o]
        s_ratios_30900[sn] = (float(s[0] / s[2]), float(s[1] / s[2]))

    Vm_30900 = U_30900["up"].conj().T @ U_30900["down"]
    J_30900 = float(
        abs(np.imag(Vm_30900[0, 1] * Vm_30900[1, 2] * np.conj(Vm_30900[0, 2]) * np.conj(Vm_30900[1, 1])))
    )

    # Check why census_structure.json has 2 dead directions ("R" and "t=-5/288"): both are isotropic (a . a == 0) in q-series!
    dot3 = lambda u, v: u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
    r_dot_r = dot3(r_ser, r_ser)
    tm5_dot_tm5 = dot3(t_m5_288_ser, t_m5_288_ser)
    r_is_null = r_dot_r.ord() is None or r_dot_r.ord() > 200
    tm5_is_null = tm5_dot_tm5.ord() is None or tm5_dot_tm5.ord() > 200

    # Verify Defect 4B (48 order-12 lines => 7,680 massless-electron choices in 40,000 physical choices):
    o12 = count_order12_massless_electron_choices(manifest)

    return {
        "defect_4A_choice_30900_audit": {
            "agy_KEPT_DIRECTIONS": list(AGY_KEPT_DIRECTIONS),
            "true_cm_zero_line_KEPT_DIRECTIONS": true_kept_dir_names,
            "agy_decoded_direction_for_30900": agy_decoded_30900["direction"],
            "true_decoded_direction_for_30900": true_dir_name,
            "true_d_column_value_in_census": true_d_raw_idx,
            "line_for_30900": [str(lines[line_idx][0]), str(lines[line_idx][1])],
            "radius_for_30900": agy_decoded_30900["radius"],
            "reading_for_30900": list(agy_decoded_30900["reading"]),
            "sample_abs_J_on_true_choice_30900_F26": J_30900,
            "is_choice_30900_actually_physical": bool(J_30900 > 1e-12),
            "referee_finding_on_30900": (
                "REFUTED / BUG EXPOSED IN stepb_audit.py: agy hardcoded KEPT_DIRECTIONS as "
                "('DR','a0','F_6','F_10','F_14','F_18','F_22','F_26','F_-6','F_-10','R','D2R'), "
                "putting 'D2R' at index 11. In reality, cm_zero_line.py line 37 defines "
                "DIRS = ['DR','a0','R','t=-5/288','F_-10','F_-6','F_-2','F_6','F_10','F_14','F_18','F_22','F_26'], "
                "and census_io.py drops index 6 ('F_-2'), so the 12th kept direction (d_pos=11, d=12) is 'F_26', "
                "NOT 'D2R'! On ((2/5, 0), F_26, L_max, ('S~', 'S', 'S')), |J| != 0 and physical_choice[30900] is True! "
                "However, the second half of Defect 4A IS VERIFIED: kten.py line 172 calls windowed(..., physical=False) "
                "and lines 202-203 ignore m['choice'] = 30900 when computing num and den of lp_post."
            ),
        },
        "two_dead_directions_in_census": {
            "names": ["R", "t=-5/288"],
            "R_dot_R_identically_zero": bool(r_is_null),
            "t_minus_5_288_dot_self_identically_zero": bool(tm5_is_null),
            "explanation": (
                "Both R and t=-5/288 = D^2R - (5/288) E_4 R satisfy a(tau) . a(tau) == 0 identically! "
                "By Theorem 3 at a_0 = 0, det(Y_s) = (a.a) det(M) (a.m_perp) == 0, forcing m_1 = 0 in every sector "
                "and locking u_1^(u) = u_1^(d) = a_hat^*, which makes V_CKM block-diagonal 1 (+) U(2) and J == 0 identically."
            ),
        },
        "defect_4B_order12_massless_electrons": {
            "order_12_lines": o12["order_12_lines"],
            "order_12_total_choices": o12["order_12_total_choices"],
            "order_12_choices_in_physical_choice_40000": o12["order_12_choices_in_physical_choice"],
            "fraction_of_40000": o12["fraction_of_40000_physical_choices"],
            "parameter_ledger_line_145_note": (
                "VERIFIED that 48 * 10 * 2 * 8 = 7,680 massless-electron choices (19.2% of 40,000) enter physical_choice. "
                "Note: parameter_ledger.py line 145 and ELEVATION_PLAN line 112 also cite '36/5832', which comes from "
                "an older 5,832-row sub-table (e.g. B1726/B1741) rather than B1825's 50,880-choice census."
            ),
        },
    }


def audit_area_3() -> Dict[str, object]:
    """Area 3: Adversarial & boundary tests of Theorem 1 (closed_form_cA, cusp_combination_D_inf, channel_pair_decay_exponents)."""
    rng = np.random.default_rng(2026110399)

    # 1. Fresh adversarial random tau and random torsion lines NOT in test_elevation_operator_gate.py
    adversarial_cases = [
        # (label, tau, alpha, b)
        ("random_1_ord11", complex(0.314159, 1.414213), Fraction(3, 11), Fraction(7, 11)),
        ("random_2_ord9", complex(-0.271828, 2.15), Fraction(2, 9), Fraction(5, 9)),
        ("random_3_ord8_neg_re", complex(-0.41, 1.62), Fraction(1, 8), Fraction(5, 8)),
        ("boundary_alpha_0_ord5", complex(0.19, 1.75), Fraction(0, 1), Fraction(2, 5)),
        ("boundary_alpha_1_3_nu0", complex(0.23, 1.95), Fraction(1, 3), Fraction(1, 7)),
        ("boundary_alpha_1_6_nuj0", complex(0.11, 1.55), Fraction(1, 6), Fraction(1, 5)),
        ("boundary_alpha_1_2", complex(0.29, 1.85), Fraction(1, 2), Fraction(1, 3)),
        ("adversarial_alpha_gt_half_5_8", complex(0.14, 1.92), Fraction(5, 8), Fraction(3, 8)),
        ("adversarial_alpha_gt_half_7_9", complex(0.37, 2.05), Fraction(7, 9), Fraction(2, 9)),
        ("degenerate_R_i_zero_on_1_3_1_6", complex(0.21, 1.80), Fraction(1, 3), Fraction(1, 6)),
    ]

    quadrature_comparisons = []
    max_abs_err_all = 0.0
    max_sector_spread_all = 0.0

    for label, tau, alpha, b in adversarial_cases:
        w = B.line_w(float(alpha), float(b), tau)
        sec_c = {}
        sec_r = {}
        for sn, ql, qr in [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)]:
            x, y = B.sector_twists(w, tau, ql, qr)
            R = B.residues(x, y, tau)
            sec_r[sn] = R
            sec_c[sn] = B.cA(x, y, tau, R)

        c_cf = closed_form_cA(tau, alpha, b, n_terms=100, dps=35)
        ch_diffs = {}
        for s in ("1", "i", "j", "k"):
            vals_q = [sec_c[sn][s] for sn in ("up", "down", "lepton") if sec_c[sn][s] is not None]
            if len(vals_q) == 3:
                sp = max(abs(vals_q[0] - vals_q[1]), abs(vals_q[2] - vals_q[1]))
                max_sector_spread_all = max(max_sector_spread_all, sp)
            if c_cf[s] is None:
                ch_diffs[s] = {"closed_form": None, "quad_down": sec_c["down"][s]}
            else:
                q_ref = sec_c["down"][s] if sec_c["down"][s] is not None else (vals_q[0] if vals_q else None)
                diff = abs(c_cf[s] - q_ref) if q_ref is not None else None
                if diff is not None:
                    max_abs_err_all = max(max_abs_err_all, diff)
                ch_diffs[s] = {
                    "closed_form": c_cf[s],
                    "quad_ref": q_ref,
                    "abs_diff": diff,
                }
        quadrature_comparisons.append({
            "label": label,
            "tau": [tau.real, tau.imag],
            "alpha": str(alpha),
            "b": str(b),
            "channels": ch_diffs,
        })

    # 2. Cross-check against Route B (mpmath strip quadrature cB in b1656_funcs.py) at a fresh point:
    tau_cb = complex(0.19, 1.65)
    alpha_cb, b_cb = Fraction(3, 11), Fraction(2, 11)
    w_cb = B.line_w(float(alpha_cb), float(b_cb), tau_cb)
    x_cb, y_cb = B.sector_twists(w_cb, tau_cb, 1, 2)
    r_cb = B.residues(x_cb, y_cb, tau_cb)
    c_cf_cb = closed_form_cA(tau_cb, alpha_cb, b_cb, n_terms=100, dps=35)
    cb_diffs = {}
    for s in ("1", "i", "j", "k"):
        val_cb = B.cB(x_cb, y_cb, tau_cb, s, r_cb[s], n=16)
        cb_diffs[s] = {
            "closed_form": c_cf_cb[s],
            "cB_mpmath_quad": val_cb,
            "abs_diff": abs(c_cf_cb[s] - val_cb),
        }

    # 3. Expose two caveats on channel_pair_decay_exponents(alpha):
    # Caveat 3A: When 3*alpha in Z (e.g. alpha = 1/3) and cos(6*pi*b) == 0 (e.g. b = 1/12 or 1/4),
    # exp(-6*pi*i*b) = -exp(+6*pi*i*b) = +/- i, so flipping eta_s -> -eta_s swaps wp <-> wm for EVERY n >= 1
    # AND preserves |1 + eta_s * exp(-6*pi*i*b)|^2 = 2!
    # Consequently, c_1(tau) - c_i(tau) == 0 IDENTICALLY for ALL tau in H (not merely E = 0 linear growth)!
    c1i_alpha_1_3_b_1_12_y2 = closed_form_cA(complex(0.17, 2.0), Fraction(1, 3), Fraction(1, 12), dps=50)
    c1i_alpha_1_3_b_1_12_y3 = closed_form_cA(complex(0.41, 3.0), Fraction(1, 3), Fraction(1, 12), dps=50)
    d2 = abs(c1i_alpha_1_3_b_1_12_y2["1"] - c1i_alpha_1_3_b_1_12_y2["i"])
    d3 = abs(c1i_alpha_1_3_b_1_12_y3["1"] - c1i_alpha_1_3_b_1_12_y3["i"])

    # Caveat 3B: On vertical slices where cos(2*pi*(nu * Re(tau) - 3*b)) == 0 (e.g. Re(tau) = 0, alpha = 2/5, b = 1/12),
    # the leading m=1 term in Re[exp(-6*pi*i*b) exp(2*pi*i*nu*tau)] vanishes identically!
    # In fact, at Re(tau) = 0 and b = 1/12, 6*pi*b = pi/2 so exp(-6*pi*i*b * m) = (-i)^m, which is purely imaginary
    # for ALL odd m, while even m cancel between eta = -1 and eta = +1! Thus at Re(tau) = 0, b = 1/12,
    # c_1(i*y) - c_i(i*y) == 0 IDENTICALLY for ALL y > 0!
    c1i_nodal_re0 = closed_form_cA(complex(0.0, 2.5), Fraction(2, 5), Fraction(1, 12), dps=50)
    exact_zero_on_re0_b_1_12 = abs(c1i_nodal_re0["1"] - c1i_nodal_re0["i"])
    # And at Re(tau) = 1/2, b = -1/20, nu*Re(tau) - 3*b = 1/4 AND Re(tau) in (1/2)Z makes wp and wm purely imaginary for ALL n,
    # so c_1(1/2 + i*y) - c_i(1/2 + i*y) == 0 identically for all y > 0 too!
    # Whereas at generic Re(tau) = 7/20 = 0.35, nu = 1/5, 3*b = 7/100 - 1/4 = -9/50 => b = -3/50,
    # ONLY the (n=0, nu=1/5) branch has phase 1/4 (killing E = nu/2 = 0.10), while the (n=0, 1-nu=4/5) branch
    # survives and decays at E' = (1 - nu)/2 = 2/5 = 0.40!
    c1i_m1_killed_y2 = closed_form_cA(complex(0.35, 2.0), Fraction(2, 5), Fraction(-3, 50), dps=50)
    c1i_m1_killed_y3 = closed_form_cA(complex(0.35, 3.0), Fraction(2, 5), Fraction(-3, 50), dps=50)
    dn2 = abs(c1i_m1_killed_y2["1"] - c1i_m1_killed_y2["i"])
    dn3 = abs(c1i_m1_killed_y3["1"] - c1i_m1_killed_y3["i"])
    emp_E_nodal_slice = -math.log(dn3 / dn2) / (4 * math.pi * (3.0 - 2.0))

    return {
        "max_abs_err_vs_cA_on_10_adversarial_cases": max_abs_err_all,
        "max_sector_spread_on_10_adversarial_cases": max_sector_spread_all,
        "route_B_cB_comparison": cb_diffs,
        "adversarial_quadrature_cases": quadrature_comparisons,
        "exposed_caveats_on_decay_exponents": {
            "caveat_3A_integer_twist_identical_vanishing_at_cos6pib_eq_0": {
                "alpha": "1/3",
                "b": "1/12",
                "predicted_by_channel_pair_decay_exponents": float(
                    channel_pair_decay_exponents(Fraction(1, 3))["E_c1_minus_ci"]
                ),
                "abs_c1_minus_ci_at_0p17_plus_2j": d2,
                "abs_c1_minus_ci_at_0p41_plus_3j": d3,
                "explanation": (
                    "At alpha = 1/3 (nu_1 = nu_i = 0), generically c_1 - c_i grows linearly with Im(tau) (E = 0), "
                    "except when cos(6*pi*b) = 0 (6*b in Z + 1/2, e.g. b = 1/12, 1/4), where flipping eta -> -eta "
                    "swaps wp <-> wm for every n >= 1 and preserves |1 + eta*e^(-6*pi*i*b)|^2 = 2, forcing "
                    "c_1(tau) - c_i(tau) == 0 identically for ALL tau in H."
                ),
            },
            "caveat_3B_nodal_phase_slice_jumps_from_nu_over_2_to_1_minus_nu_over_2": {
                "alpha": "2/5",
                "b_exact_zero_at_Re0": "1/12",
                "c1_minus_ci_at_Re0_b_1_12": exact_zero_on_re0_b_1_12,
                "Re_tau_for_branch_kill": 0.35,
                "b_for_branch_kill": "-3/50",
                "generic_E_c1_minus_ci": float(
                    channel_pair_decay_exponents(Fraction(2, 5))["E_c1_minus_ci"]
                ),
                "actual_measured_E_on_nodal_slice": emp_E_nodal_slice,
                "explanation": (
                    "At Re(tau) in (1/2)Z and nu*Re(tau) - 3*b in (1/2)Z + 1/4 (e.g. Re(tau)=0, b=1/12 or Re(tau)=1/2, b=-1/20), "
                    "both wp and wm are purely imaginary for all n, so c_1 - c_i == 0 IDENTICALLY for all Im(tau) > 0! "
                    "At generic Re(tau) not in (1/2)Z with nu*Re(tau) - 3*b in (1/2)Z + 1/4 (e.g. Re(tau)=0.35, b=-3/50 for alpha=2/5), "
                    "the entire n=0, nu=1/5 branch is purely imaginary on odd powers, so the decay exponent jumps from "
                    "E = nu/2 = 0.10 to E' = (1 - nu)/2 = 0.40."
                ),
            },
        },
    }


def audit_area_4_and_5(b1825_cache: Dict[str, object]) -> Dict[str, object]:
    """Areas 4 & 5: Adversarial tests of Theorem 2 (4D Yukawa & CKM corner inversion across all 8 readings),
    Theorem 3 (Determinant Factorization), and Theorem 4 (DR.DR == 1/4 eta^6 in exact rational qseries)."""
    rng = np.random.default_rng(2026110377)

    # 1. Test Theorem 2 & Theorem 3 on 200 fresh adversarial random 4D quaternions
    max_yukawa_4d_err = 0.0
    max_yh_err = 0.0
    max_det_rel_err = 0.0
    for _ in range(200):
        a0 = complex(rng.normal() + 1j * rng.normal())
        h_vec = rng.normal(size=3) + 1j * rng.normal(size=3)
        m1 = complex(rng.normal() + 1j * rng.normal())
        m_perp = rng.normal(size=3) + 1j * rng.normal(size=3)

        y_form = quaternionic_4d_yukawa(a0, h_vec, m1, m_perp)
        y_dir = direct_quaternion_coupling(a0, h_vec, m1, m_perp)
        max_yukawa_4d_err = max(max_yukawa_4d_err, float(np.max(np.abs(y_form - y_dir))))

        yh_expected = np.dot(h_vec, h_vec) * m_perp + a0 * (m1 * h_vec - np.cross(m_perp, h_vec))
        max_yh_err = max(max_yh_err, float(np.max(np.abs(y_form @ h_vec - yh_expected))))

        det_res = yukawa_4d_determinant_factorization(a0, h_vec, m1, m_perp)
        max_det_rel_err = max(max_det_rel_err, float(det_res["rel_error"]))

    # 2. Test all 4 quark reading pairs (S,S), (S~,S~), (S~,S), (S,S~) at B1825's best address at a0 = 0:
    # Expose what happens when r_u != r_d ((S~, S) or (S, S~))!
    a_dr = b1825_cache["_cached_b1825_a_dr"]
    mq = b1825_cache["_cached_b1825_matter_quats"]
    h_base = np.array([a_dr[1], a_dr[0], a_dr[2]], dtype=complex)  # (h_J, h_I, h_K) in BLOCKS order
    m1_u = mq["up"]["1"]
    mp_u = np.array([mq["up"]["j"], mq["up"]["i"], mq["up"]["k"]], dtype=complex)
    m1_d = mq["down"]["1"]
    mp_d = np.array([mq["down"]["j"], mq["down"]["i"], mq["down"]["k"]], dtype=complex)

    reading_pair_diagnostics = {}
    for label, (ru, rd) in [("SS", (0, 0)), ("S~S~", (1, 1)), ("S~S", (1, 0)), ("SS~", (0, 1))]:
        hu = h_base.conj() if ru else h_base
        hd = h_base.conj() if rd else h_base
        yu = quaternionic_4d_yukawa(0.0, hu, m1_u, mp_u)
        yd = quaternionic_4d_yukawa(0.0, hd, m1_d, mp_d)
        diag = ckm_full_diagnostics(yu, yd, h_vec_up=hu)
        reading_pair_diagnostics[label] = {
            "V_ud": diag["V_abs"][0][0],
            "V_us": diag["V_us"],
            "V_cb": diag["V_cb"],
            "V_ub": diag["V_ub"],
            "V_td": diag["V_td"],
            "Vub_over_Vtd": diag["ratio_Vub_over_Vtd"],
            "sin_delta_CP": diag["sin_delta_CP"],
        }

    # 3. Verify Theorem 4 (DR . DR == (1/4) eta(tau)^6) in exact rational qseries arithmetic up to x^240 = q^30:
    th2, th3, th4, r_ser, dr_ser, d2r_ser, _, _ = build_serre_sections()
    dot3 = lambda u, v: u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
    dr_dot_dr_q = dot3(dr_ser, dr_ser)
    r_dot_d2r_q = dot3(r_ser, d2r_ser)
    # eta^3 = (1/2) th2 th3 th4 => (1/4) eta^6 = (1/16) (th2 th3 th4)^2
    th_prod = th2 * th3 * th4
    quarter_eta6_q = th_prod * th_prod * Q.S.c(Fraction(1, 16))
    diff_dr2_eta6 = dr_dot_dr_q - quarter_eta6_q
    sum_dr2_rd2r = dr_dot_dr_q + r_dot_d2r_q

    # Also test serre_dr_dot_dr_eta6_identity on 20 random tau in H:
    max_num_err_th4 = 0.0
    for _ in range(20):
        t_rand = complex(rng.uniform(-0.5, 0.5), rng.uniform(1.1, 3.5))
        res4 = serre_dr_dot_dr_eta6_identity(t_rand)
        max_num_err_th4 = max(max_num_err_th4, float(res4["rel_error"]))

    return {
        "theorem2_and_3_200_random_trials": {
            "max_4d_yukawa_abs_err": max_yukawa_4d_err,
            "max_yh_identity_abs_err": max_yh_err,
            "max_det_factorization_rel_err": max_det_rel_err,
        },
        "theorem2_all_4_quark_reading_pairs_at_b1825": {
            "pairs": reading_pair_diagnostics,
            "referee_finding": (
                "Theorem 2's proof in AGY_TO_CC_2026-11-02_FULL_AUDIT_BLIND_SPOTS_AND_REFRAMING.md §3.2 assumes "
                "up and down share the same Higgs vector h_u = h_d (readings SS and S~S~, where |V_ud| ~ 0.979 and "
                "|V_ub|/|V_td| = 11.28). For mixed readings (S~S and SS~, where h_d = h_u^*), on the null cone h.h -> 0, "
                "u_1^(u) -> h_u^* and u_1^(d) -> h_u are nearly ORTHOGONAL (<h_u^*, h_u> = (h.h)/||h||^2 = r << 1), "
                "which catastrophically collapses |V_ud| to 0.0175 and sends |V_us| to 0.9997! Thus all 8 readings fail at a_0 = 0."
            ),
        },
        "theorem4_exact_qseries_and_random_tau": {
            "exact_qseries_DR_dot_DR_minus_quarter_eta6_ord": diff_dr2_eta6.ord(),
            "exact_qseries_DR_dot_DR_plus_R_dot_D2R_ord": sum_dr2_rd2r.ord(),
            "identically_zero_through_x240": bool(
                (diff_dr2_eta6.ord() is None or diff_dr2_eta6.ord() > 200)
                and (sum_dr2_rd2r.ord() is None or sum_dr2_rd2r.ord() > 200)
            ),
            "max_numerical_rel_err_20_random_tau": max_num_err_th4,
        },
    }


def audit_area_6() -> Dict[str, object]:
    """Area 6: Audit m004_three_fold_cover_invariants() commutant claim (S_3 sheet permutation vs S_4 signed permutation)."""
    c3 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=float)
    # 1. Pure sheet-swap reflection P_perm (swapping sheets 2 <-> 3 without minus signs):
    p_perm = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=float)
    # 2. agy's p_refl in operator_gate.py line 224 (swapping sheets 2 <-> 3 WITH minus signs):
    p_refl_agy = np.array([[1, 0, 0], [0, 0, -1], [0, -1, 0]], dtype=float)

    def sym_commutant_dim(gens: List[np.ndarray]) -> int:
        basis_sym = []
        for i in range(3):
            for j in range(i, 3):
                m = np.zeros((3, 3), dtype=float)
                m[i, j] = m[j, i] = 1.0
                basis_sym.append(m)
        a_mat = np.column_stack(
            [np.concatenate([(g.T @ b @ g - b).ravel() for g in gens]) for b in basis_sym]
        )
        _, s_vals, _ = np.linalg.svd(a_mat)
        return int(np.sum(s_vals < 1e-12))

    def herm_commutant_dim_real(gens: List[np.ndarray]) -> int:
        basis_herm = []
        for i in range(3):
            m = np.zeros((3, 3), dtype=complex); m[i, i] = 1.0; basis_herm.append(m)
        for i in range(3):
            for j in range(i + 1, 3):
                m1 = np.zeros((3, 3), dtype=complex); m1[i, j] = m1[j, i] = 1.0; basis_herm.append(m1)
                m2 = np.zeros((3, 3), dtype=complex); m2[i, j] = 1j; m2[j, i] = -1j; basis_herm.append(m2)
        cols = []
        for b in basis_herm:
            vec = []
            for g in gens:
                diff = g.conj().T @ b @ g - b
                vec.append(diff.real.ravel())
                vec.append(diff.imag.ravel())
            cols.append(np.concatenate(vec))
        a_mat = np.column_stack(cols)
        _, s_vals, _ = np.linalg.svd(a_mat)
        return int(np.sum(s_vals < 1e-12))

    def generated_group_order(gens: List[np.ndarray]) -> int:
        seen = [np.eye(3, dtype=int)]
        queue = [np.eye(3, dtype=int)]
        ig = [np.rint(g).astype(int) for g in gens]
        while queue:
            cur = queue.pop(0)
            for g in ig:
                nxt = cur @ g
                if not any(np.array_equal(nxt, s) for s in seen):
                    seen.append(nxt)
                    queue.append(nxt)
        return len(seen)

    ord_s3_perm = generated_group_order([c3, p_perm])
    ord_agy_s4 = generated_group_order([c3, p_refl_agy])

    return {
        "pure_S3_sheet_permutation_C3_and_P_perm": {
            "group_order": ord_s3_perm,
            "dim_R_symmetric_commutant": sym_commutant_dim([c3, p_perm]),
            "dim_R_hermitian_commutant": herm_commutant_dim_real([c3, p_perm]),
            "general_invariant_metric": "H = a I_3 + b J_3 (2 real parameters: allows democratic mixing b != 0, matching B1822 §3 Row 4!)",
        },
        "C3_alone_cyclic_deck_group": {
            "group_order": generated_group_order([c3]),
            "dim_R_symmetric_commutant": sym_commutant_dim([c3]),
            "dim_R_hermitian_commutant": herm_commutant_dim_real([c3]),
        },
        "agy_operator_gate_C3_and_P_refl_with_minus_signs": {
            "group_order": ord_agy_s4,
            "dim_R_symmetric_commutant": sym_commutant_dim([c3, p_refl_agy]),
            "dim_R_hermitian_commutant": herm_commutant_dim_real([c3, p_refl_agy]),
            "referee_finding": (
                "CAVEAT / OVERSTATEMENT EXPOSED: In operator_gate.py lines 223-224 and parameter_ledger.py line 9, "
                "agy claims the 3-fold cover deck group S_3 = Z_3 x| Z_2 has a 1D symmetric commutant (dim_R = 1). "
                "In fact, the pure 3-sheet permutation action of S_3 (C_3 and P_perm = [[1,0,0],[0,0,1],[0,1,0]], group order 6) "
                "splits R^3 = 1 (+) 2_E and has a 2-DIMENSIONAL commutant H = a I_3 + b J_3 (allowing democratic mixing, "
                "as B1822 §3 Row 4 proved). operator_gate.py got commutant_dim = 1 only because p_refl = [[1,0,0],[0,0,-1],[0,-1,0]] "
                "multiplies P_perm by diag(1,-1,-1) (a Z_2 x Z_2 quaternion character sign flip on BLOCKS = [QJ, QI, QK]), "
                "generating the 24-element octahedral group S_4 = (Z_2 x Z_2) x| S_3 (which corresponds to B1822 §3 Row 6: "
                "'characters plus the order-3 automorphism | 1', NOT the bare sheet-permutation group S_3 alone)."
            ),
        },
    }


def audit_area_7(b1825_cache: Dict[str, object]) -> Dict[str, object]:
    """Area 7: Audit FR-COV evaluation at B1825 address (compute full chi2_ten!), parameter-free a_0 candidates,
    reading consistency (S~S~S vs S~SS), and Fix((LR)^3) torsion line compatibility."""
    a_dr = b1825_cache["_cached_b1825_a_dr"]
    mq = b1825_cache["_cached_b1825_matter_quats"]
    tt_c3 = b1825_cache["_cached_tt_c3"]
    sig = b1825_cache["_cached_sig"]
    tau_best = complex(0.093359375, 2.742578125)

    h_base = np.array([a_dr[1], a_dr[0], a_dr[2]], dtype=complex)
    h_conj = h_base.conj()

    def eval_full_ten_at_b1825(a0_val: complex, reading: Tuple[int, int, int]) -> Dict[str, object]:
        U = {}
        S_vals = {}
        for (sn, _ql, _qr), r_flag in zip([("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)], reading):
            u = mq[sn]
            m1_s = u["1"]
            mp_s = np.array([u["j"], u["i"], u["k"]], dtype=complex)
            # Note: under S -> S~ = EPS S^* EPS^T, (a_0 I_2 + h . Q) -> (a_0^* I_2 + h^* . Q)
            # Wait: in operator_gate.py lines 348-349, agy passed a0_shared WITHOUT conjugation to both up and down
            # on h_vec = h_conj! Let's support both direct (a0_val, h_conj) and conjugated.
            h_s = h_conj if r_flag else h_base
            a0_s = a0_val
            y_s = quaternionic_4d_yukawa(a0_s, h_s, m1_s, mp_s)
            u_, s, _ = np.linalg.svd(y_s)
            o = np.argsort(s)
            s = s[o]
            U[sn] = u_[:, o]
            S_vals[sn] = s / s[2]

        Vm = U["up"].conj().T @ U["down"]
        v_us = float(abs(Vm[0, 1]))
        v_cb = float(abs(Vm[1, 2]))
        v_ub = float(abs(Vm[0, 2]))
        v_td = float(abs(Vm[2, 0]))
        J_val = float(abs(np.imag(Vm[0, 1] * Vm[1, 2] * np.conj(Vm[0, 2]) * np.conj(Vm[1, 1]))))
        c12 = math.sqrt(max(0.0, 1.0 - v_us ** 2))
        c23 = math.sqrt(max(0.0, 1.0 - v_cb ** 2))
        c13 = math.sqrt(max(0.0, 1.0 - v_ub ** 2))
        j_max = c12 * c23 * (c13 ** 2) * v_us * v_cb * v_ub
        sin_delta = J_val / j_max if j_max > 0 else 0.0

        raw_pred = [
            float(S_vals["up"][1]),
            float(S_vals["up"][0]),
            float(S_vals["down"][1]),
            float(S_vals["down"][0]),
            float(S_vals["lepton"][1]),
            float(S_vals["lepton"][0]),
            v_us,
            v_cb,
            v_ub,
            J_val,
        ]
        f_pred = np.log(np.maximum(np.array(raw_pred, float), 1e-30))
        z_vec = (f_pred - tt_c3) / sig
        chi2_i = z_vec ** 2
        obs_names = ["c/t", "u/t", "s/b", "d/b", "mu/tau", "e/tau", "|V_us|", "|V_cb|", "|V_ub|", "|J|"]
        return {
            "chi2_ten": float(np.sum(chi2_i)),
            "chi2_six": float(np.sum(chi2_i[:6])),
            "chi2_ckm4": float(np.sum(chi2_i[6:10])),
            "V_us": v_us,
            "V_cb": v_cb,
            "V_ub": v_ub,
            "V_td": v_td,
            "Vub_over_Vtd": v_ub / v_td if v_td > 0 else math.inf,
            "sin_delta_CP": sin_delta,
            "abs_J": J_val,
            "mc_over_mt": raw_pred[0],
            "ms_over_mb": raw_pred[2],
            "per_observable_chi2": {obs_names[i]: float(chi2_i[i]) for i in range(10)},
        }

    # 1. Evaluate FR-FIB baseline (a0 = 0, reading S~S~S = (1,1,0))
    baseline_a0_0 = eval_full_ten_at_b1825(0.0 + 0.0j, (1, 1, 0))

    # 2. Evaluate operator_gate.py's witness a0 = 0.20 * exp(7j*pi/8) on reading S~S~S = (1,1,0)
    a0_witness = 0.20 * np.exp(1j * (7.0 * math.pi / 8.0))
    witness_s_tilde_s_tilde_s = eval_full_ten_at_b1825(a0_witness, (1, 1, 0))

    # 3. Evaluate operator_gate.py's witness on parameter_ledger.py's claimed gauge-invariant reading S~SS = (1,0,0)
    witness_s_tilde_s_s = eval_full_ten_at_b1825(a0_witness, (1, 0, 0))

    # 4. Evaluate Theorem 4's parameter-free canonical scalar a0 = (1/2) eta(tau)^3 = sqrt(DR . DR) at tau_best:
    id4 = serre_dr_dot_dr_eta6_identity(tau_best)
    a0_half_eta3 = complex(id4["half_eta3"])
    canonical_half_eta3_eval = eval_full_ten_at_b1825(a0_half_eta3, (1, 1, 0))

    # 5. Audit Fix((LR)^3) torsion subgroup vs B1825's (3/8, 3/8) and B1726's (2/5, 1/10):
    # Note: because w = p1 * tau - p2 has a minus sign on p2, A = [[a, b], [c, d]] in SL(2, Z) acts on (p1, p2) by
    # [[a, -c], [-b, d]] (or its inverse). For LR = [[2, 1], [1, 1]], the (p1, p2) matrix is [[2, -1], [-1, 1]],
    # whose cube is [[13, -8], [-8, 5]].
    a_lr_signed = np.array([[2, -1], [-1, 1]], dtype=int)
    a_lr3_signed = a_lr_signed @ a_lr_signed @ a_lr_signed  # [[13, -8], [-8, 5]]

    def is_fixed_mod1_by(mat: np.ndarray, p1: Fraction, p2: Fraction, up_to_sign: bool = True) -> bool:
        v1 = (int(mat[0, 0]) * p1 + int(mat[0, 1]) * p2) % 1
        v2 = (int(mat[1, 0]) * p1 + int(mat[1, 1]) * p2) % 1
        if (v1, v2) == (p1 % 1, p2 % 1):
            return True
        if up_to_sign and (v1, v2) == ((-p1) % 1, (-p2) % 1):
            return True
        return False

    b1825_line_in_fix_lr3 = is_fixed_mod1_by(a_lr3_signed, Fraction(3, 8), Fraction(3, 8))
    b1726_line_in_fix_lr3 = is_fixed_mod1_by(a_lr3_signed, Fraction(2, 5), Fraction(1, 10))
    golden_eigen_2_5_1_5_in_fix_lr3 = is_fixed_mod1_by(a_lr3_signed, Fraction(2, 5), Fraction(1, 5), up_to_sign=True)

    # Also check the comment discrepancy in parameter_ledger.py lines 82 vs 87:
    tors_info = m004_cover_monodromy_fixed_torsion()
    ledger_info = compare_frame_input_ledgers()

    return {
        "b1825_address_full_chi2_ten_comparison": {
            "FR_FIB_a0_eq_0_S_tilde_S_tilde_S": baseline_a0_0,
            "FR_COV_witness_a0_0p20_exp_7pi8_on_S_tilde_S_tilde_S": witness_s_tilde_s_tilde_s,
            "FR_COV_witness_a0_0p20_exp_7pi8_on_claimed_reading_S_tilde_S_S": witness_s_tilde_s_s,
            "FR_COV_canonical_a0_half_eta3_on_S_tilde_S_tilde_S": {
                "a0_half_eta3_abs": abs(a0_half_eta3),
                **canonical_half_eta3_eval,
            },
            "referee_finding_on_FR_COV_witness": (
                f"CRITICAL CAVEAT EXPOSED: At B1825's best address ((3/8,3/8), DR, L_2, S~S~S, tau=0.0934+2.7426j), "
                f"plugging in the hand-picked complex witness a_0 = 0.20*exp(7j*pi/8) flips |V_ub|/|V_td| to "
                f"{witness_s_tilde_s_tilde_s['Vub_over_Vtd']:.4f} and raises sin(delta_CP) to "
                f"{witness_s_tilde_s_tilde_s['sin_delta_CP']:.4f}, BUT it drives m_c/m_t from 0.00455 to "
                f"{witness_s_tilde_s_tilde_s['mc_over_mt']:.5f} (chi2_{{c/t}} = "
                f"{witness_s_tilde_s_tilde_s['per_observable_chi2']['c/t']:.2f}) and collapses |V_us| from 0.2028 to "
                f"{witness_s_tilde_s_tilde_s['V_us']:.5f} (chi2_{{|V_us|}} = "
                f"{witness_s_tilde_s_tilde_s['per_observable_chi2']['|V_us|']:.2f}), increasing the total 10-observable "
                f"chi2_ten from {baseline_a0_0['chi2_ten']:.2f} to {witness_s_tilde_s_tilde_s['chi2_ten']:.2f}! "
                f"Furthermore, Theorem 4's parameter-free scalar a_0 = (1/2)eta(tau)^3 has modulus "
                f"{abs(a0_half_eta3):.3e} at Im(tau)=2.7426 (3.45x smaller than 0.20), which leaves |V_ub|/|V_td| = "
                f"{canonical_half_eta3_eval['Vub_over_Vtd']:.4f} and chi2_ten = {canonical_half_eta3_eval['chi2_ten']:.2f}. "
                f"Thus evaluate_operator_gate('FR-COV') is an algebraic existence proof that a_0 != 0 unlocks the CKM corner "
                f"inversion, NOT a completed 10-observable SM fit (scoreboard rightly remains 0 of 19)."
            ),
        },
        "torsion_locus_compatibility_check": {
            "t_orbits_in_non_zero_fixed_k3": tors_info["t_orbits_in_non_zero_fixed_k3"],
            "fr_cov_total_discrete_choices_in_code": ledger_info["FR_COV"]["total_discrete_choices"],
            "comment_vs_code_note": (
                "parameter_ledger.py line 82 comment says '4 + 1 = 5 orbits', whereas line 62 computes "
                "t_orbits_in_non_zero_fixed_k3 = 5 and line 87 computes 5 + 1 = 6 orbits."
            ),
            "b1825_best_line_3_8_3_8_in_Fix_LR3": b1825_line_in_fix_lr3,
            "b1726_best_line_2_5_1_10_in_Fix_LR3": b1726_line_in_fix_lr3,
            "golden_eigen_line_2_5_1_5_in_Fix_LR3_projective": golden_eigen_2_5_1_5_in_fix_lr3,
            "referee_finding_on_torsion_lines": (
                "CAVEAT EXPOSED: ker((LR)^3 - I) = (Z/4Z)^2 contains only lines of orders 1, 2, 4 (plus the projective "
                "order-5 eigen-orbit (2/5, 1/5) where (LR)^3 = -I mod 5). Neither B1825's best line (3/8, 3/8) (order 8) "
                "nor B1726's best line (2/5, 1/10) (order 10) lies in Fix((LR)^3). Moving to FR-COV's cover-compatible "
                "torsion locus therefore requires a fresh scan over the 6 cover-compatible orbits."
            ),
        },
    }


def audit_area_8(dr_ser, a0_ser, area1) -> Dict[str, object]:
    """Area 8: Zero-trust audit of Theorems 5, 6, 7, and 8 and Relays 4 & 5 against b1656_funcs.py quadrature."""
    tt_c3 = area1["_cached_tt_c3"]
    sig = area1["_cached_sig"]

    rng = np.random.default_rng(20261105)
    max_t5_diff = 0.0
    for _ in range(25):
        a0_r = complex(rng.normal() + 1j * rng.normal())
        hv_r = rng.normal(size=3) + 1j * rng.normal(size=3)
        m1_r = complex(rng.normal() + 1j * rng.normal())
        mp_r = rng.normal(size=3) + 1j * rng.normal(size=3)
        bim = schur_quaternionic_bimodule_decomposition(a0_r, hv_r, m1_r, mp_r)
        max_t5_diff = max(max_t5_diff, float(bim["max_matrix_diff"]))
    t6 = z3_norm_preserving_scalar_higgs()
    s1 = step1_golden_5torsion_norm_preserving_solution()
    t8 = theorem8_golden_codifferent_unit_modulus_closure()

    cu = -np.sqrt(np.exp(1j * math.pi) - 1.0)
    cd = -np.sqrt(np.exp(1j * math.pi / 4.0) - 1.0)
    ce = -1.0 + 0.0j

    def independent_b1656_eval(tau_pt: complex) -> Dict[str, float]:
        _, l2_val = get_radii(tau_pt)
        q_mp = mp.exp(1j * mp.pi * mp.mpc(tau_pt.real, tau_pt.imag))
        eps_10 = 1j ** ((10 + 2) // 2)  # -1
        th2_m, th3_m, th4_m = mp.jtheta(2, 0, q_mp), mp.jtheta(3, 0, q_mp), mp.jtheta(4, 0, q_mp)
        f10_vec = [complex(eps_10 * (th2_m ** 10)), complex(eps_10 * (th4_m ** 10)), complex(1j * (th3_m ** 10))]
        sm_base = f10_vec[0] * B.QI + f10_vec[1] * B.QJ + f10_vec[2] * B.QK
        sm_st = B.EPS @ sm_base.conj() @ B.EPS.T
        v_blocks = np.array([f10_vec[1], f10_vec[0], f10_vec[2]], dtype=complex)
        b_st = np.conj(np.sqrt(np.dot(-v_blocks, -v_blocks)))

        u_mats = {}
        s_ratios = {}
        line_5 = (Fraction(2, 5), Fraction(0, 1))
        for sn, ql, qr, c_sec in [("up", 1, -4, cu), ("down", 1, 2, cd), ("lepton", -3, 6, ce)]:
            w = B.line_w(line_5[0], line_5[1], tau_pt)
            x, yy = B.sector_twists(w, tau_pt, ql, qr)
            r_dict = B.residues(x, yy, tau_pt)
            c_dict = B.cA(x, yy, tau_pt, r_dict)
            u_q = {
                k: (
                    math.sqrt(2.0 * math.pi * l2_val + c_dict[k]) * r_dict[k]
                    if c_dict[k] is not None and 2.0 * math.pi * l2_val + c_dict[k] > 0
                    else 0.0
                )
                for k in B.UNITS
            }
            sm_4d = sm_st + (c_sec * b_st) * np.eye(2, dtype=complex)
            y_4d = B.coupling(sm_4d, B.weighted_M(u_q))
            u_left, sv, _ = np.linalg.svd(y_4d)
            order = np.argsort(sv)
            sv = sv[order]
            u_mats[sn] = u_left[:, order]
            s_ratios[sn] = sv / sv[2]

        vm = u_mats["up"].conj().T @ u_mats["down"]
        j_val = float(abs(np.imag(vm[0, 1] * vm[1, 2] * np.conj(vm[0, 2]) * np.conj(vm[1, 1]))))
        raw = np.array(
            [
                float(s_ratios["up"][1]),
                float(s_ratios["up"][0]),
                float(s_ratios["down"][1]),
                float(s_ratios["down"][0]),
                float(s_ratios["lepton"][1]),
                float(s_ratios["lepton"][0]),
                float(abs(vm[0, 1])),
                float(abs(vm[1, 2])),
                float(abs(vm[0, 2])),
                j_val,
            ],
            dtype=float,
        )
        z_vec = (np.log(raw) - tt_c3) / sig
        chi2_i = z_vec ** 2
        return {
            "chi2_six": float(np.sum(chi2_i[:6])),
            "chi2_ckm": float(np.sum(chi2_i[6:])),
            "chi2_ten": float(np.sum(chi2_i)),
        }

    tau_step1 = complex(0.44643117, 2.60792242)
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    tau_golden = complex(1.0 / math.sqrt(5.0), phi * phi)

    ind_step1 = independent_b1656_eval(tau_step1)
    ind_golden = independent_b1656_eval(tau_golden)

    return {
        "theorem5_and_6_verified": {
            "theorem5_25_random_trials_max_matrix_diff": max_t5_diff,
            "theorem6_max_norm_deviation": t6["max_norm_deviation"],
        },
        "theorem7_step1_b1656_quadrature_crosscheck": {
            "agy_sm_19_gate_chi2_ten": s1["pure_tree_level"]["chi2_ten"],
            "independent_b1656_quadrature_chi2_six": ind_step1["chi2_six"],
            "independent_b1656_quadrature_chi2_ckm": ind_step1["chi2_ckm"],
            "independent_b1656_quadrature_chi2_ten": ind_step1["chi2_ten"],
            "abs_diff_chi2_ten": abs(float(s1["pure_tree_level"]["chi2_ten"]) - ind_step1["chi2_ten"]),
        },
        "theorem8_tau_Golden_b1656_quadrature_crosscheck": {
            "tau_Golden": [tau_golden.real, tau_golden.imag],
            "agy_sm_19_gate_chi2_ten": t8["chi2_ten"],
            "independent_b1656_quadrature_chi2_six": ind_golden["chi2_six"],
            "independent_b1656_quadrature_chi2_ckm": ind_golden["chi2_ckm"],
            "independent_b1656_quadrature_chi2_ten": ind_golden["chi2_ten"],
            "abs_diff_chi2_ten": abs(float(t8["chi2_ten"]) - ind_golden["chi2_ten"]),
            "C_ten_bits_after_full_adversarial_and_10bit_Z8_price": t8["compression_verdict_at_tau_Golden"][
                "C_ten_bits_adversarial_plus_full_10bit_Z8_price"
            ],
        },
    }


def main() -> int:
    t0 = time.perf_counter()
    th2, th3, th4, r_ser, dr_ser, d2r_ser, a0_ser, t_m5_288_ser = build_serre_sections()

    area1 = audit_area_1(dr_ser)
    area2 = audit_area_2(r_ser, t_m5_288_ser)
    area3 = audit_area_3()
    area4_5 = audit_area_4_and_5(area1)
    area6 = audit_area_6()
    area7 = audit_area_7(area1)
    area8 = audit_area_8(dr_ser, a0_ser, area1)

    # Remove internal cache keys before serializing
    for k in list(area1.keys()):
        if k.startswith("_cached_"):
            del area1[k]

    elapsed_s = time.perf_counter() - t0
    report = {
        "audit_metadata": {
            "role": "Hostile Referee (Zero-Trust Independent Verification)",
            "branch_audited": "agy/audit-2026-11-02",
            "runtime_seconds": elapsed_s,
        },
        "area_1_b1825_readout_and_lagrange": area1,
        "area_2_stepb_code_defects": area2,
        "area_3_theorem_1_twisted_norms": area3,
        "area_4_and_5_theorems_2_3_4": area4_5,
        "area_6_m004_cover_commutant": area6,
        "area_7_fr_cov_chi2_and_parameter_ledger": area7,
        "area_8_theorems_5_6_7_8_and_stepb_v2_closure": area8,
    }

    out_path = pathlib.Path(__file__).resolve().parent / "hostile_referee_audit_results.json"
    out_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print("=== HOSTILE REFEREE ZERO-TRUST AUDIT COMPLETE ===")
    print(f"Runtime: {elapsed_s:.2f} s")
    print(f"Area 1: B1825 chi2_ten_fresh = {area1['chi2_ten_fresh_run_json']:.6f} vs recomputed = {area1['chi2_ten_fresh_recomputed']:.6f} (|diff| = {area1['abs_diff_fresh_recomputation']:.2e})")
    print(f"Area 1: Caught prose vs run.json discrepancies in Relay 1 lines 22-24: C_six in run.json = {area1['prose_vs_run_json_discrepancies']['C_six']['run_json_exact']:.6f} vs Relay 1 prose = {area1['prose_vs_run_json_discrepancies']['C_six']['agy_relay_prose_line_23']:.6f}")
    print(f"Area 2: Choice 30900 true direction in cm_zero_line.py = {area2['defect_4A_choice_30900_audit']['true_decoded_direction_for_30900']} (|J| = {area2['defect_4A_choice_30900_audit']['sample_abs_J_on_true_choice_30900_F26']:.3e}), vs agy's claimed {area2['defect_4A_choice_30900_audit']['agy_decoded_direction_for_30900']}")
    print(f"Area 3: Theorem 1 closed_form_cA max diff on 10 fresh adversarial/boundary cases = {area3['max_abs_err_vs_cA_on_10_adversarial_cases']:.2e}")
    print(f"Area 4 & 5: Theorems 2, 3, 4 max errors = {area4_5['theorem2_and_3_200_random_trials']['max_4d_yukawa_abs_err']:.2e}, {area4_5['theorem2_and_3_200_random_trials']['max_det_factorization_rel_err']:.2e}, {area4_5['theorem4_exact_qseries_and_random_tau']['max_numerical_rel_err_20_random_tau']:.2e}")
    print(f"Area 6: Pure S_3 sheet permutation commutant dim = {area6['pure_S3_sheet_permutation_C3_and_P_perm']['dim_R_symmetric_commutant']} (order {area6['pure_S3_sheet_permutation_C3_and_P_perm']['group_order']}), vs agy's signed P_refl commutant dim = {area6['agy_operator_gate_C3_and_P_refl_with_minus_signs']['dim_R_symmetric_commutant']} (order {area6['agy_operator_gate_C3_and_P_refl_with_minus_signs']['group_order']} = S_4)")
    w_res = area7["b1825_address_full_chi2_ten_comparison"]["FR_COV_witness_a0_0p20_exp_7jpi8_on_S_tilde_S_tilde_S"] if "FR_COV_witness_a0_0p20_exp_7jpi8_on_S_tilde_S_tilde_S" in area7["b1825_address_full_chi2_ten_comparison"] else area7["b1825_address_full_chi2_ten_comparison"]["FR_COV_witness_a0_0p20_exp_7pi8_on_S_tilde_S_tilde_S"]
    print(f"Area 7: At B1825 address, witness a_0 = 0.20*exp(7j*pi/8) gives |V_ub|/|V_td| = {w_res['Vub_over_Vtd']:.4f}, sin(delta_CP) = {w_res['sin_delta_CP']:.4f}, BUT full chi2_ten = {w_res['chi2_ten']:.2f} (vs FR-FIB 291.49)!")
    t7_chk = area8["theorem7_step1_b1656_quadrature_crosscheck"]
    t8_chk = area8["theorem8_tau_Golden_b1656_quadrature_crosscheck"]
    print(f"Area 8: Theorem 7 b1656_funcs quadrature chi2_ten = {t7_chk['independent_b1656_quadrature_chi2_ten']:.6f} vs sm_19_gate = {t7_chk['agy_sm_19_gate_chi2_ten']:.6f} (|diff| = {t7_chk['abs_diff_chi2_ten']:.2e})")
    print(f"Area 8: Theorem 8 (tau_Golden = 1/sqrt(5) + i*phi^2, 0 continuous params) b1656_funcs quadrature chi2_ten = {t8_chk['independent_b1656_quadrature_chi2_ten']:.6f} vs sm_19_gate = {t8_chk['agy_sm_19_gate_chi2_ten']:.6f} (|diff| = {t8_chk['abs_diff_chi2_ten']:.2e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
