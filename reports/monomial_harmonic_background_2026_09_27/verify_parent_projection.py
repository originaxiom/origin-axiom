"""Full-parent projection controls; independent literal E8-root realization."""
from pathlib import Path
import sys
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "m6_parent_admission_2026_09_27"))
import verify_parent_admission as parent


def projection_control():
    gauge, structure = parent.bases_twice()
    b = sp.Matrix.hstack(*(sp.Matrix(v) for v in structure))
    g = sp.Matrix.hstack(*(sp.Matrix(v) for v in gauge))
    pi = b*(b.T*b).inv()*b.T
    roots = {tuple(v) for v in parent.roots_twice()}
    assert pi*pi == pi and pi.T == pi and pi.rank() == 4
    assert pi*g == sp.zeros(8, 4) and pi*b == b
    for column in range(4):
        v = b[:, column]
        reflection = sp.eye(8)-2*v*v.T/(v.T*v)[0]
        assert pi*reflection == reflection*pi
        assert {tuple(reflection*sp.Matrix(r)) for r in roots} == roots
    counterexamples = 0
    for root in roots:
        v = sp.Matrix(root)
        reflection = sp.eye(8)-2*v*v.T/(v.T*v)[0]
        counterexamples += int(pi*reflection != reflection*pi)
    assert counterexamples > 0
    return {"projection_rank": pi.rank(), "root_count": len(roots),
            "non_normalizing_reflections": counterexamples}


def actual_root_trace_control():
    _, structure = parent.bases_twice()
    x = list(sp.symbols("x0:4"))
    x += [-sum(x)]
    coefficients = [sum(x[:i+1]) for i in range(4)]
    trace = sum(sum(c*w for c, w in zip(coefficients, parent.dynkin(r, structure)))**2
                for r in parent.roots_twice())
    expected = 60*sum(a*a for a in x)
    assert sp.expand(trace-expected) == 0
    assert sp.expand(trace-30*sum(a*a for a in x)) != 0
    return 60


def direct_sum_gauge_control():
    d = sp.Matrix([[1, 0], [1, 1], [0, 1], [0, 0]])
    cocycle = sp.Matrix([0, 0, 0, 1])
    full = sp.diag(d, sp.eye(3))
    extended = cocycle.col_join(sp.zeros(3, 1))
    assert d.row_join(cocycle).rank() == d.rank()+1
    assert full.row_join(extended).rank() == full.rank()+1
    return True
