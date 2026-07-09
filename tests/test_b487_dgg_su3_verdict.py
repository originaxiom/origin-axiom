"""Locks for B487 (DGG SU(3) = SM gauge group: REFUTED, 13th kill).

Mostly a documentation-integrity lock: the node is a literature verdict (Gang-Yonekura
arXiv:1803.04009 says FLAVOR symmetry of a 3d N=2 theory, not a 4d gauge group), so the
four decisive refutation points and the addendum corrections are locked as the FINDINGS'
load-bearing lines, not recomputed. One numeric cross-check IS recomputed (SnapPy-guarded):
the banked correction that the metallic m=2 member is m136 (vol 3.664), NOT the 5_2 knot
(vol 2.828) — different manifolds.
"""
import pathlib

import pytest

_FIND = (pathlib.Path(__file__).resolve().parents[1]
         / "frontier" / "B487_dgg_su3_verdict" / "FINDINGS.md").read_text(encoding="utf-8")


def test_header_verdict_refuted_13th_kill():
    assert "REFUTED (13th kill)" in _FIND


def test_four_decisive_points():
    assert "**FLAVOR, not GAUGE.**" in _FIND
    assert "**3d, not 4d.**" in _FIND
    assert "**One symmetry, not three factors.**" in _FIND
    assert "**No SM matter content.**" in _FIND
    assert "(SU(2)×U(1) ⊂ SU(3))" in _FIND          # the double-counting point


def test_attribution_corrected():
    assert "Dongmin Gang and Kazuya YONEKURA" in _FIND
    assert 'NOT "Gang, Kim, and Lee"' in _FIND


def test_duality_product_addendum():
    # both metallic knots are twist knots -> SU(3) x SU(3), and m=2 is m136, not 5_2
    assert "SU(3)×SU(3)" in _FIND
    assert 'The "SU(2) from the silver knot" is false — 5₂ gives SU(3) too.' in _FIND
    assert "**The metallic m=2 is m136, NOT the 5₂ knot**" in _FIND
    assert "λ_m·σ(λ_m) = N(λ_m) = det X_m = −1" in _FIND


def test_firewall_holds():
    assert "Firewall holds; nothing physics-shaped banked." in _FIND


def test_m136_is_not_5_2_snappy():
    snappy = pytest.importorskip("snappy")
    m136 = snappy.Manifold('m136')
    k52 = snappy.Manifold('5_2')
    v1, v2 = float(m136.volume()), float(k52.volume())
    assert abs(v1 - 3.663862) < 1e-5        # the banked 3.664
    assert abs(v2 - 2.828122) < 1e-5        # the banked 2.828
    assert abs(v1 - v2) > 0.5               # different manifolds
