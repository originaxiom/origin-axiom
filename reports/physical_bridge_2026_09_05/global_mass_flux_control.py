"""Separately sealed R24 connection equality and independent exterior controls."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import time

import sympy as sp

spec = importlib.util.spec_from_file_location('r24_original', Path(__file__).with_name('global_mass_flux.py'))
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)


def even_exterior(A):
    """Differentiate exterior powers by replacing each coframe factor."""
    bases = [original.mass.cd.BASIS[j] for j in original.mass.EVEN]
    out = sp.zeros(len(bases))
    for col, basis in enumerate(bases):
        for slot, j in enumerate(basis):
            for i in range(3):
                target = list(basis)
                target[slot] = i
                if len(set(target)) != len(target):
                    continue
                sign = original.mass.permutation_sign(target)
                row = bases.index(tuple(sorted(target)))
                out[row, col] += sign*A[i, j]
    return out


@lru_cache(maxsize=1)
def connection_control():
    a = sp.Matrix(sp.symbols('a0:3', real=True))
    n = sp.Matrix(sp.symbols('n0:3', real=True))
    row = original.spin_connection_bridge()
    actual = row['mapped_connection']
    spin = -sp.I*original.pauli(a)/2
    expected = sp.kronecker_product(spin, sp.eye(2))+sp.kronecker_product(sp.eye(2), spin)
    residual = original.clean_matrix(actual-expected)
    U = original.mass.clifford_map()['U']
    independent = U.H*even_exterior(original.hat(a))*U
    basis_residuals = [original.clean_matrix((independent-expected).subs(
        {a[j]: int(i == j) for j in range(3)})) for i in range(3)]
    swapped = -sp.I*original.pauli(sp.Matrix([a[1], a[0], a[2]]))/2
    wrongs = [sp.kronecker_product(spin, sp.eye(2)), -expected,
              sp.kronecker_product(swapped, sp.eye(2))+sp.kronecker_product(sp.eye(2), swapped)]
    mass_action = spin*original.pauli(n)-original.pauli(n)*spin
    return dict(original_structural_boolean=row['connection_matches'],
                exact_residual=residual, raw_comparison_disagrees=(actual != expected and residual == sp.zeros(4)),
                independent_residual=original.clean_matrix(independent-expected),
                basis_residuals=basis_residuals,
                mutant_residuals=[original.clean_matrix(independent-W) for W in wrongs],
                mass_rotation_residual=original.clean_matrix(mass_action-original.pauli(a.cross(n))))


def run():
    start = time.monotonic()
    out = connection_control()
    return dict(control=out, runtime_seconds=time.monotonic()-start,
                scope='exact normalization and independent linear generators; original failure retained')


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, default=str), flush=True)
