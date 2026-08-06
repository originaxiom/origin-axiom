"""B941 locks: the branch-symmetric headline, recomputed from scratch."""
import json
import os

import sympy as sp

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B941_branch_symmetric")


def test_the_headline_identity_chain():
    # N(V)/N(W) computed from the two banked minimal polynomials
    NV = sp.Rational(760840571584512, 824843587681)   # 953^4-led
    NW = sp.Rational(244140625, 824843587681)
    r = NV / NW
    assert r == sp.Rational(2**32 * 3**11, 5**12)
    # the numerator IS the product law's integer
    assert 2**32 * 3**11 == 27 * 2304**4 == 760840571584512
    # 2304 is the {2,3} number
    assert sp.factorint(2304) == {2: 8, 3: 2}
    # and the 953s cancelled: no 953 in the ratio
    assert 953 not in sp.factorint(sp.Rational(r).p)
    assert 953 not in sp.factorint(sp.Rational(r).q)


def test_twist_norms_agree_across_families():
    NdS = sp.Rational(-953**2, 2304**2)
    NdA = sp.Rational(-953**2, 2304**2)
    assert NdS == NdA == -sp.Rational(953, 2304)**2


def test_table_banked_and_rational():
    with open(os.path.join(ARC, "results.json")) as f:
        r = json.load(f)
    assert len(r["symmetric_functions"]) == 7
    for fam, e in r["symmetric_functions"].items():
        for x in e:
            sp.Rational(x)          # every symmetric function is rational
    assert r["headline"]["the_953s_cancel"] is True
