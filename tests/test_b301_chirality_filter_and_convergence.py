"""B301 lock -- the E6 chirality filter (corrected to a FACT, not "SO(10) forced") + the trinification connection
(the kept SU(3)^3 = the (theta,phi) triality of B299) + the three-seat convergence as a first-class finding.
FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B301_chirality_filter_and_convergence" / "chirality_filter.py"
_spec = importlib.util.spec_from_file_location("b301", _PATH)
b301 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b301)


def test_chirality_filter_keeps_three_not_one():
    assert b301.TWENTYSEVEN_IS_COMPLEX
    assert set(b301.CHIRAL_MAXIMAL_SUBGROUPS) == {"SO(10)xU(1)", "SU(6)xSU(2)", "SU(3)^3"}
    assert b301.STABILITY_FORCES_SO10 is False                    # retracted overclaim
    assert b301.CHIRALITY_IS_A_PHYSICS_SELECTION_PRINCIPLE        # chirality = mass-protection (a world-observation)


def test_su3cubed_is_the_trinification_triality():
    assert b301.SU3CUBED_IS_THE_THETA_PHI_TRIALITY               # = B299, same structure twice


def test_three_seat_convergence_first_class():
    assert len(b301.SEATS) == 3 and b301.ALL_THREE_CONVERGE
    assert b301.BOUNDARY_IS_REAL_FOUND_THREE_WAYS


def test_firewall():
    assert b301.DERIVES_SM_VALUES is False
    assert b301.verdict()
