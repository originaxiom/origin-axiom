"""B1918's lock: the fit sees an exact Kronecker relation when it is planted, and does not see one in the channel norm;
the kept average run says the same. It writes nothing."""
import sys, json, math, pathlib, warnings
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
warnings.simplefilter("ignore")
import numpy as np
import step3_norm as S

T = complex(0.5, 1.1180339887498949)
CH = [(0.1, 0.0), (0.1, 0.6), (0.3, 0.2), (0.3, 0.8), (0.5, 0.1), (0.6, 0.4), (0.7, 0.2), (0.8, 0.7), (0.9, 0.3), (0.4, 0.9)]


def test_a_planted_kronecker_relation_is_recovered():
    A = np.array([S.features(c, T) for c in CH]); fake = A @ np.array([-4 * math.pi, 2 * math.pi, -3.0])
    co, *_ = np.linalg.lstsq(A, fake, rcond=None)
    assert abs(fake - A @ co).max() < 1e-10 and abs(co[0] + 4 * math.pi) < 1e-8


def test_the_channel_norm_is_not_of_the_kronecker_form():
    y = np.array([S.norm(c, T) for c in CH]); A = np.array([S.features(c, T) for c in CH])
    co, *_ = np.linalg.lstsq(A, y, rcond=None)
    assert abs(y - A @ co).max() > 5.0                     # a real relation would leave ~1e-9


def test_the_kept_average_run():
    d = json.loads((HERE / "step3_average.json").read_text())
    assert len(d["chars"]) == 30 and d["max_residual"] > 10.0
    page = " ".join((HERE.parent / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "residual of 29 on a spread of 177" in page and "%.0f" % d["max_residual"] == "29"
