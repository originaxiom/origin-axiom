"""B71 -- SL(3) figure-eight character variety from the trace-map fixed locus (B0-B1).

Locks: (1) the T_1^2 fixed-locus linear identifications; (2) the exact 3-component decomposition
of Fix(T_1^2) (each dim 2); (3) the Sym^2 ground-truth family lands on the geometric component V0.
"""
import importlib.util
import pathlib

import numpy as np
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b71_probe", _ROOT / "frontier" / "B71_sl3_apoly" / "probe.py")
b71 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b71)


def test_fixed_locus_linear_identifications():
    """Fix(T_1^2) forces x3=x2, x8=x5, x6=x4, x7=x1 (the 4 degree-1 consequences)."""
    x1, x2, x3, x4, x5, x6, x7, x8 = b71.X8
    eqs = b71.fixed_locus_equations()
    linear = {sp.factor(e) for e in eqs if sp.Poly(e, *b71.X8).total_degree() == 1}
    assert linear == {sp.factor(x3 - x2), sp.factor(x8 - x5),
                      sp.factor(x4 - x6), sp.factor(x1 - x7)}


def test_three_components_are_fixed():
    """V0, W1, W2 are each pointwise fixed by T_1^2 (contained in Fix(T_1^2))."""
    for _nm, (_params, coord) in b71.components().items():
        assert all(sp.expand(a - b) == 0 for a, b in zip(b71.T1_sq(coord), coord))


def test_decomposition_is_exact():
    """The reduced ideal's nonlinear part factors as (x1-x4)(x2-1), (x1-x4)(x5-1) + two cubics;
    the case split (x1=x4) | (x2=1,x5=1) yields exactly the three listed components and no other
    top-dimensional piece (lex Groebner basis has the two product generators)."""
    x1, x2, x4, x5 = sp.symbols("x1 x2 x4 x5")
    lin = dict(zip(b71.X8, (x1, x2, x2, x4, x5, x4, x1, x5)))  # apply x3=x2,x6=x4,x7=x1,x8=x5
    red = [sp.expand(e.subs(lin)) for e in b71.fixed_locus_equations()]
    red = [e for e in red if e != 0]
    G = sp.groebner(red, x1, x2, x4, x5, order="lex")
    factored = {sp.factor(g) for g in G}
    assert sp.factor((x1 - x4) * (x5 - 1)) in factored
    assert sp.factor((x2 - x5) * (x4 - 1)) in factored


def test_sym2_groundtruth_on_V0():
    """Sym^2 of the figure-eight SL(2) holonomy lands on V0 = {x1=x4, x2=x5}."""
    for xv in (3, 4, 5, 2.5, 7, -1, 0.3, 1.7, -2.5, 6, 8, 0.5 + 0.5j):
        c = b71.sym2_groundtruth_coords(xv)
        assert abs(c[0] - c[3]) + abs(c[1] - c[4]) < 1e-9


def test_sym2_is_T1sq_fixed():
    """The Sym^2 ground-truth character is fixed by the SL(3) trace map T_1^2 (extends over the
    bundle by functoriality) -- the numeric confirmation that T_1^2 is the figure-eight monodromy."""
    def T1_num(c):
        x1, x2, x3, x4, x5, x6, x7, x8 = c
        return np.array([x3, x1, x1 * x3 - x4 * x2 + x6, x8, x4, x5, x2,
                         x4 * x8 - x1 * x5 + x7], dtype=complex)
    for xv in (3, 4, 5, 2.5, 7, -1):
        c = b71.sym2_groundtruth_coords(xv)
        assert np.max(np.abs(T1_num(T1_num(c)) - c)) < 1e-8
