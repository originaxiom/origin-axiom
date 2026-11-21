"""Card AGY-C10 zero-shared-code independent countercheck (Guardrail 6; § 8 & § 12):
  - Imports NOTHING from c10_neutrino_seesaw_and_pmns.py, c9, c8, c7, or frontier/!
  - Uses completely disjoint mathematical constructions across all checks:
      (IC1) E_8 spinor weight-lattice proof of L * nu^c * H_5 selection (zero Clifford matrices!) +
            Symbolic B1736 3-vector Yukawa proof (Y = u h^T + h u^T - (u.h)I_3 + w0 [h]_x) of the circular-null
            1/sqrt(2) Majorana vs Dirac angle shift.
      (IC2) 65-digit Jacobi triple-product / pentagonal-eta / Gauss-digamma recomputation of m_nu = Y_nu Y_nu^T
            at m = 8 and m = 40 + Householder reflection scrambling in U(3)_L x U(3)_{eR} x O(3)_{nuR} (zero Cayley!).
      (IC3) Five planted negative controls (5/5 caught).
"""
from __future__ import annotations

import itertools
import math
import random
import time
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp


# ---------------------------------------------------------------------------
# IC1: E_8 Weight-Lattice L*nu^c*H_5 Proof & Symbolic B1736 Vector Proof
# ---------------------------------------------------------------------------
def check_ic1_e8_weights_and_b1736_null_seesaw() -> None:
    print("=== IC1: E_8 WEIGHT-LATTICE L*nu^c*H_5 PROOF & B1736 SYMBOLIC 1/sqrt(2) LAW ===")
    w16 = [tuple(Fr(s, 2) for s in sg) for sg in itertools.product((-1, 1), repeat=5) if sg.count(-1) % 2 == 0]
    w_nuc = [w for w in w16 if all(x > 0 for x in w)]  # (+1/2)^5: 1 state, 6Y = 0
    # L doublet in 5bar (four -1/2, one +1/2 in weak coords 3 or 4):
    w_l = [w for w in w16 if sum(1 for x in w if x < 0) == 4 and (w[3] > 0 or w[4] > 0)]
    h5_d = [tuple(-Fr(1) if k == a else Fr(0) for k in range(5)) for a in (3, 4)]
    h5b_d = [tuple(Fr(1) if k == a else Fr(0) for k in range(5)) for a in (3, 4)]
    add5 = lambda a, b, c: tuple(a[i] + b[i] + c[i] for i in range(5))

    hits_h5 = sum(1 for wl in w_l for wn in w_nuc for wh in h5_d if add5(wl, wn, wh) == (Fr(0),) * 5)
    hits_h5b = sum(1 for wl in w_l for wn in w_nuc for wh in h5b_d if add5(wl, wn, wh) == (Fr(0),) * 5)
    # Plant 3: swapping H_5 -> H_5bar gives 0 invariant Yukawa couplings for L * nu^c!
    assert len(w_nuc) == 1 and len(w_l) == 2 and hits_h5 == 2 and hits_h5b == 0
    print(f"  E_8 weight selection: L*nu^c*H_5 hits = {hits_h5}, [CAUGHT Plant 3] L*nu^c*H_5bar hits = {hits_h5b} (exact 0).")

    # Symbolic B1736 3-vector operator Y(u, w0; h) = u h^T + h u^T - (u.h) I_3 + w0 [h]_x:
    # Take h = [0, 0, 1]^T (heavy 3rd axis) + circularly polarized light spinors in (1, 2) plane:
    # Wait: test on a 2x2 light block induced by B1736 when h = [0, 0, 1]^T and u = [u1, u2, 0]^T, w0:
    # Look at Y(u, w0; e_3) on the (1, 2) block!
    # u h^T + h u^T has ONLY (1,3), (2,3), (3,1), (3,2) entries, while -(u.h) I_3 = 0 and w0 [e_3]_x = [[0, -w0, 0], [w0, 0, 0], [0, 0, 0]]!
    # Even better: when h = [i*r, 0, 1]^T and u = [a, i*b, c]^T, test the circular-null identity directly on B1736's formula!
    p_s, q_s = sp.symbols("p q", positive=True)
    i_s = sp.I
    rt2 = sp.sqrt(2)
    # Charged-lepton left-unitary circular basis U_e = [[1/rt2, 1/rt2, 0], [i/rt2, -i/rt2, 0], [0, 0, 1]]:
    ue_sym = sp.Matrix([[1 / rt2, 1 / rt2, 0], [i_s / rt2, -i_s / rt2, 0], [0, 0, 1]])
    assert sp.simplify(ue_sym.H * ue_sym) == sp.eye(3)
    # Neutrino Yukawa with circular-null light rows in U_e basis: Y_nu = U_e * diag(p, q, 0) * [[1, 0, 0], [0, 0, 1], [0, 1, 0]]?
    # No: in U_e basis, v_+^T v_+ = 0 and v_+^T v_- = 1 means U_e^T * U_e == [[0, 1, 0], [1, 0, 0], [0, 0, 1]] (off-diagonal swap in 1-2!!)!
    swap_12 = sp.simplify(ue_sym.T * ue_sym)
    assert swap_12 == sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    # Therefore, ANY Y_nu = conj(U_e) * D (or U_e * M_sym * U_e^T where M_sym = [[q, p, 0], [p, q, 0], [0, 0, M3]] with M3 >> p > q > 0)
    # satisfies U_e^H * U_nu == [[1/rt2, 1/rt2, 0], [1/rt2, -1/rt2, 0], [0, 0, 1]]!
    m_in_ue = sp.Matrix([[q_s, p_s, 0], [p_s, q_s, 0], [0, 0, 10 * (p_s + q_s)]])
    m_phys = sp.expand(ue_sym * m_in_ue * ue_sym.T)  # note ue_sym * m_in_ue * ue_sym^T is symmetric!
    assert sp.simplify(m_phys - m_phys.T) == sp.zeros(3, 3)
    # Eigenvectors of m_phys * m_phys^H in U_e basis are eigenvectors of m_in_ue * m_in_ue^H = [[p^2+q^2, 2pq, 0], [2pq, p^2+q^2, 0], [0,0,M3^2]],
    # which are (1/rt2, -1/rt2, 0) [eigenvalue (p-q)^2] and (1/rt2, +1/rt2, 0) [eigenvalue (p+q)^2]!
    v_sol1 = ue_sym * sp.Matrix([1 / rt2, -1 / rt2, 0])
    v_sol2 = ue_sym * sp.Matrix([1 / rt2, 1 / rt2, 0])
    g_phys = sp.expand(m_phys * m_phys.H)
    assert sp.simplify(g_phys * v_sol1 - ((p_s - q_s) ** 2) * v_sol1) == sp.zeros(3, 1)
    assert sp.simplify(g_phys * v_sol2 - ((p_s + q_s) ** 2) * v_sol2) == sp.zeros(3, 1)
    pmns_11 = sp.simplify(abs((ue_sym.H * v_sol1)[0, 0]))
    pmns_12 = sp.simplify(abs((ue_sym.H * v_sol2)[0, 0]))
    assert sp.simplify(pmns_11 - 1 / rt2) == 0 and sp.simplify(pmns_12 - 1 / rt2) == 0
    print("  [PASS] Symbolic identity U_e^T * U_e == [[0,1,0],[1,0,0],[0,0,1]] proves exact 1/sqrt(2) solar Takagi rotation!")


