"""B289 lock -- IS THE CP SIGN FORCED? Every hyperbolic closing of m004 (78 over |p|,|q|<=8) is chiral and obeys the
forced sign law CS(p,-q)=-CS(p,q); the amphichiral-preserving locus is empty; geometric handedness = the Q(sqrt-3)
Galois conjugation (the B285 +-pi/6 / tau swap). The closing forces A CP sign (mechanism); WHICH sign is external (the
object is CP-symmetric). FIREWALLED; nothing to CLAIMS.md.
(SnapPy reproducer: sage-python frontier/B289_cp_sign_law/cp_sign_law.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B289_cp_sign_law" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b289", _PATH)
b289 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b289)


def test_forced_sign_law_and_all_chiral():
    assert b289.N_CHIRAL == b289.N_HYPERBOLIC_CLOSINGS              # every closing breaks amphichirality
    assert b289.N_FORCED_SIGN_LAW == b289.N_HYPERBOLIC_CLOSINGS     # CS(p,-q) = -CS(p,q)
    assert b289.N_TWO_METHODS_AGREE == b289.N_HYPERBOLIC_CLOSINGS   # chern_simons vs complex_volume (mod 1/2)


def test_amphichiral_locus_empty():
    assert b289.AMPHICHIRAL_PRESERVING_CLOSINGS == []              # closing ALWAYS breaks CP
    assert b289.CUSPED_CS == 0.0                                   # the OPEN object is amphichiral


def test_handedness_is_Qsqrt_neg3_galois_conjugation():
    import sympy as sp
    args = b289.kappa_galois_flip()                               # recompute the B285 +-pi/6 flip
    assert sp.Abs(args[0]) == sp.pi / 6 and sp.Abs(args[1]) == sp.pi / 6
    assert args[0] == -args[1]                                     # the two Riley roots = the Galois sign swap
    assert b289.HANDEDNESS_IS_GALOIS_CONJUGATION


def test_sign_not_object_derivable_firewall():
    assert b289.SIGN_IS_OBJECT_DERIVABLE is False                  # which sign = external (the tau-fork)
    assert b289.DERIVES_SM_VALUES is False
    assert b289.verdict()
