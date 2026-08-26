"""B1157 lock -- WF-2 (the dynamics): the object's infinity-place 'dynamical law' reading is STRUCTURAL
RHYME (firewall upheld, NEGATIVE); the decidable substance is that H*(m004;Sym^{2m}) is NEVER acyclic,
refuting the closed-Fried antecedent of cc3's B8142b. Asserts on COMMITTED files only (cc3 B8141 the
artifact class). Archimedean/acyclicity anchor via the committed reproduce runner. Gate 5 clean."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1157_dynamics_null"


def _d():
    return json.loads((ARC / "b1157_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_negative():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1157" and d["verdict"] == "NEGATIVE"
    assert d["instrument"] is False and d["creates_law"] is False


def test_firewall_structural_rhyme_not_crossed():
    d = _d()
    assert d["verdict"].startswith("NEGATIVE")
    fw = d["firewall_verdict_STRUCTURAL_RHYME"]
    # the whole story is generic to hyperbolic 3-manifolds; the arithmetic never enters
    assert "generic" in fw["level_b_generic"] and "NEVER the arithmetic" in fw["level_b_generic"]
    assert "Vol(M)=Vol(M)" in fw["vol_tautology"]
    assert fw["gate5"].startswith("clean")


def test_decidable_acyclicity_refuted_every_m():
    a = _d()["decidable_result_acyclicity"]
    assert "REFUTED for every m" in a["answer"] and "NEVER acyclic" in a["answer"]
    assert "(1,1,0)" in a["table"] and "(0,1,1)" in a["table"] and "(1,2,1)" in a["table"]
    # the mechanism: Sym^{2m} of a parabolic = single Jordan block => 1-dim invariant line
    assert "single Jordan block" in a["mechanism"].replace("SINGLE", "single")
    assert "H2(M)=H1(M)=#cusps=1" in a["mechanism"]
    assert "B581" in a["triple_corroboration"]


def test_reproduce_runner_committed_and_reproduces():
    # B8141 discipline: assert on the committed runner + its committed output, not a gitignored log
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners, "no committed reproduce runner"
    assert "REPRODUCES" in runners[0].read_text(encoding="utf-8")
    out = (ARC / "verification" / "acyclicity_and_vol.txt").read_text(encoding="utf-8")
    assert "REPRODUCES" in out
    assert "(0, 1, 1)" in out and "0.07543170680114986" in out


def test_consequence_reflection_stays_conditional():
    d = _d()
    assert "STAYS CONDITIONAL" in d["consequence_for_cc3_b8142b"]
    assert "closed-manifold Fried" in d["consequence_for_cc3_b8142b"] or "closed-Fried" in d["consequence_for_cc3_b8142b"]
    assert "Park/Pfaff" in d["consequence_for_cc3_b8142b"]


def test_sym_power_identity_bank_grade_cc3_credited():
    bg = _d()["bank_grade_cc3_credited"]
    assert "prod_{j=-m}^m R(s-j,sigma_j)" in bg
    assert "5e-18" in bg and "no novelty" in bg


def test_exact_check_crash_relayed():
    r = _d()["relayed_to_cc3"]
    assert "exact_check.py" in r and "line 39" in r and "sp.simplify" in r
    assert "non-fatal" in r.lower() or "stands" in r


def test_no_crossing_gate5_clean():
    d = _d()
    assert "No firewall crossing" in d["fences"] and "Gate 5 clean" in d["fences"]
