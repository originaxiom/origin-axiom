"""B1677 -- the common point and the count of records (sealed). Live: the sealed instrument at n = 2 and 3 for Q8, 2T,
2I and Dic3-Dic6 -- the quaternion character is the one common point at n = 2 (the positive control, and the bite: the
instrument does find a common point where one exists), none at n = 3; the argument that Dic_m (m >= 3) forces trace zero.
Stored: the full run (n = 4 included) and its cells."""
import importlib.util, json, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1677_the_common_point_and_the_record_count"


def _cp():
    spec = importlib.util.spec_from_file_location("cp", A / "verification" / "the_common_point.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_rank_two_has_the_quaternion_point_and_rank_three_none():
    cp = _cp(); G = cp.groups()
    for n, name, expect in [(2, "Dic2", 1), (2, "2T", 0), (2, "2I", 0), (3, "Dic2", 0), (3, "2T", 0), (3, "2I", 0)]:
        cp.ORDERS_CUR[0] = cp.ORDERS[name]
        found, tested = cp.common_points(G[name], n)
        assert len(found) == expect, (n, name, len(found))
        if expect: assert all(abs(x) < 1e-9 for x in found[0]["traces"])        # the quaternion point (0, 0, 0)
    for m in (3, 4, 5, 6):                                                        # Dic_m: no filtered generating pair
        cp.ORDERS_CUR[0] = cp.ORDERS[f"Dic{m}"]
        assert cp.common_points(G[f"Dic{m}"], 2) == ([], 0)


def test_the_sealed_run():
    d = json.load(open(A / "verification" / "the_common_point.json"))
    assert all(d["cells"].values()) and len(d["cells"]) == 3
    assert len(d["groups"]["n=2 Dic2"]["common points"]) == 1
    assert all(not v["common points"] for k, v in d["groups"].items() if not k.startswith("n=2 Dic2"))
    assert d["groups"]["n=3 2I"]["tuples passing the filter and generating"] == 240
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"
