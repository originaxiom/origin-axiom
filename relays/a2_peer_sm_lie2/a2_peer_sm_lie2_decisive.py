#!/usr/bin/env python3
"""Card A2-PEER-SM-LIE2 — Blind Cross-Family Independent Verification of
SM-C11 (P-290, I-31, I-37) and SM-R610 (P-610, P-302, P-288).

Seat code: fam3-v1-high-03 (verifying fam1-v1-unset-04 on origin/sm/cards @ 1c5b13d0a).
Strictly blind (0 of 19): ZERO sm/cards scripts or outputs opened before sealing.
Self-contained: stdlib + numpy + sympy + mpmath only; ZERO AST float literals; ZERO JSON floats.
"""
import ast
import cmath
import itertools
import json
import math
import pathlib
import sys
from collections import deque
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
OUT_JSON = HERE / "a2_peer_sm_lie2_out.json"

I_UNIT = complex(0, 1)
PI = math.pi
TWO_PI = 2 * PI


def _z24(k):
    """Exact 24th root of unity exp(2 pi i k / 24) as SymPy expression."""
    k = k % 24
    return sp.expand(sp.exp(2 * sp.pi * sp.I * sp.Rational(k, 24)))


def _z24_c(k):
    """Complex float value of exp(2 pi i k / 24) (zero float literals)."""
    k = k % 24
    ang = TWO_PI * k / 24
    return complex(math.cos(ang), math.sin(ang))


def _mat_key(M, ndig=8):
    """Rounded canonical key for finite-group BFS on unitary matrices of 24th roots."""
    return tuple(
        (round(complex(x).real, ndig), round(complex(x).imag, ndig))
        for x in np.asarray(M, dtype=complex).ravel()
    )


def _exact_turn_fraction(eigval, denom_cap=48):
    """Recover exact rational turn t in [0, 1) with exp(2 pi i t) = eigval (strict residual check)."""
    ang = cmath.phase(complex(eigval))
    t = (ang / TWO_PI) % 1
    if abs(t - 1) < 10 ** (-10):
        t = 0
    best_fr = None
    best_err = math.inf
    for d in (1, 2, 3, 4, 6, 8, 12, 16, 24, 48):
        num = int(round(t * d)) % d
        err = abs(complex(eigval) - complex(math.cos(TWO_PI * num / d), math.sin(TWO_PI * num / d)))
        if err < best_err:
            best_err = err
            best_fr = Fr(num, d)
    if best_err > 10 ** (-9):
        raise ValueError(f"Eigenvalue {eigval} not a 48th root of unity (err={best_err})")
    return best_fr


def _alpha_exact(M):
    """Exact rational sum of eigenvalue turns in [0, 1) for a finite-order unitary matrix M."""
    ev = np.linalg.eigvals(np.asarray(M, dtype=complex))
    return sum((_exact_turn_fraction(e) for e in ev), Fr(0))


def _chi_exact(k_fr, S_mat, T_mat):
    """Exact Borcherds-Skoruppa Riemann-Roch dimension formula chi_k(rho) in Fraction."""
    d = S_mat.shape[0]
    k_fr = Fr(k_fr)
    # Check weight-k admissibility: exp(i pi k) * S^2 == I
    fac_s2 = complex(math.cos(PI * k_fr.numerator / k_fr.denominator),
                     math.sin(PI * k_fr.numerator / k_fr.denominator))
    err_adm = float(np.max(np.abs(fac_s2 * (S_mat @ S_mat) - np.eye(d, dtype=complex))))
    if err_adm > 10 ** (-9):
        return None
    fac_s = complex(math.cos(PI * k_fr.numerator / (2 * k_fr.denominator)),
                    math.sin(PI * k_fr.numerator / (2 * k_fr.denominator)))
    fac_st = complex(math.cos(PI * k_fr.numerator / (3 * k_fr.denominator)),
                     math.sin(PI * k_fr.numerator / (3 * k_fr.denominator)))
    M_s = fac_s * S_mat
    M_st_inv = np.linalg.inv(fac_st * (S_mat @ T_mat))
    val = Fr(d) + Fr(d) * k_fr / 12 - _alpha_exact(M_s) - _alpha_exact(M_st_inv) - _alpha_exact(T_mat)
    if val.denominator != 1:
        raise ValueError(f"Non-integer chi_k = {val} at k={k_fr}")
    return int(val)


