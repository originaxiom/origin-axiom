"""B254 locks -- the uniqueness chain & chain merger: conformal-embedding tower (E6)_1 ⊃ SU(3)_2 x SU(2)_3 x U(1)
closes at c=6; (G2)_1=Fibonacci hosts the golden SU(2)_3 (the B204 merger); McKay fields corrected. FIREWALLED
(arithmetic/CFT, not physics); nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B254_uniqueness_chain" / "uniqueness_chain.py"
_spec = importlib.util.spec_from_file_location("b254", _PATH)
b254 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b254)


def test_level1_central_charges():
    assert b254.c_level1(*b254.EXC["E6"]) == 6
    assert b254.c_level1(*b254.EXC["G2"]) == sp.Rational(14, 5)
    assert b254.c_level1(*b254.EXC["E8"]) == 8


def test_conformal_tower_closes():
    ok, cE6 = b254.conformal_tower_closes()
    assert ok and cE6 == 6
    # SU(3)_2 x (G2)_1 conformal embedding
    assert b254.c_su3(2) + b254.c_level1(*b254.EXC["G2"]) == 6


def test_chain_merger_g2_is_fibonacci_hosts_su2_3():
    ok, cG2 = b254.g2_is_fibonacci_and_hosts_su2_3()
    assert ok and cG2 == sp.Rational(14, 5)
    assert b254.c_su2(3) == sp.Rational(9, 5)


def test_mckay_fields_corrected():
    # the spine + the handoff's "other fields" correction
    assert b254.MCKAY["2T"] == (24, "E6", "Q(sqrt-3)")
    assert b254.MCKAY["2O"][2] == "Q(sqrt2)"      # E7, NOT Q(sqrt-1)/Q(sqrt-2)
    assert b254.MCKAY["2I"][2] == "Q(sqrt5)"      # E8, NOT Q(sqrt-7)


def test_amphicheiral_z2_grading():
    # Sage-verified branchings (recorded): 27 = 1 + 26, 78 = 26 + 52
    assert b254.F4_BRANCH["27"] == ("1", "26")
    assert b254.F4_BRANCH["78"] == ("26", "52")
