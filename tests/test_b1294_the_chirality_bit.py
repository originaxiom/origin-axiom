"""B1294 -- THE CHIRALITY BIT: the harvest reproduces by RUNNING, and the load-bearing numbers are pinned."""
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1294_the_chirality_bit"
VER = ARC / "verification"


def test_the_arc_reproduces_by_RUNNING_its_script():
    r = subprocess.run([sys.executable, str(VER / "harvest_chirality_bit.py")],
                       capture_output=True, text=True, cwd=str(VER))
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert r.stdout.rstrip().endswith("SELFTEST: PASS"), r.stdout[-500:]


def _j():
    return json.loads((VER / "chirality_bit.json").read_text(encoding="utf-8"))


def test_every_isometry_of_m004_has_lefschetz_number_zero_or_two():
    rows = _j()["A_isometries"]
    assert len(rows) == 8
    assert {r["lefschetz"] for r in rows} == {0, 2}
    assert all(r["lefschetz"] == 1 - r["s_mu"] for r in rows)
    # the two order-4 elements are orientation-reversing with L = 2: two isolated interior fixed points
    o4 = [r for r in rows if r["order"] == 4]
    assert len(o4) == 2 and all(r["orientation"] == "REVERSING" and r["lefschetz"] == 2 for r in o4)
    # only the orientation-preserving V4 extends to QHS fillings
    ext = {r["orientation"]: r["extends_to_QHS_fillings"] for r in rows}
    assert ext["REVERSING"] == 0 and ext["preserving"] > 0


def test_the_closed_closing_theorem_and_the_filling_loops():
    j = _j()
    assert j["B_closed_QHS_lefschetz"] == {"orientation-preserving": 0, "orientation-reversing": 2}
    loops = j["B_filling_loops"]
    for slope, c in loops.items():
        p = int(slope.split("/")[0])
        assert c == 1 + (1 if p % 2 == 0 else 0), (slope, c)   # Montesinos + H_1(-;F_2), not fc's pairing


def test_H1_of_the_cyclic_branched_covers_is_the_golden_table():
    h = _j()["C_H1_Yn"]
    assert h["3"] == [4, 4] and h["6"] == [8, 40] and h["9"] == [76, 76]
    assert h["5"] == [11, 11] and h["7"] == [29, 29] and h["11"] == [199, 199]   # (Z/L_n)^2
    assert h["2"] == [5] and h["4"] == [3, 15] and h["12"] == [144, 720]       # Z/F_n + Z/5F_n


def test_the_deck_eigenvalues_and_the_E6_spectra():
    j = _j()
    assert j["D_mod19"]["roots"] == [6, 16]
    e = j["E_E6_spectra"]
    assert e["omega1"] == {"-2/3": 10, "1/3": 16, "4/3": 1}
    assert e["omega6"] == {"-4/3": 1, "-1/3": 16, "2/3": 10}
    assert e["omega2"] == {"-1": 6, "0": 15, "1": 6}
    assert e["omega1+omega6"] == {"-2": 1, "-1": 8, "0": 9, "1": 8, "2": 1}


def test_the_verdict_registers_the_law_and_names_both_assumptions():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["creates_law"] is True and v["law_id"] == "T-CLOSED-CLOSING-COUNTS-TWO-OR-NOTHING"
    c = v["claim_one_line"]
    assert "theta-equivariance" in c and "c_(+-2,0)" in c
    assert "MUTUALLY EXCLUSIVE" in c
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    assert "T-CLOSED-CLOSING-COUNTS-TWO-OR-NOTHING" in reg
    # the synthesis surface carries the sentence, not only the arc
    mg = (ROOT / "docs" / "MAIN_GOAL.md").read_text(encoding="utf-8")
    assert "B1294" in mg and "counts 2" in mg
