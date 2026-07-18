"""B258 locks -- the two-ended unification: H27 (the two quadratic fields co-appear only at m=1, the
metallic-AND-arithmetic object) + the quantum mirror (Kashaev -> Vol = hyperbolic/E6 end; golden-root WRT ->
Q(sqrt5) = spherical/E8 end). FIREWALLED (arithmetic/quantum/geometry, not physics); nothing to CLAIMS.md."""
import importlib.util
import pathlib
import mpmath as mp
import pytest

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B258_two_ended_unification" / "two_ended_unification.py"
_spec = importlib.util.spec_from_file_location("b258", _PATH)
b258 = importlib.util.module_from_spec(_spec)
# E12 (module-level-dps sweep): two_ended_unification sets mp.mp.dps=30 at
# module level (its import-time values are computed under the dps it sets
# itself); restore the entry dps after the collection-time import so the
# assignment cannot leak into later-collected modules. (MASKED in the ordered
# cell-5 scan behind earlier identical-value leaks; found by the isolated-
# import rescan of this sweep.)
_saved_dps = mp.mp.dps
_spec.loader.exec_module(b258)
mp.mp.dps = _saved_dps


@pytest.fixture(autouse=True)
def _dps_30():
    # E12 repair (the b204 pattern): pin the module's declared dps=30 per test
    # instead of trusting the collection-time global to survive.
    saved = mp.mp.dps
    mp.mp.dps = 30
    yield
    mp.mp.dps = saved


def test_h27_both_fields_quadratic_only_at_m1():
    assert b258.both_fields_quadratic(1)                  # metallic AND arithmetic = figure-eight
    assert not b258.both_fields_quadratic(2)              # silver: trace field degree 8
    assert not b258.both_fields_quadratic(3)              # bronze: trace field degree 8


def test_trace_field_degrees():
    # figure-eight trace field is quadratic (Q(sqrt-3)); silver/bronze are degree 8 (non-arithmetic)
    assert b258.TRACE_FIELD_DEGREE == {1: 2, 2: 8, 3: 8}
    assert all(b258.discriminant_field_is_quadratic(m) for m in (1, 2, 3))


def test_kashaev_growth_recovers_volume():
    # the quantum invariant (large-color) sees the hyperbolic/E6 end: corrected growth -> Vol(4_1)
    assert abs(b258.kashaev_growth_corrected(800) - b258.VOL_4_1) < mp.mpf("0.005")
    assert abs(b258.kashaev_growth_corrected(1600) - b258.VOL_4_1) < mp.mpf("0.005")
    # monotone improvement toward Vol
    assert abs(b258.kashaev_growth_corrected(1600) - b258.VOL_4_1) < abs(b258.kashaev_growth_corrected(400) - b258.VOL_4_1)
