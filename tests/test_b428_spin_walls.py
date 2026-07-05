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
