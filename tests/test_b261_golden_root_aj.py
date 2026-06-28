"""B261 locks -- the golden-root AJ operator: at q=zeta_5 the colored-Jones recursion degenerates to a finite
antiperiod-5 one ([N]J_N = {1,-2,-2,1,0|...}, extending B240), and the Coulomb branch at the golden meridian lands
the longitude in Q(sqrt5) (L+1/L = -phi^3). The two ends are two regimes of one recursion. FIREWALLED; nothing to
CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B261_golden_root_aj" / "golden_root_aj.py"
_spec = importlib.util.spec_from_file_location("b261", _PATH)
b261 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b261)


def test_golden_root_periodicity_extends_b240():
    seq = b261.golden_root_sequence(15)
    assert seq[:4] == [1, -2, -2, 1]                       # the B240 seed
    assert all(seq[N + 5] == -seq[N] for N in range(10))   # antiperiod 5 (the recursion degenerates)
    assert all(seq[N + 10] == seq[N] for N in range(5))    # period 10


def test_golden_meridian_longitude_in_q_sqrt5():
    LpL = b261.golden_meridian_longitude()
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(LpL - (-(2 + sp.sqrt(5)))) == 0     # L + 1/L = -(2+sqrt5)
    assert sp.simplify(LpL + phi**3) == 0                  # = -phi^3, in Q(sqrt5)
