r"""THE CONJUNCTION SWEEP — is there an object-specific atom after all?

The base-rate control killed the ATOM taken alone: ~35% of census manifolds
surject onto 2T, and 36.4% of knot complements carry m004's exact count.

The cornerstone synthesis's #1 recommendation: ask for the CONJUNCTION rather
than the atom —

    trace field Q(sqrt-3)   AND   exactly two 2T surjections   AND   H_1 = Z

If the conjunction cuts the census to a handful, there IS an object-specific
atom and knot-ness moves from decoration to premise -- the only route by which
Reid's uniqueness becomes load-bearing. If the conjunction is still populous,
the atom is dead and the programme is, finally, about the class.

TRACE FIELD, and the approximation being made. Sage is unavailable (the same
blocker B735 hit), so the exact invariant trace field cannot be computed here.
Instead: the holonomy traces of a generating set are tested for membership in
Q(sqrt-3) numerically. Writing tr = x + iy, membership requires x in Q and
y/sqrt3 in Q, both at bounded denominator. This is the TRACE field of the given
generators, which contains the invariant trace field; it is a necessary
condition, not the exact invariant. Stated plainly rather than hidden: this
sweep OVER-counts, so a small answer is decisive and a large one is an upper
bound.

Validated on m004, whose traces lie in Z[omega].

Gate 5-Q. Structure only.
"""
import argparse
import collections
import importlib.util
import json
import math
import os

import snappy
from fractions import Fraction

_spec = importlib.util.spec_from_file_location(
    'br', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'base_rate_2T.py'))
br = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(br)

SQRT3 = math.sqrt(3.0)


def _is_rational(v, maxden=40, tol=1e-7):
    if abs(v) < tol:
        return True
    f = Fraction(v).limit_denominator(maxden)
    return abs(float(f) - v) < tol


def in_Qsqrt3(z, maxden=40, tol=1e-7):
    """Is the complex number z in Q(sqrt(-3))?  z = x + i*y, x in Q, y/sqrt3 in Q."""
    return _is_rational(z.real, maxden, tol) and _is_rational(z.imag / SQRT3, maxden, tol)


def trace_field_is_Qsqrt3(M, nwords=6):
    """Necessary condition: all sampled holonomy traces lie in Q(sqrt-3)."""
    try:
        G = M.fundamental_group()
        gens = G.generators()
        words = list(gens) + [a + b for a in gens for b in gens][:nwords]
        for w in words[:nwords]:
            tr = complex(G.SL2C(w).trace())
            if not in_Qsqrt3(tr):
                return False
        return True
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=3000)
    ap.add_argument('--knots', action='store_true',
                    help='sweep CensusKnots instead of the cusped census')
    args = ap.parse_args()

    # ---- validation on m004 before anything is believed ----
    m4 = snappy.Manifold('m004')
    assert trace_field_is_Qsqrt3(m4), 'm004 must pass the Q(sqrt-3) test'
    assert br.count_surjections(m4.fundamental_group())[1] // 24 == 2
    assert str(m4.homology()) == 'Z'
    print('VALIDATION m004: Q(sqrt-3) OK | exactly 2 surjections OK | H1 = Z OK\n')

    src = snappy.CensusKnots() if args.knots else snappy.OrientableCuspedCensus(cusps=1)
    label = 'CensusKnots' if args.knots else 'one-cusped census'
    print(f'sweeping {min(args.n, len(src))} of {len(src)} ({label})\n')

    tally = collections.Counter()
    survivors = []
    n = 0
    for M in src:
        if n >= args.n:
            break
        try:
            res = br.count_surjections(M.fundamental_group())
        except Exception:
            continue
        if res is None:
            continue
        n += 1
        two = (res[1] // 24 == 2)
        h1z = (str(M.homology()) == 'Z')
        fld = trace_field_is_Qsqrt3(M)
        tally['2T=2'] += two
        tally['H1=Z'] += h1z
        tally['Q(v-3)'] += bool(fld)
        if two and h1z:
            tally['2T=2 & H1=Z'] += 1
        if two and fld:
            tally['2T=2 & Q(v-3)'] += 1
        if two and h1z and fld:
            tally['ALL THREE'] += 1
            if len(survivors) < 40:
                survivors.append(M.name())
        if n % 500 == 0:
            print(f'  {n:5} swept … conjunction so far: {tally["ALL THREE"]}')

    print(f'\n{"="*66}\nTHE CONJUNCTION over {n} manifolds ({label})\n{"="*66}')
    for k in ['2T=2', 'H1=Z', 'Q(v-3)', '2T=2 & H1=Z', '2T=2 & Q(v-3)', 'ALL THREE']:
        print(f'  {k:16} {tally[k]:6}   {100*tally[k]/n:6.2f} %')
    print(f'\n  survivors of the full conjunction: {survivors}')
    json.dump({'class': label, 'n': n, 'tally': dict(tally), 'survivors': survivors},
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                f'conjunction_{"knots" if args.knots else "census"}.json'), 'w'),
              indent=1)
    print('\n  NOTE: the trace-field test is a NECESSARY condition computed on')
    print('  generator traces (Sage unavailable), so this OVER-counts. A small')
    print('  answer is decisive; a large one is an upper bound.')


if __name__ == '__main__':
    main()
