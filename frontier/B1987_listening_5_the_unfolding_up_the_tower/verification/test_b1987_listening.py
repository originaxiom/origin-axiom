"""B1987's lock: the committed run holds the two undamped arguments and the slowest decays; a third clock or a lost
alternation fails it."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent


def test_tower_spectrum():
    t = (HERE / "listen5_run.txt").read_text()
    assert "SUMMARY T1: the undamped modes' arguments over every orbit and level run (turns; 0 = the constant, 0.5 = the sign): [0.0, 0.5]" in t
    for n in (72, 648, 120, 1176):
        assert re.search(r"orbits of\s+%d \(x\d+\): undamped modes at arguments \(turns\) \[0\.0, 0\.5\]" % n, t), n
    for n in (6, 12):
        assert all("[0.0];" in l for l in t.splitlines() if re.match(r"\s+orbits of\s+%d \(" % n, l))
