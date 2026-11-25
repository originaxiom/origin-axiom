"""B2003's lock: the committed run holds the reach table (the full run takes about 13 minutes and is not rerun here; its
fast levels are rerun exactly through the same code)."""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_reach_table():
    t = (HERE / "reach_run.txt").read_text()
    rows = re.findall(r"mod +(\d+): orbit +(\d+) points, C-fixed (\d); (EXACT|NUMERIC).*?: (True|False);", t)
    got = {int(N): (int(n), int(f), s == "True") for N, n, f, _, s in [(r[0], r[1], r[2], r[3], r[4]) for r in rows]}
    assert {N: (n, f) for N, (n, f, _) in got.items()} == {9: (8, 2), 27: (72, 3), 81: (648, 3), 243: (5832, 3), 25: (1000, 1), 49: (1372, 1), 15: (40, 1), 45: (320, 2)}
    assert all(ok == (f == 3) for (n, f, ok) in got.values())   # R4: holds exactly where C fixes three points
    assert "paired by halving (multiplicity-aware) 215; charged-sector degree 215" in t and "paired by halving 1943; charged-sector dimension 1943" in t


def test_fast_levels_rerun():
    code = (HERE / "reach.py").read_text().replace("for N in (9, 27, 81, 243, 25, 49, 15, 45):", "for N in (9, 27, 15):")
    out = subprocess.run([sys.executable, "-B", "-c", code.replace("HERE = pathlib.Path(__file__).resolve().parent", "HERE = pathlib.Path(%r)" % str(HERE))], capture_output=True, text=True, timeout=900).stdout
    strip = lambda s: [l.split("  [")[0] for l in s.splitlines()]
    want = [l for l in strip((HERE / "reach_run.txt").read_text()) if re.match(r"mod +(9|27|15):", l)]
    assert strip(out) == want
