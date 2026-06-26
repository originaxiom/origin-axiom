"""B215 -- the class-field period law (the conductor-split closed form). Nothing to CLAIMS.md.

Load-bearing locks:
 - P(gamma) = lcm(t-2,t+2)/d, d = max{d'|f : gamma==+-I mod d'}, EXACT for conductor f in {2,3,4}.
 - the f=8 boundary: scalar-mod-4 class matches (d=4), but an order-2-mod-2 class splits by 2
   (period 40) while the scalar law predicts 80 -> the named open boundary.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B215_class_field_period_law"))
from period_class import (gmat, conductor, d_scalar, predicted_period, period, lcm)  # noqa: E402


def test_class_field_law_conductor_2_3_4():
    # P = lcm(t-2,t+2)/d_scalar, exact for f in {2,3,4} -- one principal + one split class each
    cases = [
        ([(4, 1)], 1),                 # t=6 f=2: not scalar mod2 -> d=1, period 8
        ([(2, 2)], 2),                 # t=6 f=2: ==I mod2 -> d=2, period 4
        ([(5, 1)], 1),                 # t=7 f=3: d=1, period 45
        ([(1, 1), (1, 1)], 3),         # t=7 f=3: ==-I mod3 -> d=3, period 15
    ]
    for w, dexp in cases:
        g = gmat(w); t = int(g.trace()); f = conductor(t * t - 4)
        assert d_scalar(g, f) == dexp, (w, d_scalar(g, f))
        assert period(w, maxk=70) == predicted_period(g) == lcm(t - 2, t + 2) // dexp, w


def test_d_divides_conductor():
    for w in [[(4, 1)], [(2, 2)], [(5, 1)], [(1, 1), (1, 1)], [(4, 4)], [(1, 2), (1, 3)]]:
        g = gmat(w); t = int(g.trace()); f = conductor(t * t - 4)
        assert f % d_scalar(g, f) == 0                      # d | f always


def test_f8_boundary():
    # t=18 (f=8): the scalar-mod-4 class matches the law; an order-2-mod-2 class does NOT (boundary)
    g_scal = gmat([(4, 4)])                                 # (17,4,4,1) == I mod 4 -> d=4
    assert d_scalar(g_scal, 8) == 4
    assert period([(4, 4)], maxk=60) == predicted_period(g_scal) == 20   # law holds on the scalar class
    g_ord2 = gmat([(1, 2), (1, 3)])                         # (15,4,11,3), not scalar mod 2
    assert d_scalar(g_ord2, 8) == 1                         # scalar law predicts d=1 (period 80) ...
    assert period([(1, 2), (1, 3)], maxk=70) == 40          # ... but the true period is 40 (d=2): BOUNDARY
    assert predicted_period(g_ord2) == 80 != 40             # the law is incomplete at f=8


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
