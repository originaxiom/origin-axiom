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


def _evaluate():
    import gzip
    import importlib.util
    import sys
    v = A / "verification"
    if str(v) not in sys.path:
        sys.path.insert(0, str(v))
    spec = importlib.util.spec_from_file_location("b1550_read_out", v / "read_out.py")
    ro = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ro)
    rows = [json.loads(x) for x in gzip.open(v / "run.jsonl.gz", "rt").read().splitlines() if x.strip()]
    pop = json.loads((v / "population.json").read_text())
    ctl = json.loads((v / "controls.json").read_text())
    idn = json.loads((v / "identity.json").read_text())
    return ro.evaluate(rows, pop, ctl, idn["holds"]), rows


def test_the_record_and_the_read_out():
    import ast
    import gzip
    v = A / "verification"
    sha = {line.split()[1]: line.split()[0] for line in (v / "run_sha256.txt").read_text().splitlines() if line.strip()}
    assert hashlib.sha256(gzip.open(v / "run.jsonl.gz").read()).hexdigest() == sha["run.jsonl"]
    (out, _), rows = _evaluate()
    banked = json.loads((v / "read_out.json").read_text())
    assert len(rows) == 120 and out["complete"]
    assert out["verdict"] == banked["verdict"] == "NEGATIVE"
    assert out["held"] == banked["held"] == ["P1", "P2", "P3", "P4", "P5", "P6", "P9"]
    assert out["states with generation-shaped members"] == ["+LR"]
    shapes = Counter()
    for k, n in out["generic counts by (route, state, order, orbit size, m_A, n, count)"].items():
        route, state, order, size, mA, nn, count = ast.literal_eval(k)
        shapes[(state, order, size, tuple(count))] += n
    assert shapes == {("+LR", 2, 12, (-1, -1)): 48, ("+LR", 4, 6, (-1, -1)): 48, ("+LR", 4, 3, (1, 0)): 12,
                      ("-LR", 2, 6, (0, -3)): 12}


def test_the_parity_labels_after_the_read_out():
    t = json.loads((A / "verification" / "post_run_tables.json").read_text())
    assert t["all generation-shaped members of the root's cover, per label"] == {"[0, 1]": 16, "[1, 0]": 16, "[1, 1]": 16}
    for order in ("order 2", "order 4"):
        g = t[order]["the golden map on the labels"]
        assert g == {"[0, 1]": [[1, 1]], "[1, 0]": [[0, 1]], "[1, 1]": [[1, 0]]}
        assert t[order]["generation-shaped members"] == 24 and t[order]["counts"] == ["[-1, -1]"]


def test_the_verdict_record():
    v = json.loads((A / "arc_verdict.json").read_text())
    assert v["id"] == "B1550" and v["verdict"] == "NEGATIVE" and v["creates_law"] is True
    assert v["prior_work"]["standing"] == "EXTENDS"
    kg = json.loads((A.parents[1] / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text())
    assert any(e["id"] == "B1550" and e["kill_form"].startswith("the-sector-is-wider") for e in kg)
