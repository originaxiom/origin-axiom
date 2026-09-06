"""Post-failure export controls; old failed source and test remain intact."""
import json

import numpy as np
import pytest

from reports.physical_bridge_2026_09_05 import g2_isolation_audit as original
from reports.physical_bridge_2026_09_05 import g2_isolation_export as repaired


def test_nested_numpy_keys_and_values_are_preserved():
    source = {np.int64(3): [np.int64(53), np.float64(1.25), np.bool_(True)]}
    assert repaired.native(source) == {3: [53, 1.25, True]}
    assert json.loads(json.dumps(repaired.native(source))) == {"3": [53, 1.25, True]}


def test_original_serialization_failure_is_still_visible():
    with pytest.raises(TypeError, match="keys must be"):
        json.dumps(original.analyze(), allow_nan=False)


def test_complete_live_result_round_trip_preserves_every_census():
    output = json.loads(json.dumps(repaired.analyze(), allow_nan=False))
    assert output["actual_B1084_group"]["nonidentity_element_census"] == {"3": 53, "1": 42}
    assert output["actual_B1084_group"]["A1_E6_intersection_dimensions"] == [1]*30
    assert output["exact_G2_counterexample"]["nonidentity_fixed_dimensions"] == [3]*7
    assert len(output["exact_G2_counterexample"]["subgroups"]) == 16
    assert output["actual_B1084_group"]["exact_common_fixed_dimension"] == 0
    assert output["upstream_B1259_selftest"]["returncode"] == 0


def test_unsupported_or_nonfinite_data_is_not_silently_stringified():
    with pytest.raises(TypeError, match="Unsupported export type"):
        repaired.native(object())
    with pytest.raises(ValueError):
        json.dumps(repaired.native({np.int64(1): np.float64(np.nan)}), allow_nan=False)
