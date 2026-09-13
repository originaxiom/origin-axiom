"""B1401 — the five |κ−2| values, the Nielsen invariance, and the parabolic-meridian attainment.

Needs SnapPy; skipped cleanly where it is unavailable so a bench without it does not red.
"""
import math
import pytest

snappy = pytest.importorskip("snappy")
import numpy as np

VALUES = {"m004": 1.0, "m009": 2 ** 0.5, "m003": 4.0,
          "v2873": 3 * 3 ** 0.5, "m202": 7.0}


def _m2(S):
    return np.array([[complex(S[0, 0]), complex(S[0, 1])],
                     [complex(S[1, 0]), complex(S[1, 1])]], dtype=complex)


def _inv2(M):
    d = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    return np.array([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]], dtype=complex) / d


def _tr(M):
    return M[0, 0] + M[1, 1]


def _kappa(G, wa, wb):
    A, B = _m2(G.SL2C(wa)), _m2(G.SL2C(wb))
    return complex(_tr(A @ B @ _inv2(A) @ _inv2(B)))


def test_the_five_values():
    for name, want in VALUES.items():
        G = snappy.Manifold(name).fundamental_group()
        assert G.num_generators() == 2, (name, G.num_generators())
        got = abs(_kappa(G, 'a', 'b') - 2)
        assert abs(got - want) < 1e-6, (name, got, want)


def test_kappa_is_constant_on_the_nielsen_class():
    """Fricke–Vogt conservation. A first pass used (a^2 b, b), which is NOT a Nielsen move —
    <a^2b, b> need not generate the same group — and that reading is withdrawn."""
    moves = [('a','b'), ('b','a'), ('a','ab'), ('ab','b'), ('a','ba'), ('ba','b'),
             ('a','B'), ('A','b'), ('A','B'), ('b','ab'), ('ab','a'), ('a','bA')]
    for name, want in VALUES.items():
        G = snappy.Manifold(name).fundamental_group()
        vals = [abs(_kappa(G, wa, wb) - 2) for wa, wb in moves]
        assert max(vals) - min(vals) < 1e-9, (name, max(vals) - min(vals))
        assert abs(vals[0] - want) < 1e-6, name
    # and the non-Nielsen pair genuinely differs on at least one manifold, which is what
    # makes it a different Nielsen class rather than a counterexample to invariance
    G = snappy.Manifold("m004").fundamental_group()
    assert abs(abs(_kappa(G, 'aab', 'b') - 2) - 3.0) < 1e-6, "the withdrawn reading's number"


def test_the_meridian_is_parabolic_and_reproduces_kappa():
    """Attainment needs tr A = ±2. Every one of the five has a parabolic meridian, and a
    meridian-containing pair gives the same κ — so the Jørgensen sum reaches |κ−2|."""
    for name, want in VALUES.items():
        M = snappy.Manifold(name)
        G = M.fundamental_group()
        mer = G.meridian(0)
        t = complex(_tr(_m2(G.SL2C(mer))))
        assert abs(abs(t) - 2) < 1e-6, (name, t)          # parabolic
        assert abs(complex(t) ** 2 - 4).real < 1e-6 or abs(complex(t) ** 2 - 4) < 1e-6
        for other in ('a', 'b'):
            assert abs(abs(_kappa(G, mer, other) - 2) - want) < 1e-6, (name, other)


def test_the_default_pair_does_NOT_attain_J_at_m004():
    """The detail that is easy to miss: re-deriving J from the default presentation gives 4.606,
    not 1. The infimum is over pairs and the minimiser is the parabolic one."""
    G = snappy.Manifold("m004").fundamental_group()
    a = _m2(G.SL2C('a'))
    km2 = abs(_kappa(G, 'a', 'b') - 2)
    sum_default = abs(complex(_tr(a)) ** 2 - 4) + km2
    assert abs(km2 - 1.0) < 1e-9
    assert sum_default > 4.6, sum_default
    # the meridian pair does attain it
    mer = G.meridian(0)
    m = _m2(G.SL2C(mer))
    sum_mer = abs(complex(_tr(m)) ** 2 - 4) + abs(_kappa(G, mer, 'a') - 2)
    assert abs(sum_mer - 1.0) < 1e-6, sum_mer
    assert sum_mer < sum_default


