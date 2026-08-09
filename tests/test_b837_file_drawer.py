"""B837 — locks the file-drawer audit: a sealed prereg carries a reporting obligation."""
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTIER = ROOT / "frontier"
KNOWN_UNREPORTED = {"B499", "B557", "B590"}

# B982 (2026-08-09): the exemption list below claimed all twelve were "audited as REPORTED in
# B837". B837's FINDINGS names only FIVE (B452, B568, B580, B634, B652). For three of the rest
# the apparent support was a NUMBERING COLLISION -- B521 states "B493-B503 collides with this
# trunk's B496-B503", and cites the AUDIT SEAT's B501_gateB_reductions / B502_gateC_commensurator
# / B503_tower_timebox, which are different arcs from main's B501_universe_word /
# B502_parity_signature / B503_external_contact. Corrected below, each with its real basis.
UNREPORTED_FOUND_BY_B982 = {"B501", "B502"}   # genuine file-drawer; B500 cites them FORWARD only
DISPOSITION_NOT_REPORT = {"B503"}             # owner-gated by its own sealed text; never fires
REPORTED_ELSEWHERE = {"B506": "B507_beta_function"}  # real report, wrong citation before
UNVERIFIED_EXEMPTIONS = {"B473", "B565", "B570"}  # cited in successors; NOT line-checked -- a debt


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
    new = ledgered - KNOWN_UNREPORTED - UNREPORTED_FOUND_BY_B982 - DISPOSITION_NOT_REPORT - {
        # audited as REPORTED and ACTUALLY NAMED in B837's findings (re-verified by B982)
        "B452", "B568", "B580", "B634", "B652",
        # reported elsewhere, citation corrected by B982
        "B506",
        # cited in successor findings but NOT line-checked; a recorded debt, not a clean pass
        "B473", "B565", "B570",
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


def test_the_B982_correction_is_recorded_and_the_debt_is_named():
    """B982: seven of twelve exemptions cited an audit that does not name them."""
    f = (FRONTIER / "B982_file_drawer_exemption_defect" / "FINDINGS.md").read_text(encoding="utf-8")
    for a in ("B501", "B502", "B503", "B506"):
        assert a in f, f"{a}'s disposition must be recorded"
    assert "collision" in f.lower(), "the numbering collision must be named"
    assert UNVERIFIED_EXEMPTIONS, "the unverified exemptions must stay a named debt"


def test_B501_and_B502_are_genuinely_unreported():
    """Their only citation is a FORWARD pointer in B500, which precedes them."""
    assert UNREPORTED_FOUND_BY_B982 == {"B501", "B502"}
    for a in UNREPORTED_FOUND_BY_B982:
        assert not any((FRONTIER / d / "FINDINGS.md").is_file()
                       for d in [p.name for p in FRONTIER.glob(f"{a}_*")]), \
            f"{a} has acquired a findings document -- move it out of the unreported set"
