"""B1541 -- THE COUNT ON THE ROOM: the seal's lock (sealed; no count read but the pulled-back class's (0, 0), which the banked
rows fix).

  - seal integrity: every file of ARTIFACT_HASHES.txt hashes as sealed, and SEAL_LEDGER carries the preregistration's digest;
  - the controls K1-K6 recorded in controls.json all hold, with K1's supplies (4, 18), K2's dimensions (23; 3, 5, 5, 5, 5 in
    both routes), K3's transport and K4's pulled-back count (0, 0);
  - the read-out's logic on synthetic rows (read_out.evaluate is pure: nothing here imports n45, controls or run, which load
    sm:B1536's route_r and reset PARI's stack);
  - the sealed population: 42 subspaces, 127 tasks, 380 readings.
Nothing here writes a tracked file."""
import hashlib
import importlib.util
import json
from itertools import combinations
from pathlib import Path

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


def test_the_verdict_is_open_until_the_bank():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["id"] == "B1541" and v["verdict"] == "OPEN"
    assert "FINDINGS.md" in {p.name for p in ARC.iterdir()}
