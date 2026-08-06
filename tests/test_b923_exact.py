"""B923 locks: the identities and the hierarchy-carrier discovery."""
import json, os
ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B923_exactification")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_ccc_identity_both_gauges():
    t = json.dumps(_res())
    assert "13824/953" in t or "'13824', '953'" in t
    assert "-6" in t


def test_pipeline_link_identity():
    t = json.dumps(_res())
    assert "824843587681" in t  # 953^4, HIER's lead: the charpoly identity anchor


def test_canonical_collapse_recorded():
    t = json.dumps(_res())
    assert "(x+3)^3" in t or "generation-degenerate" in t or "collapse" in t.lower()