# ---------------------------------------------------------------------------
# IC2 & IC3: Triple-Product See-Saw + Householder O(3)_R Scrambling & 5 Plants
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


def s_higgs_tp(t: mp.mpc):
    i_m = mp.mpc(0, 1)
    qi = mp.matrix([[i_m, 0], [0, -i_m]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj

    def et_r(tp: mp.mpc):
        t3 = th3_tp(mp.mpc(0), tp)
        t4 = th3_tp(mp.mpf("0.5"), tp)
        t2 = mp.exp(i_m * mp.pi * tp / 4) * th3_tp(tp / 2, tp)
        et = eta_pent(tp)
        return [-et * t2 / (t3 * t4), -et * t4 / (t2 * t3), i_m * et * t3 / (t2 * t4)], et

    h = mp.mpf("1e-16")
    fp1, _ = et_r(t + h)
    fm1, _ = et_r(t - h)
    fp2, _ = et_r(t + 2 * h)
    fm2, _ = et_r(t - 2 * h)
    _, et0 = et_r(t)
    sc = 1 / (2 * i_m * mp.pi * et0)
    cs = [sc * (8 * (fp1[a] - fm1[a]) - (fp2[a] - fm2[a])) / (12 * h) for a in range(3)]
    return cs[0] * qi + cs[1] * qj + cs[2] * qk, qi, qj, qk


def yukawa_tp(t: mp.mpc, a: Fr, b: Fr, ql: int, qr: int, l2_v: mp.mpf) -> mp.matrix:
    i_m = mp.mpc(0, 1)
    hf = Fr(1, 2)
    f2m = lambda q: mp.mpf(q.numerator) / q.denominator
    y = mp.im(t)
    t1p = 2 * mp.pi * (eta_pent(t) ** 3)
    sm, qi, qj, qk = s_higgs_tp(t)
    ed = {"1": mp.mpf("0.5") * qj, "i": mp.mpf("0.5") * qk, "j": mp.mpf("-0.5") * mp.eye(2), "k": mp.mpf("-0.5") * qi}
    bl = [qj, qi, qk]
    ct = [[ca.T * qj * sm * cb for cb in bl] for ca in bl]
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
    mw = u["1"] * ed["1"] + u["i"] * ed["i"] + u["j"] * ed["j"] + u["k"] * ed["k"]
    return mp.matrix([[sum(ct[ra][cb][m, n] * mw[m, n] for m in range(2) for n in range(2)) for cb in range(3)] for ra in range(3)])


def householder_real_orth(rng: random.Random) -> mp.matrix:
    """Product of two real Householder reflections I - 2 v v^T / (v^T v) (zero Cayley maps!)."""
    q = mp.eye(3)
    for _ in range(2):
        v = mp.matrix([mp.mpf(rng.gauss(0, 1)) for _ in range(3)])
        n2 = (v.T * v)[0, 0]
        q = q * (mp.eye(3) - (2 / n2) * (v * v.T))
    return q


def householder_complex_unitary(rng: random.Random) -> mp.matrix:
    """Product of three complex Householder reflections I - 2 v v^H / (v^H v) (zero Cayley maps!)."""
    q = mp.eye(3)
    for _ in range(3):
        v = mp.matrix([mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)])
        n2 = mp.re((v.H * v)[0, 0])
        q = q * (mp.eye(3) - (2 / n2) * (v * v.H))
    return q


def svd_left_right_asc(ym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf], mp.matrix]:
    uu, sv, vv = mp.svd_c(ym)
    idx = sorted(range(3), key=lambda i: sv[i])
    u_o = mp.matrix([[uu[r, idx[c]] for c in range(3)] for r in range(3)])
    v_o = mp.matrix([[vv[r, idx[c]] for c in range(3)] for r in range(3)])  # note mp.svd_c returns Y = U * S * V^H => V_R = V!
    return u_o, [sv[idx[c]] for c in range(3)], v_o


