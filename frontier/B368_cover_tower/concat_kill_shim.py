"""Shared single-seed readout (the B369 construction, importable without B369's run)."""
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B358 = os.path.join(HERE, "..", "B358_seam_certification")
sys.path.insert(0, B358)
import cyclo_engine as E                              # noqa: E402
import seam_certification as SC                       # noqa: E402

N = 15


def single_readout(powers):
    """{a: (p,q,r,s)} for the nonzero tr(Par * P_a), exactly."""
    o = len(powers)
    z = 60 // o
    par_tr = []
    for j in range(o):
        t = E.ZERO
        for x in range(N):
            t = E.add(t, powers[j][(-x) % N][x])
        par_tr.append(t)
    out = {}
    for a in range(o):
        t = E.ZERO
        for j in range(o):
            t = E.add(t, E.mul(E.zeta((-z * j * a) % 60), par_tr[j]))
        t = E.scal(Fr(1, o), t)
        if t == E.ZERO:
            continue
        sol = SC.solve_H(SC.H_avg(t))
        assert sol is not None, ("outside H", a)
        out[a] = sol
    return out
