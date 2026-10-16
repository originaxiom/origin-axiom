"""Live full-presentation tests; never a substitute for physical global admission."""
import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/surface_based_gauge_2026_10_14'
def mod(name):
    sp=importlib.util.spec_from_file_location('surface_based_gauge_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
N,R=mod('probe'),mod('reference')

def test_post_hoc_integer_inverse_stays_exact():
    assert N.phase_inverse(1,1).is_Integer
    assert N.phase_inverse(-1,1).is_Integer
    assert N.phase_inverse(1,1)==1 and N.phase_inverse(-1,1)==-1

def test_two_exact_methods_and_complete_records():
    a,b=N.run(),R.run()
    assert a['all_passed'] and b['all_passed'] and a['checks'] and b['checks']
    assert a['records']==b['records']

def test_full_based_presentation_and_actual_inner_kernel():
    c=N.run()['checks']
    for n in ['native word braid XYX','native word braid YZY','native word distant commute',
              'native word centre identity','actual based a inverse recovered','actual based b recovered',
              'gauge braid XYX','gauge braid YZY','gauge distant commute','actual SU6 centre retained']:
        assert c[n]

def test_non_scalar_repair_has_discriminating_controls():
    c=N.run()['checks']
    assert c['paired centre trivial on all240 roots'] and c['unrepaired weak identity fails']
    assert c['wrong weak angle rejected'] and c['paper middle is not literal Ri']
    assert c['specified weak root actually broken'] and c['weak Cartan actually survives']

def test_phase_census_keeps_all_directions_and_zero_phase():
    r=N.run()['records']
    assert sum(n for _,row in r['even_phase_populations'] for _,n in row)==136
    assert sum(n for _,row in r['odd_phase_populations'] for _,n in row)==112
    assert all(row[0][1]==0 for _,row in r['odd_phase_populations'])
    assert N.run()['checks']['zero phase remains in even sector']

def test_prices_the_actual_unbroken_roster():
    r=N.run()['records']
    assert r['complete_based_gauge_invariant_dimension']==r['family_adjoint_invariants']+8+r['weak_invariants']+6*r['family_symmetric_invariants']
    assert r['diagonal_block_hypercharge_invariants']<=2
