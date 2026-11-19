"""B1965's lock: the kept runs hold no counterexample (no BEST objective below -2; no aligned triplet with both heavy-pair
ratios below 1e-2 in the scan), and a structural check that can fail: a real Higgs triplet makes the two readings one,
so its charge-consistent mixing equals its same-reading mixing."""
import sys, pathlib, re
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def test_the_kept_runs_hold_no_counterexample():
    adv = (HERE / "adversary_run.txt").read_text()
    best = [float(x) for x in re.findall(r"BEST objective (-?[0-9.]+)", adv)]
    assert len(best) == 4 and min(best) > -2
    scan = (HERE / "scan_run.txt").read_text()
    counts = re.findall(r"aligned with both <= 1e-2: (\d+)", scan)
    assert len(counts) == 3 and all(int(c) == 0 for c in counts)


def test_a_real_higgs_makes_the_two_readings_one():
    import scan as SC
    h = [0.3, -0.8, 0.52]
    with SC.const_higgs(h):
        Yu = SC.DL.parts("0.13", 3.0, Fr(1, 5), Fr(2, 5), "up")[2]
    d = max(abs(Yu["S"][i, j] - Yu["St"][i, j]) for i in range(3) for j in range(3)) / max(abs(Yu["S"][i, j]) for i in range(3) for j in range(3))
    assert float(d) < 1e-25
    hc = [0.3, -0.8j, 0.52]
    with SC.const_higgs(hc):
        Yc = SC.DL.parts("0.13", 3.0, Fr(1, 5), Fr(2, 5), "up")[2]
    assert float(max(abs(Yc["S"][i, j] - Yc["St"][i, j]) for i in range(3) for j in range(3))) > 1e-3
