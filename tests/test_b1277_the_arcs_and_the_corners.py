"""B1277 addendum — the arcs and the corners: the eight isometries of m004 as affine maps of the cusp torus (from
the holonomy; the horoball pattern alone has sixteen), the two inversions with four corners each, no reflections
(the mu- and lambda-reversing involutions are glides), the theta-odd Higgs field's leading allowed cusp mode
sin(4 pi x) (pure longitude), annular partition: chi(d+M) = 0."""
import sys
from pathlib import Path
import pytest

snappy = pytest.importorskip("snappy")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1277_the_vacuum_manifold_of_the_closing" / "verification"))


def test_the_arcs_cut_the_corners_but_the_partition_is_annular(capsys):
    import arcs_and_corners as AC
    out = AC.main()
    text = capsys.readouterr().out
    aff = out['affine']
    assert sorted(aff[(1, 1)]) == [(0.0, 0.0), (0.5, 0.0)]                      # identity and the period-2 half-translation
    assert sorted(aff[(-1, -1)]) == [(0.0, 0.0), (0.5, 0.0)]                    # the two inversions, four corners each
    assert sorted(aff[(-1, 1)]) == [(0.25, 0.5), (0.75, 0.5)]                   # the order-4 rotoreflections: glides
    assert sorted(aff[(1, -1)]) == [(0.25, 0.5), (0.75, 0.5)]                   # the other involutions: glides, no fixed circles
    assert out['lead'] == [(-2, 0), (2, 0)] and out['dim'] == 1
    assert out['chi_pos'] == 0 and out['chi_neg'] == 0 and out['npos'] == 2 and out['nneg'] == 2
    assert "affine symmetries of the horoball pattern: 16" in text
    assert "[(-1, 0), (1, 0)]: decay 0.2887, allowed dim 0" in text
    assert "chi(d+M) = 0" in text
