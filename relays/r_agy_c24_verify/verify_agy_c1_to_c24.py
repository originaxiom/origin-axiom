#!/usr/bin/env python3
"""
Standalone preregistered zero-shared-code verifier for Card R-AGY-C24 (0 of 19, data-free).

Independently checks mathematical-physics, topological, QFT, custody, and quotation claims
of origin/agy/cusp-action-2026-11-20 (AGY-C1 through AGY-C24 at commit 6f285488c) across
seven pure-mathematical / QFT modules and six planted adversarial controls (PC_RAGY_1..6):

  M0  AST zero-float self-check + git custody, SHA-256 manifest, post-add edit count,
      broken path-ref scan, and exact machine-verified line quotations at 6f285488c.
  M1  Full 248-dimensional E_8 root/Cartan parity check under v_P = (0,0,0,1/2,1/2,0,0,0)
      on (10,6) subset E_8 (n_H = 12, slope 98/85 != 9/5, unbroken dim 136 = dim so(16))
      + PC_RAGY_1.
  M2  Mp(2,Z) spinoriality (U_S^4 = -I_3, det U_T != 1), G_T (order 96) meridian orders on
      pi_1(X_{4_1}), D_10 meridian parity trivialization P^m = +I_5 for even m in {2,8,40},
      longitude degree-1 kernel dim 1 != 3, and pillowcase order 2 != 4 + PC_RAGY_2.
  M3  Coordinate-free 55-digit V_{Gamma_0(5)} stationarity & Hessian window (vs r = 5 saddle,
      PC_RAGY_3), C16 5-cell bulk SU(2)_L doublet link-mass non-invariance, L_2 = 5/2 vs
      interpolated L_2 discrepancy (3.65%), and raw m = 8 arg det(Y_u Y_d) != 0 Strong-CP check.
  M4  Machacek-Vaughn 2-loop Type-II 2HDM pure-top beta (-12 vs -21/4), xi = 0 EWSB failure,
      26-decade v_EW^2 / mu_IR^2 scale offset, and linearized vs Newton tan(beta) mismatch
      + PC_RAGY_4.
  M5  Covi-Roulet-Vissani / Davidson-Nardi-Nir resonant flavored leptogenesis loop sign
      (1 - x) vs +(x - 1): symbolic large-x limit, 15.09x eps_{1,tau} inflation, sign flip of
      eps_tot(tau_*^+) and washout-weighted Y_B(tau_*^+) < 0, and 2HDM 8/23 sphaleron factor
      + PC_RAGY_5.
  M6  2I subset SU(2) non-crystallographic R^4 trace 1 + sqrt(5), 2T Hurwitz lattice index 2,
      and AGY-C24 pre-registered N = 120 vs N = 240 step-halving F2 failure (> 10^-7)
      + PC_RAGY_6.

Zero float literals appear anywhere in this file (enforced by AST inspection).
Zero measured values or held-out empirical targets are used or compared (0 of 19).
"""

from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
import itertools
import json
import math
import pathlib
import subprocess
from typing import Any, Dict, List, Sequence, Tuple

import mpmath as mp
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
OUT_PATH = HERE / "verify_agy_c1_to_c24_out.json"
OUT_SHA_PATH = HERE / "OUTPUT_SHA256.txt"
TARGET_COMMIT = "6f285488c49f4bec5354b20df14c9240aa88a009"
MERGE_BASE_COMMIT = "60a52d35959b7d6cd2008b1a23f0d365a8584208"

mp.mp.dps = 55


# ============================================================================
# Helper: Enforce Zero Float Literals in AST & Zero Floats in Output JSON
# ============================================================================

def enforce_zero_float_literals_ast() -> Dict[str, Any]:
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(__file__))
    float_lines: List[int] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            float_lines.append(getattr(node, "lineno", -1))
    return {
        "float_literal_count": len(float_lines),
        "float_literal_lines": float_lines,
        "zero_float_literals_passed": len(float_lines) == 0,
    }


