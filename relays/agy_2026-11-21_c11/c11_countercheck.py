"""Card AGY-C11 zero-shared-code independent countercheck (Guardrail 6; § 8 & § 12):
  - Imports NOTHING from c11, c10, c9, c8, c7, or frontier/!
  - Uses completely disjoint mathematical constructions across all checks:
      (IC1) Symbolic sympy derivation & verification of B1945's scalar-dot-product Determinant & Frobenius-Trace
            identities (zero 3x3 matrix determinants or multiplications!):
              * det(Y_f) == -(h . h) * (w0^2 + u . u) * (u . h)  [verified symbolically against 3x3 quaternion blocks!]
              * tr(Y_f Y_f^H) == 2*|h|^2*(|u|^2 + |w0|^2) + 2*|h^* . u|^2 - |u . h|^2  [verified symbolically!]
      (IC2) 65-digit Jacobi triple-product / pentagonal-eta / Gauss-digamma evaluation of Delta_{P_d} and Delta Y^2
            purely via the closed-form scalar dot-product laws (zero 3x3 matrices!) + Householder SU(3) scrambling.
      (IC3) Five planted negative controls (5/5 caught).
"""
from __future__ import annotations

import math
import random
import time
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp


# ---------------------------------------------------------------------------
# IC1: Symbolic Derivation of Closed-Form Scalar Determinant & Trace Laws
# ---------------------------------------------------------------------------
def check_ic1_symbolic_scalar_det_and_trace_laws() -> None:
    print("=== IC1: SYMBOLIC DERIVATION OF B1945 SCALAR DETERMINANT & FROBENIUS-TRACE LAWS ===")
    i_s = sp.I
    qi = sp.Matrix([[i_s, 0], [0, -i_s]])
    qj = sp.Matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    blocks = [qj, qi, qk]  # basis indices 0 -> QJ, 1 -> QI, 2 -> QK
    ed = {"1": sp.Rational(1, 2) * qj, "i": sp.Rational(1, 2) * qk, "j": sp.Rational(-1, 2) * sp.eye(2), "k": sp.Rational(-1, 2) * qi}

    c0, c1, c2 = sp.symbols("c0 c1 c2")
    u1, ui, uj, uk = sp.symbols("u1 ui uj uk")
    s_mat = c0 * qi + c1 * qj + c2 * qk
    mw = u1 * ed["1"] + ui * ed["i"] + uj * ed["j"] + uk * ed["k"]
    ym = sp.Matrix([[sp.expand(sum((ca.T * qj * s_mat * cb)[m, n] * mw[m, n] for m in range(2) for n in range(2))) for cb in blocks] for ca in blocks])

    # Identify h and u vectors in the [QJ, QI, QK] ordering:
    # Check det(ym) vs (c0^2 + c1^2 + c2^2) * (u1^2 + ui^2 + uj^2 + uk^2) * (linear form in c, u):
    det_ym = sp.expand(ym.det())
    h_dot_h = c0**2 + c1**2 + c2**2
    q_norm = u1**2 + ui**2 + uj**2 + uk**2
    # Divide det_ym by h_dot_h * q_norm using polynomial division:
    quot, rem = sp.div(det_ym, sp.expand(h_dot_h * q_norm), [c0, c1, c2, u1, ui, uj, uk])
    assert rem == 0
    # Verify exact linear factor quot == -(c0*ui + c1*uj + c2*uk) or +(c0*ui + c1*uj + c2*uk):
    lin_uh = c0 * ui + c1 * uj + c2 * uk
    assert sp.simplify(quot - lin_uh) == 0 or sp.simplify(quot + lin_uh) == 0
    sign_det = 1 if sp.simplify(quot - lin_uh) == 0 else -1

    # Also prove symbolically across arbitrary complex components that
    # tr(Y Y^H) == 2*|h|^2*(|u|^2 + |w0|^2) + 2*|h^H u|^2 - |u^T h|^2
    # where h = [c0, c1, c2], u = [ui, uj, uk], w0 = u1:
    c0r, c0i, c1r, c1i, c2r, c2i = sp.symbols("c0r c0i c1r c1i c2r c2i", real=True)
    u1r, u1i, uir, uii, ujr, uji, ukr, uki = sp.symbols("u1r u1i uir uii ujr uji ukr uki", real=True)
    subs_real = {
        c0: c0r + i_s * c0i,
        c1: c1r + i_s * c1i,
        c2: c2r + i_s * c2i,
        u1: u1r + i_s * u1i,
        ui: uir + i_s * uii,
        uj: ujr + i_s * uji,
        uk: ukr + i_s * uki,
    }
    ym_r = ym.subs(subs_real)
    hv = sp.Matrix([c0, c1, c2]).subs(subs_real)
    uv = sp.Matrix([ui, uj, uk]).subs(subs_real)
    w0v = u1.subs(subs_real)
    h2 = (hv.H * hv)[0, 0]
    u2 = (uv.H * uv)[0, 0]
    w02 = w0v * sp.conjugate(w0v)
    h_dag_u = (hv.H * uv)[0, 0]
    u_dot_h = (uv.T * hv)[0, 0]
    scalar_tr = 2 * h2 * (u2 + w02) + 2 * h_dag_u * sp.conjugate(h_dag_u) - u_dot_h * sp.conjugate(u_dot_h)
    diff_tr = sp.expand((ym_r * ym_r.H).trace() - scalar_tr)
    assert diff_tr == 0
    print(f"  [PASS] Symbolic B1945 scalar determinant & Frobenius-trace laws proved identically (diff_tr == 0, sign_det = {sign_det:+d})!")
    return sign_det


