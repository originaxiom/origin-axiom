"""B1963's lock: on frame C's code a charge-consistent reading deranges the cusp mixing high in the cusp and aligns it only
in the bulk; at tau = i the charge-consistent pair is (S, S).  A live run at a few points, the kept runs read for the
full grid, and the scripts' hashes checked against the ones recorded before their runs."""
import sys, pathlib, re, hashlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import height_window as HW


def test_live_deranged_high_and_the_control_at_i():
    for p in ((Fr(1, 5), Fr(2, 5)), (Fr(3, 7), Fr(1, 7))):
        mcc, mss, h = HW.point("0.13", "6.0", *p)
        assert mcc < 0.1 and h < 1e-6
        a = HW.point("0", "1.0", *p)
        assert a[0] == a[1]


def test_the_kept_runs_hold_the_window():
    hw = (HERE / "height_window_run.txt").read_text()
    for y in ("1.2", "1.5", "2.0", "2.5", "3.0", "4.0", "6.0", "10.0"):
        m = re.search(r"height +%s: 72 points; charge-consistent mixing aligned at +(\d+)" % re.escape(y), hw)
        assert m and int(m.group(1)) == 0, y
    for y in ("3.0", "4.0", "6.0", "10.0"):
        assert re.search(r"height +%s: 72 points; charge-consistent mixing aligned at +0, deranged at 72" % re.escape(y), hw)
    cols = (HERE / "columns_run.txt").read_text()
    assert "three orders of hierarchy (h <= 1e-3): 0 cases" in cols
    for line in cols.splitlines():
        m = re.match(r"x +\S+ height +(\S+): 72 points; aligned +(\d+)", line)
        if m and float(m.group(1)) >= 1.5: assert int(m.group(2)) == 0, line
    cc = (HERE / "conjugation_cycle_run.txt").read_text()
    for line in cc.splitlines():
        m = re.match(r"height +\S+ +order +\d+: +\d+ points, +\d+ degenerate; .*charge-consistent pairs deranged at (\d+), not at (\d+)", line)
        if m: assert int(m.group(2)) == 0, line


def test_the_scripts_are_the_ones_hashed_before_their_runs():
    import re as _re
    last = {}
    for m in _re.finditer(r"^\| `([a-z_]+\.py)` \| `([0-9a-f]{64})` \|", (HERE / "EXPECTATIONS_HASHED.md").read_text(), _re.M):
        last[m.group(1)] = m.group(2)
    assert set(last) == {"conjugation_cycle.py", "height_window.py", "columns.py"}
    for name, h in last.items():
        assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == h, name
