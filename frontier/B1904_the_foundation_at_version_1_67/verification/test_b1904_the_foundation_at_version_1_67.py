"""B1904 lock -- the foundation at version 1.67.

What could fail: the version or its log entry missing or out of order; a passage in which the owner was quoted standing
again, or its plain words gone; the status cell of row FK13 holding other words than this version wrote, or another
label than it had; any other status cell differing from version 1.65; a row named to the two older locks that this
version does not name.  No passage is written in this file: main's pairs are read from the arc B1898, where main's script
is held by its hash, and a failing assert names a passage by its number."""
import hashlib
import importlib.util
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]
ARC = pathlib.Path(__file__).resolve().parents[1]
HERE = pathlib.Path(__file__).resolve().parent
G = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
B1886 = ROOT / "frontier" / "B1886_the_foundation_at_version_1_65" / "verification"
B1891 = ROOT / "frontier" / "B1891_the_foundation_at_version_1_66" / "verification"

FK13_AS_THIS_VERSION_WROTE_IT = "46d45c186e0537d7e2db4cf7aa301cbac4037336595c5a4b41c11a7646543f89"      # sha256 of the status cell's text
FK13_LABEL = "**[v1.13] RULED BY THE PRINCIPLE**"
VERSION_1_66_AS_GIT_HOLDS_IT = "f7730d1d71a2a6040a0a6d11f24663d03d641fe5"                              # the blob of GENESIS.md at version 1.66
MARKS = '"“”‘’«»'


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def _bs():
    return _load("build_status_cells_for_b1904", B1886 / "build_status_cells.py")


def _snapshot():
    return json.loads((B1886 / "status_cells.json").read_text(encoding="utf-8"))["v1.65"]


def _writer():
    return _load("write_version_1_67_for_b1904", HERE / "write_version_1_67.py")


def test_the_version_and_its_log_entry():
    assert int(G.split("**Version 1.")[1].split()[0]) >= 67 and G.count("**Version 1.") == 1          # the version only moves forward
    assert re.search(r"(?m)^- \*\*v1\.67 · 2026-11-12 · main B1904\.\*\*", G)
    assert G.index("- **v1.67 · ") < G.index("- **v1.66 · ") < G.index("- **v1.65 · ")
    entry = G[G.index("- **v1.67 · "):G.index("- **v1.66 · ")]
    assert "No item is added and no status changes: the words of one status cell change (row FK13:" in entry
    assert "its label is as it was" in entry and "no status cell changes" not in entry               # the sentence main's script first wrote is not in it
    assert "B[[N]]" not in G


def test_the_seven_passages_are_in_plain_words():
    """main's seven pairs, read from main's own file: the passage that quoted the owner stands nowhere, and its plain words
    stand once and hold no quotation mark"""
    beside_mains = _writer().MAINS.parent / "__pycache__"
    there = beside_mains.exists()
    m = _writer().mains()
    assert beside_mains.exists() == there, "reading main's pairs left a folder beside main's files, which the lock of B1898 counts"
    assert len(m.EDITS) == 7
    for number, (old, new) in enumerate(m.EDITS, 1):
        assert G.count(old) == 0, "passage %d stands in the foundation as it was" % number
        assert G.count(new) == 1, "the plain words of passage %d stand %d time(s)" % (number, G.count(new))
        assert sum(old.count(q) for q in MARKS) >= 2 and not any(q in new for q in MARKS), "passage %d" % number
    # main's file is the one the arc B1898 holds by its hash, and this arc's script holds no passage of its own
    held = json.loads((ROOT / "frontier" / "B1898_review_80_one_hundred_findings_and_what_main_checked" / "verification" / "as_main_wrote_them.json").read_text(encoding="utf-8"))
    assert hashlib.sha256(_writer().MAINS.read_bytes()).hexdigest() == held["verification/checks/genesis_v1_67.py"]
    mine = (HERE / "write_version_1_67.py").read_text(encoding="utf-8") + pathlib.Path(__file__).read_text(encoding="utf-8")
    for number, (old, new) in enumerate(m.EDITS, 1):
        assert old not in mine and new not in mine, "passage %d is written in this arc's own files" % number


