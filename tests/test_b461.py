"""B461 — locks: the rung-1 exact claims + the Borromean/Whitehead volume facts.

SnapPy is an OPTIONAL dependency (`REPRODUCIBILITY.md`: the verified constants are hard-coded
and tested without it), so it is imported through `pytest.importorskip` — a bare top-level
`import snappy` here aborted COLLECTION of the whole suite on a clone without it, so zero tests
ran rather than these few skipping.
"""
import pytest

snappy = pytest.importorskip("snappy", reason="SnapPy required for the census volume facts")


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
