"""B1209 — the Lee verification. The locks pin what THIS bench derived, not what the paper says."""
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1209_lee_verification"

# the figure-eight A-polynomial (main's B67): A(M,L) = -M^4 + L(1-M^2-2M^4-M^6+M^8) - L^2 M^4
MONOMIALS = [(4, 0), (0, 1), (2, 1), (4, 1), (6, 1), (8, 1), (4, 2)]


def _hull(points):
    pts = sorted(set(points))
    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2:
                (x1, y1), (x2, y2) = out[-2], out[-1]
                if (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1) <= 0: out.pop()
                else: break
            out.append(p)
        return out
    lo, up = half(pts), half(pts[::-1])
    return lo[:-1] + up[:-1]


def _edges():
    H = _hull(MONOMIALS)
    out = []
    for i in range(len(H)):
        (x1, y1), (x2, y2) = H[i], H[(i + 1) % len(H)]
        dM, dL = x2 - x1, y2 - y1
        g = gcd(abs(dM), abs(dL)) or 1
        out.append((dL // g, dM // g))          # (a_1, b_1)
    return out


def test_a1_is_one_at_every_ideal_point_of_the_figure_eight():
    """The load-bearing fact, derived from OUR A-polynomial rather than read from the paper:
    the admissible-tangent-vector torsor has order |a_1|, and every Newton edge is L-thin."""
    a1s = [abs(a) for a, _ in _edges()]
    assert len(a1s) == 4, "the figure-eight has four ideal points"
    assert set(a1s) == {1}, f"|a_1| must be 1 at every ideal point; got {a1s}"


def test_the_boundary_slopes_are_plus_minus_four():
    """The cross-check that the Newton reading is the right reading: b_1/a_1 must reproduce the
    figure-eight's known non-zero boundary slopes."""
    slopes = {b / a for a, b in _edges() if a}
    assert slopes == {4.0, -4.0}, slopes


def test_the_torsor_group_is_trivial_so_it_is_not_the_observer_bit():
    """The kill: a trivial group cannot be the programme's Z/2. If a future edit ever made |a_1|
    exceed 1 here, the bridge would reopen and this lock should fail."""
    order = max(abs(a) for a, _ in _edges())
    assert order == 1
    assert order not in (2, 4), "Z/2 or V_4 would be direct contact with B1174/B1182"


def test_the_arc_records_all_three_answers_and_keeps_the_positive_half():
    r = json.loads((ARC / "b1209_results.json").read_text(encoding="utf-8"))
    a = r["answers"]
    assert set(a) == {"Q1_torsor", "Q2_cs_zero", "Q3_trace_field"}
    assert a["Q1_torsor"]["abs_a1_at_every_ideal_point"] == 1
    assert a["Q1_torsor"]["contact_with_the_observer_bit"] is False
    assert a["Q2_cs_zero"]["answer"] == "NO"
    assert a["Q3_trace_field"]["k_m004"] == "Q(sqrt-3)"
    # the negative must not swallow the positive: the motive over our own field still stands
    assert "Beilinson regulator" in r["net"]["positive_half"]
    assert r["net"]["W0_bar"].startswith("UNCHANGED")


def test_the_negative_is_routed_in_the_kill_graph():
    """B1207 caught this backlog rebuilding; the routing lands in the same commit as the arc."""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json")
                    .read_text(encoding="utf-8"))
    row = next(r for r in kg if r.get("id") == "B1209")
    assert row["fact_computed"] is True
    assert "torsor" in row["kill_form"]
    assert "A-polynomial" in row["hatch"], "the hatch must name the two-line reopening check"
