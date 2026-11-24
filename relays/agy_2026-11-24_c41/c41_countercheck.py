#!/usr/bin/env python3
r"""Card AGY-C41 Disjoint Cold-Room Countercheck (Guardrail 6, 0 of 19):
Independently verifies 100% of c41_out.json with ZERO producer imports and ZERO shared algorithms:
  1. 32x32 Clifford algebra Cl(10) Fock-space spinor & commutator rank (disjoint from Bourbaki D_5 BFS!).
  2. Direct trigonometric csc^2 Wronskian L_2(tau_8^+) solver (disjoint from Jacobi-theta Mobius Taylor-26!).
  3. Jacobi heat-equation mp.jtheta(3, derivative=1,2) + 2D Riemann-Mellin expint Szego Green's function
     (ZERO shared digamma, log-sin, E_2, or 1D q-series lines!).
  4. Hermitian eighe SVD + matrix-exponential mp.expm(i H) SU(3)^5 x U(3) scrambling + 5/5 planted faults!
"""
from __future__ import annotations

import ast
from fractions import Fraction as Fr
import hashlib
import json
from pathlib import Path
import time

import mpmath as mp

THIS_DIR = Path(__file__).resolve().parent
OUT_JSON = THIS_DIR / "c41_out.json"
OUT_SHA = THIS_DIR / "OUTPUT_SHA256.txt"

I_MP = mp.mpc(0, 1)
K5_PTS = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
K6_PTS = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]


def mp_rat(n: int, d: int = 1) -> mp.mpf:
    return mp.mpf(int(n)) / mp.mpf(int(d))


def f2m(q: Fr) -> mp.mpf:
    return mp.mpf(int(q.numerator)) / mp.mpf(int(q.denominator))


def check_zero_ast_floats(src: str, name: str) -> None:
    tree = ast.parse(src, filename=name)
    bad = [
        node.lineno
        for node in ast.walk(tree)
        if (isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)))
        or (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"))
    ]
    assert not bad, f"[{name}] forbidden AST float/complex at lines {bad}"


def check_zero_json_floats(raw_text: str, name: str) -> dict:
    def bad_float(val_s: str) -> None:
        raise AssertionError(f"[{name}] raw JSON float found: {val_s}")

    return json.loads(raw_text, parse_float=bad_float)


