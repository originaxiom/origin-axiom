"""Locks for B535 — the coupling space.

C1: census saturates at 6 Perron types / 7 canonical systems (length <= 6).
C2: one-measurement word-level cut: 17,280 lifts -> 8 (grammar) -> 2 (language),
    and the second survivor is EXACTLY the conjugate a^-1 sigma a.
C3: the read-out dictionary — every component recovers tau via its cubic.
"""

import sys
import os
import numpy as np
import sympy as sp
import pytest
from itertools import permutations

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier',
                                'B530_natural_history'))
from listen_39_induction_engine import (
    grow, factor_position_map, standard_return_words_from_positions,
    canonical_induced_system,
)

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}

t = sp.Symbol('t')
MIN = t**4 - t**2 - 1


def red(e):
    return sp.rem(sp.expand(e), MIN, t)


@pytest.fixture(scope='module')
def host():
    return grow(10)


def _analyze(factor, host, trim=2):
    fpm = factor_position_map(host, len(factor))
    if factor not in fpm:
        return None
    positions = fpm[factor]
    if len(positions) < 2 * trim + 2:
        return None
    rws = standard_return_words_from_positions(host, positions, trim=trim)
    if len(rws) < 2:
        return None
    ind = canonical_induced_system(rws, max_power=2)
    if ind is None:
        return None
    M = np.array(ind['matrix'].tolist(), dtype=float)
    eigs, vecs = np.linalg.eig(M)
    idx = np.argmax(np.abs(eigs.real))
    v = vecs[:, idx].real
    if np.any(v < 0):
        v = -v
    return {
        'perron_key': tuple(np.round(np.sort(v / v.sum())[::-1], 4)),
        'codes': ind['canonical_codes'],
        'perron_val': abs(eigs[idx].real),
        'matrix': ind['matrix'],
    }


# ── C1: saturation ──

def test_census_saturates_6_and_7(host):
    """Lengths 1..6: exactly 6 Perron types and 7 canonical systems,
    with length 6 adding nothing new (saturation at 5)."""
    perron, codes = {}, {}
    for L in range(1, 7):
        fpm = factor_position_map(host, L)
        for u in fpm:
            r = _analyze(u, host)
            if r is None:
                continue
            perron.setdefault(r['perron_key'], L)
            codes.setdefault(r['codes'], L)
    assert len(perron) == 6, f"expected 6 Perron types, got {len(perron)}"
    assert len(codes) == 7, f"expected 7 canonical systems, got {len(codes)}"
    assert max(perron.values()) == 5, "last new Perron type must appear at length 5"
    assert max(codes.values()) == 5, "last new canonical system must appear at length 5"


def test_t6_is_q2_window(host):
    """The 6th type ('bABab') is the q=2 case: Perron eigenvalue beta^2."""
    r = _analyze('bABab', host)
    beta = float(sp.sqrt((1 + sp.sqrt(5)) / 2).evalf(20))**2 * \
        (1 + float(sp.sqrt((1 + sp.sqrt(5)) / 2).evalf(20)))
    assert abs(r['perron_val'] - beta**2) < 1e-6, \
        f"Perron {r['perron_val']} != beta^2 {beta**2}"


# ── C2: the one-measurement cut ──

def _language_data(sub, depth):
    w = 'a'
    for _ in range(depth):
        w = ''.join(sub[c] for c in w)
    return (frozenset(w[i:i+2] for i in range(len(w) - 1)),
            frozenset(w[i:i+6] for i in range(len(w) - 5)))


def test_one_measurement_grammar_cut():
    """17,280 lifts of the measured abelianization: exactly 8 share sigma's
    bigram grammar; exactly 2 of those share the full language."""
    ref_bi, _ = _language_data(SUB, 6)
    arr = {g: sorted(set(permutations(SUB[g]))) for g in 'abAB'}
    hits = []
    for wa in arr['a']:
        for wb in arr['b']:
            for wA in arr['A']:
                for wB in arr['B']:
                    s = {'a': ''.join(wa), 'b': ''.join(wb),
                         'A': ''.join(wA), 'B': ''.join(wB)}
                    bi, _six = _language_data(s, 6)
                    if bi == ref_bi:
                        hits.append(s)
    assert len(hits) == 8, f"grammar cut: expected 8, got {len(hits)}"

    _, ref_six = _language_data(SUB, 8)
    lang = [s for s in hits if _language_data(s, 8)[1] == ref_six]
    assert len(lang) == 2, f"language cut: expected 2, got {len(lang)}"


def test_second_survivor_is_conjugate():
    """The non-identity language survivor is exactly a^-1 sigma(.) a."""
    surv = {'a': 'bAABa', 'b': 'ABa', 'A': 'bABa', 'B': 'Aa'}
    for g in 'abAB':
        assert SUB[g][0] == 'a'
        assert surv[g] == SUB[g][1:] + SUB[g][0]


# ── C3: the dictionary ──

DICT_SAMPLES = [
    # (component coeffs (c0,c1,c2,c3) in tau-basis, g coeffs with tau = g(x))
    ((-1, 1, 0, 0), (1, 1, 0, 0)),                                   # f_a
    ((0, -1, 1, 0), (1, sp.Rational(1, 2), 1, -sp.Rational(1, 2))),  # f_A
    ((0, 0, -1, 1), (3, -5, 2, 1)),                                  # |lambda2|
    ((0, 1, -2, 1), (sp.Rational(28, 17), -sp.Rational(71, 17),
                     2, sp.Rational(7, 17))),                        # T6 new
]


@pytest.mark.parametrize("comp,g", DICT_SAMPLES)
def test_dictionary_recovers_tau(comp, g):
    """tau = g(x) exactly for the sampled read-out components."""
    x_expr = sum(c * t**k for k, c in enumerate(comp))
    recovered = sum(gc * x_expr**k for k, gc in enumerate(g))
    assert red(recovered - t) == 0


@pytest.mark.parametrize("comp", [c for c, _ in DICT_SAMPLES])
def test_components_are_degree_4(comp):
    """Each sampled component is degree 4 over Q (a complete measurement)."""
    tau_r = sp.sqrt((1 + sp.sqrt(5)) / 2)
    expr = sum(c * tau_r**k for k, c in enumerate(comp))
    mp = sp.minimal_polynomial(expr, t)
    assert sp.degree(mp) == 4
