"""B1283 — the SM closing's tree-level vacuum: the charge tables and the singlet sector (fast); the nine conjugate-paired
SM-preserving branches, the surviving Z' of rank 1 on the maximal ones, the light Higgs/D pair count (slow, ~3 min)."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1283_the_sm_closings_vacuum" / "verification"))


def test_the_singlet_sector_and_its_charges():
    import sm_closing_vacuum as V
    D = V.setup()
    ch = V.charges_on_27(D)
    sing = [c for c in ch if c['colour_singlet'] and c['t3'] == 0 and c['Y'] == 0]
    assert sorted(c['lab'] for c in sing) == ['S', 'nu^c']
    qN = next(c for c in sing if c['lab'] == 'S'); qn = next(c for c in sing if c['lab'] == 'nu^c')
    assert qN['qb'] == -qn['qb'] and qN['qg'] == qn['qg']                      # an su(2)_beta doublet
    assert {(str(c['qb']), str(c['qg'])) for c in ch if c['lab'] in ('Q', 'u^c', 'e^c')} == {('0', '-2/3')}


@pytest.mark.slow
def test_the_nine_branches_and_the_surviving_z_prime(capsys):
    import sm_closing_vacuum as V
    out = V.main()
    text = capsys.readouterr().out
    assert out['ok'] and len(out['rows']) == 9 and out['exactly_sm'] == 0 and out['min_rank'] == 1
    assert all(r[3] for r in out['rows'])                                        # all conjugate-paired
    assert sorted(out['moduli'].values()) == [2] * 6 + [3] * 3
    assert out['light'] == {((1,), 1): 3, ((2,), 1): 3, ((3,), 1): 3}
    assert "E6 part -6 gamma = (5 psi - 3 chi)/2" in text and out['gamma_ok'] and out['beta_ok']
