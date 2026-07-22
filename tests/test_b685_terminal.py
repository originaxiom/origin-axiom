"""B685 terminal locks — the figure-eight is being (disc -3), no intrinsic 5."""
import sympy as sp


def test_figure_eight_shape_disc_minus3():
    z = sp.symbols("z")
    eq = z**2 - z + 1
    assert sp.discriminant(eq, z) == -3            # being, Q(sqrt-3)
    # shape = exp(i pi/3) is a root
    assert abs(complex(eq.subs(z, sp.exp(sp.I*sp.pi/3)))) < 1e-12


def test_gswz_powers_of_three():
    """REPLACED 2026-07-22 (B755 cell 3): the original assertion factorint(3**e)=={3:e}
    was VACUOUS (could never fail -- MB12 signature, flagged by the fact_computed sweep).
    The REAL computation now lives in tests/test_b755_carried.py::
    test_cell3_b685_gswz_gates_and_pure3 (the Kashaev-sum extraction reproduces the
    GSWZ eq (1) coefficients and the exact symmetrized product verifies pure-3
    denominators through u^5, matching all four printed eq (2) values).  This stub
    asserts the replacement exists so the suite fails loudly if it is ever removed."""
    import os
    path = os.path.join(os.path.dirname(__file__), "test_b755_carried.py")
    assert os.path.exists(path)
    text = open(path, encoding="utf-8").read()
    assert "test_cell3_b685_gswz_gates_and_pure3" in text
