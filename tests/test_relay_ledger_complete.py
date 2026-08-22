"""Every CC3_TO_CC relay on disk must have a row in docs/RELAY_LEDGER.md.

Companion to test_cc3_relay_index_complete.py, which locks the same relays into
docs/CC3_RELAY_INDEX.md. The index lock existed; this one did not, and on
2026-08-22 the owner's question "all relayed to cc?" surfaced a relay that was
indexed, delivered and answered -- but carried no ledger row. Its title was
"THE LEDGER THE WAVE MISSED".

The gap was structural: two surfaces, one lock. Now two.
"""
import os
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEDGER = (ROOT / "docs" / "RELAY_LEDGER.md").read_text()
RELAYS = sorted(ROOT.glob("frontier/*/relays/CC3_TO_CC_*.md"))


def test_there_are_relays_to_check():
    """An empty sweep passes vacuously -- refuse that."""
    assert len(RELAYS) > 20, f"only {len(RELAYS)} relays found; the glob is wrong"


@pytest.mark.parametrize("relay", RELAYS, ids=lambda p: p.name[:60])
def test_relay_has_a_ledger_row(relay):
    assert relay.name in LEDGER, (
        f"{relay.name} has no row in docs/RELAY_LEDGER.md -- a relay that is sent "
        f"but unledgered is invisible to relay-debt accounting"
    )