def _what_this_lock_holds_of_the_status_cells(text):
    """every way the status cells of a text are not what this version left: FK13's words, FK13's label, any other cell"""
    bs, snap = _bs(), _snapshot()
    now, tab = bs.identifier_rows(text), bs.status_table_rows(text)
    out = []
    cell = now.get("FK13", "")
    if hashlib.sha256(cell.encode("utf-8")).hexdigest() != FK13_AS_THIS_VERSION_WROTE_IT:
        out.append("FK13: the words of its status cell are not the words version 1.67 wrote")
    if bs.label(cell) != FK13_LABEL or bs.label(snap["identifier_rows"]["FK13"]) != FK13_LABEL:
        out.append("FK13: its label is not the label it had at version 1.65")
    out += ["%s: its status cell is not the cell of version 1.65" % k for k in sorted(snap["identifier_rows"]) if k != "FK13" and now.get(k) != snap["identifier_rows"][k]]
    out += ["%s: its status cell is not the cell of version 1.65" % k for k in sorted(snap["status_table_rows"]) if tab.get(k) != snap["status_table_rows"][k]]
    out += ["%s: a row that version 1.65 did not have" % k for k in sorted(set(now) - set(snap["identifier_rows"])) + sorted(set(tab) - set(snap["status_table_rows"]))]
    return out


def test_the_status_cell_of_fk13_has_its_new_words_and_its_old_label_and_no_other_cell_differs():
    bs, snap = _bs(), _snapshot()
    assert _what_this_lock_holds_of_the_status_cells(G) == []
    cell = bs.identifier_rows(G)["FK13"]
    assert cell != snap["identifier_rows"]["FK13"] and not any(q in cell for q in MARKS)             # its words did change, and they quote nothing
    assert sum(snap["identifier_rows"]["FK13"].count(q) for q in MARKS) == 2                          # the cell of 1.65 held one quotation
    # the table of rows named to the two older locks is one row, this version's: a name added there loosens both
    assert {k: v[:2] for k, v in bs.NAMED_BY_A_VERSION.items()} == {"FK13": ("v1.67", "B1904")}


def _line_of(text, opens):
    lines = [l for l in text.split("\n") if l.startswith(opens)]
    assert len(lines) == 1, opens
    return lines[0]


