"""Locks B860 -- the step-3 bit: enumeration, theta-cores, and the dial-stripped asymmetry."""
import importlib.util
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B860_step3_bit"
_S = importlib.util.spec_from_file_location("b860", _D / "step3_bit.py")
b0 = importlib.util.module_from_spec(_S)
_S.loader.exec_module(b0)
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split())


def test_the_trit_is_a_bit():
    """Two-node removals on the A4 cycle give exactly two patterns."""
    assert RES["bds_patterns"] == [[3], [2, 1]]
    assert RES["trit_is_a_bit"] is True
    pats = b0.bds_two_node_patterns()
    assert [list(p) for p in pats] == [[3], [2, 1]]


def test_all_four_subalgebras_are_theta_stable():
    for lab, t in RES["theta"].items():
        assert t["stable"] is True, lab
        assert t["even"] + t["odd"] == t["dim"], lab


def test_the_theta_cores_are_the_B2_borel_de_siebenthal_pair():
    assert RES["theta"]["SU(5)"]["even"] == 10          # so(5) = B2
    assert RES["theta"]["SU(4)xU(1)"]["even"] == 6      # so(4) = D2
    assert RES["theta"]["SM"]["even"] == 4              # so(3) x so(2)
    assert RES["theta"]["SU(3)xU(1)^2"]["even"] == 3    # so(3): NOT maximal-rank in B2
    assert RES["cores_are_B2_bds_pair"] is True


def test_the_abelian_factors_are_theta_odd():
    """dim(even) counts no u(1): SU(4)xU(1) has even 6 = dim so(4), the u(1) in the odd part."""
    assert RES["theta"]["SU(4)xU(1)"]["even"] == 6 and RES["theta"]["SU(4)xU(1)"]["dim"] == 16
    assert RES["theta"]["SM"]["even"] == 4 and RES["theta"]["SM"]["dim"] == 12


def test_the_dial_stripped_asymmetry():
    """THE POINT: SU(4)-side generation collapses; the SM's stays chiral."""
    assert RES["su4_collapses"] is True
    assert RES["sm_stays_chiral"] is True
    assert RES["generation_sm_residue"] == {"(3,2)": 1, "(3bar,1)": 2}


def test_conjugation_table_is_an_involution():
    for r, c in b0.CONJ.items():
        assert b0.CONJ[c] == r


def test_the_premise_is_named_as_a_premise():
    """The registerability principle must not be dressed as a theorem."""
    assert "premise is a premise" in _F or "The registerability premise is a premise" in _F
    assert "Not a derivation of the SM" in _F


def test_the_banked_machinery_is_cited_not_reproved():
    assert "B599" in _F and "B593" in _F
    assert "banked + locked" in _F or "banked" in _F
