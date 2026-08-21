"""B1126 lock -- V-3 the identification: NO-OBJECT-PERIOD-IS-AN-SM-RATIO, exhaustive
sealed scan; the one near-coincidence (C1/C0 vs sin theta12) dismissed on 3 grounds.
This bench re-derives the object-period value the near-coincidence turned on."""
import json
from pathlib import Path
import mpmath as mp
ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1126_identification"


def test_verdict_no_match():
    r = json.loads((ARC / "b1126_results.json").read_text(encoding="utf-8"))
    blob = json.dumps(r)
    assert "NO-OBJECT-PERIOD-IS-AN-SM-RATIO" in blob


def test_the_near_coincidence_value_reproduces():
    mp.mp.dps = 40
    C0 = mp.power(3, mp.mpf(-1) / 4)
    C1_over_C0 = mp.mpf(11) / 108 * mp.sqrt(3) * mp.pi   # = 11*pi/(36*sqrt3)
    assert abs(C1_over_C0 - mp.mpf('0.5542164724048999')) < mp.mpf('1e-14')
    sin12 = mp.sqrt(mp.mpf('0.307'))                     # NuFIT 6.0 sin^2 theta12 central
    rel = abs(C1_over_C0 - sin12) / sin12
    assert mp.mpf('2e-4') < rel < mp.mpf('4e-4')         # ~0.025%, real but not a match


def test_findings_dismiss_on_three_grounds():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "look-elsewhere" in f.lower() and "16.4%" in f
    assert "No principled instrument" in f or "no principled instrument" in f.lower()
    assert "UNCLAIMED" in f and "Relayed to cc3" in f
    assert "eighth" in f.lower()
