"""B1184 lock -- the quine synthesis: self-naming without self-signing (S4 dispositioned)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_arc_verdict_proved():
    d = json.loads((ROOT / "frontier" / "B1184_quine_synthesis" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1184" and d["verdict"] == "PROVED"
    assert "SELF-NAMING WITHOUT SELF-SIGNING" in d["claim_one_line"]
    assert "SPLIT VERDICT" in d["claim_one_line"]
    assert "census-scoped" in d["claim_one_line"]  # the one-way-family rule honored


def test_results_structure():
    d = json.loads((ROOT / "frontier" / "B1184_quine_synthesis" / "b1184_results.json").read_text(encoding="utf-8"))
    assert "STALE" in d["correction"]                       # the register's QP-1-open corrected
    assert "SURVIVES" in d["b8147_stress_test"]
    assert "no odd letter" in d["name_parity"]
    assert "complementary" in d["synthesis"]
    assert "four-rung table closes" in d["observer_table"]


def test_reproduce_committed():
    r = (ROOT / "frontier" / "B1184_quine_synthesis" / "verification" / "reproduce.sh").read_text(encoding="utf-8")
    assert "o10_150700" in r and "REPRODUCES" in r
