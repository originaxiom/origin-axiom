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
