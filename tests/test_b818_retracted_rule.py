"""B818 — locks the corrected verdicts and the RETRACTED disambiguation.

The invariant: an arc labelled RETRACTED must withdraw ITS OWN headline. An auditor that
establishes another arc's claim fails is doing positive work and must not be labelled as though
its own result were untrustworthy.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Every RETRACTED arc must carry a self-retraction marker in its own header. The vocabulary here
# is deliberately wide: a screen that searched only for RETRACT/WITHDRAWN produced three false
# positives (B192 says REFUTED, B216 OVERTURNED, B90 CORRECTED).
SELF_MARKERS = re.compile(
    r"RETRACT|WITHDRAWN|OVERTURNED|CORRECTED|REFUTED|HEADLINE OF THIS FILE IS WRONG", re.I)


def _verdicts():
    for p in sorted((ROOT / "frontier").glob("*/arc_verdict.json")):
        yield p.parent, json.loads(p.read_text(encoding="utf-8"))


def test_the_two_auditors_are_not_labelled_retracted():
    """B745 established 'CONFIRMED x2'; B525 established '4 CONFIRMED / 2 SHAKY / 3 CRACKED'."""
    got = {}
    for d, v in _verdicts():
        if v["id"] in ("B745", "B525"):
            got[v["id"]] = v["verdict"]
    assert got.get("B745") == "PROVED", f"B745 confirms two revivals; got {got.get('B745')}"
    assert got.get("B525") == "PROVED", f"B525 is the auditor, not the audited; got {got.get('B525')}"


def test_every_retracted_arc_withdraws_its_own_headline():
    """The invariant the rule encodes -- checked against each arc's own opening text."""
    bad = []
    for d, v in _verdicts():
        if v["verdict"] != "RETRACTED":
            continue
        # Read whichever findings document the arc actually uses (B826: B519 uses VERDICT.md).
        head = ""
        for name in ("FINDINGS.md", "VERDICT.md"):
            f = d / name
            if f.is_file():
                # WHOLE file, not a header window. B702 records a legitimate
                # "## RETRACTION + CORRECTION" section at line 45, and a 1500-char read
                # flagged a correctly-labelled arc as untagged (B835).
                head = f.read_text(encoding="utf-8")
                break
        if not SELF_MARKERS.search(head):
            bad.append(v["id"])
    assert not bad, (f"RETRACTED arcs with no self-retraction marker in their own header: {bad}. "
                     f"Either the label is wrong, or the arc withdraws someone ELSE's result -- "
                     f"in which case label it by what IT established (B818).")


def test_the_disambiguation_is_registered():
    p = " ".join((ROOT / "docs" / "PRACTICES.md").read_text(encoding="utf-8").split())
    assert "withdraws **its own** headline" in p or "withdraws **its own**" in p
    assert "the retraction lands on the **target** arc's record" in p


def test_retracted_stays_a_small_deliberate_set():
    """A drift guard: RETRACTED is rare by construction. A jump means the rule slipped again."""
    n = sum(1 for _, v in _verdicts() if v["verdict"] == "RETRACTED")
    assert 4 <= n <= 12, f"{n} RETRACTED verdicts -- expected a small set; re-check against B818"
