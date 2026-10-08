"""B1612 -- THE MIXING PATTERNS THE WEAVE FIXES: the sealed scripts unchanged; the patterns and the contact as recorded."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes"
V = ARC / "verification"


def test_the_sealed_scripts_are_unchanged():
    lines = [l for l in open(ARC / "ARTIFACT_HASHES.txt").read().splitlines() if l.startswith("# sealed at f008c0424")]
    assert len(lines) == 2
    for l in lines:
        sha, path = l.split()[4], l.split()[5]
        assert hashlib.sha256(open(ARC / path, "rb").read()).hexdigest() == sha


def test_the_patterns():
    d = json.load(open(V / "mixing_on_the_weave.json"))
    assert d["M1"]["faithful_on_T"] and d["M1"]["order_image_on_T"] == 96
    assert d["M3"]["distinct_full_patterns"] == 6 and set(d["M3"]["named_present"]) == {"BM", "TBM", "democratic"}
    assert d["M4"]["TM1_column_present"] and d["M4"]["TM2_column_present"]


def test_the_contact():
    c = json.load(open(V / "comparison.json"))
    assert c["D1"]["NO"]["survivors"] == [] and c["D1"]["IO"]["survivors"] == []
    assert c["D2"]["survivors"] == [] and c["D2"]["closest"]["pattern"] == "identity" and c["D2"]["closest"]["max_pull_sigma"] > 300
    cols = sorted(tuple(x) for x in c["D3"]["NO"]["columns"])
    assert cols == [(0.166667, 0.166667, 0.666667), (0.333333, 0.333333, 0.333333)]
    p = json.load(open(V / "post_seal_tm_sum_rules.json"))
    assert abs(p["NO"]["TM1_pull_sigma"]) < 2 and p["NO"]["TM2_pull_sigma"] > 4
