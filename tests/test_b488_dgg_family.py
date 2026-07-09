"""Locks for B488 (the DGG data of the metallic family) — re-executes the probe.

The two clean laws, recomputed live in SnapPy for m = 1..5 (FINDINGS verified m = 1..8;
the small range keeps the lock fast): the metallic bundle R^m L^m has N = 2m ideal
tetrahedra and one cusp, so T[A_m] = U(1)^{2m-1} (DGG gauge rank N - c), and
H1 = (Z/m)^2 (+) Z. Plus the twist-knot table (Gang-Yonekura's SU(3) domain) and the
intersection statement: the two families meet only at 4_1.
"""
import pathlib

import pytest

_FIND = (pathlib.Path(__file__).resolve().parents[1]
         / "frontier" / "B488_dgg_family" / "FINDINGS.md").read_text(encoding="utf-8")


def test_metallic_dgg_gauge_rank_and_homology_laws():
    snappy = pytest.importorskip("snappy")
    for m in range(1, 6):
        M = snappy.Manifold('b++' + 'R' * m + 'L' * m)
        assert M.num_tetrahedra() == 2 * m, m
        assert M.num_cusps() == 1, m
        assert M.num_tetrahedra() - M.num_cusps() == 2 * m - 1      # U(1)^{2m-1}
        want = "Z" if m == 1 else f"Z/{m} + Z/{m} + Z"              # (Z/m)^2 (+) Z
        assert str(M.homology()) == want, m


def test_twist_knot_dgg_table():
    snappy = pytest.importorskip("snappy")
    tets = {'4_1': 2, '5_2': 3, '6_1': 4, '7_2': 4, '8_1': 5}
    for knot, n in tets.items():
        M = snappy.Manifold(knot)
        assert M.num_tetrahedra() == n, knot                        # U(1)^{N-1}
        assert M.num_cusps() == 1 and str(M.homology()) == "Z", knot


def test_families_intersect_only_at_4_1():
    snappy = pytest.importorskip("snappy")
    # m=1 metallic bundle IS the figure-eight twist knot ...
    assert snappy.Manifold('b++RL').is_isometric_to(snappy.Manifold('4_1'))
    # ... and m=2 is the bundle m136, which is NOT the twist knot 5_2
    m2 = snappy.Manifold('b++RRLL')
    assert m2.is_isometric_to(snappy.Manifold('m136'))
    assert abs(float(m2.volume()) - float(snappy.Manifold('5_2').volume())) > 0.5


def test_findings_state_the_laws_and_firewall():
    assert "T[A_m] = U(1)^{2m−1}" in _FIND
    assert "H₁(M(A_m)) = (ℤ/m)² ⊕ ℤ" in _FIND
    assert "so Gang–Yonekura's" in _FIND and "SU(3) theorem does not apply" in _FIND
    assert "banked as mathematics, not physics" in _FIND