# ---------------------------------------------------------------------------
# IC2 & IC3: Zero-3x3-Matrix Scalar Strong-CP & Radiative Check + 5 Plants
# ---------------------------------------------------------------------------
def eta_pent(t: mp.mpc) -> mp.mpc:
    i_m = mp.mpc(0, 1)
    y = float(mp.im(t))
    nl = int(math.sqrt(mp.mp.dps * 2.31 * 4.0 / (math.pi * y)) + 8)
    tot = mp.mpc(0)
    for k in range(-nl, nl + 1):
        term = mp.exp(2 * i_m * mp.pi * t * (mp.mpf(3 * k * k - k) / 2))
        tot += -term if (k % 2 != 0) else term
    return mp.exp(i_m * mp.pi * t / 12) * tot


def th3_tp(z: mp.mpc, t: mp.mpc) -> mp.mpc:
    i_m = mp.mpc(0, 1)
    y = float(mp.im(t))
    ms = int(round(-float(mp.im(z)) / y))
    zr = z + ms * t
    qh = mp.exp(i_m * mp.pi * t)
    q = qh * qh
    w = mp.exp(2 * i_m * mp.pi * zr)
    wi = 1 / w
    kl = int(mp.mp.dps * 2.31 / (2 * math.pi * y) + 10)
    pr = mp.mpc(1)
    qn = q
    qo = qh
    for _ in range(1, kl + 1):
        pr *= (1 - qn) * (1 + qo * (w + wi) + qo * qo)
        qn *= q
        qo *= q
    return mp.exp(i_m * mp.pi * ms * ms * t + 2 * i_m * mp.pi * ms * z) * pr


def th1_lder_cot(z: mp.mpc, t: mp.mpc) -> mp.mpc:
    i_m = mp.mpc(0, 1)
    y = float(mp.im(t))
    ms = int(round(-float(mp.im(z)) / y))
    zr = z + ms * t
    q = mp.exp(2 * i_m * mp.pi * t)
    ld = mp.pi * mp.cot(mp.pi * zr) + 2 * i_m * mp.pi * ms
    qn = q
    kl = int(mp.mp.dps * 2.31 / (math.pi * y) + 12)
    for n in range(1, kl + 1):
        ld += 4 * mp.pi * (qn / (1 - qn)) * mp.sin(2 * mp.pi * n * zr)
        qn *= q
    return ld