def assert_no_json_floats(obj: Any, path: str = "root") -> None:
    if isinstance(obj, float):
        raise ValueError(f"Forbidden float in JSON output at {path}: {obj}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_json_floats(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for idx, v in enumerate(obj):
            assert_no_json_floats(v, f"{path}[{idx}]")


def frac_to_mp(q: Fraction) -> mp.mpf:
    return mp.mpf(q.numerator) / mp.mpf(q.denominator)


# ============================================================================
# Standalone Special Functions & Matrix Utilities (Zero Shared Code)
# ============================================================================

def eta_pentagonal(tau: mp.mpc) -> mp.mpc:
    im = mp.mpc(0, 1)
    y = mp.im(tau)
    n_lim = int(mp.ceil(mp.sqrt(mp.mpf(mp.mp.dps * 10) / (mp.pi * y)))) + 12
    acc = mp.mpc(0)
    for k in range(-n_lim, n_lim + 1):
        term = mp.exp(2 * im * mp.pi * tau * (mp.mpf(3 * k * k - k) / 2))
        acc += -term if (k % 2 != 0) else term
    return mp.exp(im * mp.pi * tau / 12) * acc


def theta_series_char(a: Fraction, b: Fraction, tau: mp.mpc, z: mp.mpc = mp.mpc(0)) -> mp.mpc:
    im = mp.mpc(0, 1)
    am = frac_to_mp(a)
    bm = frac_to_mp(b)
    y = mp.im(tau)
    n_lim = int(mp.ceil(mp.sqrt(mp.mpf(mp.mp.dps * 4) / (mp.pi * y)))) + 14
    acc = mp.mpc(0)
    for n in range(-n_lim, n_lim + 1):
        na = mp.mpf(n) + am
        acc += mp.exp(im * mp.pi * (na * na) * tau + 2 * im * mp.pi * na * (z + bm))
    return acc


def theta1_log_deriv(z: mp.mpc, tau: mp.mpc) -> mp.mpc:
    im = mp.mpc(0, 1)
    y = mp.im(tau)
    m_shift = int(mp.nint(-mp.im(z) / y))
    zr = z + mp.mpf(m_shift) * tau
    q = mp.exp(2 * im * mp.pi * tau)
    res = mp.pi * mp.cot(mp.pi * zr) + 2 * im * mp.pi * mp.mpf(m_shift)
    qn = q
    k_lim = int(mp.ceil(mp.mpf(mp.mp.dps * 3) / (mp.pi * y))) + 14
    for n in range(1, k_lim + 1):
        res += 4 * mp.pi * (qn / (1 - qn)) * mp.sin(2 * mp.pi * mp.mpf(n) * zr)
        qn *= q
    return res


def kronecker_fu(u1: Fraction, u2: Fraction, tau: mp.mpc) -> mp.mpf:
    im = mp.mpc(0, 1)
    af = u1 - Fraction(math.floor(u1))
    bf = u2 - Fraction(math.floor(u2))
    am, bm = frac_to_mp(af), frac_to_mp(bf)
    x, y = mp.re(tau), mp.im(tau)
    k_lim = int(mp.ceil(mp.mpf(mp.mp.dps * 3) / (2 * mp.pi * y))) + 12
    osc = mp.mpf(0)
    for m in range(-k_lim, k_lim + 1):
        ma = mp.mpf(m) + am
        if ma == 0:
            continue
        w = mp.exp(-2 * mp.pi * abs(ma) * y + 2 * im * mp.pi * (ma * x + bm))
        osc += (2 * mp.pi / abs(ma)) * mp.re(w / (1 - w))
    if af == 0:
        return (
            mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
            + y * (mp.pi**2) / (mp.sin(mp.pi * bm) ** 2)
            + osc
        )
    pn, qd = af.numerator, af.denominator
    g_sum = mp.fsum(
        mp.cos(2 * mp.pi * mp.mpf(pn * k) / mp.mpf(qd))
        * mp.log(2 * mp.sin(mp.pi * mp.mpf(k) / mp.mpf(qd)))
        for k in range(1, qd)
    )
    return -mp.pi * (2 * mp.log(2) + mp.log(y) - 2 * mp.euler - 2 * mp.log(qd) + 2 * g_sum) + osc


def standalone_yukawa_matrix(
    tau: mp.mpc, a: Fraction, b: Fraction, ql: int, qr: int, l2_val: mp.mpf
) -> mp.matrix:
    im = mp.mpc(0, 1)
    half = Fraction(1, 2)
    z0 = Fraction(0, 1)
    eta_v = eta_pentagonal(tau)
    t1p = 2 * mp.pi * (eta_v**3)
    th2 = theta_series_char(half, z0, tau)
    th3 = theta_series_char(z0, z0, tau)
    th4 = theta_series_char(z0, half, tau)
    denom = 24 * (eta_v**3)
    c0 = -(th2**2) * (th3**4 + th4**4) / denom
    c1 = +(th4**2) * (th2**4 + th3**4) / denom
    c2 = im * (th3**2) * (th2**4 - th4**4) / denom
    x0, x1 = ql * a, 2 * ql * b
    y0, y1 = qr * a, 2 * qr * b
    ap, am = x0 + y0, x0 - y0
    bp, bm = (x1 + y1) / 2, (x1 - y1) / 2
    ep = mp.exp(-2 * im * mp.pi * frac_to_mp(x0))
    kap = {"1": -im * ep, "i": mp.mpc(-1), "j": -ep, "k": im}
    cs = {"1": (ap + half, bp + half), "i": (ap + half, bp), "j": (ap, bp + half), "k": (ap, bp)}
    ds = {"1": (am + half, bm + half), "i": (am + half, bm), "j": (am, bm + half), "k": (am, bm)}
    c_shift = 2 * mp.pi * l2_val + mp.pi * mp.log(mp.im(tau)) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    em2l = mp.exp(-2 * l2_val)
    u_chan: Dict[str, mp.mpc] = {}
    for s_key in ("1", "i", "j", "k"):
        al, be = cs[s_key][0] - half, cs[s_key][1] - half
        dal, dbe = ds[s_key][0] - half, ds[s_key][1] - half
        if (al.denominator == 1 and be.denominator == 1) or (dal.denominator == 1 and dbe.denominator == 1):
            u_chan[s_key] = mp.mpc(0)
            continue
        rv = kap[s_key] * theta_series_char(cs[s_key][0], cs[s_key][1], tau) * theta_series_char(ds[s_key][0], ds[s_key][1], tau) / t1p
        a0_sq = abs(2 * im * mp.pi * frac_to_mp(al) + theta1_log_deriv(frac_to_mp(al) * tau + frac_to_mp(be), tau)) ** 2
        rad = c_shift + kronecker_fu(al, be, tau) - mp.pi * a0_sq * em2l
        u_chan[s_key] = mp.sqrt(rad) * rv if rad > 0 else mp.mpc(0)
    h_vec = [c1, c0, c2]
    u_vec = [u_chan["j"], u_chan["i"], u_chan["k"]]
    w0 = -u_chan["1"]
    uh = sum(u_vec[k] * h_vec[k] for k in range(3))
    hx = mp.matrix([[0, -h_vec[2], h_vec[1]], [h_vec[2], 0, -h_vec[0]], [-h_vec[1], h_vec[0], 0]])
    ym = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            ym[r, c] = u_vec[r] * h_vec[c] + h_vec[r] * u_vec[c] - (uh if r == c else 0) + w0 * hx[r, c]
    return ym


def herm_log_mp(g_mat: mp.matrix) -> mp.matrix:
    evs, u_mat = mp.eighe((g_mat + g_mat.H) / 2)
    return u_mat * mp.diag([mp.log(x) for x in evs]) * u_mat.H


def herm_exp_mp(l_mat: mp.matrix) -> mp.matrix:
    evs, u_mat = mp.eighe((l_mat + l_mat.H) / 2)
    return u_mat * mp.diag([mp.exp(x) for x in evs]) * u_mat.H


def svd_asc_mp(ym: mp.matrix) -> Tuple[mp.matrix, List[mp.mpf]]:
    u_m, sv_m, _ = mp.svd_c(ym)
    order = sorted(range(3), key=lambda k: sv_m[k])
    u_ord = mp.matrix([[u_m[r, order[c]] for c in range(3)] for r in range(3)])
    return u_ord, [sv_m[order[c]] for c in range(3)]


# ============================================================================
# Module M0: Git Custody, SHA-256 Manifests, & Exact Line Quote Verification
# ============================================================================

QUOTES_TO_CHECK: List[Tuple[str, int, str]] = [
    (
        "relays/AGY_TO_MAIN_2026-11-20_CHIRAL_HOLOMORPHIC_CUSP_BOUNDARY_SYNTHESIS.md",
        3,
        "hashed script before execution",
    ),
    (
        "relays/AGY_TO_MAIN_2026-11-20_CHIRAL_HOLOMORPHIC_CUSP_BOUNDARY_SYNTHESIS.md",
        11,
        "from one uniform `30 x 30` Weyl collar operator via `G_{SM}` conservation",
    ),
    (
        "relays/AGY_TO_MAIN_2026-11-20_C1_P879_RANK1_OBSTRUCTION_AND_HOLOMORPHIC_DOUBLETS.md",
        18,
        "exceeds `993 / 1000` at height `six`, `99997 / 100000` at height `fifteen`, and `1` at height `thirty`.",
    ),
    (
        "relays/agy_2026-11-20_c3/c3_cusp_three_family_gluing.py",
        382,
        "np.kron(gT, np.eye(5)) @ np.kron(np.eye(3), gW) - np.kron(np.eye(3), gW) @ np.kron(gT, np.eye(5))",
    ),
    (
        "relays/AGY_TO_MAIN_2026-11-20_C4_SPECTRAL_POTENTIAL_CUSP_CANCELLATION_AND_STATIONARITY.md",
        25,
        "selecting a net bosonic-minus-fermionic sign",
    ),
    (
        "relays/agy_2026-11-20_c5/c5_countercheck.py",
        291,
        'uu40, wu40 = uw_triple_mp(t40, Fr(1, 5), Fr(2, 5), 1, -4, mp.mpf("2.2505"))',
    ),
    (
        "relays/agy_2026-11-20_c6/c6_countercheck.py",
        109,
        "n_cusps_wang = 1",
    ),
    (
        "relays/agy_2026-11-21_c9/c9_cover_scaling_and_anomaly_inflow.py",
        265,
        "i8_three_27 = sp.expand(3 * (27 * a8_grav_unit + tr_r2 * (3 * tr_f2) / 96 + sp.Rational(3, 4) * (tr_f2 ** 2) / 24))",
    ),
    (
        "relays/agy_2026-11-21_c14/c14_2loop_2hdm_rge_and_tan_beta.py",
        175,
        "g_ir, yu_ir, _, _, _, _ = rk4_integrate(st0_pr, t_end=t_end, n_steps=4000, two_loop=False)",
    ),
    (
        "relays/AGY_TO_MAIN_2026-11-21_C15_END_TO_END_UV_IR_PIPELINE_AND_BIT_LEDGER.md",
        9,
        "|G_T| = 96",
    ),
    (
        "relays/agy_2026-11-21_c16/c16_five_cell_collar_kaplan_derivation.py",
        70,
        "m_kk = mp.sqrt(tr_g) / eps",
    ),
    (
        "relays/agy_2026-11-21_c18/c18_blind_prediction_seal_and_matched_null.py",
        166,
        "(evn[1] - evn[0]) / (evn[2] - evn[0]), mp.mpf(0), (ia[0] - ia[1]) / (ia[1] - ia[2]), tb,",
    ),
    (
        "relays/agy_2026-11-21_c21/c21_level40_cusp_coercivity_and_instanton_saddle.py",
        100,
        "wrap_amp = mp.mpf(0) if r_cutoff_wrap is None else mp.exp(-2 * r_cutoff_wrap)",
    ),
    (
        "relays/agy_2026-11-21_c22/c22_countercheck.py",
        163,
        'm11_over_mpl_sd = mp.mpf("3.93863908") / mp.mpf("25.491212")',
    ),
    (
        "relays/agy_2026-11-21_c23/c23_cosmology_vacuum_dm_leptogenesis_inflation.py",
        369,
        "f_sv = mp.sqrt(x) * ((x - 1) / reg_denom + 1 - (1 + x) * mp.log(1 + 1 / x))",
    ),
    (
        "relays/agy_2026-11-21_c23/c23_countercheck.py",
        143,
        "f_sv = mp.sqrt(x) * ((x - 1) / den + 1 - (1 + x) * mp.log(1 + 1 / x))",
    ),
    (
        "relays/cards/AGY_C24_pole-matching-and-full-toe-seal-v2.md",
        7,
        "`N = 120` vs `N = 240` step-halving residual `< 10^{-7}`",
    ),
    (
        "relays/agy_2026-11-21_c24/c24_pole_matching_and_full_toe_seal_v2.py",
        178,
        "out_120 = eval_full_toe_pipeline(n_steps=180, dps=42)",
    ),
    (
        "relays/agy_2026-11-21_c24/c24_countercheck.py",
        2,
        "Disjoint Kutta 3/8-Rule Pole/2HDM Spectrum Verifier, Cayley-Haar Single-Arm Null,",
    ),
    (
        "relays/STATUS_AGY.md",
        20,
        "`docs/seats/README`",
    ),
]


def run_module_m0_git_and_quotes() -> Dict[str, Any]:
    chk = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "cat-file", "-e", f"{TARGET_COMMIT}^{{commit}}"],
        capture_output=True,
    )
    if chk.returncode != 0:
        return {"commit_present_in_git": False, "target_commit": TARGET_COMMIT}

    ls_out = subprocess.check_output(
        ["git", "-C", str(REPO_ROOT), "ls-tree", "-r", "--name-only", TARGET_COMMIT, "relays"],
        text=True,
    ).splitlines()
    sha_files = sorted(p for p in ls_out if p.endswith("SCRIPT_SHA256.txt"))
    sha_ok = 0
    for sf in sha_files:
        parent_dir = str(pathlib.PurePosixPath(sf).parent)
        raw = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "show", f"{TARGET_COMMIT}:{sf}"], text=True
        )
        entries_ok = True
        for line in raw.strip().splitlines():
            parts = line.strip().split()
            if len(parts) >= 2:
                exp_h, fname = parts[0], parts[-1]
                fname_clean = pathlib.PurePosixPath(fname).name
                blob = subprocess.check_output(
                    ["git", "-C", str(REPO_ROOT), "show", f"{TARGET_COMMIT}:{parent_dir}/{fname_clean}"]
                )
                if hashlib.sha256(blob).hexdigest() != exp_h:
                    entries_ok = False
        if entries_ok:
            sha_ok += 1

    # Count post-addition file modifications across MERGE_BASE..TARGET_COMMIT under relays/agy_2026-*
    log_raw = subprocess.check_output(
        [
            "git",
            "-C",
            str(REPO_ROOT),
            "log",
            "--reverse",
            "--name-status",
            "--format=COMMIT:%h",
            f"{MERGE_BASE_COMMIT}..{TARGET_COMMIT}",
            "--",
            "relays",
        ],
        text=True,
    ).splitlines()
    post_add_mods = 0
    c19_run_overwritten = False
    cur_h = ""
    for ln in log_raw:
        if ln.startswith("COMMIT:"):
            cur_h = ln.split(":", 1)[1].strip()
        elif ln.startswith("M\trelays/agy_2026-"):
            post_add_mods += 1
            if "c19_e8_unimodular_spin_fork_and_s2_run.txt" in ln:
                c19_run_overwritten = True

    quote_checks: List[Dict[str, Any]] = []
    all_quotes_exact = True
    for rel_p, line_no, needle in QUOTES_TO_CHECK:
        txt = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "show", f"{TARGET_COMMIT}:{rel_p}"], text=True
        ).splitlines()
        actual_line = txt[line_no - 1] if 1 <= line_no <= len(txt) else ""
        matched = needle in actual_line
        if not matched:
            all_quotes_exact = False
        quote_checks.append(
            {
                "file": rel_p,
                "line": line_no,
                "matched": matched,
                "exact_line": actual_line,
            }
        )

    return {
        "commit_present_in_git": True,
        "target_commit": TARGET_COMMIT,
        "sha256_manifest_count": len(sha_files),
        "sha256_manifests_matching": sha_ok,
        "all_24_sha256_manifests_match": (len(sha_files) == 24 and sha_ok == 24),
        "post_addition_card_file_modifications": post_add_mods,
        "c19_committed_run_txt_overwritten_in_place": c19_run_overwritten,
        "quote_count": len(quote_checks),
        "all_quotes_exact": all_quotes_exact,
        "quotes": quote_checks,
    }


