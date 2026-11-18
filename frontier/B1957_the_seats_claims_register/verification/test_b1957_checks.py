"""B1957's second lock: the load-bearing facts of main's own checks of the seats' claims, each recomputed here (no stored
number is read) and each with the change that breaks it."""
import pathlib, sys
from fractions import Fraction as F
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "checks"))
import sm_rge_matrix as R, cim_overlap as C, cim_closed as CC


def _two_loop_mixed(swapped, th=0.02):
    e_t = np.array([0, 0, 1.0]); e_b = np.array([0, np.sin(th), np.cos(th)])
    def angle(v):
        g, H, FD, FL, lam = R.unpack(v); tu = np.linalg.eigh(H.conj().T @ H)[1][:, -1]; td = np.linalg.eigh(FD.conj().T @ FD)[1][:, -1]
        return np.arccos(min(1.0, abs(np.vdot(tu, td))))
    def part(yt, yb):
        v = R.pack([0, 0, 0], yt * np.outer(e_t, e_t), yb * np.outer(e_b, e_b), np.zeros((3, 3)), 0.0); e = 1e-3
        d = lambda loops: (np.log(np.sin(angle(v + e * R.rhs(0, v, loops, swapped)))) - np.log(np.sin(angle(v - e * R.rhs(0, v, loops, swapped))))) / (2 * e)
        return (d(2) - d(1)) / R.K ** 2
    return part(1.0, 1.0) - part(1.0, 1e-3) - part(1e-3, 1.0)


def test_the_mixings_two_loop_coefficient_is_eleven_halves_and_seven_is_the_exchanged_order():
    assert abs(_two_loop_mixed(False) + 5.5) < 0.01
    assert abs(_two_loop_mixed(True) + 7.0) < 0.01


def test_the_determinants_phase_does_not_run_and_the_singular_values_do():
    rng = np.random.default_rng(1); Y = lambda s: s * (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
    v0 = R.pack([0.5, 0.6, 1.0], Y(0.3), Y(0.2), Y(0.1), 0.3); o0, t0 = R.observables(v0); o1, t1 = R.observables(R.run(v0, -6.0))
    assert abs(t1 - t0) < 1e-12 and np.abs(o1[:9] / o0[:9] - 1).max() > 0.05


def test_the_closed_form_of_the_triple_overlap_is_the_quadrature():
    tau = 0.23 + 1.37j; w = 0.2 * tau + 0.4
    for qL, qR in ((1, -4), (1, 2), (-3, 6)):
        Yq = C.overlap(tau, qL * w, qR * w, (qL + qR) * w / 2)
        assert np.abs(Yq - CC.Y(tau, (qL - qR) * w / 2)).max() < 1e-11
        assert np.abs(Yq - CC.Y(tau, (qL - qR) * w / 2 + 0.01)).max() > 1e-3            # a moved Wilson line is seen


def test_the_overlap_is_covariant_and_the_wrong_spin_structure_is_not():
    tau = 0.23 + 1.37j
    assert C.unit_err(C.transport(3, 0.5, 0.5, tau, 0.0, "T")) < 1e-11 and C.unit_err(C.transport(3, 0.5, 0.5, tau, 0.0, "S")) < 1e-11
    assert C.unit_err(C.transport(3, 0.0, 0.0, tau, 0.0, "T")) > 0.3


def test_the_higgs_bubble_is_not_a_function_of_the_point_and_its_lift_average_is_a_multiple_of_the_identity():
    tau = 0.23 + 1.37j; w = 0.2 * tau + 0.4; k = np.arange(6); Z3 = np.diag((-1.0) ** k); X3 = np.roll(np.eye(6), 3, axis=0)
    def bub(ww):
        B = np.zeros((6, 6), complex)
        for qL, qR, nc in ((1, -4, 3), (1, 2, 3), (-3, 6, 1)):
            Yx = CC.Y(tau, (qL - qR) * ww / 2); B += nc * np.einsum("ijk,ijl->kl", Yx.conj(), Yx)
        return B
    B0 = bub(w)
    assert np.abs(bub(w + tau) - B0).max() > 1.0                                        # a lattice vector changes it
    assert np.abs(bub(w + tau) - X3 @ B0 @ X3.T).max() < 1e-10 and np.abs(bub(w + 1) - Z3 @ B0 @ Z3).max() < 1e-10
    avg = sum(g @ B0 @ g.conj().T for g in (np.eye(6), Z3, X3, Z3 @ X3)) / 4
    assert np.abs(avg - np.trace(avg) / 6 * np.eye(6)).max() < 1e-10
    assert np.abs(B0 - np.trace(B0) / 6 * np.eye(6)).max() > 0.1                        # one lift alone is not


def test_under_b_minus_l_the_up_and_down_sectors_have_one_wilson_line_and_under_hypercharge_two():
    BL3 = {"Q": 1, "u": -1, "d": -1, "L": -3, "e": 3}; Y6 = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}      # left-handed fields; 3(B - L) and 6Y
    delta = lambda ch, l, r: ch[l] - ch[r]
    assert delta(BL3, "Q", "u") == delta(BL3, "Q", "d") == 2 and delta(BL3, "L", "e") == -6                  # so the two matrices are one function of one argument
    assert (delta(Y6, "Q", "u"), delta(Y6, "Q", "d"), delta(Y6, "L", "e")) == (5, -1, -9)
    tau = 0.13 + 4j; w = 0.2 * tau + 0.4
    assert np.abs(np.abs(CC.Y(tau, delta(Y6, "Q", "u") * w / 2)) - np.abs(CC.Y(tau, delta(Y6, "Q", "d") * w / 2))).max() > 1e-3
    assert np.abs(np.abs(CC.Y(tau, 5 * w / 2)) - np.abs(CC.Y(tau, 5 * (0.6 * tau + 0.8) / 2))).max() < 1e-12         # Delta = 5 at order 5: a half-lattice point; (1, 2) and (3, 4) agree mod 2
    assert np.abs(np.abs(CC.Y(tau, 5 * w / 2)) - np.abs(CC.Y(tau, 5 * (0.4 * tau + 0.2) / 2))).max() > 1e-3          # (2, 1) is another class


def test_the_mass_terms_anomalous_dimension_agrees_between_the_two_primary_sources():
    yt2, yb2, yl2, g1s, g2s, g3s, lam = F(7, 11), F(3, 13), F(2, 17), F(5, 19), F(6, 23), F(9, 29), F(4, 31)
    lx = 2 * lam; Y2 = 3 * yt2 + 3 * yb2 + yl2; HS = 3 * yt2 ** 2 + 3 * yb2 ** 2 + yl2 ** 2
    Y4 = (F(17, 20) * g1s + F(9, 4) * g2s + 8 * g3s) * yt2 + (F(1, 4) * g1s + F(9, 4) * g2s + 8 * g3s) * yb2 + F(3, 4) * (g1s + g2s) * yl2
    LX2 = (-15 * lx ** 2 - 12 * lx * Y2 - F(9, 2) * HS - 21 * yt2 * yb2 + (F(36, 5) * g1s + 36 * g2s) * lx + 5 * Y4 + (3 + F(471, 400)) * g1s ** 2 + F(9, 8) * g1s * g2s + (15 - F(385, 16)) * g2s ** 2)
    B2 = 2 * (lam * (-30 * lam - 36 * yt2 - 36 * yb2 - 12 * yl2 + 36 * g2s + F(36, 5) * g1s) + yt2 * (-F(27, 4) * yt2 - F(21, 2) * yb2 + 20 * g3s + F(45, 8) * g2s + F(17, 8) * g1s)
              + yb2 * (-F(27, 4) * yb2 + 20 * g3s + F(45, 8) * g2s + F(5, 8) * g1s) + yl2 * (-F(9, 4) * yl2 + F(15, 8) * g2s + F(15, 8) * g1s) - F(145, 32) * g2s ** 2 + F(1671, 800) * g1s ** 2 + F(9, 16) * g2s * g1s)
    assert LX2 == B2 == F(-886154046205665125, 503238848400166736)


