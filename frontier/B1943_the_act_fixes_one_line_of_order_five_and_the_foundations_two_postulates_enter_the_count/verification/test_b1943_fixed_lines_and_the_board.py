"""B1943's lock: the theorem re-run (seconds), and the board as corrected: C02 CHOSEN on SE3 with the theorem cited, S03 is
SE1, and the registry holds the theorem."""
import json, subprocess, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())


def test_the_theorem_re_run():
    out = subprocess.run([sys.executable, "-B", str(HERE / "fixed_lines.py")], capture_output=True, text=True, timeout=600).stdout
    assert "ALL HOLD: True" in out and "CAUGHT" in out


def test_the_board_as_corrected():
    d = json.loads((ROOT / "docs" / "total_inputs_scoreboard.json").read_text())
    c02 = [j for j in d["frames"]["C"]["joints"] if j["id"] == "C02"][0]
    assert c02["type"] == "CHOSEN" and "SE3" in c02["basis"] and "T-THE-ACTS-FIXED-LINE" in c02["basis"]
    s03 = [s for s in d["shared_block"] if s["id"] == "S03"]
    assert len(s03) == 1 and "SE1" in s03[0]["basis"] and s03[0]["type"] == "CHOSEN"
    assert "| T-THE-ACTS-FIXED-LINE |" in (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text()
