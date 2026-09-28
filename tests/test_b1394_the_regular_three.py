"""B1394 lock -- THE REGULAR THREE (sealed at a4712e8d; run after the seal, verdict P1 holds, P3 SOME).

Sources on the k = 3m fixed arcs of an order-3 rotation, with a g-invariant rank-one flat line and an acyclic twisted cohomology, give
balanced arc weights: m copies of the regular representation (the lane's R32 Hopf-trace argument, generalised).  The banked identity
is m202 (R32): one rotation subgroup, k = 3; the trivial character h = (1, 2, 1) with weights (3, 0, 0); the two non-trivial invariant
characters acyclic and balanced.  The recorded census (census.json) is checked for the instrument's integrity, recounted row by row,
and held to its sealed outcome: P1 on all 96 acyclic pairs, P3 SOME (54 non-acyclic non-trivial pairs unbalanced, on five members)."""
import importlib.util
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1394_the_regular_three" / "verification"
P3_RECORDED = 54


def _load():
    spec = importlib.util.spec_from_file_location("b1394_regular_three", VER / "regular_three.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_banked_identity_m202():
    R = _load()
    rows = R.analyse(R.member_from("m202", "m202"))
    assert {r["k"] for r in rows} == {3} and len(rows) == 3
    triv = [r for r in rows if r["trivial"]]
    assert len(triv) == 1 and triv[0]["h"] == (1, 2, 1) and triv[0]["counts"] == (3, 0, 0)
    nontriv = [r for r in rows if not r["trivial"]]
    assert len(nontriv) == 2 and all(r["acyclic"] and r["counts"] == (1, 1, 1) for r in nontriv)


def test_the_recorded_census():
    d = json.load(open(VER / "census.json"))
    s, rows = d["summary"], d["rows"]
    assert s["members"] == 100 and s["members_with_rotations"] == 9 and s["pairs"] == len(rows) == 213
    assert s["arc_crosscheck_failures"] == [] and s["anomalies"] == 0
    # recounted from the rows, not read from the summary
    nontriv = [r for r in rows if not r["trivial"]]
    assert len(nontriv) == s["nontrivial"] == 192
    assert all(sum(r["counts"]) == r["k"] and r["k"] % 3 == 0 for r in rows)
    assert all(r["balanced"] == (r["counts"][0] == r["counts"][1] == r["counts"][2]) for r in rows)
    acyc = [r for r in nontriv if r["acyclic"]]
    assert len(acyc) == s["acyclic_nontrivial"] == 96                  # P2: one half
    assert all(r["balanced"] for r in rows if r["acyclic"]) and s["P1_failures"] == 0      # P1, the theorem
    assert not any(r["acyclic"] for r in rows if r["trivial"])         # the trivial character is never acyclic (h0 = 1)
    p3 = [r for r in nontriv if not r["acyclic"] and not r["balanced"]]
    assert len(p3) == s["P3_unbalanced_nonacyclic"] == P3_RECORDED     # the sealed kill test: SOME
    assert Counter(r["member"] for r in p3) == {"s959": 2, "o10_150704": 4, "o10_150725": 2, "o10_150729": 20, "cube~3.24": 26}
    assert all(max(r["counts"]) == 3 for r in p3 if r["k"] == 3)       # k = 3: all three arcs carry one weight
    assert all(sorted(r["counts"]) == [1, 1, 4] for r in p3 if r["k"] == 6)