# ============================================================================
# Module M1: E_8 (10, 6) Parity & Unbroken Gauge Algebra (AGY-C2 & AGY-C5)
# ============================================================================

def run_module_m1_e8_10_6() -> Dict[str, Any]:
    roots: List[Tuple[Fraction, ...]] = []
    z0 = Fraction(0, 1)
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (-1, 1):
                for sj in (-1, 1):
                    vec = [z0] * 8
                    vec[i], vec[j] = Fraction(si, 1), Fraction(sj, 1)
                    roots.append(tuple(vec))
    for signs in itertools.product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(tuple(Fraction(s, 2) for s in signs))

    vp = (z0, z0, z0, Fraction(1, 2), Fraction(1, 2), z0, z0, z0)
    dot = lambda u, v: sum(x * y for x, y in zip(u, v))

    even_roots = [r for r in roots if dot(vp, r).denominator == 1]
    unbroken_gauge_dim = len(even_roots) + 8  # 128 + 8 = 136 = dim so(16)

    # (10, 6) roots: one +-1 in SO(10) coords 0..4 and one +-1 in SU(4)=SO(6) coords 5..7
    roots_10_6 = [
        r for r in roots if sum(abs(x) for x in r[:5]) == 1 and sum(abs(x) for x in r[5:]) == 1
    ]
    surviving_10_6 = [r for r in roots_10_6 if dot(vp, r).denominator == 2]
    nh_full_e8 = len(surviving_10_6) // 2  # 24 / 2 = 12 complex SU(2)_L doublets
    slope_full_e8 = Fraction(220 - 2 * nh_full_e8, 110 + 5 * nh_full_e8)  # 98/85

    # Planted Control PC_RAGY_1: slicing a single (10, 1) ignores the 6 of SU(4) -> n_H = 2, slope = 9/5
    single_10_weights = []
    for idx in range(5):
        for sgn in (-1, 1):
            w = [z0] * 8
            w[idx] = Fraction(sgn, 1)
            single_10_weights.append(tuple(w))
    surviving_single_10 = [w for w in single_10_weights if dot(vp, w).denominator == 2]
    nh_single_10 = len(surviving_single_10) // 2  # 2
    slope_single_10 = Fraction(220 - 2 * nh_single_10, 110 + 5 * nh_single_10)  # 9/5

    pc1_caught = (nh_full_e8 == 12) and (nh_single_10 == 2) and (slope_full_e8 != slope_single_10)
    return {
        "e8_root_count": len(roots),
        "unbroken_gauge_dim_under_vP": unbroken_gauge_dim,
        "equals_dim_so16_136": unbroken_gauge_dim == 136,
        "roots_in_10_6": len(roots_10_6),
        "surviving_scalar_weights_in_10_6": len(surviving_10_6),
        "n_H_full_e8": nh_full_e8,
        "slope_full_e8_rational": f"{slope_full_e8.numerator}/{slope_full_e8.denominator}",
        "n_H_single_10_slice": nh_single_10,
        "slope_single_10_slice": f"{slope_single_10.numerator}/{slope_single_10.denominator}",
        "differs_from_agy_c5_two_doublet_claim": nh_full_e8 != 2,
        "PC_RAGY_1_caught": pc1_caught,
    }


# ============================================================================
# Module M2: Mp(2,Z) Spinoriality & X_{4_1}^(m) Cover Obstructions (C3 & C6)
# ============================================================================

