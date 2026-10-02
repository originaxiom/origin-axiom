"""B1454 -- GENESIS v1.0 verified on main and adopted as v1.1."""
import hashlib, importlib.util, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1454_genesis_v1_verified_and_adopted")


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(A, rel))
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m); return m


go = load("verification/genesis_own.py", "genesis_own_b1454")


def test_the_algebra_live():
    for f in (go.g1, go.g2, go.g3, go.g4, go.g8_algebra, go.g9, go.g10, go.g11):
        ok, data = f(); assert ok, f.__name__
    _, d = go.g2(); assert (d["hyperbolic_det_plus"], d["hyperbolic_det_minus"], d["torsion_free"]) == (168, 240, 48)
    assert d["by_class"] == {"LR": 16, "LP": 16, "LP^-1": 16} and d["traces_of_torsion_free_det_minus"] == [-1, 1]
    _, d = go.g4(); assert d["total"] == 758 and d["torsion_free"] == ["+LR"] and d["counts"] == d["by_formula"]
    _, d = go.g1(); assert d["without_positivity"] == [(-1, -1), (1, 1)] and go.det(d["conjugator_of_B_minus1_minus1_to_LR"]) == 1


def test_the_witnesses_are_witnesses():
    """each input of the root is needed: the witness satisfies the criterion and fails the dropped input"""
    E = ((1, 1), (-1, 0))
    assert go.torsion(E) == 1 and not go.hyperbolic(E) and go.power(E, 6) == go.I2          # without aperiodicity
    assert go.smith(go.minus_identity(go.L)) == (1, 0) and not go.hyperbolic(go.L)
    LP = go.mul(go.L, go.P)
    assert go.det(LP) == -1 and go.torsion(LP) == 1 and go.hyperbolic(LP) and go.mul(LP, LP) == go.mul(go.L, go.R)   # without orientation
    assert go.torsion(go.neg(go.mul(go.L, go.R))) == 5                                    # the sister is not torsion-free


def test_the_order_bit_and_the_bite():
    L, R, P = go.L, go.R, go.P
    assert go.mul(go.mul(go.inv(L), go.mul(L, R)), L) == go.mul(R, L) and go.det(L) == 1 and go.det(P) == -1
    # the check can fail: a non-golden matrix is not reported as golden, and a wrong count is not reproduced
    assert set(go.cf_period(go.mul(go.power(L, 2), go.power(R, 2)))) == {2}
    assert go.count_formula(8) * 2 == 32 and go.count_formula(8) * 2 != 34
    assert go.conjugator(go.mul(L, R), go.mul(go.power(L, 2), R)) is None


def test_the_recorded_runs():
    d = json.load(open(os.path.join(A, "verification", "genesis_own.json")))
    assert len(d) == 9 and all(v["ok"] for v in d.values())
    s = d["G5-G7 SnapPy"]["data"]
    assert s["torsion_free_among_them"] == ["m000"] and s["orientation_reversing_codes_read"] == 252 and s["torsion_is_abs_trace_of_wP"]
    assert s["level_names"] == {"2": ["m206"], "3": ["s961"], "4": ["t12839"], "5": ["o10_150696"], "6": ["otet12_00013"]}
    assert s["states_to_length_six"]["+LR"] == "m004" and s["states_to_length_six"]["-LLRLR"] == "m369" and len(s["states_to_length_six"]) == 24
    c = json.load(open(os.path.join(A, "verification", "citations.json")))
    assert len(c["rows"]) == 47 and all(r.get("found_in") or r.get("absent") for r in c["rows"])
    assert c["path_registry"] == {"IN-PROGRESS": 3, "DEAD": 1, "UNTOUCHED": 18, "STALLED": 3}


def test_the_citations_live():
    r = subprocess.run([sys.executable, os.path.join(A, "verification", "citations.py")], capture_output=True, text=True)
    assert r.returncode == 0 and "VERDICT genesis-citations: PASS (45 citations, 2 controls)" in r.stdout, r.stdout[-600:]


def test_the_page_is_the_received_text_with_the_listed_changes():
    am = load("adoption/amend.py", "amend_b1454")
    raw = open(os.path.join(A, "received", "GENESIS_v1_0.md"), "rb").read()
    assert hashlib.sha256(raw).hexdigest() == am.SHA_V1_0
    t, k = am.build(); cur = open(os.path.join(ROOT, "GENESIS.md")).read()
    if "**Version 1.1 ·" in cur: assert cur == t
    assert len(am.CHANGES) == 23 and k == 58 and t.count("[v1.1]") >= 20
    for needle in ("| F-MC **[v1.1]** | McKay cascade frame", "κ names two quantities", "cannot: its fibre has no finite character", "- **v1.1 · 2026-10-02 · main B1454.**"):
        assert needle in t, needle
    assert "cannot, since its fibre" not in t and "which the architecture does not have." not in t


def test_the_corrections_on_main():
    u = open(os.path.join(ROOT, "docs", "UNIQUENESS_THEOREM.md")).read()
    assert "conjugate in `SL(2,ℤ)` by `L`" in u and "`SL(2,ℤ)`-conjugate via the\nrecord-swap" not in u
    t = open(os.path.join(ROOT, "docs", "THEOREM_LEDGER.md")).read()
    assert "18 UNTOUCHED" in t and "17 UNTOUCHED" not in t
    v = json.load(open(os.path.join(A, "arc_verdict.json")))
    assert set(v["scope"]) == {"frame", "object", "reach", "hypotheses"} and v["scope"]["reach"] == "general"