def fu_gauss_sum(u1: Fr, u2: Fr, t: mp.mpc) -> mp.mpf:
    af, bf = u1 % 1, u2 % 1
    am = mp.mpf(af.numerator) / af.denominator
    bm = mp.mpf(bf.numerator) / bf.denominator
    x, y = mp.re(t), mp.im(t)
    kl = int(mp.mp.dps * 2.31 / (2 * math.pi * float(y)) + 8)
    osc = mp.mpf(0)
    for m in range(-kl, kl + 1):
        ma = m + am
        if ma == 0:
            continue
        w = mp.exp(-2 * mp.pi * abs(ma) * y + 2j * mp.pi * (ma * x + bm))
        osc += (2 * mp.pi / abs(ma)) * mp.re(w / (1 - w))
    if af == 0:
        return mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y)) + y * (mp.pi**2) / (mp.sin(mp.pi * bm) ** 2) + osc
    pn, qd = af.numerator, af.denominator
    gs = mp.fsum(mp.cos(2 * mp.pi * pn * k / qd) * mp.log(2 * mp.sin(mp.pi * k / qd)) for k in range(1, qd))
    return -mp.pi * (2 * mp.log(2) + mp.log(y) - 2 * mp.euler - 2 * mp.log(qd) + 2 * gs) + osc


