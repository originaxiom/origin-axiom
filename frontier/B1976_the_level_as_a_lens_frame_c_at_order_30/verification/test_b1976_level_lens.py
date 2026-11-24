"""B1976's lock: the committed run holds the unit test, the controls, the order-30 counts and the post hoc pattern; each
assertion fails if its number moves (a planted change of a count, a tie, or the slow rate)."""
import pathlib, re, json
HERE = pathlib.Path(__file__).resolve().parent
T = (HERE / "level30_run.txt").read_text(); J = json.loads((HERE / "level30_run.json").read_text()); P = (HERE / "top_points_run.txt").read_text()


def test_unit_ties():
    assert "N =  5: {'up~up': 'k=1', 'down~down': 'k=1', 'down~lep': 'k=1 swapped', 'lep~lep': 'k=1'}" in T
    assert "'down~up': 'k=1'" in T.split("N =  6:")[1].split("\n")[0]
    assert "N = 30: {'up~up': 'k=1', 'down~down': 'k=1', 'lep~lep': 'k=1'}" in T


def test_controls_and_counts():
    assert sum(r["updown"] < 1e-30 for r in J["P6"]) == 12 and len(J["P6"]) == 24
    assert "1 - least diagonal from 0.0e+00 to 0.0e+00" in P
    assert all(r["up_one"] == 0 and r["D"] < 1e-20 for r in J["P5"])
    assert sum(r["D"] > 0.1 for r in J["P30"]) == 88 and sum(r["up_one"] > 1e-10 for r in J["P30"]) == 92
    assert sum(r["diag"] >= 0.9 for r in J["P30"]) == 96


def test_slow_two_three_mixing():
    rates = [float(x) for x in re.findall(r"V23 (\d\.\d+)", P)]
    assert len(rates) == 5 and all(0.02 < r < 0.05 for r in rates)
