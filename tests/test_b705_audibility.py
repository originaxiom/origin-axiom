"""B705 lock — the Jones-at-zeta_5 audibility calibration (pyenv-pure)."""
import sympy as sp

def test_fig8_jones_at_zeta5_is_golden_real():
    t = sp.exp(2 * sp.I * sp.pi / 5)
    V = t**(-2) - t**(-1) + 1 - t + t**2          # figure-eight Jones
    assert abs(complex(V) - (1 - 5**0.5)) < 1e-9  # = 1 - sqrt5 = -2/phi, REAL golden
    assert abs(complex(V).imag) < 1e-9            # real -> in Q(sqrt5) -> hears

def test_audibility_law_p_mod4():
    for p in (5, 7, 11, 13):
        star = ((-1) ** ((p - 1) // 2)) * p
        assert (star > 0) == (p % 4 == 1)         # audible <=> real <=> p=1 mod4
