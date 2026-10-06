"""B1544 -- THE FLOOR AT THE CUP KERNEL: the seal's lock (sealed; no count at a non-interior class of K0 read).

  - seal integrity: every file of ARTIFACT_HASHES.txt hashes as sealed, and SEAL_LEDGER carries the preregistration's digest;
  - the controls K1-K6 recorded in controls.json all hold: the structure in both routes equals the sealed run.STRUCTURE (the
    closed supports of K0 and the deck group's action on the cusps), the banked interior and full-stratum counts, and Lemma F's
    ingredients at a generic and an interior class;
  - the read-out's logic on synthetic rows (read_out.py and run.py import nothing heavy: neither loads floor_lib at import);
  - the sealed population: 30 subspaces, 90 tasks, 180 readings;
  - the load-bearing record (WORKING_RULES 2026-10-06) is well formed.
Nothing here writes a tracked file."""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1544_the_floor_at_the_cup_kernel"
V = ARC / "verification"
COVERS = ("N45", "d10.13", "d10.16", "d10.36", "d10.40")


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
    assert n == 7
    pre = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    led = (ROOT / "docs" / "SEAL_LEDGER.md").read_text()
    assert f"`frontier/B1544_the_floor_at_the_cup_kernel/PREREGISTRATION.md` | `{pre}`" in led


def test_the_controls_hold():
    c = json.loads((V / "controls.json").read_text())
    run = _load("b1544_run_lock", V / "run.py")
    assert c["all hold"] is True
    assert all(c[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6"))
    for cid in COVERS:
        k1 = c["K1"][cid]
        sF, sR = k1["route F"], k1["route R"]
        assert sF == sR
        assert sF["closed supports of K0 [S, dim K0(S)]"] == run.STRUCTURE[cid]["closed"]
        assert {int(a): b for a, b in sF["tau on the cusps"].items()} == run.STRUCTURE[cid]["tau"]
        assert c["K3"][cid]["interior count (route F, route R)"][0] == c["K3"][cid]["banked"]
        for route in ("F", "R"):
            g, i = c["K6"][cid][route]["generic"], c["K6"][cid][route]["interior"]
            m = g["lemma F"]["m"]
            assert g["lemma F"]["h0(dN;W*)"] == i["lemma F"]["h0(dN;W*)"] == 2 * m
            assert len(g["support"]) == m and i["support"] == []
            assert g["count"][0] == -1 + 2 * m - g["lemma F"]["r1(W)"] >= -1
    n1 = {cid: c["K1"][cid]["route F"]["n(1)"] for cid in COVERS}
    assert n1 == {"N45": 4, "d10.13": 3, "d10.16": 3, "d10.36": 3, "d10.40": 3}
    assert c["K4"]["cases"] == 10


def test_the_read_out_logic():
    RO = _load("b1544_read_out_lock", V / "read_out.py")
    st = RO.selftest()
    assert st["holds"] is True and st["cases"] == 10
    assert RO.verdict({"P1": True, "P2": True, "P3": True, "P4": False, "P5": False, "P6": False}) == "PROVED"
    assert RO.verdict({"P1": True, "P2": True, "P3": True, "P4": True, "P5": False, "P6": False}) == "NEGATIVE"
    assert RO.verdict({"P1": None, "P2": True, "P3": True, "P4": True, "P5": False, "P6": False}) == "OPEN"
    assert RO.orbit_key((0, 1, 3, 5), {0: 1, 1: 0, 3: 13, 13: 3, 5: 7, 7: 5}) == \
        RO.orbit_key((0, 1, 7, 13), {0: 1, 1: 0, 3: 13, 13: 3, 5: 7, 7: 5})


def test_the_sealed_population():
    run = _load("b1544_run_lock2", V / "run.py")
    subs = sum(len(run.subspaces(cid)) for cid in run.COVERS)
    tasks = run.tasks()
    assert (subs, len(tasks), 2 * len(tasks)) == (30, 90, 180)
    assert len(set(tasks)) == 90 and run.DRAWS == 3
    sizes = {cid: sorted(len(S) for S, _ in run.STRUCTURE[cid]["closed"]) for cid in run.COVERS}
    assert sizes["N45"] == [3] * 10 + [4] * 5 + [5]
    assert sizes["d10.13"] == sizes["d10.36"] == [0, 4, 4, 4, 6]
    assert sizes["d10.16"] == sizes["d10.40"] == [0, 4]
    pre = (ARC / "PREREGISTRATION.md").read_text()
    assert "30 subspaces, 90 tasks and 180 readings" in pre


def test_the_load_bearing_record():
    lb = _load("b1544_load_bearing_lock", ROOT / "scripts" / "checks" / "load_bearing.py")
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert lb.validate(v["load_bearing"], v["scope"]) == []
    assert [e["id"] for e in v["load_bearing"]] == [f"LB{i}" for i in range(1, 8)]


def test_the_verdict_is_open_until_the_bank():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["id"] == "B1544" and v["verdict"] == "OPEN"
    assert "FINDINGS.md" in {p.name for p in ARC.iterdir()}
