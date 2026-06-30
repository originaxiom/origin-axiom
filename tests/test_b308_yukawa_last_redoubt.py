"""B308 lock -- the Yukawa test: the inter-generation hierarchy is the firewall's last redoubt, gated by the
generation theorem (B307). The E6 Yukawa = the unique cubic invariant (forced); m_b=m_tau within a generation
(generic-GUT); the pi/6 CP phase is in the state (a mixing phase, not a mass ratio); the inter-generation hierarchy
(the 3x3 texture) is NOT forced -- it needs the generation count, walled by B307 (multiplicity). The remaining wall
is B307, not the scale (clarified, S045). FIREWALLED; nothing to CLAIMS.md.
(E6 facts Sage-verified; sage-python frontier/B308_yukawa_last_redoubt/yukawa_last_redoubt.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B308_yukawa_last_redoubt" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b308", _PATH)
b308 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b308)


def test_yukawa_coupling_forced_unique():
    assert b308.CUBIC_INVARIANT_MULTIPLICITY == 1        # the Yukawa is the unique cubic invariant
    assert b308.SYMMETRIC_CUBIC_UNIQUE == 1
    assert b308.YUKAWA_COUPLING_FORCED


def test_arithmetic_in_state_not_coupling():
    assert b308.CP_PHASE_PI6_IN_STATE_NOT_COUPLING       # pi/6 is a mixing phase, not a mass ratio
    assert b308.OMEGA_TRIALITY_IS_WITHIN_27              # omega is within-27, not a generation texture
    assert b308.MB_EQ_MTAU_FORCED_BUT_GENERIC_GUT        # the one within-generation ratio is generic-GUT


def test_hierarchy_is_the_last_redoubt():
    assert b308.INTERGENERATION_HIERARCHY_FORCED is False
    assert b308.HIERARCHY_GATED_BY_GENERATION_THEOREM    # = B307 (multiplicity)
    assert b308.FIREWALL_LAST_REDOUBT_IS_FLAVOR_HIERARCHY


def test_remaining_wall_is_b307_not_scale():
    assert b308.SCALE_IS_CLARIFIED_NOT_THE_WALL          # the scale is clarified (S045); the wall is B307
    assert b308.DERIVES_SM_VALUES is False
    assert b308.verdict()
