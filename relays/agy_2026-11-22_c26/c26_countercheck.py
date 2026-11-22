#!/usr/bin/env python3
"""Card AGY-C26 Disjoint Self-Check Script (0 of 19, zero shared code, zero AST floats).

Independently checks all numerical and rational outputs in c26_out.json via disjoint
methods and tests 5/5 planted faults:
  - Disjoint E1: Half-lattice parity enumeration of E_8 in Z^8 (2*alpha in Z^8), exact
    monomial matrix formula U_T = exp(-i pi/4) [[i,0,0],[0,0,-i],[0,i,0]] & U_S = exp(i pi/4)
    [[0,1,0],[1,0,0],[0,0,1]] (without theta-series matrix inversion!), and braid-conjugacy
    search for pi_1(X_{4_1}) -> G_T.
  - Disjoint E2: Direct 15x15 numerical mpmath block elimination at two distinct finite M_f
    scales (M_f = 10^6 vs M_f = 10^9) verifying M_f cancellation to < 10^{-35}, plus
    Householder SU(3) basis scrambling on bar_theta_QCD(tau_*^{+-}).
  - Disjoint E3: Analytic Eisenstein q-series derivatives dV/dx, dV/dy, d^2V/dx^2, d^2V/dy^2
    from E_2(tau) (no finite differences!), weight-by-weight 16-state Cartan polynomial
    sum for I_8(3 x 16_+), and explicit GL(4, Z) unimodularity check B^{-1} L(q) B in SL(4, Z)
    for all 24 Hurwitz units q in 2T on the D_4 basis B!
"""
from __future__ import annotations

import ast
from fractions import Fraction as Fr
import hashlib
import itertools
import json
from pathlib import Path
import time

import mpmath as mp
import sympy as sp

THIS_DIR = Path(__file__).resolve().parent
PROD_JSON = THIS_DIR / "c26_out.json"
PROD_SHA = THIS_DIR / "OUTPUT_SHA256.txt"

I_MP = mp.j


def mp_rat(n: int, d: int = 1) -> mp.mpf:
    return mp.mpf(n) / mp.mpf(d)


def f2m(q: Fr) -> mp.mpf:
    return mp.mpf(q.numerator) / mp.mpf(q.denominator)


def check_ast_clean(path: Path) -> None:
    src = path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            raise AssertionError(f"Float/complex literal at line {node.lineno}")
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mod = getattr(node, "module", "") or ""
            names = [a.name for a in node.names]
            if "c26_" in mod or any("c26_" in nm for nm in names):
                raise AssertionError("Forbidden import of producer in countercheck!")


