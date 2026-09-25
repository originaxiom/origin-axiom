"""F14 corrected producer, every original test retained unchanged."""
from pathlib import Path
import importlib.util
import sympy as s


def load(name,filename):
    spec=importlib.util.spec_from_file_location(name,Path(__file__).with_name(filename))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


original=load('f14_original_tests','test_verify.py')
correction=load('f14_corrected_adapter','verify_v2.py')
original.v=correction.v
for name,value in vars(original).items():
    if name.startswith('test_'):
        globals()[name]=value


def test_adapter_mutability_and_no_original_test_removed():
    v=correction.v
    eq=v.intertwiner_equations((s.eye(2),),(s.eye(2),))
    assert isinstance(eq,s.MutableDenseMatrix)
    assert v.field.kernel(eq,v.q*v.q-14*v.q+1).cols==4
    old={name for name in vars(original) if name.startswith('test_')}
    assert old<={name for name in globals() if name.startswith('test_')}


def test_rational_field_nullspace_rows_convention():
    q=correction.v.q
    matrix=s.Matrix([[q,1],[q*q,q]])
    rows=matrix.to_DM().convert_to(s.QQ.frac_field(q)).nullspace(divide_last=True).to_Matrix()
    assert rows.shape==(1,2)
    assert matrix*rows.T==s.zeros(2,1)
    assert s.eye(2).to_DM().convert_to(s.QQ.frac_field(q)).nullspace().shape==(0,2)
