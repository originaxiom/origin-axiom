"""Locks B887 -- the gate audit and the four repairs."""
import json
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B887_gate_audit"
_G = (_ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
REPORTS = json.loads((_D / "audit_reports.json").read_text(encoding="utf-8"))


def test_the_audit_is_preserved_and_complete():
    assert len(REPORTS) >= 19


def test_repair_framing_scans_all_root_md():
    assert 'files = sorted(n for n in os.listdir(ROOT)' in _G
    assert '"WORKING_RULES.md"' not in _G.split("def gate_framing")[1].split("def ")[0]


def test_repair_claims_scans_whole_ledger():
    seg = _G.split("def gate_claims")[1].split("def ")[0]
    assert "re.finditer(r\"`(tests/" in seg
    assert 'text.split("## Proven", 1)[-1].split' not in seg
    assert "citation integrity, not test verdicts" in seg


def test_repair_atlas_set_equality():
    seg = _G.split("def gate_atlas_fresh")[1].split("def ")[0]
    assert "atlas_ids - ids" in seg and "ids - atlas_ids" in seg


def test_new_gate_arc_verdicts_registered_and_scoped():
    assert '"arc-verdicts": gate_arc_verdicts' in _G
    seg = _G.split("VERDICT_GRANDFATHERED = {")[1].split("}")[0]
    names = {t.strip().strip('",') for t in seg.replace("\n", " ").split('", "')}
    assert "P3_depth_exposure" in _G.split("VERDICT_GRANDFATHERED")[1]
    assert "B845_spectral_inventory" in seg


def test_all_twenty_gates_pass_now():
    out = subprocess.run([sys.executable, str(_ROOT / "scripts" / "gates" / "gates.py")],
                         capture_output=True, text=True).stdout
    assert out.count("PASS") >= 20 and "FAIL" not in out
