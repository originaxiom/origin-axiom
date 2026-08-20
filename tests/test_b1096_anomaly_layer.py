"""B1096 lock: the anomaly table over 16 vs 15, exact."""
from fractions import Fraction as F

GEN16 = [
    ("Q", 3, 2, F(1, 6), F(1, 3)),
    ("u^c", 3, 1, F(-2, 3), F(-1, 3)),
    ("d^c", 3, 1, F(1, 3), F(-1, 3)),
    ("L", 1, 2, F(-1, 2), F(-1)),
    ("e^c", 1, 1, F(1), F(1)),
    ("nu^c", 1, 1, F(0), F(1)),
]

def _table(gen):
    return (
        sum(c * i * Y ** 3 for _, c, i, Y, _ in gen),
        sum(c * i * Y for _, c, i, Y, _ in gen),
        sum(i * Y for _, c, i, Y, _ in gen if c == 3),
        sum(c * Y for _, c, i, Y, _ in gen if i == 2),
        sum(c * i * B ** 3 for _, c, i, _, B in gen),
        sum(c * i * B for _, c, i, _, B in gen),
    )

def test_derived_16_identically_zero():
    assert _table(GEN16) == (0, 0, 0, 0, 0, 0)

def test_imported_15_carries_the_BL_pair():
    g15 = [f for f in GEN16 if f[0] != "nu^c"]
    t = _table(g15)
    assert t[:4] == (0, 0, 0, 0)
    assert (t[4], t[5]) == (-1, -1)      # nu^c is the last cancellation

def test_z6_congruence_unique_4_3():
    sols = []
    for a in range(6):
        for b in range(6):
            ok = True
            for name, c, i, Y, _ in GEN16:
                t = 1 if (c == 3 and name == "Q") else (2 if c == 3 else 0)
                d = 1 if i == 2 else 0
                if (6 * Y - (a * t + b * d)) % 6 != 0:
                    ok = False
                    break
            if ok:
                sols.append((a, b))
    assert sols == [(4, 3)]
