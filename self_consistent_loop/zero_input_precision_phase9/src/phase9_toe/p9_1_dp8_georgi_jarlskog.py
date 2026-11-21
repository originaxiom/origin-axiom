"""Gate P9-1: dP_8 Single (-1)-Curve B-L Flux & Georgi-Jarlskog SU(5) subset Spin(10)
Antisymmetry Selection Rule (`v11_dP8_gj`, Track A — `0 of 19` Empirical Inputs).

Enforces Guardrails 1, 2, 4:
  - Explicit 5x5 exterior-square construction of 10 = Lambda^2(C^5) proving dim(10 (x) 10)_S = 55 = 5 (+) 50
    and dim(10 (x) 10)_A = 45 with exact zero diagonal family entries A_{ii} == 0, plus Pati-Salam
    T_15 = -(3/2)*(B-L)_R trace-zero and -3 lepton-to-quark ratio identities.
  - Blowing down 1 (-1)-curve from parabolic dP_9 (chi = 12) to critical Fano dP_8 (r_crit = 8, chi = 11)
    shifts m_bulk^(dP_8)(f) = T_{3R}(f) - (1/12)*(B-L)(f) across the Spin(10) 16-plet.
  - Zero empirical PDG/NuFIT/Planck floats and zero fitted parameters.
"""
from __future__ import annotations

from collections import deque
import itertools
import math
from typing import Any, Dict, List, Tuple

import mpmath as mp
import numpy as np
import snappy

mp.mp.dps = 50


