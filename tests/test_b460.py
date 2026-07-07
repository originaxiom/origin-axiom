"""Lock for B460 — R1: the child's spectrum head + the two-gate-validated CS method."""
import os
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B460_relation_r1_child")
sys.path.insert(0, HERE)


def test_child_shortest_geodesic():
    import snappy
    M = snappy.ManifoldHP("4_1(5,1)")
    L = M.length_spectrum(0.7)
    l0 = complex(L[0].length)
    assert abs(l0.real - 0.5780824355) < 1e-8
    assert abs(l0.imag - 2.1324306362) < 1e-8


def test_geometric_cs_gates():
    import snappy
    for p, want in [(5, 0.0770381803), (7, 0.0606168663)]:
        M = snappy.Manifold('4_1')
        _ = M.chern_simons()
        M.dehn_fill((p, 1))
        assert abs(float(M.chern_simons()) - want) < 1e-8
