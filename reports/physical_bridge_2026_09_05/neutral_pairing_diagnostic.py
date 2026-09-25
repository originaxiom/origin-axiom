"""R47 post-failure exact Gaussian-rational diagnostic; originals immutable."""
import importlib.util
import json
from pathlib import Path

import sympy as s

spec = importlib.util.spec_from_file_location(
    'r47_original_neutral', Path(__file__).with_name('neutral_tangent.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
q = v.q


def exact_zero(value):
    numerator, denominator = s.fraction(s.together(s.expand(value)))
    den = s.Poly(denominator, q, extension=s.I)
    if den.is_zero:
        raise ValueError('Zero denominator is not a field identity')
    return bool(s.Poly(numerator, q, extension=s.I).is_zero)


def zero_matrix(matrix):
    return all(exact_zero(value) for value in matrix)


def cases():
    witness = v.pairing_witness()
    result = []
    for label, a in zip(('m', 'n'), v.cc.prior.generators(q)):
        for phase in (s.Integer(1), s.Integer(-1), s.I, -s.I):
            twisted = phase*a
            residue = v.cc.clean(twisted.inv().T*witness-witness*twisted.inv())
            result.append({
                'generator': label, 'phase': str(phase),
                'structural_zero': residue == s.zeros(4),
                'exact_field_zero': zero_matrix(residue),
                'structurally_nonzero_entries': [str(x) for x in residue if x != 0]})
    return result


def controls():
    witness = v.pairing_witness()
    generators = v.cc.prior.generators(q)
    fake_zero = s.Mul(s.Integer(0), s.I, evaluate=False)
    wrong_witness = witness+s.eye(4)
    return {
        'unevaluated_zero_recognized': exact_zero(fake_zero),
        'nonzero_imaginary_rejected': not exact_zero(s.I/q),
        'nonzero_rational_rejected': not exact_zero((q*q+1)/(q+1)),
        'wrong_witness_rejected': any(not zero_matrix(a.T*wrong_witness-wrong_witness*a)
                                       for a in generators),
        'wrong_dual_phase_rejected': all(not zero_matrix(
            (phase*a).inv().T*witness-witness*(phase*a.inv()))
            for a in generators for phase in (s.I, -s.I)),
        'differentiated_identity': all(zero_matrix(a) for a in v.pairing_residuals()),
        'missing_compensator_rejected': any(not zero_matrix(a)
                                             for a in v.pairing_residuals(True))}


def run():
    rows = cases()
    checks = controls()
    return {'cases': rows, 'controls': checks,
            'all_exact_identities_pass': all(row['exact_field_zero'] for row in rows),
            'all_controls_pass': all(checks.values()),
            'structural_mismatches': sum(not row['structural_zero'] for row in rows),
            'original_failure_preserved': True,
            'canonical_geometric_pairing_derived': False,
            'physical_chirality_derived': False}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result['all_exact_identities_pass'] and result['all_controls_pass'] else 1)
