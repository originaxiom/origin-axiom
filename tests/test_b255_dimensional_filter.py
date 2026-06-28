"""B255 locks -- the dimensional filter: the tetrahedron (d=3) is the unique regular simplex whose McKay image is
an exceptional group with a complex fundamental (E6). FIREWALLED (simplices/McKay/rep theory, not physics); nothing
to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B255_dimensional_filter" / "dimensional_filter.py"
_spec = importlib.util.spec_from_file_location("b255", _PATH)
b255 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b255)


def test_simplex_so3_subgroup_only_d234():
    assert b255.is_so3_subgroup(2) and b255.is_so3_subgroup(3) and b255.is_so3_subgroup(4)
    assert not any(b255.is_so3_subgroup(d) for d in range(5, 12))


def test_mckay_images():
    assert b255.simplex_mckay_image(3)[2] == "E6"        # tetrahedron -> 2T -> E6
    assert b255.simplex_mckay_image(4)[2] == "E8"        # 5-cell -> 2I -> E8
    assert b255.simplex_mckay_image(5) is None           # d=5: no McKay


def test_unique_complex_fundamental_simplex_is_tetrahedron():
    assert b255.unique_complex_fundamental_simplex() == [3]
    assert b255.EXCEPTIONAL_COMPLEX_FUND["E6"]
    assert not b255.EXCEPTIONAL_COMPLEX_FUND["E8"]
