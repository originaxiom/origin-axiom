"""B1548 -- THE ROOM-THREE CIRCLES: the lock at the seal, and at the bank (NEGATIVE, run as sealed, read out once).

A THREAD result (THE WEAVE rule): N_45 is one cover of one thread (m003), sealed and run at the owner's ruling of 2026-10-14.
  - seal integrity: every file of ARTIFACT_HASHES.txt hashes as sealed, and SEAL_LEDGER carries the preregistration's digest;
  - the controls K1-K9 recorded in controls.json all hold (the circle in both routes, the members on it, tau's orbit of the
    five circles, Lemma Gamma's input and the Galois classes, the banked count at the trivial character, the strata at the
    first member of each order in both routes, the read-out's logic, sm:B1547's member_lib as sealed, the circles' census);
  - the structure census (census.json): 84 members, room three at each, the Galois classes alike;
  - the read-out's logic on synthetic rows, and the sealed population: 84 members, two routes, 168 tasks, three draws;
  - the record is labelled a thread result, and the sealed verdict is OPEN.
Nothing here writes a tracked file."""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1548_the_room_three_circles"
V = ARC / "verification"


def _load(alias, path):
    spec = importlib.util.spec_from_file_location(alias, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_seal_is_intact():
    n = 0
    for line in (ARC / "ARTIFACT_HASHES.txt").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        h, name = line.split(None, 1)
        assert hashlib.sha256((ARC / name).read_bytes()).hexdigest() == h, name
        n += 1
    assert n == 9
    pre = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    led = (ROOT / "docs" / "SEAL_LEDGER.md").read_text()
    assert f"`frontier/B1548_the_room_three_circles/PREREGISTRATION.md` | `{pre}`" in led


def test_the_controls_hold():
    c = json.loads((V / "controls.json").read_text())
    assert c["all hold"] is True
    assert all(c[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9"))
    k1 = c["K1"]
    assert k1["R"]["members"] == k1["F"]["members"] == 84 and k1["R"]["chi0"] == k1["F"]["chi0"]
    want = {"3": 2, "5": 4, "6": 2, "8": 4, "10": 4, "12": 4, "15": 8, "20": 8, "24": 8, "30": 8, "40": 16, "60": 16}
    assert k1["R"]["members by order"] == k1["F"]["members by order"] == want
    for r in ("R", "F"):
        assert c["K2"][r] == {"members": 84, "not trivial on a cusp": 0, "not of exact order": 0, "off the circle": 0}
        assert c["K5"][r]["a generic interior class's count"] == [4, -10]
    assert all(c["K3"]["tau maps each direction to another (up to sign)"])
    assert set(c["K4"]["powers of zeta_24 in the holonomy"]) <= {0, 4} and c["K4"]["|det| rational"] is True
    assert c["K4"]["Galois classes by order"] == {m: (2 if int(m) % 12 == 0 else 1) for m in want}
    rows = c["K6"]["members"]
    assert len(rows) == 12 and all(r["routes agree"] for r in rows)
    assert c["K7"]["holds"] is True and c["K7"]["failed"] == [] and c["K7"]["cases"] == 22
    assert c["K8"]["sealed (sm:B1547)"] == c["K8"]["now"]
    for m in ("2", "3", "4", "5"):
        assert c["K9"][m]["all with n = 3"] is True and c["K9"][m]["exactly the circles' points"] is True


def test_the_structure_census():
    s = json.loads((V / "census.json").read_text())
    assert s["route"] == "R" and s["members"] == 84 and len(s["rows"]) == 84
    assert s["n(nu^4) = 3 at every member"] is True and s["Galois classes"] == 15
    assert s["Galois classes alike in structure"] is True and s["every generic support is U"] is True
    assert all("count" not in json.dumps(r) for r in s["rows"])


def test_the_read_out_logic_and_the_sealed_population():
    RO = _load("b1548_read_out_lock", V / "read_out.py")
    st = RO.selftest()
    assert st["holds"] is True and st["failed"] == [] and st["cases"] == 22
    run = _load("b1548_run_lock", V / "run.py")
    tasks = run.tasks()
    assert (run.MEMBERS, run.ROUTES, run.DRAWS) == (84, ("R", "F"), 3)
    assert run.ORDERS == (3, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60)
    assert len(tasks) == 168 and len(set(tasks)) == 168
    pre = (ARC / "PREREGISTRATION.md").read_text()
    assert "168 tasks" in pre and "BANKED IDENTITY:" in pre and "PRIOR ART:" in pre
    assert "a THREAD result" in pre and "Seal and run it, labelled" in pre


def test_the_sealed_record():
    lb = _load("b1548_load_bearing_lock", ROOT / "scripts" / "checks" / "load_bearing.py")
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["id"] == "B1548" and v["instrument"] is False
    assert v["weave_or_thread"] == "thread"
    assert lb.validate(v["load_bearing"], v["scope"]) == []
    assert [e["id"] for e in v["load_bearing"]] == [f"LB{i}" for i in range(1, 9)]
    assert all(e["status"] == "VERIFIED" for e in v["load_bearing"])


def test_the_banked_read_out():
    import gzip
    raw = gzip.decompress((V / "run.jsonl.gz").read_bytes())
    sha = dict(reversed(line.split()) for line in (V / "run_sha256.txt").read_text().splitlines() if line.strip())
    assert hashlib.sha256(raw).hexdigest() == sha["run.jsonl"]
    assert hashlib.sha256((V / "run.jsonl.gz").read_bytes()).hexdigest() == sha["run.jsonl.gz"]
    rows = [json.loads(x) for x in raw.decode().splitlines() if x.strip()]
    assert len(rows) == 168 and len({(r["route"], r["index"]) for r in rows}) == 168
    RO = _load("b1548_read_out_bank", V / "read_out.py")
    run = _load("b1548_run_bank", V / "run.py")
    res = RO.evaluate(rows, run.tasks(), run.DRAWS, say=lambda s: None)
    res["predictions"]["P1"] = bool(json.loads((V / "identity.json").read_text()).get("identity holds"))
    res["verdict"] = RO.verdict(res)
    rec = json.loads((V / "read_out.json").read_text())
    want = {"P1": True, "P2": True, "P3": True, "P4": True, "P5": True, "P6": True, "P7": True, "P8": False, "P9": True,
            "P10": False}
    assert res["predictions"] == rec["predictions"] == want
    assert res["verdict"] == rec["verdict"] == "NEGATIVE" and res["complete"] is True
    assert res["the least generic I(W1)"] == rec["the least generic I(W1)"] == 0
    assert res["strata with generic (-3, -3)"] == [] and res["strata with a generation-shaped generic reading (both routes)"] == []
    T = _load("b1548_post_run_bank", V / "post_run_tables.py")
    tab = T.tables(rows)
    banked = json.loads((V / "post_run_tables.json").read_text())
    assert tab["R"]["generic counts by (|U|, count)"] == banked["R"]["generic counts by (|U|, count)"] == {"(0, [0, -5])": 84}
    assert tab["F"]["generic counts by (|U|, count)"] == {"(0, [0, -5])": 84}
    assert tab["R"]["largest s - k"] == banked["R"]["largest s - k"] == 0
    assert tab["R"]["largest t - k"] == banked["R"]["largest t - k"] == 5


def test_the_verdict_and_its_records():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["verdict"] == "NEGATIVE" and v["creates_law"] is True and v["weave_or_thread"] == "thread"
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text()
    assert "| T-THE-ROOM-THREE-CIRCLES |" in reg and "| B1548 |" in reg
    kills = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text())
    k = [x for x in kills if x.get("id") == "B1548"]
    assert len(k) == 1 and k[0]["kill_form"].startswith("the-third-ten-is-missing") and k[0]["fact_computed"] is True
    f = (ARC / "FINDINGS.md").read_text()
    assert "cc (the SM-derivation seat), 2026-10-14." in f and "## Seen first" in f and "0 of 19" in f
    assert "THREAD result" in f and "NEGATIVE" in f and "sweep" in f and "literature" in f
    led = (ROOT / "docs" / "SEAL_LEDGER.md").read_text()
    assert "B1548 VERDICT: NEGATIVE, run as sealed (aa350651" in led
