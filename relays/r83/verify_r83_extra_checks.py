#!/usr/bin/env python3
"""Supplemental fast (< 5s) Review 83 counterchecks (seat agy-002, card A2-R83 / M38).

Records reproducible machine checks for:
  1. B1941:
     - All 4 draws of random.Random(1939) at yv = 0.9 have x^2 + yv^2 < 1 (0 points below y = 1.2 tested).
     - Exact 50-digit mpmath evaluation at tau in {i, omega, 1.03i, 1.05i, -0.077982 + 1.051250i} showing
       Delta(i) = Delta(omega) = 0 and Delta(1.03i) = -0.115145 < 0, Delta(1.05i) = -0.392229 < 0 (both (3,3,1)
       and (1,1,1) weights), proving a positive measure supported near 1.05i reverses the fermion determinant's sign.
     - s4_pointwise_run.txt min +1.381e+00 (+1.38) vs FINDINGS.md line 33 (+1.83).
  2. B1938:
     - gauge_class_control_run.txt max |z| = 6.4 (> 3.0 threshold) vs FINDINGS.md line 83 max |z| = 2.4 (< 3.0).
  3. B1944:
     - read_the_look_run.txt W+|b |V_cb| frame/measured = 17.6 (and exp(pull * sigma) = 17.594) vs FINDINGS.md line 56 = 7.6.
  4. B1943:
     - Exact fixed torsion points of RL mod 5: {(1,3), (2,1), (3,4), (4,2)} != LR's {(1,2), (2,4), (3,1), (4,3)}.
  5. B1932:
     - pairs/q2_run.txt canon L_2 mirror residual 2.48e-5 vs const L_2 7.87e-11 (FINDINGS.md line 47 cites 8e-11).
     - ergodic_t90.json |dln| / (se/R) ratios: |V_13| = 3.25 (< 5, vs FINDINGS.md line 33 '5 to 11 times').
     - BIG_RUN_VALUES.json |ln(b/a)| range in W+: min 0.0729 (< 0.10, vs FINDINGS.md line 41 '0.10 to 0.58').

Zero physical 7-values are emitted. 0 of 19.
"""

from __future__ import annotations

import json
import math
import random
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "relays" / "r83"))
import verify_r83_counterchecks as rc  # our standalone module


def git_show(path: str) -> str:
    return subprocess.check_output(["git", "-C", str(REPO_ROOT), "show", f"b35eac607:{path}"]).decode("utf-8")


