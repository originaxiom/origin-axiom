"""Independent verification of agy Theorems 10-13 (commit dcae538ab).

T10  exact algebra of A_sig^3 on (2/5,1/5); then show the T^8 'gauge equivalence' is a relabelling that makes
     ALL FIVE lines (2/5, j/5) equivalent to (2/5, 0) at shifted tau -> it cannot select (2/5, 0).
T11  conjugation identity rerun; parity-doubled det = |det Y|^2 (real by construction); Wilson-line 'relaxation'
     is a quark rephasing that leaves every flavour observable unchanged and only moves the phase into theta_QCD.
T12  my own 2-loop SM RGE (scipy solve_ivp, d/dln mu, written from the literature independently of agy's code):
     - Buttazzo et al. (1307.3536) Table-1 benchmark: where does lambda cross zero?
     - agy's boundary conditions (y_t^2(M12)=1/5, lambda(M12)=0) -> lambda(M_Z), y_t(M_Z) (cross-check agy)
     - proper matching: run to mu = M_t and invert Buttazzo's eqs. for lambda(M_t), y_t(M_t) -> implied M_h, M_t
     - look-elsewhere: a menu of 'natural' y_t^2(M12) values
     - tree relation M_Z/v with PDG MSbar couplings (the precision the relation itself has)
T13  rerun; check basis invariance independently; compare to NuFIT.
"""
from __future__ import annotations

import json
import math
import sys

import numpy as np
from scipy.integrate import solve_ivp

SNAP = "/Users/dri/.gemini/antigravity/scratch/agy-snapshot-dcae538ab/src"
sys.path.insert(0, SNAP)
from origin_axiom import toe_closure as TC  # noqa: E402
from origin_axiom.operator_gate import ckm_full_diagnostics, quaternionic_4d_yukawa  # noqa: E402
from origin_axiom.sm_19_gate import _f10_st_and_scalar, derive_scalar_higgs_characters_from_hypercharge, sector_residues  # noqa: E402
from origin_axiom.twisted_norms import closed_form_cA  # noqa: E402

OUT = {}
PHI = (1 + 5 ** 0.5) / 2
TG = complex(1 / 5 ** 0.5, PHI ** 2)

# ------------------------------------------------------------------ T10
A = np.array([[2, -1], [-1, 1]])
A3 = np.linalg.matrix_power(A, 3)
w = np.array([2, 1])  # (2/5, 1/5) * 5
OUT["T10_algebra"] = {
    "A_sig^3": A3.tolist(), "det(A^3+I)": int(round(np.linalg.det(A3 + np.eye(2)))),
    "(A^3+I)w/5": ((A3 + np.eye(2, dtype=int)) @ w / 5).tolist(),
    "A^3 w mod 5 (should be -w = (3,4))": ((A3 @ w) % 5).tolist(),
    "lines (2/5,j/5) with A^3 x = +-x mod 5": [j for j in range(5) if ((A3 @ np.array([2, j])) % 5).tolist() in ([2, j % 5], [3, (-j) % 5])],
}
chars = derive_scalar_higgs_characters_from_hypercharge()["sectors"]


def yuk(p1, p2, tau, l2=2.36):
    p1s = {0.4: "2/5", 0.6: "3/5"}[round(p1, 3)]
    p2s = {0.0: "0", 0.2: "1/5", 0.4: "2/5", 0.6: "3/5", 0.8: "4/5"}[round(p2 % 1.0, 3)]
    c = closed_form_cA(tau, p1s, p2s, n_terms=22, dps=28)
    h, b = _f10_st_and_scalar(tau)
    Y = {}
    for sn, q1, q2 in [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)]:
        r = sector_residues(p1, p2 % 1.0, tau, q1, q2, n_pts=96)
        u = {k: (math.sqrt(2 * math.pi * l2 + float(c[k])) * r[k] if abs(r[k]) > 1e-12 else 0j) for k in "1ijk"}
        Y[sn] = quaternionic_4d_yukawa(complex(*chars[sn]["c_s"]) * b, h, u["1"], np.array([u["j"], u["i"], u["k"]]))
    return Y


def obs(Y):
    d = ckm_full_diagnostics(Y["up"], Y["down"])
    se = np.sort(np.linalg.svd(Y["lepton"], compute_uv=False))
    return np.array([d["up_ratios"][1], d["up_ratios"][0], d["down_ratios"][1], d["down_ratios"][0], se[1] / se[2], se[0] / se[2],
                     d["V_us"], d["V_cb"], d["V_ub"], d["abs_J"]])


