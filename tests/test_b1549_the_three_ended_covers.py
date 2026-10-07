"""B1549 -- THE THREE-ENDED COVERS: the seal's lock. Reads committed files only; writes nothing."""
import hashlib
import json
from pathlib import Path

A = Path(__file__).resolve().parents[1] / "frontier" / "B1549_the_three_ended_covers"


def test_the_seal_hashes():
    lines = [x for x in (A / "ARTIFACT_HASHES.txt").read_text().splitlines() if x.strip() and not x.startswith("#")]
    assert len(lines) == 13
    for line in lines:
        h, path = line.split(None, 1)
        assert hashlib.sha256((A / path.strip()).read_bytes()).hexdigest() == h, path


def test_the_population():
    pop = json.loads((A / "verification" / "population.json").read_text())
    assert len(pop["covers"]) == 13 and pop["orbits read"] == 672 and pop["routes agree on every orbit"]
    orbs = pop["member orbits"]
    assert len(orbs) == 46 and pop["members"] == 138
    assert all(o["size"] == 3 and o["m_A"] == 0 and o["P"]["n"] == 1 and o["S"]["n"] == 1 for o in orbs)
    sign = [o for o in orbs if o["order"] == 2]
    assert sorted(o["state"] for o in sign) == ["+LLLLLLR", "+LLLLLLR", "+LLLR", "-LLLLLR", "-LLR", "-LLR"]
    a4 = {"order": 12, "centre": 1, "derived": 4, "element orders": {"1": 1, "2": 3, "3": 8}}
    assert all(o["flavor group"]["G n SL"] == a4 and o["flavor group"]["G"]["order"] == 24 for o in sign)
    assert all(o["flavor group"]["G n SL"]["order"] == 48 for o in orbs if o["order"] == 4)


def test_the_controls():
    c = json.loads((A / "verification" / "controls.json").read_text())
    assert c["all hold"] and c["K1"]["holds"] and c["K4"]["holds"] and c["K5"]["holds"]
    got = {(tuple(x["character"]), x["route"]): x["got"] for x in c["K2"]}
    assert got[((0, 2, 0, 2, 0), "P")] == got[((0, 2, 0, 2, 0), "S")] == [-1, -1]
    assert got[((0, 3, 0, 1, 0), "P")] == got[((0, 3, 0, 1, 0), "S")] == [-1, 0]
    assert all(x["got"][0] == -1 for x in c["K3"])
    t = json.loads((A / "verification" / "controls_trial.json").read_text())
    assert t["all hold"] is False and all(x["got"] == [-1, -2] for x in t["K3"])


def test_the_verdict_record():
    v = json.loads((A / "arc_verdict.json").read_text())
    assert v["id"] == "B1549" and v["verdict"] in ("OPEN", "PROVED", "NEGATIVE")
    assert v["prior_work"]["standing"] == "NEW-AS-SWEPT"