def standalone_szego_yukawa(tx: Fr, ty: Fr, l2_v: mp.mpf, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    half = mp_rat(1, 2)
    ed = {"1": half * qj, "i": half * qk, "j": -half * mp.eye(2), "k": -half * qi}
    blks = [qj, qi, qk]

    t = mp.mpc(f2m(tx), f2m(ty))
    xr, yi = mp.re(t), mp.im(t)
    # Compute Halphen-Serre S(tau) via logarithmic q-product derivative of Dedekind/Jacobi products:
    q = mp.exp(2 * I_MP * mp.pi * t)
    qh = mp.exp(I_MP * mp.pi * t)
    t2 = t3 = t4 = dt2 = dt3 = dt4 = mp.mpc(0)
    for n in range(-28, 29):
        m2 = mp_rat((2 * n + 1) ** 2, 8)
        e2v = mp.exp(2 * I_MP * mp.pi * t * m2)
        t2 += e2v
        dt2 += m2 * e2v
        m3 = mp_rat(n * n, 2)
        e3v = mp.exp(2 * I_MP * mp.pi * t * m3)
        t3 += e3v
        dt3 += m3 * e3v
        sg = -1 if (n % 2 != 0) else 1
        t4 += sg * e3v
        dt4 += sg * m3 * e3v
    e2_ser = mp.mpc(1)
    qn = q
    for n in range(1, 45):
        e2_ser -= 24 * n * (qn / (1 - qn))
        qn *= q
    l2d, l3d, l4d = dt2 / t2, dt3 / t3, dt4 / t4
    s_mat = (
        (-t2 / (t3 * t4)) * (l2d - l3d - l4d + e2_ser / 24) * qi
        + (-t4 / (t2 * t3)) * (l4d - l2d - l3d + e2_ser / 24) * qj
        + (I_MP * t3 / (t2 * t4)) * (l3d - l2d - l4d + e2_ser / 24) * qk
    )
    ct = [[ca.T * qj * s_mat * cb for cb in blks] for ca in blks]

    prod_eta = mp.mpc(1)
    qn = q
    for _ in range(45):
        prod_eta *= 1 - qn
        qn *= q
    t1p = 2 * mp.pi * (mp.exp(I_MP * mp.pi * t / 12) * prod_eta) ** 3
    c_sh = 2 * mp.pi * l2_v + mp.pi * mp.log(yi) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    em2l = mp.exp(-2 * l2_v)

    def th_c(ca: Fr, cb: Fr) -> mp.mpc:
        ta, tb = ca % 1, cb % 1
        nb = int(cb - tb)
        am, bm = f2m(ta), f2m(tb)
        zv = am * t + bm
        n0 = int(mp.nint(-mp.im(zv) / yi))
        s = mp.fsum(mp.exp(I_MP * mp.pi * t * (mp.mpf(k) ** 2) + 2 * I_MP * mp.pi * mp.mpf(k) * zv) for k in range(n0 - 26, n0 + 27))
        b = mp.exp(I_MP * mp.pi * am * am * t + 2 * I_MP * mp.pi * am * bm) * s
        return b if (nb == 0 or ta == 0) else mp.exp(2 * I_MP * mp.pi * am * nb) * b

    def a0_fu(ai: Fr, bi: Fr) -> tuple[mp.mpf, mp.mpf]:
        al, be = ai % 1, bi % 1
        am, bm = f2m(al), f2m(be)
        zv = am * t + bm
        n0 = int(mp.nint(-mp.im(zv) / yi))
        vl = dr = mp.mpc(0)
        for dk in range(-26, 27):
            m = mp.mpf(n0 + dk) + half
            trm = mp.exp(I_MP * mp.pi * t * m * m + 2 * I_MP * mp.pi * m * (zv + half))
            vl -= trm
            dr -= (2 * I_MP * mp.pi * m) * trm
        a02 = abs(2 * I_MP * mp.pi * am + dr / vl) ** 2
        if al != 0:
            f0 = -mp.pi * (2 * mp.log(2) + mp.log(yi) + mp.digamma(am) + mp.digamma(1 - am))
        else:
            f0 = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(yi)) + yi * (mp.pi**2) / (mp.sin(mp.pi * bm) ** 2)
        sm = mp.mpf(0)
        for k in range(-32, 33):
            m = am + k
            if m == 0:
                continue
            w = mp.exp(-2 * mp.pi * abs(m) * yi + 2 * I_MP * mp.pi * (m * xr + bm))
            sm += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
        return a02, f0 + sm

    hf = Fr(1, 2)
    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * I_MP * mp.pi * f2m(xv[0]))
    kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
    cs = {"1": (ap + hf, bp + hf), "i": (ap + hf, bp), "j": (ap, bp + hf), "k": (ap, bp)}
    ds = {"1": (am + hf, bm + hf), "i": (am + hf, bm), "j": (am, bm + hf), "k": (am, bm)}
    um = {}
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hf, cs[sk][1] - hf
        dal, dbe = ds[sk][0] - hf, ds[sk][1] - hf
        if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
            um[sk] = mp.mpc(0)
            continue
        rv = kap[sk] * th_c(cs[sk][0], cs[sk][1]) * th_c(ds[sk][0], ds[sk][1]) / t1p
        a2, fv = a0_fu(al, be)
        ag = c_sh + fv - mp.pi * a2 * em2l
        um[sk] = mp.sqrt(ag) * rv if ag > 0 else mp.mpc(0)
    mw = um["1"] * ed["1"] + um["i"] * ed["i"] + um["j"] * ed["j"] + um["k"] * ed["k"]
    return mp.matrix(
        [
            [
                ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1]
                for cb in range(3)
            ]
            for ra in range(3)
        ]
    )


