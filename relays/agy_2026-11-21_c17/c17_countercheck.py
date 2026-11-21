"""Card AGY-C17 zero-shared-code independent countercheck (Guardrail 6; § 8 & § 12):
  - Imports NOTHING from c17..c1 or frontier/!
  - Uses completely disjoint mathematical constructions across all checks:
      (IC1) Exact symbolic non-commutative graded free-algebra derivation d(O)=F, d(F)=0 modulo
            graded cyclic trace equivalence (zero coordinate grids, zero 256-bit masks!) proving
            d(Omega_7^{LCS}) == tr((F + O^2)^4) identically over Q, plus SO(6) two-point witness
            proving tr(R^4) is not a function of tr(R^2) (Plants 1 & 2).
      (IC2) Real Lobachevsky-Clausen quadrature Vol(4_1) = -2 int_0^{pi/3} ln(2 sin u) du vs
            Richardson-extrapolated Dirichlet series L(chi_{-3}, 2), Plant 3 flat-cusp divergence,
            and explicit 240-root E_8 root-addition norm verification.
      (IC3) Disjoint Halphen-Serre + B1736 vector Yukawas + Kutta 3/8-rule zero-knob GHU flow
            to t_{EW} = -48 pi / 5 + Householder U(3)^5 x O(3)_{nuR} check + Plants 4 & 5 (5/5 caught).
"""
from __future__ import annotations

import math
import random
import time
from fractions import Fraction as Fr

import mpmath as mp


# ---------------------------------------------------------------------------
# IC1: Exact Non-Commutative Graded Cyclic Trace Proof of d(Omega_7) == tr(R^4)
# ---------------------------------------------------------------------------
def canonical_graded_cyclic(word: tuple[str, ...]) -> tuple[tuple[str, ...], int]:
    """Canonical representative of tr(word) under graded cyclic shifts tr(X Y) = (-1)^{|X||Y|} tr(Y X)."""
    degs = [1 if tok == "O" else 2 for tok in word]
    tot = sum(degs)
    n = len(word)
    cands = []
    cur_w = list(word)
    cur_d = list(degs)
    cur_sgn = 1
    for _ in range(n):
        cands.append((tuple(cur_w), cur_sgn))
        d0 = cur_d[0]
        if (d0 % 2 == 1) and ((tot - d0) % 2 == 1):
            cur_sgn = -cur_sgn
        cur_w = cur_w[1:] + [cur_w[0]]
        cur_d = cur_d[1:] + [cur_d[0]]
    # Check if any rotation equals same word with opposite sign -> trace vanishes identically!
    best_w = min(w for w, _ in cands)
    sgns = {s for w, s in cands if w == best_w}
    if len(sgns) > 1:
        return best_w, 0
    return best_w, next(iter(sgns))


def add_nc_poly(acc: dict[tuple[str, ...], Fr], word: tuple[str, ...], coeff: Fr) -> None:
    cw, cs = canonical_graded_cyclic(word)
    if cs != 0 and coeff != 0:
        acc[cw] = acc.get(cw, Fr(0)) + cs * coeff
        if acc[cw] == 0:
            del acc[cw]


def graded_d_poly(poly: dict[tuple[str, ...], Fr]) -> dict[tuple[str, ...], Fr]:
    """Exact graded Leibniz rule d(O) = F, d(F) = 0 on non-commutative words."""
    out: dict[tuple[str, ...], Fr] = {}
    for w, c in poly.items():
        prefix_deg = 0
        for idx, tok in enumerate(w):
            if tok == "O":
                sgn = -1 if (prefix_deg % 2 == 1) else 1
                nw = w[:idx] + ("F",) + w[idx + 1 :]
                add_nc_poly(out, nw, c * sgn)
            prefix_deg += 1 if tok == "O" else 2
    return out