def test_the_flavour_groups_action_has_rank_41_and_44_with_the_neutrino_operator():
    rng = np.random.default_rng(7); ri = lambda: rng.integers(-5, 6, size=(3, 3)) + 1j * rng.integers(-5, 6, size=(3, 3))
    Yu, Yd, Ye = ri(), ri(), ri(); A = ri(); Kap = A + A.T; gens = []
    for i in range(3):
        m = np.zeros((3, 3), complex); m[i, i] = 1j; gens.append(m)
    for i in range(3):
        for j in range(i + 1, 3):
            m = np.zeros((3, 3), complex); m[i, j], m[j, i] = 1, -1; gens.append(m)
            m = np.zeros((3, 3), complex); m[i, j] = m[j, i] = 1j; gens.append(m)
    z = np.zeros((3, 3), complex); cs, ce = [], []
    for slot in range(5):
        for G in gens:
            dYu = G @ Yu if slot == 0 else (-Yu @ G if slot == 1 else z); dYd = G @ Yd if slot == 0 else (-Yd @ G if slot == 2 else z); dYe = G @ Ye if slot == 3 else (-Ye @ G if slot == 4 else z)
            dK = G @ Kap + Kap @ G.T if slot == 3 else z; v = np.concatenate([M.ravel().view(float) for M in (dYu, dYd, dYe)]); cs.append(v); ce.append(np.concatenate([v, dK[np.triu_indices(3)].view(float)]))
    assert np.linalg.matrix_rank(np.array(cs), tol=1e-8) == 41 and np.linalg.matrix_rank(np.array(ce), tol=1e-8) == 44
    assert np.linalg.matrix_rank(np.array(cs)[:, :36], tol=1e-8) < 41                    # without the charged leptons' matrix the rank falls


def test_the_first_columns_drift_and_its_growth_near_degenerate_masses():
    th = np.pi / 8; s6, s3, s2 = 6 ** 0.5, 3 ** 0.5, 2 ** 0.5
    U = np.array([[2 / s6, np.cos(th) / s3, np.sin(th) / s3], [-1 / s6, np.cos(th) / s3 - np.sin(th) / s2, np.sin(th) / s3 + np.cos(th) / s2], [-1 / s6, np.cos(th) / s3 + np.sin(th) / s2, np.sin(th) / s3 - np.cos(th) / s2]], complex)
    def drift(ms, yt):
        K = U @ np.diag(ms).astype(complex) @ U.T; D = np.diag([1, 1, np.exp(-3 * yt * yt * (-30) / (32 * np.pi ** 2))]); Kir = D @ K @ D
        ev = np.linalg.eigh(Kir.conj().T @ Kir)[1]; slot = int(np.where(np.argsort([m * m for m in ms]) == 0)[0][0]); return abs(abs(ev[0, slot]) ** 2 - 2 / 3)
    assert drift((1, 2, 5), 1 / 20) < 1e-3 and drift((1, 1.00001, 5), 1 / 20) > 0.2


def test_the_casimir_slope_is_the_closed_integral_and_negative():
    from scipy.special import kv
    from scipy.integrate import quad
    for L in (0.2, 1.0, 3.0):
        C = 4 * L; k = np.arange(1, int(60 / C) + 2); x = k * C
        bessel = 4 * (-4 * 28 * np.pi ** 2 / 90 / C ** 5 - 76 * ((-1.0) ** k * (-kv(3, x) / x ** 2) * k).sum() / (2 * np.pi ** 2))
        closed = -7 * np.pi ** 2 / (1440 * L ** 5) - 19 / (2 * np.pi ** 2 * L ** 2) * quad(lambda t: np.log1p(np.exp(-4 * L * np.cosh(t))) * np.cosh(3 * t), 0, 12)[0]
        assert abs(bessel / closed - 1) < 1e-9 and closed < 0
    L = 3.0; C = 4 * L; k = np.arange(1, int(60 / C) + 2); x = k * C                    # the second branch (4 massless bosons in place of 28 net fermions): the slope is positive there, so the sign is the count's
    assert 4 * (+4 * 4 * np.pi ** 2 / 90 / C ** 5 - 76 * ((-1.0) ** k * (-kv(3, x) / x ** 2) * k).sum() / (2 * np.pi ** 2) + (96 - 64) * ((-kv(3, x) / x ** 2) * k).sum() / (2 * np.pi ** 2)) > 0


def test_the_partial_traces_are_one_half_and_the_gauge_part_is_the_hypercharge_component():
    import physical_main01 as PM
    for v in PM.PTS:
        assert abs(np.trace(PM.D(*v) @ PM.E3) - 0.5) < 1e-12 and abs(np.trace(PM.D(*v) @ PM.E2) + 0.5) < 1e-12 and abs(np.trace(PM.D(*v))) < 1e-12
    rng = np.random.default_rng(3); Y = rng.normal(size=(5, 5, 3, 3)) + 1j * rng.normal(size=(5, 5, 3, 3)); O, Fm = PM.build(Y)
    assert np.abs(PM.trW(O, PM.E3) - Fm / 2).max() < 1e-12 and np.abs(PM.trW(O, PM.E3) - Fm).max() > 0.1          # F/2, and not F
    proj = np.kron(PM.trW(O, PM.E3) / 3, PM.E3) + np.kron(PM.trW(O, PM.E2) / 2, PM.E2)
    assert np.abs(proj + np.kron(Fm / 12, PM.Y6)).max() < 1e-12


def test_two_of_the_thirty_two_candidates_are_representations():
    import web_wa1_reps as WR
    keep = []
    for k in range(1, 5):
        rT = np.diag(WR.w ** ((k * WR.X * WR.X) % 5))
        for s in (1, -1):
            Fk = WR.w ** ((s * np.outer(WR.X, WR.X)) % 5) / np.sqrt(5)
            for c in (1, -1, 1j, -1j):
                if WR.extends(c * Fk, rT) is not None: keep.append((k, s, c))
    assert keep == [(2, 1, -1), (3, -1, -1)]


def test_the_loop_seats_exponent_rule_gives_its_gap_ratios_and_its_six_w_law():
    import agyexp_ur345 as U
    from fractions import Fraction as Fr
    assert sorted({g for a in U.prim(5) if (g := U.gap(a, 1, 2)) is not None}) == [Fr(39, 31), Fr(5, 3)] == sorted({g for a in U.prim(5) if (g := U.gap(a, -3, 6)) is not None})
    assert all(U.exps(a, -3, 6) == U.exps((6 * a) % 1, 1, 2) for a in U.prim(15)) and not all(U.exps(a, -3, 6) == U.exps((3 * a) % 1, 1, 2) for a in U.prim(15))
    assert [c for c in range(10) if all(U.exps(a, -3, 6) == U.exps((c * a) % 1, 1, 2) for a in U.prim(10))] == []


