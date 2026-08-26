"""B1150 lock -- the yukawa-reads-the-clock + three-family-yukawa harvest: cloud memos 52-53
reproduce-verified. The unique coupling's depth-selection is the representation-theoretic maximum
(7 of 7 allowed blocks, odd total depth); and in the E8 possibility-space the three-family Yukawa is
epsilon_family (x) the Jordan cubic, so same-family couplings vanish by root arithmetic. memo 53's
family=epsilon independently sympy-confirmed. Kinematics only; Gate 5 untouched."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1150_yukawa_clock_and_family"


def _d():
    return json.loads((ARC / "b1150_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_proved():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1150" and d["verdict"] == "PROVED"


def test_both_reproduced():
    r = _d()["reproduce"]
    assert r["failures"] == 0 and r["byte_identical_verdict"] == r["total_certs"] == 2
    assert r["rc_zero"] == 2                                               # rc=0 = every preregistered assert GREEN


def test_reproduce_evidence_present():
    log = (ARC / "verification" / "reproduce.log").read_text(encoding="utf-8")
    assert log.count("REPRODUCES") == 2 and "SUMMARY: 2 reproduce" in log


def test_yukawa_reads_the_clock():
    m = _d()["memos"]["52"]
    assert "7 sl2-allowed depth blocks" in m and "11 forbidden" in m      # the depth selection
    assert "representation-theoretic MAXIMUM" in m and "ODD" in m         # not a tautology; the parity law
    assert "NOT a tautology" in m


def test_three_family_yukawa_possibility_space():
    m = _d()["memos"]["53"]
    assert "POSSIBILITY-SPACE" in m and "NOT object-paid" in m            # the fence up front
    assert "eps_family (x) C_Jordan" in m and "same-family" in m          # the inter-family texture
    assert "ZERO" in m and "root-lattice level" in m                      # diagonal empty by arithmetic


def test_sl3_independent_check_and_fences():
    d = _d()
    assert "dim Inv = 1" in d["memos"]["sl3_check"] and "ANTISYMMETRIC" in d["memos"]["sl3_check"]
    ic = (ARC / "verification" / "independent_check_memo53.txt").read_text(encoding="utf-8")
    assert "dim Inv_sl3(3 x 3 x 3) = 1" in ic and "CONFIRMED" in ic
    assert "POSSIBILITY-SPACE" in d["fences"] and "no value" in d["fences"]   # E8 fence + Gate 5
