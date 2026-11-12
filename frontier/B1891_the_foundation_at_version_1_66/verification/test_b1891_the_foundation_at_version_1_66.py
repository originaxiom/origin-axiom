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
        changed = {k: (snap[kind][k], now[k]) for k in snap[kind] if k in now and snap[kind][k] != now[k]}
        assert gone == [] and changed == {}, (kind, gone, changed)
    assert set(now_id) == set(snap["identifier_rows"])                      # and no item is added
    # that this can fail: a cell changed in what is read now is reported
    planted = dict(now_id, SE2="DERIVED")
    assert [k for k in snap["identifier_rows"] if snap["identifier_rows"][k] != planted.get(k)] == ["SE2"]


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
