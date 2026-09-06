"""B1273 — the object's 3-fold cyclic branched cover: Reidemeister-Schreier presentation, H_1 = Z4^2, the F(2,6)
fingerprint, the descent of the 2T holonomy with exactly three twisted classes, and the zero-diagonal texture bound."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
for arc in ("B1267_spectrum_law_rebuilt", "B1269_transport_computed", "B1273_the_three_fold_closing"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))


@pytest.fixture(scope="module")
def Y():
    import three_fold_closing as Y
    return Y


def test_the_closing_has_h1_z4_squared_and_the_fibonacci_fingerprint(Y, capsys):
    ok, pres = Y.part_a()
    assert ok
    out = capsys.readouterr().out
    assert "torsion [4, 4], free rank 0" in out
    assert "Y_3 presentation 64, F(2,6) 64" in out and "Y_3 presentation 16, F(2,6) 16" in out


def test_the_holonomy_descends_with_exactly_three_classes(Y, capsys):
    ok, pres = Y.part_a()
    capsys.readouterr()
    okb, res = Y.part_b(pres)
    assert okb
    for k in res:
        oa, h0_3, h1_3, v4, h1_2, h1_0, hchi = k
        assert (h0_3, h1_3, v4, h1_0) == (0, 3, True, 0)
        assert sorted(dict(hchi).values()) == [(0, 0), (1, 1), (1, 1), (1, 1)]
        if oa == 3:
            assert h1_2 == 0
    assert sum(res.values()) == 48


def test_the_zero_diagonal_bound_and_the_data(Y, capsys):
    assert Y.part_d()
    out = capsys.readouterr().out
    assert "135.8" in out and "42.8" in out and "16.7" in out
