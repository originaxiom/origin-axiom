"""Live exact extension, literal full boundary counts and cubic regressions."""
import importlib.util
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT/'reports/physical_bridge_2026_09_05/silver_cover_extension_2026_10_13'


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, PACKET/file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


n = load('extension_live_native', 'probe.py')
f = load('extension_live_fraction', 'reference.py')


def test_literal_four_slots_and_independent_whole_polynomials():
    native, fraction = n.run(), f.run()
    assert native['records'] == fraction['records']
    assert {key: value['rank'] for key, value in native['records']['slots'].items()} == {
        'W': 10, 'Wdual': 10, 'F': 20, 'Fdual': 20}


def test_all_filtration_dimensions_and_actual_duals():
    slots = n.run()['records']['slots']
    assert {key: value['filtration_sizes'] for key, value in slots.items()} == {
        'W': [8, 2], 'Wdual': [2, 8], 'F': [12, 8], 'Fdual': [8, 12]}
    _, _, w, _, _, _, _ = n.cy.literal()
    y = {g: s.zeros(5) for g in 'abt'}
    y['a'][0, 4] = 1
    primal = n.letters(w, y)
    dual = n.letters({g: n.cy.inv(v).T for g, v in w.items()}, {g: -v.T for g, v in y.items()})
    assert all(n.zero(dual[g]-primal[g.upper()].T) for g in 'abt')
    assert not n.zero(dual['a']-primal['a'])


def test_wrong_inverse_and_frozen_parity_are_distinguishable():
    rep = {g: s.eye(5) for g in 'abt'}
    y = {g: s.zeros(5) for g in 'abt'}
    y['a'][0, 4] = 1
    maps = n.letters(rep, y)
    assert n.zero(n.mm(maps['a'], maps['A'])-s.eye(10))
    assert not n.zero(n.mm(maps['a'], maps['A'].subs(n.q, -n.q))-s.eye(10))
    parity = s.diag(s.eye(5), -s.eye(5))
    assert not n.zero(parity*maps['a']-maps['a']*parity)


def test_phase_minor_needs_filtration_not_an_integer_scan():
    q, r = n.q, n.r
    good = s.Matrix([[r-1, q], [0, r-1]])
    bad = s.Matrix([[r-1, q], [q, r-1]])
    # Two sheets of a rank1+rank1 filtered coefficient.
    doubled_good = s.diag(good, good)
    doubled_bad = s.diag(bad, bad)
    assert n.filtration_check(doubled_good, [0], [1], 2)
    assert not n.filtration_check(doubled_bad, [0], [1], 2)
    assert s.diff(good.det(), q) == 0
    assert s.expand(s.diff(bad.det(), q)) == -2*q


def test_exterior_before_induction_and_untruncated_nonnil_control():
    instrument, _, w, _, _, _, _ = n.cy.literal()
    assert instrument.wedge(s.diag(w['a'], w['a'])).rows == 45
    assert n.run()['records']['slots']['F']['rank'] == 20
    a = s.zeros(5); a[0, 4] = 1
    b = a.T
    assert not n.zero(n.mm(s.eye(5)+n.q*a, s.eye(5)+n.q*b).applyfunc(lambda v: s.expand(v).coeff(n.q, 2)))


def test_fixed_full_boundary_retains_both_degrees_not_index_alone():
    for value in f.run()['records']['boundary_counts'].values():
        assert value['H'] == [0, 3, 0, 0]
        assert value['dual_H'] == [0, 0, 3, 0]
        assert value['rank']-value['dual_rank'] == 3
        assert value['plane_dimension']+value['dual_plane_dimension'] in (8, 12)


def test_complete_charged_tensor_keeps_cancellation_and_nonzero_terms():
    result = n.cubic.run()
    assert sum(len(item['polynomials']) for item in result['channels'].values()) == 81
    assert result['channel_classifications'] == {'QdL': 'NONZERO', 'eLL': 'CANCELLATION', 'udd': 'CANCELLATION'}
    for key in ('eLL', 'udd'):
        item = result['channels'][key]
        assert all(s.sympify(poly) == 0 for poly in item['polynomials'])
        assert any(s.sympify(poly) != 0 for poly in item['first_terms']+item['second_terms'])


def test_fixed_holomorphic_tensor_does_not_fix_kinetic_normalization():
    q = s.Symbol('real_deformation')
    tensor = s.Rational(2)
    norm0 = s.Rational(1)
    normq = 1+q*q
    assert tensor/norm0 != tensor/normq
    assert s.diff(tensor, q) == 0
    assert s.diff(tensor/normq, q) != 0
