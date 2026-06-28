"""B245 locks -- higher-color level-rank duality for 4_1: SU(2)_k color-N (sym [N-1]) == SU(k)_2 transpose
(antisym [1^{N-1}]) exactly, all N,k>=N-1; reduced transpose symmetry H^antisym(A,q)=H^sym(A,1/q) confirmed from
the independent eq-8 antisymmetric formula. Firewall-clean."""
import importlib.util
import pathlib
import cmath

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B245_higher_color_levelrank" / "higher_color_levelrank.py"
_spec = importlib.util.spec_from_file_location("b245", _PATH)
b245 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b245)


def test_symmetric_formula_validated():
    # p=1 == fundamental HOMFLY  a^2+a^-2+1-q^2-q^-2
    A, q = cmath.exp(0.53j), cmath.exp(0.37j)
    assert abs(b245.H_sym(1, A, q) - (A**2 + A**-2 + 1 - q**2 - q**-2)) < 1e-12


def test_transpose_symmetry_independent():
    # antisymmetric eq-8 formula equals symmetric with q->1/q (reduced), and differs from q->q for p>=2
    A, q = cmath.exp(0.7j), cmath.exp(0.31j)
    for p in range(1, 5):
        assert abs(b245.H_antisym(p, A, q) - b245.H_sym(p, A, 1 / q)) < 1e-12
    assert abs(b245.H_antisym(2, A, q) - b245.H_sym(2, A, q)) > 1e-6


def test_higher_color_levelrank_exact():
    # exact (no phase) for every color N and level k>=N-1
    for N in range(2, 6):
        for k in range(max(2, N - 1), N + 3):
            su2, suk = b245.levelrank_higher(N, k)
            assert abs(su2 - suk) < 1e-9, f"N={N},k={k}"


def test_fundamental_self_transpose_reduces_to_b242():
    # N=2, k=3 reproduces the golden -2/phi of B242 (the fundamental self-transpose case)
    phi = (1 + 5 ** 0.5) / 2
    su2, suk = b245.levelrank_higher(2, 3)
    assert abs(su2 - (-2 / phi)) < 1e-9 and abs(suk - (-2 / phi)) < 1e-9
