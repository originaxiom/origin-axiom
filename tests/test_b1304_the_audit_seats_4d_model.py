"""B1304 -- THE AUDIT SEAT'S 4d MODEL, PRICED: the DESIGN is sealed; the C3 locus, the B915 residual and the G2 strata reproduce by RUNNING;
the seat's suite receipt shows its own preserved state; the ToE ledger exists with its section E."""
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1304_the_audit_seats_4d_model"; VER = ARC / "verification"


def _run(script, cwd, timeout=900):
    return subprocess.run([sys.executable, str(VER / script)], capture_output=True, text=True, cwd=str(cwd), timeout=timeout)


def test_the_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")


def test_the_c3_locus_and_the_alexander_polynomial_reproduce_by_RUNNING(tmp_path):
    r = _run("b1304_c3_locus.py", tmp_path)
    assert "C3-fixed characters (as (theta_a, theta_b) in (Q/Z)^2): [(0, 0), (1/3, 2/3), (2/3, 1/3)]" in r.stdout
    assert "Delta_m202 (up to units) = t1**2*t2 + t1**2 + t1*t2**2 + t1*t2 + t1 + t2**2 + t2" in r.stdout and "Delta(chi) = -2" in r.stdout
    assert "[PASS] (c) Delta(chi) != 0 at both characters" in r.stdout and "algebraic h^1(m202; chi) = 0" in r.stdout   # the recorded mis-prediction: 0, not 1


def test_the_b915_residual_reproduces_by_RUNNING(tmp_path):
    r = _run("b1304_b915_residual.py", tmp_path, timeout=1500)
    assert "max |x1 - x2| (the first UV equation, NOT re-solved) = 0.0268397" in r.stdout and "[PASS] (a)" in r.stdout and "[PASS] (c)" in r.stdout
    j = json.loads((VER / "b1304_b915_residual.json").read_text(encoding="utf-8")); assert 0.02 < j["max_r1"] < 0.035 and j["max_r2"] < 1e-6


def test_the_g2_strata_reproduce_by_RUNNING(tmp_path):
    r = _run("b1304_g2_strata.py", tmp_path); assert r.returncode == 0, r.stdout[-1500:] + r.stderr[-1500:]
    assert "{1: [7, 1], 2: [3, 7], 4: [1, 7], 8: [0, 1]}" in r.stdout and r.stdout.rstrip().endswith("Q3: PASS")


def test_the_seat_suite_receipt_and_the_toe_ledger():
    t = (VER / "audit_focused_suite_rerun.txt").read_text(encoding="utf-8", errors="replace")
    assert "13 failed, 235 passed" in t and "8 errors" in t and t.rstrip().endswith("RC=1")          # the seat's own preserved state, not ours
    led = (ROOT / "docs" / "TOE_REQUIREMENTS_LEDGER.md").read_text(encoding="utf-8")
    assert "## E. THE DECLARED INPUTS" in led and "Say which endpoint" in led and "COMPACT real form" in led
    assert "Scope addendum 2026-09-09" in (ROOT / "frontier" / "B1259_flat_orbifolds_cannot_isolate" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "Instrument addendum 2026-09-09" in (ROOT / "frontier" / "B915_the_crossing" / "FINDINGS.md").read_text(encoding="utf-8")
