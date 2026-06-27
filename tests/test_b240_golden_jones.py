"""B240 locks -- the golden integrality of the figure-eight's colored Jones (object-specific, golden-specific).
Firewall: dimensionless quantum-invariant fact; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B240_golden_jones_integrality" / "golden_jones.py"
_spec = importlib.util.spec_from_file_location("b240_gj", _PATH)
b240 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b240)


def test_golden_integrality():
    pr = b240.products_at_root(5)
    assert b240.is_integer_vector(pr)
    assert [round(p.real) for p in pr] == [1, -2, -2, 1]


def test_J2_is_minus_two_over_phi():
    import cmath
    import numpy as np
    q = cmath.exp(2j * np.pi / 5)
    assert abs(b240.colored_jones_fig8(2, q) - (-2 / b240.PHI)) < 1e-9
    assert abs(b240.colored_jones_fig8(2, q) - (1 - 5 ** 0.5)) < 1e-9


def test_golden_and_amphicheiral_specific():
    import cmath
    import numpy as np
    assert not b240.is_integer_vector(b240.products_at_root(8))    # other root: not integral
    assert not b240.is_integer_vector(b240.products_at_root(13))
    q = cmath.exp(2j * np.pi / 5)
    tref = [b240.qdim(N, 3) * b240.colored_jones_trefoil(N, q) for N in range(1, 5)]
    assert not b240.is_integer_vector(tref)                        # chiral knot: complex -> not integral
