import json
import pytest
import sympy as sp
import verify_admission_v2 as v


def test_exact_integer_serializer():
    assert json.loads(v.exact_json({"a": [sp.Integer(-1), sp.Integer(3)]})) == {"a": [-1, 3]}


def test_no_silent_lossy_conversion():
    with pytest.raises(TypeError):
        v.exact_json(sp.Rational(1, 3))


def test_actual_topology_output():
    x = json.loads(v.exact_json(v.original.topology_control()))
    assert x["lift_obstruction_class_count"] == 5
