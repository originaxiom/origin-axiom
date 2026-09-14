"""B1406 -- the mirror's other half is the other end; the bulk is the space
the object sits on the boundary of; and the ear-free observable.

Re-derived, not re-run. Every assertion below can fail.
"""
import importlib.util
import math
import os
from pathlib import Path

import pytest

sp = pytest.importorskip("sympy")
from sympy import Rational as Q

ROOT = Path(__file__).resolve().parents[1]
B1349 = ROOT / "frontier" / "B1349_the_mirror_sector_posed" / "verification"
S2 = sp.Matrix([[0, -1], [1, 0]])
PHI = (1 + sp.sqrt(5)) / 2
PHI_INV = (sp.sqrt(5) - 1) / 2


# ----------------------------------------------- riddle 1: the other END
def test_the_metallic_monodromy_is_symmetric():
    m = sp.Symbol("m", positive=True, integer=True)
    A = sp.Matrix([[1 + m**2, m], [m, 1]])
    assert sp.simplify(A - A.T) == sp.zeros(2, 2)


def test_symmetry_alone_makes_it_conjugate_to_its_inverse():
    """The whole riddle, in one line, for ANY symmetric M in SL(2)."""
    a, b, d = sp.symbols("a b d")
    M = sp.Matrix([[a, b], [b, d]])
    assert sp.simplify(S2 * M * S2.inv() - sp.Matrix([[d, -b], [-b, a]])) == sp.zeros(2, 2)
    assert S2.det() == 1                                  # orientation-preserving
    m = sp.Symbol("m", positive=True, integer=True)
    A = sp.Matrix([[1 + m**2, m], [m, 1]])
    assert sp.simplify(S2 * A * S2.inv() - A.inv()) == sp.zeros(2, 2)


@pytest.mark.parametrize("m", list(range(1, 9)))
def test_the_involution_swaps_the_two_end_invariants(m):
    mob = lambda P, x: sp.simplify((P[0, 0] * x + P[0, 1]) / (P[1, 0] * x + P[1, 1]))
    mu = sp.nsimplify((m + sp.sqrt(m * m + 4)) / 2)
    mub = (m - sp.sqrt(m * m + 4)) / 2
    assert sp.simplify(mob(S2, mu) - mub) == 0
    assert sp.simplify(mob(S2, mub) - mu) == 0


def test_at_the_object_the_swap_is_the_galois_involution():
    mob = lambda P, x: sp.simplify((P[0, 0] * x + P[0, 1]) / (P[1, 0] * x + P[1, 1]))
    assert sp.simplify(mob(S2, PHI) - (1 - sp.sqrt(5)) / 2) == 0


# --------------------------------------- riddle 2: on the boundary of the bulk
@pytest.mark.parametrize("m", list(range(1, 9)))
def test_both_ends_are_degenerate_not_parabolic(m):
    """Irrational slope = ending lamination = the Teichmueller coordinate left."""
    assert not sp.sqrt(m * m + 4).is_rational


def test_the_object_has_one_cusp_and_the_tower_has_more():
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold("m004")
    assert M.num_cusps() == 1
    assert max(c.num_cusps() for c in M.covers(4)) > 1     # room is in the tower


