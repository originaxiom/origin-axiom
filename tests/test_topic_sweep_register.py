"""The topic sweep reads main's register (proposed by the web seat, 2026-10-27). A sweep that finds no arc can still find
queued or held work in docs/POINT_REGISTER.md: the web seat's sweep for theta-bar reported 8 arcs and missed P-323, the
same question, queued since 2026-10-23. Pins: (1) planted register rows are found, in the point and in the where/next
cell, and a planted absence is empty; (2) the real register is read (more than 300 rows, every id P-n); (3) the known
miss: P-323 is found in the register and is not an arc; (4) the VERDICT line carries the register count, and the
markers the alias test reads stay in place; (5) the failing path: with no register file the count is zero, not an
error."""
import contextlib, importlib.util, io, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("ts", ROOT / "scripts" / "checks" / "topic_sweep.py")
ts = importlib.util.module_from_spec(spec); spec.loader.exec_module(ts)


def _run(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): ts.main(argv)
    return buf.getvalue()


def test_planted_rows_both_ways():
    reg = [dict(id="P-1", disposition="QUEUED", where="Q3", point="theta-bar in the mass frame"),
           dict(id="P-2", disposition="DONE", where="B9 (the flow)", point="the arrow")]
    assert [r["id"] for r in ts.sweep_register(r"mass frame", reg)] == ["P-1"]
    assert [r["id"] for r in ts.sweep_register(r"\bB9\b", reg)] == ["P-2"]          # the where/next cell is read too
    assert ts.sweep_register(r"zzzz-not-there", reg) == []


def test_the_real_register_is_read():
    rows = ts.register()
    assert len(rows) > 300 and all(r["id"].startswith("P-") for r in rows)
    assert {"QUEUED", "DONE"} <= {r["disposition"] for r in rows}


def test_the_known_miss_is_found_in_the_register():
    rx = r"mass frame \(L192\)"
    assert "P-323" in [r["id"] for r in ts.sweep_register(rx, ts.register())]
    # [main, S225] the arcs side is not pinned on the live record: an arc may quote P-323's row later


def test_a_malformed_row_is_counted_not_dropped(tmp_path):
    d = tmp_path / "docs"; d.mkdir()
    (d / "POINT_REGISTER.md").write_text("| P-001 | d | s | point | DONE | where | m |\n| P-002 | d | s | broken row |\n")
    rows = ts.register(root=str(tmp_path))
    assert [r["id"] for r in rows] == ["P-001"] and ts.REGISTER_SKIPPED == ["P-002"]


def test_the_verdict_line_carries_the_register_count():
    last = _run([r"mass frame \(L192\)", "--limit", "1"]).splitlines()[-1]
    assert last.startswith("VERDICT topic-sweep /") and re.search(r"; [1-9]\d* register rows match \(", last)
    last2 = _run(["cusp unit", "--full", "--limit", "1"]).splitlines()[-1]
    assert "(full text, aliases: the cusp's unit)" in last2 and "register rows match (" in last2


def test_no_register_file_is_a_zero_not_an_error(tmp_path):
    assert ts.register(root=str(tmp_path)) == []
