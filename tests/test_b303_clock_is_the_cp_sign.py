"""B303 lock -- the seam/clock thread: the CP sign IS the sign of the Chern-Simons clock. The amphichiral object is
CS=0 (the CP-symmetric clock-origin); every closing has CS with a definite sign (the CP sign, B289), constant along a
fixed-orientation history; CS(1,-n)=-CS(1,n); |CS|->0 as n->inf. The one live forcing reduces to a single firewalled
identification (CS = the cosmological clock); conditional on it + the forced arrow (S045), the CP sign is internal.
The baryon magnitude stays external. FIREWALLED; nothing to CLAIMS.md.
(SnapPy reproducer: sage-python frontier/B303_clock_is_the_cp_sign/clock_is_the_cp_sign.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B303_clock_is_the_cp_sign" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b303", _PATH)
b303 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b303)


def test_cp_sign_is_sign_of_cs():
    assert b303.CUSPED_CS == 0.0                          # amphichiral = the CP-symmetric clock origin
    assert b303.CP_SIGN_IS_SIGN_OF_CS
    assert b303.AMPHICHIRAL_IS_THE_CLOCK_ORIGIN


def test_definite_arrow_and_b289_flip():
    assert b303.ladder_is_signed_and_decaying()          # CS constant-sign along a history; |CS|->0
    assert b303.DEFINITE_ARROW and b303.B289_FLIP


def test_forcing_reduced_to_two_firewalled_inputs():
    assert len(b303.FORCING_REDUCED_TO_FIREWALLED_INPUTS) == 2     # CS=clock (Alexander) + arrow forced (S045)
    assert b303.CONDITIONAL_CP_SIGN_IS_INTERNAL


def test_baryon_magnitude_external_firewall():
    assert b303.BARYON_MAGNITUDE_STILL_EXTERNAL          # eta_B from freeze-out, not the object
    assert b303.DERIVES_SM_VALUES is False
    assert b303.verdict()
