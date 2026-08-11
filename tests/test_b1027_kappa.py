"""B1027 locks — the two banked normalisations of kappa are ONE law, and kappa=2 is the free chain.

Recomputes the mathematics (WORKING_RULES rule 7). The reconciliation is the point: B160 pins
kappa = 2 + lambda^2 and B505 pins kappa - 2 = 4*lambda^2, and a restoration quoting either
without the other would bank a wrong constant.
"""
import importlib.util, pathlib
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_S = importlib.util.spec_from_file_location(
    "b1027", _ROOT / "frontier" / "B1027_kappa_two_faces" / "compute.py")
c = importlib.util.module_from_spec(_S); _S.loader.exec_module(c)


def test_B505_normalisation():
    assert sp.simplify(c.kappa_of(c.lam) - 2 - 4 * c.lam**2) == 0


def test_B160_normalisation():
    assert sp.simplify(c.kappa_of(c.lam / 2) - 2 - c.lam**2) == 0


def test_the_two_are_one_law_under_the_halving():
    assert sp.simplify(c.kappa_of(c.lam).subs(c.lam, c.lam / 2) - c.kappa_of(c.lam / 2)) == 0


def test_kappa_does_not_depend_on_the_spectral_parameter():
    """kappa is a property of the COUPLING, not of where in the spectrum you look."""
    assert sp.simplify(sp.diff(c.kappa_of(c.lam), c.E)) == 0


def test_kappa_equals_two_iff_the_chain_is_free():
    assert sp.solve(sp.Eq(c.kappa_of(c.lam), 2), c.lam) == [0]


def test_at_kappa_two_the_two_letters_collapse_to_one_matrix():
    """The alphabet carries no information at the 'nothing' point."""
    E = c.E
    assert sp.Matrix([[E - 0, -1], [1, 0]]) == sp.Matrix([[E + 0, -1], [1, 0]])
    assert sp.simplify(c.kappa_of(0) - 2) == 0


def test_the_B36_B148_route_reproduces_B160():
    """kappa = 4*I_FV + 2 (B148) composed with I_FV = lambda^2/4 on the Fibonacci line (B36)."""
    E, lam = c.E, c.lam
    x, y, z = (E - lam) / 2, E / 2, sp.Integer(1)
    I = sp.simplify(x**2 + y**2 + z**2 - 2*x*y*z - 1)
    assert sp.simplify(I - lam**2 / 4) == 0
    assert sp.simplify((4 * I + 2) - c.kappa_of(lam / 2)) == 0


def test_the_criterion_can_fail():
    """MB12: a wrong constant must be rejected, or these locks assert nothing."""
    assert sp.simplify(c.kappa_of(c.lam) - 2 - 3 * c.lam**2) != 0
    assert sp.simplify(c.kappa_of(c.lam / 2) - 2 - 4 * c.lam**2) != 0


def test_every_check_in_the_cell_passes():
    assert all(v["pass"] for v in c.R["checks"].values())
