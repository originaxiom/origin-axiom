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


CHECKED = "**[CHECKED BY MAIN 2026-11-14 (M37; register row P-849):"


def _unchecked(pages, rows):
    """the arcs whose page lacks main's check after the note that waited for it, or whose row of the classified file
    does not carry it"""
    bad = []
    for r in rows:
        t = pages[r["arc"]]
        c = r.get("checked_by_main") or {}
        at, ck = t.find(MARK), t.find(CHECKED)
        if not c or c.get("row") != "P-849" or c.get("class") not in ("family named on the page", "a deduction", "no selection of its own") \
                or ck < at or at < 0 or ("%s — %s." % (c.get("class"), c.get("words"))) not in t[ck:]:
            bad.append(r["arc"])
    return bad


def test_main_check_is_carried_to_each_page_and_row():
    """2026-11-14 (main's M37): none of the twelve is a selection without its family; main's class and words stand on
    each page after the note that waited for them, and in each row of the classified file."""
    rows = _neither()
    pages = {r["arc"]: _page(r["arc"]).read_text(encoding="utf-8") for r in rows}
    assert _unchecked(pages, rows) == []
    by = {}
    for r in rows:
        by[r["checked_by_main"]["class"]] = by.get(r["checked_by_main"]["class"], 0) + 1
    assert by == {"family named on the page": 8, "a deduction": 2, "no selection of its own": 2}
    # planted: a page without main's check; a row without it; a check standing above the note it answers
    one = rows[1]["arc"]
    t = pages[one]; ck = t.index("\n" + CHECKED)
    assert _unchecked(dict(pages, **{one: t[:ck] + t[t.index("]**\n", ck) + 4:]}), rows) == [one]
    stripped = [dict(r) for r in rows]; del stripped[0]["checked_by_main"]
    assert _unchecked(pages, stripped) == [rows[0]["arc"]]
    note = t[ck:t.index("]**\n", ck) + 4]
    moved = note + t.replace(note, "")
    assert _unchecked(dict(pages, **{one: moved}), rows) == [one]
