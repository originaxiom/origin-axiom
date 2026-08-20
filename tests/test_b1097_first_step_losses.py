"""B1097 lock: the first-step losses + the fired prediction's wall."""
import numpy as np

def _incidence(rule):
    M = [[0, 0], [0, 0]]
    for si, s in enumerate("ab"):
        for ch in rule[s]:
            M["ab".index(ch)][si] += 1
    return M

def test_order_loss_and_bite_control():
    assert _incidence({"a": "ab", "b": "a"}) == _incidence({"a": "ba", "b": "a"})
    assert _incidence({"a": "aab", "b": "a"}) != _incidence({"a": "ab", "b": "a"})

def test_sign_loss_and_phi1_minus_I():
    M = np.array([[1, 1], [1, 0]])
    M2 = M @ M
    assert round(np.linalg.det(M)) == -1
    assert round(np.linalg.det(M2)) == 1
    assert (M2 == np.array([[2, 1], [1, 1]])).all()
    assert (M2 - np.eye(2, dtype=int) == M).all()

def test_the_fired_prediction_wall_exists():
    # the M-vs-M^2 wall = B1095's even/odd-window breaking (its lock carries the numbers);
    # here: the reversal identity's parity dependence in miniature (F_7=13 vs F_8=21)
    from math import floor
    PHI = (1 + 5 ** 0.5) / 2
    A = 2 - PHI
    def bi(n, rho):
        return 1 if floor((n + 1) * A + rho) - floor(n * A + rho) else 0
    for N, expect in ((13, False), (21, True), (34, False), (55, True)):
        r = [bi(n, A) for n in range(N)]
        l = [bi(-n - 1, A) for n in range(N)]
        assert (l == r[::-1]) == expect    # closes at alternating Fibonacci indices