def test_the_cusps_indicial_roots_and_the_decay_constant():
    import sympy as sp
    r, ell, c, d = sp.symbols("r ell c delta", positive=True); beta = (sp.sqrt(1 + 4 * ell ** 2 * c) - 1) / 2
    for root in (-beta, 1 + beta): assert sp.simplify(-(root ** 2 - root) / ell ** 2 + c) == 0
    assert sp.simplify(sp.expand((beta - d) * (1 + beta + d)) - (ell ** 2 * c - d - d ** 2)) == 0
    assert sp.simplify(-((sp.Rational(1, 2)) ** 2 - sp.Rational(1, 2)) / ell ** 2 + c) != 0            # 1/2, the edge of the measure, is not a root


def test_the_twisted_eta_automaton_decays_as_one_over_root_two_and_vanishes_on_the_odd_ticks_double_cover():
    import agy002_m34 as A, mpmath as mp, numpy as np
    K, NEG, NXT, const, integ = A.cocycle(); assert const < 1e-30 and integ < 1e-30
    T = mp.zeros(24, 24)
    for i in range(24):
        for bit in (0, 1): T[i, int(NXT[bit, i])] += mp.exp(1j * mp.pi * int(K[bit, i]) / 30) / 2
    rho = max(abs(e) for e in mp.eig(T, left=False, right=False)); assert abs(rho ** 2 - mp.mpf(1) / 2) < 1e-30
    b, k, end = A.etas(10, K, NEG, NXT, (2, 4)); keep = (end != 0) & (b != 0) & (b != 1023); assert int(keep.sum()) == 95          # the note printed 85; its sealed file has 95
    n = 5; P = np.array([[0, 1], [1, 0]], dtype=object); hit = 0; halves = 0
    for w in range(1 << n):
        Mo = A.word_matrix(w, n) @ P
        for q in A.PTS:
            u = ((Mo[0, 0] * q[0] + Mo[0, 1] * q[1]) % 5, (Mo[1, 0] * q[0] + Mo[1, 1] * q[1]) % 5)
            if u not in (q, ((-q[0]) % 5, (-q[1]) % 5)): continue
            _, k2, e2 = A.etas(2 * n, K, NEG, NXT, q, bits=[(w << n) | (31 ^ w)]); assert e2[0] == 1 and k2[0] == 0; hit += 1          # exactly zero on the double cover
            _, kh, _ = A.etas(n, K, NEG, NXT, q, bits=[31 ^ w]); halves += int(kh[0] != 0)
    assert hit == 80 and halves > 0                                                                                    # (40, 40) at length 5; the halves are not zero separately
    wrong = K.copy(); wrong[0, 0] += 1; T2 = mp.zeros(24, 24)                                                           # a planted step: the radius moves
    for i in range(24):
        for bit in (0, 1): T2[i, int(NXT[bit, i])] += mp.exp(1j * mp.pi * int(wrong[bit, i]) / 30) / 2
    assert abs(max(abs(e) for e in mp.eig(T2, left=False, right=False)) ** 2 - mp.mpf(1) / 2) > 1e-6


def test_the_twisted_triplets_transport_law_under_tau_plus_one():
    import agy002_m40 as M, mpmath as mp
    tau, a, b = mp.mpc("0.13", "1.45"), mp.mpf(1) / 5, mp.mpf(2) / 5
    for eps in (1, -1):
        da, db = 3 * a, 3 * b; new, old = M.R(tau + 1, da, db - da, eps), M.R(tau, da, db, eps); ph = mp.exp(1j * mp.pi / 4 + 1j * mp.pi * da ** 2)
        pred = (ph * old[0], ph * mp.exp(2j * mp.pi * eps * da) * old[2], -ph * mp.exp(-2j * mp.pi * eps * da) * old[1])
        assert max(abs(x / y - 1) for x, y in zip(new, pred)) < 1e-30
        assert abs(new[1] / (ph * mp.exp(-2j * mp.pi * eps * da) * old[2]) - 1) > 0.1                                    # the other representative's phase does not fit


def test_heckes_period_at_discriminant_twelve_carries_the_half_and_the_full_dedekind_zeta():
    import web_wz1_other_discriminants as Z, mpmath as mp
    s = 3; I, ell, tu = Z.period((1, 2, -2), 12, s, nodes=64, N=(150, 300)); full = float(mp.mpf(12) ** (mp.mpf(s) / 2) * mp.gamma(mp.mpf(s) / 2) ** 2 / mp.gamma(s) * mp.zeta(s) * Z.Lf(s, 12))
    assert tu == (4, 1) and abs(I / full - 1) < 1e-8 and abs(I / (2 * full) - 1) > 0.4                                 # with the half; without it, off by one half


def test_the_cusp_degree_assignment_closes_only_at_higgs_charge_zero():
    import web_posthoc_closure as C
    for sec, (q1, q2, cons) in C.SEC.items():
        r = C.closing(q1, q2); hits = {m: [qh for d, qh in r[m] if d == [2, 2, 1]] for m in r}
        assert all(cons not in hits[m] for m in hits) and (hits["M1"] == hits["M2"] == ([] if sec == "up" else [0]))


def test_frame_d1_at_the_pole_is_frame_c_at_shifted_charges_and_off_it_a_non_periodic_scalar_times_it():
    import web_wb2_d1 as D
    from fractions import Fraction as Fr
    t = D.mp.mpc("0.13", "1.7"); a, b = Fr(2, 5), Fr(4, 5); ql, qr, qh = D.SEC["up"]
    Yd = D.d1(t, a, b, "up", 2); Yc = D.W.coupling("0.13", 1.7, a, b, ql - qh, qr - qh, True)["S"]; Yw = D.W.coupling("0.13", 1.7, a, b, ql, qr, True)["S"]
    assert D.W.upto(Yd, Yc) < 1e-12 and D.W.upto(Yd, Yw) > 1e-3                                                        # frame C at q' = q - q_H, and not frame C at q
    h = 2 * qh * (D.f2m(a) * t + D.f2m(b)); x, y = D.chars(ql, a, b), D.chars(qr, a, b); xp, yp = D.chars(ql - qh, a, b), D.chars(qr - qh, a, b)
    lg = [(D.mp.im(u), D.mp.log(abs(D.malt(x, y, h, u - h, t)[0, 0] / D.B.bil_mp(xp, yp, u, t)[0][0]))) for u in (D.mp.mpc("0.21", "0.13"), D.mp.mpc("-0.17", "0.31"))]
    assert abs((lg[1][1] - lg[0][1]) / (lg[1][0] - lg[0][0]) + 2 * D.mp.pi * 2 * qh * D.f2m(a)) < 1e-20                # k = -2 pi c q_H a


def test_the_two_step_scheme_gives_the_q_moment_one_minus_rho_squared_and_a_point_independent_of_the_projection():
    import physical_c3e_two_steps as P
    t = 0.02; g = lambda rho, w=np.zeros(4): P.h(t, rho, w) / t ** 2
    assert abs(g(0.7) - P.EQ * (1 - 0.49)) < 5e-3 and abs(g(1.3) - P.EQ * (1 - 1.69)) < 5e-3                           # the lane's (7); a wrong sign or power of rho fails
    assert abs((g(1 + 1e-4) - g(1 - 1e-4)) / 2e-4 + 2 * P.EQ) < 5e-3                                                  # slope -2 e_Q at rho = 1
    w = np.array([0.7, -0.4, 0.5, 0.3]); inv = []
    for ww in (np.zeros(4), w):
        rho = P.brentq(lambda x: P.h(0.1, x, ww), 0.5, 1.5, xtol=1e-15); X = P.act(P.first_step(0.1, rho, ww), P.raw(0.1, rho)); m4, mq = P.moment(X)
        assert np.abs(m4).max() < 1e-12 and abs(mq) < 1e-12                                                          # the complete moment vanishes
        inv.append([np.vdot(f, f).real for f in X])
    assert np.abs(np.array(inv[0]) - np.array(inv[1])).max() < 1e-10 and abs(inv[0][4] - 0.01) > 1e-5               # one point for both projections, and not the raw one