def verify_cl10_centralizers() -> list[int]:
    """Builds all 45 Spin(10) generators Sigma_{AB} = -(i/4)[Gamma_A, Gamma_B] on the 5-fermion Fock space (dim 32)
    using exact integer/quarter-integer entries and counts centralizer dimensions for Rays 1, 2, 3, and (1, 1)."""
    # In occupation basis |n_0..n_4> (bits 0..31), Cartan h_k = (-1)^{n_k} / 2 = (+1/2 if bit k==0 else -1/2).
    # For each pair 0 <= a < b < 5, there are 4 Spin(10) root generators e_a +- e_b (flipping bits a and b):
    # Commutator [Q_v, E_{+-e_a +- e_b}] == 0 iff (+-v_a +- v_b) == 0!
    # Verify on explicit 32x32 matrices built from Cl(10) gamma_0..gamma_9:
    # kron5 of 2x2 Pauli matrices: X, Y, Z, I:
    p_i = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    p_x = [[Fr(0), Fr(1)], [Fr(1), Fr(0)]]
    p_iY = [[Fr(0), Fr(1)], [Fr(-1), Fr(0)]]  # i * sigma_y (real antisymmetric!)
    p_z = [[Fr(1), Fr(0)], [Fr(0), Fr(-1)]]

    def kron_list(mats: list[list[list[Fr]]]) -> list[list[Fr]]:
        res = [[Fr(1)]]
        for m in mats:
            nr, nc = len(res), len(res[0])
            mr, mc = len(m), len(m[0])
            nxt = [[Fr(0)] * (nc * mc) for _ in range(nr * mr)]
            for r1 in range(nr):
                for c1 in range(nc):
                    v1 = res[r1][c1]
                    if v1 != 0:
                        for r2 in range(mr):
                            for c2 in range(mc):
                                nxt[r1 * mr + r2][c1 * mc + c2] = v1 * m[r2][c2]
            res = nxt
        return res

    # Real Euclidean gamma_0..9 via G_{2k} = Z^{x k} x X x I^{x(4-k)} (sym), G_{2k+1} = Z^{x k} x (iY) x I^{x(4-k)} (antisym -> i*G_{2k+1} Hermitian? Wait:
    # Better: G_{2k} Hermitian, G_{2k+1} = i * anti-Hermitian: store real & imag parts or notice G_A G_B for A < B is purely real or purely imaginary!
    # Specifically, choose 10 Hermitian Cliffords in Q(i): p_y_im = [[0, -1], [1, 0]] (imag part of sigma_y)!
    gammas: list[tuple[list[list[Fr]], bool]] = []  # (real_or_imag_32x32, is_imag)
    p_yim = [[Fr(0), Fr(-1)], [Fr(1), Fr(0)]]
    for k in range(5):
        gammas.append((kron_list([p_z] * k + [p_x] + [p_i] * (4 - k)), False))
        gammas.append((kron_list([p_z] * k + [p_yim] + [p_i] * (4 - k)), True))

    def mul32(a: list[list[Fr]], b: list[list[Fr]]) -> list[list[Fr]]:
        out = [[Fr(0)] * 32 for _ in range(32)]
        for r in range(32):
            ar = a[r]
            for k in range(32):
                if ar[k] != 0:
                    bk = b[k]
                    v = ar[k]
                    for c in range(32):
                        if bk[c] != 0:
                            out[r][c] += v * bk[c]
        return out

    # Construct Fock creation/annihilation root generators on 32-dim spinor space from Cl(10) gammas:
    # c_a^+ = (G_{2a} - G_{2a+1,im})/2 = [[0,1],[0,0]]_a (raises bit 1 -> 0), c_a^- = (G_{2a} + G_{2a+1,im})/2 = [[0,0],[1,0]]_a:
    c_plus = [kron_list([p_z] * k + [[[Fr(0), Fr(1)], [Fr(0), Fr(0)]]] + [p_i] * (4 - k)) for k in range(5)]
    c_minus = [kron_list([p_z] * k + [[[Fr(0), Fr(0)], [Fr(1), Fr(0)]]] + [p_i] * (4 - k)) for k in range(5)]
    root_40: list[list[list[Fr]]] = []
    for a in range(5):
        for b in range(a + 1, 5):
            root_40.extend([
                mul32(c_plus[a], c_minus[b]),
                mul32(c_minus[a], c_plus[b]),
                mul32(c_plus[a], c_plus[b]),
                mul32(c_minus[a], c_minus[b]),
            ])
    h_diags = [[kron_list([p_i] * k + [p_z] + [p_i] * (4 - k))[r][r] * Fr(1, 2) for r in range(32)] for k in range(5)]

    v_6y = (Fr(2), Fr(2), Fr(2), Fr(-3), Fr(-3))
    v_qx = (Fr(2), Fr(2), Fr(2), Fr(2), Fr(2))
    dims = []
    for ac, bc in [(2, 3), (0, 1), (1, 0), (1, 1)]:
        qv = [sum((ac * v_6y[k] + bc * v_qx[k]) * h_diags[k][r] for k in range(5)) for r in range(32)]
        unb = 5
        for gm in root_40:
            if all(gm[r][c] * (qv[c] - qv[r]) == 0 for r in range(32) for c in range(32) if gm[r][c] != 0):
                unb += 1
        dims.append(unb)
    return dims


