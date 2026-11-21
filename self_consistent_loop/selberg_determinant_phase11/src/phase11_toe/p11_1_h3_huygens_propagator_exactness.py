"""Gate P11-1: 50-Digit H^3 Huygens Propagator Exactness & Diagrammatic 3-Point vs 0-Point
Double-Counting Audit (`0 of 19` Track A — Zero Empirical Inputs, Guardrails 1-5).
"""
from __future__ import annotations

from collections import deque
import cmath
import json
import math
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import snappy

mp.mp.dps = 50
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _random_haar_u(n: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    q = q * (d / np.abs(d))
    return q / (np.linalg.det(q) ** (1.0 / n))


def _rhs76(_t: float, y: np.ndarray) -> np.ndarray:
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
        + (387.0 / 80.0 * g12 + 135.0 / 16.0 * g22 + 16.0 * g32) * he
    ) @ ye
    gp2 = 0.6 * g12
    dlam = c1 * (24.0 * (lam**2) + lam * (4.0 * tr_tot - 9.0 * g22 - 3.0 * gp2) - 2.0 * (3.0 * tu2 + 3.0 * td2 + te2) + 1.125 * (g22**2) + 0.75 * g22 * gp2 + 0.375 * (gp2**2)) + c2 * (
        -312.0 * (lam**3) - 144.0 * (lam**2) * tu + 36.0 * (lam**2) * (3.0 * g22 + gp2) - 3.0 * lam * (tu**2)
        + lam * tu * (80.0 * g32 + 22.5 * g22 + (85.0 / 6.0) * gp2) - 32.0 * g32 * (tu**2) - (8.0 / 3.0) * gp2 * (tu**2) + 30.0 * (tu**3)
    )
    dknu = c1 * (-1.5 * (he @ knu + knu @ he.T) + (-3.0 * g22 + 4.0 * lam + 2.0 * tr_tot) * knu)
    return np.concatenate([dg.real, dyu.real.ravel(), dyu.imag.ravel(), dyd.real.ravel(), dyd.imag.ravel(), dye.real.ravel(), dye.imag.ravel(), [float(dlam)], dknu.real.ravel(), dknu.imag.ravel()])


def _radial_hd_wkb_residual_50d(dim_d: int, r_val: mp.mpf, lam_val: mp.mpf) -> mp.mpf:
    """Evaluate 50-digit radial hyperbolic PDE residual |(-Delta_{H^d} + lam^2 - (d-1)^2/4) G_WKB(r)| / |G_WKB(r)|
    for G_WKB(r) = exp(-lam * r) / (4*pi * sinh(r)^{(d-1)/2}) via mpmath.diff!"""
    mp.mp.dps = 50
    p_half = mp.mpf(dim_d - 1) / mp.mpf(2)
    g_fn = lambda r: mp.exp(-lam_val * r) / (4 * mp.pi * (mp.sinh(r) ** p_half))
    dg = mp.diff(g_fn, r_val, 1)
    d2g = mp.diff(g_fn, r_val, 2)
    lap_g = d2g + mp.mpf(dim_d - 1) * mp.coth(r_val) * dg
    shift = (lam_val**2) - (p_half**2)
    res = -lap_g + shift * g_fn(r_val)
    return abs(res) / abs(g_fn(r_val))


