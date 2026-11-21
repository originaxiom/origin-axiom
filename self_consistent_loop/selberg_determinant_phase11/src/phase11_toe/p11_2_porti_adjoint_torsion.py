"""Gate P11-2: 60-Digit Wada-Dubois-Yamaguchi-Porti Adjoint sl(2, C) Reidemeister Torsion
& SL(2, Z) Modular Cusp Invariance Across m004 and All 8 Sibling m129(p, q) Overtones
(`0 of 19` Track A — Zero Empirical Inputs, Guardrails 1, 2, 4, 6).
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple

import mpmath as mp
import numpy as np
import snappy

mp.mp.dps = 60


def _sl2_to_ad3_mp(a_mat: mp.matrix) -> mp.matrix:
    a, b = a_mat[0, 0], a_mat[0, 1]
    c, d = a_mat[1, 0], a_mat[1, 1]
    return mp.matrix([
        [a * a, 2 * a * b, b * b],
        [a * c, a * d + b * c, b * d],
        [c * c, 2 * c * d, d * d],
    ])


def _extract_hp_holonomy(m_hp: Any) -> Tuple[List[str], List[str], Dict[str, mp.matrix], Tuple[str, str]]:
    mp.mp.dps = 60
    g_fg = m_hp.fundamental_group(simplify_presentation=True)
    gens = list(g_fg.generators())
    rels = list(g_fg.relators())
    m_word, l_word = g_fg.peripheral_curves()[0]
    qstr = lambda q: str(q).replace(" ", "")
    mats: Dict[str, mp.matrix] = {}
    for g in gens:
        m0 = g_fg.SL2C(g)
        a_m = mp.matrix([
            [mp.mpc(qstr(m0[0][0].real()), qstr(m0[0][0].imag())), mp.mpc(qstr(m0[0][1].real()), qstr(m0[0][1].imag()))],
            [mp.mpc(qstr(m0[1][0].real()), qstr(m0[1][0].imag())), mp.mpc(qstr(m0[1][1].real()), qstr(m0[1][1].imag()))],
        ])
        mats[g] = a_m / mp.sqrt(a_m[0, 0] * a_m[1, 1] - a_m[0, 1] * a_m[1, 0])
    return gens, rels, mats, (m_word, l_word)


def _compute_porti_from_rep(
    gens: List[str],
    rels: List[str],
    mats: Dict[str, mp.matrix],
    m_word: str,
    l_word: str,
    extract_laurent: bool = False,
) -> Dict[str, Any]:
    mp.mp.dps = 60
    n_g = len(gens)
    assert len(rels) == n_g - 1
    g_idx = {g: i for i, g in enumerate(gens)}

    a_ab = np.zeros((len(rels), n_g), dtype=int)
    for r_i, r in enumerate(rels):
        for ch in r:
            a_ab[r_i, g_idx[ch.lower()]] += 1 if ch.islower() else -1
    _, _, vh = np.linalg.svd(a_ab.astype(float))
    v = vh[-1]
    v_sc = v / min(abs(x) for x in v if abs(x) > 1e-8)
    phi: Optional[np.ndarray] = None
    for m in range(1, 5000):
        cand = np.rint(m * v_sc).astype(int)
        if np.all(np.abs(m * v_sc - cand) < 1e-5) and np.all(a_ab @ cand == 0):
            g_all = 0
            for x in cand:
                g_all = math.gcd(g_all, abs(int(x)))
            cand = cand // max(g_all, 1)
            if cand[np.argmax(np.abs(cand))] < 0:
                cand = -cand
            phi = cand
            break
    assert phi is not None

    ad_g = {g: _sl2_to_ad3_mp(mats[g]) for g in gens}
    ad_inv = {g: _sl2_to_ad3_mp(mp.matrix([[mats[g][1, 1], -mats[g][0, 1]], [-mats[g][1, 0], mats[g][0, 0]]])) for g in gens}

    max_rel_err = mp.mpf(0)
    for r in rels:
        cur = mp.eye(3)
        for ch in r:
            cur = cur * (ad_inv[ch.lower()] if ch.isupper() else ad_g[ch.lower()])
        err_r = mp.sqrt(sum(abs(cur[i, j] - (1 if i == j else 0)) ** 2 for i in range(3) for j in range(3)))
        if err_r > max_rel_err:
            max_rel_err = err_r

    nz_k = [i for i in range(n_g) if phi[i] != 0]
    best_k = max(nz_k, key=lambda kk: float(abs((mats[gens[kk]][0, 0] + mats[gens[kk]][1, 1]) ** 2 - 4)))

    def delta_mp(t_val: mp.mpc) -> mp.mpc:
        rt = {g: (t_val ** int(phi[i])) * ad_g[g] for i, g in enumerate(gens)}
        rti = {g: (t_val ** (-int(phi[i]))) * ad_inv[g] for i, g in enumerate(gens)}
        d_hat = mp.matrix(3 * (n_g - 1), 3 * (n_g - 1))
        for r_idx, r in enumerate(rels):
            blks = [mp.zeros(3, 3) for _ in range(n_g)]
            pref = mp.eye(3)
            for ch in r:
                gl = ch.lower()
                j = g_idx[gl]
                if ch.islower():
                    blks[j] = blks[j] + pref
                    pref = pref * rt[gl]
                else:
                    pref = pref * rti[gl]
                    blks[j] = blks[j] - pref
            col_off = 0
            for j in range(n_g):
                if j == best_k:
                    continue
                for a_i in range(3):
                    for b_i in range(3):
                        d_hat[3 * r_idx + a_i, col_off + b_i] = blks[j][a_i, b_i]
                col_off += 3
        return mp.det(d_hat) / mp.det(rt[gens[best_k]] - mp.eye(3))

    r_c = mp.mpf("1e-7")
    m_pts = 16
    vals = [delta_mp(mp.mpf(1) + r_c * mp.exp(2j * mp.pi * m / m_pts)) for m in range(m_pts)]
    val_1 = sum(vals) / m_pts
    der_1 = sum(vals[m] / (r_c * mp.exp(2j * mp.pi * m / m_pts)) for m in range(m_pts)) / m_pts

    laurent_coeffs: Dict[str, float] = {}
    if extract_laurent:
        n_fft = 32
        r_fft = mp.mpf("1.07")
        f_fft = [delta_mp(r_fft * mp.exp(2j * mp.pi * m / n_fft)) for m in range(n_fft)]
        for deg in range(-4, 5):
            c_d = (sum(f_fft[m] * mp.exp(-2j * mp.pi * deg * m / n_fft) for m in range(n_fft)) / n_fft) / (r_fft**deg)
            if abs(c_d) > mp.mpf("1e-12"):
                laurent_coeffs[str(deg)] = float(mp.re(c_d))

    def ew2(w: str) -> mp.matrix:
        cur = mp.eye(2)
        for ch in w:
            a_c = mats[ch.lower()]
            if ch.isupper():
                a_c = mp.matrix([[a_c[1, 1], -a_c[0, 1]], [-a_c[1, 0], a_c[0, 0]]])
            cur = cur * a_c
        return cur

    mm, ml = ew2(m_word), ew2(l_word)
    if mp.re(mm[0, 0] + mm[1, 1]) < 0:
        mm = -mm
    if mp.re(ml[0, 0] + ml[1, 1]) < 0:
        ml = -ml
    ii, jj = max([(i, j) for i in range(2) for j in range(2)], key=lambda ij: float(abs(mm[ij[0], ij[1]] - (1 if ij[0] == ij[1] else 0))))
    cusp_ratio = (ml[ii, jj] - (1 if ii == jj else 0)) / (mm[ii, jj] - (1 if ii == jj else 0))

    phi_m = sum(int(phi[g_idx[c.lower()]]) * (1 if c.islower() else -1) for c in m_word)
    phi_l = sum(int(phi[g_idx[c.lower()]]) * (1 if c.islower() else -1) for c in l_word)
    g_ml = math.gcd(abs(phi_m), abs(phi_l))
    a_m, a_l = -phi_l // g_ml, phi_m // g_ml

    tau_mu = mp.mpf(4) * abs(der_1) / (g_ml * abs(a_m + a_l * cusp_ratio))
    tau_lhom = mp.mpf(4) * abs(der_1) / g_ml
    i_mod = tau_mu * mp.sqrt(abs(mp.im(cusp_ratio)))
    return {
        "n_generators": int(n_g),
        "phi": [int(x) for x in phi.tolist()],
        "phi_m_l": [int(phi_m), int(phi_l)],
        "relator_err_60d": float(max_rel_err),
        "abs_Delta_at_1": float(abs(val_1)),
        "abs_Delta_prime_at_1": float(abs(der_1)),
        "cusp_modulus_re": float(mp.re(cusp_ratio)),
        "cusp_modulus_im": float(mp.im(cusp_ratio)),
        "tau_porti_mu": float(tau_mu),
        "tau_porti_lam_hom": float(tau_lhom),
        "I_porti_modular": float(i_mod),
        "laurent_real_coeffs": laurent_coeffs,
        "_tau_mu_mp": tau_mu,
        "_i_mod_mp": i_mod,
        "_abs_dp1_mp": abs(der_1),
    }


def run_gate_p11_2_porti_adjoint_torsion(g1_raw: Dict[str, Any]) -> Dict[str, Any]:
    """Verify 60-digit Porti/Dubois-Yamaguchi adjoint torsion on m004, m129(-3,1), SL(2,C)/SL(2,Z) transforms,
    and all 8 sibling m129(p, q) surgeries (`0 of 19` Track A)."""
    mp.mp.dps = 60
    gens0, rels0, mats0, (mw0, lw0) = _extract_hp_holonomy(snappy.ManifoldHP("m004"))
    r_m004 = _compute_porti_from_rep(gens0, rels0, mats0, mw0, lw0, extract_laurent=True)

    w0_hp = snappy.ManifoldHP("m129")
    w0_hp.dehn_fill((-3, 1), 0)
    gens1, rels1, mats1, (mw1, lw1) = _extract_hp_holonomy(w0_hp.filled_triangulation())
    r_m129_31 = _compute_porti_from_rep(gens1, rels1, mats1, mw1, lw1)

    # 1. SL(2, C) Conjugation Invariance Check g_j -> C g_j C^{-1}:
    c_conj = mp.matrix([[mp.mpc("1.7", "0.4"), mp.mpc("-0.9", "1.1")], [mp.mpc("0.3", "-0.8"), mp.mpc("0.5", "-0.2")]])
    c_conj = c_conj / mp.sqrt(c_conj[0, 0] * c_conj[1, 1] - c_conj[0, 1] * c_conj[1, 0])
    c_inv = mp.matrix([[c_conj[1, 1], -c_conj[0, 1]], [-c_conj[1, 0], c_conj[0, 0]]])
    mats0_conj = {g: c_conj * mats0[g] * c_inv for g in gens0}
    r_conj = _compute_porti_from_rep(gens0, rels0, mats0_conj, mw0, lw0)

    # 2. SL(2, Z) Peripheral Modular S-Transformation (mu', lam') = (lam, -mu) and T^3 Transformation (mu, lam + 3*mu):
    inv_word = lambda w: "".join(c.lower() if c.isupper() else c.upper() for c in reversed(w))
    r_mod_s = _compute_porti_from_rep(gens0, rels0, mats0, lw0, inv_word(mw0))
    r_mod_t3 = _compute_porti_from_rep(gens0, rels0, mats0, mw0, lw0 + mw0 + mw0 + mw0)

    mp.mp.dps = 60
    bench_2sqrt3_err = float(abs(r_m004["_tau_mu_mp"] - 2 * mp.sqrt(3)))
    bench_dp1_err = float(abs(r_m004["_abs_dp1_mp"] - mp.mpf(3)))
    pres_tau_err = float(abs(r_m004["_tau_mu_mp"] - r_m129_31["_tau_mu_mp"]))
    pres_imod_err = float(abs(r_m004["_i_mod_mp"] - r_m129_31["_i_mod_mp"]))
    conj_imod_err = float(abs(r_m004["_i_mod_mp"] - r_conj["_i_mod_mp"]))
    sl2z_imod_max_err = float(max(abs(r_m004["_i_mod_mp"] - r_mod_s["_i_mod_mp"]), abs(r_m004["_i_mod_mp"] - r_mod_t3["_i_mod_mp"])))
    unnormalized_s_frame_violation_plant = float(abs(r_mod_s["tau_porti_mu"] - r_m004["tau_porti_mu"]))

    lc = r_m004["laurent_real_coeffs"]
    poly_coeff_err = max(
        abs(abs(lc.get("-3", 0.0)) - 1.0),
        abs(abs(lc.get("-2", 0.0)) - 6.0),
        abs(abs(lc.get("-1", 0.0)) - 6.0),
        abs(abs(lc.get("0", 0.0)) - 1.0),
    )

    # 3. All 8 Sibling 1-Cusp m129(p, q) Whitehead Surgeries (`9` total surgeries including `(-3, 1)`):
    overtone_torsion_rows = []
    ov_map: Dict[Tuple[int, int], Dict[str, float]] = {}
    for ov in g1_raw["_overtones_meta"]:
        p_s, q_s = int(ov["slope"][0]), int(ov["slope"][1])
        whp = snappy.ManifoldHP("m129")
        whp.dehn_fill((p_s, q_s), 0)
        g_ov, r_ov, m_ov, (mw_ov, lw_ov) = _extract_hp_holonomy(whp.filled_triangulation())
        ro = _compute_porti_from_rep(g_ov, r_ov, m_ov, mw_ov, lw_ov)
        row = {
            "slope": [p_s, q_s],
            "vol": float(ov["vol"]),
            "cs": float(ov["cs"]),
            "abs_Delta_at_1": ro["abs_Delta_at_1"],
            "tau_porti_mu": ro["tau_porti_mu"],
            "tau_porti_lam_hom": ro["tau_porti_lam_hom"],
            "I_porti_modular": ro["I_porti_modular"],
            "one_loop_cs_weight_mu": math.sqrt(r_m004["tau_porti_mu"] / ro["tau_porti_mu"]),
            "one_loop_cs_weight_modular": math.sqrt(r_m004["I_porti_modular"] / ro["I_porti_modular"]),
        }
        overtone_torsion_rows.append(row)
        ov_map[(p_s, q_s)] = row

    all_acyclic = all(r["abs_Delta_at_1"] < 1.0e-30 and r["I_porti_modular"] > r_m004["I_porti_modular"] for r in overtone_torsion_rows)

    passed = bool(
        bench_2sqrt3_err < 1.0e-35
        and bench_dp1_err < 1.0e-35
        and poly_coeff_err < 1.0e-12
        and pres_tau_err < 1.0e-35
        and pres_imod_err < 1.0e-35
        and conj_imod_err < 1.0e-35
        and sl2z_imod_max_err < 1.0e-35
        and unnormalized_s_frame_violation_plant > 8.0
        and len(overtone_torsion_rows) == 8
        and all_acyclic
    )
    assert passed, f"Gate P11-2 failed: {bench_2sqrt3_err}, {pres_tau_err}, {all_acyclic}"

    r_m004_pub = {k: v for k, v in r_m004.items() if not k.startswith("_")}
    r_m129_pub = {k: v for k, v in r_m129_31.items() if not k.startswith("_")}

    return {
        "gate": "P11-2_wada_dubois_yamaguchi_porti_60d_adjoint_torsion",
        "gate_p11_2_passed": passed,
        "m004_benchmarks_60d": {
            "m004_record": r_m004_pub,
            "m129_minus3_1_record": r_m129_pub,
            "porti_2sqrt3_abs_err": bench_2sqrt3_err,
            "dubois_yamaguchi_dp1_eq_3_abs_err": bench_dp1_err,
            "dubois_yamaguchi_laurent_coeff_err": float(poly_coeff_err),
            "presentation_invariance_tau_err": pres_tau_err,
            "presentation_invariance_I_mod_err": pres_imod_err,
            "sl2c_conjugation_I_mod_err": conj_imod_err,
            "sl2z_modular_S_and_T3_I_mod_max_err": sl2z_imod_max_err,
        },
        "eight_sibling_m129_overtone_torsions": overtone_torsion_rows,
        "total_m129_hyperbolic_surgeries_in_mod10_family": 1 + len(overtone_torsion_rows),
        "planted_fault_signals_track_a": {
            "unnormalized_sl2z_S_framing_tau_shift_plant": unnormalized_s_frame_violation_plant,
        },
        "_ov_torsion_map": ov_map,
        "_m004_tau_mu": r_m004["tau_porti_mu"],
        "_m004_I_mod": r_m004["I_porti_modular"],
    }
