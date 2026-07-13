"""
B568-PQ lock: "Why do you persist?" — the persistence mechanism of sigma4.
Locks: seed-invariant, primitivity, Perron charpoly, R(n) n=1..8,
fixed-point uniqueness (lambda=0), and the Z/11 charge line.
Run: python3 test_pq.py   (needs numpy, sympy). All PASS as of B568-PQ.
"""
import numpy as np, sympy as sp

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
LET = ['a', 'b', 'A', 'B']


def test_seed_invariant():
    for x in LET:                      # 'a' once, at position 0, in EVERY image
        assert SUB[x][0] == 'a', x
        assert SUB[x].count('a') == 1, x
    assert min(len(SUB[x]) for x in LET) == 2   # cannot shrink (sigma(B)=aA)


def test_primitivity():
    M = np.array([[SUB[c].count(r) for c in LET] for r in LET], dtype=object)
    assert np.all(M.dot(M) > 0)        # M^2 entrywise positive => primitive


def test_perron_charpoly():
    M = sp.Matrix([[SUB[c].count(r) for c in LET] for r in LET])
    cp = sp.expand(M.charpoly().as_expr()); x = list(cp.free_symbols)[0]
    assert cp == x**4 - 2*x**3 - 5*x**2 - 4*x - 1
    beta = max(float(sp.re(r)) for r in sp.nroots(cp))
    assert abs(beta - 3.6762050160213873) < 1e-10   # Perron > 1


def _codes(k):
    C = {'a': 0, 'b': 1, 'A': 2, 'B': 3}
    w = 'a'
    for _ in range(k):
        w = ''.join(SUB[c] for c in w)
    return np.frombuffer(bytes(C[c] for c in w), dtype=np.uint8).astype(np.int64)


def _R(C, n):
    # R(n) = (max interior gap between consecutive occurrences of any length-n factor) + n - 1
    m = len(C) - n + 1
    fac = np.zeros(m, dtype=np.int64)
    for j in range(n):
        fac = fac * 4 + C[j:j + m]
    order = np.argsort(fac, kind='stable')
    sf, sp_ = fac[order], order
    same = sf[1:] == sf[:-1]
    return int((sp_[1:] - sp_[:-1])[same].max()) + n - 1


def test_recurrence_function_1_to_8():
    C = _codes(11)                     # 2.2M prefix, saturated for n<=8
    expected = {1: 8, 2: 28, 3: 31, 4: 32, 5: 102, 6: 103, 7: 104, 8: 105}
    for n, val in expected.items():
        assert _R(C, n) == val, (n, _R(C, n), val)


def test_fixed_point_uniqueness():
    l = sp.symbols('lambda', nonnegative=True)   # void is the only self-model fixed point
    assert sp.solve(sp.Eq(l * (1 + sp.sqrt(l)), l), l) == [0]


def test_charge_line_z11():
    M = sp.Matrix([[SUB[c].count(r) for c in LET] for r in LET])
    assert abs((sp.eye(4) - M).det()) == 11      # coker(I-M) = Z/11


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_') and callable(fn):
            fn(); print('PASS', name)
    print('ALL PASS')