"""B1742 -- TWO_HIGGS verified on main (P-351), PROVED.  Live: the web seat's best six-row recomputed on main's B1740
instrument with a per-sector Higgs (H_u = F_6, H_d = F_22, all S, c = 3 at 0.5625 + 2.6i on (2/5, 1/10), L_2: chi2_six
1.188, D = 9); the lepton-down identity on an even-k line for a random Higgs, and its failure off alpha = 2/5.  Stored:
the control and the grid's minima."""
import importlib.util, json, math, pathlib
from fractions import Fraction as Fr
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1742_two_higgs_verified_on_main"


def _r():
    spec = importlib.util.spec_from_file_location("b1742_repro", A / "verification" / "repro.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m


def test_stored():
    d = json.loads((A / "verification" / "repro.json").read_text(encoding="utf-8"))
    assert d["control"]["max_dln_against_B1740"] < 1e-9
    assert abs(d["best_six F6|F22"]["chi2_six"] - 1.1884) < 1e-3
    s = (A / "verification" / "scan_run.txt").read_text(encoding="utf-8")
    assert "rows below 16.75: 14 pairs [(6, 22)]" in s and "'chi2_nine': 154.136" in s


def test_best_six_row_live():
    R = _r(); r = R.readout(R.compute2(0.5625, 2.6, Fr(2, 5), Fr(1, 10), 6, 22, "L_2"))
    assert abs(r["chi2_six"] - 1.1884) < 1e-3 and abs(math.log(r["D"] / 9)) < 1e-6 and r["worst_six"] < 1.1


def test_lepton_down_identity_live():
    """on (2/5, 2/10) the lepton spectrum is the down spectrum for any Higgs; on (1/7, 3/7) it is not (planted contrast)"""
    R = _r(); rng = np.random.default_rng(1742); h = list(rng.normal(size=3) + 1j * rng.normal(size=3))

    def spectra(a, b, re_t, im_t):
        orig = R.direction
        R.direction = lambda _a, _t: h
        try:
            out = R.compute2(re_t, im_t, a, b, 0, 0, "L_2")
        finally:
            R.direction = orig
        return out["down"], out["lep"]
    d, l = spectra(Fr(2, 5), Fr(2, 10), 0.3, 2.4)
    assert max(abs(math.log(x / y)) for x, y in zip(d, l)) < 1e-9
    d, l = spectra(Fr(1, 7), Fr(3, 7), 0.8, 3.1)
    assert max(abs(math.log(x / y)) for x, y in zip(d, l)) > 0.1
