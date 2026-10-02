"""R80 conditional math; two-sided source/gap/flux controls, not SM proof."""
import ast
import importlib.util
from pathlib import Path
import pytest

BASE = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05'


def load(name):
    spec = importlib.util.spec_from_file_location(name, BASE / (name+'.py'))
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize('n', range(2, 7))
def test_all_proper_flag_blocks(n):
    m = load('source_profile'); z = m.generic(n)
    mu = z*z.H-z.H*z
    for k in range(1, n):
        p = m.projector(n, k); xi = n*p-k*m.s.eye(n)
        assert m.clean(m.s.trace(xi*mu)-n*(m.norm(z[:k,k:])-m.norm(z[k:,:k]))) == 0


def test_whole_transport_and_source_sign_not_selected_diagonal():
    out = load('source_profile').block_controls()
    assert all(out['checks'].values())
    assert out['symbolic_block_cases'] == 15


def test_actual_longitude_controls_parallel_endomorphism_not_all_matter():
    out = load('source_profile').peripheral_controls()
    assert all(out['checks'].values())
    assert out['checks']['q_one_gap_fails']


def test_actual_boundary_solution_prevents_boundaryless_false_kill():
    out = load('source_profile').boundary_controls()
    assert all(out['checks'].values())
    assert out['bulk_norm'] == '6/5' and out['outward_flux'] == '-6/5'


def test_rectangular_relation_keeps_both_currents():
    out = load('source_profile').relation_controls()
    assert all(out['checks'].values())
    assert out['rectangular_projector_cases'] == 34


def test_independent_entry_controls_are_live():
    out = load('source_profile_control').run()
    assert out['all_checks_pass']
    assert out['block_cases'] == 165 and out['edge_cases'] == 196
    assert out['checks']['full_lower_match'] and out['checks']['upper_wrong_sign']


def test_independent_and_native_boundary_values_agree():
    native = load('source_profile').boundary_controls()
    other = load('source_profile_control').run()
    assert native['bulk_norm'] == other['bulk_norm']
    assert native['outward_flux'] == other['outward_flux']


def test_independent_import_firewall():
    tree = ast.parse((BASE / 'source_profile_control.py').read_text())
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(a.name.split('.')[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.add(node.module.split('.')[0])
    assert imports == {'fractions', 'json'}
    assert not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                   and n.func.id in {'__import__', 'exec', 'eval'} for n in ast.walk(tree))
