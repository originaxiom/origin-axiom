"""The seal gates read a dated SEAL_LEDGER row by its cells from the right (2026-10-02).

Until then both gates read a row through `| date |[^|]*| path`, so a row whose description held a
"|" never reached its path cell, and the seal went unchecked: B1506's rows ("P1 |count| = 1") were
skipped by both gates (ERROR_LEDGER, 2026-09-30 rule slip and 2026-10-02 instrument slip). These
locks feed the gates a ledger in a temporary root and assert what they read; the last two lock the
live ledger and the historical list.
"""
import hashlib
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location("gates", ROOT / "scripts" / "gates" / "gates.py")
g = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(g)

# the row pattern both gates used until 2026-10-02, kept as the control
OLD_ROW = re.compile(r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|[^|]*\|\s*`([^`]+)`")

REL = "frontier/B9001_a_seal/PREREGISTRATION.md"
UNMARKED = "# B9001 sealed\n\nP1: the count is one.\n"
MARKED = "# B9001 sealed\n\nBANKED IDENTITY: B1375's census, first.\nPRIOR ART: the design-time grep.\n"


def _sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _row(date, rel, digest, text="B9001 sealed: P1 |count| = 1 ~85%"):
    return f"| {date} | {text} | `{rel}` | `{digest}` |"


def _tree(tmp_path, monkeypatch, rows, files, historical=None):
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "SEAL_LEDGER.md").write_text("\n".join(["# ledger", ""] + rows) + "\n",
                                                      encoding="utf-8")
    for rel, text in files.items():
        (tmp_path / rel).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / rel).write_text(text, encoding="utf-8")
    monkeypatch.setattr(g, "ROOT", str(tmp_path))
    monkeypatch.setattr(g, "SEAL_PROVENANCE_HISTORICAL", historical or {})


def test_a_pipe_in_the_description_does_not_hide_the_path(tmp_path, monkeypatch):
    row = _row("2026-09-30", REL, _sha(UNMARKED))
    assert OLD_ROW.match(row) is None, "the control: the old pattern stops at the description's pipe"
    assert g._seal_ledger_rows(row) == [("2026-09-30", REL, _sha(UNMARKED))]
    _tree(tmp_path, monkeypatch, [row], {REL: UNMARKED})
    assert g.gate_seal_provenance() == (False, [REL])


def test_the_digest_gate_reads_the_same_row(tmp_path, monkeypatch):
    _tree(tmp_path, monkeypatch, [_row("2026-09-30", REL, "0" * 64)], {REL: MARKED})
    ok, detail = g.gate_seal_digests()
    assert not ok and len(detail) == 1 and detail[0].startswith(REL), detail
    (tmp_path / "docs" / "SEAL_LEDGER.md").write_text(_row("2026-09-30", REL, _sha(MARKED)) + "\n",
                                                      encoding="utf-8")
    assert g.gate_seal_digests() == (True, "ok (1 sealed digests recomputed and matching)")
    assert g.gate_seal_provenance() == (True, "ok")


def test_two_rows_joined_on_one_line_are_both_read():
    line = _row("2026-08-04", "a/one.md", "1" * 64, "B891 cell") + _row("2026-08-05", "a/two.md", "2" * 64)
    assert "` || 2026-08-05 |" in line
    assert g._seal_ledger_rows(line) == [("2026-08-04", "a/one.md", "1" * 64),
                                         ("2026-08-05", "a/two.md", "2" * 64)]


def test_rows_without_a_backticked_path_second_from_the_right_are_skipped():
    rows = [
        "| 2026-10-01 | B1507 THE RECORD REREAD: PROVED, not sealed |",
        f"| 2026-08-19 | path as prose: {REL} | — | `{'3' * 64}` |",
        "| 2026-08-05 | cc3 cell9 prereg chain 1/3 (branch) | cc3 branch cell9 | `da516046` |",
        f"| 2026-08-05 | a branch seal | cc3 branch `{REL}` | `8424a335` |",
    ]
    assert g._seal_ledger_rows("\n".join(rows)) == []
    # a path whose last cell is not a 64-hex digest is still read, for the provenance gate only
    assert g._seal_ledger_rows(f"| 2026-09-30 | d |x| | `{REL}` | `8424a335` |") == [
        ("2026-09-30", REL, None)]


