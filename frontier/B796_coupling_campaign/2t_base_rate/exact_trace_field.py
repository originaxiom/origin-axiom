r"""EXACT invariant trace fields, and a validation of the numeric proxy.

The conjunction sweep used a NUMERIC test for "trace field is Q(sqrt-3)":
sampled holonomy traces tr = x + iy with x rational and y/sqrt3 rational at
bounded denominator. That is a necessary condition on the GENERATOR trace
field and it over-counts.

Sage is now installed (micromamba env "sage", with SnapPy 3.3.2 pip-installed
alongside it), so the EXACT invariant trace field is computable:

    M.invariant_trace_field_gens().find_field(prec, degree, True)

m004 returns x^2 - x + 1, i.e. Q(zeta_6) = Q(sqrt-3). Confirmed.

This script re-runs the trace-field half of the conjunction EXACTLY over a
census slice and reports, against the proxy:
    false positives  - proxy said Q(sqrt-3), exact says otherwise
    false negatives  - proxy said no, exact says Q(sqrt-3)

Run inside the sage env:
    micromamba run -n sage python exact_trace_field.py --n 300

Gate 5-Q. Structure only.
"""
import argparse
import json
import math
import os
from fractions import Fraction

import snappy

SQRT3 = math.sqrt(3.0)
DISC_M3_POLY = 'x^2 - x + 1'          # Q(zeta_6) = Q(sqrt-3)


# ----------------------------------------------------------- the numeric proxy
def _is_rational(v, maxden=40, tol=1e-7):
    if abs(v) < tol:
        return True
    return abs(float(Fraction(v).limit_denominator(maxden)) - v) < tol


def proxy_is_Qsqrt3(M, nwords=6):
    try:
        G = M.fundamental_group()
        gens = G.generators()
        words = list(gens) + [a + b for a in gens for b in gens]
        for w in words[:nwords]:
            tr = complex(G.SL2C(w).trace())
            if not (_is_rational(tr.real) and _is_rational(tr.imag / SQRT3)):
                return False
        return True
    except Exception:
        return None


# ------------------------------------------------------------- the exact test
def exact_itf(M, prec=200, degree=10):
    """Defining polynomial of the invariant trace field, or None."""
    try:
        f = M.invariant_trace_field_gens().find_field(prec, degree, True)
        return str(f[0].defining_polynomial()) if f else None
    except Exception:
        return None


def is_Qsqrt3(poly):
    """Q(sqrt-3) up to the usual presentations: x^2-x+1 or x^2+x+1 or x^2+3."""
    if poly is None:
        return None
    p = poly.replace(' ', '')
    return p in ('x^2-x+1', 'x^2+x+1', 'x^2+3')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=300)
    ap.add_argument('--knots', action='store_true')
    args = ap.parse_args()

    m4 = snappy.Manifold('m004')
    assert is_Qsqrt3(exact_itf(m4)), 'm004 must have invariant trace field Q(sqrt-3)'
    assert proxy_is_Qsqrt3(m4), 'proxy must pass m004'
    print(f'VALIDATION m004: exact ITF = {exact_itf(m4)}  -> Q(sqrt-3) OK; '
          f'proxy agrees\n')

    src = snappy.CensusKnots() if args.knots else snappy.OrientableCuspedCensus(cusps=1)
    label = 'CensusKnots' if args.knots else 'one-cusped census'

    fp, fn, agree, undecided, n = [], [], 0, 0, 0
    exact_hits = []
    for M in src:
        if n >= args.n:
            break
        p = proxy_is_Qsqrt3(M)
        e = is_Qsqrt3(exact_itf(M))
        if p is None or e is None:
            undecided += 1
            continue
        n += 1
        if e:
            exact_hits.append(M.name())
        if p == e:
            agree += 1
        elif p and not e:
            fp.append(M.name())
        else:
            fn.append(M.name())
        if n % 50 == 0:
            print(f'  {n:4} checked … exact Q(sqrt-3) hits: {len(exact_hits)}, '
                  f'FP {len(fp)}, FN {len(fn)}')

    print(f'\n{"="*64}\nPROXY vs EXACT over {n} manifolds ({label})\n{"="*64}')
    print(f'  agree                : {agree}/{n}  ({100*agree/n:.1f} %)')
    print(f'  false POSITIVES      : {len(fp)}   {fp[:10]}')
    print(f'  false NEGATIVES      : {len(fn)}   {fn[:10]}')
    print(f'  undecided (skipped)  : {undecided}')
    print(f'\n  EXACT Q(sqrt-3) manifolds found: {len(exact_hits)}  {exact_hits[:20]}')
    out = {'class': label, 'n': n, 'agree': agree, 'false_pos': fp,
           'false_neg': fn, 'undecided': undecided, 'exact_hits': exact_hits}
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     f'exact_tf_{"knots" if args.knots else "census"}.json'),
                        'w'), indent=1)


if __name__ == '__main__':
    main()
