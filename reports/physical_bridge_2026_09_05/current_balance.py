"""R41 exact matrix controls, with R40 counts reused as frozen input.

The compact-cutoff proof is authored separately. These finite calculations
are not an analytic existence theorem or an independently derived spectrum.
"""
from functools import lru_cache
import hashlib
import json
from pathlib import Path

import sympy as s


def clean(m):
    return m.applyfunc(s.expand) if isinstance(m, s.MatrixBase) else s.expand(m)


def elementary(n, a, b):
    m = s.zeros(n)
    m[a, b] = 1
    return m


def flag(n, k):
    if not 0 < k < n:
        raise ValueError('A proper nonzero flag is required')
    return s.diag(*([n-k]*k+[-k]*(n-k)))


def split(c):
    return clean((c-c.H)/2), clean((c+c.H)/2)


def contraction(c, xi):
    a, psi = split(c)
    return clean(s.trace(psi*(a*xi-xi*a)))


@lru_cache(None)
def upper(n):
    c = s.zeros(n)
    norms = {}
    for a in range(n):
        for b in range(a, n):
            r, i = s.symbols(f'r{n}_{a}_{b} i{n}_{a}_{b}', real=True)
            c[a, b] = r+s.I*i
            norms[a, b] = r*r+i*i
    return c, norms


def cross_norm(norms, n, k):
    return sum(norms[a, b] for a in range(k) for b in range(k, n))


def nonnegative_even_polynomial(expression):
    """Sufficient check only: positive coefficients need even powers too."""
    expression = clean(expression)
    symbols = sorted(expression.free_symbols, key=str)
    if not symbols:
        return bool(expression >= 0)
    return all(coefficient >= 0 and all(power % 2 == 0 for power in powers)
               for powers, coefficient in s.Poly(expression, *symbols).terms())


def moment_commutator(c):
    return clean(c*c.H-c.H*c)


def parent_directions():
    t = s.diag(1, 1, 1, 1, -4)
    u = s.diag(3, -1, -1, -1, 0)
    xis = [s.diag(flag(4, k), s.zeros(1)) for k in range(1, 4)]
    neutral = [elementary(5, 0, j) for j in range(1, 4)]
    charged, lower = elementary(5, 0, 4), elementary(5, 4, 0)
    return t, u, xis, neutral, charged, lower


def reused_counts():
    path = Path(__file__).with_name('COEFFICIENT_PARENT_NATIVE_FIRST.jsonl')
    digest = '12171ed3ccc88e9d99737a059fe09d738aaf83c2375527287463e13a4c9211e8'
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise ValueError('Frozen R40 native input changed')
    data = {r['part']: r['result'] for r in map(json.loads, path.read_text().splitlines())}
    return {name: (data['sector_'+name]['V']['n'], data['sector_'+name]['dual']['n'])
            for name in ('V', 'W', 'wedgeW')}


def run():
    c4, norms4 = upper(4)
    _, psi = split(c4)
    flag_checks = []
    for k in range(1, 4):
        cross = cross_norm(norms4, 4, k)
        margin = clean(2*s.trace(psi.H*psi)-cross)
        flag_checks.append(dict(k=k,
            contraction=clean(contraction(c4, flag(4, k))+2*cross) == 0,
            trace_zero=s.trace(flag(4, k)) == 0,
            norm=s.trace(flag(4, k)**2) == 4*k*(4-k),
            cross_bound=nonnegative_even_polynomial(margin)))
    t, u, xis, neutral, n, lower = parent_directions()
    mu = sum((moment_commutator(k) for k in neutral), s.zeros(5))
    charged_mu = moment_commutator(n)
    pv = s.diag(1, 1, 1, 1, 0)
    c5, norms5 = upper(5)
    alpha_norm = sum(norms5[j, 4] for j in range(4))
    gram = s.Matrix(3, 3, lambda j, k: s.trace(xis[j]*xis[k]))
    counts = reused_counts()
    return dict(
        flag_checks=flag_checks,
        gram=[[int(x) for x in gram.row(j)] for j in range(3)],
        block_T_pairings=[int(s.trace(xi*t)) for xi in xis],
        U_pairings=[int(s.trace(xi*u)) for xi in xis],
        minus_U_pairings=[int(-s.trace(xi*u)) for xi in xis],
        T_norm=int(s.trace(t*t)),
        neutral_checks=dict(current_is_U=mu == u,
            commutes_T=all(t*k-k*t == s.zeros(5) for k in neutral),
            retains_V=all((s.eye(5)-pv)*k*pv == s.zeros(5) for k in neutral)),
        charged_checks=dict(charge_five=t*n-n*t == 5*n,
            current=charged_mu == s.diag(1, 0, 0, 0, -1),
            T_pairing=int(s.trace(t*charged_mu)),
            flag_pairings=[int(s.trace(xi*charged_mu)) for xi in xis],
            upper_retains_V=(s.eye(5)-pv)*n*pv == s.zeros(5),
            lower_does_not=(s.eye(5)-pv)*lower*pv != s.zeros(5)),
        whole_rank_identity=clean(contraction(c5, t)+s.Rational(5, 2)*alpha_norm) == 0,
        reused_interior_counts=counts,
        conditional_flat_map_obstructed={name: pair[0] != pair[1] for name, pair in counts.items()},
        physical_background_constructed=False,
        source_action_derived=False)


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True))
