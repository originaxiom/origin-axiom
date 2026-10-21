"""Review 66, R65-6 (P-123): the topic sweep's alias table. A sweep in today's words finds the record's older words for
the same subject (the known miss: B1290's "I-26 becomes a question about the cusp", FK10's question, missed by the sweeps
of B1627, B1629 and B1632); --no-aliases does not (the bite); --full is marked on the VERDICT line; and the arcs the
point named carry their late Seen addenda."""
import glob, importlib.util, io, pathlib, re, contextlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("ts", ROOT / "scripts" / "checks" / "topic_sweep.py")
ts = importlib.util.module_from_spec(spec); spec.loader.exec_module(ts)


def _run(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): ts.main(argv)
    return buf.getvalue()


def test_the_alias_finds_the_known_miss_and_the_bite():
    rx, used = ts.expand(r"cusp unit")
    assert used == ["the cusp's unit"] and re.search(rx, "I-26 becomes a question about the cusp", re.I)
    ids = [h["id"] for h in ts.sweep(rx, ts.arcs())]
    assert "B1290" in ids
    assert "B1290" not in [h["id"] for h in ts.sweep(r"cusp unit", ts.arcs())]          # the bite: without the aliases
    assert ts.expand(r"zzzz-not-there") == (r"zzzz-not-there", [])


def test_the_verdict_line_names_full_text_and_the_aliases():
    out = _run(["cusp unit", "--full", "--limit", "1"])
    assert "(full text, aliases: the cusp's unit)" in out.splitlines()[-1]
    assert "full text" not in _run(["cusp unit", "--no-aliases", "--limit", "1"]).splitlines()[-1]


def test_the_late_seen_addenda():
    for arc in ("B1627", "B1629", "B1630", "B1632", "B1633", "B1636", "B1644"):
        text = (pathlib.Path(glob.glob(str(ROOT / "frontier" / (arc + "_*")))[0]) / "FINDINGS.md").read_text(encoding="utf-8")
        assert "## Seen late (2026-10-21, Review 66; P-123)" in text, arc
