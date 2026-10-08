"""sm:B1552 THE CHIRAL TRIPLET'S COUNT -- the lock on the banked record (reads only; writes nothing tracked).

The seal's hashes, the complete record (432 readings per route), the read-out's verdict, and the counts: every reading
(0, 0), the two routes and the draws agreeing.
"""
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1552_the_chiral_triplets_count"
VER = ARC / "verification"
SEAL_SHA = "556910b631c715867352057dad3401a50b41e949c077bdcf9ef58178f0c20e69"


def _rows(route):
    with gzip.open(VER / f"run_{route}.jsonl.gz", "rt") as f:
        return [json.loads(line) for line in f]


def test_seal_hash():
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEAL_SHA


def test_artifact_hashes():
    for line in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, name = line.split()
        assert hashlib.sha256((ARC / name).read_bytes()).hexdigest() == digest, name


def test_record_complete():
    for route in (1, 2):
        rows = _rows(route)
        done = {r["state"] for r in rows if r.get("done")}
        readings = [r for r in rows if "count" in r]
        assert len(done) == 12 and len(readings) == 432, (route, len(done), len(readings))


def test_every_count_zero_and_routes_agree():
    c1 = Counter(tuple(r["count"]) for r in _rows(1) if "count" in r)
    c2 = Counter(tuple(r["count"]) for r in _rows(2) if "count" in r)
    assert c1 == c2 == Counter({(0, 0): 432})


def test_read_out_verdict():
    d = json.loads((VER / "read_out.json").read_text(encoding="utf-8"))
    assert d["complete"] and d["P1"] and d["P2"] and d["P3"] and d["P4"]
    assert not any(v for m in d["P5"].values() for v in m.values())
    assert d["verdict"] == "NEGATIVE as sealed"


def test_identity_held():
    d = json.loads((VER / "identity.json").read_text(encoding="utf-8"))
    assert d["all held"] is True and d["I1"]["counts"] == [[-1, -1], [-1, -1]]


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1552" and d["verdict"] == "NEGATIVE" and d["instrument"] is False
    assert "|" not in d["claim_one_line"]


def test_w11_the_zero_is_a_theorem_checked():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_spin_zero.json").read_text(encoding="utf-8"))
    assert d["all held"] is True
    assert d["(1) T2 on sm:B1552's record"]["readings"] == 864
    assert d["(2) the act on V is in a finite group, every state to length 12"]["states"] == 758


def test_w12_the_joined_vacuum_has_no_interior_class():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_joined_vacuum.json").read_text(encoding="utf-8"))
    t = d["tally"]
    assert d["all held"] is True and t["(state, tick)"] >= 24
    assert t["readings with a class"] == t["n = 0 there"] == t["h1 = r1 = h0(T; A) there"] > 0


def test_w13_main_b1434_orbits_of_three_verified():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_class_index_orbits.json").read_text(encoding="utf-8"))
    assert d["all agree with B1434"] and d["every background in a deck orbit of three"]
    assert d["every count one in absolute value"] and d["signs split equally"]
    assert len(d["the states (odd trace, in B1434's range; the engine route), tick 3"]) == 4


def test_w14_the_slope_law_and_the_census():
    D = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    d = json.loads((D / "the_slope_law.json").read_text(encoding="utf-8"))
    assert d["the law held at every candidate"] and d["every in-range row agrees with B1434"]
    assert d["(3) every class paired with its opposite"]
    rows = d["(2) the census, every odd-trace state to length 6, tick 3"]
    assert all(r["the parities"]["firing modules with a parity as the extension character"] == 0 for r in rows.values())
    assert sorted(k for k, r in rows.items() if r["the parities"]["their slope class has"] != 3) == ["+LLLRRR", "+LLRLRR"]
    assert len(rows) == 12
    assert sorted(k for k, r in rows.items() if r["generation_shaped"] == 0) == ["+LLRLRR", "-LLRLRR"]
    sample = json.loads((D / "the_slope_law_sample.json").read_text(encoding="utf-8"))
    assert sample["all agree"] and sample["sampled"] == 300 and sample["firing by the law"] > 0