def test_e8s_adjoint_has_100_and_68_sl2_summands_and_the_eighth_power_trace_is_120_on_the_family():
    import physical_c3e_roster as P
    W = P.e8_weights(); n1, _ = P.summands(W, (4, 2, 0, 0, 0, 0, 0, 0)); n2, _ = P.summands(W, (4, 2, 4, 2, 0, 0, 0, 0))
    assert len(W) == 248 and (n1, n2) == (100, 68)                                                                    # ranks 148 and 180
    tr = lambda x, y, k: sum((float(w[0]) * x + float(w[1]) * y) ** k for w in W); lam = 1.3
    assert abs(tr(lam, 1j * lam, 8) - 120 * lam ** 8) < 1e-8 and abs(tr(lam, 1j * lam, 4)) < 1e-9 and abs(tr(lam, 1.1j * lam, 4)) > 1  # off the family the quartic does not vanish


def test_the_word_l_rinv_l_is_inn_a_after_the_based_quarter_turn_and_the_two_lifts_differ():
    import physical_harmonic_draft as H
    Delta = H.comp(H.L, H.Rinv, H.L); gD = H.qmul(H.qmul(H.gL, H.qinv(H.gR)), H.gL)
    assert Delta == H.comp(H.inn(H.a), H.S) and Delta != H.S and Delta != H.comp(H.S, H.inn(H.a)) and H.homology(Delta) == H.homology(H.S) == [[0, 1], [-1, 0]]
    assert gD == H.qmul(H.QI, H.gs) and H.in_E(Delta, gD) and H.in_E(H.S, H.gs) and not H.in_E(H.S, gD)
    assert H.qmul(H.gs, H.QK) == H.qmul(H.QK, H.gs) and H.qmul(gD, H.QK) == H.qmul(H.MONE, H.qmul(H.QK, gD))            # a rotation and a reflection: +1 and -1 on the top line


def test_the_boundary_response_is_the_solution_of_the_field_equations_on_a_disc():
    import math
    R, cH, G, kap, n = 1.3, 0.7, 0.9, 1.1, 2
    f0 = (kap * n / R) / (cH / G + kap * R / 2)                         # (c_H/G) f + kappa (f R^2/2 - n)/R = 0
    r, p = cH / (G * math.pi * R * R), kap / (2 * math.pi * R); B = math.pi * f0 * R * R
    E = (cH / (2 * G)) * f0 ** 2 * math.pi * R * R + (kap / 2) * ((f0 * R * R / 2 - n) / R) ** 2 * 2 * math.pi * R
    assert abs(B - p * 2 * math.pi * n / (r + p)) < 1e-12 and abs(E - r * p * (2 * math.pi * n) ** 2 / (2 * (r + p))) < 1e-12
    assert abs(math.pi * R * R * (kap * n / R) / (cH / G - kap * R / 2) - p * 2 * math.pi * n / (r + p)) > 1            # the other sign in the Robin condition fails


def test_the_figure_eight_groups_congruence_indices_at_two_three_and_four():
    import web_wz1_c3_indices as Z
    idx = {}
    for N in (2, 3, 4):
        a = ((1 % N, 0), (1 % N, 0), (0, 0), (1 % N, 0)); b = ((1 % N, 0), (0, 0), (0, (-1) % N), (1 % N, 0)); idx[N] = Z.order_psl(N) // Z.closure([a, b], N)
    assert idx == {2: 6, 3: 1, 4: 12}                                                                                 # contains Gamma(4), not Gamma(2)
    E = [((1, 0), x, (0, 0), (1, 0)) for x in ((1, 0), (0, 1))] + [((1, 0), (0, 0), x, (1, 0)) for x in ((1, 0), (0, 1))]
    assert Z.closure(E, 4) == Z.order_psl(4) == 1920                                                                 # the order formula against a full enumeration


def test_the_census_has_379_words_268_manifolds_and_33_with_an_orientation_reversing_self_map():
    import itertools
    import web_wf1_on_main as F
    words = ["".join(t) for n in range(2, 13) for t in itertools.product("LR", repeat=n)]; prim = [w for w in words if F.primitive(w)]
    states = {F.state(w) for w in prim}; mans = sorted({F.manifold(w) for w in prim}); rc = lambda v: F.canon(v, (lambda u: u,))
    amph = [m for m in mans if rc(m) == rc(F.swap(m[::-1])) or rc(m) == rc(F.swap(m))]
    assert (len(states), len(mans), len(amph)) == (379, 268, 33) and "LR" in amph and sum(1 for s in states if int(F.mat(s).trace()) % 2) == 163


def test_only_the_all_half_turn_face_admits_a_hyperbolic_step():
    import itertools, functools
    import web_wf7_on_main as G
    prods = [functools.reduce(G.comp, [G.MOVES[m] for m in seq]) for n in range(1, 5) for seq in itertools.product(G.MOVES, repeat=n)]
    hyp = lambda fs: sum(1 for f in fs if G.kind(G.h1(f)) == "hyperbolic")
    hhh = [f for f in prods if G.is_step(f, "", ("abc",))]; mhh = [f for f in prods if G.is_step(f, "a", ("abcacb",))]; mmm = [f for f in prods if G.is_step(f, "abc", ("ab", "bc", "ca"))]
    assert (len(hhh), hyp(hhh)) == (2800, 512) and (len(mhh), hyp(mhh)) == (670, 0) and (len(mmm), hyp(mmm)) == (538, 0)


def test_a_cone_point_kills_every_class_on_the_scar_and_the_free_product_has_three():
    import itertools
    import web_wf4_on_main as W
    p = 1000033; lam = (1, 2, 2, 3, -2, -1, -3, -2); out = {}
    for K in (3, 4, None):
        rels = [(1, 1), (2, 2), (3, 3)] + ([(1, 2, 3) * K] if K else []); tot = nz = 0
        for s in itertools.product((1, p - 1), repeat=3):
            if K and pow(s[0] * s[1] * s[2] % p, K, p) != 1: continue
            V = W.Rep({1: [[s[0]]], 2: [[s[1]]], 3: [[s[2]]]}, p); tot += W.cohom(V, rels)[1]
            Z = W.nullspace([[V.fox(r, g)[0][0] for g in (1, 2, 3)] for r in rels], p, 3); nz += any(sum(V.fox(lam, g)[0][0] * c[g - 1] for g in (1, 2, 3)) % p for c in Z)
        out[K] = (tot, nz)
    assert out == {3: (0, 0), 4: (2, 0), None: (5, 3)}


def test_the_golden_act_fixes_two_non_trivial_lines_of_the_266_up_to_sign():
    from fractions import Fraction as Fr
    pts = {(Fr(a, n), Fr(b, n)) for n in range(1, 13) for a in range(n) for b in range(n)}; neg = lambda q: ((-q[0]) % 1, (-q[1]) % 1); lines = {min(q, neg(q)) for q in pts}
    act = lambda q: ((q[0] - q[1]) % 1, (2 * q[1] - q[0]) % 1); fixed = sorted(q for q in lines if act(q) in (q, neg(q)))
    assert len(lines) == 266 and fixed == [(Fr(0), Fr(0)), (Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(4, 5))]                # so B1922's 'no other line' was false


