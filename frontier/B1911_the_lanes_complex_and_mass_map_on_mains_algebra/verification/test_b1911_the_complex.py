"""B1911's lock. It loads the script, whose checks run on import and whose write is under a main guard, requires every
check to hold and each planted form to fail, and holds the page's count. It writes nothing."""
import sys, io, json, contextlib, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
before = sorted(p.name for p in HERE.iterdir())
with contextlib.redirect_stdout(io.StringIO()):
    import the_complex_and_the_mass_map as W
PAGE = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
LINE = json.loads((HERE.parent / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]

def test_the_lock_wrote_nothing():
    assert sorted(p.name for p in HERE.iterdir() if p.name != "__pycache__") == [x for x in before if x != "__pycache__"]

def test_every_check_holds_and_every_plant_fails():
    assert W.CHECKS and all(c["holds"] for c in W.CHECKS), [c["check"] for c in W.CHECKS if not c["holds"]]
    plants = [c for c in W.CHECKS if "plant" in c["check"] or "control" in c["check"]]
    assert len(plants) >= 5

def test_the_page_counts_them():
    n = len(W.CHECKS)
    assert "%d checks, none failing" % n in PAGE and "%d checks, none failing" % n in LINE
