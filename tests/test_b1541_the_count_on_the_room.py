"""B1541 -- THE COUNT ON THE ROOM: the lock (banked NEGATIVE, scoped; run as sealed, read out once on 2026-10-06).

  - seal integrity: every file of ARTIFACT_HASHES.txt hashes as sealed, and SEAL_LEDGER carries the preregistration's digest;
  - the controls K1-K6 recorded in controls.json all hold, with K1's supplies (4, 18), K2's dimensions (23; 3, 5, 5, 5, 5 in
    both routes), K3's transport and K4's pulled-back count (0, 0);
  - the read-out's logic on synthetic rows (read_out.evaluate is pure: nothing here imports n45, controls or run, which load
    sm:B1536's route_r and reset PARI's stack);
  - the sealed population: 42 subspaces, 127 tasks, 380 readings;
  - the record is the run (run.jsonl.gz against run_sha256.txt) and the read-out reproduces from it (read_out.evaluate on the
    record's rows), as banked: P1, P2, P3, P6 True, P4, P5 False, verdict NEGATIVE, the counts by subspace;
  - route F, the independent audit: separate code (its imports), and its record agrees with the run at all 54 readings; a slow
    test reads one class again by route F.
Nothing here writes a tracked file."""
import gzip
import hashlib
import importlib.util
import json
import re
from itertools import combinations
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1541_the_count_on_the_room"
V = ARC / "verification"


def _read_out():
    spec = importlib.util.spec_from_file_location("b1541_read_out_lock", V / "read_out.py")
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
    assert f"`frontier/B1541_the_count_on_the_room/PREREGISTRATION.md` | `{pre}`" in (ROOT / "docs" / "SEAL_LEDGER.md").read_text()


