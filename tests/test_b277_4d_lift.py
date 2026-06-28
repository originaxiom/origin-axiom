"""B277 locks -- wall #4 (4d lift) characterized: the figure-eight's fiber Sigma_{1,1} gives a CANONICAL class-S
4d N=2* SU(2) theory (monodromy phi=RL in SL(2,Z)=S-duality), but a chiral 4d SM is blocked by two NAMED missing
inputs -- the N=2->N=1 reduction datum (chirality, wall #3) and the free type G (the CRUX). A first-class
input-required result. FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B277_4d_lift_obstruction" / "b277_4d_lift.py"
_spec = importlib.util.spec_from_file_location("b277", _PATH)
b277 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b277)


def test_verdict():
    assert b277.verdict()


def test_fiber_and_monodromy():
    assert b277.fiber_euler_char() == -1            # Sigma_{1,1}
    M, tr, det = b277.monodromy()
    assert M == (2, 1, 1, 1) and tr == 3 and det == 1   # phi = R*L in SL(2,Z)
    assert b277.is_pseudo_anosov()                  # |trace| > 2


def test_lift_is_n2_and_two_missing_inputs():
    assert b277.lift_is_n2_nonchiral()              # canonical lift is N=2 (non-chiral)
    assert set(b277.MISSING_INPUTS) == {"n2_to_n1_datum", "type_G"}   # the two named obstructions