def run_module_m2_covers_and_mp2z() -> Dict[str, Any]:
    # Monomial representation over Z/8Z (zeta_8 = exp(i*pi/4)):
    # Element = (perm_tuple, exp_mod8_tuple) where (M v)_i = zeta_8^{exp[i]} * v_{perm[i]}
    idt_m = ((0, 1, 2), (0, 0, 0))
    ut_m = ((0, 2, 1), (1, 1, 5))  # R_0 -> z8 R_0, R_1 -> z8 R_2, R_2 -> z8^5 R_1
    us_m = ((1, 0, 2), (1, 1, 1))  # R_0 -> z8 R_1, R_1 -> z8 R_0, R_2 -> z8 R_2

    def mul_m(a: Tuple[Tuple[int, ...], Tuple[int, ...]], b: Tuple[Tuple[int, ...], Tuple[int, ...]]):
        pa, ea = a
        pb, eb = b
        p_out = tuple(pb[pa[i]] for i in range(3))
        e_out = tuple((ea[i] + eb[pa[i]]) % 8 for i in range(3))
        return (p_out, e_out)

    def inv_m(a: Tuple[Tuple[int, ...], Tuple[int, ...]]):
        pa, ea = a
        pinv = [0, 0, 0]
        einv = [0, 0, 0]
        for i in range(3):
            pinv[pa[i]] = i
        for j in range(3):
            einv[j] = (-ea[pinv[j]]) % 8
        return (tuple(pinv), tuple(einv))

    def pow_m(a: Tuple[Tuple[int, ...], Tuple[int, ...]], k: int):
        res = idt_m
        for _ in range(k):
            res = mul_m(res, a)
        return res

    # Cross-check exact Z/8Z monomial matrices against 55-digit Jacobi theta evaluation of R(tau)
    im = mp.mpc(0, 1)
    half = Fraction(1, 2)
    z0 = Fraction(0, 1)
    tau_test = mp.mpc(mp.mpf(13) / 100, mp.mpf(7) / 5)

    def r_vec(t: mp.mpc) -> List[mp.mpc]:
        t2 = theta_series_char(half, z0, t)
        t3 = theta_series_char(z0, z0, t)
        t4 = theta_series_char(z0, half, t)
        d = t2 * t3 * t4
        return [-(t2 * t2) / d, -(t4 * t4) / d, im * (t3 * t3) / d]

    z8 = mp.exp(im * mp.pi / 4)

    def apply_m(elem, vec: List[mp.mpc]) -> List[mp.mpc]:
        p, e = elem
        return [(z8 ** e[i]) * vec[p[i]] for i in range(3)]

    rv0 = r_vec(tau_test)
    rv_t = r_vec(tau_test + 1)
    rv_s = [z8 * mp.sqrt(-im * tau_test) * x for x in r_vec(-1 / tau_test)]
    theta_err_t = max(abs(rv_t[i] - apply_m(ut_m, rv0)[i]) for i in range(3))
    theta_err_s = max(abs(rv_s[i] - apply_m(us_m, rv0)[i]) for i in range(3))

    us4 = pow_m(us_m, 4)
    us4_is_minus_id = us4 == ((0, 1, 2), (4, 4, 4))  # zeta_8^4 = -1

    # Enumerate finite group G_T = <U_T, U_S>
    gt_set = {idt_m}
    frontier = [idt_m]
    while frontier:
        nxt = []
        for g in frontier:
            for gen in (ut_m, us_m):
                prod = mul_m(g, gen)
                if prod not in gt_set:
                    gt_set.add(prod)
                    nxt.append(prod)
        frontier = nxt
    gt_list = sorted(gt_set)

    # Base Gamma' commutator [U_A, U_B] fixed-space dimension
    ut_inv, us_inv = inv_m(ut_m), inv_m(us_m)
    ua = mul_m(mul_m(mul_m(ut_m, us_inv), ut_m), us_m)
    ub = mul_m(mul_m(mul_m(ut_inv, us_m), ut_inv), us_inv)
    u_comm = mul_m(mul_m(ua, ub), mul_m(inv_m(ua), inv_m(ub)))
    # Diagonal entries where perm[i] == i and exp[i] == 0 give +1 eigenvalues:
    comm_fixed_dim = sum(1 for i in range(3) if u_comm[0][i] == i and u_comm[1][i] == 0)

    # Enumerate all homomorphisms pi_1(X_{4_1}) = <x, y | x y^-1 x^-1 y x = y x y^-1> -> G_T
    # (Wirtinger presentation of figure-eight knot complement: meridian = x)
    irred_reps = 0
    irred_meridian_orders = set()
    irred_m8_m40_max_ker = 0
    for gx in gt_list:
        gx_inv = inv_m(gx)
        for gy in gt_list:
            gy_inv = inv_m(gy)
            # Check Wirtinger relation: x * y^-1 * x^-1 * y * x == y * x * y^-1
            lhs = mul_m(mul_m(mul_m(mul_m(gx, gy_inv), gx_inv), gy), gx)
            rhs = mul_m(mul_m(gy, gx), gy_inv)
            if lhs != rhs:
                continue
            # Check irreducibility: subgroup generated by (gx, gy) acts transitively on {0,1,2}
            # AND is not scalar/1D-split (orbit of 0 under permutations has size 3)
            orb = {0}
            changed = True
            while changed:
                changed = False
                for g in (gx, gy):
                    for idx in list(orb):
                        if g[0][idx] not in orb:
                            orb.add(g[0][idx])
                            changed = True
            if len(orb) == 3:
                # Also verify no common eigenvector across (gx, gy): check trace inner product (1/|H|) sum |tr|^2 == 1
                sub = {idt_m}
                fr_h = [idt_m]
                while fr_h:
                    nh = []
                    for h in fr_h:
                        for gen in (gx, gy):
                            nh_el = mul_m(h, gen)
                            if nh_el not in sub:
                                sub.add(nh_el)
                                nh.append(nh_el)
                    fr_h = nh
                norm_sq = mp.mpf(0)
                for p_h, e_h in sub:
                    tr_h = sum((z8 ** e_h[i]) for i in range(3) if p_h[i] == i)
                    norm_sq += abs(tr_h) ** 2
                if abs(norm_sq / mp.mpf(len(sub)) - 1) < mp.mpf("1e-30"):
                    irred_reps += 1
                    ord_x = next(k for k in range(1, 97) if pow_m(gx, k) == idt_m)
                    irred_meridian_orders.add(ord_x)
                    for m_cov in (8, 40):
                        gm = pow_m(gx, m_cov)
                        # Count +1 eigenvalues of monomial matrix gm (cycle lengths: each cycle of length L with phase sum S contributes 1 iff S == 0 mod 8)
                        seen_c = set()
                        ker_d = 0
                        for st_i in range(3):
                            if st_i in seen_c:
                                continue
                            cur_i = st_i
                            ph_sum = 0
                            while cur_i not in seen_c:
                                seen_c.add(cur_i)
                                ph_sum = (ph_sum + gm[1][cur_i]) % 8
                                cur_i = gm[0][cur_i]
                            if ph_sum == 0:
                                ker_d += 1
                        irred_m8_m40_max_ker = max(irred_m8_m40_max_ker, ker_d)

    # Check all 20 surjections pi_1(X_{4_1}) ->> D_10: meridian has order 2 => P^m = id_5 for m in {2, 8, 40}
    els_d10 = [(s, c) for s in (1, -1) for c in range(5)]
    mul_d10 = lambda a, b: (a[0] * b[0], (a[0] * b[1] + a[1]) % 5)
    inv_d10 = lambda a: (a[0], (-a[0] * a[1]) % 5)
    idt_d10 = (1, 0)
    surj_d10 = 0
    all_even_covers_trivialize_P = True
    for dx in els_d10:
        dx_inv = inv_d10(dx)
        for dy in els_d10:
            dy_inv = inv_d10(dy)
            lhs_d = mul_d10(mul_d10(mul_d10(mul_d10(dx, dy_inv), dx_inv), dy), dx)
            rhs_d = mul_d10(mul_d10(dy, dx), dy_inv)
            if lhs_d != rhs_d:
                continue
            # Check surjectivity onto D_10
            sub_d = {idt_d10}
            fr_d = [idt_d10]
            while fr_d:
                nd = []
                for h in fr_d:
                    for gen in (dx, dy):
                        nx = mul_d10(h, gen)
                        if nx not in sub_d:
                            sub_d.add(nx)
                            nd.append(nx)
                fr_d = nd
            if len(sub_d) == 10:
                surj_d10 += 1
                for m_even in (2, 8, 40):
                    pm = idt_d10
                    for _ in range(m_even):
                        pm = mul_d10(pm, dx)
                    if pm != idt_d10:
                        all_even_covers_trivialize_P = False

    # Pillowcase spin lift hat_iota = (-i) * diag(+i, -i) = diag(+1, -1) has order 2 (not 4)
    i_sym = sp.I
    hat_iota = (-i_sym) * sp.diag(i_sym, -i_sym)
    pillow_order = next(k for k in range(1, 9) if hat_iota**k == sp.eye(2))

    # Planted Control PC_RAGY_2: universal Kronecker identity [A (x) I_5, I_3 (x) B] == 0 even when A^4 = -I_3
    a_us = sp.Matrix([[0, sp.exp(i_sym * sp.pi / 4), 0], [sp.exp(i_sym * sp.pi / 4), 0, 0], [0, 0, sp.exp(i_sym * sp.pi / 4)]])
    b_p = sp.diag(1, -1, -1, 1, 1)
    kron_comm = sp.kronecker_product(a_us, sp.eye(5)) * sp.kronecker_product(sp.eye(3), b_p) - sp.kronecker_product(sp.eye(3), b_p) * sp.kronecker_product(a_us, sp.eye(5))
    pc2_caught = (kron_comm == sp.zeros(15, 15)) and us4_is_minus_id

    return {
        "theta_check_max_err_lt_1e45": max(theta_err_t, theta_err_s) < mp.mpf("1e-45"),
        "U_S_fourth_power_is_minus_I3": us4_is_minus_id,
        "G_T_order_in_U3": len(gt_list),
        "base_commutator_fixed_dim": comm_fixed_dim,
        "irred_3d_reps_count": irred_reps,
        "irred_meridian_orders": sorted(irred_meridian_orders),
        "max_meridian_kernel_dim_at_m8_and_m40": irred_m8_m40_max_ker,
        "surjections_to_D10_count": surj_d10,
        "all_even_covers_m2_8_40_trivialize_meridian_parity_P": all_even_covers_trivialize_P,
        "pillowcase_hat_iota_exact_order": pillow_order,
        "PC_RAGY_2_caught": pc2_caught,
    }


# ============================================================================
# Module M3: V_{Gamma_0(5)} Saddle Window, C16 SU(2)_L Links, & Strong-CP
# ============================================================================

