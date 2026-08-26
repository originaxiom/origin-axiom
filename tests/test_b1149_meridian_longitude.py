"""B1149 lock -- the meridian & longitude harvest: cloud memos 49-51 reproduce-verified. The carrier's
peripheral (cusp) structure IS the matter grading -- the meridian supplies the clock (nilpotency 3,
matter = odd Jordan chains), the longitude supplies the sign (its semisimple part = the lock); the
24-dim matter sector is now 4x-overdetermined. Above it, the atlas's two arithmetic ends are unified as
the unit and ramified answers to one trace-3 form. Kinematics only; Gate 5 untouched."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1149_meridian_longitude_harvest"


def _d():
    return json.loads((ARC / "b1149_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_proved():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1149" and d["verdict"] == "PROVED"


def test_all_three_reproduced():
    r = _d()["reproduce"]
    assert r["failures"] == 0 and r["byte_identical_verdict"] == r["total_certs"] == 3
    assert r["rc_zero"] == 3                                              # rc=0 = every preregistered assert GREEN


def test_reproduce_evidence_present():
    log = (ARC / "verification" / "reproduce.log").read_text(encoding="utf-8")
    assert log.count("REPRODUCES") == 3 and "SUMMARY: 3 reproduce" in log


def test_trace_three_unification():
    m = _d()["memos"]["49"]
    assert "UNIT and RAMIFIED" in m and "trace-3" in m                   # the two-ends mechanism
    assert "nilpotency degree EXACTLY 3" in m                            # the meridian on the carrier
    assert "GOLDEN" in m and "EISENSTEIN" in m                           # the two fields


def test_odd_steps_are_matter():
    m = _d()["memos"]["50"]
    assert "6 J3 (+) 15 J2 (+) 6 J1" in m and "27:21:6" in m             # the Jordan type + grading
    assert "clock-depth parity" in m and "ODD chains" in m and "EVEN chains" in m


def test_longitude_is_the_lock():
    m = _d()["memos"]["51"]
    assert "semisimple part" in m.lower() or "SEMISIMPLE PART" in m      # the Jordan-decomposition result
    assert "the lock" in m and "dim 12" in m                             # rho_Psi(lambda)=C_Psi.(3-step); cusp-fixed=12
    assert "FOUR independent" in m                                       # the 24-sector overdetermination


def test_independent_check_and_fences():
    d = _d()
    assert "sympy" in d["memos"]["arithmetic_check"] and "x^2-3x+3" in d["memos"]["arithmetic_check"]
    ic = (ARC / "verification" / "independent_check_memo49.txt").read_text(encoding="utf-8")
    assert "CONFIRMED" in ic and "phi^2" in ic
    assert "no field" in d["fences"] and "no value" in d["fences"]       # Gate 5 fence
    tl = d["through_line"].lower()
    assert "peripheral" in tl and "meridian" in tl and "longitude" in tl
