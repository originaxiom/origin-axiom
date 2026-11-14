"""The gate `selection-family` (main's card C13, item 5; WORKING_RULES, the rule of 2026-11-12, step 3): a verdict line from
B1905 on that claims a selection, with a value or a member as its object, has a page that names the family of its criterion.

The reading of a claim is the building session's and main's to change.  Held here: the claims it reads and the sentences it
does not; what it still passes and what it still refuses though it is honest, each said; the family on the page; the line
from which the gate reads; and the gate on this repository."""
import importlib.util
import json
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _gates():
    sys.dont_write_bytecode, was = True, sys.dont_write_bytecode
    try:
        spec = importlib.util.spec_from_file_location("gates_for_selection", ROOT / "scripts" / "gates" / "gates.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
    finally:
        sys.dont_write_bytecode = was
    return m


g = _gates()
claims = g.selection_claims_in

CLAIMS = (
    "THE READ-OUT SELECTS ONE MEMBER, m004.",
    "The census picks the root m004 of the two.",
    "The flow singles out the value 3/2.",
    "So k = 1 is forced.",
    "The beat selects the lift: exactly one spin structure carries it.",
    "A finite classification selects the unique torus bundle (B0287).",          # a claim: whether its page names the family is the gate's question
)
NOT_CLAIMS = (
    "No rule selects one member.",
    "Nothing in the object selects a value.",
    "The read-out does not single out m004.",
    "Whether the weight selects one member is open.",
    "If the flow selected a value, it would be 3.",
    "The picks that stand are of the object's own structure, by a uniqueness theorem, arithmetic or a census.",   # a noun, and no value
    "B01204 says why a symmetry selects nothing (B01225).",                     # "nothing" is the object
    "The arc selects (B01204) its question.",                                   # a citation is no value
)


def test_the_claims_are_read_and_the_sentences_that_claim_nothing_are_not():
    for s in CLAIMS:
        assert claims(s), s
    for s in NOT_CLAIMS:
        assert not claims(s), s


def test_a_denial_excuses_only_in_its_own_clause_and_before_the_word():
    # a denial in an earlier clause does not excuse a claim in a later one; a denial after the word does not either
    assert claims("No measure settles it; the extremum selects the value 2.")
    assert claims("The rule selects one member, which is not m003.")
    # the twin: the same denial in the claim's own clause before the word
    assert not claims("The measure settles it; no extremum selects the value 2.")


def test_what_the_reading_still_passes_and_still_refuses_is_said():
    # STILL PASSES: a claim with no value or member as its object that a reader would call a selection
    assert not claims("The beat selects the spin structure.")
    # STILL PASSES: a claim in other words than the five
    assert not claims("The census determines the value 3.")
    # STILL REFUSED THOUGH HONEST: a deduction, which the rule is not about ("forces" as "implies"); such a line from B1905 on
    # names a family on its page or is reworded
    assert claims("m^2+4 = k^2 forces m = 0.")


def test_the_family_is_read_on_the_page_and_the_gate_reads_from_b1905_on(monkeypatch):
    lines = {"B01905": "THE COUNT SELECTS ONE ROW.", "B01906": "THE CENSUS SELECTS ONE MEMBER.", "B01907": "THE ANOMALY PICKS ONE MEMBER.",
             "B01904": "THE FLOW SELECTS ONE VALUE."}
    pages = {"B01905": "a reading", "B01906": "it is a FINITE CLASSIFICATION with a test of membership", "B01907": "a consistency condition that a candidate can violate",
             "B01904": "none"}
    mapping = {}
    for aid in lines:
        mapping["frontier/%s_x/arc_verdict.json" % aid] = json.dumps({"id": aid, "verdict": "PROVED", "claim_one_line": lines[aid]})
        mapping["frontier/%s_x/FINDINGS.md" % aid] = "# %s\n\n%s\n" % (aid, pages[aid])
    monkeypatch.setattr(g.glob, "glob", lambda pat: [os.path.join(g.ROOT, k) for k in sorted(mapping) if k.endswith("arc_verdict.json")])
    read = lambda rel: mapping[rel.replace(os.sep, "/")]
    hits, older = g.selection_family_hits(reader=read)
    assert [h[0] for h in hits] == ["B01905"] and older == 1                    # B01904 is older and counted; B01906 and B01907 name a family
    ok, msg = g.gate_selection_family(reader=read)
    assert not ok and msg.startswith("1 verdict line(s) from B1905 on claim a selection")
    mapping["frontier/B01905_x/FINDINGS.md"] += "\nIts criterion is a consistency condition.\n"
    assert g.gate_selection_family(reader=read)[0] is True
    # a page that is missing reads as naming nothing
    del mapping["frontier/B01907_x/FINDINGS.md"]
    assert [h[0] for h in g.selection_family_hits(reader=read)[0]] == ["B01907"]


def test_on_this_repository_the_gate_passes_and_counts_the_older_lines():
    ok, detail = g.GATES["selection-family"]()
    assert ok is True, detail
    hits, older = g.selection_family_hits()
    assert hits == [] and ("%d older line(s)" % older) in detail     # 2026-11-13 (C13's follow-ups, patch 3): and held by name with their class
    assert "held by name with their class" in detail
    assert g.SELECTION_FAMILY_FROM == 1905
    # B1905's own verdict line claims nothing by this reading, and its page names both families
    v = json.loads((ROOT / "frontier/B1905_selection_and_chirality_across_the_record/arc_verdict.json").read_text(encoding="utf-8"))
    assert claims(v["claim_one_line"]) == []
    assert g.SELECTION_FAMILIES.search((ROOT / "frontier/B1905_selection_and_chirality_across_the_record/FINDINGS.md").read_text(encoding="utf-8"))


def test_an_arc_whose_page_names_its_family_in_other_words_is_held_only_while_it_keeps_them():
    """2026-11-14 (built again on main's a0bfa2ff4): B1927's page names its two conventions and the condition that selects
    one, in other words than the gate's; it is held by name with those words, the builder's reading, for main to check."""
    import importlib.util, json, sys
    spec = importlib.util.spec_from_file_location("gates_for_the_hold", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec); sys.dont_write_bytecode = True; spec.loader.exec_module(g)
    held = g.SELECTION_FAMILY_NAMED_OTHERWISE
    for aid, words in held.items():
        page = next(ROOT.glob("frontier/%s_*/FINDINGS.md" % aid)).read_text(encoding="utf-8")
        assert all(w in page for w in words), aid
    hits, _ = g.selection_family_hits()
    assert not [h for h in hits if h[0] in held]
    # planted: the page without the words that name its family is reported again
    aid = next(iter(held))
    real = g._read
    def read(rel):
        text = real(rel)
        return text.replace(held[aid][0], "") if rel.replace("\\", "/").startswith("frontier/%s_" % aid) and rel.endswith("FINDINGS.md") else text
    hits, _ = g.selection_family_hits(reader=read)
    assert [h[0] for h in hits] == [aid]


def test_the_older_lines_are_held_by_name_with_their_class():
    """C13's follow-ups, patch 3 (main's M23, item 5): every verdict line before B1905 that the reading reports as a claim is
    classified once, with its clauses word for word and, for a family named, the page's words. Planted: a row taken out,
    a class not of the four, a family's words not on the page, a row whose line reads other clauses."""
    import json
    g = _gates()
    bad, by_class = g.older_selection_lines()
    assert bad == [] and set(by_class) <= set(g.SELECTION_CLASSES) and sum(by_class.values()) == 115, (bad, by_class)
    real = (ROOT / g.SELECTION_FAMILY_OLDER).read_text(encoding="utf-8")
    table = json.loads(real)

    def reader_with(t):
        def read(rel):
            return json.dumps(t, ensure_ascii=False) if rel == g.SELECTION_FAMILY_OLDER else (ROOT / rel).read_text(encoding="utf-8")
        return read

    rows = table["rows"]
    one_out = dict(table, rows=[r for r in rows if r["arc"] != "B1228"])
    assert g.older_selection_lines(reader_with(one_out))[0] == ["B1228: an older verdict line read as a claim and not classified"]
    wrong = dict(table, rows=[dict(r, **{"class": "obvious"}) if r["arc"] == "B924" else r for r in rows])
    assert g.older_selection_lines(reader_with(wrong))[0] == ["B924: the class 'obvious' is not one of deduction, no claim, family named, neither"]
    words = dict(table, rows=[dict(r, **{"on the page": "a census of nothing"}) if r["arc"] == "B1477" else r for r in rows])
    assert g.older_selection_lines(reader_with(words))[0] == ["B1477: the words the table gives for its family are not on its page"]
    other = dict(table, rows=[dict(r, clauses=["another clause"]) if r["arc"] == "B44" else r for r in rows])
    assert g.older_selection_lines(reader_with(other))[0] == ["B44: its verdict line reads other clauses than the table holds"]
    # the twin: the table as it is
    assert g.older_selection_lines(reader_with(table))[0] == []
