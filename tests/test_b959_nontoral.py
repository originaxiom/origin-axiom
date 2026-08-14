"""B959 locks — L133's decisive cell. Seal integrity first."""
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B959_nontoral_rank4"
SEAL_SHA = "6c5d76e695ff7958ab3e15d079e5676e594f61b753648e82f0b1363cec0723aa"


def _n(p):
    t = re.sub(r"(?m)^\s*>\s?", "", p.read_text(encoding="utf-8")).replace("*", "")
    return " ".join(t.split())


def test_seal_integrity_prereg_hash_unchanged():
    assert hashlib.sha256((CELL / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEAL_SHA


def test_the_seal_carries_its_provenance_fields():
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt


def test_the_hinge_is_stated_before_computing():
    t = _n(CELL / "PREREGISTRATION.md")
    assert "non-toral" in t
    assert "The hinge, stated before computing" in t


def test_the_prior_is_disclosed_as_NO_GO():
    t = _n(CELL / "PREREGISTRATION.md")
    assert "NO-GO, moderately favoured" in t
    assert "FOUND is the convenient answer and must clear the higher bar" in t


def test_the_valuable_outcome_is_named_as_the_negative():
    t = _n(CELL / "PREREGISTRATION.md")
    assert "convert the programme's four independent negatives into one" in t


# ------------------------------------------------- the cells, after compute

import json  # noqa: E402


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_the_banked_identity_gate_passed():
    g = _res()["cell1_gate"]
    assert g["dim_Z_su3_colour"] == 16 and g["passed"] is True


def test_inner_involutions_all_fix_the_full_cartan():
    c = _res()["cell2_inner_involutions"]
    assert c["sign_gradings_tested"] == 63
    assert c["all_fix_the_full_Cartan"] is True
    assert c["fixed_subalgebra_rank"] == 6


def test_the_outer_route_makes_the_27_real_and_covers_F4_and_C4_at_once():
    c = _res()["cell3_outer_route"]
    assert c["diagram_automorphisms"] == 2 and c["nontrivial"] == 1 and c["order"] == 2
    assert sorted(map(sorted, c["swapped_node_pairs"])) == [[0, 5], [2, 4]]
    assert "SELF-DUAL" in c["conclusion"]
    assert c["form_independent"] is True


def test_the_hatch_has_elementary_abelian_rank_at_most_two():
    h = _res()["cell4_hatch_ranks"]
    assert h["A4"]["elem_ab_2_rank"] == 2 and h["D5"]["elem_ab_2_rank"] == 1
    assert h["S5"]["elem_ab_2_rank"] == 2
    assert max(v["elem_ab_3_rank"] for k, v in h.items() if k != "max_over_hatch") == 1
    assert h["max_over_hatch"] == 2


def test_the_verdict_is_NO_GO_with_its_scope_stated():
    v = _res()["verdict"]
    assert v["outcome"] == "NO-GO"
    assert "simply connected" in v["scope"]
    assert len(v["routes_closed"]) == 3


def test_the_remaining_hatch_is_named_not_hidden():
    """A no-go that overstates its scope is worse than no no-go."""
    v = _res()["verdict"]
    assert "ADJOINT" in v["hatch_NOT_closed"]
    t = " ".join((CELL / "FINDINGS.md").read_text(encoding="utf-8").replace("*", "").split())
    assert "THE ONE HATCH THIS DOES NOT CLOSE" in t
    assert "L136" in t
    assert "does not say the object cannot reach the sm" in t.lower()


def test_the_torality_citation_is_flagged_as_load_bearing():
    r = _res()["torality_step"]
    assert r["cited_not_rederived"] is True
    assert r["assumes_simply_connected"] is True
    assert r["breaks_at_rank"] == 3