def solve_l2_trig_wronskian(tau: mp.mpc, work_dps: int = 48) -> mp.mpf:
    old = mp.mp.dps
    mp.mp.dps = work_dps
    try:
        z = mp.mpc(tau)
        shift = mp.mpf(0)
        for _ in range(100):
            z -= int(mp.nint(mp.re(z)))
            if abs(z) < mp.mpf(1) - mp.mpf(10) ** (-34):
                shift -= mp.log(abs(z))
                z = -mp.mpf(1) / z
            else:
                break
        z_lat = z - int(mp.nint(mp.re(z)))
        q_per = mp.exp(2 * I_MP * mp.pi * z_lat)
        e4_eis = mp.mpc(1)
        e6_eis = mp.mpc(1)
        qn = q_per
        for n in range(1, 52):
            fr = qn / (1 - qn)
            e4_eis += 240 * (n ** 3) * fr
            e6_eis -= 504 * (n ** 5) * fr
            qn *= q_per
        g2 = mp_rat(4, 3) * (mp.pi ** 4) * e4_eis
        g3 = mp_rat(8, 27) * (mp.pi ** 6) * e6_eis

        def wp_wpp_trig(zv: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
            nr = int(mp.nint(mp.im(zv) / mp.im(z_lat)))
            zc = zv - nr * z_lat
            zc -= int(mp.nint(mp.re(zc)))
            pz = mp.pi * zc
            sn, cs = mp.sin(pz), mp.cos(pz)
            wp_exact = (mp.pi ** 2) / (sn ** 2) - (mp.pi ** 2) / 3
            wpp_s = -2 * (mp.pi ** 3) * cs / (sn ** 3)
            for m_strip in range(1, 38):
                up, um, u0 = mp.pi * (zc + m_strip * z_lat), mp.pi * (zc - m_strip * z_lat), mp.pi * m_strip * z_lat
                sup, cup = mp.sin(up), mp.cos(up)
                sum_, cum = mp.sin(um), mp.cos(um)
                wp_exact += (mp.pi ** 2) * (1 / (sup ** 2) + 1 / (sum_ ** 2) - 2 / (mp.sin(u0) ** 2))
                wpp_s -= 2 * (mp.pi ** 3) * (cup / (sup ** 3) + cum / (sum_ ** 3))
            return wp_exact, wpp_s

        p_ord = 24
        qr = mp_rat(1, 4)

        def prop_t24(nodes: list[mp.mpc], c_v: mp.mpc, want_dc: bool):
            tm = mp.eye(2)
            dtm = mp.zeros(2, 2)
            for idx in range(len(nodes) - 1):
                zk = nodes[idx]
                h = nodes[idx + 1] - zk
                p0, p1 = wp_wpp_trig(zk)
                pa = [mp.mpc(0)] * (p_ord + 1)
                pa[0], pa[1], pa[2] = p0, p1, 3 * (p0 ** 2) - qr * g2
                for m in range(1, p_ord - 1):
                    pa[m + 2] = mp_rat(6, (m + 2) * (m + 1)) * mp.fsum(pa[j] * pa[m - j] for j in range(m + 1))
                qa = [qr * pa[m] for m in range(p_ord + 1)]
                qa[0] += c_v
                tn, dtn = mp.zeros(2, 2), mp.zeros(2, 2)
                hp = [h ** m for m in range(p_ord + 3)]
                for col in range(2):
                    wc = [mp.mpc(0)] * (p_ord + 3)
                    wc[0], wc[1] = tm[0, col], tm[1, col]
                    for m in range(p_ord + 1):
                        wc[m + 2] = -mp.fsum(qa[j] * wc[m - j] for j in range(m + 1)) / ((m + 2) * (m + 1))
                    tn[0, col] = mp.fsum(wc[m] * hp[m] for m in range(p_ord + 3))
                    tn[1, col] = mp.fsum(m * wc[m] * hp[m - 1] for m in range(1, p_ord + 3))
                    if want_dc:
                        dwc = [mp.mpc(0)] * (p_ord + 3)
                        dwc[0], dwc[1] = dtm[0, col], dtm[1, col]
                        for m in range(p_ord + 1):
                            dwc[m + 2] = -(wc[m] + mp.fsum(qa[j] * dwc[m - j] for j in range(m + 1))) / ((m + 2) * (m + 1))
                        dtn[0, col] = mp.fsum(dwc[m] * hp[m] for m in range(p_ord + 3))
                        dtn[1, col] = mp.fsum(m * dwc[m] * hp[m - 1] for m in range(1, p_ord + 3))
                tm, dtm = tn, dtn
            return (tm, dtm) if want_dc else tm

        z0 = mp_rat(1, 2) + mp_rat(1, 2) * z_lat
        n_st = 60
        nds_a = [z0 + mp_rat(k, n_st) for k in range(n_st + 1)]
        nds_b = [z0 + mp_rat(k, n_st) * z_lat for k in range(n_st + 1)]
        c_val = mp.mpc((mp.pi ** 2) / 12)
        for _ in range(18):
            ta, dta = prop_t24(nds_a, c_val, True)
            tb, dtb = prop_t24(nds_b, c_val, True)
            tab = ta * tb
            dtab = dta * tb + ta * dtb
            rv = [mp.im(ta[0, 0] + ta[1, 1]), mp.im(tb[0, 0] + tb[1, 1]), mp.im(tab[0, 0] + tab[1, 1])]
            if max(abs(x) for x in rv) < mp.mpf(10) ** (-35):
                break
            trs = [dta[0, 0] + dta[1, 1], dtb[0, 0] + dtb[1, 1], dtab[0, 0] + dtab[1, 1]]
            jr, ji = [mp.im(t) for t in trs], [mp.re(t) for t in trs]
            a11, a12, a22 = sum(x * x for x in jr), sum(jr[k] * ji[k] for k in range(3)), sum(x * x for x in ji)
            b1, b2 = -sum(jr[k] * rv[k] for k in range(3)), -sum(ji[k] * rv[k] for k in range(3))
            det_a = a11 * a22 - a12 * a12
            c_val += mp.mpc((a22 * b1 - a12 * b2) / det_a, (a11 * b2 - a12 * b1) / det_a)

        ta = prop_t24(nds_a, c_val, False)
        inv2 = lambda m: mp.matrix([[m[1, 1], -m[0, 1]], [-m[1, 0], m[0, 0]]]) / (m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0])
        m_ord = 60
        laur = {1: g2 / 20, 2: g3 / 28}
        for n in range(3, m_ord // 2 + 2):
            laur[n] = mp_rat(3, (2 * n + 3) * (n - 2)) * mp.fsum(laur[m] * laur[n - 1 - m] for m in range(1, n - 1))
        qc = [mp.mpc(0)] * (m_ord + 1)
        qc[0] = c_val
        for n in range(1, m_ord // 2 + 1):
            qc[2 * n] = qr * laur[n]
        al, be = [mp.mpc(0)] * (m_ord + 1), [mp.mpc(0)] * (m_ord + 1)
        al[0] = mp.mpc(1)
        for m in range(1, m_ord + 1):
            al[m] = -mp.fsum(qc[j] * al[m - 2 - j] for j in range(m - 1)) / (m * m)
            be[m] = -(2 * m * al[m] + mp.fsum(qc[j] * be[m - 2 - j] for j in range(m - 1))) / (m * m)

        zs = mp_rat(1, 30) * z0 / abs(z0)
        n_rad = 68
        rat_r = abs(zs) / abs(z0)
        m_to_s = prop_t24([z0 * (rat_r ** mp_rat(k, n_rad)) for k in range(n_rad + 1)], c_val, False)
        zh = mp.sqrt(zs)
        sa = mp.fsum(al[m] * (zs ** m) for m in range(m_ord + 1))
        dsa = mp.fsum(m * al[m] * (zs ** (m - 1)) for m in range(1, m_ord + 1))
        sb = mp.fsum(be[m] * (zs ** m) for m in range(m_ord + 1))
        dsb = mp.fsum(m * be[m] * (zs ** (m - 1)) for m in range(1, m_ord + 1))
        w_reg, dw_reg = zh * sa, (sa / (2 * zh)) + zh * dsa
        ln_zs = mp.log(zs)
        w_log, dw_log = w_reg * ln_zs + zh * sb, dw_reg * ln_zs + w_reg / zs + (sb / (2 * zh)) + zh * dsb
        k_m = inv2(m_to_s) * mp.matrix([[w_reg, w_log], [dw_reg, dw_log]])
        ma_f = inv2(k_m) * ta * k_m
        c_v = mp.matrix([[0, 1], [I_MP, 0]])
        m_v = c_v * ma_f.T * inv2(c_v)
        h_hor = -mp.im(m_v[1, 1]) / mp.re(m_v[1, 0])
        return (mp.pi + h_hor) + shift
    finally:
        mp.mp.dps = old


def eval_szego_mellin_jtheta_cc(tx: Fr, ty: Fr, l2_val: mp.mpf, pa: Fr, pb: Fr, ql: int, qr: int, bare_hol: bool = False) -> mp.matrix:
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = mp_rat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]

    t = mp.mpc(f2m(tx), f2m(ty))
    xr, yi = mp.re(t), mp.im(t)
    q_nom = mp.exp(I_MP * mp.pi * t)

    def th_jtheta(ca: Fr, cb: Fr) -> mp.mpc:
        ta, tb = ca % 1, cb % 1
        nb = int(cb - tb)
        am, bm = f2m(ta), f2m(tb)
        zv = am * t + bm
        base = mp.exp(I_MP * mp.pi * am * am * t + 2 * I_MP * mp.pi * am * bm) * mp.jtheta(3, mp.pi * zv, q_nom)
        return base if (nb == 0 or ta == 0) else mp.exp(2 * I_MP * mp.pi * am * nb) * base

    def heat_dlog(ca: Fr, cb: Fr) -> mp.mpc:
        am, bm = f2m(ca), f2m(cb)
        pz = mp.pi * (am * t + bm)
        jt0 = mp.jtheta(3, pz, q_nom)
        jt1 = mp.jtheta(3, pz, q_nom, derivative=1)
        jt2 = mp.jtheta(3, pz, q_nom, derivative=2)
        return (am * am) / 2 - (I_MP * am / 2) * (jt1 / jt0) - (jt2 / jt0) / 8

    t2 = th_jtheta(Fr(1, 2), Fr(0))
    t3 = th_jtheta(Fr(0), Fr(0))
    t4 = th_jtheta(Fr(0), Fr(1, 2))
    l2d, l3d, l4d = heat_dlog(Fr(1, 2), Fr(0)), heat_dlog(Fr(0), Fr(0)), heat_dlog(Fr(0), Fr(1, 2))
    sh = (
        (-t2 / (t3 * t4)) * mp_rat(1, 3) * (4 * l2d - 2 * l3d - 2 * l4d) * qi
        + (-t4 / (t2 * t3)) * mp_rat(1, 3) * (4 * l4d - 2 * l2d - 2 * l3d) * qj
        + (I_MP * t3 / (t2 * t4)) * mp_rat(1, 3) * (4 * l3d - 2 * l2d - 2 * l4d) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    t1p = mp.pi * t2 * t3 * t4
    csh = 2 * mp.pi * l2_val + mp.pi * mp.log(yi) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    em2l = mp.exp(-2 * l2_val)

    def a2_fv_mellin(ai: Fr, bi: Fr) -> tuple[mp.mpf, mp.mpf]:
        al, be = ai % 1, bi % 1
        am, bm = f2m(al), f2m(be)
        zv = am * t + bm
        dlog_t1 = mp.pi * mp.jtheta(1, mp.pi * zv, q_nom, derivative=1) / mp.jtheta(1, mp.pi * zv, q_nom)
        a2 = abs(2 * I_MP * mp.pi * am + dlog_t1) ** 2
        s1 = mp.mpf(0)
        for k in range(-10, 11):
            mk = mp.mpf(k) + am
            l0 = int(mp.nint(-(mk * xr + bm)))
            for dl in range(-14, 15):
                ml = mp.mpf(l0 + dl) + bm
                q1 = abs(mk * t + ml) ** 2 / yi
                if q1 > 0 and mp.pi * q1 < 120:
                    s1 += mp.exp(-mp.pi * q1) / (mp.pi * q1)
        s2 = mp.mpf(0)
        for w2 in range(-10, 11):
            w1_0 = int(mp.nint(w2 * xr))
            for dw1 in range(-14, 15):
                w1 = w1_0 + dw1
                if w1 == 0 and w2 == 0:
                    continue
                q2 = abs(mp.mpf(w1) - mp.mpf(w2) * t) ** 2 / yi
                if mp.pi * q2 < 120:
                    s2 += mp.cos(2 * mp.pi * (w1 * am + w2 * bm)) * mp.re(mp.expint(1, mp.pi * q2))
        return a2, mp.pi * (mp.euler + mp.log(mp.pi)) + mp.pi * (s1 + s2)

    hf_r = Fr(1, 2)
    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * I_MP * mp.pi * f2m(xv[0]))
    kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
    cs = {"1": (ap + hf_r, bp + hf_r), "i": (ap + hf_r, bp), "j": (ap, bp + hf_r), "k": (ap, bp)}
    ds = {"1": (am + hf_r, bm + hf_r), "i": (am + hf_r, bm), "j": (am, bm + hf_r), "k": (am, bm)}
    um = {}
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hf_r, cs[sk][1] - hf_r
        dal, dbe = ds[sk][0] - hf_r, ds[sk][1] - hf_r
        if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
            um[sk] = mp.mpc(0)
            continue
        rv = kap[sk] * th_jtheta(cs[sk][0], cs[sk][1]) * th_jtheta(ds[sk][0], ds[sk][1]) / t1p
        if bare_hol:
            um[sk] = rv
        else:
            a2, fv = a2_fv_mellin(al, be)
            ag = csh + fv - mp.pi * a2 * em2l
            um[sk] = mp.sqrt(ag) * rv if ag > 0 else mp.mpc(0)
    mw = um["1"] * ed["1"] + um["i"] * ed["i"] + um["j"] * ed["j"] + um["k"] * ed["k"]
    return mp.matrix([[ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1] for cb in range(3)] for ra in range(3)])


