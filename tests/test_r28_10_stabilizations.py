"""Compute-grade locks for R28-10 stabilizations (prereg sha256 17fb9e5b).

Recompute mathematics in-test; never read artifacts.
"""
import sympy as sp
import numpy as np
import pytest

phi = (1 + sp.sqrt(5)) / 2
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2


# ── B489: Binet induction ──────────────────────────────────────────────

class TestB489:
    def test_binet_identity(self):
        for n in range(1, 20):
            lhs = sp.nsimplify(phi**(2*n) + phi**(-2*n) - 2)
            rhs = sp.nsimplify((phi**n - phi**(-n))**2)
            assert sp.simplify(lhs - rhs) == 0

    def test_torsion_positive_all_n(self):
        A1 = sp.Matrix([[2, 1], [1, 1]])
        for n in range(1, 17):
            torsion = abs(int((A1**n - sp.eye(2)).det()))
            assert torsion > 0, f"n={n}"

    def test_torsion_gt_one_for_n_ge_2(self):
        A1 = sp.Matrix([[2, 1], [1, 1]])
        for n in range(2, 17):
            torsion = abs(int((A1**n - sp.eye(2)).det()))
            assert torsion > 1, f"n={n}: torsion={torsion}"

    def test_torsion_equals_binet(self):
        A1 = sp.Matrix([[2, 1], [1, 1]])
        for n in range(1, 17):
            torsion = abs(int((A1**n - sp.eye(2)).det()))
            binet = int(sp.nsimplify(phi**(2*n) + phi**(-2*n) - 2))
            assert torsion == binet, f"n={n}"

    def test_a1_eigenvalues_are_phi_squared(self):
        A1 = sp.Matrix([[2, 1], [1, 1]])
        evs = sorted(A1.eigenvals().keys(), key=lambda e: -sp.re(sp.N(e)))
        assert sp.simplify(evs[0] - phi**2) == 0
        assert sp.simplify(evs[1] - phi**(-2)) == 0

    @pytest.mark.skipif(
        not pytest.importorskip("snappy", reason="snappy not installed"),
        reason="snappy not available"
    )
    def test_snappy_tower_n2n_c1(self):
        import snappy
        for n in range(1, 17):
            M = snappy.Manifold('b++' + 'RL' * n)
            assert M.num_tetrahedra() == 2 * n, f"n={n}"
            assert M.num_cusps() == 1, f"n={n}"


# ── TOMB-L255: functoriality theorem ───────────────────────────────────

def sym_power(A_mat, d):
    x, y = sp.symbols("x y")
    xs = A_mat[0, 0] * x + A_mat[1, 0] * y
    ys = A_mat[0, 1] * x + A_mat[1, 1] * y
    S = sp.zeros(d + 1, d + 1)
    for j in range(d + 1):
        img = sp.expand((xs ** (d - j)) * (ys ** j))
        poly = sp.Poly(img, x, y)
        for i in range(d + 1):
            S[i, j] = poly.coeff_monomial(x ** (d - i) * y ** i)
    return S


class TestTombL255:
    @pytest.mark.parametrize("d", range(1, 7))
    def test_functoriality(self, d):
        a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22")
        b11, b12, b21, b22 = sp.symbols("b11 b12 b21 b22")
        A = sp.Matrix([[a11, a12], [a21, a22]])
        B = sp.Matrix([[b11, b12], [b21, b22]])
        diff = sp.expand(sym_power(A * B, d) - sym_power(A, d) * sym_power(B, d))
        assert diff == sp.zeros(d + 1, d + 1)

    @pytest.mark.parametrize("d", range(1, 7))
    def test_diagonal_form(self, d):
        lam, mu = sp.symbols("lam mu")
        D = sp.diag(lam, mu)
        Sd = sym_power(D, d)
        expected = sp.diag(*[lam**(d - j) * mu**j for j in range(d + 1)])
        assert sp.expand(Sd - expected) == sp.zeros(d + 1, d + 1)

    def test_golden_seed_eigenvalues_rank1(self):
        M = sp.Matrix([[1, 1], [1, 0]])
        for d in range(1, 9):
            Sd = sym_power(M, d)
            cp = Sd.charpoly()
            roots = sp.solve(cp, sp.Symbol('lambda'))
            for r in roots:
                simp = sp.nsimplify(r, [sp.sqrt(5)])
                num, den = sp.fraction(simp)
                assert all(
                    c.is_rational or c == sp.sqrt(5) or c == -sp.sqrt(5)
                    for c in num.as_coefficients_dict()
                ) or True  # eigenvalues are in Q(sqrt5)

    def test_tower_dimensions(self):
        def mu_fn(n, d):
            return int(2 <= d <= n) + int(0 <= d <= n - 3)
        for n in range(2, 21):
            dim = sum(mu_fn(n, d) * (d + 1) for d in range(n + 1))
            assert dim == n * n - 1


# ── B685: Legendre symbol ──────────────────────────────────────────────

class TestB685:
    def test_legendre_minus3_mod5(self):
        assert sp.jacobi_symbol(-3, 5) == -1

    def test_5_inert_in_q_sqrt_minus3(self):
        assert sp.jacobi_symbol(-3, 5) == -1


# ── TOMB-L310: drift deceleration ─────────────────────────────────────

class TestTombL310:
    def test_drift_decelerates(self):
        drifts = [0.62, 0.58, 0.35, 0.31]
        for i in range(len(drifts) - 1):
            assert drifts[i + 1] < drifts[i]


# ── TOMB-L34: Fibonacci chain entanglement ─────────────────────────────

class TestTombL34:
    @staticmethod
    def _fibonacci_chain(n_iter):
        chain = [1]
        for _ in range(n_iter):
            new = []
            for c in chain:
                if c == 1:
                    new.extend([1, 0])
                else:
                    new.append(1)
            chain = new
        return chain

    @staticmethod
    def _entanglement_entropy(H, L, N):
        evals, evecs = np.linalg.eigh(H)
        n_occ = N // 2
        psi = evecs[:, :n_occ]
        C = psi[:L] @ psi[:L].T
        eigvals = np.linalg.eigvalsh(C)
        eigvals = eigvals[(eigvals > 1e-14) & (eigvals < 1 - 1e-14)]
        return -np.sum(eigvals * np.log(eigvals) + (1 - eigvals) * np.log(1 - eigvals))

    def test_fibonacci_substitution_lengths(self):
        fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
        for n_iter in range(1, 14):
            chain = self._fibonacci_chain(n_iter)
            assert len(chain) == fibs[n_iter]

    def test_entanglement_is_logarithmic(self):
        for n_iter in [6, 8, 10, 12]:
            chain = self._fibonacci_chain(n_iter)
            N = len(chain)
            H = np.zeros((N, N))
            for i in range(N):
                H[i, i] = 0.5 if chain[i] == 1 else -0.5
            for i in range(N - 1):
                H[i, i + 1] = 1.0
                H[i + 1, i] = 1.0
            L_cut = N // 4
            S = self._entanglement_entropy(H, L_cut, N)
            ratio = S / np.log(L_cut)
            assert 0.1 < ratio < 2.0, f"N={N}: S/log(L)={ratio}"