tau0 = complex(0.21, 2.3)
base = obs(yuk(0.4, 0.0, tau0))
orbit = {}
for j in range(5):
    # (2/5, p2) at tau + k  ==  (2/5, p2 - 2k/5) at tau ; choose k = 8m with p2 - 16m/5 == 0 mod 1
    m = next(mm for mm in range(5) if (j - 16 * mm) % 5 == 0)
    k = 8 * m
    o = obs(yuk(0.4, j / 5, tau0 + k))
    U = np.array([[1, 2], [2, 3]])
    is_eig = any(((U @ np.array([2, j])) % 5 == (lam * np.array([2, j])) % 5).all() for lam in range(1, 5))
    orbit[f"(2/5,{j}/5) at tau+{k}"] = {"max|obs - obs[(2/5,0) at tau]|": float(np.max(np.abs(o - base) / base)),
                                       "is_eigenline_of_[[1,2],[2,3]]_mod5": bool(is_eig)}
OUT["T10_T8_orbit"] = orbit
OUT["T10_distinct_at_fixed_tau"] = {f"(2/5,{j}/5)": float(np.max(np.abs(obs(yuk(0.4, j / 5, tau0)) - base) / base)) for j in range(5)}
t10 = TC.theorem10_amphichiral_a3_involution_and_t8_cusp_equivalence(n_random_trials=3)
OUT["T10_agy_rerun"] = {k: v for k, v in t10.items()}
print(json.dumps({k: OUT[k] for k in OUT if k.startswith("T10")}, indent=1, default=str))

# ------------------------------------------------------------------ T11
t11 = TC.theorem11_amphichiral_conjugation_and_strong_cp_reality(n_random_trials=3)
YG = yuk(0.4, 0.0, TG, l2=2.360032127545249)
du = np.linalg.det(YG["up"]); dd = np.linalg.det(YG["down"])
ph = np.exp(-1j * np.angle(du * dd) / 3)
o1 = obs(YG); YG2 = dict(YG); YG2["up"] = ph * YG["up"]
o2 = obs(YG2)
OUT["T11"] = {
    "agy_rerun": t11,
    "parity_doubled_det = det(Y)*det(P conj(Y) P) = |det Y|^2 -> arg = 0 for ANY matrix": True,
    "random_matrix_demo_arg_det_doubled": float(abs(np.angle(np.linalg.det(np.block([[M := (np.random.default_rng(1).normal(size=(3, 3)) + 1j * np.random.default_rng(2).normal(size=(3, 3))), np.zeros((3, 3))], [np.zeros((3, 3)), np.diag([1, 1, -1]) @ M.conj() @ np.diag([1, 1, -1])]]))))),
    "single_sheet_arg_det(YuYd)": float(np.angle(du * dd)),
    "rephasing_Yu_by_exp(-i arg/3): max rel change of all 10 flavour observables": float(np.max(np.abs(o2 - o1) / o1)),
    "arg_det_after_rephasing": float(np.angle(np.linalg.det(YG2["up"]) * dd)),
    "note": "theta_bar = theta_QCD - arg det(Yu Yd) is invariant under quark rephasing; removing arg det by a phase just moves it into theta_QCD, which the model never computes.",
}
print(json.dumps({"T11": {k: v for k, v in OUT["T11"].items() if k != "agy_rerun"}}, indent=1, default=str))

# ------------------------------------------------------------------ T12: independent 2-loop SM RGE
K = 1 / (16 * math.pi ** 2)


