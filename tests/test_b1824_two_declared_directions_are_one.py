"""B1824 -- a0 = eta^4 F_-2 / 6 identically: B1697's a0 = D^2 R - E4 R/48 (Serre derivatives) against B1730's
F_-2 = eta^5 (th2^-2, th4^-2, i th3^-2), by numerical differentiation at 30 digits (independent of the proof's formulas);
N(a0) = i eta^21 / 864 follows from B1730's N(F_a) = i 2^a eta^9; a control that must fail: B1810's direction
t = -5/288 (D^2 R - (5/288) E4 R) is not proportional to F_-2.  theta_2 is summed in tau (mpmath's jtheta(2, 0, q) takes
the principal q^(1/4), wrong for |Re tau| > 1)."""
import json, pathlib
import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1824_two_declared_directions_are_one" / "verification"


def _forms(t):
    q = mp.exp(1j * mp.pi * t)
    t2 = mp.nsum(lambda n: mp.exp(1j * mp.pi * t * (n + mp.mpf(1) / 2) ** 2), [-mp.inf, mp.inf])
    return t2, mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)


def _eta(t):
    return mp.exp(2j * mp.pi * t / 24) * mp.qp(mp.exp(2j * mp.pi * t))


def _E(t, k):
    qq = mp.exp(2j * mp.pi * t)
    c = {2: -24, 4: 240}[k]
    return 1 + c * mp.nsum(lambda n: n ** (k - 1) * qq ** n / (1 - qq ** n), [1, mp.inf])


def _direction(t, tt):
    """D^2 R + tt E4 R, componentwise"""
    def R(u, k):
        a, b, c = _forms(u); d = a * b * c
        return [-a * a / d, -c * c / d, 1j * b * b / d][k]
    qd = lambda f, s: mp.diff(f, s) / (2j * mp.pi)
    out = []
    for k in range(3):
        DR = lambda s: qd(lambda u: R(u, k), s) + _E(s, 2) / 24 * R(s, k)
        out.append(qd(DR, t) - mp.mpf(3) / 2 / 12 * _E(t, 2) * DR(t) + tt * _E(t, 4) * R(t, k))
    return out


def test_the_identity_and_its_norm():
    mp.mp.dps = 30
    for t in (mp.mpc("0.21", "1.07"), mp.mpc("1.6", "0.85")):
        a0 = _direction(t, mp.mpf(-1) / 48)
        a, b, c = _forms(t); h = _eta(t)
        F = [h ** 5 / a ** 2, h ** 5 / c ** 2, 1j * h ** 5 / b ** 2]
        for k in range(3):
            assert abs(a0[k] / (h ** 4 * F[k] / 6) - 1) < mp.mpf(10) ** -20
        assert abs(a0[0] * a0[1] * a0[2] / (1j * h ** 21 / 864) - 1) < mp.mpf(10) ** -20


def test_the_control_fails():
    mp.mp.dps = 30
    t = mp.mpc("0.21", "1.07")
    d = _direction(t, mp.mpf(-5) / 288)
    a, b, c = _forms(t); h = _eta(t)
    F = [h ** 5 / a ** 2, h ** 5 / c ** 2, 1j * h ** 5 / b ** 2]
    r = [d[k] / F[k] for k in range(3)]
    assert max(abs(r[k] / r[0] - 1) for k in (1, 2)) > 1e-3     # not one line


def test_the_committed_checks():
    m = json.loads((V / "a0_identity_main.json").read_text(encoding="utf-8"))
    assert all(max(r["ratio_minus_1"]) < 1e-35 for r in m["part2"])
    assert m["part1"]["R1 (th2/(th3 th4))"]["a0_over_R"] == "-C*(A + C)/48"
    tab = json.loads((V / "b1810_a0_vs_Fm2.json").read_text(encoding="utf-8"))
    assert tab["pairs"] == 64 and tab["max_mass_ratio_difference"] < 1e-14 and tab["max_V_difference_where_defined"] < 1e-13
    ref = json.loads((V / "referee" / "t_a0.json").read_text(encoding="utf-8"))
    assert ref["exact_qseries_a0_equals_P3_over_48_times_theta_minus2"] == [True, True, True]
    assert ref["exact_compared_up_to_x_power"] == 200