def test_a_metallic_tick_has_a_mark_exactly_for_odd_m():
    for m in range(1, 13):
        N = m * m + 4; Ap = ((m * m + 2, m), (m, 2))
        ker = [(x, y) for x in range(N) for y in range(N) if (Ap[0][0] * x + Ap[0][1] * y) % N == 0 and (Ap[1][0] * x + Ap[1][1] * y) % N == 0]
        full = any(all((k * x) % N or (k * y) % N for k in range(1, N)) for x, y in ker)
        assert full == (m % 2 == 1) and len(ker) == N                                  # the kernel mod N of A + 1; a vector of full order N in it exactly for odd m
        if m % 2:
            lam = (m * pow(2, -1, N)) % N; assert (lam * lam + 1) % N == 0 and ((m * m + 2) % N, m % N) == ((lam * m) % N, (lam * 2) % N)
        else:
            assert not any((x * x + 1) % N == 0 for x in range(N))                               # no square root of -1 at all: 4 divides N


def test_the_cusp_rule_is_the_integrals_condition_and_the_floor_alone_is_not():
    b = lambda a: (a - 1) // 2 if a >= 1 else a // 2; fin = lambda a, n: (a - 2 * n > 0) or (a == 2 * n and a <= 0); G = range(-40, 41)
    assert all(fin(a, n) == (n <= b(a)) for a in G for n in G)
    assert sorted({a for a in G for n in G if fin(a, n) != (n <= a // 2)}) == [a for a in G if a >= 2 and a % 2 == 0]


def test_the_eigenvalue_field_is_the_levels_field_exactly_at_the_metallic_traces():
    import web_wc8_part4_on_main as P
    assert all((P.sqfree(t * t - 4) == P.sqfree(t + 2)) == P.issq(t - 2) for t in range(3, 3001))
    assert (P.sqfree(3 * 3 - 4) == P.sqfree(3 + 2)) != P.issq(3 + 2)                             # the control with t + 2 fails at once


def test_the_per_centre_rule_of_the_reversing_involution_holds_on_every_palindromic_cyclic_word():
    import itertools
    import web_tube_p740_rule as T
    seen = set(); kinds = {"between": 0, "on": 0}
    for n in range(2, 11):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t); rots = [w[i:] + w[:i] for i in range(n)]
            if "L" not in w or "R" not in w or len(set(rots)) < n or min(rots) in seen: continue
            seen.add(min(rots))
            for pair in T.centres(min(rots)):
                for centre in pair:
                    Z, W = T.Z_at(min(rots), centre); kinds[centre[0]] += 1
                    assert T.det(Z) == -1 and T.mul(Z, Z) == T.ONE and T.mul(T.mul(Z, W), T.inv(Z)) == T.inv(W)       # an involution that reverses the word
                    assert T.one2(Z) == (centre[0] == "between")                                                      # the rule; exchanged, it fails on every centre
    assert kinds["between"] > 50 and kinds["on"] > 50
    A = T.M("L" * 6 + "R" + "LR" * 6); X = ((-1, 6), (0, 1))
    assert T.mul(T.mul(X, A), T.inv(X)) == T.inv(A) and T.one2(X) and not T.one2(T.mul(X, A))


def test_an_invariant_function_is_stationary_at_i_and_at_omega_and_not_elsewhere():
    import mpmath as mp
    import web_weave_action_on_tau as W
    f = lambda x, y: W.E_fourier(mp.mpc(x, y), mp.mpf(3))
    gi, hi = W.grad_hess(f, W.I); go, ho = W.grad_hess(f, W.OM); gg, _ = W.grad_hess(f, W.GEN)
    assert gi < 1e-6 and go < 1e-6 and gg > 1 and hi[0] < 0 < hi[1] and ho[0] > 0                     # a saddle at i, a minimum at omega


def test_the_threads_classes_modulo_2_and_the_census_to_length_8():
    import web_selection_exact as S
    words = [w for n in range(2, 13) for w in S.lyndon(n)]
    assert len(words) == 745 and len([w for w in words if len(w) <= 8]) == 69
    for w in words:
        c = S.cls(w); assert (c == "transposition") == (len(w) % 2 == 1)                      # L and R are transpositions modulo 2
    sw = str.maketrans("LR", "RL"); canon = lambda w: min(min(w[i:] + w[:i] for i in range(len(w))), min(w.translate(sw)[i:] + w.translate(sw)[:i] for i in range(len(w))))
    up = {canon(w): S.cls(w) for w in words if len(w) <= 8}
    assert [sum(1 for v in up.values() if v == k) for k in ("3-cycle", "transposition", "identity")] == [16, 13, 8]


def test_a_chiral_thread_sees_the_level_and_its_mirror_sees_it_with_the_other_sign():
    import math, warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore"); import web_scale_census as C
    v1, c1, _ = C.data("LLR"); v2, c2, _ = C.data("LRR"); v0, c0, _ = C.data("LR")
    assert abs(c1 + math.pi ** 2 / 24) < 1e-9 and abs(c1 + c2) < 1e-9 and abs(v1 - v2) < 1e-9 and abs(c0) < 1e-9 and abs(v0 - 2.0298832128) < 1e-9
    vm, cm, _ = __import__("web_scale_troot_tsign").data("b+-LR")
    assert abs(abs(cm) - math.pi ** 2 / 2) < 1e-9                                               # the sign of the monodromy shifts the invariant by a quarter


def test_an_isotropic_direction_and_a_real_one_overlap_by_at_most_one_half():
    import math
    import web_first_row_bound as B
    rng = np.random.default_rng(4)
    for _ in range(4000):
        u = rng.normal(size=3) + 1j * rng.normal(size=3); v = rng.normal(size=3) + 1j * rng.normal(size=3)
        assert B.ratio(u, v) <= B.bound(B.sig(u), B.sig(v)) + 1e-12
    x = np.array([1.0, 0, 0]); y = np.array([0, 1.0, 0]); iso = x + 1j * y
    assert abs(B.sig(iso)) < 1e-15 and abs(B.ratio(iso, x) - 0.5) < 1e-15 and B.bound(0.0, 1.0) == 0.5        # attained
    assert B.ratio(iso, iso) > B.bound(0.0, 1.0)                                                             # and the cap is not a bound for two isotropic directions


def test_the_subregular_sl2_of_e6_fixes_no_vector_of_the_27_so_it_is_not_inside_f4():
    import web_session_relay_f4 as E
    Ci = E.inverse(E.C); w27 = E.weights((1, 0, 0, 0, 0, 0)); assert len(w27) == 27
    def content(d):
        eigs = []
        for w in w27:
            coef = [sum(Ci[i][j] * w[j] for j in range(6)) for i in range(6)]; eigs.append(int(sum(coef[i] * d[i] for i in range(6))))
        return E.sl2_content(eigs)
    assert content((2, 2, 2, 2, 2, 2)) == {16: 1, 8: 1, 0: 1}                    # the regular sl2: 17 + 9 + 1, a fixed vector, as inside F4
    assert content((2, 2, 0, 2, 2, 2)) == {12: 1, 8: 1, 4: 1}                    # the subregular one: 13 + 9 + 5, none


def test_order_three_gives_three_fixed_points_and_is_prime_to_e6s_outer_group():
    import web_session_relay_three as T
    assert len(T.autos(T.C)) == 2                                                  # the outer group of E6 has order 2 ...
    D4 = T.cartan([(0, 1), (1, 2), (1, 3)], 4); assert len(T.autos(D4)) == 6       # ... and D4's has 6: there order 3 is not forced inner
    img, length = T.longest(T.C); perm = tuple(tuple(-x for x in v).index(1) for v in img)
    assert length == 36 and perm == (4, 3, 2, 1, 0, 5)                             # -w0 is the non-trivial automorphism of E6
    F4 = T.cartan([(0, 1), (2, 3)], 4, double=[(1, 2)]); img, length = T.longest(F4)
    assert length == 24 and all(tuple(-x for x in img[i]).index(1) == i for i in range(4))          # and the identity on F4: -1 is in W(F4)
    fixed = lambda a, b, c, d, N=12: sum(1 for x in range(N) for y in range(N) if ((a - 1) * x + b * y) % N == 0 and (c * x + (d - 1) * y) % N == 0)
    assert fixed(0, -1, 1, -1) == 3 and fixed(-1, 0, 0, -1) == 4 and fixed(0, -1, 1, 0) == 2 and fixed(1, -1, 1, 0) == 1      # orders 3, 2, 4, 6


def test_the_half_letter_carries_the_reflection_to_the_reverser_at_a_letter():
    h = F(1, 2); mul = lambda X, Y: tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2)); Fm = ((-1, 0), (0, 1)); one = ((1, 0), (0, 1))
    for half, mhalf, inv in ((((1, h), (0, 1)), ((1, -h), (0, 1)), ((1, -1), (0, 1))), (((1, 0), (h, 1)), ((1, 0), (-h, 1)), ((1, 0), (-1, 1)))):
        assert mul(mul(half, Fm), mhalf) == mul(Fm, inv)                           # x^(1/2) F x^(-1/2) = F x^-1
        assert mul(mul(half, one), mhalf) != mul(Fm, inv)                          # which is not what the identity gives


