"""B1010 — locks for the consolidation-loss audit and the two restorations.

The pattern these locks copy (from B1007's lesson): when a false belief costs an arc, lock the
fact that refutes it. The false belief here was second-order — the consolidations BELIEVED they
carried the record. These assert the restored laws stay restored, and that the restorations
remain mathematically true, not merely present as text.
"""
from __future__ import annotations

import pathlib
import sys

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_the_kappa_identities_hold_exactly():
    """The law's mathematics, re-computed at lock time — never restored from memory (B1010 §1)."""
    u = sp.exp(2 * sp.pi * sp.I / 3)
    kappa = u**2 + 2
    assert sp.simplify((kappa - 2) - u**2) == 0, "kappa - 2 must equal omega^2"
    assert sp.Abs(sp.simplify(kappa - 2)).simplify() == 1, "the obstruction must be a UNIT"
    assert sp.simplify(sp.arg(kappa.expand(complex=True)) + sp.pi / 6) == 0, (
        "arg(kappa) must be -pi/6 at u = omega — the matter face's CP phase")


def test_the_kappa_unification_is_in_both_consolidations():
    """The loss B1010 measured: LAW_MAP cited B309/B518 zero times; THE_FRAMEWORK had zero kappa.

    If either regresses, a consolidation was rewritten without reading the whole record again —
    the exact failure mode the refresh campaign exists to end.
    """
    law_map = (ROOT / "docs" / "LAW_MAP.md").read_text(encoding="utf-8")
    framework = (ROOT / "docs" / "THE_FRAMEWORK.md").read_text(encoding="utf-8")
    assert "B309" in law_map and "B518" in law_map, "the kappa-unification row left LAW_MAP"
    assert "κ-UNIFICATION" in law_map
    assert "κ = tr[a,b]" in framework, "THE_FRAMEWORK lost the bridge equation again"
    assert "ℚ(√−3) → 2T → McKay-E₆" in framework, (
        "the matter chain — why the cascade exists — must stay stated in the framework")


def test_the_coupling_law_is_in_the_framework_value_layer():
    """u†Mu — the value-as-coupling law — had ZERO occurrences in the framework's value layer."""
    framework = (ROOT / "docs" / "THE_FRAMEWORK.md").read_text(encoding="utf-8")
    assert "u†M_odd u" in framework, "the coupling form left the framework"
    assert "B856" in framework and "FORCES a value" in framework, (
        "the family law's operative sentence must stay quoted")
    assert "L150" in framework, (
        "the un-made tone↔Hermitian junction must stay flagged as open until L150 resolves")


def test_L150_and_the_refresh_campaign_are_registered():
    leads = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    assert "L150" in leads and "u†M_odd u" in leads
    campaign = (ROOT / "docs" / "THE_CAMPAIGN.md").read_text(encoding="utf-8")
    assert "CONSOLIDATION REFRESH" in campaign
    assert "consolidation-debt ledger" in campaign, (
        "the refresh discipline's deliverable must stay named")


def test_crossing_requirements_exist_and_carry_the_three_mechanisms():
    """The fourth crossing's gate: a prereg that cannot check every row does not seal."""
    doc = (ROOT / "docs" / "CROSSING_REQUIREMENTS.md").read_text(encoding="utf-8")
    for mechanism in ("assumed interpolation", "wrong hemisphere", "missing normalisation"):
        assert mechanism in doc, f"the anatomy lost mechanism '{mechanism}'"
    for req in ("R1", "R10"):
        assert req in doc
    assert "HIT-SHAPE is not it" in doc, (
        "the success definition must keep excluding shape-only outcomes")
