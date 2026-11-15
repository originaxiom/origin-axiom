"""B1945's lock: frame C's pointwise cusp exponents (pointwise_exponents.json) against three independent sources.
(1) B1788's closed form e(m2/m3) = 1/2 - (||2 q_L a|| + ||2 q_R a||)/2, computed here from the charges;
(2) W178's exact tuple on the slope-2/5 lines (3/10, 4/5, 1/5, 11/20), harvest row 1497;
(3) the averaged read-out's decay rates from B1940's own file (area_measure_mp.json), which must be the minima over the
    24 points of the pointwise exponents."""
import json, math, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
D = json.loads((HERE / "pointwise_exponents.json").read_text())
SIXY = {"Q": 1, "u": -4, "d": 2}
SEC = {"up": ("Q", "u"), "down": ("Q", "d")}
KEYS = {"up": ("up|L_2|S", "up|L_2|St"), "down": ("down|L_2|S", "down|L_2|St")}


def nd(x):
    x = x % 1
    return min(x, 1 - x)


A0 = json.loads((HERE / "pointwise_exponents_a0.json").read_text())   # the a = 0 points at 40, 60, 80 (40 + 3.5 Im tau digits)


def last(k, p, j):
    """the exponent k of a ratio C y^s |q|^k, fitted from the two slopes between three heights: 24, 32, 40 for a != 0,
    and 40, 60, 80 for the a = 0 points, which carry a power of Im tau"""
    if p in A0:
        (s1, s2), (y0, y1, y2) = A0[p][k][j], (40, 60, 80)
    else:
        (s1, s2), (y0, y1, y2) = D[p][k][j], (24, 32, 40)
    L1, L2 = math.log(y1 / y0), math.log(y2 / y1); h = 2 * math.pi * (y1 - y0)
    assert y2 - y1 == y1 - y0
    pw = (s1 - s2) * h / (L2 - L1)
    return s1 + pw * L1 / h


def test_the_a_zero_points():
    assert sorted(A0) == ["0,1/5", "0,2/5", "0,3/5", "0,4/5"]
    for p in A0:
        for k, want in (("up|L_2|S", (0.5, 1.0)), ("up|L_2|St", (0.5, 0.5)), ("down|L_2|S", (0.5, 1.0)), ("down|L_2|St", (0.5, 0.5))):
            got = (last(k, p, 0), last(k, p, 1))
            assert all(abs(g - w) < 2e-3 for g, w in zip(got, want)), (p, k, got)


def test_every_second_generation_cell_is_the_closed_form():
    n = 0
    for p in D:
        a = Fr(p.split(",")[0])
        for sec, (ql, qr) in SEC.items():
            e = Fr(1, 2) - (nd(2 * SIXY[ql] * a) + nd(2 * SIXY[qr] * a)) / 2
            for k in KEYS[sec]:
                tol = 2e-3 if p in A0 else 1e-3      # the a = 0 cells carry corrections beyond one power of Im tau; the grid is 5e-3
                assert abs(last(k, p, 0) - float(e)) < tol, (p, k, last(k, p, 0), e)
                n += 1
    assert n == 96


def test_the_slope_two_fifths_points_are_w178s_tuple():
    for p in D:
        if Fr(p.split(",")[0]) in (Fr(2, 5), Fr(3, 5)):
            got = (last("up|L_2|St", p, 0), last("up|L_2|St", p, 1), last("down|L_2|S", p, 0), last("down|L_2|S", p, 1))
            assert all(abs(g - w) < 1e-3 for g, w in zip(got, (0.3, 0.8, 0.2, 0.55))), (p, got)


def test_the_average_takes_the_minima():
    A = json.loads((next((ROOT / "frontier").glob("B1940_*")) / "verification" / "area_measure_mp.json").read_text())
    F = A["fbar_at_heights_held"]; y0, y1 = "30", "37"
    order = ["up|L_2|St", "up|L_2|S", "down|L_2|S", "down|L_2|St"]
    for i, k in enumerate(order):
        for j in range(2):
            slope = -(math.log(F[y1][2 * i + j]) - math.log(F[y0][2 * i + j])) / (2 * math.pi * 7)
            m = min(last(k, p, j) for p in D)
            assert abs(slope - m) < 5e-3, (k, j, slope, m)


def test_b1788s_tropical_rule_gives_every_cell_both_generations():
    import sys; sys.path.insert(0, str(HERE)); import tropical_check as TC
    c = TC.cells()
    assert len(c) == 192 and max(abs(g - float(pe)) for *_, g, pe in c) < 2e-3
    assert sum(abs(g - float(pe)) > 2e-3 for *_, g, pe in TC.cells(dict(TC.SIXY, u=-3))) >= 40     # a planted charge breaks it


def test_b1659s_law_on_frame_c():
    import sys; sys.path.insert(0, str(HERE)); import determinant_law as DL
    mp = DL.mp; EPS = mp.matrix([[0, 1], [-1, 0]])
    for (a, b, sec) in ((Fr(1, 5), Fr(2, 5), "up"), (Fr(2, 5), Fr(1, 5), "down")):
        RD, Mw, Ys, u, cs, ds = DL.parts("0.13", 1.7, a, b, sec)
        for rn in ("S", "St"):
            S = RD[rn]; pair = sum(((EPS * S * Mw.T)[i, i] for i in range(2)), mp.mpc(0))
            assert abs(mp.det(Ys[rn]) - 4 * mp.det(S) * mp.det(Mw) * pair) < mp.mpf(10) ** -25 * abs(mp.det(Ys[rn]))
            assert abs(mp.det(Ys[rn]) - 4 * mp.det(S) * mp.det(Mw) * pair * (1 + mp.mpf(10) ** -6)) > mp.mpf(10) ** -25 * abs(mp.det(Ys[rn]))
