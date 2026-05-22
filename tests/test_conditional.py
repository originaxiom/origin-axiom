"""
Conditional claims C1-C4 (CLAIMS.md).

Each is true ONLY given a named assumption. These tests check the *conditional*
statement and nothing stronger. C1 (axioms force L, R) and C4 (an 11-manifold
census) are not independently computable here — they are documented in CLAIMS.md
with their assumptions.
"""

import sympy as sp

from origin_axiom.constants import PHI
from origin_axiom.topology import is_torsion_free_hyperbolic, unique_trace_three


def test_C2_fibonacci_F_squared_from_perron_eigenvector():
    """
    C2 — A's Perron eigenvector reconstructs the Fibonacci |F|^2 probability
    matrix. ASSUMPTION: the Perron-switch rule (ordered Perron weights 1:phi as
    stay:switch). Plain maximum entropy would instead give 1/2, 1/2.
    """
    stay = 1 / (1 + PHI)
    switch = PHI / (1 + PHI)
    reconstructed = sp.Matrix([[stay, switch], [switch, stay]])
    F_squared = sp.Matrix([[PHI**-2, PHI**-1], [PHI**-1, PHI**-2]])
    assert sp.simplify(reconstructed - F_squared) == sp.zeros(2, 2)


def test_C3_trace_three_sieve_within_its_scope():
    """
    C3 — trace 3 is the unique torsion-free hyperbolic trace, WITHIN the class
    of once-punctured-torus bundles with SL(2,Z) monodromy. The sieve does not
    claim anything outside that class.
    """
    assert unique_trace_three() == [3]
    assert is_torsion_free_hyperbolic(3)
