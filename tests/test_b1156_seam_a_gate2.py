"""B1156 lock -- SEAM-A Gate 2 sharpened by the WF-1 adversarial workflow: the a-priori MISMATCH that
B1155 leaned on is REFUTED (a finite-mu_n-truncation theorem, not a codomain wall); the full/Arakelov
arithmetic CS carries the Borel regulator of xi=[e^{i pi/3}] in K_3(Q(sqrt-3)) = Vol. Verdict = FLOOR
(the finite-phase->Vol map is NEEDS-SPECIALIST). Asserts on COMMITTED files only (cc3 B8141 the artifact
class). Archimedean anchor via the committed reproduce runner. No crossing; Gate 5 untouched."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1156_seam_a_gate2"


def _d():
    return json.loads((ARC / "b1156_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1156" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False


def test_seal_is_floor_from_the_workflow():
    d = _d()
    assert d["provenance_workflow"]["seal"] == "FLOOR"
    assert d["provenance_workflow"]["agents"] == 10
    assert "NEEDS-SPECIALIST" in d["verdict_outcome_FLOOR"]


def test_apriori_mismatch_refuted_as_truncation_theorem():
    d = _d()
    r = d["why_not_mismatch"]["refutation"]
    assert "REFUTED" in r
    assert "TRUNCATION" in r and "mu_n" in r
    assert "CONTAINS R" in r  # the untruncated codomain contains the reals
    # the refutation is not a fresh claim -- it echoes B1108 (banked)
    assert "B1108" in d["why_not_mismatch"]["not_a_new_claim"]


def test_category_correction_three_completions():
    comp = _d()["category_correction"]["three_completions_of_xi"]
    assert set(comp.keys()) == {"archimedean_inf", "finite_mod_n", "p_adic"}
    assert "Vol" in comp["archimedean_inf"] and "torsion" in comp["finite_mod_n"]
    # B800 is the p-adic completion, not the finite Kim action
    assert "B800" in _d()["category_correction"]["consequence"] and "P-ADIC" in _d()["category_correction"]["consequence"]


def test_archimedean_anchor_reproduces_committed_runner():
    # B8141 discipline: assert on the committed reproduce runner + its committed output, not a gitignored log
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners, "no committed reproduce runner"
    assert "REPRODUCES" in runners[0].read_text(encoding="utf-8")
    anchor = (ARC / "verification" / "archimedean_anchor.txt").read_text(encoding="utf-8")
    assert "2.02988321281930725" in anchor and "REPRODUCES" in anchor
    assert "z^2 - z + 1      = 0.0" in anchor


def test_v3_residual_quarantined_not_banked():
    q = _d()["quarantined_not_banked"]
    assert "REFUTED" in q and "NOT BANKED" in q and "immaterial" in q


def test_exact_remaining_computation_named():
    rc = _d()["exact_remaining_computation"]
    assert "Andersen-Hansen" in rc and "CUSPED" in rc and "Arakelov" in rc
    assert "OA-C1045" in rc  # the codex-side W0 gap


def test_no_crossing_gate5_untouched():
    d = _d()
    assert "No firewall crossing" in d["fences"] and "Gate 5 untouched" in d["fences"]
