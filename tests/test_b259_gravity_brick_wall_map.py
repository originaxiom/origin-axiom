"""B259 locks -- the gravity brick (Mostow metric solves 3d Einstein with Lambda=-1) + the honest five-wall map
(exactly one THEOREM, the rest open/quantitative gaps). MATH firewall-clean; physics reading -> S043; nothing to
CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B259_gravity_brick_wall_map" / "gravity_brick.py"
_spec = importlib.util.spec_from_file_location("b259", _PATH)
b259 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b259)


def test_mostow_metric_solves_3d_einstein():
    ratios, Rscal, Lam = b259.ricci_of_constant_curvature_3d()
    assert ratios == [-2, -2, -2]   # Ric = -2 g
    assert Rscal == -6              # scalar curvature of H^3
    assert Lam == [-1]             # 3d vacuum Einstein forces Lambda=-1: hyperbolic IS Einstein


def test_five_wall_map_is_one_theorem_not_all_walled():
    # the honest correction to "walled by theorem": exactly ONE wall is a theorem
    theorems = [k for k, w in b259.WALLS.items() if w["status"].startswith("THEOREM")]
    assert theorems == [1]                      # only the holonomy-breaking embedding is a theorem
    assert any("QGAP" in w["status"] for w in b259.WALLS.values())   # #5 the 122-order scale gap
    opens = [k for k, w in b259.WALLS.items() if w["status"].startswith("OPEN")]
    assert set(opens) == {2, 3, 4}              # the rest are uncomputed gaps, not impossibilities


def test_every_wall_has_an_open_reframing_or_framework():
    # no wall is left as a bare negative -- each carries the published framework that could bridge it
    for w in b259.WALLS.values():
        assert w["open_reframing"] and len(w["open_reframing"]) > 20
