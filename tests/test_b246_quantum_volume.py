"""B246 locks -- the figure-eight symmetric large-color VC gives the COMPLEMENT volume 2.0299 for BOTH SU(2) and
SU(3) (A=q^N washes out), NOT the SL(3) geometric 8.1195; the fixed-A generalized volume is A-dependent and nonzero.
Firewall-clean."""
import importlib.util
import pathlib
import cmath

import mpmath as mp
import pytest

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B246_quantum_volume" / "quantum_volume.py"
_spec = importlib.util.spec_from_file_location("b246", _PATH)
b246 = importlib.util.module_from_spec(_spec)
# E12 (module-level-dps sweep): quantum_volume sets mp.mp.dps=30 at module level
# (its import-time constants are computed under the dps it sets itself); restore
# the entry dps after the collection-time import so the assignment cannot leak
# into later-collected modules. (This file was MASKED in the original cell-5
# scan: the b204 leak had already set 30 before it, so no transition showed.)
_saved_dps = mp.mp.dps
_spec.loader.exec_module(b246)
mp.mp.dps = _saved_dps


@pytest.fixture(autouse=True)
def _dps_30():
    # E12 repair (the b204 pattern): vc_growth/fixedA_volume compute in mpmath
    # at RUNTIME; pin the module's declared dps=30 per test instead of trusting
    # the collection-time global to survive.
    saved = mp.mp.dps
    mp.mp.dps = 30
    yield
    mp.mp.dps = saved


def test_formula_validated_fundamental():
    import mpmath as mp
    A, q = mp.e ** (mp.mpc(0, 0.53)), mp.e ** (mp.mpc(0, 0.37))
    assert abs(complex(b246.H_red(1, A, q)) - (complex(A) ** 2 + complex(A) ** -2 + 1
               - complex(q) ** 2 - complex(q) ** -2)) < 1e-12


def test_su2_and_su3_both_head_to_complement_volume():
    # both descend toward ~2.03, SU(3) lags SU(2) (slower), and BOTH are far below 4*Vol=8.12 and 2*Vol=4.06
    g2_200, g2_400 = b246.vc_growth(200, 2), b246.vc_growth(400, 2)
    g3_200, g3_400 = b246.vc_growth(200, 3), b246.vc_growth(400, 3)
    assert g2_400 < g2_200 and g3_400 < g3_200            # monotone descending
    assert g3_400 > g2_400                                 # SU(3) lags (slower convergence)
    for g in (g2_400, g3_400):
        assert 2.0 < g < 2.6                              # heading to 2.03, nowhere near 4.06 or 8.12
    # recorded extrapolations: both the complement volume, not the SL(3) geometric
    assert abs(b246.EXTRAP_SU2 - b246.VOL_4_1) < 5e-3
    assert abs(b246.EXTRAP_SU3 - b246.VOL_4_1) < 5e-3
    assert abs(b246.EXTRAP_SU3 - 4 * b246.VOL_4_1) > 6.0  # decisively NOT 8.1195


def test_fixedA_generalized_volume_is_A_dependent():
    assert abs(b246.fixedA_volume(400, 1.0)) < 1e-2       # A=1: no growth
    v15, v20, v30 = (b246.fixedA_volume(400, a) for a in (1.5, 2.0, 3.0))
    assert 0 < v15 < v20 < v30                            # strictly increasing, continuous in A (no special 8.12)