def run_gate_p11_1_h3_huygens_propagator_exactness() -> Dict[str, Any]:
    """Prove 50-digit H^3 Huygens exactness of the 3-point geodesic propagator vs H^2/H^4 WKB non-exactness
    and vs diagrammatic 0-point Selberg trace double-counting plants (Track A, 0 empirical inputs)."""
    mp.mp.dps = 50
    p10 = json.loads((PROJECT_ROOT.parent / "precision_falsifiability_phase10" / "outputs" / "phase10_results.json").read_text(encoding="utf-8"))
    ser10 = p10["gate_p10_5_track_b_scorecard"]["serialized_v12_operators"]

    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    hl2 = mp.acosh((mp.mpf(2) + 2 * omega) / 2)
    ell1_mp, th1_mp = 2 * mp.re(hl1), 2 * mp.im(hl1)
    ell2_mp, th2_mp = 2 * mp.re(hl2), 2 * mp.im(hl2)
    lam1_mp = mp.mpf("2.9745505801732")

    # 1. 50-Digit H^3 Huygens PDE Exactness vs H^2 (d=2) and H^4 (d=4) Centrifugal Curvature Residuals:
    test_radii = [ell1_mp, ell2_mp, mp.mpf("2.5")]
    h3_max_res = float(max(_radial_hd_wkb_residual_50d(3, r_v, lam1_mp) for r_v in test_radii))
    h2_ell1_res = float(_radial_hd_wkb_residual_50d(2, ell1_mp, lam1_mp))
    h4_ell1_res = float(_radial_hd_wkb_residual_50d(4, ell1_mp, lam1_mp))

    # Centrifugal Liouville potential coefficient (d-1)(d-3)/4:
    centrifugal_coeff_d2 = float((2 - 1) * (2 - 3) / 4.0)
    centrifugal_coeff_d3 = float((3 - 1) * (3 - 3) / 4.0)
    centrifugal_coeff_d4 = float((4 - 1) * (4 - 3) / 4.0)

    # 2. Construct Pure Track-A Geodesic Propagator Operator Builder to Test 3-Point vs 0-Point Double-Counting Plants:
    ell1, th1 = float(ell1_mp), float(th1_mp)
    ell2, th2 = float(ell2_mp), float(th2_mp)
    lam1 = float(lam1_mp)
    vol_m5 = float(10 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3))))
    vol0 = vol_m5 / 5.0

    c3t = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    xh = np.diag([1.0, -1.0, -1.0]).astype(complex)
    a4g = {"a": c3t, "A": c3t.T, "b": xh @ c3t, "B": c3t.T @ xh}
    wf_mat = lambda w: np.linalg.multi_dot([a4g[c] for c in w]) if len(w) > 1 else (a4g[w] if w else np.eye(3, dtype=complex))

    a4_mats = [np.eye(3, dtype=complex)]
    fr = [c3t, xh @ c3t]
    while fr:
        m_cur = fr.pop()
        if not any(np.linalg.norm(m_cur - x_m) < 1e-12 for x_m in a4_mats):
            a4_mats.append(m_cur)
            for g_m in (c3t, xh @ c3t):
                fr.extend([m_cur @ g_m, g_m @ m_cur])

    pa = tuple((-x) % 5 for x in range(5))
    pb = tuple((1 - x) % 5 for x in range(5))
    d5g = {"a": pa, "A": pa, "b": pb, "B": pb}
    pmul = lambda p, q: tuple(p[q[i]] for i in range(5))
    pinv = lambda p: tuple(p.index(i) for i in range(5))
    d5_perms = [(0, 1, 2, 3, 4)]
    fr5 = [pa, pb]
    while fr5:
        p = fr5.pop()
        if p not in d5_perms:
            d5_perms.append(p)
            for g_p in (pa, pb):
                fr5.extend([pmul(p, g_p), pmul(g_p, p)])

    def eval_mat(w: str, mp_m: Dict[str, np.ndarray]) -> np.ndarray:
        cur = np.eye(3, dtype=complex)
        for ch in w:
            m_c = mp_m[ch.lower()]
            cur = cur @ (m_c.conj().T if ch.isupper() else m_c)
        return cur

    def eval_perm(w: str, mp_p: Dict[str, Tuple[int, ...]]) -> Tuple[int, ...]:
        cur = (0, 1, 2, 3, 4)
        for ch in w:
            p = mp_p[ch.lower()]
            cur = pmul(cur, pinv(p) if ch.isupper() else p)
        return cur

    w4 = snappy.Manifold("m129")
    w4.dehn_fill((-3, 1), 0)
    rels4 = w4.fundamental_group(simplify_presentation=False).relators()
    m_ab_tgt = c3t.T @ (xh @ c3t)
    m_abab_tgt = c3t.T @ (c3t.T @ xh) @ c3t @ (xh @ c3t)
    mpm_exact = [
        {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}
        for mb in [c3t, c3t.T]
        for mc in a4_mats
        for md in a4_mats
        if all(np.linalg.norm(eval_mat(r, {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}) - np.eye(3)) < 1e-12 for r in rels4)
        and np.linalg.norm(eval_mat("BcbC", {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}) - m_ab_tgt) < 1e-12
        and np.linalg.norm(eval_mat("Cb", {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}) - m_abab_tgt) < 1e-12
    ][0]

    mpp_exact = None
    for p_b in d5_perms:
        for p_c in d5_perms:
            for p_d in d5_perms:
                mpp = {"a": pmul(p_d, pinv(p_c)), "b": p_b, "c": p_c, "d": p_d}
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
                    if len(sub) == 10 and p_b[0] == 0 and eval_perm("Abd", mpp)[0] == 0:
                        mpp_exact = mpp
                        break
            if mpp_exact is not None:
                break
        if mpp_exact is not None:
            break
    assert mpp_exact is not None

    def wf_m004(w: str) -> Tuple[np.ndarray, int]:
        m_acc = np.eye(3, dtype=complex)
        pd = (0, 1, 2, 3, 4)
        for ch in w:
            m_acc = m_acc @ a4g[ch]
            pd = tuple(pd[d5g[ch][i]] for i in range(5))
        return m_acc, [x for x in range(5) if pd[x] == x][0]

    inv_m = {"a": "A", "A": "a", "b": "B", "B": "b", "c": "C", "C": "c", "d": "D", "D": "d"}
    words4 = [""]
    qw: deque[str] = deque([""])
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
    sl2c_np = lambda g_fg, w: np.array([[complex(g_fg.SL2C(w)[0, 0]), complex(g_fg.SL2C(w)[0, 1])], [complex(g_fg.SL2C(w)[1, 0]), complex(g_fg.SL2C(w)[1, 1])]], dtype=complex)

    def cusp1_frame(g_fg: Any) -> Tuple[np.ndarray, np.ndarray]:
        mb = sl2c_np(g_fg, "b")
        mb_s = mb if np.trace(mb).real >= 0 else -mb
        _, _, vh = np.linalg.svd(mb_s - np.eye(2, dtype=complex))
        v1 = vh[-1].conj()
        v1 = v1 / np.linalg.norm(v1)
        v2 = np.array([-np.conj(v1[1]), np.conj(v1[0])], dtype=complex)
        u_f = np.column_stack([v1, v2])
        return u_f, u_f.conj().T

    ov_cache = []
    for ov in ser10["overtones"]:
        p_s, q_s = ov["slope"]
        w_mfd = snappy.Manifold("m129")
        _ = w_mfd.chern_simons()
        w_mfd.dehn_fill((p_s, q_s), 0)
        vol, cs, sym_m = float(ov["vol"]), float(ov["cs"]), int(ov["sym_plus"])
        gf = w_mfd.fundamental_group(simplify_presentation=False)
        u_f, u_inv = cusp1_frame(gf)
        cmats = [(gw, u_inv @ sl2c_np(gf, gw) @ u_f) for gw in words4]
        z_ford = max(1.0 / abs(m_x[1, 0]) for _, m_x in cmats if abs(m_x[1, 0]) > 1e-7)
        spec = w_mfd.length_spectrum(1.80, include_words=True, grouped=False)
        s5: Dict[float, List[Any]] = {}
        sr: Dict[float, List[Any]] = {}
        for g in spec:
            wd, ln, tw = g["word"], float(g["length"].real), float(g["length"].imag)
            mw = u_inv @ sl2c_np(gf, wd) @ u_f
            best_zh, best_w, best_mid = -1.0, wd, 1e9
            for gw, mgw in cmats[:250]:
                mc = mgw @ mw @ np.array([[mgw[1, 1], -mgw[0, 1]], [-mgw[1, 0], mgw[0, 0]]], dtype=complex)
                if abs(mc[1, 0]) > 1e-8:
                    zh = float(abs(np.sqrt((mc[0, 0] + mc[1, 1]) ** 2 - 4.0)) / (2.0 * abs(mc[1, 0]))) / z_ford
                    mid = abs((mc[0, 0] - mc[1, 1]) / (2.0 * mc[1, 0]))
                    if zh > best_zh + 1e-6 or (abs(zh - best_zh) <= 1e-6 and mid < best_mid):
                        best_zh, best_mid, best_w = zh, mid, gw + wd + inv_word(gw)
            mg = eval_mat(best_w, mpm_exact)
            pg = eval_perm(best_w, mpp_exact)
            fx = [x for x in range(5) if pg[x] == x]
            if len(fx) == 0:
                prim_l = 5.0 * ln if ln < 0.8 else ln
                eff_ln = prim_l + 2.0 * max(0.0, -math.log(max(best_zh, 1e-12)))
                s5.setdefault(round(eff_ln, 4), []).append((eff_ln, 5.0 * tw if ln < 0.8 else tw, prim_l, mg))
            elif len(fx) == 1:
                eff_ln = ln + 2.0 * max(0.0, -math.log(max(best_zh, 1e-12)))
                sr.setdefault(round(eff_ln, 4), []).append((eff_ln, tw, ln, mg, fx[0]))
        w_m = (4.0 / sym_m) * cmath.exp(-(10.0 / math.pi) * (vol - vol0) - 20.0j * math.pi * cs)
        ov_cache.append(((p_s, q_s), w_m, s5, sr))

    z5 = np.exp(2j * math.pi / 5.0)
    v0 = np.ones(3, dtype=complex) / math.sqrt(3.0)
    p_v0 = np.outer(v0, v0.conj())
    p_perp = np.eye(3, dtype=complex) - p_v0
    gy = math.sqrt(0.6)
    cos_r = math.sqrt(0.6)
    shell2_words = [("AAb", 1.0), ("Abb", 1.0), ("AABab", -1.0), ("ABaab", -1.0)]
    shell2_neg = [("AABab", -1.0), ("ABaab", -1.0)]
    ws1 = np.exp(0.5j * th1) * z5 * wf_mat("Ab") + np.exp(-0.5j * th1) * (z5**4) * wf_mat("ABab")
    ys1 = (z5**2) * wf_mat("ABab")
    cs2 = sum(np.exp(0.5j * s * th2) * (z5 ** wf_m004(w)[1]) * wf_m004(w)[0] for w, s in shell2_words)
    s2_d = sum(np.exp(1j * s * th2) * np.outer(wf_m004(w)[0] @ v0, (wf_m004(w)[0] @ v0).conj()) for w, s in shell2_words)

    wn = {"nu_c": 0.0, "e_c": 3.0 / 10.5, "L": 4.5 / 10.5, "d_c": 7.0 / 10.5, "u_c": 8.0 / 10.5, "Q": 1.0}
    yh = {"nu_c": 0.0, "e_c": 1.0, "L": -0.5, "d_c": 1.0 / 3.0, "u_c": -2.0 / 3.0, "Q": 1.0 / 6.0}
    qxn = {"nu_c": -1.0, "e_c": -0.2, "L": 0.6, "d_c": 0.6, "u_c": -0.2, "Q": -0.2}
    t3r = {"nu_c": -0.5, "e_c": 0.5, "L": 0.0, "d_c": 0.5, "u_c": -0.5, "Q": 0.0}
    bl_w = {"nu_c": 1.0, "e_c": 1.0, "L": -1.0, "d_c": -1.0 / 3.0, "u_c": -1.0 / 3.0, "Q": 1.0 / 3.0}

    reg_i, reg_h = 0.5 * math.log(2.0 * math.pi), 0.5 * math.log(2.0)
    t_i, t_h = [0.8, 6.0, 5.0], [8.2, 3.0, 4.0]
    rsh_g = [(-1.0 / (8.0 * math.pi**2)) * (-3.5 * t_i[i] * reg_i - 3.5 * t_h[i] * reg_h) for i in range(3)]
    d_sh = [rsh_g[i] - rsh_g[2] for i in range(3)]

    def eval_propagator_kernel(ker_fn: Callable[[float, float, float, float], float], bm: Optional[List[np.ndarray]] = None) -> Dict[str, Any]:
        ep1 = ker_fn(ell1, th1, ell1, 1.0)
        ep2 = ker_fn(ell2, th2, ell2, -1.0)
        r_sh = ep2 / ep1
        lc = (4.0 * ((math.pi**2) / 15.0) / ep1) ** 0.2
        au_2w = (9.0 * vol_m5 * ((2.0 * lc) ** 3)) / (30.0 * (math.pi**3)) - math.log(math.pi)

        def c_uv(m_b: float) -> float:
            if abs(m_b) < 1e-12:
                return 1.0
            return math.sqrt(4.0 * abs(m_b) * lc / (1.0 - math.exp(-4.0 * abs(m_b) * lc))) if m_b < 0 else math.sqrt(4.0 * m_b * lc / (math.exp(4.0 * m_b) * lc - 1.0))

        # Exact collar localization profile:
        c_uv_exact = lambda m_b: 1.0 if abs(m_b) < 1e-12 else (math.sqrt(4.0 * abs(m_b) * lc / (1.0 - math.exp(-4.0 * abs(m_b) * lc))) if m_b < 0 else math.sqrt(4.0 * m_b * lc / (math.exp(4.0 * m_b * lc) - 1.0)))
        c_ir_exact = lambda m_b: c_uv_exact(-m_b)
        b_cl = lambda m_b: 1.0 if abs(m_b) < 1e-12 else math.sqrt(math.tanh(abs(m_b) * lc) / (abs(m_b) * lc))

        c_ir_dp9 = {k: c_ir_exact(t3r[k]) for k in t3r}
        per_ov_dy: Dict[Tuple[int, int], List[np.ndarray]] = {}
        per_ov_wm: Dict[Tuple[int, int], complex] = {}
        dy_ov_tot = [np.zeros((3, 3), dtype=complex) for _ in range(4)]

        for sl_key, w_m, s5, sr in ov_cache:
            per_ov_wm[sl_key] = w_m
            dy_4: List[np.ndarray] = []
            for idx, (fl, fr_k, yh_v, qh_v) in enumerate([("Q", "u_c", 0.5, 1.0), ("Q", "d_c", -0.5, -1.0), ("L", "e_c", -0.5, -1.0), ("L", "nu_c", 0.5, 1.0)]):
                w_eff = 0.2 * c_ir_dp9[fl] * c_ir_dp9[fr_k]
                ql = (qxn[fl] + 0.2 * qh_v) + gy * (yh[fl] + 0.5 * yh_v)
                qr = (qxn[fr_k] + 0.2 * qh_v) + gy * (yh[fr_k] + 0.5 * yh_v)
                dy = np.zeros((3, 3), dtype=complex)
                for _, glist in sorted(s5.items()):
                    ln0, tw0, pl0, _ = glist[0]
                    ep_s = ker_fn(ln0, tw0, pl0, 1.0)
                    ws = sum(np.exp(0.5j * tw) * (z5 ** (1 if tw > 0 else 4)) * mg for _, tw, _, mg in glist)
                    ys = sum((z5**2) * mg for _, tw, _, mg in glist if tw < 0)
                    t1l = wn[fl] * ws + gy * (yh[fl] + yh_v) * ys
                    t1r = wn[fr_k] * ws + gy * (yh[fr_k] + yh_v) * ys
                    dy += w_eff * ep_s * (np.outer(t1l @ v0, (t1r @ v0).conj()) + (1.0 / 3.0) * (np.outer(t1l @ v0, v0.conj()) + np.outer(v0, (t1r @ v0).conj())))
                for _, glist in sorted(sr.items()):
                    ln0, tw0, pl0, *_ = glist[0]
                    ep_s = ker_fn(ln0, tw0, pl0, -1.0)
                    cs_m = sum(np.exp(0.5j * tw) * (z5**fx0) * mg for _, tw, _, mg, fx0 in glist)
                    sd_m = sum(np.exp(1j * tw) * np.outer(mg @ v0, (mg @ v0).conj()) for _, tw, _, mg, _ in glist)
                    t2l, t2r = ql * cs_m, qr * cs_m
                    dy += w_eff * ep_s * (np.outer(t2l @ v0, (t2r @ v0).conj()) + (1.0 / 3.0) * (np.outer(t2l @ v0, v0.conj()) + np.outer(v0, (t2r @ v0).conj())) + (ql * qr) * sd_m)
                if idx == 0:
                    dy_dressed = dy @ (p_v0 + 0.5 * p_perp)
                elif idx in (1, 2):
                    dy_dressed = dy * cos_r
                else:
                    dy_dressed = dy
                dy_4.append(dy_dressed)
                dy_ov_tot[idx] = dy_ov_tot[idx] + w_m * dy_dressed
            per_ov_dy[sl_key] = dy_4

        mb_d = {k: t3r[k] - (1.0 / 12.0) * bl_w[k] for k in t3r}
        c_u = {k: c_uv_exact(mb_d[k]) for k in t3r}
        c_i = {k: c_ir_exact(mb_d[k]) for k in t3r}
        b_c = {k: b_cl(mb_d[k]) for k in t3r}
        ym_list: List[np.ndarray] = []
        for idx, (fl, fr_k, yh_v, qh_v) in enumerate([("Q", "u_c", 0.5, 1.0), ("Q", "d_c", -0.5, -1.0), ("L", "e_c", -0.5, -1.0), ("L", "nu_c", 0.5, 1.0)]):
            w_uv = c_u[fl] * c_u[fr_k]
            w_lp = w_uv + b_c[fl] * b_c[fr_k]
            w_ir = 0.2 * c_i[fl] * c_i[fr_k]
            t1l = wn[fl] * ws1 + gy * (yh[fl] + yh_v) * ys1
            t1r = ((-1.5 * bl_w[fr_k]) if yh_v < 0 else 1.0) * (wn[fr_k] * ws1 + gy * (yh[fr_k] + yh_v) * ys1)
            ql = (qxn[fl] + 0.2 * qh_v) + gy * (yh[fl] + 0.5 * yh_v)
            qr = (qxn[fr_k] + 0.2 * qh_v) + gy * (yh[fr_k] + 0.5 * yh_v)
            t2l, t2r = ql * cs2, qr * cs2
            tl_t, tr_t = t1l + t2l, t1r + t2r
            ym = (
                w_uv * np.outer(v0, v0.conj())
                + w_lp * ep1 * np.outer(t1l @ v0, (t1r @ v0).conj())
                + (1.0 / 3.0) * w_lp * ep1 * (np.outer(t1l @ v0, v0.conj()) + np.outer(v0, (t1r @ v0).conj()))
                + ep2 * (w_uv * np.outer(t2l @ v0, (t2r @ v0).conj()) + w_ir * (ql * qr) * s2_d)
                + w_lp * (ep1**2) * np.outer(tl_t @ tl_t @ v0, (tr_t @ tr_t @ v0).conj())
                + (1.0 / 3.0) * w_lp * (ep1**2) * (np.outer(tl_t @ tl_t @ v0, (tr_t @ v0).conj()) + np.outer(tl_t @ v0, (tr_t @ tr_t @ v0).conj()))
            )
            if idx == 0:
                ym = ym @ (p_v0 + 0.5 * p_perp)
            elif idx in (1, 2):
                ym = ym * cos_r
            ym_list.append(ym)

        yw_list = [ym_list[i] + dy_ov_tot[i] for i in range(4)]
        mrs = (b_c["nu_c"] / c_u["nu_c"]) ** 2
        k_diag = np.diag([1.0, r_sh, r_sh**2]).astype(complex)
        s2_k = sum(np.exp(1j * s * th2) * (wf_mat(w) @ k_diag @ wf_mat(w).T) for w, s in shell2_words)
        l_neg = sum(0.5 * np.exp(1j * s * th2) * (wf_mat(w) + wf_mat(w).T) for w, s in shell2_neg)
        k_u = k_diag - 0.2 * r_sh * s2_k + r_sh * l_neg

        def rge_at(lr_v: float, b_m: Optional[List[np.ndarray]] = None) -> Tuple[float, float, float, Dict[str, float]]:
            ig3 = au_2w / (4.0 * math.pi)
            guv = np.sqrt(1.0 / np.array([ig3 + d_sh[0], ig3 + d_sh[1], ig3 + d_sh[2]]))
            gb = float(np.mean(guv))
            sf = gb / float(np.max(np.linalg.svd(yw_list[0], compute_uv=False)))
            yu0, yd0, ye0, ynu0 = yw_list[0] * sf, yw_list[1] * sf, yw_list[2] * sf, yw_list[3] * sf
            ynt = float(np.max(np.linalg.svd(ynu0, compute_uv=False)))
            knu0 = ((ynt**2) / mrs) * k_u.copy()
            lam0 = ((gb**2) / 8.0) * ((0.1272571765 * math.sqrt((1.0 / au_2w) / 0.04)) ** 2)
            if b_m is not None:
                uq, uu, ud, ul, ue = b_m
                yu0, yd0, ye0, knu0 = uq @ yu0 @ uu.conj().T, uq @ yd0 @ ud.conj().T, ul @ ye0 @ ue.conj().T, ul @ knu0 @ ul.T
            y0 = np.concatenate([guv.real, yu0.real.ravel(), yu0.imag.ravel(), yd0.real.ravel(), yd0.imag.ravel(), ye0.real.ravel(), ye0.imag.ravel(), [lam0], knu0.real.ravel(), knu0.imag.ravel()])
            sol = solve_ivp(_rhs76, (0.0, -lr_v), y0, method="DOP853", rtol=1e-11, atol=1e-13)
            yf = sol.y[:, -1]
            g1_v, g2_v, g3_v = yf[0:3]
            yu = (yf[3:12] + 1j * yf[12:21]).reshape(3, 3)
            yd = (yf[21:30] + 1j * yf[30:39]).reshape(3, 3)
            ye = (yf[39:48] + 1j * yf[48:57]).reshape(3, 3)
            lam = float(yf[57])
            knu = 0.5 * ((yf[58:67] + 1j * yf[67:76]).reshape(3, 3) + (yf[58:67] + 1j * yf[67:76]).reshape(3, 3).T)
            wu, su_d, _ = np.linalg.svd(yu)
            wd, sd_d, _ = np.linalg.svd(yd)
            we, se_d, _ = np.linalg.svd(ye)
            wnu, snu_d, _ = np.linalg.svd(knu)
            wu_a, su = wu[:, ::-1], su_d[::-1]
            wd_a, sd = wd[:, ::-1], sd_d[::-1]
            we_a, se = we[:, ::-1], se_d[::-1]
            wnu_a, snu = wnu[:, ::-1], snu_d[::-1]
            vc = wu_a.conj().T @ wd_a
            avc = np.abs(vc)
            jq = abs(float(np.imag(vc[0, 1] * vc[1, 2] * np.conj(vc[0, 2]) * np.conj(vc[1, 1]))))
            up = we_a.conj().T @ wnu_a
            aup = np.abs(up)
            s13_sq = float(aup[0, 2] ** 2)
            c13_sq = max(1.0 - s13_sq, 1e-15)
            mw_v = float(0.5 * g2_v)
            mh_v = math.sqrt(2.0 * max(lam, 0.0))
            mz_v = float(0.5 * math.sqrt(g2_v * g2_v + 0.6 * g1_v * g1_v))
            aem_inv = float((4.0 * math.pi) * (1.0 / (0.6 * g1_v * g1_v) + 1.0 / (g2_v * g2_v)))
            a3 = float((g3_v * g3_v) / (4.0 * math.pi))
            return mz_v, aem_inv, a3, {
                "sin2_thetaW_MZ_MSbar": float((0.6 * g1_v * g1_v) / (g2_v * g2_v + 0.6 * g1_v * g1_v)),
                "MW_over_vEW": mw_v,
                "MZ_over_vEW": mz_v,
                "mH_over_vEW": mh_v,
                "mH_over_MW": mh_v / mw_v,
                "m_t_over_vEW": float(su[2] / math.sqrt(2.0)),
                "mt_over_mb": float(su[2] / sd[2]),
                "mb_over_mtau": float(sd[2] / se[2]),
                "mc_over_mt": float(su[1] / su[2]),
                "mu_over_mc": float(su[0] / su[1]),
                "ms_over_mb": float(sd[1] / sd[2]),
                "md_over_ms": float(sd[0] / sd[1]),
                "mmu_over_mtau": float(se[1] / se[2]),
                "me_over_mmu": float(se[0] / se[1]),
                "V_us": float(avc[0, 1]),
                "V_cb": float(avc[1, 2]),
                "V_ub": float(avc[0, 2]),
                "abs_J_q": jq,
                "sin2_theta12": float((aup[0, 1] ** 2) / c13_sq),
                "sin2_theta23": float((aup[1, 2] ** 2) / c13_sq),
                "sin2_theta13": s13_sq,
                "abs_J_lep_max": abs(float(np.imag(up[0, 1] * up[1, 2] * np.conj(up[0, 2]) * np.conj(up[1, 1])))),
                "delta_m21_sq_over_delta_m31_sq": float((snu[1] ** 2 - snu[0] ** 2) / (snu[2] ** 2 - snu[0] ** 2)),
                "mnu3_over_vEW": 0.5 * math.exp(-lr_v) * float(snu[2]),
            }

        lr_fp = float(brentq(lambda l: l - (7.5 * lc - math.log(rge_at(l)[0])), 20.0, 42.0, xtol=1e-11))
        _, aem_inv, a3, pr = rge_at(lr_fp, bm)
        return {
            "Lc": float(lc),
            "au_2w": float(au_2w),
            "lr_fp": float(lr_fp),
            "alpha_EM_inv_MZ_pred": float(aem_inv),
            "alpha_s_MZ_pred": float(a3),
            "sm24_pred": pr,
            "_Ym_base": ym_list,
            "_Yw_weave": yw_list,
            "_per_ov_dy": per_ov_dy,
            "_per_ov_wm": per_ov_wm,
            "_K_u": k_u,
            "_mrs": float(mrs),
            "_mpp_exact": mpp_exact,
        }

    ker_exact_h3 = lambda el, th, _pl, _sp: (math.exp(-lam1 * el) / abs(2.0 * cmath.sinh(0.5 * (el + 1j * th)))) / (2.0 * math.pi)
    ker_plant_stf_sq = lambda el, th, pl, _sp: (pl * math.exp(-lam1 * el) / (abs(2.0 * cmath.sinh(0.5 * (el + 1j * th))) ** 2)) / (2.0 * math.pi)

    def ker_plant_gmy_3pt(el: float, th: float, _pl: float, _sp: float) -> float:
        q = cmath.exp(-(el + 1j * th))
        pr_h = 1.0
        for n in range(2, 50):
            pr_h *= abs(1.0 - (q**n)) ** 2
        return (math.exp(-lam1 * el) / (abs(2.0 * cmath.sinh(0.5 * (el + 1j * th))) * pr_h)) / (2.0 * math.pi)

    def ker_plant_ruelle_3pt(el: float, th: float, _pl: float, sp: float) -> float:
        q = cmath.exp(-(el + 1j * th))
        rc = 1.0
        for n in range(1, 50):
            rc *= abs(1.0 - sp * (q**n)) / abs(1.0 - (q**n))
        return rc * (math.exp(-lam1 * el) / abs(2.0 * cmath.sinh(0.5 * (el + 1j * th)))) / (2.0 * math.pi)

    exact_res = eval_propagator_kernel(ker_exact_h3)
    plant_stf_sq = eval_propagator_kernel(ker_plant_stf_sq)
    plant_gmy_3pt = eval_propagator_kernel(ker_plant_gmy_3pt)
    plant_ruelle_3pt = eval_propagator_kernel(ker_plant_ruelle_3pt)

    # 10-trial SU(3)^5 Haar check on exact H^3 propagator:
    rng_h = np.random.default_rng(20261141)
    keys_s = sorted(exact_res["sm24_pred"].keys())
    v_ref = np.array([exact_res["sm24_pred"][k] for k in keys_s])
    haar_max = 0.0
    for _ in range(10):
        pr_h = eval_propagator_kernel(ker_exact_h3, [_random_haar_u(3, rng_h) for _ in range(5)])["sm24_pred"]
        vr = np.array([pr_h[k] for k in keys_s])
        haar_max = max(haar_max, float(np.max(np.abs(vr - v_ref) / np.maximum(np.abs(v_ref), 1.0))))

    passed = bool(
        h3_max_res < 1.0e-45
        and h2_ell1_res > 0.10
        and h4_ell1_res > 0.10
        and abs(centrifugal_coeff_d3) < 1.0e-15
        and haar_max < 1.0e-11
        and abs(plant_stf_sq["alpha_EM_inv_MZ_pred"] - exact_res["alpha_EM_inv_MZ_pred"]) > 30.0
    )
    assert passed, "Gate P11-1 failed"

    return {
        "gate": "P11-1_h3_huygens_propagator_exactness_and_double_counting_audit",
        "gate_p11_1_passed": passed,
        "h3_huygens_radial_pde_benchmarks": {
            "h3_d3_50d_max_pde_residual": h3_max_res,
            "h2_d2_wkb_inexactness_residual_plant": h2_ell1_res,
            "h4_d4_wkb_inexactness_residual_plant": h4_ell1_res,
            "liouville_centrifugal_coeff_d2": centrifugal_coeff_d2,
            "liouville_centrifugal_coeff_d3": centrifugal_coeff_d3,
            "liouville_centrifugal_coeff_d4": centrifugal_coeff_d4,
        },
        "exact_h3_3pt_propagator_track_a": {
            "Lc": exact_res["Lc"],
            "alpha_GUT_inv_2wall_0": exact_res["au_2w"],
            "ln_MKK_MZ_0": exact_res["lr_fp"],
            "alpha_EM_inv_MZ_pred": exact_res["alpha_EM_inv_MZ_pred"],
            "alpha_s_MZ_pred": exact_res["alpha_s_MZ_pred"],
            "haar_10trial_SU3x5_max_err": haar_max,
            "sm24_predictions": exact_res["sm24_pred"],
        },
        "planted_double_counted_0pt_in_3pt_signals_track_a": {
            "stf_2sinh_squared_alpha_EM_inv_plant": plant_stf_sq["alpha_EM_inv_MZ_pred"],
            "stf_2sinh_squared_sm24_plant": plant_stf_sq["sm24_pred"],
            "gmy_infinite_prod_3pt_alpha_EM_inv_plant": plant_gmy_3pt["alpha_EM_inv_MZ_pred"],
            "gmy_infinite_prod_3pt_sm24_plant": plant_gmy_3pt["sm24_pred"],
            "ruelle_spin_prod_3pt_alpha_EM_inv_plant": plant_ruelle_3pt["alpha_EM_inv_MZ_pred"],
            "ruelle_spin_prod_3pt_sm24_plant": plant_ruelle_3pt["sm24_pred"],
        },
        "_Ym_base": exact_res["_Ym_base"],
        "_Yw_weave": exact_res["_Yw_weave"],
        "_per_ov_dy": exact_res["_per_ov_dy"],
        "_per_ov_wm": exact_res["_per_ov_wm"],
        "_K_u": exact_res["_K_u"],
        "_mrs": exact_res["_mrs"],
        "_mpp_exact": exact_res["_mpp_exact"],
        "_overtones_meta": ser10["overtones"],
    }
