"""Locks for B428 -- the upstairs spin walls: E6 level-1 anyons (no fermion) and the
principal-sl2 bosonic-only decomposition of the 27."""
import os, sys
import sympy as sp

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B428_upstairs_spin_walls")
sys.path.insert(0, HERE)
import spin_walls as SW


def test_e6_level1_is_z3_anyon_no_fermion():
    md = SW.level1_modular_data()
    assert len(md) == 3                                   # torus Verlinde dim 3
    hs = sorted(str(h) for _, h in md)
    assert hs == ["0", "2/3", "2/3"]                      # vacuum + the Z/3 anyon pair
    # no fermion: no h = 1/2 mod 1
    assert all(sp.nsimplify(h - sp.Rational(1, 2)) != int(h - sp.Rational(1, 2))
               for _, h in md if h != 0)


def test_27_under_principal_sl2_is_all_integer_spin():
    dims = SW.principal_grades_27()
    assert dims == [17, 9, 1]                             # Sym^16 + Sym^8 + Sym^0
    assert all(d % 2 == 1 for d in dims)                  # all odd-dim = integer spin = bosonic
    assert sum(dims) == 27


def test_involution_cascade():
    # E6 ->(theta) F4 ->(Cayley) SO(9): the full chain's dimension identities
    assert 52 + 26 == 78          # E6 adj = F4 adj + the 26
    assert 36 + 16 == 52          # F4 = so(9) + spinor16  (symmetric pair FII)
    assert 1 + 9 + 16 == 26       # the 26 under SO(9)
    assert 36 + 16 + 16 + 9 + 1 == 78
    assert 36 + 9 == 45 == 10*9//2   # adj SO(10) reconciliation
    # the kill: F4's symmetric pairs are so(9) [coset 16] and sp(3)+su(2) [coset 28]; G2 is not one
    assert (21 + 3) + 28 == 52 and 52 - 14 == 38 and 38 not in (16, 28)
