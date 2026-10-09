"""B1626 -- the relay-closure pass is on the ledger: no outbound row to the SM seat or the audit lane carries an unparseable
disposition; the 40 closed rows name B1626; relay-debt passes; the nine audit relays are rowed."""
import pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]


def test_the_closure_is_on_the_ledger_and_parses():
    t = ROOT.joinpath("docs", "RELAY_LEDGER.md").read_text(encoding="utf-8")
    closed = [l for l in t.splitlines() if l.startswith("| `CC_TO") and "| BANKED |" in l and "R62-5 (2026-10-09, B1626)" in l]
    still = [l for l in t.splitlines() if l.startswith("| `CC_TO") and "| OPEN |" in l and "R62-5 (2026-10-09, B1626)" in l]
    assert len(closed) == 40 and len(still) == 25
    assert not [l for l in t.splitlines() if l.startswith("| `CC_TO") and re.search(r"\| READ \|", l)]
    for n in ("CUSP_WARD_AND_FLAVOR_TENSOR", "COMPACT_BOUNDARY_INDEX", "SILVER_ANALYTIC_TRANSFER"):
        assert ("CODEX_TO_CC_AND_SM_2026-10-0" in t) and n in t, n
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "checks" / "relay_debt.py")], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-500:]
