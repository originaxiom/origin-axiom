"""B1100 lock: the exact table's headline facts from the stored records."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "frontier/B1100_landing_content"

def test_exact_table_tiles_and_branches():
    r = json.load(open(D / "b1100_exact_table.json"))
    assert r["sum"] == 27
    assert r["sl2"] == {"-2": 6, "0": 15, "2": 6}

def test_the_27_is_complex_with_witness():
    r = json.load(open(D / "b1100_exact_table.json"))
    assert r["real"] is False
    assert "CRootOf" in r["witness"] and ", 3, 0)" in r["witness"]  # mult-3 class, negation absent

def test_class_sizes_and_bijective_exclusion():
    r = json.load(open(D / "b1100_exact_table.json"))
    sizes = sorted((m for _, m in r["classes"]), reverse=True)
    assert sizes == [3]*6 + [1]*9
    assert r["match"] is None                      # bijective form excluded

def test_collapse_pattern_hit():
    h = json.load(open(D / "b1100_hypercharge.json"))
    assert h["pattern_hit"] is True and len(h["t_float"]) == 4
