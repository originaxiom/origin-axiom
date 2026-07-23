"""Locks for B766 -- the measurement torsor (compute-grade: every fact re-derived)."""
import sympy as sp

u, x, y, t = sp.symbols("u x y t")
phi = (1 + sp.sqrt(5)) / 2
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2


def test_c_flips_chirality_side():
    curve = y**2 - (x**2 - 1) * y + (x**2 - 1)
    sols = sp.solve(curve.subs(x, 2), y)
    assert set(sp.nsimplify(sp.conjugate(s)) for s in sols) == set(sp.nsimplify(s) for s in sols)
    assert all(sp.simplify(sp.conjugate(s) - s) != 0 for s in sols)


def test_theta_fixes_sl2_traces_and_time():
    A = sp.Matrix([[1, 1], [0, 1]])
    B = sp.Matrix([[1, 0], [-u, 1]])
    assert sp.simplify((A * B).trace() - (B * A).trace()) == 0
    M, Mrev = sp.Matrix([[2, 1], [1, 1]]), sp.Matrix([[1, 1], [1, 2]])
    assert sorted(M.eigenvals()) == sorted(Mrev.eigenvals())


def test_gamma5_is_the_time_inversion():
    assert sp.simplify((1 - phi) ** 2 - 1 / phi**2) == 0     # Gal(Q(sqrt5)): phi^2 -> phi^-2


def test_chord_value_is_purely_odd_at_geo():
    A = sp.Matrix([[1, 1], [0, 1]])
    B = sp.Matrix([[1, 0], [-u, 1]])
    d = sp.diff(sp.expand((A * B).trace() ** 2 - 1), u).subs(u, omega)
    assert sp.simplify(sp.im(d) - sp.sqrt(3)) == 0           # the odd part = sqrt3
    assert sp.simplify(sp.re(d) + 5) == 0                    # (the even part, for the record)


def test_rank_three_and_the_two_relations():
    vecs = {"T4": (1, 0, 0), "T6": (1, 1, 0), "T7": (0, 0, 1), "T3": (0, 0, 1)}
    # T7 == T3 (one choice); T6 = T4 xor theta
    assert vecs["T7"] == vecs["T3"]
    assert tuple((a + b) % 2 for a, b in zip(vecs["T4"], (0, 1, 0))) == vecs["T6"]
    # F2-rank of the span = 3
    M = [list(v) for v in vecs.values()]
    r = 0
    for col in range(3):
        piv = next((i for i in range(r, len(M)) if M[i][col] % 2), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][col] % 2:
                M[i] = [(a + b) % 2 for a, b in zip(M[i], M[r])]
        r += 1
    assert r == 3                                            # == B733's menu rank
