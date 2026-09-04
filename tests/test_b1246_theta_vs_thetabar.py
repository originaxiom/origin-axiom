"""B1246 — I-18's price is sharpened: the type dictionary reaches theta, not theta-bar."""
import json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1246_theta_vs_thetabar"

def _row(rid):
    for line in (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8").splitlines():
        if line.startswith(f"| {rid} |"):
            return line
    raise AssertionError(f"{rid} missing")

def test_I18_carries_the_theta_vs_thetabar_distinction():
    r = _row("I-18")
    assert "Yukawa" in r, "the contingency must be ON THE ROW, not only in the log"
    assert "P-odd" in r and "C-even" in r and "T-odd" in r, "the shared type is why it cannot discriminate"
    # strip markdown emphasis before matching -- the row writes "**two** candidates"
    flat = re.sub(r"\*+", "", r).lower()
    assert "two candidates" in flat, flat[:300]

def test_the_row_is_still_UNEARNED_and_the_ratchet_did_not_move():
    assert "**UNEARNED**" in _row("I-18")
    b = json.loads((ROOT / "docs" / "IDENTIFICATION_BASELINE.json").read_text(encoding="utf-8"))
    assert "I-18" in b["rows"], "sharpening a price must not silently un-register the row"

def test_the_discriminating_fact_is_RUN_not_asserted():
    r = subprocess.run([sys.executable, "verification/b1246_chiral_invariance.py"],
                       capture_output=True, text=True, cwd=str(ARC),
                       env={"PATH": "/usr/bin:/bin"})
    assert r.returncode == 0, r.stdout + r.stderr
    assert r.stdout.rstrip().endswith("REPRODUCES"), r.stdout[-400:]

def test_the_arc_declares_its_own_scope_split():
    """part (i) computed, part (ii) standard-and-stated -- the arc must say which is which."""
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert "STANDARD QFT, stated and not derived" in v["note"]
    assert v["identifications"][0]["row"] == "I-18" and v["identifications"][0]["status"] == "UNEARNED"
