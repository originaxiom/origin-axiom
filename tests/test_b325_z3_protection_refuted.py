"""B325 lock -- Chat-2's 'symmetry obstruction' (Part 2) is REFUTED. The generation Z/3 acts as the regular rep
(trivial + omega + omega^2 = three DISTINCT 1-dim irreps); the two light modes are the omega and omega^2 irreps --
DIFFERENT irreps, so no Wigner protection. A generic complex Z/3-invariant (circulant) operator SPLITS the two light
singular values; the equal magnitudes of our alpha*J + omega*P are ACCIDENTAL (|omega|=1), not Z/3-protection, and do
not transfer to the physical E6-cubic mass matrix. So a Z/3-invariant cubic CAN lift the light masses -> the CRUX does
NOT relocate to Level 4; it stays the Level-3 E6-cubic computation. (Part 1, the exact omega-circulant, stands as B324.)
Nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B325_z3_protection_refuted" / "z3_protection_refuted.py"
_spec = importlib.util.spec_from_file_location("b325", _PATH)
b325 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b325)


def test_light_modes_are_different_irreps():
    assert b325.LIGHT_MODES_ARE_DIFFERENT_IRREPS                   # omega, omega^2 -- no Wigner protection


def test_z3_invariant_splits_light():
    assert b325.generic_z3_invariant_splits_light()               # generic complex circulant splits
    assert b325.Z3_INVARIANT_CAN_SPLIT_LIGHT


def test_overlap_degeneracy_is_accidental():
    assert b325.overlap_light_magnitudes() == [1.0, 1.0]          # equal, but from |omega|=1
    assert b325.OVERLAP_DEGENERACY_IS_ACCIDENTAL
    assert b325.OVERLAP_NOT_THE_PHYSICAL_MASS


def test_crux_stays_level3():
    assert b325.CHAT2_OBSTRUCTION_REFUTED
    assert b325.CRUX_STAYS_LEVEL3_NOT_RELOCATED
    assert b325.DERIVES_SM_VALUES is False
    assert b325.verdict()
