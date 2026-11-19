"""B1962's lock: the frame-C control reproduces B1946, and frame D1 (frame C at identity E's shifted charges) deranges the
cusp mixing for every reading pair at height 30, with the leptons copying the down sector transposed.  A live run on
three of the 24 points, plus the kept run file read for the full table."""
import sys, pathlib, re
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import d1_mixing as D1


def _table(c, pts):
    D1.POINTS[:] = pts
    names = D1.install(c) if c else {"up": "up", "down": "down", "lep": "lep"}
    return D1.table(names, 30.0)


def test_live_frame_d1_deranges_and_the_control_aligns():
    saved = list(D1.POINTS)
    try:
        pts = [(Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(0), Fr(3, 5))]
        res0, _ = _table(0, pts)
        assert min(d for d, o in res0[("S", "S")]) > 1 - 1e-6            # frame C, as B1946
        for c in (2, -2):
            res, lep = _table(c, pts)
            for k in D1.PAIRS:
                assert min(d for d, o in res[k]) < 0.1, (c, k)           # some point deranged, every pair
            for r in ("S", "St"):
                assert max(t[1] for t in lep[r]) < 1e-30 and max(t[2] for t in lep[r]) < 1e-30, (c, r)
    finally:
        D1.POINTS[:] = saved


def test_the_kept_run_has_no_aligned_pair_at_height_30_for_c_plus_or_minus_2():
    run = (HERE / "d1_mixing_run.txt").read_text()
    blocks = re.split(r"^c = ", run, flags=re.M)[1:]
    assert [b.split(":")[0].strip() for b in blocks] == ["+0", "-2", "+2"]
    for b in blocks[1:]:
        for m in re.finditer(r"height 30\.0  up \S+\s+down \S+\s*: smallest diagonal \|V\| ([0-9.e+-]+)", b):
            assert float(m.group(1)) < 0.1
    c0 = blocks[0]
    assert "height 30.0  up S  down S : smallest diagonal |V| 1.000e+00, largest off-diagonal 6.277e-05" in c0
