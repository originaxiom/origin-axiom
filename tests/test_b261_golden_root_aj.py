"""B261 locks -- the golden-root AJ operator: at q=zeta_5 the colored-Jones recursion degenerates to a finite
antiperiod-5 one ([N]J_N = {1,-2,-2,1,0|...}, extending B240), and the Coulomb branch at the golden meridian lands
the longitude in Q(sqrt5) (L+1/L = -phi^3). The two ends are two regimes of one recursion. FIREWALLED; nothing to
CLAIMS.md."""
import importlib.util
import pathlib

import mpmath as mp
import pytest
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B261_golden_root_aj" / "golden_root_aj.py"
_spec = importlib.util.spec_from_file_location("b261", _PATH)
b261 = importlib.util.module_from_spec(_spec)
# E12 (module-level-dps sweep): golden_root_aj sets mp.mp.dps=50 at module level;
# pytest runs this import at COLLECTION time, so without the save/restore the
# assignment leaks into every later-collected module's import and (if last in
# sorted order) into every runtime test. The module computes its own import-time
# values under the dps it sets itself, so restoring afterwards changes nothing
# for b261 and un-leaks the global.
_saved_dps = mp.mp.dps
_spec.loader.exec_module(b261)
mp.mp.dps = _saved_dps


@pytest.fixture(autouse=True)
def _dps_50():
    # E12 repair (the b204 pattern): golden_root_sequence computes the colored
    # Jones at q=zeta_5 in mpmath at RUNTIME and rounds to integers; pin the
    # dps=50 the module declares, per test, instead of trusting the collection-
    # time global to survive.
    saved = mp.mp.dps
    mp.mp.dps = 50
    yield
    mp.mp.dps = saved


def test_golden_root_periodicity_extends_b240():
    seq = b261.golden_root_sequence(15)
    assert seq[:4] == [1, -2, -2, 1]                       # the B240 seed
    assert all(seq[N + 5] == -seq[N] for N in range(10))   # antiperiod 5 (the recursion degenerates)
    assert all(seq[N + 10] == seq[N] for N in range(5))    # period 10


def test_golden_meridian_longitude_in_q_sqrt5():
    LpL = b261.golden_meridian_longitude()
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(LpL - (-(2 + sp.sqrt(5)))) == 0     # L + 1/L = -(2+sqrt5)
    assert sp.simplify(LpL + phi**3) == 0                  # = -phi^3, in Q(sqrt5)
