#!/usr/bin/env python3
"""
B1763 verification script: Matter Kähler metric and residual flavour pulls.

Investigates chiral matter field modular weights (k_10, k_5bar) in the Kähler metric:
  K_i = (2 Im tau)^{-k_i} |Phi_i|^2
under level N = 6 modular symmetry.

Evaluates the canonical kinetic normalization:
  Y_u -> (2 Im tau)^{(k_{10,i} + k_{10,j} - k_Hu)/2} Y_u^{ij}
  Y_d -> (2 Im tau)^{(k_{10,i} + k_{5bar,j} - k_Hd)/2} Y_d^{ij}
  Y_e -> (2 Im tau)^{(k_{5bar,i} + k_{10,j} - k_Hd)/2} Y_e^{ij}

Demonstrates that an exact N=6 arithmetic progression in 5bar:
  Delta k_{5bar} = (-1/3, -1/6, 0) = -1/6 * (2, 1, 0), with Delta k_10 = (0, 0, 0)
reduces the total 10-observable chi^2 at M_GUT from 32.27 down to 23.42,
relieving CKM and Jarlskog pulls without introducing continuous parameters.
"""

import sys
import math
import json
import pathlib
from fractions import Fraction as Fr
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier" / "B1743_the_principled_pencils_and_the_nines_target" / "verification"))
sys.path.insert(0, str(ROOT / "frontier" / "B1757_step_twos_free_doublets_at_the_strip" / "verification"))

import pencils as P
import free_doublets as FD

OBSERVABLE_NAMES = [
    "log(m_e/m_mu)",
    "log(m_mu/m_tau)",
    "log(m_d/m_s)",
    "log(m_s/m_b)",
    "log(m_u/m_c)",
    "log(m_c/m_t)",
    "log|V_us|",
    "log|V_cb|",
    "log|V_ub|",
    "|J_CP|"
]

J_PDG = 3.08e-5
J_SIG = 0.15e-5

def gauge_h1(v: np.ndarray) -> np.ndarray:
    v = np.asarray(v, dtype=complex)
    v = v / np.linalg.norm(v)
    return v * np.exp(-1j * np.angle(v[1]))

def mat_pow_herm(H: np.ndarray, p: float) -> np.ndarray:
    evals, evecs = np.linalg.eigh(H)
    return (evecs * (evals ** p)) @ evecs.conj().T

def evaluate_point(re_t: float, im_t: float, B, M_fd: dict, dk10: list, dk5: list) -> dict:
    tau = complex(re_t, im_t)
    two_im_tau = 2.0 * im_t

    F = P.forms(tau)
    dr = gauge_h1(F["DR"])
    dr_conj = gauge_h1(np.conj(F["DR"]))
    v_012 = np.array([0.0 + 0.0j, dr_conj[1], dr_conj[2]])

    Sigmas = {}
    for sec in ("up", "down", "lep"):
        bY = []
        for c_idx in range(3):
            e_c = np.zeros(3, dtype=complex)
            e_c[c_idx] = 1.0
            bY.append(B.coupling(P.R.Smat(list(e_c), B), M_fd[(sec, "L_max")]))
        S = np.zeros((3, 3), dtype=complex)
        for c_idx in range(3):
            for d_idx in range(3):
                S[c_idx, d_idx] = np.trace(bY[c_idx].conj().T @ bY[d_idx])
        Sigmas[sec] = S / np.trace(S).real

    S_u = Sigmas["up"]
    S_d = Sigmas["down"]
    delta_u = 0.5 * float(np.real(S_u[0, 0]))
    p_nat = 1.0 + delta_u

    hd_p = gauge_h1(mat_pow_herm(np.conj(S_d), -p_nat) @ v_012)
    lam_12_u = float(np.real(np.vdot(v_012, S_u @ v_012)))
    lam_0_u = float(np.real(S_u[0, 0]))
    boost_u = lam_12_u / lam_0_u
    e1_schur_conj = np.conj(-(S_d[0, 1] * dr[1] + S_d[0, 2] * dr[2]) / S_d[0, 0])
    z_L3 = complex(boost_u * (-dr[0].real), abs(e1_schur_conj))
    hu_L3 = gauge_h1(np.array([z_L3, dr_conj[1], dr_conj[2]]))

    Su, Sd = P.R.Smat(list(hu_L3), B), P.R.Smat(list(hd_p), B)
    Yu_raw = B.coupling(Su, M_fd[("up", "L_max")])
    Yd_raw = B.coupling(Sd, M_fd[("down", "L_max")])
    Ye_raw = B.coupling(Sd, M_fd[("lep", "L_max")])

    D10 = np.diag([two_im_tau ** (k / 2.0) for k in dk10])
    D5 = np.diag([two_im_tau ** (k / 2.0) for k in dk5])

    Yu = D10 @ Yu_raw @ D10
    Yd = D10 @ Yd_raw @ D5
    Ye = D5 @ Ye_raw @ D10

    Y = {"up": Yu, "down": Yd, "lep": Ye}
    six = []
    for s in ("up", "down", "lep"):
        sv = np.maximum(np.linalg.svd(Y[s], compute_uv=False), 1e-300)
        six += [math.log(sv[1] / sv[0]), math.log(sv[2] / sv[0])]
    six = np.array(six) + np.array([0, 0, 0, 0, P.LC, -P.LC])
    Uu = np.linalg.svd(Y["up"])[0][:, ::-1]
    Ud = np.linalg.svd(Y["down"])[0][:, ::-1]
    V = np.conj(Uu.T) @ Ud
    ck = np.log(np.maximum([abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2])], 1e-300))

    T9_GUT = P.T9.copy()
    T9_GUT[4] += math.log(2.84 / 3.14) * 0.5
    T9_GUT[2] -= math.log(2.84 / 3.14) * 0.5
    T9_GUT[5] += math.log(0.269 / 0.297) * 0.5
    T9_GUT[3] -= math.log(0.269 / 0.297) * 0.5

    pulls_mz = (np.concatenate([six, ck]) - P.T9) / P.S9
    pulls_gut = (np.concatenate([six, ck]) - T9_GUT) / P.S9

    c6_mz = float((pulls_mz[:6] ** 2).sum())
    c_ckm_mz = float((pulls_mz[6:] ** 2).sum())
    c9_mz = float((pulls_mz ** 2).sum())

    c6_gut = float((pulls_gut[:6] ** 2).sum())
    c_ckm_gut = float((pulls_gut[6:] ** 2).sum())
    c9_gut = float((pulls_gut ** 2).sum())

    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    pull_J = (abs(J) - J_PDG) / J_SIG
    c10_gut = c9_gut + float(pull_J ** 2)
    c10_mz = c9_mz + float(pull_J ** 2)

    return {
        "tau": [float(re_t), float(im_t)],
        "two_im_tau": two_im_tau,
        "dk10": dk10,
        "dk5": dk5,
        "chi2_6_mz": c6_mz,
        "chi2_ckm_mz": c_ckm_mz,
        "chi2_9_mz": c9_mz,
        "chi2_10_mz": c10_mz,
        "chi2_6_gut": c6_gut,
        "chi2_ckm_gut": c_ckm_gut,
        "chi2_9_gut": c9_gut,
        "chi2_10_gut": c10_gut,
        "Jarlskog": abs(J),
        "pull_J": pull_J,
        "pulls_gut_9": pulls_gut.tolist(),
        "pulls_mz_9": pulls_mz.tolist(),
        "CKM_magnitudes": [[float(abs(V[i, j])) for j in range(3)] for i in range(3)],
    }

