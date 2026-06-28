"""B266 locks -- wall #2: the figure-eight's arithmetic canonically selects E6 via the ramified prime.
Fig-8 group ->> SL(2,F_3)=2T=McKay-E6; two ends Q(sqrt-3)/3->E6, Q(sqrt5)/5->E8; E7(2O) homeless (not SL(2,q)).
FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B266_arithmetic_selects_e6" / "arithmetic_selects_e6.py"
_spec = importlib.util.spec_from_file_location("b266", _PATH)
b266 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b266)


def test_fig8_surjects_onto_2T():
    # the figure-eight group's Riley rep mod the ramified prime (sqrt-3) generates all of SL(2,F_3) = 2T
    assert b266.fig8_mod3_order() == b266.sl2_order(3) == 24


def test_mckay_marks_match_affine_ade():
    # 2T->E6, 2I->E8, 2O->E7 (marks = binary-polyhedral irrep dims = affine ADE marks)
    for g, info in b266.MCKAY.items():
        assert sorted(info["marks"]) == sorted(b266.AFFINE_MARKS[info["affine_type"]])
    assert b266.MCKAY["2T"]["affine_type"] == "E6"
    assert b266.MCKAY["2T"]["as_SL2Fq"] == 3 and b266.MCKAY["2I"]["as_SL2Fq"] == 5


def test_two_ends_and_e7_homeless():
    # Q(sqrt-3) ramifies at 3 -> F_3 -> 2T/E6 ; Q(sqrt5) ramifies at 5 -> F_5 -> 2I/E8
    assert b266.ramified_prime_and_residue(-3) == (-3, {3: 3})
    assert b266.ramified_prime_and_residue(5) == (5, {5: 5})
    # E7 = 2O (order 48) is never SL(2,q): no prime-reduction home (B256)
    assert 48 not in [b266.sl2_order(q) for q in range(2, 40)]
    assert b266.MCKAY["2O"]["as_SL2Fq"] is None
