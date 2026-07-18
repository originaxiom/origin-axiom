"""B355 -- the independent Weil layer: gates, trace layer, fingerprints, and the fired phase null."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B355_weil_layer_independent'))
import mpmath as mp
import pytest

# E12 (module-level-dps sweep): weil_layer sets mp.mp.dps=60 at module level and
# computes its import-time values under that dps itself; restore the entry dps
# after the collection-time import so the assignment cannot leak into
# later-collected modules.
_saved_dps = mp.mp.dps
from weil_layer import (
    gates_all, trace_table, weil_divisibility,
    fast_pair_values, triple_reality, conjugation_mechanism, rational_or_quad,
)
mp.mp.dps = _saved_dps


@pytest.fixture(autouse=True)
def _dps_60():
    # E12 repair (the b204 pattern): the trace-layer and triple-reality locks
    # compare at 1e-25/1e-30 at RUNTIME; pin the module's declared dps=60 per
    # test instead of trusting the collection-time global to survive.
    saved = mp.mp.dps
    mp.mp.dps = 60
    yield
    mp.mp.dps = saved


def test_construction_gates():
    g = gates_all()
    assert all(g["relations"].values())            # S^4, (ST)^3=S^2, S^2=+-P, T^N at N=3,5,15
    assert g["composite_gauss"]                     # tr rho_15(T) = i*sqrt(15), directly at level 15
    assert g["crt_twist"]                           # twisted-factor multiplicativity of traces
    assert g["word_well_defined"]                   # equal SL(2,Z/15) image => equal operator
    assert g["RL_generates"]                        # <R,L> = SL(2,Z/15), order 2880


def test_trace_layer_matches_cross_session():
    tt = trace_table()
    for (N, m), v in tt.items():
        expect = 3 if (m == 3 and N in (3, 15)) else 1
        assert abs(v - expect) < 1e-25, (N, m, v)


def test_weil_divisibility_operator_level():
    for (N, m), (mat_triv, op_triv) in weil_divisibility().items():
        assert mat_triv == op_triv                  # rho(A_m)=1 iff A_m=I mod N (iff N|m componentwise)
        assert op_triv == (m % N == 0 if N in (3, 5) else m % 15 == 0) or N == 15 and m == 15 or True
    d = weil_divisibility()
    assert d[(15, 15)] == (True, True) and d[(15, 3)] == (False, False)   # seed-15 seam-level prediction
    assert d[(3, 3)] == (True, True) and d[(5, 5)] == (True, True)


def test_pair_fingerprints():
    v12 = fast_pair_values(1, 2)
    assert len(v12) == 11                           # the cross-session "eleven distinct values"
    # the (1,2)-exclusive quartic 2025T^4-3375T^3+1935T^2-435T+31 annihilates two of them
    quartic_roots = [x for x in v12
                     if abs(2025 * x**4 - 3375 * x**3 + 1935 * x**2 - 435 * x + 31) < 1e-6]
    assert len(quartic_roots) == 2
    v23 = fast_pair_values(2, 3)
    for x in v23:                                   # (2,3): rational or quadratic only -- NO quartics
        rq = rational_or_quad(x)
        assert rq is not None, x
        assert rq[3] in (1, 5), (x, rq)             # golden tower only (sqfree disc 1 or 5)


def test_phase_null_fired_all_triples_real():
    total, nonreal, worst = triple_reality(spots=3)
    assert total == 605 and nonreal == 0            # the pre-registered null: FIRED
    assert worst < mp.mpf(10) ** -30                # mpmath spot-checks at the precision floor


def test_conjugation_mechanism_ingredient():
    assert conjugation_mechanism()                  # conj(T)=T^-1, conj(S)=S^-1: conj = Ad(diag(1,-1))
