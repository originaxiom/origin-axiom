"""B1279 — the symmetries of the closing on its Standard-Model lines: the eight isometries of m004 as automorphisms
of the presentation (fast), and (slow) their lifts to Y_3, Y_6, Y_9, the golden eigenlines mod 19, the 19 624 orbits
of the 706 464 SM lines, the mirror pairing."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
for arc in ("B1267_spectrum_law_rebuilt", "B1268_cusped_net_chirality_bound", "B1269_transport_computed",
            "B1273_the_three_fold_closing", "B1274_the_tower_and_its_doubles", "B1275_the_cubic_made_explicit",
            "B1276_the_relations_the_chain_forces", "B1277_the_vacuum_manifold_of_the_closing",
            "B1278_the_six_fold_closing", "B1279_the_symmetries_of_the_closing"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))


def test_the_eight_isometries_are_automorphisms_of_the_presentation(capsys):
    import symmetries_on_the_lines as X
    classes, t_lam = X.part_a()
    text = capsys.readouterr().out
    assert len(classes) == 8 and abs(abs(t_lam) - 2 * 3 ** 0.5) < 1e-9
    W = {1: 'a', -1: 'A', 2: 'b', -2: 'B'}
    words = {key: (''.join(W[x] for x in u), ''.join(W[x] for x in v), o) for key, (u, v, o) in classes.items()}
    assert words[((-1, -1), (0.0, 0.0))] == ('A', 'B', 1)                 # the inversion
    assert words[((1, 1), (0.0, 0.5))] == ('b', 'a', 1)                   # the period-2 swap (half the longitude)
    assert {words[k][2] for k in words if k[0] in ((-1, 1), (1, -1))} == {-1}   # the four orientation-reversing ones
    assert {words[k][2] for k in words if k[0] in ((1, 1), (-1, -1))} == {1}
    assert "distinct outer classes found (cusp map, translation part (b_mu, b_lam)): 8" in text


@pytest.mark.slow
def test_the_mirror_pairs_the_standard_model_vacua(capsys):
    import symmetries_on_the_lines as X
    out = X.main()
    text = capsys.readouterr().out
    assert out['n_sm'] == 706464 and out['group'] == 72 and out['orbits'] == 19624
    assert sorted(out['roots19']) == [6, 16]
    assert "Y_3: H_1 = Z/4 + Z/4; the actions of the eight lifts and of the deck t on the 16 characters are well defined; the group they generate has order 24" in text
    assert "the group they generate has order 48" in text
    assert "(0, 706464)" in text                                             # the period-2 swap inverts every line
    assert "(353232, 353232)" in text                                        # one glide lift: one eigenline fixed, the other inverted
