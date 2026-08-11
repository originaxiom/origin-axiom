"""B1024 — locks: the class computations, the consistency anchors, the unconditional half."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1024_l153_bits"))


def test_the_classes_and_the_generation():
    from b1024_cells import cls, cls_structure, CHI_C, CHI_M, ALL_MINUS, ALL_ONES
    assert cls(CHI_M) == (0, 0), "the D2-coboundary consistency anchor (B936) must hold"
    assert cls(ALL_MINUS) == (1, 1), "the D-nonzero consistency anchor (B936) must hold"
    assert cls(CHI_C) == (1, 0), "conjugation's shadow class -- the unconditional generator"
    assert cls_structure(ALL_ONES) == (1, 1), "reversal's bare-lift structure class"
    span = {(0, 0), (1, 0), (1, 1), (0, 1)}
    got = {(0, 0), cls(CHI_C), cls_structure(ALL_ONES),
           tuple((a + b) % 2 for a, b in zip(cls(CHI_C), cls_structure(ALL_ONES)))}
    assert got == span, "the two shadows must generate ALL of H^1"


def test_d4_stays_refuted_and_r11_is_tightened():
    import json
    v = json.loads((ROOT / "frontier" / "B1024_l153_bits" / "arc_verdict.json").read_text())
    c = v["claim_one_line"]
    assert "REFUTED UNCONDITIONALLY" in c and "d = 2" in c
    assert "SENSITIVITY NAMED" in c, "the phi+ alternative must stay priced"
    t = (ROOT / "docs" / "CROSSING_REQUIREMENTS.md").read_text(encoding="utf-8")
    flat = " ".join(t.replace("**", "").split())
    assert "d = 2" in flat and "L153" in flat, "R11 must carry the tightened deficit"
