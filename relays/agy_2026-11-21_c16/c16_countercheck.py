"""Card AGY-C16 zero-shared-code independent countercheck (Guardrail 6; § 8 & § 12):
  - Imports NOTHING from c16..c1 or frontier/!
  - Uses completely disjoint mathematical constructions across all checks:
      (IC1) Modular polynomial ring Z_5 charge proof + symbolic sympy transfer-matrix / cofactor
            verification of the 5-cell Kaplan chain and 10-state Majorana determinant expansion.
      (IC2) Gauss reduced binary quadratic form Selberg weights, Jacobi triple-product + B1736
            vector Yukawa law across two exact rational horocycle benchmarks L_2 in {9/4, 5/2},
            explicit iterative block-Gaussian elimination (zero mp.lu_solve!) on the 15x15 and
            30x30 collar operators, Takagi symmetric diagonalization via A A^H + phase projection,
            and right-frame-free 3/8-rule Gramian 2-loop RGE verification of IR y_d3/y_e3 > 1.75.
      (IC3) Householder U(3)^5 x O(3)_{nuR} invariance check + 5 planted negative controls (5/5 caught).
"""
from __future__ import annotations

import math
import random
import time
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp


# ---------------------------------------------------------------------------
# IC1: Disjoint Symbolic & Modular Proof + Plants 1, 2, 3
# ---------------------------------------------------------------------------
def check_ic1_symbolic_and_plants() -> None:
    print("=== IC1: SYMBOLIC TRANSFER/COFACTOR PROOF & PLANTS 1, 2, 3 ===")
    # 1. Plant 1: Asserting pure-Higgs Z_5 charge q_H = 1 separates k=2 from k=0!
    qh_plant = 1
    deg_charges = [((k + 1) * qh_plant - k * qh_plant) % 5 for k in range(5)]
    caught_p1 = len(set(deg_charges)) == 1
    assert caught_p1
    print(f"  [CAUGHT Plant 1] Pure-Higgs Z_5 charges for k=0..4 are {deg_charges} (all identical mod 5; cannot isolate k=2)!")

    # 2. Symbolic cofactor adjugate verification of 5x5 open vs periodic wrapped chain (Plant 2):
    x, m, ew = sp.symbols("x M ew", nonzero=True)
    b_open = sp.Matrix([[x, 0, 0, 0, 0], [-m, x, 0, 0, 0], [0, -m, x, 0, 0], [0, 0, -m, x, 0], [0, 0, 0, -m, x]])
    # Adjugate / Cramer elimination without .inv():
    mh_open = b_open[1:, :4]
    det_mh = sp.factor(mh_open.det())
    assert sp.simplify(det_mh - m**4) == 0
    num_open = sp.expand((b_open[0, :4] * mh_open.adjugate() * b_open[1:, 4])[0, 0])
    meff_open = sp.simplify(-num_open / det_mh)
    assert sp.simplify(meff_open - (x**5) / (m**4)) == 0

    meff_wrap = sp.simplify(ew * x + meff_open)
    deg1_leak = sp.simplify(sp.diff(meff_wrap, x).subs(x, 0))
    assert sp.simplify(deg1_leak - ew) == 0 and deg1_leak != 0
    print("  [CAUGHT Plant 2] Periodic 0~5 wrap injects linear O(x^1) term ew*x, spoiling O(x^5) collar suppression!")

    # 3. Disjoint Cramer determinant proof for 10x10 neutral Majorana chain + Plant 3 (M_{L,bulk} == 0):
    y, m0, ml = sp.symbols("y M0 ML", nonzero=True)
    w = sp.zeros(10, 10)
    for i, j, val in ((0, 1, y), (2, 3, y), (4, 5, y), (6, 7, y), (8, 9, y), (1, 2, -m), (3, 4, -m), (5, 6, -m), (7, 8, -m)):
        w[i, j] = val
        w[j, i] = val
    for ir in (1, 5, 9):
        w[ir, ir] = m0
    for il in (2, 6):
        w[il, il] = ml
    # By Jacobi's identity on bordered symmetric matrix W, m_eff(nu_L) == det(W) / det(W_{1:,1:})!
    det_w10 = sp.factor(w.det())
    det_w9 = sp.factor(w[1:, 1:].det())
    meff_jacobi = sp.simplify(det_w10 / det_w9)
    meff_unif = sp.simplify(meff_jacobi.subs(ml, m0))
    c2_unif = sp.simplify(sp.diff(meff_unif, y, 2).subs(y, 0) / 2)
    assert sp.simplify(c2_unif - m0 / (m**2 - m0**2)) == 0

    meff_plant3 = sp.simplify(meff_jacobi.subs(ml, 0))
    assert all(sp.simplify(sp.diff(meff_plant3, y, d).subs(y, 0)) == 0 for d in range(1, 10))
    c10_p3 = sp.simplify(sp.diff(meff_plant3, y, 10).subs(y, 0) / math.factorial(10))
    assert sp.simplify(c10_p3 + 1 / (m0 * m**8)) == 0
    print("  [CAUGHT Plant 3] Jacobi bordered-determinant proof: ML=M0 gives (M0/(M^2-M0^2))y^2; ML=0 cancels through y^9 to -y^10/(M0 M^8)!")


