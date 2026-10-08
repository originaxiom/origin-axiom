"""B1613 -- TM1'S FORWARD PREDICTION: the sealed instrument unchanged; the band as recorded; P10 registered."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1613_tm1s_forward_prediction"


def test_sealed_and_recorded():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 540e12dd0: ")
    assert hashlib.sha256(open(ARC / "verification" / "tm1_forward.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "tm1_forward.json"))
    assert d["F1"]["identity_holds"] and d["F3"]["n_points"] == 0
    lo, hi = d["F2"]["three_sigma_theta23_41.27_to_49.86"]["lower_half_plane_deg"]
    assert 240 <= lo < hi <= 300 and abs(d["F2"]["central"]["sin2_theta12_TM1"] - 0.318) < 1e-3


def test_p10_is_registered():
    r = open(ROOT / "docs" / "FALSIFIER_REGISTER.md", encoding="utf-8").read()
    assert "**P10**" in r and "B1613" in r
