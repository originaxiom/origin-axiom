"""B1546 -- THE LOW-RANK CLASSES: the lock (banked NEGATIVE, run as sealed; read out once 2026-10-06 21:05:27Z).

  - seal integrity: every file of ARTIFACT_HASHES.txt hashes as sealed, and SEAL_LEDGER carries the preregistration's digest;
  - the controls K1-K7 recorded in controls.json all hold: the structure in both routes is the sealed one (Proposition L's
    checks L0-L3, the spaces' dimensions, the eigen-lines and the entries of F they fill, Lemma M's input, the three-cusp
    strata of K0), and the banked counts are reproduced;
  - the read-out's logic on synthetic rows (read_out.py and run.py import nothing heavy at import);
  - the sealed population: 22 subspaces, 66 tasks, 132 readings;
  - the load-bearing record (WORKING_RULES 2026-10-06) is well formed;
  - the banked read-out, re-derived in memory from the gzipped record (its sha-256s checked): NEGATIVE, every family's generic
    class at I(W) >= -1, the Massey rank 0 at every interior subspace;
  - the verdict and its records (THEOREM_REGISTRY, the kill graph, FINDINGS).
Nothing here writes a tracked file."""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1546_the_low_rank_classes"
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
    assert n == 8
    pre = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    led = (ROOT / "docs" / "SEAL_LEDGER.md").read_text()
    assert f"`frontier/B1546_the_low_rank_classes/PREREGISTRATION.md` | `{pre}`" in led


