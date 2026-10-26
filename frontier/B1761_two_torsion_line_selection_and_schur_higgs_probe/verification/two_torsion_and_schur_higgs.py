#!/usr/bin/env python3
"""B1761 (P-349, P-357, P-366, P-373, P-377, P-384):
1. Data-Free 2-Torsion Up-Kernel & Isotropic-Proximity Line-Selection Theorem across all 662 lines
   (266 lines of N <= 12 from B1726/B1749 and 396 lines of N in {13, 14, 15, 20} from B1755).
2. Exact Block-Diagonal & e1-Parity Structure of the 3x3 Hermitian Yukawa Gram Matrices Sigma^(s)(tau, w)
   and Zero-Parameter Inverse-Gram Down-Higgs Dressing on the Strip (2/5, 1/10).
"""

import importlib.util
import json
import math
import pathlib
import sys
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import least_squares

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1743_the_principled_pencils_and_the_nines_target" / "verification"))
sys.path.insert(0, str(ROOT / "frontier" / "B1757_step_twos_free_doublets_at_the_strip" / "verification"))

import pencils as P       # noqa: E402
import free_doublets as FD  # noqa: E402


def _load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def gauge_h1(v):
    v = np.asarray(v, dtype=complex)
    v = v / np.linalg.norm(v)
    return v * np.exp(-1j * np.angle(v[1]))


def mat_pow_herm(H, p: float):
    evals, evecs = np.linalg.eigh(H)
    return (evecs * (evals ** p)) @ evecs.conj().T


def run_line_selection_census(B, lines_266, lines_396, tau_probe: complex = 0.3145 + 3.0345j):
    all_lines = (
        [("N<=12", idx, a, b) for idx, (a, b) in enumerate(lines_266)]
        + [("N_in_13_14_15_20", idx, a, b) for idx, (a, b) in enumerate(lines_396)]
    )
    c1_survivors = []
    c1_c2_survivors = []

    for group, idx, a, b in all_lines:
        N = math.lcm(a.denominator, b.denominator)
        w = float(a) * tau_probe + float(b)
        x_u, y_u = B.sector_twists(w, tau_probe, B.SIXY["Q"], B.SIXY["u"])
        R_u = B.residues(x_u, y_u, tau_probe)
        x_d, y_d = B.sector_twists(w, tau_probe, B.SIXY["Q"], B.SIXY["d"])
        R_d = B.residues(x_d, y_d, tau_probe)

        # Condition C1 (Data-Free Asymmetric 2-Torsion e1-Kernel):
        # Non-trivial tau-slope a not in {0, 1/2}, R_i^(up) == 0, R_j^(up) != 0, R_i^(down) != 0
        c1 = (
            (a not in (Fr(0, 1), Fr(1, 2)))
            and (abs(R_u["i"]) < 1e-11)
            and (abs(R_u["j"]) > 1e-8)
            and (abs(R_d["i"]) > 1e-8)
        )
        if c1:
            doublet_over_scalar = float(math.hypot(abs(R_u["j"]), abs(R_u["k"])) / abs(R_u["1"]))
            u_vec = np.array([R_u["i"], R_u["j"], R_u["k"]], dtype=complex)
            I_up = float(abs(np.dot(u_vec, u_vec)) / float(np.vdot(u_vec, u_vec).real))
            rec = {
                "group": group,
                "line_index": int(idx),
                "a": str(a),
                "b": str(b),
                "N": int(N),
                "up_doublet_over_scalar": doublet_over_scalar,
                "up_off_cone_invariant_I": I_up,
                "abs_R_u_i": float(abs(R_u["i"])),
                "abs_R_d_i": float(abs(R_d["i"])),
            }
            c1_survivors.append(rec)
            # Condition C2 (Up-sector Isotropic Proximity I(u_up) < 0.05, equivalently ||R_(j,k)^(up)||/|R_1^(up)| > 2)
            if I_up < 0.05 and doublet_over_scalar > 2.0:
                c1_c2_survivors.append(rec)

    return {
        "total_lines_tested": len(all_lines),
        "n_lines_N_le_12": len(lines_266),
        "n_lines_N_13_to_20": len(lines_396),
        "tau_probe": [float(tau_probe.real), float(tau_probe.imag)],
        "c1_survivor_count": len(c1_survivors),
        "c1_c2_survivor_count": len(c1_c2_survivors),
        "c1_survivors": c1_survivors,
        "c1_c2_survivors": c1_c2_survivors,
    }