def run_module_m3_potential_collar_strong_cp() -> Dict[str, Any]:
    def v_gamma0_5(x_re: mp.mpf, y_im: mp.mpf, r_weight: mp.mpf) -> mp.mpf:
        t = mp.mpc(x_re, y_im)
        v1 = -mp.pi * mp.log(y_im * (abs(eta_pentagonal(t)) ** 4))
        v5 = -mp.pi * mp.log(5 * y_im * (abs(eta_pentagonal(5 * t)) ** 4))
        return (v1 + r_weight * v5) / 2

    x0 = mp.mpf(2) / 5
    y0 = mp.mpf(1) / 5
    h_step = mp.mpf("1e-12")

    def grad_and_det_hess(r_w: mp.mpf) -> Tuple[mp.mpf, mp.mpf, mp.mpf]:
        f00 = v_gamma0_5(x0, y0, r_w)
        fxp = v_gamma0_5(x0 + h_step, y0, r_w)
        fxm = v_gamma0_5(x0 - h_step, y0, r_w)
        fyp = v_gamma0_5(x0, y0 + h_step, r_w)
        fym = v_gamma0_5(x0, y0 - h_step, r_w)
        fpp = v_gamma0_5(x0 + h_step, y0 + h_step, r_w)
        fpm = v_gamma0_5(x0 + h_step, y0 - h_step, r_w)
        fmp = v_gamma0_5(x0 - h_step, y0 + h_step, r_w)
        fmm = v_gamma0_5(x0 - h_step, y0 - h_step, r_w)
        gx = (fxp - fxm) / (2 * h_step)
        gy = (fyp - fym) / (2 * h_step)
        hxx = (fxp - 2 * f00 + fxm) / (h_step * h_step)
        hyy = (fyp - 2 * f00 + fym) / (h_step * h_step)
        hxy = (fpp - fpm - fmp + fmm) / (4 * h_step * h_step)
        return mp.hypot(gx, gy), hxx + hyy, hxx * hyy - hxy * hxy

    gn1, tr1, det1 = grad_and_det_hess(mp.mpf(1))
    _, _, det_r5 = grad_and_det_hess(mp.mpf(5))
    pc3_caught = (det1 > 0) and (det_r5 < 0)

    # Symbolic 5-cell Kaplan Schur complement: bulk links (2,1) and (4,3) carry SU(2)_L doublets Q_2, Q_4
    yu_s, yd_s, m1, m2, m3, m4 = sp.symbols("y_u y_d M_1 M_2 M_3 M_4", positive=True)
    d5_sym = sp.Matrix(
        [
            [yu_s, 0, 0, 0, 0],
            [-m1, yu_s, 0, 0, 0],
            [0, -m2, yu_s, 0, 0],
            [0, 0, -m3, yu_s, 0],
            [0, 0, 0, -m4, yu_s],
        ]
    )
    # Schur complement of bottom-right 4x4 block onto (0,4) chiral mode:
    a_tl = sp.Matrix([[d5_sym[0, 4]]])
    b_tr = d5_sym[0, :4]
    c_bl = d5_sym[1:, 4]
    d_br = d5_sym[1:, :4]
    schur_eff = sp.simplify((a_tl - b_tr * d_br.inv() * c_bl)[0, 0])
    # Exact Schur identity: y_u^5 / (M_1 M_2 M_3 M_4); if SU(2)_L holds on bulk doublets, M_2(u)==M_2(d) and M_4(u)==M_4(d),
    # whereas AGY-C16 sets M_k(f) = sqrt(tr(Y_f^H Y_f))/eps so M_2(u)/M_2(d) = y_u/y_d != 1 when y_u != y_d!
    su2_bulk_link_ratio = sp.simplify(
        (sp.sqrt(3 * yu_s**2) / sp.sqrt(3 * yd_s**2)).subs({yu_s: 2, yd_s: 1})
    )

    # Raw m = 8 Strong-CP phases at p3 = (1/5, 2/5) and p4 = (1/6, 1/6) (both L_2 = 5/2 and grid-interpolated L_2)
    tau_m8 = mp.mpc(mp.mpf(16) / 5, mp.mpf(8) / 5)
    l2_rat = mp.mpf(5) / 2
    p3, p4 = (Fraction(1, 5), Fraction(2, 5)), (Fraction(1, 6), Fraction(1, 6))
    yu_p3 = standalone_yukawa_matrix(tau_m8, p3[0], p3[1], 1, -4, l2_rat)
    yd_p3 = standalone_yukawa_matrix(tau_m8, p3[0], p3[1], 1, 2, l2_rat)
    yu_p4 = standalone_yukawa_matrix(tau_m8, p4[0], p4[1], 1, -4, l2_rat)
    yd_p4 = standalone_yukawa_matrix(tau_m8, p4[0], p4[1], 1, 2, l2_rat)
    arg_p3 = mp.arg(mp.det(yu_p3 * yd_p3))
    arg_p4 = mp.arg(mp.det(yu_p4 * yd_p4))

    return {
        "v_gamma0_5_grad_norm_r1": mp.nstr(gn1, 6),
        "v_gamma0_5_det_hess_r1": mp.nstr(det1, 10),
        "v_gamma0_5_det_hess_r5_saddle": mp.nstr(det_r5, 10),
        "schur_5cell_formula": str(schur_eff),
        "su2_bulk_doublet_mass_ratio_for_yu2_yd1": str(su2_bulk_link_ratio),
        "su2_broken_when_tr_yu_neq_tr_yd": su2_bulk_link_ratio != 1,
        "raw_m8_strong_cp_arg_det_p3_rad": mp.nstr(arg_p3, 10),
        "raw_m8_strong_cp_arg_det_p4_rad": mp.nstr(arg_p4, 10),
        "raw_m8_strong_cp_nonzero": (abs(arg_p3) > mp.mpf("1e-1")) and (abs(arg_p4) > mp.mpf("1")),
        "PC_RAGY_3_caught": pc3_caught,
    }


# ============================================================================
# Shared Standalone Pipeline Builder for Modules M4, M5, M6
# ============================================================================

def selberg_prim_counts_up_to_4() -> Tuple[int, int]:
    # Primitive hyperbolic conjugacy classes in PSL(2, Z) of trace 3 ([LR], [RL] -> 2) and trace 4 ([L^2 R], [R^2 L] -> 2)
    return 2, 2


def build_uv_yukawas_standalone(l2_val: mp.mpf, dps: int = 44) -> Tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix]:
    old_dps = mp.mp.dps
    mp.mp.dps = dps
    try:
        c3_cnt, c4_cnt = selberg_prim_counts_up_to_4()

        def sel_w(tr_i: int) -> mp.mpf:
            lam = (mp.mpf(tr_i) + mp.sqrt(mp.mpf(tr_i * tr_i - 4))) / 2
            return mp.fsum((lam ** (-4 * m)) / (mp.mpf(m) * (1 - (lam ** (-2 * m)))) for m in range(1, 40))

        w3, w4 = mp.mpf(c3_cnt) * sel_w(3), mp.mpf(c4_cnt) * sel_w(4)
        om3, om4 = w3 / (w3 + w4), w4 / (w3 + w4)
        tau8 = mp.mpc(mp.mpf(16) / 5, mp.mpf(8) / 5)
        p3, p4 = (Fraction(1, 5), Fraction(2, 5)), (Fraction(1, 6), Fraction(1, 6))
        mats: List[mp.matrix] = []
        for ql, qr in ((1, -4), (1, 2), (-3, 6)):
            y3 = standalone_yukawa_matrix(tau8, p3[0], p3[1], ql, qr, l2_val)
            y4 = standalone_yukawa_matrix(tau8, p4[0], p4[1], ql, qr, l2_val)
            gj = herm_exp_mp(om3 * herm_log_mp(y3 * y3.H) + om4 * herm_log_mp(y4 * y4.H))
            evs, u_m = mp.eighe((gj + gj.H) / 2)
            mats.append(u_m * mp.diag([mp.sqrt(max(mp.mpf(0), x)) for x in evs]) * u_m.H)
        yn_raw = standalone_yukawa_matrix(tau8, p3[0], p3[1], -3, 0, l2_val)
        tr_d5 = lambda ym: (ym * ((ym.H * ym) ** 2)) / (mp.re((ym.H * ym)[0, 0] + (ym.H * ym)[1, 1] + (ym.H * ym)[2, 2]) ** 2)
        return tr_d5(mats[0]), tr_d5(mats[1]), tr_d5(mats[2]), yn_raw
    finally:
        mp.mp.dps = old_dps