def test_the_controls_hold():
    c = json.loads((V / "controls.json").read_text())
    assert c["all hold"] is True
    assert all(c[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6"))
    assert c["K1"]["route N (n(1), n(rho))"] == c["K1"]["route R (n(1), n(rho))"] == [4, 18]
    assert c["K1"]["degree"] == 45 and c["K1"]["cusps"] == 5
    assert c["K2"]["h1 (route N p_N, route R p_N, route R p_R)"] == [23, 23, 23]
    assert c["K2"]["eigenspaces (route N)"] == c["K2"]["eigenspaces (route R, p_R)"] == [3, 5, 5, 5, 5]
    assert c["K3"]["rank on H^1"] == 23 and c["K3"]["carries deck_N to deck_R"] is True
    assert c["K4"]["route N"] == c["K4"]["route R"] == c["K4"]["route R at p_N (transported)"] == [0, 0]
    assert c["K6"]["cases"] == 8


def test_the_read_out_logic():
    RO = _read_out()
    tasks = [("A", "S=", 0), ("B", "j=1", 0), ("C", "pulled back", 0)]

    def rows(counts, tamper=None):
        out = [dict(part="C", subspace="pulled back", draw=0, route=r,
                    reading={"count": [0, 0], "k": 5, "rk d1": {}, "all": True, "failed": []}) for r in ("N", "R")]
        for part, name, draw in tasks[:2]:
            for route in ("N", "R at p_N (the same class)", "R"):
                cnt = tamper if (tamper and route == "R at p_N (the same class)") else counts[name]
                out.append(dict(part=part, subspace=name, draw=draw, route=route,
                                reading={"count": list(cnt), "k": 5, "rk d1": {}, "all": True, "failed": []}))
        return out
    neg = RO.evaluate(rows({"S=": (-1, -4), "j=1": (-2, -7)}), tasks, say=lambda s: None)["predictions"]
    assert neg == {"P1": True, "P2": True, "P3": True, "P4": False, "P5": False, "P6": True}
    assert RO.verdict(neg) == "NEGATIVE"
    three = RO.evaluate(rows({"S=": (-3, -3), "j=1": (-2, -7)}), tasks, say=lambda s: None)["predictions"]
    assert three["P5"] is True and RO.verdict(three) == "PROVED"
    off = RO.evaluate(rows({"S=": (-1, -4), "j=1": (-2, -7)}, tamper=(-3, -3)), tasks, say=lambda s: None)["predictions"]
    assert off["P1"] is False and off["P5"] is False and RO.verdict(off) == "OPEN"
    anom = RO.evaluate(rows({"S=": (-3, 3), "j=1": (-2, -7)}), tasks, say=lambda s: None)["predictions"]
    assert anom["P4"] is False
    short = RO.evaluate(rows({"S=": (-1, -4), "j=1": (-2, -7)})[:-1], tasks, say=lambda s: None)["predictions"]
    assert short["P4"] is None and RO.verdict(short) == "OPEN"


def test_the_sealed_population():
    names = ["S=" + ",".join(map(str, S)) for k in range(6) for S in combinations(range(5), k)]
    assert len(names) == 32
    pre = (ARC / "PREREGISTRATION.md").read_text()
    assert "127 tasks and 380 readings" in pre and "42 subspaces × 3 draws × 3 readings" in pre
    assert 42 * 3 + 1 == 127 and 42 * 3 * 3 + 2 == 380


COUNTS = {"A S=0,1,2,3,4": [[5, -5]], "B j=0": [[0, -5]], "B j=0 interior": [[-1, -10]], "B j=1": [[5, -5]],
          "B j=1 interior": [[3, -10]], "B j=2": [[5, -5]], "B j=2 interior": [[3, -10]], "B j=3": [[5, -5]],
          "B j=3 interior": [[3, -10]], "B j=4": [[5, -5]], "B j=4 interior": [[3, -10]]}
PRED = {"P1": True, "P2": True, "P3": True, "P4": False, "P5": False, "P6": True}


def _sealed_tasks():
    names = ["S=" + ",".join(map(str, S)) for k in range(6) for S in combinations(range(5), k)]
    subs = [("A", n) for n in names] + [("B", f"j={j}") for j in range(5)] + [("B", f"j={j} interior") for j in range(5)]
    return [(part, name, draw) for part, name in subs for draw in range(3)] + [("C", "pulled back", 0)]


def test_the_record_is_the_run():
    sha = dict(reversed(line.split()) for line in (V / "run_sha256.txt").read_text().splitlines() if line.strip())
    raw = gzip.open(V / "run.jsonl.gz", "rb").read()
    assert hashlib.sha256((V / "run.jsonl.gz").read_bytes()).hexdigest() == sha["run.jsonl.gz"]
    assert hashlib.sha256(raw).hexdigest() == sha["run.jsonl"]
    assert len([x for x in raw.decode().splitlines() if x.strip()]) == 380


def test_the_read_out_as_banked():
    ro = json.loads((V / "read_out.json").read_text())
    assert ro["predictions"] == PRED and ro["verdict"] == "NEGATIVE" and ro["complete"] is True
    assert ro["tasks"] == ro["tasks read in full"] == 127
    by = ro["the counts by subspace (route N; route R's own)"]
    for k, v in COUNTS.items():
        assert by[k] == v, k
    for k, v in by.items():
        if k.startswith("A S="):
            n = len([x for x in k[4:].split(",") if x])
            assert v == [[4, -10]] if n <= 2 else v == [[5, -7]] if n == 3 else v == [[5, -6]] if n == 4 else v == [[5, -5]], k
    assert ro["generation-shaped classes"] == [] and ro["three-generation classes"] == []
    assert ro["the pulled-back class"] == {"N": [0, 0], "R": [0, 0]}


def test_the_read_out_reproduces_from_the_record():
    RO = _read_out()
    rows = [json.loads(x) for x in gzip.open(V / "run.jsonl.gz", "rt").read().splitlines() if x.strip()]
    res = RO.evaluate(rows, _sealed_tasks(), say=lambda s: None)
    assert res["predictions"] == PRED and RO.verdict(res["predictions"]) == "NEGATIVE"
    ro = json.loads((V / "read_out.json").read_text())
    assert res["the counts by subspace (route N; route R's own)"] == ro["the counts by subspace (route N; route R's own)"]


def test_route_f_is_separate_code():
    src = (V / "route_f.py").read_text()
    mods = set(re.findall(r"^\s*(?:import|from)\s+([\w.]+)", src, re.M))
    assert mods <= {"fractions", "math", "numpy"}, mods
    for banned in ("cypari", "flint", "route_r", "route_n", "cover_lib", "exact_lib", "exact_states", "n45", "B1536"):
        assert banned not in src.split('"""', 2)[-1], banned


def test_the_audit_agrees():
    a = json.loads((V / "audit_f.json").read_text())
    assert a["agrees"] is True and a["structure agrees"] is True and a["disagreements"] == []
    assert len(a["readings"]) == 54 and all(r["agrees"] for r in a["readings"])
    assert a["positive control: non-zero counts returned exactly"] == 54
    assert len(a["primes"]) == 3 and all(int(p) % 120 == 1 for p in a["primes"])
    for st in a["primes"].values():
        assert (st["h1(rho)"], st["n(rho)"], st["n(1)"], st["eigenspaces"]) == (23, 18, 4, [3, 5, 5, 5, 5])


@pytest.mark.slow
def test_route_f_reads_one_class_again():
    import random
    import numpy as np
    spec = importlib.util.spec_from_file_location("b1541_route_f_lock", V / "route_f.py")
    F = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(F)
    data = json.loads((V / "route_f_input_n45.json").read_text())
    S = F.State(data)
    cov = F.Cover(S, data["perms"])
    p = F.primes(1)[0]
    mats = S.four(p, F.root_of_order(p, 24))
    assert all(S.checks(mats, p).values())
    C = F.Coh(cov, F.base_system(cov, mats), p, keep=True)
    rng = random.Random(7)
    z = F.mm(C.Z, np.array([[rng.randrange(1, p)] for _ in range(C.Z.shape[1])], dtype=np.int64), p).ravel()
    assert F.count(cov, mats, z, p)[0] == [5, -5]


def test_the_verdict_as_banked():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["id"] == "B1541" and v["verdict"] == "NEGATIVE"
    lb = importlib.util.spec_from_file_location("b1541_load_bearing_lock", ROOT / "scripts" / "checks" / "load_bearing.py")
    mod = importlib.util.module_from_spec(lb)
    lb.loader.exec_module(mod)
    assert mod.validate(v["load_bearing"], v["scope"]) == []