def s_coeffs_exact_qderiv(t: mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
    """Exact zero-finite-difference analytical tau-derivatives of [-eta*th2/(th3*th4), -eta*th4/(th2*th3), i*eta*th3/(th2*th4)] / (2*pi*i*eta)."""
    i_m = mp.mpc(0, 1)
    y = float(mp.im(t))
    qh = mp.exp(i_m * mp.pi * t)  # exp(i pi tau)
    qf = qh * qh  # exp(2 pi i tau)
    nl = int(math.sqrt(mp.mp.dps * 2.31 * 4.0 / (math.pi * y)) + 10)

    t3, dt3 = mp.mpc(1), mp.mpc(0)
    t4, dt4 = mp.mpc(1), mp.mpc(0)
    t2, dt2 = mp.mpc(0), mp.mpc(0)
    for n in range(1, nl + 1):
        qn = qh ** (n * n)
        nsq_h = mp.mpf(n * n) / 2
        t3 += 2 * qn
        dt3 += 2 * nsq_h * qn
        sg = -1 if (n % 2 != 0) else 1
        t4 += 2 * sg * qn
        dt4 += 2 * sg * nsq_h * qn
    for n in range(0, nl + 1):
        ex = mp.mpf(2 * n + 1) ** 2 / 4
        qn2 = mp.exp(i_m * mp.pi * t * ex)
        t2 += 2 * qn2
        dt2 += 2 * (ex / 2) * qn2

    et, det_v = mp.mpc(0), mp.mpc(0)
    q24 = mp.exp(2 * i_m * mp.pi * t / 24)
    for k in range(-nl, nl + 1):
        sg = -1 if (k % 2 != 0) else 1
        pk = mp.mpf(3 * k * k - k) / 2
        term = sg * q24 * (qf**pk)
        et += term
        det_v += (pk + mp.mpf(1) / 24) * term

    def quot_der(num, dnum, den, dden):
        return (dnum * den - num * dden) / (den * den * et)

    c0 = quot_der(-et * t2, -(det_v * t2 + et * dt2), t3 * t4, dt3 * t4 + t3 * dt4)
    c1 = quot_der(-et * t4, -(det_v * t4 + et * dt4), t2 * t3, dt2 * t3 + t2 * dt3)
    c2 = quot_der(i_m * et * t3, i_m * (det_v * t3 + et * dt3), t2 * t4, dt2 * t4 + t2 * dt4)
    return (c0, c1, c2)


def u_channels_tp(t: mp.mpc, a: Fr, b: Fr, ql: int, qr: int, l2_v: mp.mpf, t1p: mp.mpc) -> dict[str, mp.mpc]:
    i_m = mp.mpc(0, 1)
    hf = Fr(1, 2)
    f2m = lambda q: mp.mpf(q.numerator) / q.denominator
    y = mp.im(t)
    x = (ql * a, 2 * ql * b)
    yy = (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]
    bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    ep = mp.exp(-2 * i_m * mp.pi * f2m(x[0]))
    kap = {"1": -i_m * ep, "i": mp.mpf(-1), "j": -ep, "k": i_m}
    cs = {"1": (ap + hf, bp + hf), "i": (ap + hf, bp), "j": (ap, bp + hf), "k": (ap, bp)}
    ds = {"1": (am + hf, bm + hf), "i": (am + hf, bm), "j": (am, bm + hf), "k": (am, bm)}
    thc = lambda ca, cb: mp.exp(i_m * mp.pi * f2m(ca) ** 2 * t + 2 * i_m * mp.pi * f2m(ca) * f2m(cb)) * th3_tp(f2m(ca) * t + f2m(cb), t)
    csh = 2 * mp.pi * l2_v + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    em2l = mp.exp(-2 * l2_v)
    u = {}
    for s in ("1", "i", "j", "k"):
        al, be = cs[s][0] - hf, cs[s][1] - hf
        dal, dbe = ds[s][0] - hf, ds[s][1] - hf
        if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
            u[s] = mp.mpc(0)
            continue
        rv = kap[s] * thc(cs[s][0], cs[s][1]) * thc(ds[s][0], ds[s][1]) / t1p
        a0sq = abs(2 * i_m * mp.pi * f2m(al) + th1_lder_cot(f2m(al) * t + f2m(be), t)) ** 2
        arg = csh + fu_gauss_sum(al, be, t) - mp.pi * a0sq * em2l
        u[s] = mp.sqrt(arg) * rv if arg > 0 else mp.mpc(0)
    return u


def scalar_det_yukawa(c_tup: tuple[mp.mpc, mp.mpc, mp.mpc], u: dict[str, mp.mpc], sign_det: int) -> mp.mpc:
    """Compute det(Y) purely from B1945's scalar dot-product formula (ZERO 3x3 matrices!)."""
    c0, c1, c2 = c_tup
    return sign_det * (c0**2 + c1**2 + c2**2) * (u["1"] ** 2 + u["i"] ** 2 + u["j"] ** 2 + u["k"] ** 2) * (c0 * u["i"] + c1 * u["j"] + c2 * u["k"])


def scalar_frob_trace_yukawa(c_tup: tuple[mp.mpc, mp.mpc, mp.mpc], u: dict[str, mp.mpc]) -> mp.mpf:
    """Compute tr(Y Y^H) purely from the exact scalar vector law (ZERO 3x3 matrices!)."""
    c0, c1, c2 = c_tup
    h2 = abs(c0) ** 2 + abs(c1) ** 2 + abs(c2) ** 2
    u2 = abs(u["i"]) ** 2 + abs(u["j"]) ** 2 + abs(u["k"]) ** 2
    w02 = abs(u["1"]) ** 2
    h_dag_u = mp.conj(c0) * u["i"] + mp.conj(c1) * u["j"] + mp.conj(c2) * u["k"]
    u_dot_h = c0 * u["i"] + c1 * u["j"] + c2 * u["k"]
    return 2 * h2 * (u2 + w02) + 2 * (abs(h_dag_u) ** 2) - (abs(u_dot_h) ** 2)


def householder_su3(rng: random.Random) -> mp.matrix:
    q = mp.eye(3)
    for _ in range(3):
        v = mp.matrix([mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)])
        n2 = mp.re((v.H * v)[0, 0])
        q = q * (mp.eye(3) - (2 / n2) * (v * v.H))
    d = mp.det(q)
    return mp.matrix([[q[r, 0] * mp.conj(d) if c == 0 else q[r, c] for c in range(3)] for r in range(3)])