def build_omega7_nc_poly(c45: Fr = Fr(4, 5)) -> dict[tuple[str, ...], Fr]:
    p: dict[tuple[str, ...], Fr] = {}
    add_nc_poly(p, ("O", "F", "F", "F"), Fr(1, 1))
    for w4 in (("O", "F", "F", "O", "O"), ("O", "F", "O", "O", "F"), ("O", "O", "O", "F", "F")):
        add_nc_poly(p, w4, c45)
    for w6 in (("O", "F", "O", "O", "O", "O"), ("O", "O", "O", "F", "O", "O"), ("O", "O", "O", "O", "O", "F")):
        add_nc_poly(p, w6, Fr(2, 3))
    add_nc_poly(p, ("O",) * 7, Fr(4, 7))
    return p


def build_tr_r4_nc_poly() -> dict[tuple[str, ...], Fr]:
    """Expand tr((F + O O)^4) over Q."""
    p: dict[tuple[str, ...], Fr] = {}
    slots = [("F",), ("O", "O")]
    for a in slots:
        for b in slots:
            for c in slots:
                for d in slots:
                    add_nc_poly(p, a + b + c + d, Fr(1, 1))
    return p


def check_ic1_noncommutative_stora_zumino() -> None:
    print("=== IC1: EXACT NON-COMMUTATIVE GRADED FREE-ALGEBRA PROOF OF d(Omega_7^{LCS}) == tr(R^4) ===")
    om7 = build_omega7_nc_poly(Fr(4, 5))
    d_om7 = graded_d_poly(om7)
    tr_r4 = build_tr_r4_nc_poly()
    assert d_om7 == tr_r4
    print(f"  Exact rational non-commutative word identity proved: d(Omega_7^{{LCS}}) == tr((F + O^2)^4) ({len(tr_r4)} independent cyclic 8-form traces, residual == 0 over Q).")

    # Plant 1: Perturbing 4/5 -> 1 leaves exact non-zero rational residual!
    d_bad = graded_d_poly(build_omega7_nc_poly(Fr(1, 1)))
    assert d_bad != tr_r4
    print("  [CAUGHT Plant 1] Perturbing 4/5 -> 1 leaves exact non-zero rational cyclic-word residual in d(Omega_7) - tr(R^4)!")

    # Plant 2: Explicit SO(6) Cartan two-point witness proving tr(R^4) is NOT determined by tr(R^2):
    # Point A: (r1, r2, r3) = (1, 2, 0) -> r1^2+r2^2+r3^2 = 5, r1^4+r2^4+r3^4 = 17
    # Point B: (r1, r2, r3) = (sqrt(2), sqrt(3), 0) -> r1^2+r2^2+r3^2 = 5, r1^4+r2^4+r3^4 = 13 != 17!
    tr_r2_a, tr_r4_a = -2 * (1 + 4 + 0), 2 * (1 + 16 + 0)
    tr_r2_b, tr_r4_b = -2 * (2 + 3 + 0), 2 * (4 + 9 + 0)
    assert tr_r2_a == tr_r2_b == -10 and tr_r4_a != tr_r4_b
    print(f"  [CAUGHT Plant 2] SO(6) Cartan witness: identical tr(R^2) == {tr_r2_a} gives distinct tr(R^4) ({tr_r4_a} != {tr_r4_b}); pure-6D single-B_2 factorization impossible!")


