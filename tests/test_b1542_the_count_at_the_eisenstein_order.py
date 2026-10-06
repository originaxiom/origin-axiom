"""B1542 -- THE COUNT AT THE EISENSTEIN ORDER: the seal's lock (sealed; no count read).

  - seal integrity: every file of ARTIFACT_HASHES.txt hashes as sealed, and SEAL_LEDGER carries the preregistration's digest;
  - the controls K1-K7 recorded in controls.json all hold, with K1's supplies ((3, 3) or (3, 7)), K2's dimensions in both
    routes, K3's transport, K4's N_45 values and K7's identification of the state's group with m003;
  - the read-out's logic on synthetic rows (read_out.evaluate is pure: nothing here imports ncyc, controls or run, which load
    sm:B1536's route_r and reset PARI's stack);
  - the sealed population: 556 tasks, 1,664 readings;
  - the load-bearing record (WORKING_RULES 2026-10-06) is well formed.
Nothing here writes a tracked file."""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1542_the_count_at_the_eisenstein_order"
V = ARC / "verification"
SIX = ("d10.13", "d10.36")
FOUR = ("d10.16", "d10.40")


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
    assert f"`frontier/B1542_the_count_at_the_eisenstein_order/PREREGISTRATION.md` | `{pre}`" in led


def test_the_controls_hold():
    c = json.loads((V / "controls.json").read_text())
    assert c["all hold"] is True
    assert all(c[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7"))
    for cid in SIX + FOUR:
        k1, k2, k3 = c["K1"][cid], c["K2"][cid], c["K3"][cid]
        nr = 3 if cid in SIX else 7
        assert k1["degree"] == 60 and k1["cusps"] == (6 if cid in SIX else 4) and k1["the cover sm:B1540 read"] is True
        assert k1["route N (prime, n(1), n(rho), capW, capL2)"][1:] == k1["route R (prime, n(1), n(rho), capW, capL2)"][1:] \
            == [3, nr, 4, nr]
        h1 = 9 if cid in SIX else 11
        eig = [5, 0, 0, 4, 0, 0] if cid in SIX else [5, 0, 2, 2, 2, 0]
        inter = [2, 0, 0, 1, 0, 0] if cid in SIX else [2, 0, 2, 1, 2, 0]
        assert k2["h1 (route N p_N, route R p_N, route R p_R)"] == [h1] * 3
        assert k2["eigenspaces (route N; route R, p_R)"] == [eig, eig]
        assert k2["interior parts (route N; route R, p_R)"] == [inter, inter] and sum(inter) == nr
        assert k3["rank on H^1"] == h1 and k3["carries deck_N to deck_R"] is True
    assert c["K4"]["eigenspaces (route N; route R, p_R)"] == [[3, 5, 5, 5, 5]] * 2
    assert c["K4"]["pulled back (route N, route R, route R at p_N transported)"] == [[0, 0]] * 3
    o3, c3, o4, c4 = c["K7"]["subgroup classes by index <= 7 (ours m003, census m003, ours m004, census m004)"]
    assert o3 == c3 and o4 == c4 and o3 != o4
    assert c["K7"]["isometries"] == {"b+-LR ~ m003": True, "b+-LR ~ m004": False}
    assert c["K6"]["cases"] == 15


def test_the_read_out_logic():
    RO = _load("b1542_read_out_lock", V / "read_out.py")
    tasks = [("d10.13", "A", "S=", 0), ("d10.13", "B", "j=3", 0), ("d10.13", "C", "pulled back", 0),
             ("d10.16", "C", "pulled back", 0)]

    def rows(counts, tamper=None, pb=(0, 0)):
        out = []
        for cid in ("d10.13", "d10.16"):
            out += [dict(cover=cid, part="C", subspace="pulled back", draw=0, route=r,
                         reading={"count": list(pb), "k": 5, "rk d1": {}, "all": True, "failed": []}) for r in ("N", "R")]
        for cid, part, name, draw in tasks[:2]:
            for route in ("N", RO.SAME, "R"):
                cnt = tamper if (tamper and route == RO.SAME) else counts[name]
                out.append(dict(cover=cid, part=part, subspace=name, draw=draw, route=route,
                                reading={"count": list(cnt), "k": 5, "rk d1": {}, "all": True, "failed": []}))
        return out
    say = lambda s: None  # noqa: E731
    neg = RO.evaluate(rows({"S=": (-1, -4), "j=3": (-2, -7)}), tasks, say=say)["predictions"]
    assert neg == {"P1": True, "P2": True, "P3": True, "P4": False, "P5": False, "P6": True}
    assert RO.verdict(neg) == "NEGATIVE"
    three = RO.evaluate(rows({"S=": (-3, -3), "j=3": (-2, -7)}), tasks, say=say)["predictions"]
    assert three["P5"] is True and RO.verdict(three) == "PROVED"
    off = RO.evaluate(rows({"S=": (-1, -4), "j=3": (-2, -7)}, tamper=(-3, -3)), tasks, say=say)["predictions"]
    assert off["P1"] is False and off["P5"] is False and RO.verdict(off) == "OPEN"
    anom = RO.evaluate(rows({"S=": (-3, 3), "j=3": (-2, -7)}), tasks, say=say)["predictions"]
    assert anom["P4"] is False
    short = RO.evaluate(rows({"S=": (-1, -4), "j=3": (-2, -7)})[:-1], tasks, say=say)["predictions"]
    assert short["P4"] is None and RO.verdict(short) == "OPEN"
    onecount = RO.evaluate(rows({"S=": (-1, -4), "j=3": (-2, -7)}, pb=(1, 1)), tasks, say=say)["predictions"]
    assert onecount["P6"] is True


def test_the_sealed_population():
    n_sub = {cid: 2 ** 6 + 2 + 2 for cid in SIX}
    n_sub.update({cid: 2 ** 4 + 4 + 4 for cid in FOUR})
    tasks = sum(3 * n + 1 for n in n_sub.values())
    readings = sum(9 * n + 2 for n in n_sub.values())
    assert (tasks, readings) == (556, 1664)
    pre = (ARC / "PREREGISTRATION.md").read_text()
    assert "556 tasks and 1,664 readings" in pre


def test_the_load_bearing_record():
    lb = _load("b1542_load_bearing_lock", ROOT / "scripts" / "checks" / "load_bearing.py")
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert lb.validate(v["load_bearing"], v["scope"]) == []
    assert [e["id"] for e in v["load_bearing"]] == [f"LB{i}" for i in range(1, 8)]


def test_the_verdict_is_open_until_the_bank():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["id"] == "B1542" and v["verdict"] == "OPEN"
    assert "FINDINGS.md" in {p.name for p in ARC.iterdir()}