def _trace(sw):
    """the trace of a signed word's matrix, L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]] (GENESIS §2)"""
    a, b, c, d = 1, 0, 0, 1
    for ch in sw[1:]:
        if ch == "L":
            a, b, c, d = a, a + b, c, c + d
        else:
            a, b, c, d = a + b, b, c + d, d
    return (a + d) * (1 if sw[0] == "+" else -1)


def test_w15_the_hand_theorem():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_hand_theorem.json").read_text(encoding="utf-8"))
    assert all(d["summary"].values()), d["summary"]
    assert d["(iv) det on T by generator (eighths, the two lifts)"] == {"L": [1, 5], "R": [3, 7], "-I": [2, 6]}
    direct = d["(iii) the direct tick-3 act, every odd-trace state to length 8 (both signs)"]
    assert direct["odd-trace states read"] == 32 == direct["tick-3 act = det(w|T) I on T"]
    hand = d["(v) the hand rule from the determinant, GENESIS's states to length 12"]
    assert hand["odd trace"] == 326 == hand["agrees with n_L - n_R + 2[sign -] = 2 mod 4"]
    assert hand["odd-trace words"] == 163 == hand["odd-trace words with exactly one twin apart"]


def test_w15_the_weaves_own_extensions_and_the_mod_16_law():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_weave_extension.json").read_text(encoding="utf-8"))
    summ = dict(d["summary"])
    summ.update(d["(c) length 8, reduced rule"]["summary"])
    assert len(d["summary"]) == 12 and len(d["(c) length 8, reduced rule"]["summary"]) == 20
    for sw, v in summ.items():
        assert v["readings"] > 0
        assert set(v["values"]) <= {1}                                # every firing reading is +1
        assert v["non-zero"] in (0, v["readings"])                     # three or nothing: all or none
        silent = v["non-zero"] == 0
        assert silent == (_trace(sw) % 16 in (1, 15)), sw              # the mod-16 law
    assert sorted(k for k, v in summ.items() if v["non-zero"] == 0) == ["+LLLLLRRR", "+LLRLRR", "-LLLLLRRR", "-LLRLRR"]
    for prime, rows in d["(b) two further primes"].items():
        assert rows["+LR"]["non-zero"] == rows["+LR"]["readings"] and rows["+LLRLRR"]["non-zero"] == 0, prime


def test_w15_the_prediction_recorded_and_its_second_part_failed():
    D = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
    assert "t ≡ ±1 (mod 16)" in (D / "W15_PREDICTION.md").read_text(encoding="utf-8")
    d = json.loads((D / "the_prediction_test.json").read_text(encoding="utf-8"))
    assert d["the control carries some"] and not d["the predicted silent states carry none"] and not d["the prediction holds"]
    assert {s: r["generation_shaped"] for s, r in d["rows"].items()} == {"+LLLLLRRR": 3064, "-LLLLLRRR": 336,
                                                                         "+LLLLLLLR": 480, "-LLLLLLLR": 336}


def test_w15_the_weaves_five_is_not_generation_shaped():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_weaves_five.json").read_text(encoding="utf-8"))
    for sw, v in d["summary"].items():
        pairs = {tuple(x) for x in v["pairs for W"]}
        dual = {tuple(x) for x in v["pairs for W*"]}
        if sw in ("+LLRLRR", "-LLRLRR"):
            assert pairs == dual == {(0, 0)}, sw
        else:
            assert pairs <= {(1, 3), (2, 3)} and dual <= {(-1, -3), (-2, -3)} and (1, 3) in pairs, sw
        assert all(p[0] != p[1] for p in pairs | dual if p != (0, 0))   # never the shape n_5bar = n_10
