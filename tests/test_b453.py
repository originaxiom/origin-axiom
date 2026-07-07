"""Locks for B453 — Ethogram E1: the identical child + the Lucas launder."""
import sympy as sp


def test_identical_child():
    import snappy
    M = snappy.Manifold("4_1(5,1)")
    N = snappy.Manifold("5_2(5,1)")
    assert M.is_isometric_to(N)
    assert str(M.homology()) == "Z/5"


def test_z5_cover_homology_and_lucas():
    import snappy
    M = snappy.Manifold("4_1(5,1)")
    covs = M.covers(5)
    assert len(covs) == 1
    H = covs[0].homology()
    assert H.betti_number() == 0
    assert str(H) == "Z/11 + Z/11"
    # the Lucas/Alexander launder: |prod Delta(zeta_5^k)| = 121 = L_5^2
    t = sp.Symbol('t')
    alex = t**2 - 3*t + 1
    prod = sp.prod([alex.subs(t, sp.exp(2*sp.pi*sp.I*k/5)) for k in range(1, 5)])
    assert sp.Abs(sp.nsimplify(sp.expand_complex(prod))) == 121


def test_no_other_low_index_covers():
    import snappy
    M = snappy.Manifold("4_1(5,1)")
    for k in (2, 3, 4, 6):
        assert len(M.covers(k)) == 0
