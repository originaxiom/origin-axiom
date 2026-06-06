"""B98 (Probe 1) -- locking tests: the figure-eight trace-map Jacobian at the GEOMETRIC rep is
(t-1)(t^2-5t+1) (NOT the Dickson tower), reproducing the adjoint torsion tau_1=-3 (the trivial-rep tower
and the geometric-rep torsion are different objects); and the tower != the Kostant principal-sl(2)
branching."""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b98", _ROOT / "frontier" / "B98_geometric_jacobian" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_geometric_fixed_point_in_trace_field():
    """x_geom = (3+sqrt(-3))/2 satisfies x^2-3x+3=0 (the figure-eight trace field Q(sqrt-3))."""
    xg = B.geometric_fixed_point()
    assert sp.simplify(xg**2 - 3 * xg + 3) == 0


def test_geometric_jacobian_is_torsion_not_tower():
    """char(D T_1^2)|_geom = (t-1)(t^2-5t+1); the transverse quadratic gives the adjoint torsion -3, and
    is NOT a Dickson char(M_1^k) (the tower is a trivial-rep object)."""
    t = sp.symbols("t")
    assert sp.expand(B.char_at_geometric() - (t - 1) * (t**2 - 5 * t + 1)) == 0
    assert B.torsion_from_geometric_jacobian() == -3
    # t^2-5t+1 is not any Dickson char(M_1^k)=t^2-L_k t+(-1)^k for M_1=[[1,1],[1,0]] (Lucas L_k != 5 with +1)
    M = sp.Matrix([[1, 1], [1, 0]])
    lucas = {int(sp.trace(M**k)) for k in range(1, 9)}
    assert 5 not in lucas                                  # no Dickson factor is t^2-5t+1


def test_tower_is_not_kostant_branching():
    for n in (3, 4):
        kostant, tower, same = B.tower_vs_kostant(n)
        assert same is False                              # tower != even-only Sym^{2k} (Kostant)
