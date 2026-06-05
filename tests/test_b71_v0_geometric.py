"""B71 (P2, V48) -- the geometric V0 component has no tidy A-variety monomial relation."""
import importlib.util
import pathlib

import numpy as np

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b71_v0", _ROOT / "frontier" / "B71_sl3_apoly" / "v0_geometric.py")
v0 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v0)


def test_v0_meridian_commutes_but_no_monomial_relation():
    data, commute = v0.v0_peripheral_data()
    assert len(data) >= 8
    assert np.median(commute) < 1e-6                       # mu commutes with [A,B] (V46)
    assert v0.smallest_monomial_spread(data) > 1e-2        # no clean monomial M^a L^b is constant
