"""B232 locks -- the rho_n catalog stabilization recursion (R). Capped at n<=5 to stay fast (the symbolic
Sym^d char-polys for d>=7 are slow; the full n=8 run lives in the probe's __main__). Firewall: standalone
Lie/invariant theory; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B232_rho_n_plethysm" / "plethysm_recursion.py"
_spec = importlib.util.spec_from_file_location("b232_recursion", _PATH)
b232 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b232)


def test_recursion_holds_for_formula_n3_to_5():
    """(R): tower(n) == tower(n-1) * Sym^n * Sym^{n-3}, symbolic in m, n=3..5."""
    for n in (3, 4, 5):
        assert b232.recursion_holds_formula(n)


def test_recursion_holds_on_real_jacobian():
    """(R) on the proved (n=4) / structural (n=5) tower -- the ACTUAL Jacobian obeys the stabilization."""
    assert b232.recursion_holds_real(4)
    assert b232.recursion_holds_real(5)


def test_cohomological_route_violates_recursion():
    """adversarial: the foreclosed char(M)^{n^2-1} does NOT obey (R) -> (R) selects the true tower."""
    for n in (3, 4, 5):
        assert b232.cohomological_breaks_recursion(n)


def test_dimension_is_n2_minus_1():
    import sympy as sp
    for n in (3, 4, 5):
        assert sp.degree(b232.sym_tower(n), b232.t) == n * n - 1
