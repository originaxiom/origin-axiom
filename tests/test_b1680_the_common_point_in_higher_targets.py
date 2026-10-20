"""B1680 -- the common point in targets of higher rank (sealed). Live: the sealed instrument at n = 2 on H(3) (every
generating pair fixed: the positive control and the bite) and on A4 and Delta(54) (none), and at n = 3 on H(3) (every
filtered triple moved). Stored: the full run and its cells."""
import importlib.util, json, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1680_the_common_point_in_higher_targets"


def _h():
    spec = importlib.util.spec_from_file_location("h", A / "verification" / "the_common_point_in_higher_targets.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_live_controls_and_rank_three():
    h = _h(); T = h.targets()
    assert h.common_points(T["H(3) (U3)"], 2, 27) == (432, 432)
    assert h.common_points(T["A4 (SO3)"], 2, 12)[0] == 0 and h.common_points(T["Delta54 (SU3)"], 2, 54)[0] == 0
    found, tested = h.common_points(T["H(3) (U3)"], 3, 27)
    assert (found, tested) == (0, 3888)


def test_the_sealed_run():
    d = json.load(open(A / "verification" / "the_common_point_in_higher_targets.json"))
    assert all(d["cells"].values()) and len(d["cells"]) == 3
    assert d["n=2 targets with a common point"] == ["n=2 Q8 (SU2)", "n=2 H(3) (U3)", "n=2 H(5) (U5)"]
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"
