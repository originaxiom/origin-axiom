"""B942 locks — L113, the BC/CMR falsifier.

Seal integrity first, per the preregistration. The remaining locks (one per
cell, plus the kill-condition-execution lock) are added when the cells run;
until then this file holds the seal, which is the part that must be
untamperable while the computation is still ahead of us.
"""
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B942_l113_bc_falsifier"
SEAL_SHA = "48cd1ea291277f8c85637a9c817a554edc7bc4370bf7ec893bec223428ebc5a2"


def test_seal_integrity_prereg_hash_unchanged():
    got = hashlib.sha256((CELL / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert got == SEAL_SHA


def test_seal_integrity_ledger_row_matches():
    ledger = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    rows = [r for r in ledger.splitlines() if "B942" in r and SEAL_SHA in r]
    assert len(rows) == 1


def test_the_kill_condition_is_quoted_in_the_seal():
    """The prereg must carry the locked kill condition verbatim, so the seat
    cannot soften it on contact with the answer."""
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "L113 YES" in txt
    assert "the observer construction's foundation fails" in txt


def test_the_criterion_forbids_a_third_outcome():
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "There is no third outcome" in txt
    assert "does **not** default to the programme's favour" in txt


def test_the_prior_was_disclosed_against_the_programme():
    """The disclosed prior must be the inconvenient one, stated before compute."""
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    m = re.search(r"\*\*OUTCOME YES, high\.\*\*", txt)
    assert m, "the prior must be disclosed as OUTCOME YES"
    assert "executes a kill condition against the programme's own construction" in txt


# ----------------------------------------------------- the cells, after compute

import json  # noqa: E402


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_cell1_the_identification_was_explicit_in_our_own_text():
    r = _res()
    assert r["c1_b723_names_the_CMR_system"]["value"] is True
    assert r["c1_b723_names_Gal_Kab_over_K"]["value"] is True
    assert r["CELL1_identification_is_explicit"]["value"] is True


def test_cell2_conjugation_is_not_in_the_label_group():
    """The load-bearing fact, computed two independent ways."""
    r = _res()
    assert r["c2_conjugation_moves_it"]["value"] is True
    assert r["CELL2_c_in_Gal_Kab_over_K"]["value"] is False
    assert r["c2_c_never_in_GalK"]["value"] is True
    assert r["c2_index_always_2"]["value"] is True
    layers = r["c2_cyclotomic_layers"]["value"]
    assert len(layers) >= 12
    for L in layers:
        assert L["c_in_GalK"] is False
        assert L["index"] == 2


def test_cell3a_the_transition_is_the_zeta_pole_and_a_finite_level_has_none():
    r = _res()
    assert r["c3a_pole_confirmed"]["value"] is True
    got = float(r["c3a_zetaK_residue_at_s1_numeric"]["value"][-1])
    predicted = float(r["c3a_zetaK_residue_predicted"]["value"])
    assert abs(got - predicted) < 1e-9
    # the class-number formula value, independently
    import math
    assert abs(predicted - 2 * math.pi / (6 * math.sqrt(3))) < 1e-9


def test_cell3b_no_canonical_Z2_quotient():
    r = _res()
    counts = r["c3b_counts"]["value"]
    assert r["c3b_count_nondecreasing"]["value"] is True
    assert r["c3b_count_strict_rises"]["value"] >= 3
    assert max(counts) > 1, "more than one Z/2 quotient => no canonical choice"
    assert r["c3b_canonical_Z2_exists"]["value"] is False


def test_cell3cd_the_remaining_hatches_are_closed():
    r = _res()
    assert r["c3c_conjugation_action_on_labels_is_trivial"]["value"] is True
    assert r["c3d_real_place_available"]["value"] is False
    assert r["c3d_K_signature_r1_r2"]["value"] == [0, 1]


def test_cell4_one_label_cannot_carry_both():
    r = _res()
    assert r["c4_one_label_cannot_be_both"]["value"] is True
    assert r["c4_action_is_free_and_transitive"]["value"] is True


def test_the_kill_condition_was_EXECUTED_not_softened():
    """The point of the seal: a YES must land as a retraction in the findings."""
    r = _res()
    assert r["verdict"]["outcome"] == "YES"
    assert r["verdict"]["kill_condition_executes"] is True
    txt = (CELL / "FINDINGS.md").read_text(encoding="utf-8")
    assert "It is hereby executed" in txt
    assert "RETRACTED" in txt
    for clause in ("CHIRALITY = the extremal-KMS", "cannot produce the c-swap"):
        assert clause in txt


def test_the_surviving_clause_is_marked_UNEARNED_not_certified():
    """The arc must refuse to wave through the neighbouring clause."""
    txt = (CELL / "FINDINGS.md").read_text(encoding="utf-8")
    assert "UNEARNED, not refuted" in txt
    assert "NEW OPEN LEAD (registered)" in txt


def test_the_replacement_is_stated_as_falsifiable():
    txt = (CELL / "FINDINGS.md").read_text(encoding="utf-8")
    assert "the object's c-swap is not\nthermodynamic" in txt.replace("**", "") or \
        "c-swap is not" in txt
    assert "falsifiable relocation" in txt
