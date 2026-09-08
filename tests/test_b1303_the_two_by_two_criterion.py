"""B1303 — the 2x2 criterion: h^1(Y_n; psi) = 1 iff A(x_{n-1}) ... A(x_0) = I on the fixed-quotient presentation of the
n-fold cyclic branched cover; reproduces B1301's supports at every level 2 ... 13 (counts, orders, deck-eigen structure),
the refined law's clause-by-clause census on Y_10 and Y_15, and B1278/B1300's Standard-Model lines of Y_9 from the
criterion's own support (fast, ~40 s); the homomorphism counts of the three presentations and the levels 18 and 21 at scale
(slow)."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "frontier" / "B1303_the_two_by_two_criterion" / "verification"
sys.path.insert(0, str(HERE))

B1301_SUPPORT = {2: 0, 3: 3, 4: 0, 5: 20, 6: 27, 7: 56, 8: 0, 9: 147, 10: 20, 11: 396, 12: 123, 13: 1040}


def test_the_criterion_reproduces_every_support_of_b1301():
    import criterion as C
    for n, cnt in B1301_SUPPORT.items():
        L = C.level(n)
        assert L['count'] == cnt, (n, L['count'])
    L9 = C.level(9)
    assert L9['byord'] == {2: 3, 19: 36, 38: 108} and L9['eig'][(19, 6)] == 18 and L9['eig'][(19, 16)] == 18
    L11 = C.level(11)
    assert L11['eig'] == {(199, 63): 198, (199, 139): 198}
    L12 = C.level(12)
    assert L12['byord'] == {2: 3, 8: 24, 16: 96}


def test_the_refined_law_clause_by_clause():
    import refined_law as R
    t10 = R.test(10)
    assert t10[('eigen', 'lam_ord>=3', 'u^n=+-1', True)] == 20 and t10[('eigen', 'lam_ord<3', 'u^n mixed', False)] == 80
    assert t10[('eigen', 'lam_ord<3', 'u^n=+-1', False)] == 4 and t10[('not-eigen', False)] == 15020
    assert all(k[-1] == (k[0] == 'eigen' and k[1] == 'lam_ord>=3' and k[2] == 'u^n=+-1') for k in t10)
    t15 = R.test(15)
    assert t15[('eigen', 'lam_ord>=3', 'u^n=+-1', True)] == 680 and t15[('eigen', 'lam_ord>=3', 'u^n mixed', False)] == 600
    assert t15[('not-eigen', False)] == 115000
    assert all(k[-1] == (k[0] == 'eigen' and k[1] == 'lam_ord>=3' and k[2] == 'u^n=+-1') for k in t15)


def test_the_lines_of_y9_from_the_criterions_support():
    import odd_alphabet_lines as O
    r = O.run(HERE / "support_mt_Y9.json", "Y_9")
    assert r['form'] and r['n_three'] == 758593 and r['n_broken'] == 737568 and r['n_sm'] == 706464 and r['n_full'] == 568656
    assert r['d_tot'] == {3: 706464} and len(r['patterns']) == 67
    r18 = O.run(HERE / "support_mt_Y18.json", "Y_18")
    assert r18['n_sm'] == 706464 and r18['n_full'] == 568656 and r18['d_tot'] == {3: 706464}


def test_the_law_on_the_eigencharacters_of_y20_and_y15():
    import eigen_census as E
    t20 = E.level(20)
    assert t20[(0, 'unramified', '+', '+', 1)] == 20 and t20[(0, 'unramified', '-', '-', 0)] == 80      # the 41-part: sign - at an even level
    law = lambda par, ram, signs, gsign, h: h == int(ram == 'unramified' and gsign in ('+', '-') and (par == 1 or gsign == '+'))
    assert all(law(*key) for key in t20)
    t15 = E.level(15)
    assert t15[(1, 'unramified', '++', '+', 1)] == 300 and t15[(1, 'unramified', '+-', 'mixed', 0)] == 300
    assert all(law(*key) for key in t15)


@pytest.mark.slow
def test_the_three_presentations_agree_on_homomorphism_counts(capsys):
    import presentations_hom_counts  # noqa: F401  (runs at import; prints the table)
    text = capsys.readouterr().out
    for line in text.strip().split("\n"):
        for cell in line.split("; ")[1:] if "; " in line else []:
            nums = [int(w) for w in cell.replace(":", "").split() if w.isdigit()]
            assert len(set(nums)) == 1, line


@pytest.mark.slow
def test_y18_and_y21_at_scale(tmp_path):
    import criterion_at_scale as S
    S.OUT = tmp_path
    d18 = S.level(18)
    assert len(d18['positives']) == 171 and len(d18['K3']) == 145 and len(d18['K2']) == 27
    d21 = S.level(21)
    assert len(d21['positives']) == 48947


@pytest.mark.slow
def test_y15s_odd_alphabet_keeps_two_light_triplet_pairs():
    import odd_alphabet_lines as O
    sys.path.insert(0, str(ROOT / "frontier" / "B1302_the_one_triplet_vacua" / "verification"))
    import one_triplet_vacua as V
    r = O.run(HERE / "support_mt_Y15.json", "Y_15")
    assert r['n_sm'] == 5016142400 and r['n_full'] == 4960988960 and r['d_tot'] == {3: 5016142400} and len(r['patterns']) == 67
    out = V.analyse(r['patterns'], "Y_15")
    assert out['minT'] == 2 and out['lines_solved'] == 0
