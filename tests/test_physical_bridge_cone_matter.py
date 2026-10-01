import importlib.util
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/cone_matter.py'
spec=importlib.util.spec_from_file_location('r74_matter',p)
C=importlib.util.module_from_spec(spec);spec.loader.exec_module(C)

def test_actual_exterior_coefficient_and_twist_not_dimension_analogy():
    out=C.coefficient_controls()
    assert out['coefficient_dimension']==6 and all(out['checks'].values())

def test_changing_matter_operator_requires_radial_and_nilpotent_terms():
    out=C.actual_controls()
    assert out['form_dimension']==48 and all(out['checks'].values())

def test_supplied_aspect_changes_window_without_changing_acyclicity():
    out=C.limiting_controls()
    assert out['critical_limiting_dimension']==24 and all(out['checks'].values())

def test_exact_graph_and_scalar_contraction_constants():
    out=C.contraction_controls()
    assert out['witnessed_quotient_dimension']==24 and out['scalar_seed_dimension']==6
    assert all(out['checks'].values())

def test_actual_scalar_equation_joins_separate_d_and_delta():
    assert all(C.scalar_controls()['checks'].values())

def test_nonlinear_product_norms_have_a_bad_decay_control():
    assert all(C.product_controls()['checks'].values())

def test_local_seeds_are_not_maximal_end_or_chiral_particle_count():
    out=C.contraction_controls()
    assert out['witnessed_signature']==[12,12]
    assert out['scalar_seed_dimension']<out['witnessed_signature'][0]

def test_complete_frozen_control_population():
    out=C.run()
    assert set(out['groups'])=={'coefficient','actual','limit','contraction','scalar','products'}
    assert out['all_checks_pass']
