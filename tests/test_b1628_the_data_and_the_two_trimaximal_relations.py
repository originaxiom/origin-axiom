"""B1628 -- the sealed instrument unchanged; TM1 within 2 sigma and TM2 at 2.74 sigma on NuFIT 6.0 (R3, R4 fail as sealed); JUNO
reported, not graded; P10' registered."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1628_the_data_and_the_two_trimaximal_relations"


def test_sealed_and_recorded():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at c395a2cd5: ")
    assert hashlib.sha256(open(ARC / "verification" / "two_relations.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "two_relations.json"))
    g = d["sets"]["NuFIT_6.0_graded"]
    for o in ("NO", "IO"):
        assert g[o]["TM1_within_2sigma"] and not g[o]["TM2_beyond_3sigma"]
        assert 2.6 < g[o]["TM2"]["pull_sigma"] < 2.9 and g[o]["TM2"]["inside_3sigma_range"]
    j = d["sets"]["JUNO_2025_reported_not_graded"]["NO"]
    assert j["TM2_beyond_3sigma"] and not j["TM2"]["inside_3sigma_range"]
    assert "| **P10′** |" in ROOT.joinpath("docs", "FALSIFIER_REGISTER.md").read_text(encoding="utf-8")
