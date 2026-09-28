"""B1397 lock -- THE CAP'S GENERATIONS.

A flux cap's chirality is linear in the charges, <F, mu> n per weight (Riemann-Roch on the capped torus, SL(2)_beta doublets
included).  Anomaly-free exactly when F is orthogonal to hypercharge (no independent quartic Casimir in E6, E7, E8).  Net generations
with F orthogonal to Y: E6 frames even (F78 2dn, F27 -2dn/3, F27+78 4dn/3), the E7 frame every integer ((4d/3 + e) n, n chiral 27s
along t), the E8 frame zero.  The banked identity and the hand cases are re-run; the recorded scan is re-read."""
import importlib.util
import json
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1397_the_caps_generations" / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1397_cap_generations", VER / "cap_generations.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_banked_identity_and_the_hand_cases():
    C = _load()
    assert C.banked_identity() == []
    cases = {("F78", (0, 1)): (1, 2), ("F27", (0, 1)): (3, -2), ("F27+78", (0, 1)): (3, 4), ("F133", (0, 0, 1)): (1, 1),
             ("F133", (0, 1, Fr(2, 3))): (1, 2), ("F248", (0, 1, (Fr(1), Fr(-1), Fr(0)))): (3, 0)}
    for (frame, F), (n_min, g) in cases.items():
        assert C.minimal_n(frame, F) == n_min, (frame, F)
        r = C.analyse(frame, F, n_min)
        assert r["anomaly_free"] and not r["xy_chiral"] and not r["exotic"] and r["g"] == g, (frame, F, r)
        assert r["g"] == C.g_formula(frame, F, n_min)
    for frame, F in (("F78", (1, 0)), ("F27+78", (1, 1)), ("F133", (Fr(-1, 2), 0, 1))):
        r = C.analyse(frame, F, C.minimal_n(frame, F))
        assert not r["anomaly_free"] and r["xy_chiral"], (frame, F)       # a hypercharge component: anomalous, X,Y chiral


def test_the_recorded_scan():
    d = json.load(open(VER / "cap_generations.json"))
    assert d["fails"] == [] and len(d["rows"]) == 1875
    ach = {f: [int(Fr(x)) for x in v] for f, v in d["achieved"].items()}
    assert all(g % 2 == 0 for f in ("F27", "F78") for g in ach[f])                # E6 frames: even
    assert all(g % 4 == 0 for g in ach["F27+78"])
    assert ach["F248"] == [0]                                                    # E8: vector-like
    assert set(range(-18, 19)) <= set(ach["F133"])                               # E7: every integer, three included
    assert all(r["anomaly_free"] == (r["F"][0] == "0") for r in d["rows"] if r["integral"])
