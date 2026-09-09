"""B1323 -- the genesis upgrades: the DESIGN is sealed; U3 (dictionary) and U2 (criterion census) PASS with their key facts pinned;
U1 (fork F9) is ROBUST on both carriers with the m004 control green, the minimal three-record toral closure is the cube of the
plastic number, the minimal three-record surface bundle is m129 (chiral by two methods) and the record-swap/reflection distinction
is pinned; U2 and U3 re-run live under OA_SLOW."""
import hashlib, json, os, subprocess, sys
from pathlib import Path
import pytest
ROOT = Path(__file__).resolve().parents[1]; ARC = ROOT / "frontier" / "B1323_the_genesis_upgrades"; V = ARC / "verification"


def _j(name):
    return json.loads((V / name).read_text(encoding="utf-8"))


def test_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")


def test_u3_dictionary_lemma_pinned():
    j = _j("u3_dictionary.json"); assert j["PASS"]
    i = j["i"]; assert i["matrices_not_in_GL2Z"] == 0 and i["matrices_not_nonneg"] == 0 and i["matrices_not_in_LRP_monoid"] == 0
    assert i["nonneg_GL2Z_entries_le_13"] == 462 and i["realised_by_St"] == 462 and i["not_realised"] == 0
    ii = j["ii"]; assert ii["M(Fib) == L.P"] and ii["(LP)^2 == LR == A"] and ii["(PL)^2 == RL"] and ii["PLP == R"] and ii["LR and RL conjugate by P"]
    assert list(ii["fp coefficients LR (r, s-p, -q)"]) == [1, -1, -1] and list(ii["fp coefficients RL"]) == [1, 1, -1]
    assert j["iii"]["isometric to m004"] is True and j["iii"]["a*B cusps"] == 1
    assert j["iv"]["cutting == fib"] is True and j["iv"]["cf(1/phi)"][1:11] == [1] * 10


def test_u2_criterion_census_pinned():
    j = _j("u2_criterion_census.json"); assert j["census"]["PASS"]
    assert j["K1"]["is_sqrt5"] and j["K1"]["tied_periods"] == [[1]] and j["K1"]["is_2sqrt2_second"]
    assert j["K3"]["class_number_h+(5)"] == 1 and j["K3"]["first_trace_gt_2"] == 3
    assert j["K4"]["torsion_free_closures"] == [[1, 1]]
    assert list(j["K5"]["fundamental"]) == [1, 1, 1] and list(j["K5"]["fricke"]) == [3, 3, 3]
    assert j["K6"]["smallest_disc"] == 5 and j["K7"]["is_phi"]
    assert j["K8"]["is_plastic"] and not j["K8"]["is_phi"] and j["K8"]["below_phi"] and list(j["K8"]["coeffs"]) == [0, -1, -1]


def test_u1_fork_f9_pinned():
    j = _j("u1_substrate_count.json")
    assert j["F9"] == {"toral": "ROBUST by theorem (exhibited)", "surface": "ROBUST", "control_PASS": True}
    b = j["b"]; assert b["all_chi_zero"] and b["chi_values"] == [0] and b["min_trace_mixed_hyperbolic"] == 3 and b["mixed_hyperbolic"] == 162
    assert [round(x, 6) for x in b["minimal_examples"][0]["eig_moduli"]] == [0.655866, 0.655866, 2.324718]
    c = j["c"]; assert c["carriers_with_H1_rank_3"] == [[0, 4], [1, 2], [2, 0]]
    ctrl = c["control_S_1_1_aB"]; assert ctrl["is_m004"] and ctrl["amphichiral"] and ctrl["shape_field_Q(sqrt-3)"]
    assert ctrl["self_isometries"] == {"isometries": 8, "orientation_preserving": 4, "orientation_reversing": 4}
    assert c["keepers_of_Q(sqrt-3)"] == [] and c["three_line_class_members"] == []
    s12 = {r["word"]: r for r in c["results"]["S_1_2"]["classes"]}; s04 = {r["word"]: r for r in c["results"]["S_0_4"]["classes"]}
    m129 = s12["abC"]; assert "m129(0,0)(0,0)" in m129["identify"] and m129["cusps"] == 2 and abs(m129["volume"] - 3.6638623767088) < 1e-9
    assert m129["amphichiral"] is False and m129["amphichiral_by_isometry"]["amphichiral"] is False
    assert m129["self_isometries"] == {"isometries": 8, "orientation_preserving": 8, "orientation_reversing": 0}
    assert m129["vs_record_swap"]["orientation_preserving"] == 8 and m129["vs_mirror_word"]["orientation_reversing"] == 8 and m129["vs_mirror_word"]["orientation_preserving"] == 0
    assert m129["shape_field"]["all_in_Q(sqrt-3)"] is False and sorted(map(tuple, m129["shape_field"]["min_polys"])) == [(1, -2, 2), (1, 0, 1), (2, -2, 1), (2, -2, 1)]
    t = s04["aB"]; assert "t12047(0,0)(0,0)(0,0)(0,0)" in t["identify"] and t["amphichiral"] is True and t["sym_order"] == 64 and t["cusps"] == 4
    assert "s780(0,0)(0,0)" in s12["acB"]["identify"] and s12["acB"]["amphichiral"] is False
    assert c["mirror_test"]["PASS_A (minimal hyperbolic three-record bundle is chiral)"] is True


def test_three_record_minimal_closure_is_the_plastic_number_cubed():
    """exact: the minimal-trace mixed hyperbolic closure E12.E31.E23 has characteristic polynomial t^3 - 3t^2 + 2t - 1,
    which is the minimal polynomial of rho^3 for rho the plastic number (x^3 - x - 1) -- the three-record analogue of A = (golden)^2."""
    import sympy as sp
    t, x = sp.symbols('t x')
    E = lambda i, j: sp.eye(3) + sp.Matrix(3, 3, lambda a, b: 1 if (a, b) == (i - 1, j - 1) else 0)
    B = E(1, 2) * E(3, 1) * E(2, 3)
    cp = sp.factor(B.charpoly(t).as_expr())
    assert sp.expand(cp - (t ** 3 - 3 * t ** 2 + 2 * t - 1)) == 0
    # rho^3 = rho + 1: the minimal polynomial of rho^3 is the resultant of x^3 - x - 1 and t - x^3 in x
    mp_rho3 = sp.factor(sp.resultant(x ** 3 - x - 1, t - x ** 3, x))
    assert sp.expand(mp_rho3 - (t ** 3 - 3 * t ** 2 + 2 * t - 1)) == 0 or sp.expand(mp_rho3 + (t ** 3 - 3 * t ** 2 + 2 * t - 1)) == 0
    assert B.det() == 1 and (B - sp.eye(3)).det() in (1, -1)


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="live re-run of U3 and U2 (about half a minute)")
def test_live_reruns_u3_u2():
    for script in ("u3_dictionary.py", "u2_criterion_census.py"):
        r = subprocess.run([sys.executable, str(V / script)], capture_output=True, text=True, cwd=str(V), timeout=900)
        assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
