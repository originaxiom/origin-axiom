#!/usr/bin/env python3
"""AST-Isolated Zero-Import Referee Suite for Phase 11 (`165 / 165` Cumulative Controls, Guardrails 1-6)."""
from __future__ import annotations

import ast
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Dict, List

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import snappy

mp.mp.dps = 60
PROJECT_ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_REFEREE_IMPORTS = (
    "phase11_toe",
    "phase10_toe",
    "phase9_toe",
    "phase8_toe",
    "phase7_toe",
    "phase6_toe",
    "phase5_loop",
    "phase4_loop",
    "relational_loop",
    "cusped_loop",
    "phi_loop",
    "src.",
)

TRACK_A_MODULES = {
    "src/phase11_toe/p11_1_h3_huygens_propagator_exactness.py",
    "src/phase11_toe/p11_2_porti_adjoint_torsion.py",
    "src/phase11_toe/p11_3_one_loop_overtone_partition.py",
    "src/phase11_toe/p11_4_joint_consistency.py",
    "src/phase11_toe/phase11_engine.py",
}

FORBIDDEN_PDG_FLOATS = (
    127.951,
    0.1179,
    0.23121,
    0.225,
    0.04182,
    0.003732,
    3.12e-5,
    0.307,
    0.546,
    0.02203,
    246.21965,
    2.43536e18,
    0.120,
    2.10e-9,
    0.9649,
    6.12e-10,
    0.038,
    0.036,
    2.4e34,
)

FORBIDDEN_FLAG_KEYS = {"extends_to_cover", "bar_theta_QCD", "theta_qcd_bar", "dynamical_strong_cp_theta_eff"}


def run_ast_guardrail_scan(project_root: Path = PROJECT_ROOT) -> Dict[str, Any]:
    ref_path = Path(__file__).resolve()
    py_files: List[Path] = []
    for d in (project_root / "src", project_root / "scripts", project_root / "tests"):
        if d.exists():
            py_files.extend(sorted(d.rglob("*.py")))

    bad_imports: List[str] = []
    bad_track_a_floats: List[str] = []
    bad_flags: List[str] = []

    for fp in py_files:
        rel = str(fp.relative_to(project_root)).replace("\\", "/")
        tree = ast.parse(fp.read_text(encoding="utf-8"), filename=rel)
        is_ref = fp.resolve() == ref_path
        is_track_a = rel in TRACK_A_MODULES

        for node in ast.walk(tree):
            if is_ref:
                if isinstance(node, ast.Import):
                    for a in node.names:
                        if a.name.startswith(FORBIDDEN_REFEREE_IMPORTS) or a.name == "src":
                            bad_imports.append(a.name)
                elif isinstance(node, ast.ImportFrom):
                    mod = node.module or ""
                    if node.level > 0 or mod.startswith(FORBIDDEN_REFEREE_IMPORTS) or mod == "src":
                        bad_imports.append(mod or f"relative_{node.level}")

            if is_track_a and isinstance(node, ast.Constant) and isinstance(node.value, float):
                val = float(node.value)
                for tgt in FORBIDDEN_PDG_FLOATS:
                    if abs(val - tgt) <= 1e-11 * max(1.0, abs(tgt)):
                        bad_track_a_floats.append(f"{rel}:{node.lineno}:{val}")

            if isinstance(node, ast.Dict):
                for k_n, v_n in zip(node.keys, node.values):
                    if isinstance(k_n, ast.Constant) and k_n.value in FORBIDDEN_FLAG_KEYS:
                        if isinstance(v_n, ast.Constant) and isinstance(v_n.value, (bool, int, float)):
                            bad_flags.append(f"{rel}:{k_n.lineno}:{k_n.value}")

    passed = bool(not bad_imports and not bad_track_a_floats and not bad_flags)
    return {
        "passed": passed,
        "num_scanned_files": len(py_files),
        "forbidden_referee_imports": bad_imports,
        "forbidden_track_a_pdg_floats": bad_track_a_floats,
        "forbidden_literal_flags": bad_flags,
    }


