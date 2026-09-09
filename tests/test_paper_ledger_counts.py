"""The paper's ledger-count tool (scripts/checks/paper_ledger_counts.py): the prose counts must equal
the table's rows, and the tool must not miscount. B1237: the tool's first draft counted the
dimensionful-unit row (external by design) as non-continuous and reported a MISMATCH against a
correct paper -- an instrument that cries wolf is ignored, so its own count is locked here."""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOL = ROOT / "scripts" / "checks" / "paper_ledger_counts.py"


def test_the_tool_agrees_with_the_paper_and_its_plant_bites():
    r = subprocess.run([sys.executable, str(TOOL), "--selftest"], capture_output=True, text=True, cwd=str(ROOT))
    assert r.returncode == 0, r.stdout + r.stderr
    assert "non-continuous: 6" in r.stdout
    assert "MISMATCH" not in r.stdout
    assert "CONTROLS PASS" in r.stdout


def test_the_dimensionful_row_is_not_a_non_continuous_row():
    spec_src = TOOL.read_text(encoding="utf-8")
    assert '"dimensionful" not in t' in spec_src