def main() -> None:
    l2_interp = rc.a2c.CanonicalL2Interpolant()

    # 1. B1941 checks:
    rng = random.Random(1939)
    y09_draws = []
    pts_kept = []
    for yv in (0.9, 1.2, 1.6, 2.2, 3.0, 4.5, 6.0, 9.0):
        for _ in range(4):
            x = rng.uniform(-0.5, 0.5)
            norm_sq = x * x + yv * yv
            if yv == 0.9:
                y09_draws.append({"x": round(x, 8), "abs_tau_sq": round(norm_sq, 8), "kept": norm_sq >= 1.0})
            if norm_sq >= 1.0:
                pts_kept.append((x, yv))

    special_taus = [
        ("i", 1.0j),
        ("omega", 0.5 + 0.5j * math.sqrt(3.0)),
        ("1.03i", 1.03j),
        ("1.05i", 1.05j),
        ("ind11", -0.077982 + 1.051250j),
    ]
    special_evals = {}
    for label, t in special_taus:
        l2_v = float(l2_interp.eval_fd(np.array([t]))[0])
        st = rc.eval_mp_det_and_tr2_12pt(t, l2_v, exact_weight=True)
        d331 = 3.0 * (st[("up", "St")][0] - st[("up", "S")][0]) + 4.0 * (st[("down", "S")][0] - st[("down", "St")][0])
        d111 = 1.0 * (st[("up", "St")][0] - st[("up", "S")][0]) + 2.0 * (st[("down", "S")][0] - st[("down", "St")][0])
        special_evals[label] = {
            "tau": [round(t.real, 8), round(t.imag, 8)],
            "abs_tau_sq": round(abs(t) ** 2, 8),
            "L_2": round(l2_v, 8),
            "Delta_ln_det_331": round(d331, 8),
            "Delta_ln_det_111": round(d111, 8),
        }

    s4_run = git_show(
        "frontier/B1941_a_fermion_determinant_prefers_one_higgs_world_at_every_point_and_a_one_loop_trace_the_other/verification/s4_pointwise_run.txt"
    )
    m_s4 = re.search(r"ln det, weights 3,3,1, exact weight\s+positive at\s+(\d+) of (\d+) points\s+min ([0-9.e+-]+)\s+max ([0-9.e+-]+)", s4_run)
    assert m_s4 is not None

    # 2. B1938 control check:
    b1938_ctl = git_show(
        "frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/verification/gauge_class_control_run.txt"
    ).strip()
    m_ctl = re.search(r"max \|z\| ([0-9.]+)", b1938_ctl)
    assert m_ctl is not None

    # 3. B1944 W+|b |V_cb| frame/measured check:
    b1944_run = git_show(
        "frontier/B1944_the_big_run_read_frame_c_fails_and_the_average_washes_out_the_hierarchy/verification/read_the_look_run.txt"
    )
    b1940_out_v3 = json.loads(
        git_show("frontier/B1940_the_area_options_corrected_in_extended_precision/verification/big_run_output_v3.json")
    )
    # In big_run_output_v3.json, pulls_nine[7] is |V_cb| with sigma floor 0.1017...:
    # Extract directly from read_the_look_run.txt W+|b block:
    m_b1944 = re.search(r"W\+\|b.*?\|V_cb\|\s+([0-9.]+)", b1944_run, flags=re.S)
    assert m_b1944 is not None

    # 4. B1943 RL vs LR fixed points mod 5:
    L = np.array([[1, 1], [0, 1]], dtype=int)
    R = np.array([[1, 0], [1, 1]], dtype=int)
    lr_pts5 = rc.fixed_up_to_sign_orders(L @ R, 10)[5]
    rl_pts5 = rc.fixed_up_to_sign_orders(R @ L, 10)[5]

    # 5. B1932 checks (log-ratios and z-multiples only; zero raw 7-values):
    e_t90 = json.loads(
        git_show(
            "frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/ergodic_t90.json"
        )
    )
    r_tr = np.array(e_t90["R_truncated"], dtype=float)
    r_ex = np.array(e_t90["R_exact_weight"], dtype=float)
    se_tr = np.array(e_t90["se_truncated"], dtype=float)
    dln_over_rel_se = [round(float(abs(math.log(r_ex[i] / r_tr[i])) / (se_tr[i] / r_tr[i])), 4) for i in range(7)]

    v_b1932 = json.loads(
        git_show(
            "frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/BIG_RUN_VALUES.json"
        )
    )
    wm_dln = [
        round(abs(math.log(v_b1932["options"]["W-|b (area)"]["values"][i] / v_b1932["options"]["W-|a (move count)"]["values"][i])), 6)
        for i in range(7)
    ]
    wp_dln = [
        round(abs(math.log(v_b1932["options"]["W+|b (area)"]["values"][i] / v_b1932["options"]["W+|a (move count)"]["values"][i])), 6)
        for i in range(7)
    ]

    out = {
        "b1941": {
            "seed_1939_yv_0_9_draws": y09_draws,
            "seed_1939_actual_min_height": min(y for _, y in pts_kept),
            "s4_run_txt_331_exact_min_max": [float(m_s4.group(3)), float(m_s4.group(4))],
            "findings_line_33_claimed_min": 1.83,
            "special_lower_fd_points_mpmath": special_evals,
        },
        "b1938": {
            "gauge_class_control_run_max_abs_z": float(m_ctl.group(1)),
            "findings_line_83_claimed_max_abs_z": 2.4,
            "control_threshold_for_CAUGHT": 3.0,
        },
        "b1944": {
            "read_the_look_run_W_plus_b_Vcb_ratio": float(m_b1944.group(1)),
            "findings_line_56_claimed_Vcb_ratio": 7.6,
        },
        "b1943": {
            "LR_fixed_points_mod_5": lr_pts5,
            "RL_fixed_points_mod_5": rl_pts5,
        },
        "b1932": {
            "ergodic_t90_abs_dln_over_rel_se": dln_over_rel_se,
            "W_minus_measure_abs_dln_min_max": [min(wm_dln), max(wm_dln)],
            "W_plus_measure_abs_dln_min_max": [min(wp_dln), max(wp_dln)],
        },
    }

    out_path = Path(__file__).resolve().parent / "verify_r83_extra_checks.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n")
    print("B1941 seed 1939 actual min height:", out["b1941"]["seed_1939_actual_min_height"])
    print("B1941 Delta(1.05i) 331 & 111:", special_evals["1.05i"]["Delta_ln_det_331"], special_evals["1.05i"]["Delta_ln_det_111"])
    print("B1938 control max |z|:", out["b1938"]["gauge_class_control_run_max_abs_z"], "vs FINDINGS:", 2.4)
    print("B1944 W+|b |V_cb| ratio:", out["b1944"]["read_the_look_run_W_plus_b_Vcb_ratio"], "vs FINDINGS:", 7.6)
    print("B1932 |V_13| shift / rel_se:", dln_over_rel_se[6], "; W+ measure min |dln|:", min(wp_dln))
    print("Saved", out_path.name, "successfully.")


if __name__ == "__main__":
    main()
