"""B143 -- Campaign-1 feasibility scope. Algebraic parts unconditional; topological/588 via importorskip."""
import pytest

from frontier.B143_interaction_feasibility.probe import (
    algebraic_landscape_reuses_b131,
    algebraic_venue_is_mirror_blind,
    topological_venue,
    verify_588_claim,
)


def test_algebraic_venue_is_mirror_blind():
    """The key gating fact: the (kappa,trT) algebraic venue is mirror-invariant, hence blind to chirality-(ii)."""
    a = algebraic_venue_is_mirror_blind()
    assert a["all_trace_mirror_invariant"] is True


def test_algebraic_landscape_reuses_b131():
    """The landscape venue works: reuse of B131 reproduces the exact (1,2) fork = {-4,-2}."""
    r = algebraic_landscape_reuses_b131()
    assert r["reproduces_B131_minus4_minus2"] is True


def test_topological_venue_verdict():
    """Topological venue: closed JSJ composite, no SnapPy direct-glue API (needs Regina / manual)."""
    t = topological_venue()
    if "skipped" in t:
        pytest.skip(t["skipped"])
    assert t["snappy_direct_boundary_glue_api"] is False
    assert t["seed1_cusps"] == 1 and t["seed2_cusps"] == 1


def test_588_claim_corrected():
    """The 588/Massey claim: s776 != Borromean (L6a4); Massey attribution dead for s776 (K-I)."""
    v = verify_588_claim()
    if "skipped" in v:
        pytest.skip(v["skipped"])
    assert v["s776_eq_L6a4"] is False
    assert any("6^3_1" in x for x in v["s776_identify"])
