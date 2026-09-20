"""R39 exact controls; finite tests do not certify the global authored proof."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

SPEC = importlib.util.spec_from_file_location(
    'physical_bridge_parent_background', Path(__file__).resolve().parents[1]/
    'reports/physical_bridge_2026_09_05/parent_background.py')
pb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pb)


def test_entire_248_joint_roster_and_actual_spinor():
    b = pb.branching()
    assert sum(b['actual'].values()) == 248
    assert b['actual'] == b['expected'] and b['actual_spinor']
    assert b['actual'][(0,)*8] == 8
    assert len(b['d5']) == 40 and len(b['spin']) == 16 and len(b['vector']) == 10


def test_defining_map_and_faithful_center_not_dimension_only():
    b = pb.branching()
    assert b['all_a3_roots'] and b['charges'] == [3, -1, -1, -1]
    assert b['weight_gram'] == sp.eye(4)-sp.ones(4)/4
    assert b['center_phases'] == [1, sp.I, -1, -sp.I]
    assert b['wrong'] != b['actual'] and sum(b['wrong'].values()) == 248
    assert sp.expand(b['adjoint_trace']-60*b['defining_trace']) == 0
    assert b['trace_ratio'] == 60


def test_complete_symbolic_curvature_and_both_mutants():
    f = pb.curvature_blocks()
    assert pb.zero(f['residual']) and f['trace'] == 0
    assert not pb.zero(f['omitted_neutral_row'])
    assert not pb.zero(f['reversed_charge_column'])


def test_block_instrument_rejects_nontraceless_or_wrong_shapes():
    with pytest.raises(ValueError):
        pb.block(0, sp.zeros(1, 2), sp.zeros(3, 1), sp.zeros(3))
    with pytest.raises(ValueError):
        pb.block(0, sp.zeros(1, 3), sp.zeros(3, 1), sp.eye(3))
    with pytest.raises(ValueError):
        pb.gram_residual(sp.eye(2))


def test_whole_moment_and_F01_source_sign_conversion():
    m = pb.restricted_moment()
    assert pb.zero(m['residual']) and pb.zero(m['source_conversion'])
    assert sp.expand(m['projector_pairing']+2*sp.trace(m['gram'])) == 0
    assert m['scalar_source_pairing'] == 0
    assert m['H_source_pairing'] == 12


def test_Gram_rank_is_not_the_number_of_nonzero_entries():
    for a in (sp.diag(1, 0, 0), sp.diag(1, 1, 0), sp.ones(3)):
        assert not pb.zero(pb.gram_residual(a))
    assert pb.zero(pb.gram_residual(sp.eye(3)))
    assert pb.zero(pb.gram_residual(sp.zeros(3)))
    assert not pb.zero(pb.gram_residual(sp.diag(1, 2, 3)))


def test_Maurer_Cartan_precursor_and_full_flatness():
    g = pb.geometric_controls()
    assert g['precursor'] == g['precursor_expected']
    assert all(pb.zero(a) for a in g['sl2_residuals']+g['curvature'])
    changed = list(pb.connection())
    changed[2] *= 2
    assert any(not pb.zero(a) for a in pb.curvature(tuple(changed)))


def test_all_real_PDEs_and_Hermitian_conventions():
    g = pb.geometric_controls()
    H = pb.generators()[2]
    assert g['hermitian_phi'] and g['hermitian_W']
    assert g['divergence'] == -2*H and g['commutator'] == 2*H
    assert pb.zero(g['moment'])
    assert all(pb.zero(a) for a in g['real_flatness']+g['higgs_derivative'])


def test_ablation_of_commutator_or_curved_metric_fails():
    g = pb.geometric_controls()
    assert not pb.zero(g['divergence'])
    assert not pb.zero(g['flat_metric_moment'])
    assert any(not pb.zero(a) for a in g['gauge_curvature'])


def test_central_projection_is_zero_while_full_dropped_background_fails():
    g = pb.geometric_controls()
    assert g['dropped_central'] == 0
    assert g['dropped_moment'] == sp.diag(0, -4, 2, 2)
    assert any(not pb.zero(a) for a in g['dropped_curvature'])


def test_positive_norm_and_exact_cusp_tail_not_volume_divergence():
    area, Z, tail = pb.cusp_norm()
    assert pb.geometric_controls()['phi_norm'] == 15
    assert tail == 15*area/(2*Z**2)
    assert sp.diff(tail, Z) == -15*area/Z**3
    assert sp.limit(tail, Z, sp.oo) == 0


def test_exterior_instrument_known_scalar_action_and_bracket():
    E, F, H = pb.generators()
    assert pb.exterior_action(sp.eye(4)) == 2*sp.eye(6)
    assert pb.comm(pb.exterior_action(E), pb.exterior_action(F)) == pb.exterior_action(H)


def test_complete_invariant_spaces_and_ten_extra_generators():
    inv = pb.invariants()
    assert inv['kernel_dimensions'] == [0, 1, 0]
    assert len(inv['wedge_kernels']) == 1
    assert any(v != 0 for v in inv['wedge_kernels'][0])
    assert all(pb.zero(a*inv['wedge_kernels'][0]) for a in inv['wedge_actions'])
    assert inv['unbroken_dimension'] == 55


def test_unbroken_algebra_entire_B5_roots_and_cartan_not_55_alone():
    inv = pb.invariants()
    roots = set(inv['unbroken_weights'])-{(0,)*5}
    assert roots == inv['B5_roots'] and len(roots) == 50
    assert inv['unbroken_weights'][(0,)*5] == 5
    assert {sum(t*t for t in r) for r in roots} == {1, 2}
    assert sum(sum(t*t for t in r) == 1 for r in roots) == 10
    assert inv['cartan'] == sp.Matrix([[2, -1, 0, 0, 0], [-1, 2, -1, 0, 0],
                                       [0, -1, 2, -1, 0], [0, 0, -1, 2, -1],
                                       [0, 0, 0, -2, 2]])
    assert inv['cartan'].det() == 2
    assert pb.branching()['d5'] != roots


def test_explicit_unitary_duality_of_connection_and_positive_adjoint():
    inv = pb.invariants()
    J = inv['J']
    assert J.T == -J and J.H*J == sp.eye(4)
    assert all(pb.zero(a) for a in inv['invariance']+inv['flat_intertwiner']+inv['adjoint_intertwiner'])
    assert inv['bilinear_dimension'] == 1
    assert inv['with_U_bilinear_dimension'] == 0
    assert not pb.zero(pb.U.T*J+J*pb.U)


def test_local_invariant_line_does_not_split_the_physical_operator():
    g = pb.geometric_controls()
    assert g['flag_preserved'] and not g['adjoint_flag_preserved']
    assert g['laplacian_mixing'] == sp.Matrix([0, sp.sqrt(3)*pb.z, 0, 0])
    flat = (sp.zeros(4),)*3
    section = pb.x*sp.eye(4)[:, 0]
    assert pb.zero(pb.laplacian_zero(flat, section))
