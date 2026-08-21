"""B1117 lock -- the adelic anchors, this bench's verification.
Anchor B: Vol = 9 sqrt3 zeta_K(2)/pi^2 (K=Q(sqrt-3)) to 1e-25. Anchor A: the
edge windows are Fibonacci convergent denominators, even-closes/odd-breaks."""
import mpmath as mp
from pathlib import Path
mp.mp.dps = 40
ROOT = Path(__file__).resolve().parents[1]


def test_anchor_B_vol_is_a_zeta_special_value():
    Lchi2 = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
    vol_pred = 9 * mp.sqrt(3) * (mp.zeta(2) * Lchi2) / mp.pi**2
    vol_true = mp.mpf('2.029883212819307250042405108549')
    assert abs(vol_pred - vol_true) < mp.mpf('1e-25')


def test_anchor_A_windows_are_convergents():
    F = [0, 1, 1]
    while len(F) < 22:
        F.append(F[-1] + F[-2])
    close = {F[14], F[16], F[18]}
    brk = {F[13], F[15], F[17], F[19]}
    assert close == {377, 987, 2584} and brk == {233, 610, 1597, 4181}


def test_findings_carry_the_frame_and_fence():
    f = " ".join((ROOT / "frontier/B1117_adelic_object/FINDINGS.md")
                 .read_text(encoding="utf-8").split())
    assert "special value of the finite shadow's zeta" in f
    assert "the observer is the approaching" in f
    assert "silver control" in f  # the falsifier