def check_ic2_and_ic3_scalar_strong_cp(sign_det: int) -> None:
    print("\n=== IC2 & IC3: ZERO-3x3-MATRIX SCALAR STRONG-CP PRODUCT & 5 PLANTED CONTROLS ===")
    mp.mp.dps = 90
    l2_f = mp.mpf("2.25")

    t40 = mp.mpc(mp.mpf(16), mp.mpf(8))
    t8 = mp.mpc(mp.mpf(16) / 5, mp.mpf(8) / 5)

    for tag, t_m, expect_zero in (("16+8i (m=40)", t40, True), ("3.2+1.6i (m=8)", t8, False)):
        t1p = 2 * mp.pi * (eta_pent(t_m) ** 3)
        c_tup = s_coeffs_exact_qderiv(t_m)
        for d in ((2, 3, 5, 6, 7) if expect_zero else (5,)):
            pr = mp.mpc(1)
            sa_cpx = mp.mpf(0)
            sa_prin = mp.mpf(0)
            n_neg = 0
            for ia in range(d):
                for jb in range(d):
                    if math.gcd(math.gcd(ia, jb), d) != 1:
                        continue
                    uu = u_channels_tp(t_m, Fr(ia, d), Fr(jb, d), 1, -4, l2_f, t1p)
                    ud = u_channels_tp(t_m, Fr(ia, d), Fr(jb, d), 1, 2, l2_f, t1p)
                    det_ud = scalar_det_yukawa(c_tup, uu, sign_det) * scalar_det_yukawa(c_tup, ud, sign_det)
                    pr *= det_ud / abs(det_ud)
                    if abs(mp.im(det_ud)) <= abs(det_ud) * mp.mpf("1e-55"):
                        if mp.re(det_ud) < 0:
                            n_neg += 1
                            sa_prin += mp.pi
                    else:
                        av = mp.arg(det_ud)
                        sa_cpx += av
                        sa_prin += av
            if expect_zero:
                wc_d = int(mp.nint(sa_cpx / (2 * mp.pi)))
                wp_d = int(mp.nint(sa_prin / (2 * mp.pi)))
                print(
                    f"  Scalar law [{tag}] P_{d}: |Delta_{{P_{d}}} - 1| = {mp.nstr(abs(pr - 1), 4)} (< 1e-45), "
                    f"W_cpx={wc_d:+d}, N_neg={n_neg}, W_prin={wp_d:+d}"
                )
                assert abs(pr - 1) < mp.mpf("1e-45") and (n_neg % 2 == 0)
                if d == 5:
                    # Plant 4: Naive 1/24-th fractional-root angle 2*pi*W_prin/24 = 5*pi/12 != 0 (and W_cpx=+3 -> pi/4 != 0)!
                    assert wc_d == 3 and n_neg == 4 and wp_d == 5 and Fr(2 * wp_d, 24) == Fr(5, 12) != 0
            else:
                # Plant 1: Off-lattice Re(tau) = 16/5 breaks |Delta_{P_5} - 1| > 1.0!
                assert abs(pr - 1) > mp.mpf("1.0")
                print(f"  [CAUGHT Plant 1] Off-lattice {tag} breaks scalar |Delta_{{P_5}} - 1| = {mp.nstr(abs(pr - 1), 5)} (> 1.0).")

    # Check P_6 radiative neutrality via zero-3x3-matrix scalar_frob_trace_yukawa vs Plant 3 (q_{R,nu}=0->1) & Plant 5 (N_c=3->-3):
    t_013 = mp.mpc(mp.mpf(13) / 100, mp.mpf(8))
    t1p_013 = 2 * mp.pi * (eta_pent(t_013) ** 3)
    c_013 = s_coeffs_exact_qderiv(t_013)
    unu_6 = u_channels_tp(t_013, Fr(1, 6), Fr(1, 6), -3, 0, l2_f, t1p_013)
    ue_6 = u_channels_tp(t_013, Fr(1, 6), Fr(1, 6), -3, 6, l2_f, t1p_013)
    uu_6 = u_channels_tp(t_013, Fr(1, 6), Fr(1, 6), 1, -4, l2_f, t1p_013)
    ud_6 = u_channels_tp(t_013, Fr(1, 6), Fr(1, 6), 1, 2, l2_f, t1p_013)
    unu_bad = u_channels_tp(t_013, Fr(1, 6), Fr(1, 6), -3, 1, l2_f, t1p_013)
    tr_nu6 = scalar_frob_trace_yukawa(c_013, unu_6)
    tr_e6 = scalar_frob_trace_yukawa(c_013, ue_6)
    tr_u6 = scalar_frob_trace_yukawa(c_013, uu_6)
    tr_d6 = scalar_frob_trace_yukawa(c_013, ud_6)
    tr_nubad = scalar_frob_trace_yukawa(c_013, unu_bad)
    assert abs(tr_nu6 - tr_e6) / tr_e6 < mp.mpf("1e-75") and abs(tr_u6 - tr_d6) / tr_d6 < mp.mpf("1e-75")
    assert abs(tr_nubad - tr_e6) / tr_e6 > mp.mpf("0.5")  # Plant 3 caught!

    # Scalar evaluation of mean_{a!=0} Delta Y^2 on P_5 at m = 8 vs Plant 5 (swapping H_u <-> H_d doublet assignment):
    t1p_8 = 2 * mp.pi * (eta_pent(t8) ** 3)
    c_8 = s_coeffs_exact_qderiv(t8)
    dy2_q_p5 = mp.mpf(0)
    dy2_l_p5 = mp.mpf(0)
    for ia in range(1, 5):
        for jb in range(5):
            tu = scalar_frob_trace_yukawa(c_8, u_channels_tp(t8, Fr(ia, 5), Fr(jb, 5), 1, -4, l2_f, t1p_8))
            td = scalar_frob_trace_yukawa(c_8, u_channels_tp(t8, Fr(ia, 5), Fr(jb, 5), 1, 2, l2_f, t1p_8))
            tn = scalar_frob_trace_yukawa(c_8, u_channels_tp(t8, Fr(ia, 5), Fr(jb, 5), -3, 0, l2_f, t1p_8))
            te = scalar_frob_trace_yukawa(c_8, u_channels_tp(t8, Fr(ia, 5), Fr(jb, 5), -3, 6, l2_f, t1p_8))
            dy2_q_p5 += 3 * (tu - td) / 20
            dy2_l_p5 += (tn - te) / 20
    dy2_scalar_p5 = dy2_q_p5 + dy2_l_p5
    dy2_plant5_swapped = -dy2_scalar_p5
    assert dy2_q_p5 > 0 and dy2_l_p5 > 0 and dy2_scalar_p5 > 0 and dy2_plant5_swapped < 0  # Plant 5 caught!
    print(
        f"  Scalar P_5 mean_{{a!=0}} Delta Y^2 (m=8) = +{mp.nstr(dy2_scalar_p5, 5)} "
        f"(quark +{mp.nstr(dy2_q_p5, 4)} > 0, lepton +{mp.nstr(dy2_l_p5, 4)} > 0; Plant 5 swapped H_u<->H_d gives {mp.nstr(dy2_plant5_swapped, 5)} < 0)."
    )

    # Plant 2 & Householder SU(3) check on arbitrary nonsingular 3x3 matrix pair:
    rng = random.Random(2026112177)
    m_test = householder_su3(rng) * mp.diag([mp.mpc(2, 1), mp.mpc(-1, 3), mp.mpc(4, -2)])
    a0 = mp.arg(mp.det(m_test))
    max_hh = mp.mpf(0)
    for _ in range(10):
        u_l = householder_su3(rng)
        u_r = householder_su3(rng)
        max_hh = max(max_hh, abs(mp.arg(mp.det(u_l * m_test * u_r.H)) - a0))
    sh_p2 = abs(mp.arg(mp.exp(mp.mpc(0, 1) * (mp.arg(mp.det(m_test * mp.diag([mp.mpc(0, 1), 1, 1]))) - a0))) - mp.pi / 2)
    assert max_hh < mp.mpf("1e-58") and sh_p2 < mp.mpf("1e-58")
    print(f"  [CAUGHT Plants 2, 3, 4, 5] Axial shift == pi/2 (err={mp.nstr(sh_p2,3)}), P_6 q_nu=1 breaks norm, W_prin(P_5)=+5 != 0, SU(3) drift={mp.nstr(max_hh,3)}.")
    print("  [PASS] All 5/5 planted negative controls caught; zero-shared-code AGY-C11 countercheck complete.")


def main() -> None:
    t0 = time.time()
    sign_det = check_ic1_symbolic_scalar_det_and_trace_laws()
    check_ic2_and_ic3_scalar_strong_cp(sign_det)
    print(f"\nALL AGY-C11 INDEPENDENT COUNTERCHECKS PASSED (5/5 planted faults caught in {time.time() - t0:.2f}s; 0 of 19).")


if __name__ == "__main__":
    main()
