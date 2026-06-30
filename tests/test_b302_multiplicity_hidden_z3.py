"""B302 lock -- the multiplicity thread: the generation ℤ/3 is the figure-eight's HIDDEN SYMMETRY (relational, not
internal). The object has no order-3 (Sym=D4 order 8, knot group torsion-free), but the commensurator PGL(2,O_-3) does
(Neumann-Reid; m004 = the arithmetic ℚ(√−3) knot, B282). The figure-eight is an index-12 cover of the order-3 minimal
orbifold. Explains B298 (degree-2 obstruction = torsion-free); locates the multiplicity in the relation, does NOT
derive 3 generations (firewalled). Nothing to CLAIMS.md.
(SnapPy+Sage reproducer: sage-python frontier/B302_multiplicity_hidden_z3/multiplicity_hidden_z3.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B302_multiplicity_hidden_z3" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b302", _PATH)
b302 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b302)


def test_object_has_no_order3():
    assert b302.SYM_ORDER == 8                            # D4 = 2^3, no order-3
    assert b302.KNOT_GROUP_TORSION_FREE


def test_commensurator_has_order3():
    assert b302.order3_matrix_check()                    # [[0,-1],[1,-1]] order 3 (re-verified sympy)
    assert b302.eisenstein_unit_order3()                 # ω order 3
    assert b302.COMMENSURATOR_HAS_ORDER3


def test_cover_index_12():
    assert abs(b302.cover_index() - 12) < 0.5            # Riley; figure-eight index 12 in PSL(2,O_-3)


def test_generation_z3_is_relational_firewall():
    assert b302.GENERATION_Z3_IS_HIDDEN_SYMMETRY
    assert b302.EXPLAINS_B298                            # degree-2 obstruction = torsion-free knot group
    assert b302.DERIVES_THREE_GENERATIONS is False
    assert b302.verdict()
