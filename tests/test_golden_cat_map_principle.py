"""Lock for the unifying principle: the E6 torsion = the cat map's periodic-point product."""
import sympy as sp
def F(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def test_torsion_equals_periodic_points():
    A = sp.Matrix([[2, 1], [1, 1]])
    I = sp.eye(2)
    for j in range(1, 7):
        assert abs((A**(2*j) - I).det()) == 5*F(2*j)**2  # #Fix(A^{2j}) = 5 F_{2j}^2
