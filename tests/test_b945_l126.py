"""B945 locks — L126: one Z/2 or two? Seal integrity first, per the prereg."""
import hashlib
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B945_l126_one_z2"
SEAL_SHA = "4873215851b1ea76adbf7997b6795ed502dad7597d15ddb3f55bacb109d1dfdf"


def test_seal_integrity_prereg_hash_unchanged():
    got = hashlib.sha256((CELL / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert got == SEAL_SHA


def test_the_prior_is_declared_split_and_names_the_degeneracy_in_advance():
    """The scoping observation that RL has only two cyclic rotations was made
    BEFORE the seal, and cells 2-3 were pre-committed because of it."""
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "Split, and honestly so" in txt
    assert "two** cyclic rotations" in txt
    assert "pre-committed here rather than added after" in txt


def test_the_convenient_answer_is_named_as_such():
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "The convenient answer is LOCKED" in txt


def test_instrument_failure_branch_is_defined():
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "INSTRUMENT FAILURE" in txt


# ------------------------------------------------- the cells, after compute

import json  # noqa: E402


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_cell1_the_object_has_the_FULL_klein_stabilizer():
    c = _res()["cell1"]
    assert set(c["stabilizer"]) == {"1", "rho", "sigma", "rho.sigma"}
    assert c["is_amphichiral_GHH"] is True
    assert c["rho_alone_fixes"] is True and c["sigma_alone_fixes"] is True


def test_cell2_the_whole_metallic_locus_decouples_them():
    r = _res()
    assert r["cell2_all_amphichiral"] is True
    assert r["cell2_rho_alone_always"] is True
    assert r["cell2_sigma_alone_always"] is True
    assert len(r["cell2"]) == 8, "m = 1..8"


def test_cell3_the_locked_class_exists_and_is_the_majority():
    """The discovery: among amphichiral bundles, diagonal-only is more common."""
    r = _res()
    full = r["cell3_amphichiral_with_full_V"]
    diag = r["cell3_amphichiral_diagonal_only"]
    assert full == 13 and diag == 18
    assert diag > full, "the LOCKED class is the majority among amphichiral words"
    assert r["cell3_n_cyclic_classes"] == 241


def test_cell4_is_defused_by_its_own_vacuity_check():
    c = _res()["cell4"]
    assert c["R_transpose_is_L"] is True
    assert c["W_is_symmetric"] is True
    assert c["reverse_equals_swap_of_transpose"] is True
    # and the vacuity check must be recorded, so no depth is read into it
    assert c["every_matrix_conj_to_transpose_over_a_field"] is True
    # markdown is hard-wrapped: normalise whitespace before matching prose
    txt = " ".join((CELL / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "no content at the level of" in txt and "must be **integral**" in txt


def test_the_unification_is_WITHDRAWN_not_softened():
    r = _res()
    assert r["verdict"]["outcome_at_the_object"] == "INDEPENDENT"
    txt = " ".join((CELL / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "Withdrawn" in txt
    assert "do **not** collapse to one choice" in txt
    assert "L126 is **CLOSED, negative.**" in txt
