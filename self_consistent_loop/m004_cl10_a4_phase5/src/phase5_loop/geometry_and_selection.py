"""Gate P5-1 (Track A, 0 of 19): Hyperbolic Geometry of m004 & M^(5) = 8^3_4, Margulis Apex Roots,
Covering-Space Systole Lift, Non-SUSY A_4 Selection, & 2-Torsion Majorana Conservation."""

from __future__ import annotations

from collections import deque
import math
from typing import Any, Dict

import mpmath as mp
import numpy as np

mp.mp.dps = 50


def run_gate_p5_1_geometry() -> Dict[str, Any]:
    """Verify m004 SL(2, Z[omega]) geodesic shells, M^(5) covering lift, apex heights, and 2-torsion seesaw."""
    def zw_mul(x, y):
        return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0] - x[1] * y[1])

    def zw_add(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def mmul(M, N):
        return (
            (zw_add(zw_mul(M[0][0], N[0][0]), zw_mul(M[0][1], N[1][0])), zw_add(zw_mul(M[0][0], N[0][1]), zw_mul(M[0][1], N[1][1]))),
            (zw_add(zw_mul(M[1][0], N[0][0]), zw_mul(M[1][1], N[1][0])), zw_add(zw_mul(M[1][0], N[0][1]), zw_mul(M[1][1], N[1][1]))),
        )

    def minv(M):
        a, b = M[0][0], M[0][1]
        c, d = M[1][0], M[1][1]
        return ((d, (-b[0], -b[1])), ((-c[0], -c[1]), a))

    def cpsl(M):
        fl = (M[0][0][0], M[0][0][1], M[0][1][0], M[0][1][1], M[1][0][0], M[1][0][1], M[1][1][0], M[1][1][1])
        ng = tuple(-v for v in fl)
        return min(fl, ng)

    I_z = (((1, 0), (0, 0)), ((0, 0), (1, 0)))
    A_z = (((1, 0), (1, 0)), ((0, 0), (1, 0)))
    Ai_z = (((1, 0), (-1, 0)), ((0, 0), (1, 0)))
    B_z = (((1, 0), (0, 0)), ((0, -1), (1, 0)))
    Bi_z = (((1, 0), (0, 0)), ((0, 1), (1, 0)))

    C3T = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=int)
    Xh = np.diag([1, -1, -1]).astype(int)
    pA, pB = tuple((-x) % 5 for x in range(5)), tuple((1 - x) % 5 for x in range(5))
    gens = [
        ("a", A_z, C3T, pA),
        ("A", Ai_z, C3T.T, pA),
        ("b", B_z, Xh @ C3T, pB),
        ("B", Bi_z, C3T.T @ Xh, pB),
    ]
    inv_c = {"a": "A", "A": "a", "b": "B", "B": "b"}

    vis = {cpsl(I_z): ("", I_z, np.eye(3, dtype=int), (0, 1, 2, 3, 4))}
    q = deque([("", I_z, np.eye(3, dtype=int), (0, 1, 2, 3, 4))])
    while q:
        w, M, Ma4, pd = q.popleft()
        if len(w) >= 7:
            continue
        for ch, gz, ga4, gp in gens:
            if w and inv_c[w[-1]] == ch:
                continue
            M2 = mmul(M, gz)
            k = cpsl(M2)
            if k not in vis:
                pd2 = tuple(pd[gp[i]] for i in range(5))
                vis[k] = (w + ch, M2, Ma4 @ ga4, pd2)
                q.append((w + ch, M2, Ma4 @ ga4, pd2))

    # Index-5 covering subgroup pi_1(M^(5)) = Stab_{D_5}(0):
    H_el = [(w, M, Ma4, pd) for (w, M, Ma4, pd) in vis.values() if pd[0] == 0 and w != ""]
    H_c = [M for (w, M, _, _) in H_el if len(w) <= 4] + [I_z]
    H_ci = [(C, minv(C)) for C in H_c]

    omega = mp.exp(2j * mp.pi / 3)
    n_m5_ell1 = 0
    n_m5_ell2 = 0
    seen = set()
    for w, M, _, _ in sorted(H_el, key=lambda x: len(x[0])):
        tp, tq = zw_add(M[0][0], M[1][1])
        if tq == 0 and abs(tp) <= 2:
            continue
        k = cpsl(M)
        if k in seen:
            continue
        orb = set()
        Minv = minv(M)
        for C, Ci in H_ci:
            orb.add(cpsl(mmul(mmul(C, M), Ci)))
            orb.add(cpsl(mmul(mmul(C, Minv), Ci)))
        seen |= orb
        tr_mp = mp.mpf(tp) + mp.mpf(tq) * omega
        s_tr = -tr_mp if (mp.re(tr_mp) < 0 or (mp.re(tr_mp) == 0 and mp.im(tr_mp) < 0)) else tr_mp
        ell = float(2 * mp.re(mp.acosh(s_tr / 2)))
        if abs(ell - 1.087070145) < 1e-4:
            n_m5_ell1 += 1
        elif abs(ell - 1.662885891) < 1e-4:
            n_m5_ell2 += 1

    # Exact 50-digit lengths, twists, Margulis apex heights, and B940 Selberg scales:
    def eval_zw_word(word: str):
        M = I_z
        Ma4 = np.eye(3, dtype=int)
        pd = (0, 1, 2, 3, 4)
        gmap = {c: (gz, ga4, gp) for c, gz, ga4, gp in gens}
        for c in word:
            gz, ga4, gp = gmap[c]
            M = mmul(M, gz)
            Ma4 = Ma4 @ ga4
            pd = tuple(pd[gp[i]] for i in range(5))
        tp, tq = zw_add(M[0][0], M[1][1])
        tr = mp.mpf(tp) + mp.mpf(tq) * omega
        c_mp = mp.mpf(M[1][0][0]) + mp.mpf(M[1][0][1]) * omega
        s_tr = -tr if (mp.re(tr) < 0 or (mp.re(tr) == 0 and mp.im(tr) < 0)) else tr
        hl = mp.acosh(s_tr / 2)
        z_ap = (abs(mp.sqrt(tr**2 - 4)) / (2 * abs(c_mp))) if abs(c_mp) > 0 else mp.mpf(0)
        return 2 * mp.re(hl), 2 * mp.im(hl), z_ap, Ma4, pd

    ell1, th1, z_ap_Ab, _, pd_Ab = eval_zw_word("Ab")
    ell2, th2, z_ap_AAb, _, pd_AAb = eval_zw_word("AAb")
    z_aaB_fourth_minus_3 = float(abs(z_ap_AAb**4 - 3))

    lam1_b940 = mp.mpf("2.9745505801732")
    eps1 = (mp.exp(-lam1_b940 * ell1) / abs(2 * mp.sinh((ell1 + 1j * th1) / 2))) / (2 * mp.pi)
    eps2 = (mp.exp(-lam1_b940 * ell2) / abs(2 * mp.sinh((ell2 + 1j * th2) / 2))) / (2 * mp.pi)
    r_sh = eps2 / eps1

    # Explicit nullspace dimensions on T^2 vs m004:
    _, _, _, M_a, _ = eval_zw_word("a")
    _, _, _, M_b, _ = eval_zw_word("b")
    dim_cusp_inv = int(np.sum(np.linalg.svd(M_a - np.eye(3), compute_uv=False) < 1e-12))
    dim_bulk_inv = int(np.sum(np.linalg.svd(np.vstack([M_a - np.eye(3), M_b - np.eye(3)]), compute_uv=False) < 1e-12))

    # 2-torsion Majorana fiber character conservation check (Clause N3):
    chars = [(1, 0), (0, 1), (1, 1)]
    offdiag_allowed = sum(
        1 for i in range(3) for j in range(3) if i != j and ((chars[i][0] + chars[j][0]) % 2 == 0 and (chars[i][1] + chars[j][1]) % 2 == 0)
    )
    diag_allowed = sum(1 for i in range(3) if ((2 * chars[i][0]) % 2 == 0 and (2 * chars[i][1]) % 2 == 0))

    # 50-digit hyperbolic volume V_5 = 5 Vol(m004) = 10 * Im(Li_2(e^{i*pi/3})) (2 ideal regular tetrahedra):
    vol_m004 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    vol_m5 = 5 * vol_m004

    passed = bool(
        n_m5_ell1 == 0
        and n_m5_ell2 == 4
        and float(z_ap_Ab) < 1.0
        and z_aaB_fourth_minus_3 < 1e-48
        and dim_cusp_inv == 1
        and dim_bulk_inv == 0
        and offdiag_allowed == 0
        and diag_allowed == 3
    )

    return {
        "gate_p5_1_passed": passed,
        "vol_m004": float(vol_m004),
        "vol_m5_cover": float(vol_m5),
        "ell1_systole": float(ell1),
        "theta1_rad": float(th1),
        "ell2_reflection": float(ell2),
        "theta2_rad": float(th2),
        "z_apex_Ab": float(z_ap_Ab),
        "z_apex_AAb": float(z_ap_AAb),
        "z_apex_AAb_fourth_minus_3_err": z_aaB_fourth_minus_3,
        "m5_closed_geodesics_at_ell1": n_m5_ell1,
        "m5_closed_systoles_at_ell2": n_m5_ell2,
        "exact_covering_sheet_fraction": 0.2,
        "eps_1": float(eps1),
        "eps_2": float(eps2),
        "r_sh": float(r_sh),
        "dim_cusp_A4_invariants": dim_cusp_inv,
        "dim_bulk_A4_invariants": dim_bulk_inv,
        "majorana_2torsion_offdiag_allowed": offdiag_allowed,
        "majorana_2torsion_diag_allowed": diag_allowed,
    }