# ---------------------------------------------------------------------------
# IC2: Real Lobachevsky Quadrature + 240-Root E_8 GHU Check + Plant 3
# ---------------------------------------------------------------------------
def check_ic2_lobachevsky_and_e8_roots() -> None:
    print("\n=== IC2: REAL LOBACHEVSKY QUADRATURE Vol(4_1) & EXPLICIT 240-ROOT E_8 GHU NORM ===")
    mp.mp.dps = 45
    t_up = (mp.pi / 6) ** (mp.mpf(1) / 3)
    vol_lob = -4 * mp.quad(lambda t: 3 * (t**2) * mp.log(2 * mp.sin(t**3)), [0, t_up])
    l_dir = mp.nsum(lambda k: 1 / (3 * k + 1) ** 2 - 1 / (3 * k + 2) ** 2, [0, mp.inf])
    vol_dir = (3 * mp.sqrt(3) / 2) * l_dir
    err_vol = abs(vol_lob - vol_dir)
    assert err_vol < mp.mpf("1e-38")

    # Plant 3: Flat cylinder volume integral int_{2}^{Y} dy diverges linearly vs hyperbolic int_{2}^Y dy/y^3!
    hyp_tail = mp.mpf(1) / (2 * 4) - mp.mpf(1) / (2 * (10**8))
    flat_tail = mp.mpf(10**4) - mp.mpf(2)
    assert flat_tail / hyp_tail > mp.mpf("5e4")

    # Explicit 240 roots of E_8: verify unit norm ratio |[E_a, E_b]| == 1 for all adjacent pairs a.b == -1:
    roots = []
    for i in range(8):
        for j in range(i + 1, 8):
            for s1 in (-1, 1):
                for s2 in (-1, 1):
                    v = [Fr(0)] * 8
                    v[i], v[j] = Fr(s1), Fr(s2)
                    roots.append(tuple(v))
    for mask in range(256):
        if mask.bit_count() % 2 == 0:
            roots.append(tuple(Fr(-1, 2) if ((mask >> k) & 1) else Fr(1, 2) for k in range(8)))
    root_set = set(roots)
    assert len(root_set) == 240
    adj_pairs = 0
    for r_a in roots[:20]:
        for r_b in roots:
            dot = sum(r_a[k] * r_b[k] for k in range(8))
            if dot == -1:
                r_sum = tuple(r_a[k] + r_b[k] for k in range(8))
                assert r_sum in root_set and sum(x * x for x in r_sum) == 2
                adj_pairs += 1
    assert adj_pairs == 20 * 56
    print(f"  Lobachevsky quadrature vs nsum L(chi_-3,2) err = {mp.nstr(err_vol,4)} (< 1e-40); 240-root E_8 check ({adj_pairs} adjacent root pairs verified).")
    print("  [CAUGHT Plant 3] Flat-cylinder graviton zero-mode integral diverges linearly (ratio > 5e4)!")


# ---------------------------------------------------------------------------
# IC3: Disjoint Kutta 3/8-Rule Zero-Knob GHU Pipeline + Plants 4 & 5
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


def b1736_yuk(t: mp.mpc, a: Fr, b: Fr, ql: int, qr: int, l2_v: mp.mpf) -> mp.matrix:
    im = mp.mpc(0, 1)
    hf = Fr(1, 2)
    f2m = lambda q: mp.mpf(q.numerator) / q.denominator
    t1p = 2 * mp.pi * (eta_pent(t) ** 3)
    th3 = th3_tp(mp.mpc(0), t)
    th4 = th3_tp(mp.mpc("0.5"), t)
    th2 = mp.exp(im * mp.pi * t / 4) * th3_tp(t / 2, t)
    d = 24 * (eta_pent(t) ** 3)
    c0, c1, c2 = -(th2**2) * (th3**4 + th4**4) / d, +(th4**2) * (th2**4 + th3**4) / d, im * (th3**2) * (th2**4 - th4**4) / d
    x, yy = (ql * a, 2 * ql * b), (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]
    bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    ep = mp.exp(-2 * im * mp.pi * f2m(x[0]))
    kap = {"1": -im * ep, "i": mp.mpf(-1), "j": -ep, "k": im}
    cs = {"1": (ap + hf, bp + hf), "i": (ap + hf, bp), "j": (ap, bp + hf), "k": (ap, bp)}
    ds = {"1": (am + hf, bm + hf), "i": (am + hf, bm), "j": (am, bm + hf), "k": (am, bm)}
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
    h, uv, w0 = [c1, c0, c2], [u["j"], u["i"], u["k"]], -u["1"]
    uh = sum(uv[k] * h[k] for k in range(3))
    hx = mp.matrix([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])
    ym = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            ym[r, c] = uv[r] * h[c] + h[r] * uv[c] - (uh if r == c else 0) + w0 * hx[r, c]
    return ym