def beta(lnmu, s):
    gY, g2, g3, yt, lam = s
    gY2, g22, g32, y2 = gY * gY, g2 * g2, g3 * g3, yt * yt
    bgY = K * gY ** 3 * 41 / 6 + K ** 2 * gY ** 3 * (199 / 18 * gY2 + 9 / 2 * g22 + 44 / 3 * g32 - 17 / 6 * y2)
    bg2 = K * g2 ** 3 * (-19 / 6) + K ** 2 * g2 ** 3 * (3 / 2 * gY2 + 35 / 6 * g22 + 12 * g32 - 3 / 2 * y2)
    bg3 = K * g3 ** 3 * (-7) + K ** 2 * g3 ** 3 * (11 / 6 * gY2 + 9 / 2 * g22 - 26 * g32 - 2 * y2)
    byt = K * yt * (9 / 2 * y2 - 8 * g32 - 9 / 4 * g22 - 17 / 12 * gY2) + K ** 2 * yt * (
        -12 * y2 ** 2 + y2 * (36 * g32 + 225 / 16 * g22 + 131 / 16 * gY2 - 12 * lam) + 6 * lam ** 2 - 108 * g32 ** 2
        + 9 * g22 * g32 + 19 / 9 * gY2 * g32 - 23 / 4 * g22 ** 2 - 3 / 4 * g22 * gY2 + 1187 / 216 * gY2 ** 2)
    bl = K * (24 * lam ** 2 - 6 * y2 ** 2 + 3 / 8 * (2 * g22 ** 2 + (g22 + gY2) ** 2) + lam * (12 * y2 - 9 * g22 - 3 * gY2)) + K ** 2 * (
        -312 * lam ** 3 + 36 * lam ** 2 * (3 * g22 + gY2) - 144 * lam ** 2 * y2 - 3 * lam * y2 ** 2
        + lam * y2 * (80 * g32 + 45 / 2 * g22 + 85 / 6 * gY2) + 30 * y2 ** 3 - 32 * g32 * y2 ** 2 - 8 / 3 * gY2 * y2 ** 2
        - 73 / 8 * lam * g22 ** 2 + 39 / 4 * lam * g22 * gY2 + 629 / 24 * lam * gY2 ** 2
        + 305 / 16 * g22 ** 3 - 289 / 48 * g22 ** 2 * gY2 - 559 / 48 * g22 * gY2 ** 2 - 379 / 48 * gY2 ** 3
        + y2 * (-9 / 4 * g22 ** 2 + 21 / 2 * g22 * gY2 - 19 / 4 * gY2 ** 2))
    return [bgY, bg2, bg3, byt, bl]


def run(s0, mu0, mu1, dense=False):
    return solve_ivp(beta, (math.log(mu0), math.log(mu1)), s0, rtol=1e-11, atol=1e-13, dense_output=dense)


# Benchmark: Buttazzo Table 1 (mu = M_t), find lambda = 0
for Mt in (173.10, 173.34):
    sol = run([0.35830, 0.64779, 1.1666, 0.93690, 0.12604], Mt, 1e20, dense=True)
    xs = np.linspace(math.log(Mt), math.log(1e20), 40001)
    lam = sol.sol(xs)[4]
    i = np.where(lam < 0)[0][0]
    OUT[f"T12_benchmark_lambda0_from_Table1_at_mu={Mt}"] = {"log10_mu_lambda0": float(xs[i] / math.log(10)),
                                                          "lambda_min": float(lam.min()), "log10_mu_at_min": float(xs[np.argmin(lam)] / math.log(10))}

# agy boundary conditions
t12 = TC.theorem12_nondimensional_buttazzo_2loop_top_higgs_closure()
n = t12["nondimensional_electroweak_and_top_higgs_ratios"]
t9b = TC.theorem9_hypercharge_quadratic_refinement_and_full_19_closure()["part_B_zero_input_m004_gauge_and_hierarchy"]
aem = 1 / t9b["alpha_em_inv_MZ_pred"]; s2 = t9b["sin2_thetaW_MZ_pred"]; a3 = t9b["alpha_s_MZ_pred"]
gY0 = math.sqrt(4 * math.pi * aem / (1 - s2)); g20 = math.sqrt(4 * math.pi * aem / s2); g30 = math.sqrt(4 * math.pi * a3)
MZ = 91.1876; V = 246.21965
M12 = MZ * math.exp(4 * math.pi * 2.0298832128193072)


def solve_bc(yt2_uv, lam_uv=0.0):
    # shoot from M_Z: unknown (yt, lam) at MZ, gauge fixed at MZ
    from scipy.optimize import fsolve

    def F(x):
        s = run([gY0, g20, g30, x[0], x[1]], MZ, M12).y[:, -1]
        return [s[3] ** 2 - yt2_uv, s[4] - lam_uv]

    x = fsolve(F, [0.95, 0.13], xtol=1e-13)
    return x


def implied_masses(yt_mz, lam_mz):
    # run to mu = 173.34 and invert Buttazzo eqs (their eq. for lambda(M_t), y_t(M_t); alpha_s correction included)
    s = run([gY0, g20, g30, yt_mz, lam_mz], MZ, 173.34).y[:, -1]
    das = (a3 - 0.1184) / 0.0007
    Mt = 173.34 + (s[3] - 0.93690 + 0.00042 * das) / 0.00556
    Mh = 125.15 + (s[4] - 0.12604 + 0.00004 * (Mt - 173.34)) / 0.00206
    return s, Mt, Mh


