"""B269 locks -- T[4_1] Rungs 2 (cusp Weyl Z/2 exact A-poly symmetry; flavor=O(2) not SU(2)) + 3 (state-integral
saddle z=e^{i pi/3} -> Vol=2.0299, B250). FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

import mpmath as mp
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B269_t41_rungs_2_3" / "t41_rungs_2_3.py"
_spec = importlib.util.spec_from_file_location("b269", _PATH)
b269 = importlib.util.module_from_spec(_spec)
# E12 (module-level-dps sweep): t41_rungs_2_3 sets mp.mp.dps=30 at module level
# (its import-time GEOMETRIC_SHAPE is computed under that dps, which the module
# sets itself); restore the entry dps after the collection-time import so the
# assignment cannot leak into later-collected modules.
_saved_dps = mp.mp.dps
_spec.loader.exec_module(b269)
mp.mp.dps = _saved_dps

import pytest  # noqa: E402


@pytest.fixture(autouse=True)
def _dps_30():
    # E12 repair (the b204 pattern): complex_volume_from_saddle computes at
    # RUNTIME and the GEOMETRIC_SHAPE comparison asserts at 1e-25; pin the
    # module's declared dps=30 per test instead of trusting the collection-time
    # global to survive.
    saved = mp.mp.dps
    mp.mp.dps = 30
    yield
    mp.mp.dps = saved


def test_rung2_cusp_weyl_symmetry():
    # the meridian Weyl Z/2 (M,L)->(1/M,1/L) is an exact symmetry of the figure-eight A-polynomial
    assert b269.cusp_weyl_invariant()
    L = sp.Symbol("L")
    assert b269.complete_structure_longitude() == (L + 1)**2   # complete/amphichiral, double root L=-1


def test_rung3_saddle_reproduces_complex_volume():
    # state-integral saddle = regular ideal tetrahedron e^{i pi/3} -> Vol(4_1)=2.0299 (B250)
    assert abs(b269.complex_volume_from_saddle() - mp.mpf("2.0298832128")) < 1e-9


def test_saddle_shape_is_ramified_prime_center():
    # the saddle shape is e^{i pi/3} = Riley t (B264) = the center reduced mod (sqrt-3) to make 2T (B266)
    assert abs(b269.GEOMETRIC_SHAPE - mp.e ** (1j * mp.pi / 3)) < 1e-25
