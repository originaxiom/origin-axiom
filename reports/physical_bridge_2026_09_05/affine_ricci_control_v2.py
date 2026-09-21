"""Separately sealed canonicalization diagnostic; original R42 stays frozen."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sys

import sympy as s

path = Path(__file__).with_name('affine_background.py')
spec = importlib.util.spec_from_file_location('r42_v2_original', path)
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)


def polynomial_zero(matrix, variables):
    return all(s.Poly(s.expand(entry), *variables).is_zero for entry in matrix)


@lru_cache(None)
def contraction():
    ks, _ = original.blocks(original.cubic())
    rs = original.gauss(ks)
    ric = s.Matrix(3,3,lambda j,k: sum(rs[i,j][i,k] for i in range(3)))
    gram = s.Matrix(3,3,lambda j,k: s.trace(ks[j]*ks[k]))
    variables = sorted(set().union(*(v.free_symbols for mat in ks for v in mat)),key=str)
    return ric, gram, variables


def run():
    ric, gram, variables = contraction()
    residual = ric+2*s.eye(3)-gram
    old = original.run()
    checks = {key:value for key,value in old['generic'].items()
              if isinstance(value,bool) and key != 'ricci'}
    for group in ('hyperbolic','simplex','holonomy'):
        checks.update({group+'_'+key:value for key,value in old[group].items() if isinstance(value,bool)})
    checks.update(
        canonical_ricci=original.clean(residual) == s.zeros(3),
        expanded_polynomial=polynomial_zero(residual,variables),
        wrong_constant=original.clean(ric-2*s.eye(3)-gram) == -4*s.eye(3),
        wrong_cubic_rejected=not polynomial_zero(ric+2*s.eye(3)+gram,variables),
        constant_control_rejected=not polynomial_zero(s.eye(3),variables),
        quadric_norm=old['hyperbolic']['norm'] == '6',
        simplex_norm=old['simplex']['psi_norm'] == '12')
    return dict(checks=checks, all_checks_pass=all(checks.values()),
        preserved_original_structural_ricci=old['generic']['ricci'],
        scope='Canonical polynomial comparison and finite controls, not independent global analysis or physics.')


if __name__ == '__main__':
    result = run()
    print(json.dumps(result,sort_keys=True))
    sys.exit(0 if result['all_checks_pass'] else 1)