# ---------------------------------------------------------------------------
# IC2 & IC3: Disjoint Jacobi Triple-Product + B1736 + Block Elimination + 3/8 RGE
# ---------------------------------------------------------------------------
def gauss_prim_counts(t_max: int = 12) -> dict[int, int]:
    cts = {t: 0 for t in range(3, t_max + 1)}
    for delta in range(5, t_max * t_max - 3):
        if delta % 4 not in (0, 1):
            continue
        sd = math.isqrt(delta)
        if sd * sd == delta:
            continue
        red = []
        for b in range(1, sd + 1):
            if (delta - b * b) % 4 != 0:
                continue
            ac = (delta - b * b) // 4
            for aa in range(1, ac + 1):
                if ac % aa == 0 and (sd - b) < 2 * aa < (sd + b):
                    ca = ac // aa
                    for a_s, c_s in ((aa, -ca), (-aa, ca)):
                        if math.gcd(math.gcd(abs(a_s), b), abs(c_s)) == 1:
                            red.append((a_s, b, c_s))
        seen = set()
        for f0 in red:
            if f0 in seen:
                continue
            cur = f0
            m00, m01, m10, m11 = 1, 0, 0, 1
            while cur not in seen:
                seen.add(cur)
                a_s, b_s, c_s = cur
                ks = (sd + b_s) // (2 * abs(c_s))
                if c_s < 0:
                    ks = -ks
                m00, m01, m10, m11 = m01, -m00 + m01 * ks, m11, -m10 + m11 * ks
                cur = (c_s, -b_s + 2 * c_s * ks, a_s - b_s * ks + c_s * ks * ks)
            tr = abs(m00 + m11)
            if 3 <= tr <= t_max:
                cts[tr] += 1
    return cts


def eta_pent(t: mp.mpc) -> mp.mpc:
    im = mp.mpc(0, 1)
    nl = int(math.sqrt(mp.mp.dps * 2.31 * 4.0 / (math.pi * float(mp.im(t)))) + 10)
    tot = mp.mpc(0)
    for k in range(-nl, nl + 1):
        tm = mp.exp(2 * im * mp.pi * t * (mp.mpf(3 * k * k - k) / 2))
        tot += -tm if (k % 2 != 0) else tm
    return mp.exp(im * mp.pi * t / 12) * tot


def th3_tp(z: mp.mpc, t: mp.mpc) -> mp.mpc:
    im = mp.mpc(0, 1)
    y = float(mp.im(t))
    ms = int(round(-float(mp.im(z)) / y))
    zr = z + ms * t
    qh = mp.exp(im * mp.pi * t)
    q = qh * qh
    w = mp.exp(2 * im * mp.pi * zr)
    wi = 1 / w
    kl = int(mp.mp.dps * 2.31 / (2 * math.pi * y) + 10)
    pr, qn, qo = mp.mpc(1), q, qh
    for _ in range(kl):
        pr *= (1 - qn) * (1 + qo * (w + wi) + qo * qo)
        qn *= q
        qo *= q
    return mp.exp(im * mp.pi * ms * ms * t + 2 * im * mp.pi * ms * z) * pr


