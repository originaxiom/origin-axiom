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
