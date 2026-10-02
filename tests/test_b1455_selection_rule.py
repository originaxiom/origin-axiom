"""B1455 -- the selection rule, and the test that decides it on the bridge's vacua."""
import importlib.util, json, os, sys
from fractions import Fraction as F
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1455_the_selection_rule_and_the_deciding_test", "verification")
spec = importlib.util.spec_from_file_location("mirror_on_the_family_b1455", os.path.join(V, "mirror_on_the_family.py"))
R1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(R1)


def short_chars(g, n=7):
    out = {}; level = {"": R1.ident(4)}
    for L in range(1, n + 1):
        nxt = {}
        for w, A in level.items():
            for c in "mn":
                B = R1.mul(A, g[c]); nxt[w + c] = B; out[w + c] = R1.tr(B)
        level = nxt
    return out


def test_the_dual_of_the_vacuum_at_q_is_the_vacuum_at_one_over_q_live():
    for q in (F(2), F(7, 3)):
        T = R1.targets(q); c = {k: short_chars(v) for k, v in T.items()}
        assert c["rho_q*"] == c["rho_1/q"] and c["rho_q"] == c["rho_1/q*"]
        assert c["rho_q"] != c["rho_1/q"] and c["rho_q"] != c["rho_q*"], "the instrument separates the targets off q = 1"
    T = R1.targets(F(1)); c = {k: short_chars(v) for k, v in T.items()}
    assert c["rho_q"] == c["rho_q*"], "and they agree at the hyperbolic point"


def test_inversion_then_dual_fixes_every_vacuum_and_the_swap_fixes_it_bare_live():
    q = F(5, 2); T = R1.targets(q)
    assert short_chars(R1.pulled("iota", T["rho_q"])) == short_chars(T["rho_q*"])
    assert short_chars(R1.pulled("swap", T["rho_q"])) == short_chars(T["rho_q"])
    assert short_chars(R1.pulled("iota", T["rho_q"])) != short_chars(T["rho_q"])


def test_only_four_of_the_eight_are_automorphisms_live():
    g = R1.ballas(F(3))
    auto = sorted(s for s in R1.CANDS if R1.word(R1.apply(s, R1.REL), g) == R1.ident(4))
    assert auto == ["N,M", "id", "iota", "swap"], "the sealed prediction of eight failed"


def test_the_recorded_runs():
    d = json.load(open(os.path.join(V, "mirror_on_the_family.json")))
    assert all(v["orientation"] == "preserved" for v in d["C1"].values() if v["automorphism"]) and sum(v["automorphism"] for v in d["C1"].values()) == 4
    assert d["Theta_sigma_fixes_every_vacuum"] == {"id": False, "iota": True, "swap": False, "N,M": True}
    assert d["bare_sigma_fixes_every_vacuum"] == {"id": True, "iota": False, "swap": True, "N,M": False} and d["outside_the_family"] == []
    assert d["symbolic"]["longitude trace"] == "(3*q**4 + 1)/q**3" and d["symbolic"]["rho_q o iota ~ rho_q* on words to length 4"] is True
    f = json.load(open(os.path.join(V, "followup_index.json")))["q0 = 17 + 12 sqrt 2, twist -1"]
    assert f["I(A)"] == 0 and f["I(W1)"] == -1 and f["I(W1*)"] == 1
    assert [f["I(%s^* W1)" % s] for s in ("iota", "swap", "tau")] == [-1, -1, -1], "the count is unchanged by a rotation and by a MIRROR"
    assert [f["I(Theta_%s W1)" % s] for s in ("iota", "swap", "tau")] == [1, 1, 1], "and odd under symmetry-then-dual"
    e = json.load(open(os.path.join(V, "mirror_extension.json")))
    assert e["counts"] == {"reversing": 152, "preserving": 122} and len(e["every_reversing_map"]) == 2
    m = json.load(open(os.path.join(V, "mirror_fixes_the_counted_one.json")))
    assert m["tau (MIRROR, keeps the longitude)"]["W1(q0)"]["conjugate"] is True and m["iota (rotation, inverts the longitude)"]["W1(1/q0)"]["conjugate"] is True
    assert m["iota (rotation, inverts the longitude)"]["W1(q0)"]["conjugate"] is False
    h = json.load(open(os.path.join(V, "handoff_claims.json")))
    assert h["sturmian"]["each_is_the_fixed_point_shifted"] and not h["sturmian"]["control_other_slope_found"]
    assert h["onto_SL(2,5)"]["m004"]["surjections"] == 0 and h["onto_SL(2,5)"]["m202"]["surjections"] == 1440


def test_route_two_agrees_and_shares_no_code():
    r = json.load(open(os.path.join(V, "route2", "route2_results.json")))
    assert set(r) >= {"C0", "C1", "C2", "C2_symbolic_iota"} and r["C2_symbolic_iota"]["rho_q"]["dim"] == 0 and r["C2_symbolic_iota"]["rho_q*"]["dim"] == 1
    src = open(os.path.join(V, "route2", "route2.py")).read()
    assert "mirror_on_the_family" not in src and "nullspace" in src, "an intertwiner computation that imports nothing of Route 1"


def test_the_verdict_is_scoped_and_routed():
    v = json.load(open(os.path.join(V, "..", "arc_verdict.json")))
    assert v["verdict"] == "NEGATIVE" and v["scope"]["frame"] == "F-HE" and v["scope"]["reach"] == "single"
    kg = json.load(open(os.path.join(ROOT, "frontier", "B738_pathfinder_compiler", "kill_graph.json")))
    r = [x for x in kg if x.get("id") == "B1455"]
    assert len(r) == 1 and r[0]["scope"] == v["scope"] and "relation" in r[0]["hatch"]
