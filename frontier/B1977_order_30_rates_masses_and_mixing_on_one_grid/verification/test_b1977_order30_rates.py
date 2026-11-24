"""B1977's lock: the committed rates hold the sealed results; each check fails if a rate leaves its rational, a count moves,
or the class count changes."""
import pathlib, json
HERE = pathlib.Path(__file__).resolve().parent
R = json.loads((HERE / "rates30_run.json").read_text())
SLOW = {("4/15", "1/30"), ("4/15", "11/30"), ("4/15", "7/10"), ("11/15", "3/10"), ("11/15", "19/30")}


def test_slow_points():
    s = [r for r in R if (r["a"], r["b"]) in SLOW]
    assert len(s) == 5
    for r in s:
        assert abs(r["up_m2m3"] - 2 / 5) < 3e-3 and abs(r["down_m2m3"] - 7 / 15) < 3e-3 and abs(r["lep_m2m3"] - 2 / 5) < 3e-3
        assert abs(r["V12"] - 3 / 5) < 3e-3 and abs(r["V23"] - 1 / 30) < 2e-3 and abs(r["V13"] - (r["V12"] + r["V23"])) < 3e-3
        assert r["diag"] > 0.999


def test_grid_and_classes():
    allr = [v for r in R for k, v in r.items() if k not in ("a", "b", "diag", "off") and v is not None]
    assert len(allr) == 864 and sum(abs(v * 60 - round(v * 60)) / 60 <= 3e-3 for v in allr) == 860
    cls = {tuple(round(r[k], 3) for k in ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")) for r in R}
    assert len(cls) == 17
    hier = lambda r: r["up_m2m3"] >= 0.1 and r["up_m1m3"] >= 0.2 and r["down_m2m3"] >= 0.1 and r["down_m1m3"] >= 0.2
    assert sum(r["diag"] >= 0.9 and hier(r) and min(r["V12"], r["V23"], r["V13"]) < 0.1 for r in R) == 30
