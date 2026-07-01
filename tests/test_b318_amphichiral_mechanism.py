"""B318 lock -- the amphichiral involution tau (= complex conjugation, fig-8 amphichiral CS=0) is the GEOMETRIC firewall
mechanism for the EISENSTEIN end: it is the Galois auto of the imaginary trace field Q(sqrt-3) (sqrt-3->-sqrt-3), so it
symmetrizes the CP sign +/-pi/6 (B285), CS, and all Q(sqrt-3) data (deepens B285). But tau FIXES the real golden field
Q(sqrt5), so B314's golden Galois (sqrt5->-sqrt5, colored Jones) is arithmetic-only, no geometric involution. So Chat-1's
'tau symmetrizes ALL invariants' overclaimed the golden end; the two ends have two DIFFERENT mechanisms (geometric +
arithmetic), refining K020/B314. Also absorbs Chat-2's correct B311 catch (the golden discriminant factor is the
definitional monodromy eigenvalue). Firewalled; nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B318_amphichiral_mechanism" / "amphichiral_mechanism.py"
_spec = importlib.util.spec_from_file_location("b318", _PATH)
b318 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b318)


def test_tau_is_galois_of_eisenstein_trivial_on_golden():
    assert b318.tau_is_galois_of_eisenstein()                      # conj(sqrt-3) = -sqrt-3, nontrivial
    assert b318.tau_is_trivial_on_golden()                        # conj(sqrt5) = sqrt5, trivial
    assert b318.tau_action_on(sp.sqrt(-3))[0] == -sp.sqrt(-3)


def test_amphichirality_covers_eisenstein_deepens_b285():
    assert b318.TAU_IS_COMPLEX_CONJUGATION
    assert b318.AMPHICHIRALITY_COVERS_EISENSTEIN
    assert b318.DEEPENS_B285_CP_SIGN_IS_GEOMETRIC


def test_golden_arithmetic_only_chat1_overclaimed():
    assert b318.GOLDEN_END_IS_ARITHMETIC_ONLY
    assert b318.CHAT1_RESULT3_OVERCLAIMED_GOLDEN
    assert b318.TWO_ENDS_TWO_DIFFERENT_MECHANISMS


def test_absorbs_b311_correction():
    assert b318.B311_GOLDEN_FACTOR_IS_DEFINITIONAL               # Chat-2: x^2-3x+1 = monodromy eigenvalue quadratic
    assert b318.DERIVES_SM_VALUES is False
    assert b318.verdict()
