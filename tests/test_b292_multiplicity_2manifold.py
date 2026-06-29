"""B292 lock -- WHICH 2-MANIFOLD supplies the multiplicity? The owner's 'multiplicity' is realized but TRIPARTITE:
only the fiber Sigma_{1,1} (chi=-1, monodromy phi=RL) is a literal 2-manifold; the metallic tower R^m L^m and the
filling family (1,n) are discrete sequences of 3-manifolds (arithmetic / scale). NONE supplies the N=2->N=1 chiral
datum -> wall #4 stays blocked (B277); the chiral 4d SM is a stop-gate. FIREWALLED; nothing to CLAIMS.md.
(SnapPy reproducer: sage-python frontier/B292_multiplicity_2manifold/multiplicity_2manifold.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B292_multiplicity_2manifold" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b292", _PATH)
b292 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b292)


def test_fiber_is_the_only_2manifold():
    assert b292.fiber_euler_char() == -1                       # Sigma_{1,1}: 2 - 2g - n
    assert b292.FIBER_IS_THE_2MANIFOLD
    assert b292.FIBER_MONODROMY_TRACE == 3                     # phi = RL pseudo-Anosov


def test_tower_and_fillings_are_3manifold_sequences():
    assert b292.tower_traces() == [3, 6, 11, 18, 27, 38]       # m^2 + 2
    assert b292.TOWER_ARITHMETIC_M == [1, 2]                   # B125
    assert b292.TOWER_IS_3MFLD_SEQUENCE and b292.FILLINGS_IS_3MFLD_SEQUENCE


def test_multiplicity_tripartite_no_chiral_datum():
    assert b292.MULTIPLICITY_TRIPARTITE
    assert b292.CHIRAL_DATUM_SUPPLIED is False                 # none gives N=2->N=1


def test_chiral_4d_sm_is_stop_gate_firewall():
    assert b292.CHIRAL_4D_SM_IS_STOP_GATE                      # B277 two reasons; NEEDS-SPECIALIST
    assert b292.DERIVES_SM_VALUES is False
    assert b292.verdict()
