"""R77 live mathematics, including independent producer and fail controls."""
import ast
import importlib.util
from pathlib import Path


BASE = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05'


def load(name):
    spec = importlib.util.spec_from_file_location(name, BASE / (name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_native_complete_image_and_both_signs():
    m = load('source_core')
    target = m.generic_source(5)
    assert m.moment(m.source_fields(target)) == target
    assert m.moment(m.source_fields(-target)) == -target


def test_traceful_and_nonhermitian_are_rejected():
    m = load('source_core')
    bad = m.s.zeros(5)
    bad[0, 1] = 1
    for target in (m.s.eye(5), bad):
        rejected = False
        try:
            m.source_fields(target)
        except ValueError:
            rejected = True
        assert rejected


def test_coupled_auxiliary_and_field_variations():
    m = load('source_core')
    out = m.action_controls()
    assert all(out['checks'].values())
    assert m.s.Rational(out['source_second_variation']) > 0


def test_current_partition_is_square_weighted():
    out = load('source_core').localization_controls()
    assert all(out['checks'].values())


def test_profile_price_and_gradient_live_control():
    out = load('source_core').profile_controls()
    assert all(out['checks'].values())
    assert out['kinetic_norm'] == '1/15'
    assert out['gradient_norm'] == '2/3'


def test_structure_duality_not_untransported_sign_choice():
    out = load('source_core').duality_controls()
    assert all(out['checks'].values())


def test_independent_row_reduction_covers_every_basis_direction():
    m = load('source_core_control')
    answer = m.run()
    assert answer['rank'] == 24
    assert all(m.moment(m.fields_for(b)) == b for b in m.hermitian_basis())
    assert answer['all_checks_pass']


def test_independent_quadratic_extraction_has_opposite_outcome():
    m = load('source_core_control')
    answer = m.run()
    assert m.F(answer['tail_coefficients'][2]) == 0
    assert m.F(answer['tail_coefficients'][4]) > 0
    assert m.F(answer['gradient_coefficients'][2]) == m.F(2, 3)
    assert m.coefficients(lambda t: 4*t*t) == tuple(map(m.F, (0, 0, 4, 0, 0)))


def test_independent_import_firewall():
    tree = ast.parse((BASE / 'source_core_control.py').read_text())
    modules = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(q.name.split('.')[0] for q in node.names)
        elif isinstance(node, ast.ImportFrom):
            modules.add(node.module.split('.')[0])
    assert modules == {'fractions', 'functools', 'json'}
    assert not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                   and n.func.id in {'__import__', 'eval', 'exec'} for n in ast.walk(tree))


def test_producers_agree_on_normalized_profile_controls():
    native = load('source_core').profile_controls()
    independent = load('source_core_control').run()
    assert native['kinetic_norm'] == '1/15'
    assert native['gradient_norm'] == independent['gradient_coefficients'][2]
