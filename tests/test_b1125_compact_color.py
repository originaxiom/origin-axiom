"""B1125 lock -- V-2 compact color: NO-COMPACT-HOST, exhaustive; the color A2 is (5,3)
not (0,8); E6(-26) reached but color non-compact. Fast: assert the banked result JSON."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1125_compact_color"


def test_verdict_no_compact_host():
    r = json.loads((ARC / "b1125_results.json").read_text(encoding="utf-8"))
    assert r["verdict"] == "NO-COMPACT-HOST"
    assert r["genuine_compact_color_hits"] == []
    assert r["compact_color_hits"] == []
    # the candidate form E6(-26) IS reached, yet no compact color (the discriminating point)
    assert -26 in r["all_characters_seen_allowed"]
    # no impossible characters -> the classification checksum stayed clean
    assert r["all_characters_seen_disallowed"] == []


def test_findings_carry_mechanism_and_fences():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "(5,3" in f and "(0,8)" in f                      # the discriminating signatures
    assert "NECESSARY BUT NOT SUFFICIENT" in f               # the checksum lesson
    assert "ANTILINEAR" in f and "mirror-conjugation" in f  # the type distinction + successor
    assert "V-2′" in f                                  # the sharpened open cell is named
    assert "3 of 4 B1119 controls" in f or "3/4" in f        # the honest control fence
