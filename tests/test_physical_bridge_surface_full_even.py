"""All regular-even phase/connection safeguards, not odd-domain certification."""
import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/surface_even_channels_2026_10_14'
def mod(name):
    sp=importlib.util.spec_from_file_location('surface_full_even_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
N,R=mod('full_even_probe'),mod('full_even_reference')

def test_two_exact_full_population_methods():
    a,b=N.run(),R.run()
    assert a['all_passed'] and b['all_passed'] and a['checks'] and b['checks']
    assert a['records']==b['records']

def test_phase_projectors_exhaust_short_periodic_not_only_fixed_vectors():
    p=N.run()['records']['short_periodic_phase_populations']
    assert sum(sum(row) for _,row in p)==82
    assert all(n>=0 for _,row in p for n in row)
    assert all(sum(row)>0 for _,row in p)
    assert N.run()['checks']['short periodic does not mean zero x phase']

def test_complete_connection_not_only_contracted_K():
    c=N.run()['checks']
    assert c['Omega1 is complete connection'] and c['Omega3 is complete connection']
    assert c['full spin contraction remains unchanged']
    assert c['Omega1 norm bound exact'] and c['Omega3 norm bound exact']

def test_uniform_strata_and_ordinary_zero_unit_control():
    c=N.run()['checks']
    assert c['short nonzero lower bound eventually grows']
    assert c['x nonzero lower bound eventually grows']
    assert c['nearest canonical bound positive']
    assert c['ordinary zero unit cannot pass last-stratum bound']

def test_actual_powers_and_conjugate_population_control():
    c=N.run()['checks']
    assert c['actual T preserves short-cycle matrix'] and c['actual T transports long-cycle matrix']
    assert c['literal fourth power is retained centre']
    assert c['omitting conjugate exterior sector changes136']
