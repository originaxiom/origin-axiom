"""B1610 -- THE HANDS ON THE FOUNDING TORSOR: the sealed instrument unchanged; hand (ii) on the torsor as recorded; hand (i)
on no rule; the spectral detector vacuous; GENESIS and the kill graph carry it."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1610_the_hands_on_the_founding_torsor"
V = ARC / "verification"


def test_the_sealed_instrument_is_unchanged():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at f916539c6: ")
    assert hashlib.sha256(open(V / "hands_on_the_torsor.py", "rb").read()).hexdigest() == first.split()[4]


def test_hand_ii_is_the_c_bit_given_the_arrow():
    d = json.load(open(V / "hands_on_the_torsor.json"))
    assert d["H0"]["size"] == 4 and d["H0"]["closed"] and d["H0"]["all_positive"]
    r = d["reads"]
    assert [r[n]["sense"] for n in ("sigma", "C", "rev", "C_rev", "inverse")] == ["backward", "forward", "backward", "forward", "forward"]
    assert [r[n]["double_tick_sense"] for n in ("sigma", "C", "rev", "C_rev", "inverse")] == ["forward", "backward", "forward", "backward", "backward"]
    h = d["H3"]
    assert h["C"]["hand_ii_sense_of_double_tick"] == "flips" and h["reversal"]["hand_ii_sense_of_double_tick"] == "keeps" and h["arrow"]["hand_ii_sense_of_double_tick"] == "flips"


def test_hand_i_is_on_no_rule_and_the_spectral_detector_is_vacuous():
    r = json.load(open(V / "hands_on_the_torsor.json"))["reads"]
    assert all(r[n]["form_on_V"] == "reverses" and r[n]["double_tick_form_on_V"] == "keeps" and r[n]["double_tick_keeps_T"] for n in r)
    # every double tick's turns on T are the regular Z/3 set {0, 1/3, 2/3} (1.0 and 0.0 are one angle): no hand can live there
    for n in r:
        assert sorted(round(t % 1, 4) for t in r[n]["double_tick_turns_on_T"]) == [0.0, 0.3333, 0.6667]


def test_genesis_and_the_kill_graph_carry_it():
    g = open(ROOT / "GENESIS.md", encoding="utf-8").read()
    assert int(g.split("**Version 1.")[1].split()[0]) >= 31 and "THE HANDS ON THE FOUNDING TORSOR (main, B1610" in g
    k = json.load(open(ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json"))
    e = [x for x in k if isinstance(x, dict) and x.get("id") == "B1610"]
    assert e and e[-1]["scope"]["reach"] == "general"
