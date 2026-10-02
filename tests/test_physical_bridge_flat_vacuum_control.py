import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/flat_vacuum_control.py'
SPEC=importlib.util.spec_from_file_location('r76_flat_control',P)
C=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(C)


def test_nonzero_cusp_primitive_and_same_nonsplit_class():
    out=C.run()
    assert out['primitive']==['1','0','0','0']
    assert out['all_checks_pass'] and out['passed']==out['total']==12
