"""B1808 -- three generations cut a curve, not a point (P-419): the committed run's lattice and curves."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1808_three_generations_cut_a_curve_not_a_point" / "verification"


def test_the_invariant_lattice_and_the_curves():
    r = json.loads((V / "three_generations_in_f2h.json").read_text(encoding="utf-8"))
    lr = r["LR"]
    assert lr["rank Lambda_A"] == 4 and lr["det Q"] == 5 and lr["signature (+,-)"] == [2, 2]
    for c in lr["the (1,1) curves of the first six such classes"]:
        assert (float(c["det M_w (sign: >0 a curve in H^2)"]) > 0) == (c["chi"] == -3)
    for t in (4, 5, 6, 7):
        assert r["B_%d" % t]["det Q"] == t * t - 4 and r["B_%d" % t]["signature (+,-)"] == [2, 2]
