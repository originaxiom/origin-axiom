"""Sensitivity of agy's inter-sector, neutrino and PMNS outputs to the hand-set constants in the code."""
from __future__ import annotations

import itertools
import json
import math
import sys

import mpmath as mp
import numpy as np

sys.path.insert(0, "/Users/dri/.gemini/antigravity/scratch/agy-snapshot-dfe4c6f90/src")
from origin_axiom.sm_19_gate import _f10_st_and_scalar, theorem8_golden_codifferent_unit_modulus_closure  # noqa: E402
from origin_axiom.toe_closure import (  # noqa: E402
    phase2_weinberg_neutrino_spectrum_closure,
    phase6_complete_pmns_unitary_and_cp_closure,
    phase7_exact_it_rge_light_generation_closure,
)

PHI = (1 + 5 ** 0.5) / 2
TG = complex(1 / 5 ** 0.5, PHI ** 2)
res = {}

# 1. 'eta6_quarter' = |b_st|^2 vs the actual |eta(tau)|^6/4
_, b = _f10_st_and_scalar(TG)
q = mp.exp(2j * mp.pi * mp.mpc(TG.real, TG.imag))
eta = q ** (mp.mpf(1) / 24) * mp.qp(q)
res["eta_check"] = {"abs_b_st_sq (agy 'eta6_quarter')": float(abs(b) ** 2), "true_abs_eta^6/4": float(abs(eta) ** 6 / 4),
                    "ratio": float(abs(b) ** 2 / (abs(eta) ** 6 / 4))}

# 2. Inter-sector: m_b/m_tau and m_t/m_b dependence on I_top=0.1462 and exp(-0.0170)
t8 = theorem8_golden_codifferent_unit_modulus_closure()
inter = t8["inter_sector_scales"]
I7 = phase7_exact_it_rge_light_generation_closure()["I_t_exact_1loop_integral"]
mbt = inter["mb_over_mtau_MZ_pred"]; mtb = inter["mt_over_mb_MZ_pred"]
res["inter_sector"] = {
    "mb/mtau_agy(I=0.1462)": mbt, "pdg": 2.86 / 1.746,
    "mb/mtau_if_I=phase7_I_t(0.0984)": mbt * math.exp(0.1462 - I7),
    "mb/mtau_if_I=0": mbt * math.exp(0.1462),
    "mt/mb_agy(with exp(-0.0170))": mtb, "pdg": 171.7 / 2.85,
    "mt/mb_without_exp(-0.0170)": mtb * math.exp(0.0170),
    "note": "alpha_EM and sin2thetaW inside mb/mtau are PDG inputs (lines 742-743)",
}

# 3. Neutrinos: role of the inserted factors 3 and 1/3, and of I_top
p2 = phase2_weinberg_neutrino_spectrum_closure()
sv = p2["weinberg_singular_values"]
m3 = p2["m3_meV_pred"]
res["neutrino"] = {
    "m3_agy": m3, "m2_agy": p2["m2_meV_pred"], "m1_agy": p2["m1_meV_pred"],
    "m2_without_inserted_factor_3": m3 * sv[1] / sv[2], "m1_without_inserted_factor_1/3": m3 * sv[0] / sv[2],
    "sqrt_dm21_pdg": 8.608, "m3_if_I_top=phase7_I_t": m3 * math.exp(0.1462 - I7),
    "m3_true_eta_instead_of_b10": m3 * (abs(eta) ** 6 / 4) / (abs(b) ** 2),
}

# 4. PMNS: freedom in which overlap matrix / row / column is read
p6 = phase6_complete_pmns_unitary_and_cp_closure()
from agy_eval import TAU_GOLDEN, l2_of  # noqa: E402
from origin_axiom.operator_gate import quaternionic_4d_yukawa  # noqa: E402
from origin_axiom.sm_19_gate import sector_residues  # noqa: E402
from origin_axiom.twisted_norms import closed_form_cA  # noqa: E402
c_vals = closed_form_cA(TG, "2/5", "0", n_terms=14, dps=20)
h_st, b_st = _f10_st_and_scalar(TG)
r_e = sector_residues(0.4, 0.0, TG, -3, 6, n_pts=64)
l2 = float(np.interp(TG.imag, [2.0, 2.25, 2.5, 2.75, 3.0], [2.4404154646430865, 2.406639297403933, 2.3796454106029277, 2.3577376878276057, 2.3397188997332714]))
u = {k: math.sqrt(2 * math.pi * l2 + float(c_vals[k])) * r_e[k] for k in "1ijk"}
ye = quaternionic_4d_yukawa(-b_st, h_st, u["1"], np.array([u["j"], u["i"], u["k"]]))
U, s, Vh = np.linalg.svd(ye); o = np.argsort(s); U = U[:, o]; V = Vh.conj().T[:, o]
mats = {"V^T U": np.abs(V.T @ U) ** 2, "U^dag V": np.abs(U.conj().T @ V) ** 2}
targets = {"s12": (0.307, 0.013), "s13": (0.0220, 0.0007), "s23": (0.546, 0.021)}
cnt = {k: 0 for k in targets}; total = 0
for nm, M in mats.items():
    for pr in itertools.permutations(range(3)):
        for pc in itertools.permutations(range(3)):
            P = M[np.ix_(pr, pc)]
            s13 = P[0, 2]
            if s13 >= 1:
                continue
            s12 = P[0, 1] / (1 - s13); s23 = P[1, 2] / (1 - s13)
            total += 1
            for k, v in (("s12", s12), ("s13", s13), ("s23", s23)):
                t, e = targets[k]
                if abs(v - t) <= 2 * e:
                    cnt[k] += 1
res["pmns"] = {
    "agy_values": {k: p6[k] for k in ("sin2_theta12_maj_pred", "sin2_theta13_lr_pred", "sin2_theta23_lr_pred", "delta_CP_PMNS_deg_pred")},
    "agy_readout": "theta12 from V^T U row 1; theta13 from U^dag V [2,2]; theta23 from U^dag V column 0; delta quadrant set to 180+arcsin by hand",
    "n_consistent_PDG_readouts_(2 matrices x 36 row/col perms)": total,
    "n_readouts_within_2sigma_per_angle": cnt,
    "matrices": {k: np.round(v, 4).tolist() for k, v in mats.items()},
    "physics_note": "PMNS = U_e^dag U_nu (two LEFT-handed rotations). V_e is the right-handed rotation of the charged lepton; U_nu is never computed.",
}
print(json.dumps(res, indent=1, default=str))
json.dump(res, open("sensitivity_results.json", "w"), indent=1, default=str)
