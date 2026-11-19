"""B1968's lock: the kept column runs hold 28 rows, no counterexample, and a floor of at least 0.45; the scripts are the
ones hashed before their runs; and the channel extraction reproduces the frame's coupling live (a check that can fail)."""
import sys, pathlib, re, hashlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def test_the_kept_runs():
    rows, finals = [], []
    for x in ("0", "0.13", "0.25", "0.5"):
        t = (HERE / ("reach_run_%s.txt" % x)).read_text()
        rows += [float(v) for v in re.findall(r"least max m2/m3 there ([0-9.e+-]+)", t)]
        finals += [int(v) for v in re.findall(r"COUNTEREXAMPLES \(x = [0-9.]+\): (\d+)", t)]
    assert len(rows) == 28 and min(rows) >= 0.45 and finals == [0, 0, 0, 0]


def test_the_scripts_are_the_ones_hashed():
    md = (HERE / "EXPECTATIONS_HASHED.md").read_text()
    for name in ("reach.py", "reach_column.py"):
        h = re.search(r"\| `%s` \| `([0-9a-f]{64})` \|" % re.escape(name), md).group(1)
        assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == h, name


def test_the_closed_form_with_extracted_channels_is_the_frames_coupling():
    import reach as R
    RD, Mw, Ys, *_ = R.DL.parts("0.13", 3.0, Fr(1, 5), Fr(2, 5), "up")
    S = RD["S"]; h = np.array([complex((S[0, 1] - S[1, 0]) / 2), complex((S[0, 0] - S[1, 1]) / 2j), complex((S[0, 1] + S[1, 0]) / 2j)])
    u, w = R.channels("0.13", 3.0, Fr(1, 5), Fr(2, 5), "up")
    Yf = np.array([[complex(Ys["S"][i, j]) for j in range(3)] for i in range(3)])
    assert np.abs(R.Y(h, u, w) - Yf).max() / np.abs(Yf).max() < 1e-12
