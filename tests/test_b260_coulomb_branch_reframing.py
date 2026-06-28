"""B260 locks -- the Coulomb-branch reframing of wall #1: the figure-eight A-polynomial is the Coulomb branch of
T[4_1] (M,L = fugacities, not gauge holonomies), dissolving the false obstruction while NOT building a bridge.
FIREWALLED (3d-3d / quantum topology, not physics); nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B260_coulomb_branch_reframing" / "coulomb_branch.py"
_spec = importlib.util.spec_from_file_location("b260", _PATH)
b260 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b260)


def test_a_polynomial_complete_structure():
    # meridian parabolic M=1 -> A=(L+1)^2 -> longitude L=-1 (the complete hyperbolic structure)
    L = sp.symbols("L")
    assert b260.complete_structure_longitude() == (L + 1) ** 2


def test_boundary_slopes_are_figure_eight():
    # the Newton polygon must contain the +-4 boundary-slope corners that identify 4_1's A-polynomial
    verts = b260.newton_polygon_slopes()
    assert (0, 4) in verts and (2, 4) in verts and (1, 8) in verts and (1, 0) in verts


def test_reframing_is_honest_both_halves():
    r = b260.REFRAMING
    assert r["dissolves_false_obstruction"] is True          # SL(2,C) is a Coulomb coordinate
    assert r["wall1_is_obstruction_to_physics"] is False     # true theorem, wrong question
    assert r["manufactures_e6_gauge_group"] is False         # T[4_1] abelian; no bridge built
    assert r["improves_honesty_not_proximity"] is True
    assert r["quantizes_to_colored_jones"] is True           # AJ through-line to the quantum face (B258)
