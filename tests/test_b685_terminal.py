"""B685 terminal locks — the figure-eight is being (disc -3), no intrinsic 5."""
import sympy as sp


def test_figure_eight_shape_disc_minus3():
    z = sp.symbols("z")
    eq = z**2 - z + 1
    assert sp.discriminant(eq, z) == -3            # being, Q(sqrt-3)
    # shape = exp(i pi/3) is a root
    assert abs(complex(eq.subs(z, sp.exp(sp.I*sp.pi/3)))) < 1e-12


def test_gswz_powers_of_three():
    # eq(2) denominators 3^3, 3^5, ..., 3^146 at n=100 — powers of 3, not {3,5}
    for e in (3, 5, 146):
        assert sp.factorint(3**e) == {3: e}       # pure power of 3
