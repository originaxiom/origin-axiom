#!/usr/bin/env python3
"""B1759: Sector-Universal Puncture Norm Theorem and Data-Free Off-Cone Higgs Dressing Probe.

1. Certifies Theorem 1 (Sector-Universal Puncture Norm Theorem, P-357 Step 2):
   For every Standard Model sector (q_L, q_R) in {up, down, lep}, the normalized
   elliptic channel kernel K_s(u; x, y) = P_s(u; x, y) / R_s(x, y) depends only
   on the sum twist x + y = (q_L + q_R) w = +/- 3 w. Since |K_s(-u; -3w)| = |K_s(u; 3w)|,
   the finite puncture norm constant c_s(tau, w) satisfies the exact identity
       c_s^(up)(tau, w) = c_s^(down)(tau, w) = c_s^(lep)(tau, w)
   at every (tau, w) and for every channel s in {1, i, j, k} with R_s != 0.

2. Compares the boundary-dressed Dedekind-period directions and raw sector-twist
   matter vectors against the committed B1757 free-doublet vectors on the strip.
"""

from __future__ import annotations
from fractions import Fraction as Fr
import json
import math
import pathlib
import sys
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(
    0,
    str(
        ROOT
        / "frontier"
        / "B1743_the_principled_pencils_and_the_nines_target"
        / "verification"
    ),
)
sys.path.insert(
    0,
    str(
        ROOT
        / "frontier"
        / "B1757_step_twos_free_doublets_at_the_strip"
        / "verification"
    ),
)

import pencils as P  # noqa: E402
import free_doublets as FD  # noqa: E402

B = P.R.CEN._modules()["B"]
col = P.R.CEN._modules()["col"]


def align_h2_positive(v: np.ndarray) -> np.ndarray:
    v = np.asarray(v, dtype=complex)
    v = v / np.linalg.norm(v)
    if abs(v[1]) > 1e-15:
        v = v * np.exp(-1j * np.angle(v[1]))
    return v