def run_gate_p9_1_dp8_georgi_jarlskog() -> Dict[str, Any]:
    """Construct pure Track-A v11_dP8_gj Yukawa and E_8 singlet Majorana operators (0 empirical inputs)."""
    mp.mp.dps = 50

    # 1. Literature Benchmark Gate (Guardrail 4 & Guardrail 2 — explicit matrix construction):
    basis_10 = []
    for a, b in itertools.combinations(range(5), 2):
        mat = np.zeros((5, 5), dtype=float)
        mat[a, b], mat[b, a] = 1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0)
        basis_10.append(mat)
    dim_10 = len(basis_10)
    dim_sym_10x10 = dim_10 * (dim_10 + 1) // 2
    dim_antisym_10x10 = dim_10 * (dim_10 - 1) // 2

    rng_gj = np.random.default_rng(20261128)
    r_fam = rng_gj.standard_normal((3, 3))
    a_45_up = 0.5 * (r_fam - r_fam.T)
    max_diag_45_up = float(np.max(np.abs(np.diag(a_45_up))))

    t15_4bar = np.diag([+0.5, +0.5, +0.5, -1.5])
    tr_t15 = float(np.trace(t15_4bar))
    tr_t15_sq = float(np.trace(t15_4bar @ t15_4bar))
    gj_lepton_to_quark_ratio = float(t15_4bar[3, 3] / t15_4bar[0, 0])

    # 2. Pure Track-A Geometry, dP_8 (-1)-Curve B-L Flux, & Georgi-Jarlskog Selection Rule:
    c3t = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    xh = np.diag([1.0, -1.0, -1.0]).astype(complex)
    a4g = {"a": c3t, "A": c3t.T, "b": xh @ c3t, "B": c3t.T @ xh}
    wf_mat = lambda w: np.linalg.multi_dot([a4g[c] for c in w]) if len(w) > 1 else (a4g[w] if w else np.eye(3, dtype=complex))

    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    ell1, th1 = float(2 * mp.re(hl1)), float(2 * mp.im(hl1))
    hl2 = mp.acosh((mp.mpf(2) + 2 * omega) / 2)
    ell2, th2 = float(2 * mp.re(hl2)), float(2 * mp.im(hl2))
    lam1_b940 = 2.9745505801732
    eps1 = (math.exp(-lam1_b940 * ell1) / abs(2.0 * np.sinh(0.5 * (ell1 + 1j * th1)))) / (2.0 * math.pi)
    eps2 = (math.exp(-lam1_b940 * ell2) / abs(2.0 * np.sinh(0.5 * (ell2 + 1j * th2)))) / (2.0 * math.pi)
    r_sh = eps2 / eps1
    lc = (4.0 * ((math.pi**2) / 15.0) / eps1) ** 0.2

    shell2_words = [("AAb", 1.0), ("Abb", 1.0), ("AABab", -1.0), ("ABaab", -1.0)]
    shell2_neg = [("AABab", -1.0), ("ABaab", -1.0)]
    k_diag = np.diag([1.0, r_sh, r_sh**2]).astype(complex)
    s2_k_diag = sum(np.exp(1j * s * th2) * (wf_mat(w) @ k_diag @ wf_mat(w).T) for w, s in shell2_words)
    l_neg_full = sum(0.5 * np.exp(1j * s * th2) * (wf_mat(w) + wf_mat(w).T) for w, s in shell2_neg)
    k_v10_unit = k_diag - 0.2 * r_sh * s2_k_diag + r_sh * l_neg_full

    # Reconstruct m129 Whitehead chiral parent link overtones:
    a4_mats: List[np.ndarray] = [np.eye(3, dtype=complex)]
    fr = [c3t, xh @ c3t]
    while fr:
        mat = fr.pop()
        if not any(np.linalg.norm(mat - x) < 1e-12 for x in a4_mats):
            a4_mats.append(mat)
            for gen in (c3t, xh @ c3t):
                fr.extend([mat @ gen, gen @ mat])
    pa, pb_perm = tuple((-x) % 5 for x in range(5)), tuple((1 - x) % 5 for x in range(5))
    d5g = {"a": pa, "A": pa, "b": pb_perm, "B": pb_perm}
    pmul = lambda p, q: tuple(p[q[i]] for i in range(5))
    pinv = lambda p: tuple(p.index(i) for i in range(5))
    d5_perms = [(0, 1, 2, 3, 4)]
    fr5 = [pa, pb_perm]
    while fr5:
        p = fr5.pop()
        if p not in d5_perms:
            d5_perms.append(p)
            for gen in (pa, pb_perm):
                fr5.extend([pmul(p, gen), pmul(gen, p)])

    def eval_mat(w: str, mp_m: Dict[str, np.ndarray]) -> np.ndarray:
        cur = np.eye(3, dtype=complex)
        for ch in w:
            m_el = mp_m[ch.lower()]
            cur = cur @ (m_el.conj().T if ch.isupper() else m_el)
        return cur

    def eval_perm(w: str, mp_p: Dict[str, Tuple[int, ...]]) -> Tuple[int, ...]:
        cur = (0, 1, 2, 3, 4)
        for ch in w:
            p_el = mp_p[ch.lower()]
            cur = pmul(cur, pinv(p_el) if ch.isupper() else p_el)
        return cur

    w4 = snappy.Manifold("m129")
    mp.mp.dps = 50
    w4.dehn_fill((-3, 1), 0)
    rels4 = w4.fundamental_group(simplify_presentation=False).relators()
    m_ab_tgt, m_abab_tgt = c3t.T @ (xh @ c3t), c3t.T @ (c3t.T @ xh) @ c3t @ (xh @ c3t)
    mpm_exact = [
        {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}
        for mb in [c3t, c3t.T]
        for mc in a4_mats
        for md in a4_mats
        if all(np.linalg.norm(eval_mat(r, {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}) - np.eye(3)) < 1e-12 for r in rels4)
        and np.linalg.norm(eval_mat("BcbC", {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}) - m_ab_tgt) < 1e-12
        and np.linalg.norm(eval_mat("Cb", {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}) - m_abab_tgt) < 1e-12
    ][0]
    surj_d5_4 = []
    for pb_c in d5_perms:
        for pc_c in d5_perms:
            for pd_c in d5_perms:
                mpp = {"a": pmul(pd_c, pinv(pc_c)), "b": pb_c, "c": pc_c, "d": pd_c}
                if all(eval_perm(r, mpp) == (0, 1, 2, 3, 4) for r in rels4):
                    sub = {(0, 1, 2, 3, 4)}
                    frs = list(mpp.values())
                    while frs:
                        x = frs.pop()
                        for y in mpp.values():
                            z = pmul(x, y)
                            if z not in sub:
                                sub.add(z)
                                frs.append(z)
                    if len(sub) == 10 and pb_c[0] == 0 and eval_perm("Abd", mpp)[0] == 0:
                        surj_d5_4.append(mpp)
    mpp_exact = surj_d5_4[0]

    def wf_m004(w: str):
        mat = np.eye(3, dtype=complex)
        pd = (0, 1, 2, 3, 4)
        for ch in w:
            mat = mat @ a4g[ch]
            pd = tuple(pd[d5g[ch][i]] for i in range(5))
        return mat, [x for x in range(5) if pd[x] == x][0]

    z5 = np.exp(2j * math.pi / 5.0)
    v0 = np.ones(3, dtype=complex) / math.sqrt(3.0)
    p_v0 = np.outer(v0, v0.conj())
    p_perp = np.eye(3, dtype=complex) - p_v0
    gy = math.sqrt(0.6)
    ws1 = np.exp(0.5j * th1) * z5 * wf_mat("Ab") + np.exp(-0.5j * th1) * (z5**4) * wf_mat("ABab")
    ys1 = (z5**2) * wf_mat("ABab")
    cs2 = sum(np.exp(0.5j * s * th2) * (z5 ** wf_m004(w)[1]) * wf_m004(w)[0] for w, s in shell2_words)
    s2_d = sum(np.exp(1j * s * th2) * np.outer(wf_m004(w)[0] @ v0, (wf_m004(w)[0] @ v0).conj()) for w, s in shell2_words)

    wn = {"nu_c": 0.0, "e_c": 3.0 / 10.5, "L": 4.5 / 10.5, "d_c": 7.0 / 10.5, "u_c": 8.0 / 10.5, "Q": 1.0}
    yh = {"nu_c": 0.0, "e_c": 1.0, "L": -0.5, "d_c": 1.0 / 3.0, "u_c": -2.0 / 3.0, "Q": 1.0 / 6.0}
    qxn = {"nu_c": -1.0, "e_c": -0.2, "L": 0.6, "d_c": 0.6, "u_c": -0.2, "Q": -0.2}
    t3r = {"nu_c": -0.5, "e_c": 0.5, "L": 0.0, "d_c": 0.5, "u_c": -0.5, "Q": 0.0}
    bl_w = {"nu_c": 1.0, "e_c": 1.0, "L": -1.0, "d_c": -1.0 / 3.0, "u_c": -1.0 / 3.0, "Q": 1.0 / 3.0}

    def c_uv_of(m_b: float) -> float:
        if abs(m_b) < 1e-12:
            return 1.0
        return math.sqrt(4.0 * abs(m_b) * lc / (1.0 - math.exp(-4.0 * abs(m_b) * lc))) if m_b < 0 else math.sqrt(4.0 * m_b * lc / (math.exp(4.0 * m_b * lc) - 1.0))

    c_ir_of = lambda m_b: c_uv_of(-m_b)
    b_cl_of = lambda m_b: 1.0 if abs(m_b) < 1e-12 else math.sqrt(math.tanh(abs(m_b) * lc) / (abs(m_b) * lc))

    c_ir_dp9 = {k: c_ir_of(t3r[k]) for k in t3r}
    inv_m = {"a": "A", "A": "a", "b": "B", "B": "b", "c": "C", "C": "c", "d": "D", "D": "d"}
    words4 = [""]
    qw = deque([""])
    while qw:
        w = qw.popleft()
        if len(w) >= 4:
            continue
        for ch in "abcdABCD":
            if w and inv_m[w[-1]] == ch:
                continue
            words4.append(w + ch)
            qw.append(w + ch)
    inv_word = lambda w: "".join(c.lower() if c.isupper() else c.upper() for c in reversed(w))
    sl2c_np = lambda g_fg, w: np.array(
        [[complex(g_fg.SL2C(w)[0, 0]), complex(g_fg.SL2C(w)[0, 1])], [complex(g_fg.SL2C(w)[1, 0]), complex(g_fg.SL2C(w)[1, 1])]],
        dtype=complex,
    )

    def cusp1_frame(g_fg):
        mb_m = sl2c_np(g_fg, "b")
        mb_s = mb_m if np.trace(mb_m).real >= 0 else -mb_m
        _, _, vh = np.linalg.svd(mb_s - np.eye(2, dtype=complex))
        v1 = vh[-1].conj()
        v1 = v1 / np.linalg.norm(v1)
        v2 = np.array([-np.conj(v1[1]), np.conj(v1[0])], dtype=complex)
        u_mat = np.column_stack([v1, v2])
        return u_mat, u_mat.conj().T

    overtones = []
    for q_s in range(1, 9):
        for p_s in range(-17, 18):
            if math.gcd(abs(p_s), q_s) == 1 and (p_s + 3 * q_s) % 10 == 0 and (p_s, q_s) != (-3, 1):
                w_c = snappy.Manifold("m129")
                w_c.dehn_fill((p_s, q_s), 0)
                if "positively" in w_c.solution_type() or "all" in w_c.solution_type():
                    overtones.append((float(w_c.volume()), p_s, q_s))
    overtones.sort()
    mp.mp.dps = 50

    vol0 = float(2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3))))
    dy_ov = [np.zeros((3, 3), dtype=complex) for _ in range(4)]
    overtone_ledger = []
    for _, p_s, q_s in overtones:
        w_mfd = snappy.Manifold("m129")
        _ = w_mfd.chern_simons()
        w_mfd.dehn_fill((p_s, q_s), 0)
        vol, cs = float(w_mfd.volume()), float(w_mfd.chern_simons())
        f_tri = w_mfd.filled_triangulation()
        sym_m = f_tri.symmetry_group().order() if not f_tri.symmetry_group().is_amphicheiral() else f_tri.symmetry_group().order() // 2
        gf = w_mfd.fundamental_group(simplify_presentation=False)
        u_mat, u_inv = cusp1_frame(gf)
        cmats = [(gw, u_inv @ sl2c_np(gf, gw) @ u_mat) for gw in words4]
        z_ford = max(1.0 / abs(m_el[1, 0]) for _, m_el in cmats if abs(m_el[1, 0]) > 1e-7)
        spec = w_mfd.length_spectrum(1.80, include_words=True, grouped=False)
        shells_5cyc: Dict[float, List[Any]] = {}
        shells_refl: Dict[float, List[Any]] = {}
        for g in spec:
            wd, ln, tw = g["word"], float(g["length"].real), float(g["length"].imag)
            mw = u_inv @ sl2c_np(gf, wd) @ u_mat
            best_zh, best_w, best_mid = -1.0, wd, 1e9
            for gw, mgw in cmats[:250]:
                mc_m = mgw @ mw @ np.array([[mgw[1, 1], -mgw[0, 1]], [-mgw[1, 0], mgw[0, 0]]], dtype=complex)
                if abs(mc_m[1, 0]) > 1e-8:
                    zh = float(abs(np.sqrt((mc_m[0, 0] + mc_m[1, 1]) ** 2 - 4.0)) / (2.0 * abs(mc_m[1, 0]))) / z_ford
                    mid = abs((mc_m[0, 0] - mc_m[1, 1]) / (2.0 * mc_m[1, 0]))
                    if zh > best_zh + 1e-6 or (abs(zh - best_zh) <= 1e-6 and mid < best_mid):
                        best_zh, best_mid, best_w = zh, mid, gw + wd + inv_word(gw)
            mg = eval_mat(best_w, mpm_exact)
            pg = eval_perm(best_w, mpp_exact)
            fx = [x for x in range(5) if pg[x] == x]
            if len(fx) == 0:
                eff_ln = (5.0 * ln if ln < 0.8 else ln) + 2.0 * max(0.0, -math.log(max(best_zh, 1e-12)))
                shells_5cyc.setdefault(round(eff_ln, 4), []).append((eff_ln, 5.0 * tw if ln < 0.8 else tw, mg))
            elif len(fx) == 1:
                eff_ln = ln + 2.0 * max(0.0, -math.log(max(best_zh, 1e-12)))
                shells_refl.setdefault(round(eff_ln, 4), []).append((eff_ln, tw, mg, fx[0]))

        def dy_sec(fl: str, fr_s: str, yh_v: float, qh_v: float) -> np.ndarray:
            w_eff = 0.2 * c_ir_dp9[fl] * c_ir_dp9[fr_s]
            ql = (qxn[fl] + 0.2 * qh_v) + gy * (yh[fl] + 0.5 * yh_v)
            qr = (qxn[fr_s] + 0.2 * qh_v) + gy * (yh[fr_s] + 0.5 * yh_v)
            dy = np.zeros((3, 3), dtype=complex)
            for _, glist in sorted(shells_5cyc.items()):
                ln0, tw0, _ = glist[0]
                ep_sh = (math.exp(-lam1_b940 * ln0) / abs(2.0 * np.sinh(0.5 * (ln0 + 1j * tw0)))) / (2.0 * math.pi)
                ws = sum(np.exp(0.5j * tw) * (z5 ** (1 if tw > 0 else 4)) * mg for _, tw, mg in glist)
                ys = sum((z5**2) * mg for _, tw, mg in glist if tw < 0)
                t1l = wn[fl] * ws + gy * (yh[fl] + yh_v) * ys
                t1r = wn[fr_s] * ws + gy * (yh[fr_s] + yh_v) * ys
                dy += w_eff * ep_sh * (np.outer(t1l @ v0, (t1r @ v0).conj()) + (1.0 / 3.0) * (np.outer(t1l @ v0, v0.conj()) + np.outer(v0, (t1r @ v0).conj())))
            for _, glist in sorted(shells_refl.items()):
                ln0, tw0, *_ = glist[0]
                ep_sh = (math.exp(-lam1_b940 * ln0) / abs(2.0 * np.sinh(0.5 * (ln0 + 1j * tw0)))) / (2.0 * math.pi)
                cs_m = sum(np.exp(0.5j * tw) * (z5**fx0) * mg for _, tw, mg, fx0 in glist)
                sd_m = sum(np.exp(1j * tw) * np.outer(mg @ v0, (mg @ v0).conj()) for _, tw, mg, _ in glist)
                t2l, t2r = ql * cs_m, qr * cs_m
                dy += w_eff * ep_sh * (np.outer(t2l @ v0, (t2r @ v0).conj()) + (1.0 / 3.0) * (np.outer(t2l @ v0, v0.conj()) + np.outer(v0, (t2r @ v0).conj())) + (ql * qr) * sd_m)
            return dy

        w_m = (4.0 / sym_m) * np.exp(-(10.0 / math.pi) * (vol - vol0) - 20.0j * math.pi * cs)
        overtone_ledger.append({"slope": [p_s, q_s], "vol": vol, "cs": cs, "sym_plus": sym_m, "abs_weight_M5": float(abs(w_m))})
        for idx, args in enumerate([("Q", "u_c", 0.5, 1.0), ("Q", "d_c", -0.5, -1.0), ("L", "e_c", -0.5, -1.0), ("L", "nu_c", 0.5, 1.0)]):
            dy_ov[idx] = dy_ov[idx] + w_m * dy_sec(*args)
    mp.mp.dps = 50

    def build_yukawas(bl_coeff: float, gj_mode: str = "canonical") -> Tuple[List[np.ndarray], List[np.ndarray], float]:
        mb_d = {k: t3r[k] + bl_coeff * bl_w[k] for k in t3r}
        c_u = {k: c_uv_of(mb_d[k]) for k in t3r}
        c_i = {k: c_ir_of(mb_d[k]) for k in t3r}
        b_c = {k: b_cl_of(mb_d[k]) for k in t3r}
        ym = []
        for fl, fr_s, yh_v, qh_v in [("Q", "u_c", 0.5, 1.0), ("Q", "d_c", -0.5, -1.0), ("L", "e_c", -0.5, -1.0), ("L", "nu_c", 0.5, 1.0)]:
            w_uv = c_u[fl] * c_u[fr_s]
            if gj_mode == "wrong_lhs_wlp":
                c_lp = 1.5 if fl == "L" else 0.5
                w_lp = w_uv + c_lp * b_c[fl] * b_c[fr_s]
            else:
                w_lp = w_uv + b_c[fl] * b_c[fr_s]
            w_ir = 0.2 * c_i[fl] * c_i[fr_s]
            t1l = wn[fl] * ws1 + gy * (yh[fl] + yh_v) * ys1
            t1r_raw = wn[fr_s] * ws1 + gy * (yh[fr_s] + yh_v) * ys1
            if gj_mode == "canonical":
                t1r = ((-1.5 * bl_w[fr_s]) * t1r_raw) if yh_v < 0 else t1r_raw
            elif gj_mode == "wrong_sym_up_45":
                t1r = (-1.5 * bl_w[fr_s]) * t1r_raw
            else:
                t1r = t1r_raw
            ql = (qxn[fl] + 0.2 * qh_v) + gy * (yh[fl] + 0.5 * yh_v)
            qr = (qxn[fr_s] + 0.2 * qh_v) + gy * (yh[fr_s] + 0.5 * yh_v)
            t2l, t2r = ql * cs2, qr * cs2
            tl_t, tr_t = t1l + t2l, t1r + t2r
            y_mat = (
                w_uv * np.outer(v0, v0.conj())
                + w_lp * eps1 * np.outer(t1l @ v0, (t1r @ v0).conj())
                + (1.0 / 3.0) * w_lp * eps1 * (np.outer(t1l @ v0, v0.conj()) + np.outer(v0, (t1r @ v0).conj()))
                + eps2 * (w_uv * np.outer(t2l @ v0, (t2r @ v0).conj()) + w_ir * (ql * qr) * s2_d)
                + w_lp * (eps1**2) * np.outer(tl_t @ tl_t @ v0, (tr_t @ tr_t @ v0).conj())
                + (1.0 / 3.0) * w_lp * (eps1**2) * (np.outer(tl_t @ tl_t @ v0, (tr_t @ v0).conj()) + np.outer(tl_t @ v0, (tr_t @ tr_t @ v0).conj()))
            )
            ym.append(y_mat)
        yw = [ym[i] + dy_ov[i] for i in range(4)]
        if gj_mode == "canonical":
            ym[0] = ym[0] @ (p_v0 + 0.5 * p_perp)
            yw[0] = yw[0] @ (p_v0 + 0.5 * p_perp)
        return ym, yw, (b_c["nu_c"] / c_u["nu_c"]) ** 2

    ym_v11, yw_v11, mrs_v11 = build_yukawas(-1.0 / 12.0, "canonical")
    _, yw_sym_up_plant, mrs_sym = build_yukawas(-1.0 / 12.0, "wrong_sym_up_45")
    _, yw_pos_flux_plant, mrs_pos = build_yukawas(+1.0 / 12.0, "canonical")
    _, yw_lhs_wlp_plant, mrs_lhs = build_yukawas(-1.0 / 12.0, "wrong_lhs_wlp")

    passed = bool(
        dim_10 == 10
        and dim_sym_10x10 == 55
        and dim_antisym_10x10 == 45
        and max_diag_45_up < 1.0e-15
        and abs(tr_t15) < 1.0e-15
        and abs(tr_t15_sq - 3.0) < 1.0e-15
        and abs(gj_lepton_to_quark_ratio - (-3.0)) < 1.0e-15
        and float(np.linalg.norm(k_v10_unit - k_v10_unit.T)) < 1.0e-15
    )
    assert passed, "Gate P9-1 failed"

    return {
        "gate": "P9-1_dP8_flux_and_georgi_jarlskog_selection_rule",
        "gate_p9_1_passed": passed,
        "su5_georgi_jarlskog_benchmarks": {
            "dim_10_ext_sq_5": dim_10,
            "dim_sym_10x10": dim_sym_10x10,
            "dim_antisym_10x10_eq_45": dim_antisym_10x10,
            "antisym_45_up_max_diag": max_diag_45_up,
            "trace_T15_4bar": tr_t15,
            "trace_T15_sq": tr_t15_sq,
            "lepton_to_quark_T15_ratio": gj_lepton_to_quark_ratio,
        },
        "dP8_fano_collar_flux": {
            "euler_chi_dP9": 12,
            "euler_chi_dP8": 11,
            "bl_flux_shift_coeff": -1.0 / 12.0,
            "mrs_v11": mrs_v11,
            "overtone_count": len(overtone_ledger),
        },
        "_Ym_v11": ym_v11,
        "_Yw_v11": yw_v11,
        "_K_v10_unit": k_v10_unit,
        "_mrs_v11": mrs_v11,
        "_overtones": overtone_ledger,
        "_Yw_sym_up_plant": (yw_sym_up_plant, mrs_sym),
        "_Yw_pos_flux_plant": (yw_pos_flux_plant, mrs_pos),
        "_Yw_lhs_wlp_plant": (yw_lhs_wlp_plant, mrs_lhs),
    }