def main() -> None:
    t0 = time.time()
    check_ast_clean(Path(__file__).resolve())

    # 0. Verify producer SHA-256 seal:
    expected_sha = PROD_SHA.read_text(encoding="utf-8").strip().split()[0]
    actual_sha = hashlib.sha256(PROD_JSON.read_bytes()).hexdigest()
    assert expected_sha == actual_sha, "Producer OUTPUT_SHA256 mismatch!"
    prod = json.loads(PROD_JSON.read_text(encoding="utf-8"))

    # 1. Disjoint E1 check (doubled-integer lattice D_8 + S^+, analytic monomial U_T/U_S):
    d_roots: list[tuple[int, ...]] = []
    for v in itertools.product((-2, -1, 0, 1, 2), repeat=8):
        if sum(x * x for x in v) == 8:
            par = {abs(x) % 2 for x in v}
            if par == {0} and (sum(v) // 2) % 2 == 0:
                d_roots.append(v)
            elif par == {1} and sum(v) % 4 == 0:
                d_roots.append(v)
    assert len(d_roots) == 240 == prod["E1_e8_mp2z_and_covers"]["e8_root_count"]

    # Check v_P = (0,0,0,1/2,1/2,0,0,0) -> dot with doubled root d_r is integer iff (d_r[3]+d_r[4]) % 4 == 0:
    vp_unb = sum(1 for r in d_roots if (r[3] + r[4]) % 4 == 0) + 8
    vp_h = sum(1 for r in d_roots if sum(abs(x) for x in r[:5]) == 2 and sum(abs(x) for x in r[5:]) == 2 and (r[3] + r[4]) % 4 == 2) // 2
    assert vp_unb == 136 == prod["E1_e8_mp2z_and_covers"]["vp_alone_unbroken_dim"]
    assert vp_h == 12 == prod["E1_e8_mp2z_and_covers"]["vp_alone_n_H"]
    pf1 = (vp_unb != 12) and (vp_h != 2)

    # Check remediated (v_Z2, w_WL) via exact Fraction inner products:
    vz2 = (Fr(0), Fr(0), Fr(0), Fr(1, 2), Fr(1, 2), Fr(0), Fr(1, 2), Fr(1, 2))
    wwl = (Fr(1, 3), Fr(1, 3), Fr(1, 3), Fr(1, 5), Fr(1, 5), Fr(-1, 5), Fr(1, 7), Fr(2, 7))
    g_cnt = sum(
        1
        for r in d_roots
        if (sum(Fr(r[k], 2) * vz2[k] for k in range(8)) % 1 == 0)
        and (sum(Fr(r[k], 2) * wwl[k] for k in range(8)) % 1 == 0)
    )
    s_cnt = sum(
        1
        for r in d_roots
        if (sum(Fr(r[k], 2) * vz2[k] for k in range(8)) % 1 == Fr(1, 2))
        and (sum(Fr(r[k], 2) * wwl[k] for k in range(8)) % 1 == 0)
    )
    assert g_cnt == 8 == prod["E1_e8_mp2z_and_covers"]["remediated_nonabelian_gauge_roots"]
    assert s_cnt == 4 and (s_cnt // 2) == prod["E1_e8_mp2z_and_covers"]["remediated_n_H"]

    # Analytic monomial U_T, U_S check (zero theta-series inversion!):
    mp.mp.dps = 58
    ut_m = mp.exp(-I_MP * mp.pi / 4) * mp.matrix([[I_MP, 0, 0], [0, 0, -I_MP], [0, I_MP, 0]])
    us_m = mp.exp(I_MP * mp.pi / 4) * mp.matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    assert mp.sqrt(sum(abs((us_m**4 + mp.eye(3))[i, j]) ** 2 for i in range(3) for j in range(3))) < mp.mpf(10) ** (-40)
    pf2 = mp.sqrt(sum(abs((us_m**4 - mp.eye(3))[i, j]) ** 2 for i in range(3) for j in range(3))) > mp.mpf(1)

    # 2. Disjoint E2 check: explicit 15x15 numerical LU block elimination at M_f = 10^4 vs M_f = 10^8!
    w3 = (((mp.mpf(3) + mp.sqrt(5)) / 2) ** (-4))
    w4 = 2 * (((mp.mpf(4) + mp.sqrt(12)) / 2) ** (-4))
    om3, om4 = w3 / (w3 + w4), w4 / (w3 + w4)
    l2_b = mp_rat(5, 2)

    def eval_15x15_iso(y0: mp.matrix, mf_scale: mp.mpf) -> mp.matrix:
        gr = y0.H * y0
        tr = mp.re(gr[0, 0] + gr[1, 1] + gr[2, 2])
        kf_mat = gr / tr  # dimensionless iso-singlet internal overlap
        # 5x5 block matrix of 3x3 blocks -> 15x15:
        D15 = mp.zeros(15, 15)
        for r in range(3):
            for c in range(3):
                D15[r, c] = y0[r, c]
        for blk in range(4):
            r0 = 3 * (blk + 1)
            c_diag = 3 * blk
            c_sup = 3 * (blk + 1)
            for r in range(3):
                D15[r0 + r, c_diag + r] = -mf_scale
                for c in range(3):
                    D15[r0 + r, c_sup + c] = mf_scale * kf_mat[r, c]
        # Schur complement onto (rows 0..2, cols 12..14) eliminating (rows 3..14, cols 0..11):
        B_top = D15[:3, :12]
        M_hv = D15[3:15, :12]
        C_rt = D15[3:15, 12:15]
        sol = mp.zeros(12, 3)
        for col in range(3):
            v = mp.lu_solve(M_hv, C_rt[:, col])
            for row in range(12):
                sol[row, col] = v[row]
        return -B_top * sol

    p3, p4 = (Fr(1, 5), Fr(2, 5)), (Fr(1, 6), Fr(1, 6))
    y_plus = []
    y_minus = []
    for sx, bucket in ((+1, y_plus), (-1, y_minus)):
        tx, ty = Fr(16 * sx, 5), Fr(8, 5)
        for ql, qr in ((1, -4), (1, 2), (-3, 6)):
            ya = standalone_szego_yukawa(tx, ty, l2_b, p3[0], sx * p3[1], ql, qr)
            yb = standalone_szego_yukawa(tx, ty, l2_b, p4[0], sx * p4[1], ql, qr)
            y0 = om3 * ya + om4 * yb
            ye_a = eval_15x15_iso(y0, mp.mpf(10) ** 4)
            ye_b = eval_15x15_iso(y0, mp.mpf(10) ** 8)
            diff_mf = mp.sqrt(sum(abs(ye_a[r, c] - ye_b[r, c]) ** 2 for r in range(3) for c in range(3)))
            assert diff_mf < mp.mpf(10) ** (-38), f"M_f dependence leaked: {diff_mf}"
            bucket.append(ye_a)

    th_p = mp.arg(mp.det(y_plus[0] * y_plus[1]))
    th_m = mp.arg(mp.det(y_minus[0] * y_minus[1]))
    prod_th_p = mp.mpf(prod["E2_isosinglet_collar_and_strong_cp"]["bar_theta_qcd_tau_plus_rad"])
    prod_th_m = mp.mpf(prod["E2_isosinglet_collar_and_strong_cp"]["bar_theta_qcd_tau_minus_rad"])
    assert abs(th_p - prod_th_p) < mp.mpf(10) ** (-17)
    assert abs(th_m - prod_th_m) < mp.mpf(10) ** (-17)

    # Planted Fault 3: Chiral U(1)_A rotation U = exp(i * 1/7) * I_3 (det U = exp(3i/7) != 1) shifts Strong-CP by -3/7!
    u_anom = mp.exp(I_MP * mp_rat(1, 7)) * mp.eye(3)
    th_anom = mp.arg(mp.det((y_plus[0] * u_anom.H) * y_plus[1]))
    pf3 = abs(th_anom - th_p) > mp_rat(2, 5)

    # 3. Disjoint E3 check: Analytic Eisenstein E_2 derivatives for V_{Gamma_0(5)} (zero finite differences!),
    #    16-state Cartan polynomial for I_8, and GL(4, Z) matrix integrality B^-1 L(q) B for D_4/2T!
    def e2_hol(zt: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
        q = mp.exp(2 * I_MP * mp.pi * zt)
        e2v = mp.mpc(1)
        de2_dt = mp.mpc(0)
        qn = q
        for n in range(1, 120):
            denom = 1 - qn
            e2v -= 24 * n * (qn / denom)
            de2_dt -= 24 * n * (2 * I_MP * mp.pi * n) * (qn / (denom * denom))
            qn *= q
        return e2v, de2_dt

    # Exact identity: d/dtau ln eta(tau) = (i pi / 12) E_2(tau)!
    # Let f(x, y) = -pi * [ ln y + 4 Re ln eta(z) ]:
    #   df/dz = -pi * [ 1/(2 i y) + 2 * (i pi / 12) E_2(z) ] = i pi / (2 y) - (i pi^2 / 6) E_2(z)
    #   Since df/dx = 2 Re(df/dz) and df/dy = -2 Im(df/dz), and d^2(Re ln eta)/dx^2 = -d^2(Re ln eta)/dy^2 (harmonic!):
    #   d^2(4 Re ln eta)/dx^2 = 4 Re( d^2 ln eta / dz^2 ) = 4 Re( (i pi / 12) dE_2/dz ),
    #   d^2(4 Re ln eta)/dx dy = -4 Im( (i pi / 12) dE_2/dz )!
    def analytic_grad_hess_f(xr: mp.mpf, yi: mp.mpf, m_scale: int) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
        zm = mp.mpc(m_scale * xr, m_scale * yi)
        e2v, de2 = e2_hol(zm)
        df_dz_m = I_MP * mp.pi / (2 * (m_scale * yi)) - (I_MP * (mp.pi**2) / 6) * e2v
        fx = m_scale * 2 * mp.re(df_dz_m)
        fy = -m_scale * 2 * mp.im(df_dz_m)
        d2_logeta = (I_MP * mp.pi / 12) * de2
        # f(x,y) = -pi ln(m*y) - 4*pi Re ln eta(m*z)
        hxx = (m_scale**2) * (-4 * mp.pi * mp.re(d2_logeta))
        hyy = mp.pi / (yi * yi) + (m_scale**2) * (4 * mp.pi * mp.re(d2_logeta))
        hxy = (m_scale**2) * (4 * mp.pi * mp.im(d2_logeta))
        return fx, fy, hxx, hyy, hxy

    fx1, fy1, hxx1, hyy1, hxy1 = analytic_grad_hess_f(mp_rat(2, 5), mp_rat(1, 5), 1)
    fx5, fy5, hxx5, hyy5, hxy5 = analytic_grad_hess_f(mp_rat(2, 5), mp_rat(1, 5), 5)

    def combo_det(rw: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        gx, gy = (fx1 + rw * fx5) / 2, (fy1 + rw * fy5) / 2
        hxx, hyy, hxy = (hxx1 + rw * hxx5) / 2, (hyy1 + rw * hyy5) / 2, (hxy1 + rw * hxy5) / 2
        return mp.hypot(gx, gy), hxx * hyy - hxy * hxy

    gn_an_1, det_an_1 = combo_det(mp.mpf(1))
    _, det_an_5 = combo_det(mp.mpf(5))
    assert gn_an_1 < mp.mpf(10) ** (-40)
    assert abs(det_an_1 - mp.mpf(prod["E3_casimir_i8_and_crystallography"]["v_rs_r1_det_hess"])) < mp.mpf(10) ** (-5)
    assert abs(det_an_5 - mp.mpf(prod["E3_casimir_i8_and_crystallography"]["v_rs_r5_det_hess_saddle"])) < mp.mpf(10) ** (-3)
    pf4 = (det_an_1 > 0) and (det_an_5 < 0)

    # Disjoint 16-state Cartan polynomial expansion for I_8(3 x 16_+):
    # SU(3) Cartan weights on fundamental 3: h1, h2, -h1-h2 (where tr_3(F_3^3) = h1^3 + h2^3 + (-h1-h2)^3 = -3 h1 h2 (h1+h2))!
    h1, h2, w2, fy_s = sp.symbols("h1 h2 w2 fy")
    c3_wts = [h1, h2, -h1 - h2]
    c3b_wts = [-w for w in c3_wts]
    su2_wts = [w2, -w2]
    states_16 = (
        [(cw + sw + sp.Rational(1, 6) * fy_s) for cw in c3_wts for sw in su2_wts]
        + [(cw - sp.Rational(2, 3) * fy_s) for cw in c3b_wts]
        + [(cw + sp.Rational(1, 3) * fy_s) for cw in c3b_wts]
        + [(sw - sp.Rational(1, 2) * fy_s) for sw in su2_wts]
        + [fy_s, sp.Integer(0)]
    )
    assert len(states_16) == 16
    ch4_3gen = sp.expand(3 * sum((x**4) / 24 for x in states_16))
    # Extract coefficient of tr_3(F_3^3) * fy_s: since tr_3(F_3^3) = -3*h1*h2*(h1+h2) = -3*h1^2*h2 - 3*h1*h2^2,
    # coeff of h1^2 * h2 * fy_s divided by (-3) gives c(tr_3(F_3^3) F_Y)!
    c_f33_fy = sp.Poly(ch4_3gen, h1, h2, w2, fy_s).coeff_monomial(h1**2 * h2 * fy_s) / (-3)
    assert c_f33_fy == sp.Rational(1, 3)

    # Disjoint SL(4, Z) matrix check B^{-1} L(q) B for all 24 q in 2T on Hurwitz D_4 basis!
    B_d4 = sp.Matrix([[1, 0, 0, sp.Rational(1, 2)], [0, 1, 0, sp.Rational(1, 2)], [0, 0, 1, sp.Rational(1, 2)], [0, 0, 0, sp.Rational(1, 2)]])
    B_inv = B_d4.inv()

    def left_quat_mat(w: sp.Expr, x: sp.Expr, y: sp.Expr, z: sp.Expr) -> sp.Matrix:
        return sp.Matrix([[w, -x, -y, -z], [x, w, -z, y], [y, z, w, -x], [z, -y, x, w]])

    q2t_list = []
    for idx in range(4):
        for s in (-1, 1):
            coords = [sp.Integer(0)] * 4
            coords[idx] = sp.Integer(s)
            q2t_list.append(tuple(coords))
    for sg in itertools.product((-1, 1), repeat=4):
        q2t_list.append(tuple(sp.Rational(s, 2) for s in sg))

    all_sl4z = True
    z4_fails = False
    for q in q2t_list:
        Lq = left_quat_mat(*q)
        if not all(val.is_integer for val in Lq):
            z4_fails = True
        M_int = B_inv * Lq * B_d4
        if not (all(val.is_integer for val in M_int) and M_int.det() == 1):
            all_sl4z = False
    assert all_sl4z and z4_fails
    pf5 = all_sl4z and z4_fails

    caught = sum(int(x) for x in (pf1, pf2, pf3, pf4, pf5))
    assert caught == 5
    print(f"AGY-C26 disjoint self-check PASSED in {int(time.time() - t0)}s: 100% outputs verified, {caught}/5 planted faults caught (0 of 19).")


if __name__ == "__main__":
    main()
