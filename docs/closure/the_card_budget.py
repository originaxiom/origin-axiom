#!/usr/bin/env python3
"""The closure cards' location-free information budget (P-611; the SM seat, relay section 351). Data-free arithmetic:
no measured central value and no frame value enters. Inputs are the bar's own definitions and the targets' measured
relative precisions.

THE_FINAL_ACTS_BAR: p_V = P_null(|X - v| <= |x - v|), X the pipeline's prediction in null worlds; PASSED needs v inside
the prediction's 68% band and p_V < 0.01/m_V. The budget models X near v as log-uniform over W decades (the bar's default
reference law), so p_V = 2 d / (W ln 10) for a distance d = |ln x - ln v| small against the range.

A frame whose true log-error is eps (Gaussian) gives d ~ |N(0, s)|, s = sqrt(eps^2 + sigma_exp^2). Its stated 68% band is
B = sqrt(sigma_th^2 + sigma_exp^2), with sigma_th the card's truncation allowance (S1.3: ALLOW for y_b/y_t, 2 ALLOW for r;
sigma_delta and sigma_num omitted, which only widens B). Two rules are budgeted:
  per-target (GENESIS v1.60 GAP1 condition 3 as written): each target d_i <= B_i and p_V,i < 0.01/m_V;
  joint (relay section 349, C4b, corrected in section 351): each d_i <= B_i and p_V,1 * p_V,2 < 0.01/m_V, the product
  being the independent-null value -- a LOWER bound on the true joint p_V, so this column is an upper bound on power.
"""
import json
import math
from pathlib import Path

import numpy as np

ALLOW = 0.10
SIG_EXP = {"y_b/y_t": 0.0102, "r": 0.0266}       # relative 1-sigma, rounded: HZ2021's m_b, m_t; NuFIT 6.0 IC24 NO
TH_FACTOR = {"y_b/y_t": 1.0, "r": 2.0}             # sigma_th = factor * ALLOW (S1.3 e, S2.2 e)
WS = (2, 3, 4, 6, 10)                               # decades of the log-uniform model
MVS = (2, 5, 10, 15, 20)
EPS = (0.0, 0.05, 0.10, 0.20)                       # the frame's true log-error per singular-value ratio
N_MC, SEED = 400_000, 351


def power_single(t, eps, W, mV):
    s = math.hypot(eps * TH_FACTOR[t], SIG_EXP[t])
    B = math.hypot(ALLOW * TH_FACTOR[t], SIG_EXP[t])
    dstar = 0.01 / mV * W * math.log(10) / 2
    return math.erf(min(B, dstar) / (s * math.sqrt(2)))


def power_joint(eps, W, mV, rng):
    d = {}
    for t in SIG_EXP:
        s = math.hypot(eps * TH_FACTOR[t], SIG_EXP[t])
        d[t] = np.abs(rng.normal(0.0, s, N_MC))
    B = {t: math.hypot(ALLOW * TH_FACTOR[t], SIG_EXP[t]) for t in SIG_EXP}
    f = 1 / (W * math.log(10))
    p = (2 * d["y_b/y_t"] * f) * (2 * d["r"] * f)
    ok = (d["y_b/y_t"] <= B["y_b/y_t"]) & (d["r"] <= B["r"]) & (p < 0.01 / mV)
    return float(ok.mean())


def w_required(t, eps, mV, z=0.6745):
    """the log-uniform width (decades) at which a median-distance frame reaches p_V = 0.01/m_V"""
    s = math.hypot(eps * TH_FACTOR[t], SIG_EXP[t])
    return 2 * z * s * mV / (0.01 * math.log(10))


def main():
    rng = np.random.default_rng(SEED)
    rows = []
    for eps in EPS:
        for W in WS:
            for mV in MVS:
                py, pr = power_single("y_b/y_t", eps, W, mV), power_single("r", eps, W, mV)
                rows.append({"eps": eps, "W_decades": W, "m_V": mV, "power_y": py, "power_r": pr,
                             "power_both_per_target": py * pr, "power_joint_upper": power_joint(eps, W, mV, rng)})
    wreq = {t: {f"eps={e}": {f"m_V={m}": w_required(t, e, m) for m in MVS} for e in EPS} for t in SIG_EXP}
    out = {"inputs": {"ALLOW": ALLOW, "sigma_exp": SIG_EXP, "th_factor": TH_FACTOR, "W": WS, "m_V": MVS, "eps": EPS,
                      "N_MC": N_MC, "seed": SEED}, "rows": rows, "W_required_decades": wreq}
    here = Path(__file__).resolve().parent
    (here / "the_card_budget.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    lines = ["eps  W  m_V  power_y  power_r  both_per_target  joint_upper"]
    for r in rows:
        lines.append(f"{r['eps']:.2f} {r['W_decades']:2d} {r['m_V']:3d}  {r['power_y']:.4f}  {r['power_r']:.4f}  "
                     f"{r['power_both_per_target']:.5f}  {r['power_joint_upper']:.4f}")
    lines.append("W required (decades), median-distance frame, p_V = 0.01/m_V:")
    for t in wreq:
        for e in wreq[t]:
            lines.append(f"  {t} {e}: " + ", ".join(f"{k} {v:.1f}" for k, v in wreq[t][e].items()))
    (here / "the_card_budget_run.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
