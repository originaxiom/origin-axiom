"""B1282 — the sibling's germ: m202's twelve isometries as automorphisms (fast), the deformation classes h^1(m202; Sym^n) = 2 on
every even slot (and on the odd ones, for this lift), and the inversion acting as the E6 outer automorphism's sign on every slot, uniquely (the slots
n <= 8 fast; all six slots slow)."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1282_the_siblings_germ" / "verification"))
snappy = pytest.importorskip("snappy")


def test_m202_isometries_and_the_small_slots():
    import sibling_germ as S
    out = S.main(slots=(0, 1, 2, 3, 8), verbose=False)
    assert out['found'] == 180 and out['classes'] == 12
    assert out['h1'] == {0: 2, 1: 2, 2: 2, 3: 2, 8: 2} and out['finite_order']
    inv = out['results'][2][1]['inversion (A,B)'][0]
    assert all(abs(inv[i, j] - (1 if i == j else 0)) < 1e-15 for i in range(2) for j in range(2))
    inv8 = out['results'][8][1]['inversion (A,B)'][0]
    assert all(abs(inv8[i, j] - (-1 if i == j else 0)) < 1e-15 for i in range(2) for j in range(2))


@pytest.mark.slow
def test_the_inversion_is_the_unique_isometry_realising_theta_on_m202(capsys):
    import sibling_germ as S
    out = S.main()
    text = capsys.readouterr().out
    assert out['h1_ok'] and out['finite_order']
    assert [k for k, v in out['realises'].items() if v] == ['inversion (A,B)']
    assert "isometries realising theta" in text
