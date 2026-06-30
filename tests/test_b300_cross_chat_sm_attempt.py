"""B300 lock -- the cross-chat SM-from-axiom attempt, assessed: Column B collapses to TWO walls (the coupling/action
category + the degree-3 carrier), and three independent seats (the seam arc + Chat-1 + Chat-2) converge on the
structural theorem. Verified arithmetic: E6+A2->E8 prime-3 glue (9/9=1); scale = one rod l_P. The one live forcing
(CP-sign clock gauge-fixing) is triple-convergent. FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B300_cross_chat_sm_attempt" / "cross_chat_sm_attempt.py"
_spec = importlib.util.spec_from_file_location("b300", _PATH)
b300 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b300)


def test_column_b_collapses_to_two_walls():
    assert b300.N_COLUMN_B_WALLS == 2
    assert set(b300.COLUMN_B_WALLS) == {"A_coupling_action_category", "B_degree3_carrier"}


def test_e6_a2_e8_prime3_glue():
    assert b300.e6_a2_e8_prime3_glue()                  # det(E6)*det(A2)/3^2 = 1 = det(E8)


def test_scale_one_rod():
    assert abs(b300.ldS_over_lP(3) - 0.3989) < 1e-3     # k=3 -> ~0.40 (no hierarchy at origin)
    assert b300.ldS_over_lP(6.6e122) > 1e60             # k~1e122 -> the Planck-cosmic gap


def test_convergence_and_live_forcing_firewall():
    assert b300.SEATS_CONVERGE_ON_STRUCTURAL_THEOREM
    assert b300.LIVE_FORCING_TRIPLE_CONVERGENT          # B295 + Chat-1 + Chat-2 all name it
    assert b300.DERIVES_SM_VALUES is False
    assert b300.verdict()
