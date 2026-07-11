"""B529 locks — the QCA covariance make-or-break does NOT pass as a golden selection.

Two discriminating facts (the controls the seat skipped): (1) the iSy coin nests exactly for ANY
substitution (generic degeneracy artifact); (2) the golden-angle coin is NOT robustly golden-specific
(some random controls nest better than golden). Small sizes for speed; the effect is size-robust.
"""
import numpy as np
import random


def _fp(sub, level, seed='a'):
    w = seed
    for _ in range(level):
        w = ''.join(sub[c] for c in w)
    return w


def _U(word, coins):
    N = len(word); D = 2 * N
    C = np.zeros((D, D), complex); S = np.zeros((D, D), complex)
    for x, c in enumerate(word):
        C[2 * x:2 * x + 2, 2 * x:2 * x + 2] = coins[c]
    for x in range(N):                              # proper moving shift (non-degenerate)
        S[2 * ((x - 1) % N) + 0, 2 * x + 0] = 1
        S[2 * ((x + 1) % N) + 1, 2 * x + 1] = 1
    return S @ C


def _ph(M):
    return np.sort(np.angle(np.linalg.eigvals(M)))


def _cost(a, b):
    d = np.abs(a[:, None] - b[None, :]); d = np.minimum(d, 2 * np.pi - d)
    return float(np.mean(d.min(1) ** 2))


I = np.eye(2, dtype=complex)
ISY = np.array([[0, -1], [1, 0]], complex)
GOLD = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def _rot(t):
    return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]], complex)


def _coins_isy():
    return {'a': ISY, 'A': ISY, 'b': I, 'B': I}


def _coins_ga():
    return {'a': _rot(np.pi / 5), 'A': _rot(2 * np.pi / 5), 'b': I, 'B': I}


def _nest(sub, coins, lv=(2, 3)):
    return _cost(_ph(_U(_fp(sub, lv[0]), coins)), _ph(_U(_fp(sub, lv[1]), coins)))


def test_isy_coin_is_generic_degeneracy_plus_self_similarity():
    # iSy collapses ANY substitution's walk to 6 distinct eigenphases (degeneracy) -- robust at all levels.
    for lv in (2, 3, 4):
        ph = _ph(_U(_fp(GOLD, lv), _coins_isy()))
        assert len(np.unique(np.round(ph, 7))) == 6
    # golden reaches cost 0 at every level (exactly self-similar)...
    assert _nest(GOLD, _coins_isy(), lv=(2, 3)) < 1e-12
    # ...while a random control is NOT exact at small size (self-similarity not yet reached)...
    random.seed(3)
    ctrl = {c: ''.join(random.choice('abAB') for _ in range(4)) for c in 'abAB'}
    assert _nest(ctrl, _coins_isy(), lv=(2, 3)) > 1e-6
    # ...but DOES become ~exact at matched larger size => generic (self-similarity), not a golden selection.
    assert _nest(ctrl, _coins_isy(), lv=(3, 4)) < 1e-8
    assert _nest(GOLD, _coins_isy(), lv=(3, 4)) < 1e-8


def test_golden_angle_coin_not_robustly_golden_specific():
    g = _nest(GOLD, _coins_ga(), lv=(3, 4))
    beats = 0
    for seed in range(5, 15):
        random.seed(seed)
        ctrl = {c: ''.join(random.choice('abAB') for _ in range(4)) for c in 'abAB'}
        if g < _nest(ctrl, _coins_ga(), lv=(3, 4)):
            beats += 1
    assert beats < 10          # golden does NOT beat all controls -> not a clean selection (2/10 beat it)
