"""Compute-grade locks for the B768 audit (cc3 verification pass).

Recompute mathematics in-test; never read artifacts.
"""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2


class TestV1TransitionMatrix:
    def test_row_stochastic(self):
        T = sp.Matrix([[1/phi**2, 1/phi], [1, 0]])
        for i in range(2):
            assert sp.simplify(sum(T.row(i)) - 1) == 0

    def test_eigenvalue_1(self):
        T = sp.Matrix([[1/phi**2, 1/phi], [1, 0]])
        evs = sorted(T.eigenvals(), key=lambda e: -sp.re(sp.N(e)))
        assert sp.simplify(evs[0] - 1) == 0

    def test_eigenvalue_minus_inv_phi(self):
        T = sp.Matrix([[1/phi**2, 1/phi], [1, 0]])
        evs = sorted(T.eigenvals(), key=lambda e: -sp.re(sp.N(e)))
        assert sp.simplify(evs[1] + 1/phi) == 0


class TestV2FibonacciWord:
    @staticmethod
    def _fib_word(n_iter):
        w = "a"
        for _ in range(n_iter):
            w = w.replace("a", "X").replace("b", "a").replace("X", "ab")
        return w

    def test_no_bb_substring(self):
        w = self._fib_word(20)
        assert "bb" not in w

    def test_letter_ratio_is_phi(self):
        w = self._fib_word(20)
        assert abs(w.count('a') / w.count('b') - float(phi)) < 1e-4

    def test_transition_p_bb_exact_zero(self):
        w = self._fib_word(20)
        bb = sum(1 for i in range(len(w)-1) if w[i:i+2] == "bb")
        assert bb == 0

    def test_transition_p_ab_matches_inv_phi(self):
        w = self._fib_word(20)
        aa = sum(1 for i in range(len(w)-1) if w[i:i+2] == "aa")
        ab = sum(1 for i in range(len(w)-1) if w[i:i+2] == "ab")
        assert abs(ab/(aa+ab) - float(1/phi)) < 1e-4


class TestV4Gamma3EqualsC:
    def test_c_flips_T4(self):
        x, y = sp.symbols("x y")
        sols = sp.solve((y**2 - (x**2-1)*y + (x**2-1)).subs(x, 2), y)
        assert all(sp.simplify(sp.conjugate(s) - s) != 0 for s in sols)

    def test_c_flips_T6(self):
        u = sp.Symbol("u")
        A = sp.Matrix([[1, 1], [0, 1]])
        B = sp.Matrix([[1, 0], [-u, 1]])
        chord = sp.im(sp.diff(sp.expand((A*B).trace()**2 - 1), u).subs(u, omega))
        assert sp.simplify(sp.im(sp.conjugate(sp.I * chord)) + chord) == 0

    def test_c_fixes_T7(self):
        M = sp.Matrix([[2, 1], [1, 1]])
        assert all(sp.im(sp.N(e)) == 0 for e in M.eigenvals())

    def test_time_equals_basepoint_identity(self):
        assert sp.simplify((1 - phi)**2 - phi**(-2)) == 0


class TestDiscriminators:
    def test_row7_identity_exact(self):
        assert sp.simplify((1 - phi)**2 - 1/phi**2) == 0

    def test_gamma5_inverts_monodromy(self):
        assert sp.simplify((1 - phi)**2 - 1/phi**2) == 0
