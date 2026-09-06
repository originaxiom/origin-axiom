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


def test_every_ledger_row_is_well_formed():
    """The scoreboard must PARSE. Unescaped pipes silently split cells and break rendering.

    Two rows were malformed when this gate was written (2026-09-06): I-16's absolute-value
    bars |D| and I-24's restriction bar [C18, D2|W18] -- the latter written the same day by
    the seat that added the row. Both were REFUTED rows so the price was never corrupted,
    but the table rendered wrong and any field-position parse broke. Escape pipes as \\| .
    """
    import re
    led = (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8")
    bad = []
    for line in led.splitlines():
        m = re.match(r"\|\s*(I-\d+)\s*\|", line)
        if m and len(re.split(r"(?<!\\)\|", line)) != 11:
            bad.append((m.group(1), len(re.split(r"(?<!\\)\|", line))))
    assert not bad, f"ledger rows with the wrong field count (escape pipes as \\|): {bad}"


def test_the_status_census_is_the_one_the_price_uses():
    """Guards against a malformed row silently changing the counted status."""
    import re
    from collections import Counter
    led = (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8")
    c = Counter()
    for line in led.splitlines():
        if re.match(r"\|\s*I-\d+\s*\|", line):
            st = re.search(r"\*\*(EARNED|UNEARNED|REFUTED)\*\*", line)
            c[st.group(1) if st else "?"] += 1
    assert c["?"] == 0, "every ledger row must carry exactly one bolded status token"
    P = _mod()
    from collections import Counter as C2
    assert C2(P.ledger_census().values())["UNEARNED"] == c["UNEARNED"]