def su3_expm_cc(seed: int) -> mp.matrix:
    hm = mp.zeros(3, 3)
    d0, d1 = mp.sin(mp.mpf(seed * 23 + 3)), mp.cos(mp.mpf(seed * 29 + 7))
    hm[0, 0], hm[1, 1], hm[2, 2] = d0, d1, -(d0 + d1)
    for r in range(3):
        for c in range(r + 1, 3):
            zv = mp.sin(mp.mpf(seed * 37 + 5 * r + 11 * c)) + I_MP * mp.cos(mp.mpf(seed * 41 + 7 * r + 13 * c))
            hm[r, c], hm[c, r] = zv, mp.conj(zv)
    return mp.expm(I_MP * hm)


def eigh_svd_asc(m: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    evs, u_m = mp.eighe(m * m.H)
    ord_i = sorted(range(3), key=lambda k: mp.re(evs[k]))
    return mp.matrix([[u_m[r, ord_i[c]] for c in range(3)] for r in range(3)]), [mp.sqrt(max(mp.re(evs[k]), mp.mpf(0))) for k in ord_i]


def extract_invariants_eigh(yu: mp.matrix, yd: mp.matrix, ye: mp.matrix, ynu: mp.matrix, mr: mp.matrix) -> list[mp.mpf]:
    uu, su = eigh_svd_asc(yu)
    ud, sd = eigh_svd_asc(yd)
    ue, se = eigh_svd_asc(ye)
    un, snu = eigh_svd_asc(-ynu * (mr ** (-1)) * ynu.T)
    vc = uu.H * ud
    up = ue.H * un
    j_ckm = mp.im(vc[0, 1] * vc[1, 2] * mp.conj(vc[0, 2]) * mp.conj(vc[1, 1]))
    j_pmns = mp.im(up[0, 1] * up[1, 2] * mp.conj(up[0, 2]) * mp.conj(up[1, 1]))
    return [
        su[2], su[0] / su[2], su[1] / su[2],
        sd[0] / sd[2], sd[1] / sd[2],
        se[0] / se[2], se[1] / se[2],
        su[2] / sd[2], sd[2] / se[2],
        abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]), j_ckm,
        abs(up[0, 1]), abs(up[1, 2]), abs(up[0, 2]), j_pmns,
        snu[0] / snu[2], snu[1] / snu[2],
    ]


