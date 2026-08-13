"""B1063 locks -- the refresh verdict: the eight misses, the clause, the closure."""
import pathlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1063_refresh_verdict"


def test_window_log_pins_the_misses():
    log = (ARC / "refresh_windows.log").read_text()
    assert "MISS by 44 deg (240 vs [157,196])" in log
    assert "MISS by 2 deg (240 vs [171,238])" in log
    assert "MISS by 9 deg (240 vs [249,296])" in log
    assert "MISS by 17 deg (240 vs [257,310])" in log
    assert "HIT" not in log.replace("...", "")
    assert "2.21x" in log


def test_findings_closure_discipline():
    f = " ".join((ARC / "FINDINGS.md").read_text().split())
    assert "eight misses" in f.lower() or "Eight window-target pairs, eight misses" in f
    assert "CONFIRMED-DECISIVE" in f
    assert "SPENT" in f                        # the one-shot discipline
    assert "NEW arc under a NEW seal" in f     # no standing re-armed window
    assert "fetch-currency defect" in f        # the trigger's own finding
    assert "not as encouragement" in f         # the 2-degree fence
    assert "NEGATIVE" in f
