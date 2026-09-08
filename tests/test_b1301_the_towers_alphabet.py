"""B1301 — the tower's alphabet: the Standard-Model lines of Y_9 and Y_12 from the stored supports (Y_9 reproduces B1278
and B1300 on every count; Y_12: 34 752 SM lines, the colour triplet thinned to one generation on 31 488 of them, never to
none), and the exhaustive sweeps of Y_2 ... Y_9 with the deck-eigen census (fast, ~1.5 min); the sweeps of Y_10, Y_11,
Y_12 and the roots derivation (slow, ~12 min)."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "frontier" / "B1301_the_towers_alphabet" / "verification"
sys.path.insert(0, str(HERE))


def test_the_lines_of_y9_and_y12_from_their_supports():
    import lines_from_support as LS
    r9 = LS.run(HERE / "support_Y9.json", 9, roots=HERE / "e6_roots_qul.json")
    assert r9['K'] == 145 and r9['counts'] == dict(three_gen=758593, su5_broken=737568, sm_vacua=706464, full=568656)
    assert r9['d_totals'] == [3] and r9['n_split'] == 0 and r9['proj_is_family'] and r9['ever']['D'] == 0
    assert r9['d_gen'] == {(1, 1, 1): 706464}
    assert set(k[0] for k in r9['roots_kept']) == {8}                                    # exactly the SM's SU(5) roots, always
    r12 = LS.run(HERE / "support_Y12.json", 12, roots=HERE / "e6_roots_qul.json")
    assert r12['K'] == 97 and r12['letter_orders'] == {1: 1, 16: 96}
    assert r12['counts'] == dict(three_gen=190849, su5_broken=181440, sm_vacua=34752, full=3264)
    assert r12['d_totals'] == [1, 3] and r12['n_split'] == 0 and r12['ever']['D'] == 31488 and r12['ever']['nu^c'] == 0
    assert r12['d_gen'] == {(0, 0, 1): 10496, (0, 1, 0): 10496, (1, 0, 0): 10496, (1, 1, 1): 3264}
    assert r12['hist'][(3, 3, 1, 3)] == 2304 and r12['hist'][(3, 3, 1, 0)] == 1536 and r12['hist'][(3, 3, 3, 3)] == 3264
    assert not r12['squares_are_letters'] and not r12['square_is_family']


def test_the_sweeps_of_the_small_closings_and_the_eigen_law():
    import tower_alphabet as T
    exp_support = {2: 0, 3: 3, 4: 0, 5: 20, 6: 27, 7: 56, 8: 0, 9: 147}
    for n in (2, 3, 4, 5, 6, 7, 8, 9):
        L = T.level(n, workers=3, control_orbits=5)
        assert len(L['pos']) == exp_support[n], n
        # the odd support is exactly the eigencharacters with an eigenvalue of exact order n >= 3 (primes 11, 29, 19),
        # and the eigencharacters with lambda = -1 (order-5, from the lens space Y_2) have h^1 = 0
        for (o, lam, h), cnt in L['eig'].items():
            if o == 1:
                continue
            if o == 5 and lam == 4:
                assert h == 0, (n, o, lam)
            elif o in (11, 29, 19):
                assert h == 1, (n, o, lam)
    assert L['sup_eig'] == {(19, 6): 18, (19, 16): 18, (2, None): 3, (38, None): 108}


@pytest.mark.slow
def test_y10_y11_y12_and_the_pre_registered_prediction():
    import tower_alphabet as T
    L10 = T.level(10, workers=3); L11 = T.level(11, workers=3); L12 = T.level(12, workers=3)
    assert len(L10['pos']) == 20 and len(L11['pos']) == 396 and len(L12['pos']) == 123
    assert L11['sup_eig'] == {(199, 63): 198, (199, 139): 198}
    assert L10['eig'][(55, 9, 0)] == 40 and L10['eig'][(55, 49, 0)] == 40 and L10['eig'][(11, 5, 1)] == 10
    assert L12['dist'] == {0: 103557, 1: 123}


@pytest.mark.slow
def test_the_roots_file_is_b1277s():
    import json
    import e6_roots_qul_derive as E
    out = E.derive()
    stored = json.loads((HERE / "e6_roots_qul.json").read_text())
    assert out['table27'] == {k: tuple(v) for k, v in stored['table27'].items()}
    assert sorted(r['qul'] for r in out['roots']) == sorted(tuple(r['qul']) for r in stored['roots'])
    assert out['n_su5'] == 20 and out['n_sm'] == 8
