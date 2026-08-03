"""Locks B861 -- the fused cascade."""
import importlib.util
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B861_fused_cascade"
_S = importlib.util.spec_from_file_location("b861", _D / "fused_cascade.py")
b1 = importlib.util.module_from_spec(_S)
_S.loader.exec_module(b1)
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split())


def test_the_chain_is_the_sm_chain_and_unique_at_every_step():
    assert RES["chain"] == ["E6", "SO(10)xU(1)", "SU(5)xU(1)", "SM"]
    assert RES["chain_is_sm"] is True
    for k in ("step1_E6", "step2_SO10", "step3_SU5"):
        assert RES[k]["unique"] is True, k


def test_the_criterion_is_not_vacuous():
    """It can fail (Sp(8), SU(4)xU(1)) and can pass -- both directions locked."""
    assert RES["criterion_can_fail"] is True
    assert RES["criterion_can_pass"] is True
    s1 = {r["option"]: r["registerable"] for r in RES["step1_E6"]["menu"]}
    assert s1["Sp(8)"] is False, "the 27 under C4 is self-dual"
    s3 = {r["option"]: r["registerable"] for r in RES["step3_SU5"]["menu"]}
    assert s3["SU(4)xU(1)"] is False and s3["SM"] is True


def test_the_deviation_clause_dissolves():
    assert RES["deviation_clause_dissolves"] is True


def test_where_the_principle_bites_vs_where_ranking_decides():
    """The gate bites exactly twice (Sp(8), SU(4)xU(1)); elsewhere max-dim decides."""
    bites = []
    for k in ("step1_E6", "step2_SO10", "step3_SU5"):
        for r in RES[k]["menu"]:
            if not r["registerable"]:
                bites.append(r["option"])
    assert sorted(bites) == ["Sp(8)", "SU(4)xU(1)"], bites


def test_conjugation_table_is_an_involution_with_no_name_collisions():
    for r, c in b1.CONJ.items():
        assert b1.CONJ[c] == r
    # the SU(4) "6" is self-dual; the SU(6) "6bar/6c" pair is complex -- named apart
    assert b1.CONJ["6"] == "6"
    assert b1.CONJ["6bar"] != "6bar"


def test_the_first_draft_error_is_recorded():
    """Coset multisets are vacuous; the draft returned SU(3)^3. Must stay on the record."""
    assert "VACUOUS" in _F
    assert "SU(3)³ as the step-1 winner" in _F or "SU(3)^3 as the step-1 winner" in _F.replace("³","^3")


def test_menu_completeness_stays_the_single_external_dependency():
    assert "P5" in _F and "single external" in _F


def test_su3_9_branching_flagged_unresolved():
    assert "UNRESOLVED" in _F
