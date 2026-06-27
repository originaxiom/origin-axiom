"""B243 locks -- level-rank=conjugation is universal across k (exact iff amphicheiral); the figure-eight's value
hits golden/silver at k=3,6 but the 'metallic ladder' breaks (bronze k=11 is non-quadratic). Firewall-clean."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B243_levelrank_conjugation_general" / "levelrank_general.py"
_spec = importlib.util.spec_from_file_location("b243", _PATH)
b243 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b243)


def test_mechanism_universal_across_levels():
    # figure-eight (amphicheiral): SU(2)_k = SU(k)_2 exactly for ALL k; trefoil (chiral): complex conjugates
    for k in range(2, 11):
        f2, fk = b243.levelrank_pair(b243.P_fig8, k)
        t2, tk = b243.levelrank_pair(b243.P_tref, k)
        assert abs(f2 - fk) < 1e-9                       # amphicheiral -> exact at every level
        assert abs(t2 - tk.conjugate()) < 1e-9           # chiral -> conjugates (level-rank = conjugation)


def test_golden_and_silver_values():
    assert abs(b243.fig8_value(3) - (-2 / b243.PHI)) < 1e-9     # k=3: golden -2/phi
    assert abs(b243.fig8_value(6) - (1 - 2 ** 0.5)) < 1e-9       # k=6: silver 1-sqrt2
    assert abs(b243.fig8_value(8)) < 1e-9                        # k=8: 0
    assert abs(b243.fig8_value(10) - (2 - 3 ** 0.5)) < 1e-9      # k=10: sqrt3


def test_ladder_breaks_bronze_not_in_Q_sqrt13():
    # bronze k=11 (kappa=13): V is degree 6 (Sage-verified) -> NOT a + b*sqrt13 for any small rationals.
    V = b243.fig8_value(11)
    s13 = 13 ** 0.5
    # exhaustive small-lattice check: no a+b*sqrt13 with |a|,|b| <= 8 over denominators <= 6 matches
    for den in range(1, 7):
        for an in range(-8 * den, 8 * den + 1):
            for bn in range(-8 * den, 8 * den + 1):
                if abs((an / den) + (bn / den) * s13 - V) < 1e-9:
                    raise AssertionError(f"unexpectedly in Q(sqrt13): {an}/{den} + {bn}/{den} sqrt13")
    # (and it is not rational either)
    assert min(abs(V - n) for n in range(-3, 4)) > 1e-6
