"""Lock for B555 — THE PREDICTION (exact internal consistency)."""
import numpy as np

phi = (1 + np.sqrt(5)) / 2
tau = np.sqrt(phi)
S = phi + 1 + phi*tau + tau
F = {'a': phi/S, 'b': 1/S, 'A': phi*tau/S, 'B': tau/S}


def test_one_measurement_law_exact():
    """f_A = tau*f_a and (f_a+f_b) = tau^2*f_a exactly."""
    assert abs(F['A'] - tau*F['a']) < 1e-12
    assert abs((F['a']+F['b']) - tau**2*F['a']) < 1e-12
    assert abs(F['a'] - (tau-1)) < 1e-12          # f_a = tau-1, the anchor


def test_degree4_off_golden_lattice():
    """Every predicted label sits >1e-2 off Z+Z/phi (the degree-4 signature)."""
    for v in [F['b'], F['B'], F['a'], F['A'], F['a']+F['b']]:
        x = min(v, 1-v)
        d = min(abs((P + Q/phi) % 1 - x) for P in range(-6, 7) for Q in range(-6, 7))
        assert d > 1e-2


def test_silver_control_disjoint():
    """A silver label is not a dictionary value (control discriminates)."""
    ag = 1 + np.sqrt(2)
    silver = 1/ag
    assert all(abs(silver - v) > 1e-2 for v in [F['b'], F['B'], F['a'], F['A']])
