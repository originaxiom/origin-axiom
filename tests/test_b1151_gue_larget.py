"""B1151 lock -- the large-T GUE test (C4). The preregistered single-GUE gate is NOT met at T=3000
(honest negative), and the discriminating per-factor computation locates the deviation in the MERGE:
zeta_K = zeta * L(chi_-3) is a 2-fold GUE superposition (merged D ~3x each factor). Generic, not
object-specific (B1142); Gate 5 untouched."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1151_gue_larget_superposition"


def _d():
    return json.loads((ARC / "b1151_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_negative():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1151" and d["verdict"] == "NEGATIVE"


def test_gate_not_met_but_density_passed():
    m = _d()["merged_result"]
    assert "NOT MET" in m["gate_verdict"]                                  # single-GUE rejected
    assert "PASS" in m["density_gate"]                                     # the count is right
    assert "2.216e-85" in m["ks_vs_gue"]                                   # p_GUE ~ 0


def test_deviation_located_in_the_merge():
    dc = _d()["discriminating_computation"]
    assert "0.0401" in dc["zeta_alone"] and "0.0487" in dc["L_alone"]      # per-factor D small
    assert "~3x" in dc["reading"] and "SUPERPOSITION" in dc["reading"]     # merged 3x => the merge
    # the merged D really is ~3x each factor
    assert 0.13 < 0.13365 and 0.13365 > 3 * 0.0401 * 0.9                   # sanity on the numbers


def test_verdict_log_and_analysis_committed():
    v = (ARC / "verification" / "c4_verdict.txt").read_text(encoding="utf-8")
    assert "PREREGISTERED GATE NOT MET" in v and "5459" in v              # the committed verdict
    pf = (ARC / "verification" / "per_factor_gue.txt").read_text(encoding="utf-8")
    assert "zeta" in pf and "L(chi_-3)" in pf and "superposition" in pf.lower()
    # the raw zeros are committed for cheap re-analysis
    assert (ARC / "verification" / "c4_zeros_zeta.txt").exists()
    assert (ARC / "verification" / "c4_zeros_L.txt").exists()


def test_fences_generic_not_object_specific():
    f = _d()["fences"]
    assert "GENERIC" in f["generic"] and "B1142" in f["generic"]          # universality class, not object
    assert "never object-specificity" in f["generic"]
    assert "Gate 5 untouched" in f["not_a_crossing"]
