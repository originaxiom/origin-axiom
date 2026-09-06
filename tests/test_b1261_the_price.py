"""B1261 — the price: the ledgers agree, and structural content never offsets parameters."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1261_the_price_computed" / "verification" / "the_price.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import the_price as P
    return P


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_the_ratchet_and_the_row_census_agree():
    """If these drift, the price is unreadable and the headline is meaningless."""
    P = _mod()
    from collections import Counter
    rows = P.ledger_census()
    c = Counter(rows.values())
    b = P.baseline()
    assert b["unearned"] == c["UNEARNED"]
    assert b["total_rows"] == len(rows)


def test_the_price_is_axioms_plus_unearned():
    P = _mod()
    from collections import Counter
    c = Counter(P.ledger_census().values())
    assert P.AXIOMS + c["UNEARNED"] == 4 + c["UNEARNED"]
    assert P.SM_PARAMS_MIN == 19 and P.SM_PARAMS_NU == 26
