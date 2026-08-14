"""B947 locks — L130, the thinning law. Seal integrity first."""
import hashlib
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B947_thinning_law"
SEAL_SHA = "610fa7119c6a4fa8b55fe3155eebf5de0527ab4ac85f460a2f473eb69c51807c"


def test_seal_integrity_prereg_hash_unchanged():
    assert hashlib.sha256((CELL / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEAL_SHA


def test_the_seal_carries_its_provenance_fields():
    """The first seal under the seal-provenance gate must actually carry them."""
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt


def test_the_vacuity_exclusion_was_declared_in_advance():
    txt = " ".join((CELL / "PREREGISTRATION.md").read_text(encoding="utf-8").split())
    assert "Pre-declared vacuity exclusion" in txt
    assert "cannot be chosen after seeing results" in txt


def test_the_normalisation_defect_is_named_not_inherited():
    txt = " ".join((CELL / "PREREGISTRATION.md").read_text(encoding="utf-8").split())
    assert "if the normaliser is free" in txt
    assert "nearly vacuous" in txt


def test_the_convenient_answer_is_named():
    txt = " ".join((CELL / "PREREGISTRATION.md").read_text(encoding="utf-8").split())
    assert "LAW is the convenient answer and must clear the higher bar" in txt


# ------------------------------------------------- the cells, after compute

import json  # noqa: E402
import pathlib as _pl  # noqa: E402

import sys  # noqa: E402
sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_the_banked_identity_gate_passed():
    assert _res()["banked_identity_gate"] is True


def test_the_exclusion_set_was_empty_so_it_could_not_shape_the_result():
    assert _res()["excluded"] == []


def test_five_hold_and_two_fail():
    r = _res()
    assert r["verdict"] == "SPECIAL"
    assert sorted(r["failures"]) == ["kappa_compact", "mu_charge"]
    holds = [k for k, v in r["families"].items() if v["pattern_holds"]]
    assert len(holds) == 5


def test_the_two_failures_are_not_borderline():
    r = _res()
    for f in r["failures"]:
        assert r["families"][f]["P_mid_only"] == []
        assert len(r["families"][f]["P_lead"]) >= 5


def test_the_seal_gloss_is_corrected_not_obeyed_blindly():
    """Five families hold; the prereg's 'about V alone' gloss is not banked."""
    assert contains(CELL / "FINDINGS.md",
                    "that gloss is not what the data says",
                    "not banking a conclusion the computation contradicts")


def test_the_structured_split_is_flagged_POST_HOC_not_claimed():
    assert contains(CELL / "FINDINGS.md",
                    "post-hoc", "registered, not claimed", "L137",
                    "would convert a failed prediction into a success story")
