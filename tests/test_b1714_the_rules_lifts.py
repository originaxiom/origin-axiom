"""B1714 -- the rule's lifts (P-225). Stored: only the common point and the central characters are fixed by two of the
rule, L and R; the rule's lifts at the common point have orders 3 and 6 and T-type eigenvectors. Live: the trace maps'
fixed points by exact substitution, and the T-type Bloch vectors from the stored lifts."""
import itertools, json, math, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1714_the_rules_lifts" / "verification"


def _d():
    return json.loads((A / "the_rules_lifts.json").read_text(encoding="utf-8"))


def test_stored():
    d = _d()
    assert d["only_common_point_and_central"] and d["rule_fixes_two_points_per_twist"] and d["all_eigenvectors_T_type"]
    assert d["orders"] == [3, 6]
    for pts in d["points_fixed_by_two"].values():
        assert len(pts) == 5 and ["0", "0", "0"] in pts


def test_live_fixed_points():
    rule = lambda x, y, z: (z, x, x * z - y)
    L = lambda x, y, z: (x, z, x * z - y)
    R = lambda x, y, z: (z, y, y * z - x)
    pts = [(0, 0, 0)] + [(2 * a, 2 * b, 2 * a * b) for a in (1, -1) for b in (1, -1)]
    for p in pts:
        for f in (rule, L, R):
            img = f(*p)
            assert any(img == (e1 * p[0], e2 * p[1], e1 * e2 * p[2]) for e1, e2 in itertools.product((1, -1), repeat=2))
    # a control: a generic point is fixed by none of the three under any twist
    p = (0.3, 1.1, -0.7)
    for f in (rule, L, R):
        img = f(*p)
        assert not any(all(abs(u - v) < 1e-12 for u, v in zip(img, (e1 * p[0], e2 * p[1], e1 * e2 * p[2])))
                       for e1, e2 in itertools.product((1, -1), repeat=2))


def test_live_t_type():
    for v in _d()["lifts_at_common_point"].values():
        assert v["kernel_sv"] < 1e-12 < v["next_sv"]
        q = v["quaternion"]
        assert abs(sum(c * c for c in q) - 1) < 1e-12 and all(abs(abs(c) - 0.5) < 1e-12 for c in q)
        for b in v["bloch"]:
            assert all(abs(abs(c) - 1 / math.sqrt(3)) < 1e-12 for c in b)
