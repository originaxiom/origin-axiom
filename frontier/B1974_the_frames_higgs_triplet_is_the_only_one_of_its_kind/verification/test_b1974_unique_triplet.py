"""B1974's lock: the committed runs hold each input of the proof; each check fails if an input moves (the identity breaks, the
transformation stops being constant, the stabilizer of component 0 changes, the cusp orders shift, or c_0 gains or loses a zero),
and if eta * c ever fits M_2(Gamma(2)) (the corrected claim)."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
A = (HERE / "c13_check_run.txt").read_text(); B = (HERE / "d1_facts_run.txt").read_text()
num = lambda pat, s: float(re.search(pat, s).group(1))


def test_identity_and_representation():
    assert num(r"worst relative residual over 5 tau: ([\d.e-]+)", A) < 1e-30
    assert num(r"R_T c\(tau\): residual ([\d.e-]+)", A) < 1e-30 and num(r"R_S c\(tau\): residual ([\d.e-]+)", A) < 1e-25
    rt = re.search(r"R_T = (\[\[.*?\]\])", A).group(1)
    assert rt.startswith("[['(0.707107 + 0.707107j)'")          # component 0 fixed by T with e^{i pi/4}


def test_eta_c_not_in_m2_gamma2():
    res = [float(x) for x in re.findall(r"th4\^4 ; relative residual ([\d.e-]+)", A)]
    assert len(res) == 3 and min(res) > 0.05


def test_cusp_orders_and_zeros():
    orders = [float(x) for x in re.search(r"between heights 20 and 30: \[([^\]]+)\]", B).group(1).split(",")]
    assert abs(orders[0] - 0.125) < 1e-6 and abs(orders[1] + 0.125) < 1e-6 and abs(orders[2] + 0.125) < 1e-6
    assert num(r"\|E\(\(1\+i\)/2\)\| = ([\d.e-]+)", B) < 1e-20
    assert abs(num(r"about \(1\+i\)/2: (-?[\d.e-]+)", B) - 1) < 1e-6
    assert abs(num(r"0\.62 < Im < 2\.5: (-?[\d.e-]+)", B)) < 1e-6
    assert abs(1 / 8 - 1 / 4 + 1 / 2 - (3 / 2) * 3 / 12) < 1e-15   # the valence count
