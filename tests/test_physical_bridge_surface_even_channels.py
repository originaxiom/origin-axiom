"""Actual high-frequency companion profile and canonical-channel bound."""
import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/surface_even_channels_2026_10_14'
def mod(name):
    sp=importlib.util.spec_from_file_location('even_channels_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
N,R=mod('probe'),mod('reference')

def test_separate_exact_live_records():
    a,b=N.run(),R.run()
    assert a['all_passed'] and b['all_passed'] and a['checks'] and b['checks']
    assert a['records']==b['records']

def test_actual_coefficient_and_inverse_deck_convention():
    c=N.run()['checks']
    for j in (0,1):
        assert c[f'actual Lie field {j}'] and c[f'actual puncture even {j}']
        assert all(c[f'actual character {j} {x}'] for x in ['A','B','T'])
        assert c[f'actual cusp sign cancellation {j}']

def test_profile_retains_full_mixed_spin_term():
    c=N.run()['checks']
    assert c['joint spin projector'] and c['profile internal chirality retained']
    assert c['exact full high frequency zero profile']
    assert c['omitted mixed term fails this profile'] and c['reversed mixed term fails this profile']

def test_norm_and_escape_are_not_a_fixed_frequency_inference():
    c=N.run()['checks']
    assert c['exact whole line profile norm'] and c['exact normalized low height tail']
    assert c['cutoff residual tends to zero at growing frequency']
    assert c['norm escapes every fixed compact height']
    assert c['fixed frequency positive threshold is not zero profile exclusion']

def test_R_bound_keeps_derivatives_and_entire_cross_term():
    c=N.run()['checks']
    assert c['radial derivative twist anticommutes'] and c['all vertical frequencies twist anticommutes']
    assert c['full mixed twist cross term'] and c['twist square is positive']
    assert N.run()['records']['uniform_squared_bounds_ell_one'][1]==['canonical0',3,16]

def test_constant_asymptotic_spectrum_is_a_separate_limit():
    c=N.run()['checks'];r=R.run()['checks']
    assert c['whole fixed frequency asymptotic polynomial']
    assert all(v for k,v in r.items() if k.startswith('full asymptotic squared matrix '))
    assert c['nonabelian parent direction not identically decoupled']
