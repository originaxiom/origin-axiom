"""RGE check of agy's Higgs-mass 'predictions' (Theorem 9C 1-loop: 132.07 GeV; Phase 3 2-loop: 126.28 GeV).

agy integrates in t = ln(mu/M_Z)/(2*pi). In that variable the textbook SM running is
  d g_i^2/dt   = b_i g_i^4 / (4 pi)                     (agy: (2 b_i) g^4 /(8 pi)  -> correct)
  d y_t^2/dt   = y_t^2 [9/2 y_t^2 - 8 g3^2 - 9/4 g2^2 - 17/20 g1^2] / (4 pi)   (agy divides by 8 pi -> half)
  d lam/dt     = [24 lam^2 + 12 lam y_t^2 - 6 y_t^4 - 3 lam(3 g2^2 + 3/5 g1^2) + 3/8(2 g2^4 + (g2^2 + 3/5 g1^2)^2)] / (8 pi)
                 (agy: 12 lam^2 + 6 lam y^2 - 3 y^4 - 1.5 lam(...) + 3/16(...) over 8 pi -> half)
with V = lam (H^dag H)^2, m_H^2 = 2 lam v^2 (agy's own convention: m_H = sqrt(2 lam) v).
2-loop: agy's 2-loop lam and y_t pieces (Buttazzo et al. 2013 dominant terms) are likewise exactly half
(30 y^6 -> 15, -32 g3^2 y^4 -> -16, 80 -> 40, -3 -> -1.5, -144 -> -72, -312 -> -156); its 2-loop g3 piece (-52) is right.

We rerun agy's exact boundary conditions with (a) agy's code as written, (b) the factor-2 bug fixed,
keeping agy's truncation, and (c) PDG low-energy inputs for reference.
"""
from __future__ import annotations

import json
import math
import sys

import numpy as np

sys.path.insert(0, "/Users/dri/.gemini/antigravity/scratch/agy-snapshot-dfe4c6f90/src")
from origin_axiom.sm_19_gate import theorem9_hypercharge_quadratic_refinement_and_full_19_closure  # noqa: E402

V_EW = 246.21965
MZ = 91.1876


def make_deriv(fix: bool, two_loop: bool):
    s = 2.0 if fix else 1.0
    f1 = 1.0 / (8.0 * math.pi)
    f2 = 1.0 / (128.0 * math.pi ** 3)

    def deriv(st):
        g1, g2, g3, yt, lam = st
        dg1 = (41.0 / 5.0) * g1 ** 2 * f1
        dg2 = (-19.0 / 3.0) * g2 ** 2 * f1
        dg3 = (-14.0) * g3 ** 2 * f1
        dyt = s * yt * (4.5 * yt - 8.0 * g3 - 2.25 * g2 - 0.85 * g1) * f1
        dlam = s * (12.0 * lam ** 2 + 6.0 * lam * yt - 3.0 * yt ** 2 - 1.5 * lam * (3.0 * g2 + 0.6 * g1)
                    + (3.0 / 16.0) * (2.0 * g2 ** 2 + (g2 + 0.6 * g1) ** 2)) * f1
        if two_loop:
            dg3 += -52.0 * g3 ** 3 * f2
            dyt += s * yt * (-12.0 * yt ** 2 + 36.0 * g3 * yt - 108.0 * g3 ** 2) * f2
            dlam += s * (15.0 * yt ** 3 - 16.0 * g3 * yt ** 2 + 40.0 * g3 * lam * yt - 1.5 * lam * yt ** 2
                         - 72.0 * lam ** 2 * yt - 156.0 * lam ** 3) * f2
        return np.array([dg1, dg2, dg3, dyt, dlam])

    return deriv


def lam_at_top(state0, t_end, deriv, n=2000):
    st = np.array(state0, dtype=float)
    dt = t_end / n
    for _ in range(n):
        k1 = deriv(st); k2 = deriv(st + 0.5 * dt * k1); k3 = deriv(st + 0.5 * dt * k2); k4 = deriv(st + dt * k3)
        st = st + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
    return st


def solve_mh(g1, g2, g3, yt2, t_end, fix, two_loop):
    deriv = make_deriv(fix, two_loop)
    lo, hi = 0.0, 0.4
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if lam_at_top([g1, g2, g3, yt2, mid], t_end, deriv)[4] < 0:
            lo = mid
        else:
            hi = mid
    lam = 0.5 * (lo + hi)
    return lam, math.sqrt(2 * lam) * V_EW


t9 = theorem9_hypercharge_quadratic_refinement_and_full_19_closure()
pb = t9["part_B_zero_input_m004_gauge_and_hierarchy"]; pc = t9["part_C_block_V_strong_cp_top_and_higgs_criticality"]
a12, t12 = pb["alpha_12_inv_pred_21_vol_m004"], pb["t_12_pred_2_vol_m004"]
a1 = a12 + 4.1 * t12; a2 = a12 - 19 / 6 * t12; a3 = a12 - 7 * math.log(4 / 3 ** 0.5) - 7 * t12
g1, g2, g3 = 4 * math.pi / a1, 4 * math.pi / a2, 4 * math.pi / a3
mt_pole = pc["mt_pole_GeV_pred"]
# 1-loop chain (Theorem 9C): MSbar via 1-loop QCD
yt2_1 = (math.sqrt(2) * mt_pole * (1 - 4 * (1 / a3) / (3 * math.pi)) / V_EW) ** 2
asp = (1 / a3) / math.pi
yt2_2 = (math.sqrt(2) * mt_pole / (1 + 4 / 3 * asp + 8.23 * asp ** 2) / V_EW) ** 2

res = {"inputs": {"alpha12_inv": a12, "t12": t12, "M12_GeV": MZ * math.exp(2 * math.pi * t12), "mt_pole": mt_pole,
                  "alpha_s_MZ": 1 / a3}}
for name, yt2, two in [("theorem9C_1loop", yt2_1, False), ("phase3_2loop", yt2_2, True)]:
    lam_bug, mh_bug = solve_mh(g1, g2, g3, yt2, t12, fix=False, two_loop=two)
    lam_fix, mh_fix = solve_mh(g1, g2, g3, yt2, t12, fix=True, two_loop=two)
    res[name] = {"agy_as_written": {"lambda_MZ": lam_bug, "mH": mh_bug},
                 "factor2_fixed": {"lambda_MZ": lam_fix, "mH": mh_fix}}

# Reference: PDG-ish inputs at M_Z
aem, s2w, as_ = 127.951, 0.23122, 0.1179
a1p = 0.6 * aem * (1 - s2w); a2p = aem * s2w; a3p = 1 / as_
asp = as_ / math.pi
yt2_p = (math.sqrt(2) * 172.69 / (1 + 4 / 3 * asp + 8.23 * asp ** 2) / V_EW) ** 2
for nm, tend in [("lambda0_at_M12_1.09e13", t12), ("lambda0_at_Mpl_2.4e18", math.log(2.435e18 / MZ) / (2 * math.pi))]:
    res["PDG_inputs_" + nm] = {
        "agy_as_written_2loop": solve_mh(4 * math.pi / a1p, 4 * math.pi / a2p, 4 * math.pi / a3p, yt2_p, tend, False, True)[1],
        "factor2_fixed_2loop": solve_mh(4 * math.pi / a1p, 4 * math.pi / a2p, 4 * math.pi / a3p, yt2_p, tend, True, True)[1],
    }
print(json.dumps(res, indent=1))
json.dump(res, open("rge_check_results.json", "w"), indent=1)
