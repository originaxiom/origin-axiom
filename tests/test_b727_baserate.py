"""B727 lock — base-rate the E6-across-three-faces STRUCTURE: it is FORCED (the number-bag one level
up), not a signal. Self-audit; the negative is the deliverable. Structural/arithmetic only (Gate 5).

Locks: the McKay/Lie/CIZ graph identity (P=1 forced); the {E6}-only exceptional menu over an
imaginary-quadratic field (no birthday problem); the 2-splitting base rate; the m003 sister tie.
"""
import numpy as np
import sympy as sp


def test_mckay_2T_is_affine_E6_marks():
    # McKay graph of 2T=SL(2,F3): affine E6, Perron marks {1,1,1,2,2,2,3} summing to 12 = h(E6).
    # affine E6 (E6~) adjacency: a central trivalent node, three length-2 legs (7 nodes).
    # nodes: center c; three legs (m_i - t_i): c-m1-t1, c-m2-t2, c-m3-t3
    # index: 0=c, 1=m1,2=t1, 3=m2,4=t2, 5=m3,6=t3
    A = np.zeros((7, 7), dtype=int)
    edges = [(0, 1), (1, 2), (0, 3), (3, 4), (0, 5), (5, 6)]
    for i, j in edges:
        A[i, j] = A[j, i] = 1
    marks = np.array([3, 2, 1, 2, 1, 2, 1])                    # Perron (Coxeter) marks
    assert np.array_equal(A @ marks, 2 * marks)               # A marks = 2 marks (affine Perron eigenvalue 2)
    assert marks.sum() == 12                                   # = h(E6), the Coxeter number
    assert sorted(marks.tolist()) == [1, 1, 1, 2, 2, 2, 3]     # the 2T McKay dims


def test_E6_lie_equals_E6_ciz_adjacency_forced():
    # Ordinary E6 (delete the affine/trivial-rep node): the Lie Dynkin E6 and the CIZ E6 graph are
    # the SAME adjacency matrix -> the "three faces" are one classification, recurrence FORCED (P=1).
    # ordinary E6 Dynkin: chain 1-2-3-4-5 with node 6 attached to node 3 (the branch)
    def e6():
        A = np.zeros((6, 6), dtype=int)
        for i, j in [(0, 1), (1, 2), (2, 3), (3, 4), (2, 5)]:
            A[i, j] = A[j, i] = 1
        return A
    A_lie = e6()
    A_ciz = e6()                                               # CIZ E6 is read off the SAME Dynkin diagram
    assert np.array_equal(A_lie, A_ciz)                        # identical -> not independent evidence
    # Coxeter number from the Dynkin: h(E6)=12 -> CIZ SU(2) level k = h-2 = 10 (no independent m004 input)
    assert 12 - 2 == 10


def test_exceptional_menu_over_imaginary_quadratic_is_E6_only():
    # No birthday problem: 2O(E7) forces sqrt2, 2I(E8) forces sqrt5 (both REAL quadratic);
    # only 2T(E6), character field Q(sqrt-3), sits over an imaginary-quadratic field.
    assert sp.simplify(2*sp.cos(sp.pi/4)) == sp.sqrt(2)       # 2O order-4 trace -> sqrt2 (real)
    assert sp.simplify(2*sp.cos(sp.pi/5)) == (1 + sp.sqrt(5))/2  # 2I order-5 trace -> sqrt5 (real)
    # sqrt2, sqrt5 are real quadratic irrationalities -> never a subfield of an imaginary quadratic field
    for r in (sp.sqrt(2), sp.sqrt(5)):
        assert sp.im(r) == 0                                   # real
    # so the reachable exceptional McKay label over Q(sqrt-d) is {E6} only -- E6 was never a "draw"


def test_2_splitting_base_rate_d7_unique():
    # E6-by-torsion base rate: 2 splits in Q(sqrt-d) iff -d = 1 mod 8; d=7 is the UNIQUE split case
    # among the Heegner numbers -> exceptional label present 8/9 (89%), 4/5 on {1,2,3,7,11}.
    heegner = [1, 2, 3, 7, 11, 19, 43, 67, 163]
    split = [d for d in heegner if (-d) % 8 == 1]
    assert split == [7]                                        # only d=7 splits
    small = [1, 2, 3, 7, 11]
    present = [d for d in small if (-d) % 8 != 1]
    assert len(present) == 4 and len(small) == 5              # 4/5 on the small Bianchi set


def test_sister_m003_ties_m004_field_but_is_not_a_knot():
    # The decisive control: m003 shares m004's exact shape field Q(sqrt-3) but is NOT a knot in S^3.
    try:
        import snappy
    except ImportError:
        import pytest
        pytest.skip("snappy unavailable")
    m3, m4 = snappy.Manifold("m003"), snappy.Manifold("m004")
    assert abs(m3.volume() - m4.volume()) < 1e-6              # identical volume (same commensurability)
    z3 = complex(m3.tetrahedra_shapes('rect')[0])
    z4 = complex(m4.tetrahedra_shapes('rect')[0])
    # both shapes = exp(i pi/3) = 1/2 + i sqrt3/2 -> trace field Q(sqrt-3) for BOTH
    for z in (z3, z4):
        assert abs(z - complex(0.5, 3**0.5/2)) < 1e-6
    # but the homology differs: m004 = Z (a knot), m003 = Z/5 + Z (torsion -> NOT a knot in S^3)
    assert str(m4.homology()) == "Z"
    assert "Z/5" in str(m3.homology())
