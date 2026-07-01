"""B316 lock -- H32: does the arithmetic ladder extend past {sqrt-3, sqrt5} to Q(sqrt-7)? The unimodular monodromy
imaginary discs floor at {-4 (Q(i)), -3 (Q(sqrt-3))} (the amphichiral fields). Q(sqrt-7) (disc -7) PASSES the trace-1
congruence (-7==1 mod 4) but is BELOW the floor -> unreachable by any unimodular monodromy. Yet Q(sqrt-7) IS in the
object's arithmetic -- the CHIRAL pair RRL/RLL (arithmetic bundles, B147). So the ladder does NOT extend to -7; -7 is
the CHIRALITY field, reached by breaking amphichirality, not by the metallic ladder. H32's prediction (-7 appears) is
confirmed; the mechanism is chirality. Firewalled; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B316_sqrt7_chirality_field" / "sqrt7_chirality_field.py"
_spec = importlib.util.spec_from_file_location("b316", _PATH)
b316 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b316)


def test_imaginary_ladder_floors_at_minus_4():
    assert b316.imaginary_unimodular_discs() == [-4, -3]           # Q(i), Q(sqrt-3) -- amphichiral
    assert b316.IMAGINARY_LADDER_FLOORS_AT_MINUS_4


def test_neg7_permitted_by_congruence_forbidden_by_floor():
    assert b316.neg7_passes_congruence()                           # -7 == 1 mod 4
    assert b316.neg7_below_floor()                                 # -7 < -4 -> unreachable by monodromy
    assert b316.NEG7_PERMITTED_BY_CONGRUENCE and b316.NEG7_UNREACHABLE_BY_MONODROMY


def test_neg7_is_the_chirality_field():
    assert b316.NEG7_IS_THE_CHIRALITY_FIELD                        # RRL/RLL arithmetic chiral bundles (B147)
    assert b316.LADDER_DOES_NOT_EXTEND_TO_NEG7
    assert b316.NEG7_APPEARS_PREDICTION_CONFIRMED
    assert b316.DERIVES_SM_VALUES is False
    assert b316.verdict()