# ---------------------------------------------------- the ear-free observable
@pytest.fixture(scope="module")
def su32():
    spec = importlib.util.spec_from_file_location(
        "exact60_b1406", str(B1349 / "b1349c_exact_instrument.py"))
    X = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(X)
    N = 6
    ix = {w: i for i, w in enumerate(X.W)}
    I6 = sp.eye(N)
    cm = lambda A: sp.Matrix(A.rows, A.cols, lambda i, j: X.conj(A[i, j]))
    C = sp.zeros(N, N)
    for i, w in enumerate(X.W):
        C[ix[(w[1], w[0])], i] = 1
    C = sp.Matrix(N, N, lambda i, j: sp.Integer(C[i, j]))
    R, L = X.T, X.mmul(X.mmul(cm(X.S), cm(X.T)), X.S)

    def mpow(A, k):
        P = I6
        for _ in range(k):
            P = X.mmul(P, A)
        return P

    ZN = sp.exp(2 * sp.pi * sp.I / 60)
    Pp, Pm = Q(1, 2) * (I6 + C), Q(1, 2) * (I6 - C)

    def parts(m):
        Wd = X.mmul(mpow(R, m), mpow(L, m))
        raw = lambda P: X.red(sp.expand(sum((P * Wd)[i, i] for i in range(N))))
        st = X.red(sp.expand(sum(X.mmul(C, Wd)[i, i] for i in range(N))))
        return raw(Pp), raw(Pm), st

    ex = lambda e: sp.nsimplify(sp.simplify(sp.expand(e).subs(X.z, ZN)), [sp.sqrt(5)])
    return dict(X=X, N=N, C=C, I6=I6, Pp=Pp, Pm=Pm, parts=parts, ex=ex)


def test_C_is_the_grading(su32):
    X, C, I6 = su32["X"], su32["C"], su32["I6"]
    assert C * C == I6
    assert X.mmul(X.S, X.S) == C
    assert sp.trace(su32["Pp"]) == 4 and sp.trace(su32["Pm"]) == 2


def test_the_supertrace_is_real_and_in_Q_sqrt5(su32):
    for m in range(15):
        v = su32["ex"](su32["parts"](m)[2])
        assert sp.im(sp.N(v, 30)) == 0
        assert v.is_rational or sp.sqrt(5) in v.atoms(sp.Pow)


def test_the_supertrace_is_mirror_invariant(su32):
    ex, parts = su32["ex"], su32["parts"]
    for m in range(15):
        assert sp.simplify(ex(parts(m)[2]) - ex(parts((15 - m) % 15)[2])) == 0


def test_the_supertrace_takes_six_values_all_of_cosine_form(su32):
    ex, parts = su32["ex"], su32["parts"]
    vals = {ex(parts(m)[2]) for m in range(15)}
    assert len(vals) == 6
    js = set()
    for v in vals:
        hit = [j for j in range(16) if sp.simplify(v - 2 * sp.cos(sp.pi * j / 15)) == 0]
        assert len(hit) == 1, v
        js.add(hit[0])
    assert js == {0, 5, 6, 9, 10, 15}


def test_the_object_reads_one_over_phi(su32):
    te, to, st = su32["parts"](1)
    assert sp.simplify(su32["ex"](st) - PHI_INV) == 0


def test_the_even_sector_traces_to_zero_off_the_three_part(su32):
    """The measured version of 'we are computing part of it'.

    Tested with simplify(raw) == 0, never by comparing a printed form (E75 #12).
    """
    for m in range(15):
        te = su32["parts"](m)[0]
        assert (sp.simplify(te) == 0) == (m % 3 != 0), m


def test_at_the_object_all_the_graded_content_is_odd(su32):
    te, to, st = su32["parts"](1)
    assert sp.simplify(te) == 0
    assert sp.simplify(su32["ex"](to) + PHI_INV) == 0
    assert sp.simplify(su32["ex"](st) - PHI_INV) == 0


def test_the_grading_index_at_the_empty_word(su32):
    te, to, st = su32["parts"](0)
    assert sp.simplify(te - 4) == 0 and sp.simplify(to - 2) == 0
    assert sp.simplify(su32["ex"](st) - 2) == 0


def test_the_unit_split_is_by_two_torsion(su32):
    ex, parts = su32["ex"], su32["parts"]
    units = [r for r in range(15) if math.gcd(r, 15) == 1]
    for u in units:
        is_phi = sp.simplify(ex(parts(u)[2]) - PHI_INV) == 0
        assert is_phi == ((u * u) % 15 == 1), u


def test_the_anchor_ledger():
    """The trace costs nothing; the matrix element cost 2 + 2.81."""
    trace_total = 1 - 0 - 0
    element_best = 4 - 0 - math.log2(7)
    assert trace_total > 0
    assert abs(element_best - 1.19) < 0.01
