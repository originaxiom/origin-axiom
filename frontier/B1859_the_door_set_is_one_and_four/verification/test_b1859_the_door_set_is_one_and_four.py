"""B1859 -- the door set is {1, 4}; the corrected arcs keep their verdicts; the living pages carry the correction."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def run(name):
    return subprocess.run([sys.executable, "-B", str(HERE / name)], capture_output=True, text=True, check=True, timeout=900).stdout


def test_the_door_set_reproduces():
    out = run("door_set.py")
    assert out == (HERE / "door_set_run.txt").read_text(encoding="utf-8")
    lines = out.splitlines()
    assert "shadow order 120" in lines[0] and "the E8 door" in lines[0]
    assert "shadow order  32  involutions 7" in lines[1]
    assert "shadow order 120" in lines[3] and "the E8 door" in lines[3]
    assert sum("the E8 door" in l for l in lines) == 2 and "[1, 4]" in lines[-1]


def test_the_2t_quotients_reproduce():
    out = run("two_t_quotients.py")
    assert out == (HERE / "two_t_quotients_run.txt").read_text(encoding="utf-8")
    lines = out.splitlines()
    assert " 48 =  2 classes" in lines[0] and "  0 =  0 classes" in lines[3]
    assert "surjections onto SL(2, 5): 0" in out


def test_the_verdicts_of_the_corrected_arcs_are_not_reversed():
    """Refute the clause, keep the computation: B997 and B1019 stay PROVED and carry the correction in their verdict lines."""
    for arc in ("B997_golden_conductor_uniqueness", "B1019_l149_silver_cascade"):
        v = json.loads((ROOT / "frontier" / arc / "arc_verdict.json").read_text(encoding="utf-8"))
        assert v["verdict"] in ("PROVED", "NEGATIVE") and "B1859" in v["claim_one_line"], arc


def test_the_living_pages_carry_the_correction():
    for rel in ("docs/THE_CLAIM.md", "GENESIS.md", "docs/LAW_MAP.md", "docs/THEOREM_REGISTRY.md", "docs/KIND_TABLE.md",
                "docs/THE_CHAIN_STATUS.md", "docs/THE_FRAMEWORK.md", "docs/MASTERPLAN.md", "ROADMAP.md", "docs/OPEN_PROBLEMS.md",
                "docs/PRICED_DOORS.md", "docs/PRIOR_ART_DOSSIER_ENTRANCE_AND_EXIT.md"):
        assert "B1859" in (ROOT / rel).read_text(encoding="utf-8"), rel