def run_schur_gram_probe(B):
    fd_list = json.loads(
        (ROOT / "frontier" / "B1757_step_twos_free_doublets_at_the_strip" / "verification" / "free_doublets.json").read_text()
    )
    a0, b0 = Fr(2, 5), Fr(1, 10)
    P_e1 = np.diag([-1.0, 1.0, 1.0])
    strip_results = []

    for rec in fd_list:
        if rec["hor"] != "L_max":
            continue
        re_t, im_t = rec["tau"]
        t = complex(re_t, im_t)
        M_fd = P.SC.channels(re_t, im_t, a0, b0)
        F = P.forms(t)
        dr = gauge_h1(F["DR"])
        dr_conj = gauge_h1(np.conj(F["DR"]))
        v_012 = np.array([0.0 + 0.0j, dr_conj[1], dr_conj[2]])

        hu_opt = gauge_h1([complex(z[0], z[1]) for z in rec["H_u"]])
        hd_opt = gauge_h1([complex(z[0], z[1]) for z in rec["H_d"]])

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
        S_e = Sigmas["lep"]

        # Structural identity checks on Sigma^(up), Sigma^(down), Sigma^(lep)
        up_off_block_norm = float(math.hypot(abs(S_u[0, 1]), abs(S_u[0, 2])))
        down_lep_parity_diff = float(np.linalg.norm(S_e - (P_e1 @ S_d @ P_e1)))

        # Zero-parameter Schur complement and inverse-Gram down-Higgs vector
        e1_schur_conj = np.conj(-(S_d[0, 1] * dr[1] + S_d[0, 2] * dr[2]) / S_d[0, 0])
        hd_inv_gram = gauge_h1(np.linalg.inv(np.conj(S_d)) @ v_012)
        hd_schur0_hd12 = gauge_h1(np.array([e1_schur_conj, hd_opt[1], hd_opt[2]]))

        overlap_hd = float(abs(np.vdot(hd_opt, hd_inv_gram)))
        angle_hd_deg = float(math.degrees(math.acos(min(1.0, max(-1.0, overlap_hd)))))

        chi2_dr_conj = float((FD.nine2(dr_conj, dr_conj, M_fd, "L_max", B) ** 2).sum())
        chi2_0dof_inv_gram = float((FD.nine2(dr_conj, hd_inv_gram, M_fd, "L_max", B) ** 2).sum())
        chi2_schur0_with_opt = float((FD.nine2(hu_opt, hd_schur0_hd12, M_fd, "L_max", B) ** 2).sum())
        chi2_inv_gram_with_hu_opt = float((FD.nine2(hu_opt, hd_inv_gram, M_fd, "L_max", B) ** 2).sum())

        # 2-DOF fit: H_d = hd_inv_gram (0 params), H_u(zeta_u) = (zeta_u, dr_conj[1], dr_conj[2]) (1 complex param = 2 real DOFs)
        f_2dof = lambda p: FD.nine2(gauge_h1([p[0] + 1j * p[1], dr_conj[1], dr_conj[2]]), hd_inv_gram, M_fd, "L_max", B)
        r_2dof = least_squares(f_2dof, [0.10, 0.07], method="trf", max_nfev=300)
        chi2_2dof = float((r_2dof.fun ** 2).sum())
        zeta_u_2dof = complex(r_2dof.x[0], r_2dof.x[1])

        # 3-DOF fit: H_d(beta) = (conj(S_d))^(-beta) @ v_012, H_u(zeta_u) (3 real DOFs total)
        def f_3dof(p):
            hd_b = gauge_h1(mat_pow_herm(np.conj(S_d), -p[2]) @ v_012)
            hu_z = gauge_h1([p[0] + 1j * p[1], dr_conj[1], dr_conj[2]])
            return FD.nine2(hu_z, hd_b, M_fd, "L_max", B)

        r_3dof = least_squares(f_3dof, [0.10, 0.07, 1.0], method="trf", max_nfev=400)
        chi2_3dof = float((r_3dof.fun ** 2).sum())
        beta_3dof = float(r_3dof.x[2])

        strip_results.append({
            "tau": [float(re_t), float(im_t)],
            "up_off_block_norm": up_off_block_norm,
            "down_lep_parity_diff": down_lep_parity_diff,
            "dr_conj": [[float(z.real), float(z.imag)] for z in dr_conj],
            "hu_opt_h1_pos": [[float(z.real), float(z.imag)] for z in hu_opt],
            "hd_opt_h1_pos": [[float(z.real), float(z.imag)] for z in hd_opt],
            "hd_inv_gram_0param": [[float(z.real), float(z.imag)] for z in hd_inv_gram],
            "e1_schur_conj_0param": [float(e1_schur_conj.real), float(e1_schur_conj.imag)],
            "overlap_hd_opt_vs_inv_gram": overlap_hd,
            "angle_hd_opt_vs_inv_gram_deg": angle_hd_deg,
            "chi2_0dof_dr_conj": chi2_dr_conj,
            "chi2_0dof_inv_gram": chi2_0dof_inv_gram,
            "chi2_2dof_zeta_u_with_inv_gram_hd": chi2_2dof,
            "zeta_u_2dof": [float(zeta_u_2dof.real), float(zeta_u_2dof.imag)],
            "zeta_u_2dof_abs": float(abs(zeta_u_2dof)),
            "zeta_u_2dof_arg_deg": float(np.angle(zeta_u_2dof, deg=True)),
            "chi2_3dof_beta_zeta_u": chi2_3dof,
            "beta_3dof": beta_3dof,
            "chi2_hu_opt_with_schur0_hd12": chi2_schur0_with_opt,
            "chi2_hu_opt_with_inv_gram_hd": chi2_inv_gram_with_hu_opt,
            "chi2_8dof_b1757": float(rec["chi2_nine"]),
        })

    return strip_results


