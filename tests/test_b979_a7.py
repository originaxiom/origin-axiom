"""B979 locks — A7 is load-bearing; the four-letter principle forces the object up to one bit."""
import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B979_L131_A7"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_A7_is_load_bearing():
    assert _res()["verdict"].startswith("NO")


def test_LR_and_RL_are_conjugate_but_the_based_invariant_differs():
    t = sp.symbols('tau')
    L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]])
    P = sp.Matrix([[0, 1], [1, 0]])
    assert sp.simplify(P * (L * R) * P.inv() - R * L) == sp.zeros(2, 2)

    def fp(M):
        a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
        return sp.expand(c * t**2 + (d - a) * t - b)
    assert sp.simplify(fp(L * R) - fp(R * L)) != 0, "based invariants must differ"


def test_the_golden_polynomial_carries_phi():
    t = sp.symbols('tau')
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(phi**2 - phi - 1) == 0


def test_the_positive_content_is_one_bit():
    r = _res()
    assert "SINGLE BINARY CHOICE" in r["THE_POSITIVE_CONTENT"]
    assert "UP TO ONE BIT" in r["THE_POSITIVE_CONTENT"]


def test_the_fourth_instance_is_recorded():
    assert "fourth" in _res()["fourth_instance"].lower()
    assert contains(CELL / "FINDINGS.md", "the most embarrassing of the four",
                    "would not have caught this one")
