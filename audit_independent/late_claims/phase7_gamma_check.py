"""Phase 7 check: is gamma_six = (+1,-2,+2,+3/2,+1,0) the SM's 1-loop running, or a fit?

SM 1-loop (Machacek-Vaughn / e.g. Xing-Zhou-Zhou 2008), top-dominance, running DOWN from mu_UV to M_Z with
I = int y_t^2/(16 pi^2) dln mu:
   ln(m_c/m_t), ln(m_u/m_t)  : +3/2 I     (beta_{Y_u} contains +3/2 Y_u Y_u^dag)
   ln(m_s/m_b), ln(m_d/m_b)  : -3/2 I     (beta_{Y_d} contains -3/2 Y_u Y_u^dag; b feels y_t, s,d do not)
   lepton ratios              :  0         (no y_t generation dependence)
   |V_us|                     :  0
   |V_cb|, |V_ub|             : +3/2 I
   |J|                        : +3   I
"""
from __future__ import annotations

import itertools
import json
import sys

import numpy as np

sys.path.insert(0, "/Users/dri/.gemini/antigravity/scratch/agy-snapshot-dfe4c6f90/src")
from origin_axiom.sm_19_gate import C3_SHIFTED_TARGETS_10, GAMMA_TOP_10, SIGMA_LOG_10  # noqa: E402
from origin_axiom.toe_closure import phase7_exact_it_rge_light_generation_closure  # noqa: E402

p7 = phase7_exact_it_rge_light_generation_closure()
I = p7["I_t_exact_1loop_integral"]
from agy_eval import TAU_GOLDEN, observables  # noqa: E402
obs = observables(TAU_GOLDEN)
# agy's t8 used n_terms=14/dps=20/n_pts=64; recompute with those for exactness
from origin_axiom.sm_19_gate import theorem8_golden_codifferent_unit_modulus_closure  # noqa: E402
obs = np.array(theorem8_golden_codifferent_unit_modulus_closure()["observables_10"])


def chi2(o):
    z = (np.log(o) - np.log(C3_SHIFTED_TARGETS_10)) / SIGMA_LOG_10
    return float(np.sum(z[:6] ** 2)), float(np.sum(z[6:] ** 2)), float(np.sum(z ** 2)), z


res = {"I_t_agy": I, "tree": chi2(obs)[:3]}
vecs = {
    "phase7_agy (+1,-2,+2,+1.5,+1,0,...)": np.array([1, -2, 2, 1.5, 1, 0, 0, 0, 0, 0.0]),
    "sm_19_gate GAMMA_TOP_10 (agy earlier)": GAMMA_TOP_10,
    "SM 1-loop top-dominance (downward)": np.array([1.5, 1.5, -1.5, -1.5, 0, 0, 0, 1.5, 1.5, 3.0]),
}
for nm, g in vecs.items():
    s, c, t, z = chi2(obs * np.exp(g * I))
    res[nm] = {"chi2_six": s, "chi2_ckm": c, "chi2_ten": t, "passes_gate_23.209": t <= 23.209251158954356 and s <= 16.811893829770927 and c <= 15.086272469388987,
               "z": np.round(z, 2).tolist()}

# Is agy's vector a fit? Search all half-integer vectors in [-3,3]^5 (e/tau fixed 0, CKM untouched as in phase 7)
grid = np.arange(-3, 3.01, 0.5)
lo = np.log(obs[:5]); tg = np.log(C3_SHIFTED_TARGETS_10[:5]); sg = SIGMA_LOG_10[:5]
best = []
G = np.array(list(itertools.product(grid, repeat=5)))
Z = (lo[None, :] + G * I - tg[None, :]) / sg[None, :]
chi5 = np.sum(Z ** 2, axis=1) + chi2(obs)[3][5] ** 2
order = np.argsort(chi5)
agy_g = np.array([1, -2, 2, 1.5, 1])
agy_idx = int(np.where(np.all(G == agy_g, axis=1))[0][0])
rank = int(np.where(order == agy_idx)[0][0]) + 1
res["gamma_search"] = {
    "n_half_integer_vectors": int(len(G)),
    "agy_vector_chi2_six": float(chi5[agy_idx]),
    "agy_vector_rank": rank,
    "best5": [(G[k].tolist(), float(chi5[k])) for k in order[:5]],
    "unconstrained_optimum_per_entry_(gamma=(ln target - ln obs)/I)": ((tg - lo) / I).round(2).tolist(),
}
print(json.dumps(res, indent=1))
json.dump(res, open("phase7_gamma_check.json", "w"), indent=1)
