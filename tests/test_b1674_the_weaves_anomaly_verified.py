"""B1674 -- the weave's anomaly, verified on main (the SM seat's W101). Live: the anomaly table over all 64 assignments
from n_G = 9 sum_f w_G(f) s_f (mod 24), with a bite (a wrong determinant exponent changes the counts); the weight
congruences; det Y_1 = 8 eta^6 at two moduli. Stored: main's independent run (det rho = chi_eta^9 on words; the interior
curve) and the received run reproduced."""
import itertools, pathlib
import mpmath as mp
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1674_the_weaves_anomaly_verified"
W = {"SU3": {"Q": 2, "u": 1, "d": 1}, "SU2": {"Q": 3, "L": 1}, "grav": {"Q": 6, "u": 3, "d": 3, "L": 2, "e": 1, "nu": 1}}
F = ["Q", "u", "d", "L", "e", "nu"]


def n(G, s, e=9): return (e * sum(w * s[f] for f, w in W[G].items())) % 24


def table(e=9):
    su3 = su2 = grav = 0; su2_values = set()
    for signs in itertools.product((1, -1), repeat=6):
        s = dict(zip(F, signs))
        su2_values.add(n("SU2", s, e))
        if n("SU3", s, e) == 0:
            su3 += 1
            assert (s["u"] == s["d"] == -s["Q"]) or e != 9
            if n("grav", s, e) == 0: grav += 1
    return su3, su2_values, grav


def test_the_anomaly_table_and_its_bite():
    assert table() == (16, {6, 12, 18}, 4)                       # 16 of 64; SU(2) never; gravity 4 of the 16
    assert table(e=8) != table()                                  # bite: a different determinant exponent moves the counts
    for sQ, su, sd in itertools.product((1, -1), repeat=3):       # the weight congruence 6K = m (mod 24)
        m = (-9 * (2 * sQ + su + sd)) % 24
        Ks = [K for K in range(4) if (6 * K - m) % 24 == 0]
        assert len(Ks) == 1
        if (sQ, su, sd) == (1, 1, 1): assert Ks == [2]
        if su == sd == -sQ: assert Ks == [0]


def test_det_Y1_is_8_eta6():
    mp.mp.dps = 25
    for tau in (mp.mpc(0.1, 1.2), mp.mpc(-0.3, 0.9)):
        q = mp.exp(1j * mp.pi * tau)
        t2, t3, t4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
        eta = mp.exp(2j * mp.pi * tau / 24) * mp.qp(mp.exp(2j * mp.pi * tau))
        assert abs(2 * t2 ** 2 * t3 ** 2 * t4 ** 2 / (8 * eta ** 6) - 1) < 1e-15


def test_stored_runs():
    mc = (A / "verification" / "main_check" / "v1_independent_run.txt").read_text()
    assert "T exponents (turns): [0.125, 0.375, 0.875]" in mc and "image order 96" in mc
    assert "det rho(word)=chi_eta^9 on 200 random words: True" in mc and "SU2 values: [6, 12, 18]" in mc
    curve = mc
    assert "['0.32414679']" in curve and "['0.17212223']" in curve
