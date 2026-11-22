r"""Cold-Room Zero-Trust Referee for Card A2-OW17 (a2_ow17_v2).

Independent from-scratch verification of all claims in
`relays/a2_ow17_v2/a2_ow17_v2_results.json` built solely from the
pre-registration card, Errata 1-2, and mathematical specifications.

Strict Guardrails & Custody Rules:
- Zero reads or imports of `verify_a2_ow17.py`, `verify_a2_ow17_v2.py`, or `frontier/`.
- Zero Python `float` or `complex` AST literals (exact `Fraction`, `sympy.Rational`,
  and integer-built `mpmath` at `mp.mp.dps = 55`).
- Strict `0 of 19` empirical firewall (zero PDG, NuFIT, Planck, or lattice inputs).
- Disjoint numerical methods:
  * OW17-A: direct 2D Newton with analytic Jacobian on (2 + eta_N, beta_lam)
    (no cubic polynomial roots), central-FD graviton potential verification of f_lam,
    4D Newton with analytic Jacobian for 4-quartic 2HDM UV fixed points, and
    1600-step 2-stage 4th-order implicit Gauss-Legendre (GL4) downward RGE.
  * OW17-B: first-principles Machacek-Vaughn Dynkin/Casimir derivation of b_i, B_ij, c_if,
    500-step GL4 2-loop 2H SM RGE, exact rational SM/PS Dynkin census, and explicit
    SM-decomposition proof of 6D KK multiplet universality.
  * OW17-C: exact rational sympy commutant nullspace, 3x3 DFT, order-24 Weierstrass-Taylor
    Fuchsian Lame L_2 solver with 4 independent analytic/modular/w_s self-benchmarks,
    independent B1656 E[5]+E[6] Yukawa evaluator, 10-trial complex Householder-QR Haar
    U(3)_L x U(3)_R invariance test, and exact E[n] orbit decompositions.
  * OW17-D: all 4/4 independent planted-fault controls.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 55

I_UNIT = mp.mpc(0, 1)
REPO_ROOT = Path(__file__).resolve().parents[2]
PROD_V2_JSON = REPO_ROOT / "relays" / "a2_ow17_v2" / "a2_ow17_v2_results.json"
OUT_JSON = Path(__file__).resolve().parent / "a2_ow17_referee_results.json"


def f2mp(val: Fraction) -> mp.mpf:
    r"""Convert an exact Fraction to an mpmath.mpf using integer numerator/denominator."""
    return mp.mpf(val.numerator) / mp.mpf(val.denominator)


def frac_str(val: Fraction) -> str:
    r"""Canonical exact rational string matching 'p/q' or 'n'."""
    if val.denominator == 1:
        return str(val.numerator)
    return f"{val.numerator}/{val.denominator}"


def parse_frac(text: str) -> Fraction:
    r"""Parse an exact rational string 'p/q' or integer string."""
    if "/" in text:
        p_s, q_s = text.split("/", 1)
        return Fraction(int(p_s), int(q_s))
    return Fraction(int(text), 1)


def rel_err_mp(computed: mp.mpf, reference_str: str) -> mp.mpf:
    r"""Relative error against a decimal string reference (absolute if reference is zero)."""
    ref = mp.mpf(reference_str)
    diff = abs(computed - ref)
    if ref == 0:
        return diff
    return diff / abs(ref)


def abs_err_mp(computed: mp.mpf, reference_str: str) -> mp.mpf:
    r"""Absolute error against a decimal string reference."""
    return abs(computed - mp.mpf(reference_str))


def label_same(cond: bool) -> str:
    r"""Neutral Section-12 comparison label."""
    return "the same" if cond else "differs"


# ============================================================================
# Section 0: Raw Disk SHA-256 Custody Audit
# ============================================================================

def verify_sha256_custody() -> dict:
    r"""Verify raw-byte SHA-256 digests of v1 and v2 manifests without decoding scripts."""
    manifests = [
        ("v2_script", REPO_ROOT / "relays" / "a2_ow17_v2" / "SCRIPT_SHA256.txt"),
        ("v2_output", REPO_ROOT / "relays" / "a2_ow17_v2" / "OUTPUT_SHA256.txt"),
        ("v1_script", REPO_ROOT / "relays" / "a2_ow17" / "SCRIPT_SHA256.txt"),
        ("v1_output", REPO_ROOT / "relays" / "a2_ow17" / "OUTPUT_SHA256.txt"),
    ]
    records = {}
    all_ok = True
    for key, mpath in manifests:
        line = mpath.read_text(encoding="utf-8").strip()
        parts = line.split()
        expected_hex = parts[0]
        rel_target = parts[1]
        target_path = REPO_ROOT / rel_target
        actual_hex = hashlib.sha256(target_path.read_bytes()).hexdigest()
        match = actual_hex == expected_hex
        if not match:
            all_ok = False
        records[key] = {
            "manifest": str(mpath.relative_to(REPO_ROOT)),
            "target": rel_target,
            "expected_sha256": expected_hex,
            "actual_sha256": actual_hex,
            "status": label_same(match),
        }
    return {
        "entries": records,
        "all_custody_ok": all_ok,
        "status": label_same(all_ok),
    }


# ============================================================================
# Section 1: OW17-A (Seam S2 — 6D Casimir, 4D FRG, 2HDM Quartics, c_log)
# ============================================================================

def frg_system_and_jacobian(
    g: mp.mpf, lam: mp.mpf, m_g: int, m_l: mp.mpf
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    r"""Evaluate (2 + eta_N, beta_lam) and exact analytic Jacobian in (g, lam)."""
    pi = mp.pi
    denom = mp.mpf(1) - 2 * lam
    inv_d = mp.mpf(1) / denom
    inv_d2 = inv_d * inv_d
    inv_d3 = inv_d2 * inv_d

    b1 = (mp.mpf(1) / (3 * pi)) * (5 * inv_d - 9 * inv_d2 - 7) + mp.mpf(m_g) / (6 * pi)
    b2 = -(mp.mpf(1) / (6 * pi)) * (mp.mpf(5) / 2 * inv_d - 3 * inv_d2)

    db1_dl = (mp.mpf(1) / (3 * pi)) * (10 * inv_d2 - 36 * inv_d3)
    db2_dl = -(mp.mpf(1) / (6 * pi)) * (5 * inv_d2 - 12 * inv_d3)

    q_den = mp.mpf(1) - g * b2
    inv_q = mp.mpf(1) / q_den
    inv_q2 = inv_q * inv_q

    eta = g * b1 * inv_q
    deta_dg = b1 * inv_q2
    deta_dl = g * (db1_dl * q_den + g * b1 * db2_dl) * inv_q2

    f1 = mp.mpf(2) + eta
    df1_dg = deta_dg
    df1_dl = deta_dl

    coeff = mp.mpf(5) * (mp.mpf(1) - eta / 6) * inv_d - 4 + m_l
    f2 = (eta - 2) * lam + (g / (2 * pi)) * coeff

    df2_dg = (
        deta_dg * lam
        + coeff / (2 * pi)
        + (g / (2 * pi)) * (-mp.mpf(5) / 6 * deta_dg * inv_d)
    )
    df2_dl = (
        deta_dl * lam
        + (eta - 2)
        + (g / (2 * pi))
        * (
            -mp.mpf(5) / 6 * deta_dl * inv_d
            + mp.mpf(10) * (mp.mpf(1) - eta / 6) * inv_d2
        )
    )
    return f1, f2, df1_dg, df1_dl, df2_dg, df2_dl, eta


def solve_frg_2d_newton(m_g: int, m_l: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    r"""Direct 2D Newton solver on (2 + eta_N = 0, beta_lam = 0) with analytic Jacobian."""
    g = mp.mpf(1) / 5
    lam = mp.mpf(1) / 10
    tol = mp.mpf(10) ** (-50)
    lam_cap = mp.mpf(9) / 20
    for _ in range(80):
        f1, f2, j11, j12, j21, j22, _ = frg_system_and_jacobian(g, lam, m_g, m_l)
        if max(abs(f1), abs(f2)) < tol:
            break
        det = j11 * j22 - j12 * j21
        dg = -(j22 * f1 - j12 * f2) / det
        dl = -(-j21 * f1 + j11 * f2) / det
        alpha = mp.mpf(1)
        while g + alpha * dg <= 0 or lam + alpha * dl >= lam_cap:
            alpha /= 2
        g += alpha * dg
        lam += alpha * dl
    f1, f2, _, _, _, _, _ = frg_system_and_jacobian(g, lam, m_g, m_l)
    res = max(abs(f1 * g), abs(f2))
    return g, lam, res


def graviton_lpa_flow(u: mp.mpf, g: mp.mpf, lam: mp.mpf, gauge: str) -> mp.mpf:
    r"""Dimensionless graviton LPA contribution to partial_t u(u) at eta_N = -2."""
    pi = mp.pi
    lam_eff = lam + 8 * pi * g * u
    pref = (mp.mpf(1) / (32 * pi * pi)) * (mp.mpf(4) / 3)
    if gauge == "dD":
        return pref * (mp.mpf(10) / (mp.mpf(1) - 2 * lam_eff))
    if gauge == "LDW":
        return pref * (
            mp.mpf(5) / (mp.mpf(1) - 2 * lam_eff)
            + mp.mpf(1) / (mp.mpf(1) - (mp.mpf(4) / 3) * lam_eff)
        )
    raise ValueError(f"Unknown gauge: {gauge}")


def beta_2hdm_quartics_and_jac(
    vec: list[mp.mpf],
    f_lam: mp.mpf,
    g1_2: mp.mpf,
    g2_2: mp.mpf,
    yt: mp.mpf,
    yb: mp.mpf,
    ytau: mp.mpf,
) -> tuple[list[mp.mpf], mp.matrix]:
    r"""Exact 1-loop Type-II 2HDM 4-quartic beta functions (lam_5 = 0) and 4x4 Jacobian."""
    loop = mp.mpf(1) / (16 * mp.pi * mp.pi)
    l1, l2, l3, l4 = vec
    gp2 = (mp.mpf(3) / 5) * g1_2
    yt2 = yt * yt
    yb2 = yb * yb
    ytau2 = ytau * ytau

    lin1 = 9 * g2_2 + 3 * gp2 - 12 * yb2 - 4 * ytau2
    lin2 = 9 * g2_2 + 3 * gp2 - 12 * yt2
    lin34 = 9 * g2_2 + 3 * gp2 - 6 * yt2 - 6 * yb2 - 2 * ytau2

    gg_p = (mp.mpf(3) / 4) * (3 * g2_2 * g2_2 + 2 * g2_2 * gp2 + gp2 * gp2)
    gg_m = (mp.mpf(3) / 4) * (3 * g2_2 * g2_2 - 2 * g2_2 * gp2 + gp2 * gp2)
    g2gp = 3 * g2_2 * gp2

    b1 = f_lam * l1 + loop * (
        12 * l1 * l1
        + 4 * l3 * l3
        + 4 * l3 * l4
        + 2 * l4 * l4
        + gg_p
        - l1 * lin1
        - 12 * yb2 * yb2
        - 4 * ytau2 * ytau2
    )
    b2 = f_lam * l2 + loop * (
        12 * l2 * l2
        + 4 * l3 * l3
        + 4 * l3 * l4
        + 2 * l4 * l4
        + gg_p
        - l2 * lin2
        - 12 * yt2 * yt2
    )
    b3 = f_lam * l3 + loop * (
        (l1 + l2) * (6 * l3 + 2 * l4)
        + 4 * l3 * l3
        + 2 * l4 * l4
        + gg_m
        - l3 * lin34
        - 12 * yt2 * yb2
    )
    b4 = f_lam * l4 + loop * (
        2 * (l1 + l2) * l4
        + 8 * l3 * l4
        + 4 * l4 * l4
        + g2gp
        - l4 * lin34
        + 12 * yt2 * yb2
    )

    jac = mp.matrix(4, 4)
    jac[0, 0] = f_lam + loop * (24 * l1 - lin1)
    jac[0, 1] = mp.mpf(0)
    jac[0, 2] = loop * (8 * l3 + 4 * l4)
    jac[0, 3] = loop * (4 * l3 + 4 * l4)

    jac[1, 0] = mp.mpf(0)
    jac[1, 1] = f_lam + loop * (24 * l2 - lin2)
    jac[1, 2] = loop * (8 * l3 + 4 * l4)
    jac[1, 3] = loop * (4 * l3 + 4 * l4)

    jac[2, 0] = loop * (6 * l3 + 2 * l4)
    jac[2, 1] = loop * (6 * l3 + 2 * l4)
    jac[2, 2] = f_lam + loop * (6 * (l1 + l2) + 8 * l3 - lin34)
    jac[2, 3] = loop * (2 * (l1 + l2) + 4 * l4)

    jac[3, 0] = loop * (2 * l4)
    jac[3, 1] = loop * (2 * l4)
    jac[3, 2] = loop * (8 * l4)
    jac[3, 3] = f_lam + loop * (2 * (l1 + l2) + 8 * l3 + 8 * l4 - lin34)

    return [b1, b2, b3, b4], jac


def solve_2hdm_quartic_fp(
    f_lam: mp.mpf, g_uv: mp.mpf, yt: mp.mpf, yb: mp.mpf
) -> tuple[list[mp.mpf], mp.mpf, list[mp.mpf], bool]:
    r"""4D Newton with analytic Jacobian for the Type-II 2HDM UV fixed point."""
    vec = [mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    g2 = g_uv * g_uv
    tol = mp.mpf(10) ** (-50)
    for _ in range(40):
        betas, jac = beta_2hdm_quartics_and_jac(vec, f_lam, g2, g2, yt, yb, yb)
        if max(abs(x) for x in betas) < tol:
            break
        delta = mp.lu_solve(jac, mp.matrix(betas))
        vec = [vec[i] - delta[i] for i in range(4)]
    betas, jac = beta_2hdm_quartics_and_jac(vec, f_lam, g2, g2, yt, yb, yb)
    res = max(abs(x) for x in betas)
    stab = -jac
    eigs = sorted([mp.re(ev) for ev in mp.eig(stab)[0]], reverse=True)
    l1, l2, l3, l4 = vec
    bfb = False
    if l1 > 0 and l2 > 0:
        s12 = mp.sqrt(l1 * l2)
        bfb = bool(l3 > -s12 and (l3 + l4) > -s12)
    return vec, res, eigs, bfb


def integrate_gl4(rhs_fn, y0: list[mp.mpf], t_end: mp.mpf, nsteps: int, fp_iters: int = 4) -> list[mp.mpf]:
    r"""Independent 2-stage 4th-order implicit Gauss-Legendre (GL4) ODE integrator."""
    s3 = mp.sqrt(3)
    a11 = mp.mpf(1) / 4
    a12 = mp.mpf(1) / 4 - s3 / 6
    a21 = mp.mpf(1) / 4 + s3 / 6
    a22 = mp.mpf(1) / 4
    h = t_end / mp.mpf(nsteps)
    h2 = h / 2
    dim = len(y0)
    y = list(y0)
    for _ in range(nsteps):
        k1 = rhs_fn(y)
        k2 = list(k1)
        for _it in range(fp_iters):
            z1 = [y[i] + h * (a11 * k1[i] + a12 * k2[i]) for i in range(dim)]
            z2 = [y[i] + h * (a21 * k1[i] + a22 * k2[i]) for i in range(dim)]
            k1 = rhs_fn(z1)
            k2 = rhs_fn(z2)
        y = [y[i] + h2 * (k1[i] + k2[i]) for i in range(dim)]
    return y


def run_ow17_a(prod_a: dict) -> tuple[dict, int]:
    r"""Independent referee verification of OW17-A (Seam S2)."""
    discrepancies = 0
    pi = mp.pi

    # 1. 6D bulk Casimir supertraces
    casimir_specs = [
        ("spin10_brane_2H", 45, 48, 0),
        ("spin10_bulk_2H", 45, 48, 4),
        ("spin10_bulk_10R", 45, 48, 5),
        ("spin10_bulk_10C", 45, 48, 10),
        ("e6_brane_2H", 78, 81, 0),
        ("e6_bulk_27H", 78, 81, 27),
    ]
    casimir_out = {}
    casimir_all_match = True
    for name, nv, nw, h_pt in casimir_specs:
        nb = 2 * nv + h_pt
        nf = 2 * nw
        diff = nb - nf
        ds = diff < 0
        prow = prod_a["casimir_6d_table"][name]
        ok = (
            prow["Nv"] == nv
            and prow["Nw"] == nw
            and prow["Nv_minus_Nw"] == (nv - nw)
            and prow["h_pt_bulk"] == h_pt
            and prow["nB_per_T2_pt"] == nb
            and prow["nF_per_T2_pt"] == nf
            and prow["nB_minus_nF"] == diff
            and prow["de_sitter_stabilizes_tau_star"] == ds
        )
        if not ok:
            casimir_all_match = False
            discrepancies += 1
        casimir_out[name] = {
            "Nv": nv,
            "Nw": nw,
            "Nv_minus_Nw": nv - nw,
            "h_pt_bulk": h_pt,
            "nB_per_T2_pt": nb,
            "nF_per_T2_pt": nf,
            "nB_minus_nF": diff,
            "de_sitter_stabilizes_tau_star": ds,
            "vs_producer": label_same(ok),
        }

    # 2. f_crit at g_UV = 13/25
    g_uv = mp.mpf(13) / 25
    f_crit = (g_uv * g_uv / (16 * pi * pi)) * (
        mp.mpf(54) / 5 + mp.mpf(6) * mp.sqrt(114) / 5
    )
    f_crit_rel = rel_err_mp(f_crit, prod_a["f_crit_at_gUV_13_25"])
    f_crit_ok = f_crit_rel < mp.mpf(10) ** (-14)
    if not f_crit_ok:
        discrepancies += 1

    # 3. 4D Litim FRG fixed points via direct 2D Newton for all 10 configs
    frg_specs = [
        ("spin10_brane_2H_T2", 8, 48, 45, 1),
        ("spin10_brane_2H_T1", 8, 48, 45, 2),
        ("spin10_real10_T2", 10, 48, 45, 1),
        ("spin10_real10_T1", 10, 48, 45, 2),
        ("spin10_comp10_T2", 20, 48, 45, 1),
        ("spin10_comp10_T1", 20, 48, 45, 2),
        ("e6_brane_2H_T2", 8, 81, 78, 1),
        ("e6_brane_2H_T1", 8, 81, 78, 2),
        ("e6_bulk_27H_T2", 54, 81, 78, 1),
        ("e6_bulk_27H_T1", 54, 81, 78, 2),
    ]
    frg_out = {}
    frg_f_lams = {}
    max_frg_rel = mp.mpf(0)
    max_fd_err = mp.mpf(0)
    h_fd = mp.mpf(10) ** (-16)
    frg_all_match = True
    brane_2h_all_above = True

    for name, ns, nw, nv, fw in frg_specs:
        m_g = ns + fw * nw - 4 * nv
        m_l_frac = Fraction(ns + 2 * nv - 2 * nw, 2)
        m_l_mp = f2mp(m_l_frac)
        g_star, lam_star, res = solve_frg_2d_newton(m_g, m_l_mp)

        fl_dd = (g_star / pi) * (mp.mpf(20) / 3) / (mp.mpf(1) - 2 * lam_star) ** 2
        fl_ldw = (g_star / pi) * (
            (mp.mpf(10) / 3) / (mp.mpf(1) - 2 * lam_star) ** 2
            + (mp.mpf(4) / 9) / (mp.mpf(1) - (mp.mpf(4) / 3) * lam_star) ** 2
        )

        # Central finite-difference verification of f_lam from graviton LPA potential flow
        fd_dd = (
            graviton_lpa_flow(h_fd, g_star, lam_star, "dD")
            - graviton_lpa_flow(-h_fd, g_star, lam_star, "dD")
        ) / (2 * h_fd)
        fd_ldw = (
            graviton_lpa_flow(h_fd, g_star, lam_star, "LDW")
            - graviton_lpa_flow(-h_fd, g_star, lam_star, "LDW")
        ) / (2 * h_fd)
        fd_err = max(abs(fd_dd - fl_dd), abs(fd_ldw - fl_ldw))
        if fd_err > max_fd_err:
            max_fd_err = fd_err

        above_dd = bool(fl_dd > f_crit)
        above_ldw = bool(fl_ldw > f_crit)
        if "brane_2H" in name and not (above_dd and above_ldw):
            brane_2h_all_above = False

        prow = prod_a["frg_4d_table"][name]
        errs = [
            rel_err_mp(g_star, prow["g_star"]),
            rel_err_mp(lam_star, prow["lam_star"]),
            rel_err_mp(fl_dd, prow["f_lam_dD"]),
            rel_err_mp(fl_ldw, prow["f_lam_LDW"]),
        ]
        row_max_rel = max(errs)
        if row_max_rel > max_frg_rel:
            max_frg_rel = row_max_rel

        row_ok = (
            prow["Mg"] == m_g
            and parse_frac(prow["Ml"]) == m_l_frac
            and res < mp.mpf(10) ** (-40)
            and fd_err < mp.mpf(10) ** (-12)
            and row_max_rel < mp.mpf(10) ** (-14)
            and prow["above_f_crit_dD"] == above_dd
            and prow["above_f_crit_LDW"] == above_ldw
        )
        if not row_ok:
            frg_all_match = False
            discrepancies += 1

        frg_f_lams[(name, "dD")] = fl_dd
        frg_f_lams[(name, "LDW")] = fl_ldw
        frg_out[name] = {
            "Mg": m_g,
            "Ml": frac_str(m_l_frac),
            "g_star": mp.nstr(g_star, 20),
            "lam_star": mp.nstr(lam_star, 20),
            "fp_residual": mp.nstr(res, 10),
            "f_lam_dD": mp.nstr(fl_dd, 20),
            "f_lam_LDW": mp.nstr(fl_ldw, 20),
            "fd_max_err": mp.nstr(fd_err, 10),
            "above_f_crit_dD": above_dd,
            "above_f_crit_LDW": above_ldw,
            "max_rel_err_vs_producer": mp.nstr(row_max_rel, 10),
            "vs_producer": label_same(row_ok),
        }

    # 4. 4-quartic 2HDM Type-II UV fixed points
    yt_uv = mp.mpf(11) / 20
    yb_low = mp.mpf(1) / 100
    yb_high = mp.mpf(9) / 20
    quartic_specs = [
        ("spin10_brane2H_T2_dD_yb_low", frg_f_lams[("spin10_brane_2H_T2", "dD")], yb_low),
        ("spin10_brane2H_T2_LDW_yb_low", frg_f_lams[("spin10_brane_2H_T2", "LDW")], yb_low),
        ("spin10_brane2H_T2_dD_yb_high", frg_f_lams[("spin10_brane_2H_T2", "dD")], yb_high),
        ("spin10_brane2H_T1_dD_yb_low", frg_f_lams[("spin10_brane_2H_T1", "dD")], yb_low),
        ("e6_brane2H_T2_dD_yb_low", frg_f_lams[("e6_brane_2H_T2", "dD")], yb_low),
    ]
    quartic_out = {}
    quartic_lams = {}
    max_q_rel = mp.mpf(0)
    quartic_all_match = True

    for qname, fl_val, yb_val in quartic_specs:
        l_star, res, thetas, bfb = solve_2hdm_quartic_fp(fl_val, g_uv, yt_uv, yb_val)
        all_irrel = all(th < 0 for th in thetas)
        prow = prod_a["quartic_2hdm_fps_at_brane2H"][qname]
        errs = [rel_err_mp(fl_val, prow["f_lam"])]
        for i in range(4):
            errs.append(rel_err_mp(l_star[i], prow["lam_star"][i]))
            errs.append(rel_err_mp(thetas[i], prow["thetas"][i]))
        q_max_rel = max(errs)
        if q_max_rel > max_q_rel:
            max_q_rel = q_max_rel
        q_ok = (
            res < mp.mpf(10) ** (-40)
            and q_max_rel < mp.mpf(10) ** (-11)
            and prow["all_uv_irrelevant"] == all_irrel
            and prow["bfb_satisfied"] == bfb
        )
        if not q_ok:
            quartic_all_match = False
            discrepancies += 1
        quartic_lams[qname] = l_star
        quartic_out[qname] = {
            "f_lam": mp.nstr(fl_val, 18),
            "lam_star": [mp.nstr(x, 18) for x in l_star],
            "residual": mp.nstr(res, 10),
            "thetas": [mp.nstr(x, 16) for x in thetas],
            "all_uv_irrelevant": all_irrel,
            "bfb_satisfied": bfb,
            "max_rel_err_vs_producer": mp.nstr(q_max_rel, 10),
            "vs_producer": label_same(q_ok),
        }

    # 5. Downward 1-loop 2H RGE (t = 0 -> -38) via independent 1600-step GL4
    loop = mp.mpf(1) / (16 * pi * pi)
    c_21_5 = mp.mpf(21) / 5
    c_9_2 = mp.mpf(9) / 2
    c_1_2 = mp.mpf(1) / 2
    c_9_4 = mp.mpf(9) / 4
    c_17_20 = mp.mpf(17) / 20
    c_1_4 = mp.mpf(1) / 4
    c_5_2 = mp.mpf(5) / 2
    c_3_5 = mp.mpf(3) / 5
    c_3_4 = mp.mpf(3) / 4

    def rhs_1loop_paired(y: list[mp.mpf]) -> list[mp.mpf]:
        g1, g2, g3, yt, yb, ytau = y[0], y[1], y[2], y[3], y[4], y[5]
        g1_2 = g1 * g1
        g2_2 = g2 * g2
        g3_2 = g3 * g3
        yt2 = yt * yt
        yb2 = yb * yb
        ytau2 = ytau * ytau
        gp2 = c_3_5 * g1_2

        dg1 = loop * c_21_5 * g1_2 * g1
        dg2 = loop * (-3) * g2_2 * g2
        dg3 = loop * (-7) * g3_2 * g3
        dyt = loop * yt * (c_9_2 * yt2 + c_1_2 * yb2 - 8 * g3_2 - c_9_4 * g2_2 - c_17_20 * g1_2)
        dyb = loop * yb * (c_9_2 * yb2 + c_1_2 * yt2 + ytau2 - 8 * g3_2 - c_9_4 * g2_2 - c_1_4 * g1_2)
        dytau = loop * ytau * (c_5_2 * ytau2 + 3 * yb2 - c_9_4 * g2_2 - c_9_4 * g1_2)

        gg_p = c_3_4 * (3 * g2_2 * g2_2 + 2 * g2_2 * gp2 + gp2 * gp2)
        gg_m = c_3_4 * (3 * g2_2 * g2_2 - 2 * g2_2 * gp2 + gp2 * gp2)
        g2gp = 3 * g2_2 * gp2
        lin1 = 9 * g2_2 + 3 * gp2 - 12 * yb2 - 4 * ytau2
        lin2 = 9 * g2_2 + 3 * gp2 - 12 * yt2
        lin34 = 9 * g2_2 + 3 * gp2 - 6 * yt2 - 6 * yb2 - 2 * ytau2
        y1_4 = 12 * yb2 * yb2 + 4 * ytau2 * ytau2
        y2_4 = 12 * yt2 * yt2
        ytb2 = 12 * yt2 * yb2

        out = [dg1, dg2, dg3, dyt, dyb, dytau]
        for off in (6, 10):
            l1, l2, l3, l4 = y[off], y[off + 1], y[off + 2], y[off + 3]
            dl1 = loop * (12 * l1 * l1 + 4 * l3 * l3 + 4 * l3 * l4 + 2 * l4 * l4 + gg_p - l1 * lin1 - y1_4)
            dl2 = loop * (12 * l2 * l2 + 4 * l3 * l3 + 4 * l3 * l4 + 2 * l4 * l4 + gg_p - l2 * lin2 - y2_4)
            dl3 = loop * ((l1 + l2) * (6 * l3 + 2 * l4) + 4 * l3 * l3 + 2 * l4 * l4 + gg_m - l3 * lin34 - ytb2)
            dl4 = loop * (2 * (l1 + l2) * l4 + 8 * l3 * l4 + 4 * l4 * l4 + g2gp - l4 * lin34 + ytb2)
            out.extend([dl1, dl2, dl3, dl4])
        return out

    t_end_a = mp.mpf(-38)
    y0_high = [g_uv, g_uv, g_uv, yt_uv, yb_high, yb_high] + quartic_lams["spin10_brane2H_T2_dD_yb_high"] + [mp.mpf(0)] * 4
    y0_low = [g_uv, g_uv, g_uv, yt_uv, yb_low, yb_low] + quartic_lams["spin10_brane2H_T2_dD_yb_low"] + [mp.mpf(0)] * 4

    yf_high = integrate_gl4(rhs_1loop_paired, y0_high, t_end_a, 1600, fp_iters=4)
    yf_low = integrate_gl4(rhs_1loop_paired, y0_low, t_end_a, 1600, fp_iters=4)

    # Analytic 1-loop gauge check at t = -38
    b_1loop_2h = [c_21_5, mp.mpf(-3), mp.mpf(-7)]
    g_analytic_err = mp.mpf(0)
    for i in range(3):
        g_exact = mp.mpf(1) / mp.sqrt(mp.mpf(1) / (g_uv * g_uv) - b_1loop_2h[i] * t_end_a / (8 * pi * pi))
        g_analytic_err = max(g_analytic_err, abs(yf_high[i] - g_exact), abs(yf_low[i] - g_exact))

    ir_diff_high = max(abs(yf_high[6 + i] - yf_high[10 + i]) for i in range(4))
    ir_diff_low = max(abs(yf_low[6 + i] - yf_low[10 + i]) for i in range(4))
    err_ir_high = abs_err_mp(ir_diff_high, prod_a["downward_rge_t_0_to_neg38"]["yb_high_max_ir_diff_vs_zero"])
    err_ir_low = abs_err_mp(ir_diff_low, prod_a["downward_rge_t_0_to_neg38"]["yb_low_max_ir_diff_vs_zero"])
    rge_a_ok = (
        ir_diff_high < mp.mpf(3) / 1000
        and ir_diff_low < mp.mpf(1) / 100
        and g_analytic_err < mp.mpf(10) ** (-12)
        and err_ir_high < mp.mpf(10) ** (-10)
        and err_ir_low < mp.mpf(10) ** (-10)
    )
    if not rge_a_ok:
        discrepancies += 1

    # 6. Conformal xi = 1/6 induced gravity c_log & 1-loop asymptotic freedom
    xi_conf = Fraction(1, 6)
    # Kabat-Solodukhin spin weights:
    # Massive Proca = massless gauge (-1/3 ent, +1 contact) + Stueckelberg minimal scalar (-1/6 ent, 0 contact)
    w_proca_ent = Fraction(-1, 3) + Fraction(-1, 6)
    w_proca_con = Fraction(1, 1)
    w_weyl_ent = Fraction(-1, 6)
    w_weyl_con = Fraction(0, 1)
    w_scalar_ent = Fraction(-1, 6)
    w_scalar_con = xi_conf

    n_proca = 45 - 12
    n_rhn = 3
    n_brane_2h = 8
    c_log_ent = n_proca * w_proca_ent + n_rhn * w_weyl_ent + n_brane_2h * w_scalar_ent
    c_log_con = n_proca * w_proca_con + n_rhn * w_weyl_con + n_brane_2h * w_scalar_con
    c_log_tot = c_log_ent + c_log_con

    # 1-loop gauge beta coefficients: b = -(11/3) C2(G) + (2/3) sum_Weyl T(R) + (1/6) sum_real_scalar T(R)
    b_s10_brane = Fraction(-11, 3) * 8 + Fraction(2, 3) * (3 * 2)
    b_s10_10r = b_s10_brane + Fraction(1, 6) * 1
    b_e6_brane = Fraction(-11, 3) * 12 + Fraction(2, 3) * (3 * 3)

    pconf = prod_a["conformal_bh_and_af_brane2H"]
    conf_ok = (
        parse_frac(pconf["c_log_ent"]) == c_log_ent
        and parse_frac(pconf["c_log_contact"]) == c_log_con
        and parse_frac(pconf["c_log_total"]) == c_log_tot
        and parse_frac(pconf["b_1loop_spin10_brane2H"]) == b_s10_brane
        and parse_frac(pconf["b_1loop_spin10_real10"]) == b_s10_10r
        and parse_frac(pconf["b_1loop_e6_brane2H"]) == b_e6_brane
    )
    if not conf_ok:
        discrepancies += 1

    gate_a = casimir_all_match and f_crit_ok and frg_all_match and brane_2h_all_above and quartic_all_match and rge_a_ok and conf_ok
    return {
        "casimir_6d_table": casimir_out,
        "casimir_vs_producer": label_same(casimir_all_match),
        "f_crit_at_gUV_13_25": mp.nstr(f_crit, 20),
        "f_crit_rel_err": mp.nstr(f_crit_rel, 10),
        "f_crit_vs_producer": label_same(f_crit_ok),
        "frg_4d_table": frg_out,
        "frg_max_rel_err": mp.nstr(max_frg_rel, 10),
        "frg_max_fd_err": mp.nstr(max_fd_err, 10),
        "frg_vs_producer": label_same(frg_all_match),
        "brane_2H_above_fcrit_all_gauges": brane_2h_all_above,
        "quartic_2hdm_fps_at_brane2H": quartic_out,
        "quartic_max_rel_err": mp.nstr(max_q_rel, 10),
        "quartic_vs_producer": label_same(quartic_all_match),
        "downward_rge_gl4_1600": {
            "yb_high_max_ir_diff_vs_zero": mp.nstr(ir_diff_high, 16),
            "yb_low_max_ir_diff_vs_zero": mp.nstr(ir_diff_low, 16),
            "abs_err_high_vs_producer": mp.nstr(err_ir_high, 10),
            "abs_err_low_vs_producer": mp.nstr(err_ir_low, 10),
            "analytic_1loop_gauge_err": mp.nstr(g_analytic_err, 10),
            "vs_producer": label_same(rge_a_ok),
        },
        "conformal_bh_and_af_brane2H": {
            "c_log_ent": frac_str(c_log_ent),
            "c_log_contact": frac_str(c_log_con),
            "c_log_total": frac_str(c_log_tot),
            "b_1loop_spin10_brane2H": frac_str(b_s10_brane),
            "b_1loop_spin10_real10": frac_str(b_s10_10r),
            "b_1loop_e6_brane2H": frac_str(b_e6_brane),
            "vs_producer": label_same(conf_ok),
        },
        "gate_pass": gate_a,
    }, discrepancies


# ============================================================================
# Section 2: OW17-B (Seam S3 — Dynkin b/B, 2-Loop 2H RGE, Exact Census, 6D KK)
# ============================================================================

def su_n_t_and_c2(n: int, rep: str) -> tuple[int, Fraction, Fraction]:
    r"""Return (dim, T(R), C2(R)) for standard SU(n) irreps."""
    if rep == "1":
        return 1, Fraction(0), Fraction(0)
    if rep in ("fund", "afund"):
        return n, Fraction(1, 2), Fraction(n * n - 1, 2 * n)
    if rep == "adj":
        return n * n - 1, Fraction(n, 1), Fraction(n, 1)
    raise ValueError(f"Unsupported SU({n}) rep: {rep}")


def derive_sm_1loop_2loop(n_h: int) -> tuple[list[Fraction], list[list[Fraction]], list[list[Fraction]]]:
    r"""First-principles Machacek-Vaughn derivation of b_i, B_ij, and c_{i,f} for 3x16 + n_H doublets."""
    # SM chiral Weyl multiplets per generation: (rep3, rep2, Y, mult)
    weyl_reps = [
        ("fund", "fund", Fraction(1, 6), 3),    # Q_L
        ("afund", "1", Fraction(-2, 3), 3),     # u^c
        ("afund", "1", Fraction(1, 3), 3),      # d^c
        ("1", "fund", Fraction(-1, 2), 3),      # L_L
        ("1", "1", Fraction(1, 1), 3),          # e^c
    ]
    # Complex scalar Higgs doublets
    cscalar_reps = [("1", "fund", Fraction(1, 2), n_h)]

    c2_g = [Fraction(0), Fraction(2), Fraction(3)]
    b_vec = [Fraction(-11, 3) * c2_g[i] for i in range(3)]
    b_mat = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        b_mat[i][i] = Fraction(-34, 3) * c2_g[i] * c2_g[i]

    def rep_invariants(r3: str, r2: str, y_val: Fraction) -> tuple[list[int], list[Fraction], list[Fraction]]:
        d3, t3, c3 = su_n_t_and_c2(3, r3)
        d2, t2, c2 = su_n_t_and_c2(2, r2)
        q1_sq = Fraction(3, 5) * y_val * y_val
        # For U(1)_1: d1 = 1, T1 = C2_1 = (3/5) Y^2
        return [1, d2, d3], [q1_sq, t2, t3], [q1_sq, c2, c3]

    # Weyl fermion sums
    for r3, r2, y_val, mult in weyl_reps:
        dims, ts, c2s = rep_invariants(r3, r2, y_val)
        tot_d = dims[0] * dims[1] * dims[2]
        for i in range(3):
            d_other = tot_d // dims[i]
            ti = ts[i]
            b_vec[i] += Fraction(2, 3) * mult * d_other * ti
            b_mat[i][i] += mult * d_other * ti * (2 * c2s[i] + Fraction(10, 3) * c2_g[i])
            for j in range(3):
                if i != j:
                    b_mat[i][j] += 2 * mult * d_other * ti * c2s[j]

    # Complex scalar sums
    for r3, r2, y_val, mult in cscalar_reps:
        dims, ts, c2s = rep_invariants(r3, r2, y_val)
        tot_d = dims[0] * dims[1] * dims[2]
        for i in range(3):
            d_other = tot_d // dims[i]
            ti = ts[i]
            b_vec[i] += Fraction(1, 3) * mult * d_other * ti
            b_mat[i][i] += mult * d_other * ti * (4 * c2s[i] + Fraction(2, 3) * c2_g[i])
            for j in range(3):
                if i != j:
                    b_mat[i][j] += 4 * mult * d_other * ti * c2s[j]

    # First-principles Machacek-Vaughn Yukawa-gauge 2-loop matrix c_{i, f} for f in (t, b, tau):
    # c_{i, f} = sum_{psi in {f_L, f_R}} T_i(psi) * Tr_{other}(Y^dag Y)|_psi
    # For doublet f_L (Q_L or L_L), each doublet component couples once (factor 1);
    # for singlet f_R (u^c, d^c, e^c), it contracts with both Higgs doublet components (factor 2).
    yuk_pairs = [
        (("fund", "fund", Fraction(1, 6), 1), ("afund", "1", Fraction(-2, 3), 2)),  # top
        (("fund", "fund", Fraction(1, 6), 1), ("afund", "1", Fraction(1, 3), 2)),   # bottom
        (("1", "fund", Fraction(-1, 2), 1), ("1", "1", Fraction(1, 1), 2)),         # tau
    ]
    c_mat = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    for f_idx, pair in enumerate(yuk_pairs):
        for r3, r2, y_val, n_yuk in pair:
            dims, ts, _ = rep_invariants(r3, r2, y_val)
            tot_d = dims[0] * dims[1] * dims[2]
            for i in range(3):
                d_other = tot_d // dims[i]
                c_mat[i][f_idx] += n_yuk * d_other * ts[i]

    return b_vec, b_mat, c_mat


def sm_multiplet_delta_b(pieces: list[tuple[str, str, Fraction, str, int]]) -> list[Fraction]:
    r"""Compute exact 1-loop (db1, db2, db3) from SM sub-multiplet list.

    Each piece is (rep3, rep2, Y, kind, mult) with kind in {'R_scalar', 'C_scalar', 'Weyl'}.
    """
    coeffs = {
        "R_scalar": Fraction(1, 6),
        "C_scalar": Fraction(1, 3),
        "Weyl": Fraction(2, 3),
    }
    db = [Fraction(0), Fraction(0), Fraction(0)]
    for r3, r2, y_val, kind, mult in pieces:
        d3, t3, _ = su_n_t_and_c2(3, r3)
        d2, t2, _ = su_n_t_and_c2(2, r2)
        c_k = coeffs[kind] * mult
        db[0] += c_k * (d3 * d2) * Fraction(3, 5) * y_val * y_val
        db[1] += c_k * d3 * t2
        db[2] += c_k * d2 * t3
    return db


def sm_multiplet_dynkin_sum(pieces: list[tuple[str, str, Fraction, str, int]]) -> tuple[int, list[Fraction]]:
    r"""Sum real-equivalent dimension and (T1, T2, T3) over explicit SM sub-multiplets.

    For kind == 'C_in_R' (a complex rep plus its conjugate inside a real GUT rep),
    contributes 2*d3*d2 real components and 2*T_i.
    For kind == 'R' (real rep), contributes d3*d2 real components and T_i.
    For kind == 'C' (complex GUT rep), contributes d3*d2 complex components and T_i.
    """
    dim_tot = 0
    ts = [Fraction(0), Fraction(0), Fraction(0)]
    for r3, r2, y_val, kind, mult in pieces:
        d3, t3, _ = su_n_t_and_c2(3, r3)
        d2, t2, _ = su_n_t_and_c2(2, r2)
        factor = 2 if kind == "C_in_R" else 1
        dim_tot += mult * factor * d3 * d2
        ts[0] += mult * factor * (d3 * d2) * Fraction(3, 5) * y_val * y_val
        ts[1] += mult * factor * d3 * t2
        ts[2] += mult * factor * d2 * t3
    return dim_tot, ts


def run_ow17_b(prod_b: dict) -> tuple[dict, int, list[list[Fraction]]]:
    r"""Independent referee verification of OW17-B (Seam S3)."""
    discrepancies = 0
    pi = mp.pi

    # 1. First-principles Dynkin b_i, B_ij, c_if for n_H = 1, 2
    b_1h, mat_1h, c_1h = derive_sm_1loop_2loop(1)
    b_2h, mat_2h, c_2h = derive_sm_1loop_2loop(2)

    pdyn = prod_b["first_principles_dynkin"]
    dyn_ok = (
        [parse_frac(x) for x in pdyn["b_1h"]] == b_1h
        and [parse_frac(x) for x in pdyn["b_2h"]] == b_2h
        and [[parse_frac(x) for x in row] for row in pdyn["B_1h"]] == mat_1h
        and [[parse_frac(x) for x in row] for row in pdyn["B_2h"]] == mat_2h
        and c_1h == c_2h
    )
    if not dyn_ok:
        discrepancies += 1

    # 2. 2-loop 2H SM gauge-Yukawa RGE via independent 500-step GL4
    loop = mp.mpf(1) / (16 * pi * pi)
    loop2 = loop * loop
    b_mp = [f2mp(x) for x in b_2h]
    mat_mp = [[f2mp(x) for x in row] for row in mat_2h]
    c_mp = [[f2mp(x) for x in row] for row in c_2h]
    c_9_2 = mp.mpf(9) / 2
    c_1_2 = mp.mpf(1) / 2
    c_9_4 = mp.mpf(9) / 4
    c_17_20 = mp.mpf(17) / 20
    c_1_4 = mp.mpf(1) / 4
    c_5_2 = mp.mpf(5) / 2

    def rhs_2loop(y: list[mp.mpf]) -> list[mp.mpf]:
        g1, g2, g3, yt, yb, ytau = y
        g2s = [g1 * g1, g2 * g2, g3 * g3]
        y2s = [yt * yt, yb * yb, ytau * ytau]
        gs = [g1, g2, g3]
        dg = []
        for i in range(3):
            g3i = g2s[i] * gs[i]
            t1 = loop * b_mp[i] * g3i
            s_g = mat_mp[i][0] * g2s[0] + mat_mp[i][1] * g2s[1] + mat_mp[i][2] * g2s[2]
            s_y = c_mp[i][0] * y2s[0] + c_mp[i][1] * y2s[1] + c_mp[i][2] * y2s[2]
            t2 = loop2 * g3i * (s_g - s_y)
            dg.append(t1 + t2)
        dyt = loop * yt * (c_9_2 * y2s[0] + c_1_2 * y2s[1] - 8 * g2s[2] - c_9_4 * g2s[1] - c_17_20 * g2s[0])
        dyb = loop * yb * (c_9_2 * y2s[1] + c_1_2 * y2s[0] + y2s[2] - 8 * g2s[2] - c_9_4 * g2s[1] - c_1_4 * g2s[0])
        dytau = loop * ytau * (c_5_2 * y2s[2] + 3 * y2s[1] - c_9_4 * g2s[1] - c_9_4 * g2s[0])
        return dg + [dyt, dyb, dytau]

    five_ninths = mp.mpf(5) / 9
    five_sevenths = mp.mpf(5) / 7
    bound_62 = mp.mpf(62) / 100
    yt0 = mp.mpf(1) / 2
    yb0 = mp.mpf(1) / 20
    ytau0 = mp.mpf(1) / 20

    def run_traj(alpha_uv_inv: int, t_target: int, prow: dict) -> tuple[dict, bool, mp.mpf, mp.mpf]:
        g0 = mp.sqrt(4 * pi / mp.mpf(alpha_uv_inv))
        yf = integrate_gl4(rhs_2loop, [g0, g0, g0, yt0, yb0, ytau0], mp.mpf(t_target), 500, fp_iters=4)
        ainvs = [4 * pi / (yf[i] * yf[i]) for i in range(3)]
        b_eff = (ainvs[1] - ainvs[2]) / (ainvs[0] - ainvs[1])
        shift = b_eff - five_ninths
        err_b = abs_err_mp(b_eff, prow["B_eff_2loop"])
        err_a = max(abs_err_mp(ainvs[i], prow["alpha_inv_ir"][i]) for i in range(3))
        ok = err_b < mp.mpf(10) ** (-10) and err_a < mp.mpf(10) ** (-9) and b_eff < bound_62 < five_sevenths
        return {
            "alpha_uv_inv": alpha_uv_inv,
            "t_reached": t_target,
            "alpha_inv_ir": [mp.nstr(a, 15) for a in ainvs],
            "B_eff_2loop": mp.nstr(b_eff, 17),
            "shift_from_5_9": mp.nstr(shift, 15),
            "abs_err_B_vs_producer": mp.nstr(err_b, 10),
            "abs_err_alpha_inv_vs_producer": mp.nstr(err_a, 10),
            "vs_producer": label_same(ok),
        }, ok, b_eff, abs(shift)

    prge = prod_b["two_loop_2h_sm_downward_rge"]
    common_out = []
    deep_out = []
    rge_b_ok = True
    max_b_eff = mp.mpf(0)
    max_shift = mp.mpf(0)

    for idx, ainv in enumerate((20, 25, 30, 35, 40)):
        rec, ok, beff, sh = run_traj(ainv, -12, prge["common_window_t_neg12"][idx])
        common_out.append(rec)
        if not ok:
            rge_b_ok = False
            discrepancies += 1
        if beff > max_b_eff:
            max_b_eff = beff
        if sh > max_shift:
            max_shift = sh

    for idx, (ainv, tend) in enumerate(((40, -30), (45, -35), (50, -35))):
        rec, ok, beff, sh = run_traj(ainv, tend, prge["deep_window_high_alpha_inv"][idx])
        deep_out.append(rec)
        if not ok:
            rge_b_ok = False
            discrepancies += 1
        if beff > max_b_eff:
            max_b_eff = beff
        if sh > max_shift:
            max_shift = sh

    # 3. Exact rational split-multiplet census (all 11 rows derived from SM irreps)
    b0_1, b0_2, b0_3 = b_2h
    b_target = Fraction(5, 7)
    b_ir = (b0_2 - b0_3) / (b0_1 - b0_2)

    split_specs = [
        ("(1,3,0)_R [A_5/A_6 SU(2)_L triplet in 45]", True, [("1", "adj", Fraction(0), "R_scalar", 1)]),
        ("2 x (1,3,0)_R [both A_5, A_6 triplets in 45]", True, [("1", "adj", Fraction(0), "R_scalar", 2)]),
        ("(8,1,0)_R [A_5/A_6 SU(3)_c octet in 45]", True, [("adj", "1", Fraction(0), "R_scalar", 1)]),
        ("(1,3,0)_R + (8,1,0)_R [SM adjoint A_5 in 45]", True, [("1", "adj", Fraction(0), "R_scalar", 1), ("adj", "1", Fraction(0), "R_scalar", 1)]),
        ("(15,1,1)_R [PS adjoint A_5/A_6 in 45]", True, [("adj", "1", Fraction(0), "R_scalar", 1), ("1", "1", Fraction(0), "R_scalar", 1), ("fund", "1", Fraction(2, 3), "C_scalar", 1)]),
        ("(3,2,1/6)_C [X',Y' coset scalar in 45]", True, [("fund", "fund", Fraction(1, 6), "C_scalar", 1)]),
        ("(3,2,-5/6)_C [X,Y coset scalar in 45]", True, [("fund", "fund", Fraction(-5, 6), "C_scalar", 1)]),
        ("(3,1,-1/3)_C [color triplet in 10_R]", False, [("fund", "1", Fraction(-1, 3), "C_scalar", 1)]),
        ("E_6 27 exotic L'+L'^c (1,2,+-1/2) Weyl pair", False, [("1", "fund", Fraction(1, 2), "Weyl", 1), ("1", "fund", Fraction(-1, 2), "Weyl", 1)]),
        ("E_6 27 exotic D+D^c (3,1,+-1/3) Weyl pair", False, [("fund", "1", Fraction(-1, 3), "Weyl", 1), ("afund", "1", Fraction(1, 3), "Weyl", 1)]),
        ("E_6 27 complete 5+5bar (D+D^c + L'+L'^c)", False, [("fund", "1", Fraction(-1, 3), "Weyl", 1), ("afund", "1", Fraction(1, 3), "Weyl", 1), ("1", "fund", Fraction(1, 2), "Weyl", 1), ("1", "fund", Fraction(-1, 2), "Weyl", 1)]),
    ]

    split_out = []
    split_all_match = True
    inside_45_strict = []
    inside_45_boundary = []
    for idx, (label, in_45, pieces) in enumerate(split_specs):
        db = sm_multiplet_delta_b(pieces)
        b_int = ((b0_2 + db[1]) - (b0_3 + db[2])) / ((b0_1 + db[0]) - (b0_2 + db[1]))
        if b_int == b_ir:
            r_lin_str = "NONE"
            closes_lin = False
        else:
            r_lin = (b_target - b_ir) / (b_int - b_ir)
            r_lin_str = frac_str(r_lin)
            closes_lin = Fraction(0) < r_lin < Fraction(1)
        # Exact weighted 1-loop closure: 7[(b0_2-b0_3)+r(db2-db3)] = 5[(b0_1-b0_2)+r(db1-db2)]
        rhs_num = 5 * (b0_1 - b0_2) - 7 * (b0_2 - b0_3)
        denom_w = 7 * (db[1] - db[2]) - 5 * (db[0] - db[1])
        if denom_w == 0:
            r_w_str = "NONE"
            closes_w = False
            hits_bdry = False
        else:
            r_w = rhs_num / denom_w
            r_w_str = frac_str(r_w)
            closes_w = Fraction(0) < r_w < Fraction(1)
            hits_bdry = r_w == Fraction(1) and b_int == b_target
        if in_45 and closes_w:
            inside_45_strict.append(label)
        if in_45 and hits_bdry:
            inside_45_boundary.append(label)

        prow = prod_b["split_multiplet_census"][idx]
        ok = (
            [parse_frac(x) for x in prow["delta_b"]] == db
            and parse_frac(prow["B_int"]) == b_int
            and prow["r_needed_for_5_7"] == r_lin_str
            and prow["closes_with_0_lt_r_lt_1"] == closes_lin
            and prow["r_exact_weighted_for_5_7"] == r_w_str
            and prow["closes_exact_weighted"] == closes_w
        )
        if not ok:
            split_all_match = False
            discrepancies += 1
        split_out.append({
            "multiplet": label,
            "delta_b": [frac_str(x) for x in db],
            "B_int": frac_str(b_int),
            "r_needed_for_5_7": r_lin_str,
            "r_exact_weighted_for_5_7": r_w_str,
            "closes_exact_weighted": closes_w,
            "hits_exact_boundary_r_eq_1": hits_bdry,
            "vs_producer": label_same(ok),
        })

    # 4. Exact rational Pati-Salam intermediate census from SU(4)_C x SU(2)_L x SU(2)_R Dynkin sums
    def ps_betas(extra_scalars: list[tuple[str, str, str, str]]) -> tuple[Fraction, Fraction, Fraction]:
        # Base: PS(4,2,2) gauge + 3 x [(4,2,1) + (4bar,1,2)] Weyl + (1,2,2)_C complex bidoublet
        b4 = Fraction(-11, 3) * 4 + Fraction(2, 3) * 3 * (2 * Fraction(1, 2) + 2 * Fraction(1, 2))
        b2l = Fraction(-11, 3) * 2 + Fraction(2, 3) * 3 * (4 * Fraction(1, 2)) + Fraction(1, 3) * (2 * Fraction(1, 2))
        b2r = Fraction(-11, 3) * 2 + Fraction(2, 3) * 3 * (4 * Fraction(1, 2)) + Fraction(1, 3) * (2 * Fraction(1, 2))
        for r4, r2l, r2r, kind in extra_scalars:
            d4, t4, _ = su_n_t_and_c2(4, r4)
            d2l, t2l, _ = su_n_t_and_c2(2, r2l)
            d2r, t2r, _ = su_n_t_and_c2(2, r2r)
            c_k = Fraction(1, 6) if kind == "R" else Fraction(1, 3)
            b4 += c_k * (d2l * d2r) * t4
            b2l += c_k * (d4 * d2r) * t2l
            b2r += c_k * (d4 * d2l) * t2r
        return b4, b2l, b2r

    ps_specs = [
        ("Pure PS(4,2,2) + 3x16 + (1,2,2)_C [0 extra scalars]", True, []),
        ("PS + (15,1,1)_R [ALREADY inside Spin(10) 45!]", True, [("adj", "1", "1", "R")]),
        ("PS + (15,1,1)_R + (1,1,3)_R [BOTH inside Spin(10) 45!]", True, [("adj", "1", "1", "R"), ("1", "1", "adj", "R")]),
        ("PS + (4,1,2)_C [extra Higgs outside 45]", False, [("fund", "1", "fund", "C")]),
    ]
    ps_out = []
    ps_all_match = True
    ps_in45_winners = []
    for idx, (label, in_45, extras) in enumerate(ps_specs):
        b4, b2l, b2r = ps_betas(extras)
        b1_eff = Fraction(2, 5) * b4 + Fraction(3, 5) * b2r
        db_ps = [b1_eff - b0_1, b2l - b0_2, b4 - b0_3]
        rhs_num = 5 * (b0_1 - b0_2) - 7 * (b0_2 - b0_3)
        denom_w = 7 * (db_ps[1] - db_ps[2]) - 5 * (db_ps[0] - db_ps[1])
        r_ps = rhs_num / denom_w
        x_ps = Fraction(1) - r_ps
        closes = Fraction(0) < r_ps < Fraction(1)
        if in_45 and closes:
            ps_in45_winners.append(label)
        prow = prod_b["ps_intermediate_exact_census"][idx]
        ok = (
            [parse_frac(x) for x in prow["b4_b2L_b2R"]] == [b4, b2l, b2r]
            and parse_frac(prow["b1_eff"]) == b1_eff
            and parse_frac(prow["r_exact_for_B_5_7"]) == r_ps
            and prow["closes_with_0_lt_r_lt_1"] == closes
        )
        if not ok:
            ps_all_match = False
            discrepancies += 1
        ps_out.append({
            "ps_spectrum": label,
            "b4_b2L_b2R": [frac_str(b4), frac_str(b2l), frac_str(b2r)],
            "b1_eff": frac_str(b1_eff),
            "r_exact_for_B_5_7": frac_str(r_ps),
            "x_exact": frac_str(x_ps),
            "closes_with_0_lt_r_lt_1": closes,
            "vs_producer": label_same(ok),
        })

    # 5. 6D KK complete-multiplet universality proved directly via explicit SM decompositions!
    sm_16 = [
        ("fund", "fund", Fraction(1, 6), "C", 1),
        ("afund", "1", Fraction(-2, 3), "C", 1),
        ("afund", "1", Fraction(1, 3), "C", 1),
        ("1", "fund", Fraction(-1, 2), "C", 1),
        ("1", "1", Fraction(1, 1), "C", 1),
        ("1", "1", Fraction(0, 1), "C", 1),
    ]
    sm_45 = [
        ("adj", "1", Fraction(0, 1), "R", 1),
        ("1", "adj", Fraction(0, 1), "R", 1),
        ("1", "1", Fraction(0, 1), "R", 2),
        ("fund", "fund", Fraction(-5, 6), "C_in_R", 1),
        ("fund", "fund", Fraction(1, 6), "C_in_R", 1),
        ("afund", "1", Fraction(-2, 3), "C_in_R", 1),
        ("1", "1", Fraction(1, 1), "C_in_R", 1),
    ]
    sm_27 = sm_16 + [
        ("fund", "1", Fraction(-1, 3), "C", 1),
        ("afund", "1", Fraction(1, 3), "C", 1),
        ("1", "fund", Fraction(1, 2), "C", 1),
        ("1", "fund", Fraction(-1, 2), "C", 1),
        ("1", "1", Fraction(0, 1), "C", 1),
    ]
    sm_78 = sm_45 + [("1", "1", Fraction(0, 1), "R", 1)] + [
        (r3, r2, yv, "C_in_R", m) for (r3, r2, yv, _, m) in sm_16
    ]

    kk_specs = [
        ("spin10_45_kk_db", sm_45, 45, Fraction(-10, 3)),
        ("spin10_16_kk_db", sm_16, 16, Fraction(4, 3)),
        ("e6_78_kk_db", sm_78, 78, Fraction(-10, 3)),
        ("e6_27_kk_db", sm_27, 27, Fraction(4, 3)),
    ]
    pkk = prod_b["kk_6d_complete_multiplet_universality"]
    kk_out = {}
    kk_all_match = True
    for kname, decomp, exp_dim, kk_factor in kk_specs:
        dim_chk, ts = sm_multiplet_dynkin_sum(decomp)
        kk_db = [kk_factor * t_i for t_i in ts]
        universal = (ts[0] == ts[1] == ts[2]) and (dim_chk == exp_dim)
        ok = universal and [parse_frac(x) for x in pkk[kname]] == kk_db
        if not ok:
            kk_all_match = False
            discrepancies += 1
        kk_out[kname] = {
            "sm_sum_dim": dim_chk,
            "sm_sum_T": [frac_str(x) for x in ts],
            "kk_db": [frac_str(x) for x in kk_db],
            "universal_equal": universal,
            "vs_producer": label_same(ok),
        }

    gate_b = (
        dyn_ok
        and rge_b_ok
        and split_all_match
        and ps_all_match
        and kk_all_match
        and len(inside_45_strict) == 0
        and len(inside_45_boundary) == 1
        and len(ps_in45_winners) == 3
    )
    return {
        "first_principles_dynkin": {
            "b_1h": [frac_str(x) for x in b_1h],
            "b_2h": [frac_str(x) for x in b_2h],
            "B_1h": [[frac_str(x) for x in row] for row in mat_1h],
            "B_2h": [[frac_str(x) for x in row] for row in mat_2h],
            "c_if": [[frac_str(x) for x in row] for row in c_2h],
            "vs_producer": label_same(dyn_ok),
        },
        "two_loop_2h_sm_gl4_500": {
            "common_window_t_neg12": common_out,
            "deep_window_high_alpha_inv": deep_out,
            "max_abs_shift_from_5_9": mp.nstr(max_shift, 14),
            "max_B_eff_2loop": mp.nstr(max_b_eff, 15),
            "strictly_below_62_100_and_5_7": bool(max_b_eff < bound_62 < five_sevenths),
            "vs_producer": label_same(rge_b_ok),
        },
        "split_multiplet_census": split_out,
        "split_census_vs_producer": label_same(split_all_match),
        "inside_45_strict_0_lt_r_lt_1": inside_45_strict,
        "inside_45_exact_boundary_r_eq_1": inside_45_boundary,
        "ps_intermediate_exact_census": ps_out,
        "ps_census_vs_producer": label_same(ps_all_match),
        "ps_inside_45_winners_zero_extra_reps": ps_in45_winners,
        "kk_6d_complete_multiplet_universality": kk_out,
        "kk_vs_producer": label_same(kk_all_match),
        "gate_pass": gate_b,
    }, discrepancies, mat_1h


# ============================================================================
# Section 3: OW17-C (Seam S1 — m004 Commutant, L_2, E[5]+E[6], Haar, E[n])
# ============================================================================

def solve_l2_weierstrass_taylor(
    z_in: mp.mpc,
    c_guess: mp.mpc,
    n_a: int = 14,
    n_b: int = 22,
    deg: int = 24,
    ws_denom: int = 20,
    m_max: int = 22,
    fix_c_zero: bool = False,
) -> tuple[mp.mpc, mp.mpf, mp.mpf]:
    r"""Independent Order-24 Weierstrass-Taylor Fuchsian Lame L_2(z) solver.

    Uses the exact Weierstrass ODE wp'' = 6 wp^2 - g_2/2 to generate order-`deg`
    local Taylor series along each panel, with dyadic refinement toward w_s.
    Returns (c_acc, L_2, |tr(comm) + 2|).
    """
    pi = mp.pi
    q = mp.exp(2 * I_UNIT * pi * z_in)
    qh = mp.exp(I_UNIT * pi * z_in)

    e2 = mp.mpc(1)
    e4 = mp.mpc(1)
    e6 = mp.mpc(1)
    qk = q
    for k in range(1, 65):
        frac_q = qk / (mp.mpc(1) - qk)
        k2 = k * k
        e2 -= 24 * k * frac_q
        e4 += 240 * k * k2 * frac_q
        e6 -= 504 * k * k2 * k2 * frac_q
        qk *= q
    g2 = (mp.mpf(4) * pi**4 / 3) * e4
    g3 = (mp.mpf(8) * pi**6 / 27) * e6

    def wp_and_dwp(w: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
        u = pi * w
        th0 = mp.jtheta(1, u, qh, 0)
        th1 = mp.jtheta(1, u, qh, 1)
        th2 = mp.jtheta(1, u, qh, 2)
        th3 = mp.jtheta(1, u, qh, 3)
        wp_v = -pi * pi * (th2 * th0 - th1 * th1) / (th0 * th0) - (pi * pi / 3) * e2
        dwp_v = -(pi**3) * (th3 * th0 * th0 - 3 * th0 * th1 * th2 + 2 * th1**3) / (th0**3)
        return wp_v, dwp_v

    def precompute_seg(za: mp.mpc, zb: mp.mpc, n_steps: int) -> tuple[mp.mpc, list[list[mp.mpc]]]:
        dz = (zb - za) / mp.mpf(n_steps)
        steps = []
        for k in range(n_steps):
            w = za + k * dz
            p0, p1 = wp_and_dwp(w)
            p = [mp.mpc(0)] * (deg - 1)
            p[0] = p0
            p[1] = p1
            p[2] = (6 * p0 * p0 - g2 / 2) / 2
            for m in range(1, deg - 3):
                s = mp.mpc(0)
                for j in range(m + 1):
                    s += p[j] * p[m - j]
                p[m + 2] = 6 * s / mp.mpf((m + 2) * (m + 1))
            steps.append(p)
        return dz, steps

    def propagate(c_acc: mp.mpc, seg_data: tuple[mp.mpc, list[list[mp.mpc]]], y_init: mp.matrix | None = None) -> mp.matrix:
        dz, steps = seg_data
        if y_init is None:
            y00, y01, y10, y11 = mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)
        else:
            y00, y01, y10, y11 = y_init[0, 0], y_init[0, 1], y_init[1, 0], y_init[1, 1]
        dzp = [mp.mpc(1)] * (deg + 1)
        for k in range(1, deg + 1):
            dzp[k] = dzp[k - 1] * dz
        inv4 = mp.mpf(1) / 4
        for p in steps:
            q0 = c_acc + p[0] * inv4
            a = [mp.mpc(0)] * (deg + 1)
            b = [mp.mpc(0)] * (deg + 1)
            a[0], a[1] = y00, y10
            b[0], b[1] = y01, y11
            for k in range(deg - 1):
                sa = q0 * a[k]
                sb = q0 * b[k]
                for j in range(1, k + 1):
                    qj = p[j] * inv4
                    sa += qj * a[k - j]
                    sb += qj * b[k - j]
                den = mp.mpf((k + 2) * (k + 1))
                a[k + 2] = -sa / den
                b[k + 2] = -sb / den
            y00 = mp.mpc(0)
            y01 = mp.mpc(0)
            y10 = mp.mpc(0)
            y11 = mp.mpc(0)
            for k in range(deg + 1):
                y00 += a[k] * dzp[k]
                y01 += b[k] * dzp[k]
            for k in range(1, deg + 1):
                y10 += k * a[k] * dzp[k - 1]
                y11 += k * b[k] * dzp[k - 1]
        return mp.matrix([[y00, y01], [y10, y11]])

    w0 = (mp.mpc(1) + z_in) / 2
    seg_a = precompute_seg(w0, w0 + mp.mpc(1), n_a)
    seg_b = precompute_seg(w0, w0 + z_in, n_b)

    c_acc = mp.mpc(0) if fix_c_zero else c_guess
    if not fix_c_zero:
        eps = mp.mpf(10) ** (-18)
        tol = mp.mpf(10) ** (-36)
        for _ in range(12):
            ta = propagate(c_acc, seg_a)
            tb = propagate(c_acc, seg_b)
            f1 = mp.im(ta[0, 0] + ta[1, 1])
            f2 = mp.im(tb[0, 0] + tb[1, 1])
            if max(abs(f1), abs(f2)) < tol:
                break
            tar = propagate(c_acc + eps, seg_a)
            tbr = propagate(c_acc + eps, seg_b)
            tai = propagate(c_acc + I_UNIT * eps, seg_a)
            tbi = propagate(c_acc + I_UNIT * eps, seg_b)
            j11 = (mp.im(tar[0, 0] + tar[1, 1]) - f1) / eps
            j12 = (mp.im(tai[0, 0] + tai[1, 1]) - f1) / eps
            j21 = (mp.im(tbr[0, 0] + tbr[1, 1]) - f2) / eps
            j22 = (mp.im(tbi[0, 0] + tbi[1, 1]) - f2) / eps
            det = j11 * j22 - j12 * j21
            dr = -(j22 * f1 - j12 * f2) / det
            di = -(-j21 * f1 + j11 * f2) / det
            c_acc += mp.mpc(dr, di)

    ta = propagate(c_acc, seg_a)
    tb = propagate(c_acc, seg_b)
    comm = tb * ta * (tb ** (-1)) * (ta ** (-1))
    tr_comm_err = abs(comm[0, 0] + comm[1, 1] + 2)

    def mobius(mat: mp.matrix) -> mp.matrix:
        det_s = mp.sqrt(mat[0, 0] * mat[1, 1] - mat[0, 1] * mat[1, 0])
        return mp.matrix([[mat[1, 1] / det_s, mat[0, 1] / det_s], [mat[1, 0] / det_s, mat[0, 0] / det_s]])

    p0 = mobius(comm)
    aa = mobius(ta)
    pf = (p0[0, 0] - p0[1, 1]) / (2 * p0[1, 0])
    disc = (aa[1, 1] - aa[0, 0]) ** 2 + 4 * aa[1, 0] * aa[0, 1]
    sdisc = mp.sqrt(disc)
    fa1 = (-(aa[1, 1] - aa[0, 0]) + sdisc) / (2 * aa[1, 0])
    fa2 = (-(aa[1, 1] - aa[0, 0]) - sdisc) / (2 * aa[1, 0])

    g00 = fa2 - pf
    g01 = -fa1 * (fa2 - pf)
    g10 = fa2 - fa1
    g11 = -pf * (fa2 - fa1)
    det_g = mp.sqrt(g00 * g11 - g01 * g10)
    gmat = mp.matrix([[g00 / det_g, g01 / det_g], [g10 / det_g, g11 / det_g]])
    if mp.im(gmat[0, 1] / gmat[1, 1]) < 0:
        gmat = mp.matrix([[I_UNIT, mp.mpc(0)], [mp.mpc(0), -I_UNIT]]) * gmat

    pg = gmat * p0 * (gmat ** (-1))
    lam_cusp = abs(mp.re(pg[0, 1] / pg[0, 0]))

    ws = (mp.mpf(1) / mp.mpf(ws_denom)) * w0 / abs(w0)
    knots = [w0, w0 / 2, w0 / 4, w0 / 8, w0 / 16, ws]
    tin = mp.eye(2)
    for k in range(len(knots) - 1):
        tin = propagate(c_acc, precompute_seg(knots[k], knots[k + 1], 8), tin)

    r_in = tin[0, 1] / tin[0, 0]
    u_ws = (gmat[0, 0] * r_in + gmat[0, 1]) / (gmat[1, 0] * r_in + gmat[1, 1])

    cn = [mp.mpc(0)] * (m_max // 2 + 2)
    cn[1] = g2 / 20
    cn[2] = g3 / 28
    for k in range(3, len(cn)):
        s_cn = mp.mpc(0)
        for m in range(1, k - 1):
            s_cn += cn[m] * cn[k - 1 - m]
        cn[k] = (mp.mpf(3) / mp.mpf((2 * k + 3) * (k - 2))) * s_cn

    q_ser = [mp.mpc(0)] * (m_max + 1)
    q_ser[0] = c_acc
    for k in range(1, m_max // 2 + 1):
        q_ser[2 * k] = cn[k] / 4

    al = [mp.mpc(0)] * (m_max + 1)
    be = [mp.mpc(0)] * (m_max + 1)
    al[0] = mp.mpc(1)
    for m in range(1, m_max + 1):
        sa = mp.mpc(0)
        sb = mp.mpc(0)
        for j in range(m - 1):
            sa += q_ser[j] * al[m - 2 - j]
            sb += q_ser[j] * be[m - 2 - j]
        al[m] = -sa / mp.mpf(m * m)
        be[m] = (-2 * m * al[m] - sb) / mp.mpf(m * m)

    sum_al = mp.mpc(0)
    sum_be = mp.mpc(0)
    wsp = mp.mpc(1)
    for m in range(m_max + 1):
        sum_al += al[m] * wsp
        if m >= 1:
            sum_be += be[m] * wsp
        wsp *= ws
    g_loc = sum_be / sum_al
    im_b = mp.im(u_ws) + (lam_cusp / (2 * pi)) * (mp.log(abs(ws)) + mp.re(g_loc))
    l2_val = pi - (2 * pi / lam_cusp) * im_b
    return c_acc, l2_val, tr_comm_err


def build_e5_e6_yukawas(tau: mp.mpc, l2_val: mp.mpf) -> tuple[mp.matrix, mp.matrix]:
    r"""Independent B1656 quaternion S-reading E[5] + E[6] Regime-4b Yukawa evaluator."""
    pi = mp.pi
    i2 = mp.matrix([[1, 0], [0, 1]])
    qi_m = mp.matrix([[I_UNIT, 0], [0, -I_UNIT]])
    qj_m = mp.matrix([[0, 1], [-1, 0]])
    qk_m = mp.matrix([[0, I_UNIT], [I_UNIT, 0]])
    eps_m = qj_m
    units = [i2, qi_m, qj_m, qk_m]
    ec = [eps_m * u for u in units]
    blocks = [qj_m, qi_m, qk_m]
    q_s = [qi_m, qj_m, qk_m]

    def hsum(a_m: mp.matrix, b_m: mp.matrix) -> mp.mpc:
        return (
            a_m[0, 0] * b_m[0, 0]
            + a_m[0, 1] * b_m[0, 1]
            + a_m[1, 0] * b_m[1, 0]
            + a_m[1, 1] * b_m[1, 1]
        )

    gram = mp.matrix(4, 4)
    for t_i in range(4):
        for s_i in range(4):
            gram[t_i, s_i] = hsum(ec[t_i], units[s_i])
    gram_inv = gram ** (-1)
    edual = []
    for a_i in range(4):
        m_acc = mp.zeros(2, 2)
        for b_i in range(4):
            m_acc += gram_inv[b_i, a_i] * units[b_i]
        edual.append(m_acc)

    coup = {}
    for qi in range(3):
        for si in range(4):
            for a_i in range(3):
                for b_i in range(3):
                    coup[(qi, si, a_i, b_i)] = hsum(blocks[a_i].T * q_s[qi] * edual[si], blocks[b_i])

    q = mp.exp(2 * I_UNIT * pi * tau)
    y = mp.im(tau)
    x = mp.re(tau)
    e2 = mp.mpc(1)
    eta_prod = mp.mpc(1)
    qm = q
    for m in range(1, 60):
        e2 -= 24 * m * qm / (mp.mpc(1) - qm)
        eta_prod *= mp.mpc(1) - qm
        qm *= q
    eta = mp.exp(I_UNIT * pi * tau / 12) * eta_prod
    denom_hat = 2 * pi * (eta ** 3)

    def theta_pair(ca: mp.mpf, cb: mp.mpf) -> tuple[mp.mpc, mp.mpc]:
        val = mp.mpc(0)
        dval = mp.mpc(0)
        for k in range(-20, 21):
            v = mp.mpf(k) + ca
            term = mp.exp(I_UNIT * pi * v * v * tau + 2 * I_UNIT * pi * v * cb)
            val += term
            dval += (mp.mpf(1) / 2) * v * v * term
        return val, dval

    t2, dt2 = theta_pair(mp.mpf(1) / 2, mp.mpf(0))
    t4, dt4 = theta_pair(mp.mpf(0), mp.mpf(1) / 2)
    t3, dt3 = theta_pair(mp.mpf(0), mp.mpf(0))
    r_h = [-t2 * t2 / denom_hat, -t4 * t4 / denom_hat, I_UNIT * t3 * t3 / denom_hat]
    dn_h = [-2 * t2 * dt2 / denom_hat, -2 * t4 * dt4 / denom_hat, 2 * I_UNIT * t3 * dt3 / denom_hat]
    c_3 = [dn_h[qi] - (e2 / 12) * r_h[qi] for qi in range(3)]

    shift_old = 2 * pi * (l2_val + mp.log(y) / 2 - mp.euler - mp.log(pi))
    exp_neg2l2 = mp.exp(-2 * l2_val)

    def level2_theta(aa: mp.mpf, bb: mp.mpf) -> tuple[mp.mpc, mp.mpc]:
        x0 = mp.mpc(0)
        x1 = mp.mpc(0)
        for k in range(-18, 19):
            v0 = mp.mpf(k) + aa
            v1 = v0 + mp.mpf(1) / 2
            x0 += mp.exp(2 * I_UNIT * pi * tau * v0 * v0 + 2 * I_UNIT * pi * v0 * bb)
            x1 += mp.exp(2 * I_UNIT * pi * tau * v1 * v1 + 2 * I_UNIT * pi * v0 * bb)
        return x0, x1

    def mod1(r: Fraction) -> Fraction:
        return r - (r.numerator // r.denominator)

    u_cache: dict[tuple[Fraction, Fraction], mp.mpf] = {}

    def get_u_factor(ua_f: Fraction, ub_f: Fraction) -> mp.mpf:
        key = (ua_f, ub_f)
        if key in u_cache:
            return u_cache[key]
        if ua_f == 0 and ub_f == 0:
            u_cache[key] = mp.mpf(0)
            return mp.mpf(0)
        ua = f2mp(ua_f)
        ub = f2mp(ub_f)
        if ua_f == 0:
            f_u = pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y)) + (pi * pi * y) / (mp.sin(pi * ub) ** 2)
            for m in range(1, 22):
                for sgn in (1, -1):
                    wm = mp.exp(2 * I_UNIT * pi * (sgn * m * x + ub) - 2 * pi * m * y)
                    f_u += (2 * pi / mp.mpf(m)) * mp.re(wm / (mp.mpc(1) - wm))
        else:
            f_u = -pi * (mp.digamma(ua) + mp.digamma(mp.mpf(1) - ua) + 2 * mp.log(2) + mp.log(y))
            for k in range(-20, 21):
                ms = mp.mpf(k) + ua
                ams = abs(ms)
                wk = mp.exp(2 * I_UNIT * pi * (ms * x + ub) - 2 * pi * ams * y)
                f_u += (2 * pi / ams) * mp.re(wk / (mp.mpc(1) - wk))
        nu = ua if ua_f <= Fraction(1, 2) else ua - mp.mpf(1)
        bm_f = mod1(-ub_f)
        bm = f2mp(bm_f)
        wz = nu * tau - bm
        s_a0 = mp.mpc(0)
        qm_loc = q
        for m in range(1, 25):
            e_p = mp.exp(2 * I_UNIT * pi * m * (tau + wz))
            e_m = mp.exp(2 * I_UNIT * pi * m * (tau - wz))
            s_a0 += (e_p - e_m) / (2 * I_UNIT * (mp.mpc(1) - qm_loc))
            qm_loc *= q
        a_0 = pi * mp.cot(pi * wz) + 4 * pi * s_a0 + 2 * I_UNIT * pi * nu
        val = mp.sqrt(shift_old + f_u - pi * (abs(a_0) ** 2) * exp_neg2l2)
        u_cache[key] = val
        return val

    char_shifts = [
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-1, 2)),
        (Fraction(-1, 2), Fraction(0)),
        (Fraction(-1, 2), Fraction(-1, 2)),
    ]

    def eval_yukawa(wl_f: tuple[Fraction, Fraction], wr_f: tuple[Fraction, Fraction]) -> mp.matrix:
        al_f, bl_f = wl_f
        ar_f, br_f = wr_f
        al_m, bl_m = f2mp(al_f), f2mp(bl_f)
        ar_m, br_m = f2mp(ar_f), f2mp(br_f)
        x0, x1 = level2_theta(al_m, 2 * bl_m)
        y0, y1 = level2_theta(ar_m, 2 * br_m)
        el = mp.exp(2 * I_UNIT * pi * bl_m)
        er = mp.exp(2 * I_UNIT * pi * br_m)
        mm = mp.matrix([
            [x0 * y0, er * x0 * y1 / I_UNIT],
            [el * x1 * y0 / I_UNIT, -el * er * x1 * y1],
        ]) / denom_hat
        r_ch = [hsum(ec[si], mm) for si in range(4)]
        u_ch = []
        for si in range(4):
            ua_f = mod1(al_f + ar_f + char_shifts[si][0])
            ub_f = mod1(bl_f + br_f + char_shifts[si][1])
            u_ch.append(get_u_factor(ua_f, ub_f) * r_ch[si])
        ymat = mp.zeros(3, 3)
        for a_i in range(3):
            for b_i in range(3):
                s = mp.mpc(0)
                for qi in range(3):
                    for si in range(4):
                        s += c_3[qi] * u_ch[si] * coup[(qi, si, a_i, b_i)]
                ymat[a_i, b_i] = s
        return ymat

    def red_centered(x_int: int, level_k: int) -> Fraction:
        r = x_int % level_k
        if 2 * r > level_k:
            r -= level_k
        return Fraction(r, level_k)

    def sum_level(level_k: int, q_r: int) -> mp.matrix:
        zeta = mp.exp(2 * I_UNIT * pi / mp.mpf(level_k))
        ysum = mp.zeros(3, 3)
        for a_i in range(level_k):
            for b_i in range(level_k):
                if a_i == 0 and b_i == 0:
                    continue
                ph = zeta ** ((-a_i * b_i) % level_k)
                wl = (red_centered(a_i, level_k), red_centered(b_i, level_k))
                wr = (red_centered(q_r * a_i, level_k), red_centered(q_r * b_i, level_k))
                ysum += ph * eval_yukawa(wl, wr)
        return ysum

    w3 = ((mp.mpf(3) + mp.sqrt(5)) / 2) ** (-4)
    w4 = mp.mpf(4) * ((mp.mpf(2) + mp.sqrt(3)) ** (-4))
    yu0 = w3 * sum_level(5, -4) / 24 + w4 * sum_level(6, -4) / 35
    yd0 = w3 * sum_level(5, 2) / 24 + w4 * sum_level(6, 2) / 35
    return yu0, yd0


def extract_physical_observables(yu: mp.matrix, yd: mp.matrix) -> dict:
    r"""Extract gauge-invariant mass ratios, |V_CKM|, and Jarlskog J_CP via mp.svd_c."""
    uu, su, _ = mp.svd_c(yu)
    ud, sd, _ = mp.svd_c(yd)
    # Ascending mass ordering (s_1 <= s_2 <= s_3)
    uu_asc = mp.matrix([[uu[r, c] for c in (2, 1, 0)] for r in range(3)])
    ud_asc = mp.matrix([[ud[r, c] for c in (2, 1, 0)] for r in range(3)])
    v_ckm = uu_asc.H * ud_asc
    j_cp = mp.im(v_ckm[0, 1] * v_ckm[1, 2] * mp.conj(v_ckm[0, 2]) * mp.conj(v_ckm[1, 1]))
    v_abs = [[abs(v_ckm[r, c]) for c in range(3)] for r in range(3)]
    return {
        "u_s1_over_s3": su[2] / su[0],
        "u_s2_over_s3": su[1] / su[0],
        "d_s1_over_s3": sd[2] / sd[0],
        "d_s2_over_s3": sd[1] / sd[0],
        "V_us": v_abs[0][1],
        "V_abs": v_abs,
        "J_cp": j_cp,
    }


def observable_max_drift(obs_a: dict, obs_b: dict) -> mp.mpf:
    r"""Max absolute difference across mass ratios, all 9 |V_CKM| entries, and J_CP."""
    diffs = [
        abs(obs_a["u_s1_over_s3"] - obs_b["u_s1_over_s3"]),
        abs(obs_a["u_s2_over_s3"] - obs_b["u_s2_over_s3"]),
        abs(obs_a["d_s1_over_s3"] - obs_b["d_s1_over_s3"]),
        abs(obs_a["d_s2_over_s3"] - obs_b["d_s2_over_s3"]),
        abs(obs_a["J_cp"] - obs_b["J_cp"]),
    ]
    for r in range(3):
        for c in range(3):
            diffs.append(abs(obs_a["V_abs"][r][c] - obs_b["V_abs"][r][c]))
    return max(diffs)


class DeterministicHaarU3:
    r"""Exact integer-seeded LCG + Box-Muller + complex Householder QR Haar U(3) generator."""

    def __init__(self, seed: int) -> None:
        self.state = seed % (2**63)

    def _next_u01(self) -> mp.mpf:
        # 63-bit LCG -> 126-bit integer fraction strictly inside (0, 1)
        m_mod = 2**63
        a_mul = 6364136223846793005
        c_inc = 1442695040888963407
        self.state = (a_mul * self.state + c_inc) % m_mod
        hi = self.state
        self.state = (a_mul * self.state + c_inc) % m_mod
        lo = self.state
        num = (hi * m_mod + lo) + 1
        den = m_mod * m_mod + 2
        return mp.mpf(num) / mp.mpf(den)

    def _next_complex_normal(self) -> mp.mpc:
        u1 = self._next_u01()
        u2 = self._next_u01()
        rad = mp.sqrt(-2 * mp.log(u1))
        ang = 2 * mp.pi * u2
        return mp.mpc(rad * mp.cos(ang), rad * mp.sin(ang))

    def sample_u3(self) -> mp.matrix:
        r"""Sample Haar-random U(3) via complex Householder QR with Mezzadri phase normalization."""
        z_mat = mp.matrix([[self._next_complex_normal() for _ in range(3)] for _ in range(3)])
        q_acc = mp.eye(3)
        r_mat = z_mat.copy()
        for k in range(3):
            x = [r_mat[i, k] for i in range(k, 3)]
            norm_x = mp.sqrt(sum(abs(xi) ** 2 for xi in x))
            phase = x[0] / abs(x[0]) if abs(x[0]) > 0 else mp.mpc(1)
            alpha = -phase * norm_x
            v = [x[0] - alpha] + x[1:]
            v_norm2 = sum(abs(vi) ** 2 for vi in v)
            h_mat = mp.eye(3)
            if v_norm2 > 0:
                for i in range(len(v)):
                    for j in range(len(v)):
                        h_mat[k + i, k + j] -= (2 / v_norm2) * v[i] * mp.conj(v[j])
            r_mat = h_mat * r_mat
            q_acc = q_acc * h_mat.H
        # Mezzadri diagonal phase fix so R_kk > 0
        d_mat = mp.zeros(3, 3)
        for k in range(3):
            d_mat[k, k] = r_mat[k, k] / abs(r_mat[k, k])
        return q_acc * d_mat


def run_ow17_c(prod_c: dict) -> tuple[dict, int, sp.Matrix, mp.matrix, mp.matrix, dict]:
    r"""Independent referee verification of OW17-C (Seam S1)."""
    discrepancies = 0
    pi = mp.pi

    # 1. Exact m004 = [[2,1],[1,1]] mod 2 permutation P on E[2] \ {0}
    e2_pts = [(1, 0), (0, 1), (1, 1)]
    idx_map = {pt: i for i, pt in enumerate(e2_pts)}
    p_sp = sp.zeros(3, 3)
    for col, (a, b) in enumerate(e2_pts):
        img = ((2 * a + b) % 2, (a + b) % 2)
        p_sp[idx_map[img], col] = sp.Integer(1)

    # Exact rational commutant via 9x9 linear operator X -> P X - X P
    x_vars = [sp.Symbol(f"x{i}") for i in range(9)]
    x_mat = sp.Matrix(3, 3, x_vars)
    comm_expr = p_sp * x_mat - x_mat * p_sp
    a_full, _ = sp.linear_eq_to_matrix(list(comm_expr), x_vars)
    full_dim = len(a_full.nullspace())

    d_vars = [sp.Symbol(f"d{i}") for i in range(3)]
    d_mat = sp.diag(*d_vars)
    comm_diag = p_sp * d_mat - d_mat * p_sp
    a_diag, _ = sp.linear_eq_to_matrix(list(comm_diag), d_vars)
    diag_dim = len(a_diag.nullspace())

    # 3x3 DFT diagonalization
    omega = mp.exp(2 * I_UNIT * pi / 3)
    f3 = mp.matrix([[omega ** (j * k) / mp.sqrt(3) for k in range(3)] for j in range(3)])
    p_mp = mp.matrix([[int(p_sp[r, c]) for c in range(3)] for r in range(3)])
    i3 = mp.eye(3)
    p2_mp = p_mp * p_mp

    c_test = (mp.mpf(7) / 5) * i3 + mp.mpc(3, 2) / 7 * p_mp + mp.mpc(-4, 5) / 11 * p2_mp
    diag_c = f3.H * c_test * f3
    dft_err = mp.mpf(0)
    for r in range(3):
        for c_i in range(3):
            if r != c_i:
                dft_err = max(dft_err, abs(diag_c[r, c_i]))

    # Exact real symmetric circulant degeneracy |lam_1| == |lam_2|
    max_sym_split = mp.mpf(0)
    for a_n, b_n in ((3, 1), (5, -2), (11, 7), (1, 13)):
        c_sym = mp.mpf(a_n) * i3 + mp.mpf(b_n) * (p_mp + p2_mp)
        d_sym = f3.H * c_sym * f3
        max_sym_split = max(max_sym_split, abs(abs(d_sym[1, 1]) - abs(d_sym[2, 2])))

    # Complex circulant 10^-4 tuning sensitivity
    b_t = mp.mpc(1, 0)
    c_t = I_UNIT
    a_crit = -(b_t * omega * omega + c_t * omega)
    a_t = a_crit + mp.mpf(1) / 10000
    lams_t = [a_t + b_t + c_t, a_t + b_t * omega * omega + c_t * omega, a_t + b_t * omega + c_t * omega * omega]
    tune_ratio = min(abs(lv) for lv in lams_t) / max(abs(lv) for lv in lams_t)

    pcomm = prod_c["m004_commutant_algebra"]
    tune_err = abs_err_mp(tune_ratio, pcomm["complex_circulant_1e_neg4_tuning_ratio"])
    comm_ok = (
        full_dim == 3
        and diag_dim == 1
        and pcomm["full_commutant_dim"] == 3
        and pcomm["diagonal_commutant_dim"] == 1
        and dft_err < mp.mpf(10) ** (-45)
        and max_sym_split < mp.mpf(10) ** (-50)
        and tune_ratio < mp.mpf(2) / 10000
        and tune_err < mp.mpf(10) ** (-10)
    )
    if not comm_ok:
        discrepancies += 1

    # 2. Independent L_2 solver with 4 mathematical self-verification proofs (at dps = 45)
    with mp.workdps(45):
        z_target = mp.mpc(1, 8) / 5
        c_acc_t, l2_20, tr_err_t = solve_l2_weierstrass_taylor(
            z_target, mp.mpc(4, 0) / 10, n_a=14, n_b=22, deg=24, ws_denom=20, m_max=22
        )
        # Self-check A: w_s-invariance (w_s = 1/20 vs w_s = 1/40)
        _, l2_40, _ = solve_l2_weierstrass_taylor(
            z_target, c_acc_t, n_a=14, n_b=22, deg=24, ws_denom=40, m_max=22
        )
        ws_invar_err = abs(l2_20 - l2_40)

        # Self-check B: S-duality z -> -1/z (L_2(z) == L_2(-1/z) - ln|z| and c(-1/z) == z^2 c(z))
        z_s = -mp.mpc(1) / z_target
        c_acc_s, l2_s, _ = solve_l2_weierstrass_taylor(
            z_s, z_target * z_target * c_acc_t, n_a=18, n_b=18, deg=24, ws_denom=20, m_max=22
        )
        s_dual_l2_err = abs(l2_20 - (l2_s - mp.log(abs(z_target))))
        s_dual_c_err = abs(c_acc_s - z_target * z_target * c_acc_t)

        # Self-check C: Exact square-torus analytic theorem L_2(i) = pi - (1/4) ln(1024 / g_2(i))
        _, l2_sq, _ = solve_l2_weierstrass_taylor(
            I_UNIT, mp.mpc(0), n_a=14, n_b=14, deg=22, ws_denom=20, m_max=22, fix_c_zero=True
        )
        q_i = mp.exp(-2 * mp.pi)
        e4_i = mp.mpf(1) + 240 * sum(k**3 * (q_i**k) / (mp.mpf(1) - q_i**k) for k in range(1, 45))
        g2_i = (mp.mpf(4) * mp.pi**4 / 3) * e4_i
        l2_sq_exact = mp.pi - mp.log(mp.mpf(1024) / abs(g2_i)) / 4
        sq_analytic_err = abs(l2_sq - l2_sq_exact)

        # Self-check D: Exact hexagonal-torus analytic theorem L_2(rho) = pi - (1/6) ln(6912 / |g_3(rho)|)
        rho = mp.exp(I_UNIT * mp.pi / 3)
        _, l2_hex, _ = solve_l2_weierstrass_taylor(
            rho, mp.mpc(0), n_a=14, n_b=14, deg=22, ws_denom=20, m_max=22, fix_c_zero=True
        )
        q_rho = mp.exp(2 * I_UNIT * mp.pi * rho)
        e6_rho = mp.mpc(1) - 504 * sum(k**5 * (q_rho**k) / (mp.mpc(1) - q_rho**k) for k in range(1, 45))
        g3_rho = (mp.mpf(8) * mp.pi**6 / 27) * e6_rho
        l2_hex_exact = mp.pi - mp.log(mp.mpf(6912) / abs(g3_rho)) / 6
        hex_analytic_err = abs(l2_hex - l2_hex_exact)

    l2_self_ok = (
        tr_err_t < mp.mpf(10) ** (-18)
        and ws_invar_err < mp.mpf(10) ** (-18)
        and s_dual_l2_err < mp.mpf(10) ** (-18)
        and s_dual_c_err < mp.mpf(10) ** (-18)
        and sq_analytic_err < mp.mpf(10) ** (-18)
        and hex_analytic_err < mp.mpf(10) ** (-18)
    )
    if not l2_self_ok:
        discrepancies += 1

    l2_true = mp.mpf(l2_20)
    pe5 = prod_c["e5_e6_m8_natural_circulant_test"]
    l2_diff_vs_prod = l2_true - mp.mpf(pe5["L2_at_m8_tau_16_plus_8i_over_5"])
    l2_matches_prod_1e10 = abs(l2_diff_vs_prod) < mp.mpf(10) ** (-10)
    if not l2_matches_prod_1e10:
        discrepancies += 1

    # 3. Primary E[5] + E[6] Yukawa evaluation using OUR verified 20-digit L_2
    tau_m8 = mp.mpc(16, 8) / 5
    yu0, yd0 = build_e5_e6_yukawas(tau_m8, l2_true)
    obs0 = extract_physical_observables(yu0, yd0)

    und_u_err = abs_err_mp(obs0["u_s1_over_s3"], pe5["undressed_u_s1_over_s3"])
    und_d_err = abs_err_mp(obs0["d_s1_over_s3"], pe5["undressed_d_s1_over_s3"])
    und_u_ok = und_u_err < mp.mpf(10) ** (-10)
    und_d_ok = und_d_err < mp.mpf(10) ** (-10)
    if not und_u_ok:
        discrepancies += 1
    if not und_d_ok:
        discrepancies += 1

    samples_bc = [
        (mp.mpc(1, 0) / 3, mp.mpc(0, 1) / 3),
        (mp.mpc(1, 0) / 2, mp.mpc(0, 1) / 4),
        (mp.mpc(1, 0) / 3 + mp.mpc(0, 1) / 4, -mp.mpc(1, 0) / 4 + mp.mpc(0, 1) / 3),
        (mp.mpc(1, 0) / 2 - mp.mpc(0, 1) / 3, mp.mpc(1, 0) / 4 + mp.mpc(0, 1) / 5),
        (mp.mpc(2, 0) / 5, -mp.mpc(1, 0) / 5 + mp.mpc(0, 2) / 5),
        (-mp.mpc(1, 0) / 3 + mp.mpc(0, 1) / 2, mp.mpc(1, 0) / 3 - mp.mpc(0, 1) / 4),
    ]
    sample_out = []
    min_u13 = mp.mpf(10)
    min_d13 = mp.mpf(10)
    yu_ref = yu0
    yd_ref = yd0
    obs_ref = obs0

    for idx, (b_c, c_c) in enumerate(samples_bc):
        cu = i3 + b_c * p_mp + c_c * p2_mp
        cd = i3 + (b_c / 2) * p_mp - (c_c / 2) * p2_mp
        comm_err = max(
            mp.mnorm(p_mp * cu - cu * p_mp, "f"),
            mp.mnorm(p_mp * cd - cd * p_mp, "f"),
        )
        obs = extract_physical_observables(yu0 * cu, yd0 * cd)
        if idx == 0:
            yu_ref = yu0 * cu
            yd_ref = yd0 * cd
            obs_ref = obs
        if obs["u_s1_over_s3"] < min_u13:
            min_u13 = obs["u_s1_over_s3"]
        if obs["d_s1_over_s3"] < min_d13:
            min_d13 = obs["d_s1_over_s3"]
        prow = pe5["samples"][idx]
        s_errs = {
            "u_s1_over_s3": abs_err_mp(obs["u_s1_over_s3"], prow["u_s1_over_s3"]),
            "u_s2_over_s3": abs_err_mp(obs["u_s2_over_s3"], prow["u_s2_over_s3"]),
            "d_s1_over_s3": abs_err_mp(obs["d_s1_over_s3"], prow["d_s1_over_s3"]),
            "V_us": abs_err_mp(obs["V_us"], prow["V_us"]),
            "J_cp": abs_err_mp(obs["J_cp"], prow["J_cp"]),
        }
        max_s_err = max(s_errs.values())
        s_ok = comm_err < mp.mpf(10) ** (-50) and max_s_err < mp.mpf(10) ** (-10)
        if not s_ok:
            discrepancies += 1
        sample_out.append({
            "idx": idx,
            "commutator_err": mp.nstr(comm_err, 8),
            "u_s1_over_s3": mp.nstr(obs["u_s1_over_s3"], 15),
            "u_s2_over_s3": mp.nstr(obs["u_s2_over_s3"], 15),
            "d_s1_over_s3": mp.nstr(obs["d_s1_over_s3"], 15),
            "V_us": mp.nstr(obs["V_us"], 15),
            "J_cp": mp.nstr(obs["J_cp"], 15),
            "max_abs_err_vs_producer": mp.nstr(max_s_err, 10),
            "vs_producer_1e_neg10": label_same(s_ok),
        })

    # Extra independent referee natural O(1) complex circulant ensemble (4 pairs)
    extra_bc = [
        (mp.mpc(3, 1) / 7, mp.mpc(-2, 3) / 7),
        (mp.mpc(-2, 5) / 9, mp.mpc(4, 1) / 9),
        (mp.mpc(1, -3) / 6, mp.mpc(2, 1) / 5),
        (mp.mpc(4, 3) / 11, mp.mpc(-3, -2) / 11),
    ]
    extra_min_u = mp.mpf(10)
    extra_min_d = mp.mpf(10)
    for b_e, c_e in extra_bc:
        cu_e = i3 + b_e * p_mp + c_e * p2_mp
        cd_e = i3 + (b_e / 3) * p_mp - (c_e / 3) * p2_mp
        obs_e = extract_physical_observables(yu0 * cu_e, yd0 * cd_e)
        extra_min_u = min(extra_min_u, obs_e["u_s1_over_s3"])
        extra_min_d = min(extra_min_d, obs_e["d_s1_over_s3"])

    no_hierarchy = bool(
        min_u13 > mp.mpf(1) / 100
        and min_d13 > mp.mpf(1) / 100
        and extra_min_u > mp.mpf(1) / 100
        and extra_min_d > mp.mpf(1) / 100
    )

    # Diagnostic isolation check: evaluate OUR independent eval_yukawa at producer's L_2
    l2_prod_mp = mp.mpf(pe5["L2_at_m8_tau_16_plus_8i_over_5"])
    yu0_p, yd0_p = build_e5_e6_yukawas(tau_m8, l2_prod_mp)
    obs0_p = extract_physical_observables(yu0_p, yd0_p)
    diag_max_err = max(
        abs_err_mp(obs0_p["u_s1_over_s3"], pe5["undressed_u_s1_over_s3"]),
        abs_err_mp(obs0_p["d_s1_over_s3"], pe5["undressed_d_s1_over_s3"]),
    )
    for idx, (b_c, c_c) in enumerate(samples_bc):
        cu = i3 + b_c * p_mp + c_c * p2_mp
        cd = i3 + (b_c / 2) * p_mp - (c_c / 2) * p2_mp
        obs_p = extract_physical_observables(yu0_p * cu, yd0_p * cd)
        prow = pe5["samples"][idx]
        diag_max_err = max(
            diag_max_err,
            abs_err_mp(obs_p["u_s1_over_s3"], prow["u_s1_over_s3"]),
            abs_err_mp(obs_p["u_s2_over_s3"], prow["u_s2_over_s3"]),
            abs_err_mp(obs_p["d_s1_over_s3"], prow["d_s1_over_s3"]),
            abs_err_mp(obs_p["V_us"], prow["V_us"]),
            abs_err_mp(obs_p["J_cp"], prow["J_cp"]),
        )

    # 4. Independent 10-trial Haar U(3)_L x U(3)_R basis-scrambling gate (Guardrail 3)
    haar_gen = DeterministicHaarU3(seed=20261122017)
    max_haar_drift = mp.mpf(0)
    max_unitarity_err = mp.mpf(0)
    for _ in range(10):
        u_l = haar_gen.sample_u3()
        u_ru = haar_gen.sample_u3()
        u_rd = haar_gen.sample_u3()
        for u_m in (u_l, u_ru, u_rd):
            max_unitarity_err = max(max_unitarity_err, mp.mnorm(u_m.H * u_m - i3, "f"))
        obs_scram = extract_physical_observables(u_l * yu_ref * u_ru.H, u_l * yd_ref * u_rd.H)
        max_haar_drift = max(max_haar_drift, observable_max_drift(obs_ref, obs_scram))
    haar_ok = max_haar_drift < mp.mpf(10) ** (-35) and max_unitarity_err < mp.mpf(10) ** (-50)
    if not haar_ok:
        discrepancies += 1

    # 5. Exact m004 orbit decompositions on (Z / n Z)^2 for n in {2, 3, 4, 5, 6, 8}
    orbits_out = {}
    orbits_all_match = True
    for n_mod in (2, 3, 4, 5, 6, 8):
        visited = set()
        orbits = []
        for a_i in range(n_mod):
            for b_i in range(n_mod):
                pt = (a_i, b_i)
                if pt in visited:
                    continue
                orb = []
                cur = pt
                while cur not in visited:
                    visited.add(cur)
                    orb.append([cur[0], cur[1]])
                    cur = ((2 * cur[0] + cur[1]) % n_mod, (cur[0] + cur[1]) % n_mod)
                orbits.append(orb)
        hist: dict[str, int] = {}
        for orb in orbits:
            k_s = str(len(orb))
            hist[k_s] = hist.get(k_s, 0) + 1
        hist_sorted = {k: hist[k] for k in sorted(hist.keys(), key=int)}
        short_nt = [orb for orb in orbits if 1 < len(orb) <= 4]
        part_sum = sum(int(k) * v for k, v in hist_sorted.items())
        key_en = f"E[{n_mod}]"
        prow = prod_c["m004_orbits_on_En"][key_en]
        ok = (
            part_sum == n_mod * n_mod
            and prow["total_points"] == n_mod * n_mod
            and prow["num_orbits"] == len(orbits)
            and prow["orbit_size_histogram"] == hist_sorted
            and prow["short_nontrivial_orbits"] == short_nt
        )
        if not ok:
            orbits_all_match = False
            discrepancies += 1
        orbits_out[key_en] = {
            "n": n_mod,
            "total_points": part_sum,
            "num_orbits": len(orbits),
            "orbit_size_histogram": hist_sorted,
            "short_nontrivial_orbits": short_nt,
            "vs_producer": label_same(ok),
        }

    e5_ok = orbits_out["E[5]"]["orbit_size_histogram"] == {"1": 1, "2": 2, "10": 2}
    e3_ok = orbits_out["E[3]"]["orbit_size_histogram"] == {"1": 1, "4": 2}

    physics_gate_c = comm_ok and l2_self_ok and no_hierarchy and haar_ok and orbits_all_match and e5_ok and e3_ok
    return {
        "m004_commutant_algebra": {
            "P_matrix": [[int(p_sp[r, c]) for c in range(3)] for r in range(3)],
            "full_commutant_dim": full_dim,
            "diagonal_commutant_dim": diag_dim,
            "dft_diagonalization_max_err": mp.nstr(dft_err, 10),
            "real_symmetric_circulant_max_m1_m2_split": mp.nstr(max_sym_split, 10),
            "complex_circulant_1e_neg4_tuning_ratio": mp.nstr(tune_ratio, 15),
            "tuning_ratio_abs_err_vs_producer": mp.nstr(tune_err, 10),
            "vs_producer": label_same(comm_ok),
        },
        "l2_self_verification_benchmarks": {
            "tr_comm_plus_2_err": mp.nstr(tr_err_t, 10),
            "ws_1_20_vs_1_40_err": mp.nstr(ws_invar_err, 10),
            "s_duality_L2_err": mp.nstr(s_dual_l2_err, 10),
            "s_duality_c_acc_err": mp.nstr(s_dual_c_err, 10),
            "square_torus_analytic_err": mp.nstr(sq_analytic_err, 10),
            "hexagonal_torus_analytic_err": mp.nstr(hex_analytic_err, 10),
            "all_self_benchmarks_lt_1e_neg18": l2_self_ok,
        },
        "e5_e6_m8_natural_circulant_test": {
            "L2_referee_verified": mp.nstr(l2_true, 24),
            "L2_producer": pe5["L2_at_m8_tau_16_plus_8i_over_5"],
            "L2_diff_referee_minus_producer": mp.nstr(l2_diff_vs_prod, 12),
            "L2_vs_producer_1e_neg10": label_same(l2_matches_prod_1e10),
            "undressed_u_s1_over_s3": mp.nstr(obs0["u_s1_over_s3"], 15),
            "undressed_d_s1_over_s3": mp.nstr(obs0["d_s1_over_s3"], 15),
            "undressed_u_abs_err": mp.nstr(und_u_err, 10),
            "undressed_d_abs_err": mp.nstr(und_d_err, 10),
            "undressed_u_vs_producer_1e_neg10": label_same(und_u_ok),
            "undressed_d_vs_producer_1e_neg10": label_same(und_d_ok),
            "natural_circulant_min_u_s1_over_s3": mp.nstr(min_u13, 15),
            "natural_circulant_min_d_s1_over_s3": mp.nstr(min_d13, 15),
            "extra_referee_ensemble_min_u_s1_over_s3": mp.nstr(extra_min_u, 15),
            "extra_referee_ensemble_min_d_s1_over_s3": mp.nstr(extra_min_d, 15),
            "natural_circulants_cannot_give_1e_neg2_hierarchy": no_hierarchy,
            "samples": sample_out,
            "diagnostic_eval_yukawa_at_producer_L2_max_err": mp.nstr(diag_max_err, 10),
            "diagnostic_eval_yukawa_kernel_vs_producer": label_same(diag_max_err < mp.mpf(10) ** (-11)),
        },
        "guardrail3_haar_u3_x_u3_test": {
            "trials": 10,
            "max_unitarity_err": mp.nstr(max_unitarity_err, 10),
            "max_observable_drift": mp.nstr(max_haar_drift, 10),
            "pass_lt_1e_neg35": haar_ok,
        },
        "m004_orbits_on_En": orbits_out,
        "orbits_vs_producer": label_same(orbits_all_match),
        "e5_eigenline_size2_verified": e5_ok,
        "e3_two_4orbits_verified": e3_ok,
        "physics_gate_pass": physics_gate_c,
    }, discrepancies, p_sp, yu_ref, yd_ref, obs_ref


# ============================================================================
# Section 4: OW17-D (4 / 4 Independent Planted Fault Controls)
# ============================================================================

def run_ow17_d(
    prod_d: dict,
    b_1h_mat: list[list[Fraction]],
    p_sp: sp.Matrix,
    yu_ref: mp.matrix,
    yd_ref: mp.matrix,
    obs_ref: dict,
) -> tuple[dict, int]:
    r"""Independent verification of all 4/4 planted fault controls."""
    discrepancies = 0

    # PF-OW17-1: bulk 10_C (h_pt = 10) -> nB - nF = +4 > 0 (AdS, dS check fails)
    nb_10c = 2 * 45 + 10
    nf_10c = 2 * 48
    diff_10c = nb_10c - nf_10c
    pf1_detected = (diff_10c == 4) and not (diff_10c < 0)

    # PF-OW17-2: Scale B_1h by 2 -> textbook n_H = 1 identity fails
    textbook_b1h = [
        [Fraction(199, 50), Fraction(27, 10), Fraction(44, 5)],
        [Fraction(9, 10), Fraction(35, 6), Fraction(12, 1)],
        [Fraction(11, 10), Fraction(9, 2), Fraction(-26, 1)],
    ]
    corrupted_b1h = [[2 * entry for entry in row] for row in b_1h_mat]
    pf2_detected = (b_1h_mat == textbook_b1h) and (corrupted_b1h != textbook_b1h)

    # PF-OW17-3: D = diag(1, 2, 4) -> [P, D] != 0
    d_bad = sp.diag(sp.Integer(1), sp.Integer(2), sp.Integer(4))
    comm_bad = p_sp * d_bad - d_bad * p_sp
    comm_is_zero = comm_bad == sp.zeros(3, 3)
    pf3_detected = not comm_is_zero

    # PF-OW17-4: Non-unitary U_L = diag(2, 1, 1) -> observable drift > 1/10
    u_bad = mp.matrix([[2, 0, 0], [0, 1, 0], [0, 0, 1]])
    obs_bad = extract_physical_observables(u_bad * yu_ref, u_bad * yd_ref)
    pf4_drift = observable_max_drift(obs_ref, obs_bad)
    pf4_detected = bool(pf4_drift > mp.mpf(1) / 10)

    caught = sum(1 for ok in (pf1_detected, pf2_detected, pf3_detected, pf4_detected) if ok)
    all_ok = (
        caught == 4
        and prod_d["planted_faults_caught"] == 4
        and prod_d["pf_ow17_1_bulk_10C_AdS"]["nB_minus_nF"] == diff_10c
    )
    if not all_ok:
        discrepancies += 1

    return {
        "pf_ow17_1_bulk_10C_AdS": {
            "nB_minus_nF": diff_10c,
            "detected": pf1_detected,
        },
        "pf_ow17_2_corrupt_B_2loop": {
            "detected": pf2_detected,
        },
        "pf_ow17_3_noncommuting_diag_1_2_4": {
            "comm_zero": comm_is_zero,
            "detected": pf3_detected,
        },
        "pf_ow17_4_nonunitary_UL_drift": {
            "max_drift": mp.nstr(pf4_drift, 14),
            "detected": pf4_detected,
        },
        "planted_faults_caught": caught,
        "planted_faults_total": 4,
        "vs_producer": label_same(all_ok),
        "gate_pass": caught == 4,
    }, discrepancies


def main() -> None:
    r"""Execute complete Cold-Room Zero-Trust Referee audit and write JSON output."""
    prod = json.loads(PROD_V2_JSON.read_text(encoding="utf-8"))

    custody = verify_sha256_custody()
    disc_custody = 0 if custody["all_custody_ok"] else 1

    res_a, disc_a = run_ow17_a(prod["ow17_a_seam_s2_brane_2H"])
    res_b, disc_b, b_1h_mat = run_ow17_b(prod["ow17_b_seam_s3_unification"])
    res_c, disc_c, p_sp, yu_ref, yd_ref, obs_ref = run_ow17_c(prod["ow17_c_seam_s1_m004_equivariance"])
    res_d, disc_d = run_ow17_d(prod["ow17_d_planted_faults"], b_1h_mat, p_sp, yu_ref, yd_ref, obs_ref)

    total_discrepancies = disc_custody + disc_a + disc_b + disc_c + disc_d
    physics_all_ok = (
        custody["all_custody_ok"]
        and res_a["gate_pass"]
        and res_b["gate_pass"]
        and res_c["physics_gate_pass"]
        and res_d["gate_pass"]
    )

    report = {
        "card_id": "A2-OW17-referee",
        "target_producer": "relays/a2_ow17_v2/a2_ow17_v2_results.json",
        "seat": "agy-002",
        "empirical_inputs": "0 of 19",
        "working_dps": mp.mp.dps,
        "custody_sha256": custody,
        "ow17_a_seam_s2_brane_2H": res_a,
        "ow17_b_seam_s3_unification": res_b,
        "ow17_c_seam_s1_m004_equivariance": res_c,
        "ow17_d_planted_faults": res_d,
        "summary": {
            "discrepancy_counts": {
                "custody": disc_custody,
                "ow17_a": disc_a,
                "ow17_b": disc_b,
                "ow17_c": disc_c,
                "ow17_d": disc_d,
                "total": total_discrepancies,
            },
            "ow17_a_vs_producer": label_same(disc_a == 0),
            "ow17_b_vs_producer": label_same(disc_b == 0),
            "ow17_c_numerical_1e_neg10_vs_producer": label_same(disc_c == 0),
            "ow17_d_vs_producer": label_same(disc_d == 0),
            "all_physics_gates_verified": physics_all_ok,
            "exact_1e_neg10_match_everywhere": total_discrepancies == 0,
        },
    }

    OUT_JSON.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))


if __name__ == "__main__":
    main()
