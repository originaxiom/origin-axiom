"""B1891 lock -- the foundation at version 1.66.

What could fail: a status cell differing from version 1.65 as committed; one of the four corrected sentences standing in its old
form outside the bracket that quotes it; the version's log entry missing or out of order."""
import importlib.util
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]
ARC = pathlib.Path(__file__).resolve().parents[1]
G = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
FLAT = " ".join(G.split())


def test_the_version_and_its_log_entry():
    assert int(G.split("**Version 1.")[1].split()[0]) >= 66 and G.count("**Version 1.") == 1          # the version only moves forward
    assert re.search(r"(?m)^- \*\*v1\.66 · 2026-11-12 · main B1891\.\*\*", G)
    assert G.index("- **v1.66 · ") < G.index("- **v1.65 · ") < G.index("- **v1.64 · ")
    assert "No item is added and no status cell changes." in G and "The v1.65 entry below is not rewritten." in G


def test_no_status_cell_changed_from_version_1_65():
    """both kinds of row, read by the builder of B1886's snapshot, against that snapshot's cells for 1.65"""
    b = ROOT / "frontier" / "B1886_the_foundation_at_version_1_65" / "verification"
    spec = importlib.util.spec_from_file_location("build_status_cells_for_b1891", b / "build_status_cells.py")
    bs = importlib.util.module_from_spec(spec); spec.loader.exec_module(bs)
    snap = json.loads((b / "status_cells.json").read_text(encoding="utf-8"))["v1.65"]
    now_id, now_tab = bs.identifier_rows(G), bs.status_table_rows(G)
    assert len(snap["identifier_rows"]) == 32 and len(snap["status_table_rows"]) == 21
    for kind, now in (("identifier_rows", now_id), ("status_table_rows", now_tab)):
        gone = sorted(set(snap[kind]) - set(now))
        # CHANGED 2026-11-12 (the foundation's version 1.67, arc B1904; main's word in its M18).  It read:
        #     changed = {k: (snap[kind][k], now[k]) for k in snap[kind] if k in now and snap[kind][k] != now[k]}
        #     assert gone == [] and changed == {}, (kind, gone, changed)
        # Version 1.67 puts the account in the bracket of FK13's status cell in plain words; its label is as it was.  What
        # this lock protects is that no STATUS changes without a version saying so.  A row that a version names (beside
        # the snapshot's builder) is compared by its label, every other row by its whole cell.  The message names rows,
        # not cells: a cell of the snapshot can hold words that are printed nowhere.
        changed = sorted(k for k in snap[kind] if k in now and bs.differs(k, snap[kind][k], now[k]))
        assert gone == [] and changed == [], (kind, gone, changed)
    assert set(now_id) == set(snap["identifier_rows"])                      # and no item is added
    # that this can fail: a cell changed in what is read now is reported
    planted = dict(now_id, SE2="DERIVED")
    # (2026-11-12, version 1.67: compared as the lines above compare.  It read: snap["identifier_rows"][k] != planted.get(k))
    assert [k for k in snap["identifier_rows"] if bs.differs(k, snap["identifier_rows"][k], planted.get(k))] == ["SE2"]


# ---- Review 80 (2026-11-12; a reader's finding F6, its second part, not checked by main, made again here).  The test above
# compares the cells of the rows that the snapshot holds, and the set of rows that open with an identifier.  It does not
# compare the set of rows of the status tables, so a row added to one is not seen; and the builder reads a row by its bars
# with a space on each side, so a row written with no spaces is read by neither of its two readings.
def _the_snapshots_builder():
    b = ROOT / "frontier" / "B1886_the_foundation_at_version_1_65" / "verification"
    spec = importlib.util.spec_from_file_location("build_status_cells_for_b1891_again", b / "build_status_cells.py")
    bs = importlib.util.module_from_spec(spec); spec.loader.exec_module(bs)
    return bs, json.loads((b / "status_cells.json").read_text(encoding="utf-8"))["v1.65"]


def _rows_that_are_not_read(text):
    """the rows of a table that have not as many cells as their table's header, counted as the builder counts them: by bars
    with a space on each side.  Such a row is skipped by the builder without a word."""
    out, width = [], None
    for n, line in enumerate(text.split("\n"), 1):
        if not line.lstrip().startswith("|"):
            width = None
            continue
        if set(line.replace("|", "").replace(" ", "")) <= set("-:"):
            continue
        cells = len(line.strip().strip("|").split(" | "))
        if width is None:
            width = cells
        elif cells != width:
            out.append(n)
    return out


