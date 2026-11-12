"""B1894 lock -- Review 79's second round.

What could fail: a finding in the table with no row in the count, or twice; a quotation of a reader's file that is not in the
file it names at the commit read; a number on the page that is not the data's; the sign the round corrected standing again in
one of the four places; a mend the table names being undone."""
import importlib.util
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = ARC.parents[1]
A = json.loads((HERE / "answers.json").read_text(encoding="utf-8"))
F = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())


def test_the_table_and_the_count_are_one():
    rows = re.findall(r"^\| (2(?:W|SM-|A|X)\d+) \|", (ARC / "ANSWERS.md").read_text(encoding="utf-8"), re.M)
    assert rows == A["ids"] and len(rows) == len(set(rows)) == A["findings"] == sum(A["by reader"].values())
    for prefix, reader in (("2W", "the web seat"), ("2SM-", "the SM seat"), ("2A", "agy-002"), ("2X", "agy-exp")):
        assert sum(1 for r in rows if re.fullmatch(re.escape(prefix) + r"\d+", r)) == A["by reader"][reader], reader
    assert A["held in full"] + len(A["reproduced in part"]) == A["findings"]
    groups = A["found by more than one reader"]
    assert {x for g in groups for x in g} <= set(rows) and A["distinct faults"] == A["findings"] - sum(len(g) - 1 for g in groups)
    assert set(A["a correction that did not travel"]) <= set(rows)
    assert "%d findings on main's mends, and all held" % A["findings"] in F and "%d distinct faults" % A["distinct faults"] in F
    n = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]
    assert "%s of the %d" % (n[len(A["a correction that did not travel"])].capitalize(), A["findings"]) in F


def test_the_readers_check_of_the_ninety_nine_adds_up_and_is_what_the_page_says():
    c = A["the readers' check of main's 99 answers"]
    total = {k: sum(v.get(k, 0) for v in c.values()) for k in ("checked", "right and complete", "not complete", "not mended, as main had said", "with the builder")}
    assert total["checked"] == 99 == sum(total[k] for k in total if k != "checked")
    assert "They report %d right and complete, %d not complete" % (total["right and complete"], total["not complete"]) in F
    assert "and %d still with the builder" % total["with the builder"] in F
    t = A["the tripwire against planted errors, by the SM seat"]
    assert "| the first round's planted errors, against the lock as it was then | %d of %d that were faults |" % (t["caught at the first round"], t["the first round's errors that were faults"]) in F
    assert "| the same errors, against the lock as mended at Review 79 | %d of %d |" % (t["caught after Review 79's mend"], t["the first round's errors that were faults"]) in F
    assert "| %d new errors, against the lock as mended at Review 79 | %d |" % (t["new errors"], t["new errors caught"]) in F


def test_every_quotation_was_found_and_the_check_can_fail():
    q = json.loads((HERE / "quote_check.json").read_text(encoding="utf-8"))
    assert set(q) == {"the SM seat", "the web seat", "agy-002", "agy-exp"}
    sm = q["the SM seat"]
    assert sm["found"] + sm["of its own first file, found there"] == sm["quotations"] and sm["found nowhere"] == 0
    assert all(v["quotations"] == v["found"] > 0 for k, v in q.items() if k != "the SM seat")
    assert sm["control: the first quotation altered by one character is reported missing"] is True
    in_main = sum(v["found"] for v in q.values())
    assert "%d of %d in main's files" % (in_main, in_main) in F
    spec = importlib.util.spec_from_file_location("b1894_quote_check", HERE / "quote_check.py"); qc = importlib.util.module_from_spec(spec); spec.loader.exec_module(qc)
    for reader, r in qc.build().items():
        assert r is None or r == q[reader], reader


def test_the_sign_stands_corrected_in_the_four_places():
    old = "the index is their sum above its value at no unit, so a unit on one line gives one"
    for rel in ("docs/THEOREM_REGISTRY.md", "docs/LAW_MAP.md", "frontier/B1641_w46_on_main_and_the_two_objects/arc_verdict.json"):
        t = (ROOT / rel).read_text(encoding="utf-8")
        assert t.count(old) == 1, rel                                   # kept once, inside the bracket that corrects it
        i = t.index(old)
        assert "This bracket first read" in t[i - 60:i] and "minus the sum of the units: -3 for the uniform unit" in t[i - 700:i], rel
    note = (ROOT / "frontier" / "B1641_w46_on_main_and_the_two_objects" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "CORRECTED 2026-11-12, a second time" in note and "gives the index −3, and a unit on" in note
    table = json.loads((ROOT / "frontier" / "B1641_w46_on_main_and_the_two_objects" / "verification" / "w46_on_main.json").read_text(encoding="utf-8"))["W3"]
    assert all(round(ident["table"]["0,n=1"][0]) == -3 and round(ident["table"]["0,n=-1"][0]) == 3 for ident in table.values())


def test_the_arc_says_what_it_did_not_do():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("were not run against the tripwire's new form", "have been read by nobody but main", "What main got wrong in this round", "Not closed, and asserted as open",
              "## Seen first", "## Disclosed", "0 of 19"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1894" and set(v["scope"]) == {"frame", "object", "reach", "hypotheses"} and v["scope"]["reach"] in ("single", "class", "general")
    assert v["claim_one_line"].endswith("0 of 19.")