def test_the_historical_list_holds_only_the_sealed_bytes_of_a_seal_before_the_fix(tmp_path, monkeypatch):
    listed = {REL: _sha(UNMARKED)}
    _tree(tmp_path, monkeypatch, [_row("2026-09-30", REL, _sha(UNMARKED))], {REL: UNMARKED}, listed)
    ok, detail = g.gate_seal_provenance()
    assert ok and REL in detail, detail
    # the listed bytes changed: the seal is flagged and the entry is reported unneeded
    (tmp_path / REL).write_text(UNMARKED + "\n", encoding="utf-8")
    ok, detail = g.gate_seal_provenance()
    assert not ok and detail[0] == REL and "SEAL_PROVENANCE_HISTORICAL lists" in detail[1], detail
    # a seal first ledgered on the fix date cannot be listed, whatever its digest
    (tmp_path / REL).write_text(UNMARKED, encoding="utf-8")
    (tmp_path / "docs" / "SEAL_LEDGER.md").write_text(
        _row(g.SEAL_ROWS_FROM_RIGHT, REL, _sha(UNMARKED)) + "\n", encoding="utf-8")
    ok, detail = g.gate_seal_provenance()
    assert not ok and detail[0] == REL, detail
    # an entry that no ledger row needs fails the gate
    (tmp_path / "docs" / "SEAL_LEDGER.md").write_text("# ledger\n", encoding="utf-8")
    ok, detail = g.gate_seal_provenance()
    assert not ok and len(detail) == 1 and REL in detail[0], detail


def test_the_live_ledger_reads_the_rows_the_old_pattern_skipped():
    text = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    read = {(d, p) for d, p, _ in g._seal_ledger_rows(text)}
    old = {m.group(1, 2) for m in map(OLD_ROW.match, text.splitlines()) if m}
    assert old <= read, "the new reading must keep every row the old one read"
    b1506 = [ln for ln in text.splitlines() if ln.startswith("| 2026-09-30 | B1506")]
    assert len(b1506) == 2 and all("|count|" in ln and not OLD_ROW.match(ln) for ln in b1506)
    assert ("2026-09-30", "frontier/B1506_the_level/PREREGISTRATION.md") in read
    assert ("2026-08-05", "frontier/B897_27_under_g20/PREREGISTRATION.md") in read - old
    ok, detail = g.gate_seal_provenance()
    assert ok and "frontier/B1506_the_level/PREREGISTRATION.md" in detail, detail
    ok, detail = g.gate_seal_digests()
    assert ok, detail


def test_every_historical_seal_has_its_disposition_recorded():
    errors = (ROOT / "docs" / "ERROR_LEDGER.md").read_text(encoding="utf-8")
    ledger = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    src = (ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    assert g.SEAL_PROVENANCE_HISTORICAL, "the list exists because B1506 needs it"
    for rel, digest in g.SEAL_PROVENANCE_HISTORICAL.items():
        arc = Path(rel).parent
        arc_id = arc.name.split("_")[0]
        assert hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == digest and digest in ledger
        findings = (ROOT / arc / "FINDINGS.md").read_text(encoding="utf-8")
        assert "SEAL_PROVENANCE_HISTORICAL" in findings, f"{arc_id}: no dated FINDINGS note"
        rows = [ln for ln in errors.splitlines() if arc_id in ln and "SEAL_PROVENANCE_HISTORICAL" in ln]
        assert rows, f"{arc_id}: no ERROR_LEDGER row naming its listing"
        comment = re.search(rf"((?:[ \t]*#.*\n)+)[ \t]*\"{re.escape(rel)}\"", src)
        assert comment and arc_id in comment.group(1) and "ERROR_LEDGER" in comment.group(1), (
            f"{arc_id}: the entry needs a comment naming the arc and its ERROR_LEDGER row")