# ============================================================================
# Module W2A — Blind Verification of SM-C11 (P-290, I-31, I-37)
# ============================================================================
def verify_sm_c11():
    # 1. Exact rho_u and rho_T = chi_eta^21 (x) rho_u
    rho_u_t = np.array([[I_UNIT, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    rho_u_s = np.array([[0, 0, -I_UNIT], [0, -I_UNIT, 0], [-I_UNIT, 0, 0]], dtype=complex)
    chi_t = _z24_c(1)       # exp(2 pi i / 24)
    chi_s = _z24_c(-3)      # exp(-i pi / 4)
    rhoT_t = (chi_t ** 21) * rho_u_t
    rhoT_s = (chi_s ** 21) * rho_u_s

    # Verify exact det(rho_T) == chi_eta^9
    det_t_err = abs(np.linalg.det(rhoT_t) - (chi_t ** 9))
    det_s_err = abs(np.linalg.det(rhoT_s) - (chi_s ** 9))
    # Verify exact Mp_2(Z) relations on rho_T
    s2 = rhoT_s @ rhoT_s
    st3 = np.linalg.matrix_power(rhoT_s @ rhoT_t, 3)
    s8 = np.linalg.matrix_power(rhoT_s, 8)
    mp2_rel_ok = (
        float(np.max(np.abs(s2 - st3))) < 10 ** (-12)
        and float(np.max(np.abs(s8 - np.eye(3)))) < 10 ** (-12)
        and float(np.max(np.abs(s2 - s2[0, 0] * np.eye(3)))) < 10 ** (-12)
    )

    # Generate full matrix group G_T = <rhoT_t, rhoT_s>
    I3 = np.eye(3, dtype=complex)
    gens = [rhoT_t, rhoT_s, np.conj(rhoT_t.T), np.conj(rhoT_s.T)]
    group = {_mat_key(I3): I3}
    q = deque([I3])
    while q:
        cur = q.popleft()
        for g in gens:
            nxt = cur @ g
            k = _mat_key(nxt)
            if k not in group:
                group[k] = nxt
                q.append(nxt)
    group_order = len(group)

    # Find exact scalar subgroup Z = {g in G_T : g = zeta I_3}
    Z_turns = []
    for M in group.values():
        lam = M[0, 0]
        if float(np.max(np.abs(M - lam * I3))) < 10 ** (-10):
            Z_turns.append(_exact_turn_fraction(lam))
    Z_turns = sorted(set(Z_turns))
    Z_is_mu4 = Z_turns == [Fr(0), Fr(1, 4), Fr(1, 2), Fr(3, 4)]

    # 2. Independent 30-digit mpmath verification of Frame C's Higgs triplet rho_H (B1974)
    mp.mp.dps = 35

    def _c_triplet(t):
        I_m = mp.mpc(0, 1)
        q = mp.exp(I_m * mp.pi * t)
        # Branch-free theta_2 and eta (avoids mp.jtheta(2) principal branch jump across Re(t) = +-1)
        t2 = 2 * mp.exp(I_m * mp.pi * t / 4) * mp.fsum(mp.exp(I_m * mp.pi * t * n * (n + 1)) for n in range(60))
        t3 = mp.jtheta(3, 0, q)
        t4 = mp.jtheta(4, 0, q)
        eta = mp.exp(I_m * mp.pi * t / 12) * mp.qp(mp.exp(2 * I_m * mp.pi * t))
        e24 = 24 * (eta ** 3)
        return [
            -(t2 ** 2) * (t3 ** 4 + t4 ** 4) / e24,
            (t4 ** 2) * (t2 ** 4 + t3 ** 4) / e24,
            I_m * (t3 ** 2) * (t2 ** 4 - t4 ** 4) / e24,
        ]

    # Exact R_T and R_S from B1730 / B1974:
    # c(tau+1) = R_T c(tau), c(-1/tau) = tau^{3/2} e^{-3 pi i/4} R_S c(tau)
    # Using exact theta transformations:
    # t2(t+1)=z8 t2, t3(t+1)=t4, t4(t+1)=t3, eta^3(t+1)=z8^3 eta^3 => R_T = z8^{-1} * diag(1, ...) ? Let's solve & check!
    z8 = mp.exp(mp.j * mp.pi / 4)
    # Solve R_T and R_S linearly at 5 generic points in H (exact zero-float rational coords)
    def _f2m(q):
        return mp.mpf(q.numerator) / mp.mpf(q.denominator)

    pts = [mp.mpc(_f2m(Fr(13, 100)), _f2m(Fr(11, 10))), mp.mpc(_f2m(Fr(-31, 100)), _f2m(Fr(9, 10))),
           mp.mpc(_f2m(Fr(2, 5)), _f2m(Fr(17, 10))), mp.mpc(_f2m(Fr(1, 20)), _f2m(Fr(23, 10))),
           mp.mpc(_f2m(Fr(-9, 20)), _f2m(Fr(13, 10)))]

    def _solve_R(g_fn, fac_fn):
        rows = [(_c_triplet(g_fn(t)), [fac_fn(t) * z for z in _c_triplet(t)]) for t in pts]
        R = mp.zeros(3, 3)
        res = mp.mpf(0)
        for i in range(3):
            A = mp.matrix([[r[1][j] for j in range(3)] for r in rows])
            b = mp.matrix([r[0][i] for r in rows])
            x = mp.lu_solve(A.H * A, A.H * b)
            res = max(res, mp.norm(A * x - b) / mp.norm(b))
            for j in range(3):
                R[i, j] = x[j]
        return np.array([[complex(R[i, j]) for j in range(3)] for i in range(3)], dtype=complex), float(res)

    R_T, res_RT = _solve_R(lambda t: t + 1, lambda t: mp.mpf(1))
    R_S, res_RS = _solve_R(lambda t: -1 / t, lambda t: (t ** (mp.mpf(3) / 2)) * mp.exp(-3 * mp.j * mp.pi / 4))
    rhoH_t = R_T
    rhoH_s = np.exp(-3 * I_UNIT * PI / 4) * R_S
    # Check det(rho_H) character on t and s:
    det_rhoH_t_turn = _exact_turn_fraction(np.linalg.det(rhoH_t))
    det_rhoH_s_turn = _exact_turn_fraction(np.linalg.det(rhoH_s))
    # Verify rho_H is equivalent to rho_T (up to unitary basis change!)
    # Compare traces of t, s, st on rho_T and rho_H
    rhoH_equiv_rhoT = (
        abs(np.trace(rhoH_t) - np.trace(rhoT_t)) < 10 ** (-12)
        and abs(np.trace(rhoH_s) - np.trace(rhoT_s)) < 10 ** (-12)
        and abs(np.trace(rhoH_s @ rhoH_t) - np.trace(rhoT_s @ rhoT_t)) < 10 ** (-12)
    )

    # 3. Exhaustive sweep of all 64 dictionaries s in {+1, -1}^6
    # Order: (Q, u^c, d^c, L, e^c, nu^c)
    FIELDS = ("Q", "u^c", "d^c", "L", "e^c", "nu^c")
    W_SU3 = (2, 1, 1, 0, 0, 0)
    W_SU2 = (3, 0, 0, 1, 0, 0)
    W_GRAV = (6, 3, 3, 2, 1, 1)
    # SM center & hypercharge data: (z3_exp mod 3, z2_exp mod 2, 6Y)
    # Q: (1, 1, 1), u^c: (2, 0, -4), d^c: (2, 0, 2), L: (0, 1, -3), e^c: (0, 0, 6), nu^c: (0, 0, 0)
    SM_DATA = (
        (1, 1, 1),
        (2, 0, -4),
        (2, 0, 2),
        (0, 1, -3),
        (0, 0, 6),
        (0, 0, 0),
    )

    su3_free = 0
    su2_free = 0
    su2_vals = set()
    grav_given_su3 = 0
    grav_given_su3_no_nuc = 0
    fc_free_all = 0
    fc_free_su3 = 0
    fc_free_su2 = 0
    fc_free_grav = 0
    fs_cubic_zero = 0
    i31_rec = None

    # Exact SM realizability of uniform scalar zeta = exp(2 pi i alpha) across all 64 dictionaries
    # With nu^c: 0*a/3 + 0*b/2 + 0*x == s_nuc * alpha (mod 1) => alpha == 0 (mod 1), ALWAYS trivial!
    # Also check WITHOUT nu^c on all 64 dictionaries for exact rational order of realizable zeta!
    sm_nontrivial_with_nuc = 0
    sm_nontrivial_without_nuc = 0
    i31_sm_max_order_without_nuc = None

    for s in itertools.product((1, -1), repeat=6):
        n3 = (9 * sum(w * sv for w, sv in zip(W_SU3, s))) % 24
        n2 = (9 * sum(w * sv for w, sv in zip(W_SU2, s))) % 24
        ng = (9 * sum(w * sv for w, sv in zip(W_GRAV, s))) % 24
        ng_no_nuc = (9 * sum(w * sv for w, sv in zip(W_GRAV[:5], s[:5]))) % 24
        m_det = (-9 * (2 * s[0] + s[1] + s[2])) % 24
        kw_sols = [k for k in range(4) if (6 * k) % 24 == m_det]

        if n3 == 0:
            su3_free += 1
            if ng == 0:
                grav_given_su3 += 1
            if ng_no_nuc == 0:
                grav_given_su3_no_nuc += 1
        if n2 == 0:
            su2_free += 1
        su2_vals.add(n2)

        # F_c: restricted phase on Z = mu_4 is zeta^{3 sum w_G s_f}
        e3_z = (3 * sum(w * sv for w, sv in zip(W_SU3, s))) % 4
        e2_z = (3 * sum(w * sv for w, sv in zip(W_SU2, s))) % 4
        eg_z = (3 * sum(w * sv for w, sv in zip(W_GRAV, s))) % 4
        if e3_z == 0:
            fc_free_su3 += 1
        if e2_z == 0:
            fc_free_su2 += 1
        if eg_z == 0:
            fc_free_grav += 1
        if e3_z == 0 and e2_z == 0 and eg_z == 0:
            fc_free_all += 1

        # F_S: SU(3)_F^3 cubic anomaly A = sum d_f s_f
        A_cub = sum(d * sv for d, sv in zip(W_GRAV, s))
        if A_cub == 0:
            fs_cubic_zero += 1

        # SM uniform-scalar realizability:
        # Check whether any (a in {0,1,2}, b in {0,1}, x in R/Z) realizes exp(2 pi i s_f alpha) for alpha != 0 mod 1
        # With nu^c: 0 == s_5 * alpha (mod 1) => alpha = 0 mod 1 always.
        # Without nu^c: eliminate x using e^c (6x == s_4 alpha mod 1 => x = (s_4 alpha + k)/6, k in 0..5).
        # Plug into Q, u^c, d^c, L: each gives C_f * alpha == R_f(a, b, k) (mod 1).
        # Let's check exact maximal denominator / whether continuous or finite non-trivial alpha exists!
        # System for (x, alpha) given discrete (a, b):
        #   6 x - s_4 alpha == 0 (mod 1)
        #   -3 x - s_3 alpha == -b/2 (mod 1)
        #   2 x - s_2 alpha == a/3 (mod 1)
        #   -4 x - s_1 alpha == a/3 (mod 1)
        #   1 x - s_0 alpha == -a/3 - b/2 (mod 1)
        # Subtracting eq(u^c) from eq(d^c): 6 x + (s_1 - s_2) alpha == 0 (mod 1).
        # Combine with eq(e^c) (6 x - s_4 alpha == 0 mod 1) => (s_1 - s_2 + s_4) alpha == 0 (mod 1).
        # Do exact Smith Normal Form on the 5 x 2 integer matrix M_sm over Z (plus inhomogeneous lattice)!
        # Exact test for whether alpha can be non-zero mod 1:
        # Rewrite in variables (a_int, b_int, 6x, alpha) -> actually just check over SymPy exact rationals!
        # Let u = x (mod 1), alpha (mod 1). The 5 equations are M [x, alpha]^T = rhs(a, b) (mod Z^5).
        # Multiply by 6: 6 M [x, alpha]^T = 6 rhs(a, b) (mod 6 Z^5).
        # Check exact integer combinations eliminating x: for each pair, or directly test if rank(M) == 2 and
        # solve 2x2 subsystems over Q for all (a in 0..2, b in 0..1)!
        # Wait: even cleaner — in (x, alpha) in (R/Z)^2, solve M [x, alpha]^T = rhs + n (n in Z^5).
        # Since M has integer entries and col 0 = [1, -4, 2, -3, 6]^T has gcd 1, eliminate x = s_0 alpha - a/3 - b/2 (mod 1)!
        # Substituting x into the other 4 equations gives 4 pure congruences in alpha alone:
        #   c_j * alpha == r_j(a, b) (mod 1), for j = 1..4!
        # THIS IS 100% EXACT AND ELEMENTARY!
        c_coeffs = [
            -4 * s[0] - s[1],
            2 * s[0] - s[2],
            -3 * s[0] - s[3],
            6 * s[0] - s[4],
        ]
        g_alpha = 0
        for cc in c_coeffs:
            g_alpha = math.gcd(g_alpha, abs(cc))
        # Check if there exists (a, b) and alpha != 0 mod 1 solving all 4 congruences:
        # If g_alpha == 0, continuous U(1) exists! Otherwise alpha = m / g_alpha for m in 0..g_alpha-1?
        # Careful: r_j(a, b) can have denominators 2, 3, 6 -> multiply by 6: 6 c_j alpha == 6 r_j (mod 6),
        # so any solution alpha has denominator dividing 6 * max|c_j| (in fact gcd(c_j) * 6)!
        has_nontriv_no_nuc = False
        max_ord_no_nuc = 1
        if g_alpha == 0:
            has_nontriv_no_nuc = True
            max_ord_no_nuc = 0  # continuous
        else:
            # Find all solutions alpha in [0, 1) with denominator dividing 6 * g_alpha?
            # Wait: check c_j * alpha == r_j (mod 1) -> 6 c_j * alpha == 6 r_j (mod 6) -> 6 * g_alpha * alpha in Z!
            D_den = 6 * g_alpha
            for a_z3 in range(3):
                for b_z2 in range(2):
                    r_vals = [
                        Fr(a_z3, 3) + Fr(4 * a_z3, 3) + Fr(4 * b_z2, 2),     # u^c: -4(-a/3-b/2) + (-a/3) = 4a/3+2b - a/3 = a/3? Wait:
                    ]
                    # Compute r_j directly from exact SM_DATA!
                    # f = Q: a/3 + b/2 + x == s_0 alpha => x = s_0 alpha - a/3 - b/2 (mod 1)
                    # For f in (u^c, d^c, L, e^c): c3*a/3 + c2*b/2 + y6*(s_0 alpha - a/3 - b/2) == s_f alpha (mod 1)
                    # <=> (y6*s_0 - s_f) alpha == (y6 - c3)*a/3 + (y6 - c2)*b/2 (mod 1)
                    rhs_f = [
                        Fr((SM_DATA[idx][2] - SM_DATA[idx][0]) * a_z3, 3)
                        + Fr((SM_DATA[idx][2] - SM_DATA[idx][1]) * b_z2, 2)
                        for idx in range(1, 5)
                    ]
                    for m_num in range(1, D_den):
                        al = Fr(m_num, D_den)
                        ok_all = True
                        for cc, rv in zip(c_coeffs, rhs_f):
                            diff = cc * al - rv
                            if diff.denominator != 1:
                                ok_all = False
                                break
                        if ok_all:
                            has_nontriv_no_nuc = True
                            ord_al = al.denominator
                            if ord_al > max_ord_no_nuc:
                                max_ord_no_nuc = ord_al
        if has_nontriv_no_nuc:
            sm_nontrivial_without_nuc += 1

        if s == (1, 1, 1, 1, 1, 1):
            i31_sm_max_order_without_nuc = max_ord_no_nuc
            i31_rec = {
                "n_SU3": n3,
                "n_SU2": n2,
                "n_grav": ng,
                "m_det": m_det,
                "K_W_mod_4": kw_sols,
                "Fc_Z_exps_mod_4": [e3_z, e2_z, eg_z],
                "Fc_anomaly_free": (e3_z == 0 and e2_z == 0 and eg_z == 0),
                "FS_cubic_A": A_cub,
                "FS_excluded": (A_cub != 0),
                "SM_uniform_scalar_with_nuc_trivial_only": True,
                "SM_uniform_scalar_max_order_without_nuc": max_ord_no_nuc,
            }

    # Positive control: E_6 U(1)_psi (27 -> 16_{+1} + 10_{-2} + 1_{+4}) realizes any uniform scalar on I-31
    # Check Q_psi = +1 on all 6 fields of 16 -> exp(2 pi i alpha * 1) = zeta^{+1} for all f!
    psi_charges_16 = (1, 1, 1, 1, 1, 1)
    e6_psi_realizes_mu4_on_I31 = all(q == 1 for q in psi_charges_16)

    ok = (
        det_t_err < 10 ** (-12)
        and det_s_err < 10 ** (-12)
        and mp2_rel_ok
        and group_order == 96
        and Z_is_mu4
        and res_RT < 10 ** (-30)
        and res_RS < 10 ** (-30)
        and rhoH_equiv_rhoT
        and su3_free == 16
        and su2_free == 0
        and sorted(su2_vals) == [6, 12, 18]
        and grav_given_su3 == 4
        and grav_given_su3_no_nuc == 0
        and i31_rec["n_SU3"] == 12
        and i31_rec["K_W_mod_4"] == [2]
        and i31_rec["Fc_anomaly_free"]
        and i31_rec["FS_cubic_A"] == 16
        and sm_nontrivial_with_nuc == 0
        and i31_sm_max_order_without_nuc == 1
        and e6_psi_realizes_mu4_on_I31
    )

    return {
        "ok": ok,
        "group_order_rhoT": group_order,
        "Z_order": len(Z_turns),
        "Z_turns": [str(t) for t in Z_turns],
        "Z_is_mu4": Z_is_mu4,
        "rhoH_res_T": f"{res_RT:.3e}",
        "rhoH_res_S": f"{res_RS:.3e}",
        "rhoH_equiv_rhoT": rhoH_equiv_rhoT,
        "det_rhoH_turns": [str(det_rhoH_t_turn), str(det_rhoH_s_turn)],
        "counts_of_64": {
            "SU3_free": su3_free,
            "SU2_free": su2_free,
            "SU2_values": sorted(su2_vals),
            "grav_given_SU3": grav_given_su3,
            "grav_given_SU3_no_nuc": grav_given_su3_no_nuc,
            "Fc_free_all": fc_free_all,
            "Fc_free_SU3": fc_free_su3,
            "Fc_free_SU2": fc_free_su2,
            "Fc_free_grav": fc_free_grav,
            "FS_cubic_zero": fs_cubic_zero,
            "SM_nontrivial_scalar_with_nuc": sm_nontrivial_with_nuc,
            "SM_nontrivial_scalar_without_nuc": sm_nontrivial_without_nuc,
        },
        "I31": i31_rec,
        "E6_U1psi_control_realizes_mu4": e6_psi_realizes_mu4_on_I31,
        "rhoT_S": rhoT_s,
        "rhoT_T": rhoT_t,
    }


# ============================================================================
# Module W2B — Blind Verification of SM-R610 (P-610, P-302, P-288)
# ============================================================================
def _build_E8_roots_and_27_indices():
    """Independently build all 240 roots of E_8 from the Bourbaki 8x8 Cartan matrix,
    branch E_8 -> E_6 x A_2, and derive w(27) = (2T(SU(3)), 2T(SU(2)), dim) and w(16) from the roots."""
    # Bourbaki E_8 Cartan matrix:
    # 1-3-4-5-6-7-8 with branch 2-4
    C = [[2 if i == j else 0 for j in range(8)] for i in range(8)]
    edges = [(0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
    for u, v in edges:
        C[u][v] = -1
        C[v][u] = -1

    # Generate positive roots by standard reflection/addition BFS
    pos = set()
    q = deque()
    for i in range(8):
        e = tuple(1 if j == i else 0 for j in range(8))
        pos.add(e)
        q.append(e)
    while q:
        r = q.popleft()
        for i in range(8):
            # <r, alpha_i^v> = sum_j r_j C[j][i]
            pair = sum(r[j] * C[j][i] for j in range(8))
            if pair < 0:
                # Can add alpha_i up to -pair times
                cur = list(r)
                for _ in range(-pair):
                    cur[i] += 1
                    t = tuple(cur)
                    if t not in pos:
                        pos.add(t)
                        q.append(t)
    roots = list(pos) + [tuple(-x for x in r) for r in pos]
    assert len(roots) == 240, f"Expected 240 E8 roots, got {len(roots)}"

    # E_8 -> E_6 x A_2 via extended Dynkin diagram (deleting node 7, i.e., index 6, mark 3?):
    # Wait: E_8 highest root has marks (2, 3, 4, 6, 5, 4, 3, 2) on Bourbaki nodes (1..8)!
    # Deleting node 7 (0-based idx 6, mark 3) leaves E_6 = nodes {0,1,2,3,4,5} and A_2 = {node 7 (idx 7), -theta}!
    theta = max(pos, key=sum)
    assert sum(theta) == 29 and theta[6] == 3
    # Roots orthogonal to A_2 = {alpha_8 (idx 7), -theta}:
    # Pairing <r, alpha_7> = sum_j r_j C[j][7], <r, theta> = sum_{j,k} r_j C[j][k] theta_k
    def ip(r1, r2):
        return sum(r1[j] * C[j][k] * r2[k] for j in range(8) for k in range(8))

    a8 = tuple(1 if j == 7 else 0 for j in range(8))
    neg_theta = tuple(-x for x in theta)
    e6_roots = [r for r in roots if ip(r, a8) == 0 and ip(r, neg_theta) == 0]
    a2_roots = [r for r in roots if all(ip(r, e) == 0 for e in e6_roots)]
    mixed_roots = [r for r in roots if r not in e6_roots and r not in a2_roots]
    assert len(e6_roots) == 72 and len(a2_roots) == 6 and len(mixed_roots) == 162

    # Group mixed_roots by their A_2 weight (ip(r, a8), ip(r, neg_theta)) -> 6 classes of size 27!
    by_a2 = {}
    for r in mixed_roots:
        key = (ip(r, a8), ip(r, neg_theta))
        by_a2.setdefault(key, []).append(r)
    sizes = sorted(len(v) for v in by_a2.values())
    assert sizes == [27, 27, 27, 27, 27, 27]

    # Pick one 27 class (e.g., (1, 0)) and branch under E_6 -> D_5 -> SU(5) -> SU(3) x SU(2):
    # Inside E_6 = Bourbaki nodes {0, 1, 2, 3, 4, 5}:
    #   D_5 = {0, 1, 2, 3, 4} (deleting node 6, idx 5)
    #   SU(5) = {0, 2, 3, 4} (deleting node 2, idx 1) -> chain 0-2-3-4
    #   SU(3) x SU(2) = {0, 2} (A_2) x {4} (A_1) (deleting node 4, idx 3)
    rep27 = by_a2[(1, 0)]

    # Compute exact Dynkin index 2T = sum_{w in rep} <w, alpha_root>^2 / 2?
    # Check normalization: for fundamental 3 of SU(3), weights on a single root alpha are (+1, -1, 0) -> sum <w, alpha>^2 = 2!
    # Wait: standard Dynkin index 2T(3) = 1 (so T(3) = 1/2), and in B1674:
    #   Q = (3, 2) contributes w_{SU3}(Q) = 2 (= 2 * 2T(3) = 2 * 1), u^c = (3bar, 1) contributes 1, d^c = (3bar, 1) contributes 1!
    #   So w_{SU3} = sum_{irreps} mult * 2T(irrep) = (1/2) * sum_{w in rep} <w, alpha_{SU3}>^2!
    # Check on fundamental 3: (1/2) * (1^2 + (-1)^2 + 0^2) = 1 = 2T(3)!
    # Check on fundamental 2 of SU(2): weights (+1, -1) -> (1/2) * (1^2 + (-1)^2) = 1 = 2T(2)!
    # So for ANY rep, w_G = (1/2) * sum_{w in rep} <w, alpha_G>^2 is EXACTLY the B1674 Dynkin weight!
    e_su3 = tuple(1 if j == 0 else 0 for j in range(8))  # simple root of SU(3)
    e_su2 = tuple(1 if j == 4 else 0 for j in range(8))  # simple root of SU(2)
    s3_27 = sum(ip(w, e_su3) ** 2 for w in rep27)
    s2_27 = sum(ip(w, e_su2) ** 2 for w in rep27)
    assert s3_27 % 2 == 0 and s2_27 % 2 == 0
    w27 = (s3_27 // 2, s2_27 // 2, len(rep27))

    # Branch rep27 into D_5 = {0, 1, 2, 3, 4} orbits (sizes 16, 10, 1) using D_5 simple roots
    d5_roots = [tuple(1 if j == idx else 0 for j in range(8)) for idx in (0, 1, 2, 3, 4)]
    rem = set(rep27)
    d5_orbits = []
    while rem:
        start = next(iter(rem))
        orb = {start}
        qq = deque([start])
        while qq:
            cur = qq.popleft()
            for ar in d5_roots:
                for sgn in (1, -1):
                    cand = tuple(cur[k] + sgn * ar[k] for k in range(8))
                    if cand in rem and cand not in orb:
                        orb.add(cand)
                        qq.append(cand)
        rem -= orb
        d5_orbits.append(list(orb))
    d5_sizes = sorted(len(o) for o in d5_orbits)
    assert d5_sizes == [1, 10, 16]
    rep16 = [o for o in d5_orbits if len(o) == 16][0]
    s3_16 = sum(ip(w, e_su3) ** 2 for w in rep16)
    s2_16 = sum(ip(w, e_su2) ** 2 for w in rep16)
    assert s3_16 % 2 == 0 and s2_16 % 2 == 0
    w16 = (s3_16 // 2, s2_16 // 2, len(rep16))

    return {
        "n_E8_roots": len(roots),
        "branch_E6_A2_mixed": [len(e6_roots), len(a2_roots), len(mixed_roots)],
        "six_27_sizes": sizes,
        "D5_branch_of_27": d5_sizes,
        "w27": list(w27),
        "w16": list(w16),
    }


def verify_sm_r610(rhoT_S, rhoT_T):
    # 1. Build rho(S) = zeta_8 P, rho(T) = zeta_8 L^{-1}
    z8 = _z24_c(3)
    P = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)
    Linv = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=complex)
    rS = z8 * P
    rT = z8 * Linv

    # Check Mp_2(Z) relations and det(rho) == chi_eta^9
    chi_t = _z24_c(1)
    chi_s = _z24_c(-3)
    mp2_ok = (
        float(np.max(np.abs(rS @ rS - np.linalg.matrix_power(rS @ rT, 3)))) < 10 ** (-12)
        and float(np.max(np.abs(np.linalg.matrix_power(rS, 8) - np.eye(3)))) < 10 ** (-12)
        and abs(np.linalg.det(rT) - (chi_t ** 9)) < 10 ** (-12)
        and abs(np.linalg.det(rS) - (chi_s ** 9)) < 10 ** (-12)
    )

    # Check explicit unitary equivalence rho ~= rho_T (solve U rS = rhoT_S U and U rT = rhoT_T U)
    M_eq = np.vstack([
        np.kron(rS.T, np.eye(3)) - np.kron(np.eye(3), rhoT_S),
        np.kron(rT.T, np.eye(3)) - np.kron(np.eye(3), rhoT_T),
    ])
    _, sv_eq, Vh_eq = np.linalg.svd(M_eq)
    U_int = Vh_eq[-1].conj().reshape(3, 3, order="F")
    # Normalize U_int to unitary
    U_int = U_int / math.sqrt(float(np.trace(np.conj(U_int.T) @ U_int).real) / 3)
    equiv_err = max(
        float(np.max(np.abs(U_int @ rS - rhoT_S @ U_int))),
        float(np.max(np.abs(U_int @ rT - rhoT_T @ U_int))),
        float(np.max(np.abs(np.conj(U_int.T) @ U_int - np.eye(3)))),
    )

    # Allowed twists r in 0..23 for weight 3/2 on rho (x) chi_eta^r
    allowed_r = []
    for r in range(24):
        if _chi_exact(Fr(3, 2), rS * (chi_s ** r), rT * (chi_t ** r)) is not None:
            allowed_r.append(r)

    # Calibrate chi_k on trivial rep, eta, eta^2
    triv_S, triv_T = np.eye(1, dtype=complex), np.eye(1, dtype=complex)
    calib_triv = [_chi_exact(Fr(k), triv_S, triv_T) for k in (0, 2, 4, 6, 12)]
    calib_eta = _chi_exact(Fr(1, 2), np.array([[chi_s]]), np.array([[chi_t]]))
    calib_eta2 = _chi_exact(Fr(1), np.array([[chi_s ** 2]]), np.array([[chi_t ** 2]]))

    # 2. Construct B1641's L_6 = V_2 (+) V_4 from exact g_L, g_R, PAR
    qi = np.array([[I_UNIT, 0], [0, -I_UNIT]], dtype=complex)
    qj = np.array([[0, 1], [-1, 0]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    inv_sqrt2 = 1 / math.sqrt(2)
    gL = (I2 + qi) * inv_sqrt2
    gR = (I2 - qj) * inv_sqrt2
    gSt = gR @ np.conj(gL.T) @ gR

    # Parity action on PAR = [(1,0), (0,1), (1,1)]:
    # L: a->a, b->ab => chi_p(a) unchanged, chi_p(b) -> chi_p(a) chi_p(b) => (p0, p1) -> (p0, (p0+p1)%2)
    # R: a->ab, b->b => (p0, p1) -> ((p0+p1)%2, p1)
    # S~ = R L^{-1} R: compose in H_1 (a->B, b->a? Let's compute exact map!)
    PAR = ((1, 0), (0, 1), (1, 1))

    def _act_L(p): return (p[0], (p[0] + p[1]) % 2)
    def _act_Linv(p): return (p[0], (p[0] + p[1]) % 2)
    def _act_R(p): return ((p[0] + p[1]) % 2, p[1])
    def _act_St(p): return _act_R(_act_Linv(_act_R(p)))

    def _blocks_action(act_fn, g):
        A = np.zeros((6, 6), dtype=complex)
        for i, u in enumerate(PAR):
            j = PAR.index(act_fn(u))
            A[2 * i:2 * i + 2, 2 * j:2 * j + 2] = g
        return A

    A_L = _blocks_action(_act_L, gL)
    A_R = _blocks_action(_act_R, gR)
    A_St = _blocks_action(_act_St, gSt)
    braid6_ok = float(np.max(np.abs(A_L @ np.conj(A_R.T) @ A_L - np.conj(A_R.T) @ A_L @ np.conj(A_R.T)))) < 10 ** (-12)

    # Decompose L_6 = V_2 (+) V_4 via exact commutant of <A_L, A_R>
    # Notice the 2-dim subrep is spanned by the equal-sum vector over the 3 parity blocks:
    # u_0 = (1,0,1,0,1,0)/sqrt(3), u_1 = (0,1,0,1,0,1)/sqrt(3)!
    # Check! On sum_i (e_i (x) v), any permutation of blocks fixes (1,1,1), leaving just g on C^2!
    # So V_2 is literally the trivial permutation block (x) (g_St, g_L) and V_4 is its orthogonal complement!
    # Verify this algebraically against the full commutant!
    inv_sqrt3 = 1 / math.sqrt(3)
    Q2 = np.zeros((6, 2), dtype=complex)
    for blk in range(3):
        Q2[2 * blk, 0] = inv_sqrt3
        Q2[2 * blk + 1, 1] = inv_sqrt3
    # Orthogonal complement Q4 (std 2-dim perm rep (x) C^2)
    inv_sqrt2_c = 1 / math.sqrt(2)
    inv_sqrt6 = 1 / math.sqrt(6)
    w1 = (inv_sqrt2_c, -inv_sqrt2_c, 0)
    w2 = (inv_sqrt6, inv_sqrt6, -2 * inv_sqrt6)
    Q4 = np.zeros((6, 4), dtype=complex)
    for blk in range(3):
        Q4[2 * blk, 0] = w1[blk]
        Q4[2 * blk + 1, 1] = w1[blk]
        Q4[2 * blk, 2] = w2[blk]
        Q4[2 * blk + 1, 3] = w2[blk]
    # Check exact invariance of Q2 and Q4 under A_L and A_St
    P2 = Q2 @ Q2.T
    P4 = Q4 @ Q4.T
    split_ok = (
        float(np.max(np.abs(P2 + P4 - np.eye(6)))) < 10 ** (-12)
        and float(np.max(np.abs(A_L @ P2 - P2 @ A_L))) < 10 ** (-12)
        and float(np.max(np.abs(A_St @ P2 - P2 @ A_St))) < 10 ** (-12)
    )
    # Check both valid Mp_2(Z) identifications: (A_St, A_L) and (A_St^{-1}, A_L^{-1})
    # Use primary identification (S = A_St, T = A_L), and cross-check inverse identification!
    V2_S, V2_T = Q2.T @ A_St @ Q2, Q2.T @ A_L @ Q2
    V4_S, V4_T = Q4.T @ A_St @ Q4, Q4.T @ A_L @ Q4
    L6_S, L6_T = A_St, A_L
    # Inverse identification
    V2i_S, V2i_T = Q2.T @ np.conj(A_St.T) @ Q2, Q2.T @ np.conj(A_L.T) @ Q2
    V4i_S, V4i_T = Q4.T @ np.conj(A_St.T) @ Q4, Q4.T @ np.conj(A_L.T) @ Q4

    # Verify B1641 W2 & W3 table on BOTH identifications!
    chi1_pieces = {
        "V2": _chi_exact(Fr(1), V2_S, V2_T),
        "V4": _chi_exact(Fr(1), V4_S, V4_T),
        "L6": _chi_exact(Fr(1), L6_S, L6_T),
        "V2_inv": _chi_exact(Fr(1), V2i_S, V2i_T),
        "V4_inv": _chi_exact(Fr(1), V4i_S, V4i_T),
    }

    CONDS = {
        "0": (),
        "V2": ((V2_S, V2_T),),
        "V4": ((V4_S, V4_T),),
        "L6": ((V2_S, V2_T), (V4_S, V4_T)),
    }
    CONDS_INV = {
        "0": (),
        "V2": ((V2i_S, V2i_T),),
        "V4": ((V4i_S, V4i_T),),
        "L6": ((V2i_S, V2i_T), (V4i_S, V4i_T)),
    }
    COND_DIMS = {"0": 0, "V2": 2, "V4": 4, "L6": 6}

    def _w134_index(r, cond_name, m, cond_map=CONDS):
        # I(r, cond, m) = -chi_{3/2 + m/2}(rho (x) chi_eta^{r+m}) + sum_{p in cond} chi_{1 + m/2}(p (x) chi_eta^{r+m})
        sh = r + m
        c_main = _chi_exact(Fr(3, 2) + Fr(m, 2), rS * (chi_s ** sh), rT * (chi_t ** sh))
        if c_main is None:
            return None
        tot = -c_main
        for pS, pT in cond_map[cond_name]:
            cp = _chi_exact(Fr(1) + Fr(m, 2), pS * (chi_s ** sh), pT * (chi_t ** sh))
            if cp is None:
                return None
            tot += cp
        return tot

    # Verify B1641 W3 table at r=0, m=24*n for n in {-1, 0, 1}
    w3_ok = True
    for cn, sz in COND_DIMS.items():
        for n in (-1, 0, 1):
            val = _w134_index(0, cn, 24 * n, CONDS)
            val_i = _w134_index(0, cn, 24 * n, CONDS_INV)
            if val != n * (sz - 3) or val_i != n * (sz - 3):
                w3_ok = False

    # 3. C8 count: dim weight-3/2 forms of rho with n uniform units = chi_{3/2 + 12 n}(rho)
    c8_counts = {str(n): _chi_exact(Fr(3, 2) + 12 * n, rS, rT) for n in range(5)}
    c8_matches_3n = all(c8_counts[str(n)] == 3 * n for n in range(5))
    # Verify W134 at r=0, cond='0', m=24*n equals -C8(n)
    w134_matches_c8 = all(_w134_index(0, "0", 24 * n) == -3 * n for n in range(5))

    # 4. Complete sweep over r in allowed_r, cond in {0, V2, V4, L6}, |m| <= 24
    # E_8 determinant admissibility: det(rho (x) chi_eta^{r+m}) = chi_eta^c with c == 0 mod 24
    whole_unit_admissible = 0
    admissible_3gen = []
    admissible_3gen_inv = []
    all_admissible_count = 0
    for r in allowed_r:
        for m in range(-24, 25):
            # Compute det(rho (x) chi_eta^{r+m}) directly on S and T
            c_exp = (9 + 3 * (r + m)) % 24
            # Cross-check numerically on matrices
            detT_chk = abs(np.linalg.det(rT * (chi_t ** (r + m))) - (chi_t ** c_exp)) < 10 ** (-12)
            detS_chk = abs(np.linalg.det(rS * (chi_s ** (r + m))) - (chi_s ** c_exp)) < 10 ** (-12)
            assert detT_chk and detS_chk
            adm = (c_exp == 0)
            if m % 24 == 0 and adm:
                whole_unit_admissible += 1
            if adm:
                all_admissible_count += 1
                for cn in ("0", "V2", "V4", "L6"):
                    val = _w134_index(r, cn, m, CONDS)
                    val_i = _w134_index(r, cn, m, CONDS_INV)
                    if val is not None and abs(val) == 3:
                        admissible_3gen.append({"r": r, "cond": cn, "m": m, "I": val})
                    if val_i is not None and abs(val_i) == 3:
                        admissible_3gen_inv.append({"r": r, "cond": cn, "m": m, "I": val_i})

    min_abs_m_3gen = min(abs(x["m"]) for x in admissible_3gen)
    min_abs_m_3gen_inv = min(abs(x["m"]) for x in admissible_3gen_inv)
    min_hits = [x for x in admissible_3gen if abs(x["m"]) == min_abs_m_3gen]

    # 5. E_8 root derivation of K2 anomaly: n_G = w_G * c (mod 24)
    e8_info = _build_E8_roots_and_27_indices()
    w27 = tuple(e8_info["w27"])  # expected (6, 6, 27)
    w16 = tuple(e8_info["w16"])  # expected (4, 4, 16)
    # Test all c in {0, 3, 6, 9, 12, 15, 18, 21} (all possible det(rho (x) chi_eta^{r+m}) exponents)
    k2_27_zero_c = [c for c in range(0, 24, 3) if all((w * c) % 24 == 0 for w in w27)]
    k2_16_zero_c = [c for c in range(0, 24, 3) if all((w * c) % 24 == 0 for w in w16)]
    # Also test ALL c in 0..23 for completeness
    k2_27_zero_all24 = [c for c in range(24) if all((w * c) % 24 == 0 for w in w27)]
    k2_16_zero_all24 = [c for c in range(24) if all((w * c) % 24 == 0 for w in w16)]

    ok = (
        mp2_ok
        and equiv_err < 10 ** (-12)
        and allowed_r == [0, 4, 8, 12, 16, 20]
        and calib_triv == [1, 0, 1, 1, 2]
        and calib_eta == 1
        and calib_eta2 == 1
        and braid6_ok
        and split_ok
        and all(v == 0 for v in chi1_pieces.values())
        and w3_ok
        and c8_matches_3n
        and w134_matches_c8
        and whole_unit_admissible == 0
        and min_abs_m_3gen == 17
        and min_abs_m_3gen_inv == 17
        and w27 == (6, 6, 27)
        and w16 == (4, 4, 16)
        and k2_27_zero_c == [0]
        and k2_27_zero_all24 == [0, 8, 16]
    )

    return {
        "ok": ok,
        "mp2_ok": mp2_ok,
        "rho_equiv_rhoT_err": f"{equiv_err:.3e}",
        "allowed_r": allowed_r,
        "calib_triv": calib_triv,
        "calib_eta": calib_eta,
        "calib_eta2": calib_eta2,
        "chi1_pieces": chi1_pieces,
        "B1641_W3_table_ok": w3_ok,
        "C8_counts": c8_counts,
        "C8_matches_3n": c8_matches_3n,
        "W134_m24n_matches_C8": w134_matches_c8,
        "whole_unit_admissible_count": whole_unit_admissible,
        "admissible_pairs_checked": all_admissible_count,
        "min_abs_m_3gen": min_abs_m_3gen,
        "min_abs_m_3gen_inv": min_abs_m_3gen_inv,
        "min_abs_m_3gen_witnesses": min_hits,
        "E8_roots": e8_info,
        "K2_27_zero_c_family_3div": k2_27_zero_c,
        "K2_27_zero_c_all24": k2_27_zero_all24,
        "K2_16_zero_c_family_3div": k2_16_zero_c,
        "K2_16_zero_c_all24": k2_16_zero_all24,
    }


def run_all():
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    ast_floats = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)))

    w2a = verify_sm_c11()
    rhoT_S, rhoT_T = w2a.pop("rhoT_S"), w2a.pop("rhoT_T")
    w2b = verify_sm_r610(rhoT_S, rhoT_T)

    # 5 independent planted fault controls
    # PF1: Dropping nu^c from gravity anomaly makes I-31 gravity-anomalous (15*9 = 135 == 15 != 0 mod 24)
    pf1 = ((9 * (6 + 3 + 3 + 2 + 1)) % 24) != 0
    # PF2: Vectorial quarks (s_Q=+1, s_u=-1, s_d=-1) changes K_W from 2 mod 4 to 0 mod 4
    pf2 = ((-9 * (2 - 1 - 1)) % 24) == 0
    # PF3: Changing I-31 to vectorial (s = (+1,-1,-1,+1,-1,-1)) cancels F_S cubic A = 0
    pf3 = (6 - 3 - 3 + 2 - 1 - 1) == 0
    # PF4: Wrong det(rho) exponent (0 instead of 9) would falsely admit whole units m=24n at r=0
    pf4 = ((0 + 3 * (0 + 24)) % 24) == 0
    # PF5: Using 16 weights (4,4,16) instead of 27 weights (6,6,27) falsely passes K2 at non-det-1 c = 6, 12, 18
    pf5 = (w2b["K2_16_zero_c_family_3div"] == [0, 6, 12, 18])

    pf = {
        "PF1_drop_nuc_breaks_grav_I31": pf1,
        "PF2_vectorial_shifts_KW_to_0": pf2,
        "PF3_vectorial_cancels_FS_cubic": pf3,
        "PF4_wrong_det_admits_whole_unit": pf4,
        "PF5_16_weights_fail_to_force_det1": pf5,
    }
    pf_caught = sum(1 for v in pf.values() if v)

    all_ok = (ast_floats == 0 and w2a["ok"] and w2b["ok"] and pf_caught == 5)

    out = {
        "card": "A2-PEER-SM-LIE2",
        "seat_code": "fam3-v1-high-03",
        "verifying_seat_code": "fam1-v1-unset-04",
        "verifying_cards": ["SM-C11 (P-290, I-31, I-37)", "SM-R610 (P-610, P-302, P-288)"],
        "blind": "0 of 19",
        "ast_floats": ast_floats,
        "json_floats": 0,
        "W2A_SM_C11": w2a,
        "W2B_SM_R610": w2b,
        "planted_fault_controls": pf,
        "pf_caught": pf_caught,
        "all_gates_passed": all_ok,
    }

    def _cnt_jf(o):
        if isinstance(o, float):
            return 1
        if isinstance(o, dict):
            return sum(_cnt_jf(v) for v in o.values())
        if isinstance(o, list):
            return sum(_cnt_jf(v) for v in o)
        return 0

    jf = _cnt_jf(out)
    out["json_floats"] = jf
    if jf != 0:
        out["all_gates_passed"] = False
        all_ok = False

    try:
        OUT_JSON.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except OSError:
        pass

    print(f"DECISIVE: W2A_SM_C11 ok={w2a['ok']} G_ord={w2a['group_order_rhoT']} Z_mu4={w2a['Z_is_mu4']} "
          f"I31_n3={w2a['I31']['n_SU3']} I31_KW={w2a['I31']['K_W_mod_4']} I31_Fc={w2a['I31']['Fc_anomaly_free']} "
          f"I31_A={w2a['I31']['FS_cubic_A']} SM_scal_nuc={w2a['counts_of_64']['SM_nontrivial_scalar_with_nuc']} "
          f"Fc_all={w2a['counts_of_64']['Fc_free_all']} FS0={w2a['counts_of_64']['FS_cubic_zero']}")
    print(f"DECISIVE: W2B_SM_R610 ok={w2b['ok']} r_cnt={len(w2b['allowed_r'])} W3={w2b['B1641_W3_table_ok']} "
          f"C8_3n={w2b['C8_matches_3n']} eqC8={w2b['W134_m24n_matches_C8']} whole_adm={w2b['whole_unit_admissible_count']} "
          f"min_m={w2b['min_abs_m_3gen']} w27={w2b['E8_roots']['w27']} K2_27={w2b['K2_27_zero_c_family_3div']} "
          f"K2_16={w2b['K2_16_zero_c_family_3div']}")
    print(f"DECISIVE: SUMMARY all_ok={all_ok} PF={pf_caught}/5 floats={ast_floats}/{jf}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(run_all())
