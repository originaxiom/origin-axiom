"""B229 -- the TCI's two 3d-3d bulk realizations are DIFFERENT 3-manifolds (3-manifold form of B228).
Nothing to CLAIMS.md.

Load-bearing locks (exact):
  - TCI is the same CFT both ways: c_ordinary(M(4,5)) = c_super(SM(3,5)) = 7/10.
  - ordinary recipe (det 1): TCI -> S^2(3,4,5), |H_1|=83 (reproduces B227).
  - super recipe (det 2): TCI -> S^2(3,3,5), |H_1|=66.
  - DIFFERENT bulk: base orbifold and |H_1| both differ.
"""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B229_tci_super_seifert"))
from super_seifert import c_ordinary, c_super, seifert, h1_order, find_RS  # noqa: E402


def test_same_cft_both_labels():
    assert c_ordinary(5, 4) == c_super(5, 3) == Fr(7, 10)   # TCI = M(4,5) = SM(3,5)


def test_determinant_is_su2_level():
    # ordinary recipe uses SU(2)_1 (det 1); super uses SU(2)_2 (det 2)
    R, S = find_RS(5, 4, 1)
    assert 5 * S - 4 * R == 1
    R, S = find_RS(5, 3, 2)
    assert 5 * S - 3 * R == 2


def test_ordinary_tci_seifert():
    fib, cone = seifert(5, 4, 1)
    assert tuple(sorted(cone)) == (3, 4, 5)
    assert h1_order(fib) == 83                               # = B227's TCI / 40a1-side value


def test_super_tci_seifert():
    fib, cone = seifert(5, 3, 2)
    assert tuple(sorted(cone)) == (3, 3, 5)
    assert h1_order(fib) == 66


def test_one_cft_two_bulk_manifolds():
    _, cone_o = seifert(5, 4, 1)
    _, cone_s = seifert(5, 3, 2)
    fib_o, _ = seifert(5, 4, 1)
    fib_s, _ = seifert(5, 3, 2)
    assert tuple(sorted(cone_o)) != tuple(sorted(cone_s))    # different base orbifold
    assert h1_order(fib_o) != h1_order(fib_s)                # different |H_1|


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
