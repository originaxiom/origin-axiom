"""B461 — locks: the rung-1 exact claims + the Borromean/Whitehead volume facts."""
import snappy


def test_borromean_volume_two_octahedra():
    M = snappy.Manifold('L6a4')
    v_oct = 3.663862376708876
    assert abs(float(M.volume()) - 2 * v_oct) < 1e-9


def test_homology_and_cusps():
    M = snappy.Manifold('L6a4')
    assert M.num_cusps() == 3
    assert str(M.homology()) == 'Z + Z + Z'


def test_whitehead_control():
    W = snappy.Manifold('m129')
    assert W.num_cusps() == 2
    assert abs(float(W.volume()) - 3.663862376708876) < 1e-9   # one octahedron
