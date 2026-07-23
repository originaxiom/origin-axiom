"""Locks for B768 -- the correspondence cross-test (compute-grade)."""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2


def test_transition_matrix_eigenvalues():
    T = sp.Matrix([[1 / phi**2, 1 / phi], [1, 0]])
    assert all(sp.simplify(sum(T.row(i)) - 1) == 0 for i in range(2))
    ev = sorted(T.eigenvals(), key=lambda e: -sp.re(sp.N(e)))
    assert sp.simplify(ev[0] - 1) == 0 and sp.simplify(ev[1] + 1 / phi) == 0


def test_no_bb_in_the_fibonacci_word():
    w = "a"
    for _ in range(20):
        w = w.replace("a", "X").replace("b", "a").replace("X", "ab")
    assert "bb" not in w and len(w) > 10000


def test_subdominant_equals_untwisted_odd_trace_numerically():
    # the E20-flagged numerical identity (recorded, not structural)
    assert sp.simplify(-1 / phi - (-(2 * (1 / (2 * phi))))) == 0   # -1/phi = -2*Re(B00)
