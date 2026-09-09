"""B1262 — I-9 refuted: no genus V4 for disc -15."""
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1262_i9_refuted" / "verification" / "genus_v4_does_not_exist.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import genus_v4_does_not_exist as G
    return G


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_class_numbers_validated():
    G = _mod()
    for D, h in {-15: 2, -23: 3, -4: 1, -3: 1, -47: 5}.items():
        assert len(G.reduced_forms(D)) == h, D


def test_the_genus_group_of_disc_minus_15_has_order_two():
    G = _mod()
    assert G.n_genera(-15) == 2 and len(G.reduced_forms(-15)) == 2


def test_the_criterion_can_yield_order_four():
    """MB12: t = 3 discriminants DO give 4 genera — order 2 is about -15, not the method."""
    G = _mod()
    assert G.n_genera(-84) == 4 and G.n_genera(-120) == 4


def test_I9_is_registered_REFUTED_and_the_price_dropped():
    led = (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8")
    row = next(l for l in led.splitlines() if l.startswith("| I-9 |"))
    assert "**REFUTED**" in row and "B1262" in row
    b = json.loads((ROOT / "docs" / "IDENTIFICATION_BASELINE.json").read_text(encoding="utf-8"))
    assert "I-9" not in b["rows"]
    low = next(x for x in b["_baseline_lowerings"] if "I-9" in x.get("rows", []))
    assert low["from"] == 11 and low["to"] == 10 and low.get("reason")
