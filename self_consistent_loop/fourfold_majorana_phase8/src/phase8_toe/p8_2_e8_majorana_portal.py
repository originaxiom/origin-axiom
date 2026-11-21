"""Gate P8-2 (Track A, `0 of 19`): E_8 -> Spin(10) x SU(4) Root Enumeration & Zero-Parameter
(1, 15) Singlet Negative-Torsion Shell-2 Linear Seesaw Portal (`v10_e8_weave`).

Strictly 0 empirical inputs (zero PDG/NuFIT/Planck float literals).
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


def _random_haar_u(n: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    q = q * (d / np.abs(d))
    return q / (np.linalg.det(q) ** (1.0 / n))


def run_gate_p8_2_e8_majorana_portal() -> Dict[str, Any]:
    mp.mp.dps = 50

    # 1. Literature Benchmark Gate (Guardrail 4):
    # (a) Explicit enumeration of 240 roots + 8 Cartans = 248 of E_8 under Spin(10) x SU(4):
    r_d5, r_d3, r_10_6, r_16_4, r_16b_4b = 0, 0, 0, 0, 0
    for idx in itertools.combinations(range(8), 2):
        for _s1, _s2 in itertools.product([-1, 1], repeat=2):
            in5 = sum(1 for k in idx if k < 5)
            if in5 == 2:
                r_d5 += 1
            elif in5 == 0:
                r_d3 += 1
            else:
                r_10_6 += 1
    for signs in itertools.product([-1, 1], repeat=8):
        if signs.count(-1) % 2 == 0:
            if signs[:5].count(-1) % 2 == 0:
                r_16_4 += 1
            else:
                r_16b_4b += 1
    e8_branching = {
        "dim_45_1": r_d5 + 5,
        "dim_1_15": r_d3 + 3,
        "dim_10_6": r_10_6,
        "dim_16_4": r_16_4,
        "dim_16bar_4bar": r_16b_4b,
        "total_dim": (r_d5 + 5) + (r_d3 + 3) + r_10_6 + r_16_4 + r_16b_4b,
    }

    # (b) Exact 50-digit 9x9 Malinsky-Romao-Valle (PRL 95 (2005) 161801) Schur-complement sign & eigenvalue check:
    rng_b = np.random.default_rng(20261124)
    m_d = 0.1 * (rng_b.standard_normal((3, 3)) + 1j * rng_b.standard_normal((3, 3)))
    m_s = 0.05 * (rng_b.standard_normal((3, 3)) + 1j * rng_b.standard_normal((3, 3)))
    M_R = 1.0e8 * np.diag([1.0, 0.4, 0.2]).astype(complex)
    M_S = 5.0e8 * np.eye(3, dtype=complex)
    M_NS = 1.0e5 * np.eye(3, dtype=complex)
    M_big = np.block([
        [np.zeros((3, 3), dtype=complex), m_d, m_s],
        [m_d.T, M_R, M_NS],
        [m_s.T, M_NS.T, M_S],
    ])
    M_heavy = np.block([[M_R, M_NS], [M_NS.T, M_S]])
    M_eff_exact = -np.hstack([m_d, m_s]) @ np.linalg.inv(M_heavy) @ np.vstack([m_d.T, m_s.T])
    M_R_inv = np.linalg.inv(M_R)
    M_S_inv = np.linalg.inv(M_S)
    M_eff_lead = (
        -m_d @ M_R_inv @ m_d.T
        + m_d @ M_R_inv @ M_NS @ M_S_inv @ m_s.T
        + m_s @ M_S_inv @ M_NS.T @ M_R_inv @ m_d.T
        - m_s @ M_S_inv @ m_s.T
    )
    M_big_mp = mp.matrix(M_big.tolist())
    M_h_mp = mp.matrix(M_heavy.tolist())
    m_row_mp = mp.matrix(np.hstack([m_d, m_s]).tolist())
    M_eff_mp = -m_row_mp * (M_h_mp**-1) * m_row_mp.T
    sv_9x9 = sorted(float(x) for x in mp.svd_c(M_big_mp, compute_uv=False))[:3]
    sv_eff = sorted(float(x) for x in mp.svd_c(M_eff_mp, compute_uv=False))
    mrv_9x9_rel_err = float(max(abs(a - b) / b for a, b in zip(sv_9x9, sv_eff)))
    mrv_schur_sign_rel_err = float(np.linalg.norm(M_eff_exact - M_eff_lead) / np.linalg.norm(M_eff_exact))

    # 2. Pure Track-A Geometry & Zero-Parameter E_8 Shell-2 Linear Seesaw Operator:
    C3T = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    Xh = np.diag([1.0, -1.0, -1.0]).astype(complex)
    a4g = {"a": C3T, "A": C3T.T, "b": Xh @ C3T, "B": C3T.T @ Xh}

    def wf_mat(w: str) -> np.ndarray:
        M = np.eye(3, dtype=complex)
        for ch in w:
            M = M @ a4g[ch]
        return M

    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    ell1, th1 = float(2 * mp.re(hl1)), float(2 * mp.im(hl1))
    hl2 = mp.acosh((mp.mpf(2) + 2 * omega) / 2)
    ell2, th2 = float(2 * mp.re(hl2)), float(2 * mp.im(hl2))
    lam1_b940 = 2.9745505801732
    eps1 = (math.exp(-lam1_b940 * ell1) / abs(2.0 * np.sinh(0.5 * (ell1 + 1j * th1)))) / (2.0 * math.pi)
    eps2 = (math.exp(-lam1_b940 * ell2) / abs(2.0 * np.sinh(0.5 * (ell2 + 1j * th2)))) / (2.0 * math.pi)
    r_sh = eps2 / eps1
    Lc = (4.0 * ((math.pi**2) / 15.0) / eps1) ** 0.2
    cp = math.sqrt(2.0 * Lc / (1.0 - math.exp(-2.0 * Lc)))
    cm = math.sqrt(2.0 * Lc / (math.exp(2.0 * Lc) - 1.0))
    bs = math.sqrt(2.0 * math.tanh(0.5 * Lc) / Lc)
    mrs = (bs / cp) ** 2

    shell2_words = [("AAb", 1.0), ("Abb", 1.0), ("AABab", -1.0), ("ABaab", -1.0)]
    shell2_neg = [("AABab", -1.0), ("ABaab", -1.0)]
    shell2_pos = [("AAb", 1.0), ("Abb", 1.0)]

    K_diag = np.diag([1.0, r_sh, r_sh**2]).astype(complex)
    S2_K_diag = sum(np.exp(1j * s * th2) * (wf_mat(w) @ K_diag @ wf_mat(w).T) for w, s in shell2_words)
    K_pin_unit = K_diag + (-0.2 * r_sh) * S2_K_diag

    L_neg_full = sum(0.5 * np.exp(1j * s * th2) * (wf_mat(w) + wf_mat(w).T) for w, s in shell2_neg)
    K_v10_e8_unit = K_pin_unit + r_sh * L_neg_full
    K_diluted_unit = K_pin_unit + 0.2 * r_sh * L_neg_full

    leakage_01 = float(abs(L_neg_full[0, 1]))
    leakage_12 = float(abs(L_neg_full[1, 2]))
    reactor_02_match_err = float(abs(L_neg_full[0, 2] - (-np.exp(-1j * th2))))
    symmetry_err_v10 = float(np.linalg.norm(K_v10_e8_unit - K_v10_e8_unit.T))

    # Planted-Fault Operators (computed directly, Guardrail 2):
    L_asym_plant = sum(np.exp(1j * s * th2) * wf_mat(w) for w, s in shell2_neg)
    K_asym_plant = K_pin_unit + r_sh * L_asym_plant
    asym_majorana_violation_norm = float(np.linalg.norm(K_asym_plant - K_asym_plant.T))

    L_pos_plant = sum(0.5 * np.exp(1j * s * th2) * (wf_mat(w) + wf_mat(w).T) for w, s in shell2_pos)
    K_pos_plant = K_pin_unit + r_sh * L_pos_plant
    pos_pair_02_abs = float(abs(L_pos_plant[0, 2]))
    pos_pair_01_abs = float(abs(L_pos_plant[0, 1]))

    # 3. Self-Contained Construction of Y_weave + Same-Bundle Whitehead Overtones (pure Track A):
    a4_mats: List[np.ndarray] = [np.eye(3, dtype=complex)]
    fr = [C3T, Xh @ C3T]
    while fr:
        M = fr.pop()
        if not any(np.linalg.norm(M - X) < 1e-12 for X in a4_mats):
            a4_mats.append(M)
            for G in (C3T, Xh @ C3T):
                fr.extend([M @ G, G @ M])

    pA = tuple((-x) % 5 for x in range(5))
    pB = tuple((1 - x) % 5 for x in range(5))
    d5g = {"a": pA, "A": pA, "b": pB, "B": pB}

    def pmul(p: Tuple[int, ...], q: Tuple[int, ...]) -> Tuple[int, ...]:
        return tuple(p[q[i]] for i in range(5))

    def pinv(p: Tuple[int, ...]) -> Tuple[int, ...]:
        r = [0] * 5
        for i, v in enumerate(p):
            r[v] = i
        return tuple(r)

    d5_perms = [(0, 1, 2, 3, 4)]
    fr5 = [pA, pB]
    while fr5:
        p = fr5.pop()
        if p not in d5_perms:
            d5_perms.append(p)
            for g in (pA, pB):
                fr5.extend([pmul(p, g), pmul(g, p)])

    def eval_mat(w: str, mp_m: Dict[str, np.ndarray]) -> np.ndarray:
        cur = np.eye(3, dtype=complex)
        for ch in w:
            M = mp_m[ch.lower()]
            cur = cur @ (M.conj().T if ch.isupper() else M)
        return cur

    def eval_perm(w: str, mp_p: Dict[str, Tuple[int, ...]]) -> Tuple[int, ...]:
        cur = (0, 1, 2, 3, 4)
        for ch in w:
            p = mp_p[ch.lower()]
            cur = pmul(cur, pinv(p) if ch.isupper() else p)
        return cur

    W4 = snappy.Manifold("m129")
    W4.dehn_fill((-3, 1), 0)
    rels4 = W4.fundamental_group(simplify_presentation=False).relators()
    M_Ab_tgt, M_ABab_tgt = C3T.T @ (Xh @ C3T), C3T.T @ (C3T.T @ Xh) @ C3T @ (Xh @ C3T)
    mpm_exact = [
        {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}
        for mb in [C3T, C3T.T]
        for mc in a4_mats
        for md in a4_mats
        if all(np.linalg.norm(eval_mat(r, {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}) - np.eye(3)) < 1e-12 for r in rels4)
        and np.linalg.norm(eval_mat("BcbC", {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}) - M_Ab_tgt) < 1e-12
        and np.linalg.norm(eval_mat("Cb", {"a": md @ mc.conj().T, "b": mb, "c": mc, "d": md}) - M_ABab_tgt) < 1e-12
    ][0]
    surj_d5_4 = []
    for pb in d5_perms:
        for pc in d5_perms:
            for pd in d5_perms:
                mpp = {"a": pmul(pd, pinv(pc)), "b": pb, "c": pc, "d": pd}
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
                    if len(sub) == 10 and pb[0] == 0 and eval_perm("Abd", mpp)[0] == 0:
                        surj_d5_4.append(mpp)
    mpp_exact = surj_d5_4[0]

    def wf_m004(w: str):
        M = np.eye(3, dtype=complex)
        pd = (0, 1, 2, 3, 4)
        for ch in w:
            M = M @ a4g[ch]
            gp = d5g[ch]
            pd = tuple(pd[gp[i]] for i in range(5))
        fx = [x for x in range(5) if pd[x] == x]
        return M, (fx[0] if fx else None)

    z5 = np.exp(2j * math.pi / 5.0)
    v0 = np.ones(3, dtype=complex) / math.sqrt(3.0)
    gY = math.sqrt(0.6)
    Ws1 = np.exp(0.5j * th1) * z5 * wf_mat("Ab") + np.exp(-0.5j * th1) * (z5**4) * wf_mat("ABab")
    Ys1 = (z5**2) * wf_mat("ABab")
    Cs2 = sum(np.exp(0.5j * s * th2) * (z5 ** wf_m004(w)[1]) * wf_m004(w)[0] for w, s in shell2_words)
    S2_d = sum(np.exp(1j * s * th2) * np.outer(wf_m004(w)[0] @ v0, (wf_m004(w)[0] @ v0).conj()) for w, s in shell2_words)

    wn = {"nu_c": 0.0, "e_c": 3.0 / 10.5, "L": 4.5 / 10.5, "d_c": 7.0 / 10.5, "u_c": 8.0 / 10.5, "Q": 1.0}
    yh = {"nu_c": 0.0, "e_c": 1.0, "L": -0.5, "d_c": 1.0 / 3.0, "u_c": -2.0 / 3.0, "Q": 1.0 / 6.0}
    qxn = {"nu_c": -1.0, "e_c": -0.2, "L": 0.6, "d_c": 0.6, "u_c": -0.2, "Q": -0.2}
    t3r = {"nu_c": -0.5, "e_c": 0.5, "L": 0.0, "d_c": 0.5, "u_c": -0.5, "Q": 0.0}
    c_uv = {k: (1.0 if abs(t3r[k]) < 1e-12 else (cp if t3r[k] < 0 else cm)) for k in t3r}
    c_ir = {k: (1.0 if abs(t3r[k]) < 1e-12 else (cm if t3r[k] < 0 else cp)) for k in t3r}
    b_cl = {k: (1.0 if abs(t3r[k]) < 1e-12 else bs) for k in t3r}

    def sY_v7(fL: str, fR: str, yH: float, qH: float) -> np.ndarray:
        w_uv = c_uv[fL] * c_uv[fR]
        w_lp = w_uv + b_cl[fL] * b_cl[fR]
        w_ir = 0.2 * c_ir[fL] * c_ir[fR]
        T1L = wn[fL] * Ws1 + gY * (yh[fL] + yH) * Ys1
        T1R = wn[fR] * Ws1 + gY * (yh[fR] + yH) * Ys1
        qL = (qxn[fL] + 0.2 * qH) + gY * (yh[fL] + 0.5 * yH)
        qR = (qxn[fR] + 0.2 * qH) + gY * (yh[fR] + 0.5 * yH)
        T2L, T2R = qL * Cs2, qR * Cs2
        TL_t, TR_t = T1L + T2L, T1R + T2R
        gf = 1.0 / 3.0
        return (
            w_uv * np.outer(v0, v0.conj())
            + w_lp * eps1 * np.outer(T1L @ v0, (T1R @ v0).conj())
            + gf * w_lp * eps1 * (np.outer(T1L @ v0, v0.conj()) + np.outer(v0, (T1R @ v0).conj()))
            + eps2 * (w_uv * np.outer(T2L @ v0, (T2R @ v0).conj()) + w_ir * (qL * qR) * S2_d)
            + w_lp * (eps1**2) * np.outer(TL_t @ TL_t @ v0, (TR_t @ TR_t @ v0).conj())
            + gf * w_lp * (eps1**2) * (np.outer(TL_t @ TL_t @ v0, (TR_t @ v0).conj()) + np.outer(TL_t @ v0, (TR_t @ TR_t @ v0).conj()))
        )

    Y_weave = [
        sY_v7("Q", "u_c", 0.5, 1.0),
        sY_v7("Q", "d_c", -0.5, -1.0),
        sY_v7("L", "e_c", -0.5, -1.0),
        sY_v7("L", "nu_c", 0.5, 1.0),
    ]

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

    def inv_word(w: str) -> str:
        return "".join(c.lower() if c.isupper() else c.upper() for c in reversed(w))

    def sl2c_np(G_fg, w: str) -> np.ndarray:
        S = G_fg.SL2C(w)
        return np.array([[complex(S[0, 0]), complex(S[0, 1])], [complex(S[1, 0]), complex(S[1, 1])]], dtype=complex)

    def cusp1_frame(G_fg) -> Tuple[np.ndarray, np.ndarray]:
        Mb = sl2c_np(G_fg, "b")
        Mb_s = Mb if np.trace(Mb).real >= 0 else -Mb
        _, _, vh = np.linalg.svd(Mb_s - np.eye(2, dtype=complex))
        v1 = vh[-1].conj()
        v1 = v1 / np.linalg.norm(v1)
        v2 = np.array([-np.conj(v1[1]), np.conj(v1[0])], dtype=complex)
        U = np.column_stack([v1, v2])
        return U, U.conj().T

    overtones = []
    for q_s in range(1, 9):
        for p_s in range(-17, 18):
            if math.gcd(abs(p_s), q_s) == 1 and (p_s + 3 * q_s) % 10 == 0 and (p_s, q_s) != (-3, 1):
                W_c = snappy.Manifold("m129")
                W_c.dehn_fill((p_s, q_s), 0)
                if "positively" in W_c.solution_type() or "all" in W_c.solution_type():
                    overtones.append((float(W_c.volume()), p_s, q_s))
    overtones.sort()

    vol0 = float(2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3))))
    overtone_ledger: List[Dict[str, Any]] = []
    for _, p_s, q_s in overtones:
        W = snappy.Manifold("m129")
        _ = W.chern_simons()
        W.dehn_fill((p_s, q_s), 0)
        vol, cs = float(W.volume()), float(W.chern_simons())
        F = W.filled_triangulation()
        sym_m = F.symmetry_group().order() if not F.symmetry_group().is_amphicheiral() else F.symmetry_group().order() // 2
        Gf = W.fundamental_group(simplify_presentation=False)
        U, Uinv = cusp1_frame(Gf)
        cmats = [(gw, Uinv @ sl2c_np(Gf, gw) @ U) for gw in words4]
        z_ford = max(1.0 / abs(M[1, 0]) for _, M in cmats if abs(M[1, 0]) > 1e-7)
        spec = W.length_spectrum(1.80, include_words=True, grouped=False)
        shells_5cyc: Dict[float, List[Any]] = {}
        shells_refl: Dict[float, List[Any]] = {}
        for g in spec:
            wd, ln, tw = g["word"], float(g["length"].real), float(g["length"].imag)
            Mw = Uinv @ sl2c_np(Gf, wd) @ U
            best_zh, best_w, best_mid = -1.0, wd, 1e9
            for gw, Mgw in cmats[:250]:
                Mc = Mgw @ Mw @ np.array([[Mgw[1, 1], -Mgw[0, 1]], [-Mgw[1, 0], Mgw[0, 0]]], dtype=complex)
                if abs(Mc[1, 0]) > 1e-8:
                    zh = float(abs(np.sqrt((Mc[0, 0] + Mc[1, 1]) ** 2 - 4.0)) / (2.0 * abs(Mc[1, 0]))) / z_ford
                    mid = abs((Mc[0, 0] - Mc[1, 1]) / (2.0 * Mc[1, 0]))
                    if zh > best_zh + 1e-6 or (abs(zh - best_zh) <= 1e-6 and mid < best_mid):
                        best_zh, best_mid, best_w = zh, mid, gw + wd + inv_word(gw)
            Mg = eval_mat(best_w, mpm_exact)
            pg = eval_perm(best_w, mpp_exact)
            fx = [x for x in range(5) if pg[x] == x]
            if len(fx) == 0:
                eff_ln = (5.0 * ln if ln < 0.8 else ln) + 2.0 * max(0.0, -math.log(max(best_zh, 1e-12)))
                shells_5cyc.setdefault(round(eff_ln, 4), []).append((eff_ln, 5.0 * tw if ln < 0.8 else tw, Mg))
            elif len(fx) == 1:
                eff_ln = ln + 2.0 * max(0.0, -math.log(max(best_zh, 1e-12)))
                shells_refl.setdefault(round(eff_ln, 4), []).append((eff_ln, tw, Mg, fx[0]))

        def dY_sec(fL: str, fR: str, yH: float, qH: float) -> np.ndarray:
            w_eff = 0.2 * c_ir[fL] * c_ir[fR]
            qL = (qxn[fL] + 0.2 * qH) + gY * (yh[fL] + 0.5 * yH)
            qR = (qxn[fR] + 0.2 * qH) + gY * (yh[fR] + 0.5 * yH)
            gf = 1.0 / 3.0
            dY = np.zeros((3, 3), dtype=complex)
            for _, glist in sorted(shells_5cyc.items()):
                ln0, tw0, _ = glist[0]
                ep_sh = (math.exp(-lam1_b940 * ln0) / abs(2.0 * np.sinh(0.5 * (ln0 + 1j * tw0)))) / (2.0 * math.pi)
                Ws = sum(np.exp(0.5j * tw) * (z5 ** (1 if tw > 0 else 4)) * Mg for _, tw, Mg in glist)
                Ys = sum((z5**2) * Mg for _, tw, Mg in glist if tw < 0)
                T1L = wn[fL] * Ws + gY * (yh[fL] + yH) * Ys
                T1R = wn[fR] * Ws + gY * (yh[fR] + yH) * Ys
                dY += w_eff * ep_sh * (np.outer(T1L @ v0, (T1R @ v0).conj()) + gf * (np.outer(T1L @ v0, v0.conj()) + np.outer(v0, (T1R @ v0).conj())))
            for _, glist in sorted(shells_refl.items()):
                ln0, tw0, *_ = glist[0]
                ep_sh = (math.exp(-lam1_b940 * ln0) / abs(2.0 * np.sinh(0.5 * (ln0 + 1j * tw0)))) / (2.0 * math.pi)
                Cs = sum(np.exp(0.5j * tw) * (z5**fx0) * Mg for _, tw, Mg, fx0 in glist)
                Sd = sum(np.exp(1j * tw) * np.outer(Mg @ v0, (Mg @ v0).conj()) for _, tw, Mg, _ in glist)
                T2L, T2R = qL * Cs, qR * Cs
                dY += w_eff * ep_sh * (np.outer(T2L @ v0, (T2R @ v0).conj()) + gf * (np.outer(T2L @ v0, v0.conj()) + np.outer(v0, (T2R @ v0).conj())) + (qL * qR) * Sd)
            return dY

        w_m = (4.0 / sym_m) * np.exp(-(10.0 / math.pi) * (vol - vol0) - 20.0j * math.pi * cs)
        overtone_ledger.append({"slope": [p_s, q_s], "vol": vol, "cs": cs, "sym_plus": sym_m, "abs_weight_M5": float(abs(w_m))})
        for idx, args in enumerate([("Q", "u_c", 0.5, 1.0), ("Q", "d_c", -0.5, -1.0), ("L", "e_c", -0.5, -1.0), ("L", "nu_c", 0.5, 1.0)]):
            Y_weave[idx] = Y_weave[idx] + w_m * dY_sec(*args)

    # Guardrail 3 Falsification Plant: Single-matrix left-right overlap U_L^dagger U_R of Y_e:
    rng_lr = np.random.default_rng(20261125)
    U_eL0, _, V_eR0_h = np.linalg.svd(Y_weave[2])
    ov_0 = float(abs((U_eL0.conj().T @ V_eR0_h.conj().T)[0, 2])) ** 2
    UL_r, UR_r = _random_haar_u(3, rng_lr), _random_haar_u(3, rng_lr)
    U_eL1, _, V_eR1_h = np.linalg.svd(UL_r @ Y_weave[2] @ UR_r.conj().T)
    ov_1 = float(abs((U_eL1.conj().T @ V_eR1_h.conj().T)[0, 2])) ** 2
    single_matrix_lr_overlap_drift = abs(ov_1 - ov_0)

    passed = bool(
        e8_branching["total_dim"] == 248
        and e8_branching["dim_1_15"] == 15
        and mrv_9x9_rel_err < 1.0e-12
        and mrv_schur_sign_rel_err < 1.0e-5
        and leakage_01 < 1.0e-15
        and leakage_12 < 1.0e-15
        and reactor_02_match_err < 1.0e-15
        and symmetry_err_v10 < 1.0e-15
        and asym_majorana_violation_norm > 0.1
        and pos_pair_02_abs < 1.0e-15
        and pos_pair_01_abs > 0.99
        and single_matrix_lr_overlap_drift > 0.05
    )
    assert passed, "Gate P8-2 assertion failed"

    return {
        "gate_p8_2_passed": passed,
        "e8_spin10_su4_branching": e8_branching,
        "malinsky_romao_valle_benchmark": {
            "sv_9x9_vs_schur_50d_rel_err": mrv_9x9_rel_err,
            "schur_opposite_offdiag_sign_lead_rel_err": mrv_schur_sign_rel_err,
        },
        "theorem_P8_2_negative_torsion_shell2_reactor_selection": {
            "leakage_abs_01": leakage_01,
            "leakage_abs_12": leakage_12,
            "reactor_02_minus_neg_exp_neg_ith2_err": reactor_02_match_err,
            "majorana_symmetry_norm_err": symmetry_err_v10,
        },
        "planted_fault_signals": {
            "asymmetric_non_majorana_norm_violation": asym_majorana_violation_norm,
            "wrong_positive_torsion_pair_02_abs": pos_pair_02_abs,
            "wrong_positive_torsion_pair_01_abs": pos_pair_01_abs,
            "single_matrix_lr_overlap_haar_drift_plant": single_matrix_lr_overlap_drift,
        },
        "r_sh": r_sh,
        "mrs": mrs,
        "same_bundle_overtones_M5": overtone_ledger,
        "_Y_weave": tuple(Y_weave),
        "_K_v10_e8_unit": K_v10_e8_unit,
        "_K_diluted_unit": K_diluted_unit,
        "_K_pos_plant": K_pos_plant,
    }
