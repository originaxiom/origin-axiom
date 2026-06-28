"""B279 lock -- the amphicheiral tau of 4_1 FIXES (does not swap) its 2 spin structures. Topology; the physics
reading is firewalled and rests on an unverified link. FIREWALLED; nothing to CLAIMS.md.
(Heavy SnapPy inputs reproduced by sage-python spin_structure_bit_snappy.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B279_spin_structure_bit" / "spin_bit_verdict.py"
_spec = importlib.util.spec_from_file_location("b279", _PATH)
b279 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b279)


def test_two_spin_structures():
    assert b279.N_SPIN_STRUCTURES == 2


def test_bit_is_fix():
    assert b279.BIT == "FIX"
    assert b279.IS_AMBIENT and b279.HOMOLOGICAL_ACTION_TRIVIAL
    assert b279.verdict()


def test_physics_link_is_firewalled_not_claimed():
    assert b279.PHYSICS_LINK_VERIFIED is False     # the fix->non-chiral-vacuum reading is NOT banked
