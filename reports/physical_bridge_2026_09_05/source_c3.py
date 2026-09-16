"""R32 exact representation controls; analytic hypotheses are in the proof.

The finite chain models are not new triangulations or PDE discretizations.
No empirical mass, physical quotient choice or independent proof is certified.
"""
from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as sp


def local(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


c3 = local('r32_frozen_c3', 'resolved_fermion_c3_control.py')
Z = (-1 + sp.I*sp.sqrt(3))/2


def clean(x):
    return sp.simplify(sp.expand_complex(x))


def matrix(M):
    return sp.Matrix(M).applyfunc(clean)


def weight(a):
    if not isinstance(a, int):
        raise ValueError('integer character exponent required')
    return clean(Z**(a % 3))


def action(exponents, phase=0, generator=1):
    if generator not in (1, 2):
        raise ValueError('nonidentity C3 generator required')
    if not isinstance(phase, int):
        raise ValueError('integer scalar lift phase required')
    return sp.diag(*(weight(generator*(a+phase)) for a in exponents))


def projector(U, order=3):
    U = sp.Matrix(U)
    if not isinstance(order, int) or order < 1 or U.rows != U.cols:
        raise ValueError('square finite-order representation required')
    if matrix(U**order-sp.eye(U.rows)) != sp.zeros(U.rows):
        raise ValueError('lift does not have the declared group order')
    return matrix(sum((U**k for k in range(order)), sp.zeros(U.rows))/order)


def zero_trace_triples():
    return [p for p in itertools.product(range(3), repeat=3)
            if clean(sum(weight(a) for a in p)) == 0]


def equivariant(d, U0, U1):
    return matrix(U1*d-d*U0) == sp.zeros(d.rows, d.cols)


def projected_betti(differentials, actions, order=3):
    if len(differentials)+1 != len(actions):
        raise ValueError('one action in each cochain degree required')
    for d, a, b in zip(differentials, actions, actions[1:]):
        if d.shape != (b.rows, a.rows) or not equivariant(d, a, b):
            raise ValueError('differential is not equivariant')
    for a, b in zip(differentials, differentials[1:]):
        if matrix(b*a) != sp.zeros(b.rows, a.cols):
            raise ValueError('not a cochain complex')
    P = [projector(U, order) for U in actions]
    outgoing = [int(matrix(d*p).rank()) for d, p in zip(differentials, P)] + [0]
    incoming = [0] + outgoing[:-1]
    return [int(p.rank())-a-b for p, a, b in zip(P, incoming, outgoing)]


def trivial_cone(phase=0):
    # Minimal base cohomology plus the actual nonzero restriction H0(Q)->H0(N).
    d0 = sp.Matrix([0, 0, 1, 1, 1])
    d1 = sp.zeros(1, 5)
    acts = [action([0], phase), action([1, 2, 0, 0, 0], phase), action([0], phase)]
    betti = projected_betti([d0, d1], acts)
    h1 = action([0, 0, 1, 2], phase)
    h2 = action([0], phase)
    net_by_trace = clean(sum(sp.trace(h1**i)-sp.trace(h2**i) for i in range(3))/3)
    return dict(projected_betti=betti, odd_minus_even=betti[1]-betti[0]-betti[2],
                index_from_character=net_by_trace,
                fixed_fibre_trace=clean(3*weight(phase)),
                base_lefschetz=clean(sp.trace(acts[0])-sp.trace(action([1, 2], phase))+sp.trace(acts[2])))


def core_complex(t, phase=0):
    t = sp.sympify(t)
    if t.has(sp.Float) or t.is_real is not True:
        raise ValueError('exact real attachment parameter required')
    U = action([0, 1, 2], phase)
    d = t*sp.eye(3)
    P = projector(U)
    D = sp.BlockMatrix([[sp.zeros(3), d.H], [d, sp.zeros(3)]]).as_explicit()
    group = sp.diag(U, U)
    honest = sp.diag(P, P)
    drop_core = sp.diag(sp.zeros(3), P)
    return dict(t=t, phase=phase, projected_betti=projected_betti([d], [U, U]),
                positive_square=matrix(D**2-t**2*sp.eye(6)) == sp.zeros(6),
                commutes=matrix(D*group-group*D) == sp.zeros(6),
                honest_projection_commutes=matrix(D*honest-honest*D) == sp.zeros(6),
                drop_core_commutes=matrix(D*drop_core-drop_core*D) == sp.zeros(6),
                retained_even=int(P.rank()), retained_odd=int(P.rank()))


def tensor_invariants(multiplicities, phase=0):
    if len(multiplicities) != 3 or any(type(n) is not int or n < 0 for n in multiplicities):
        raise ValueError('three nonnegative integer multiplicities required')
    # Independent weight enumeration; the proof is all-W, this is a finite control.
    exponents = [a+b+phase for a in range(3) for b, n in enumerate(multiplicities) for _ in range(n)]
    return sum(e % 3 == 0 for e in exponents)


def reflection_circle(n=1):
    if type(n) is not int or n <= 0:
        raise ValueError('positive integral Fourier level required')
    # Bases (cos nx, sin nx), (cos nx dx, sin nx dx), derivative by columns.
    d = sp.Matrix([[0, n], [-n, 0]])
    U0, U1 = sp.diag(1, -1), sp.diag(-1, 1)
    D = sp.BlockMatrix([[sp.zeros(2), d.T], [d, sp.zeros(2)]]).as_explicit()
    U = sp.diag(U0, U1)
    return dict(zero_betti=projected_betti([sp.zeros(1)], [sp.eye(1), -sp.eye(1)], 2),
                positive_even=int(projector(U0, 2).rank()),
                positive_odd=int(projector(U1, 2).rank()),
                positive_acyclic=projected_betti([d], [U0, U1], 2),
                intertwines=equivariant(d, U0, U1),
                commutes=D*U == U*D, square=D**2 == n*n*sp.eye(4))


@lru_cache(maxsize=1)
def actual_characters():
    return c3.run()


def run():
    actual = actual_characters()
    triples = zero_trace_triples()
    lifts = []
    for phase, generator in itertools.product(range(3), (1, 2)):
        U = action([0, 1, 2], phase, generator)
        P = projector(U)
        lifts.append(dict(phase=phase, generator=generator, action=U.tolist(),
                          projector=P.tolist(), rank=int(P.rank()),
                          unitary=matrix(U.H*U) == sp.eye(3), idempotent=matrix(P*P) == P))
    trivial = [trivial_cone(p) for p in range(3)]
    core = [core_complex(t, p) for t, p in itertools.product((0, 1, 2, sp.Rational(1, 7)), range(3))]
    circles = [reflection_circle(n) for n in (1, 2, 5)]
    tensor = [dict(multiplicities=list(m), phase=p, dimension=tensor_invariants(m, p))
              for m, p in itertools.product(itertools.product(range(3), repeat=3), range(3))]
    checks = dict(
        actual_source_characters=all(actual['checks'].values()),
        trace_multiset=sorted(triples) == sorted(itertools.permutations(range(3))),
        all_lifts_one_invariant=all(r['rank'] == 1 and r['unitary'] and r['idempotent'] for r in lifts),
        trivial_cone_counts=[r['projected_betti'] for r in trivial] == [[0, 2, 1], [0, 1, 0], [0, 1, 0]],
        trivial_net_and_trace=all(r['odd_minus_even'] == r['index_from_character'] == 1
                                and r['fixed_fibre_trace'] == r['base_lefschetz'] for r in trivial),
        core_projection=all(r['projected_betti'] == ([1, 1] if r['t'] == 0 else [0, 0])
                            and r['commutes'] and r['positive_square'] and r['honest_projection_commutes']
                            and r['drop_core_commutes'] == (r['t'] == 0) for r in core),
        tensor_count=all(r['dimension'] == sum(r['multiplicities']) for r in tensor),
        zero_mode_counterexample=all(r['zero_betti'] == [1, 0] and r['positive_even'] == r['positive_odd'] == 1
                                    and r['positive_acyclic'] == [0, 0] and r['intertwines'] and r['commutes'] and r['square'] for r in circles))
    return dict(scope='Exact finite controls for the authored conditional equivariant-source proof; not a new geometry or PDE certificate.',
                checks=checks, all_checks_pass=all(checks.values()), actual_character_control=actual,
                zero_trace_triples=triples, lift_controls=lifts, trivial_controls=trivial,
                core_controls=core, circle_controls=circles, tensor_controls=tensor)


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, default=str, indent=2, sort_keys=True))
    if not result['all_checks_pass']:
        raise SystemExit(1)