def evolve_agy_rge_standalone(
    yu0: mp.matrix,
    yd0: mp.matrix,
    ye0: mp.matrix,
    yn0: mp.matrix,
    n_steps: int,
    xi_val: mp.mpf = mp.mpf(1) / 2,
    dps: int = 44,
) -> Dict[str, Any]:
    old_dps = mp.mp.dps
    mp.mp.dps = dps
    try:
        inv16 = mp.mpf(1) / (16 * (mp.pi**2))
        inv16_2 = inv16 * inv16
        b1 = [mp.mpf(21) / 5, mp.mpf(-3), mp.mpf(-7)]
        b2 = [
            [mp.mpf(104) / 25, mp.mpf(18) / 5, mp.mpf(44) / 5],
            [mp.mpf(6) / 5, mp.mpf(8), mp.mpf(12)],
            [mp.mpf(11) / 10, mp.mpf(9) / 2, mp.mpf(-26)],
        ]
        tr3 = lambda m: mp.re(m[0, 0] + m[1, 1] + m[2, 2])
        z3 = mp.zeros(3, 3)
        t_nu = -mp.mpf(16) * mp.pi / 5
        t_ew = -mp.mpf(48) * mp.pi / 5
        g0_sq = mp.pi / 10
        g0 = mp.sqrt(g0_sq)
        m12_sq = mp.mpf(1) / 40

        def rhs(st):
            g, yu, yd, ye, yn, mr, lam, mh2 = st
            g1_2, g2_2, g3_2 = g[0] ** 2, g[1] ** 2, g[2] ** 2
            gy2, gw2 = (mp.mpf(3) / 5) * g1_2, g2_2
            gu, gd, ge, gn = yu * yu.H, yd * yd.H, ye * ye.H, yn * yn.H
            tru, trd, tre, trn = tr3(gu), tr3(gd), tr3(ge), tr3(gn)
            tru4, trd4, tre4, trn4, trud = tr3(gu * gu), tr3(gd * gd), tr3(ge * ge), tr3(gn * gn), tr3(gu * gd)
            tu, td = 3 * tru + trn, 3 * trd + tre
            fb = [
                (mp.mpf(17) / 10) * tru + (mp.mpf(1) / 2) * trd + (mp.mpf(3) / 2) * tre + (mp.mpf(3) / 10) * trn,
                (mp.mpf(3) / 2) * (tru + trd) + (mp.mpf(1) / 2) * (tre + trn),
                2 * (tru + trd),
            ]
            dg = [
                inv16 * b1[i] * (g[i] ** 3)
                + inv16_2 * (g[i] ** 3) * (sum(b2[i][j] * (g[j] ** 2) for j in range(3)) - fb[i])
                for i in range(3)
            ]
            dyu = inv16 * ((tu - (mp.mpf(17) / 20) * g1_2 - (mp.mpf(9) / 4) * g2_2 - 8 * g3_2) * yu + ((mp.mpf(3) / 2) * gu + (mp.mpf(1) / 2) * gd) * yu) + inv16_2 * ((-108 * g3_2**2 + 20 * g3_2 * tru) * yu + (16 * g3_2 * gu - (mp.mpf(9) / 4) * tu * gu + (mp.mpf(3) / 2) * gu * gu) * yu)
            dyd = inv16 * ((td - (mp.mpf(1) / 4) * g1_2 - (mp.mpf(9) / 4) * g2_2 - 8 * g3_2) * yd + ((mp.mpf(3) / 2) * gd + (mp.mpf(1) / 2) * gu) * yd) + inv16_2 * ((-108 * g3_2**2 + 20 * g3_2 * trd) * yd + (16 * g3_2 * gd - (mp.mpf(9) / 4) * td * gd + (mp.mpf(3) / 2) * gd * gd) * yd)
            dye = inv16 * ((td - (mp.mpf(9) / 4) * (g1_2 + g2_2)) * ye + ((mp.mpf(3) / 2) * ge + (mp.mpf(1) / 2) * gn) * ye) + inv16_2 * ((-(mp.mpf(9) / 4) * td * ge + (mp.mpf(3) / 2) * ge * ge) * ye)
            dyn = inv16 * ((tu - (mp.mpf(9) / 20) * g1_2 - (mp.mpf(9) / 4) * g2_2) * yn + ((mp.mpf(3) / 2) * gn + (mp.mpf(1) / 2) * ge) * yn) + inv16_2 * ((-(mp.mpf(9) / 4) * tu * gn + (mp.mpf(3) / 2) * gn * gn) * yn)
            hn = yn.H * yn
            dmr = 2 * inv16 * (mr * hn + hn.T * mr)
            l1, l2, l3, l4 = lam
            c34 = mp.mpf(3) / 4
            dl1 = inv16 * (12 * l1**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2 + (4 * td - 3 * gy2 - 9 * gw2) * l1 + c34 * (gy2**2 + 2 * gy2 * gw2 + 3 * gw2**2) - 12 * trd4 - 4 * tre4)
            dl2 = inv16 * (12 * l2**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2 + (4 * tu - 3 * gy2 - 9 * gw2) * l2 + c34 * (gy2**2 + 2 * gy2 * gw2 + 3 * gw2**2) - 12 * tru4 - 4 * trn4)
            dl3 = inv16 * ((l1 + l2) * (6 * l3 + 2 * l4) + 4 * l3**2 + 2 * l4**2 + (2 * tu + 2 * td - 3 * gy2 - 9 * gw2) * l3 + c34 * (gy2**2 - 2 * gy2 * gw2 + 3 * gw2**2) - 12 * trud)
            dl4 = inv16 * (2 * (l1 + l2) * l4 + 8 * l3 * l4 + 4 * l4**2 + (2 * tu + 2 * td - 3 * gy2 - 9 * gw2) * l4 + 3 * gy2 * gw2 + 12 * trud)
            gew = (mp.mpf(9) / 10) * g1_2 + (mp.mpf(9) / 2) * g2_2
            dmh2 = [inv16 * (2 * tu * (mh2[0] + 2 * xi_val) - gew * xi_val), inv16 * (2 * td * (mh2[1] + 2 * xi_val) - gew * xi_val)]
            return (dg, dyu, dyd, dye, dyn, dmr, [dl1, dl2, dl3, dl4], dmh2)

        def add_st(sa, sb, cf):
            return (
                [sa[0][i] + cf * sb[0][i] for i in range(3)],
                sa[1] + cf * sb[1],
                sa[2] + cf * sb[2],
                sa[3] + cf * sb[3],
                sa[4] + cf * sb[4],
                sa[5] + cf * sb[5],
                [sa[6][i] + cf * sb[6][i] for i in range(4)],
                [sa[7][0] + cf * sb[7][0], sa[7][1] + cf * sb[7][1]],
            )

        lam0 = [(mp.mpf(2) / 5) * g0_sq, (mp.mpf(2) / 5) * g0_sq, (mp.mpf(1) / 10) * g0_sq, -(mp.mpf(1) / 2) * g0_sq]
        st = ([g0, g0, g0], yu0.copy(), yd0.copy(), ye0.copy(), yn0.copy(), mp.eye(3), lam0, [mp.mpf(1), mp.mpf(1)])
        na = n_steps // 3
        dta = t_nu / mp.mpf(na)
        for _ in range(na):
            k1 = rhs(st)
            k2 = rhs(add_st(st, k1, dta / 2))
            k3 = rhs(add_st(st, k2, dta / 2))
            k4 = rhs(add_st(st, k3, dta))
            cb = (
                [k1[0][i] + 2 * k2[0][i] + 2 * k3[0][i] + k4[0][i] for i in range(3)],
                k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1],
                k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2],
                k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3],
                k1[4] + 2 * k2[4] + 2 * k3[4] + k4[4],
                k1[5] + 2 * k2[5] + 2 * k3[5] + k4[5],
                [k1[6][i] + 2 * k2[6][i] + 2 * k3[6][i] + k4[6][i] for i in range(4)],
                [k1[7][0] + 2 * k2[7][0] + 2 * k3[7][0] + k4[7][0], k1[7][1] + 2 * k2[7][1] + 2 * k3[7][1] + k4[7][1]],
            )
            st = add_st(st, cb, dta / 6)

        ye_tnu = st[3].copy()
        yn_tnu = st[4].copy()
        mr_tnu = (st[5] + st[5].T) / 2

        nb = n_steps - na
        dtb = (t_ew - t_nu) / mp.mpf(nb)
        st_ir = (st[0], st[1], st[2], st[3], z3.copy(), z3.copy(), st[6], st[7])
        for _ in range(nb):
            k1 = rhs(st_ir)
            k2 = rhs(add_st(st_ir, k1, dtb / 2))
            k3 = rhs(add_st(st_ir, k2, dtb / 2))
            k4 = rhs(add_st(st_ir, k3, dtb))
            cb = (
                [k1[0][i] + 2 * k2[0][i] + 2 * k3[0][i] + k4[0][i] for i in range(3)],
                k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1],
                k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2],
                k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3],
                z3,
                z3,
                [k1[6][i] + 2 * k2[6][i] + 2 * k3[6][i] + k4[6][i] for i in range(4)],
                [k1[7][0] + 2 * k2[7][0] + 2 * k3[7][0] + k4[7][0], k1[7][1] + 2 * k2[7][1] + 2 * k3[7][1] + k4[7][1]],
            )
            st_ir = add_st(st_ir, cb, dtb / 6)

        return {
            "g_ir": st_ir[0],
            "yu_ir": st_ir[1],
            "yd_ir": st_ir[2],
            "ye_ir": st_ir[3],
            "lam_ir": st_ir[6],
            "mh2_ir": st_ir[7],
            "m12_sq": m12_sq,
            "ye_tnu": ye_tnu,
            "yn_tnu": yn_tnu,
            "mr_tnu": mr_tnu,
        }
    finally:
        mp.mp.dps = old_dps


def solve_2hdm_newton(lam: List[mp.mpf], mh2: List[mp.mpf], m12_sq: mp.mpf) -> Tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    l1, l2, l3, l4 = lam
    l34 = l3 + l4
    mhu2, mhd2 = mh2
    vu = mp.sqrt(max(mp.mpf("1e-30"), -2 * mhu2 / l2))
    vd = m12_sq * vu / (mhd2 + (l34 / 2) * (vu**2))
    for _ in range(35):
        f1 = mhd2 * vd - m12_sq * vu + (l1 / 2) * (vd**3) + (l34 / 2) * vd * (vu**2)
        f2 = mhu2 * vu - m12_sq * vd + (l2 / 2) * (vu**3) + (l34 / 2) * (vd**2) * vu
        if max(abs(f1), abs(f2)) < mp.mpf("1e-36"):
            break
        j11 = mhd2 + (mp.mpf(3) / 2) * l1 * (vd**2) + (l34 / 2) * (vu**2)
        j12 = -m12_sq + l34 * vd * vu
        j22 = mhu2 + (mp.mpf(3) / 2) * l2 * (vu**2) + (l34 / 2) * (vd**2)
        det_j = j11 * j22 - j12 * j12
        vd -= (j22 * f1 - j12 * f2) / det_j
        vu -= (-j12 * f1 + j11 * f2) / det_j
    vew = mp.sqrt(vd**2 + vu**2)
    tb_exact = vu / vd
    ma0_over_vew = mp.sqrt(m12_sq * (vu / vd + vd / vu)) / vew
    return vd, vu, tb_exact, ma0_over_vew


