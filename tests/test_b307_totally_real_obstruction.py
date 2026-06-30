"""B307 lock -- the generation count, closed by the totally-real obstruction. THEOREM: no hyperbolic knot has a
cyclic-cubic (C3) trace field (C3 totally real; hyperbolic trace fields have a complex place). Census-confirmed
(32 cubic trace fields, all signature (1,1)=S3, 0 cyclic). So three symmetric generations are arithmetically
impossible in a single hyperbolic knot -> forced to MULTIPLICITY (B302). Unifies B298 + B302. Chat-2's 5_2
refutation verified. FIREWALLED; nothing to CLAIMS.md.
(SnapPy+Sage reproducer: sage-python frontier/B307_totally_real_obstruction/totally_real_obstruction.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B307_totally_real_obstruction" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b307", _PATH)
b307 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b307)


def test_five2_is_s3_naive_conjecture_refuted():
    assert b307.five2_is_S3()                            # x^3-x^2+1, disc -23 -> S3 -> 1+2 (Chat-2 refutation)
    assert b307.FIVE2_IS_S3_SPLITS_1PLUS2


def test_c3_totally_real_obstruction():
    assert b307.c3_samples_totally_real()                # C3 cubics are totally real (disc square, positive)
    assert b307.C3_CUBICS_ARE_TOTALLY_REAL
    assert b307.HYPERBOLIC_TRACE_FIELD_HAS_COMPLEX_PLACE


def test_census_zero_cyclic_cubics():
    assert b307.N_CYCLIC_C3 == 0                         # 0 of 32 cubic trace fields are cyclic
    assert set(b307.CUBIC_SIGNATURES) == {(1, 1)}        # all S3


def test_three_generations_forced_to_multiplicity():
    assert b307.NO_HYPERBOLIC_KNOT_HAS_C3_TRACE_FIELD
    assert b307.THREE_SYMMETRIC_GENERATIONS_IMPOSSIBLE_IN_ONE_KNOT
    assert b307.GENERATIONS_FORCED_TO_MULTIPLICITY      # B302 is the only route
    assert b307.DERIVES_SM_VALUES is False
    assert b307.verdict()
