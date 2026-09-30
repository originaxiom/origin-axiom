"""Nonzero and deliberately wrong cubic controls, separately sealed."""
import importlib.util
from pathlib import Path

p=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/cover_action_cubic_control.py'
spec=importlib.util.spec_from_file_location('r58_cubic_control',p)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


def test_nonzero_tensor_and_wrong_sheet_merge():
    d=m.run()
    assert d['all_checks_pass'] and d['passed']==d['total']==5
    assert d['sheet_cubic']==d['transported_cubic']==12
    assert d['wrong_merged_cubic']==108
    assert d['wedge_coefficient']==36
    assert not d['physical_coupling_predicted']


def test_wedge_is_alternating_and_zero_control_remains():
    h=m.s.diag(1,-1); e=m.s.Matrix([[0,1],[0,0]]); f=e.T
    assert m.wedge_coefficient([h,e,f])==6
    assert m.wedge_coefficient([e,h,f])==-6
    assert m.wedge_coefficient([h,h,f])==0
