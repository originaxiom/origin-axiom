"""B313 lock -- three-seat cross-check: (a) the Fibonacci/(G2)_1 bridge (Face IV <-> content) is REAL but GENERIC
(c-chain SU(2)_3 9/5 -> (G2)_1 14/5 -> (E6)_1 6 exact; 27 -> (7,3)+(1,6) so "matter=anyons" refuted; E6 ⊃ G2 x SU(3)
Slansky, object part = B261); (b) the upstream "is m=1 forced?" meditation reduces to the banked no-forced-choice
program -- m=1 is the MOST-SELECTED member (K009: systole + the non-metric expansion threshold B120 + arithmeticity
{m=1,m=2}), a single seed does not choose (K013/B130), heterogeneity (two distinct seeds) makes the fork (S032-B/B131),
the open target is S032-A. Confirms the structural theorem from a 5th direction. Nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B313_fibonacci_bridge_and_no_forced_choice" / "fibonacci_bridge_and_no_forced_choice.py"
_spec = importlib.util.spec_from_file_location("b313", _PATH)
b313 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b313)


def test_fibonacci_bridge_central_charges_exact():
    assert b313.central_charge_chain() == (sp.Rational(9, 5), sp.Rational(14, 5), sp.Integer(6))
    assert b313.chain_is_exact()                                  # +1 boson then +16/5


def test_matter_equals_anyons_refuted():
    assert b313.branching_27_refutes_matter_equals_anyons()       # 27 = (7,3)+(1,6), not 7
    assert b313.MATTER_EQUALS_ANYONS_REFUTED


def test_bridge_generic_object_part_is_b261():
    assert b313.BRIDGE_IS_GENERIC and b313.OBJECT_SPECIFIC_PART_IS_B261


def test_upstream_reduces_to_no_forced_choice():
    assert b313.M1_HAS_NONMETRIC_SELECTOR                         # K009 criterion 2 (expansion threshold, B120)
    assert b313.M1_IS_MOST_SELECTED_NOT_FORCED                    # P000 stands; member contingent
    assert b313.SINGLE_SEED_DOES_NOT_CHOOSE                       # K013/B130 moduli space
    assert b313.HETEROGENEITY_MAKES_THE_FORK                      # S032-B/B131 two distinct seeds
    assert b313.S032A_THEOREM_VERSION_IS_THE_OPEN_TARGET          # the genuine open MATH target
    assert b313.DERIVES_SM_VALUES is False
    assert b313.verdict()
