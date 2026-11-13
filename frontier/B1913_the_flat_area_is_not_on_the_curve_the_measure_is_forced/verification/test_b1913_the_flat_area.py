"""B1913's lock. It evaluates the state at a point and at two moves of it: |f|^2 must be unchanged and |f|^2/y^2 must change
by |cz+d|^4; it plants the flat density as if it were invariant, which must fail; and it holds the page to the kept run. It
writes nothing."""
import sys, json, pathlib
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_flat_area_is_not_on_the_curve as W
PAGE = " ".join((HERE.parent / "FINDINGS.md").read_text(encoding="utf-8").split())
z = mp.mpc("0.24", "0.40")

def test_the_density_is_on_the_curve_and_the_flat_one_is_not():
    for g in ((1, 0, 5, 1), (2, -1, 5, -2)):
        w = W.mob(g, z); j4 = abs(g[2] * z + g[3]) ** 4
        assert abs(W.dens(w) / W.dens(z) - 1) < 1e-12
        assert abs(W.flat(w) / W.flat(z) - j4) / j4 < 1e-12
        assert abs(W.flat(w) / W.flat(z) - 1) > 1                    # planted: the flat density taken as invariant fails

def test_the_page_is_the_kept_run():
    k = json.loads((HERE / "the_flat_area_is_not_on_the_curve.json").read_text(encoding="utf-8"))
    assert k["|f|^2"]["distance between the two"] < 1e-9 and abs(k["|f|^2/y^2"]["distance between the two"] - 0.0654) < 5e-4
    assert "%.4f" % k["move (1, 0, 5, 1): |cz+d|^4"] in PAGE and "%.4f" % k["move (2, -1, 5, -2): |cz+d|^4"] in PAGE
    assert "0.065 apart" in PAGE