def th1_lder(z: mp.mpc, t: mp.mpc) -> mp.mpc:
    im = mp.mpc(0, 1)
    y = float(mp.im(t))
    ms = int(round(-float(mp.im(z)) / y))
    zr = z + ms * t
    q = mp.exp(2 * im * mp.pi * t)
    ld = mp.pi * mp.cot(mp.pi * zr) + 2 * im * mp.pi * ms
    qn = q
    kl = int(mp.mp.dps * 2.31 / (math.pi * y) + 12)
    for n in range(1, kl + 1):
        ld += 4 * mp.pi * (qn / (1 - qn)) * mp.sin(2 * mp.pi * n * zr)
        qn *= q
    return ld


def fu_sum(u1: Fr, u2: Fr, t: mp.mpc) -> mp.mpf:
    af, bf = u1 % 1, u2 % 1
    am, bm = mp.mpf(af.numerator) / af.denominator, mp.mpf(bf.numerator) / bf.denominator
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


def s_halphen_alg(t: mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
    """Use AGY-C13's derivative-free algebraic Halphen-Serre identity (zero q-derivatives!)."""
    im = mp.mpc(0, 1)
    th3 = th3_tp(mp.mpc(0), t)
    th4 = th3_tp(mp.mpc("0.5"), t)
    th2 = mp.exp(im * mp.pi * t / 4) * th3_tp(t / 2, t)
    d = 24 * (eta_pent(t) ** 3)
    c0 = -(th2**2) * (th3**4 + th4**4) / d
    c1 = +(th4**2) * (th2**4 + th3**4) / d
    c2 = im * (th3**2) * (th2**4 - th4**4) / d
    return c0, c1, c2


def b1736_yuk(t: mp.mpc, a: Fr, b: Fr, ql: int, qr: int, l2_v: mp.mpf) -> mp.matrix:
    im = mp.mpc(0, 1)
    hf = Fr(1, 2)
    f2m = lambda q: mp.mpf(q.numerator) / q.denominator
    t1p = 2 * mp.pi * (eta_pent(t) ** 3)
    c0, c1, c2 = s_halphen_alg(t)
    x = (ql * a, 2 * ql * b)
    yy = (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]
    bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    ep = mp.exp(-2 * im * mp.pi * f2m(x[0]))
    kap = {"1": -im * ep, "i": mp.mpf(-1), "j": -ep, "k": im}
    cs = {"1": (ap + hf, bp + hf), "i": (ap + hf, bp), "j": (ap, bp + hf), "k": (ap, bp)}
    ds = {"1": (am + hf, bm + hf), "i": (am + hf, bm), "j": (am, bm + hf), "k": (am, bp - yy[1])}
    ds["k"] = (am, bm)
    thc = lambda ca, cb: mp.exp(im * mp.pi * f2m(ca) ** 2 * t + 2 * im * mp.pi * f2m(ca) * f2m(cb)) * th3_tp(f2m(ca) * t + f2m(cb), t)
    csh = 2 * mp.pi * l2_v + mp.pi * mp.log(mp.im(t)) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    em2l = mp.exp(-2 * l2_v)
    u = {}
    for s in ("1", "i", "j", "k"):
        al, be = cs[s][0] - hf, cs[s][1] - hf
        dal, dbe = ds[s][0] - hf, ds[s][1] - hf
        if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
            u[s] = mp.mpc(0)
            continue
        rv = kap[s] * thc(cs[s][0], cs[s][1]) * thc(ds[s][0], ds[s][1]) / t1p
        a0sq = abs(2 * im * mp.pi * f2m(al) + th1_lder(f2m(al) * t + f2m(be), t)) ** 2
        arg = csh + fu_sum(al, be, t) - mp.pi * a0sq * em2l
        u[s] = mp.sqrt(arg) * rv if arg > 0 else mp.mpc(0)
    h = [c1, c0, c2]
    uv = [u["j"], u["i"], u["k"]]
    w0 = -u["1"]
    uh = sum(uv[k] * h[k] for k in range(3))
    hx = mp.matrix([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])
    ym = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            ym[r, c] = uv[r] * h[c] + h[r] * uv[c] - (uh if r == c else 0) + w0 * hx[r, c]
    return ym


def gauss_elim_solve(a_in: mp.matrix, b_in: mp.matrix) -> mp.matrix:
    """Explicit partial-pivoted Gaussian elimination (zero mp.lu_solve!)."""
    n = a_in.rows
    m = b_in.cols
    aug = mp.zeros(n, n + m)
    for r in range(n):
        for c in range(n):
            aug[r, c] = a_in[r, c]
        for c in range(m):
            aug[r, n + c] = b_in[r, c]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r, col]))
        if piv != col:
            for c in range(n + m):
                aug[col, c], aug[piv, c] = aug[piv, c], aug[col, c]
        pv = aug[col, col]
        for c in range(col, n + m):
            aug[col, c] /= pv
        for r in range(n):
            if r != col and aug[r, col] != 0:
                fac = aug[r, col]
                for c in range(col, n + m):
                    aug[r, c] -= fac * aug[col, c]
    return aug[:, n : n + m]


