"""B1029 locks — HCF(Q(sqrt-15)) = Q(sqrt5, sqrt-3): the seam is the ends' class field."""
import importlib.util, pathlib
import sympy as sp

_R = pathlib.Path(__file__).resolve().parents[1]
_S = importlib.util.spec_from_file_location(
    "b1029", _R / "frontier" / "B1029_seam_class_field" / "compute.py")
c = importlib.util.module_from_spec(_S); _S.loader.exec_module(c)


def test_the_seam_is_the_product_of_the_two_ends():
    assert sp.simplify(sp.sqrt(5) * sp.sqrt(-3) - sp.sqrt(-15)) == 0


def test_the_two_ends_are_the_seams_prime_discriminants():
    assert (c.disc(5), c.disc(-3)) == (5, -3)
    assert c.disc(5) * c.disc(-3) == c.disc(-15) == -15


def test_class_number_two_by_counting_reduced_forms():
    assert c.reduced_forms(-15) == [(1, 1, 4), (2, 1, 2)]


def test_genus_field_equals_hilbert_class_field_here():
    """t = 2 prime discriminants gives genus degree 2^(t-1) = 2 = h, so they coincide."""
    assert 2 ** (2 - 1) == len(c.reduced_forms(-15))


def test_the_compositum_has_degree_four_over_Q():
    t = sp.Symbol("t")
    assert sp.degree(sp.minimal_polynomial(sp.sqrt(5) + sp.sqrt(-3), t), t) == 4


def test_the_criterion_can_fail():
    """MB12: a discriminant with a different factorisation must not pass the same reasoning."""
    # disc -20 = 5 * (-4): also two prime discriminants, but h(-20) = 2 as well -- so use a case
    # where the genus/class counts genuinely differ: disc -23 has h = 3, an ODD class number, so
    # its genus field (trivial, t = 1) is strictly smaller than its Hilbert class field.
    assert len(c.reduced_forms(-23)) == 3
    assert 2 ** (1 - 1) != len(c.reduced_forms(-23))


def test_all_cell_checks_pass():
    assert all(v["pass"] for v in c.R["checks"].values())
