"""B206 -- the golden object's spin/congruence shadow = 2I = SL(2,F5) = McKay-E8 (V203). pyenv.

Classical/trace level PSL(2,F5)=A5 (5 irreps); quantum/spin level SL(2,F5)=2I (9 irreps); the Z/2 is
the center {+-I} = spin cover; 4 extra spinorial irreps {2,2,4,6}; 2I dims = affine E8 marks; golden-
specific (field Q(sqrt5)). Ingredients standard; firewall = McKay-E8 (rep theory), NOT physics E8.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B206_golden_spin_cover_e8"))
from golden_spin_cover import summary, DIMS_2I, DIMS_A5, sqfree  # noqa: E402


def test_spin_cover_structure():
    s = summary()
    assert s["|SL(2,F5)|"] == 120          # = |2I|
    assert s["|PSL(2,F5)|"] == 60          # = |A5|
    assert s["|center|"] == 2              # the spin Z/2 (SU(2)->SO(3))
    assert s["#cc_SL"] == 9                # 2I: 9 irreps = affine E8 nodes
    assert s["#cc_PSL"] == 5               # A5: 5 irreps
    assert s["n_spinorial"] == 4           # 9-5 spinorial irreps the quantum level adds


def test_mckay_e8_marks():
    assert sum(d * d for d in DIMS_2I) == 120     # affine E8 marks, sum sq = |2I|
    assert sum(d * d for d in DIMS_A5) == 60
    assert sorted(DIMS_2I) == [1, 2, 2, 3, 3, 4, 4, 5, 6]


def test_golden_specificity_corrected():
    # re-audit (2026-06-25): golden is the MINIMAL member of the Q(sqrt5)/E8 family, NOT the unique one.
    s = summary()
    # field is EXACTLY Q(sqrt5) (sqfree=5) for the odd-index Lucas family, not just {1,4}
    assert s["field_is_sqrt5"][:4] == [1, 4, 11, 29]
    assert sqfree(11 * 11 + 4) == 5 and sqfree(29 * 29 + 4) == 5   # the cap-m<=8 artifact, exposed
    # the 2I=SL(2,F5) shadow (5 | m^2+4) is WIDER still: m == +-1 mod 5
    assert s["two_I_shadow_ms"][:6] == [1, 4, 6, 9, 11, 14]
    # golden is the minimal one (smallest disc); silver/bronze fields are NOT disc-5
    assert sqfree(1 + 4) == 5 and sqfree(4 + 4) == 2 and sqfree(9 + 4) == 13


def test_golden_monodromy_SURJECTS_onto_2I():
    # LOAD-BEARING (re-audit fix): the shadow is the WHOLE SL(2,F5)=2I, i.e. <R,L> surjects (order 120) --
    # not merely that one element RL has finite order 10 (which alone does NOT establish the 2I shadow).
    s = summary()
    assert s["monodromy_shadow_order"] == 120     # <R,L> mod 5 = all of SL(2,F5) = 2I
    assert s["RL_single_order"] == 10             # a single RL element: only a cyclic order-10 subgroup
    assert s["RL_mod5_order"] == 10               # (consistent with the single-element order)


if __name__ == "__main__":
    test_spin_cover_structure()
    test_mckay_e8_marks()
    test_golden_specificity_corrected()
    test_golden_monodromy_SURJECTS_onto_2I()
    print("ALL CHECKS PASS")
