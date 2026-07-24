"""B772 -- the negatives adequacy audit: locks on the finding (the honest self-scrutiny record)."""
import json
import pathlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B772_negatives_adequacy"


def _load():
    return json.loads((ARC / "audit_results.json").read_text())


def test_fourteen_negatives_classified():
    d = _load()
    assert len(d["rows"]) == 14
    for r in d["rows"]:
        assert r["verdict"] in ("ROBUST", "PROVISIONAL", "NEEDS-DEEPER-LEVEL", "CONTENT-FREE-THESIS-PREDICTED")


def test_only_four_robust():
    # the load-bearing negatives: exact/structural, object-native, seam-independent
    d = _load()
    robust = sorted(r["id"] for r in d["rows"] if r["verdict"] == "ROBUST")
    assert robust == ["OI-173", "OI-186", "W2-148r", "W2-237"]


def test_corpus_is_not_seam_over_determined():
    # the hypothesis-refutation: 12/14 object-native and seam-independent
    d = _load()
    independent = sum(1 for r in d["rows"] if r["independent_of_seam"])
    assert independent == 12


def test_trace_blind_risk_set():
    # the real finding: exactly these four negatives are computed in the chord-blind projection
    d = _load()
    blind = sorted(r["id"] for r in d["rows"] if r["level_projection"] == "TRACE-BLIND-RISK")
    assert blind == ["W3-067", "W3-082", "W4-115", "W4-304"]


def test_recompute_flagged_majority():
    # 9/14 need re-computation (deeper level / chord / object-native input / defect fix)
    d = _load()
    assert sum(1 for r in d["rows"] if r["recompute_recommended"]) == 9
