"""B1794 -- the object's bundles on the frame of the right parity.  The committed runs: every listed hyperbolic closed filling of
m004 has H^2(X;Q) = H^4(X;Q) = 0; the cusped frame has one relative class (H^2_c = Q pairing with H^4 = Q); the grid of 184
fillings has H1 = Z/|p| with b1 > 0 only at the Sol slope; the integral H^2 of a closed frame is torsion; on m003 the only
b1 > 0 slope is the volume-0 fibre boundary; the Sym2 bundle is trivial on PSL."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1794_the_objects_bundles_on_the_frame_of_the_right_parity" / "verification"


def test_no_rational_class_on_the_closed_frames():
    run = (V / "cohomology_run.txt").read_text(encoding="utf-8")
    assert "every listed hyperbolic filling has H^2(X;Q) = H^4(X;Q) = 0: True" in run
    assert "hyperbolic fillings with b1(M) > 0 among those listed: 0" in run
    for l in run.splitlines():
        if "hyperbolic=True" in l:
            assert l.rstrip().endswith("b(X) = [1, 0, 0, 2, 0, 0, 1]")


def test_the_cusped_frame_has_one_relative_class():
    run = (V / "cohomology_run.txt").read_text(encoding="utf-8")
    assert "X = M x SO(3), rational Betti b0..b6: [1, 1, 0, 1, 1, 0, 0]" in run
    assert "b^c_0..b^c_6: [0, 0, 1, 1, 0, 1, 1]" in run


def test_the_referee():
    chk = (V / "referee" / "check_run.txt").read_text(encoding="utf-8")
    assert "grid fillings checked: 184" in chk and "failures: []" in chk
    assert "non-geometric solution types on grid: [(-4, 1), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 0), (1, 1), (2, 1), (3, 1), (4, 1)]" in chk
    for m in re.finditer(r"closed filling H1=Z/(\d+):  H\^2\(X;Z\) = \((\d+), \[([0-9, ]*)\]\)", chk):
        assert m.group(2) == "0" and sorted(int(t) for t in m.group(3).split(",")) == sorted([2, int(m.group(1))])
    assert "cusped m004: H^2(X;Z) = (0, [2])  H^4(X;Z) = (1, [])" in chk
    m003 = (V / "referee" / "m003_run.txt").read_text(encoding="utf-8")
    assert "b1>0 slopes on grid: [(-1, 2)]" in m003 and "volume: 0" in m003
    triv = (V / "referee" / "triv_run.txt").read_text(encoding="utf-8")
    assert "Sym2: phi invariant: True  PSL-well-defined: True" in triv
    for f in V.rglob("*"):
        if f.is_file():
            t = f.read_text(encoding="utf-8", errors="replace")
            assert ("/" + "Users/") not in t and ("/" + "private/") not in t
