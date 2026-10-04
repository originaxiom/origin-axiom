"""B1540 -- THE ROOM FOR THREE, AT THE GOLDEN AND THE EISENSTEIN ORDERS: the lock.

  - the census record (verification/pulled_back_rooms.json): thirty room covers, no conflicting banked value, seven cyclic covers
    with room >= 3 (m003's d9.2 at order 5; d10.13, d10.14, d10.16, d10.36, d10.38, d10.40 at order 6), m004's best room 1;
  - N_45's record (verification/room_n45.json): supplies (4, 18) by Lemma A, route N and route R; H_1 = Z^9 + (Z/2)^2 with five
    cusps; room 5; the pulled-back count (0, 0) by the banked rows and in both routes; every route agrees;
  - the degree-60 record (verification/room_60.json): (3, 3) or (3, 7) in both routes and by Lemma A, b1 - cusps = 3, rooms
    3, 3, 4, 3, 3, 4, four conjugacy classes; every route agrees;
  - a live re-derivation of N_45 from sm:B1536's banked rows alone (pure Python);
  - the full reproductions (slow): pulled_back_rooms.py, room_60.py and room_n45.py reproduce their records.
Nothing here writes a tracked file."""
import gzip
import importlib.util
import json
from fractions import Fraction as Fr
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1540_the_room_for_three"
VER = ARC / "verification"
B1536V = ROOT / "frontier" / "B1536_the_finite_covers" / "verification"
SIX = ["m003:d10.13", "m003:d10.14", "m003:d10.16", "m003:d10.36", "m003:d10.38", "m003:d10.40"]


def _record(name):
    return json.loads((VER / name).read_text())


def _module(alias, name):
    spec = importlib.util.spec_from_file_location(alias, VER / name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_census_record():
    r = _record("pulled_back_rooms.json")
    assert r["population"] == 30 and len(r["by member"]) == 30
    assert r["conflicts"] == 0
    assert r["members with room >= 3 on a fixed pulled-back cyclic cover"] == sorted(SIX + ["m003:d9.2"])
    assert r["m004: best room on a fixed pulled-back cyclic cover"] == 1
    assert sum(x["cyclic subgroups fully fixed"] for x in r["by member"].values()) == 117
    d92 = r["by member"]["m003:d9.2"]["room >= 3"]
    assert [(x["order"], x["degree"], x["(n(1), n(rho))"], x["room"]) for x in d92] == [(5, 45, [4, 18], 5)]
    want = {"m003:d10.13": ([3, 3], 3), "m003:d10.14": ([3, 3], 3), "m003:d10.16": ([3, 7], 4),
            "m003:d10.36": ([3, 3], 3), "m003:d10.38": ([3, 3], 3), "m003:d10.40": ([3, 7], 4)}
    for key, (s, room) in want.items():
        rows = r["by member"][key]["room >= 3"]
        assert [(x["order"], x["degree"], x["(n(1), n(rho))"], x["room"]) for x in rows] == [(6, 60, s, room)]
    others = [x for k, x in r["by member"].items() if k not in want and k != "m003:d9.2"]
    assert all(x["room >= 3"] == [] and (x["best room"] or 0) <= 2 for x in others)


def test_the_record():
    r = _record("room_n45.json")
    assert r["Lemma A: (n(1), n(rho)) of N_45"] == [4, 18]
    assert r["Lemma A: room at the trivial character"] == 5
    assert [r["route N at the trivial character"][k] for k in ("n(1)", "n(rho)", "capW", "capL2")] == [4, 18, 5, 18]
    assert [r["route R at the trivial character"][k] for k in ("n(1)", "n(rho)", "capW", "capL2", "h1(rho)")] == [4, 18, 5, 18, 23]
    assert r["N_45: degree, cusps, connected"] == [45, 5, True]
    assert r["N_45: H_1 (free rank, torsion); b1 - cusps"] == [9, [2, 2], 4]
    assert r["Proposition P: the count at the pulled-back class, by the banked rows"] == [0, 0]
    assert r["the pulled-back class read directly (I(W), I(L2W), identities), routes N and R"] == [[0, 0, True], [0, 0, True]]
    assert r["every route agrees"] is True
    assert r["room at the trivial character of N_45: min(capW, capL2)"] == 5


def test_the_degree_60_record():
    r = _record("room_60.json")
    assert sorted(r["covers"]) == SIX
    for key, x in r["covers"].items():
        four = 7 if key in ("m003:d10.16", "m003:d10.40") else 3
        cusps = 4 if four == 7 else 6
        assert [x["degree"], x["cusps"], x["connected"]] == [60, cusps, True]
        assert x["route N (prime, n(1), n(rho), capW, capL2)"] == [16775281, 3, four, 4, four]
        assert x["route R (prime, n(1), n(rho), capW, capL2)"] == [2147482801, 3, four, 4, four]
        assert x["H_1 (free rank, torsion); b1 - cusps"] == [cusps + 3, [4, 12], 3]
        assert x["Lemma A from the banked rows: (n(1), n(rho)), room"] == [[3, four], min(4, four)]
        assert x["every route agrees"] is True
    assert r["rooms"] == {"m003:d10.13": 3, "m003:d10.14": 3, "m003:d10.16": 4, "m003:d10.36": 3, "m003:d10.38": 3,
                          "m003:d10.40": 4}
    assert r["conjugacy classes (covers of m003 up to conjugacy)"] == [["m003:d10.13", "m003:d10.14"], ["m003:d10.16"],
                                                                      ["m003:d10.36", "m003:d10.38"], ["m003:d10.40"]]
    assert r["every route agrees"] is True


def test_the_banked_rows_fix_n45():
    rows = {}
    for route in ("R", "N"):
        for line in gzip.open(B1536V / f"run_{route}_m003.jsonl.gz", "rt"):
            x = json.loads(line)
            if not x.get("done") and x["cover"] == "d9.2":
                rows[(route, tuple(x["u"]), x["kappa"])] = x
    u0 = (Fr(1, 5), Fr(3, 5))
    us = [tuple((j * a) % 1 for a in u0) for j in range(5)]
    key = lambda route, u: (route, (str(u[0]), str(u[1])), "0")  # noqa: E731
    for route in ("R", "N"):
        line = [0] + [rows[key(route, us[j])]["S"]["n(L)"] for j in range(1, 5)]
        four = [rows[key(route, tuple((2 * a) % 1 for a in us[j]))]["S"]["n((VL)*)"] for j in range(5)]
        assert line == [0, 1, 1, 1, 1] and four == [2, 4, 4, 4, 4]
        assert (sum(line), sum(four)) == (4, 18) and min(1 + sum(line), sum(four)) == 5
        counts = [rows[key(route, u)]["P"]["count"] for u in us]
        assert counts == [[0, 0]] * 5


@pytest.mark.slow
def test_the_census_is_reproduced():
    now = json.loads(json.dumps(_module("b1540_pb_repro", "pulled_back_rooms.py").main()))
    assert now == _record("pulled_back_rooms.json")


@pytest.mark.slow
def test_the_degree_60_record_is_reproduced():
    now = json.loads(json.dumps(_module("b1540_r60_repro", "room_60.py").main()))
    assert now == _record("room_60.json")


@pytest.mark.slow
def test_the_record_is_reproduced():
    now = json.loads(json.dumps(_module("b1540_room_repro", "room_n45.py").main()))
    assert now == _record("room_n45.json")