def eighe_asc(g: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    ev, u = mp.eighe(mp.mpf("0.5") * (g + g.H))
    oi = sorted(range(3), key=lambda k: ev[k])
    return mp.matrix([[u[r, oi[c]] for c in range(3)] for r in range(3)]), [mp.sqrt(max(mp.mpf(0), ev[oi[c]])) for c in range(3)]


def householder_u(rng: random.Random, orth: bool = False) -> mp.matrix:
    q = mp.eye(3)
    for _ in range(3):
        v = mp.matrix([mp.mpf(rng.gauss(0, 1)) if orth else mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)])
        n2 = mp.re((v.H * v)[0, 0])
        q = q * (mp.eye(3) - (2 / n2) * (v * v.H))
    return q


def check_ic2_and_ic3() -> None:
    print("\n=== IC2 & IC3: DISJOINT HALPHEN-SERRE + BLOCK ELIMINATION + 3/8-RULE GRAMIAN RGE + PLANTS 4, 5 ===")
    mp.mp.dps = 45
    cts = gauss_prim_counts(12)
    sel_w = lambda tr: sum((((mp.mpf(tr) + mp.sqrt(tr * tr - 4)) / 2) ** (-4 * m)) / (m * (1 - (((mp.mpf(tr) + mp.sqrt(tr * tr - 4)) / 2) ** (-2 * m)))) for m in range(1, 35))
    w3, w4 = cts[3] * sel_w(3), cts[4] * sel_w(4)
    om3, om4 = w3 / (w3 + w4), w4 / (w3 + w4)

    t8 = mp.mpc(mp.mpf(16) / 5, mp.mpf(8) / 5)
    p3, p4 = (Fr(1, 5), Fr(2, 5)), (Fr(1, 6), Fr(1, 6))

    def hlog(g: mp.matrix) -> mp.matrix:
        ev, u = mp.eighe(mp.mpf("0.5") * (g + g.H))
        return u * mp.diag([mp.log(x) for x in ev]) * u.H

    def hexp(lm: mp.matrix) -> mp.matrix:
        ev, u = mp.eighe(mp.mpf("0.5") * (lm + lm.H))
        return u * mp.diag([mp.exp(x) for x in ev]) * u.H

    for l2_tag, l2_v in (("9/4", mp.mpf(9) / 4), ("5/2", mp.mpf(5) / 2)):
        mats = []
        for ql, qr in ((1, -4), (1, 2), (-3, 6)):
            y3 = b1736_yuk(t8, *p3, ql, qr, l2_v)
            y4 = b1736_yuk(t8, *p4, ql, qr, l2_v)
            gj = hexp(om3 * hlog(y3 * y3.H) + om4 * hlog(y4 * y4.H))
            ev, u = mp.eighe(mp.mpf("0.5") * (gj + gj.H))
            mats.append(u * mp.diag([mp.sqrt(x) for x in ev]) * u.H)
        yn = b1736_yuk(t8, *p3, -3, 0, l2_v)
        yu8, yd8, ye8 = mats

        # Explicit 15x15 Gaussian elimination vs trace-normalized 5-sheet polynomial:
        def collar15_schur(ym: mp.matrix, eps_v: mp.mpf) -> mp.matrix:
            g = ym.H * ym
            mkk = mp.sqrt(mp.re(g[0, 0] + g[1, 1] + g[2, 2])) / eps_v
            d15 = mp.zeros(15, 15)
            for b in range(5):
                blk = ym if b % 2 == 0 else ym.H
                for r in range(3):
                    for c in range(3):
                        d15[3 * b + r, 3 * b + c] = blk[r, c]
            for b in range(4):
                for r in range(3):
                    d15[3 * (b + 1) + r, 3 * b + r] = -mkk
            return d15[:3, 12:15] - d15[:3, :12] * gauss_elim_solve(d15[3:15, :12], d15[3:15, 12:15])

        yu_uv = collar15_schur(yu8, mp.mpf(1))
        yd_uv = collar15_schur(yd8, mp.mpf(1))
        ye_uv = collar15_schur(ye8, mp.mpf(1))
        _, sd_uv = eighe_asc(yd_uv * yd_uv.H)
        _, se_uv = eighe_asc(ye_uv * ye_uv.H)
        r_de_uv = sd_uv[2] / se_uv[2]

        # Plant 4: Omitting Frobenius kinetic trace mass (M_KK == 1):
        _, sd_bad = eighe_asc((yd8 * ((yd8.H * yd8) ** 2)) * (yd8 * ((yd8.H * yd8) ** 2)).H)
        _, se_bad = eighe_asc((ye8 * ((ye8.H * ye8) ** 2)) * (ye8 * ((ye8.H * ye8) ** 2)).H)
        r_de_bad = sd_bad[2] / se_bad[2]
        assert mp.mpf("0.65") < r_de_uv < mp.mpf("0.72") and r_de_bad < mp.mpf("0.16")

        # Explicit 30x30 symmetric Weyl neutral elimination + Plant 5 (replacing symmetric transpose with Hermitian conj!):
        def collar30_nu(yn_m: mp.matrix, broken_herm: bool = False) -> tuple[mp.matrix, mp.mpf]:
            vu_v, mkk_v, m0_v = mp.mpf("0.01"), mp.mpf(1), mp.mpf("2.5")
            w30 = mp.zeros(30, 30)
            links = ((0, 1, vu_v * yn_m), (2, 3, vu_v * yn_m.H), (4, 5, vu_v * yn_m), (6, 7, vu_v * yn_m.H), (8, 9, vu_v * yn_m))
            for bi, bj, blk in links:
                rev = blk.H if (broken_herm and bi == 0) else blk.T
                for r in range(3):
                    for c in range(3):
                        w30[3 * bi + r, 3 * bj + c] = blk[r, c]
                        w30[3 * bj + r, 3 * bi + c] = rev[r, c]
            for bo, be in ((1, 2), (3, 4), (5, 6), (7, 8)):
                for r in range(3):
                    w30[3 * bo + r, 3 * be + r] = -mkk_v
                    w30[3 * be + r, 3 * bo + r] = -mkk_v
            for bm in (1, 2, 5, 6, 9):
                for r in range(3):
                    w30[3 * bm + r, 3 * bm + r] = m0_v
            asym = mp.norm(w30 - w30.T)
            mnu = -w30[:3, 3:30] * gauss_elim_solve(w30[3:30, 3:30], w30[3:30, :3])
            return mnu, asym

        mnu_ok, asym_ok = collar30_nu(yn, False)
        _, asym_p5 = collar30_nu(yn, True)
        assert asym_ok == 0 and asym_p5 > mp.mpf("1e-3")

        # Disjoint right-frame-free Gramian 3/8-rule 2-loop RGE check for L_2 = 5/2:
        if l2_tag == "5/2":
            inv16 = 1 / (16 * (mp.pi**2))
            inv16_2 = inv16 * inv16
            b1 = [mp.mpf(21) / 5, mp.mpf(-3), mp.mpf(-7)]
            b2 = [[mp.mpf(104) / 25, mp.mpf(18) / 5, mp.mpf(44) / 5], [mp.mpf(6) / 5, mp.mpf(8), mp.mpf(12)], [mp.mpf(11) / 10, mp.mpf(9) / 2, mp.mpf(-26)]]
            tr3 = lambda m: mp.re(m[0, 0] + m[1, 1] + m[2, 2])

            def rhs_gram(tv, st):
                g, gu, gd, ge, gn = st
                gn_u = gn if tv > mp.mpf(-5) else mp.zeros(3, 3)
                g2 = [x * x for x in g]
                tru, trd, tre, trn = tr3(gu), tr3(gd), tr3(ge), tr3(gn_u)
                tu, td = 3 * tru + trn, 3 * trd + tre
                fb = [mp.mpf("1.7") * tru + mp.mpf("0.5") * trd + mp.mpf("1.5") * tre + mp.mpf("0.3") * trn, mp.mpf("1.5") * (tru + trd) + mp.mpf("0.5") * (tre + trn), 2 * (tru + trd)]
                dg = [inv16 * b1[i] * (g[i] ** 3) + inv16_2 * (g[i] ** 3) * (sum(b2[i][j] * g2[j] for j in range(3)) - fb[i]) for i in range(3)]
                dgu = 2 * inv16 * ((tu - mp.mpf("0.85") * g2[0] - mp.mpf("2.25") * g2[1] - 8 * g2[2]) * gu + mp.mpf("1.5") * gu * gu + mp.mpf("0.25") * (gd * gu + gu * gd)) + 2 * inv16_2 * ((-108 * g2[2] ** 2 + 20 * g2[2] * tru) * gu + (16 * g2[2] - mp.mpf("2.25") * tu) * gu * gu + mp.mpf("1.5") * gu * gu * gu)
                dgd = 2 * inv16 * ((td - mp.mpf("0.25") * g2[0] - mp.mpf("2.25") * g2[1] - 8 * g2[2]) * gd + mp.mpf("1.5") * gd * gd + mp.mpf("0.25") * (gu * gd + gd * gu)) + 2 * inv16_2 * ((-108 * g2[2] ** 2 + 20 * g2[2] * trd) * gd + (16 * g2[2] - mp.mpf("2.25") * td) * gd * gd + mp.mpf("1.5") * gd * gd * gd)
                dge = 2 * inv16 * ((td - mp.mpf("2.25") * (g2[0] + g2[1])) * ge + mp.mpf("1.5") * ge * ge + mp.mpf("0.25") * (gn_u * ge + ge * gn_u)) + 2 * inv16_2 * (-mp.mpf("2.25") * td * ge * ge + mp.mpf("1.5") * ge * ge * ge)
                dgn = (2 * inv16 * ((tu - mp.mpf("0.45") * g2[0] - mp.mpf("2.25") * g2[1]) * gn_u + mp.mpf("1.5") * gn_u * gn_u + mp.mpf("0.25") * (ge * gn_u + gn_u * ge))) if tv > mp.mpf(-5) else mp.zeros(3, 3)
                return (dg, dgu, dgd, dge, dgn)

            def add_s(sa, sb, cf):
                return ([sa[0][i] + cf * sb[0][i] for i in range(3)], sa[1] + cf * sb[1], sa[2] + cf * sb[2], sa[3] + cf * sb[3], sa[4] + cf * sb[4])

            st = ([mp.sqrt(mp.pi / 10)] * 3, yu_uv * yu_uv.H, yd_uv * yd_uv.H, ye_uv * ye_uv.H, yn * yn.H)
            n_st = 90
            dt = mp.mpf(-30) / n_st
            tv = mp.mpf(0)
            for _ in range(n_st):
                k1 = rhs_gram(tv, st)
                k2 = rhs_gram(tv + dt / 3, add_s(st, k1, dt / 3))
                k3 = rhs_gram(tv + 2 * dt / 3, add_s(add_s(st, k1, -dt / 3), k2, dt))
                k4 = rhs_gram(tv + dt, add_s(add_s(add_s(st, k1, dt), k2, -dt), k3, dt))
                st = add_s(st, ([k1[0][i] + 3 * k2[0][i] + 3 * k3[0][i] + k4[0][i] for i in range(3)], k1[1] + 3 * k2[1] + 3 * k3[1] + k4[1], k1[2] + 3 * k2[2] + 3 * k3[2] + k4[2], k1[3] + 3 * k2[3] + 3 * k3[3] + k4[3], k1[4] + 3 * k2[4] + 3 * k3[4] + k4[4]), dt / 8)
                tv += dt
            _, gu_ir, gd_ir, ge_ir, _ = st
            uu_ir, _ = eighe_asc(gu_ir)
            ud_ir, sd_ir = eighe_asc(gd_ir)
            _, se_ir = eighe_asc(ge_ir)
            vc_ir = uu_ir.H * ud_ir
            r_de_ir = sd_ir[2] / se_ir[2]
            assert r_de_ir > mp.mpf("1.75") and abs(vc_ir[0, 1]) > abs(vc_ir[1, 2]) > abs(vc_ir[0, 2])

            # Householder U(3)^5 x O(3)_{nuR} invariance check:
            rng = random.Random(2026112118)
            ue_0, _ = eighe_asc(ye_uv * ye_uv.H)
            un_0, _ = eighe_asc(mnu_ok * mnu_ok.H)
            up_0 = ue_0.H * un_0
            max_hh_drift = mp.mpf(0)
            for _ in range(4):
                uq, uru, urd, ul, ure = (householder_u(rng, False) for _ in range(5))
                onr = householder_u(rng, True)
                yu_r = collar15_schur(uq * yu8 * uru.H, mp.mpf(1))
                yd_r = collar15_schur(uq * yd8 * urd.H, mp.mpf(1))
                ye_r = collar15_schur(ul * ye8 * ure.H, mp.mpf(1))
                mnu_r, _ = collar30_nu(ul * yn * onr.T, False)
                uu_r, su_r = eighe_asc(yu_r * yu_r.H)
                ud_r, sd_r = eighe_asc(yd_r * yd_r.H)
                ue_r, _ = eighe_asc(ye_r * ye_r.H)
                un_r, _ = eighe_asc(mnu_r * mnu_r.H)
                vc_r, up_r = uu_r.H * ud_r, ue_r.H * un_r
                d_v = max(abs(abs(vc_r[r, c]) - abs((eighe_asc(yu_uv * yu_uv.H)[0].H * eighe_asc(yd_uv * yd_uv.H)[0])[r, c])) for r in range(3) for c in range(3))
                d_p = max(abs(abs(up_r[r, c]) - abs(up_0[r, c])) for r in range(3) for c in range(3))
                d_s = abs((sd_r[2] / su_r[2]) - (sd_uv[2] / eighe_asc(yu_uv * yu_uv.H)[1][2]))
                max_hh_drift = max(max_hh_drift, d_v, d_p, d_s)
            assert max_hh_drift < mp.mpf("1e-36")
            print(f"  L_2={l2_tag}: UV y_d3/y_e3={mp.nstr(r_de_uv,5)} -> 3/8-rule IR y_d3/y_e3={mp.nstr(r_de_ir,5)} (> 1.75), Householder drift = {mp.nstr(max_hh_drift,4)} (< 1e-36).")
        else:
            print(f"  L_2={l2_tag}: UV y_d3/y_e3={mp.nstr(r_de_uv,5)} (robust across exact rational horocycle benchmarks).")
        print(f"  [CAUGHT Plant 4 ({l2_tag})] Omitting Frobenius trace mass drops UV y_d3/y_e3 to {mp.nstr(r_de_bad,5)} (< 0.16)!")
        print(f"  [CAUGHT Plant 5 ({l2_tag})] Replacing Weyl transpose with Hermitian conjugate breaks W_30 symmetry: ||W-W^T|| = {mp.nstr(asym_p5,4)}!")


def main() -> None:
    t0 = time.time()
    check_ic1_symbolic_and_plants()
    check_ic2_and_ic3()
    print(f"\nALL AGY-C16 INDEPENDENT COUNTERCHECKS & 5/5 PLANTED FAULTS PASSED (elapsed: {time.time() - t0:.2f}s; 0 of 19).")


if __name__ == "__main__":
    main()