def test_the_bound_is_a_corollary_not_a_second_claim():
    """J = |κ−2| + inf|tr²A−4| ≥ |κ−2| because the first term is non-negative. Checked as
    arithmetic on every Nielsen-equivalent pair: the sum never falls below |κ−2|."""
    for name, want in VALUES.items():
        G = snappy.Manifold(name).fundamental_group()
        for wa, wb in [('a','b'), ('b','a'), ('a','ab'), ('ab','b'), ('a','B')]:
            s = abs(complex(_tr(_m2(G.SL2C(wa)))) ** 2 - 4) + abs(_kappa(G, wa, wb) - 2)
            assert s >= want - 1e-9, (name, wa, wb, s, want)
        # Jørgensen's inequality itself must hold on every pair
            assert s >= 1.0 - 1e-9, (name, wa, wb, s)


# --- addendum 1: does the parabolic pair GENERATE? ---

from math import gcd


def _exps(word):
    e = [0, 0]
    for ch in word:
        i = 0 if ch.lower() == 'a' else 1
        e[i] += 1 if ch.islower() else -1
    return e


def _index(rows):
    """gcd of the 2x2 minors = index of the span in Z^2 (0 if rank < 2)."""
    g = 0
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            g = gcd(g, abs(int(rows[i][0] * rows[j][1] - rows[i][1] * rows[j][0])))
    return g


def test_the_meridian_word_proves_generation_for_three():
    """m004, m009: meridian = 'ab'; v2873: 'BA' = (ab)^-1. Then a^-1.(ab) = b."""
    for name in ("m004", "m009"):
        assert snappy.Manifold(name).fundamental_group().meridian(0) == 'ab', name
    assert snappy.Manifold("v2873").fundamental_group().meridian(0) == 'BA'


def test_m202_meridian_pairs_provably_do_NOT_generate():
    """THE CORRECTION to §4: a necessary H_1 condition fails for both m202 meridian pairs."""
    G = snappy.Manifold("m202").fundamental_group()
    rels = [_exps(r) for r in G.relators()]
    full = _index([[1, 0], [0, 1]] + rels)
    em = _exps(G.meridian(0))
    for other in ([1, 0], [0, 1]):
        assert _index([em, other] + rels) != full, "m202 meridian pair must FAIL the H_1 test"
    # and m003's (mer,b) fails too, while (mer,a) passes
    H = snappy.Manifold("m003").fundamental_group()
    hr = [_exps(r) for r in H.relators()]
    hfull = _index([[1, 0], [0, 1]] + hr)
    hm = _exps(H.meridian(0))
    assert _index([hm, [0, 1]] + hr) != hfull, "m003 (mer,b) must FAIL"
    assert _index([hm, [1, 0]] + hr) == hfull, "m003 (mer,a) must PASS"


def test_m202_is_recovered_by_its_longitude():
    """longitude(0) = 'bba' is parabolic, pairs with b, gives |k-2| = 7, and PROVABLY generates
    because b^-2.(b^2 a) = a."""
    M = snappy.Manifold("m202")
    G = M.fundamental_group()
    assert M.num_cusps() == 2
    lon = G.longitude(0)
    assert lon == 'bba', lon
    t = complex(_tr(_m2(G.SL2C(lon))))
    assert abs(abs(t) - 2) < 1e-6, "must be parabolic"
    assert abs(abs(_kappa(G, lon, 'b') - 2) - 7.0) < 1e-6
    rels = [_exps(r) for r in G.relators()]
    assert _index([_exps(lon), [0, 1]] + rels) == _index([[1, 0], [0, 1]] + rels)
    # the word argument: 'bba' with 'b' recovers 'a'
    assert lon.count('a') + lon.count('A') == 1, "a occurs once -> solvable"


def test_m003_is_the_one_open_case():
    """Its candidate parabolics each contain 'a' more than once, so no generator is immediately
    recoverable; the necessary condition passes but generation is NOT proved."""
    G = snappy.Manifold("m003").fundamental_group()
    for w in (G.meridian(0), G.longitude(0)):
        t = complex(_tr(_m2(G.SL2C(w))))
        assert abs(abs(t) - 2) < 1e-6
        assert abs(abs(_kappa(G, w, 'a') - 2) - 4.0) < 1e-6
        assert w.count('a') + w.count('A') > 1, (w, "if this were 1 the case would close")


def test_m004_is_the_only_one_needing_no_proviso():
    """Jorgensen's inequality gives J >= 1 unconditionally, and |k-2| = 1, so the lower bound is
    free at m004 alone -- it sits at the FLOOR of the inequality."""
    G = snappy.Manifold("m004").fundamental_group()
    assert abs(abs(_kappa(G, 'a', 'b') - 2) - 1.0) < 1e-9
    for name, v in VALUES.items():
        if name == "m004":
            continue
        assert v > 1.0, (name, v)          # every other value is strictly above the floor
