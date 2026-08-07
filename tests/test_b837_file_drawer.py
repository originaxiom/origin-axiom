"""B837 — locks the file-drawer audit: a sealed prereg carries a reporting obligation."""
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTIER = ROOT / "frontier"
KNOWN_UNREPORTED = {"B499", "B557", "B590"}


def _sealed_without_report():
    out = []
    for d in sorted(FRONTIER.iterdir()):
        if not d.is_dir():
            continue
        if any((d / n).is_file() for n in ("FINDINGS.md", "VERDICT.md")):
            continue
        if (d / "arc_verdict.json").is_file():
            continue
        if any("PREREG" in f.upper() for f in os.listdir(d)):
            m = re.match(r"(B\d+)", d.name)
            if m:
                out.append(m.group(1))
    return set(out)


def test_the_unreported_set_has_not_grown():
    """A NEW sealed prereg with no report is a new file-drawer entry and must be caught."""
    sealed = _sealed_without_report()
    ledger = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    ledgered = {a for a in sealed if re.search(rf"\|\s*{a}\b", ledger) or f"{a} " in ledger}
    new = ledgered - KNOWN_UNREPORTED - {
        # the 12 audited as REPORTED in a successor arc's findings (B837)
        "B452", "B473", "B501", "B502", "B503", "B506", "B565", "B568", "B570", "B580",
        "B634", "B652",
        # B913 is DESIGN-ONLY by its own sealed text ("this design seal is the cell's entire
        # content; no computation follows under this ID"). Its choice is reported in B914's
        # FINDINGS, which names the seal and states that no other magnitude appears anywhere
        # in that cell. Audit trail: frontier/B913_r3c_design/DESIGN_DISPOSITION.md.
        "B913"}
    assert not new, (
        f"new sealed-and-ledgered prereg(s) with no findings report: {sorted(new)} -- "
        f"report the result or record a disposition (B837)")


def test_the_three_named_loose_ends_are_still_named():
    f = " ".join((FRONTIER / "B837_file_drawer_audit" / "FINDINGS.md").read_text(
        encoding="utf-8").split())
    for a in KNOWN_UNREPORTED:
        assert a in f, f"{a} must stay named as an unreported sealed prereg"
    assert "citation ≠ report" in f or "citation" in f


def test_a_stub_without_a_prereg_carries_no_obligation():
    """29 no-document dirs hold no prereg -- a stub is not a broken promise."""
    nodoc_no_prereg = []
    for d in FRONTIER.iterdir():
        if not d.is_dir():
            continue
        if any((d / n).is_file() for n in ("FINDINGS.md", "VERDICT.md")):
            continue
        if (d / "arc_verdict.json").is_file():
            continue
        if not any("PREREG" in f.upper() for f in os.listdir(d)):
            nodoc_no_prereg.append(d.name)
    assert len(nodoc_no_prereg) >= 10, "the prereg-free stub population should still exist"


def test_the_B913_exemption_is_a_pointer_not_a_black_hole():
    """An exemption must be discoverable: the disposition record must exist, and the
    successor arc must actually report the design it exempts."""
    cell = ROOT / "frontier" / "B913_r3c_design"
    disp = cell / "DESIGN_DISPOSITION.md"
    assert disp.is_file(), "the exempted cell must carry its audit trail"
    # markdown is hard-wrapped and the sealed text is quoted, so strip blockquote
    # markers and normalise whitespace before matching
    raw = disp.read_text(encoding="utf-8")
    txt = " ".join(re.sub(r"(?m)^\s*>\s?", "", raw).split())
    assert "no computation follows under this ID" in txt
    assert "Where it was consumed" in txt
    # and the successor really does report it
    b914 = next((ROOT / "frontier").glob("B914_*/FINDINGS.md"))
    body = " ".join(b914.read_text(encoding="utf-8").split())
    assert "B913" in body and "|det Gram|^{1/3}" in body
