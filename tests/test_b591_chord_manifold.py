"""B591 — the chord's manifold (locks): the tone is the torsion.

H1(-A1 bundle) = Z + Z/5 (the golden tone's conductor as first homology);
plain-vs-twisted torsion = det(A-I) vs det(A+I) (B588's two conductors);
Delta(-1) = det(A+I) = 5; the monodromy-twisted complement-double is an
integral homology sphere. See frontier/B591_chord_manifold/FINDINGS.md.
"""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

A1 = sp.Matrix([[2, 1], [1, 1]])
A2 = sp.Matrix([[5, 2], [2, 1]])
A3 = sp.Matrix([[10, 3], [3, 1]])


def _h1(phi):
    d = smith_normal_form(sp.Matrix(phi) - sp.eye(2))
    tors = sorted(int(abs(d[i, i])) for i in range(2) if abs(d[i, i]) not in (0, 1))
    free = 1 + sum(1 for i in range(2) if d[i, i] == 0)
    return free, tors


def test_two_lifts_torsion():
    assert _h1(A1) == (1, [])            # golden plain: torsion-free (unit det(A-I))
    assert _h1(-A1) == (1, [5])          # the mirror twist carries the 5
    assert _h1(A2) == (1, [2, 2]) and _h1(-A2) == (1, [2, 4])
    assert _h1(A3) == (1, [3, 3]) and _h1(-A3) == (1, [13])


def test_conductors_are_the_torsions():
    for A in (A1, A2, A3):
        dminus = abs(int(sp.det(A - sp.eye(2))))
        dplus = abs(int(sp.det(A + sp.eye(2))))
        tp = _h1(A)[1]
        tm = _h1(-A)[1]
        assert (sp.prod(tp) if tp else 1) == (dminus if dminus != 1 else 1)
        assert sp.prod(tm) == dplus


def test_identity_of_the_five():
    t = sp.Symbol('t')
    Delta = sp.expand(sp.det(t * sp.eye(2) - A1))
    assert Delta == t ** 2 - 3 * t + 1
    assert Delta.subs(t, -1) == 5 == sp.det(A1 + sp.eye(2))


def test_twisted_double_is_homology_sphere():
    for g in (A1, -A1):
        a, b = int(g[0, 0]), int(g[0, 1])
        d = smith_normal_form(sp.Matrix([[1, -a], [0, b]]))
        tors = [int(abs(d[i, i])) for i in range(2) if abs(d[i, i]) not in (0, 1)]
        free = sum(1 for i in range(2) if d[i, i] == 0)
        assert free == 0 and not tors                 # H1 = 0


def test_branched_double_cover_snappy():
    import pytest
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold("4_1")
    M2 = M.covers(2, cover_type="cyclic")[0]
    assert M2.num_cusps() == 1
    M2.dehn_fill((1, 0))
    assert "Z/5" in str(M2.filled_triangulation().homology())
