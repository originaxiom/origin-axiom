"""B298 lock -- the figure-eight does NOT force three generations (the degree-2 obstruction). Cross-chat convergent
(Chat-1 + Chat-2 + this session): Q(sqrt-3) is degree 2 (Galois Z/2) -> matter multiplicities 1 or 2, never 3; seven
routes all give 1 or 2; 3-fold covers of m004 = 1. The cubic-carrier conjecture: 3 generations need a CUBIC trace
field. Sharpens B292/B282. FIREWALLED; nothing to CLAIMS.md.
(SnapPy reproducer: sage-python frontier/B298_generation_obstruction/generation_obstruction.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B298_generation_obstruction" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b298", _PATH)
b298 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b298)


def test_trace_field_is_degree2_galois_z2():
    assert b298.trace_field_is_degree2()                 # Q(sqrt-3), disc -3
    assert b298.TRACE_FIELD_DEGREE == 2 and b298.GALOIS_GROUP_ORDER == 2


def test_all_seven_routes_give_1_or_2():
    assert b298.all_routes_give_1_or_2()
    assert b298.THREE_FOLD_COVER_COUNT == 1              # SnapPy: exactly one, H1 = Z/4+Z/4+Z


def test_does_not_force_three_generations():
    assert b298.FORCES_THREE_GENERATIONS is False
    assert b298.THREE_IS_A_VALUE_NOT_A_MULTIPLICITY     # 3 = a value (dim/level/trace/prime/center), not a mult


def test_cubic_carrier_conjecture_firewall():
    assert "CUBIC" in b298.CUBIC_CARRIER_CONJECTURE
    assert b298.DERIVES_SM_VALUES is False
    assert b298.verdict()
