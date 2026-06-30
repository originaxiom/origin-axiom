"""B296 lock -- Arc II verification of the seam arc. The adversarial red-team returns SURVIVES on every probe (no
refutations, no firewall leaks); extended checks strengthen B287/B288/B291. The novelty audit confirms the classical
math is KNOWN with citations (claims 1,2,4a) and flags the genuinely-new connections (claims 3,4b,5) as
APPEARS-NOVEL/NEEDS-SPECIALIST; the program does not claim the math as original. Nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B296_seam_arc_verification" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b296", _PATH)
b296 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b296)


def test_redteam_all_survive_no_leaks():
    assert all(v == "SURVIVES" for v in b296.REDTEAM_VERDICTS.values())
    assert b296.N_REFUTED == 0 and b296.N_FIREWALL_LEAKS == 0


def test_extended_adversarial_checks():
    assert b296.EXTENDED_CHECKS["B288_arithmetic_up_to_12"] == 0        # 174 closings, still 0 arithmetic
    assert b296.EXTENDED_CHECKS["B291_min_volume_slope"] == (5, 1)      # min-vol stable over larger grid


def test_novelty_classical_known_connections_flagged():
    assert b296.NOVELTY["claim1_distinguished_closing"] == "KNOWN"
    assert b296.NOVELTY["claim2_arithmeticity_lost"] == "KNOWN"
    assert b296.NOVELTY["claim4a_goldman_nz_symplectic"] == "KNOWN"
    assert set(b296.NOVEL_CLAIMS_NEEDS_SPECIALIST) == {"claim3_handedness_galois",
                                                       "claim4b_clock_lambda_cstime", "claim5_seam_reframe"}
    assert b296.PROGRAM_CLAIMS_MATH_AS_ORIGINAL is False                # honest: math classical, reframe is new


def test_verdict_firewall():
    assert b296.DERIVES_SM_VALUES is False
    assert b296.verdict()
