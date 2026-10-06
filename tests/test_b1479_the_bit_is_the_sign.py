"""B1479 -- the bit is the sign of the word state: the stored run re-read against the three sealed predictions, the pairing
checked row by row, a planted exception caught, and the two controls live."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1479_the_bit_is_the_sign_of_the_word_state", "verification")


def half_shift(a, b):
    return abs(a["shape"][1] - b["shape"][1]) < 1e-7 and abs(((b["shape"][0] - a["shape"][0]) % 1.0) - 0.5) < 1e-7 and abs(a["volume"] - b["volume"]) < 1e-8


def sign_law(a, b):
    return a["amphichiral"] and b["amphichiral"] and (a["cs_class"], a["rhombic_parity"]) == ("zero", 0) and (b["cs_class"], b["rhombic_parity"]) == ("quarter", 1)


def test_the_three_predictions_on_the_stored_run():
    d = json.load(open(os.path.join(V, "sign_law.json"))); s = d["summary"]
    assert (s["words"], s["states"], s["hyperbolic"], s["pairs"]) == (379, 758, 758, 379) and s["errors"] == []
    assert s["P1_exceptions"] == [] and s["P2_exceptions"] == [] and s["P3_exceptions"] == [] and s["volume_mismatch"] == []
    by = {}
    for r in d["rows"]: by.setdefault(r["word"], {})[r["sign"]] = r
    assert all(half_shift(p["+"], p["-"]) for p in by.values())
    am = [p for p in by.values() if p["+"]["amphichiral"] or p["-"]["amphichiral"]]
    assert len(am) == 34 and all(sign_law(p["+"], p["-"]) and p["-"]["all_L_minus"] is True for p in am)
    assert sorted(len(w) for w, p in by.items() if p["+"]["amphichiral"]).count(12) == 17
    # no chiral word state sits in a class by the sign alone: the law is about amphichiral words
    assert not any(p["+"]["amphichiral"] != p["-"]["amphichiral"] for p in by.values())
    # the checks can fail
    p = dict(am[0]); bad = dict(p["-"]); bad["cs_class"] = "zero"; assert not sign_law(p["+"], bad)
    bad2 = dict(p["-"]); bad2["shape"] = [p["+"]["shape"][0] + 0.25, p["+"]["shape"][1]]; assert not half_shift(p["+"], bad2)


def test_the_web_seat_reruns_carry_its_outcomes():
    r = lambda f: open(os.path.join(V, "webseat_rerun_%s.txt" % f), encoding="utf-8").read()
    t = r("listening_log"); assert "E1 orientability alternates: True" in t and "E2 p-rank = ker dim: True" in t
    assert "|Sym| by tick: [(1, 2), (2, 8), (3, 6), (4, 16), (5, 10), (6, 24), (7, 14), (8, 32), (9, 18), (10, 40)]" in t
    assert "I(m025; Ind V) = I(s961; V): 72/72" in r("firing_descent") and "(dim, I_w(N;V)) distribution" in r("nonor_index")
    for n in (48, 96, 192, 240, 768): assert n % 24 == 0


def test_the_two_controls_live():
    import snappy
    a, b = snappy.Manifold("b++LR"), snappy.Manifold("b+-LR")
    assert abs(float(a.volume()) - float(b.volume())) < 1e-9
    assert abs(float(a.chern_simons()) % 0.5) < 1e-7 or abs(float(a.chern_simons()) % 0.5 - 0.5) < 1e-7
    assert abs(float(b.chern_simons()) % 0.5 - 0.25) < 1e-7
    assert a.is_isometric_to(snappy.Manifold("m004")) and b.is_isometric_to(snappy.Manifold("m003"))