def _what_differs_from_version_1_65(text):
    """every difference of the foundation's status rows from the snapshot of version 1.65: a row gone, a cell changed, a row
    added to either kind, and a row that the builder does not read"""
    bs, snap = _the_snapshots_builder()
    out = []
    for kind, now in (("identifier_rows", bs.identifier_rows(text)), ("status_table_rows", bs.status_table_rows(text))):
        out += ["%s: gone: %s" % (kind, k) for k in sorted(set(snap[kind]) - set(now))]
        out += ["%s: changed: %s" % (kind, k) for k in snap[kind] if k in now and bs.differs(k, snap[kind][k], now[k])]      # until version 1.67: snap[kind][k] != now[k]
        out += ["%s: added: %s" % (kind, k) for k in sorted(set(now) - set(snap[kind]))]
    out += ["a row that is not read, at line %d" % n for n in _rows_that_are_not_read(text)]
    return out


def _as_the_test_above_compares(text):
    """True where the comparisons of the test above pass on a text"""
    bs, snap = _the_snapshots_builder()
    now_id, now_tab = bs.identifier_rows(text), bs.status_table_rows(text)
    for kind, now in (("identifier_rows", now_id), ("status_table_rows", now_tab)):
        if sorted(set(snap[kind]) - set(now)) or {k for k in snap[kind] if k in now and bs.differs(k, snap[kind][k], now[k])}:      # until version 1.67: the whole cell
            return False
    return set(now_id) == set(snap["identifier_rows"])


def test_no_row_is_added_to_a_status_table_and_no_row_goes_unread():
    assert _what_differs_from_version_1_65(G) == [] and _as_the_test_above_compares(G)
    first = "| PF1 "
    assert G.count("\n" + first) == 1
    at = G.index("\n" + first) + 1
    planted = {
        "a row added to a status table, with no identifier": G[:at] + "| a new face | planted | planted words | DERIVED |\n" + G[at:],
        "a row with an identifier, written with no spaces at its bars": G[:at] + "|PF9|planted|planted words|DERIVED|\n" + G[at:],
        "a row with no identifier and no spaces": G[:at] + "|a new face|planted|planted words|DERIVED|\n" + G[at:],
    }
    for what, text in planted.items():
        assert _as_the_test_above_compares(text), what                            # the test above passes: the finding
        assert _what_differs_from_version_1_65(text), what
    # what the test above does see is seen here as well: a cell changed, and a row with an identifier added
    cell = G[at:G.index("\n", at)]
    assert cell.rstrip().endswith("|") and not _as_the_test_above_compares(G[:at] + cell.rsplit(" | ", 1)[0] + " | PLANTED |" + G[at + len(cell):])
    assert _what_differs_from_version_1_65(G[:at] + cell.rsplit(" | ", 1)[0] + " | PLANTED |" + G[at + len(cell):])


def test_the_four_sentences_stand_corrected_and_the_old_forms_only_where_they_are_quoted():
    for new in ("Fourteen entries of the record, which are eleven things, came as suppositions",
                "most of what the record holds about the weave is unchanged, and what changes is the hand",
                "the walk's law of run lengths and the absence of a fixed modulus stand",
                "among the histories of at most five letters that are not a power of a shorter one it is the only one that does"):
        assert new in FLAT, new
    assert "the two fixed characters, the walk's measure and the absence of a fixed modulus stand" not in FLAT      # the sentence itself is gone ("the walk's measure" is said elsewhere, of the walk)
    # [CHANGED 2026-11-12 (Review 80, the web seat's finding 6): the fourth sentence's old form was not looked for, and the
    #  old sentence put back beside the new one passed.  It is looked for now.  It is not kept in the foundation, so it need
    #  not be found; where it is found it must be a quotation beside its correction, like the others.]
    for old, kept in (("Eleven entries", True), ("every statement the record holds about the weave is unchanged except the hand", True),
                      ("is the only history of at most five letters that does", False)):
        places = [m.start() for m in re.finditer(re.escape(old), FLAT)]
        assert places or not kept, old                                      # the first two old forms are kept, quoted, where they are corrected
        for k in places:
            assert re.search(r"\[v1\.66|This read|v1\.66 ·", FLAT[max(0, k - 400):k + 60]), (old, FLAT[max(0, k - 120):k + 60])
    assert '("A condition to derive")' not in G                              # the quotation of the owner is in plain words


def test_the_arc_says_what_it_is():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("No item is added", "Who found them", "What is not done", "## Seen first", "## Disclosed", "0 of 19"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1891" and set(v["scope"]) == {"frame", "object", "reach", "hypotheses"} and v["claim_one_line"].endswith("0 of 19.")
