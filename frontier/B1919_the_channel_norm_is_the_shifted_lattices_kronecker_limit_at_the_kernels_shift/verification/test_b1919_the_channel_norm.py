"""B1919's lock: the seat's formula against main's norm at two characteristics (recomputed), the kept 24 cases, and the
rotated placement failing. It writes nothing."""
import sys, json, pathlib, warnings
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
warnings.simplefilter("ignore")
import mpmath as mp
import seat_formula as SF, step3_norm as S

T = complex(0.5, 1.1180339887498949); TAU = mp.mpc(T.real, T.imag)
C = -2 * mp.pi * (mp.euler + mp.log(mp.pi))


def rhs(u1, u2):
    return float(SF.F(u1, u2, TAU) + mp.pi * mp.log(TAU.imag) + C)


def test_the_formula_holds_and_the_rotation_fails():
    for c in [(0.3, 0.6), (0.7, 0.2)]:
        n = S.norm(c, T)
        assert abs(n - rhs(c[0] - .5, c[1] - .5)) < 1e-6
        assert abs(n - rhs(c[1] - .5, -(c[0] - .5))) > 1.0           # planted: the rotated shift


def test_the_kept_cases():
    d = json.loads((HERE / "seat_formula_check.json").read_text())
    assert len(d) == 24 and max(x["diff"] for x in d) < 1e-6 and len({tuple(x["tau"]) for x in d}) == 3
