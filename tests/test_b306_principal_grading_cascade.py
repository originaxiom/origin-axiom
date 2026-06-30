"""B306 lock -- the principal-grading cascade of E6: forced pseudo-Levi chain E6 -> SU(6)xSU(2) -> SU(3)^3 ->
SU(3)^2xSU(2) -> SU(3)xSU(2)xSU(2)xU(1)^2 (left-right, N=5, contains SM) -> SU(2)^3. The SM-shaped point is the N=5
left-right group (SM = break SU(2)_R, external); Chat-1's dim-14 window matches no clean centralizer; the saddle is
SU(2)^3, NOT SU(3)xU(1)^4 (refuted 3rd time). FIREWALLED; nothing to CLAIMS.md.
(E6 cascade Sage-verified; sage-python frontier/B306_principal_grading_cascade/principal_grading_cascade.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B306_principal_grading_cascade" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b306", _PATH)
b306 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b306)


def test_forced_cascade_counts():
    assert b306.mod_count(3) == 9 and b306.mod_count(5) == 5 and b306.mod_count(6) == 3
    assert b306.CASCADE[3][0] == [3, 3, 3] and b306.CASCADE[6][0] == [1, 1, 1]


def test_sm_shaped_point_is_n5_left_right():
    assert b306.SM_SHAPED_POINT_IS_N5
    assert b306.CASCADE[5][0] == [1, 1, 3]               # SU(3) x SU(2) x SU(2) x U(1)^2
    assert b306.SM_IS_EXACT_ENDPOINT is False            # SM = break SU(2)_R + project U(1) (external)


def test_chat1_claims_refuted():
    assert b306.CHAT1_DIM14_WINDOW_MATCHES_NO_CENTRALIZER
    assert b306.SADDLE_IS_SU2_CUBED_NOT_SU3U1_4          # 3rd refutation


def test_firewall():
    assert b306.CASCADE_IS_GENERIC_E6                    # standard Borel-de Siebenthal
    assert b306.N5_LEVEL_COINCIDENCE_IS_LEAP
    assert b306.DERIVES_SM_VALUES is False
    assert b306.verdict()
