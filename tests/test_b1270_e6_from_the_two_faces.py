"""B1270 — E6 from the two faces: the lattice theorem and the founding-ratio map fast, the
48-surjection coefficient table in the slow lane."""
import sys
from pathlib import Path
from fractions import Fraction as F
import pytest

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1270_e6_from_the_two_faces" / "verification"
sys.path.insert(0, str(VER))


@pytest.fixture(scope="module")
def TF():
    import e6_from_the_two_faces as TF
    return TF


def test_the_golden_face_is_e8_the_icosians(TF):
    units = TF.unit_icosians()
    assert len(units) == 120
    assert all(TF.QN(u) == TF.Q5(1) for u in units)
    roots = TF.e8_roots(units)
    assert len(roots) == 240 and all(TF.bil(r, r) == 2 for r in roots)
    one = (TF.Q5(1), TF.Q5(0), TF.Q5(0), TF.Q5(0))
    from collections import Counter
    orders = Counter(TF.orders_of(u, one, TF.key) for u in units)
    assert dict(orders) == {1: 1, 2: 1, 3: 20, 4: 30, 5: 24, 6: 20, 10: 24}


def test_the_eisenstein_ratio_cuts_out_e6(TF):
    """{1, g} for an order-3 unit is A2 (det 3); its complement has 72 roots with the E6 Cartan matrix."""
    units = TF.unit_icosians()
    roots = TF.e8_roots(units)
    one = (TF.Q5(1), TF.Q5(0), TF.Q5(0), TF.Q5(0))
    w = next(u for u in units if TF.orders_of(u, one, TF.key) == 3)
    dA2, GA2 = TF.gram_det([one, w])
    assert dA2 == 3 and GA2.tolist() == [[2, -1], [-1, 2]]
    perp = [r for r in roots if TF.bil(r, one) == 0 and TF.bil(r, w) == 0]
    assert len(perp) == 72
    # simple roots of a positive system: a positive root that is not a sum of two positive roots
    import random
    rng = random.Random(3)
    while True:
        h = [rng.randint(-97, 97) for _ in range(8)]
        ht = lambda r: sum(hh * float(v) for hh, v in zip(h, [c.x for c in r] + [c.y for c in r]))
        if all(abs(ht(r)) > 1e-9 for r in perp):
            break
    pos = [r for r in perp if ht(r) > 0]
    posk = {TF.key(r) for r in pos}
    simple = [r for r in pos if not any(TF.key(tuple(a - b for a, b in zip(r, s))) in posk
                                       for s in pos if TF.key(s) != TF.key(r))]
    assert len(simple) == 6
    C = [[TF.bil(a, b) for b in simple] for a in simple]
    degs = sorted(sum(1 for x in row if x == -1) for row in C)
    assert degs == [1, 1, 1, 2, 2, 3]                        # the E6 diagram: one branch node, three legs
    import sympy as sp
    assert sp.Matrix([[sp.Rational(x) for x in row] for row in C]).det() == 3
    # the control: the plane {1, i} of an order-4 unit is NOT Eisenstein and its complement is not E6
    i4 = next(u for u in units if TF.orders_of(u, one, TF.key) == 4)
    perp4 = [r for r in roots if TF.bil(r, one) == 0 and TF.bil(r, i4) == 0]
    assert len(perp4) != 72


def test_the_two_letters_land_in_the_icosians_with_the_ratio_of_order_3(TF):
    def mul5(A, B):
        p, q, r, s_ = A
        t, u, v, w_ = B
        return ((p*t + q*v) % 5, (p*u + q*w_) % 5, (r*t + s_*v) % 5, (r*u + s_*w_) % 5)
    R5, L5, I5 = (1, 1, 0, 1), (1, 0, 1, 1), (1, 0, 0, 1)
    seen, frontier = {I5}, [I5]
    while frontier:
        nxt = []
        for M in frontier:
            for g in (R5, L5):
                P = mul5(M, g)
                if P not in seen:
                    seen.add(P)
                    nxt.append(P)
        frontier = nxt
    assert len(seen) == 120                                   # <R, L> mod 5 = SL(2, F5) = 2I
    g5 = tuple((-x) % 5 for x in mul5(R5, (1, 0, 4, 1)))     # g = -R L^-1
    assert mul5(mul5(g5, g5), g5) == I5 and g5 != I5           # order 3


def test_the_six_classes_of_27(TF):
    units = TF.unit_icosians()
    roots = TF.e8_roots(units)
    one = (TF.Q5(1), TF.Q5(0), TF.Q5(0), TF.Q5(0))
    w = next(u for u in units if TF.orders_of(u, one, TF.key) == 3)
    from collections import Counter
    cls = Counter((TF.bil(r, one), TF.bil(r, w)) for r in roots)
    assert cls[(F(0), F(0))] == 72 and cls[(F(2), F(-1))] == 1     # E6 and the root "1" itself
    twenty_sevens = [k for k, v in cls.items() if v == 27]
    assert len(twenty_sevens) == 6


@pytest.mark.slow
def test_the_eisenstein_twists_carry_no_net_27s_on_m004(TF):
    results = TF.part2()
    assert sum(results.values()) == 48
    for k, v in results.items():
        ord_a, ord_b, h1_2, h1_2p, h1_2pp, h0p, rp, h0pp, rpp, N = k
        assert (h1_2p, h1_2pp, N) == (0, 0, 0)
        assert h1_2 == (2 if ord_a == 6 else 0)
