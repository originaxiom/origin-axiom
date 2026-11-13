"""B1921's lock: the S-shift recomputed at one case, its plant (no shift) failing, and the kept nine cases. It writes nothing."""
import sys, math, json, pathlib, warnings
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
warnings.simplefilter("ignore")
import step3_norm as S


def test_the_shift_recomputed_and_the_plant_fails():
    t = complex(0.13, 1.07); c = (0.3, 0.6)
    n = S.norm(c, t); nS = S.norm((c[1], -c[0]), -1 / t)
    assert abs(nS + 2 * math.pi * math.log(abs(t)) - n) < 1e-7
    assert abs(nS - n) > 0.1                                   # planted: the end not shifted


def test_the_kept_cases():
    d = json.loads((HERE / "s_shift.json").read_text())
    assert len(d) == 9 and max(abs(x["residual"]) for x in d) < 5e-9 and min(abs(x["without the shift"]) for x in d) > 0.3
