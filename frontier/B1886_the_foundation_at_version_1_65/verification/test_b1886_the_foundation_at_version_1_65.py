"""B1886 lock -- the foundation at version 1.65.

What could fail: a status cell of an older item differing from the committed v1.64; a new item missing or typed otherwise; the
sentence on even ticks struck instead of re-typed; the map or the budget not carrying the new items."""
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[3]
ARC = pathlib.Path(__file__).resolve().parents[1]
G = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
V164 = "8f0b03814"                       # main's commit that holds version 1.64 as it last stood


def _rows(text):
    """the status cell of every table row that opens with one of the foundation's identifiers"""
    out = {}
    for line in text.split("\n"):
    # (2026-11-12, Review 79: the GAP alternative below matches no row; the foundation's GAPs are bullets, not table rows.  Kept, so that
    #  the pattern is the one the arc was landed with; the rows it reads are the PF, GM, SE, T-ROOT and FK rows.)
        m = re.match(r"^\| ((?:PF\d|GM\d[a-d]?|SE\d|T-ROOT|FK\d+|GAP\d))\b[^|]*\|", line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        ident = m.group(1)
        status = cells[3] if ident.startswith("PF") else cells[2]
        out.setdefault(ident, status)
    return out


def test_the_version_and_its_log_entry():
    # 2026-11-12: the header named this version while it was the last; a later version keeps this arc's entry and moves the header on
    assert int(G.split("**Version 1.")[1].split()[0]) >= 65 and G.count("**Version 1.") == 1
    assert re.search(r"(?m)^- \*\*v1\.65 · 2026-11-11 · main B1886\.\*\*", G)
    assert "No status cell of an existing item changes; the v1.64 entry below is not rewritten." in G
    assert G.index("- **v1.65 · ") < G.index("- **v1.64 · ")


def test_no_status_cell_of_an_existing_item_changed():
    # CORRECTED 2026-11-12 (Review 79): where git did not hold the commit this test SKIPPED, so on a shallow clone or an export the
    # arc's central claim was not tested and the suite stayed green.  The older version's cells are now a committed file
    # (status_cells.json, built by build_status_cells.py), read wherever git cannot give them; the next test holds that file.
    r = subprocess.run(["git", "-C", str(ROOT), "show", V164 + ":GENESIS.md"], capture_output=True, text=True)
    if r.returncode == 0:
        assert "**Version 1.64 · 2026-11-10 · canonical.**" in r.stdout
        old = _rows(r.stdout)
    else:
        old = json.loads((pathlib.Path(__file__).resolve().parent / "status_cells.json").read_text(encoding="utf-8"))["v1.64"]["identifier_rows"]
    new = _rows(G)
    assert len(old) == 29                                                                     # the rows of v1.64 that open with an identifier: a fixed commit, so a fixed count
    assert {"PF1", "PF2", "PF3", "GM1", "GM5c", "GM5d", "SE1", "SE2", "T-ROOT", "FK1", "FK2", "FK3", "FK9", "FK15"} <= set(old)
    assert set(new) - set(old) == {"PF5", "SE3", "FK16"}                # the three new items, and no other
    changed = {k: (old[k], new[k]) for k in old if old[k] != new.get(k)}
    assert changed == {}, changed
    assert old["GM5c"] == new["GM5c"] == "OPEN" and old["SE2"] == new["SE2"] == "CHOSEN" and new["FK2"] == "CHOSEN" and new["FK3"] == "OPEN"


def test_the_three_new_items_and_their_types():
    rows = _rows(G)
    assert rows["PF5"] == "OPEN" and rows["FK16"] == "OPEN" and rows["SE3"].startswith("POSTULATED (main's entry, tagged")
    assert "| PF5 **[v1.65]** | **The claim: the whole has one self-consistent outcome.**" in G and "Nothing in this file is derived from it" in G
    assert "| SE3 **[v1.65]** | **The ground is the act itself: the tick.** Its level is the prime that its discriminant is, 5." in G
    assert "By which reading the level is 5 is part of the postulate" in G and "that rule gives the tick no line at any level" in G
    assert "| FK16 **[v1.65]** | The observer's place" in G
    assert G.count("PF4") == 2                                           # the candidate fourth face of FK15, and the note that says the number is taken


def test_even_ticks_is_re_typed_and_not_struck():
    assert "GM5c: **even ticks observed**" in G                            # the sentence of v1.33 stands in the text
    assert "is no longer recorded as a ruling" in G and "it is a condition that the weight has to deliver" in G
    assert "The criterion is necessary and is not shown sufficient" in G and "GM5c stays OPEN." in G
    assert "That is not derived, and it is not counted as derived" in G
    assert "No status here is set by a ruling on a fact." in G
    assert "This file holds on the status of every item of the foundation." in G


def test_the_map_the_budget_and_the_falsifier_register_carry_it():
    nodes = {n["id"]: n for n in json.loads((ROOT / "frontier" / "B1858_the_closure_map" / "NODES.json").read_text(encoding="utf-8"))}
    assert nodes["G:SE3"]["grade"] == "POSTULATED" and nodes["G:SE3"]["weave_or_thread"] == "thread"
    assert nodes["G:PF5"]["grade"] == "OPEN" and nodes["G:PF5"]["weave_or_thread"] == "weave"
    assert nodes["G:FK16"]["grade"] == "OPEN" and nodes["G:FK16"]["weave_or_thread"] == "weave"
    assert nodes["G:GM5c"]["grade"] == "OPEN" and nodes["G:SE2"]["grade"] == "CHOSEN"
    prog = json.loads((ROOT / "frontier" / "B1861_the_closure_programme" / "PROGRAMME.json").read_text(encoding="utf-8"))
    ground = [i for i in prog["inputs"] if i["name"] == "the ground"]
    assert len(ground) == 1 and ground[0]["kinds"] == {"axiom": 1} and ground[0]["members"] == ["G:SE3"]
    assert prog["exits"]["the ground"][0] == "ADMITTED" and prog["exits"]["the orientation"][0] == "BACK-EDGE NAMED"
    assert prog["stats"]["budget"]["axiom"] >= 9 and prog["stats"]["independent_choices"] >= 39
    pk = {p["id"]: p for p in prog["packages"]}
    assert "G:SE3" in pk["WP-1.5"]["nodes"] and "G:PF5" in pk["WP-1.6"]["nodes"] and "G:FK16" in pk["WP-1.4"]["nodes"]
    fr = (ROOT / "docs" / "FALSIFIER_REGISTER.md").read_text(encoding="utf-8")
    assert "## The programme's own claim" in fr and "two distinct self-consistent outcomes of the joint action, exhibited" in fr


def test_the_arc_says_what_it_does_not_do():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("No status cell of an existing item changes", "It derives nothing and earns no value", "## Seen first", "## Disclosed", "0 of 19"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1886" and v["claim_one_line"].endswith("0 of 19.")


def test_every_status_cell_of_both_kinds_of_row_at_both_versions():
    """Added 2026-11-12 (Review 79).  The findings said the lock compares "them all" with the committed v1.64.  It read the 29 rows
    that open with an identifier and not the foundation's other tables that carry a status; a reader's own route found 19 such
    rows, none changed.  Both kinds are held here, from a committed snapshot of the two versions, so the comparison runs in any
    checkout and cannot skip; and where git has the two commits the snapshot is rebuilt from them and must be the same."""
    import importlib.util
    here = pathlib.Path(__file__).resolve().parent
    S = json.loads((here / "status_cells.json").read_text(encoding="utf-8"))
    a, b = S["v1.64"], S["v1.65"]
    assert (a["commit"], b["commit"]) == (V164, "9ace774f4") and all(re.fullmatch(r"[0-9a-f]{40}", x["blob"]) for x in (a, b)) and a["blob"] != b["blob"]
    assert (len(a["identifier_rows"]), len(a["status_table_rows"])) == (29, 19)               # two fixed commits, so fixed counts
    for kind in ("identifier_rows", "status_table_rows"):
        changed = {k: (a[kind][k], b[kind].get(k)) for k in a[kind] if a[kind][k] != b[kind].get(k)}
        assert changed == {}, (kind, changed)                                                 # no row of v1.64 is gone, and no status cell of one has changed
    assert set(b["identifier_rows"]) - set(a["identifier_rows"]) == {"PF5", "SE3", "FK16"}
    assert sorted(k.split(" :: ")[1] for k in set(b["status_table_rows"]) - set(a["status_table_rows"])) == ["PF5 **[v1.65]**", "SE3 **[v1.65]**"]
    # that this can fail: a status cell changed in the second snapshot is reported
    planted = dict(b["identifier_rows"], GM5c="DERIVED")
    assert {k for k in a["identifier_rows"] if a["identifier_rows"][k] != planted.get(k)} == {"GM5c"}
    # the snapshot is git's, wherever git has the commits
    spec = importlib.util.spec_from_file_location("build_status_cells", here / "build_status_cells.py"); bs = importlib.util.module_from_spec(spec); spec.loader.exec_module(bs)
    rebuilt = bs.build()
    assert rebuilt is None or rebuilt == S
    assert bs.identifier_rows(G) == _rows(G)                                                  # the builder's reading of a row is this lock's