# ============================================================================
# Module M4: 2-Loop 2HDM Beta Coefficient, xi = 0 EWSB, & tan(beta) Mismatch
# ============================================================================

def run_module_m4_rge_and_ewsb(
    uv_mats_rat: Tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix],
    uv_mats_interp: Tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix],
) -> Dict[str, Any]:
    # 1. Exact Machacek-Vaughn pure-top 2-loop coefficient in Type-II 2HDM:
    # +(3/2) G_u^2 Y_u - (9/4) T_u G_u Y_u - (9/4) tr(3 G_u^2 + G_nu^2) Y_u -> +3/2 - 27/4 - 27/4 = -12
    c_mv_exact = Fraction(3, 2) - Fraction(9, 4) * 3 - Fraction(9, 4) * 3
    c_agy_trunc = Fraction(3, 2) - Fraction(9, 4) * 3  # -21/4

    # Planted Control PC_RAGY_4: pure-y_t ODE dy/dt = c * y^5 / (16*pi^2)^2 over dt = -30:
    # Self-step-halving N=2000 vs N=4000 on truncated -21/4 converges to < 1e-12 while differing from exact -12!
    def integrate_pure_yt(c_coeff: Fraction, n_st: int) -> mp.mpf:
        inv16_2 = mp.mpf(1) / ((16 * (mp.pi**2)) ** 2)
        cm = frac_to_mp(c_coeff)
        y_cur = mp.mpf(1)
        dt = -mp.mpf(30) / mp.mpf(n_st)
        f_rhs = lambda yv: cm * inv16_2 * (yv**5)
        for _ in range(n_st):
            k1 = f_rhs(y_cur)
            k2 = f_rhs(y_cur + (dt / 2) * k1)
            k3 = f_rhs(y_cur + (dt / 2) * k2)
            k4 = f_rhs(y_cur + dt * k3)
            y_cur += (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        return y_cur

    yt_trunc_2k = integrate_pure_yt(c_agy_trunc, 2000)
    yt_trunc_4k = integrate_pure_yt(c_agy_trunc, 4000)
    yt_exact_4k = integrate_pure_yt(c_mv_exact, 4000)
    self_conv_err = abs(yt_trunc_4k - yt_trunc_2k) / yt_trunc_4k
    trunc_vs_exact_err = abs(yt_trunc_4k - yt_exact_4k) / yt_exact_4k
    pc4_caught = (self_conv_err < mp.mpf("1e-12")) and (trunc_vs_exact_err > mp.mpf("1e-4"))

    # 2. Check L_2 = 5/2 (countercheck) vs grid-interpolated L_2 = 2.5170518... (producer) discrepancy on u_m1_over_m3
    rge_rat = evolve_agy_rge_standalone(*uv_mats_rat, n_steps=180, xi_val=mp.mpf(1) / 2, dps=42)
    rge_int = evolve_agy_rge_standalone(*uv_mats_interp, n_steps=180, xi_val=mp.mpf(1) / 2, dps=42)
    _, svu_rat = svd_asc_mp(rge_rat["yu_ir"])
    _, svu_int = svd_asc_mp(rge_int["yu_ir"])
    um13_rat = svu_rat[0] / svu_rat[2]
    um13_int = svu_int[0] / svu_int[2]
    l2_rel_mismatch = abs(um13_int - um13_rat) / um13_int

    # 3. Check xi = 0 EWSB failure and linearized vs exact Newton tan(beta) mismatch + 26-decade hierarchy
    rge_no_xi = evolve_agy_rge_standalone(*uv_mats_interp, n_steps=120, xi_val=mp.mpf(0), dps=42)
    mhu2_no_xi = rge_no_xi["mh2_ir"][0]

    mhu2_ir, mhd2_ir = rge_int["mh2_ir"]
    l1, l2, l3, l4 = rge_int["lam_ir"]
    m12_sq = rge_int["m12_sq"]
    vu_sq_lin = -2 * mhu2_ir / l2
    tb_lin = (mhd2_ir + ((l3 + l4) / 2) * vu_sq_lin) / m12_sq
    vd_ex, vu_ex, tb_exact, _ = solve_2hdm_newton(rge_int["lam_ir"], rge_int["mh2_ir"], m12_sq)
    tb_rel_diff = abs(tb_lin - tb_exact) / tb_exact
    vew_sq_over_m0_sq = vd_ex**2 + vu_ex**2
    mu_ir_sq_over_uv_sq = mp.exp(-mp.mpf(96) * mp.pi / 5)

    return {
        "pure_top_2loop_exact_mv": str(c_mv_exact),
        "pure_top_2loop_agy_truncated": f"{c_agy_trunc.numerator}/{c_agy_trunc.denominator}",
        "missing_2loop_top_fraction": "9/16",
        "l2_countercheck_vs_producer_um13_rel_diff": mp.nstr(l2_rel_mismatch, 6),
        "m_Hu_sq_at_xi_zero": mp.nstr(mhu2_no_xi, 8),
        "ewsb_fails_without_nondecoupled_xi": mhu2_no_xi > 0,
        "tan_beta_linearized_c18": mp.nstr(tb_lin, 12),
        "tan_beta_newton_exact_c24": mp.nstr(tb_exact, 12),
        "tan_beta_internal_rel_mismatch": mp.nstr(tb_rel_diff, 6),
        "vew_sq_over_m0_sq": mp.nstr(vew_sq_over_m0_sq, 6),
        "mu_ir_sq_over_uv_sq": mp.nstr(mu_ir_sq_over_uv_sq, 6),
        "PC_RAGY_4_caught": pc4_caught,
    }


# ============================================================================
# Module M5: Resonant Flavored Leptogenesis Sign Bug (AGY-C23 & AGY-C24)
# ============================================================================

def eval_leptogenesis_flavors(
    ye_m: mp.matrix, yn_m: mp.matrix, mr_m: mp.matrix, use_buggy_sign: bool
) -> Dict[str, Any]:
    # Charged-lepton left eigenbasis U_e and Takagi symmetric diagonalization M_R = U_R^* diag(M_i) U_R^H
    _, ue_ord_svd = svd_asc_mp(ye_m)
    # Note: svd_asc_mp returns (U_ord, sv_list); unpack properly:
    ue_u, _ = svd_asc_mp(ye_m)
    mr_h = mr_m.H * mr_m
    ev_sq, u0 = mp.eighe((mr_h + mr_h.H) / 2)
    ord_m = sorted(range(3), key=lambda k: ev_sq[k])
    m_vals = [mp.sqrt(max(mp.mpf(0), ev_sq[k])) for k in ord_m]
    u_tak = mp.matrix([[u0[r, ord_m[c]] for c in range(3)] for r in range(3)])
    sym_diag = u_tak.T * mr_m * u_tak
    for c in range(3):
        ph = mp.arg(sym_diag[c, c]) / 2
        for r in range(3):
            u_tak[r, c] *= mp.exp(-mp.mpc(0, 1) * ph)
    y_hat = ue_u.H * yn_m.conj() * u_tak
    h_mat = y_hat.H * y_hat
    m1 = m_vals[0]
    eps_flav = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    for j in (1, 2):
        x = (m_vals[j] / m1) ** 2
        gam_j_over_m1 = mp.sqrt(x) * mp.re(h_mat[j, j]) / (8 * mp.pi)
        den = ((1 - x) ** 2) + (gam_j_over_m1**2)
        num_sign = (x - 1) if use_buggy_sign else (1 - x)
        f_sv = mp.sqrt(x) * (num_sign / den + 1 - (1 + x) * mp.log(1 + 1 / x))
        g_osc = num_sign / den
        for al in range(3):
            t1 = mp.im(mp.conj(y_hat[al, 0]) * y_hat[al, j] * h_mat[0, j]) * f_sv
            t2 = mp.im(mp.conj(y_hat[al, 0]) * y_hat[al, j] * h_mat[j, 0]) * g_osc
            eps_flav[al] += (t1 + t2) / (8 * mp.pi * mp.re(h_mat[0, 0]))
    h00 = mp.re(h_mat[0, 0])
    p_tau = abs(y_hat[2, 0]) ** 2 / h00
    p_emu = 1 - p_tau
    # Strong-washout relative flavor survival weight ~ P_{1,a}^{-1.16} (Buchmuller-Di Bari-Plumacher / Blanchet-Di Bari)
    exp_w = mp.mpf(29) / 25  # 1.16
    yl_prop = eps_flav[2] * (p_tau ** (-exp_w)) + (eps_flav[0] + eps_flav[1]) * (p_emu ** (-exp_w))
    return {
        "eps_flav": eps_flav,
        "eps_tot": eps_flav[0] + eps_flav[1] + eps_flav[2],
        "p_1_emu": p_emu,
        "p_1_tau": p_tau,
        "washout_weighted_Y_B_sign": -1 if yl_prop > 0 else +1,
    }


def run_module_m5_leptogenesis(
    uv_mats_interp: Tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix],
) -> Dict[str, Any]:
    # Symbolic large-x asymptotic check of Covi-Roulet-Vissani f_SV(x)
    x_s = sp.Symbol("x", positive=True)
    f_true_sym = sp.sqrt(x_s) * (1 / (1 - x_s) + 1 - (1 + x_s) * sp.log(1 + 1 / x_s))
    f_bug_sym = sp.sqrt(x_s) * ((x_s - 1) / ((1 - x_s) ** 2) + 1 - (1 + x_s) * sp.log(1 + 1 / x_s))
    lead_true = sp.limit(sp.sqrt(x_s) * f_true_sym, x_s, sp.oo)  # -3/2
    lead_bug = sp.limit(sp.sqrt(x_s) * f_bug_sym, x_s, sp.oo)    # +1/2

    rge240 = evolve_agy_rge_standalone(*uv_mats_interp, n_steps=240, xi_val=mp.mpf(1) / 2, dps=44)
    res_bug = eval_leptogenesis_flavors(rge240["ye_tnu"], rge240["yn_tnu"], rge240["mr_tnu"], use_buggy_sign=True)
    res_true = eval_leptogenesis_flavors(rge240["ye_tnu"], rge240["yn_tnu"], rge240["mr_tnu"], use_buggy_sign=False)

    eps_tau_inflation = abs(res_bug["eps_flav"][2] / res_true["eps_flav"][2])
    sph_1hdm = Fraction(28, 79)
    sph_2hdm = Fraction(8 * 3 + 4 * 2, 22 * 3 + 13 * 2)  # 32/92 = 8/23

    pc5_caught = (
        (lead_true == sp.Rational(-3, 2))
        and (lead_bug == sp.Rational(1, 2))
        and (res_bug["eps_tot"] < 0 < res_true["eps_tot"])
        and (res_true["washout_weighted_Y_B_sign"] == -1)
    )
    return {
        "large_x_sqrt_x_limit_true_crv": str(lead_true),
        "large_x_sqrt_x_limit_buggy_c23": str(lead_bug),
        "buggy_eps_1_tau": mp.nstr(res_bug["eps_flav"][2], 10),
        "true_crv_eps_1_tau": mp.nstr(res_true["eps_flav"][2], 10),
        "eps_1_tau_inflation_factor": mp.nstr(eps_tau_inflation, 6),
        "buggy_eps_tot": mp.nstr(res_bug["eps_tot"], 10),
        "true_crv_eps_tot": mp.nstr(res_true["eps_tot"], 10),
        "true_eps_1_e_plus_mu": mp.nstr(res_true["eps_flav"][0] + res_true["eps_flav"][1], 10),
        "branching_P_1_emu": mp.nstr(res_true["p_1_emu"], 6),
        "branching_P_1_tau": mp.nstr(res_true["p_1_tau"], 6),
        "true_washout_weighted_Y_B_sign_on_tau_star_plus": res_true["washout_weighted_Y_B_sign"],
        "sphaleron_factor_2hdm_exact": f"{sph_2hdm.numerator}/{sph_2hdm.denominator}",
        "sphaleron_factor_used_in_v2_json": f"{sph_1hdm.numerator}/{sph_1hdm.denominator}",
        "PC_RAGY_5_caught": pc5_caught,
    }


