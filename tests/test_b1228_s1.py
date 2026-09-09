"""B1228 -- S1. The locks assert FACTS, and one of them guards the RETRACTION:
if a later seat upgrades this arc to "sigma = 1 established", the suite goes red."""
import itertools, json, pathlib
from fractions import Fraction as F
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1228_S1_the_nomination"

SL = {"A1":(3,2,1),"A2":(8,3,2),"D4":(28,6,4),"E6":(78,12,6),"E7":(133,18,7),"E8":(248,30,8)}

def test_simply_laced_level1_c_equals_rank():
    for J,(d,h,r) in SL.items():
        assert F(d, 1+h) == r, (J, F(d,1+h), r)

def test_sigma_is_one_for_E6_alone():
    ones = [J for J,(d,h,r) in SL.items() if F(d,1+h)/6 == 1]
    assert ones == ["E6"], ones
    # and the near-miss that makes the test non-vacuous
    assert F(SL["A2"][0], 1+SL["A2"][1])/6 == F(1,3)

def test_the_nomination_holds_and_the_control_bites():
    snappy = pytest.importorskip("snappy")
    G = [(a,b,c,d) for a,b,c,d in itertools.product(range(3),repeat=4) if (a*d-b*c)%3==1]
    assert len(G) == 24
    mul = lambda X,Y: ((X[0]*Y[0]+X[1]*Y[2])%3,(X[0]*Y[1]+X[1]*Y[3])%3,
                       (X[2]*Y[0]+X[3]*Y[2])%3,(X[2]*Y[1]+X[3]*Y[3])%3)
    inv = lambda X: (X[3]%3,(-X[1])%3,(-X[2])%3,X[0]%3)
    I = (1,0,0,1)
    def surj_count(name):
        P = snappy.Manifold(name).fundamental_group()
        g, rels = P.generators(), P.relators()
        if len(g) != 2: return None
        n = 0
        for A,B in itertools.product(G, repeat=2):
            asg = {g[0]:A, g[1]:B}
            ok = True
            for r in rels:
                v = I
                for ch in r:
                    m = asg[ch.lower()]
                    v = mul(v, m if ch.islower() else inv(m))
                if v != I: ok = False; break
            if not ok: continue
            S, fr = {I}, [I]
            while fr:
                x = fr.pop()
                for gg in (A,B):
                    for y in (mul(x,gg), mul(x,inv(gg))):
                        if y not in S: S.add(y); fr.append(y)
            if len(S) == 24: n += 1
        return n
    assert surj_count("m004") == 48
    assert surj_count("5_2") == 0, "control must bite -- not every knot nominates 2T"

def test_the_level_is_forced_by_inventory():
    c = lambda k: F(k*78, k+12)
    assert c(1) == 6 and c(1)/6 == 1
    for k in (2,3):
        assert c(k)/6 != 1, k          # blindness to k is load-bearing, not decorative

def test_the_retraction_stands():
    """sigma = 1 is NOT established. If this arc is ever upgraded to claim it, red the suite."""
    v = json.loads((ARC/"arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "OPEN", v["verdict"]
    claim = v["claim_one_line"]
    assert "RETRACT" in claim.upper()
    assert "NOT sigma = 1" in claim or "sigma is NOT deleted" in claim
    txt = (ARC/"FINDINGS.md").read_text(encoding="utf-8")
    assert "The retraction" in txt and "It does not" in txt
