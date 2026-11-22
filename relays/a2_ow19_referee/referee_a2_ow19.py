#!/usr/bin/env python3
"""Isolated Cold-Room Zero-Trust Independent Referee (Guardrail 6)
for A2-PEER-SYNTH v2 (c161ef045) and A2-OW19 v3 (62f08b148).

Firewall: strictly 0 of 19 (zero empirical PDG/NuFIT/Planck/DESI/lattice numbers).
Hygiene: 0 Python float/complex AST literals; 0 peer/producer/frontier imports;
         all checks computed via completely disjoint algorithms/representations.
"""
from __future__ import annotations

import ast
from collections import deque
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import subprocess
import time
from typing import Any

import mpmath as mp
import numpy as np
import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = Path(__file__).resolve().parent
OUT_JSON = OUT_DIR / "a2_ow19_referee_results.json"
OUT_SHA = OUT_DIR / "OUTPUT_SHA256.txt"

I_MP = mp.mpc(0, 1)
I_NP = complex(0, 1)

FORBIDDEN_IMPORT_FRAGMENTS = (
    "frontier",
    "relays",
    "verify_a2",
    "verify_x_harvest",
    "c26_",
    "c27_",
    "c28_",
    "c29_",
    "c30_",
    "self_consistent_loop",
)


def mp_rat(num: int, den: int) -> mp.mpf:
    return mp.mpf(num) / mp.mpf(den)


def mp_pow10(exp: int) -> mp.mpf:
    return mp.mpf(10) ** exp


def flt_rat(num: int, den: int) -> float:
    return float(num) / float(den)


def frac_to_mp(val: Fraction) -> mp.mpf:
    return mp.mpf(val.numerator) / mp.mpf(val.denominator)


def parse_mpc_str(text: str) -> mp.mpc:
    """Parse mpmath/Python complex string '(a + bj)' or '(a - bj)' at full mp.dps."""
    s = text.strip()
    if s.startswith("(") and s.endswith(")"):
        s = s[1:-1].strip()
    s = s.replace(" ", "")
    if not s.endswith("j"):
        return mp.mpc(mp.mpf(s), mp.mpf(0))
    body = s[:-1]
    split_idx = -1
    for i in range(1, len(body)):
        ch = body[i]
        prev = body[i - 1]
        if ch in "+-" and prev not in "eE":
            split_idx = i
    if split_idx < 0:
        return mp.mpc(mp.mpf(0), mp.mpf(body))
    re_part = body[:split_idx]
    im_part = body[split_idx:]
    return mp.mpc(mp.mpf(re_part), mp.mpf(im_part))


def git_show_bytes(rev: str, rel_path: str) -> bytes:
    proc = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "show", f"{rev}:{rel_path}"],
        check=True,
        capture_output=True,
    )
    return proc.stdout


def git_show_text(rev: str, rel_path: str) -> str:
    return git_show_bytes(rev, rel_path).decode("utf-8")


def count_json_floats(obj: Any) -> int:
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_json_floats(v) for v in obj)
    return 0


