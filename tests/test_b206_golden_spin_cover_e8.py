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


def test_golden_specificity():
    # only the Q(sqrt5) family (m=1,4) hits disc 5 => 2I=SL(2,F5)=McKay-E8
    fields = {m: sqfree(m * m + 4) for m in range(1, 9)}
    assert fields[1] == 5 and fields[4] == 5
    assert all(fields[m] != 5 for m in (2, 3, 5, 6, 7, 8))


def test_golden_monodromy_reduces_into_2I():
    assert summary()["RL_mod5_order"] == 10   # RL=[[2,1],[1,1]] mod 5, finite order in SL(2,F5)=2I


if __name__ == "__main__":
    test_spin_cover_structure()
    test_mckay_e8_marks()
    test_golden_specificity()
    test_golden_monodromy_reduces_into_2I()
    print("ALL CHECKS PASS")
