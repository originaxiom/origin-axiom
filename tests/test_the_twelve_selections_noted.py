"""2026-11-13 (main's M29): the twelve older verdict lines of class "neither" in that classification each carry a
dated note on their arc's page, marked as waiting on main's check of the classification's rows (the classification of
the older verdict lines that the gate selection-family reads, in the folder of the arc that read the record for
selection and chirality).

The twelve are read from the classification itself, so a row that changes class changes what is held here."""
import hashlib, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CLASSIFIED = sorted(ROOT.glob("frontier/*/verification/older_verdict_lines_classified.json"))[0]
MARK = "**[NOTED 2026-11-13 (the building session, at main's word in M29;"
WAITS = "This reading WAITS ON MAIN'S CHECK of that classification's rows"


def _neither():
    return [r for r in json.loads(CLASSIFIED.read_text(encoding="utf-8"))["rows"] if r["class"] == "neither"]


def _page(arc):
    for v in sorted(ROOT.glob("frontier/%s_*/arc_verdict.json" % arc)):
        if json.loads(v.read_text(encoding="utf-8")).get("id") == arc:
            return v.parent / "FINDINGS.md"
    raise AssertionError("no folder for " + arc)


def _unnoted(pages):
    """the arcs whose page lacks the note, its words, or its mark of waiting"""
    bad = []
    for r in _neither():
        t = pages[r["arc"]]
        at = t.find(MARK)
        if at < 0 or t.count(MARK) != 1 or WAITS not in t[at:] or any("“%s”" % c not in t[at:] for c in r["clauses"]):
            bad.append(r["arc"])
    return bad


def test_the_twelve_are_the_classifications_and_each_is_noted():
    rows = _neither()
    arcs = [r["arc"] for r in rows]
    # the twelve, held by the digest of their list as sent on 2026-11-13: the paper's verification manifest counts every
    # lock that names an arc of the paper, and this lock is about none of the paper's claims, so it names no arc
    assert len(arcs) == 12 and hashlib.sha256(",".join(arcs).encode()).hexdigest() == "bba84b5bdb61f0d2756d2168b384d4f71789724bbef08ecc3cff6fadfc17b00e"
    pages = {a: _page(a).read_text(encoding="utf-8") for a in arcs}
    assert _unnoted(pages) == []
    # planted: one note taken out, one note without its mark of waiting, one note whose clause differs
    one, two, three = arcs[2], arcs[9], arcs[0]
    assert _unnoted(dict(pages, **{one: pages[one][:pages[one].index(MARK)]})) == [one]
    assert _unnoted(dict(pages, **{two: pages[two].replace(WAITS, "This reading is settled")})) == [two]
    clause = rows[0]["clauses"][0]
    at = pages[three].index(MARK)
    changed = pages[three][:at] + pages[three][at:].replace(clause, clause[:-1] + "#", 1)
    assert _unnoted(dict(pages, **{three: changed})) == [three]


def test_no_other_page_carries_the_note():
    neither = {r["arc"] for r in _neither()}
    carrying = set()
    for p in ROOT.glob("frontier/B*/FINDINGS.md"):
        if MARK in p.read_text(encoding="utf-8", errors="ignore"):
            carrying.add(p.parent.name.split("_")[0])
    assert carrying == neither
