"""Live bundle/operator locks, not transcript or physical-spectrum assertions."""
import importlib.util
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]/'reports'/'physical_bridge_2026_09_05'/'surface_parent_dictionary_2026_10_13'


def module(name):
    spec=importlib.util.spec_from_file_location('surface_'+name,BASE/(name+'.py'))
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


NATIVE=module('probe')
REFERENCE=module('reference')


def test_independent_whole_records_and_live_predicates():
    a,b=NATIVE.run(),REFERENCE.run()
    assert a['checks'] and b['checks'] and a['all_passed'] and b['all_passed']
    assert a['records']==b['records']


def test_actual_holomorphic_metric_not_period_density():
    c=NATIVE.run()['checks']
    assert c['actual holomorphic real Jacobian']
    assert c['canonical norm from all inverse metric entries']
    assert c['real period density is not holomorphic determinant']


def test_full_form_connection_and_nonzero_twist():
    c=NATIVE.run()['checks']
    assert all(c[f'whole exterior connection agrees {j}'] for j in range(4))
    assert all(c[f'whole Dolbeault Clifford symbol {j}'] for j in range(4))
    assert c['canonical constant vacuum solves local operator']
    assert c['ordinary constant vacuum is not canonical']
    assert c['wrong twist sign rejected']


def test_full_mixed_curvature_not_mass_by_dimension():
    c=NATIVE.run()['checks']
    assert c['dropping mixed term changes canonical vacuum']
    assert all(c[f'canonical full Lichnerowicz coefficient {j}'] for j in range(15))


def test_actual_eight_dimensional_weyl_operator_and_companions():
    c=NATIVE.run()['checks']
    assert c['physical Weyl grading is actual tensor map']
    assert c['internal Euler block not a copied form operator']
    assert c['credited full248 companion roster'] and c['all branching blocks including dual']


def test_domain_admission_is_not_unchanged_index():
    c=NATIVE.run()['checks']
    assert c['selfadjoint bounded difference'] and c['exact bound rather than a vanished perturbation']
    assert all(c[f'critical trace preserved rank {j}'] for j in range(7))
    assert c['index control actual initial zero profile']
    assert c['index control actual bounded-shift zero profile']
    assert c['index control crosses asymptotic threshold']


def test_R_line_and_gauge_generator_cannot_be_identified_globally():
    c=NATIVE.run()['checks']
    assert c['every Cartan has traceless full adjoint action']
    assert c['nonzero scalar identity is not full E8 adjoint']
    assert c['a proper root sector may have genuine charge']
    assert c['omitted conjugate changes full charge trace']
    assert c['cusp unit and geometric twist kept separate']
    assert c['integer flux cannot simply be relabelled']


def test_flat_and_wrong_operator_controls_are_live():
    a,b=NATIVE.run()['checks'],REFERENCE.run()['checks']
    assert a['flat Kahler connection control'] and b['flat metric has no canonical twist']
    assert b['missing mixed term retained as failure'] and b['wrong twist retained as failure']
