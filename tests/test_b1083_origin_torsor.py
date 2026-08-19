"""B1083 lock: the origin torsor typed — the arrow is not a torsor bit."""
from itertools import product

def _apply(r, w): return ''.join(r[c] for c in w)
def _rev(w): return w[::-1]
def _swap(w): return w.translate(str.maketrans('ab', 'ba'))
def _conj(op, r): return {c: op(r[op(c)]) for c in 'ab'}

BASE = {'a': 'ab', 'b': 'a'}

def test_k4_orbit_free_transitive():
    orbit = [BASE, _conj(_rev, BASE), _conj(_swap, BASE), _conj(_rev, _conj(_swap, BASE))]
    assert len({(r['a'], r['b']) for r in orbit}) == 4

def test_arrow_not_a_torsor_bit():
    orbit = [BASE, _conj(_rev, BASE), _conj(_swap, BASE), _conj(_rev, _conj(_swap, BASE))]
    for r in orbit:
        assert set(r['a'] + r['b']) <= set('ab'), "a K4 element produced a non-forward rule"

def _has_preimage(target, maxlen=8):
    for L in range(1, maxlen + 1):
        for w in product('ab', repeat=L):
            if _apply(BASE, ''.join(w)) == target:
                return True
    return False

def test_arrow_lives_in_nonsurjectivity():
    assert not _has_preimage('bb')
    assert _has_preimage('aaa')  # sigma(bbb) = aaa

def test_tick_squares_to_monodromy():
    M = [[1, 1], [1, 0]]
    det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    M2 = [[sum(M[i][k]*M[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    assert det == -1
    assert M2 == [[2, 1], [1, 1]]           # = RL, the figure-eight monodromy
    assert M2[0][0] + M2[1][1] == 3          # trace 3, t^2 - 3t + 1
