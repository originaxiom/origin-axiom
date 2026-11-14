"""B1919's lock: the seat's formula against main's norm at two characteristics (recomputed), the kept 24 cases, and the
rotated placement failing. It writes nothing."""
import sys, json, pathlib, warnings
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
warnings.simplefilter("ignore")
import mpmath as mp
import seat_formula as SF, step3_norm as S

import pytest


@pytest.fixture(autouse=True)
def _pin_precision():
    # 2026-11-14 (found while mending Review 82): seat_formula.py sets 20 digits at import, and in the full suite
    # tests/conftest.py restores the collection-entry precision (15) after collection, so the formula's pole subtraction
    # lost about 1.7e-4 and this lock failed in-suite while passing alone. The lock now pins its own precision; the
    # suite-wide fixture restores the global after each test.
    mp.mp.dps = 20
    yield


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
    # Review 82 (2026-11-14): the kept 24 are reproduced by a committed script, value for value, and their three points
    # lie on the golden geodesic (centre 1/2, radius sqrt(5)/2) to the four decimals they are kept to
    r = json.loads((HERE / "seat_formula_24_run.json").read_text())
    assert len(r) == 24 and [(x["tau"], x["c"]) for x in r] == [(x["tau"], x["c"]) for x in d]
    assert max(x["N vs kept"] for x in r) < 1e-12 and max(x["F vs kept"] for x in r) < 1e-12
    assert all(abs(abs(complex(*x["tau"]) - 0.5) - 5 ** 0.5 / 2) < 1e-4 for x in d)