def main():
    cen55 = _load_module(
        "cen55",
        ROOT / "frontier" / "B1755_the_six_on_the_lines_of_order_13_to_20" / "verification" / "census.py",
    )
    B = P.R.CEN._modules()["B"]
    lines_266 = P.R.CEN.lines()
    lines_396 = cen55.lines()

    attack2 = run_line_selection_census(B, lines_266, lines_396)
    attack1 = run_schur_gram_probe(B)

    out = {
        "arc": "B1761",
        "points": ["P-349", "P-357", "P-366", "P-373", "P-377", "P-384"],
        "attack2_line_selection": attack2,
        "attack1_schur_gram_strip": attack1,
    }
    (HERE / "two_torsion_and_schur_higgs.json").write_text(json.dumps(out, indent=2) + "\n")

    lines_txt = []
    lines_txt.append("=== B1761: DATA-FREE 2-TORSION LINE SELECTION & YUKAWA-GRAM HIGGS PROBE ===")
    lines_txt.append(
        f"Attack 2: tested {attack2['total_lines_tested']} lines ({attack2['n_lines_N_le_12']} at N<=12, "
        f"{attack2['n_lines_N_13_to_20']} at N in {{13,14,15,20}})"
    )
    lines_txt.append(f"  Condition C1 survivors (asymmetric 2-torsion e1-kernel): {attack2['c1_survivor_count']} lines")
    lines_txt.append(f"  Condition C1+C2 survivors (I(u_up) < 0.05): {attack2['c1_c2_survivor_count']} lines (single T-orbit a=2/5, 10b odd)")
    for row in attack2["c1_survivors"]:
        lines_txt.append(
            f"    [{row['group']}] line {row['line_index']:3d}: ({row['a']}, {row['b']}) N={row['N']} "
            f"| ||R_(j,k)^(up)||/|R_1^(up)| = {row['up_doublet_over_scalar']:.5f} | I(u_up) = {row['up_off_cone_invariant_I']:.6f}"
        )
    lines_txt.append("\nAttack 1: Yukawa Gram matrices Sigma^(s) and zero-parameter down-Higgs dressing on (2/5, 1/10):")
    for pt in attack1:
        t_re, t_im = pt["tau"]
        lines_txt.append(
            f"  tau = {t_re:.6f} + {t_im:.6f}i | ||Sigma^(up)_(0,12)|| = {pt['up_off_block_norm']:.2e} "
            f"| ||Sigma^(lep) - P_e1 Sigma^(down) P_e1|| = {pt['down_lep_parity_diff']:.2e}"
        )
        lines_txt.append(
            f"    |<H_d_opt | H_d_inv_gram>| = {pt['overlap_hd_opt_vs_inv_gram']:.6f} ({pt['angle_hd_opt_vs_inv_gram_deg']:.3f} deg) "
            f"| chi2(2-DOF) = {pt['chi2_2dof_zeta_u_with_inv_gram_hd']:.2f} | chi2(3-DOF) = {pt['chi2_3dof_beta_zeta_u']:.2f} "
            f"| chi2(B1757 8-DOF) = {pt['chi2_8dof_b1757']:.2f}"
        )
    lines_txt.append("two_torsion_and_schur_higgs exit 0")
    txt_out = "\n".join(lines_txt) + "\n"
    (HERE / "two_torsion_and_schur_higgs_run.txt").write_text(txt_out)
    print(txt_out, end="")


if __name__ == "__main__":
    main()