# ============================================================================
# Module M6: 2I Non-Crystallography, 2T Hurwitz Lattice, & C24 F2 Failure
# ============================================================================

def run_module_m6_mtheory_and_c24_f2(
    uv_mats_interp: Tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix],
) -> Dict[str, Any]:
    # 1. Order-10 element g_10 in 2I subset SU(2) acting on C^2 = R^4 has real trace 4*cos(pi/5) = 1 + sqrt(5)
    tr_g10 = sp.simplify(4 * sp.cos(sp.pi / 5))
    tr_g10_is_integer = tr_g10.is_integer is True

    # 2. Order-3 Hurwitz unit q = (1 + i + j + k)/2 in 2T acting by left quaternion multiplication on e_0 = (1,0,0,0)
    q_e0 = (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))
    z4_preserved_by_2t = all(coord.denominator == 1 for coord in q_e0)

    # 3. AGY-C24 pre-registered F2 test: N = 120 vs N = 240 step-halving residual (< 10^-7 required by Card AGY-C24)
    rge_120 = evolve_agy_rge_standalone(*uv_mats_interp, n_steps=120, xi_val=mp.mpf(1) / 2, dps=44)
    rge_240 = evolve_agy_rge_standalone(*uv_mats_interp, n_steps=240, xi_val=mp.mpf(1) / 2, dps=44)
    _, _, _, ma0_120 = solve_2hdm_newton(rge_120["lam_ir"], rge_120["mh2_ir"], rge_120["m12_sq"])
    _, _, _, ma0_240 = solve_2hdm_newton(rge_240["lam_ir"], rge_240["mh2_ir"], rge_240["m12_sq"])
    f2_rel_120_240 = abs(ma0_240 - ma0_120) / ma0_240

    # Planted Control PC_RAGY_6: substituting N = 180 vs N = 360 (as c24 lines 178-179 did) drops below 10^-7
    rge_180 = evolve_agy_rge_standalone(*uv_mats_interp, n_steps=180, xi_val=mp.mpf(1) / 2, dps=44)
    rge_360 = evolve_agy_rge_standalone(*uv_mats_interp, n_steps=360, xi_val=mp.mpf(1) / 2, dps=44)
    _, _, _, ma0_180 = solve_2hdm_newton(rge_180["lam_ir"], rge_180["mh2_ir"], rge_180["m12_sq"])
    _, _, _, ma0_360 = solve_2hdm_newton(rge_360["lam_ir"], rge_360["mh2_ir"], rge_360["m12_sq"])
    rel_180_360 = abs(ma0_360 - ma0_180) / ma0_360

    thresh = mp.mpf("1e-7")
    pc6_caught = (f2_rel_120_240 > thresh) and (rel_180_360 < thresh)
    return {
        "trace_R4_order10_in_2I": str(tr_g10),
        "compact_T4_mod_2I_crystallographic_allowed": tr_g10_is_integer,
        "hurwitz_2T_image_of_1000": [f"{c.numerator}/{c.denominator}" for c in q_e0],
        "cubic_Z4_lattice_preserved_by_2T": z4_preserved_by_2t,
        "c24_true_N120_vs_N240_rel_drift_higgs_A0": mp.nstr(f2_rel_120_240, 10),
        "c24_preregistered_F2_failed_gt_1e7": f2_rel_120_240 > thresh,
        "c24_substituted_N180_vs_N360_rel_drift_higgs_A0": mp.nstr(rel_180_360, 10),
        "PC_RAGY_6_caught": pc6_caught,
    }


def main() -> None:
    ast_check = enforce_zero_float_literals_ast()
    assert ast_check["zero_float_literals_passed"], f"Float literals found: {ast_check}"

    m0 = run_module_m0_git_and_quotes()
    m1 = run_module_m1_e8_10_6()
    m2 = run_module_m2_covers_and_mp2z()
    m3 = run_module_m3_potential_collar_strong_cp()

    # Build standalone UV Yukawas at rational L_2 = 5/2 (countercheck value) and grid-interpolated rationalized L_2
    l2_rat = mp.mpf(5) / 2
    l2_interp = mp.mpf(25170518393860516) / mp.mpf(10000000000000000)
    uv_rat = build_uv_yukawas_standalone(l2_rat, dps=44)
    uv_interp = build_uv_yukawas_standalone(l2_interp, dps=44)

    m4 = run_module_m4_rge_and_ewsb(uv_rat, uv_interp)
    m5 = run_module_m5_leptogenesis(uv_interp)
    m6 = run_module_m6_mtheory_and_c24_f2(uv_interp)

    plants_caught = sum(
        int(x)
        for x in (
            m1["PC_RAGY_1_caught"],
            m2["PC_RAGY_2_caught"],
            m3["PC_RAGY_3_caught"],
            m4["PC_RAGY_4_caught"],
            m5["PC_RAGY_5_caught"],
            m6["PC_RAGY_6_caught"],
        )
    )

    out_doc: Dict[str, Any] = {
        "card": "R-AGY-C24",
        "target_branch": "origin/agy/cusp-action-2026-11-20",
        "target_commit": TARGET_COMMIT,
        "empirical_firewall": "0 of 19",
        "ast_zero_float_check": ast_check,
        "M0_git_custody_and_quotes": m0,
        "M1_e8_10_6_multiplicity": m1,
        "M2_covers_and_mp2z": m2,
        "M3_potential_collar_and_strong_cp": m3,
        "M4_2loop_2hdm_rge_and_ewsb": m4,
        "M5_resonant_leptogenesis_sign": m5,
        "M6_mtheory_crystallography_and_c24_f2": m6,
        "planted_controls_caught": plants_caught,
        "planted_controls_total": 6,
        "all_6_planted_controls_caught": plants_caught == 6,
    }

    assert_no_json_floats(out_doc)
    payload = json.dumps(out_doc, indent=2, sort_keys=True) + "\n"
    OUT_PATH.write_text(payload, encoding="utf-8")
    out_sha = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    OUT_SHA_PATH.write_text(f"{out_sha}  {OUT_PATH.name}\n", encoding="utf-8")
    print(f"R-AGY-C24 standalone check complete: {plants_caught}/6 planted controls caught; SHA-256={out_sha}")


if __name__ == "__main__":
    main()
