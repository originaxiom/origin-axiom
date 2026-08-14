"""B907 locks. Pre-results: the seal. Results locks appended at banking."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B907_real_form_selector")
SEALED_SHA = "cd7aae3b1e102359f40fa0e6d3db12a08d68517bff263dd2f7f80548ba518690"


def test_prereg_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA


def _verdict():
    import json
    with open(os.path.join(ARC, "verdict.json")) as f:
        return json.load(f)


def test_exactly_two_wall_real_involutions_both_e62():
    v = _verdict()
    assert len(v) == 2
    for row in v:
        assert row["kind"] == "outer"
        assert row["eps"] == {"8": -1, "14": 1, "16": -1, "22": 1}
        assert row["phi_involution_samples"] is True
        assert row["composite_fixed_dim"] == 38
        assert row["form"] == "e6(2)"


def test_the_two_are_global_negations():
    v = _verdict()
    s1, s2 = v[0]["signs"], v[1]["signs"]
    assert [a*b for a, b in zip(s1, s2)] == [-1]*6


def test_inner_e6m14_class_obstruction():
    import json
    with open(os.path.join(ARC, "sweep_results.json")) as f:
        r = json.load(f)
    rows46 = [row for row in r["inner"] if row["fixed_dim"] == 46]
    assert len(rows46) == 27
    assert all(not row["C_compatible"] for row in rows46)


def test_completeness_verified_flag():
    import json
    with open(os.path.join(ARC, "completeness_verify_results.json")) as f:
        r = json.load(f)
    txt = json.dumps(r)
    assert "fail" not in txt.lower() or '"failures": 0' in txt or '"failed": 0' in txt


def test_sign_locking_survivors():
    import json
    with open(os.path.join(ARC, "completeness_results.json")) as f:
        r = json.load(f)
    txt = json.dumps(r)
    assert "(-1, 1, -1, 1)" in txt or "[-1, 1, -1, 1]" in txt
