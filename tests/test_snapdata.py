"""P9 — figure-eight knot complement (4_1) verified data.

Hardened 2026-07-01 (audit): the constant anchors are no longer only mirrored
literals — the volume is recomputed *independently* of both ``constants.py``
and SnapPy from the ideal-triangulation dilogarithm formula, and every clause
of P9 (H1, Chern–Simons, amphichirality, the sister's torsion) now has a live
SnapPy cross-check when SnapPy is installed. Without SnapPy the dilogarithm
test still breaks the constants' circularity; the live checks skip.
"""

import mpmath as mp
import pytest

from origin_axiom.constants import CS_FIG8, CS_SISTER, VOL_FIG8


def test_figure_eight_constants():
    assert abs(VOL_FIG8 - 2.0298832128) < 1e-9   # minimal hyperbolic volume
    assert CS_FIG8 == 0.0                        # Chern-Simons invariant
    assert CS_SISTER == 0.25                     # sister m003 differs in CS


def test_volume_recomputed_independently_from_the_dilogarithm():
    # The figure-eight complement decomposes into two regular ideal tetrahedra
    # of shape z = e^{i pi/3} (the Eisenstein shape, cf. P12); each has volume
    # Im(Li_2(z)) (the Bloch-Wigner value at the regular shape, where the
    # correction term log|z| arg(1-z) vanishes since |z| = 1). This recomputes
    # VOL_FIG8 with no SnapPy and no reuse of the stored constant.
    mp.mp.dps = 30
    shape = mp.e ** (1j * mp.pi / 3)
    vol = 2 * mp.im(mp.polylog(2, shape))
    assert abs(vol - VOL_FIG8) < 1e-12


def test_snappy_volume_crosscheck_if_available():
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold("4_1")
    assert abs(M.volume() - VOL_FIG8) < 1e-6


def test_snappy_homology_crosscheck_if_available():
    # P9: H1(4_1) = Z; sister m003: H1 = Z + Z/5.
    snappy = pytest.importorskip("snappy")
    h_fig8 = snappy.Manifold("4_1").homology()
    assert h_fig8.betti_number() == 1
    assert h_fig8.order() == "infinite" or str(h_fig8) == "Z"
    h_sister = snappy.Manifold("m003").homology()
    assert h_sister.betti_number() == 1
    assert sorted(str(h_sister).replace(" ", "").split("+")) == ["Z", "Z/5"]


def test_snappy_chern_simons_crosscheck_if_available():
    snappy = pytest.importorskip("snappy")
    assert abs(snappy.Manifold("4_1").chern_simons() - CS_FIG8) < 1e-9
    assert abs(snappy.Manifold("m003").chern_simons() - CS_SISTER) < 1e-9


def test_snappy_amphichirality_crosscheck_if_available():
    # P9: 4_1 is amphichiral. Per the MB guard in REPRODUCIBILITY.md, the
    # correct test is symmetry_group().is_amphicheiral() gated on the group
    # being provably full — NOT is_isometric_to(mirror), which is
    # orientation-blind.
    snappy = pytest.importorskip("snappy")
    sg = snappy.Manifold("4_1").symmetry_group()
    assert sg.is_full_group()
    assert sg.is_amphicheiral()


def test_snappy_sister_shares_the_volume_if_available():
    # P9: m003 has the same (minimal) volume as 4_1.
    snappy = pytest.importorskip("snappy")
    v1 = snappy.Manifold("4_1").volume()
    v2 = snappy.Manifold("m003").volume()
    assert abs(v1 - v2) < 1e-9
