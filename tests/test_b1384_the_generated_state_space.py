"""B1384 lock -- THE GENERATED STATE SPACE: the corrective handoff's load-bearing mathematics re-derived with own code.
S0 the signed state (-I = (L^2 R^-1)^2); S1 the common SL5 in E8 (the SM centraliser is exactly the structure A4 + u1_Y);
S2 the parabolic lemma; S3 one versus three is Shapiro plus Mackey on Gamma6 normal in Gamma2; S4 the Sym^4 control and its
order-5 twists on M2 (one prime here; the run record has three)."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1384_the_generated_state_space" / "verification"
_spec = importlib.util.spec_from_file_location("b1384_handoff_checks", VER / "handoff_checks.py")
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)


def test_signed_state_and_common_sl5():
    assert H.s0_signed_state() == "(L^2 R^-1)^2 = -I"
    assert H.s0b_the_swap_and_the_orientation_fork() == {"sigma": "RP", "sigma^2": "RL", "(P sigma P)^2": "LR"}
    out = H.s1_common_sl5()
    assert out == {"centraliser_roots": 20, "e6_roots": 72, "family": 6, "mixed": 12}


def test_parabolic_lemma():
    out = H.s2_parabolic_lemma(trials=20)
    assert out["X cancels"] is True


def test_one_versus_three_is_shapiro_and_mackey():
    out = H.s3_shapiro_mackey(want_firing=2, want_quiet=6)
    assert out["with I != 0"] >= 2 and out["unipotent T^3 != 1 with (T^3-1)^2 = 0"] >= 1


def test_sym4_order5_twists_have_index_zero():
    H.PRIMES = (601,)
    rows = H.s4_sym4_twists()
    assert rows[601]["Sym4 untwisted I"] == 0
    assert rows[601]["twists"] == [((0, 1, 1, 2, 1), (0, 1, 1, 2, 1), 0)]
