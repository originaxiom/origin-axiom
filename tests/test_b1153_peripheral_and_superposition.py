"""B1153 lock -- the peripheral identity + the superposition speaks: cloud memos 54-55
reproduce-verified. memo 54: tr(ab^-1)=gal(kappa) is the Riley relation in disguise + the full fixed
locus is 3 points (closes codex OA-C1082/OA-C1083). memo 55: C4's honest negative (B1151) closes
POSITIVE -- the merged zeta_K spacing IS the 2-fold GUE superposition of zeta*L(chi_-3). Generic, no
crossing; Gate 5 untouched."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1153_peripheral_and_superposition"


def _d():
    return json.loads((ARC / "b1153_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_proved():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1153" and d["verdict"] == "PROVED"


def test_both_reproduced():
    r = _d()["reproduce"]
    assert r["failures"] == 0 and r["byte_identical_verdict"] == r["total_certs"] == 2 and r["rc_zero"] == 2


def test_reproduce_evidence_present():
    log = (ARC / "verification" / "reproduce.log").read_text(encoding="utf-8")
    assert log.count("REPRODUCES") == 2 and "SUMMARY: 2 reproduce" in log


def test_peripheral_identity_and_fixed_locus():
    m = _d()["memos"]["54"]
    assert "Riley relation" in m and "gal(kappa)" in m                    # the identity
    assert "S-3 = P + (x^2-4)" in m and "parabolic" in m                  # exact where parabolic, defect x^2-4
    assert "3 points" in m and "z^2(z^2+12)" in m and "OA-C1082" in m     # the full fixed locus, codex row closed


def test_superposition_closes_c4_positive():
    m = _d()["memos"]["55"]
    assert "D=0.02400" in m and "two halves of one statement" in m        # the positive fit
    assert "522c7caa" in m and "zeta*L(chi_-3)" in m                      # ran on B1151's own data; the product


def test_independent_check_corrections_and_fences():
    d = _d()
    ic = (ARC / "verification" / "independent_check_memo54.txt").read_text(encoding="utf-8")
    assert "S-3-(P+(x^2-4)) = 0" in ic and "3 points" in ic               # memo 54 independently confirmed
    assert "'a second'" in d["corrections_adopted"]                       # memo 43 scope correction adopted
    assert "antiunitary' -> 'semilinear'" in d["corrections_adopted"]     # the terminology correction
    assert "no firewall crossing" in d["fences"] and "Gate 5 untouched" in d["fences"]