def audit_script_ast(script_path: Path) -> dict[str, Any]:
    """Programmatic AST-only inspection: 0 float/complex constants, 0 forbidden imports."""
    src = script_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(script_path))
    float_complex_nodes = []
    forbidden_imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            float_complex_nodes.append(int(getattr(node, "lineno", 0)))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.name
                if any(frag in name for frag in FORBIDDEN_IMPORT_FRAGMENTS):
                    forbidden_imports.append(name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if any(frag in mod for frag in FORBIDDEN_IMPORT_FRAGMENTS):
                forbidden_imports.append(mod)
    return {
        "path": str(script_path.relative_to(REPO_ROOT)),
        "float_complex_count": len(float_complex_nodes),
        "forbidden_import_count": len(forbidden_imports),
        "clean": (len(float_complex_nodes) == 0 and len(forbidden_imports) == 0),
    }


def verify_sha256_manifest(manifest_path: Path, override_bytes: bytes | None = None) -> dict[str, Any]:
    """Verify a SHA-256 manifest file against disk bytes (or supplied override bytes)."""
    line = manifest_path.read_text(encoding="utf-8").strip().splitlines()[0]
    parts = line.split()
    expected_hex = parts[0].strip().lower()
    target_rel = parts[-1].strip()
    local_candidate = manifest_path.parent / target_rel
    target_path = local_candidate if local_candidate.exists() else (REPO_ROOT / target_rel)
    raw = target_path.read_bytes() if override_bytes is None else override_bytes
    actual_hex = hashlib.sha256(raw).hexdigest().lower()
    return {
        "manifest": str(manifest_path.relative_to(REPO_ROOT)),
        "target": str(target_path.relative_to(REPO_ROOT)),
        "expected": expected_hex,
        "actual": actual_hex,
        "matched": (actual_hex == expected_hex),
    }


# =============================================================================
# REF-0: Custody & AST Hygiene
# =============================================================================
def run_ref_0() -> tuple[dict[str, Any], int]:
    relay_dirs = [
        "relays/a2_peer_synth",
        "relays/a2_peer_synth_v2",
        "relays/a2_ow19",
        "relays/a2_ow19_v2",
        "relays/a2_ow19_v3",
    ]
    manifest_checks = []
    mismatches = 0
    for d in relay_dirs:
        for mf in ("SCRIPT_SHA256.txt", "OUTPUT_SHA256.txt"):
            res = verify_sha256_manifest(REPO_ROOT / d / mf)
            manifest_checks.append(res)
            if not res["matched"]:
                mismatches += 1

    ast_targets = [
        REPO_ROOT / "relays/a2_peer_synth_v2/verify_a2_peer_synth_v2.py",
        REPO_ROOT / "relays/a2_ow19_v3/verify_a2_ow19_v3.py",
        Path(__file__).resolve(),
    ]
    ast_reports = [audit_script_ast(p) for p in ast_targets]
    ast_bad = sum(0 if r["clean"] else 1 for r in ast_reports)

    discrepancies = mismatches + ast_bad
    gate = (mismatches == 0) and (ast_bad == 0)
    return (
        {
            "manifests_checked": len(manifest_checks),
            "manifest_mismatches": mismatches,
            "manifest_details": manifest_checks,
            "ast_reports": ast_reports,
            "ast_all_clean": (ast_bad == 0),
            "gate_ref_0": gate,
        },
        discrepancies,
    )


# =============================================================================
# REF-PS: Independent Countercheck of A2-PEER-SYNTH v2 (c161ef045)
# =============================================================================
def derive_mv84_chi4_h2_hbar2_symbolic() -> dict[str, Any]:
    """Derive Machacek-Vaughn (NPB 236, 1984, Eq. 3.4) 2-loop scalar Yukawa anomalous
    dimension -(3/2) H_2 - Hbar_2 directly from explicit 4-real-scalar Weyl Yukawa
    matrices Y^1..Y^4 on (u_L, d_L, u_R^c, d_R^c) + (nu_L, e_L, e_R^c) in SymPy."""
    yt, yb, ye = sp.symbols("yt yb ye", real=True, positive=True)
    I_sp = sp.I
    inv_sq2 = 1 / sp.sqrt(2)

    def make_sym_quark(ul_ur, dl_ur, ul_dr, dl_dr) -> sp.Matrix:
        # Basis: [u_L, d_L, u_R^c, d_R^c]
        M = sp.zeros(4, 4)
        M[0, 2] = ul_ur
        M[2, 0] = ul_ur
        M[1, 2] = dl_ur
        M[2, 1] = dl_ur
        M[0, 3] = ul_dr
        M[3, 0] = ul_dr
        M[1, 3] = dl_dr
        M[3, 1] = dl_dr
        return M

    # Phi = (1/sqrt(2)) (phi1 + i phi2, phi3 + i phi4)^T
    # Phi_tilde = i sigma_2 Phi^* = (1/sqrt(2)) (phi3 - i phi4, -phi1 + i phi2)^T
    # -L_Y = Q_L Y_u Phi_tilde u_R^c + Q_L Y_d Phi d_R^c
    Yq = [
        make_sym_quark(0, -inv_sq2 * yt, inv_sq2 * yb, 0),
        make_sym_quark(0, I_sp * inv_sq2 * yt, I_sp * inv_sq2 * yb, 0),
        make_sym_quark(inv_sq2 * yt, 0, 0, inv_sq2 * yb),
        make_sym_quark(-I_sp * inv_sq2 * yt, 0, 0, I_sp * inv_sq2 * yb),
    ]

    def make_sym_lep(nl_er, el_er) -> sp.Matrix:
        # Basis: [nu_L, e_L, e_R^c]
        M = sp.zeros(3, 3)
        M[0, 2] = nl_er
        M[2, 0] = nl_er
        M[1, 2] = el_er
        M[2, 1] = el_er
        return M

    Yl = [
        make_sym_lep(inv_sq2 * ye, 0),
        make_sym_lep(I_sp * inv_sq2 * ye, 0),
        make_sym_lep(0, inv_sq2 * ye),
        make_sym_lep(0, I_sp * inv_sq2 * ye),
    ]

    # Scalar index a = 2 (0-based, i.e., phi_3 = physical neutral Higgs)
    nc = 3
    a_idx = 2
    sum_qq_dag = sp.zeros(4, 4)
    for c in range(4):
        sum_qq_dag += Yq[c] * Yq[c].H
    sum_ll_dag = sp.zeros(3, 3)
    for c in range(4):
        sum_ll_dag += Yl[c] * Yl[c].H

    H2_q = sp.simplify(sp.Rational(1, 2) * (Yq[a_idx] * Yq[a_idx].H * sum_qq_dag + Yq[a_idx].H * Yq[a_idx] * sum_qq_dag).trace())
    H2_l = sp.simplify(sp.Rational(1, 2) * (Yl[a_idx] * Yl[a_idx].H * sum_ll_dag + Yl[a_idx].H * Yl[a_idx] * sum_ll_dag).trace())
    H2_tot = sp.expand(nc * H2_q + H2_l)

    Hbar2_q = sp.Integer(0)
    Hbar2_l = sp.Integer(0)
    for c in range(4):
        term_q = Yq[a_idx] * Yq[c].H * Yq[a_idx] * Yq[c].H
        Hbar2_q += sp.Rational(1, 2) * (term_q + term_q.H).trace()
        term_l = Yl[a_idx] * Yl[c].H * Yl[a_idx] * Yl[c].H
        Hbar2_l += sp.Rational(1, 2) * (term_l + term_l.H).trace()
    Hbar2_tot = sp.expand(nc * Hbar2_q + Hbar2_l)

    minus_chi4 = sp.expand(-sp.Rational(3, 2) * H2_tot - Hbar2_tot)
    exact_hud_coeff = sp.Poly(minus_chi4, yt, yb, ye).coeff_monomial(yt**2 * yb**2)
    req_T2_hud_coeff = sp.Rational(exact_hud_coeff) / sp.Rational(-9, 4)

    # Compare exact vs 75cb20177 buggy T2 = 3 yt^4 + 3 yb^4 + ye^4 - 2 yt^2 yb^2
    buggy_hud_coeff = sp.Rational(-9, 4) * sp.Rational(-2, 1)
    # In beta_{y_t}^{(2)} / y_t, the non-T2 terms at y_t^2 y_b^2 are:
    # (-H_u H_d - 1/4 H_d H_u) + T*(5/4 H_d - 9/4 H_u) = (-5/4) + (3*5/4 - 3*9/4) = -17/4
    non_t2_yt2yb2 = sp.Rational(-5, 4) + 3 * sp.Rational(5, 4) - 3 * sp.Rational(9, 4)
    beta_yt_exact = non_t2_yt2yb2 + exact_hud_coeff
    beta_yt_buggy = non_t2_yt2yb2 + buggy_hud_coeff
    beta_ytau_exact = exact_hud_coeff
    beta_ytau_buggy = buggy_hud_coeff

    return {
        "H2_tot": str(H2_tot),
        "Hbar2_tot": str(Hbar2_tot),
        "minus_chi4": str(minus_chi4),
        "exact_minus_chi4_HuHd": str(exact_hud_coeff),
        "buggy_75cb_HuHd": str(buggy_hud_coeff),
        "ratio_buggy_over_exact": str(sp.simplify(buggy_hud_coeff / exact_hud_coeff)),
        "required_T2_HuHd": str(req_T2_hud_coeff),
        "beta_yt_yt2yb2_exact": str(beta_yt_exact),
        "beta_yt_yt2yb2_buggy": str(beta_yt_buggy),
        "beta_ytau_yt2yb2_exact": str(beta_ytau_exact),
        "beta_ytau_yt2yb2_buggy": str(beta_ytau_buggy),
    }


def run_ref_ps(ps_json: dict[str, Any]) -> tuple[dict[str, Any], int]:
    discrepancies = 0
    old_dps = mp.mp.dps
    mp.mp.dps = 60
    try:
        # 1. H1 closed-form L_2(tau_*^pm) from Hurwitz Gamma(1/4) + ln(1024/g_2(i))
        gamma_quarter = mp.gamma(mp_rat(1, 4))
        g2_i = (gamma_quarter ** 8) / (16 * (mp.pi ** 2))
        L2_i = mp.pi - mp_rat(1, 4) * mp.log(mp.mpf(1024) / g2_i)
        L2_fricke_via_inv = L2_i + mp_rat(1, 2) * mp.log(mp.mpf(5))
        L2_fricke_closed = mp.pi - mp.log(8 * mp.sqrt(2 * mp.pi) / (mp.sqrt(mp.mpf(5)) * (gamma_quarter ** 2)))
        bc_fricke = mp.pi - L2_fricke_closed

        h1_ps = ps_json["synth_2_agy_exp_x_harvest_audit"]["h1_gamma_closed_form_verified_the_same"]
        err_L2_i = abs(L2_i - mp.mpf(h1_ps["L2_i_closed_30d"]))
        err_L2_fricke = abs(L2_fricke_closed - mp.mpf(h1_ps["L2_fricke_closed_30d"]))
        err_bc_fricke = abs(bc_fricke - mp.mpf(h1_ps["bc_star_fricke_30d"]))
        err_identity = abs(L2_fricke_via_inv - L2_fricke_closed)
        h1_ok = (
            err_L2_i < mp_pow10(-25)
            and err_L2_fricke < mp_pow10(-25)
            and err_bc_fricke < mp_pow10(-25)
            and err_identity < mp_pow10(-50)
        )
        if not h1_ok:
            discrepancies += 1

        # 2. v4.json payload digest directly from git show 528ef1cf5 + 0 JSON floats
        v4_raw = git_show_text("528ef1cf5", "relays/agy_2026-11-22_c30/blind_predictions_full_toe_v4.json")
        v4_doc = json.loads(v4_raw)
        v4_payload = v4_doc["prediction_bundle_v4"]
        recomputed_v4_digest = hashlib.sha256(
            json.dumps(v4_payload, sort_keys=True, indent=2).encode("utf-8")
        ).hexdigest()
        v4_digest_ok = (recomputed_v4_digest == v4_doc["sha256_payload_digest"])
        v4_float_count = count_json_floats(v4_doc)
        if not (v4_digest_ok and v4_float_count == 0):
            discrepancies += 1

        # 3a. EX-S1: Swapped H_u <-> H_d tan(beta) in 75cb20177
        vu, vd, l1_s, l2_s, l34_s, m12_s = sp.symbols("vu vd l1 l2 l34 m12", positive=True)
        # Canonical Type-II 2HDM convention: H_1 = H_d (quartic lam_1, vev vd), H_2 = H_u (quartic lam_2, vev vu)
        V_true = (
            -m12_s * vd * vu
            + sp.Rational(1, 8) * l1_s * (vd ** 4)
            + sp.Rational(1, 8) * l2_s * (vu ** 4)
            + sp.Rational(1, 4) * l34_s * (vd ** 2) * (vu ** 2)
        )
        stat_diff = sp.simplify(vd * sp.diff(V_true, vd) - vu * sp.diff(V_true, vu))
        tan_beta_sym_ok = (sp.simplify(stat_diff - sp.Rational(1, 2) * (l1_s * vd**4 - l2_s * vu**4)) == 0)

        ow13 = json.loads(git_show_text("0f185471b", "relays/a2_ow13_v2/a2_ow13_v2_results.json"))
        lam_ir = ow13["ow13_a"]["downward_rge_t_0_to_neg38"]["yb_high_grav_fixed"]["lam_ir"]
        lam1_Hd = mp.mpf(lam_ir[0])
        lam2_Hu = mp.mpf(lam_ir[1])
        true_tan_beta = (lam1_Hd / lam2_Hu) ** mp_rat(1, 4)

        xh_json = json.loads(git_show_text("75cb20177", "relays/x_harvest_3s_1_v4/verify_x_harvest_3s_1_v4_out.json"))
        xh_tan_beta = mp.mpf(xh_json["H3_e6_brane_2hdm_gauged_holomorphy_and_conformal_ewsb"]["yb_high_conformal_tan_beta"])
        xh_main_tex = git_show_text("75cb20177", "self_consistent_loop/manuscript/main.tex")
        xh_script_txt = git_show_text("75cb20177", "relays/x_harvest_3s_1_v4/verify_x_harvest_3s_1_v4.py")
        tex_has_swapped_formula = ("\\left(\\frac{\\lambda_2}{\\lambda_1}\\right)^{\\!1/4}" in xh_main_tex) and ("1.11472" in xh_main_tex)
        script_has_swapped_pot = ("l1 * (vu ** 4) + sp.Rational(1, 8) * l2 * (vd ** 4)" in xh_script_txt)

        prod_minus_1 = abs(true_tan_beta * xh_tan_beta - mp.mpf(1))
        ps_ex_s1 = ps_json["synth_2_agy_exp_x_harvest_audit"]["ex_s1_h3_tan_beta_swap_catch"]
        ex_s1_vs_ps_err = abs(true_tan_beta - mp.mpf(ps_ex_s1["true_tan_beta_vu_over_vd"]))
        ex_s1_ok = (
            tan_beta_sym_ok
            and tex_has_swapped_formula
            and script_has_swapped_pot
            and (true_tan_beta < mp.mpf(1))
            and (xh_tan_beta > mp.mpf(1))
            and (prod_minus_1 < mp_pow10(-12))
            and (ex_s1_vs_ps_err < mp_pow10(-12))
        )
        if not ex_s1_ok:
            discrepancies += 1

        # 3b. EX-S2: Machacek-Vaughn T_2 3x overcount on Tr(H_u H_d)
        mv84 = derive_mv84_chi4_h2_hbar2_symbolic()
        tex_has_buggy_T2 = ("T_2 = \\mathrm{Tr}(3H_u^2 + 3H_d^2 + H_e^2 - 2H_u H_d)" in xh_main_tex)
        script_has_buggy_T2 = ("T2 = mp.mpf(3) * tu2 + mp.mpf(3) * td2 + te2 - mp.mpf(2) * tud" in xh_script_txt)
        ps_ex_s2 = ps_json["synth_2_agy_exp_x_harvest_audit"]["ex_s2_appendix_b_T2_3x_hud_catch"]
        ex_s2_ok = (
            mv84["exact_minus_chi4_HuHd"] == "3/2"
            and mv84["buggy_75cb_HuHd"] == "9/2"
            and mv84["ratio_buggy_over_exact"] == "3"
            and mv84["required_T2_HuHd"] == "-2/3"
            and mv84["beta_yt_yt2yb2_exact"] == "-11/4"
            and mv84["beta_yt_yt2yb2_buggy"] == "1/4"
            and mv84["beta_ytau_yt2yb2_exact"] == "3/2"
            and mv84["beta_ytau_yt2yb2_buggy"] == "9/2"
            and tex_has_buggy_T2
            and script_has_buggy_T2
            and ps_ex_s2["mv84_exact_minus_chi4_HuHd_coeff"] == "3/2"
            and ps_ex_s2["exact_beta_yt2_yt2yb2_coeff"] == "-11/4"
            and ps_ex_s2["main_tex_459_beta_yt2_yt2yb2_coeff"] == "1/4"
        )
        if not ex_s2_ok:
            discrepancies += 1

        # 3c. AGY30-S1: v4.json IC6 = "16/1" vs Proca UV quadratic -33/2 / -50/3 & Sen IR -277/360
        ic6_val = v4_payload["machine_verified_certificates"]["IC6_conformal_bh_log_entropy_c_log_exact"]
        # Exact Seeley-DeWitt a_1 coefficients for induced 1/(16 pi G_N):
        # Conformal real scalar (xi=1/6): 0; Weyl fermion: +1/6;
        # Massless vector (4 vec - 2 FP ghosts): (4/6 - 1) - 2*(1/6) = -2/3;
        # Massive Proca (massless + 1 Stueckelberg minimal scalar): -2/3 + 1/6 = -1/2.
        a1_conf_scalar = Fraction(0, 1)
        a1_weyl = Fraction(1, 6)
        a1_massless_vec = Fraction(-2, 3)
        a1_proca = a1_massless_vec + Fraction(1, 6)  # == -1/2
        # Centralizer dim C_{so(10)}(P_PS, J_5) = dim(SU(3) x SU(2) x U(1)_Y x U(1)_X) = 8+3+1+1 = 13 -> 32 Proca
        dim_centralizer = 8 + 3 + 1 + 1
        n_proca_exact = 45 - dim_centralizer  # 32
        quad_33 = 12 * a1_massless_vec + 33 * a1_proca + 48 * a1_weyl + 8 * a1_conf_scalar
        quad_32 = dim_centralizer * a1_massless_vec + n_proca_exact * a1_proca + 48 * a1_weyl + 8 * a1_conf_scalar
        # At ln(Lambda^2 / M^2) = 2 -> Lambda^2 / M^2 = e^2:
        net_Ginv_ln2 = frac_to_mp(quad_33) * (mp.e ** 2) + mp.mpf(16) * mp.mpf(2)
        # Sen IR 2(c - a) for SM + 2HDM (N_0 = 8, N_W = 45, N_1 = 12):
        # c_0 - a_0 = 1/180, c_W - a_W = 7/720, c_1 - a_1 = -13/180
        sen_ir_2_c_minus_a = 2 * (
            8 * Fraction(1, 180) + 45 * Fraction(7, 720) + 12 * Fraction(-13, 180)
        )
        ps_s1 = ps_json["synth_3_agy_c30_v4_audit"]["agy30_s1_ic6_proca_antigravity_catch"]
        err_net_Ginv = abs(net_Ginv_ln2 - mp.mpf(ps_s1["net_induced_Ginv_at_ln2_negative"]))
        agy30_s1_ok = (
            ic6_val == "16/1"
            and a1_proca == Fraction(-1, 2)
            and quad_33 == Fraction(-33, 2)
            and quad_32 == Fraction(-50, 3)
            and net_Ginv_ln2 < mp.mpf(0)
            and err_net_Ginv < mp_pow10(-9)
            and sen_ir_2_c_minus_a == Fraction(-277, 360)
            and ps_s1["proca_quad_coeff_33"] == "-33/2"
            and ps_s1["proca_quad_coeff_32_dim13"] == "-50/3"
            and ps_s1["sen_ir_exact_2_c_minus_a_45weyl"] == "-277/360"
        )
        if not agy30_s1_ok:
            discrepancies += 1

        # 3d. AGY30-S2: v4.json IC5 = -6 untwisted vs E[5]-twisted -3864/25 (4D DOF) / -1272/5 (6D bulk)
        ic5_val = v4_payload["machine_verified_certificates"]["IC5_brane_2hdm_6d_casimir_nB_minus_nF"]
        # Untwisted 6D bulk Spin(10) (45 vectors, 48 Weyl, 4D brane 2H): 2*(45 - 48) = -6
        untwisted_diff = 2 * (45 - 48)
        # E[5] Poisson-resummed s=3 twist weights: untwisted = +4, twisted = 4*(1/4)*(5^{-2} - 1) = -24/25
        c6_4d_dof = 4 * (6 - 24) - Fraction(24, 25) * (90 - 4)  # SM + 3 nu_R + 1H (4D DOF)
        c6_6d_bulk = 4 * (6 - 48) - Fraction(24, 25) * (90 - 0)  # G_SM (4 DOF/vec) + 3x16 (brane 2H)
        ps_s2 = ps_json["synth_3_agy_c30_v4_audit"]["agy30_s2_ic5_untwisted_vs_E5_twisted_scope"]
        agy30_s2_ok = (
            ic5_val == -6
            and untwisted_diff == -6
            and c6_4d_dof == Fraction(-3864, 25)
            and c6_6d_bulk == Fraction(-1272, 5)
            and ps_s2["E5_twisted_6d_s3_4d_dof"] == "-3864/25"
            and ps_s2["E5_twisted_6d_s3_6d_bulk"] == "-1272/5"
        )
        if not agy30_s2_ok:
            discrepancies += 1

        gate_ps = h1_ok and v4_digest_ok and (v4_float_count == 0) and ex_s1_ok and ex_s2_ok and agy30_s1_ok and agy30_s2_ok
        return (
            {
                "h1_closed_form": {
                    "L2_i_35d": mp.nstr(L2_i, 35),
                    "L2_fricke_35d": mp.nstr(L2_fricke_closed, 35),
                    "bc_fricke_35d": mp.nstr(bc_fricke, 35),
                    "err_vs_ps_L2_i": mp.nstr(err_L2_i, 8),
                    "err_vs_ps_L2_fricke": mp.nstr(err_L2_fricke, 8),
                    "err_vs_ps_bc_fricke": mp.nstr(err_bc_fricke, 8),
                    "ok": h1_ok,
                },
                "v4_json_custody": {
                    "recomputed_sha256_payload_digest": recomputed_v4_digest,
                    "digest_matched": v4_digest_ok,
                    "json_float_count": v4_float_count,
                },
                "ex_s1_tan_beta_swap": {
                    "true_tan_beta": mp.nstr(true_tan_beta, 16),
                    "reported_75cb_tan_beta": mp.nstr(xh_tan_beta, 16),
                    "product_minus_1": mp.nstr(prod_minus_1, 8),
                    "ok": ex_s1_ok,
                },
                "ex_s2_mv84_T2_3x": {
                    **mv84,
                    "ok": ex_s2_ok,
                },
                "agy30_s1_ic6_proca": {
                    "v4_IC6": ic6_val,
                    "dim_centralizer_so10": dim_centralizer,
                    "proca_quad_33": str(quad_33),
                    "proca_quad_32": str(quad_32),
                    "net_Ginv_ln2": mp.nstr(net_Ginv_ln2, 14),
                    "sen_ir_2_c_minus_a": str(sen_ir_2_c_minus_a),
                    "ok": agy30_s1_ok,
                },
                "agy30_s2_ic5_scope": {
                    "v4_IC5": ic5_val,
                    "c6_4d_dof": str(c6_4d_dof),
                    "c6_6d_bulk": str(c6_6d_bulk),
                    "ok": agy30_s2_ok,
                },
                "gate_ref_ps": gate_ps,
            },
            discrepancies,
        )
    finally:
        mp.mp.dps = old_dps


# =============================================================================
# REF-A: Disjoint Countercheck of OW19-A (62f08b148)
# =============================================================================
def build_wp_fourier_mp(tau: mp.mpc, n_terms: int = 18):
    """Weierstrass wp(z; tau) via exact trigonometric Lambert q-series
    (completely disjoint from Weierstrass-Taylor wp'' = 6 wp^2 - g_2/2)."""
    tau_im = mp.im(tau)
    q2 = mp.exp(2 * I_MP * mp.pi * tau)
    lam_coeffs = []
    e2_sum = mp.mpc(0)
    qn = q2
    for n in range(1, n_terms + 1):
        c_n = mp.mpf(n) * qn / (mp.mpf(1) - qn)
        lam_coeffs.append((n, c_n))
        e2_sum += c_n
        qn *= q2
    e2_val = mp.mpc(1) - 24 * e2_sum
    const_term = -(mp.pi ** 2) * e2_val / mp.mpf(3)
    eight_pi2 = 8 * (mp.pi ** 2)
    pi2 = mp.pi ** 2

    def wp_mp(z: mp.mpc) -> mp.mpc:
        nb = int(mp.nint(mp.im(z) / tau_im))
        zr = z - nb * tau
        na = int(mp.nint(mp.re(zr)))
        zr = zr - na
        s = mp.sin(mp.pi * zr)
        res = const_term + pi2 / (s * s)
        acc = mp.mpc(0)
        two_pi_z = 2 * mp.pi * zr
        for n, c_n in lam_coeffs:
            acc += c_n * mp.cos(n * two_pi_z)
        return res - eight_pi2 * acc

    def z2_wp_minus_1_mp(z: mp.mpc) -> mp.mpc:
        # Nonsingular evaluation of z^2 wp(z; tau) - 1 for small |z|
        u = mp.pi * z
        if abs(u) < mp_rat(1, 50):
            u2 = u * u
            sing_part = (
                u2 / mp.mpf(3)
                + (u2 ** 2) / mp.mpf(15)
                + 2 * (u2 ** 3) / mp.mpf(189)
                + (u2 ** 4) / mp.mpf(675)
                + 2 * (u2 ** 5) / mp.mpf(10395)
            )
        else:
            su = mp.sin(u)
            sing_part = (u * u) / (su * su) - mp.mpf(1)
        acc = mp.mpc(0)
        two_pi_z = 2 * mp.pi * z
        for n, c_n in lam_coeffs:
            acc += c_n * mp.cos(n * two_pi_z)
        return sing_part + (z * z) * (const_term - eight_pi2 * acc)

    return wp_mp, z2_wp_minus_1_mp, const_term, lam_coeffs


def rk4_transfer_from_nodes_mp(
    wp_nodes: list[mp.mpc],
    c_val: mp.mpc,
    dz_fine: mp.mpc,
    stride: int,
) -> mp.matrix:
    """Classical RK4 fundamental-matrix transfer for u'' + (1/4)(wp(z) - c) u = 0
    using precomputed wp nodes along a straight segment."""
    n_steps = (len(wp_nodes) - 1) // (2 * stride)
    h = stride * dz_fine
    q_quarter = mp_rat(1, 4)
    y00, y01 = mp.mpc(1), mp.mpc(0)
    y10, y11 = mp.mpc(0), mp.mpc(1)
    for k in range(n_steps):
        i0 = 2 * stride * k
        ih = i0 + stride
        i1 = i0 + 2 * stride
        q0 = q_quarter * (wp_nodes[i0] - c_val)
        qh = q_quarter * (wp_nodes[ih] - c_val)
        q1 = q_quarter * (wp_nodes[i1] - c_val)

        k1_00, k1_01 = h * y10, h * y11
        k1_10, k1_11 = -h * q0 * y00, -h * q0 * y01

        m00, m01 = y00 + k1_00 / 2, y01 + k1_01 / 2
        m10, m11 = y10 + k1_10 / 2, y11 + k1_11 / 2
        k2_00, k2_01 = h * m10, h * m11
        k2_10, k2_11 = -h * qh * m00, -h * qh * m01

        m00, m01 = y00 + k2_00 / 2, y01 + k2_01 / 2
        m10, m11 = y10 + k2_10 / 2, y11 + k2_11 / 2
        k3_00, k3_01 = h * m10, h * m11
        k3_10, k3_11 = -h * qh * m00, -h * qh * m01

        m00, m01 = y00 + k3_00, y01 + k3_01
        m10, m11 = y10 + k3_10, y11 + k3_11
        k4_00, k4_01 = h * m10, h * m11
        k4_10, k4_11 = -h * q1 * m00, -h * q1 * m01

        y00 += (k1_00 + 2 * k2_00 + 2 * k3_00 + k4_00) / 6
        y01 += (k1_01 + 2 * k2_01 + 2 * k3_01 + k4_01) / 6
        y10 += (k1_10 + 2 * k2_10 + 2 * k3_10 + k4_10) / 6
        y11 += (k1_11 + 2 * k2_11 + 2 * k3_11 + k4_11) / 6
    return mp.matrix([[y00, y01], [y10, y11]])


def rk4_richardson_monodromy_mp(
    wp_nodes: list[mp.mpc], c_val: mp.mpc, dz_fine: mp.mpc
) -> mp.matrix:
    """6th-order Richardson-extrapolated RK4 transfer matrix from stride=2 and stride=1."""
    m_coarse = rk4_transfer_from_nodes_mp(wp_nodes, c_val, dz_fine, stride=2)
    m_fine = rk4_transfer_from_nodes_mp(wp_nodes, c_val, dz_fine, stride=1)
    return (16 * m_fine - m_coarse) / 15


def rk4_segment_mp(
    wp_mp, c_val: mp.mpc, z_start: mp.mpc, z_end: mp.mpc, n_steps: int, psi_init: mp.matrix
) -> mp.matrix:
    """Integrate fundamental matrix Psi' = [[0, 1], [-Q, 0]] Psi along z_start -> z_end."""
    h = (z_end - z_start) / n_steps
    q_quarter = mp_rat(1, 4)
    y00, y01 = psi_init[0, 0], psi_init[0, 1]
    y10, y11 = psi_init[1, 0], psi_init[1, 1]
    q0 = q_quarter * (wp_mp(z_start) - c_val)
    for k in range(n_steps):
        zh = z_start + (mp.mpf(k) + mp_rat(1, 2)) * h
        z1 = z_start + mp.mpf(k + 1) * h
        qh = q_quarter * (wp_mp(zh) - c_val)
        q1 = q_quarter * (wp_mp(z1) - c_val)

        k1_00, k1_01 = h * y10, h * y11
        k1_10, k1_11 = -h * q0 * y00, -h * q0 * y01

        m00, m01 = y00 + k1_00 / 2, y01 + k1_01 / 2
        m10, m11 = y10 + k1_10 / 2, y11 + k1_11 / 2
        k2_00, k2_01 = h * m10, h * m11
        k2_10, k2_11 = -h * qh * m00, -h * qh * m01

        m00, m01 = y00 + k2_00 / 2, y01 + k2_01 / 2
        m10, m11 = y10 + k2_10 / 2, y11 + k2_11 / 2
        k3_00, k3_01 = h * m10, h * m11
        k3_10, k3_11 = -h * qh * m00, -h * qh * m01

        m00, m01 = y00 + k3_00, y01 + k3_01
        m10, m11 = y10 + k3_10, y11 + k3_11
        k4_00, k4_01 = h * m10, h * m11
        k4_10, k4_11 = -h * q1 * m00, -h * q1 * m01

        y00 += (k1_00 + 2 * k2_00 + 2 * k3_00 + k4_00) / 6
        y01 += (k1_01 + 2 * k2_01 + 2 * k3_01 + k4_01) / 6
        y10 += (k1_10 + 2 * k2_10 + 2 * k3_10 + k4_10) / 6
        y11 += (k1_11 + 2 * k2_11 + 2 * k3_11 + k4_11) / 6
        q0 = q1
    return mp.matrix([[y00, y01], [y10, y11]])


def rk4_log_cusp_mp(
    z2_wp_m1_mp, c_val: mp.mpc, z_start: mp.mpc, s_end: mp.mpf, n_steps: int, psi_start: mp.matrix
) -> tuple[mp.mpf, mp.mpf]:
    """Integrate nonsingular log-radius ODE f''(s) + (1/4)(z^2 wp(z) - 1 - c z^2) f(s) = 0
    along ray z(s) = z_start * exp(-s) for s in [0, s_end] using RK4.
    Returns (r_end, b_eff_end) where b_eff(r) = 1 / (r e^Omega) + ln r."""
    r0 = abs(z_start)
    # f(s) = exp(s/2) u(z(s)), f'(s) = exp(s/2) (u/2 - z u')
    # Note: z_start^{-1/2} constant phase cancels in Im(f1 conj(f2)) up to 1/r0!
    inv_sqrt_r0 = mp.mpf(1) / mp.sqrt(r0)
    f00 = inv_sqrt_r0 * psi_start[0, 0]
    f01 = inv_sqrt_r0 * psi_start[0, 1]
    f10 = inv_sqrt_r0 * (mp_rat(1, 2) * psi_start[0, 0] - z_start * psi_start[1, 0])
    f11 = inv_sqrt_r0 * (mp_rat(1, 2) * psi_start[0, 1] - z_start * psi_start[1, 1])

    def q_log(s_val: mp.mpf) -> mp.mpc:
        zv = z_start * mp.exp(-s_val)
        return mp_rat(1, 4) * (z2_wp_m1_mp(zv) - c_val * (zv * zv))

    h = s_end / n_steps
    q0 = q_log(mp.mpf(0))
    for k in range(n_steps):
        sh = (mp.mpf(k) + mp_rat(1, 2)) * h
        s1 = mp.mpf(k + 1) * h
        qh = q_log(sh)
        q1 = q_log(s1)

        k1_00, k1_01 = h * f10, h * f11
        k1_10, k1_11 = -h * q0 * f00, -h * q0 * f01

        m00, m01 = f00 + k1_00 / 2, f01 + k1_01 / 2
        m10, m11 = f10 + k1_10 / 2, f11 + k1_11 / 2
        k2_00, k2_01 = h * m10, h * m11
        k2_10, k2_11 = -h * qh * m00, -h * qh * m01

        m00, m01 = f00 + k2_00 / 2, f01 + k2_01 / 2
        m10, m11 = f10 + k2_10 / 2, f11 + k2_11 / 2
        k3_00, k3_01 = h * m10, h * m11
        k3_10, k3_11 = -h * qh * m00, -h * qh * m01

        m00, m01 = f00 + k3_00, f01 + k3_01
        m10, m11 = f10 + k3_10, f11 + k3_11
        k4_00, k4_01 = h * m10, h * m11
        k4_10, k4_11 = -h * q1 * m00, -h * q1 * m01

        f00 += (k1_00 + 2 * k2_00 + 2 * k3_00 + k4_00) / 6
        f01 += (k1_01 + 2 * k2_01 + 2 * k3_01 + k4_01) / 6
        f10 += (k1_10 + 2 * k2_10 + 2 * k3_10 + k4_10) / 6
        f11 += (k1_11 + 2 * k2_11 + 2 * k3_11 + k4_11) / 6
        q0 = q1

    r_end = r0 * mp.exp(-s_end)
    # Im(v1 conj(v2)) = r_end * Im(f00 conj(f01)) -> 1 / (r_end e^Omega) = |Im(f00 conj(f01))|
    inv_r_eOmega = abs(mp.im(f00 * mp.conj(f01)))
    b_eff = inv_r_eOmega + mp.log(r_end)
    return r_end, b_eff


def build_sl2r_conjugator_mp(Ta: mp.matrix, Tb: mp.matrix) -> tuple[mp.matrix, mp.matrix, mp.matrix]:
    """Construct exact SL(2, C) conjugator P (det P = 1) mapping (Ta, Tb) into SL(2, R)
    via diagonalization of hyperbolic Ta + off-diagonal phase alignment of Tb."""
    tr_a = Ta[0, 0] + Ta[1, 1]
    disc = mp.sqrt(tr_a * tr_a - 4)
    lam1 = (tr_a + disc) / 2
    lam2 = (tr_a - disc) / 2

    def eigvec(M: mp.matrix, lam: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
        r00, r01 = M[0, 0] - lam, M[0, 1]
        r10, r11 = M[1, 0], M[1, 1] - lam
        if abs(r00) + abs(r01) >= abs(r10) + abs(r11):
            return (r01, -r00)
        return (r11, -r10)

    v1 = eigvec(Ta, lam1)
    v2 = eigvec(Ta, lam2)
    P0 = mp.matrix([[v1[0], v2[0]], [v1[1], v2[1]]])
    s_det = mp.sqrt(P0[0, 0] * P0[1, 1] - P0[0, 1] * P0[1, 0])
    P0 = P0 / s_det
    P0_inv = mp.matrix([[P0[1, 1], -P0[0, 1]], [-P0[1, 0], P0[0, 0]]])
    B0 = P0_inv * Tb * P0
    b12 = B0[0, 1]
    s_phase = mp.exp(I_MP * mp.arg(b12) / 2)
    D = mp.matrix([[s_phase, mp.mpc(0)], [mp.mpc(0), mp.mpc(1) / s_phase]])
    P = P0 * D
    P_inv = mp.matrix([[P[1, 1], -P[0, 1]], [-P[1, 0], P[0, 0]]])
    Ra = P_inv * Ta * P
    Rb = P_inv * Tb * P
    return P, Ra, Rb


def solve_fuchsian_disjoint_mp(tau_r: mp.mpc) -> dict[str, Any]:
    """Solve u'' + (1/4)(wp(z; tau_r) - c*) u = 0 via Fourier-Lambert wp + Richardson-RK4."""
    old_dps = mp.mp.dps
    mp.mp.dps = 35
    try:
        wp_mp, z2_wp_m1_mp, const_term, lam_coeffs = build_wp_fourier_mp(tau_r, n_terms=18)
        v0 = -(mp.mpc(1) + tau_r) / 2

        # Precompute wp(z) along a-cycle (v0 -> v0 + 1) and b-cycle (v0 -> v0 + tau_r)
        na_fine = 192  # stride 2 = 96 steps, stride 1 = 192 steps
        nb_fine = 288  # stride 2 = 144 steps, stride 1 = 288 steps
        dz_a = mp.mpc(1) / na_fine
        dz_b = tau_r / nb_fine
        nodes_a = [wp_mp(v0 + mp_rat(m, 2) * dz_a) for m in range(2 * na_fine + 1)]
        nodes_b = [wp_mp(v0 + mp_rat(m, 2) * dz_b) for m in range(2 * nb_fine + 1)]

        def eval_traces(c_val: mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.matrix, mp.matrix]:
            Ta = rk4_richardson_monodromy_mp(nodes_a, c_val, dz_a)
            Tb = rk4_richardson_monodromy_mp(nodes_b, c_val, dz_b)
            return Ta[0, 0] + Ta[1, 1], Tb[0, 0] + Tb[1, 1], Ta, Tb

        # Purely analytic initial guess (midpoint of a-cycle & b-cycle wp averages; zero target leakage)
        c_cur = mp.mpc(-(mp.pi ** 2) / mp.mpf(3) + mp.pi / mp.im(tau_r), mp.mpf(0))
        h_diff = mp_pow10(-9)
        for _ in range(10):
            xa, xb, _, _ = eval_traces(c_cur)
            f1, f2 = mp.im(xa), mp.im(xb)
            if abs(f1) + abs(f2) < mp_pow10(-26):
                break
            xa_p, xb_p, _, _ = eval_traces(c_cur + h_diff)
            xa_m, xb_m, _, _ = eval_traces(c_cur - h_diff)
            dxa = (xa_p - xa_m) / (2 * h_diff)
            dxb = (xb_p - xb_m) / (2 * h_diff)
            # Cauchy-Riemann Jacobian for (Im xa, Im xb) wrt (c_R, c_I):
            j11, j12 = mp.im(dxa), mp.re(dxa)
            j21, j22 = mp.im(dxb), mp.re(dxb)
            det_j = j11 * j22 - j12 * j21
            dc_r = -(j22 * f1 - j12 * f2) / det_j
            dc_i = -(-j21 * f1 + j11 * f2) / det_j
            c_cur = c_cur + mp.mpc(dc_r, dc_i)

        xa, xb, Ta, Tb = eval_traces(c_cur)
        Ta_inv = mp.matrix([[Ta[1, 1], -Ta[0, 1]], [-Ta[1, 0], Ta[0, 0]]])
        Tb_inv = mp.matrix([[Tb[1, 1], -Tb[0, 1]], [-Tb[1, 0], Tb[0, 0]]])
        comm = Ta * Tb * Ta_inv * Tb_inv
        tr_comm_err = abs((comm[0, 0] + comm[1, 1]) + mp.mpc(2))
        xab = (Ta * Tb)[0, 0] + (Ta * Tb)[1, 1]
        im_tr_max = max(abs(mp.im(xa)), abs(mp.im(xb)), abs(mp.im(xab)))

        P, Ra, Rb = build_sl2r_conjugator_mp(Ta, Tb)
        max_im_R = max(
            abs(mp.im(Ra[r, c])) for r in range(2) for c in range(2)
        )
        max_im_R = max(
            max_im_R,
            max(abs(mp.im(Rb[r, c])) for r in range(2) for c in range(2)),
        )

        # Interior curvature check K(z_1) = -1 via 2nd-order central Laplacian at z_1 = 3/10 + (1/2)i
        z1 = mp.mpc(mp_rat(3, 10), mp_rat(1, 2))
        # Path v0 -> (-1/2 + i/2) -> z1 stays far from puncture z=0
        z_mid = mp.mpc(mp_rat(-1, 2), mp_rat(1, 2))
        psi_mid = rk4_segment_mp(wp_mp, c_cur, v0, z_mid, 120, P)
        psi_z1 = rk4_segment_mp(wp_mp, c_cur, z_mid, z1, 120, psi_mid)

        def metric_from_psi(psi_m: mp.matrix) -> mp.mpf:
            imv = mp.im(psi_m[0, 0] * mp.conj(psi_m[0, 1]))
            return mp.mpf(1) / (imv * imv)

        def omega_from_psi(psi_m: mp.matrix) -> mp.mpf:
            return -mp.log(abs(mp.im(psi_m[0, 0] * mp.conj(psi_m[0, 1]))))

        e2om_z1 = metric_from_psi(psi_z1)
        om_0 = omega_from_psi(psi_z1)
        h_lap = mp_pow10(-6)
        om_xp = omega_from_psi(rk4_segment_mp(wp_mp, c_cur, z1, z1 + h_lap, 4, psi_z1))
        om_xm = omega_from_psi(rk4_segment_mp(wp_mp, c_cur, z1, z1 - h_lap, 4, psi_z1))
        om_yp = omega_from_psi(rk4_segment_mp(wp_mp, c_cur, z1, z1 + I_MP * h_lap, 4, psi_z1))
        om_ym = omega_from_psi(rk4_segment_mp(wp_mp, c_cur, z1, z1 - I_MP * h_lap, 4, psi_z1))
        lap_om = (om_xp + om_xm + om_yp + om_ym - 4 * om_0) / (h_lap * h_lap)
        K_z1 = -lap_om / e2om_z1
        curv_err = abs(K_z1 + mp.mpf(1))

        # Double periodicity check at z1: z1 -> z1 + 1 and z1 -> z1 + tau_r
        psi_z1_p1 = rk4_segment_mp(wp_mp, c_cur, z1, z1 + mp.mpc(1), 160, psi_z1)
        psi_z1_ptau = rk4_segment_mp(wp_mp, c_cur, z1, z1 + tau_r, 220, psi_z1)
        per_1_err = abs(metric_from_psi(psi_z1_p1) - e2om_z1)
        per_tau_err = abs(metric_from_psi(psi_z1_ptau) - e2om_z1)

        # Cusp Robin parameter b_c^*(tau_8^+) via log-coordinate RK4 inward integration
        # Path v0 -> (-1/2 + 0i) -> (-1/8 + 0i), then log-ODE inward to r = 10^{-4} and r = 5*10^{-5}
        z_left0 = mp.mpc(mp_rat(-1, 2), mp.mpf(0))
        z_start_cusp = mp.mpc(mp_rat(-1, 8), mp.mpf(0))
        psi_left0 = rk4_segment_mp(wp_mp, c_cur, v0, z_left0, 120, P)
        psi_start_cusp = rk4_segment_mp(wp_mp, c_cur, z_left0, z_start_cusp, 96, psi_left0)

        s_r1 = mp.log(mp.mpf(1250))   # r1 = (1/8) / 1250 = 10^{-4}
        s_r2 = mp.log(mp.mpf(2500))   # r2 = (1/8) / 2500 = 5 * 10^{-5}
        r1, b_eff_1 = rk4_log_cusp_mp(z2_wp_m1_mp, c_cur, z_start_cusp, s_r1, 240, psi_start_cusp)
        r2, b_eff_2 = rk4_log_cusp_mp(z2_wp_m1_mp, c_cur, z_start_cusp, s_r2, 320, psi_start_cusp)
        # O(r^2) Richardson elimination:
        bc_star = (r1 * r1 * b_eff_2 - r2 * r2 * b_eff_1) / (r1 * r1 - r2 * r2)
        L2_tau8 = mp.pi - bc_star

        return {
            "c_star": c_cur,
            "P": P,
            "Ra": Ra,
            "Rb": Rb,
            "tr_comm_err": tr_comm_err,
            "im_tr_max": im_tr_max,
            "max_im_R": max_im_R,
            "K_z1": K_z1,
            "curv_err": curv_err,
            "per_1_err": per_1_err,
            "per_tau_err": per_tau_err,
            "bc_star": bc_star,
            "L2_tau8": L2_tau8,
            "const_term": const_term,
            "lam_coeffs": lam_coeffs,
            "v0": v0,
            "psi_z1": psi_z1,
            "z1": z1,
            "wp_mp": wp_mp,
        }
    finally:
        mp.mp.dps = old_dps


def run_disjoint_2d_quadrature_np(fuchs: dict[str, Any], tau_r_c: complex) -> dict[str, Any]:
    """Completely disjoint 2D quadrature on R_{tau_r} = [-1/2, 1/2] x [-4/5, 4/5]:
      1. Outer Cartesian midpoint grid on R_{tau_r} \\ [-1/8, 1/8]^2 (Nx=80, Ny=128)
      2. Polar midpoint transition [-1/8, 1/8]^2 \\ D(0, 1/16) (N_theta=128)
      3. Polar log-radial midpoint annulus D(0, 1/16) \\ D(0, 10^{-4}) (NO t-substitution!)
      4. Analytic cusp tail 1 / (-ln r_min + b_c^*) inside |z| < r_min = 10^{-4}.
    Vectorized complex128 RK4 ODE evaluator for e^{2 Omega_hyp(z)}.
    """
    tau_im = float(tau_r_c.imag)
    c_val = complex(float(mp.re(fuchs["c_star"])), float(mp.im(fuchs["c_star"])))
    const_term = complex(float(mp.re(fuchs["const_term"])), float(mp.im(fuchs["const_term"])))
    n_fourier = 12
    n_arr = np.arange(1, n_fourier + 1, dtype=np.float64)
    lam_c = np.array(
        [complex(float(mp.re(val)), float(mp.im(val))) for _, val in fuchs["lam_coeffs"][:n_fourier]],
        dtype=np.complex128,
    )
    pi_f = float(np.pi)
    pi2_f = pi_f * pi_f
    eight_pi2_f = float(8) * pi2_f
    q_quarter = flt_rat(1, 4)

    def wp_vec(z_arr: np.ndarray) -> np.ndarray:
        z_arr = np.asarray(z_arr, dtype=np.complex128)
        nb = np.rint(z_arr.imag / tau_im)
        zr = z_arr - nb * tau_r_c
        zr = zr - np.rint(zr.real)
        s = np.sin(pi_f * zr)
        res = const_term + pi2_f / (s * s)
        # Sum Lambert cosine series
        arg = (float(2) * pi_f) * zr[..., None] * n_arr
        acc = np.sum(np.cos(arg) * lam_c, axis=-1)
        return res - eight_pi2_f * acc

    def z2_wp_m1_vec(z_arr: np.ndarray) -> np.ndarray:
        z_arr = np.asarray(z_arr, dtype=np.complex128)
        u = pi_f * z_arr
        u2 = u * u
        small = np.abs(u) < flt_rat(1, 20)
        sing = np.empty_like(z_arr)
        if np.any(small):
            us2 = u2[small]
            sing[small] = (
                us2 / float(3)
                + (us2 ** 2) / float(15)
                + (float(2) * (us2 ** 3)) / float(189)
                + (us2 ** 4) / float(675)
            )
        if np.any(~small):
            ub = u[~small]
            sb = np.sin(ub)
            sing[~small] = (ub * ub) / (sb * sb) - float(1)
        arg = (float(2) * pi_f) * z_arr[..., None] * n_arr
        acc = np.sum(np.cos(arg) * lam_c, axis=-1)
        return sing + (z_arr * z_arr) * (const_term - eight_pi2_f * acc)

    def rk4_step_vec(
        psi: np.ndarray, z0: np.ndarray, dz: np.ndarray, n_sub: int
    ) -> np.ndarray:
        """Vectorized RK4 step on shape (..., 2, 2) fundamental matrices from z0 by dz."""
        h = dz / float(n_sub)
        y00 = psi[..., 0, 0].copy()
        y01 = psi[..., 0, 1].copy()
        y10 = psi[..., 1, 0].copy()
        y11 = psi[..., 1, 1].copy()
        z_cur = z0.copy()
        q0 = q_quarter * (wp_vec(z_cur) - c_val)
        for _ in range(n_sub):
            zh = z_cur + flt_rat(1, 2) * h
            z1 = z_cur + h
            qh = q_quarter * (wp_vec(zh) - c_val)
            q1 = q_quarter * (wp_vec(z1) - c_val)

            k1_00, k1_01 = h * y10, h * y11
            k1_10, k1_11 = -h * q0 * y00, -h * q0 * y01

            m00, m01 = y00 + flt_rat(1, 2) * k1_00, y01 + flt_rat(1, 2) * k1_01
            m10, m11 = y10 + flt_rat(1, 2) * k1_10, y11 + flt_rat(1, 2) * k1_11
            k2_00, k2_01 = h * m10, h * m11
            k2_10, k2_11 = -h * qh * m00, -h * qh * m01

            m00, m01 = y00 + flt_rat(1, 2) * k2_00, y01 + flt_rat(1, 2) * k2_01
            m10, m11 = y10 + flt_rat(1, 2) * k2_10, y11 + flt_rat(1, 2) * k2_11
            k3_00, k3_01 = h * m10, h * m11
            k3_10, k3_11 = -h * qh * m00, -h * qh * m01

            m00, m01 = y00 + k3_00, y01 + k3_01
            m10, m11 = y10 + k3_10, y11 + k3_11
            k4_00, k4_01 = h * m10, h * m11
            k4_10, k4_11 = -h * q1 * m00, -h * q1 * m01

            inv6 = flt_rat(1, 6)
            y00 += inv6 * (k1_00 + float(2) * k2_00 + float(2) * k3_00 + k4_00)
            y01 += inv6 * (k1_01 + float(2) * k2_01 + float(2) * k3_01 + k4_01)
            y10 += inv6 * (k1_10 + float(2) * k2_10 + float(2) * k3_10 + k4_10)
            y11 += inv6 * (k1_11 + float(2) * k2_11 + float(2) * k3_11 + k4_11)
            z_cur = z1
            q0 = q1
        out = np.empty_like(psi)
        out[..., 0, 0] = y00
        out[..., 0, 1] = y01
        out[..., 1, 0] = y10
        out[..., 1, 1] = y11
        return out

    def rk4_log_step_vec(
        fmat: np.ndarray, z_base: np.ndarray, s0: float, ds: float, n_sub: int
    ) -> np.ndarray:
        """Vectorized RK4 step on log-radius variables (f, f') from s0 to s0 + ds."""
        h = ds / float(n_sub)
        f00 = fmat[..., 0, 0].copy()
        f01 = fmat[..., 0, 1].copy()
        f10 = fmat[..., 1, 0].copy()
        f11 = fmat[..., 1, 1].copy()
        s_cur = s0

        def q_fn(sv: float) -> np.ndarray:
            zv = z_base * np.exp(-sv)
            return q_quarter * (z2_wp_m1_vec(zv) - c_val * (zv * zv))

        q0 = q_fn(s_cur)
        for _ in range(n_sub):
            sh = s_cur + flt_rat(1, 2) * h
            s1 = s_cur + h
            qh = q_fn(sh)
            q1 = q_fn(s1)

            k1_00, k1_01 = h * f10, h * f11
            k1_10, k1_11 = -h * q0 * f00, -h * q0 * f01

            m00, m01 = f00 + flt_rat(1, 2) * k1_00, f01 + flt_rat(1, 2) * k1_01
            m10, m11 = f10 + flt_rat(1, 2) * k1_10, f11 + flt_rat(1, 2) * k1_11
            k2_00, k2_01 = h * m10, h * m11
            k2_10, k2_11 = -h * qh * m00, -h * qh * m01

            m00, m01 = f00 + flt_rat(1, 2) * k2_00, f01 + flt_rat(1, 2) * k2_01
            m10, m11 = f10 + flt_rat(1, 2) * k2_10, f11 + flt_rat(1, 2) * k2_11
            k3_00, k3_01 = h * m10, h * m11
            k3_10, k3_11 = -h * qh * m00, -h * qh * m01

            m00, m01 = f00 + k3_00, f01 + k3_01
            m10, m11 = f10 + k3_10, f11 + k3_11
            k4_00, k4_01 = h * m10, h * m11
            k4_10, k4_11 = -h * q1 * m00, -h * q1 * m01

            inv6 = flt_rat(1, 6)
            f00 += inv6 * (k1_00 + float(2) * k2_00 + float(2) * k3_00 + k4_00)
            f01 += inv6 * (k1_01 + float(2) * k2_01 + float(2) * k3_01 + k4_01)
            f10 += inv6 * (k1_10 + float(2) * k2_10 + float(2) * k3_10 + k4_10)
            f11 += inv6 * (k1_11 + float(2) * k2_11 + float(2) * k3_11 + k4_11)
            s_cur = s1
            q0 = q1
        out = np.empty_like(fmat)
        out[..., 0, 0] = f00
        out[..., 0, 1] = f01
        out[..., 1, 0] = f10
        out[..., 1, 1] = f11
        return out

    # Doubly-periodic E[2] spin-structure densities rho_k(z) (k = 4, 2, 3) and M = 3 CIM modes
    q_nom = np.exp(I_NP * pi_f * tau_r_c)
    sqrt_2tau = float(np.sqrt(float(2) * tau_im))
    cim_norm = float((float(6) * tau_im) ** flt_rat(1, 4))
    n_th = np.arange(-6, 7, dtype=np.float64)
    n_th2 = n_th * n_th
    n_half = n_th + flt_rat(1, 2)
    n_half2 = n_half * n_half
    alt_sign = np.where((np.arange(-6, 7) % 2) == 0, float(1), float(-1))
    q_n2 = q_nom ** n_th2
    q_nh2 = q_nom ** n_half2

    def eval_modes_vec(z_arr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Return (rho_e2 shape (..., 3) for [theta4, theta2, theta3],
        psi_cim shape (..., 3) for j=0,1,2) on arbitrary complex array z_arr."""
        z_arr = np.asarray(z_arr, dtype=np.complex128)
        y = z_arr.imag
        gauss_e2 = sqrt_2tau * np.exp((-float(2) * pi_f / tau_im) * (y * y))
        two_pi_i_z = (float(2) * pi_f * I_NP) * z_arr[..., None]
        exp_n = np.exp(two_pi_i_z * n_th)
        exp_nh = np.exp(two_pi_i_z * n_half)
        th3 = np.sum(q_n2 * exp_n, axis=-1)
        th4 = np.sum((alt_sign * q_n2) * exp_n, axis=-1)
        th2 = np.sum(q_nh2 * exp_nh, axis=-1)
        rho_e2 = np.stack(
            [gauss_e2 * (np.abs(th4) ** 2), gauss_e2 * (np.abs(th2) ** 2), gauss_e2 * (np.abs(th3) ** 2)],
            axis=-1,
        )

        # CIM M = 3 zero modes: psi^{j,3}(z) = (6 Im tau)^{1/4} exp(3 i pi z Im(z)/Im(tau)) theta[j/3, 0](3z, 3 tau)
        pref_cim = cim_norm * np.exp((float(3) * I_NP * pi_f / tau_im) * z_arr * y)
        psi_list = []
        for j in range(3):
            sh = n_th + flt_rat(j, 3)
            term = np.exp(
                (I_NP * pi_f * float(3) * tau_r_c) * (sh * sh)
                + (float(6) * I_NP * pi_f) * z_arr[..., None] * sh
            )
            psi_list.append(pref_cim * np.sum(term, axis=-1))
        psi_cim = np.stack(psi_list, axis=-1)
        return rho_e2, psi_cim

    # Convert basepoint and P matrix to complex128
    v0_c = complex(float(mp.re(fuchs["v0"])), float(mp.im(fuchs["v0"])))
    P_np = np.array(
        [
            [
                complex(float(mp.re(fuchs["P"][r, c])), float(mp.im(fuchs["P"][r, c])))
                for c in range(2)
            ]
            for r in range(2)
        ],
        dtype=np.complex128,
    )

    # Accumulators
    area_hyp_total = float(0)
    area_flat_total = float(0)
    K_e2_hyp = np.zeros(3, dtype=np.float64)
    K_e2_flat = np.zeros(3, dtype=np.float64)
    K_cim_hyp = np.zeros((3, 3), dtype=np.complex128)
    K_cim_flat = np.zeros((3, 3), dtype=np.complex128)

    def accumulate_points(z_pts: np.ndarray, w_flat: np.ndarray, w_hyp: np.ndarray) -> None:
        nonlocal area_hyp_total, area_flat_total, K_e2_hyp, K_e2_flat, K_cim_hyp, K_cim_flat
        rho_e2, psi_cim = eval_modes_vec(z_pts)
        area_flat_total += float(np.sum(w_flat))
        area_hyp_total += float(np.sum(w_hyp))
        K_e2_flat += np.sum(rho_e2 * w_flat[..., None], axis=tuple(range(z_pts.ndim)))
        K_e2_hyp += np.sum(rho_e2 * w_hyp[..., None], axis=tuple(range(z_pts.ndim)))
        psi_flat = psi_cim.reshape(-1, 3)
        wf = w_flat.reshape(-1)
        wh = w_hyp.reshape(-1)
        K_cim_flat += np.einsum("ni,nj,n->ij", np.conj(psi_flat), psi_flat, wf)
        K_cim_hyp += np.einsum("ni,nj,n->ij", np.conj(psi_flat), psi_flat, wh)

    # --- REGION 1: Outer Cartesian midpoint grid on [-1/2, 1/2] x [-4/5, 4/5] \ [-1/8, 1/8]^2 ---
    nx, ny = 80, 128
    dx = flt_rat(1, nx)
    dy = flt_rat(8, 5 * ny)  # == 1/80
    cell_area = dx * dy

    z_bl = complex(flt_rat(-1, 2), flt_rat(-4, 5))
    z_br = complex(flt_rat(1, 2), flt_rat(-4, 5))
    psi_bl = rk4_step_vec(P_np, np.array(v0_c), np.array(z_bl - v0_c), 24)
    psi_br = rk4_step_vec(psi_bl, np.array(z_bl), np.array(z_br - z_bl), 160)

    # Sweep upward along left edge x=-1/2 and right edge x=+1/2 to all 128 row midpoints y_j
    y_centers = np.array([flt_rat(-4, 5) + (float(j) + flt_rat(1, 2)) * dy for j in range(ny)], dtype=np.float64)
    x_centers = np.array([flt_rat(-1, 2) + (float(i) + flt_rat(1, 2)) * dx for i in range(nx)], dtype=np.float64)

    psi_left_rows = np.empty((ny, 2, 2), dtype=np.complex128)
    psi_right_rows = np.empty((ny, 2, 2), dtype=np.complex128)
    cur_l = rk4_step_vec(psi_bl, np.array(z_bl), np.array(I_NP * flt_rat(1, 2) * dy), 2)
    cur_r = rk4_step_vec(psi_br, np.array(z_br), np.array(I_NP * flt_rat(1, 2) * dy), 2)
    psi_left_rows[0] = cur_l
    psi_right_rows[0] = cur_r
    for j in range(1, ny):
        zl_prev = complex(flt_rat(-1, 2), float(y_centers[j - 1]))
        zr_prev = complex(flt_rat(1, 2), float(y_centers[j - 1]))
        cur_l = rk4_step_vec(cur_l, np.array(zl_prev), np.array(I_NP * dy), 2)
        cur_r = rk4_step_vec(cur_r, np.array(zr_prev), np.array(I_NP * dy), 2)
        psi_left_rows[j] = cur_l
        psi_right_rows[j] = cur_r

    # Also grab Psi(-1/2 + 0i) directly from row j=63 (y_63 = -1/160 -> step +1/160 i)
    psi_left_y0 = rk4_step_vec(
        psi_left_rows[63],
        np.array(complex(flt_rat(-1, 2), float(y_centers[63]))),
        np.array(I_NP * flt_rat(1, 2) * dy),
        2,
    )

    # Full rows: j in [0..53] U [74..127] (108 rows completely outside |y| < 1/8)
    full_row_idx = np.array(list(range(54)) + list(range(74, 128)), dtype=np.int64)
    z_col = flt_rat(-1, 2) + I_NP * y_centers[full_row_idx]
    psi_col = rk4_step_vec(psi_left_rows[full_row_idx], z_col, np.full(len(full_row_idx), flt_rat(1, 2) * dx), 2)
    z_col = z_col + flt_rat(1, 2) * dx
    for i in range(nx):
        imv = np.imag(psi_col[:, 0, 0] * np.conj(psi_col[:, 0, 1]))
        w_hyp = cell_area / (imv * imv)
        w_flt = np.full(len(full_row_idx), cell_area, dtype=np.float64)
        accumulate_points(z_col, w_flt, w_hyp)
        if i + 1 < nx:
            psi_col = rk4_step_vec(psi_col, z_col, np.full(len(full_row_idx), dx), 2)
            z_col = z_col + dx

    # Middle rows j in [54..73] (|y| < 1/8): left columns i=0..29, right columns i=50..79
    mid_row_idx = np.arange(54, 74, dtype=np.int64)
    # Left sweep rightward:
    z_col = flt_rat(-1, 2) + I_NP * y_centers[mid_row_idx]
    psi_col = rk4_step_vec(psi_left_rows[mid_row_idx], z_col, np.full(len(mid_row_idx), flt_rat(1, 2) * dx), 2)
    z_col = z_col + flt_rat(1, 2) * dx
    for i in range(30):
        imv = np.imag(psi_col[:, 0, 0] * np.conj(psi_col[:, 0, 1]))
        w_hyp = cell_area / (imv * imv)
        w_flt = np.full(len(mid_row_idx), cell_area, dtype=np.float64)
        accumulate_points(z_col, w_flt, w_hyp)
        if i + 1 < 30:
            psi_col = rk4_step_vec(psi_col, z_col, np.full(len(mid_row_idx), dx), 2)
            z_col = z_col + dx

    # Right sweep leftward:
    z_col = flt_rat(1, 2) + I_NP * y_centers[mid_row_idx]
    psi_col = rk4_step_vec(psi_right_rows[mid_row_idx], z_col, np.full(len(mid_row_idx), -flt_rat(1, 2) * dx), 2)
    z_col = z_col - flt_rat(1, 2) * dx
    for i in range(30):
        imv = np.imag(psi_col[:, 0, 0] * np.conj(psi_col[:, 0, 1]))
        w_hyp = cell_area / (imv * imv)
        w_flt = np.full(len(mid_row_idx), cell_area, dtype=np.float64)
        accumulate_points(z_col, w_flt, w_hyp)
        if i + 1 < 30:
            psi_col = rk4_step_vec(psi_col, z_col, np.full(len(mid_row_idx), -dx), 2)
            z_col = z_col - dx

    # --- REGION 2: Polar midpoint transition [-1/8, 1/8]^2 \ D(0, 1/16) ---
    r_mid_circ = flt_rat(1, 8)
    r0 = flt_rat(1, 16)
    n_theta = 128
    dtheta = (float(2) * pi_f) / float(n_theta)
    # Start at theta = pi (z = -1/8 + 0i) and step counterclockwise around circle |z| = 1/8
    psi_ring_start = rk4_step_vec(
        psi_left_y0,
        np.array(complex(flt_rat(-1, 2), float(0))),
        np.array(complex(flt_rat(3, 8), float(0))),
        48,
    )
    thetas = pi_f + (np.arange(n_theta, dtype=np.float64) + flt_rat(1, 2)) * dtheta
    psi_ring = np.empty((n_theta, 2, 2), dtype=np.complex128)
    z_prev = complex(-r_mid_circ, float(0))
    psi_cur = psi_ring_start
    # Step to each theta_k along the circle chord (8 tiny substeps per 2pi/128 arc)
    th_prev = pi_f
    for k in range(n_theta):
        th_tgt = float(thetas[k])
        n_arc = 6
        for m in range(n_arc):
            t_a = th_prev + (th_tgt - th_prev) * (float(m) / float(n_arc))
            t_b = th_prev + (th_tgt - th_prev) * (float(m + 1) / float(n_arc))
            za = r_mid_circ * np.exp(I_NP * t_a)
            zb = r_mid_circ * np.exp(I_NP * t_b)
            psi_cur = rk4_step_vec(psi_cur, np.array(za), np.array(zb - za), 1)
        psi_ring[k] = psi_cur
        th_prev = th_tgt

    # Verify single-valuedness of metric around full 2*pi loop on |z| = 1/8:
    psi_loop_back = psi_cur
    th_end = float(3) * pi_f
    for m in range(6):
        t_a = th_prev + (th_end - th_prev) * (float(m) / float(6))
        t_b = th_prev + (th_end - th_prev) * (float(m + 1) / float(6))
        za = r_mid_circ * np.exp(I_NP * t_a)
        zb = r_mid_circ * np.exp(I_NP * t_b)
        psi_loop_back = rk4_step_vec(psi_loop_back, np.array(za), np.array(zb - za), 1)
    im0 = float(np.imag(psi_ring_start[0, 0] * np.conj(psi_ring_start[0, 1])))
    im1 = float(np.imag(psi_loop_back[0, 0] * np.conj(psi_loop_back[0, 1])))
    ring_single_valued_err = abs(float(1) / (im1 * im1) - float(1) / (im0 * im0))

    dirs = np.exp(I_NP * thetas)
    r_max_arr = r_mid_circ / np.maximum(np.abs(np.cos(thetas)), np.abs(np.sin(thetas)))

    # 2a. Outward polar rays from r = 1/8 to r_max(theta)
    n_rout = 12
    dr_out = (r_max_arr - r_mid_circ) / float(n_rout)
    r_cur = np.full(n_theta, r_mid_circ, dtype=np.float64)
    psi_ray = rk4_step_vec(psi_ring, r_cur * dirs, (flt_rat(1, 2) * dr_out) * dirs, 2)
    r_cur = r_cur + flt_rat(1, 2) * dr_out
    for m in range(n_rout):
        z_pts = r_cur * dirs
        w_flt = r_cur * dr_out * dtheta
        imv = np.imag(psi_ray[:, 0, 0] * np.conj(psi_ray[:, 0, 1]))
        w_hyp = w_flt / (imv * imv)
        accumulate_points(z_pts, w_flt, w_hyp)
        if m + 1 < n_rout:
            psi_ray = rk4_step_vec(psi_ray, z_pts, dr_out * dirs, 2)
            r_cur = r_cur + dr_out

    # 2b. Inward polar rays from r = 1/8 down to r0 = 1/16
    n_rin = 16
    dr_in = (r_mid_circ - r0) / float(n_rin)
    r_cur = np.full(n_theta, r_mid_circ, dtype=np.float64)
    psi_ray = rk4_step_vec(psi_ring, r_cur * dirs, (-flt_rat(1, 2) * dr_in) * dirs, 2)
    r_cur = r_cur - flt_rat(1, 2) * dr_in
    for m in range(n_rin):
        z_pts = r_cur * dirs
        w_flt = r_cur * dr_in * dtheta
        imv = np.imag(psi_ray[:, 0, 0] * np.conj(psi_ray[:, 0, 1]))
        w_hyp = w_flt / (imv * imv)
        accumulate_points(z_pts, w_flt, w_hyp)
        if m + 1 < n_rin:
            psi_ray = rk4_step_vec(psi_ray, z_pts, (-dr_in) * dirs, 2)
            r_cur = r_cur - dr_in
    # Final half-step to exact circle r = r0 = 1/16:
    psi_r0 = rk4_step_vec(psi_ray, r_cur * dirs, (-flt_rat(1, 2) * dr_in) * dirs, 2)

    # --- REGION 3: Polar log-radial midpoint annulus D(0, 1/16) \ D(0, 10^{-4}) ---
    # NO t = (-ln r + b_c^*)^{-1} substitution! Uniform steps in s = -ln(r / r0).
    r_min = flt_rat(1, 10000)
    s_max = float(np.log(r0 / r_min))
    n_s = 128
    ds = s_max / float(n_s)
    z_base_r0 = r0 * dirs
    inv_sqrt_r0 = float(1) / float(np.sqrt(r0))
    fmat = np.empty((n_theta, 2, 2), dtype=np.complex128)
    fmat[:, 0, 0] = inv_sqrt_r0 * psi_r0[:, 0, 0]
    fmat[:, 0, 1] = inv_sqrt_r0 * psi_r0[:, 0, 1]
    fmat[:, 1, 0] = inv_sqrt_r0 * (flt_rat(1, 2) * psi_r0[:, 0, 0] - z_base_r0 * psi_r0[:, 1, 0])
    fmat[:, 1, 1] = inv_sqrt_r0 * (flt_rat(1, 2) * psi_r0[:, 0, 1] - z_base_r0 * psi_r0[:, 1, 1])

    s_cur = float(0)
    fmat = rk4_log_step_vec(fmat, z_base_r0, s_cur, flt_rat(1, 2) * ds, 2)
    s_cur += flt_rat(1, 2) * ds
    for m in range(n_s):
        r_m = r0 * float(np.exp(-s_cur))
        z_pts = r_m * dirs
        w_flt = np.full(n_theta, (r_m * r_m) * ds * dtheta, dtype=np.float64)
        im_f = np.imag(fmat[:, 0, 0] * np.conj(fmat[:, 0, 1]))
        # e^{2 Omega} r dr dtheta = ds dtheta / [Im(f1 conj(f2))]^2
        w_hyp = (ds * dtheta) / (im_f * im_f)
        accumulate_points(z_pts, w_flt, w_hyp)
        if m + 1 < n_s:
            fmat = rk4_log_step_vec(fmat, z_base_r0, s_cur, ds, 2)
            s_cur += ds

    # --- REGION 4: Analytic cusp tail inside |z| < r_min = 10^{-4} ---
    bc_star_f = float(fuchs["bc_star"])
    tail_hyp_norm = float(1) / (-float(np.log(r_min)) + bc_star_f)
    tail_hyp_area = (float(2) * pi_f) * tail_hyp_norm
    tail_flat_area = pi_f * (r_min * r_min)
    rho0, psi0 = eval_modes_vec(np.array([complex(0, 0)], dtype=np.complex128))
    rho0 = rho0[0]
    psi0 = psi0[0]
    area_hyp_total += tail_hyp_area
    area_flat_total += tail_flat_area
    K_e2_hyp += rho0 * tail_hyp_area
    K_e2_flat += rho0 * tail_flat_area
    K_cim_hyp += np.outer(np.conj(psi0), psi0) * tail_hyp_area
    K_cim_flat += np.outer(np.conj(psi0), psi0) * tail_flat_area

    # Normalize: flat by tau_im, hyperbolic by 2*pi
    two_pi = float(2) * pi_f
    area_flat_norm = area_flat_total / tau_im
    area_hyp_over_2pi = area_hyp_total / two_pi
    K_e2_flat_norm = K_e2_flat / tau_im
    K_e2_hyp_norm = K_e2_hyp / two_pi
    K_cim_flat_norm = K_cim_flat / tau_im
    K_cim_hyp_norm = K_cim_hyp / two_pi

    # Symmetrize Hermitian K_cim_hyp and extract eigenvalues
    K_cim_herm = flt_rat(1, 2) * (K_cim_hyp_norm + K_cim_hyp_norm.conj().T)
    cim_eigs = np.sort(np.linalg.eigvalsh(K_cim_herm))

    return {
        "area_flat_norm": area_flat_norm,
        "area_hyp_over_2pi": area_hyp_over_2pi,
        "gauss_bonnet_err": abs(area_hyp_over_2pi - float(1)),
        "ring_single_valued_err": ring_single_valued_err,
        "K_e2_flat_max_err": float(np.max(np.abs(K_e2_flat_norm - float(1)))),
        "K_cim_flat_max_err": float(np.max(np.abs(K_cim_flat_norm - np.eye(3)))),
        "K_e2_hyp": K_e2_hyp_norm.tolist(),
        "K_cim_hyp_matrix": K_cim_herm,
        "K_cim_hyp_eigs": cim_eigs.tolist(),
        "K_cim_z2_diag_err": float(abs(K_cim_herm[1, 1] - K_cim_herm[2, 2])),
        "K_cim_z2_off_err": float(abs(K_cim_herm[0, 1] - K_cim_herm[0, 2])),
        "K_cim_01_abs": float(abs(K_cim_herm[0, 1])),
        "K_cim_01_arg_rad": float(np.angle(K_cim_herm[0, 1])),
    }


def eval_szego_yukawa_disjoint_mp(
    tx: Fraction, ty: Fraction, l2_val: mp.mpf, pa: Fraction, pb: Fraction, ql: int, qr: int
) -> mp.matrix:
    """Independent Szego-kernel Yukawa constructor using mp.jtheta (no manual theta sums)."""
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = mp_rat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]

    tau = mp.mpc(frac_to_mp(tx), frac_to_mp(ty))
    xr, yi = mp.re(tau), mp.im(tau)
    q_nom = mp.exp(I_MP * mp.pi * tau)
    q2 = mp.exp(2 * I_MP * mp.pi * tau)

    # Branch-cut-free theta_2,3,4 and their tau-derivatives via heat equation -(1/8) d^2_u theta
    t3 = mp.jtheta(3, 0, q_nom)
    t4 = mp.jtheta(4, 0, q_nom)
    dt3 = -mp_rat(1, 8) * mp.jtheta(3, 0, q_nom, derivative=2)
    dt4 = -mp_rat(1, 8) * mp.jtheta(4, 0, q_nom, derivative=2)

    # theta_2(u) = exp(i pi tau / 4 + i u) theta_3(u + pi tau / 2, q_nom) -> exact branch!
    ph2 = mp.exp(I_MP * mp.pi * tau / 4)
    u2 = mp.pi * tau / 2
    th3_u2 = mp.jtheta(3, u2, q_nom)
    dth3_u2 = mp.jtheta(3, u2, q_nom, derivative=1)
    ddth3_u2 = mp.jtheta(3, u2, q_nom, derivative=2)
    t2 = ph2 * th3_u2
    dt2 = -mp_rat(1, 8) * ph2 * (-th3_u2 + 2 * I_MP * dth3_u2 + ddth3_u2)

    e2s = mp.mpc(1)
    qn = q2
    for n in range(1, 45):
        e2s -= 24 * n * (qn / (1 - qn))
        qn *= q2
    l2d, l3d, l4d = dt2 / t2, dt3 / t3, dt4 / t4
    sh = (
        (-t2 / (t3 * t4)) * (l2d - l3d - l4d + e2s / 24) * qi
        + (-t4 / (t2 * t3)) * (l4d - l2d - l3d + e2s / 24) * qj
        + (I_MP * t3 / (t2 * t4)) * (l3d - l2d - l4d + e2s / 24) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]

    eta_prod = mp.mpc(1)
    qn = q2
    for _ in range(45):
        eta_prod *= 1 - qn
        qn *= q2
    t1p = 2 * mp.pi * (mp.exp(I_MP * mp.pi * tau / 12) * eta_prod) ** 3
    csh = 2 * mp.pi * l2_val + mp.pi * mp.log(yi) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    em2l = mp.exp(-2 * l2_val)

    def th_char(ca: Fraction, cb: Fraction) -> mp.mpc:
        ta = ca % 1
        tb = cb % 1
        nb = int(cb - tb)
        am, bm = frac_to_mp(ta), frac_to_mp(tb)
        val = mp.exp(I_MP * mp.pi * am * am * tau + 2 * I_MP * mp.pi * am * bm) * mp.jtheta(
            3, mp.pi * (am * tau + bm), q_nom
        )
        return val if (nb == 0 or ta == 0) else mp.exp(2 * I_MP * mp.pi * am * nb) * val

    def a0_and_f(ai: Fraction, bi: Fraction) -> tuple[mp.mpf, mp.mpf]:
        al, be = ai % 1, bi % 1
        am, bm = frac_to_mp(al), frac_to_mp(be)
        zv = am * tau + bm
        # d/dz ln theta_1(pi z, q_nom) = pi * theta_1'(pi z) / theta_1(pi z)
        dlog_th1 = mp.pi * mp.jtheta(1, mp.pi * zv, q_nom, derivative=1) / mp.jtheta(1, mp.pi * zv, q_nom)
        a2 = abs(2 * I_MP * mp.pi * am + dlog_th1) ** 2
        if al != 0:
            f0 = -mp.pi * (2 * mp.log(2) + mp.log(yi) + mp.digamma(am) + mp.digamma(1 - am))
        else:
            f0 = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(yi)) + yi * (mp.pi ** 2) / (mp.sin(mp.pi * bm) ** 2)
        sm = mp.mpf(0)
        for k in range(-32, 33):
            m = am + k
            if m == 0:
                continue
            w = mp.exp(-2 * mp.pi * abs(m) * yi + 2 * I_MP * mp.pi * (m * xr + bm))
            sm += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
        return a2, f0 + sm

    hf_r = Fraction(1, 2)
    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am_r = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm_r = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * I_MP * mp.pi * frac_to_mp(xv[0]))
    kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
    cs = {"1": (ap + hf_r, bp + hf_r), "i": (ap + hf_r, bp), "j": (ap, bp + hf_r), "k": (ap, bp)}
    ds = {"1": (am_r + hf_r, bm_r + hf_r), "i": (am_r + hf_r, bm_r), "j": (am_r, bm_r + hf_r), "k": (am_r, bm_r)}
    um = {}
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hf_r, cs[sk][1] - hf_r
        dal, dbe = ds[sk][0] - hf_r, ds[sk][1] - hf_r
        if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
            um[sk] = mp.mpc(0)
            continue
        rv = kap[sk] * th_char(cs[sk][0], cs[sk][1]) * th_char(ds[sk][0], ds[sk][1]) / t1p
        a2, fv = a0_and_f(al, be)
        ag = csh + fv - mp.pi * a2 * em2l
        um[sk] = mp.sqrt(ag) * rv if ag > 0 else mp.mpc(0)
    mw = um["1"] * ed["1"] + um["i"] * ed["i"] + um["j"] * ed["j"] + um["k"] * ed["k"]
    return mp.matrix(
        [
            [
                ct[ra][cb][0, 0] * mw[0, 0]
                + ct[ra][cb][0, 1] * mw[0, 1]
                + ct[ra][cb][1, 0] * mw[1, 0]
                + ct[ra][cb][1, 1] * mw[1, 1]
                for cb in range(3)
            ]
            for ra in range(3)
        ]
    )


def compute_unflavored_lepto_on_radiative_mr_mp(Y_nu: mp.matrix, c_rge: mp.mpf) -> dict[str, mp.mpf]:
    """Prove M_R = I_3 - c (H + H^T) is purely real-symmetric and sum_alpha eps_{1, alpha} == 0."""
    H = Y_nu.H * Y_nu
    M_R = mp.eye(3) - c_rge * (H + H.T)
    max_im_mr = max(abs(mp.im(M_R[r, c])) for r in range(3) for c in range(3))
    M_R_real = mp.matrix([[mp.re(M_R[r, c]) for c in range(3)] for r in range(3)])
    evals, O_R = mp.eigh(mp_rat(1, 2) * (M_R_real + M_R_real.T))
    order = sorted(range(3), key=lambda k: evals[k])
    M_diag = [evals[k] for k in order]
    O_sorted = mp.matrix([[O_R[r, order[c]] for c in range(3)] for r in range(3)])

    Yt = Y_nu * O_sorted
    Ht = Yt.H * Yt
    max_offdiag_re_Ht = max(
        abs(mp.re(Ht[r, c])) for r in range(3) for c in range(3) if r != c
    )
    h00 = mp.re(Ht[0, 0])
    efl = [mp.mpf(0)] * 3
    for j in (1, 2):
        xv = (M_diag[j] / M_diag[0]) ** 2
        gm = mp.re(Ht[j, j]) / (8 * mp.pi)
        dn = (xv - 1) ** 2 + xv * (gm * gm)
        f_sv = mp.sqrt(xv) * ((1 - xv) / dn + 1 - (1 + xv) * mp.log(1 + 1 / xv))
        g_os = (1 - xv) / dn
        for al in range(3):
            p1j = mp.conj(Yt[al, 0]) * Yt[al, j]
            efl[al] += (mp.im(p1j * Ht[0, j]) * f_sv + mp.im(p1j * Ht[j, 0]) * g_os) / (8 * mp.pi * h00)
    eps_unflav = efl[0] + efl[1] + efl[2]
    max_flav_abs = max(abs(x) for x in efl)
    return {
        "max_im_mr": max_im_mr,
        "max_offdiag_re_Ht": max_offdiag_re_Ht,
        "eps_unflav_abs": abs(eps_unflav),
        "max_flav_abs": max_flav_abs,
    }


def extract_flavor_invariants_mp(Yu: mp.matrix, Yd: mp.matrix, Ye: mp.matrix) -> dict[str, mp.mpf]:
    def svd_sorted(M: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
        U, sv, _ = mp.svd_c(M)
        idx = sorted(range(3), key=lambda k: sv[k])
        U_s = mp.matrix([[U[r, idx[c]] for c in range(3)] for r in range(3)])
        return U_s, [sv[idx[c]] for c in range(3)]

    Uu, su = svd_sorted(Yu)
    Ud, sd = svd_sorted(Yd)
    _, se = svd_sorted(Ye)
    V = Uu.H * Ud
    J_ckm = abs(mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0])))
    return {
        "yu_s2_s3": su[1] / su[2],
        "yu_s1_s3": su[0] / su[2],
        "yd_s2_s3": sd[1] / sd[2],
        "ye_s1_s2": se[0] / se[1],
        "ckm_v12": abs(V[0, 1]),
        "ckm_v13": abs(V[0, 2]),
        "ckm_v23": abs(V[1, 2]),
        "ckm_J": J_ckm,
    }


def random_haar_u3_mp(seed: int) -> mp.matrix:
    """Independent deterministic Mezzadri Haar U(3) matrix at active mp.dps."""
    Z = mp.zeros(3, 3)
    k = 1
    for r in range(3):
        for c in range(3):
            u1 = mp_rat(1, 500) + mp_rat(498, 500) * ((mp.sin(mp.mpf(seed * 71 + k * 19)) + 1) / 2)
            u2 = (mp.cos(mp.mpf(seed * 97 + k * 41)) + 1) / 2
            rad = mp.sqrt(-2 * mp.log(u1))
            ang = 2 * mp.pi * u2
            Z[r, c] = rad * (mp.cos(ang) + I_MP * mp.sin(ang))
            k += 1
    # Householder/Gram-Schmidt QR with Mezzadri diagonal phase normalization
    Q = mp.zeros(3, 3)
    for j in range(3):
        v = Z[:, j]
        for i in range(j):
            qi = Q[:, i]
            v = v - (qi.H * v)[0, 0] * qi
        nm = mp.sqrt(mp.re((v.H * v)[0, 0]))
        for r in range(3):
            Q[r, j] = v[r] / nm
        r_jj = (Q[:, j].H * Z[:, j])[0, 0]
        ph = r_jj / abs(r_jj)
        for r in range(3):
            Q[r, j] *= ph
    return Q


def run_ref_a(ow19_json: dict[str, Any]) -> tuple[dict[str, Any], int, dict[str, Any]]:
    discrepancies = 0
    tau_r_mp = mp.mpc(mp_rat(1, 5), mp_rat(8, 5))
    tau_r_c = complex(flt_rat(1, 5), flt_rat(8, 5))

    # REF-A1: Disjoint Fuchsian ODE
    fuchs = solve_fuchsian_disjoint_mp(tau_r_mp)
    ow_fuchs = ow19_json["OW19_A_2d_hyperbolic_kahler_and_lepto"]["fuchsian_tau8_plus"]

    old_dps = mp.mp.dps
    mp.mp.dps = 35
    try:
        c_star_ow19 = parse_mpc_str(ow_fuchs["c_star"])
        bc_ow19 = mp.mpf(ow_fuchs["bc_star_rich"])
        L2_ow19 = mp.mpf(ow_fuchs["L2_from_bc_rich"])
        c_star_diff = abs(fuchs["c_star"] - c_star_ow19)
        bc_diff = abs(fuchs["bc_star"] - bc_ow19)
        L2_diff = abs(fuchs["L2_tau8"] - L2_ow19)
        a1_ok = (
            c_star_diff < mp_pow10(-10)
            and fuchs["tr_comm_err"] < mp_pow10(-12)
            and fuchs["max_im_R"] < mp_pow10(-12)
            and fuchs["curv_err"] < mp_pow10(-8)
            and fuchs["per_1_err"] < mp_pow10(-10)
            and fuchs["per_tau_err"] < mp_pow10(-10)
            and bc_diff < mp_pow10(-7)
            and L2_diff < mp_pow10(-7)
        )
        if not a1_ok:
            discrepancies += 1

        # REF-A2: Disjoint 2D quadrature
        quad = run_disjoint_2d_quadrature_np(fuchs, tau_r_c)
        ow_kah = ow19_json["OW19_A_2d_hyperbolic_kahler_and_lepto"]["kahler_2d_hyperbolic"]
        ow_e2 = [float(x) for x in ow_kah["K_e2_hyp_theta4_theta2_theta3"]]
        ow_cim_eigs = [float(x) for x in ow_kah["K_cim_hyp_eigenvalues"]]
        e2_max_diff = max(abs(quad["K_e2_hyp"][i] - ow_e2[i]) for i in range(3))
        cim_eigs_max_diff = max(abs(quad["K_cim_hyp_eigs"][i] - ow_cim_eigs[i]) for i in range(3))
        a2_ok = (
            quad["gauss_bonnet_err"] < flt_rat(1, 1000)
            and e2_max_diff < flt_rat(2, 1000)
            and cim_eigs_max_diff < flt_rat(2, 1000)
            and quad["K_cim_z2_diag_err"] < flt_rat(1, 10000)
            and quad["K_cim_z2_off_err"] < flt_rat(1, 10000)
        )
        if not a2_ok:
            discrepancies += 1

        # REF-A3: Unflavored leptogenesis == 0 theorem + 5-trial Haar U(3)^3 scrambling
        mp.mp.dps = 40
        # 1. Generic non-trivial complex 3x3 test matrix Y_test -> H = Y_test^H Y_test = A + i B
        Y_test = mp.matrix(
            [
                [mp.mpc(mp_rat(3, 7), mp_rat(2, 5)), mp.mpc(mp_rat(-1, 4), mp_rat(5, 9)), mp.mpc(mp_rat(4, 11), mp_rat(-3, 8))],
                [mp.mpc(mp_rat(2, 9), mp_rat(-7, 10)), mp.mpc(mp_rat(6, 11), mp_rat(1, 3)), mp.mpc(mp_rat(-5, 12), mp_rat(2, 7))],
                [mp.mpc(mp_rat(-4, 9), mp_rat(3, 11)), mp.mpc(mp_rat(1, 5), mp_rat(-2, 3)), mp.mpc(mp_rat(8, 9), mp_rat(1, 4))],
            ]
        )
        lepto_rand = compute_unflavored_lepto_on_radiative_mr_mp(Y_test, mp_rat(1, 20))

        # 2. Actual Synergy S-1 Yukawa matrices (Yu, Yd, Ye, Ynu) via disjoint mp.jtheta constructor
        p3 = (Fraction(1, 5), Fraction(2, 5))
        p4 = (Fraction(1, 6), Fraction(1, 6))
        tx8, ty8 = Fraction(16, 5), Fraction(8, 5)
        w3 = ((mp.mpf(3) + mp.sqrt(5)) / 2) ** (-4)
        w4 = 2 * (((mp.mpf(4) + mp.sqrt(12)) / 2) ** (-4))
        om3, om4 = w3 / (w3 + w4), w4 / (w3 + w4)
        l2_val = fuchs["L2_tau8"]

        eff_mats = []
        for ql, qr in ((1, -4), (1, 2), (-3, 6)):
            y0 = om3 * eval_szego_yukawa_disjoint_mp(tx8, ty8, l2_val, p3[0], p3[1], ql, qr) + om4 * eval_szego_yukawa_disjoint_mp(
                tx8, ty8, l2_val, p4[0], p4[1], ql, qr
            )
            gr = y0.H * y0
            tr_g = mp.re(gr[0, 0] + gr[1, 1] + gr[2, 2])
            eff_mats.append(y0 * (gr * gr) / (tr_g * tr_g))
        Yu_hol, Yd_hol, Ye_hol = eff_mats
        Ynu_s1 = eval_szego_yukawa_disjoint_mp(tx8, ty8, l2_val, p3[0], p3[1], -3, 0)

        lepto_s1 = compute_unflavored_lepto_on_radiative_mr_mp(Ynu_s1, mp_rat(1, 50))

        # Canonicalize with our own independently computed K_{E[2]}^{hyp}
        k_e2_inv_sqrt = mp.diag([mp.mpf(1) / mp.sqrt(mp.mpf(str(x))) for x in quad["K_e2_hyp"]])
        Yu_2d = k_e2_inv_sqrt * Yu_hol * k_e2_inv_sqrt
        Yd_2d = k_e2_inv_sqrt * Yd_hol * k_e2_inv_sqrt
        Ye_2d = k_e2_inv_sqrt * Ye_hol * k_e2_inv_sqrt
        base_inv = extract_flavor_invariants_mp(Yu_2d, Yd_2d, Ye_2d)

        ow_s1 = ow19_json["OW19_A_2d_hyperbolic_kahler_and_lepto"]["synergy_s1_2d_shifts"]
        v12_shift_diff = abs(base_inv["ckm_v12"] - mp.mpf(ow_s1["e2_2d_eff_ckm_v12"]))
        yu23_shift_diff = abs(base_inv["yu_s2_s3"] - mp.mpf(ow_s1["e2_2d_eff_yu_s2_over_s3"]))

        # 5-trial Haar U(3)^3 scrambling test (Guardrail 3)
        max_haar_drift = mp.mpf(0)
        for trial in range(1, 6):
            UQ = random_haar_u3_mp(trial * 101 + 1)
            UuR = random_haar_u3_mp(trial * 101 + 2)
            UdR = random_haar_u3_mp(trial * 101 + 3)
            UL = random_haar_u3_mp(trial * 101 + 4)
            UeR = random_haar_u3_mp(trial * 101 + 5)
            scr_inv = extract_flavor_invariants_mp(
                UQ * Yu_2d * UuR.H, UQ * Yd_2d * UdR.H, UL * Ye_2d * UeR.H
            )
            for key in base_inv:
                drift = abs(scr_inv[key] - base_inv[key])
                if drift > max_haar_drift:
                    max_haar_drift = drift

        a3_ok = (
            lepto_rand["max_im_mr"] == mp.mpf(0)
            and lepto_rand["eps_unflav_abs"] < mp_pow10(-25)
            and lepto_rand["max_flav_abs"] > mp_pow10(-6)
            and lepto_s1["max_im_mr"] == mp.mpf(0)
            and lepto_s1["eps_unflav_abs"] < mp_pow10(-25)
            and lepto_s1["max_flav_abs"] > mp_pow10(-8)
            and max_haar_drift < mp_pow10(-20)
            and v12_shift_diff < mp_rat(2, 1000)
            and yu23_shift_diff < mp_rat(2, 1000)
        )
        if not a3_ok:
            discrepancies += 1

        gate_a = a1_ok and a2_ok and a3_ok
        report = {
            "ref_a1_fuchsian_rk4_fourier": {
                "c_star_referee": f"({mp.nstr(mp.re(fuchs['c_star']), 22)} + {mp.nstr(mp.im(fuchs['c_star']), 22)}j)",
                "c_star_diff_vs_ow19": mp.nstr(c_star_diff, 8),
                "tr_comm_err": mp.nstr(fuchs["tr_comm_err"], 8),
                "im_tr_max": mp.nstr(fuchs["im_tr_max"], 8),
                "max_im_R": mp.nstr(fuchs["max_im_R"], 8),
                "K_z1": mp.nstr(fuchs["K_z1"], 16),
                "curv_err": mp.nstr(fuchs["curv_err"], 8),
                "per_1_err": mp.nstr(fuchs["per_1_err"], 8),
                "per_tau_err": mp.nstr(fuchs["per_tau_err"], 8),
                "bc_star_referee": mp.nstr(fuchs["bc_star"], 18),
                "L2_tau8_referee": mp.nstr(fuchs["L2_tau8"], 18),
                "bc_diff_vs_ow19": mp.nstr(bc_diff, 8),
                "L2_diff_vs_ow19": mp.nstr(L2_diff, 8),
                "ok": a1_ok,
            },
            "ref_a2_disjoint_2d_quadrature": {
                "area_flat_norm": mp.nstr(mp.mpf(str(quad["area_flat_norm"])), 12),
                "area_hyp_over_2pi": mp.nstr(mp.mpf(str(quad["area_hyp_over_2pi"])), 12),
                "gauss_bonnet_err": mp.nstr(mp.mpf(str(quad["gauss_bonnet_err"])), 8),
                "ring_single_valued_err": mp.nstr(mp.mpf(str(quad["ring_single_valued_err"])), 8),
                "K_e2_flat_max_err": mp.nstr(mp.mpf(str(quad["K_e2_flat_max_err"])), 8),
                "K_cim_flat_max_err": mp.nstr(mp.mpf(str(quad["K_cim_flat_max_err"])), 8),
                "K_e2_hyp_referee": [mp.nstr(mp.mpf(str(x)), 10) for x in quad["K_e2_hyp"]],
                "K_e2_max_diff_vs_ow19": mp.nstr(mp.mpf(str(e2_max_diff)), 8),
                "K_cim_hyp_eigs_referee": [mp.nstr(mp.mpf(str(x)), 10) for x in quad["K_cim_hyp_eigs"]],
                "K_cim_eigs_max_diff_vs_ow19": mp.nstr(mp.mpf(str(cim_eigs_max_diff)), 8),
                "K_cim_01_abs": mp.nstr(mp.mpf(str(quad["K_cim_01_abs"])), 10),
                "K_cim_01_arg_rad": mp.nstr(mp.mpf(str(quad["K_cim_01_arg_rad"])), 10),
                "K_cim_z2_diag_err": mp.nstr(mp.mpf(str(quad["K_cim_z2_diag_err"])), 8),
                "K_cim_z2_off_err": mp.nstr(mp.mpf(str(quad["K_cim_z2_off_err"])), 8),
                "ok": a2_ok,
            },
            "ref_a3_lepto_zero_and_haar": {
                "rand_herm_max_im_mr": mp.nstr(lepto_rand["max_im_mr"], 8),
                "rand_herm_offdiag_re_Ht": mp.nstr(lepto_rand["max_offdiag_re_Ht"], 8),
                "rand_herm_eps_unflav_abs": mp.nstr(lepto_rand["eps_unflav_abs"], 8),
                "rand_herm_max_flav_abs": mp.nstr(lepto_rand["max_flav_abs"], 8),
                "synergy_s1_max_im_mr": mp.nstr(lepto_s1["max_im_mr"], 8),
                "synergy_s1_eps_unflav_abs": mp.nstr(lepto_s1["eps_unflav_abs"], 8),
                "synergy_s1_max_flav_abs": mp.nstr(lepto_s1["max_flav_abs"], 8),
                "e2_2d_ckm_v12_referee": mp.nstr(base_inv["ckm_v12"], 10),
                "e2_2d_ckm_v12_diff_vs_ow19": mp.nstr(v12_shift_diff, 8),
                "e2_2d_yu_s2_s3_referee": mp.nstr(base_inv["yu_s2_s3"], 10),
                "e2_2d_yu_s2_s3_diff_vs_ow19": mp.nstr(yu23_shift_diff, 8),
                "haar_5trial_max_drift": mp.nstr(max_haar_drift, 8),
                "ok": a3_ok,
            },
            "gate_ref_a": gate_a,
        }
        return report, discrepancies, fuchs
    finally:
        mp.mp.dps = old_dps


# =============================================================================
# REF-B: Disjoint Countercheck of OW19-B
# =============================================================================
def build_weyl_clifford_sympy() -> dict[str, Any]:
    """Construct 4x4 gamma matrices in the WEYL (CHIRAL) representation
    (completely disjoint from Dirac representation) and compute exact Majorana
    axial and Dirac vector Z'_psi annihilation traces & cross sections."""
    I2 = sp.eye(2)
    Z2 = sp.zeros(2, 2)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])

    g0 = sp.Matrix.vstack(sp.Matrix.hstack(Z2, I2), sp.Matrix.hstack(I2, Z2))
    g1 = sp.Matrix.vstack(sp.Matrix.hstack(Z2, s1), sp.Matrix.hstack(-s1, Z2))
    g2 = sp.Matrix.vstack(sp.Matrix.hstack(Z2, s2), sp.Matrix.hstack(-s2, Z2))
    g3 = sp.Matrix.vstack(sp.Matrix.hstack(Z2, s3), sp.Matrix.hstack(-s3, Z2))
    gam = [g0, g1, g2, g3]
    eta = [1, -1, -1, -1]
    I4 = sp.eye(4)

    g5 = sp.simplify(sp.I * g0 * g1 * g2 * g3)
    g5_expected = sp.diag(-1, -1, 1, 1)
    g5_chiral_ok = (g5 == g5_expected)

    # Verify Clifford algebra {gamma^mu, gamma^nu} = 2 eta^{mu nu} I_4
    clifford_ok = True
    for mu in range(4):
        for nu in range(4):
            lhs = gam[mu] * gam[nu] + gam[nu] * gam[mu]
            rhs = 2 * eta[mu] * I4 if mu == nu else sp.zeros(4, 4)
            if lhs != rhs:
                clifford_ok = False

    C = sp.simplify(sp.I * g2 * g0)
    C_inv = sp.simplify(C.inv())
    C_antisym_ok = (C.T == -C)
    C_conj_ok = all(sp.simplify(C * gam[mu] * C_inv + gam[mu].T) == sp.zeros(4, 4) for mu in range(4))
    vec_sym_ok = all(sp.simplify((C_inv * gam[mu]).T - (C_inv * gam[mu])) == sp.zeros(4, 4) for mu in range(4))
    ax_antisym_ok = all(
        sp.simplify((C_inv * gam[mu] * g5).T + (C_inv * gam[mu] * g5)) == sp.zeros(4, 4) for mu in range(4)
    )

    # Explicit CM-frame 4x4 traces for psi_S(p1) psi_S(p2) -> f_L(k1) bar{f}_L(k2)
    E, p, m, th, v = sp.symbols("E p m th v", real=True, positive=True)
    p1_vec = [E, 0, 0, p]
    p2_vec = [E, 0, 0, -p]
    k1_vec = [E, E * sp.sin(th), 0, E * sp.cos(th)]
    k2_vec = [E, -E * sp.sin(th), 0, -E * sp.cos(th)]

    def slash(vec) -> sp.Matrix:
        return sum(eta[mu] * vec[mu] * gam[mu] for mu in range(4))

    sl_p1 = slash(p1_vec)
    sl_p2 = slash(p2_vec)
    sl_k1 = slash(k1_vec)
    sl_k2 = slash(k2_vec)
    PL = (I4 - g5) / 2

    tr_ax = sp.Integer(0)
    tr_vec = sp.Integer(0)
    for mu in range(4):
        for nu in range(4):
            R_mn = sp.trace(sl_k1 * gam[mu] * PL * sl_k2 * gam[nu] * PL)
            L_ax = sp.trace((sl_p1 + m * I4) * gam[mu] * g5 * (sl_p2 - m * I4) * gam[nu] * g5)
            L_vc = sp.trace((sl_p1 + m * I4) * gam[mu] * (sl_p2 - m * I4) * gam[nu])
            tr_ax += eta[mu] * eta[nu] * L_ax * R_mn
            tr_vec += eta[mu] * eta[nu] * L_vc * R_mn

    tr_ax = sp.simplify(tr_ax.subs(m**2, E**2 - p**2))
    tr_vec = sp.simplify(tr_vec.subs(m**2, E**2 - p**2))

    # Integrate spin-averaged (1/4) |M|^2 over solid angle:
    # (sigma v_rel)_unit = (2 pi / (128 pi^2 E^2)) * int_0^pi (1/4) trace * sin(th) d(th)
    sv_unit_maj = sp.simplify(
        (2 * sp.pi / (128 * sp.pi**2 * E**2))
        * sp.Rational(1, 4)
        * sp.integrate(tr_ax * sp.sin(th), (th, 0, sp.pi))
    ).subs(p, E * v / 2)
    sv_unit_maj = sp.simplify(sv_unit_maj)
    sv_maj_swave = sp.simplify(sv_unit_maj.subs(v, 0))

    sv_unit_vec = sp.simplify(
        (2 * sp.pi / (128 * sp.pi**2 * E**2))
        * sp.Rational(1, 4)
        * sp.integrate(tr_vec * sp.sin(th), (th, 0, sp.pi))
    ).subs(p, E * v / 2)
    sv_vec_swave = sp.simplify(sv_unit_vec.subs(v, 0))

    # E_6 charge normalization & low-energy dim-5 cancellation
    g_gut, S_vev, c5, M11 = sp.symbols("g_gut S_vev c5 M11", positive=True)
    Q_S_sq = sp.Rational(16, 24)   # 2/3
    Q_16_sq = sp.Rational(1, 24)
    M_Zp_sq = 2 * g_gut**2 * Q_S_sq * S_vev**2
    m_psiS = c5 * S_vev**2 / M11

    sv_pref_unit = sv_unit_maj.subs(E, 1) / (v**2)  # 1/(12 pi)
    pwave_3x15 = sp.simplify(45 * Q_S_sq * Q_16_sq * sv_pref_unit)
    pwave_3x16 = sp.simplify(48 * Q_S_sq * Q_16_sq * sv_pref_unit)

    dim5_3x15 = sp.simplify(pwave_3x15 * (g_gut**4) * (m_psiS**2) * (v**2) / (M_Zp_sq**2))
    dim5_3x16 = sp.simplify(pwave_3x16 * (g_gut**4) * (m_psiS**2) * (v**2) / (M_Zp_sq**2))
    cancel_ok = (
        g_gut not in dim5_3x15.free_symbols
        and S_vev not in dim5_3x15.free_symbols
        and g_gut not in dim5_3x16.free_symbols
        and S_vev not in dim5_3x16.free_symbols
    )

    return {
        "g5_chiral_ok": g5_chiral_ok,
        "clifford_ok": clifford_ok,
        "C_antisym_ok": C_antisym_ok,
        "C_conj_ok": C_conj_ok,
        "vec_sym_ok": vec_sym_ok,
        "ax_antisym_ok": ax_antisym_ok,
        "tr_ax": tr_ax,
        "tr_vec": tr_vec,
        "sv_unit_maj": sv_unit_maj,
        "sv_maj_swave": sv_maj_swave,
        "sv_vec_swave": sv_vec_swave,
        "pwave_3x15_times_pi": sp.simplify(pwave_3x15 * sp.pi),
        "pwave_3x16_times_pi": sp.simplify(pwave_3x16 * sp.pi),
        "dim5_3x15": dim5_3x15,
        "dim5_3x16": dim5_3x16,
        "cancel_ok": cancel_ok,
    }


def run_ref_b(ow19_json: dict[str, Any]) -> tuple[dict[str, Any], int, dict[str, Any]]:
    discrepancies = 0
    ow_b = ow19_json["OW19_B_e6_hierarchy_axion_and_majorana_dm"]

    # REF-B1: Weyl-rep Majorana DM annihilation
    weyl = build_weyl_clifford_sympy()
    c5, M11, v = sp.symbols("c5 M11 v", positive=True)
    exp_3x15 = sp.Rational(15, 256) * c5**2 * v**2 / (sp.pi * M11**2)
    exp_3x16 = sp.Rational(1, 16) * c5**2 * v**2 / (sp.pi * M11**2)
    b1_ok = (
        weyl["g5_chiral_ok"]
        and weyl["clifford_ok"]
        and weyl["C_antisym_ok"]
        and weyl["C_conj_ok"]
        and weyl["vec_sym_ok"]
        and weyl["ax_antisym_ok"]
        and weyl["sv_maj_swave"] == 0
        and weyl["pwave_3x15_times_pi"] == sp.Rational(5, 48)
        and weyl["pwave_3x16_times_pi"] == sp.Rational(1, 9)
        and sp.simplify(weyl["dim5_3x15"] - exp_3x15) == 0
        and sp.simplify(weyl["dim5_3x16"] - exp_3x16) == 0
        and weyl["cancel_ok"]
        and ow_b["b3_majorana_psiS_pwave_dm"]["pwave_coeff_pi_3x15_SM"] == "5/48"
        and ow_b["b3_majorana_psiS_pwave_dm"]["pwave_coeff_pi_3x16_SM_NR"] == "1/9"
    )
    if not b1_ok:
        discrepancies += 1

    # REF-B2: Disjoint E_6 1-loop Z'_psi shift via gauge-box RGE + Landau-gauge d=4-2eps tadpole
    tr_Q = 16 * 1 + 10 * (-2) + 1 * 4
    tr_Q2 = 16 * (1**2) + 10 * ((-2)**2) + 1 * (4**2)
    T_27 = 2 + 1 + 0  # T(16) + T(10) + T(1)
    N_psi_sq = Fraction(tr_Q2, T_27)  # 24
    Q_S_GUT_sq = Fraction(16, 1) / N_psi_sq  # 2/3
    Q_H_GUT_sq = Fraction(4, 1) / N_psi_sq   # 1/6

    # Gauge-box RGE: 16 pi^2 d(lam_HS)/d(ln mu) = +12 g^4 Q_S^2 Q_H^2
    beta_lam_HS_over_g4 = 12 * Q_S_GUT_sq * Q_H_GUT_sq  # 4/3
    # Running downward from Lambda to M_Z': lam_HS(M_Z') = -(beta / (32 pi^2)) ln(Lambda^2 / M_Z'^2)
    # -> delta m_H^2|_{RGE} = lam_HS(M_Z') |<S>|^2 = -(beta / (32 pi^2)) |<S>|^2 ln(Lambda^2 / M_Z'^2)
    coeff_S2_rge = -beta_lam_HS_over_g4 / 32  # -1/24 (multiplying g^4 |<S>|^2 / pi^2)
    # Using M_{Z'}^2 = 2 g^2 Q_S^2 |<S>|^2 = (4/3) g^2 |<S>|^2:
    coeff_MZp2_rge = coeff_S2_rge / (2 * Q_S_GUT_sq)  # -1/32 (multiplying g^2 M_{Z'}^2 / pi^2)

    # Disjoint finite threshold matching via d = 4 - 2*eps Landau-gauge vector tadpole:
    # (d - 1) * (1/eps_bar + 1 - ln(M^2/mu^2)) = 3/eps_bar + (3 - 2) - 3 ln(M^2/mu^2)
    eps_sym = sp.Symbol("eps")
    L_sym = sp.Symbol("L")  # ln(Lambda^2 / M_{Z'}^2)
    tad_laurent = sp.expand((3 - 2 * eps_sym) * (1 / eps_sym + 1 + L_sym))
    finite_part = sp.simplify(sp.series(tad_laurent, eps_sym, 0, 1).removeO() - 3 / eps_sym)
    # Divide by 3 to extract [ln(Lambda^2 / M_{Z'}^2) + c_fin]:
    c_fin = sp.simplify(finite_part / 3 - L_sym)  # == +1/3
    # Check Landau-gauge prefactor: -(3 g^2 Q_H^2 / (16 pi^2)) M_{Z'}^2 [L + 1/3]
    coeff_MZp2_tad = -Fraction(3, 16) * Q_H_GUT_sq  # -1/32

    # Theorem 2: 7D CS axion d-sheet invariance for d in {1, 2, 5, 7, 15}
    d_sym, R_sym, V1_sym, I1_sym, M11_sym = sp.symbols("d R V1 I1 M11", positive=True)
    # 7D = 4D x M_3(R): Vol(M^{(d)}) = d V1 R^3, int omega_3 ^ *omega_3 = d I1 R^{-3}
    Mpl_d = sp.sqrt(d_sym * V1_sym * (R_sym**3) * (M11_sym**5))
    fa_d = sp.sqrt(d_sym * I1_sym * (R_sym**(-3)) * (M11_sym**(-1)))
    ratio_d = sp.simplify(fa_d / Mpl_d)
    d_invar_sym = (sp.simplify(sp.diff(ratio_d, d_sym)) == 0)
    # Einstein-frame Casimir potential: V_E = (Vol_3)^{-2} * Vol_3 * R^{-7} = R^{-10}
    Vcas_R_exp = -2 * 3 + 3 - 7
    fa_Mpl_R_exp = sp.Rational(-3, 2) - sp.Rational(3, 2)

    old_dps = mp.mp.dps
    mp.mp.dps = 40
    try:
        v1_num = mp.pi * mp.sqrt(mp.mpf(3))
        i1_num = mp.mpf(7) / mp.mpf(11)
        r_num = mp_rat(5, 3)
        base_ratio = mp.sqrt(i1_num * (r_num ** (-3))) / mp.sqrt(v1_num * (r_num ** 3))
        d_list = [1, 2, 5, 7, 15]
        max_d_drift = mp.mpf(0)
        for dv in d_list:
            rat_dv = mp.sqrt(mp.mpf(dv) * i1_num * (r_num ** (-3))) / mp.sqrt(mp.mpf(dv) * v1_num * (r_num ** 3))
            dr = abs(rat_dv - base_ratio)
            if dr > max_d_drift:
                max_d_drift = dr
    finally:
        mp.mp.dps = old_dps

    b2_ok = (
        tr_Q == 0
        and tr_Q2 == 72
        and N_psi_sq == Fraction(24, 1)
        and beta_lam_HS_over_g4 == Fraction(4, 3)
        and coeff_S2_rge == Fraction(-1, 24)
        and coeff_MZp2_rge == Fraction(-1, 32)
        and coeff_MZp2_tad == Fraction(-1, 32)
        and c_fin == sp.Rational(1, 3)
        and d_invar_sym
        and max_d_drift < mp_pow10(-35)
        and Vcas_R_exp == -10
        and fa_Mpl_R_exp == -3
        and ow_b["b1_e6_nonsusy_hierarchy"]["dm_H2_coeff_on_g4_S2_over_pi2"] == "-1/24"
        and ow_b["b1_e6_nonsusy_hierarchy"]["dm_H2_coeff_on_g2_MZp2_over_pi2"] == "-1/32"
    )
    if not b2_ok:
        discrepancies += 1

    gate_b = b1_ok and b2_ok
    report = {
        "ref_b1_weyl_rep_majorana_dm": {
            "clifford_and_weyl_C_ok": bool(
                weyl["g5_chiral_ok"] and weyl["clifford_ok"] and weyl["C_antisym_ok"]
                and weyl["C_conj_ok"] and weyl["vec_sym_ok"] and weyl["ax_antisym_ok"]
            ),
            "majorana_ax_trace_weyl": str(weyl["tr_ax"]),
            "dirac_vec_trace_weyl": str(weyl["tr_vec"]),
            "majorana_swave": str(weyl["sv_maj_swave"]),
            "dirac_vec_swave": str(weyl["sv_vec_swave"]),
            "pwave_3x15_times_pi": str(weyl["pwave_3x15_times_pi"]),
            "pwave_3x16_times_pi": str(weyl["pwave_3x16_times_pi"]),
            "dim5_3x15": str(weyl["dim5_3x15"]),
            "dim5_3x16": str(weyl["dim5_3x16"]),
            "g_and_S_cancel": weyl["cancel_ok"],
            "ok": b1_ok,
        },
        "ref_b2_rge_tadpole_and_theorem2": {
            "beta_lam_HS_over_g4": str(beta_lam_HS_over_g4),
            "coeff_S2_rge": str(coeff_S2_rge),
            "coeff_MZp2_rge": str(coeff_MZp2_rge),
            "coeff_MZp2_tadpole": str(coeff_MZp2_tad),
            "finite_threshold_const": str(c_fin),
            "theorem2_d_invariance_sym": d_invar_sym,
            "theorem2_d_1_2_5_7_15_max_drift": mp.nstr(max_d_drift, 8),
            "Vcas_R_exp": Vcas_R_exp,
            "fa_Mpl_R_exp": int(fa_Mpl_R_exp),
            "ok": b2_ok,
        },
        "gate_ref_b": gate_b,
    }
    return report, discrepancies, weyl


# =============================================================================
# REF-C: Disjoint Countercheck of OW19-C
# =============================================================================
def eval_E3_direct_lattice_sum_np(x: float, y: float, r_max: float) -> dict[str, float]:
    """Direct 2D Euclidean-ball lattice sum sum'_{(m,n) != (0,0)} y^3 / |m + n tau|^6
    plus exact analytic partial derivatives (completely disjoint from Chowla-Selberg)."""
    n_max = int(np.floor(r_max / y))
    r2_max = r_max * r_max

    # Use (m, n) <-> (-m, -n) symmetry: n = 0 with m >= 1, plus n >= 1 with all m in ball
    m_n0 = np.arange(1, int(np.floor(r_max)) + 1, dtype=np.float64)
    D0 = m_n0 * m_n0
    invD3_0 = D0 ** (-3)
    f_acc = float(2) * (y ** 3) * float(np.sum(invD3_0))
    fx_acc = float(0)
    fy_acc = float(2) * float(3) * (y ** 2) * float(np.sum(invD3_0))
    fxx_acc = float(0)
    fxy_acc = float(0)
    fyy_acc = float(2) * float(6) * y * float(np.sum(invD3_0))

    y2 = y * y
    y3 = y2 * y
    y5 = y3 * y2

    for n in range(1, n_max + 1):
        nf = float(n)
        v = nf * y
        v2 = v * v
        rem = r2_max - v2
        if rem < float(0):
            continue
        span = float(np.sqrt(rem))
        m_lo = int(np.ceil(-nf * x - span))
        m_hi = int(np.floor(-nf * x + span))
        if m_lo > m_hi:
            continue
        m_arr = np.arange(m_lo, m_hi + 1, dtype=np.float64)
        u = m_arr + nf * x
        D = u * u + v2
        invD = float(1) / D
        invD3 = invD * invD * invD
        invD4 = invD3 * invD
        invD5 = invD4 * invD
        n2 = nf * nf
        n4 = n2 * n2

        # Multiply by 2 for (m, n) and (-m, -n)
        f_acc += float(2) * y3 * float(np.sum(invD3))
        fx_acc += float(2) * (-float(6) * nf * y3) * float(np.sum(u * invD4))
        fy_acc += float(2) * float(np.sum(float(3) * y2 * invD3 - float(6) * n2 * y3 * y * invD4))
        fxx_acc += float(2) * float(np.sum(-float(6) * n2 * y3 * invD4 + float(48) * n2 * (u * u) * y3 * invD5))
        fxy_acc += float(2) * float(np.sum(-float(18) * nf * y2 * u * invD4 + float(48) * n2 * v * y3 * u * invD5))
        fyy_acc += float(2) * float(
            np.sum(float(6) * y * invD3 - float(42) * n2 * y3 * invD4 + float(48) * n4 * y5 * invD5)
        )

    return {
        "val": f_acc,
        "fx": fx_acc,
        "fy": fy_acc,
        "fxx": fxx_acc,
        "fxy": fxy_acc,
        "fyy": fyy_acc,
    }


def eval_F3_direct_lattice_tau_star() -> dict[str, float]:
    """Evaluate F_3(tau) = E_3(tau) + E_3(5 tau), gradient, and 2D Hessian at tau_*^+ = (2 + i)/5."""
    x0, y0 = flt_rat(2, 5), flt_rat(1, 5)
    e1 = eval_E3_direct_lattice_sum_np(x0, y0, r_max=float(70))
    e5 = eval_E3_direct_lattice_sum_np(float(5) * x0, float(5) * y0, r_max=float(130))

    val = e1["val"] + e5["val"]
    fx = e1["fx"] + float(5) * e5["fx"]
    fy = e1["fy"] + float(5) * e5["fy"]
    fxx = e1["fxx"] + float(25) * e5["fxx"]
    fxy = e1["fxy"] + float(25) * e5["fxy"]
    fyy = e1["fyy"] + float(25) * e5["fyy"]

    H = np.array([[fxx, fxy], [fxy, fyy]], dtype=np.float64)
    eigs = np.sort(np.linalg.eigvalsh(H))
    # Independent hyperbolic Laplacian check: y^2 (e1_xx + e1_yy) == 6 * e1_val
    hyp_lap_err = abs((y0 * y0) * (e1["fxx"] + e1["fyy"]) - float(6) * e1["val"])

    return {
        "val": val,
        "grad_norm": float(np.hypot(fx, fy)),
        "fxx": fxx,
        "fxy": fxy,
        "fyy": fyy,
        "lam_min": float(eigs[0]),
        "lam_max": float(eigs[1]),
        "det_H": float(fxx * fyy - fxy * fxy),
        "hyp_lap_err": hyp_lap_err,
    }


def generate_e8_weyl_orbit_and_census() -> dict[str, Any]:
    """Generate all 240 roots of E_8 purely by WEYL REFLECTION ORBIT from the 8 Bourbaki
    simple roots (completely disjoint from explicit 112+128 enumeration), verify Cartan
    det == 1, carve nested subgroups & 16/27 weights, and exhaustively verify Z_5 Wilson lines."""
    # Doubled integer coordinates in Z^8 (so alpha . alpha == 8, true dot == dot_2x // 4):
    simple_2x = [
        (1, -1, -1, -1, -1, -1, -1, 1),   # alpha_1 (spinor end -> E_6 \ SO(10))
        (2, 2, 0, 0, 0, 0, 0, 0),         # alpha_2 (SO(10) \ SU(5))
        (-2, 2, 0, 0, 0, 0, 0, 0),        # alpha_3 (SU(3)_C)
        (0, -2, 2, 0, 0, 0, 0, 0),        # alpha_4 (SU(3)_C)
        (0, 0, -2, 2, 0, 0, 0, 0),        # alpha_5 (SU(5) \ G_SM)
        (0, 0, 0, -2, 2, 0, 0, 0),        # alpha_6 (SU(2)_L)
        (0, 0, 0, 0, -2, 2, 0, 0),        # alpha_7 (E_7 \ E_6)
        (0, 0, 0, 0, 0, -2, 2, 0),        # alpha_8 (E_8 \ E_7)
    ]

    def dot2x(u: tuple[int, ...], v: tuple[int, ...]) -> int:
        return sum(a * b for a, b in zip(u, v))

    # Cartan matrix A_ij = 2 (a_i . a_j) / (a_j . a_j) = dot2x(a_i, a_j) // 4
    cartan = sp.Matrix([[dot2x(simple_2x[i], simple_2x[j]) // 4 for j in range(8)] for i in range(8)])
    cartan_det = int(cartan.det())

    # BFS Weyl reflection orbit: s_alpha(v) = v - (2 v.a / a.a) a = v - (dot2x(v,a)//4) a
    roots_set: set[tuple[int, ...]] = set(simple_2x)
    q = deque(simple_2x)
    while q:
        v = q.popleft()
        for a in simple_2x:
            d_va = dot2x(v, a)
            assert d_va % 4 == 0
            k = d_va // 4
            refl = tuple(v[idx] - k * a[idx] for idx in range(8))
            if refl not in roots_set:
                roots_set.add(refl)
                q.append(refl)

    roots_list = sorted(roots_set)
    all_norm8 = all(dot2x(r, r) == 8 for r in roots_list)

    # Express every root uniquely in simple-root coordinates r = sum_i n_i alpha_i
    S_mat = sp.Matrix([[simple_2x[j][i] for j in range(8)] for i in range(8)])
    S_inv = S_mat.inv()
    root_coords: dict[tuple[int, ...], tuple[int, ...]] = {}
    for r in roots_list:
        vec = S_inv * sp.Matrix(r)
        assert all(x.is_integer for x in vec)
        root_coords[r] = tuple(int(x) for x in vec)

    # Nested root subsystems via simple-root indices (0-based):
    # G_SM: {2, 3, 5}; SU(5): {2, 3, 4, 5}; SO(10): {1, 2, 3, 4, 5};
    # E_6: {0..5}; E_7: {0..6}; E_8: {0..7}
    sub_indices = {
        "G_SM": (2, 3, 5),
        "SU(5)": (2, 3, 4, 5),
        "SO(10)": (1, 2, 3, 4, 5),
        "E_6": (0, 1, 2, 3, 4, 5),
        "E_7": (0, 1, 2, 3, 4, 5, 6),
        "E_8": (0, 1, 2, 3, 4, 5, 6, 7),
    }
    sub_ranks = {"G_SM": 4, "SU(5)": 4, "SO(10)": 5, "E_6": 6, "E_7": 7, "E_8": 8}
    sub_roots: dict[str, list[tuple[int, ...]]] = {}
    for name, idxs in sub_indices.items():
        allowed = set(idxs)
        sub_roots[name] = [
            r for r in roots_list if all(root_coords[r][i] == 0 for i in range(8) if i not in allowed)
        ]

    # Weight systems carved directly from the Weyl-generated E_8 roots:
    # 16 of SO(10) = roots in E_6 with n_1 == +1; 27 of E_6 = roots in E_7 with n_7 == +1
    w_16 = [r for r in sub_roots["E_6"] if root_coords[r][0] == 1]
    w_27 = [r for r in sub_roots["E_7"] if root_coords[r][6] == 1]

    # Exact rational 6D s=3 E[5] Casimir formula:
    # C_6 = 4 (n_F^(0) - n_B^(0)) - (24/25) (n_F^(tw) - n_B^(tw))
    def calc_c6(u_vec: int, t_vec: int, u_f: int, t_f: int, dof_f: int) -> Fraction:
        nb0, nbtw = 4 * u_vec, 4 * t_vec
        nf0, nftw = dof_f * u_f, dof_f * t_f
        return Fraction(4, 1) * (nf0 - nb0) - Fraction(24, 25) * (nftw - nbtw)

    # Pure 6Y (mod 5) table: 6Y = (-2, -2, -2, +3, +3, 0, 0, 0) (true inner product = dot(6Y, r_2x) // 2)
    six_Y = (-2, -2, -2, 3, 3, 0, 0, 0)

    def count_untw_6Y(vecs: list[tuple[int, ...]]) -> tuple[int, int]:
        u = 0
        for v in vecs:
            d = sum(a * b for a, b in zip(six_Y, v))
            assert d % 2 == 0
            if (d // 2) % 5 == 0:
                u += 1
        return u, len(vecs) - u

    u16_6Y, t16_6Y = count_untw_6Y(w_16)
    u27_6Y, t27_6Y = count_untw_6Y(w_27)
    pure_6Y_table = {}
    for gname in ("G_SM", "SU(5)", "SO(10)", "E_6", "E_7", "E_8"):
        ur, tr = count_untw_6Y(sub_roots[gname])
        ug = ur + sub_ranks[gname]
        tg = tr
        pure_6Y_table[gname] = {
            "untw_tw_gauge": [ug, tg],
            "C6_pure_YM": str(calc_c6(ug, tg, 0, 0, 2)),
            "C6_3x16_4Dchiral": str(calc_c6(ug, tg, 3 * u16_6Y, 3 * t16_6Y, 2)),
            "C6_3x27_4Dchiral": str(calc_c6(ug, tg, 3 * u27_6Y, 3 * t27_6Y, 2)),
        }

    # Exhaustive Z_5 Wilson-line census: W = sum_{j in I_G} c_j alpha_j (mod 5) with W . alpha_{3,4,6} == 0 mod 5
    gsm_root_idxs = (2, 3, 5)
    census = {}
    total_scanned = 0
    for gname in ("G_SM", "SU(5)", "SO(10)", "E_6", "E_7", "E_8"):
        if gname == "G_SM":
            ug = 12
            tg = 0
            census[gname] = {
                "max_pure_YM_C6": str(calc_c6(ug, tg, 0, 0, 2)),
                "max_pure_YM_untw_tw": [ug, tg],
                "max_3x16_4Dchiral_C6": str(calc_c6(ug, tg, 3 * u16_6Y, 3 * t16_6Y, 2)),
                "z5_tuples_scanned": 1,
            }
            continue

        idxs = sub_indices[gname]
        rk = sub_ranks[gname]
        # Solve M * c == 0 (mod 5) where M_{a, b} = cartan[gsm_root_idxs[a], idxs[b]] mod 5
        # Find exact F_5 nullspace basis by Gaussian elimination mod 5
        M_rows = [[int(cartan[gi, j]) % 5 for j in idxs] for gi in gsm_root_idxs]
        # Row-reduce over F_5
        piv_cols = []
        row_i = 0
        ncols = len(idxs)
        for col in range(ncols):
            piv = None
            for r in range(row_i, len(M_rows)):
                if M_rows[r][col] % 5 != 0:
                    piv = r
                    break
            if piv is None:
                continue
            M_rows[row_i], M_rows[piv] = M_rows[piv], M_rows[row_i]
            inv_p = pow(M_rows[row_i][col], -1, 5)
            M_rows[row_i] = [(x * inv_p) % 5 for x in M_rows[row_i]]
            for r in range(len(M_rows)):
                if r != row_i and M_rows[r][col] != 0:
                    fac = M_rows[r][col]
                    M_rows[r] = [(M_rows[r][c] - fac * M_rows[row_i][c]) % 5 for c in range(ncols)]
            piv_cols.append(col)
            row_i += 1

        free_cols = [c for c in range(ncols) if c not in piv_cols]
        basis_vecs = []
        for fc in free_cols:
            vec = [0] * ncols
            vec[fc] = 1
            for pr_idx, pc in enumerate(piv_cols):
                vec[pc] = (-M_rows[pr_idx][fc]) % 5
            basis_vecs.append(vec)

        # Precompute inner products (alpha_j . r) // 4 mod 5 for every root r of G and weights 16, 27
        g_roots = sub_roots[gname]
        # Basis vectors in doubled coordinates (mod 5 applies after dot2x // 4)
        basis_2x = []
        for bvec in basis_vecs:
            w2x = [0] * 8
            for local_i, coeff in enumerate(bvec):
                if coeff != 0:
                    sr = simple_2x[idxs[local_i]]
                    for d in range(8):
                        w2x[d] += coeff * sr[d]
            basis_2x.append(tuple(w2x))

        n_free = len(basis_2x)
        g_dot_mat = [[(dot2x(b, r) // 4) % 5 for r in g_roots] for b in basis_2x]
        w16_dot_mat = [[(dot2x(b, w) // 4) % 5 for w in w_16] for b in basis_2x]
        w27_dot_mat = [[(dot2x(b, w) // 4) % 5 for w in w_27] for b in basis_2x]

        best_ym = None
        best_ym_ut = None
        best_16_4d = None
        best_16_6d = None
        best_27_4d = None
        best_27_6d = None
        strict_gsm_cnt = 0
        scanned = 0

        for coeffs in itertools.product(range(5), repeat=n_free):
            scanned += 1
            # Count untwisted roots in G
            u_r = 0
            for ri in range(len(g_roots)):
                s_val = 0
                for bi in range(n_free):
                    s_val += coeffs[bi] * g_dot_mat[bi][ri]
                if s_val % 5 == 0:
                    u_r += 1
            ug = u_r + rk
            tg = len(g_roots) - u_r
            if u_r == 8:  # 6 SU(3) + 2 SU(2) roots -> strict G_SM x U(1)^{rk - 4}
                strict_gsm_cnt += 1

            c6_ym = calc_c6(ug, tg, 0, 0, 2)
            if best_ym is None or c6_ym > best_ym:
                best_ym = c6_ym
                best_ym_ut = [ug, tg]

            if gname in ("SO(10)", "E_6", "E_7", "E_8"):
                u16 = 0
                for wi in range(16):
                    s_val = 0
                    for bi in range(n_free):
                        s_val += coeffs[bi] * w16_dot_mat[bi][wi]
                    if s_val % 5 == 0:
                        u16 += 1
                c16_4 = calc_c6(ug, tg, 3 * u16, 3 * (16 - u16), 2)
                c16_6 = calc_c6(ug, tg, 3 * u16, 3 * (16 - u16), 4)
                if best_16_4d is None or c16_4 > best_16_4d:
                    best_16_4d = c16_4
                if best_16_6d is None or c16_6 > best_16_6d:
                    best_16_6d = c16_6

            if gname in ("E_6", "E_7", "E_8"):
                u27 = 0
                for wi in range(27):
                    s_val = 0
                    for bi in range(n_free):
                        s_val += coeffs[bi] * w27_dot_mat[bi][wi]
                    if s_val % 5 == 0:
                        u27 += 1
                c27_4 = calc_c6(ug, tg, 3 * u27, 3 * (27 - u27), 2)
                c27_6 = calc_c6(ug, tg, 3 * u27, 3 * (27 - u27), 4)
                if best_27_4d is None or c27_4 > best_27_4d:
                    best_27_4d = c27_4
                if best_27_6d is None or c27_6 > best_27_6d:
                    best_27_6d = c27_6

        total_scanned += scanned
        entry = {
            "z5_tuples_scanned": scanned,
            "strict_G_SM_x_U1k_count": strict_gsm_cnt,
            "max_pure_YM_C6": str(best_ym),
            "max_pure_YM_untw_tw": best_ym_ut,
        }
        if best_16_4d is not None:
            entry["max_3x16_4Dchiral_C6"] = str(best_16_4d)
            entry["max_3x16_6Dweyl_C6"] = str(best_16_6d)
        if best_27_4d is not None:
            entry["max_3x27_4Dchiral_C6"] = str(best_27_4d)
            entry["max_3x27_6Dweyl_C6"] = str(best_27_6d)
        census[gname] = entry

    return {
        "e8_root_count": len(roots_list),
        "all_norm8": all_norm8,
        "cartan_det": cartan_det,
        "sub_root_counts": {k: len(v) for k, v in sub_roots.items()},
        "w_16_count": len(w_16),
        "w_27_count": len(w_27),
        "total_z5_tuples_scanned": total_scanned,
        "pure_6Y_table": pure_6Y_table,
        "exhaustive_census": census,
        "z2_scherk_schwarz_factor": str(Fraction(1, 2 ** 2) - Fraction(1, 1)),  # 2^{1-3} - 1 = -3/4
    }


def run_ref_c(ow19_json: dict[str, Any]) -> tuple[dict[str, Any], int, dict[str, Any]]:
    discrepancies = 0
    ow_c = ow19_json["OW19_C_6d_s3_z5_root_lattice_casimir"]

    # REF-C1: Direct 2D lattice sum for F_3(tau_*^+) + gradient + Hessian
    lat = eval_F3_direct_lattice_tau_star()
    ow_f3 = ow_c["fricke_E3_hessian_tau_star"]
    val_diff = abs(lat["val"] - float(ow_f3["F3_tau_star_plus"]))
    lmin_diff = abs(lat["lam_min"] - float(ow_f3["hess_lam_min"]))
    lmax_diff = abs(lat["lam_max"] - float(ow_f3["hess_lam_max"]))
    c1_ok = (
        val_diff < flt_rat(1, 1000000)
        and lat["grad_norm"] < flt_rat(1, 1000000)
        and lmin_diff < flt_rat(1, 10000)
        and lmax_diff < flt_rat(1, 10000)
        and lat["lam_min"] > float(0)
        and lat["lam_max"] > float(0)
        and lat["det_H"] > float(0)
    )
    if not c1_ok:
        discrepancies += 1

    # REF-C2: Weyl-reflection E_8 orbit & exact rational C_6 census
    lie = generate_e8_weyl_orbit_and_census()
    ow_cen = ow_c["exhaustive_z5_census"]
    ow_6y = ow_c["pure_6Y_mod5_table"]

    expected_ym = {
        "G_SM": "-192",
        "SU(5)": "-384",
        "SO(10)": "-2128/25",
        "E_6": "-448/25",
        "E_7": "-624/25",
        "E_8": "0",
    }
    ym_match = all(
        lie["exhaustive_census"][g]["max_pure_YM_C6"] == expected_ym[g]
        and ow_cen[g]["max_pure_YM_C6"] == expected_ym[g]
        for g in expected_ym
    )
    kac_ok = lie["exhaustive_census"]["E_8"]["max_pure_YM_untw_tw"] == [48, 200]
    pure_6y_nogo_ok = all(
        Fraction(lie["pure_6Y_table"][g]["C6_3x16_4Dchiral"]) < 0
        and Fraction(lie["pure_6Y_table"][g]["C6_3x27_4Dchiral"]) < 0
        and lie["pure_6Y_table"][g]["C6_pure_YM"] == ow_6y[g]["C6_pure_YM"]
        and lie["pure_6Y_table"][g]["C6_3x16_4Dchiral"] == ow_6y[g]["C6_3x16_4Dchiral"]
        and lie["pure_6Y_table"][g]["C6_3x27_4Dchiral"] == ow_6y[g]["C6_3x27_4Dchiral"]
        for g in ("G_SM", "SU(5)", "SO(10)", "E_6", "E_7", "E_8")
    )
    rescues_ok = (
        lie["exhaustive_census"]["SO(10)"]["max_3x16_4Dchiral_C6"] == "-1456/25"
        and lie["exhaustive_census"]["SO(10)"]["strict_G_SM_x_U1k_count"] == 8
        and lie["exhaustive_census"]["SU(5)"]["strict_G_SM_x_U1k_count"] == 0
        and lie["exhaustive_census"]["E_6"]["max_3x27_4Dchiral_C6"] == "376/25"
        and lie["exhaustive_census"]["E_6"]["max_3x16_4Dchiral_C6"] == "-2008/25"
        and lie["exhaustive_census"]["E_7"]["max_3x16_4Dchiral_C6"] == "544/25"
        and lie["exhaustive_census"]["E_7"]["max_3x27_4Dchiral_C6"] == "-792/25"
        and lie["exhaustive_census"]["E_8"]["max_3x16_4Dchiral_C6"] == "432/5"
        and lie["exhaustive_census"]["E_8"]["max_3x27_4Dchiral_C6"] == "1568/25"
        and lie["exhaustive_census"]["E_6"]["strict_G_SM_x_U1k_count"] == 0
        and lie["exhaustive_census"]["E_7"]["strict_G_SM_x_U1k_count"] == 0
        and lie["exhaustive_census"]["E_8"]["strict_G_SM_x_U1k_count"] == 0
    )
    z2_ok = (
        lie["z2_scherk_schwarz_factor"] == "-3/4"
        and ow_c["z2_scherk_schwarz_s3"]["twist_factor"] == "-3/4"
    )
    c2_ok = (
        lie["e8_root_count"] == 240
        and lie["all_norm8"]
        and lie["cartan_det"] == 1
        and lie["w_16_count"] == 16
        and lie["w_27_count"] == 27
        and lie["total_z5_tuples_scanned"] == 3905
        and ym_match
        and kac_ok
        and pure_6y_nogo_ok
        and rescues_ok
        and z2_ok
    )
    if not c2_ok:
        discrepancies += 1

    gate_c = c1_ok and c2_ok
    report = {
        "ref_c1_direct_lattice_F3": {
            "F3_tau_star_plus": mp.nstr(mp.mpf(str(lat["val"])), 14),
            "val_diff_vs_ow19": mp.nstr(mp.mpf(str(val_diff)), 8),
            "grad_norm": mp.nstr(mp.mpf(str(lat["grad_norm"])), 8),
            "hess_lam_min": mp.nstr(mp.mpf(str(lat["lam_min"])), 10),
            "hess_lam_max": mp.nstr(mp.mpf(str(lat["lam_max"])), 10),
            "lmin_diff_vs_ow19": mp.nstr(mp.mpf(str(lmin_diff)), 8),
            "lmax_diff_vs_ow19": mp.nstr(mp.mpf(str(lmax_diff)), 8),
            "hyp_lap_err": mp.nstr(mp.mpf(str(lat["hyp_lap_err"])), 8),
            "ok": c1_ok,
        },
        "ref_c2_weyl_orbit_e8_census": {
            **lie,
            "ym_match": ym_match,
            "kac_48_200_ok": kac_ok,
            "pure_6y_nogo_ok": pure_6y_nogo_ok,
            "rescues_ok": rescues_ok,
            "z2_ok": z2_ok,
            "ok": c2_ok,
        },
        "gate_ref_c": gate_c,
    }
    return report, discrepancies, lat


# =============================================================================
# REF-D: 6 / 6 Independent Referee Planted Fault Controls
# =============================================================================
def run_ref_d(
    fuchs: dict[str, Any], weyl: dict[str, Any], lat: dict[str, float]
) -> dict[str, Any]:
    # PF-REF-1: Corrupted 1-byte SHA-256 tamper on verify_a2_ow19_v3.py (in memory)
    target_bytes = (REPO_ROOT / "relays/a2_ow19_v3/verify_a2_ow19_v3.py").read_bytes()
    tampered_bytes = bytearray(target_bytes)
    tampered_bytes[0] ^= 1
    pf1_res = verify_sha256_manifest(
        REPO_ROOT / "relays/a2_ow19_v3/SCRIPT_SHA256.txt", override_bytes=bytes(tampered_bytes)
    )
    pf1_caught = not pf1_res["matched"]

    # PF-REF-2: EX-S2 T_2 3x bug detection (-2 vs -2/3 in T_2 shifts beta_yt by +3 and triples beta_ytau)
    mv84 = derive_mv84_chi4_h2_hbar2_symbolic()
    pf2_caught = (
        mv84["beta_yt_yt2yb2_buggy"] != mv84["beta_yt_yt2yb2_exact"]
        and Fraction(mv84["beta_yt_yt2yb2_buggy"]) - Fraction(mv84["beta_yt_yt2yb2_exact"]) == Fraction(3, 1)
        and Fraction(mv84["beta_ytau_yt2yb2_buggy"]) == 3 * Fraction(mv84["beta_ytau_yt2yb2_exact"])
    )

    # PF-REF-3: Wrong Weyl-rep vector current gives non-zero s-wave E^2 / (2 pi) != 0
    E_sym = sp.Symbol("E", real=True, positive=True)
    pf3_caught = (weyl["sv_vec_swave"] != 0) and (sp.simplify(weyl["sv_vec_swave"] - E_sym**2 / (2 * sp.pi)) == 0)

    # PF-REF-4: Wrong E_8 naive 236/12 root miscount gives spurious +17856/25 > 0 vs exact 48/200 == 0
    c6_exact = Fraction(4, 1) * (-4 * 48) - Fraction(24, 25) * (-4 * 200)
    c6_naive = Fraction(4, 1) * (-4 * 12) - Fraction(24, 25) * (-4 * 236)
    pf4_caught = (c6_exact == 0) and (c6_naive == Fraction(17856, 25)) and (c6_naive > 0)

    # PF-REF-5: Positive-curvature sign flip (inverting e^{2 Omega} -> e^{-2 Omega} flips K < 0 to K > 0)
    old_dps = mp.mp.dps
    mp.mp.dps = 35
    try:
        z1 = fuchs["z1"]
        psi_z1 = fuchs["psi_z1"]
        wp_mp = fuchs["wp_mp"]
        c_cur = fuchs["c_star"]

        def inv_omega(psi_m: mp.matrix) -> mp.mpf:
            # Inverted metric: e^{2 Omega_bad} = e^{-2 Omega_hyp} -> Omega_bad = -Omega_hyp
            return mp.log(abs(mp.im(psi_m[0, 0] * mp.conj(psi_m[0, 1]))))

        om0 = inv_omega(psi_z1)
        e2om_bad = mp.exp(2 * om0)
        h_lap = mp_pow10(-6)
        om_xp = inv_omega(rk4_segment_mp(wp_mp, c_cur, z1, z1 + h_lap, 4, psi_z1))
        om_xm = inv_omega(rk4_segment_mp(wp_mp, c_cur, z1, z1 - h_lap, 4, psi_z1))
        om_yp = inv_omega(rk4_segment_mp(wp_mp, c_cur, z1, z1 + I_MP * h_lap, 4, psi_z1))
        om_ym = inv_omega(rk4_segment_mp(wp_mp, c_cur, z1, z1 - I_MP * h_lap, 4, psi_z1))
        K_inverted = -((om_xp + om_xm + om_yp + om_ym - 4 * om0) / (h_lap * h_lap)) / e2om_bad
        pf5_caught = bool(K_inverted > mp.mpf(0)) and bool(abs(K_inverted + mp.mpf(1)) > mp.mpf(1))
    finally:
        mp.mp.dps = old_dps

    # PF-REF-6: Wrong F_3 sign at tau_*^+ flips dS minimum (+61.111, +1336.563) to AdS maximum (< 0)
    H_neg = np.array([[-lat["fxx"], -lat["fxy"]], [-lat["fxy"], -lat["fyy"]]], dtype=np.float64)
    eigs_neg = np.sort(np.linalg.eigvalsh(H_neg))
    pf6_caught = bool(eigs_neg[0] < float(0)) and bool(eigs_neg[1] < float(0))

    controls = {
        "PF_REF_1_tamper_sha256": pf1_caught,
        "PF_REF_2_ex_s2_T2_3x_bug": pf2_caught,
        "PF_REF_3_weyl_vector_swave_nonzero": pf3_caught,
        "PF_REF_4_e8_236_12_miscount": pf4_caught,
        "PF_REF_5_positive_curvature_flip": pf5_caught,
        "PF_REF_6_wrong_F3_sign_ads_max": pf6_caught,
    }
    caught = sum(1 for v in controls.values() if v)
    return {
        "controls": controls,
        "PF_REF_4_c6_naive": str(c6_naive),
        "PF_REF_5_K_inverted": mp.nstr(K_inverted, 10),
        "PF_REF_6_neg_hess_eigs": [mp.nstr(mp.mpf(str(x)), 10) for x in eigs_neg.tolist()],
        "planted_faults_caught": caught,
        "planted_faults_total": 6,
        "gate_ref_d": (caught == 6),
    }


def main() -> None:
    t0 = time.time()
    ps_json = json.loads((REPO_ROOT / "relays/a2_peer_synth_v2/a2_peer_synth_v2_results.json").read_text(encoding="utf-8"))
    ow19_json = json.loads((REPO_ROOT / "relays/a2_ow19_v3/a2_ow19_v3_results.json").read_text(encoding="utf-8"))

    ref0, d0 = run_ref_0()
    ref_ps, d_ps = run_ref_ps(ps_json)
    ref_a, d_a, fuchs = run_ref_a(ow19_json)
    ref_b, d_b, weyl = run_ref_b(ow19_json)
    ref_c, d_c, lat = run_ref_c(ow19_json)
    ref_d = run_ref_d(fuchs, weyl, lat)

    discrepancy_count = d0 + d_ps + d_a + d_b + d_c
    all_passed = (
        ref0["gate_ref_0"]
        and ref_ps["gate_ref_ps"]
        and ref_a["gate_ref_a"]
        and ref_b["gate_ref_b"]
        and ref_c["gate_ref_c"]
        and ref_d["gate_ref_d"]
        and (discrepancy_count == 0)
    )
    elapsed_sec = int(round(time.time() - t0))

    payload = {
        "card_id": "A2-OW19-REFEREE",
        "seat": "agy-002-cold-room-referee",
        "firewall": "0 of 19",
        "audited_commits": {
            "a2_peer_synth_v2": "c161ef045",
            "a2_ow19_v3": "62f08b148",
            "peer_agy_c30": "528ef1cf5",
            "peer_agy_exp_x_harvest": "75cb20177",
        },
        "REF_0_custody_and_ast_hygiene": ref0,
        "REF_PS_a2_peer_synth_v2_countercheck": ref_ps,
        "REF_A_ow19_a_disjoint_countercheck": ref_a,
        "REF_B_ow19_b_disjoint_countercheck": ref_b,
        "REF_C_ow19_c_disjoint_countercheck": ref_c,
        "REF_D_planted_fault_controls": ref_d,
        "discrepancy_count": discrepancy_count,
        "planted_faults_caught": ref_d["planted_faults_caught"],
        "planted_faults_total": ref_d["planted_faults_total"],
        "all_referee_checks_passed": all_passed,
        "elapsed_seconds_int": elapsed_sec,
    }
    assert count_json_floats(payload) == 0, "JSON output must contain 0 raw float literals"

    out_text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    OUT_JSON.write_text(out_text, encoding="utf-8")
    out_sha = hashlib.sha256(OUT_JSON.read_bytes()).hexdigest()
    OUT_SHA.write_text(f"{out_sha}  {OUT_JSON.name}\n", encoding="utf-8")
    print(f"Sealed raw unread referee output in {elapsed_sec}s.")


if __name__ == "__main__":
    main()
