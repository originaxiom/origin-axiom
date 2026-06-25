"""B214 -- the general-word period law + class-field refinement + the Funar deflation. Nothing to CLAIMS.md.

Load-bearing locks (the FORMULA and the refinement, NOT the identical-trace examples):
 - P = lcm(det(g-I), det(g+I)) on the principal class (many words, incl. non-symmetric).
 - the conductor-split: at conductor f>1 the period splits (lcm/d, d|f); at f=1 it does not.
 - the deflation: M1~M2 conjugate but M0 not -> |Z|-equality is Funar, not conjugacy/'interaction'.
"""
import os
import sys
from math import gcd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B214_general_word_period_law"))
from period_law import (gmat, det_moduli, lcm, lcm_law, conductor,  # noqa: E402
                        period, conjugate)


def test_general_word_period_law_principal_class():
    # P = lcm(det(g-I), det(g+I)); fundamental-disc words are principal -> exact lcm (fast: period<=48)
    cases = [[(1, 2)], [(1, 3)], [(2, 3)], [(1, 5)], [(3, 4)], [(1, 1), (1, 2)]]
    for w in cases:
        dm, dp = det_moduli(w)
        assert period(w, maxk=70) == lcm(dm, dp), w


def test_conductor_split_refinement():
    # the NEW content: conductor f>1 -> period splits across classes by a divisor of f
    assert conductor(6 * 6 - 4) == 2 and conductor(7 * 7 - 4) == 3 and conductor(5 * 5 - 4) == 1
    # disc 32 (f=2): [(4,1)] principal (lcm), [(2,2)] split by 2
    assert period([(4, 1)], maxk=40) == lcm_law([(4, 1)])           # 8 = lcm
    assert period([(2, 2)], maxk=40) == lcm_law([(2, 2)]) // 2      # 4 = lcm/2
    # disc 45 (f=3): R^5L principal (lcm 45), (RL)^2 split by 3 (15)
    assert period([(5, 1)], maxk=80) == lcm_law([(5, 1)])           # 45 = lcm (period 45 needs maxk>=61)
    assert period([(1, 1), (1, 1)], maxk=40) == lcm_law([(1, 1), (1, 1)]) // 3   # 15 = lcm/3
    # disc 21 (f=1): both classes the same period (no split)
    assert period([(3, 1)], maxk=40) == period([(1, 3)], maxk=40) == lcm_law([(3, 1)])  # 21


def test_deflation_funar_not_conjugacy():
    # the over-read / cross-chat claim corrected: NOT all conjugate, and |Z|-equality is Funar
    M0, M1, M2 = gmat([(1, 1), (2, 2)]), gmat([(1, 2), (2, 1)]), gmat([(2, 1), (1, 2)])
    assert conjugate(M1, M2) is True              # conjugate -> same |Z| is Jeffrey's theorem
    assert conjugate(M0, M1) is False             # M0 a DIFFERENT class ...
    assert conjugate(M0, M2) is False
    assert conjugate(gmat([(1, 1), (1, 1)]), gmat([(5, 1)])) is False   # (RL)^2 != R^5L (tr 7)


def test_funar_same_Z_different_class():
    # M0 (different class from M1) nonetheless has identical |Z| at several levels -> Funar
    from period_law import Zabs
    M0w, M1w = [(1, 1), (2, 2)], [(1, 2), (2, 1)]
    assert not conjugate(gmat(M0w), gmat(M1w))           # non-conjugate ...
    for k in (8, 12, 17, 23):
        assert abs(Zabs(M0w, k) - Zabs(M1w, k)) < 1e-9   # ... yet identical WRT (Funar)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
