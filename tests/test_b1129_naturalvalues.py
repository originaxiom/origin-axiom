"""B1129 lock -- P-NATURALVALUES: NATURAL-VALUES-DISJOINT; the |det phi|=2/3 vs Koide 2/3
near-miss named + dismissed. This bench re-derives the two 2/3's."""
import json
from pathlib import Path
import mpmath as mp
ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1129_natural_values_disjoint"


def test_verdict_disjoint():
    r = json.loads((ARC / "b1129_results.json").read_text(encoding="utf-8"))
    assert "NATURAL-VALUES-DISJOINT" in json.dumps(r)


def test_the_det_phi_koide_near_miss_numbers():
    mp.mp.dps = 30
    # |det phi| = 2/3 exactly (B904)
    detphi = mp.mpf(2) / 3
    # Koide Q from PDG charged-lepton masses (MeV)
    me, mmu, mtau = mp.mpf('0.51099895'), mp.mpf('105.6583755'), mp.mpf('1776.86')
    Q = (me + mmu + mtau) / (mp.sqrt(me) + mp.sqrt(mmu) + mp.sqrt(mtau))**2
    # they agree to ~5 digits -- a real near-miss, correctly dismissed (no instrument)
    assert abs(Q - detphi) < mp.mpf('1e-4')
    assert abs(Q - detphi) > mp.mpf('1e-7')   # NOT exact -- Koide is empirical, ~5 digits


def test_findings_dismiss_and_close():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "NATURAL-VALUES-DISJOINT" in f
    assert "|det φ| = 2/3" in f and "Koide" in f
    assert "four independent grounds" in f or "four grounds" in f
    assert "physics-shaped, not physics-valued" in f
