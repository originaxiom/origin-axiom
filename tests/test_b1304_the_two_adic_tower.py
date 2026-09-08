"""B1304 — the 2-adic tower ends at Y_12: Y_24's 2-primary support, alphabet, Standard-Model lines and one-triplet vacua
are Y_12's (control: Y_12 reproduces B1301/B1302), and the criterion's product is unipotent on every non-trivial
character (~40 s)."""
import sys
import pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1304_the_two_adic_tower" / "verification"))


def test_y24_is_y12_pulled_back():
    import two_adic_lines as T
    out = T.main()
    assert out['ok']
    for n in (12, 24):
        assert out[n]['support'] == 123 and out[n]['byord'] == {2: 3, 8: 24, 16: 96} and out[n]['K3'] == 97 and out[n]['K2'] == 27
        assert out[n]['counts'] == {'three': 190849, 'broken': 181440, 'sm': 34752, 'full': 3264}
        assert out[n]['d_tot'] == {1: 31488, 3: 3264} and len(out[n]['patterns']) == 265
        assert out[n]['vacua']['minT'] == 1 and out[n]['vacua']['lines_solved'] == 768 and out[n]['vacua']['solved_patterns'] == 6
    assert out[24]['patterns'] == out[12]['patterns']


def test_the_product_is_unipotent_on_every_non_trivial_character():
    import unipotent_census as U
    for n, sup in ((5, 20), (6, 27), (9, 147), (10, 20)):
        r = U.level(n)
        cls = r['cls']
        assert cls['(False, True, False, True)'] == 1                                   # the trivial character alone is not unipotent
        assert cls['(True, True, True, False)'] == sup                                  # the identity exactly on the support
        assert sum(v for k, v in cls.items() if k.startswith('(True')) == r['unip'] and r['unip'] == {5: 120, 6: 319, 9: 5775, 10: 15124}[n]


@pytest.mark.slow
def test_the_two_lemmas_on_every_pair_of_levels():
    import two_lemmas as L
    assert L.main()


def test_the_law_in_conductor_form_on_the_small_levels():
    import conductor_law as C
    for n in (5, 9, 10, 12, 15, 20):
        tab = C.level(n)
        assert all(C.law(k) for k in tab), (n, tab)
    t15 = C.level(15)
    assert t15[(1, 'unramified', '+', 1)] == 340 and t15[(1, 'unramified', 'mixed', 0)] == 600
    t20 = C.level(20)
    assert t20[(0, 'unramified', '-', 0)] == 80 and t20[(1, 'unramified', '+', 1)] == 10

def test_the_positive_half_of_the_law_is_a_theorem():
    import law_positive_half as P
    P.check_A()                                   # the free-group identities behind the presentation identity
    assert P.check_B(2000)                        # conductor form <=> odd-order form on every (m, u), m <= 2000
    assert P.check_C(9)                           # every eigencharacter class of every level <= 9: N0 structure, prediction


def test_the_odd_half_deck_criterion_is_the_support_away_from_the_two_adic_exceptions():
    import odd_half_deck_criterion as O
    # exact agreement at the odd levels and at 4, 8 (no support); the two-adic conductor 6 is the exception (27 carry, 3 fixed)
    assert all(O.level(n) for n in (3, 4, 5, 7, 8, 9))
    assert not O.level(6)
