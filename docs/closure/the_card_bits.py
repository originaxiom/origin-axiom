#!/usr/bin/env python3
"""The closure cards' location-free information budget in bits (P-611; main's ask 2(b) of 2026-11-05; the SM seat,
relay section 352). Data-free: widths only -- no measured central value and no frame value enters.

A pass places the target inside the prediction's 68% band, of full width 2B in ln. Against a stated prior range of
W decades, uniform in ln, the band's guaranteed information is

    I = log2( W ln 10 / (2 B) )  bits,

and a pass with p_V < 0.01/m_V requires log2(m_V / 0.01) bits of rarity. B = sqrt(sigma_th^2 + sigma_exp^2), with
sigma_th = k ALLOW (k = 1 for y_b/y_t, k = 2 for r; relay section 349, S1.3 and S2.2); sigma_delta and sigma_num are
omitted (they only widen B, so I is an upper bound). Rows are given at sigma_th = k ALLOW and at smaller declared values,
down to sigma_th = 0, where I is the measured precision's own information (P-611's best case).
"""
import json
import math
from pathlib import Path

ALLOW = 0.10
SIG_EXP = {"y_b/y_t": 0.0102, "r": 0.0266}         # relative 1-sigma (rounded): HZ2021 m_b, m_t; NuFIT 6.0 IC24 NO
K = {"y_b/y_t": 1.0, "r": 2.0}
PRIOR_W = {"y_b/y_t": (2, 3, 4, 6), "r": (2, 3, 4, 6)}
DECLARED = {"y_b/y_t": (10.0, 4.0, 4.0), "r": (1.0, 1e-4, 4.0)}   # (upper, lower, W): the ranges proposed in section 352
SIG_TH_PER_RATIO = (ALLOW, 0.05, 0.03, 0.01, 0.0)
MVS = (10, 12, 15, 19, 20)


def bits(t, W, s_ratio):
    B = math.hypot(K[t] * s_ratio, SIG_EXP[t])
    return math.log2(W * math.log(10) / (2 * B))


def main():
    rows = []
    for t in SIG_EXP:
        for s in SIG_TH_PER_RATIO:
            for W in PRIOR_W[t]:
                rows.append({"target": t, "sigma_th_per_ratio": s, "W_decades": W, "bits": bits(t, W, s)})
    need = {f"m_V={m}": math.log2(m / 0.01) for m in MVS}
    joint = {}
    for s in SIG_TH_PER_RATIO:
        Wy, Wr = DECLARED["y_b/y_t"][2], DECLARED["r"][2]
        joint[f"sigma_th={s}"] = bits("y_b/y_t", Wy, s) + bits("r", Wr, s)
    out = {"inputs": {"ALLOW": ALLOW, "sigma_exp": SIG_EXP, "k": K, "declared_prior_ranges": DECLARED},
           "rows": rows, "bits_needed_for_p_V_below_0.01_over_m_V": need,
           "joint_band_bits_at_declared_ranges_upper_bound": joint}
    here = Path(__file__).resolve().parent
    (here / "the_card_bits.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    lines = ["target   sigma_th/ratio  W  bits"]
    for r in rows:
        lines.append(f"{r['target']:8s} {r['sigma_th_per_ratio']:.2f}  {r['W_decades']}  {r['bits']:.2f}")
    lines.append("bits needed: " + ", ".join(f"{k} {v:.2f}" for k, v in need.items()))
    lines.append("joint band bits at the declared ranges (y 4 decades, r 4 decades), an upper bound (independence):")
    lines += [f"  {k}: {v:.2f}" for k, v in joint.items()]
    (here / "the_card_bits_run.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
