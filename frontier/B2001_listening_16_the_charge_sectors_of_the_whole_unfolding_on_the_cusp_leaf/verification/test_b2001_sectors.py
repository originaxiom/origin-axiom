"""B2001's lock: the post hoc checks rerun (fast) and the committed sector run holds the page's facts."""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_posthoc_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "halving_posthoc.py")], capture_output=True, text=True, timeout=1800).stdout
    assert out == (HERE / "halving_posthoc_run.txt").read_text()
    assert "'L': 'CRC^-1', 'R': 'C^2LC^-2', 'CLC^-1': 'C^2RC^-2'" in out
    ratios = [float(r) for r in re.findall(r"ratio ([\d.]+)", out)]
    assert len(ratios) == 6 and abs(ratios[0] - 2) < 1e-10 and abs(ratios[1] - 2) < 1e-10 and all(abs(r - 2) > 1e-3 for r in ratios[2:])


def test_sector_run_facts():
    t = (HERE / "sectors_run.txt").read_text()
    assert t.count("[W, C] = 0.0") == 7
    assert "SUMMARY G3 (W6): the neutral sector's slowest decay differs from the charged pair's at every level run: True" in t
    rows = re.findall(r"W6: q=0: dim \d+, top ([\d.]+), slowest decay ([\d.]+); q=1: dim \d+, top ([\d.]+), slowest decay ([\d.]+)", t)
    assert len(rows) == 7 and all(float(a) == 1.0 and float(c) < 0.5 and float(b) > 0.85 for a, b, c, d in rows)
    assert rows[-1][1] == rows[-2][1] == "0.986507" and rows[-1][3] == rows[-2][3] == "0.493254"
