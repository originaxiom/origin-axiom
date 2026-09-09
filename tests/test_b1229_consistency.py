"""B1229 -- the consistency turn. Locks the FACTS (the Deligne/MMS menu and the cut),
and the FENCES (the end-state must not be claimed as achieved)."""
import json, pathlib
from fractions import Fraction as F
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1229_the_consistency_turn"

DELIGNE = {"A1":(3,2,2),"A2":(8,3,3),"G2":(14,4,2),"D4":(28,6,4),
           "F4":(52,9,2),"E6":(78,12,3),"E7":(133,18,2)}   # dim, h^v, #primaries

def test_the_menu_is_finite_and_sigma_is_rational():
    sig = {g: F(d,1+h)/6 for g,(d,h,n) in DELIGNE.items()}
    assert len(sig) == 7
    for s in sig.values():
        assert s.denominator >= 1                      # rational by construction
    assert sig["E6"] == 1 and sig["A2"] == F(1,3)

def test_the_Z3_cut_leaves_exactly_two():
    keep = [g for g,(d,h,n) in DELIGNE.items() if n == 3]
    assert sorted(keep) == ["A2","E6"], keep
    sig = sorted(F(DELIGNE[g][0], 1+DELIGNE[g][1])/6 for g in keep)
    assert sig == [F(1,3), F(1)]                       # sigma is ONE BIT

def test_the_cut_is_not_vacuous():
    """If every Deligne member had 3 primaries the cut would say nothing."""
    n3 = sum(1 for _,(d,h,n) in DELIGNE.items() if n == 3)
    assert 0 < n3 < len(DELIGNE), n3

def test_end_state_is_not_claimed_achieved():
    """The two candidates are NOT results. If a later seat upgrades them, red the suite."""
    e = json.load(open(ARC/"endstate.json"))
    assert e["candidate"] == 2
    assert e["b1225_untouched"] is True
    grades = {r["grade"] for r in e["rows"]}
    assert "CANDIDATE" in grades
    v = json.load(open(ARC/"arc_verdict.json"))
    assert v["verdict"] == "OPEN"
    assert "NOT CLAIMED NOW" in v["claim_one_line"]
