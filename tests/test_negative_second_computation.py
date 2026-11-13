"""Card C19 (2026-11-13, main's M29): the gate `negative-second-computation` holds WORKING_RULES' rule of 2026-11-13 (the
author's instruction after B1918; register row P-842). From B1923 on, a NEGATIVE verdict names a second computation made
in `cites_seat`, or its verdict line says PROVISIONAL; and its arc's page has a section "What the wall teaches".

Each planted case below stands with its twin: the same verdict file with the one thing the rule asks put right passes."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts", "gates"))
import gates

WALL = "# B99923\n\n## What the wall teaches\n\nThe wall rests on one assumption.\n"


def _plant(monkeypatch, arcs):
    """arcs: {folder: (verdict file as a dict, FINDINGS text or None)}; the gate reads only these"""
    mapping = {}
    for folder, (d, page) in arcs.items():
        mapping["frontier/%s/arc_verdict.json" % folder] = json.dumps(d)
        if page is not None:
            mapping["frontier/%s/FINDINGS.md" % folder] = page
    monkeypatch.setattr(gates.glob, "glob", lambda pat: [os.path.join(gates.ROOT, k) for k in mapping if k.endswith(".json")])

    def reader(rel):
        return mapping[rel.replace(os.sep, "/")]                 # a page not planted raises, as a missing file does
    return reader


def _negative(n, cites=(), line="the route closes within these forms"):
    return {"id": "B%d" % n, "verdict": "NEGATIVE", "cites_seat": list(cites), "claim_one_line": line}


def test_a_negative_with_no_second_computation_and_no_provisional_fails_and_its_twin_passes(monkeypatch):
    """the card's control: a NEGATIVE from B1923 on, no second computation named, the line not PROVISIONAL"""
    rd = _plant(monkeypatch, {"B99923_x": (_negative(99923), WALL)})
    ok, msg = gates.gate_negative_second_computation(reader=rd)
    assert not ok and "B99923" in msg and "PROVISIONAL" in msg
    rd = _plant(monkeypatch, {"B99923_x": (_negative(99923, line="PROVISIONAL: the route closes within these forms"), WALL)})
    assert gates.gate_negative_second_computation(reader=rd)[0]
    rd = _plant(monkeypatch, {"B99923_x": (_negative(99923, cites=["agy-002's second computation on its own code"]), WALL)})
    assert gates.gate_negative_second_computation(reader=rd)[0]


def test_a_second_computation_named_only_as_owed_does_not_count(monkeypatch):
    for words in ("a second computation is assigned to agy-002", "second computation owed", "the second computation: pending",
                  "a second computation is not yet made"):
        rd = _plant(monkeypatch, {"B99924_y": (_negative(99924, cites=[words]), WALL)})
        ok, msg = gates.gate_negative_second_computation(reader=rd)
        assert not ok and "B99924" in msg, words
    rd = _plant(monkeypatch, {"B99924_y": (_negative(99924, cites=["the web seat's sealed scan: a second computation of B99924"]), WALL)})
    assert gates.gate_negative_second_computation(reader=rd)[0]


def test_a_negative_whose_page_does_not_say_what_the_wall_teaches_fails(monkeypatch):
    line = "PROVISIONAL: the route closes within these forms"
    for page in ("# B99925\n\nThe route closes.\n", "# B99925\n\nwhat the wall teaches, said in passing and not as a section\n", None):
        rd = _plant(monkeypatch, {"B99925_z": (_negative(99925, line=line), page)})
        ok, msg = gates.gate_negative_second_computation(reader=rd)
        assert not ok and "What the wall teaches" in msg, page
    for page in (WALL, "# B99925\n\n### 7. What the wall teaches: the assumption it rests on\n"):
        rd = _plant(monkeypatch, {"B99925_z": (_negative(99925, line=line), page)})
        assert gates.gate_negative_second_computation(reader=rd)[0], page


def test_the_rule_binds_from_b1923_and_reads_negatives_only(monkeypatch):
    rd = _plant(monkeypatch, {"B1922_before": (_negative(1922), None),
                              "B1923_on": ({"id": "B1923", "verdict": "PROVED", "cites_seat": [], "claim_one_line": "x"}, None),
                              "B1924_open": ({"id": "B1924", "verdict": "OPEN", "cites_seat": [], "claim_one_line": "x"}, None)})
    assert gates.negative_without_second(reader=rd) == []
    rd = _plant(monkeypatch, {"B1923_on": (_negative(1923), None)})
    assert [a for a, _ in gates.negative_without_second(reader=rd)] == ["B1923", "B1923"]


def test_the_gate_is_registered_with_this_control_and_passes_on_the_record():
    assert gates.GATES["negative-second-computation"] is gates.gate_negative_second_computation
    reg = json.load(open(os.path.join(ROOT, "tests", "GATE_CONTROLS.json"), encoding="utf-8"))
    assert reg["negative-second-computation"].endswith(
        "::test_a_negative_with_no_second_computation_and_no_provisional_fails_and_its_twin_passes")
    ok, msg = gates.gate_negative_second_computation()
    assert ok, msg
