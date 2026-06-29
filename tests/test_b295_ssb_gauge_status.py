"""B295 lock -- the SSB/gauge status of the CP sign (Chat-2 adjudicated). Curie is NOT a hard wall (SSB loophole),
but the SSB 'tau-symmetric double-well potential' is ABSENT (the program's V(tau) is the modular-tau / golden /
single-well object, disjoint from the Eisenstein +-pi/6 vacua), and 'tau is gauged' is a stop-gate (B279 [LEAP]).
NET: B289 stands (the sign is external); the mechanism is open. FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B295_ssb_gauge_status" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b295", _PATH)
b295 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b295)


def test_curie_is_not_a_hard_wall():
    assert b295.CURIE_IS_A_HARD_WALL is False                  # SSB loophole -> corrects P011/B286


def test_ssb_potential_absent_wrong_tau():
    import importlib
    ssb = b295.ssb
    # CP vacua are Eisenstein (Q(sqrt-3)); V's critical points are golden (Q(sqrt5)); disjoint:
    assert ssb.vacua_disjoint_from_potential()
    crit, kinds = ssb.potential_critical_points()
    assert sorted(kinds.values()) == ["max", "min"]           # single-well, not a degenerate double-well
    assert b295.SSB_POTENTIAL_PRESENT is False


def test_tau_gauged_is_a_stop_gate():
    assert b295.TAU_GAUGED_IS_VERIFIED is False                # B279 [LEAP], NEEDS-SPECIALIST
    assert any("gauged" in g for g in b295.STOP_GATES)


def test_sign_external_mechanism_open_firewall():
    assert b295.SIGN_IS_EXTERNAL                               # B289 stands
    assert b295.SIGN_MECHANISM_ESTABLISHED is False            # neither SSB nor gauge-fixing shown in-sandbox
    assert b295.DERIVES_SM_VALUES is False
    assert b295.verdict()
