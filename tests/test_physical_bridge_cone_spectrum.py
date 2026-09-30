"""R63 cone operator controls; no global physical-domain certificate."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('r63', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/cone_spectrum.py')
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def test_full_operator_is_derived_from_metric_forms():
    assert all(C.metric_controls()['checks'].values())


def test_generic_symbol_and_complex_unitary_reduction():
    assert all(C.spectrum_controls()['checks'].values())


def test_critical_window_endpoints_and_link_scale():
    assert all(C.threshold_controls()['checks'].values())
    assert C.threshold_controls()['critical_counts']==[4, 4, 0, 0]


def test_fourier_bound_includes_higgs_and_connection_for_both_links():
    for kind in ('square', 'hexagonal'):
        out = C.fourier_controls(kind)
        assert all(out['checks'].values())
        assert out['nonzero_fourier_lower_bound']>s.Rational(3, 4)


def test_no_link_cohomology_is_not_no_radial_data():
    assert all(C.koszul_controls()['checks'].values())
    assert sum(bool(-s.Rational(1, 2)<x<s.Rational(1, 2)) for x in C.eigenvalues(s.Rational(5, 16)))==4


def test_fast_modes_have_separate_zero_residuals():
    rows = C.mode_controls()['rows']
    for name in ('fast1', 'fast2'):
        assert C.zero(rows[name]['d']) and C.zero(rows[name]['adjoint'])
        assert rows[name]['power']>0


def test_slow_modes_only_cancel_in_the_sum():
    rows = C.mode_controls()['rows']
    for name in ('slowEven', 'slowOdd'):
        assert not C.zero(rows[name]['d'])
        assert C.zero(rows[name]['d']+rows[name]['adjoint'])
        assert rows[name]['d_norm_coefficient']>0 and rows[name]['power']<0


def test_degree_green_form_and_local_primitive_controls():
    out = C.mode_controls()
    assert all(out['checks'].values())
    assert out['green_pairing'].det()!=0


def test_radial_unitary_transport_does_not_have_an_apex_limit():
    assert all(C.radial_gauge_controls()['checks'].values())


def test_scope_and_all_control_groups():
    with pytest.raises(ValueError):
        C.eigenvalues(-1)
    with pytest.raises(ValueError):
        C.fourier_controls('complete cusp')
    data = C.run()
    assert data['all_checks_pass'] and len(data['checks'])==69
