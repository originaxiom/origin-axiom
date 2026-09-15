"""B993 addendum -- the E6 entry point's base rate, exact: 145/400 admit a surjection onto SL(2,3), 124/400 share m004's count of two
classes up to Aut; the JSON is pinned and, under OA_SLOW, recomputed live (about five seconds)."""
import json, os, subprocess, sys
from pathlib import Path
import pytest
ROOT = Path(__file__).resolve().parents[1]; V = ROOT / "frontier" / "B993_cornerstone_verified" / "verification"


def test_pinned_rates():
    d = json.loads((V / "sl23_baserate.json").read_text(encoding="utf-8"))
    assert d["N"] == 400 and d["with_at_least_one"] == 145 and d["exactly_m004_count"] == 124 and d["m004_classes"] == 2
    assert d["distribution_of_classes"] == {"2": 124, "0": 255, "4": 14, "6": 4, "10": 2, "12": 1}
    assert d["tie_list_first_12"][:11] == ["m003", "m004", "m007", "m022", "m026", "m027", "m029", "m030", "m033", "m034", "m036"]


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="live recount (seconds)")
def test_live_recount(tmp_path):
    r = subprocess.run([sys.executable, str(V / "sl23_baserate.py"), "400"], capture_output=True, text=True, cwd=str(tmp_path), timeout=1800)
    assert r.returncode == 0 and '"with_at_least_one": 145' in r.stdout and '"exactly_m004_count": 124' in r.stdout, r.stdout[-1500:]
