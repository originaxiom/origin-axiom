"""B8076 locks -- the paper-closure campaign cannot silently lose an item.

This is the anti-drift mechanism.  The failure mode it guards against is not error but
DRIFT: an item named, agreed real, then quietly not done while attention moves.  The corpus
carries that defect on record -- the standing law-harvest has run twice in forty-six
reviews, and R32-9b's 105 candidates were carried through six reviews unopened.

So: the ledger is a tracked artifact, the item count is pinned, every status must be one of
four, and GREEN requires an evidence path that EXISTS ON DISK.  An item cannot be deleted,
renamed away, or closed on prose without this test noticing.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "frontier", "B8076_paper_closure", "CAMPAIGN.md")
PREREG = os.path.join(ROOT, "frontier", "B8076_paper_closure", "PREREGISTRATION.md")

N_ITEMS = 12
STATUSES = {"GREEN", "OPEN", "BLOCKED", "WITHDRAWN"}


def _plain(s):
    """Strip markdown emphasis before matching.

    PRACTICES: "Strip emphasis, blockquote markers and whitespace before matching; match
    on the property, not the rendering. A lock that reads formatting is testing the
    typesetter."  A first version of this file compared the raw cell and rejected
    **GREEN** -- it was reading the typesetter, and the ledger was right.
    """
    return s.replace("*", "").replace("`", "").strip()


def _rows():
    """The ledger rows: (number, status, evidence)."""
    out = []
    for line in open(LEDGER, encoding="utf-8"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6 or not re.fullmatch(r"\d+", _plain(cells[0])):
            continue
        out.append((int(_plain(cells[0])), _plain(cells[4]), cells[5]))
    return out


def test_the_ledger_and_its_seal_exist():
    assert os.path.exists(LEDGER), "the campaign ledger is gone"
    assert os.path.exists(PREREG), "the campaign's sealed preregistration is gone"


def test_exactly_twelve_items_and_none_renumbered():
    """The count is pinned.  Deleting an item, or quietly merging two, fails here."""
    rows = _rows()
    assert len(rows) == N_ITEMS, f"expected {N_ITEMS} items, ledger has {len(rows)}"
    assert sorted(n for n, _, _ in rows) == list(range(1, N_ITEMS + 1))


def test_every_item_carries_one_of_the_four_statuses():
    """No blank statuses, no invented ones.  An item with no status is an item drifting."""
    for n, status, _ in _rows():
        assert status in STATUSES, f"item {n} has status {status!r}, not one of {sorted(STATUSES)}"


def test_every_closed_item_names_evidence_that_exists():
    """GREEN on prose is the exact thing this campaign exists to prevent.  A closed item must
    point at a path on disk -- a script, a deposited artifact, a test -- and the path must
    resolve.  BLOCKED and WITHDRAWN are legitimate closures and are exempt from the path
    requirement, but must still say something."""
    for n, status, evidence in _rows():
        if status == "GREEN":
            assert evidence and evidence != "—", f"item {n} is GREEN with no evidence"
            toks = re.findall(r"`([^`]+)`", evidence)
            # An evidence cell also carries inline mathematics in backticks.  A token is a
            # PATH CLAIM if it looks like one; those must resolve, and at least one must be
            # present.  (A first version required every backticked token to be a file, which
            # made the lock reject `dim z(S)` -- reading the typesetter again, cf. _plain.)
            # A path claim looks like a path: a slash and no spaces, or a known
            # extension. (An earlier version accepted any token containing "/", which
            # flagged the inline formula h = (a^2+b^2+ab+3a+3b)/15 as a missing file.)
            claims = [x for x in toks
                      if ("/" in x and " " not in x)
                      or x.endswith((".py", ".md", ".json", ".txt"))]
            assert claims, f"item {n} is GREEN but names no evidence path: {evidence!r}"
            for p in claims:
                full = os.path.join(ROOT, p.split(":")[0])
                assert os.path.exists(full), f"item {n} cites a path that does not exist: {p}"
        elif status in ("BLOCKED", "WITHDRAWN"):
            assert evidence and evidence != "—", \
                f"item {n} is {status} but records no reason"


def test_the_terminus_items_are_named_as_such():
    """Items 1-3 are the terminus; they are why the campaign exists.  If they are ever
    reworded into something smaller, this fails."""
    text = open(LEDGER, encoding="utf-8").read()
    assert "14-locus" in text
    assert "rung spectrum" in text
    assert "64 Levi" in text


def test_the_standing_rules_survive():
    """The three controls that exist because of specific banked failures."""
    text = open(LEDGER, encoding="utf-8").read()
    assert "No item closes on prose" in text
    assert "quantifier" in text
    assert "printed constant" in text          # error class E843, from B8070