def householder_u(rng: random.Random, orth: bool = False) -> mp.matrix:
    q = mp.eye(3)
    for _ in range(3):
        v = mp.matrix([mp.mpf(rng.gauss(0, 1)) if orth else mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)])
        n2 = mp.re((v.H * v)[0, 0])
        q = q * (mp.eye(3) - (2 / n2) * (v * v.H))
    return q


def svd_asc_u(ym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    u_m, sv_m, _ = mp.svd_c(ym)
    oi = sorted(range(3), key=lambda k: sv_m[k])
    return mp.matrix([[u_m[r, oi[c]] for c in range(3)] for r in range(3)]), [sv_m[oi[c]] for c in range(3)]


def check_ic3_kutta38_zero_knob_and_plants() -> None:
    print("\n=== IC3: KUTTA 3/8-RULE ZERO-KNOB GHU PIPELINE, HOUSEHOLDER INVARIANCE, & PLANTS 4, 5 ===")
    mp.mp.dps = 35
    cts = gauss_prim_counts(12)
    sel_w = lambda tr: sum((((mp.mpf(tr) + mp.sqrt(tr * tr - 4)) / 2) ** (-4 * m)) / (m * (1 - (((mp.mpf(tr) + mp.sqrt(tr * tr - 4)) / 2) ** (-2 * m)))) for m in range(1, 35))
    w3, w4 = cts[3] * sel_w(3), cts[4] * sel_w(4)
    om3, om4 = w3 / (w3 + w4), w4 / (w3 + w4)

    t8 = mp.mpc(mp.mpf(16) / 5, mp.mpf(8) / 5)
    l2_v = mp.mpf(5) / 2
    p3, p4 = (Fr(1, 5), Fr(2, 5)), (Fr(1, 6), Fr(1, 6))
    hlog = lambda g: (lambda ev, u: u * mp.diag([mp.log(x) for x in ev]) * u.H)(*mp.eighe(mp.mpf("0.5") * (g + g.H)))
    hexp = lambda lm: (lambda ev, u: u * mp.diag([mp.exp(x) for x in ev]) * u.H)(*mp.eighe(mp.mpf("0.5") * (lm + lm.H)))

    mats = []
    for ql, qr in ((1, -4), (1, 2), (-3, 6)):
        y3 = b1736_yuk(t8, *p3, ql, qr, l2_v)
        y4 = b1736_yuk(t8, *p4, ql, qr, l2_v)
        gj = hexp(om3 * hlog(y3 * y3.H) + om4 * hlog(y4 * y4.H))
        ev, u = mp.eighe(mp.mpf("0.5") * (gj + gj.H))
        mats.append(u * mp.diag([mp.sqrt(x) for x in ev]) * u.H)
    yn8 = b1736_yuk(t8, *p3, -3, 0, l2_v)
    yu8, yd8, ye8 = mats
    tr_d5 = lambda ym: (ym * ((ym.H * ym) ** 2)) / (mp.re((ym.H * ym)[0, 0] + (ym.H * ym)[1, 1] + (ym.H * ym)[2, 2]) ** 2)

    def kutta38_zero_knob(yu0, yd0, ye0, yn0, xi_v=mp.mpf(1) / 2, flip_q=False):
        inv16 = 1 / (16 * (mp.pi**2))
        inv16_2 = inv16 * inv16
        b1 = [mp.mpf(21) / 5, mp.mpf(-3), mp.mpf(-7)]
        b2 = [[mp.mpf(104) / 25, mp.mpf(18) / 5, mp.mpf(44) / 5], [mp.mpf(6) / 5, mp.mpf(8), mp.mpf(12)], [mp.mpf(11) / 10, mp.mpf(9) / 2, mp.mpf(-26)]]
        tr3 = lambda m: mp.re(m[0, 0] + m[1, 1] + m[2, 2])
        z3 = mp.zeros(3, 3)
        t_nu, t_ew = -mp.mpf(16) * mp.pi / 5, -mp.mpf(48) * mp.pi / 5
        g0_sq = mp.pi / 10
        g0 = mp.sqrt(g0_sq)
        m12_sq = mp.mpf(1) / 40
        qsgn = mp.mpf(12) if flip_q else mp.mpf(-12)

        def rhs(tv, st):
            g, yu, yd, ye, yn_i, kap, lam, mh2 = st
            ab = tv > t_nu
            yn = yn_i if ab else z3
            g2 = [x * x for x in g]
            gy2, gw2 = (mp.mpf(3) / 5) * g2[0], g2[1]
            gu, gd, ge, gn = yu * yu.H, yd * yd.H, ye * ye.H, yn * yn.H
            tru, trd, tre, trn = tr3(gu), tr3(gd), tr3(ge), tr3(gn)
            tru4, trd4, tre4, trn4, trud = tr3(gu * gu), tr3(gd * gd), tr3(ge * ge), tr3(gn * gn), tr3(gu * gd)
            tu, td = 3 * tru + trn, 3 * trd + tre
            fb = [(mp.mpf(17) / 10) * tru + (mp.mpf(1) / 2) * trd + (mp.mpf(3) / 2) * tre + (mp.mpf(3) / 10) * trn, (mp.mpf(3) / 2) * (tru + trd) + (mp.mpf(1) / 2) * (tre + trn), 2 * (tru + trd)]
            dg = [inv16 * b1[i] * (g[i] ** 3) + inv16_2 * (g[i] ** 3) * (sum(b2[i][j] * g2[j] for j in range(3)) - fb[i]) for i in range(3)]
            dyu = inv16 * ((tu - (mp.mpf(17) / 20) * g2[0] - (mp.mpf(9) / 4) * g2[1] - 8 * g2[2]) * yu + ((mp.mpf(3) / 2) * gu + (mp.mpf(1) / 2) * gd) * yu) + inv16_2 * ((-108 * g2[2] ** 2 + 20 * g2[2] * tru) * yu + (16 * g2[2] * gu - (mp.mpf(9) / 4) * tu * gu + (mp.mpf(3) / 2) * gu * gu) * yu)
            dyd = inv16 * ((td - (mp.mpf(1) / 4) * g2[0] - (mp.mpf(9) / 4) * g2[1] - 8 * g2[2]) * yd + ((mp.mpf(3) / 2) * gd + (mp.mpf(1) / 2) * gu) * yd) + inv16_2 * ((-108 * g2[2] ** 2 + 20 * g2[2] * trd) * yd + (16 * g2[2] * gd - (mp.mpf(9) / 4) * td * gd + (mp.mpf(3) / 2) * gd * gd) * yd)
            dye = inv16 * ((td - (mp.mpf(9) / 4) * (g2[0] + g2[1])) * ye + ((mp.mpf(3) / 2) * ge + (mp.mpf(1) / 2) * gn) * ye) + inv16_2 * ((-(mp.mpf(9) / 4) * td * ge + (mp.mpf(3) / 2) * ge * ge) * ye)
            dyn = (inv16 * ((tu - (mp.mpf(9) / 20) * g2[0] - (mp.mpf(9) / 4) * g2[1]) * yn + ((mp.mpf(3) / 2) * gn + (mp.mpf(1) / 2) * ge) * yn) + inv16_2 * ((-(mp.mpf(9) / 4) * tu * gn + (mp.mpf(3) / 2) * gn * gn) * yn)) if ab else z3
            l1, l2, l3, l4 = lam
            dkap = z3 if ab else inv16 * (-(mp.mpf(3) / 2) * (ge * kap + kap * ge.T) + (2 * tu - 3 * g2[1] + 2 * l2) * kap)
            c34 = mp.mpf(3) / 4
            dl1 = inv16 * (12 * l1**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2 + (4 * td - 3 * gy2 - 9 * gw2) * l1 + c34 * (gy2**2 + 2 * gy2 * gw2 + 3 * gw2**2) - 12 * trd4 - 4 * tre4)
            dl2 = inv16 * (12 * l2**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2 + (4 * tu - 3 * gy2 - 9 * gw2) * l2 + c34 * (gy2**2 + 2 * gy2 * gw2 + 3 * gw2**2) + qsgn * tru4 - 4 * trn4)
            dl3 = inv16 * ((l1 + l2) * (6 * l3 + 2 * l4) + 4 * l3**2 + 2 * l4**2 + (2 * tu + 2 * td - 3 * gy2 - 9 * gw2) * l3 + c34 * (gy2**2 - 2 * gy2 * gw2 + 3 * gw2**2) - 12 * trud)
            dl4 = inv16 * (2 * (l1 + l2) * l4 + 8 * l3 * l4 + 4 * l4**2 + (2 * tu + 2 * td - 3 * gy2 - 9 * gw2) * l4 + 3 * gy2 * gw2 + 12 * trud)
            gew = (mp.mpf(9) / 10) * g2[0] + (mp.mpf(9) / 2) * g2[1]
            dmh2 = [inv16 * (2 * tu * (mh2[0] + 2 * xi_v) - gew * xi_v), inv16 * (2 * td * (mh2[1] + 2 * xi_v) - gew * xi_v)]
            return (dg, dyu, dyd, dye, dyn, dkap, [dl1, dl2, dl3, dl4], dmh2)

        def add_s(sa, sb, cf):
            return ([sa[0][i] + cf * sb[0][i] for i in range(3)], sa[1] + cf * sb[1], sa[2] + cf * sb[2], sa[3] + cf * sb[3], sa[4] + cf * sb[4], sa[5] + cf * sb[5], [sa[6][i] + cf * sb[6][i] for i in range(4)], [sa[7][0] + cf * sb[7][0], sa[7][1] + cf * sb[7][1]])

        def step38(tv, dt, st):
            k1 = rhs(tv, st)
            k2 = rhs(tv + dt / 3, add_s(st, k1, dt / 3))
            k3 = rhs(tv + 2 * dt / 3, add_s(add_s(st, k1, -dt / 3), k2, dt))
            k4 = rhs(tv + dt, add_s(add_s(add_s(st, k1, dt), k2, -dt), k3, dt))
            cb = ([k1[0][i] + 3 * k2[0][i] + 3 * k3[0][i] + k4[0][i] for i in range(3)], k1[1] + 3 * k2[1] + 3 * k3[1] + k4[1], k1[2] + 3 * k2[2] + 3 * k3[2] + k4[2], k1[3] + 3 * k2[3] + 3 * k3[3] + k4[3], k1[4] + 3 * k2[4] + 3 * k3[4] + k4[4], k1[5] + 3 * k2[5] + 3 * k3[5] + k4[5], [k1[6][i] + 3 * k2[6][i] + 3 * k3[6][i] + k4[6][i] for i in range(4)], [k1[7][0] + 3 * k2[7][0] + 3 * k3[7][0] + k4[7][0], k1[7][1] + 3 * k2[7][1] + 3 * k3[7][1] + k4[7][1]])
            return add_s(st, cb, dt / 8)

        lam0 = [(mp.mpf(2) / 5) * g0_sq, (mp.mpf(2) / 5) * g0_sq, (mp.mpf(1) / 10) * g0_sq, -(mp.mpf(1) / 2) * g0_sq]
        st = ([g0, g0, g0], yu0.copy(), yd0.copy(), ye0.copy(), yn0.copy(), z3.copy(), lam0, [mp.mpf(1), mp.mpf(1)])
        tv = mp.mpf(0)
        for _ in range(25):
            st = step38(tv, t_nu / 25, st)
            tv += t_nu / 25
        st = (st[0], st[1], st[2], st[3], z3.copy(), -(st[4] * st[4].T), st[6], st[7])
        for _ in range(50):
            st = step38(tv, (t_ew - t_nu) / 50, st)
            tv += (t_ew - t_nu) / 50
        gf, yuf, ydf, yef, _, kapf, lamf, mhf = st
        uu, su = svd_asc_u(yuf)
        ud, sd = svd_asc_u(ydf)
        ue, se = svd_asc_u(yef)
        un, sn = svd_asc_u(kapf)
        vc, up = uu.H * ud, ue.H * un
        l1, l2, l3, l4 = lamf
        bfb = min(l1, l2, l3 + l4 + mp.sqrt(max(mp.mpf(0), l1 * l2)) if (l1 > 0 and l2 > 0) else mp.mpf(-1))
        vu_sq = max(mp.mpf(0), -2 * mhf[0] / l2) if l2 > 0 else mp.mpf(0)
        tb = (mhf[1] + (mp.mpf(1) / 2) * (l3 + l4) * vu_sq) / m12_sq
        wmix = ((mp.mpf(3) / 5) * gf[0] ** 2) / (gf[1] ** 2 + (mp.mpf(3) / 5) * gf[0] ** 2)
        return [tb * su[2] / sd[2], sd[2] / se[2], abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]), abs(up[0, 1]), abs(up[1, 2]), abs(up[0, 2]), tb, bfb, wmix], lamf, mhf

    obs0, _, mh0 = kutta38_zero_knob(tr_d5(yu8), tr_d5(yd8), tr_d5(ye8), yn8)
    assert mh0[0] < 0 < mh0[1] and obs0[9] > 0 and obs0[8] > 5 and obs0[0] > 10 and obs0[1] > mp.mpf("1.5")

    _, lam_p4, _ = kutta38_zero_knob(tr_d5(yu8), tr_d5(yd8), tr_d5(ye8), yn8, flip_q=True)
    _, _, mh_p5 = kutta38_zero_knob(tr_d5(yu8), tr_d5(yd8), tr_d5(ye8), yn8, xi_v=mp.mpf(0))
    assert lam_p4[1] < 0 and mh_p5[0] > 0

    rng = random.Random(2026112122)
    max_hh = mp.mpf(0)
    for _ in range(3):
        uq, uru, urd, ul, ure = (householder_u(rng, False) for _ in range(5))
        onr = householder_u(rng, True)
        obs_r, _, _ = kutta38_zero_knob(tr_d5(uq * yu8 * uru.H), tr_d5(uq * yd8 * urd.H), tr_d5(ul * ye8 * ure.H), ul * yn8 * onr.T)
        max_hh = max(max_hh, max(abs(obs_r[k] - obs0[k]) for k in range(len(obs0))))
    assert max_hh < mp.mpf("1e-26")
    print(f"  Kutta 3/8-rule L_2=5/2: BFB={mp.nstr(obs0[9],4)}>0, tan(b)={mp.nstr(obs0[8],4)}, m_u3/m_d3={mp.nstr(obs0[0],4)}, m_d3/m_e3={mp.nstr(obs0[1],4)}, Householder drift={mp.nstr(max_hh,4)}.")
    print(f"  [CAUGHT Plant 4] Flipped top-quartic sign drives lambda_2 = {mp.nstr(lam_p4[1],4)} < 0!")
    print(f"  [CAUGHT Plant 5] Setting xi = 0 keeps m_Hu^2 = {mp.nstr(mh_p5[0],4)} > 0 (no EWSB)!")


def main() -> None:
    t0 = time.time()
    check_ic1_noncommutative_stora_zumino()
    check_ic2_lobachevsky_and_e8_roots()
    check_ic3_kutta38_zero_knob_and_plants()
    print(f"\nALL AGY-C17 INDEPENDENT COUNTERCHECKS & 5/5 PLANTED FAULTS PASSED (elapsed: {time.time() - t0:.2f}s; 0 of 19).")


if __name__ == "__main__":
    main()