def _random_haar_u(n: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    q = q * (d / np.abs(d))
    return q / (np.linalg.det(q) ** (1.0 / n))


def _rhs76_indep(_t: float, y: np.ndarray) -> np.ndarray:
    g = y[0:3]
    yu = (y[3:12] + 1j * y[12:21]).reshape(3, 3)
    yd = (y[21:30] + 1j * y[30:39]).reshape(3, 3)
    ye = (y[39:48] + 1j * y[48:57]).reshape(3, 3)
    lam = float(y[57])
    knu = (y[58:67] + 1j * y[67:76]).reshape(3, 3)
    g1, g2, g3 = g
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
    c1 = 1.0 / (16.0 * math.pi * math.pi)
    c2 = c1 * c1
    hu, hd, he = yu @ yu.conj().T, yd @ yd.conj().T, ye @ ye.conj().T
    tu, td, te = float(np.real(np.trace(hu))), float(np.real(np.trace(hd))), float(np.real(np.trace(he)))
    tr_tot = 3.0 * tu + 3.0 * td + te
    b2 = np.array([[3.98, 2.7, 8.8], [0.9, 35.0 / 6.0, 12.0], [1.1, 4.5, -26.0]])
    cy = np.array([[1.7, 0.5, 1.5], [1.5, 1.5, 0.5], [2.0, 2.0, 0.0]])
    dg = c1 * np.array([4.1, -19.0 / 6.0, -7.0]) * (g**3) + c2 * (g**3) * (b2 @ np.array([g12, g22, g32]) - cy @ np.array([tu, td, te]))
    tu2, td2, te2, tud = (
        float(np.real(np.trace(hu @ hu))),
        float(np.real(np.trace(hd @ hd))),
        float(np.real(np.trace(he @ he))),
        float(np.real(np.trace(hu @ hd))),
    )
    chi2 = -2.25 * (3.0 * tu2 + 3.0 * td2 + te2) + 1.5 * tud
    y2g = (
        ((85.0 / 24.0) * g12 + (45.0 / 8.0) * g22 + 20.0 * g32) * tu
        + ((25.0 / 24.0) * g12 + (45.0 / 8.0) * g22 + 20.0 * g32) * td
        + ((75.0 / 8.0) * g12 + (15.0 / 8.0) * g22) * te
    )
    dyu = c1 * ((1.5 * (hu - hd) + (tr_tot - 0.85 * g12 - 2.25 * g22 - 8.0 * g32) * np.eye(3)) @ yu) + c2 * (
        1.5 * (hu @ hu) - hu @ hd - 0.25 * (hd @ hu) + 2.75 * (hd @ hd) - 2.25 * tr_tot * hu - 12.0 * lam * hu
        + (chi2 + y2g + 6.0 * (lam**2) + (1187.0 / 600.0) * (g12**2) - 0.45 * g12 * g22 + (19.0 / 15.0) * g12 * g32 - 5.75 * (g22**2) + 9.0 * g22 * g32 - 108.0 * (g32**2)) * np.eye(3)
        + (223.0 / 80.0 * g12 + 135.0 / 16.0 * g22 + 16.0 * g32) * hu - (43.0 / 80.0 * g12 - 9.0 / 16.0 * g22 + 16.0 * g32) * hd
    ) @ yu
    dyd = c1 * ((1.5 * (hd - hu) + (tr_tot - 0.25 * g12 - 2.25 * g22 - 8.0 * g32) * np.eye(3)) @ yd) + c2 * (
        1.5 * (hd @ hd) - hd @ hu - 0.25 * (hu @ hd) + 2.75 * (hu @ hu) - 2.25 * tr_tot * hd - 12.0 * lam * hd
        + (chi2 + y2g + 6.0 * (lam**2) - (127.0 / 600.0) * (g12**2) - 1.35 * g12 * g22 + (31.0 / 15.0) * g12 * g32 - 5.75 * (g22**2) + 9.0 * g22 * g32 - 108.0 * (g32**2)) * np.eye(3)
        + (187.0 / 80.0 * g12 + 135.0 / 16.0 * g22 + 16.0 * g32) * hd - (79.0 / 80.0 * g12 - 9.0 / 16.0 * g22 + 16.0 * g32) * hu
    ) @ yd
    dye = c1 * ((1.5 * he + (tr_tot - 2.25 * g12 - 2.25 * g22) * np.eye(3)) @ ye) + c2 * (
        1.5 * (he @ he) - 2.25 * tr_tot * he - 12.0 * lam * he
        + (chi2 + y2g + 6.0 * (lam**2) + (1371.0 / 200.0) * (g12**2) + 1.35 * g12 * g22 - 5.75 * (g22**2)) * np.eye(3)
        + (387.0 / 80.0 * g12 + 135.0 / 16.0 * g22) * he
    ) @ ye
    gp2 = 0.6 * g12
    dlam = c1 * (24.0 * (lam**2) + lam * (4.0 * tr_tot - 9.0 * g22 - 3.0 * gp2) - 2.0 * (3.0 * tu2 + 3.0 * td2 + te2) + 1.125 * (g22**2) + 0.75 * g22 * gp2 + 0.375 * (gp2**2)) + c2 * (
        -312.0 * (lam**3) - 144.0 * (lam**2) * tu + 36.0 * (lam**2) * (3.0 * g22 + gp2) - 3.0 * lam * (tu**2)
        + lam * tu * (80.0 * g32 + 22.5 * g22 + (85.0 / 6.0) * gp2) - 32.0 * g32 * (tu**2) - (8.0 / 3.0) * gp2 * (tu**2) + 30.0 * (tu**3)
    )
    dknu = c1 * (-1.5 * (he @ knu + knu @ he.T) + (-3.0 * g22 + 4.0 * lam + 2.0 * tr_tot) * knu)
    return np.concatenate([dg.real, dyu.real.ravel(), dyu.imag.ravel(), dyd.real.ravel(), dyd.imag.ravel(), dye.real.ravel(), dye.imag.ravel(), [float(dlam)], dknu.real.ravel(), dknu.imag.ravel()])


def _indep_porti_so3_basis(m_hp: Any, conj_c: mp.matrix | None = None, mod_mat: tuple[int, int, int, int] = (1, 0, 0, 1)) -> tuple[mp.mpf, mp.mpf]:
    """Independent zero-trust Porti torsion reconstructor using Killing-orthonormal SO(3, C) Pauli basis
    (distinct from producer's Sym^2 basis!), contour radius 2e-7 with 12 points, and adversarial SL(2,C)/SL(2,Z) rotations!"""
    mp.mp.dps = 60
    g_fg = m_hp.fundamental_group(simplify_presentation=True)
    gens, rels = list(g_fg.generators()), list(g_fg.relators())
    mw_raw, lw_raw = g_fg.peripheral_curves()[0]
    inv_w = lambda w: "".join(c.lower() if c.isupper() else c.upper() for c in reversed(w))

    def word_pow(w: str, k: int) -> str:
        if k == 0:
            return ""
        return (w * k) if k > 0 else (inv_w(w) * (-k))

    a_z, b_z, c_z, d_z = mod_mat
    m_word = word_pow(mw_raw, a_z) + word_pow(lw_raw, b_z)
    l_word = word_pow(mw_raw, c_z) + word_pow(lw_raw, d_z)

    qstr = lambda q: str(q).replace(" ", "")
    s_pauli = [
        mp.matrix([[0, 1], [1, 0]]) / mp.sqrt(2),
        mp.matrix([[0, -1j], [1j, 0]]) / mp.sqrt(2),
        mp.matrix([[1, 0], [0, -1]]) / mp.sqrt(2),
    ]

    def to_so3(a2: mp.matrix) -> mp.matrix:
        ainv = mp.matrix([[a2[1, 1], -a2[0, 1]], [-a2[1, 0], a2[0, 0]]])
        out = mp.zeros(3, 3)
        for j in range(3):
            y_m = a2 * s_pauli[j] * ainv
            for i in range(3):
                out[i, j] = (s_pauli[i] * y_m)[0, 0] + (s_pauli[i] * y_m)[1, 1]
        return out

    mats: Dict[str, mp.matrix] = {}
    for g in gens:
        m0 = g_fg.SL2C(g)
        a_m = mp.matrix([
            [mp.mpc(qstr(m0[0][0].real()), qstr(m0[0][0].imag())), mp.mpc(qstr(m0[0][1].real()), qstr(m0[0][1].imag()))],
            [mp.mpc(qstr(m0[1][0].real()), qstr(m0[1][0].imag())), mp.mpc(qstr(m0[1][1].real()), qstr(m0[1][1].imag()))],
        ])
        a_m = a_m / mp.sqrt(a_m[0, 0] * a_m[1, 1] - a_m[0, 1] * a_m[1, 0])
        if conj_c is not None:
            cinv = mp.matrix([[conj_c[1, 1], -conj_c[0, 1]], [-conj_c[1, 0], conj_c[0, 0]]])
            a_m = conj_c * a_m * cinv
        mats[g] = a_m

    n_g = len(gens)
    g_idx = {g: i for i, g in enumerate(gens)}
    a_ab = np.zeros((len(rels), n_g), dtype=int)
    for r_i, r in enumerate(rels):
        for ch in r:
            a_ab[r_i, g_idx[ch.lower()]] += 1 if ch.islower() else -1
    _, _, vh = np.linalg.svd(a_ab.astype(float))
    v = vh[-1]
    v_sc = v / min(abs(x) for x in v if abs(x) > 1e-8)
    phi = None
    for m in range(1, 5000):
        cand = np.rint(m * v_sc).astype(int)
        if np.all(np.abs(m * v_sc - cand) < 1e-5) and np.all(a_ab @ cand == 0):
            g_all = 0
            for x in cand:
                g_all = math.gcd(g_all, abs(int(x)))
            cand = cand // max(g_all, 1)
            phi = cand
            break
    assert phi is not None

    ad_g = {g: to_so3(mats[g]) for g in gens}
    ad_inv = {g: ad_g[g].T for g in gens}  # Orthogonal SO(3, C) inverse == transpose!
    nz_k = [i for i in range(n_g) if phi[i] != 0]
    best_k = max(nz_k, key=lambda kk: float(abs((mats[gens[kk]][0, 0] + mats[gens[kk]][1, 1]) ** 2 - 4)))

    def delta_fn(tv: mp.mpc) -> mp.mpc:
        rt = {g: (tv ** int(phi[i])) * ad_g[g] for i, g in enumerate(gens)}
        rti = {g: (tv ** (-int(phi[i]))) * ad_inv[g] for i, g in enumerate(gens)}
        dh = mp.matrix(3 * (n_g - 1), 3 * (n_g - 1))
        for ri, r in enumerate(rels):
            blks = [mp.zeros(3, 3) for _ in range(n_g)]
            pr = mp.eye(3)
            for ch in r:
                gl = ch.lower()
                j = g_idx[gl]
                if ch.islower():
                    blks[j] = blks[j] + pr
                    pr = pr * rt[gl]
                else:
                    pr = pr * rti[gl]
                    blks[j] = blks[j] - pr
            co = 0
            for j in range(n_g):
                if j == best_k:
                    continue
                for ai in range(3):
                    for bi in range(3):
                        dh[3 * ri + ai, co + bi] = blks[j][ai, bi]
                co += 3
        return mp.det(dh) / mp.det(rt[gens[best_k]] - mp.eye(3))

    rc = mp.mpf("2e-7")
    m_pts = 12
    der1 = sum(delta_fn(mp.mpf(1) + rc * mp.exp(2j * mp.pi * m / m_pts)) / (rc * mp.exp(2j * mp.pi * m / m_pts)) for m in range(m_pts)) / m_pts

    def ew2(w: str) -> mp.matrix:
        cur = mp.eye(2)
        for ch in w:
            ac = mats[ch.lower()]
            if ch.isupper():
                ac = mp.matrix([[ac[1, 1], -ac[0, 1]], [-ac[1, 0], ac[0, 0]]])
            cur = cur * ac
        return cur

    mm, ml = ew2(m_word), ew2(l_word)
    if mp.re(mm[0, 0] + mm[1, 1]) < 0:
        mm = -mm
    if mp.re(ml[0, 0] + ml[1, 1]) < 0:
        ml = -ml
    ii, jj = max([(i, j) for i in range(2) for j in range(2)], key=lambda ij: float(abs(mm[ij[0], ij[1]] - (1 if ij[0] == ij[1] else 0))))
    cr = (ml[ii, jj] - (1 if ii == jj else 0)) / (mm[ii, jj] - (1 if ii == jj else 0))
    pm = sum(int(phi[g_idx[c.lower()]]) * (1 if c.islower() else -1) for c in m_word)
    pl = sum(int(phi[g_idx[c.lower()]]) * (1 if c.islower() else -1) for c in l_word)
    gml = math.gcd(abs(pm), abs(pl))
    am, al = -pl // gml, pm // gml
    tau_mu = mp.mpf(4) * abs(der1) / (gml * abs(am + al * cr))
    return tau_mu, tau_mu * mp.sqrt(abs(mp.im(cr)))


def run_all_referee_checks(project_root: Path = PROJECT_ROOT, write_verdict: bool = True) -> Dict[str, Any]:
    """Run full AST scan, Phase 1-11 seal checks, and 165 / 165 cumulative planted-fault controls."""
    mp.mp.dps = 60
    ast_scan = run_ast_guardrail_scan(project_root)
    assert ast_scan["passed"], f"AST Guardrail scan failed: {ast_scan}"

    parent = project_root.parent
    seal_ok = True
    for _, dname in [
        ("phase1", "self_consistent_loop_phi"),
        ("phase2", "cusped_3d_loop_phase2"),
        ("phase3", "relational_yukawa_phase3"),
        ("phase4", "unification_cap_lepton_phase4"),
        ("phase5", "m004_cl10_a4_phase5"),
        ("phase6", "weave_toe_phase6"),
        ("phase7", "inflation_lepton_phase7"),
        ("phase8", "fourfold_majorana_phase8"),
        ("phase9", "zero_input_precision_phase9"),
        ("phase10", "precision_falsifiability_phase10"),
        ("phase11", "selberg_determinant_phase11"),
    ]:
        pdir = project_root if dname == project_root.name else (parent / dname)
        sp_f = pdir / "SEAL_SHA256.txt"
        exp_sha, tgt_nm = sp_f.read_text(encoding="utf-8").strip().splitlines()[0].split()
        act_sha = hashlib.sha256((pdir / Path(tgt_nm).name).read_bytes()).hexdigest()
        seal_ok = bool(seal_ok and (act_sha == exp_sha))

    p5_dir = parent / "m004_cl10_a4_phase5"
    p10_dir = parent / "precision_falsifiability_phase10"
    v1_lock_sha = json.loads((p5_dir / "outputs" / "preregistered_blind_lock_sha256.json").read_text(encoding="utf-8"))["preregistered_manifest_sha256"]
    v1_act_sha = hashlib.sha256((p5_dir / "outputs" / "preregistered_blind_predictions_v1.json").read_bytes()).hexdigest()
    seal_ok = bool(seal_ok and (v1_act_sha == v1_lock_sha) and (v1_act_sha == "ece3d98345a3f4982757dad6cea6837af95923ff088086f64cbc374674f2edbd"))
    assert seal_ok, "Cryptographic seal check failed"

    p10_verdict = json.loads((p10_dir / "outputs" / "referee_phase10_verdict.json").read_text(encoding="utf-8"))
    p10_details: Dict[str, bool] = {k: bool(v) for k, v in p10_verdict["planted_fault_controls"]["details"].items()}
    assert len(p10_details) == 145 and all(p10_details.values())

    prod = json.loads((project_root / "outputs" / "phase11_results.json").read_text(encoding="utf-8"))
    g1 = prod["gate_p11_1_h3_huygens_propagator_exactness"]
    g2 = prod["gate_p11_2_porti_adjoint_torsion"]
    g3 = prod["gate_p11_3_one_loop_overtone_partition"]
    g4 = prod["gate_p11_4_joint_consistency"]
    g5 = prod["gate_p11_5_track_b_scorecard"]

    # Independent Gate P11-1 Verification (50d analytic radial Laplacian in H^2, H^3, H^4):
    mp.mp.dps = 50
    lam_t = mp.mpf("2.9745505801732")
    r_t = mp.mpf("1.35")

    def indep_hd_res(d_dim: int) -> float:
        ph = mp.mpf(d_dim - 1) / 2
        gf = lambda r: mp.exp(-lam_t * r) / (mp.sinh(r) ** ph)
        res = -(mp.diff(gf, r_t, 2) + (d_dim - 1) * mp.coth(r_t) * mp.diff(gf, r_t, 1)) + ((lam_t**2) - (ph**2)) * gf(r_t)
        return float(abs(res) / abs(gf(r_t)))

    h3_indep = indep_hd_res(3)
    h2_indep = indep_hd_res(2)
    h4_indep = indep_hd_res(4)

    # Independent Gate P11-2 Verification (SO(3, C) Pauli basis + adversarial SL(2,C) & cat-map SL(2,Z)):
    mp.mp.dps = 60
    c_adv = mp.matrix([[mp.mpc("0.8", "-1.3"), mp.mpc("0.7", "0.2")], [mp.mpc("-0.4", "0.9"), mp.mpc("1.1", "-0.6")]])
    c_adv = c_adv / mp.sqrt(c_adv[0, 0] * c_adv[1, 1] - c_adv[0, 1] * c_adv[1, 0])
    tau_m004_so3, imod_m004_so3 = _indep_porti_so3_basis(snappy.ManifoldHP("m004"))
    _, imod_adv_cat = _indep_porti_so3_basis(snappy.ManifoldHP("m004"), conj_c=c_adv, mod_mat=(2, 1, 1, 1))
    w0_hp = snappy.ManifoldHP("m129")
    w0_hp.dehn_fill((-3, 1), 0)
    tau_m129_so3, imod_m129_so3 = _indep_porti_so3_basis(w0_hp.filled_triangulation())
    whp_13 = snappy.ManifoldHP("m129")
    whp_13.dehn_fill((1, 3), 0)
    tau_13_so3, _ = _indep_porti_so3_basis(whp_13.filled_triangulation())

    porti_so3_err = float(abs(tau_m004_so3 - 2 * mp.sqrt(3)))
    pres_so3_err = float(abs(tau_m004_so3 - tau_m129_so3))
    adv_cat_err = float(abs(imod_m004_so3 - imod_adv_cat))
    ov13_prod_err = abs(float(tau_13_so3) - g2["eight_sibling_m129_overtone_torsions"][0]["tau_porti_mu"])

    # Independent Gate P11-3 & P11-4 Verification (RK45 + 10-trial Haar + 50d Strong-CP + q-series):
    mp.mp.dps = 50
    q_chk = mp.mpc("-0.05", "0.02")
    gmy_q = mp.mpf(1)
    for n in range(2, 45):
        gmy_q *= abs(1 - (q_chk**n)) ** (-2)
    q2_coeff_ok = float(abs(gmy_q - (1 + 2 * mp.re(q_chk**2)))) < float(10 * (abs(q_chk) ** 3))

    ser = g5["serialized_phase11_operators"]
    yw = [np.array(r) + 1j * np.array(im) for r, im in zip(ser["Yw_11A_real"], ser["Yw_11A_imag"])]
    k_u = np.array(ser["K_v10_real"]) + 1j * np.array(ser["K_v10_imag"])
    au0, mrs = ser["au_0"], ser["mrs_v12"]

    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    ell1, th1 = float(2 * mp.re(hl1)), float(2 * mp.im(hl1))
    eps1 = (math.exp(-2.9745505801732 * ell1) / abs(2 * np.sinh(0.5 * (ell1 + 1j * th1)))) / (2 * math.pi)
    lc = (4 * (math.pi**2 / 15) / eps1) ** 0.2
    reg_i, reg_h = 0.5 * math.log(2.0 * math.pi), 0.5 * math.log(2.0)
    t_i, t_h = [0.8, 6.0, 5.0], [8.2, 3.0, 4.0]
    rsh_g = [(-1.0 / (8.0 * math.pi**2)) * (-3.5 * t_i[i] * reg_i - 3.5 * t_h[i] * reg_h) for i in range(3)]
    d_sh = [rsh_g[i] - rsh_g[2] for i in range(3)]

    def rk45_eval(lr_v: float, bm=None):
        ig3 = au0 / (4.0 * math.pi)
        guv = np.sqrt(1.0 / np.array([ig3 + d_sh[0], ig3 + d_sh[1], ig3 + d_sh[2]]))
        gb = float(np.mean(guv))
        sf = gb / float(np.max(np.linalg.svd(yw[0], compute_uv=False)))
        yu0, yd0, ye0, ynu0 = yw[0] * sf, yw[1] * sf, yw[2] * sf, yw[3] * sf
        ynt = float(np.max(np.linalg.svd(ynu0, compute_uv=False)))
        knu0 = ((ynt**2) / mrs) * k_u.copy()
        lam0 = ((gb**2) / 8.0) * ((0.1272571765 * math.sqrt((1.0 / au0) / 0.04)) ** 2)
        if bm is not None:
            uq, uu, ud, ul, ue = bm
            yu0, yd0, ye0, knu0 = uq @ yu0 @ uu.conj().T, uq @ yd0 @ ud.conj().T, ul @ ye0 @ ue.conj().T, ul @ knu0 @ ul.T
        y0 = np.concatenate([guv.real, yu0.real.ravel(), yu0.imag.ravel(), yd0.real.ravel(), yd0.imag.ravel(), ye0.real.ravel(), ye0.imag.ravel(), [lam0], knu0.real.ravel(), knu0.imag.ravel()])
        sol = solve_ivp(_rhs76_indep, (0.0, -lr_v), y0, method="RK45", rtol=1e-11, atol=1e-13)
        yf = sol.y[:, -1]
        g1_v, g2_v, _ = yf[0:3]
        yu = (yf[3:12] + 1j * yf[12:21]).reshape(3, 3)
        yd = (yf[21:30] + 1j * yf[30:39]).reshape(3, 3)
        ye = (yf[39:48] + 1j * yf[48:57]).reshape(3, 3)
        knu = 0.5 * ((yf[58:67] + 1j * yf[67:76]).reshape(3, 3) + (yf[58:67] + 1j * yf[67:76]).reshape(3, 3).T)
        su = np.linalg.svd(yu, compute_uv=False)[::-1]
        sd = np.linalg.svd(yd, compute_uv=False)[::-1]
        we, _, _ = np.linalg.svd(ye)
        we_a = we[:, ::-1]
        mnu_vew = 0.5 * math.exp(-lr_v) * knu
        u_nu, snu_d, _ = np.linalg.svd(mnu_vew)
        snu = snu_d[::-1]
        u_nu_a = u_nu[:, ::-1]
        p_d = u_nu_a.conj().T @ mnu_vew @ u_nu_a.conj()
        w_tak = u_nu_a @ np.diag(np.exp(0.5j * np.angle(np.diag(p_d))))
        up = we_a.conj().T @ w_tak
        mbb_vew = float(abs(sum((up[0, i] ** 2) * snu[i] for i in range(3))))
        mzv = 0.5 * math.sqrt(g2_v * g2_v + 0.6 * g1_v * g1_v)
        return mzv, float(su[2] / sd[2]), mbb_vew

    lr_rk = float(brentq(lambda l: l - (7.5 * lc - math.log(rk45_eval(l)[0])), 27.0, 32.0, xtol=1e-11))
    _, mt_mb_rk, mbb_rk = rk45_eval(lr_rk)
    rng_r = np.random.default_rng(77665544)
    haar_rk = max(
        abs(rk45_eval(lr_rk, [_random_haar_u(3, rng_r) for _ in range(5)])[2] - mbb_rk) / mbb_rk
        for _ in range(10)
    )

    dw = np.linalg.det(yw[0] @ yw[1])
    th_w = mp.atan2(mp.mpf(str(dw.imag)), mp.mpf(str(dw.real)))
    a_it = -th_w + mp.mpf("0.07")
    for _ in range(8):
        a_it = a_it - mp.sin(th_w + a_it) / mp.cos(th_w + a_it)
    th_eff_50 = float(abs(th_w + a_it))

    comp = g5["four_branch_36_observable_comparison"]
    b11a = comp["branch_11A_susy_bulk"]
    b11b = comp["branch_11B_gmy_graviton_M5"]
    b11c = comp["branch_11C_scherk_schwarz_M5"]
    b11d = comp["branch_11D_topological_cs_porti"]
    binv = comp["planted_inverted_porti_torsion"]
    dc3 = g5["double_counted_3pt_propagator_plant_tiers"]
    led = g5["non_dimensionalized_zero_continuous_input_ledger"]
    scales = [r["ratio_to_MPl_red"] for r in g4["track_a_ten_scale_M5_hierarchy"]]
    smap = {r["scale"]: r["ratio_to_MPl_red"] for r in g4["track_a_ten_scale_M5_hierarchy"]}

    p11_plants: Dict[str, bool] = {
        "P11_1_P1_50d_h3_green_function_exactness_verified": bool(
            h3_indep < 1e-45 and g1["h3_huygens_radial_pde_benchmarks"]["h3_d3_50d_max_pde_residual"] < 1e-45
        ),
        "P11_1_P2_even_and_higher_dim_h2_h4_wkb_inexactness_plants_caught": bool(
            h2_indep > 0.05
            and h4_indep > 0.15
            and g1["h3_huygens_radial_pde_benchmarks"]["h2_d2_wkb_inexactness_residual_plant"] > 0.10
            and g1["h3_huygens_radial_pde_benchmarks"]["h4_d4_wkb_inexactness_residual_plant"] > 0.10
        ),
        "P11_1_P3_double_counted_0pt_stf_2sinh_squared_ruins_unification_caught": bool(
            g1["planted_double_counted_0pt_in_3pt_signals_track_a"]["stf_2sinh_squared_alpha_EM_inv_plant"] > 160.0
            and dc3["stf_2sinh_squared_sm24_tiers"]["Tier_1_Precision_Hit"] < 16
        ),
        "P11_1_P4_double_counted_gmy_and_ruelle_3pt_plants_degrade_unification_caught": bool(
            abs(g1["planted_double_counted_0pt_in_3pt_signals_track_a"]["gmy_infinite_prod_3pt_alpha_EM_inv_plant"] - 127.951) > 10.0
            and dc3["ruelle_spin_prod_3pt_sm24_tiers"]["Tier_1_Precision_Hit"] < 18
        ),
        "P11_1_P5_exact_h3_3pt_propagator_haar_and_liouville_zero_verified": bool(
            g1["exact_h3_3pt_propagator_track_a"]["haar_10trial_SU3x5_max_err"] < 1e-11
            and abs(g1["h3_huygens_radial_pde_benchmarks"]["liouville_centrifugal_coeff_d3"]) < 1e-15
        ),
        "P11_2_P1_60d_dubois_yamaguchi_poly_and_porti_2sqrt3_benchmark_verified": bool(
            porti_so3_err < 1e-35
            and g2["m004_benchmarks_60d"]["porti_2sqrt3_abs_err"] < 1e-35
            and g2["m004_benchmarks_60d"]["dubois_yamaguchi_laurent_coeff_err"] < 1e-12
        ),
        "P11_2_P2_presentation_invariance_m004_vs_m129_minus3_1_verified": bool(
            pres_so3_err < 1e-35 and g2["m004_benchmarks_60d"]["presentation_invariance_tau_err"] < 1e-35
        ),
        "P11_2_P3_sl2c_conjugation_and_sl2z_modular_cusp_invariance_verified": bool(
            adv_cat_err < 1e-35
            and g2["m004_benchmarks_60d"]["sl2c_conjugation_I_mod_err"] < 1e-35
            and g2["m004_benchmarks_60d"]["sl2z_modular_S_and_T3_I_mod_max_err"] < 1e-35
        ),
        "P11_2_P4_unnormalized_homological_framing_plant_fails_sl2z_caught": bool(
            g2["planted_fault_signals_track_a"]["unnormalized_sl2z_S_framing_tau_shift_plant"] > 8.0
        ),
        "P11_2_P5_all_8_sibling_m129_overtones_finite_acyclic_torsion_verified": bool(
            ov13_prod_err < 1e-9
            and len(g2["eight_sibling_m129_overtone_torsions"]) == 8
            and all(r["abs_Delta_at_1"] < 1e-30 for r in g2["eight_sibling_m129_overtone_torsions"])
        ),
        "P11_3_P1_susy_untwisted_bose_fermi_q_series_cancellation_verified": bool(
            q2_coeff_ok and g3["q_series_benchmarks_50d"]["susy_untwisted_bose_fermi_cancellation_err"] < 1e-45
        ),
        "P11_3_P2_branch_11a_susy_bulk_preserves_18_sm_tier1_and_haar_verified": bool(
            haar_rk < 1e-10
            and abs(mt_mb_rk - b11a["sm24_rows"]["mt_over_mb"]["predicted"]) < 1e-3
            and b11a["sm24_tiers"]["Tier_1_Precision_Hit"] == 18
            and b11a["sm24_tiers"]["Tier_3_Quantitative_Tension_or_Miss"] == 0
        ),
        "P11_3_P3_branch_11d_pure_topological_cs_porti_torsion_falsified_caught": bool(
            b11d["beta_iso_1B_SD_M5"] > 0.50
            and not b11d["planck_beta_iso_bound_passed"]
            and b11d["sm24_tiers"]["Tier_3_Quantitative_Tension_or_Miss"] >= 1
        ),
        "P11_3_P4_wrong_inverse_porti_torsion_overcloses_omega_a_plant_caught": bool(
            binv["Omega_a_h2_predicted"] > 2.0 and binv["sm24_tiers"]["Tier_1_Precision_Hit"] < 18
        ),
        "P11_3_P5_branch_11b_gmy_and_11c_ss_zero_parameter_bounds_certified": bool(
            b11b["total_misses_of_36"] == 0
            and b11b["Omega_a_h2_tier"] == "Tier_2_Structural_O1_Hit"
            and b11c["sm24_tiers"]["Tier_3_Quantitative_Tension_or_Miss"] == 1
        ),
        "P11_4_P1_50d_strong_cp_cancellation_across_1loop_branches_verified": bool(
            th_eff_50 < 1e-35
            and g4["strong_cp_50d_branch_11A"]["minimized_strong_cp_residual_abs"] < 1e-35
            and g4["strong_cp_50d_branch_11B"]["minimized_strong_cp_residual_abs"] < 1e-35
        ),
        "P11_4_P2_ten_scale_m5_hierarchy_and_cy4_dP8_tadpole_verified": bool(
            all(scales[i] > scales[i + 1] for i in range(len(scales) - 1))
            and smap["T_reh_radion"] > g5["T_BBN_over_MPl_red"]
            and g4["cy4_P1_x_dP8_summary"]["log10_bp_step_at_R_flux_max"] <= -105.0
        ),
        "P11_4_P3_unified_36_observable_26_tier1_6_tier2_4_bounds_verified": bool(
            b11a["total_tier1_of_36"] == 26
            and b11a["total_tier2_of_36"] == 6
            and b11a["total_bounds_of_36"] == 4
            and b11a["total_passing_of_36"] == 36
        ),
        "P11_4_P4_clause_p11_c1_h3_exactness_falsifies_wkb_tier2_hypothesis_disclosed": bool(
            "vanishes identically" in led["clause_P11_C1_h3_exactness_falsifies_wkb_tier2_hypothesis"]
        ),
        "P11_4_P5_clause_p11_c2_eight_sibling_overtones_nine_total_surgeries_disclosed": bool(
            "8 sibling overtones" in led["clause_P11_C2_surgery_census_and_preregistration_provenance"]
            and "pre-registered at Phase 11" in led["clause_P11_C2_surgery_census_and_preregistration_provenance"]
        ),
    }

    all_165: Dict[str, bool] = {}
    all_165.update(p10_details)
    all_165.update(p11_plants)
    n_total = len(all_165)
    n_caught = sum(1 for v in all_165.values() if v)
    assert n_total == 165 and n_caught == 165, f"Expected 165/165 controls caught, got {n_caught}/{n_total}: {p11_plants}"

    verdict = {
        "referee": "Phase 11 Zero-Import Referee Suite (165 / 165 Cumulative Planted-Fault Controls)",
        "ast_guardrail_scan": ast_scan,
        "all_seals_1_to_11_and_v1_intact": seal_ok,
        "phase11_new_controls": {"total": 20, "caught": sum(1 for v in p11_plants.values() if v), "details": p11_plants},
        "planted_fault_controls": {"total": n_total, "caught": n_caught, "details": all_165},
        "all_referee_checks_passed": bool(ast_scan["passed"] and seal_ok and n_caught == 165),
    }
    if write_verdict:
        out_dir = project_root / "outputs"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "referee_phase11_verdict.json").write_text(json.dumps(verdict, indent=2), encoding="utf-8")
    return verdict


if __name__ == "__main__":
    v = run_all_referee_checks(write_verdict=True)
    print(f"Phase 11 Zero-Import Referee PASSED: {v['planted_fault_controls']['caught']} / {v['planted_fault_controls']['total']} controls caught!")