def test_a_three_cusped_manifold_has_a_symmetry_of_order_three_that_is_trivial_on_one_cusp():
    import snappy
    M = snappy.Manifold("otet10_00005"); G = M.symmetry_group(); n = G.order(); iso = G.isometries(); assert M.num_cusps() == 3 and n == 12
    ident = next(i for i in range(n) if all(G.multiply_elements(i, j) == j for j in range(n))); seen = set()
    for i in range(n):
        if i != ident and G.multiply_elements(G.multiply_elements(i, i), i) == ident:
            assert list(iso[i].cusp_images()) == [0, 1, 2]; seen.add(tuple(int(A[0, 0] + A[1, 1]) for A in iso[i].cusp_maps()))
    assert seen == {(-1, 2, -1)}                                                   # half of (3 + 0 + 3) is 3


def _e8_roots():
    import itertools
    roots = set()
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [F(0)] * 8; v[i] = F(si); v[j] = F(sj); roots.add(tuple(v))
    for signs in itertools.product((1, -1), repeat=8):
        if sum(1 for s in signs if s < 0) % 2 == 0: roots.add(tuple(F(s, 2) for s in signs))
    return roots


def test_the_colour_centraliser_in_e8_is_e6_and_the_reflection_splits_it_38_and_40():
    roots = _e8_roots(); assert len(roots) == 240
    dot = lambda a, b: sum(p * q for p, q in zip(a, b)); colour = [r for r in roots if all(c == 0 for c in r[3:]) and sum(r[:3]) == 0]; assert len(colour) == 6
    e6 = [r for r in roots if all(dot(r, c) == 0 for c in colour)]; Q = lambda r: F(2, 3) * (r[0] + r[1] + r[2])
    assert len(e6) == 72 and sorted({Q(r) for r in e6}) == [-1, 0, 1] and sum(1 for r in e6 if Q(r) == 1) == 16
    assert {Q(r) for r in roots} > {Q(r) for r in e6}                              # thirds outside E6: the reflection has order 6 on E8
    lam = (0, 0, 0, 2, 1, 2, 1, 0); even = [r for r in e6 if (Q(r) - dot(lam, r)) % 2 == 0]
    assert len(even) + 6 == 38 and len(e6) - len(even) == 40
    assert all(Q(r) == 0 or dot(lam, r) % 2 == 1 for r in even)                    # the charge's sign exchanges a spinor's two halves: its even part is the odd weights
    assert sum(1 for r in e6 if Q(r) != 0 and dot(lam, r) % 2 == 0) == 16          # which the weight alone would have put on the other side


def test_the_protected_quartic_needs_the_coupling_at_least_root_two_times_the_charge():
    lhs = lambda y2, e2, x, z: y2 * x * z + e2 / 2 * (x - z) ** 2; low = lambda e2, x, z: e2 / 2 * (x + z) ** 2
    for x, z in ((F(1), F(1)), (F(3), F(1, 7)), (F(0), F(5)), (F(2, 3), F(9, 4))):
        assert lhs(F(2), F(1), x, z) == low(F(1), x, z)                            # equality at y^2 = 2 e^2, for every x and z
        assert lhs(F(5), F(1), x, z) >= low(F(1), x, z)
    assert lhs(F(1), F(1), F(1), F(1)) < low(F(1), F(1), F(1))                     # and below it the bound fails


def test_the_axis_stabiliser_in_the_binary_octahedral_group_has_order_sixteen():
    import physical_state_orbit as O, itertools
    I2, qi, qj, qk = O.I2, O.qi, O.qj, O.qk; gens = [(I2 + qi) / np.sqrt(2), (I2 + qj) / np.sqrt(2)]; G = [I2]; grew = True
    while grew:
        grew = False
        for g in list(G):
            for h in gens:
                x = g @ h
                if not any(np.allclose(x, y) for y in G): G.append(x); grew = True
    assert len(G) == 48
    stab = [g for g in G if np.allclose(g @ qk @ np.linalg.inv(g), qk) or np.allclose(g @ qk @ np.linalg.inv(g), -qk)]
    assert len(stab) == 16 and len(G) // len(stab) == 3                            # three axes, three cosets
    assert len([g for g in stab if np.allclose(g @ qi @ np.linalg.inv(g), qi) or np.allclose(g @ qi @ np.linalg.inv(g), -qi)]) == 8


def test_the_figure_eight_group_has_index_twelve_by_volume_and_by_its_images():
    import mpmath as mp
    mp.mp.dps = 30; vol = 3 * mp.clsin(2, 2 * mp.pi / 3); L2 = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
    cov = mp.mpf(3) ** mp.mpf("1.5") * mp.zeta(2) * L2 / (4 * mp.pi ** 2); assert abs(vol / cov - 12) < mp.mpf(10) ** -25
    assert abs(2 * mp.clsin(2, mp.pi / 3) / cov - 12) < mp.mpf(10) ** -25 and abs(mp.clsin(2, mp.pi / 3) / cov - 12) > 1      # one tetrahedron is not the knot
    for N, order in ((2, 10), (4, 320)):
        mulr = lambda x, y: ((x[0] * y[0] - x[1] * y[1]) % N, (x[0] * y[1] + x[1] * y[0] - x[1] * y[1]) % N); addr = lambda x, y: ((x[0] + y[0]) % N, (x[1] + y[1]) % N)
        mm = lambda X, Y: tuple(tuple(addr(mulr(X[i][0], Y[0][j]), mulr(X[i][1], Y[1][j])) for j in range(2)) for i in range(2))
        one, zero = (1, 0), (0, 0); a = ((one, one), (zero, one)); b = ((one, zero), ((0, (-1) % N), one)); I = ((one, zero), (zero, one)); mI = ((((-1) % N, 0), zero), (zero, ((-1) % N, 0)))
        seen = {I}; todo = [I]
        while todo:
            X = todo.pop()
            for g in (a, b):
                Y = mm(X, g)
                if Y not in seen: seen.add(Y); todo.append(Y)
        assert len(seen) == order and mI in seen                                  # indices 60/10 = 6 and 3840/320 = 12


