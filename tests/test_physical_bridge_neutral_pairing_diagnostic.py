"""Separately sealed R47 diagnostic; does not overwrite the original failure."""
import importlib.util
from pathlib import Path

import sympy as s

path = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/neutral_pairing_diagnostic.py'
spec = importlib.util.spec_from_file_location('r47_pairing_diagnostic', path)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_exact_predicate_has_both_zero_and_nonzero_controls():
    assert v.exact_zero(s.Mul(s.Integer(0), s.I, evaluate=False))
    assert not v.exact_zero(s.I/v.q)
    assert not v.exact_zero((v.q*v.q+1)/(v.q+1))


def test_all_eight_literal_inverse_dual_identities_over_exact_field():
    rows = v.cases()
    assert len(rows) == 8
    assert all(row['exact_field_zero'] for row in rows)
    assert any(not row['structural_zero'] for row in rows)


def test_wrong_witness_and_wrong_dual_phase_are_rejected():
    checks = v.controls()
    assert checks['wrong_witness_rejected']
    assert checks['wrong_dual_phase_rejected']


def test_differentiated_identity_and_omitted_compensator_control():
    checks = v.controls()
    assert checks['differentiated_identity']
    assert checks['missing_compensator_rejected']
