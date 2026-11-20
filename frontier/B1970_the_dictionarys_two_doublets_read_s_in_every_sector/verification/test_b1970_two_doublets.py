"""B1970's lock: re-run the checks and hold their decisive lines; and a control that can fail: if the up operator used
the same 10-states as the down operator (one doublet), D2's disjointness line would read False."""
import sys, pathlib, subprocess
HERE = pathlib.Path(__file__).resolve().parent


def test_the_checks_rerun_and_hold():
    out = subprocess.run([sys.executable, "-B", str(HERE / "two_doublets.py")], capture_output=True, text=True, cwd=HERE).stdout
    assert out.strip() == (HERE / "two_doublets_run.txt").read_text().strip()
    assert "D1: the 10's hypercharges: [(Fraction(-1, 2), 2), (Fraction(-1, 3), 3), (Fraction(1, 3), 3), (Fraction(1, 2), 2)]" in out
    assert "the up operator's 10-states and the down operator's are disjoint: True; the down and lepton operators share theirs: True" in out
    assert out.count("D3: the frame's") == 3 and all(l.endswith("True") for l in out.splitlines() if l.startswith("D3:"))
    assert "smallest diagonal |V| 1.000000" in out


def test_the_holomorphy_lines_separate_the_readings():
    out = (HERE / "two_doublets_run.txt").read_text()
    import re
    ratios = [float(x) for x in re.findall(r"= ([0-9.]+e-\d+)", " ".join(l for l in out.splitlines() if l.startswith("D4")))]
    assert ratios and max(ratios) < 1e-15