def test_no_power_of_the_golden_tick_fixes_a_class_and_the_silver_square_root_does_not_change_that():
    mul = lambda X, Y: tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2)); J = ((1, 1), (1, 0)); P = ((1, 0), (0, 1)); dets = []
    for n in range(1, 13): P = mul(P, J); dets.append((P[0][0] - 1) * (P[1][1] - 1) - P[0][1] * P[1][0])
    assert [abs(d) for d in dets[:8]] == [1, 1, 4, 5, 11, 16, 29, 45] and all(d != 0 for d in dets)
    I2 = ((1, 0), (0, 1)); assert (I2[0][0] - 1) * (I2[1][1] - 1) - I2[0][1] * I2[1][0] == 0      # the identity, by contrast, fixes everything: b_1 would be 3


def test_the_sign_of_the_equation_is_the_sign_of_the_curvature():
    import sympy as sp
    z, zb = sp.symbols("z zb"); curv = lambda rho: sp.simplify(-4 * sp.exp(-2 * rho) * sp.diff(rho, z, zb)); Lh = -sp.log(z * zb)
    assert curv(-sp.log(Lh) - sp.log(z * zb) / 2) == -4 and curv(-sp.log(1 + z * zb)) == 4
    assert sp.simplify(-sp.diff(-sp.log(Lh), z, zb) + sp.exp(-2 * sp.log(Lh)) / (z * zb)) == 0          # the cusp solves this sign
    assert sp.simplify(-sp.diff(-sp.log(Lh), z, zb) - sp.exp(-2 * sp.log(Lh)) / (z * zb)) != 0          # and not the other


def test_a_common_zero_of_the_two_maps_leaves_as_many_classes_as_its_order():
    import physical_cyclic_mass as CM, sympy as sp
    w = sp.symbols("w")
    for f0, f1, want in ((w ** 2, w * (w - 1), 1), (w ** 2, sp.Integer(0), 2), (w ** 2, (w - 1) * (w - 2), 0)):
        d1, d2, (n0, n1, n2) = CM.trunc_complex(f0, f1, 6); r1, r2 = d1.rank(), d2.rank()
        assert (n0 - r1, n1 - r1 - r2, n2 - r2) == (0, want, want)
    assert CM.h1(-2, False) == 2 and CM.h0(2, False) == 2 and CM.h1(-1, False) == 1 and CM.h0(1, False) == 1 and CM.h0(0, False) == 0 and CM.h0(0, True) == 1


def test_the_square_of_the_fourier_generator_is_the_parity_up_to_the_gauss_scalar():
    for N, r, want in ((3, 2, -1), (5, 3, 1)):
        h = pow(2, -1, N); w = np.exp(2j * np.pi / N); x = np.arange(N); g = sum(w ** ((r * h * k * k) % N) for k in range(N)) / np.sqrt(N)
        T = np.diag(w ** ((r * h * x * x) % N)); C = np.zeros((N, N)); C[(-x) % N, x] = 1; Fm = w ** ((-r * np.outer(x, x)) % N) / np.sqrt(N); S = Fm / g
        assert np.allclose(Fm @ Fm, C) and np.allclose(np.linalg.matrix_power(S @ T, 3), S @ S) and np.allclose(S @ S, want * C)
        assert not np.allclose(np.linalg.matrix_power(Fm @ T, 3), Fm @ Fm) or abs(g - 1) < 1e-12        # without the scalar the relation fails unless the scalar is 1


def test_the_one_loop_relation_among_the_couplings():
    """added at Review 84: a record cited the three coefficients and its check computed one of them"""
    b1, b2, b3 = F(41, 10), F(-19, 6), F(-7)
    den = (b1 - b2) + F(8, 5) * (b2 - b3)
    assert (F(3, 5) * (b2 - b3) / den, (b1 - b2) / den) == (F(23, 134), F(109, 201))         # sin^2 = 23/134 + (109/201) alpha_EM/alpha_3
    d = (F(-10) - b1, F(-7, 3) - b2, F(-7, 3) - b3)                                           # the Pati-Salam stage's coefficients minus the Standard Model's
    assert (b2 - b3, b1 - b2) == (F(23, 6), F(109, 15))
    assert F(22) * F(23, 3) / 67 == F(506, 201)
    assert (F(3, 5) * (F(-7, 3) - F(-7)) / den) != F(23, 134)                                 # another b2 gives another constant


def test_the_pair_of_coefficient_spheres_is_not_the_native_pair_and_the_composite_is():
    import physical_four_form as FF, math
    qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]], dtype=complex)
    trs = [float(np.trace(FF.gc(qi @ FF.Dp(p), qj @ FF.Dp(-p))).real) for p in (0.0, 0.5, math.pi / 2)]
    assert all(abs(t - (2 - 4 * math.cos(p) ** 2)) < 1e-12 for t, p in zip(trs, (0.0, 0.5, math.pi / 2))) and abs(trs[0] - trs[2]) > 3      # one gauge orbit, traces from -2 to 2
    rng = np.random.default_rng(7); cv = lambda: rng.normal(size=2) + 1j * rng.normal(size=2); un = lambda: (lambda x: x / np.linalg.norm(x))(cv())
    u0, v0, d1, d2 = un(), un(), cv(), cv()
    def curve(s):
        u_ = u0 + s * d1; v_ = v0 + s * d2; return u_ / np.linalg.norm(u_), v_ / np.linalg.norm(v_)
    AW = lambda u_, v_: (FF.Um(u_) @ FF.Jm @ np.linalg.inv(FF.Um(u_)), FF.Um(u_) @ np.linalg.inv(FF.Um(np.conj(v_))))
    assert max(np.abs(a - b).max() for a, b in zip(AW(u0, v0), AW(np.exp(0.6j) * u0, np.exp(-0.6j) * v0))) < 1e-12          # the composite is constant on the orbit
    h = 1e-5; (um, vm), (up, vp) = curve(-h), curve(h); du, dv = (up - um) / (2 * h), (vp - vm) / (2 * h)
    A0, W0 = AW(u0, v0); dA = (AW(up, vp)[0] - AW(um, vm)[0]) / (2 * h); dW = (AW(up, vp)[1] - AW(um, vm)[1]) / (2 * h); k = dW @ np.linalg.inv(W0); DA = dA - FF.com(k, A0) / 2
    lhs, conn = FF.quot(u0, v0, du, dv)
    assert abs(lhs - (FF.ip(DA, DA) + FF.ip(k, k)) / 2) < 1e-7 and abs(conn - (np.vdot(u0, du).imag - FF.ip(A0, k) / 2)) < 1e-7
    assert abs(lhs - (FF.ip(dA, dA) + FF.ip(k, k)) / 2) > 1e-3                                                                 # without the cross term the metric is another