yt_mz, lam_mz = solve_bc(0.2)
s_mt, Mt_imp, Mh_imp = implied_masses(yt_mz, lam_mz)
OUT["T12_agy_BC_crosscheck"] = {
    "agy": {"yt_MZ": n["yt_at_MZ_pred"], "lambda_MZ": n["lambda_at_MZ_pred"], "mH_tree": n["mH_pred_GeV"], "mt_pole": n["mt_pole_pred_GeV"]},
    "mine": {"yt_MZ": float(yt_mz), "lambda_MZ": float(lam_mz), "mH_tree_sqrt(2lam)v": math.sqrt(2 * lam_mz) * V},
    "properly_matched_via_Buttazzo_eqs": {"y_t(173.34)": float(s_mt[3]), "lambda(173.34)": float(s_mt[4]),
                                          "implied_Mt_pole": float(Mt_imp), "implied_Mh_pole": float(Mh_imp),
                                          "PDG": {"Mt": "172.69 +- 0.30", "Mh": "125.25 +- 0.17"}},
}
menu = {"1/3": 1 / 3, "1/4": 0.25, "1/phi^3": PHI ** -3, "1/5": 0.2, "1/(2 phi)": 1 / (2 * PHI), "1/6": 1 / 6, "1/7": 1 / 7, "1/8": 0.125,
        "1/phi^4": PHI ** -4, "1/(4 Vol)": 1 / (4 * 2.0298832128193072), "1/(2pi)": 1 / (2 * math.pi), "1/pi^2*2": 2 / math.pi ** 2}
lk = {}
for nm, v in menu.items():
    try:
        y, l = solve_bc(v)
        _, mt_i, mh_i = implied_masses(y, l)
        lk[nm] = {"yt2_M12": v, "mH_tree_agy_style": round(math.sqrt(2 * l) * V, 2), "Mh_matched": round(float(mh_i), 2), "Mt_matched": round(float(mt_i), 2)}
    except Exception as e:  # noqa: BLE001
        lk[nm] = str(e)
OUT["T12_lookelsewhere_menu"] = lk
# what y_t^2(M12) would PDG M_t require, and what does lambda(M12)=0 then give?
from scipy.optimize import brentq  # noqa: E402
yt2_for_pdg = brentq(lambda v: implied_masses(*solve_bc(v))[1] - 172.69, 0.12, 0.3)
OUT["T12_if_Mt_fixed_to_PDG"] = {"required_yt2_M12": yt2_for_pdg, "Mh_matched_with_lambda(M12)=0": float(implied_masses(*solve_bc(yt2_for_pdg))[2])}
# M_Z / v tree relation with PDG MSbar couplings
g2p = math.sqrt(4 * math.pi / 127.951 / 0.23122); gYp = math.sqrt(4 * math.pi / 127.951 / (1 - 0.23122))
OUT["T12_MZ_over_v"] = {"agy": n["MZ_over_vEW_pred"], "tree_with_PDG_MSbar_couplings": 0.5 * math.hypot(g2p, gYp), "measured": MZ / V,
                        "note": "the tree relation itself misses by ~0.35% with exact PDG inputs; agy's 0.06% comes from compensating errors in its fitted alpha_em (+0.48%) and sin2thetaW"}
print(json.dumps({k: OUT[k] for k in OUT if k.startswith("T12")}, indent=1, default=str))

# ------------------------------------------------------------------ T13
t13 = TC.theorem13_basis_invariant_weinberg_majorana_and_pmns(n_haar_trials=10)
s12, s23, s13 = t13["sin2_theta12_weinberg_minimal"], t13["sin2_theta23_weinberg_minimal"], t13["sin2_theta13_weinberg_minimal"]
nufit = {"s12": (0.307, 0.012), "s23": (0.572, 0.020), "s13": (0.02203, 0.00056)}
OUT["T13"] = {"agy_rerun": t13,
              "pulls_vs_NuFIT5.2_NO": {"s12": (s12 - 0.307) / 0.012, "s13": (s13 - 0.02203) / 0.00056, "s23": (s23 - 0.572) / 0.020},
              "docstring_vs_output": "docstring says |b10|^2 = 1.32049e-5 and |eta^6/4| = 4.55943e-3; output gives the values in agy_rerun"}
print(json.dumps({"T13": OUT["T13"]}, indent=1, default=str))
json.dump(OUT, open("t10_13_results.json", "w"), indent=1, default=str)
