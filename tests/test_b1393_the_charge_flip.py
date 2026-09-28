"""B1393 lock -- THE CHARGE FLIP (PROVED; cube~3.24's cuspidal twist exact).

An index formula computes net chirality only for an end condition that flips with the charge; with one condition for both charges
the net chirality is one Betti number at q and -q.  On cube~3.24's cuspidal Higgs twist L_t (t = e^q) the charge-blind count is
zero at every real coupling: a1 = r1 = 4, so no twisted class is interior (n = 0, main's I = 0), and the Fox matrix drops rank only
at the primitive cube roots of unity (determinantal divisor 9(t^2 + t + 1)^2).  On one disc in a cusp the flip gives -chi(M, D) = 1
and the blind condition 0."""
import importlib.util
import warnings
from fractions import Fraction as Fr
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1393_the_charge_flip" / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1393_charge_flip", VER / "charge_flip.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_charge_blind_count_vanishes():
    C = _load()
    P = C.Pres()
    assert P.b1 == 5
    for t in (Fr(2), Fr(3, 2)):
        x, y = P.numbers(t), P.numbers(1 / t)
        assert (x["a1"], x["r1"], x["n"]) == (4, 4, 0) and (y["a1"], y["r1"], y["n"]) == (4, 4, 0)
        assert x["r1"] + y["r1"] == x["t1"] == 8                      # the annihilator property (B1297)
        assert x["euler"] == 0


def test_the_jump_points_are_the_cube_roots_of_unity():
    import sympy as sp
    C = _load()
    r, g, fac, real_pos = C.part_B(C.Pres())
    t = sp.Symbol("x")
    assert r == 3
    assert sp.expand(sp.sympify(str(g).replace("^", "**")) - 9 * (t ** 2 + t + 1) ** 2) == 0
    assert real_pos == []                                              # no real coupling is special


def test_flip_against_blind_on_a_disc():
    C = _load()
    assert C.part_C(C.Pres()) == (1, 0)                                # -chi(M, D) = 1 with the flip; 0 without
