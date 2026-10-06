"""B1543 -- THE LINE MUST LEAD: the lock (PROVED; a corollary of sm:B1535's Theorem C (ii), checked on the banked record, and a
census of banked data, read again directly).

  - Corollary C' (I(W) >= rk delta1_W - b0 - n(L)) and the two facts C'' rests on (rk delta1_W <= n(V); Theorem C (i)) hold at
    every banked reading that carries the rank: the record, and check_readings() reproducing it from sm:B1541's and sm:B1536's
    banked records;
  - the corollaries' arithmetic on synthetic values: where C' is tight, the maximal-rank criterion, and the trivial character's
    3 <= n(rho) <= n(1) - 2;
  - N_45's cup ranks by subspace (sm:B1541's record): 9 on every cusp stratum, 8 on the twisted eigenspaces, 4 on zeta^0, 0 at
    the pulled-back class, and C' an equality exactly where FINDINGS says;
  - the census as recorded (117 covers, none meeting the criterion) and its direct reading (every cover read without Lemma A, in
    two routes and by integer homology, agreeing with Lemma A's sums); the graded census (585 deck eigenspaces, the graded
    criterion met only at 16 empty ones; the four's h^1 per eigenspace as sm:B1542's K2); slow tests re-run both censuses from
    the banked rows;
  - sm:B1542's record after its read-out: C' at all 1,664 readings, the deck grading at its 216 eigenspace readings; and the
    floor I(W) >= -b0 at all 6,756 banked readings that carry the count (an observation, recorded, not a theorem);
  - the verdict as banked, with its prior_work and load_bearing records valid.
Nothing here writes a tracked file."""
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1543_the_line_must_lead"
V = ARC / "verification"


