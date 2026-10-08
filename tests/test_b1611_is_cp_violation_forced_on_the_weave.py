"""B1611 -- IS CP VIOLATION FORCED ON THE WEAVE?: the sealed instrument unchanged; the automorphism and CP counts as
recorded; the swap a consistent CP on every sector; GENESIS carries it."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1611_is_cp_violation_forced_on_the_weave"
V = ARC / "verification"


def test_the_sealed_instrument_is_unchanged():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 43ec84e8b: ")
    assert hashlib.sha256(open(V / "cp_on_the_weave.py", "rb").read()).hexdigest() == first.split()[4]


def test_the_cells_as_recorded():
    d = json.load(open(V / "cp_on_the_weave.json"))
    assert d["C1"]["order_G"] == 96 and d["C1"]["order_G_with_swap"] == 192
    c2 = d["C2"]
    assert c2["automorphisms"] == 96 and c2["inner"] == 24 and c2["cp_candidates_on_T"] == 24
    assert c2["swap_conjugation_is_an_automorphism"] and c2["swap_conjugation_sends_T_to_Tbar"]
    assert d["C3"]["class_inverting_automorphisms"] == 24 and d["C3"]["type_I"] is False
    assert d["C4"]["consistent_cp_on_T_exists"]
    for lab in ("T(x)T", "T(x)Tbar"):
        v = d["C5"][lab]
        assert v["sectors_forcing_cp_violation"] == [] and sorted(p["dim"] for p in v["pieces"]) == [1, 2, 3, 3]
        assert all(p["norm"] == 1.0 and p["consistent_cp_on_T_and_r"] > 0 for p in v["pieces"])


def test_one_cp_on_every_sector_and_it_is_the_swap():
    p = json.load(open(V / "post_seal_one_cp.json"))
    assert p["one_cp_consistent_on_every_sector"] == 10 and p["those_are_involutions_up_to_inner"]
    assert p["swap_conjugation_consistent_on_every_sector"] and all(v[0] == 1.0 for v in p["swap_conjugation"].values())


def test_genesis_carries_it():
    g = open(ROOT / "GENESIS.md", encoding="utf-8").read()
    assert int(g.split("**Version 1.")[1].split()[0]) >= 32 and "CP ON THE WEAVE (main, B1611" in g
    assert "the weave's generalized CP is the record swap" in g
