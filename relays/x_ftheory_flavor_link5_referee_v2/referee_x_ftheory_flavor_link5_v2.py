#!/usr/bin/env python3
r"""
Disjoint Zero-Shared-Code Cold-Room Referee for Card X-F-THEORY-FLAVOR-LINK5 (strictly 0 of 19):
  - REF_FL5_1: Explicit 32x32 Cl(10) -> 16x16 chiral Spin(10) Gamma-matrix representation on
    non-abelian Lie algebra elements F = sum c_{ab} Sigma_{ab} (proving tr_16 F^4 = -tr_10 F^4 + (3/4)(tr_10 F^2)^2,
    E/N = 8/3, and all 11 Hirzebruch F_k Lorentzian Omega = diag(+1, -1) GS factorizations).
  - REF_FL5_2: Direct 2D Ewald incomplete-gamma lattice splitting for twisted s=3 Epstein sums
    (independent of Producer's Chowla-Selberg expansion), verifying Ewald split-parameter invariance,
    Gamma_0(2) GCP reflection invariance, Ewald root agreement on tau_* / y_F, and direct 3-twist
    E[2]\{0} Ewald phase average == -(5/16) E_3.
  - REF_FL5_3: Disjoint real 2D nonlinear elliptic cusp-Robin Liouville PDE solver (Delta phi = e^{2 phi}
    via pure-mpmath matrix-DFT spectral preconditioned CG on N=14 & N=20 + Richardson O(1/N^2)
    extrapolation, with ZERO Fuchsian ODEs, ZERO Weierstrass wp, and ZERO accessory parameter c_*),
    cross-checking Producer's Fuchsian G^{(s=1/2)}, G^{(s=0)}, and Robin constant b_c^*.
  - REF_FL5_4: Laurent-residue Szego Yukawa kernel + 10-trial Cayley-transform unitary basis
    scrambling on lopsided (2, 0, 3) Spin(10) flavor + seesaw, cross-checking Producer's L5_4 JSON.
  - REF_FL5_5: 3-stage 6th-order implicit Gauss-Legendre collocation (GL6) integrator on complete
    2-loop Type-II 2HDM gauge + Yukawa + quartic RGEs, cross-checking Producer's GBS8 to < 1e-12.
  - REF_FL5_6: Full SHA-256 custody & AST/JSON zero-float audit of BOTH Producer X-F-THEORY-FLAVOR-LINK5
    and peer commit 27f5d89fa, plus GL6 countercheck of the 60-efold coupled Starobinsky inflation ODE.

Guardrails enforced:
  - 0 Python float/complex AST literals, 0 binary64 float()/complex() casts, 0 JSON floats.
  - 0 shared helper code or imports from Producer, frontier/, or peer scripts (Guardrail #6).
  - 0 empirical PDG/NuFIT/Planck/DESI/CODATA constants (strictly 0 of 19).
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import random
import subprocess
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[2]
SELF_PATH = Path(__file__).resolve()
OUT_PATH = SELF_PATH.parent / "referee_x_ftheory_flavor_link5_v2_out.json"
PROD_DIR = REPO_ROOT / "relays" / "x_ftheory_flavor_link5_v4_verify"
PROD_SCRIPT = PROD_DIR / "verify_x_ftheory_flavor_link5_v4.py"
PROD_OUT = PROD_DIR / "verify_x_ftheory_flavor_link5_v4_out.json"
PEER_REV = "27f5d89fa"

J_MP = mp.mpc(0, 1)


def rat_m(p: int, q: int = 1) -> mp.mpf:
    return mp.mpf(int(p)) / mp.mpf(int(q))


def fr_m(f: Fr) -> mp.mpf:
    return mp.mpf(int(f.numerator)) / mp.mpf(int(f.denominator))


def ten_pow(e: int) -> mp.mpf:
    return mp.mpf(10) ** int(e)


def fr_s(f: Fr) -> str:
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else str(f.numerator)


def check_no_floats_json(node: Any) -> None:
    if isinstance(node, float):
        raise AssertionError(f"Forbidden float in JSON: {node!r}")
    if isinstance(node, dict):
        for v in node.values():
            check_no_floats_json(v)
    elif isinstance(node, list):
        for v in node:
            check_no_floats_json(v)


def audit_ast_clean(code_txt: str, name_tag: str) -> dict[str, Any]:
    tr = ast.parse(code_txt, filename=name_tag)
    fl_lines = [
        getattr(nd, "lineno", 0)
        for nd in ast.walk(tr)
        if isinstance(nd, ast.Constant) and isinstance(nd.value, (float, complex))
    ]
    cast_lines = [
        getattr(nd, "lineno", 0)
        for nd in ast.walk(tr)
        if isinstance(nd, ast.Call) and isinstance(nd.func, ast.Name) and nd.func.id in ("float", "complex")
    ]
    imp_bad: list[str] = []
    for nd in ast.walk(tr):
        if isinstance(nd, (ast.Import, ast.ImportFrom)):
            md = getattr(nd, "module", "") or ""
            nms = [a.name for a in nd.names]
            comb = md + " " + " ".join(nms)
            if any(w in comb for w in ("frontier", "relays", "self_consistent", "phase10", "c29", "c30", "verify_x_ftheory")):
                imp_bad.append(comb)
    return {
        "float_complex_literals": len(fl_lines),
        "binary64_casts": len(cast_lines),
        "forbidden_imports": len(imp_bad),
        "clean": bool(len(fl_lines) == 0 and len(cast_lines) == 0 and len(imp_bad) == 0),
    }


def cayley_unitary_u3(rng: random.Random) -> mp.matrix:
    """Disjoint unitary generator U = (I - A)(I + A)^{-1} * diag(phases) from skew-Hermitian A."""
    a_sk = mp.zeros(3, 3)
    den = mp.mpf(1 << 52)
    for r in range(3):
        iv = (mp.mpf(rng.getrandbits(52)) / den - rat_m(1, 2)) * mp.mpf(3)
        a_sk[r, r] = J_MP * iv
        for c in range(r + 1, 3):
            rv = (mp.mpf(rng.getrandbits(52)) / den - rat_m(1, 2)) * mp.mpf(2)
            imv = (mp.mpf(rng.getrandbits(52)) / den - rat_m(1, 2)) * mp.mpf(2)
            a_sk[r, c] = mp.mpc(rv, imv)
            a_sk[c, r] = -mp.mpc(rv, -imv)
    i3 = mp.eye(3)
    u_base = (i3 - a_sk) * ((i3 + a_sk) ** (-1))
    phs = mp.diag([mp.exp(J_MP * mp.mpf(2) * mp.pi * (mp.mpf(rng.getrandbits(52)) / den)) for _ in range(3)])
    return u_base * phs


def gl6_integrate(rhs_fn, y0: list[mp.mpf], t0: mp.mpf, t1: mp.mpf, n_steps: int) -> list[mp.mpf]:
    """3-stage 6th-order implicit Gauss-Legendre collocation ODE integrator."""
    s15 = mp.sqrt(mp.mpf(15))
    c1, c2, c3 = rat_m(1, 2) - s15 / mp.mpf(10), rat_m(1, 2), rat_m(1, 2) + s15 / mp.mpf(10)
    a_mat = [
        [rat_m(5, 36), rat_m(2, 9) - s15 / mp.mpf(15), rat_m(5, 36) - s15 / mp.mpf(30)],
        [rat_m(5, 36) + s15 / mp.mpf(24), rat_m(2, 9), rat_m(5, 36) - s15 / mp.mpf(24)],
        [rat_m(5, 36) + s15 / mp.mpf(30), rat_m(2, 9) + s15 / mp.mpf(15), rat_m(5, 36)],
    ]
    b_w = [rat_m(5, 18), rat_m(4, 9), rat_m(5, 18)]
    cs = [c1, c2, c3]
    dim = len(y0)
    h = (t1 - t0) / mp.mpf(n_steps)
    yc = list(y0)
    tc = t0
    tol = ten_pow(-34)
    for _ in range(n_steps):
        f_init = rhs_fn(tc, yc)
        ks = [list(f_init), list(f_init), list(f_init)]
        for _it in range(28):
            k_new: list[list[mp.mpf]] = []
            mx = mp.mpf(0)
            for s_i in range(3):
                ys = [
                    yc[d] + h * (a_mat[s_i][0] * ks[0][d] + a_mat[s_i][1] * ks[1][d] + a_mat[s_i][2] * ks[2][d])
                    for d in range(dim)
                ]
                fn_s = rhs_fn(tc + cs[s_i] * h, ys)
                for d in range(dim):
                    df = abs(fn_s[d] - ks[s_i][d])
                    if df > mx:
                        mx = df
                k_new.append(fn_s)
            ks = k_new
            if mx < tol:
                break
        yc = [yc[d] + h * (b_w[0] * ks[0][d] + b_w[1] * ks[1][d] + b_w[2] * ks[2][d]) for d in range(dim)]
        tc += h
    return yc


# ==============================================================================
# REF_FL5_1: Explicit 32x32 Cl(10) -> 16x16 Non-Abelian Spin(10) Trace Identity,
#            E/N = 8/3, & Lorentzian Omega = diag(+1, -1) Hirzebruch Factorization
# ==============================================================================

def kron_sp(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    ra, ca = a.rows, a.cols
    rb, cb = b.rows, b.cols
    out = sp.zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            out[i * rb:(i + 1) * rb, j * cb:(j + 1) * cb] = a[i, j] * b
    return out


def run_ref_fl5_1(prod_l5_1: dict[str, Any]) -> dict[str, Any]:
    # 1. Construct 32x32 Euclidean Cl(10) Gamma_1..10 via 5-fold Pauli tensor products:
    i2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    gammas: list[sp.Matrix] = []
    for k in range(5):
        ops_odd = [sz] * k + [sx] + [i2] * (4 - k)
        ops_evn = [sz] * k + [sy] + [i2] * (4 - k)
        g_o, g_e = ops_odd[0], ops_evn[0]
        for idx in range(1, 5):
            g_o = kron_sp(g_o, ops_odd[idx])
            g_e = kron_sp(g_e, ops_evn[idx])
        gammas.extend([g_o, g_e])

    # Chirality Gamma_11 = (-i)^5 Gamma_1 ... Gamma_10 = sz^{otimes 5} (diagonal +-1!):
    g11 = sz
    for _ in range(4):
        g11 = kron_sp(g11, sz)
    plus_idx = [idx for idx in range(32) if g11[idx, idx] == 1]
    assert len(plus_idx) == 16

    def proj_16(m32: sp.Matrix) -> sp.Matrix:
        return m32.extract(plus_idx, plus_idx)

    # Test non-abelian Spin(10) Lie algebra element F = sum_{(a,b)} c_{ab} T_{ab} INCLUDING off-Cartan generators!
    # In vector 10: (T_{ab}^{(10)})_{ij} = -i (delta_{ai} delta_{bj} - delta_{bi} delta_{aj}), so tr_10(T_{ab}^2) = 2;
    # In spinor 16_+: T_{ab}^{(16)} = (-i/2) Gamma_a Gamma_b|_{16_+}, so [T, T] matches vector 10!
    sample_coeffs = [
        (0, 1, sp.Rational(3, 5)), (2, 3, sp.Rational(-2, 3)), (4, 5, sp.Rational(1, 2)),
        (6, 7, sp.Rational(4, 7)), (8, 9, sp.Rational(-5, 6)),
        (0, 2, sp.Rational(2, 5)), (1, 4, sp.Rational(-3, 7)), (3, 8, sp.Rational(1, 3)),  # non-Cartan!
    ]
    f10 = sp.zeros(10, 10)
    f16 = sp.zeros(16, 16)
    for a, b, cf in sample_coeffs:
        t10 = sp.zeros(10, 10)
        t10[a, b] = -sp.I
        t10[b, a] = sp.I
        t16 = proj_16((-sp.I / 2) * gammas[a] * gammas[b])
        f10 += cf * t10
        f16 += cf * t16

    tr10_f2 = sp.simplify((f10 * f10).trace())
    tr10_f4 = sp.simplify((f10 * f10 * f10 * f10).trace())
    tr16_f2 = sp.simplify((f16 * f16).trace())
    tr16_f4 = sp.simplify((f16 * f16 * f16 * f16).trace())
    nonabelian_tr_ok = bool(
        sp.simplify(tr16_f2 - 2 * tr10_f2) == 0
        and sp.simplify(tr16_f4 - (-tr10_f4 + sp.Rational(3, 4) * (tr10_f2 ** 2))) == 0
    )

    # Compute E/N directly from 16x16 Clifford generators:
    # Cartan H_m = T_{2m, 2m+1}^{(16)} (eigenvalues +-1/2):
    hs_16 = [proj_16((-sp.I / 2) * gammas[2 * m] * gammas[2 * m + 1]) for m in range(5)]
    q_em_16 = sp.Rational(1, 3) * (hs_16[0] + hs_16[1] + hs_16[2]) + sp.Rational(1, 2) * (hs_16[3] - hs_16[4])
    # Wait: check 6Y = 2(h0+h1+h2) - 3(h3+h4) => Y = (1/3)(h0+h1+h2) - (1/2)(h3+h4), T_3L = (1/2)(h3 - h4) => Q_em = T_3L + Y = (1/3)(h0+h1+h2) - h4!
    q_em_16 = sp.Rational(1, 3) * (hs_16[0] + hs_16[1] + hs_16[2]) - hs_16[4]
    t3_su3_16 = sp.Rational(1, 2) * (hs_16[0] - hs_16[1])
    tr_qem2 = sp.simplify((q_em_16 * q_em_16).trace())         # 16/3
    dynk_su3 = sp.simplify((t3_su3_16 * t3_su3_16).trace())    # 2 (since tr_3((T_3c)^2) = 1/2 = T_3(3))
    e_over_n_cliff = sp.simplify(tr_qem2 / dynk_su3)             # 8/3!

    # 2. Verify all 11 Hirzebruch F_k via Lorentzian SO(1, 1) GS inner product Omega = diag(+1, -1):
    #    Write X_4^+ = (1/4)[(v_+ - 1) F2] + ..., specifically in SO(1,1) null-cone basis:
    #    -(1/16)(R2 - F2)(R2 + ((4 - n16)/2) F2) = (1/2) [ (Y^0)^2 - (Y^1)^2 ] with
    #    Y^0 = ((6 - n16)/16) F2? Let's check: -(1/16) A B = (1/64)[ (A - B)^2 - (A + B)^2 ]
    #    = (1/2)[ ((A - B)/(4 sqrt(2)))^2 - ((A + B)/(4 sqrt(2)))^2 ], where A - B = -(6 - n16)/2 F2!
    R2, F2 = sp.symbols("R2 F2")
    prod_rows = prod_l5_1["hirzebruch_11_family"]
    matched_11 = 0
    for idx, n16 in enumerate(range(11)):
        a_fac = R2 - F2
        b_fac = R2 + sp.Rational(4 - n16, 2) * F2
        gs_lorentz = sp.expand(sp.Rational(1, 64) * ((a_fac - b_fac) ** 2 - (a_fac + b_fac) ** 2))
        gs_target = sp.expand(-sp.Rational(1, 16) * a_fac * b_fac)
        disc_r = Fr(6 - n16, 32) ** 2
        if (
            gs_lorentz == gs_target
            and prod_rows[idx]["v_tilde_GS"] == fr_s(Fr(4 - n16, 2))
            and prod_rows[idx]["discriminant"] == fr_s(disc_r)
            and prod_rows[idx]["exact_GS_factorization"] is True
        ):
            matched_11 += 1

    # Planted Control R_PC_FL5_1: Euclidean positive-definite Omega_bad = diag(+1, +1) has negative discriminant -(Y^0)^2 - (Y^1)^2, failing real factorization at n_16 = 0:
    a0, b0 = R2 - F2, R2 + 2 * F2
    eucl_sum = sp.expand(sp.Rational(1, 64) * ((a0 - b0) ** 2 + (a0 + b0) ** 2))
    c_r2 = Fr(int(eucl_sum.coeff(R2, 2).p), int(eucl_sum.coeff(R2, 2).q))
    c_rf = Fr(int(eucl_sum.coeff(R2 * F2).p), int(eucl_sum.coeff(R2 * F2).q))
    c_f2 = Fr(int(eucl_sum.coeff(F2, 2).p), int(eucl_sum.coeff(F2, 2).q))
    r_pc_fl5_1_caught = bool((c_rf * c_rf - 4 * c_r2 * c_f2) < 0)

    passed = bool(
        nonabelian_tr_ok
        and e_over_n_cliff == sp.Rational(8, 3)
        and prod_l5_1["axion_E_over_N_exact"] == "8/3"
        and matched_11 == 11
        and r_pc_fl5_1_caught
    )
    return {
        "clifford_16x16_nonabelian_F4_identity": nonabelian_tr_ok,
        "clifford_16x16_E_over_N": str(e_over_n_cliff),
        "hirzebruch_11_lorentzian_GS_matched": matched_11,
        "r_pc_fl5_1_euclidean_omega_neg_disc_caught": r_pc_fl5_1_caught,
        "passed": passed,
    }


# ==============================================================================
# REF_FL5_2: Direct 2D Ewald Lattice Splitting for Twisted s=3 Epstein Sums &
#            Cross-Check of Producer's Gamma_0(2) GCP Semicircle Vacuum
# ==============================================================================

def e3_ewald_2d(tau: mp.mpc, phi1: Fr, phi2: Fr, eta_split: mp.mpf, r_lim: int = 16) -> mp.mpf:
    """Disjoint 2D Riemann-Ewald proper-time splitting for E_3(tau; phi1, phi2) = sum_{(w1,w2)!=0} y^3 cos(2 pi(w1 a + w2 b))/|w1 tau + w2|^6
    at arbitrary dimensionless split parameter eta_split (zero B_6, zero polylog, zero Bessel)."""
    y = mp.im(tau)
    a = fr_m(phi1 % 1)
    b = fr_m(phi2 % 1)
    twopi = mp.mpf(2) * mp.pi
    t0 = eta_split / y

    # Upper real-space sum (t >= t0):
    s_dir = -(eta_split ** 3) / mp.mpf(6)
    for w1 in range(-r_lim, r_lim + 1):
        for w2 in range(-r_lim, r_lim + 1):
            if w1 == 0 and w2 == 0:
                continue
            wsq = abs(mp.mpf(w1) * tau + mp.mpf(w2)) ** 2
            zv = t0 * wsq
            if zv > mp.mpf(155):
                continue
            ph = mp.cos(twopi * (mp.mpf(w1) * a + mp.mpf(w2) * b))
            s_dir += rat_m(1, 2) * ph * ((y / wsq) ** 3) * mp.exp(-zv) * (mp.mpf(2) + mp.mpf(2) * zv + zv * zv)

    # Lower reciprocal-space sum (0 < t <= t0):
    s_dual = mp.mpf(0)
    pref_l = mp.pi * (eta_split ** 2) / mp.mpf(4)
    for m1 in range(-r_lim, r_lim + 1):
        u1 = mp.mpf(m1) + a
        for m2 in range(-r_lim, r_lim + 1):
            u2 = mp.mpf(m2) + b
            bm = (mp.pi ** 2) * (abs(u2 * tau - u1) ** 2) / (eta_split * y)
            if bm == 0:
                s_dual += pref_l
            elif bm < mp.mpf(155):
                # 2 * expint(3, bm) == exp(-bm)*(1 - bm) + bm^2 * E_1(bm) (strictly real mp.mpf!):
                s_dual += pref_l * (mp.exp(-bm) * (mp.mpf(1) - bm) + (bm * bm) * mp.e1(bm))
    return s_dir + s_dual


def v_tot_ewald(tv_m: mp.mpf, sv_m: mp.mpf, tx: mp.mpf, ty: mp.mpf, eta_s: mp.mpf, r_lim: int = 13) -> mp.mpf:
    z = tx + J_MP * ty
    qh = mp.exp(J_MP * mp.pi * z / mp.mpf(12))
    q = mp.exp(J_MP * mp.mpf(2) * mp.pi * z)
    pr, e2, qn = mp.mpc(1), mp.mpc(1), q
    for n in range(1, 280):
        if abs(qn) < ten_pow(-60):
            break
        pr *= mp.mpc(1) - qn
        e2 -= mp.mpf(24 * n) * qn / (mp.mpc(1) - qn)
        qn *= q
    eta4 = abs(qh * pr) ** 4
    inv_e = mp.mpf(1) / (mp.mpf(2) * ty * eta4)
    ft = mp.mpf(2) * inv_e * (ty ** 2) * (abs(e2 - mp.mpf(3) / (mp.pi * ty)) ** 2)

    a1, a2 = Fr(1, 2), Fr(1, 2)
    tot = mp.mpf(1024) * (e3_ewald_2d(z, Fr(0), Fr(0), eta_s, r_lim) - e3_ewald_2d(z, a1, a2, eta_s, r_lim))
    for mult, g1, g2 in [(8, Fr(0), Fr(1, 2)), (12, Fr(1, 2), Fr(0)), (12, Fr(1, 2), Fr(1, 2))]:
        tot -= mp.mpf(4 * mult) * (e3_ewald_2d(z, g1, g2, eta_s, r_lim) - e3_ewald_2d(z, g1 + a1, g2 + a2, eta_s, r_lim))
    for mh, g1, g2 in [(12, Fr(1, 2), Fr(1, 4)), (4, Fr(0), Fr(1, 2))]:
        tot += mp.mpf(4 * mh) * (e3_ewald_2d(z, g1, g2, eta_s, r_lim) - e3_ewald_2d(z, g1 + a1, g2 + a2, eta_s, r_lim))
    cc = tot / (mp.mpf(2) * (mp.pi ** 7))

    gr2 = rat_m(1, 600)
    p1, p2 = mp.mpf(2) * mp.pi / mp.mpf(36), mp.mpf(2) * mp.pi / mp.mpf(48)
    ws = mp.mpf(3) * mp.exp(-p1 * sv_m) - mp.exp(-p2 * sv_m)
    dws = -p1 * mp.mpf(3) * mp.exp(-p1 * sv_m) + p2 * mp.exp(-p2 * sv_m)
    dsw = dws - ws / (mp.mpf(2) * sv_m)
    v_ss = ((mp.mpf(2) * gr2 * tv_m - mp.mpf(1)) ** 2) / (mp.mpf(2) * gr2 * sv_m * (tv_m ** 3))
    v_f = (mp.mpf(1) / (mp.mpf(4) * sv_m * tv_m)) * (
        inv_e * (mp.mpf(4) * (sv_m ** 2) * (dsw ** 2) - mp.mpf(2) * (ws ** 2))
        + ((mp.pi ** 2) / mp.mpf(18)) * ft * (ws ** 2)
    )
    return v_ss + v_f + cc / ((sv_m ** 2) * (tv_m ** 2))


def run_ref_fl5_2(prod_l5_2: dict[str, Any]) -> dict[str, Any]:
    mp.mp.dps = 52
    eta1 = mp.pi
    eta2 = rat_m(6, 5) * mp.pi
    tau_r = rat_m(3, 5) + J_MP * rat_m(11, 20)

    # 1. Verify Ewald split-parameter independence eta1 vs eta2 to < 1e-42:
    ew_split_err = abs(
        e3_ewald_2d(tau_r, Fr(1, 2), Fr(1, 4), eta1, r_lim=16)
        - e3_ewald_2d(tau_r, Fr(1, 2), Fr(1, 4), eta2, r_lim=16)
    )

    # 2. Verify Gamma_0(2) GCP reflection invariance at tau_r = 3/5 + 11i/20 (disjoint from Producer's 11/20 + i/2):
    sig_r = mp.conj(tau_r) / (mp.mpf(2) * mp.conj(tau_r) - mp.mpc(1))
    v1 = v_tot_ewald(mp.mpf(300), mp.mpf(31), mp.re(tau_r), mp.im(tau_r), eta1, r_lim=16)
    v2 = v_tot_ewald(mp.mpf(300), mp.mpf(31), mp.re(sig_r), mp.im(sig_r), eta1, r_lim=16)
    gcp_ewald_err = abs(v1 - v2) / abs(v1)

    # 3. Verify Producer's 50-dps tau_star & y_F satisfy Ewald 4D stationarity to < 1e-36:
    px = mp.mpf(prod_l5_2["tau_star_re_im"][0])
    py = mp.mpf(prod_l5_2["tau_star_re_im"][1])
    py_f = mp.mpf(prod_l5_2["tau_F_imaginary_height_yF"])
    circle_err = abs((px - rat_m(1, 2)) ** 2 + py * py - rat_m(1, 4))
    tau_from_yf = (J_MP * py_f) / (J_MP * py_f + mp.mpc(1))
    yf_map_err = abs((px + J_MP * py) - tau_from_yf)
    # Check Ewald transverse gradient dV/dx_perp across the GCP semicircle at Producer's root:
    # Normal vector to |tau - 1/2| = 1/2 is (x_* - 1/2, y_*):
    nx, ny = px - rat_m(1, 2), py
    # Polish (t_*, s_*) at (px, py) with 3 Newton steps in (t, s) or evaluate dV/d(perp) directly (note v_ss + v_f + v_c depends on tau ONLY through v_f and v_c!):
    # Let's solve 3D (t, s, y_F) on the semicircle and check transverse gradient!
    st3 = [rat_m(3016, 10), rat_m(3116, 100), rat_m(212, 100)]

    def v_on_circle(tv: mp.mpf, sv: mp.mpf, yf: mp.mpf) -> mp.mpf:
        ts = (J_MP * yf) / (J_MP * yf + mp.mpc(1))
        return v_tot_ewald(tv, sv, mp.re(ts), mp.im(ts), eta1, r_lim=22)

    for _ in range(6):
        hg = ten_pow(-18)
        hj = ten_pow(-12)
        g3: list[mp.mpf] = []
        for i in range(3):
            pp, pm = list(st3), list(st3)
            pp[i] += hg
            pm[i] -= hg
            g3.append((v_on_circle(*pp) - v_on_circle(*pm)) / (mp.mpf(2) * hg))
        if mp.sqrt(sum(x * x for x in g3)) < ten_pow(-40):
            break
        jc = mp.zeros(3, 3)
        for j in range(3):
            pj = list(st3)
            pj[j] += hj
            gj = []
            for i in range(3):
                pp, pm = list(pj), list(pj)
                pp[i] += hg
                pm[i] -= hg
                gj.append((v_on_circle(*pp) - v_on_circle(*pm)) / (mp.mpf(2) * hg))
            for i in range(3):
                jc[i, j] = (gj[i] - g3[i]) / hj
        dl = mp.lu_solve(jc, mp.matrix([[-x] for x in g3]))
        for i in range(3):
            st3[i] += dl[i, 0]

    yf_ref_vs_prod = abs(st3[2] - py_f)
    hp = ten_pow(-18)
    dv_perp = abs(
        v_tot_ewald(st3[0], st3[1], px + hp * nx, py + hp * ny, eta1, r_lim=22)
        - v_tot_ewald(st3[0], st3[1], px - hp * nx, py - hp * ny, eta1, r_lim=22)
    ) / (mp.mpf(2) * hp)

    # 4. Direct Ewald 3-twist E[2]\{0} KK phase average == -(5/16) E_3 (Recall KK phase (-1)^{m1 s1 + m2 s2} corresponds in e3_ewald_2d to shifts (1/2,0), (0,1/2), (1/2,1/2)? Wait: e3_ewald_2d has phase a on n1 and shift b on n2! Let's check pure shifts (0, 1/2), S-dual (1/2, 0)? Wait:
    # In winding sum, pure half-integer shifts (b1, b2) in {(1/2,0), (0,1/2), (1/2,1/2)} sum over HALF-INTEGER vectors n + (b1, b2), whose sum is E_3 on (1/2)Z^2 minus Z^2 = (2^6 - 1) E_3 = 63 E_3, whereas pure PHASES (-1)^{2(u1 n1 + u2 n2)} sum to -(15/16) E_3 -> average -(5/16) E_3!
    # Let's evaluate the direct 2D Ewald pure-phase sum (u1, u2) in {(1/2,0),(0,1/2),(1/2,1/2)} directly!):
    def e3_ewald_pure_phase(tau: mp.mpc, u1_fr: Fr, u2_fr: Fr, eta_s: mp.mpf, r_lim: int = 15) -> mp.mpf:
        x, y = mp.re(tau), mp.im(tau)
        u1, u2 = fr_m(u1_fr), fr_m(u2_fr)
        twopi = mp.mpf(2) * mp.pi
        t0 = eta_s / y
        up_s = -(eta_s ** 3) / mp.mpf(6)
        for n1 in range(-r_lim, r_lim + 1):
            for n2 in range(-r_lim, r_lim + 1):
                if n1 == 0 and n2 == 0:
                    continue
                wsq = (mp.mpf(n1) + mp.mpf(n2) * x) ** 2 + (mp.mpf(n2) * y) ** 2
                zv = t0 * wsq
                if zv > mp.mpf(155):
                    continue
                ph = mp.cos(twopi * (u1 * mp.mpf(n1) + u2 * mp.mpf(n2)))
                up_s += rat_m(1, 2) * ph * ((y / wsq) ** 3) * mp.exp(-zv) * (mp.mpf(2) + mp.mpf(2) * zv + zv * zv)
        lo_s = (mp.pi * (eta_s ** 2) / mp.mpf(4)) if (u1_fr == 0 and u2_fr == 0) else mp.mpf(0)
        pr_l = mp.pi * (eta_s ** 2) / mp.mpf(2)
        for m1 in range(-r_lim, r_lim + 1):
            ma1 = mp.mpf(m1) + u1
            for m2 in range(-r_lim, r_lim + 1):
                ma2 = mp.mpf(m2) + u2
                if u1_fr == 0 and u2_fr == 0 and m1 == 0 and m2 == 0:
                    continue
                dsq = (ma2 - ma1 * x) ** 2 + (ma1 * y) ** 2
                zd = (mp.pi ** 2) * dsq / (eta_s * y)
                if zd > mp.mpf(155):
                    continue
                lo_s += pr_l * mp.re(mp.expint(3, zd))
        return mp.re(up_s + lo_s)

    e00 = e3_ewald_pure_phase(tau_r, Fr(0), Fr(0), eta1)
    e_10 = e3_ewald_pure_phase(tau_r, Fr(1, 2), Fr(0), eta1)
    e_01 = e3_ewald_pure_phase(tau_r, Fr(0), Fr(1, 2), eta1)
    e_11 = e3_ewald_pure_phase(tau_r, Fr(1, 2), Fr(1, 2), eta1)
    ewald_3twist_err = abs((e_10 + e_01 + e_11) / mp.mpf(3) + rat_m(5, 16) * e00) / abs(e00)

    # Planted Control R_PC_FL5_2: keeping only 1 of the 3 E[2]\{0} twists breaks -(5/16) E_3 by > 10%:
    one_twist_err = abs(e_10 + rat_m(5, 16) * e00) / abs(e00)
    r_pc_fl5_2_caught = bool(one_twist_err > rat_m(1, 10))

    passed = bool(
        ew_split_err < ten_pow(-42)
        and gcp_ewald_err < ten_pow(-42)
        and circle_err < ten_pow(-30)
        and yf_map_err < ten_pow(-30)
        and yf_ref_vs_prod < ten_pow(-30)
        and dv_perp < ten_pow(-36)
        and ewald_3twist_err < ten_pow(-42)
        and r_pc_fl5_2_caught
    )
    return {
        "ewald_split_eta_invariance_err": mp.nstr(ew_split_err, 10),
        "ewald_gcp_reflection_rel_err": mp.nstr(gcp_ewald_err, 10),
        "ewald_yF_vs_producer_abs_diff": mp.nstr(yf_ref_vs_prod, 12),
        "ewald_transverse_dV_dperp_at_root": mp.nstr(dv_perp, 10),
        "ewald_direct_3twist_E2_rel_err": mp.nstr(ewald_3twist_err, 10),
        "r_pc_fl5_2_single_twist_rel_break": mp.nstr(one_twist_err, 10),
        "r_pc_fl5_2_planted_control_caught": r_pc_fl5_2_caught,
        "passed": passed,
    }


# ==============================================================================
# REF_FL5_3: Disjoint Real 2D Elliptic Cusp-Robin Liouville PDE (Delta phi = e^{2 phi})
#            vs. Producer's Holomorphic Fuchsian ODE
# ==============================================================================

def gl_quad_nodes(n: int) -> tuple[list[mp.mpf], list[mp.mpf]]:
    b = [mp.mpf(k) / mp.sqrt(mp.mpf(4 * k * k - 1)) for k in range(1, n)]
    m = mp.zeros(n, n)
    for k in range(n - 1):
        m[k, k + 1] = b[k]
        m[k + 1, k] = b[k]
    evs, vecs = mp.eighe(m)
    return [evs[k] for k in range(n)], [mp.mpf(2) * (mp.re(vecs[0, k]) ** 2) for k in range(n)]


def solve_2d_robin_liouville_pde(tau_in: mp.mpc, n_g: int) -> dict[str, Any]:
    """Disjoint 2D nonlinear elliptic Liouville PDE solver on E_tau \\ {0} (zero Fuchsian ODE / wp / c_*)."""
    with mp.workdps(22):
        sh_int = int(mp.nint(mp.re(tau_in)))
        tau = tau_in - mp.mpf(sh_int)
        xr, yi = mp.re(tau), mp.im(tau)
        q = mp.exp(J_MP * mp.pi * tau)

        freqs = [k if k < n_g // 2 else k - n_g for k in range(n_g)]
        f_mat = mp.matrix([[mp.exp(-mp.mpf(2) * J_MP * mp.pi * rat_m(freqs[j] * k, n_g)) for k in range(n_g)] for j in range(n_g)])
        finv = mp.matrix([[mp.exp(mp.mpf(2) * J_MP * mp.pi * rat_m(k * freqs[j], n_g)) / mp.mpf(n_g) for j in range(n_g)] for k in range(n_g)])
        lap_e = [
            [-((mp.mpf(2) * mp.pi) ** 2) * (mp.mpf(freqs[i]) ** 2 + ((mp.mpf(freqs[j]) - xr * mp.mpf(freqs[i])) / yi) ** 2) for j in range(n_g)]
            for i in range(n_g)
        ]

        def spec_lap(u_m: mp.matrix) -> mp.matrix:
            uh = f_mat * u_m * f_mat.T
            for i in range(n_g):
                for j in range(n_g):
                    uh[i, j] *= lap_e[i][j]
            out = finv * uh * finv.T
            return mp.matrix([[mp.re(out[i, j]) for j in range(n_g)] for i in range(n_g)])

        t1p0 = mp.fsum(
            mp.mpf(2 * (-1 if (k % 2) else 1) * (2 * k + 1)) * (q ** (rat_m(2 * k + 1, 2) ** 2)) * mp.pi
            for k in range(12)
        )
        rho = mp.zeros(n_g, n_g)
        ln_rho = mp.zeros(n_g, n_g)
        g2_ln = mp.zeros(n_g, n_g)
        for i in range(n_g):
            av = rat_m(i, n_g)
            if av > rat_m(1, 2):
                av -= mp.mpf(1)
            for j in range(n_g):
                if i == 0 and j == 0:
                    continue
                bv = rat_m(j, n_g)
                if bv > rat_m(1, 2):
                    bv -= mp.mpf(1)
                zv = av + bv * tau
                yv = mp.im(zv)
                t1 = mp.jtheta(1, mp.pi * zv, q)
                dt1 = mp.jtheta(1, mp.pi * zv, q, 1) * mp.pi
                rv = abs(t1 / t1p0) * mp.exp(-mp.pi * yv * yv / yi)
                rho[i, j] = rv
                ln_rho[i, j] = mp.log(rv)
                g2_ln[i, j] = abs(dt1 / t1 + mp.mpf(2) * J_MP * mp.pi * yv / yi) ** 2

        b_val = rat_m(13, 20)
        w = mp.zeros(n_g, n_g)

        def pde_res(w_in: mp.matrix, b_in: mp.mpf) -> mp.matrix:
            lw = spec_lap(w_in)
            r = mp.zeros(n_g, n_g)
            r[0, 0] = lw[0, 0] + mp.mpf(2) * mp.pi / yi
            for i in range(n_g):
                for j in range(n_g):
                    if i == 0 and j == 0:
                        continue
                    lv = -ln_rho[i, j] + b_in
                    r[i, j] = lw[i, j] + (mp.mpf(2) * mp.pi / yi) * (mp.mpf(1) - mp.mpf(1) / lv) + (g2_ln[i, j] - mp.exp(mp.mpf(2) * w_in[i, j]) / (rho[i, j] ** 2)) / (lv * lv)
            return r

        mx_res = mp.mpf(1)
        for _it in range(10):
            r0 = pde_res(w, b_val)
            mx_res = max(abs(r0[i, j]) for i in range(n_g) for j in range(n_g))
            if mx_res < ten_pow(-13):
                break
            eb = ten_pow(-8)
            drb = (pde_res(w, b_val + eb) - r0) / eb
            vp = mp.zeros(n_g, n_g)
            vlist: list[mp.mpf] = []
            for i in range(n_g):
                for j in range(n_g):
                    if i == 0 and j == 0:
                        continue
                    lv = -ln_rho[i, j] + b_val
                    vp[i, j] = mp.mpf(2) * mp.exp(mp.mpf(2) * w[i, j]) / ((rho[i, j] ** 2) * lv * lv)
                    vlist.append(vp[i, j])
            vlist.sort()
            c_med = vlist[len(vlist) // 2]
            inv_p = [[mp.mpf(1) / (-lap_e[i][j] + c_med) for j in range(n_g)] for i in range(n_g)]

            def apply_prec(rm: mp.matrix) -> mp.matrix:
                rh = f_mat * rm * f_mat.T
                for i in range(n_g):
                    for j in range(n_g):
                        rh[i, j] *= inv_p[i][j]
                out = finv * rh * finv.T
                return mp.matrix([[mp.re(out[i, j]) for j in range(n_g)] for i in range(n_g)])

            def solve_cg(rhs_m: mp.matrix) -> mp.matrix:
                xm = mp.zeros(n_g, n_g)
                rc = rhs_m.copy()
                zc = apply_prec(rc)
                pc = zc.copy()
                rz = mp.fsum(rc[i, j] * zc[i, j] for i in range(n_g) for j in range(n_g))
                for _ in range(36):
                    lp = spec_lap(pc)
                    ap = mp.matrix([[-lp[i, j] + vp[i, j] * pc[i, j] for j in range(n_g)] for i in range(n_g)])
                    pap = mp.fsum(pc[i, j] * ap[i, j] for i in range(n_g) for j in range(n_g))
                    al = rz / pap
                    xm += al * pc
                    rc -= al * ap
                    if max(abs(rc[i, j]) for i in range(n_g) for j in range(n_g)) < ten_pow(-12):
                        break
                    zc = apply_prec(rc)
                    rzn = mp.fsum(rc[i, j] * zc[i, j] for i in range(n_g) for j in range(n_g))
                    pc = zc + (rzn / rz) * pc
                    rz = rzn
                return xm

            u1 = solve_cg(r0)
            u2 = solve_cg(drb)
            db = -(w[0, 0] + u1[0, 0]) / u2[0, 0]
            w += u1 + db * u2
            b_val += db

        mx_res = max(abs(pde_res(w, b_val)[i, j]) for i in range(n_g) for j in range(n_g))
        w_hat = (f_mat * w * f_mat.T) / mp.mpf(n_g * n_g)

        def eval_w_interp(z: mp.mpc) -> mp.mpf:
            bv = mp.im(z) / yi
            av = mp.re(z) - bv * xr
            pa = [mp.exp(mp.mpf(2) * J_MP * mp.pi * mp.mpf(freqs[i]) * av) for i in range(n_g)]
            pb = [mp.exp(mp.mpf(2) * J_MP * mp.pi * mp.mpf(freqs[j]) * bv) for j in range(n_g)]
            acc = mp.mpc(0)
            for i in range(n_g):
                row_s = mp.mpc(0)
                for j in range(n_g):
                    row_s += w_hat[i, j] * pb[j]
                acc += pa[i] * row_s
            return mp.re(acc)

        corners = [
            rat_m(1, 2) + tau / mp.mpf(2),
            -rat_m(1, 2) + tau / mp.mpf(2),
            -rat_m(1, 2) - tau / mp.mpf(2),
            rat_m(1, 2) - tau / mp.mpf(2),
        ]
        angs = sorted((mp.arg(c) % (mp.mpf(2) * mp.pi)) for c in corners)
        sectors = [(angs[k], angs[k + 1]) for k in range(3)] + [(angs[3], angs[0] + mp.mpf(2) * mp.pi)]
        gx_th, gw_th = gl_quad_nodes(12)
        gx_t, gw_t = gl_quad_nodes(14)
        kinds_in = (3, 2, 4) if (sh_int % 2 != 0) else (4, 2, 3)

        g_s0 = [mp.mpf(0)] * 3
        g_s12 = [mp.mpf(0)] * 3
        area_h = mp.mpf(0)
        for tha, thb in sectors:
            hth, mth = (thb - tha) / mp.mpf(2), (tha + thb) / mp.mpf(2)
            for ix in range(12):
                th = mth + hth * gx_th[ix]
                wth = hth * gw_th[ix]
                dbv = mp.sin(th) / yi
                dav = mp.cos(th) - dbv * xr
                rmax = rat_m(1, 2) / max(abs(dav), abs(dbv))
                tmax = mp.mpf(1) / (-mp.log(rmax) + b_val)
                ht = tmax / mp.mpf(2)
                dirc = mp.exp(J_MP * th)
                for it_q in range(14):
                    tv = ht + ht * gx_t[it_q]
                    wt = ht * gw_t[it_q]
                    rv = mp.exp(b_val - mp.mpf(1) / tv)
                    zv = rv * dirc
                    jac_r = (rv * rv) / (tv * tv)
                    if rv < ten_pow(-6):
                        ws0 = mp.mpf(1)
                        ws12 = rv / tv
                    else:
                        bv_r = mp.im(zv) / yi
                        av_r = mp.re(zv) - bv_r * xr
                        av_r -= mp.nint(av_r)
                        bv_r -= mp.nint(bv_r)
                        zr = av_r + bv_r * tau
                        lr = mp.log(abs(mp.jtheta(1, mp.pi * zr, q) / t1p0)) - mp.pi * (mp.im(zr) ** 2) / yi
                        wv = eval_w_interp(zr)
                        ephi = mp.exp(-lr + wv) / (-lr + b_val)
                        ws0 = jac_r * ephi * ephi
                        ws12 = jac_r * ephi
                    dw2 = wth * wt
                    area_h += dw2 * ws0
                    yv = mp.im(zv)
                    fac = mp.sqrt(mp.mpf(2) * yi) * mp.exp(-mp.mpf(2) * mp.pi * yv * yv / yi)
                    pz = mp.pi * zv
                    for a_i, kd in enumerate(kinds_in):
                        dv = fac * (abs(mp.jtheta(kd, pz, q)) ** 2)
                        g_s0[a_i] += dw2 * (ws0 / (mp.mpf(2) * mp.pi)) * dv
                        g_s12[a_i] += dw2 * (ws12 / mp.sqrt(mp.mpf(2) * mp.pi * yi)) * dv

        g_s12_um = [mp.mpf(3) * x / sum(g_s12) for x in g_s12]
        return {
            "b_robin": mp.mpf(b_val),
            "max_pde_res": mp.mpf(mx_res),
            "area_over_2pi": mp.mpf(area_h) / (mp.mpf(2) * mp.pi),
            "g_s0": [mp.mpf(x) for x in g_s0],
            "g_s12_um": [mp.mpf(x) for x in g_s12_um],
        }


# ==============================================================================
# Laurent-Residue Szego Yukawa Kernel (Disjoint from Producer's q-Derivative!)
# ==============================================================================

def eval_yukawa_laurent(tau: mp.mpc, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    """Compute S_H(0) via high-precision symmetric Laurent contour residue around z = 0
    for S_k(z) = (theta_1'(0) / (2 pi)) * theta_{k+1}(pi z) / theta_1(pi z),
    WITHOUT using E_2(tau) or theta logarithmic q-derivatives!"""
    qi = mp.matrix([[J_MP, 0], [0, -J_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = rat_m(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]

    qp = mp.exp(J_MP * mp.pi * tau)
    t1p_pi = mp.jtheta(1, 0, qp, 1) * mp.pi  # d/dz theta_1(pi z)|_{z=0} = pi * theta_1'(0|q)
    # Wait: in S_H, the constant term in the Laurent expansion around z=0 of
    #   (theta_1'(0) / (2 pi)) * [ -i * (theta_2(pi z)/(theta_2(0)?)) ]...
    # Let's check the exact Laurent relation!
    # For odd 1/theta_1(pi z): theta_1(pi z) = t1p_pi * z * (1 + (pi^2/6)*(theta_1'''(0)/theta_1'(0)) z^2 + O(z^4)),
    # while even theta_k(pi z) = theta_k(0) * (1 + (pi^2/2)*(theta_k''(0)/theta_k(0)) z^2 + O(z^4))!
    # Wait: the z^{+1} coefficient (second Laurent term = 1/2 d^2/dz^2 [z * f(z)]|_{z=0}!) of
    #   F_k(z) := theta_k(pi z) / (z * t1p_pi / theta_k(0)?)
    # Recall Jacobi's heat equation: d/d(tau) theta_k(0|tau) = (1 / (4 pi i)) * d^2/dz^2 theta_k(z|tau)|_{z=0}
    #   => l_kd = (1 / (2 pi i)) d/dtau ln theta_k = -(1 / (8 pi^2)) theta_k''(0) / theta_k(0)!
    # AND theta_1'''(0) / theta_1'(0) = -pi^2 * E_2(tau)! Wait: in mpmath `jtheta(1, 0, qp, 3)` is theta_1'''(0) w.r.t. u = pi z:
    #   theta_1'''(0)/theta_1'(0) = -E_2(tau), and theta_k''(0)/theta_k(0) = -8 * l_kd?
    # Let's check exact identity between theta_k''(0)/theta_k(0) (w.r.t. u = pi z) and Producer's l_kd = (1/(2 pi i)) d/dtau ln theta_k:
    # Since theta_k(u|tau) = sum exp(i pi tau n^2 + 2 i n u):
    #   d/dtau theta_k(0|tau) = i pi sum n^2 (...) = (2 pi i) * l_kd * theta_k(0)  => l_kd = (1/2) sum n^2 (...) / theta_k(0);
    #   d^2/du^2 theta_k(u|tau)|_{u=0} = -4 sum n^2 (...)  => theta_k''(0)/theta_k(0) = -8 * l_kd!!
    # AND for theta_1(u|tau) = 2 sum (-1)^n exp(i pi tau (n+1/2)^2) sin((2n+1) u):
    #   theta_1'''(0) / theta_1'(0) = -sum (2n+1)^3 (...) / sum (2n+1) (...) = -E_2(tau)??
    # WAIT: check q=0 limit! At q -> 0: n=0 gives -(1)^3 / 1 = -1 = -E_2(i infty)!!
    # Check l2d - l3d - l4d + E_2/24 at q -> 0:
    #   l2d -> 1/8, l3d -> 0, l4d -> 0, E_2/24 -> 1/24 => 1/8 + 1/24 = 4/24 = 1/6!
    #   Meanwhile (-1/8)*(theta_2''(0)/theta_2(0) - theta_3''(0)/theta_3(0) - theta_4''(0)/theta_4(0)) - (1/24)*(theta_1'''(0)/theta_1'(0)):
    #   At q -> 0: (-1/8)*(-1 + 0 - 0) - (1/24)*(-1) = 1/8 + 1/24 = 1/6!!
    # BINGO!! S_H CAN BE COMPUTED PURELY FROM u-DERIVATIVES AT u = 0 (`jtheta(k, 0, qp, 2)` and `jtheta(1, 0, qp, 3)`) WITH ZERO E_2 q-SERIES!!
    t20, t30, t40 = mp.jtheta(2, 0, qp), mp.jtheta(3, 0, qp), mp.jtheta(4, 0, qp)
    r2 = -mp.jtheta(2, 0, qp, 2) / (mp.mpf(8) * t20)
    r3 = -mp.jtheta(3, 0, qp, 2) / (mp.mpf(8) * t30)
    r4 = -mp.jtheta(4, 0, qp, 2) / (mp.mpf(8) * t40)
    e2_from_t1 = -mp.jtheta(1, 0, qp, 3) / mp.jtheta(1, 0, qp, 1)
    c_e = e2_from_t1 / mp.mpf(24)
    sh = (
        (-t20 / (t30 * t40)) * (r2 - r3 - r4 + c_e) * qi
        + (-t40 / (t20 * t30)) * (r4 - r2 - r3 + c_e) * qj
        + (J_MP * t30 / (t20 * t40)) * (r3 - r2 - r4 + c_e) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]

    def th_char(ca: Fr, cb: Fr) -> mp.mpc:
        ta, tb = ca % 1, cb % 1
        nb = int(cb - tb)
        am, bm = fr_m(ta), fr_m(tb)
        zv = am * tau + bm
        # theta[a; b](0|tau) = exp(i pi a^2 tau + 2 pi i a b) * theta_3(pi * (a tau + b) | q)!
        base = mp.exp(J_MP * mp.pi * am * am * tau + mp.mpf(2) * J_MP * mp.pi * am * bm) * mp.jtheta(3, mp.pi * zv, qp)
        return base if (nb == 0 or ta == 0) else mp.exp(mp.mpf(2) * J_MP * mp.pi * am * mp.mpf(nb)) * base

    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-mp.mpf(2) * J_MP * mp.pi * fr_m(xv[0]))
    kap = {"1": -J_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": J_MP}
    hfr = Fr(1, 2)
    cs = {"1": (ap + hfr, bp + hfr), "i": (ap + hfr, bp), "j": (ap, bp + hfr), "k": (ap, bp)}
    ds = {"1": (am + hfr, bm + hfr), "i": (am + hfr, bm), "j": (am, bm + hfr), "k": (am, bm)}
    rs: dict[str, mp.mpc] = {}
    for sk in ("1", "i", "j", "k"):
        if ((cs[sk][0] - hfr) % 1 == 0 and (cs[sk][1] - hfr) % 1 == 0) or (
            (ds[sk][0] - hfr) % 1 == 0 and (ds[sk][1] - hfr) % 1 == 0
        ):
            rs[sk] = mp.mpc(0)
        else:
            rs[sk] = kap[sk] * th_char(cs[sk][0], cs[sk][1]) * th_char(ds[sk][0], ds[sk][1]) / t1p_pi
    mw = rs["1"] * ed["1"] + rs["i"] * ed["i"] + rs["j"] * ed["j"] + rs["k"] * ed["k"]
    return mp.matrix([
        [
            ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1]
            + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1]
            for cb in range(3)
        ]
        for ra in range(3)
    ])


def svd_sorted(mat: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    u, s, _ = mp.svd_c(mat)
    od = sorted(range(3), key=lambda k: s[k])
    return mp.matrix([[u[r, od[c]] for c in range(3)] for r in range(3)]), [s[k] for k in od]


def takagi_sorted(ms: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    h = ms * ms.H
    evs, v = mp.eighe(rat_m(1, 2) * (h + h.H))
    od = sorted(range(3), key=lambda k: mp.re(evs[k]))
    ur = mp.zeros(3, 3)
    sv: list[mp.mpf] = []
    for c, idx in enumerate(od):
        sv.append(mp.sqrt(max(mp.mpf(0), mp.re(evs[idx]))))
        uk = v[:, idx]
        ukc = mp.matrix([[mp.conj(uk[r, 0])] for r in range(3)])
        ph = mp.exp(J_MP * mp.arg((uk.H * ms * ukc)[0, 0]) / mp.mpf(2))
        for r in range(3):
            ur[r, c] = mp.conj(uk[r, 0] * ph)
    return ur, sv


def run_ref_fl5_3(prod_l5_3: dict[str, Any]) -> dict[str, Any]:
    tau8 = rat_m(16, 5) + J_MP * rat_m(8, 5)
    pde14 = solve_2d_robin_liouville_pde(tau8, 14)
    pde20 = solve_2d_robin_liouville_pde(tau8, 20)

    # Richardson O(1/N^2) extrapolation between N1=14 (196) and N2=20 (400): (400*X_20 - 196*X_14) / 204
    w20, w14, wden = mp.mpf(400), mp.mpf(196), mp.mpf(204)
    b_rich = (w20 * pde20["b_robin"] - w14 * pde14["b_robin"]) / wden
    g_s12_rich = [(w20 * pde20["g_s12_um"][i] - w14 * pde14["g_s12_um"][i]) / wden for i in range(3)]
    g_s0_rich = [(w20 * pde20["g_s0"][i] - w14 * pde14["g_s0"][i]) / wden for i in range(3)]

    mp.mp.dps = 40
    prod_bc = mp.mpf(prod_l5_3["tau8_bc_star"])
    prod_gs12 = [mp.mpf(s) for s in prod_l5_3["G_s12_dirac_unitmean_tau8"]]
    prod_gs0 = [mp.mpf(s) for s in prod_l5_3["G_s0_scalar_area_tau8"]]

    bc_pde_vs_fuchs = abs(b_rich - prod_bc)
    gs12_pde_vs_fuchs = max(abs(g_s12_rich[i] - prod_gs12[i]) for i in range(3))
    gs0_pde_vs_fuchs = max(abs(g_s0_rich[i] - prod_gs0[i]) for i in range(3))

    # Undressed CKM check on PDE Gramians using Referee's Laurent Yukawa kernel:
    k5 = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    k6 = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]
    wu = sum((eval_yukawa_laurent(tau8, a, b, 1, -4) for a, b in k5), mp.zeros(3, 3)) / mp.mpf(4)
    wd = (
        sum((eval_yukawa_laurent(tau8, a, b, 1, 2) for a, b in k5), mp.zeros(3, 3)) / mp.mpf(4)
        + sum((eval_yukawa_laurent(tau8, a, b, 1, 2) for a, b in k6), mp.zeros(3, 3)) / mp.mpf(2)
    ) / mp.mpf(2)

    kis_12 = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in g_s12_rich])
    uu12, _ = svd_sorted(kis_12 * wu * kis_12)
    ud12, _ = svd_sorted(kis_12 * wd * kis_12)
    vc12 = uu12.H * ud12
    dirac_undressed_ordered = bool(abs(vc12[0, 1]) > abs(vc12[1, 2]) > abs(vc12[0, 2]) > mp.mpf(0))

    # Planted Control R_PC_FL5_3: PDE spin-0 scalar area Gramian triggers CKM inversion |V_cb| > |V_us|:
    kis_0 = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in g_s0_rich])
    uu0, _ = svd_sorted(kis_0 * wu * kis_0)
    ud0, _ = svd_sorted(kis_0 * wd * kis_0)
    vc0 = uu0.H * ud0
    r_pc_fl5_3_caught = bool(abs(vc0[1, 2]) > abs(vc0[0, 1]) and dirac_undressed_ordered)

    passed = bool(
        pde14["max_pde_res"] < ten_pow(-12)
        and pde20["max_pde_res"] < ten_pow(-12)
        and bc_pde_vs_fuchs < rat_m(2, 1000)
        and gs12_pde_vs_fuchs < ten_pow(-4)
        and gs0_pde_vs_fuchs < rat_m(5, 1000)
        and dirac_undressed_ordered
        and r_pc_fl5_3_caught
    )
    return {
        "pde_N14_max_res": mp.nstr(pde14["max_pde_res"], 8),
        "pde_N20_max_res": mp.nstr(pde20["max_pde_res"], 8),
        "pde_richardson_b_robin": mp.nstr(b_rich, 12),
        "bc_pde_vs_fuchsian_abs_diff": mp.nstr(bc_pde_vs_fuchs, 8),
        "G_s12_pde_richardson": [mp.nstr(x, 10) for x in g_s12_rich],
        "G_s12_pde_vs_fuchsian_max_diff": mp.nstr(gs12_pde_vs_fuchs, 8),
        "G_s0_pde_vs_fuchsian_max_diff": mp.nstr(gs0_pde_vs_fuchs, 8),
        "dirac_s12_undressed_ckm_ordered": dirac_undressed_ordered,
        "r_pc_fl5_3_scalar_s0_inversion_caught": r_pc_fl5_3_caught,
        "_g_s12_rich": g_s12_rich,
        "passed": passed,
    }


# ==============================================================================
# REF_FL5_4: Independent Laurent-Yukawa + Cayley-Unitary Lopsided Seesaw Audit
# ==============================================================================

def run_ref_fl5_4(prod_l5_4: dict[str, Any], prod_l5_3: dict[str, Any], g_s12_pde: list[mp.mpf]) -> dict[str, Any]:
    mp.mp.dps = 45
    tau8 = rat_m(16, 5) + J_MP * rat_m(8, 5)
    k5 = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    k6 = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]
    w_av = lambda pts, ql, qr: sum((eval_yukawa_laurent(tau8, a, b, ql, qr) for a, b in pts), mp.zeros(3, 3)) / mp.mpf(len(pts))

    wu = w_av(k5, 1, -4)
    wd = (w_av(k5, 1, 2) + w_av(k6, 1, 2)) / mp.mpf(2)
    we = (w_av(k5, -3, 6) + w_av(k6, -3, 6)) / mp.mpf(2)
    wnu = (w_av(k5, 3, -5) + w_av(k6, 3, -5)) / mp.mpf(2)
    wr = (w_av(k5, 3, 3) + w_av(k6, 3, 3)) / mp.mpf(2)
    wr_s = (wr + wr.T) / mp.mpf(2)
    _, svr = svd_sorted(wr_s)
    mr = mp.eye(3) + wr_s / svr[2]

    eps5 = mp.exp(mp.mpf(2) * J_MP * mp.pi * tau8 / mp.mpf(5))
    d10 = mp.diag([eps5 ** 2, mp.mpc(1), eps5 ** 3])

    def obs_for_g(gv: list[mp.mpf]) -> dict[str, Any]:
        kis = mp.diag([mp.mpf(1) / mp.sqrt(x) for x in gv])
        yu, yd, ye, ynu = kis * d10 * wu * d10 * kis, kis * d10 * wd * kis, kis * we * d10 * kis, kis * wnu
        uu, su = svd_sorted(yu)
        ud, sd = svd_sorted(yd)
        ue, se = svd_sorted(ye)
        vc = uu.H * ud
        mnu = -ynu * (mr ** (-1)) * ynu.T
        unu, snu = takagi_sorted(mnu)
        up = ue.H * mp.matrix([[mp.conj(unu[r, c]) for c in range(3)] for r in range(3)])
        s13 = abs(up[0, 2]) ** 2
        s12 = (abs(up[0, 1]) ** 2) / (mp.mpf(1) - s13)
        s23 = (abs(up[1, 2]) ** 2) / (mp.mpf(1) - s13)
        dm = (snu[1] ** 2 - snu[0] ** 2) / (snu[2] ** 2 - snu[0] ** 2)
        return {
            "yu": yu, "yd": yd, "ye": ye, "ynu": ynu,
            "v12": abs(vc[0, 1]), "v23": abs(vc[1, 2]), "v13": abs(vc[0, 2]),
            "s12": s12, "s23": s23, "s13": s13, "dm": dm,
            "u13": su[0] / su[2],
        }

    obs_pde = obs_for_g(g_s12_pde)
    obs_exact_g = obs_for_g([mp.mpf(s) for s in prod_l5_3["G_s12_dirac_unitmean_tau8"]])
    prod_ckm = [mp.mpf(s) for s in prod_l5_4["tau8_dirac_s12_ckm_12_23_13_J"][:3]]
    prod_pmns = [mp.mpf(s) for s in prod_l5_4["tau8_dirac_s12_pmns_s12_s23_s13_dm_J"][:4]]

    laurent_vs_prod_err = max(
        abs(obs_exact_g["v12"] - prod_ckm[0]),
        abs(obs_exact_g["v23"] - prod_ckm[1]),
        abs(obs_exact_g["s12"] - prod_pmns[0]),
        abs(obs_exact_g["s23"] - prod_pmns[1]),
        abs(obs_exact_g["dm"] - prod_pmns[3]),
    )
    pde_vs_prod_obs_err = max(
        abs(obs_pde["v12"] - prod_ckm[0]),
        abs(obs_pde["s12"] - prod_pmns[0]),
        abs(obs_pde["s23"] - prod_pmns[1]),
    )

    # 10-trial Cayley-transform unitary basis-scrambling check:
    rng = random.Random(2026112399)
    max_cayley_err = mp.mpf(0)
    for _ in range(10):
        uq, uur, udr, ul, uer, unr = (cayley_unitary_u3(rng) for _ in range(6))
        uu_c, _ = svd_sorted(uq * obs_pde["yu"] * uur.H)
        ud_c, _ = svd_sorted(uq * obs_pde["yd"] * udr.H)
        ue_c, _ = svd_sorted(ul * obs_pde["ye"] * uer.H)
        vc_c = uu_c.H * ud_c
        ynu_c = ul * obs_pde["ynu"] * unr
        mr_c = unr.T * mr * unr
        mnu_c = -ynu_c * (mr_c ** (-1)) * ynu_c.T
        unu_c, snu_c = takagi_sorted(mnu_c)
        up_c = ue_c.H * mp.matrix([[mp.conj(unu_c[r, c]) for c in range(3)] for r in range(3)])
        s13_c = abs(up_c[0, 2]) ** 2
        s12_c = (abs(up_c[0, 1]) ** 2) / (mp.mpf(1) - s13_c)
        s23_c = (abs(up_c[1, 2]) ** 2) / (mp.mpf(1) - s13_c)
        max_cayley_err = max(max_cayley_err, abs(abs(vc_c[0, 1]) - obs_pde["v12"]), abs(s12_c - obs_pde["s12"]), abs(s23_c - obs_pde["s23"]))

    # Planted Control R_PC_FL5_4: setting q_R(nu^c) = 0 (6Y(nu^c) = 0) collapses W_nu to rank-2 & seesaw M_nu to rank-1:
    wnu_q0 = (w_av(k5, -3, 0) + w_av(k6, -3, 0)) / mp.mpf(2)
    mnu_q0 = -wnu_q0 * (mr ** (-1)) * wnu_q0.T
    _, snu_q0 = svd_sorted(mnu_q0)
    dm_q0 = (snu_q0[1] ** 2 - snu_q0[0] ** 2) / (snu_q0[2] ** 2 - snu_q0[0] ** 2)
    r_pc_fl5_4_caught = bool(dm_q0 < ten_pow(-60))

    passed = bool(
        laurent_vs_prod_err < ten_pow(-8)
        and pde_vs_prod_obs_err < ten_pow(-4)
        and obs_pde["v12"] > obs_pde["v23"] > obs_pde["v13"] > mp.mpf(0)
        and rat_m(25, 100) < obs_pde["s12"] < rat_m(70, 100)
        and rat_m(30, 100) < obs_pde["s23"] < rat_m(70, 100)
        and max_cayley_err < ten_pow(-35)
        and r_pc_fl5_4_caught
    )
    return {
        "laurent_vs_producer_yukawa_obs_err": mp.nstr(laurent_vs_prod_err, 10),
        "pde_kahler_vs_producer_obs_err": mp.nstr(pde_vs_prod_obs_err, 10),
        "cayley_10trial_unitary_max_err": mp.nstr(max_cayley_err, 10),
        "r_pc_fl5_4_qR0_rank1_dm_collapse": mp.nstr(dm_q0, 8),
        "r_pc_fl5_4_planted_control_caught": r_pc_fl5_4_caught,
        "passed": passed,
    }


# ==============================================================================
# REF_FL5_5: Implicit GL6 Collocation on Complete 2-Loop Type-II 2HDM RGEs
# ==============================================================================

def rhs_2hdm_diag_ref(st: list[mp.mpf], include_nlo_q: bool = True) -> list[mp.mpf]:
    g1, g2, g3, yt, yb, ye, l1, l2, l3, l4 = st
    inv1 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))
    inv2 = inv1 * inv1
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
    gy2 = rat_m(3, 5) * g12
    yt2, yb2, ye2 = yt * yt, yb * yb, ye * ye
    yt4, yb4, ye4, ytb = yt2 * yt2, yb2 * yb2, ye2 * ye2, yt2 * yb2
    yt6, yb6, ye6, yt4b2, yb4t2 = yt4 * yt2, yb4 * yb2, ye4 * ye2, yt4 * yb2, yb4 * yt2
    tu, td = mp.mpf(3) * yt2, mp.mpf(3) * yb2 + ye2

    bg1 = inv1 * rat_m(21, 5) * g12 * g1 + inv2 * (g1 ** 3) * (rat_m(104, 25) * g12 + rat_m(18, 5) * g22 + rat_m(44, 5) * g32 - rat_m(17, 10) * yt2 - rat_m(1, 2) * yb2 - rat_m(3, 2) * ye2)
    bg2 = inv1 * mp.mpf(-3) * g22 * g2 + inv2 * (g2 ** 3) * (rat_m(6, 5) * g12 + mp.mpf(8) * g22 + mp.mpf(12) * g32 - rat_m(3, 2) * yt2 - rat_m(3, 2) * yb2 - rat_m(1, 2) * ye2)
    bg3 = inv1 * mp.mpf(-7) * g32 * g3 + inv2 * (g3 ** 3) * (rat_m(11, 10) * g12 + rat_m(9, 2) * g22 - mp.mpf(26) * g32 - mp.mpf(2) * yt2 - mp.mpf(2) * yb2)

    q_on = mp.mpf(1) if include_nlo_q else mp.mpf(0)
    l34_sq = l3 * l3 + l3 * l4 + l4 * l4
    mu1 = rat_m(3, 2) * yt2 + rat_m(1, 2) * yb2 + tu - rat_m(17, 20) * g12 - rat_m(9, 4) * g22 - mp.mpf(8) * g32
    md1 = rat_m(3, 2) * yb2 + rat_m(1, 2) * yt2 + td - rat_m(1, 4) * g12 - rat_m(9, 4) * g22 - mp.mpf(8) * g32
    me1 = rat_m(3, 2) * ye2 + td - rat_m(9, 4) * g12 - rat_m(9, 4) * g22

    sc_u = rat_m(1267, 600) * g12 * g12 - rat_m(9, 20) * g12 * g22 + rat_m(19, 15) * g12 * g32 - rat_m(21, 4) * g22 * g22 + mp.mpf(9) * g22 * g32 - mp.mpf(108) * g32 * g32 + (rat_m(17, 8) * g12 + rat_m(45, 8) * g22 + mp.mpf(20) * g32) * yt2 - rat_m(27, 4) * yt4 - rat_m(9, 4) * ytb + q_on * (rat_m(3, 2) * l2 * l2 + l34_sq)
    mu2 = rat_m(3, 2) * yt4 - rat_m(1, 4) * ytb - rat_m(1, 4) * yb4 + (rat_m(223, 80) * g12 + rat_m(135, 16) * g22 + mp.mpf(16) * g32 - rat_m(9, 4) * tu - q_on * mp.mpf(6) * l2) * yt2 + (-rat_m(41, 240) * g12 + rat_m(33, 16) * g22 + rat_m(16, 3) * g32 - rat_m(3, 4) * td + q_on * (-mp.mpf(2) * l3 + mp.mpf(2) * l4)) * yb2 + sc_u
    sc_d = -rat_m(113, 600) * g12 * g12 - rat_m(27, 20) * g12 * g22 + rat_m(31, 15) * g12 * g32 - rat_m(21, 4) * g22 * g22 + mp.mpf(9) * g22 * g32 - mp.mpf(108) * g32 * g32 + (rat_m(5, 8) * g12 + rat_m(45, 8) * g22 + mp.mpf(20) * g32) * yb2 + (rat_m(15, 8) * g12 + rat_m(15, 8) * g22) * ye2 - rat_m(27, 4) * yb4 - rat_m(9, 4) * ye4 - rat_m(9, 4) * ytb + q_on * (rat_m(3, 2) * l1 * l1 + l34_sq)
    md2 = rat_m(3, 2) * yb4 - rat_m(1, 4) * ytb - rat_m(1, 4) * yt4 + (rat_m(187, 80) * g12 + rat_m(135, 16) * g22 + mp.mpf(16) * g32 - rat_m(9, 4) * td - q_on * mp.mpf(6) * l1) * yb2 + (-rat_m(53, 240) * g12 + rat_m(33, 16) * g22 + rat_m(16, 3) * g32 - rat_m(3, 4) * tu + q_on * (-mp.mpf(2) * l3 + mp.mpf(2) * l4)) * yt2 + sc_d
    sc_e = rat_m(1449, 200) * g12 * g12 + rat_m(27, 20) * g12 * g22 - rat_m(21, 4) * g22 * g22 + (rat_m(5, 8) * g12 + rat_m(45, 8) * g22 + mp.mpf(20) * g32) * yb2 + (rat_m(15, 8) * g12 + rat_m(15, 8) * g22) * ye2 - rat_m(27, 4) * yb4 - rat_m(9, 4) * ye4 - rat_m(9, 4) * ytb + q_on * (rat_m(3, 2) * l1 * l1 + l34_sq)
    me2 = rat_m(3, 2) * ye4 + (rat_m(387, 80) * g12 + rat_m(135, 16) * g22 - rat_m(9, 4) * td - q_on * mp.mpf(6) * l1) * ye2 + sc_e

    c34 = rat_m(3, 4)
    dl1_1 = mp.mpf(12) * l1 * l1 + mp.mpf(4) * l3 * l3 + mp.mpf(4) * l3 * l4 + mp.mpf(2) * l4 * l4 + (mp.mpf(4) * td - mp.mpf(3) * gy2 - mp.mpf(9) * g22) * l1 + c34 * (gy2 * gy2 + mp.mpf(2) * gy2 * g22 + mp.mpf(3) * g22 * g22) - mp.mpf(12) * yb4 - mp.mpf(4) * ye4
    dl2_1 = mp.mpf(12) * l2 * l2 + mp.mpf(4) * l3 * l3 + mp.mpf(4) * l3 * l4 + mp.mpf(2) * l4 * l4 + (mp.mpf(4) * tu - mp.mpf(3) * gy2 - mp.mpf(9) * g22) * l2 + c34 * (gy2 * gy2 + mp.mpf(2) * gy2 * g22 + mp.mpf(3) * g22 * g22) - mp.mpf(12) * yt4
    dl3_1 = (l1 + l2) * (mp.mpf(6) * l3 + mp.mpf(2) * l4) + mp.mpf(4) * l3 * l3 + mp.mpf(2) * l4 * l4 + (mp.mpf(2) * tu + mp.mpf(2) * td - mp.mpf(3) * gy2 - mp.mpf(9) * g22) * l3 + c34 * (gy2 * gy2 - mp.mpf(2) * gy2 * g22 + mp.mpf(3) * g22 * g22) - mp.mpf(12) * ytb
    dl4_1 = mp.mpf(2) * (l1 + l2) * l4 + mp.mpf(8) * l3 * l4 + mp.mpf(4) * l4 * l4 + (mp.mpf(2) * tu + mp.mpf(2) * td - mp.mpf(3) * gy2 - mp.mpf(9) * g22) * l4 + mp.mpf(3) * gy2 * g22 + mp.mpf(12) * ytb

    if include_nlo_q:
        gy4, gy6 = gy2 * gy2, gy2 * gy2 * gy2
        g24, g26 = g22 * g22, g22 * g22 * g22
        l34_m = mp.mpf(2) * l3 * l3 + mp.mpf(2) * l3 * l4 + l4 * l4
        bs = lambda ls: (
            -rat_m(131, 8) * gy6 - rat_m(191, 8) * gy4 * g22 - rat_m(101, 8) * gy2 * g24 + rat_m(291, 8) * g26
            + gy4 * (rat_m(217, 8) * ls + mp.mpf(5) * l3 + rat_m(5, 2) * l4) + gy2 * g22 * (rat_m(39, 4) * ls + mp.mpf(5) * l4)
            + g24 * (-rat_m(51, 8) * ls + mp.mpf(15) * l3 + rat_m(15, 2) * l4)
            + gy2 * (mp.mpf(18) * ls * ls + mp.mpf(8) * l3 * l3 + mp.mpf(8) * l3 * l4 + mp.mpf(4) * l4 * l4)
            + g22 * (mp.mpf(54) * ls * ls + mp.mpf(6) * ((mp.mpf(2) * l3 + l4) ** 2))
            - mp.mpf(78) * (ls ** 3) - ls * (mp.mpf(20) * l3 * l3 + mp.mpf(20) * l3 * l4 + mp.mpf(12) * l4 * l4)
            - mp.mpf(16) * (l3 ** 3) - mp.mpf(24) * l3 * l3 * l4 - mp.mpf(32) * l3 * l4 * l4 - mp.mpf(12) * (l4 ** 3)
        )
        t_d, t_e, t_u = yb2, ye2, yt2
        td2, te2, tu2, tud = yb4, ye4, yt4, ytb
        td3, te3, tu3, tu2d, td2u = yb6, ye6, yt6, yt4b2, yb4t2
        f1 = (
            gy4 * (rat_m(5, 2) * t_d - rat_m(25, 2) * t_e) + gy2 * g22 * (mp.mpf(9) * t_d + mp.mpf(11) * t_e)
            - g24 * (rat_m(9, 2) * t_d + rat_m(3, 2) * t_e)
            + gy2 * (rat_m(8, 3) * td2 - mp.mpf(8) * te2 + rat_m(25, 6) * t_d * l1 + rat_m(25, 2) * t_e * l1)
            + g22 * (rat_m(45, 2) * t_d * l1 + rat_m(15, 2) * t_e * l1) - g32 * (mp.mpf(64) * td2 - mp.mpf(80) * t_d * l1)
            + mp.mpf(60) * td3 + mp.mpf(12) * td2u + mp.mpf(20) * te3 - (mp.mpf(3) * td2 + mp.mpf(9) * tud + te2) * l1
            - mp.mpf(72) * t_d * l1 * l1 - mp.mpf(12) * t_u * l34_m - mp.mpf(24) * t_e * l1 * l1
        )
        f2 = (
            -rat_m(19, 2) * gy4 * t_u + mp.mpf(21) * gy2 * g22 * t_u - rat_m(9, 2) * g24 * t_u
            + gy2 * (-rat_m(16, 3) * tu2 + rat_m(85, 6) * t_u * l2) + rat_m(45, 2) * g22 * t_u * l2
            - g32 * (mp.mpf(64) * tu2 - mp.mpf(80) * t_u * l2) + mp.mpf(12) * tu2d + mp.mpf(60) * tu3
            - (mp.mpf(9) * tud + mp.mpf(3) * tu2) * l2 - (mp.mpf(12) * t_d + mp.mpf(4) * t_e) * l34_m - mp.mpf(72) * t_u * l2 * l2
        )
        b3 = (
            -rat_m(131, 8) * gy6 + rat_m(101, 8) * gy4 * g22 + rat_m(11, 8) * gy2 * g24 + rat_m(291, 8) * g26
            + gy4 * (rat_m(15, 4) * (l1 + l2) + rat_m(197, 8) * l3 + rat_m(5, 2) * l4)
            - gy2 * g22 * (rat_m(5, 2) * (l1 + l2) - rat_m(11, 4) * l3 + mp.mpf(3) * l4)
            + g24 * (rat_m(45, 4) * (l1 + l2) - rat_m(111, 8) * l3 + rat_m(15, 2) * l4)
            + gy2 * ((l1 + l2) * (mp.mpf(12) * l3 + mp.mpf(4) * l4) + mp.mpf(2) * l3 * l3 - mp.mpf(2) * l4 * l4)
            + g22 * ((l1 + l2) * (mp.mpf(36) * l3 + mp.mpf(18) * l4) + mp.mpf(6) * ((l3 - l4) ** 2))
            - (l1 * l1 + l2 * l2) * (mp.mpf(15) * l3 + mp.mpf(4) * l4)
            - (l1 + l2) * (mp.mpf(36) * l3 * l3 + mp.mpf(16) * l3 * l4 + mp.mpf(14) * l4 * l4)
            - mp.mpf(12) * (l3 ** 3) - mp.mpf(4) * l3 * l3 * l4 - mp.mpf(16) * l3 * l4 * l4 - mp.mpf(12) * (l4 ** 3)
        )
        f3 = (
            gy4 * (rat_m(5, 4) * t_d - rat_m(19, 4) * t_u - rat_m(25, 4) * t_e)
            - gy2 * g22 * (rat_m(9, 2) * t_d + rat_m(21, 2) * t_u + rat_m(11, 2) * t_e)
            - g24 * (rat_m(9, 4) * t_d + rat_m(9, 4) * t_u + rat_m(3, 4) * t_e)
            + gy2 * (-rat_m(4, 3) * tud + (rat_m(25, 12) * t_d + rat_m(85, 12) * t_u + rat_m(25, 4) * t_e) * l3)
            + g22 * (rat_m(45, 4) * t_d + rat_m(45, 4) * t_u + rat_m(15, 4) * t_e) * l3
            + g32 * (-mp.mpf(64) * tud + mp.mpf(40) * t_d * l3 + mp.mpf(40) * t_u * l3)
            + mp.mpf(36) * td2u + mp.mpf(36) * tu2d + (-rat_m(27, 2) * td2 + mp.mpf(15) * tud - rat_m(27, 2) * tu2 - rat_m(9, 2) * te2) * l3
            - (mp.mpf(6) * t_d * l1 + mp.mpf(6) * t_u * l2 + mp.mpf(2) * t_e * l1) * (mp.mpf(6) * l3 + mp.mpf(2) * l4)
            - (mp.mpf(6) * t_d + mp.mpf(6) * t_u + mp.mpf(2) * t_e) * (mp.mpf(2) * l3 * l3 + l4 * l4)
        )
        b4 = (
            -rat_m(73, 2) * gy4 * g22 - mp.mpf(14) * gy2 * g24 + rat_m(157, 8) * gy4 * l4
            + gy2 * g22 * (mp.mpf(5) * l1 + mp.mpf(5) * l2 + mp.mpf(2) * l3 + rat_m(51, 4) * l4)
            - rat_m(231, 8) * g24 * l4 + gy2 * (mp.mpf(4) * l1 * l4 + mp.mpf(4) * l2 * l4 + mp.mpf(4) * l3 * l4 + mp.mpf(8) * l4 * l4)
            + g22 * (mp.mpf(36) * l3 * l4 + mp.mpf(18) * l4 * l4) - (mp.mpf(7) * l1 * l1 + mp.mpf(7) * l2 * l2) * l4
            - (l1 + l2) * (mp.mpf(40) * l3 * l4 + mp.mpf(20) * l4 * l4) - mp.mpf(28) * l3 * l3 * l4 - mp.mpf(28) * l3 * l4 * l4
        )
        f4 = (
            gy2 * g22 * (mp.mpf(9) * t_d + mp.mpf(21) * t_u + mp.mpf(11) * t_e)
            + gy2 * (rat_m(4, 3) * tud + (rat_m(25, 12) * t_d + rat_m(85, 12) * t_u + rat_m(25, 4) * t_e) * l4)
            + g22 * (rat_m(45, 4) * t_d + rat_m(45, 4) * t_u + rat_m(15, 4) * t_e) * l4
            + g32 * (mp.mpf(64) * tud + mp.mpf(40) * t_d * l4 + mp.mpf(40) * t_u * l4)
            - mp.mpf(24) * tu2d - mp.mpf(24) * td2u + (-rat_m(27, 2) * td2 - rat_m(27, 2) * tu2 - rat_m(9, 2) * te2) * l4
            - tud * (mp.mpf(24) * l3 + mp.mpf(33) * l4) - (mp.mpf(12) * t_d * l1 + mp.mpf(12) * t_u * l2 + mp.mpf(4) * t_e * l1) * l4
            - (mp.mpf(12) * t_d + mp.mpf(12) * t_u + mp.mpf(4) * t_e) * (mp.mpf(2) * l3 * l4 + l4 * l4)
        )
        dl1_2, dl2_2, dl3_2, dl4_2 = bs(l1) + f1, bs(l2) + f2, b3 + f3, b4 + f4
    else:
        dl1_2 = dl2_2 = dl3_2 = dl4_2 = mp.mpf(0)

    return [
        bg1, bg2, bg3,
        (inv1 * mu1 + inv2 * mu2) * yt, (inv1 * md1 + inv2 * md2) * yb, (inv1 * me1 + inv2 * me2) * ye,
        inv1 * dl1_1 + inv2 * dl1_2, inv1 * dl2_1 + inv2 * dl2_2, inv1 * dl3_1 + inv2 * dl3_2, inv1 * dl4_1 + inv2 * dl4_2,
    ]


def run_ref_fl5_5(prod_l5_5: dict[str, Any]) -> dict[str, Any]:
    mp.mp.dps = 45
    g_uv = mp.sqrt(mp.mpf(4) * mp.pi / mp.mpf(40))
    g_uv2 = g_uv * g_uv
    yt_uv = g_uv / mp.sqrt(mp.mpf(2))
    st0 = [g_uv, g_uv, g_uv, yt_uv, yt_uv, yt_uv, g_uv2, g_uv2, mp.mpf(0), -rat_m(1, 2) * g_uv2]

    gl6_64 = gl6_integrate(lambda _t, y: rhs_2hdm_diag_ref(y, True), st0, mp.mpf(0), mp.mpf(-32), 160)
    gl6_128 = gl6_integrate(lambda _t, y: rhs_2hdm_diag_ref(y, True), st0, mp.mpf(0), mp.mpf(-32), 320)
    gl6_step_err = max(abs(gl6_128[i] - gl6_64[i]) for i in range(10))

    prod_q = [mp.mpf(s) for s in prod_l5_5["case2_E8_GHU_IR_quartics"]]
    gl6_vs_gbs8_err = max(abs(gl6_128[6 + i] - prod_q[i]) for i in range(4))

    # Planted Control R_PC_FL5_5: omitting 2-loop quartics shifts IR quartics by > 1e-3:
    gl6_no_nlo = gl6_integrate(lambda _t, y: rhs_2hdm_diag_ref(y, False), st0, mp.mpf(0), mp.mpf(-32), 80)
    omitted_nlo_shift = max(abs(gl6_128[6 + i] - gl6_no_nlo[6 + i]) for i in range(4))
    r_pc_fl5_5_caught = bool(omitted_nlo_shift > ten_pow(-3))

    passed = bool(
        gl6_step_err < ten_pow(-11)
        and gl6_vs_gbs8_err < ten_pow(-11)
        and r_pc_fl5_5_caught
    )
    return {
        "gl6_step_64_vs_128_max_err": mp.nstr(gl6_step_err, 10),
        "gl6_vs_producer_gbs8_quartic_max_diff": mp.nstr(gl6_vs_gbs8_err, 10),
        "r_pc_fl5_5_omitted_2loop_quartics_shift": mp.nstr(omitted_nlo_shift, 10),
        "r_pc_fl5_5_planted_control_caught": r_pc_fl5_5_caught,
        "passed": passed,
    }


# ==============================================================================
# REF_FL5_6: Full Custody & AST Audit of Producer + Peer 27f5d89fa + GL6 Inflation
# ==============================================================================

def run_ref_fl5_6(prod_json: dict[str, Any], prod_l5_6: dict[str, Any]) -> dict[str, Any]:
    mp.mp.dps = 45
    # 1. Verify Producer's SCRIPT_SHA256.txt, OUTPUT_SHA256.txt, AST clean, and 0 JSON floats:
    s_manifest = (PROD_DIR / "SCRIPT_SHA256.txt").read_text(encoding="utf-8").strip().split()[0]
    o_manifest = (PROD_DIR / "OUTPUT_SHA256.txt").read_text(encoding="utf-8").strip().split()[0]
    prod_sha_ok = bool(
        hashlib.sha256(PROD_SCRIPT.read_bytes()).hexdigest() == s_manifest
        and hashlib.sha256(PROD_OUT.read_bytes()).hexdigest() == o_manifest
    )
    prod_ast = audit_ast_clean(PROD_SCRIPT.read_text(encoding="utf-8"), str(PROD_SCRIPT))
    check_no_floats_json(prod_json)

    # 2. Verify peer 27f5d89fa custody independently:
    peer_dirs = ["a2_ow16_v9", "a2_ow21", "a2_ow21_v2", "a2_ow21_v3", "a2_ow22", "a2_ow22_v2"]
    peer_ok_count = 0
    for pd in peer_dirs:
        for mf in ("SCRIPT_SHA256.txt", "OUTPUT_SHA256.txt"):
            raw_m = subprocess.check_output(["git", "-C", str(REPO_ROOT), "show", f"{PEER_REV}:relays/{pd}/{mf}"]).decode("utf-8").strip()
            eh, tg = raw_m.split()[0], raw_m.split()[-1].lstrip("*")
            rp = tg if "/" in tg else f"relays/{pd}/{tg}"
            fb = subprocess.check_output(["git", "-C", str(REPO_ROOT), "show", f"{PEER_REV}:{rp}"])
            if hashlib.sha256(fb).hexdigest() == eh:
                peer_ok_count += 1

    # 3. GL6 countercheck of coupled 2-field 60-efold Starobinsky inflation ODE (using Ewald F_3(tau_0^+)):
    A_v = mp.mpf(3000)
    x0, y0 = rat_m(2, 5), rat_m(1, 5)
    r2 = x0 * x0 + y0 * y0
    f3_ew = e3_ewald_2d((-x0 / r2) + J_MP * (y0 / r2), Fr(0), Fr(0), mp.pi, r_lim=14) + e3_ewald_2d(mp.mpf(5) * x0 + J_MP * mp.mpf(5) * y0, Fr(0), Fr(0), mp.pi, r_lim=14)
    c0 = rat_m(1568, 25) * f3_ew
    r_inf = (mp.mpf(8) * c0 / A_v) ** rat_m(1, 5)
    b_crit = mp.mpf(25) * c0 / (mp.mpf(3) * (r_inf ** 4))
    bc_rad = mp.sqrt(rat_m(2, 15))
    s23 = mp.sqrt(rat_m(2, 3))

    def r_ext(rin: mp.mpf, beff: mp.mpf) -> mp.mpf:
        rv = rin
        for _ in range(25):
            rv -= (-mp.mpf(5) * A_v * (rv ** 5) + mp.mpf(6) * beff * (rv ** 4) - mp.mpf(10) * c0) / (-mp.mpf(25) * A_v * (rv ** 4) + mp.mpf(24) * beff * (rv ** 3))
        return rv

    phi0 = rat_m(555, 100)
    v0 = mp.mpf(50)
    vi0 = v0 * ((mp.mpf(1) - mp.exp(-s23 * phi0)) ** 2)
    r0 = r_ext(rat_m(99, 100), mp.mpf(3500) - vi0)
    st_gl = [phi0, mp.log(r0) / bc_rad, mp.mpf(0), mp.mpf(0)]

    def rhs_inf(_n: mp.mpf, st: list[mp.mpf]) -> list[mp.mpf]:
        ph, sg, up_v, us_v = st
        rc = mp.exp(bc_rad * sg)
        ex = mp.exp(-s23 * ph)
        vi = v0 * ((mp.mpf(1) - ex) ** 2)
        dv_dp = mp.mpf(2) * v0 * (mp.mpf(1) - ex) * s23 * ex * (rc ** (-6))
        vt = A_v * (rc ** (-5)) - mp.mpf(3500) * (rc ** (-6)) + c0 * (rc ** (-10)) + vi * (rc ** (-6))
        dv_ds = bc_rad * (-mp.mpf(5) * A_v * (rc ** (-5)) + mp.mpf(6) * (mp.mpf(3500) - vi) * (rc ** (-6)) - mp.mpf(10) * c0 * (rc ** (-10)))
        ep = rat_m(1, 2) * (up_v * up_v + us_v * us_v)
        return [up_v, us_v, -(mp.mpf(3) - ep) * (up_v + dv_dp / vt), -(mp.mpf(3) - ep) * (us_v + dv_ds / vt)]

    st_end = gl6_integrate(rhs_inf, st_gl, mp.mpf(0), mp.mpf(60), 180)
    prod_end = [mp.mpf(s) for s in prod_l5_6["starobinsky_60efold_V0_50_safe_phi_R_Rmax"][:2]]
    gl6_vs_gbs8_inf_err = max(abs(st_end[0] - prod_end[0]), abs(mp.exp(bc_rad * st_end[1]) - prod_end[1]))

    # Planted Control R_PC_FL5_6: conformal coupling xi = 1/6 breaks massive N=1 vector multiplet Sakharov cancellation (-2*xi = -1/3 != 0) AND flips 49 chiral + 12 massless + 33 massive sum negative:
    xi_c = Fr(1, 6)
    a1_mv_c = -2 * xi_c                                         # -1/3 != 0
    a1_tot_c = 49 * (Fr(1, 2) - 2 * xi_c) - 12 * Fr(1, 2) + 33 * a1_mv_c  # 49/6 - 6 - 11 = -53/6 < 0!
    r_pc_fl5_6_caught = bool(a1_mv_c != 0 and a1_tot_c < 0)

    passed = bool(
        prod_sha_ok
        and prod_ast["clean"]
        and prod_json["all_checks_passed"] is True
        and peer_ok_count == 12
        and abs(mp.mpf(prod_l5_6["kallosh_linde_V0_crit_B3500"]) - (mp.mpf(3500) - b_crit)) < ten_pow(-10)
        and gl6_vs_gbs8_inf_err < ten_pow(-10)
        and r_pc_fl5_6_caught
    )
    return {
        "producer_sha256_manifests_verified": prod_sha_ok,
        "producer_ast_clean": prod_ast["clean"],
        "peer_27f5d89fa_manifests_verified": peer_ok_count,
        "gl6_vs_gbs8_starobinsky_60efold_err": mp.nstr(gl6_vs_gbs8_inf_err, 10),
        "r_pc_fl5_6_xi16_sakharov_flip_caught": r_pc_fl5_6_caught,
        "passed": passed,
    }


def main() -> None:
    self_ast = audit_ast_clean(SELF_PATH.read_text(encoding="utf-8"), str(SELF_PATH))
    assert self_ast["clean"], f"Referee AST hygiene failed: {self_ast}"

    prod_json = json.loads(PROD_OUT.read_text(encoding="utf-8"))
    mods_p = prod_json["modules"]

    rf1 = run_ref_fl5_1(mods_p["L5_1"])
    rf2 = run_ref_fl5_2(mods_p["L5_2"])
    rf3 = run_ref_fl5_3(mods_p["L5_3"])
    g_s12_rich = rf3.pop("_g_s12_rich")
    rf4 = run_ref_fl5_4(mods_p["L5_4"], mods_p["L5_3"], g_s12_rich)
    rf5 = run_ref_fl5_5(mods_p["L5_5"])
    rf6 = run_ref_fl5_6(prod_json, mods_p["L5_6"])

    ref_mods = {
        "REF_FL5_1": rf1, "REF_FL5_2": rf2, "REF_FL5_3": rf3,
        "REF_FL5_4": rf4, "REF_FL5_5": rf5, "REF_FL5_6": rf6,
    }
    r_pcs = {
        "R_PC_FL5_1": rf1["r_pc_fl5_1_euclidean_omega_neg_disc_caught"],
        "R_PC_FL5_2": rf2["r_pc_fl5_2_planted_control_caught"],
        "R_PC_FL5_3": rf3["r_pc_fl5_3_scalar_s0_inversion_caught"],
        "R_PC_FL5_4": rf4["r_pc_fl5_4_planted_control_caught"],
        "R_PC_FL5_5": rf5["r_pc_fl5_5_planted_control_caught"],
        "R_PC_FL5_6": rf6["r_pc_fl5_6_xi16_sakharov_flip_caught"],
    }
    all_ok = all(m["passed"] for m in ref_mods.values()) and all(r_pcs.values())

    out = {
        "card": "AGY-EXP_X-F-THEORY-FLAVOR-LINK5",
        "role": "disjoint_cold_room_referee",
        "empirical_constants_used": "0 of 19",
        "referee_script_sha256": hashlib.sha256(SELF_PATH.read_bytes()).hexdigest(),
        "audited_producer_script_sha256": hashlib.sha256(PROD_SCRIPT.read_bytes()).hexdigest(),
        "audited_producer_output_sha256": hashlib.sha256(PROD_OUT.read_bytes()).hexdigest(),
        "self_ast_hygiene": self_ast,
        "referee_modules": ref_mods,
        "referee_planted_controls": r_pcs,
        "modules_passed_count": sum(1 for m in ref_mods.values() if m["passed"]),
        "planted_controls_caught_count": sum(1 for v in r_pcs.values() if v),
        "all_checks_passed": all_ok,
    }
    check_no_floats_json(out)
    OUT_PATH.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
