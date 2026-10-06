"""B1547 -- THE ROOM-THREE MEMBERS: the lock at the seal (no count at a member read).

  - seal integrity: every file of ARTIFACT_HASHES.txt hashes as sealed, and SEAL_LEDGER carries the preregistration's digest;
  - the controls K1-K8 recorded in controls.json all hold: the population in both routes (the 46 common loops, the n of the
    fifteen order-2 characters, the five room-three keys, the 1024 members named alike, 256 Galois classes of size 4), every
    member trivial on every cusp with nu^4 = chi0, tau's orbit, Lemma Gamma's input, the banked count at the trivial character
    in both routes, the strata at eight sample members in both routes, route F's class_basis;
  - the read-out's logic on synthetic rows (read_out.py and run.py import nothing heavy at import);
  - the sealed population: 1024 members, two routes, 2048 tasks, three draws per distinct stratum;
  - the load-bearing record (WORKING_RULES 2026-10-06) is well formed, and the sealed verdict is OPEN.
Nothing here writes a tracked file."""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1547_the_room_three_members"
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
    assert n == 7
    pre = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    led = (ROOT / "docs" / "SEAL_LEDGER.md").read_text()
    assert f"`frontier/B1547_the_room_three_members/PREREGISTRATION.md` | `{pre}`" in led


def test_the_controls_hold():
    c = json.loads((V / "controls.json").read_text())
    assert c["all hold"] is True
    assert all(c[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8"))
    k1 = c["K1"]
    assert k1["R"] == k1["F"]
    assert k1["R"]["loops"] == 46 and k1["R"]["n of the fifteen"] == [1] * 10 + [3] * 5
    assert k1["R"]["members"] == 1024 and k1["R"]["Galois classes by size"] == {"4": 256}
    for r in ("R", "F"):
        assert c["K2"][r] == {"members": 1024, "cusps": 5, "not trivial on a cusp": 0, "nu^4 not chi0": 0,
                              "not of order 8": 0}
        assert c["K3"][r]["tau's order on the free lattice"] == 5 and c["K3"][r]["one orbit"] is True
        assert c["K5"][r]["a generic interior class's count"] == [4, -10]
    assert set(c["K4"]["powers of zeta_24 in the holonomy"]) <= {0, 4} and c["K4"]["|det| rational"] is True
    rows = c["K6"]["members"]
    assert len(rows) == 8 and all(r["routes agree"] for r in rows)
    assert sum(1 for r in rows if any(U for U in r["R"]["distinct"])) == 4
    assert c["K7"]["holds"] is True and c["K7"]["failed"] == []
    assert all(v["the same"] for k, v in c["K8"].items() if isinstance(v, dict))


def test_the_read_out_logic():
    RO = _load("b1547_read_out_lock", V / "read_out.py")
    st = RO.selftest()
    assert st["holds"] is True and st["failed"] == [] and st["cases"] == 21


def test_the_sealed_population():
    run = _load("b1547_run_lock", V / "run.py")
    tasks = run.tasks()
    assert (run.MEMBERS, run.ROUTES, run.DRAWS) == (1024, ("R", "F"), 3)
    assert len(tasks) == 2048 and len(set(tasks)) == 2048
    pre = (ARC / "PREREGISTRATION.md").read_text()
    assert "2048 tasks" in pre and "BANKED IDENTITY:" in pre and "PRIOR ART:" in pre


def test_the_sealed_record():
    lb = _load("b1547_load_bearing_lock", ROOT / "scripts" / "checks" / "load_bearing.py")
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["id"] == "B1547" and v["verdict"] == "OPEN" and v["instrument"] is False
    assert lb.validate(v["load_bearing"], v["scope"]) == []
    assert [e["id"] for e in v["load_bearing"]] == [f"LB{i}" for i in range(1, 9)]
    f = (ARC / "FINDINGS.md").read_text()
    assert "cc (the SM-derivation seat), 2026-10-06." in f and "## Seen first" in f and "SEALED" in f
