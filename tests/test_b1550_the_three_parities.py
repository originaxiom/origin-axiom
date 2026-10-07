"""B1550 -- THE THREE PARITIES: the seal's lock. Reads committed files only; writes nothing."""
import hashlib
import json
from collections import Counter
from pathlib import Path

A = Path(__file__).resolve().parents[1] / "frontier" / "B1550_the_three_parities"


def test_the_seal_hashes():
    lines = [x for x in (A / "ARTIFACT_HASHES.txt").read_text().splitlines() if x.strip() and not x.startswith("#")]
    assert len(lines) == 13
    for line in lines:
        h, path = line.split(None, 1)
        assert hashlib.sha256((A / path.strip()).read_bytes()).hexdigest() == h, path


def test_the_population():
    pop = json.loads((A / "verification" / "population.json").read_text())
    assert [s["state"] for s in pop["states"]] == ["+LR", "-LR", "+LLLR", "-LLLR"]
    assert pop["orbits read"] == 336 and pop["routes agree on every orbit"]
    orbs = pop["member orbits"]
    assert len(orbs) == 9 and pop["members"] == 60
    assert Counter(o["state"] for o in orbs) == {"+LR": 8, "-LR": 1}
    assert not any(o["golden-fixed"] for o in orbs) and all(o["size"] in (12, 6, 3) for o in orbs)
    sign = [o for o in orbs if o["state"] == "+LR" and o["order"] == 2]
    assert len(sign) == 2 and all(o["size"] == 12 for o in sign)
    for o in sign:
        labs = Counter(tuple(m["label"]) for m in o["members"].values())
        assert labs == {(1, 0): 4, (0, 1): 4, (1, 1): 4}
        assert all(m["m_A"] == 0 and m["support"] == 2 for m in o["members"].values())
        assert (o["P"]["h1"], o["P"]["r1"], o["P"]["n"]) == (1, 0, 1) == (o["S"]["h1"], o["S"]["r1"], o["S"]["n"])
        # the V4 blocks are the label classes
        for blk in o["v4 orbits"]:
            assert len({tuple(o["members"][json.dumps(ch)]["label"]) for ch in blk}) == 1
    a, b = ({tuple(x) for x in o["orbit"]} for o in sign)
    eps = (2, 2, 2, 0, 2, 2)
    assert {tuple((u + v) % 4 for u, v in zip(x, eps)) for x in a} == b


def test_the_controls():
    c = json.loads((A / "verification" / "controls.json").read_text())
    assert c["all hold"] and c["K1"]["holds"] and c["K3"]["holds"] and c["K4"]["holds"] and c["K5"]["holds"]
    assert c["K6"]["holds"] and all(x["sign members"] == 0 for x in c["K6"]["covers"])
    assert all(x["got"] == [-1, -1] for x in c["K2"])
    assert all(r["group order"] == 12 and r["element orders"] == {"1": 1, "2": 3, "3": 8} for r in c["K3"]["rows"])