def _load(alias, path):
    spec = importlib.util.spec_from_file_location(alias, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _check():
    return _load("b1543_corollary_check_lock", V / "corollary_check.py")


def test_the_corollary_holds_on_the_record():
    c = json.loads((V / "corollary_check.json").read_text())["Corollary C' on the banked readings"]
    assert c["columns"] == ["readings", "C' violations", "C' equalities", "rk delta1_W > n(V)", "Theorem C (i) violations"]
    assert c["sm:B1541"] == [380, 0, 189, 0, 0]
    assert c["sm:B1536 Parts P and O"] == [3160, 0, 1576, 0, 0]


def test_the_check_reproduces_from_the_banked_records():
    rec = json.loads((V / "corollary_check.json").read_text())
    C = _check()
    assert C.check_readings() == rec["Corollary C' on the banked readings"]
    assert C.b1541_ranks() == rec["sm:B1541's rk delta1_W by subspace"]


def test_the_arithmetic():
    C = _check()
    # C' at a reading: the lower bound, tight or not; a violation is counted
    x = {"rk d1": {"E": 9}, "b0": 1, "n(L)": 4, "n(V)": 18, "n((VL)*)": 18, "count": [4, -10]}
    assert C.lower_bound(x) == 4
    assert C._tally([x]) == [1, 0, 1, 0, 0]
    y = dict(x, count=[3, -10])
    assert C._tally([y]) == [1, 1, 0, 0, 0]
    z = dict(x, count=[4, 1])
    assert C._tally([z])[4] == 1
    w = dict(x, **{"rk d1": {"E": 19}}, count=[14, -10])
    assert C._tally([w])[3] == 1

    def three_at_maximal_rank(h1L, nV, b0, nL, nV3):
        """the least I(W) at a class of maximal rank (C') is <= -3, and Theorem C (i) allows -3"""
        return min(h1L, nV) - b0 - nL <= -3 and nV3 >= 3
    # the trivial character: three needs 3 <= n(rho) <= n(1) - 2 (h^1(L) = n(1) + #cusps)
    for n1 in range(0, 8):
        for nr in range(0, 12):
            for cusps in (1, 2, 5):
                assert three_at_maximal_rank(n1 + cusps, nr, 1, n1, nr) == (3 <= nr <= n1 - 2), (n1, nr, cusps)
    # an injective cup map (h^1(L) <= n(V)) never allows three: I(W) >= p(L) - b0 >= -1
    assert not three_at_maximal_rank(9, 18, 1, 4, 18)
    # the degree-60 covers' prediction: (n(1), n(rho)) = (3, 3) gives I(W) >= -1 at maximal rank, (3, 7) gives I(W) >= 3
    assert min(3 + 6, 3) - 1 - 3 == -1 and min(3 + 4, 7) - 1 - 3 == 3


def test_n45_cup_ranks():
    r = json.loads((V / "corollary_check.json").read_text())["sm:B1541's rk delta1_W by subspace"]
    for k, v in r.items():
        assert len(v) == 1, k
        rk, cnt = v[0]
        if k.startswith("A cusp strata"):
            free = int(k.split()[4])
            assert rk == 9 and cnt == ([4, -10] if free <= 2 else [5, -7] if free == 3 else [5, -6] if free == 4 else [5, -5])
            assert (cnt[0] == rk - 1 - 4) == (free <= 2)
        elif k == "C pulled back":
            assert rk == 0 and cnt == [0, 0]
        else:
            j = int(k.split()[1][2:])
            assert rk == (4 if j == 0 else 8)
            assert cnt[0] == (rk - 1 - 4 if k.endswith("interior") else (0 if j == 0 else 5)), k
    assert len(r) == 6 + 10 + 1


def test_the_census_as_recorded():
    c = json.loads((V / "corollary_check.json").read_text())["the census of cyclic covers"]
    dist = {tuple(k): v for k, v in c["(n(1), n(rho)) distribution"]}
    assert c["cyclic covers"] == sum(dist.values()) == 117
    assert dist == {(0, 2): 2, (1, 1): 16, (1, 2): 28, (1, 3): 6, (1, 5): 14, (1, 6): 8, (1, 10): 24, (1, 11): 6, (3, 1): 4,
                    (3, 2): 2, (3, 3): 4, (3, 7): 2, (4, 18): 1}
    assert c["meeting 3 <= n(rho) <= n(1) - 2"] == [] and not any(3 <= r <= n - 2 for n, r in dist)
    assert c["largest n(1) - n(rho)"] == 2 and c["largest n(1)"] == 4


def test_the_census_read_directly():
    d = json.loads((V / "census_direct.json").read_text())
    assert d["covers"] == len(d["rows"]) == 117 and d["all agree"] is True
    assert d["meeting 3 <= n(rho) <= n(1) - 2 (route N and route R)"] == []
    rec = {tuple(k): v for k, v in json.loads((V / "corollary_check.json").read_text())
           ["the census of cyclic covers"]["(n(1), n(rho)) distribution"]}
    seen = {}
    for x in d["rows"]:
        assert x["agrees"] is True
        assert x["route N"][1:3] == x["route R"][1:3] == x["Lemma A (n(1), n(rho))"], x
        assert x["route N"][0] != x["route R"][0]
        assert x["H_1; b1 - cusps"][2] == x["route N"][1] and x["H_1; b1 - cusps"][0] - x["cusps"] == x["route N"][1]
        seen[tuple(x["route N"][1:3])] = seen.get(tuple(x["route N"][1:3]), 0) + 1
    assert seen == rec


def test_the_graded_census():
    g = json.loads((V / "graded_census.json").read_text())
    assert g["covers"] == len(g["rows"]) == 117 and g["eigenspaces"] == sum(x["order"] for x in g["rows"]) == 585
    meet = {(s, c, k): tuple(j) for s, c, k, j in g["meeting the graded criterion"]}
    assert meet == {("m003", c, 6): (1, 2, 4, 5) for c in ("d10.13", "d10.14", "d10.36", "d10.38")}
    assert g["meeting it and non-empty"] == []
    k2 = json.loads((ROOT / "frontier" / "B1542_the_count_at_the_eisenstein_order" / "verification" / "controls.json")
                    .read_text())["K2"]
    seen = set()
    for x in g["rows"]:
        k = x["order"]
        (nL, h1L), (n4, h4), B = x["line: n, h^1 by power"], x["four: n, h^1 by power"], x["graded bounds B_j"]
        assert [sum(nL), sum(n4)] == x["(n(1), n(rho))"]
        assert all(B[j] == sum(min(h1L[m], n4[(j + m) % k]) for m in range(k)) for j in range(k))
        n1, nr = x["(n(1), n(rho))"]
        meets = x["eigenspaces meeting the graded criterion"]
        assert all((nr >= 3 and B[j] <= n1 - 2) == (j in meets) for j in range(k))
        assert all(h4[j] == 0 for j in x["eigenspaces meeting the graded criterion"])
        if x["state"] == "m003" and x["cover"] in k2 and k == 6:
            assert h4 == k2[x["cover"]]["eigenspaces (route N; route R, p_R)"][0]
            assert [B[j] for j in range(6) if h4[j]] == ([3, 3] if x["cover"] in ("d10.13", "d10.36") else [3, 3, 4, 3])
            seen.add(x["cover"])
    assert seen == {"d10.13", "d10.16", "d10.36", "d10.40"}
    n45 = [x for x in g["rows"] if (x["state"], x["cover"], x["order"]) == ("m003", "d9.2", 5)]
    assert len(n45) == 1
    k2_n45 = json.loads((ROOT / "frontier" / "B1541_the_count_on_the_room" / "verification" / "controls.json")
                        .read_text())["K2"]["eigenspaces (route N)"]
    assert n45[0]["four: n, h^1 by power"][1] == k2_n45 == [3, 5, 5, 5, 5]
    assert n45[0]["graded bounds B_j"] == [9] * 5          # N_45's eigenspaces reach 4 and 8: below the graded bound


def test_b1542_and_the_floor():
    b = json.loads((V / "b1542_check.json").read_text())
    assert b["sm:B1542"] == [1664, 0, 0, 0, 0]
    assert b["eigenspace readings"] == 216
    assert b["rk delta1_W > B_j (graded bound)"] == [] and b["rk delta1_W > the global bound"] == []
    f = json.loads((V / "floor.json").read_text())
    assert f["readings"] == 6756 and f["below the floor"] == 0
    rows = f["by record"]
    assert {k: (v["readings"], v["I(W) = -b0"], v["with n(nu^4) >= 1"]) for k, v in rows.items()} == {
        "sm:B1535 Part M": (1552, 288, 0), "sm:B1536 Parts P and O": (3160, 1728, 784), "sm:B1541": (380, 9, 380),
        "sm:B1542": (1664, 666, 1664)}
    assert all(v["lowest I(W) + b0"] == 0 for v in rows.values())
    C = _check()
    assert C.check_b1542() == json.loads(json.dumps(b))
    assert C.floor_tally() == f


@pytest.mark.slow
def test_the_census_reproduces_from_the_banked_rows():
    rec = json.loads((V / "corollary_check.json").read_text())["the census of cyclic covers"]
    assert _check().census() == rec


@pytest.mark.slow
def test_the_graded_census_reproduces_from_the_banked_rows():
    rec = json.loads((V / "graded_census.json").read_text())
    assert json.loads(json.dumps(_check().graded_census(say=lambda *a: None), default=str)) == rec


def test_the_verdict_as_banked():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["id"] == "B1543" and v["verdict"] == "PROVED" and v["prior_work"]["standing"] == "EXTENDS"
    lb = _load("b1543_load_bearing_lock", ROOT / "scripts" / "checks" / "load_bearing.py")
    assert lb.validate(v["load_bearing"], v["scope"]) == []
    pw = _load("b1543_prior_work_lock", ROOT / "scripts" / "checks" / "prior_work.py")
    assert pw.validate(v["prior_work"]) == []
    assert {e["status"] for e in v["load_bearing"]} == {"VERIFIED"}
    text = (ARC / "FINDINGS.md").read_text()
    assert "## Seen first" in text and "Theorem 0.4" in text and "Theorem 0.1" in text
    assert "docs/dossiers/the_line_must_lead_2026-10-06/PREDICTION_FOR_B1542_BEFORE_ITS_READ_OUT.md" in text
    dossier = ROOT / "docs" / "dossiers" / "the_line_must_lead_2026-10-06"
    assert (dossier / "PREDICTION_FOR_B1542_BEFORE_ITS_READ_OUT.md").exists()