def main() -> None:
    a, b = Fr(2, 5), Fr(1, 10)
    points = FD.POINTS
    b1757_rows = json.loads(
        (
            ROOT
            / "frontier"
            / "B1757_step_twos_free_doublets_at_the_strip"
            / "verification"
            / "free_doublets.json"
        ).read_text()
    )

    u_grid = np.array(
        [
            0.07 + 0.03j,
            -0.11 + 0.08j,
            0.14 - 0.05j,
            0.23 + 0.41j,
            -0.31 - 0.19j,
        ],
        dtype=complex,
    )

    theorem1_checks = []
    strip_comparisons = []

    print("=== 1. SECTOR-UNIVERSAL PUNCTURE NORM THEOREM (THEOREM 1) ===")
    for _, re_t, im_t in points:
        t = complex(re_t, im_t)
        w = float(a) * t + float(b)
        c_sec = {}
        K_sec = {}
        R_sec = {}
        for sec, (lf, rf) in P.R.SECT.items():
            x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf])
            Rr = B.residues(x, yy, t)
            R_sec[sec] = Rr
            c_sec[sec] = B.cA(x, yy, t, Rr)
            Pr = B.pairs(x, yy, u_grid, t)
            K_sec[sec] = {
                s: (Pr[s] / Rr[s] if abs(Rr[s]) > 1e-12 else None)
                for s in ("1", "i", "j", "k")
            }

        Pr_down_neg = B.pairs(
            *B.sector_twists(w, t, B.SIXY["Q"], B.SIXY["d"]), -u_grid, t
        )
        Rr_down = R_sec["down"]
        K_down_neg = {s: Pr_down_neg[s] / Rr_down[s] for s in ("1", "i", "j", "k")}

        max_dc_j = max(
            abs(c_sec["up"]["j"] - c_sec["down"]["j"]),
            abs(c_sec["down"]["j"] - c_sec["lep"]["j"]),
        )
        max_dc_k = max(
            abs(c_sec["up"]["k"] - c_sec["down"]["k"]),
            abs(c_sec["down"]["k"] - c_sec["lep"]["k"]),
        )
        max_dc_1 = max(
            abs(c_sec["up"]["1"] - c_sec["down"]["1"]),
            abs(c_sec["down"]["1"] - c_sec["lep"]["1"]),
        )
        max_dc_i_dl = abs(c_sec["down"]["i"] - c_sec["lep"]["i"])
        max_dK_dl = float(
            max(
                np.max(np.abs(K_sec["down"][s] - K_sec["lep"][s]))
                for s in ("1", "i", "j", "k")
            )
        )
        max_dK_ud_abs = float(
            max(
                np.max(np.abs(np.abs(K_sec["up"][s]) - np.abs(K_down_neg[s])))
                for s in ("1", "j", "k")
            )
        )

        assert max_dc_j < 1e-11
        assert max_dc_k < 1e-11
        assert max_dc_1 < 1e-11
        assert max_dc_i_dl < 1e-11
        assert max_dK_dl < 1e-12
        assert max_dK_ud_abs < 1e-12
        assert abs(R_sec["up"]["i"]) < 1e-14

        row_t1 = {
            "tau": [re_t, im_t],
            "c_down": {s: float(c_sec["down"][s]) for s in ("1", "i", "j", "k")},
            "c_j_minus_c_k": float(c_sec["down"]["j"] - c_sec["down"]["k"]),
            "max_abs_diff_c_j_across_sectors": float(max_dc_j),
            "max_abs_diff_c_k_across_sectors": float(max_dc_k),
            "max_abs_diff_c_1_across_sectors": float(max_dc_1),
            "abs_diff_c_i_down_lep": float(max_dc_i_dl),
            "max_abs_diff_K_down_lep": max_dK_dl,
            "max_abs_diff_mod_K_up_vs_down_neg": max_dK_ud_abs,
            "abs_R_up_i_two_torsion": float(abs(R_sec["up"]["i"])),
        }
        theorem1_checks.append(row_t1)
        print(
            f"  tau={re_t}+{im_t}i: c_j={c_sec['down']['j']:+.4f}, c_k={c_sec['down']['k']:+.4f}, "
            f"c_i={c_sec['down']['i']:+.4f} | max|dc_j|={max_dc_j:.2e}, max|dc_k|={max_dc_k:.2e}, "
            f"|dc_i(d,l)|={max_dc_i_dl:.2e}, |R_u,i|={abs(R_sec['up']['i']):.2e}"
        )

    print("\n=== 2. STRIP PROBE: BOUNDARY-DRESSED DR & MATTER VECTORS VS B1757 ===")
    for _, re_t, im_t in points:
        t = complex(re_t, im_t)
        w = float(a) * t + float(b)
        M_fd = P.SC.channels(re_t, im_t, a, b)
        L_max = float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col]))
        F_forms = P.forms(t)
        dr = align_h2_positive(F_forms["DR"])

        x_d, y_d = B.sector_twists(w, t, B.SIXY["Q"], B.SIXY["d"])
        R_d = B.residues(x_d, y_d, t)
        c_d = B.cA(x_d, y_d, t, R_d)

        # Matter vectors u_up, u_down, u_lep
        u_vecs = {}
        u_invariants = {}
        for sec, (lf, rf) in P.R.SECT.items():
            x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf])
            Rr = B.residues(x, yy, t)
            cc = B.cA(x, yy, t, Rr)
            u_raw = {
                s: (
                    math.sqrt(2 * math.pi * L_max + cc[s]) * Rr[s]
                    if cc[s] is not None
                    else 0.0j
                )
                for s in ("1", "i", "j", "k")
            }
            u_vec = np.array([u_raw["i"], u_raw["j"], u_raw["k"]], dtype=complex)
            u_norm = FD.canon(u_vec)
            u_vecs[sec] = u_norm
            u_invariants[sec] = {
                "abs_u_i": float(abs(u_norm[0])),
                "I_off_cone": float(abs(np.sum(u_norm * u_norm))),
                "ratio_u1_over_norm3": float(abs(u_raw["1"]) / np.linalg.norm(u_vec)),
            }

        # Boundary-dressed DR invariants and scores
        dressed_dr = {}
        for alpha in (0.5, 1.0, -0.5, -1.0):
            weights = np.array(
                [(2 * math.pi * L_max + c_d[s]) ** alpha for s in ("i", "j", "k")]
            )
            hb = align_h2_positive(dr * weights)
            r_split = FD.nine2(np.conj(hb), hb, M_fd, "L_max", B)
            r_same = FD.nine2(hb, hb, M_fd, "L_max", B)
            dressed_dr[f"alpha_{alpha:+.1f}"] = {
                "alpha": alpha,
                "I_off_cone": float(abs(np.sum(hb * hb))),
                "abs_e2_minus_abs_e3": float(abs(hb[1]) - abs(hb[2])),
                "chi2_six_split": float(np.sum(r_split[:6] ** 2)),
                "chi2_nine_split": float(np.sum(r_split**2)),
                "chi2_six_same": float(np.sum(r_same[:6] ** 2)),
                "chi2_nine_same": float(np.sum(r_same**2)),
            }

        # B1757 L_max row for this point
        b1757_lmax = next(
            r for r in b1757_rows if r["tau"] == [re_t, im_t] and r["hor"] == "L_max"
        )
        hu_fit = align_h2_positive(
            np.array([c[0] + 1j * c[1] for c in b1757_lmax["H_u"]])
        )
        hd_fit = align_h2_positive(
            np.array([c[0] + 1j * c[1] for c in b1757_lmax["H_d"]])
        )

        r_base_split = FD.nine2(np.conj(dr), dr, M_fd, "L_max", B)
        r_base_same = FD.nine2(dr, dr, M_fd, "L_max", B)

        row_comp = {
            "tau": [re_t, im_t],
            "L_max": L_max,
            "baseline_DR": {
                "I_off_cone": float(abs(np.sum(dr * dr))),
                "chi2_six_split": float(np.sum(r_base_split[:6] ** 2)),
                "chi2_nine_split": float(np.sum(r_base_split**2)),
                "chi2_six_same": float(np.sum(r_base_same[:6] ** 2)),
                "chi2_nine_same": float(np.sum(r_base_same**2)),
            },
            "matter_vectors": u_invariants,
            "boundary_dressed_DR": dressed_dr,
            "b1757_fitted_L_max": {
                "chi2_nine": float(b1757_lmax["chi2_nine"]),
                "I_u": float(b1757_lmax["H_u_dot_H_u_over_norm2"]),
                "I_d": float(b1757_lmax["H_d_dot_H_d_over_norm2"]),
                "abs_hu_e1": float(abs(hu_fit[0])),
                "abs_hd_e1": float(abs(hd_fit[0])),
                "hu_abs_e2_minus_abs_e3": float(abs(hu_fit[1]) - abs(hu_fit[2])),
                "hd_abs_e2_minus_abs_e3": float(abs(hd_fit[1]) - abs(hd_fit[2])),
                "overlap_hu_with_null_same": float(
                    abs(np.vdot(np.array([0.0, 1.0, 1.0j]) / math.sqrt(2.0), hu_fit))
                ),
                "overlap_hd_with_null_same": float(
                    abs(np.vdot(np.array([0.0, 1.0, 1.0j]) / math.sqrt(2.0), hd_fit))
                ),
            },
        }
        strip_comparisons.append(row_comp)
        print(
            f"  tau={re_t}+{im_t}i: I(DR+0.5)={dressed_dr['alpha_+0.5']['I_off_cone']:.4f}, "
            f"I(DR+1.0)={dressed_dr['alpha_+1.0']['I_off_cone']:.4f}, "
            f"I(u_up)={u_invariants['up']['I_off_cone']:.4f} vs "
            f"B1757 (I_u={row_comp['b1757_fitted_L_max']['I_u']:.4f}, "
            f"I_d={row_comp['b1757_fitted_L_max']['I_d']:.4f}, "
            f"|hu_1|={row_comp['b1757_fitted_L_max']['abs_hu_e1']:.3f}, "
            f"|hd_1|={row_comp['b1757_fitted_L_max']['abs_hd_e1']:.3f})"
        )

    out = {
        "arc": "B1759",
        "points": ["P-357", "P-366", "P-377"],
        "theorem1_sector_universal_puncture_norm": theorem1_checks,
        "strip_comparisons": strip_comparisons,
    }
    out_path = HERE / "sector_universal_puncture_norm.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n")
    print("\nWrote verification/sector_universal_puncture_norm.json successfully.")


if __name__ == "__main__":
    main()