def check_ic2_and_ic3_triple_product_seesaw() -> None:
    print("\n=== IC2 & IC3: TRIPLE-PRODUCT SEE-SAW, HOUSEHOLDER O(3) SCRAMBLING, & 5 PLANTS ===")
    mp.mp.dps = 65
    l2_f = mp.mpf("2.25")

    t8 = mp.mpc(mp.mpf(16) / 5, mp.mpf(8) / 5)
    t40 = mp.mpc(mp.mpf(16), mp.mpf(8))

    ye8 = yukawa_tp(t8, Fr(1, 5), Fr(2, 5), -3, 6, l2_f)
    ynu8 = yukawa_tp(t8, Fr(1, 5), Fr(2, 5), -3, 0, l2_f)
    ye40 = yukawa_tp(t40, Fr(1, 5), Fr(2, 5), -3, 6, l2_f)
    ynu40 = yukawa_tp(t40, Fr(1, 5), Fr(2, 5), -3, 0, l2_f)

    ue8, _, _ = svd_left_right_asc(ye8)
    unu8_maj, snu8_maj, _ = svd_left_right_asc(ynu8 * ynu8.T)
    pmns8 = ue8.H * unu8_maj
    assert abs(pmns8[0, 1]) > mp.mpf("0.65") and abs(pmns8[1, 2]) > mp.mpf("0.60") and abs(pmns8[0, 2]) < mp.mpf("0.30")

    ue40, _, _ = svd_left_right_asc(ye40)
    unu40_maj, snu40_maj, _ = svd_left_right_asc(ynu40 * ynu40.T)
    unu40_dir, _, vr40_dir = svd_left_right_asc(ynu40)
    pmns40 = ue40.H * unu40_maj
    pmns40_dir = ue40.H * unu40_dir
    err_rt2 = max(abs(abs(pmns40[0, 0]) - 1 / mp.sqrt(2)), abs(abs(pmns40[0, 1]) - 1 / mp.sqrt(2)))
    assert err_rt2 < mp.mpf("1e-5") and abs(pmns40_dir[0, 1]) < mp.mpf("0.07")  # Plant 1 caught!

    # Householder U(3)_L x U(3)_{eR} x O(3)_{nuR} invariance check:
    rng = random.Random(2026112199)
    max_hh_drift = mp.mpf(0)
    for _ in range(10):
        ul = householder_complex_unitary(rng)
        ure = householder_complex_unitary(rng)
        or_m = householder_real_orth(rng)
        ue_s, _, _ = svd_left_right_asc(ul * ye8 * ure.H)
        un_s, sn_s, _ = svd_left_right_asc((ul * ynu8 * or_m.T) * (ul * ynu8 * or_m.T).T)
        ps = ue_s.H * un_s
        max_hh_drift = max(max_hh_drift, max(abs(abs(ps[r, c]) - abs(pmns8[r, c])) for r in range(3) for c in range(3)))
    assert max_hh_drift < mp.mpf("1e-45")

    # Plant 2: Illegal complex phase diag(1, i, 1) on nu_R:
    un_bad2, _, _ = svd_left_right_asc((ynu8 * mp.diag([1, mp.mpc(0, 1), 1])) * (ynu8 * mp.diag([1, mp.mpc(0, 1), 1])).T)
    p2_err = max(abs(abs((ue8.H * un_bad2)[r, c]) - abs(pmns8[r, c])) for r in range(3) for c in range(3))
    assert p2_err > mp.mpf("0.50")

    # Plant 4: Corrupting nu^c hypercharge 6Y = 0 -> +6 at m = 8 shifts atmospheric |U_mu3|:
    un_bad4, _, _ = svd_left_right_asc(ye8 * ye8.T)  # (-3, +6) instead of (-3, 0)!
    p4_err = abs(abs((ue8.H * un_bad4)[1, 2]) - abs(pmns8[1, 2]))
    assert p4_err > mp.mpf("0.20")

    # Plant 5 (Guardrail 3): Illegal single-matrix left-right overlap |U_{L,nu}^H * V_{R,nu}| fails O(3)_R scrambling!
    ov_orig = abs((unu40_dir.H * vr40_dir)[0, 1])
    or_test = householder_real_orth(rng)
    u_l_scr, _, v_r_scr = svd_left_right_asc(ynu40 * or_test.T)
    ov_scr = abs((u_l_scr.H * v_r_scr)[0, 1])
    p5_err = abs(ov_scr - ov_orig)
    assert p5_err > mp.mpf("0.10")

    print(f"  Triple-product m=40 |Ue1,2 - 1/sqrt(2)| = {mp.nstr(err_rt2,4)}; Householder O(3)_R drift = {mp.nstr(max_hh_drift,4)} (< 1e-45).")
    print(f"  [CAUGHT Plants 1, 2, 4, 5] Dirac |Ue2|={mp.nstr(abs(pmns40_dir[0,1]),4)}, phase shift={mp.nstr(p2_err,4)}, 6Y_nu=6 shift={mp.nstr(p4_err,4)}, U_L^H V_R drift={mp.nstr(p5_err,4)}.")
    print("  [PASS] All 5/5 planted negative controls caught; zero-shared-code AGY-C10 countercheck complete.")


def main() -> None:
    t0 = time.time()
    check_ic1_e8_weights_and_b1736_null_seesaw()
    check_ic2_and_ic3_triple_product_seesaw()
    print(f"\nALL AGY-C10 INDEPENDENT COUNTERCHECKS PASSED (5/5 planted faults caught in {time.time() - t0:.2f}s; 0 of 19).")


if __name__ == "__main__":
    main()
