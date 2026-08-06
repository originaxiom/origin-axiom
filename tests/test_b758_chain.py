"""Lock for B758 -- THE CHAIN (docs/THEOREM_LEDGER.md): structure + pointer integrity."""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOC = os.path.join(ROOT, "docs", "THEOREM_LEDGER.md")


def _text():
    with open(DOC, encoding="utf-8") as fh:
        return fh.read()


def test_chain_has_eighteen_links_with_valid_labels():
    # C1-C23 through 2026-08-05; C24-C43 = Part V, the B877-B919 window's same-PR
    # catch-up (2026-08-06, B920 register sweep -- cc3 loss audit A5).
    text = _text()
    links = re.findall(r"\*\*C(\d+) \[(THEOREM|CENSUS|IDENTITY|NO-GO|AXIOM|COROLLARY)[^\]]*\]", text)
    assert [int(n) for n, _ in links] == list(range(1, 44))
    grades = [g for _, g in links]
    assert grades.count("AXIOM") == 4            # C3, C4, C5, C18 (C19 = IDENTITY)
    assert grades[23:].count("AXIOM") == 0       # Part V admits no axioms
    assert text.count("PRICED") >= 4 and "remaining unpriced" in text


def test_every_cited_lock_file_exists():
    text = _text()
    for lock in set(re.findall(r"`(tests/[A-Za-z0-9_]+\.py)`", text)):
        assert os.path.exists(os.path.join(ROOT, lock)), lock


def test_axioms_priced_or_flagged():
    text = _text()
    # the three genesis axioms carry PRICED; the frontier axiom carries UNPRICED
    for c in ("C3 [AXIOM", "C4 [AXIOM", "C5 [AXIOM", "C18 [AXIOM"):
        seg = text.split(c, 1)[1][:90]
        assert "PRICED" in seg