def test_the_three_locks_against_planted_changes():
    """main's two plants (its M18), and a third.  Each lock is asked by the function its own tests ask."""
    bs = _bs()
    older = _load("lock_of_version_1_65_for_b1904", B1886 / "test_b1886_the_foundation_at_version_1_65.py")._rows_that_moved_from_version_1_64
    old = _load("lock_of_version_1_66_for_b1904", B1891 / "test_b1891_the_foundation_at_version_1_66.py")._what_differs_from_version_1_65
    mine = _what_this_lock_holds_of_the_status_cells
    assert older(G) == [] and old(G) == [] and mine(G) == []                                         # the foundation as it stands
    # 1. the label of FK13 changed: all three locks fail
    row = _line_of(G, "| FK13 ")
    assert row.count("RULED BY THE PRINCIPLE") == 1
    planted = G.replace(row, row.replace("RULED BY THE PRINCIPLE", "DERIVED"))
    assert planted != G and older(planted) == ["FK13"] and old(planted) == ["identifier_rows: changed: FK13"] and len(mine(planted)) == 2
    # 2. the bracket of another row changed: the two older locks fail (and so does this one)
    cell = bs.identifier_rows(G)["FK1"]
    assert G.count(cell) == 1 and cell.endswith(")") and bs.label(cell) != cell
    planted = G.replace(cell, cell[:-1] + ", and one word more)")
    assert bs.label(bs.identifier_rows(planted)["FK1"]) == bs.label(cell)                             # its label is as it was
    assert older(planted) == ["FK1"] and old(planted) == ["identifier_rows: changed: FK1"] and mine(planted)
    # 3. the bracket of FK13 changed again, its label as it was: the two older locks hold its label and nothing more, and pass;
    #    this lock holds its words, and fails.  That is the design, and it is why this lock must stand.
    cell = bs.identifier_rows(G)["FK13"]
    assert G.count(cell) == 1 and cell.endswith(")")
    planted = G.replace(cell, cell[:-1] + ", and one word more)")
    assert older(planted) == [] and old(planted) == [] and mine(planted) == ["FK13: the words of its status cell are not the words version 1.67 wrote"]
    # 4. a row named to the older locks that no version names: with the name taken out, the two fail on the foundation as it stands
    keep = dict(bs.NAMED_BY_A_VERSION)
    assert bs.differs("FK13", _snapshot()["identifier_rows"]["FK13"], bs.identifier_rows(G)["FK13"]) is False
    bs.NAMED_BY_A_VERSION.clear()
    try:
        assert bs.differs("FK13", _snapshot()["identifier_rows"]["FK13"], bs.identifier_rows(G)["FK13"]) is True
    finally:
        bs.NAMED_BY_A_VERSION.update(keep)


def test_the_script_writes_this_version_from_the_one_before_where_git_has_it():
    """the writer, run on the foundation of version 1.66 as git holds it, gives a text in which this version's status cells
    stand.  Where git does not hold that blob the writer is still run on the page as it stands, and must refuse: its
    passages are no longer there."""
    import subprocess
    w = _writer()
    try:
        w.version_1_67(G)
        refused = False
    except AssertionError:
        refused = True
    assert refused, "the writer ran a second time, on version 1.67"
    r = subprocess.run(["git", "-C", str(ROOT), "cat-file", "-p", VERSION_1_66_AS_GIT_HOLDS_IT], capture_output=True, text=True)
    before = r.stdout if r.returncode == 0 and "**Version 1.66 · 2026-11-12 · canonical.**" in r.stdout else None
    written = w.version_1_67(before) if before is not None else None
    assert written is None or _what_this_lock_holds_of_the_status_cells(written) == []
    assert written is None or all(written.count(new) == 1 and written.count(old) == 0 for old, new in w.mains().EDITS)
    assert before is None or sum(before.count(old) for old, _ in w.mains().EDITS) == 7             # and version 1.66 held each passage once


def test_the_sweep_found_the_passages_in_no_living_page():
    """the kept output of the sweep; the sweep itself reads every tracked file and is run by hand (the arc's Reproduce)"""
    out = (HERE / "sweep_for_the_seven_passages_out.txt").read_text(encoding="utf-8").split("\n")
    assert out[-2] == "files of another kind that hold a passage as it was: 0" and len([l for l in out if l.startswith("passage ")]) == 7
    assert all("a kept copy of an older version of the foundation" in l for l in out if l.startswith("passage "))
    sweep = _load("sweep_for_b1904", HERE / "sweep_for_the_seven_passages.py")
    assert sweep.kind("docs/A_PAGE.md").startswith("ANOTHER FILE") and sweep.kind("GENESIS.md").startswith("ANOTHER FILE")
    assert not sweep.kind("frontier/B1843_genesis_v1_62/received/GENESIS_v1_61_main.md").startswith("ANOTHER")


def test_the_arc_says_what_it_is():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("No item is added", "Who found them", "What is not done", "## Seen first", "## Disclosed", "0 of 19", "FK13", "The label is as it was"):
        assert s in f, s
    assert not any(q in f for q in "“”")
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1904" and set(v["scope"]) == {"frame", "object", "reach", "hypotheses"} and v["claim_one_line"].endswith("0 of 19.")
