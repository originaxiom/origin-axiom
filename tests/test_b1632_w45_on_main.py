"""B1632 -- the sealed instrument unchanged; the calibrations hold; no strict Mp2(Z) identification (projective lifts); among
the genuine rescalings chi_{3/2} takes 0 and 1, and the seat's T-exponents (1/8, 3/8, 7/8) give 0."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1632_w45_verified_on_main"


def test_sealed_and_diagnosed():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at ")
    assert hashlib.sha256(open(ARC / "verification" / "w45_on_main.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "w45_on_main.json"))
    assert d["C0"]["trivial_ok"] and abs(d["C0"]["eta_chi_half"] - 1) < 1e-9 and d["C1"]["valid"] == []
    p = json.load(open(ARC / "verification" / "post_seal_projective.json"))
    assert all(r["projective"] for r in p["D1"])
    assert {abs(x) for x in p["D2"]["S~,L^-1"]["chi_3_2_values"]} == {0.0, 1.0}
