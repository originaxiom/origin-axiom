"""Live finite safeguards; analytic domain transfer has its own stated hypotheses."""
import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/surface_odd_form_2026_10_14'
def mod(name):
    sp=importlib.util.spec_from_file_location('surface_odd_form_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
N,R=mod('probe'),mod('reference')

def test_two_exact_odd_form_methods():
    a,b=N.run(),R.run()
    assert a['all_passed'] and b['all_passed'] and a['checks'] and b['checks']
    assert a['records']==b['records']

def test_cross_form_keeps_actual_mixed_connection():
    c=N.run()['checks']
    assert c['full mixed first order coefficient E3'] and c['full mixed first order coefficient E4']
    assert c['no horizontal derivative in cross operator']
    assert c['all mixed second derivative coefficients cancel']
    assert c['omitted mixed spin term changes E3 coefficient']
    assert c['omitted mixed spin term changes E4 coefficient']

def test_transfer_uses_regular_opposite_chirality_not_half_pole_gradient():
    c=N.run()['checks']
    assert c['both cross matrices reverse vertical chirality']
    assert c['regular vertical gradient symbol exact']
    assert c['half pole derivative squared radial norm diverges']
    assert c['E3 coefficient norm exact one'] and c['E4 coefficient norm exact one']

def test_complete_odd_phase_population_not_three_labels():
    a=N.run()['records']['odd_phase_populations']
    assert len(a)==2 and all(sum(n for _,n in row)==56 for _,row in a)
    assert sum(n for _,row in a for _,n in row)==112
    assert all(r in (1,3,5,7) and n>=0 for _,row in a for r,n in row)
    assert N.run()['checks']['zero phase comparator fails confining frequency duty']

def test_R_density_and_absorption_are_not_hidden_changes():
    c=N.run()['checks']
    assert c['R line term anticommutes vertically']
    assert c['density term anticommutes vertically']
    assert c['absorption bound is an exact nonnegative square']
    assert c['literal Q8 coefficient relations retained']
    assert c['literal cusp fourth power retained']