def main() -> None:
    print("=" * 78)
    print("B1763: MATTER KÄHLER METRIC AND RESIDUAL FLAVOUR PULLS")
    print("=" * 78)

    B = P.R.CEN._modules()["B"]
    fd_list = json.loads((ROOT / "frontier" / "B1757_step_twos_free_doublets_at_the_strip" / "verification" / "free_doublets.json").read_text())
    a0, b0 = Fr(2, 5), Fr(1, 10)

    results = {}
    weight_schemes = [
        ("flat", [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]),
        ("step_minus_one_sixth", [0.0, 0.0, 0.0], [-1.0/3.0, -1.0/6.0, 0.0]),
        ("step_minus_one_fourth", [0.0, 0.0, 0.0], [-1.0/2.0, -1.0/4.0, 0.0]),
    ]

    for rec in fd_list:
        if rec["hor"] != "L_max":
            continue
        re_t, im_t = rec["tau"]
        point_key = f"tau_{re_t:.4f}_{im_t:.4f}"
        M_fd = P.SC.channels(re_t, im_t, a0, b0)

        results[point_key] = {}
        print(f"\n--- Strip Apex: tau = {re_t:.4f} + {im_t:.4f}i (2 Im tau = {2*im_t:.4f}) ---")
        for name, dk10, dk5 in weight_schemes:
            res = evaluate_point(re_t, im_t, B, M_fd, dk10, dk5)
            results[point_key][name] = res
            print(f"  {name:25s} | chi2_10(GUT) = {res['chi2_10_gut']:5.2f} (9={res['chi2_9_gut']:5.2f}, J={res['pull_J']:+.2f}s) | chi2_10(MZ) = {res['chi2_10_mz']:5.2f}")
            if name == "step_minus_one_sixth":
                pg = res["pulls_gut_9"]
                print(f"    GUT pulls: me/mmu={pg[0]:+.2f}, mmu/mtau={pg[1]:+.2f}, md/ms={pg[2]:+.2f}, ms/mb={pg[3]:+.2f}, mu/mc={pg[4]:+.2f}, mc/mt={pg[5]:+.2f}")
                print(f"               Vus={pg[6]:+.2f}, Vcb={pg[7]:+.2f}, Vub={pg[8]:+.2f}, J={res['pull_J']:+.2f}")

    # Save results
    out_dir = ROOT / "frontier" / "B1763_matter_kahler_metric_and_residual_flavour_pulls" / "verification"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_json = out_dir / "matter_kahler_metric.json"
    out_json.write_text(json.dumps(results, indent=2))
    print(f"\nSaved structured results to {out_json}")

if __name__ == "__main__":
    main()
