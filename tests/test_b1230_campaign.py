"""B1230 -- the consistency campaign, run 1. Locks the facts AND the self-refutation:
if a later seat restores "c=6 => E6 uniquely" without the Z/3, the suite reds."""
import json, pathlib
from fractions import Fraction as F
from math import comb
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1230_consistency_campaign_run1"
G = {"A1":(3,2),"A2":(8,3),"A3":(15,4),"A4":(24,5),"A5":(35,6),"A6":(48,7),"A7":(63,8),
     "D4":(28,6),"D5":(45,8),"D6":(66,10),"D7":(91,12),"E6":(78,12),"E7":(133,18),"E8":(248,30)}
CENTRE = {"A1":2,"A2":3,"A3":4,"A4":5,"A5":6,"A6":7,"A7":8,
          "D4":4,"D5":4,"D6":4,"D7":4,"E6":3,"E7":2,"E8":1}

def _c6():
    return [(g,k) for g,(d,h) in G.items() for k in range(1,13) if F(k*d,k+h) == 6]

def test_c6_is_NOT_unique_without_the_Z3():
    """The self-refutation. If this ever returns 1, someone has quietly narrowed the scan."""
    s = _c6()
    assert len(s) == 4, s
    assert set(s) == {("A2",9),("A6",1),("D6",1),("E6",1)}, s

def test_the_Z3_cuts_four_to_one():
    def nprim(g,k):
        if k == 1: return CENTRE[g]
        n = int(g[1:]); return comb(n+k, n)
    keep = [(g,k) for g,k in _c6() if nprim(g,k) == 3]
    assert keep == [("E6",1)], keep

def test_level_one_c_equals_rank_is_why():
    RANK = {"A6":6,"D6":6,"E6":6}
    for g,r in RANK.items():
        d,h = G[g]; assert F(d,1+h) == r == 6

def test_c1_audit_kept_its_bite_and_failed_clean():
    r = json.load(open(ARC/"c1_results.json"))
    assert r["clean"] is False
    assert r["over_counted"] and r["suspect"]
    assert "field" in r["rule"]

def test_campaign_claims_no_deletion():
    v = json.load(open(ARC/"arc_verdict.json"))
    assert v["verdict"] == "OPEN"
    assert "no row deleted" in v["claim_one_line"].lower()
