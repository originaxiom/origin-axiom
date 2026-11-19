"""B1964's lock: the lemma's algebra (exact) and its cusp limit on frame C's code at a few points; the kept grid run read
for K1 and K2; the grid script checked against the hash recorded before its run."""
import sys, pathlib, re, hashlib, subprocess
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def test_the_lemma_holds_exactly():
    out = subprocess.run([sys.executable, str(HERE / "lemma.py")], capture_output=True, text=True, cwd=HERE).stdout
    assert out.strip() == (HERE / "lemma_run.txt").read_text().strip()
    assert "L1: u^H Y(E12) = Matrix([[0], [0], [0]])" in out and "L2: u^H Y(E21) = Matrix([[0], [0], [0]])" in out
    assert "L3: <u_S, u_S~> = 0" in out and "[True, True, True]" in out and "L5: S = 2 c1 E12: True; its conjugate reading = -2 conj(c1) E21: True" in out
    assert "requires: [{b: 0, d: 0}]" in out


def test_live_light_directions_at_three_points():
    import light_directions as LD
    for (a, b) in ((Fr(1, 5), Fr(2, 5)), (Fr(3, 7), Fr(1, 7)), (Fr(2, 9), Fr(5, 9))):
        for sec in ("up", "down", "lep"):
            RD, Mw, Ys, u, cs, ds = LD.DL.parts("0.13", 30.0, a, b, sec)
            assert 1 - float(abs((LD.uS.H * LD.CM.U_of(Ys["S"])[:, 0])[0])) < 1e-10
            assert 1 - float(abs((LD.uSt.H * LD.CM.U_of(Ys["St"])[:, 0])[0])) < 1e-10


def test_the_kept_grid_run():
    run = (HERE / "light_directions_run.txt").read_text()
    assert not re.search(r"rank 2, +no match", run)
    assert sum(int(n) for n in re.findall(r"rank 2, +match +: (\d+)", run)) == 574
    assert "largest |S[1,0]/S[0,1]| at height 30: 2.34e-40" in run


def test_the_grid_script_is_the_one_hashed():
    h = re.search(r"\| `light_directions.py` \| `([0-9a-f]{64})` \|", (HERE / "EXPECTATIONS_HASHED.md").read_text()).group(1)
    assert hashlib.sha256((HERE / "light_directions.py").read_bytes()).hexdigest() == h
