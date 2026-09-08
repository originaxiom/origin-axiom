"""B1302 — the one-triplet vacua: the survival patterns of Y_9's and Y_12's SM lines, every D&F-flat VEV configuration's
tree-level light-pair census; Y_9 never below two light colour-triplet pairs (B1283/B1300), Y_12 reaches one on 768
lines with three light doublet pairs — one vector-like generation with two Higgs doublets and no exotic triplet (~30 s)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1302_the_one_triplet_vacua" / "verification"))


def test_y9_keeps_a_light_triplet_pair_and_y12_has_one_triplet_vacua():
    import one_triplet_vacua as V
    out = V.main()
    assert out['ok']
    assert out[9]['n_patterns'] == 67 and out[9]['minT'] == 2 and out[9]['lines_solved'] == 0
    assert out[12]['n_patterns'] == 265 and out[12]['minT'] == 1 and out[12]['solved_patterns'] == 6 and out[12]['lines_solved'] == 768
    solved = [b for b in out[12]['best'] if b[1] == 1]
    assert len(solved) == 6 and all(b[4] == 128 for b in solved)
    for p, bT, cfg, lp, cnt in solved:
        s = {lab: p[i] for i, lab in enumerate(V.LABELS)}
        assert sum(s['D']) == 1 and sum(s['Dbar']) == 1 and sum(s['S']) == 1                    # D in g0, Dbar in g1, N in g2
        g0, g1, g2 = s['D'].index(1), s['Dbar'].index(1), s['S'].index(1)
        assert len({g0, g1, g2}) == 3 and cfg == (g2, None, g2)                                   # <N_g2> with the flavon pair {g0 g1}
        assert lp == {'T': 1, 'H': 3, 'Q': 1, 'u^c': 1, 'e^c': 1}
        lp2, zr, zc = V.light_pairs(s, cfg, __import__('random').Random(1), names=True)
        assert zr['T'] == [('m:d^c', g2)] and zc['T'] == [('d^c', g2)]
        assert sorted(zr['H']) == sorted([('H_u', g2), ('m:L', g2), ('m:H_d', g2)])


def test_the_one_triplet_vacuums_gauge_group_and_light_charges():
    import one_triplet_vacuum_charges as C
    out = C.main()
    assert out['ok']
    assert set(out['res'].values()) == {1, 2}
    assert all(v == 2 for k, v in out['res'].items() if k.endswith('False)')) and all(v == 1 for k, v in out['res'].items() if k.endswith('True)'))
    (v1, ch1), (v2, ch2) = out['dirs']
    assert ch1['Q'] == ch1['u^c'] == ch1['e^c'] and ch1['d^c'] == ch1['L'] and ch1['H_u'] == -ch1['H_d']
    (v3, ch3), = out['dirs_nu']
    assert ch3['nu^c'] == 0 and ch3['Q'] == ch3['u^c'] == ch3['e^c'] and ch3['d^c'] == ch3['L'] == 2 * ch3['Q'] and ch3['H_u'] == 3 * ch3['Q']


def test_the_three_generation_reading_with_the_n_vev_alone():
    import three_generation_reading as R
    out = R.main()
    assert out['ok'] and out['lp'] == {'T': 3, 'H': 5, 'Q': 3, 'u^c': 3, 'e^c': 3}


def test_the_selection_among_the_768_under_the_closings_symmetries():
    import selection_768 as Sel
    out = Sel.main()
    assert out["deck t = Psi^2"] == (64, {12: 64}) and out["deck and half-deck <Psi>"] == (32, {24: 32})
    assert out["<Psi, J>"] == (8, {96: 8}) and out["<Psi, J, inversion>"] == (8, {96: 8})
    assert out["all SM lines <Psi, J, inversion>"] == (388, {48: 52, 96: 336})
