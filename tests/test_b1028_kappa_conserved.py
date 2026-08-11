"""B1028 locks — the four stratum kappa-laws, and kappa=2 as the absolutely conserved locus."""
import importlib.util, pathlib
import sympy as sp

_R = pathlib.Path(__file__).resolve().parents[1]
_S = importlib.util.spec_from_file_location(
    "b1028", _R / "frontier" / "B1028_kappa_absolutely_conserved" / "compute.py")
c = importlib.util.module_from_spec(_S); _S.loader.exec_module(c)
x, y, z, K = c.x, c.y, c.z, c.KAPPA


def test_stratum1_Aut_conserves_kappa():
    assert sp.simplify(c.push((z, x, x*z - y)) - K) == 0


def test_stratum2_law():
    T = (x**2 - 2, y**2 - 2, x*y*z - x**2 - y**2 + 2)
    assert sp.simplify(c.push(T) - 2 - (K - 2) * x**2 * y**2) == 0


def test_stratum3_thue_morse_law():
    T = (z, z, x*y*z - x**2 - y**2 + 2)
    assert sp.simplify(c.push(T) - 2 - (K - 2) * (x**2 + y**2 - x*y*z)) == 0


def test_stratum4_noninjective_image_is_inside_kappa_2():
    """phi(ab) = w^2, so z' = z^2 - 2 by Cayley-Hamilton. A first pass used z' = z and FAILED --
    the check caught the modelling error, not the law."""
    assert sp.simplify(c.push((z, z, z**2 - 2)) - 2) == 0
    assert sp.simplify(c.push((z, z, z)) - 2) != 0      # the wrong model, pinned as wrong


def test_kappa_minus_2_divides_every_stratum_law():
    """The unifying statement: kappa-2 is what every endomorphism scales."""
    for T in ((z, x, x*z - y),
              (x**2 - 2, y**2 - 2, x*y*z - x**2 - y**2 + 2),
              (z, z, x*y*z - x**2 - y**2 + 2)):
        assert sp.simplify(sp.rem(sp.expand(c.push(T) - 2), sp.expand(K - 2), x)) == 0


def test_the_criterion_can_fail():
    """MB12: a wrong cofactor must be rejected."""
    T = (x**2 - 2, y**2 - 2, x*y*z - x**2 - y**2 + 2)
    assert sp.simplify(c.push(T) - 2 - (K - 2) * x**2) != 0


def test_all_cell_checks_pass():
    assert all(v["pass"] for v in c.R["checks"].values())
