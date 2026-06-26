"""B228 -- the mechanism behind golden's SUSY-uniqueness: the ordinary/super coset coincidence at SU(2)_3.
Nothing to CLAIMS.md.

Load-bearing locks (exact rational):
  - the two GKO coset families reproduce the ordinary M(m,m+1) and N=1 super SM(m') central charges.
  - the ordinary coset == the super coset ONLY at (m,m')=(4,3) = TCI, denominator SU(2)_3 (golden) -- unique.
  - among metallic chains, only m=1 (golden) has GKO denominator SU(2)_3.
"""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B228_golden_susy_coset_mechanism"))
from coset_coincidence import (  # noqa: E402
    c_ordinary, c_super, c_ordinary_formula, c_super_formula,
    ordinary_coset, super_coset, coincidences,
)


def test_coset_central_charges():
    assert all(c_ordinary(m) == c_ordinary_formula(m) for m in range(3, 20))
    assert all(c_super(mp) == c_super_formula(mp) for mp in range(2, 20))
    assert c_ordinary(4) == c_super(3) == Fr(7, 10)         # TCI both ways


def test_unique_ordinary_super_coincidence_at_golden():
    hits = coincidences(80)
    assert hits == [(4, 3)]                                  # UNIQUE: the TCI
    # denominator level = 3 = the golden SU(2)_3
    assert ordinary_coset(4) == super_coset(3)
    assert ordinary_coset(4)[1] == 3


def test_tci_cosets_are_identical():
    # ordinary (SU(2)_2 x SU(2)_1)/SU(2)_3 == super (SU(2)_1 x SU(2)_2)/SU(2)_3 (same multiset + denominator)
    assert ordinary_coset(4)[0] == super_coset(3)[0] == frozenset([1, 2])


def test_only_golden_metallic_chain_is_super():
    # metallic chain m -> M(m^2+3, m^2+4), GKO denominator SU(2)_{m^2+2}; coincidence needs SU(2)_3
    golden = [m for m in range(1, 30) if m * m + 2 == 3]
    assert golden == [1]


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
