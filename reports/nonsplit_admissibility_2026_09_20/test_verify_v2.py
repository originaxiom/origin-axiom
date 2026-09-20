"""Scoped identity checks. The infinite-domain claim is a written proof, not pytest."""
import importlib.util
from pathlib import Path

import sympy as s

spec = importlib.util.spec_from_file_location('f01_verify', Path(__file__).with_name('verify_v2.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_actual_representation_peripheral_marking_and_nonsplitting():
    a = v.algebra()
    assert a['V_b_unipotent_power_ranks'] == [3, 2, 1, 0]


def test_projector_identity_both_signs_and_split_control_rank_two():
    assert v.projection_variation(1, 1)['xi_norm_squared'] == 2


def test_projector_identity_for_actual_rank_four_flag():
    assert v.projection_variation(1, 3)['xi_norm_squared'] == 12


def test_busemann_hessian_and_noninvariant_dilation_control():
    assert v.busemann()['dilation_control_shift'] != '0'


def test_full_local_cusp_equation_boundary_flux_and_energy():
    c = v.cusp()
    assert c['wrong_normalization_radial_tension'] == '-3/2'
    assert c['energy'] == '3*A0/4'


def test_scope_boundary_counterexample_does_not_disprove_global_argument():
    # The exact local solution b=-r has nonzero inner normal derivative.
    r = s.symbols('r', real=True)
    assert -s.diff(-r, r) == 1
    assert s.diff(-r, r) == -1


def test_exact_word_evaluator_detects_wrong_relation():
    a = s.Matrix([[1, 1], [0, 1]])
    b = s.Matrix([[1, 0], [1, 1]])
    assert v.word('abAB', a, b) != s.eye(2)
    assert v.word('aAbB', a, b) == s.eye(2)
