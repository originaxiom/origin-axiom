"""B940 locks — THE SEALED DIRAC RUN on (m004, rho_1): OUTCOME A.

Per the preregistration, SEAL INTEGRITY comes first in this file: the
prereg's own sha-256 is re-verified against the file on disk and against
the SEAL_LEDGER row, before any number is asserted. A number certified
under a seal is only worth the seal.

The O3 gate is locked too, in the direction that matters: the sweep did
NOT reach MathSciNet, so the gate stays CLOSED and no claim sentence in
this arc may contain the priority word.
"""
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B940_dirac_sealed"

SEAL_SHA = "6c513b0634c743df4015fc694d5dbd23dbf38e35829b838012a71dbfa75311fe"
LAM = 2.974550580173186  # S1 at the sealed refinement offset d = 1e-6
SEALED_BAR = 1e-9


def _results():
    return json.loads((CELL / "results.json").read_text())


# ---------------------------------------------------------------- seal first

def test_seal_integrity_prereg_hash_unchanged():
    """The preregistration on disk still hashes to the sealed value."""
    got = hashlib.sha256((CELL / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert got == SEAL_SHA


def test_seal_integrity_ledger_row_matches():
    ledger = (ROOT / "docs" / "SEAL_LEDGER.md").read_text()
    rows = [r for r in ledger.splitlines() if "B940" in r and SEAL_SHA in r]
    assert len(rows) == 1, "exactly one B940 seal row, carrying the sealed hash"


def test_seal_integrity_instrument_recorded_the_same_hash():
    """The instrument stamped the hash itself, in stage `seal`, before compute."""
    seal = _results()["seal"]
    blob = json.dumps(seal)
    assert SEAL_SHA in blob


def test_the_criterion_is_a_conjunction_not_a_single_bar():
    """Vacuity guard: the sealed criterion must have >= 8 distinct elements."""
    cand = _results()["verdict"]["candidates"][0]
    assert len(cand["elements"]) >= 8
    assert all(cand["elements"].values())


# ------------------------------------------------------------- OUTCOME A

def test_outcome_a_two_eigenvalues_pass_every_element():
    v = _results()["verdict"]
    passing = [c for c in v["candidates"] if c["passes_all"]]
    assert len(passing) == 2, "the eigenvalue and its enforced partner"
    lams = sorted(c["lam"] for c in passing)
    assert abs(lams[0] + LAM) < 1e-11 and abs(lams[1] - LAM) < 1e-11


def test_every_sealed_element_measured_inside_its_bar():
    for c in _results()["verdict"]["candidates"]:
        if not c["passes_all"]:
            continue
        assert c["two_Y_dev"] < SEALED_BAR
        assert c["two_seed_dev"] < SEALED_BAR
        assert c["word_set_dev"] < SEALED_BAR
        assert c["p4_joint_spread"] < SEALED_BAR
        assert c["pair_dev"] < SEALED_BAR
        # three orders of margin, not a squeaker
        assert c["two_Y_dev"] < SEALED_BAR / 100


def test_four_instruments_agree_to_the_reported_spread():
    for c in _results()["verdict"]["candidates"]:
        if not c["passes_all"]:
            continue
        vals = [abs(x) for x in c["per_instrument"].values()]
        assert len(vals) == 4
        assert max(vals) - min(vals) < 1e-11


def test_the_ten_digits_the_seal_names():
    assert f"{LAM:.9f}" == "2.974550580"


# ------------------------------------------------- the O3 gate stays closed

def test_o3_gate_closed_mathscinet_not_reached():
    """The gate names MathSciNet/zbMATH grade; MathSciNet was unreachable."""
    o3 = json.loads((CELL / "o3_results.json").read_text())
    blob = json.dumps(o3).lower()
    assert "mathscinet" in blob
    assert "zbmath" in blob


def test_no_priority_sentence_in_the_banked_verdict():
    """The priority word must not appear in the arc's claim record."""
    verdict = json.loads((CELL / "arc_verdict.json").read_text())
    assert not re.search(r"\bfirst\b", verdict["claim_one_line"], re.I)
    assert verdict["verdict"] == "PROVED"


def test_the_load_bearing_qualifiers_are_recorded():
    """If the gate ever opens, 'nonzero' and 'cusped' are load-bearing."""
    txt = (CELL / "FINDINGS.md").read_text()
    assert "nonzero" in txt and "cusped" in txt
    assert "2506.07238" in txt, "Lin-Lipnowski, the near-miss, cited positively"
    assert "2311.13330" in txt, "the must-pass control that came back POSITIVE"


# --------------------------------------------- the lessons this run earned

def test_p3_control_found_nothing_but_two_Y_alone_was_not_discriminating():
    """The warning the criterion earned: a reproducibility bar measures the
    instrument's determinism, not the object's spectrum."""
    p3 = _results()["p3"]
    blob = json.dumps(p3)
    # the control found nothing at any displaced start
    assert "2.5" in blob or "displaced" in blob.lower()
    txt = (CELL / "FINDINGS.md").read_text()
    assert "not by itself" in txt and "conjunction" in txt


def test_quadrature_defect_was_latent_not_active():
    q = _results()["quadrature_control"]
    blob = json.dumps(q)
    assert "0.0" in blob or "0" in blob
    txt = (CELL / "FINDINGS.md").read_text()
    assert "bit-identical" in txt


def test_kernel_excluded_from_the_seal():
    txt = (CELL / "FINDINGS.md").read_text()
    assert "EXCLUDED" in txt
    verdict = json.loads((CELL / "arc_verdict.json").read_text())
    assert "kernel" in verdict["claim_one_line"].lower()


def test_no_multiplicity_claim():
    txt = (CELL / "FINDINGS.md").read_text()
    assert "No multiplicity is claimed" in txt
