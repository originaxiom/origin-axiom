"""B1121 lock -- L176 the pair-orbit lane: the validated machinery + the honest bound."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def test_machinery_validated():
    r = json.loads((ROOT / "frontier/B1121_pair_orbits/b1121_results.json")
                   .read_text(encoding="utf-8"))
    c = r["controls"]
    assert c["C0_norm_multiplicativity"].startswith("500/500")
    assert "500/500" in c["C0_conjugate_antiautomorphism"]
    assert c["C1_leibniz_derivation"] == "60/60"
    assert c["C2_jordan_identity"] == "60/60"


def test_verdict_is_honest_open():
    r = json.loads((ROOT / "frontier/B1121_pair_orbits/b1121_results.json")
                   .read_text(encoding="utf-8"))
    assert "INCONCLUSIVE-AT-BOUND" in r["verdict"]
    d = json.loads((ROOT / "frontier/B1121_pair_orbits/arc_verdict.json")
                   .read_text(encoding="utf-8"))
    assert d["verdict"] == "OPEN"
