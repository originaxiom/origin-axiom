import json

from reports.physical_bridge_2026_09_05 import vacuum_orientation as o


def test_competing_minimum_is_not_sm_selection():
    r = o.analyze()
    assert r["potential_numerical"] < 1e-25
    assert r["zero_adjoint_potential_control"] > 0
    assert r["su5_roots_with_zero_charge"] == 0
    assert r["compact_unbroken_dimension"] == 4
    assert r["reference_Y_unbroken_dimension"] == 12
    assert r["not_gauge_equivalent_to_Y"]
    assert json.loads(json.dumps(r, allow_nan=False)) == r