def test_the_cross_module_kernel_is_a_line_and_the_planar_normal_term_is_sixteen_over_d():
    import sympy as sp
    c0, c1, c2, c3, t0, t1, f = sp.symbols("c0 c1 c2 c3 t0 t1 f"); Q = sp.zeros(5, 5)
    for i, c in enumerate((c0, c1, c2, c3)): Q[i, i + 1] = c
    Q[3, 0] = f * t0; Q[4, 1] = f * t1
    assert Q.det() == 0 and Q[0:4, 1:5].det() == c0 * c1 * c2 * c3
    Q[4, 0] = 1; assert Q.det() != 0                                              # an entry of another weight would lift the kernel
    a, s = sp.symbols("a s", real=True); d = 10 - 6 * a; D = 5 - d * s * (1 - s)
    assert sp.simplify(d * D - 9 * (1 - a ** 2) - (sp.diff(D, s) / 2) ** 2 - 16) == 0        # |v|^2 D - (D'/2)^2 = 16, with N^2 = 9 b^2


def test_a_permutation_called_an_involution_has_order_four():
    p = [4, 3, 5, 0, 1, 2, 6, 7]; q = list(range(8)); order = 0
    while True:
        q = [p[i] for i in q]; order += 1
        if q == list(range(8)): break
    assert order == 4


def test_the_monodromy_has_order_four_modulo_three_and_its_root_order_eight():
    mul = lambda X, Y, n: tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) % n for j in range(2)) for i in range(2)); one = ((1, 0), (0, 1))
    def order(X, n):
        P = tuple(tuple(x % n for x in r) for r in X); k = 1
        while P != one: P = mul(P, X, n); k += 1
        return k
    M, J = ((2, 1), (1, 1)), ((1, 1), (1, 0))
    assert order(M, 3) == 4 and order(J, 3) == 8 and mul(M, M, 3) == ((2, 0), (0, 2))          # another seat had written 'order 8' for M
    pts = [(a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0)]; act = lambda w, X: tuple(sum(w[k] * X[k][j] for k in range(2)) % 3 for j in range(2))
    orb = {(1, 0)}; w = act((1, 0), M)
    while w not in orb: orb.add(w); w = act(w, M)
    assert len(orb) == 4 and len(pts) == 8                                                     # not transitive on the eight points
    assert order(M, 5) == 10 and mul(tuple(tuple((M[i][j] + one[i][j]) % 5 for j in range(2)) for i in range(2)), tuple(tuple((M[i][j] + one[i][j]) % 5 for j in range(2)) for i in range(2)), 5) == ((0, 0), (0, 0))


def test_the_punctured_mapping_torus_has_no_second_cohomology_and_its_fourth_cover_has_torsion_3_and_15():
    import sympy as sp
    from sympy.matrices.normalforms import smith_normal_form
    d2 = sp.Matrix([[1, 1], [1, 0], [0, 0]])                                                   # M - 1 over a zero row for the base circle
    assert d2.rank() == 2                                                                      # so H_2 = 0 and H^2 = 0 on the punctured carrier
    assert sp.Matrix([[0, 0], [0, 0], [0, 0]]).rank() == 0                                     # the control: a trivial monodromy leaves H_2 = Z^2
    M = sp.Matrix([[2, 1], [1, 1]]); S = smith_normal_form(M ** 4 - sp.eye(2), domain=sp.ZZ)
    assert sorted(abs(S[i, i]) for i in range(2)) == [3, 15] and sorted(abs(x) for x in smith_normal_form(M ** 2 - sp.eye(2), domain=sp.ZZ).diagonal()) != [3, 15]
    pts = [(a, b) for a in range(15) for b in range(15) if ((33 * a + 21 * b) % 15, (21 * a + 12 * b) % 15) == (0, 0)]
    assert len(pts) == 45                                                                      # the fixed points of the fourth power on the 15-torsion


def test_the_trace_over_the_three_is_half_the_phased_sum_and_the_projection_is_F_over_twelve():
    import cmath, itertools
    z = cmath.exp(2j * cmath.pi / 5); X = np.roll(np.eye(5), 1, axis=0); Z = np.diag([z ** k for k in range(5)]); P = np.zeros((5, 5)); P[(-np.arange(5)) % 5, np.arange(5)] = 1
    P3 = (np.eye(5) + P) / 2
    for a, b in itertools.product(range(5), repeat=2):
        if (a, b) == (0, 0): continue
        D = z ** (3 * a * b) * np.linalg.matrix_power(X, a) @ np.linalg.matrix_power(Z, b)
        assert abs(np.trace(D @ P3) - 0.5) < 1e-12 and abs(np.trace(D)) < 1e-12                # main's B1953 had written 1: the factor two
    assert abs(np.trace(P3) - 3) < 1e-12 and abs(np.trace(np.eye(5) @ P3) - 0.5) > 1          # the control: the identity is not one of the 24
    Fv = 1.0; proj = np.diag([Fv / 6] * 3 + [-Fv / 4] * 2); Y6 = np.diag([-2.0, -2, -2, 3, 3])
    assert np.allclose(proj, -Fv / 12 * Y6) and not np.allclose(proj, -Fv / 6 * Y6)            # the lane's own preserved draft had the second


def test_a_free_prefactor_removes_no_input_and_the_log_quartic_is_stationary_off_its_zero():
    import sympy as sp
    v, a, Vol, c, phi = sp.symbols("v a Vol c phi", positive=True)
    assert sp.solve(sp.Eq(sp.log(v), -a * Vol + sp.log(c)), c) == [v * sp.exp(Vol * a)]        # every v is reached by a choice of c
    assert sp.solve(sp.Eq(sp.log(v), -a * Vol + sp.log(2)), v) == [2 * sp.exp(-Vol * a)]       # the control: with c fixed, v is fixed
    l0, l1 = sp.symbols("l0 l1"); V = (l0 + l1 * sp.log(phi)) * phi ** 4 / 4; dV = sp.simplify(sp.diff(V, phi) / phi ** 3)
    assert sp.simplify(dV - ((l0 + l1 * sp.log(phi)) + l1 / 4)) == 0                           # lambda + beta/4, not lambda


def test_the_even_exterior_algebra_of_three_plus_two_is_anomaly_free_only_at_the_weil_charges():
    import itertools
    def sums(a, b):
        st = [(sum(k3) * a + sum(k2) * b) for k3 in itertools.product((0, 1), repeat=3) for k2 in itertools.product((0, 1), repeat=2) if (sum(k3) + sum(k2)) % 2 == 0]
        s = F(3 * a + 2 * b, 2); return len(st), sum(q - s for q in st), sum((q - s) ** 3 for q in st)
    n, lin, cub = sums(-2, 3); assert n == 16 and lin == 0 and cub == 0                        # (1 - 5P)/2 = diag(-2, -2, -2, 3, 3)
    assert sums(1, 1)[1:] == (0, 0) and sums(-2, 3)[0] == 16                                   # the shifted charges vanish for every a, b ...
    st = [(sum(k3) * -2 + sum(k2) * 3) for k3 in itertools.product((0, 1), repeat=3) for k2 in itertools.product((0, 1), repeat=2) if (sum(k3) + sum(k2)) % 2 == 0]
    assert sum(st) == 0 and sum(q ** 3 for q in st) == 0                                       # ... and unshifted only when 3a + 2b = 0
    st1 = [(sum(k3) * 1 + sum(k2) * 1) for k3 in itertools.product((0, 1), repeat=3) for k2 in itertools.product((0, 1), repeat=2) if (sum(k3) + sum(k2)) % 2 == 0]
    assert sum(st1) != 0
