"""B1396 lock -- THE CAPPED EISENSTEIN CUSP.

(A) At a cusp rotated by an order-3 isometry, the lift's three fixed-point weights are balanced when the invariant character is
non-trivial on the cusp torus and all equal when it is trivial; (B) h^1 >= the number of cusps where the character is trivial, so an
acyclic character sees every cusp; (C) a flux cap with the arc weights has n = 0 mod 3 and content (n/3) Reg exactly when the weights
are balanced; (E) 2 counts(arcs) = sum of the rotated cusps' counts, so B1394's 54 unbalanced pairs are the characters trivial on a
rotated cusp.  The banked identity (the arithmetic of (C) exact in Q(omega), and m202) is re-run; the recorded census is recounted."""
import importlib.util
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1396_the_capped_eisenstein_cusp" / "verification"
B1394 = ROOT / "frontier" / "B1394_the_regular_three" / "verification" / "census.json"


def _load():
    spec = importlib.util.spec_from_file_location("b1396_capped_cusp", VER / "capped_cusp.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_banked_identity():
    C = _load()
    bad, ar, rows = C.identity()
    assert bad == []
    assert ar[(0, 1, 2)][0] == [-3, 0, 3, 6] and ar[(0, 1, 2)][1][3] == [1, 1, 1]      # balanced: three times one at n = 3
    assert ar[(0, 0, 0)][0] == [-3, 0, 3, 6] and ar[(0, 0, 0)][1][3] == [2, 0, 1]      # all equal: a non-regular three at n = 3
    assert ar[(0, 0, 1)][0] == [-2, 1, 4]                                               # n = sum of the exponents mod 3
    assert len(rows) == 6 and all(r["balanced"] != r["chi_trivial_on_cusp"] for r in rows)


def test_the_cusp_link_on_m202():
    C = _load()
    M = C.R3.member_from("m202", "m202")
    reps, d = M.invariant_characters(M.G1T([a for a in M.FM.auts if M.FM.aut_sign(a) == {0}
                                              and M.order(M.aut_tuple(a)) == 3][0]))
    assert d == 1 and len(reps) == 3
    assert [C.cusp_trivial(M, z, c) for z in reps for c in range(2)] == [True, True, False, False, False, False]


def test_the_recorded_census():
    d = json.load(open(VER / "capped_census.json"))
    s, pairs, rows = d["summary"], d["pairs"], d["rows"]
    assert d["failures"] == [] and s["failures"] == 0
    assert s["members"] == 100 and len(pairs) == 213 and len(rows) == 444
    # (A): every rotated cusp is balanced or all equal, balanced exactly when chi is non-trivial there
    assert all(r["balanced"] != r["all_equal"] for r in rows)
    assert all(r["balanced"] == (not r["chi_trivial_on_cusp"]) for r in rows)
    assert all(len(r["weights"]) == 3 for r in rows) and not any(r["self_arcs"] for r in rows)
    # (B): h1 >= t, and an acyclic character sees every cusp
    assert all(p["h"][1] >= len(p["trivial_cusps_all"]) for p in pairs)
    assert sum(1 for p in pairs if p["h"][1] == len(p["trivial_cusps_all"])) == 144
    assert all(not p["trivial_cusps_all"] for p in pairs if p["acyclic"])
    # (E): twice the arc counts is the sum of the cusp counts
    tot = {}
    for r in rows:
        key = (r["member"], r["sub"], r["chi"])
        tot[key] = [a + b for a, b in zip(tot.get(key, [0, 0, 0]), r["counts"])]
    assert all([2 * x for x in p["arc_counts"]] == tot[(p["member"], p["sub"], p["chi"])] for p in pairs)
    # B1394's P3 set is the set of non-trivial characters trivial on a rotated cusp
    b = json.load(open(B1394))
    p3 = Counter((r["member"], tuple(r["h"]), tuple(r["counts"])) for r in b["rows"]
                 if not r["trivial"] and not r["acyclic"] and not r["balanced"])
    here = Counter((p["member"], tuple(p["h"]), tuple(p["arc_counts"])) for p in pairs
                   if not p["trivial_chi"] and p["trivial_rotated"])
    assert p3 == here and sum(here.values()) == 54
    assert all(len(set(p["arc_counts"])) > 1 for p in pairs if not p["trivial_chi"] and p["trivial_rotated"])
    assert all(p["trivial_rotated"] for p in pairs if not p["trivial_chi"] and len(set(p["arc_counts"])) > 1)