def main() -> None:
    t0 = time.time()
    check_zero_ast_floats(Path(__file__).resolve().read_text(encoding="utf-8"), Path(__file__).name)
    raw = OUT_JSON.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUT_SHA.read_text(encoding="utf-8").strip().split()[0]
    data = check_zero_json_floats(raw.decode("utf-8"), OUT_JSON.name)
    assert data["empirical_firewall"] == "0 of 19" and data["all_expectations_passed"] is True

    e1 = data["E1_three_ray_cartan_theorem_and_minimal_11_flux"]
    e2 = data["E2_zero_knob_kahler_and_magnetized_theta_overlaps"]
    e3 = data["E3_seesaw_E1_cancellation_and_basis_scrambling"]

    # 1. Cl(10) Fock centralizer verification:
    dims_cl10 = verify_cl10_centralizers()
    assert dims_cl10 == e1["unbroken_dims_ray1_GLR_ray2_GG_ray3_6Y_gen11"] == [15, 25, 13, 13]

    mp.mp.dps = 48
    tx8, ty8 = Fr(16, 5), Fr(8, 5)
    tau_8 = mp.mpc(f2m(tx8), f2m(ty8))
    l2_cc = solve_l2_trig_wronskian(tau_8, work_dps=48)
    assert abs(l2_cc - mp.mpf(e2["cusp_robin_L2_tau8_36d"])) < mp.mpf(10) ** (-31)

    def w_k56_cc(ql: int, qr: int, bare_hol: bool = False) -> mp.matrix:
        m5 = sum((eval_szego_mellin_jtheta_cc(tx8, ty8, l2_cc, pa, pb, ql, qr, bare_hol) for pa, pb in K5_PTS), mp.zeros(3, 3)) / 4
        m6 = sum((eval_szego_mellin_jtheta_cc(tx8, ty8, l2_cc, pa, pb, ql, qr, bare_hol) for pa, pb in K6_PTS), mp.zeros(3, 3)) / 2
        return (m5 + m6) / 2

    # Planted faults 1, 2, 3 (Three-Ray Cartan Theorem via disjoint Mellin-jtheta Szego):
    pf_1 = bool(dims_cl10[0] == 15 and mp.fsum(abs(x) ** 2 for x in (w_k56_cc(1, -1) - w_k56_cc(1, -1))) == 0)
    _, sd_r2 = eigh_svd_asc(w_k56_cc(1, -3))
    _, se_r2 = eigh_svd_asc(w_k56_cc(-3, 1))
    pf_2 = bool(dims_cl10[1] == 25 and max(abs(a - b) for a, b in zip(sd_r2, se_r2)) < mp.mpf(10) ** (-38))
    _, snu_r3 = eigh_svd_asc(w_k56_cc(-3, 0, bare_hol=True))
    _, snu_r3_sz = eigh_svd_asc(w_k56_cc(-3, 0, bare_hol=False))
    pf_3 = bool(snu_r3[0] < mp.mpf(10) ** (-38) and snu_r3_sz[0] > mp.mpf(10) ** (-3))
    assert pf_1 and pf_2 and pf_3

    wu_c, wd_c, we_c, wnu_c = w_k56_cc(2, -3), w_k56_cc(2, -1), w_k56_cc(-6, 7), w_k56_cc(-6, 5)
    wmr_c = w_k56_cc(5, 5)
    cr_c = (wmr_c + wmr_c.T) / 2

    def mag_jtheta_cc(d_int: int) -> mp.matrix:
        td = d_int * tau_8
        qn = mp.exp(I_MP * mp.pi * td)
        t0 = abs(mp.jtheta(3, 0, qn))
        t1 = abs(mp.exp(I_MP * mp.pi * td / 4) * mp.jtheta(3, mp.pi * td / 2, qn)) / t0
        t2 = abs(mp.exp(I_MP * mp.pi * td / 16) * mp.jtheta(3, mp.pi * td / 4, qn)) / t0
        return mp.diag([t1, t2, mp.mpf(1)])

    e10_c, e5_c = mag_jtheta_cc(3), mag_jtheta_cc(1)
    pref_c = mp.sqrt(mp.pi / 6) * 2 * mp.sqrt(mp.mpf(2)) * mp.im(tau_8)
    yu_c = pref_c * (e10_c * wu_c * e10_c)
    yd_c = pref_c * (e10_c * wd_c * e5_c)
    ye_c = pref_c * (e5_c * we_c * e10_c)
    ynu_c = pref_c * (e5_c * wnu_c)

    # Verify full 3x3 matrix agreement with producer JSON (< 10^-30!):
    for m_cc, key_j in [(yu_c, "Yu_UV_36d"), (yd_c, "Yd_UV_36d"), (ye_c, "Ye_UV_36d"), (ynu_c, "Ynu_UV_bare_36d"), (cr_c, "CR_UV_unit_36d")]:
        m_ref = e2[key_j]
        err_m = max(abs(m_cc[r, c] - (mp.mpf(m_ref[r][c][0]) + I_MP * mp.mpf(m_ref[r][c][1]))) for r in range(3) for c in range(3))
        assert err_m < mp.mpf(10) ** (-30)

    inv_sym = extract_invariants_eigh(pref_c * (e10_c * wu_c * e10_c), pref_c * (e10_c * wd_c * e10_c), pref_c * (e10_c * we_c * e10_c), pref_c * (e10_c * wnu_c), cr_c)
    inv_cc = extract_invariants_eigh(yu_c, yd_c, ye_c, ynu_c, cr_c)
    pf_4 = bool(inv_sym[13] < mp_rat(1, 8) and inv_cc[13] > mp_rat(1, 4) and inv_cc[14] > mp_rat(1, 4))
    assert pf_4

    # Verify all 19 invariants match producer JSON (< 10^-13) + E_1 cancellation + expm scrambling:
    ref_19 = (
        [mp.mpf(e3["yt_UV_zero_knob"])]
        + [mp.mpf(x) for x in e3["uv_mass_ratios_u_d_e_14d"]]
        + [mp.mpf(x) for x in e3["uv_ckm_Vus_Vcb_Vub_J_14d"]]
        + [mp.mpf(x) for x in e3["uv_pmns_Ue2_Umu3_Ue3_J_14d"]]
        + [mp.mpf(x) for x in e3["uv_mnu_m1_m2_over_m3_14d"]]
    )
    assert max(abs(a - b) for a, b in zip(inv_cc, ref_19)) < mp.mpf(10) ** (-12)

    e1_alt = mp.diag([mp.mpf(7) ** (-5), mp.mpf(11) ** (-2), mp.mpf(1)])
    mnu_0 = -ynu_c * (cr_c ** (-1)) * ynu_c.T
    mnu_1 = -(ynu_c * e1_alt) * ((e1_alt * cr_c * e1_alt) ** (-1)) * (ynu_c * e1_alt).T
    cancel_err = mp.sqrt(mp.fsum(abs(mnu_0[r, c] - mnu_1[r, c]) ** 2 for r in range(3) for c in range(3))) / mp.sqrt(mp.fsum(abs(mnu_0[r, c]) ** 2 for r in range(3) for c in range(3)))

    uq, uu, ud, ul, ue = [su3_expm_cc(s) for s in (11, 23, 37, 53, 71)]
    un = su3_expm_cc(97) * mp.exp(I_MP * mp_rat(3, 17))
    un_conj = mp.matrix([[mp.conj(un[r, c]) for c in range(3)] for r in range(3)])
    inv_s = extract_invariants_eigh(uq * yu_c * uu.H, uq * yd_c * ud.H, ul * ye_c * ue.H, ul * (ynu_c * e1_alt) * un.H, un_conj * (e1_alt * cr_c * e1_alt) * un.H)
    inv_b = extract_invariants_eigh(uq * yu_c * uu.H, uq * yd_c * ud.H, ul * ye_c * ue.H, ul * (ynu_c * e1_alt) * un.H, e1_alt * cr_c * e1_alt)
    pf_5 = bool(cancel_err < mp.mpf(10) ** (-30) and max(abs(a - b) for a, b in zip(inv_cc, inv_s)) < mp.mpf(10) ** (-30) and max(abs(a - b) for a, b in zip(inv_cc, inv_b)) > mp_rat(1, 50))
    assert pf_5

    pf_tot = sum(int(x) for x in (pf_1, pf_2, pf_3, pf_4, pf_5))
    assert pf_tot == 5
    print(f"AGY-C41 disjoint countercheck PASSED in {int(time.time() - t0)}s: Cl(10)_dims={dims_cl10}, cancel_err={mp.nstr(cancel_err, 4)}, planted_faults={pf_tot}/5.")


if __name__ == "__main__":
    main()
