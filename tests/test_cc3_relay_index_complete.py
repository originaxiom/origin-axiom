"""Every outbound relay must appear in the index, or cc cannot find it.

Built after the index was created and then drifted within the hour: three relays -- including the
design audit and a correction the owner asked for -- were written and pushed while the index that
exists to route cc to them went unupdated. A pointer file that silently falls behind is worse than
none, because it looks authoritative.
"""
import os, re, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INDEX = os.path.join(ROOT, "docs", "CC3_RELAY_INDEX.md")

def test_index_exists():
    assert os.path.exists(INDEX), "the relay index cc is pointed at must exist"

def test_every_outbound_relay_is_listed():
    text = open(INDEX).read()
    relays = [os.path.basename(p)
              for p in glob.glob(os.path.join(ROOT, "frontier", "*", "relays", "CC3_TO_CC_*.md"))]
    assert relays, "no outbound relays found -- the glob is wrong, not the tree"
    missing = sorted(r for r in relays if r not in text)
    assert not missing, f"outbound relays absent from the index cc reads: {missing}"

def test_the_superseded_relay_is_marked_so():
    """A wrong diagnosis must never be reachable without its retraction alongside."""
    text = open(INDEX).read()
    assert "AUDIT_B1076_ONE_NOTATION_DEFECT.md" in text
    assert "SUPERSEDED" in text and "I_WAS_WRONG_THE_REAL_DEFECT.md" in text
