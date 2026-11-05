#!/usr/bin/env python3
"""The bit balance of a screen on the six (main's question (a)/(b) of 2026-11-05; the SM seat, relay section 353).
Data-free bookkeeping: no frame value and no held-out target enters. Inputs are the screen's own definitions (B1741's
compare.py: the six's sigmas with ALLOW, draws()' prior ranges) and HZ2021's printed relative errors of the six's masses
(in-sample data precisions, the six's own file).

A ratio inside a band of 1-sigma half-width s (in ln), against a prior range of W decades uniform in ln, carries
log2(W ln 10 / (2 s)) bits; the six carry the sum. A menu of K equally available configurations costs log2 K bits, and a
continuous input costs log2(its ln-range / (2 s)) at the resolution of the ratios it moves. The balance (data bits minus
menu bits) is a crude, order-of-magnitude estimate of -log2 p for a matched null; it ignores correlations between rows
(which lower the menu's effective cost) and the chi^2 threshold's shape.
"""
import json
import math
from pathlib import Path

LN10 = math.log(10)
# HZ2021 Table 2/3, 'MZ, Full SM': relative 1-sigma of each mass (the six's file)
REL = {"t": 0.75 / 168.26, "c": 0.017 / 0.620, "u": 0.21 / 1.23, "b": 0.026 / 2.839, "s": 4.61 / 53.16,
       "d": 0.19 / 2.67, "tau": 0.00028 / 1.72856, "mu": 0.000023 / 0.101766, "e": 0.00045 / 0.48307}
SIX = [("c/t", "c", "t", 2.0), ("u/t", "u", "t", 3.5), ("s/b", "s", "b", 2.0), ("d/b", "d", "b", 3.5),
       ("mu/tau", "mu", "tau", 2.0), ("e/tau", "e", "tau", 3.5)]       # W: draws()' r2 in 10^[-3,-1], r1 in 10^[-6,-2.5]
MENUS = {"B1841 (K = 4 ends)": 223 * 266 * 4 * 2, "B1839 (23 ends)": 223 * 266 * 23 * 2,
         "line and apex fixed by principle (ends 4, triple 2)": 4 * 2,
         "line, apex, end and triple fixed by principle": 1}
C_RANGE = math.log(5 / (1 / 3))                                       # c continuous in [1/3, 5]


def sigma(a, b, th):
    return math.sqrt(REL[a] ** 2 + REL[b] ** 2 + th ** 2)


def main():
    out = {"rows": []}
    for th in (0.10, 0.05, 0.03, 0.01, 0.0):
        per = {n: math.log2(W * LN10 / (2 * sigma(a, b, th))) for n, a, b, W in SIX}
        quark = sum(per[n] for n in ("c/t", "u/t", "s/b", "d/b"))
        s_lep = sigma("mu", "tau", th)
        c_bits = math.log2(C_RANGE / (2 * s_lep)) if s_lep > 0 else float("inf")
        row = {"sigma_th": th, "bits_per_ratio": per, "six_bits": sum(per.values()), "quark_four_bits": quark,
               "c_bits": c_bits, "balance": {}}
        for k, K in MENUS.items():
            m = math.log2(K)
            row["balance"][k] = {"menu_bits_without_c": m, "six_minus_menu_and_c": sum(per.values()) - m - c_bits,
                                 "quark_four_minus_menu": quark - m}
        out["rows"].append(row)
    here = Path(__file__).resolve().parent
    (here / "the_bit_balance.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    lines = []
    for r in out["rows"]:
        lines.append(f"sigma_th {r['sigma_th']:.2f}: six {r['six_bits']:.1f} bits (quark four {r['quark_four_bits']:.1f}), "
                     f"c costs {r['c_bits']:.1f}")
        for k, b in r["balance"].items():
            lines.append(f"   {k}: menu {b['menu_bits_without_c']:.1f}; six - menu - c = {b['six_minus_menu_and_c']:+.1f}; "
                         f"quark four - menu = {b['quark_four_minus_menu']:+.1f}")
    (here / "the_bit_balance_run.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
