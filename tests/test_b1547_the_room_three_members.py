"""B1547 -- THE ROOM-THREE MEMBERS: the lock (banked NEGATIVE, run as sealed; read out once 2026-10-07 04:29:29Z).

  - seal integrity: every file of ARTIFACT_HASHES.txt hashes as sealed, and SEAL_LEDGER carries the preregistration's digest;
  - the controls K1-K8 recorded in controls.json all hold: the population in both routes (the 46 common loops, the n of the
    fifteen order-2 characters, the five room-three keys, the 1024 members named alike, 256 Galois classes of size 4), every
    member trivial on every cusp with nu^4 = chi0, tau's orbit, Lemma Gamma's input, the banked count at the trivial character
    in both routes, the strata at eight sample members in both routes, route F's class_basis;
  - the read-out's logic on synthetic rows (read_out.py and run.py import nothing heavy at import);
  - the sealed population: 1024 members, two routes, 2048 tasks, three draws per distinct stratum;
  - the load-bearing record (WORKING_RULES 2026-10-06) is well formed;
  - the banked read-out, re-derived in memory from the gzipped record (its sha-256s checked): NEGATIVE, the least generic
    I(W1) -2, no (-3, -3), no generation shape; the post-run tables re-derived (s - k <= 2 at every stratum reading);
  - the verdict and its records (THEOREM_REGISTRY, the kill graph, FINDINGS).
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
    assert v["id"] == "B1547" and v["instrument"] is False
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
    assert len(rows) == 2048 and len({(r["route"], r["index"]) for r in rows}) == 2048
    RO = _load("b1547_read_out_bank", V / "read_out.py")
    run = _load("b1547_run_bank", V / "run.py")
    res = RO.evaluate(rows, run.tasks(), run.DRAWS, say=lambda s: None)
    res["predictions"]["P1"] = bool(json.loads((V / "identity.json").read_text()).get("identity holds"))
    res["verdict"] = RO.verdict(res)
    rec = json.loads((V / "read_out.json").read_text())
    want = {"P1": True, "P2": True, "P3": True, "P4": True, "P5": True, "P6": True, "P7": False, "P8": False, "P9": True,
            "P10": False}
    assert res["predictions"] == rec["predictions"] == want
    assert res["verdict"] == rec["verdict"] == "NEGATIVE" and res["complete"] is True
    assert res["the least generic I(W1)"] == rec["the least generic I(W1)"] == -2
    assert res["strata with generic (-3, -3)"] == [] and res["strata with a generation-shaped generic reading (both routes)"] == []
    assert res["route R: strata by (|U|, generic count)"] == rec["route R: strata by (|U|, generic count)"]
    T = _load("b1547_post_run_bank", V / "post_run_tables.py")
    tab = T.tables(rows)
    banked = json.loads((V / "post_run_tables.json").read_text())
    assert tab["R"]["generic counts by (|U|, count)"] == banked["R"]["generic counts by (|U|, count)"]
    assert tab["R"]["largest s - k"] == banked["R"]["largest s - k"] == 2
    assert tab["R"]["largest t - k"] == banked["R"]["largest t - k"] == 5
    assert tab["F"]["generic counts by (|U|, count)"] == tab["R"]["generic counts by (|U|, count)"]


def test_the_verdict_and_its_records():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["verdict"] == "NEGATIVE" and v["creates_law"] is True
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text()
    assert "| T-THE-ROOM-THREE-MEMBERS |" in reg and "| B1547 |" in reg
    kills = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text())
    k = [x for x in kills if x.get("id") == "B1547"]
    assert len(k) == 1 and k[0]["kill_form"].startswith("the-third-ten-is-missing") and k[0]["fact_computed"] is True
    f = (ARC / "FINDINGS.md").read_text()
    assert "cc (the SM-derivation seat), 2026-10-07." in f and "## Seen first" in f and "0 of 19" in f
    assert "sweep" in f and "literature" in f and "NEGATIVE" in f
