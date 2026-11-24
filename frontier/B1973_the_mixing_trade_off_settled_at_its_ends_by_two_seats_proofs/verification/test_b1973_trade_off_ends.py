"""B1973's lock: the committed runs hold the page's numbers; each check fails if the ceiling moves off (1+s)/(3-s), the residues
stop being rank one or stop sharing a left spinor, the weighted s_L rises past 2/5, or the witness loses its alignment or its
hierarchy."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent


def test_ceiling():
    t = (HERE / "t3_check_run.txt").read_text()
    for line in [l for l in t.splitlines() if l.startswith("order ") and "[(" in l]:
        for s, got, want in re.findall(r"\(([\d.]+), np\.float64\(([\d.]+)\), ([\d.]+)\)", line):
            assert abs(float(got) - float(want)) < 1e-4, (s, got, want)
            assert abs(float(want) - (1 + float(s)) / (3 - float(s))) < 1e-5


def test_shared_left_spinor():
    t = (HERE / "t4b_check_run.txt").read_text()
    m = re.search(r"unweighted residues: 60 cases; max mu2/mu1 = ([\d.e-]+); max s_L = ([\d.e-]+)", t)
    assert float(m.group(1)) < 1e-30 and float(m.group(2)) < 1e-15
    w = float(re.search(r"weighted M_w \(frame C\): 60 cases;\s+max s_L = ([\d.]+)", t).group(1))
    assert w < 0.4 and (1 + w) / (3 - w) < 0.54


def test_witness():
    t = (HERE / "c1_witness_run.txt").read_text()
    a = [l for l in t.splitlines() if l.startswith("(a)")][0]
    diag = float(re.search(r"least diagonal \|V\| ([\d.]+)", a).group(1)); off = float(re.search(r"largest off-diagonal ([\d.e-]+)", a).group(1))
    nums = [float(x) for x in re.findall(r"m\d/m\d ([\d.e-]+)", a)]
    assert diag > 0.999999 and off < 1e-40
    assert nums[0] <= 1e-2 and nums[1] <= 0.1 and nums[2] <= 1e-2 and nums[3] <= 0.1
