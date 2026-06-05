"""B68 / Path E (V59) -- locking test for the smarter AJ retry (confirms the V52 bounded negative).

Locks: (1) the Habiro cyclotomic J_N reproduces the figure-eight Jones polynomial (J_2); (2) at
well-conditioned |q|=1, NO consistent homogeneous order-<=2 recursion exists at generic q (Q-degree
<=4) -- the V52 result, via the independent numeric route."""
import math
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b68_cyc", _ROOT / "frontier" / "B68_aj_conjecture" / "cyclotomic_numeric.py")
cyc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cyc)


def test_habiro_reproduces_figure_eight_jones():
    """J_2 (Habiro) = q^-2 - q^-1 + 1 - q + q^2, the figure-eight Jones polynomial."""
    for t in (0.7, 1.9, 2.7):
        qv = complex(math.cos(t), math.sin(t))
        jp = qv ** -2 - qv ** -1 + 1 - qv + qv ** 2
        assert abs(cyc.J_value(2, qv) - jp) < 1e-12, t


def test_no_homogeneous_order2_recursion_generic_q():
    """No consistent homogeneous order-<=2 recursion at generic |q|=1 (DQ<=4) -- confirms V52."""
    for order in (1, 2):
        for DQ in (2, 3, 4):
            dims = [cyc.nullspace_dim(order, DQ, qv) for qv in cyc.GENERIC_Q]
            assert dims == [0] * len(cyc.GENERIC_Q), (order, DQ, dims)
