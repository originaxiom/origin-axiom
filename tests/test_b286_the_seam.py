"""B286 lock -- THE SEAM: the figure-eight is an open object; closing it (Dehn filling = the interaction with 'the
nothing') breaks its symmetries and supplies chirality, the CP sign, scale, and the clock AT THE BOUNDARY. Corrects
P011's Curie wall (a closed-system theorem misapplied to an open object). FIREWALLED; nothing to CLAIMS.md.
(SnapPy reproducer: sage-python frontier/B286_the_seam/seam_fillings.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B286_the_seam" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b286", _PATH)
b286 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b286)


def test_forced_finite_selection_set():
    assert b286.EXCEPTIONAL_COUNT == 10                       # {-4..4} + infinity (Thurston)


def test_closing_breaks_amphichirality():
    assert b286.CUSPED_CS == 0.0                              # cusped object amphichiral
    assert all(b286.is_chiral(cs) for cs in b286.FILLING_CS.values())   # every generic filling chiral


def test_wall_at_closure_not_object():
    assert b286.WALL_IS_AT_THE_CLOSURE_NOT_THE_OBJECT
    assert b286.DERIVES_SM_VALUES is False                    # firewall: locates ingredients, not values
    assert b286.verdict()
