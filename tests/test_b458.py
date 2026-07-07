"""Lock for B458 — Ethogram E5: the fig-8 per-component complex volumes are zero
(except the geometric Sym^2 pair at exactly 4x the SL(2) volume)."""
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B458_ethogram_e5_component_cs")


def test_fig8_component_complex_volumes():
    import snappy
    from snappy.ptolemy.coordinates import PtolemyCoordinates
    M = snappy.Manifold('m004')
    V = M.ptolemy_variety(3, obstruction_class=0)
    vars_ = [str(v) for v in V.variables]
    R = sp.symbols(vars_)
    gens = dict(zip(vars_, R))
    eqs = [sp.sympify(str(e), locals=gens) for e in V.equations]
    sols = sp.solve(eqs, list(R), dict=True)
    section = V.py_eval_variable_dict()
    full_map = eval(section)
    geo, q7 = [], []
    for s in sols:
        num = {k: complex(sp.N(s[sp.Symbol(k)], 30)) for k in vars_}
        if any(abs(v) < 1e-12 for v in num.values()):
            continue
        mp_ = sp.minimal_polynomial(s[sp.Symbol(vars_[1])], sp.Symbol('t'))
        pc = PtolemyCoordinates(full_map(num), is_numerical=True, py_eval_section=None,
                                manifold_thunk=(lambda M=M: M))
        cv = complex(pc.complex_volume_numerical())
        if sp.degree(mp_) == 2 and sp.discriminant(mp_, sp.Symbol('t')) == -7:
            q7.append(cv)
        elif abs(cv.real) > 1:
            geo.append(cv)
    # the geometric Sym^2 pair: +-4*Vol(4_1), CS=0
    vol41 = 2.029883212819
    assert len(geo) == 2
    assert np.allclose(sorted(c.real for c in geo), [-4 * vol41, 4 * vol41], atol=1e-6)
    assert all(abs(c.imag) < 1e-9 for c in geo)
    # THE DECISIVE NUMBERS: the Q(sqrt-7) pair is complex-volume-trivial
    assert len(q7) == 2
    assert all(abs(c) < 1e-9 for c in q7)
