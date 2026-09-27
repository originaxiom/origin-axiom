"""Rerun every frozen original test plus two-field adapter controls."""
from pathlib import Path
import importlib.util
import pytest
import sympy as s


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,Path(__file__).with_name(file))
    out=importlib.util.module_from_spec(spec); spec.loader.exec_module(out)
    return out


original=load('f15_original_tests','test_verify.py')
correction=load('f15_test_adapter','verify_v2.py')
original.v=correction.v
globals().update({name:getattr(original,name) for name in dir(original) if name.startswith('test_')})


@pytest.mark.parametrize('d',[2,3])
def test_typed_field_zero_guard(d):
    v=correction.v; k=s.QQ.algebraic_field(s.sqrt(d),s.I)
    with pytest.raises(ValueError): correction.original_coords(v.zero(4,4,k))
    assert correction.coords(v.zero(4,4,k)).is_zero_matrix
    with pytest.raises(ValueError): correction.coords(v.eye(4,k))
    for b in v.basis(k): assert (v.uncoords(correction.coords(b))-b).is_zero_matrix
