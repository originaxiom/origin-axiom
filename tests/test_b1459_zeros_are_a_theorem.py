"""B1459 -- the zeros at the complete points are a theorem, not a census."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1459_the_zeros_are_a_theorem")
V = os.path.join(A, "verification")


def test_the_sealed_run_live_on_one_level_and_its_record():
    r = subprocess.run([sys.executable, os.path.join(V, "zeros_are_a_theorem.py"), "--quick"], capture_output=True, text=True, cwd=V)
    assert r.returncode == 0 and "VERDICT zeros-are-a-theorem: PASS" in r.stdout, r.stdout[-400:] + r.stderr[-400:]
    q = json.load(open(os.path.join(V, "zeros_are_a_theorem_quick.json")))
    assert q["points"] == 12 and q["eps_plus"] == 12 and q["failures"] == [] and all(row["index"] == 0 for row in q["levels"][0]["rows"])
    d = json.load(open(os.path.join(V, "zeros_are_a_theorem.json")))
    assert d["points"] == 188 and d["eps_plus"] == 188 and d["eps_minus"] == 0 and d["factor_signs"] == {"+1": 376, "-1": 0} and d["failures"] == []
    assert len(d["levels"]) == 16 and d["theorem_holds_on_every_point"]


def test_the_geometric_sign_record_both_branches_used():
    g = json.load(open(os.path.join(V, "geometric_sign.json")))
    assert g["pass"] and g["points"] == 188 and g["failures"] == []
    assert (g["eps_geo_plus"], g["eps_geo_minus"]) == (111, 77) and g["factor_signs"] == {"+1": 239, "-1": 137}
    assert len(g["twisted"]) == 77 and all(t["index_of_V_eps"] == 0 and t["cusp_invariants_of_V_eps"] == 0 for t in g["twisted"])
    assert all(isinstance(lv["c"], list) and len(lv["c"]) > 0 for lv in g["levels"])      # one word c per level, found and unique
    c = json.load(open(os.path.join(V, "twisted_branch_control.json")))
    assert c["pass"] and c["points"] == 12 and all(r["cusp_invariants_V"] >= 1 and r["cusp_invariants_V_eps"] == 0 and r["index_V_eps"] == 0 for r in c["rows"])


def test_the_word_conjugacy_solver_bites():
    sys.path.insert(0, V); sys.argv = [sys.argv[0]]
    import geometric_sign as G
    u = (1, 2, -1, 2); v = (2, -1, 2, 1)                                # v = x^-1 u x
    assert any(G.ce.reduce_word(c + u + G.ce.inv_word(c)) == v for c in G.conjugators(u, v))
    assert G.conjugators((1, 2), (1, -2)) == [] and G.conjugators((1, 2, 1), (1, 2)) == []     # not conjugate: nothing returned
    # the engine's own iota (for negative states) is an inner twist of the bare inversion: same word length structure
    assert G.iota((1, 2, -1)) == (-1, -2, 1)
