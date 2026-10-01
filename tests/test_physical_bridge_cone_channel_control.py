import importlib.util
from pathlib import Path

path=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/cone_channel_control.py'
spec=importlib.util.spec_from_file_location('r71_cone_channel_control',path)
C=importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)

def test_complete_actual_charge_split_and_nonideal_bracket():
    out=C.charge_controls()
    assert out['dimensions']==[9,3,3] and out['full_form_matrix_dimension']==128
    assert all(out['checks'].values())

def test_full_limiting_windows_depend_on_declared_metric():
    out=C.window_controls()
    assert out['limiting_angular_dimensions']==[36,60,300]
    assert all(out['checks'].values())

def test_scalar_generator_control_and_independent_determinant():
    assert all(C.scalar_controls()['checks'].values())
    assert not C.limit_window(C.s.Rational(64,3),1,4)['inside']

def test_actual_logarithmic_schur_matches_independent_blocks():
    out=C.schur_controls()
    assert out['critical_limiting_dimension']==36
    assert out['checks']['four_analytic_blocks'] and out['checks']['actual_formal_second_order']
    assert out['checks']['missing_Schur_fails'] and out['checks']['missing_radial_K_fails']

def test_logarithmic_spectrum_Green_pairing_and_exact_Z_scope():
    out=C.schur_controls()
    assert out['exact_reducing_traces_previously_proved']==4
    assert out['checks']['B_Gamma_paired'] and out['checks']['B_Gram_Hermitian']
    assert out['checks']['complete_B_polynomial'] and out['checks']['only_Z_zeros']
    assert out['checks']['principal_Casimir'] and out['checks']['actual_radial_frame_derivative_order']

def test_L2_logarithmic_control_is_not_graph_admission():
    assert all(C.integration_controls()['checks'].values())

def test_all_two_sided_frozen_control_identities():
    out=C.run()
    assert set(out['groups'])=={'charge','window','scalar','schur','integration'}
    assert out['all_checks_pass'] and len(out['checks'])==60

