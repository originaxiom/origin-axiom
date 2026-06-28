"""B252 locks -- adjudication of the Chat-2 chirality obstruction: the obstruction holds (every conjugation-odd
structure is symmetric), but it is universal (not m-specific) and its rep-theory link is an analogy. FIREWALLED
(rep theory/topology, not physics); nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B252_chirality_obstruction" / "chirality_obstruction.py"
_spec = importlib.util.spec_from_file_location("b252", _PATH)
b252 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b252)


def test_lens_L52_is_amphichiral():
    # L(5,2) amphichiral: 2^2 = -1 mod 5; consistent with 4_1 amphicheiral
    assert b252.lens_is_amphichiral(5, 2)
    # control: L(5,1) is NOT amphichiral (1^2=1 != -1 mod 5)
    assert not b252.lens_is_amphichiral(5, 1)


def test_spherical_cs_values_pair_under_conjugation():
    assert b252.cs_values_pair_under_conjugation(5, 2)


def test_could_not_break_the_obstruction():
    # every object-intrinsic conjugation-odd structure is symmetric -> obstruction holds
    cands = b252.break_it_candidates()
    assert all(cands.values())
    assert len(cands) == 5


def test_all_four_steps_verified():
    # chat-2 right on all four steps; Step 3 (amphicheirality = E6 outer aut = 27<->27bar) is banked H36
    assert b252.E6_27_IS_COMPLEX and b252.E6_78_IS_REAL and b252.E8_DECOMP_PAIRS_27
    assert b252.STEP3_BANKED_AS_H36


def test_precision_amphichirality_universal():
    # the bare property is universal across metallic m (the E6/27<->27bar realization is m=1-specific)
    assert b252.amphichirality_is_universal_not_specific()