def test_the_controls_hold():
    c = json.loads((V / "controls.json").read_text())
    assert c["all hold"] is True
    assert all(c[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7"))
    sF, sR = c["K1"]["F"]["structure"], c["K1"]["R"]["structure"]
    assert sF == sR and sF["Proposition L holds"] is True
    assert sF["dim V_j^int"] == [2, 4, 4, 4, 4] and sF["dim (K_-j)^int"] == [3, 3, 3, 3]
    assert (sF["dim Kc0"], sF["Kc0 meets K0 in"], sF["image on Kc0"]) == (10, 0, 4)
    supp = sF["entries of F filled by each eigen-line"]
    assert supp["u1"] == [[3, 2]] and supp["va"] == [[1, 1], [4, 4]]
    filled = sorted(tuple(e) for v in supp.values() for e in v)
    assert filled == sorted((t, m) for t in range(1, 5) for m in range(1, 5))
    for route in ("F", "R"):
        pl = c["K1"][route]["Proposition L (the checks)"]
        assert all(pl["L2: gamma_j^3 in the ideal of H's 3 x 3 minors"])
        assert all(a and b for a, b in pl["L1a: pencil rank 2 at every y; kernels in K_-j"].values())
        assert c["K3"][route] == {"interior": [4, -10], "zeta^0 interior": [-1, -10], "zeta^1 interior": [3, -10],
                                  "K0(S=0,1,2)": [0, 0]}
        assert c["K6"][route]["count"] == [5, -5]
    lm = [v for k, v in sF.items() if k.startswith("Lemma M's input")][0]
    assert lm["n(1)"] == 4 and lm["generic V_0^int"] == 4 and lm["u1"] == 1 and lm["w1"] == lm["va"] == 2
    assert c["K4"]["cases"] == 13


def test_the_read_out_logic():
    RO = _load("b1546_read_out_lock", V / "read_out.py")
    st = RO.selftest()
    assert st["holds"] is True and st["cases"] == 13
    tau = {0: 1, 1: 4, 4: 2, 2: 5, 5: 0}
    assert RO.orbit_key((0, 1, 2), tau) == RO.orbit_key((1, 4, 5), tau)
    assert RO.orbit_key((0, 1, 2), tau) != RO.orbit_key((0, 1, 4), tau)


def test_the_sealed_population():
    run = _load("b1546_run_lock", V / "run.py")
    tasks = run.tasks()
    assert (len(run.SUBSPACES), len(tasks), 2 * len(tasks)) == (22, 66, 132)
    assert len(set(tasks)) == 66 and run.DRAWS == 3
    assert sum(1 for s in run.SUBSPACES if s.startswith("X:")) == 10
    assert all(run.SUBSPACES[s]["rank"] == (1 if s[0] in "ZXu" and s != "Z2" else 2) for s in run.SUBSPACES)
    pre = (ARC / "PREREGISTRATION.md").read_text()
    assert "22 subspaces, 66 tasks and 132 readings" in pre


def test_the_load_bearing_record():
    lb = _load("b1546_load_bearing_lock", ROOT / "scripts" / "checks" / "load_bearing.py")
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert lb.validate(v["load_bearing"], v["scope"]) == []
    assert [e["id"] for e in v["load_bearing"]] == [f"LB{i}" for i in range(1, 8)]


def test_the_banked_read_out():
    import gzip
    raw = gzip.decompress((V / "run.jsonl.gz").read_bytes())
    sha = dict(reversed(line.split()) for line in (V / "run_sha256.txt").read_text().splitlines() if line.strip())
    assert hashlib.sha256(raw).hexdigest() == sha["run.jsonl"]
    assert hashlib.sha256((V / "run.jsonl.gz").read_bytes()).hexdigest() == sha["run.jsonl.gz"]
    rows = [json.loads(x) for x in raw.decode().splitlines() if x.strip()]
    assert len(rows) == 132
    RO = _load("b1546_read_out_bank", V / "read_out.py")
    run = _load("b1546_run_bank", V / "run.py")
    res = RO.evaluate(rows, run.tasks(), run.SUBSPACES, run.TAU, say=lambda s: None)
    res["verdict"] = RO.verdict(res)
    rec = json.loads((V / "read_out.json").read_text())
    assert res["predictions"] == rec["predictions"] == {"P1": True, "P2": True, "P3": True, "P4": True, "P5": True,
                                                        "P6": False, "P7": False, "P8": True}
    assert res["verdict"] == rec["verdict"] == "NEGATIVE" and res["complete"] is True
    fams = res["the generic families' counts (read alike in both routes)"]
    assert fams["Z1"] == [-1, -9] and fams["Z2"] == [-1, -10]
    assert all(c == [0, -7] for s, c in fams.items() if s.startswith("X:")) and len(fams) == 12
    assert res["the least I(W) over the generic families"] == -1
    assert set(res["the Massey rank mu = -1 - I(W) at the interior subspaces"].values()) == {0}
    counts = res["the counts by subspace (route F; route R)"]
    for x in ("u1", "u2", "u3", "u4", "w1", "w2", "w3", "w4"):
        assert counts[x] == {"F": [[-1, -9]], "R": [[-1, -9]]}
    assert counts["va"] == counts["vb"] == {"F": [[-1, -8]], "R": [[-1, -8]]}
    for r in rows:
        x = r["reading"]
        if r["route"] == "R" and not x["support"]:
            assert x["rk d1"]["E"] == x["rk d1"]["E*"] == x["rk delta1_W"]          # s = r: Lemma M's mu = 0


def test_the_verdict_and_its_records():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["id"] == "B1546" and v["verdict"] == "NEGATIVE" and v["creates_law"] is True and v["instrument"] is False
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text()
    assert "| T-THE-LOW-RANK-CLASSES |" in reg and "| T-THE-MASSEY-TERM |" in reg and "| B1546 |" in reg
    kills = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text())
    k = [x for x in kills if x.get("id") == "B1546"]
    assert len(k) == 1 and k[0]["kill_form"].startswith("the-low-rank-classes-sit-on-the-floor") and k[0]["fact_computed"] is True
    f = (ARC / "FINDINGS.md").read_text()
    assert "cc (the SM-derivation seat), 2026-10-06." in f and "## Seen first" in f and "0 of 19" in f
