"""B182 -- the selection / multiplicity door (V176). Fast PSLQ locks.

Superposition PROLIFERATES: weaving N distinct-field metallic units gives a gap-label module of rank 1+N
(each distinct field adds a frequency-layer; same-field units add none). So 'more units' enriches the
structure-menu, it does not select to a unique value. The fence (selection-to-unique = a constraint/gluing
phenomenon, NEEDS-SPECIALIST) lives in multiplicity_selection.py.
"""
from mpmath import pslq, mp, mpf, sqrt
mp.dps = 50


def _alpha(m):
    return (sqrt(m * m + 4) - m) / 2


def test_rank_grows_with_distinct_field_units():
    units = [1, 2, 3, 5]                       # distinct fields sqrt 5, 2, 13, 29
    for N in (2, 3, 4):
        vec = [mpf(1)] + [_alpha(m) for m in units[:N]]
        assert pslq(vec, maxcoeff=10**6, maxsteps=10**4) is None    # independent -> rank 1+N


def test_same_field_adds_no_rank():
    rel = pslq([mpf(1), _alpha(1), _alpha(4)], maxcoeff=10**6, maxsteps=10**4)   # both Q(sqrt5)
    assert rel is not None
    assert abs(-1 + 2 * _alpha(1) - _alpha(4)) < mpf('1e-30')
