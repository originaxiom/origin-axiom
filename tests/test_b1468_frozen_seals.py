"""B1468 -- the frozen seals re-audited: six attested with quotes, thirty-five frozen."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts", "gates")); import gates


def test_the_attestations_are_six_and_their_quotes_are_in_the_files():
    att = gates.seal_attestations(); assert sorted(att) == ["B1019", "B1033", "B1036", "B1066", "B1071", "B1442"]
    for arc, a in att.items():
        txt = " ".join(open(os.path.join(ROOT, a["file"]), errors="replace").read().split()).lower()
        for k in ("banked_identity", "prior_art"): assert a[k].strip().lower()[:40] in txt, (arc, k)
    assert len(gates.SEAL_PROVENANCE_BASELINE) == 35 and not (set(att) & gates.SEAL_PROVENANCE_BASELINE)
    assert gates.gate_seal_provenance()[0]


def test_the_readers_table_was_verified_not_trusted():
    A = os.path.join(ROOT, "frontier", "B1468_the_frozen_seals_re_audited", "verification")
    raw = json.load(open(os.path.join(A, "readers_raw.json"))); ver = json.load(open(os.path.join(A, "readers_verified.json")))
    assert len(raw) == len(ver) == 42
    assert sum(1 for v in ver if v["A"] == "YES") == 18 and sum(1 for v in ver if v["B"] == "YES") == 15
    assert any(v["A"] == "YES-UNVERIFIED" or v["B"] == "YES-UNVERIFIED" for v in ver)      # the check discarded something
