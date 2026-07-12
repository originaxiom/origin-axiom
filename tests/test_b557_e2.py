"""Locks for B557 E2 — escalator rule uniqueness."""
import sympy as sp

x = sp.Symbol('x')
F = sp.Matrix([[1, 1], [1, 0]])
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
M4 = sp.Matrix([[SUB[c].count(r) for c in 'abAB'] for r in 'abAB'])


def _couple(M, C, D):
    return sp.Matrix(sp.BlockMatrix([[M, C], [D, M]]))


def test_MM2_uniquely_gives_M4():
    """(F,F^2) and (F^2,F) reproduce M4's charpoly; other simple couplings don't."""
    m4 = sp.factor(M4.charpoly(x).as_expr())
    I2, F2 = sp.eye(2), F*F
    hits = []
    for name, (C, D) in {'(M,M2)': (F, F2), '(M2,M)': (F2, F),
                         '(I,M)': (I2, F), '(M,I)': (F, I2),
                         '(I,M2)': (I2, F2), '(M,M)': (F, F)}.items():
        if sp.factor(_couple(F, C, D).charpoly(x).as_expr()) == m4:
            hits.append(name)
    assert set(hits) == {'(M,M2)', '(M2,M)'}


def test_field_doubling_needs_odd_sum():
    """Coupling (I,M) [p+q=1] also doubles -> (M,M^2) is not the unique doubler."""
    I2, F2 = sp.eye(2), F*F
    # (I,M): irreducible degree-4 (a different doubler)
    cp = sp.factor(_couple(F, I2, F).charpoly(x).as_expr())
    fl = sp.factor_list(cp)[1]
    assert len(fl) == 1 and fl[0][1] == 1        # irreducible -> genuine doubler
    # (M,M) [p+q=2, even]: reducible (no doubling)
    cp2 = sp.factor(_couple(F, F, F).charpoly(x).as_expr())
    assert len(sp.factor_list(cp2)[1]) > 1
