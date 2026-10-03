"""R81 compact-boundary comparator, not the imported PDE theorem."""
import importlib.util
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]/'reports'/'physical_bridge_2026_09_05'


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


native = load('dirichlet_admission')
reference = load('dirichlet_admission_control')


def test_native_checks():
    assert all(native.checks().values())


def test_separate_reference():
    assert all(reference.checks().values())


def test_periodic_loop_is_genuinely_nonsplit():
    d = native.data()
    assert (d['L']-sp.eye(2)).nullspace() == [sp.Matrix([1, 0])]
    assert d['L'] != sp.eye(2)


def test_transport_sign():
    d = native.data()
    assert d['N'].exp() == d['L']
    assert (-d['N']).exp() != d['L']


def test_entire_flat_and_moment_matrices():
    d = native.data()
    assert d['curvature'] == sp.zeros(2)
    assert d['moment'] == sp.zeros(2)


def test_wrong_radial_sign_is_rejected():
    d = native.data()
    assert d['wrong_curvature'] != sp.zeros(2)
    assert d['wrong_moment'] != sp.zeros(2)


def test_actual_outward_flux_not_zero():
    d = native.data()
    assert d['bulk'] == 2 and d['flux'] == -2
    assert 2*d['bulk']+2*d['flux'] == 0
    assert 2*d['bulk'] != 0


def test_positive_compact_metric():
    d = native.data()
    assert d['H'].det() == 1
    assert d['H'].subs(d['s'], d['a']) == sp.diag(sp.sqrt(2), 1/sp.sqrt(2))


def test_pole_is_not_a_complete_extension():
    rows = native.checks()
    assert rows['pole_bulk_diverges']
    assert rows['pole_metric_diverges'] and rows['pole_inverse_diverges']


def test_opposite_split_control():
    assert reference.checks()['split_control']
    assert reference.comm(reference.mat(0, 0, 0, 0), reference.mat(0, 0, 0, 0)) == reference.mat(0, 0, 0, 0)
