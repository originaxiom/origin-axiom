"""B1028 locks — the global freedom ledger (Lane I-1, sealed e13d09a5)."""
import importlib.util
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1028_freedom_ledger"


def _walk():
    spec = importlib.util.spec_from_file_location("b1028_walk", ARC / "b1028_walk.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_links_all_cited_and_zero():
    m = _walk()
    L = m.links()
    # eleven arrows, none skipped; every priced zero must carry a cite (or the explicit
    # faces row whose content is the separation of ledgers)
    assert len(L) == 11
    assert all(r["price"] == 0.0 for r in L)
    cited = [r for r in L if r["cite"] != "--"]
    assert len(cited) == 10
    # the two named risks are present and marked resolved
    joined = " ".join(r["note"] for r in L)
    assert "NAMED RISK 1 IN THE SEAL, RESOLVED" in joined
    assert "NAMED RISK 2 IN THE SEAL, RESOLVED" in joined
    # the flags are not silently dropped
    assert "FLAG" in joined and "P5" in joined


def test_cite_machinery_actually_checks():
    """The desk audit must FAIL on a wrong phrase — the self-check is load-bearing."""
    m = _walk()
    try:
        m._cite("B994_rule_variation", "THIS PHRASE IS NOT IN THE BANKED VERDICT")
        raised = False
    except AssertionError:
        raised = True
    assert raised, "_cite must reject a phrase absent from the banked claim line"


def test_outputs_and_arithmetic():
    m = _walk()
    O = m.outputs()
    total = sum(r["bits"] for r in O)
    assert abs(total - (2.0 + math.log2(3) + 1.0)) < 1e-12
    # conservative rules visible in the rows themselves
    amb = " ".join(r["ambient"] for r in O)
    assert "CONTINUUM PIN" in amb and "EXCLUDED" in amb
    v = m.verdict()
    assert v["outcome"] == "COMPRESSION"
    assert v["retroactive_bits_in"] == 0.0
    assert abs(v["conservative_bits_out"] - 4.584962500721156) < 1e-12
    assert v["declared_input_bits"] == 3.0


def test_findings_carry_the_verdict():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    flat = " ".join(t.replace("**", "").replace("−", "-").split())
    assert "COMPRESSION" in flat
    assert "0.000 bits" in flat and "4.585" in flat
    assert "named risks both RESOLVE" in flat or "named risks" in flat
    assert "The stop rule does not fire" in flat
    # the both-ways comparison (the strongest honest sentence) is present
    assert "1.585 bits > 0" in flat
    # the pending trit stays pending (not silently adopted)
    assert "recorded pending, not adopted" in flat or "PENDING, not adopted" in flat


def test_verdict_json():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    # CORRECTED 2026-11-11 (the audit's finding E7): the verdict was PROVED.  The ledger's zero is a sum of eleven prices typed
    # 0.0, and its check is a substring match; the verdict is OPEN, and the claim as first asserted is kept after the correction.
    assert v["id"] == "B1028" and v["verdict"] == "OPEN"
    c = v["claim_one_line"]
    assert c.startswith("CORRECTED 2026-11-11 (the audit's finding E7") and "ORIGINAL CLAIM AS ASSERTED: THE GLOBAL FREEDOM LEDGER" in c
    for s in ("NOT PRICED", "the family declaration", "the door set is {1, 4}", "the principal embedding", "THE ONE ENDPOINT IT CREDITS is the algebra of dimension 14"):
        assert s in c, s
    assert "COMPRESSION" in v["claim_one_line"]
    assert "THE STOP RULE DOES NOT FIRE" in v["claim_one_line"]
    for dep in ("B994", "B897", "B862", "B864", "B991", "B997", "B1019"):
        assert dep in v["depends_on"]


def test_prereg_seal_intact():
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    m = re.search(r"^([0-9a-f]{64})\s+frontier/B1028_freedom_ledger/PREREGISTRATION\.md",
                  hashes, re.M)
    assert m and m.group(1).startswith("e13d09a5")
    import hashlib
    actual = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert actual == m.group(1), "sealed prereg must remain byte-identical"


def test_the_zero_is_typed_and_the_check_is_a_substring_match():
    """the audit's finding E7, shown on the walk itself: every price is the literal 0.0 in the source, and the citation
    check passes on a claim line that has since been corrected to say the opposite of what the link needs"""
    m = _walk()
    src = (ARC / "b1028_walk.py").read_text(encoding="utf-8")
    assert src.count("price=0.0") == 11 and len(m.links()) == 11            # eleven typed zeros, and nothing else is summed
    assert "assert bits_in == 0.0" in src
    b997 = json.loads((ROOT / "frontier" / "B997_golden_conductor_uniqueness" / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert "UNIQUE METALLIC GRAMMAR" in b997 and "the door set is {1, 4}" in b997      # the phrase the walk matches, and its correction, in one line
    assert m._cite("B997_golden_conductor_uniqueness", "UNIQUE METALLIC GRAMMAR", "INFINITE FAMILY") == "B997"     # the check still passes


MARK = "the freedom ledger's zero is not a computed quantity"
CARRIED = ("frontier/B1028_freedom_ledger/FINDINGS.md", "frontier/B1028_freedom_ledger/arc_verdict.json", "ROADMAP.md", "docs/THE_CLAIM.md", "docs/THE_FRAMEWORK.md",
           "docs/THE_FINAL_ATTACK_2026-10-29.md", "docs/THE_CROSSINGS_CENSUS_2026-10-13.md", "frontier/B1643_the_crossings_census/FINDINGS.md",
           "frontier/B1030_price_lock_verification/FINDINGS.md", "frontier/B1030_price_lock_verification/arc_verdict.json", "frontier/B1222_symmetry_vanishing_thesis/FINDINGS.md")
# what was said at the time, or says something else by the same words: the logs, the campaign's status history, the plan of the
# campaign, other ledgers' own prices.  The programme's pages on the audit were listed here until 2026-11-11; they are a live page
# and are read like any other (the second reading's note: a statement in them is read by the next stranger)
HISTORY = ("PROGRESS_LOG.md", "CHANGELOG.md", "docs/CAMPAIGN_STATUS.md", "docs/progress/", "docs/handoffs/", "docs/views/", "docs/THE_WHY_CAMPAIGN.md", "docs/CROSSING_REQUIREMENTS.md",
           "docs/FIELD_EXPLORATION_REPORT.md", "docs/GRAND_COMPUTATION_v0.md", "docs/THE_FINAL_ACTS_BAR_2026-10-29.md", "frontier/B1015_", "frontier/B1128_", "frontier/B1349_",
           "frontier/B1028_freedom_ledger/ADDENDUM", "frontier/B1028_freedom_ledger/PREREGISTRATION")
# the arc's own findings lead with the correction and keep the claim below it as it was asserted: the body is the record
OWN_RECORD = ("frontier/B1028_freedom_ledger/FINDINGS.md",)
# the root pages, the same five that the lock on the knot group's level reads
ROOT_PAGES = ("ROADMAP.md", "README.md", "GENESIS.md", "CLAIMS.md", "GOVERNANCE.md")
# the zero as the record spelled it: "0.000 bits", and the walk's own words, "0.000 retroactive designer bits", which the sweep
# did not look for until a second reading found seven statements in them (2026-11-11).  NOT LOOKED FOR: "0 bits" and "no designer
# freedom"; tried on that date, they hit three pages, each another ledger's own price
OLD_ZERO = re.compile(r"0\.000\s+(?:retroactive\s+)?(?:designer\s+)?bits|zero\s+(?:retroactive\s+)?designer\s+freedom", re.I)
ABOUT_LEDGER = re.compile(r"designer|freedom[ -]ledger|B1028", re.I)


# CHANGED 2026-11-13 (C16; a cold reader's finding on R80b's part 3, patch 15, not checked by main, made again first): an item
# of a list was taken only from "-", "*", "+" or a number, so the same list with typographic bullets was one unit.  The
# pattern as it stood:
#     _A_BULLET = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
_A_BULLET = re.compile(r"^\s*(?:[-*+\u2022\u25e6\u2023\u2043\u2219\u25aa\u25cf\u2013\u2014]|\d+[.)]|[a-z][.)])\s+")


def _units(text):
    """What a reader takes in at once: a table's row; an item of a list, with the lines that continue it; and a paragraph's
    prose joined over its line breaks.
    CHANGED 2026-11-12 (Review 80; a reader's finding F13, not checked by main, made again here).  A list with no empty line
    between its items was one unit, so the correction in one item excused the zero stated in another.  Each item is a unit
    of its own now.  The lines before the first item of a paragraph are a unit, as before."""
    for para in re.split(r"\n\s*\n", text):
        rows = [l for l in para.split("\n") if l.lstrip().startswith("|")]
        items, current = [], []
        for l in para.split("\n"):
            if l.lstrip().startswith("|"):
                continue
            if _A_BULLET.match(l) and current:
                items.append(current)
                current = []
            current.append(l)
        if current:
            items.append(current)
        for u in rows + [" ".join(i) for i in items]:
            yield " ".join(u.split())


def _units_as_they_were(text):
    """the units of this sweep until 2026-11-12: a tight list was one unit.  Kept for the planted cases of the test below."""
    for para in re.split(r"\n\s*\n", text):
        rows = [l for l in para.split("\n") if l.lstrip().startswith("|")]
        prose = " ".join(l for l in para.split("\n") if not l.lstrip().startswith("|"))
        for u in rows + [prose]:
            yield " ".join(u.split())


def _bare_statements(text):
    """the units of `text` that state the zero with no correction BESIDE it.  Until 2026-11-11 the correction had only to stand
    somewhere in the same file, and it was read line by line: six pages stated the zero in a paragraph with no correction in it"""
    return [u for u in _units(text) if OLD_ZERO.search(u) and ABOUT_LEDGER.search(u) and MARK.lower() not in u.lower()]


def test_a_correction_in_one_item_of_a_list_does_not_excuse_the_zero_in_another():
    """Added 2026-11-12 (Review 80; a reader's finding F13, not checked by main, made again here).  Planted: a list whose
    first item carries the correction and whose third states the zero; and the list as it stood on B1222's page, the
    correction an item of its own before the item it corrects.  With a list read as one unit, as it was, neither is
    reported.  A twin, the correction inside the item that states the zero, is not reported."""
    note = "[CORRECTED 2026-11-11 (the audit's finding E7): " + MARK + ".]"
    bare_as_it_was = lambda text: [u for u in _units_as_they_were(text) if OLD_ZERO.search(u) and ABOUT_LEDGER.search(u) and MARK.lower() not in u.lower()]
    another_item = "The counterexamples:\n- one thing, noted. " + note + "\n- a second thing\n- **designer freedom 0.000 bits** is a count over the chain"
    as_it_stood = "The counterexamples:\n- a first thing\n- " + note + "\n- **designer freedom 0.000 bits** is a meta-accounting over the chain,\n  not an object vanishing at all"
    for what, text in (("in another item", another_item), ("an item of its own before the item it corrects", as_it_stood)):
        assert not bare_as_it_was(text), what                                    # read as one unit: not reported
        assert len(_bare_statements(text)) == 1, what
    twin = "The counterexamples:\n- a first thing\n- **designer freedom 0.000 bits** is a meta-accounting over the chain,\n  not an object vanishing at all\n  " + note
    assert not _bare_statements(twin) and not bare_as_it_was(twin)
    # the page this was found on carries the correction inside the item now, and says that it was moved
    page = (ROOT / "frontier" / "B1222_symmetry_vanishing_thesis" / "FINDINGS.md").read_text(encoding="utf-8")
    assert not _bare_statements(page) and "[MOVED 2026-11-12 (Review 80;" in page
    assert sum(1 for l in page.split("\n") if l.startswith("- [CORRECTED 2026-11-11 (the audit's finding E7)")) == 0


def _swept():
    """every page that could state it: the .md and .tex files under docs/, frontier/ and papers/, the five root pages, and every
    arc's verdict line"""
    seen = set()
    for top in ("docs", "frontier", "papers"):
        for ext in ("*.md", "*.tex"):
            for p in (ROOT / top).rglob(ext):
                rel = p.relative_to(ROOT).as_posix()
                if rel not in seen:
                    seen.add(rel)
                    try:
                        yield rel, p.read_text(encoding="utf-8")
                    except Exception:
                        continue
    for rel in ROOT_PAGES:
        yield rel, (ROOT / rel).read_text(encoding="utf-8")
    for p in (ROOT / "frontier").glob("*/arc_verdict.json"):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        yield p.relative_to(ROOT).as_posix(), "\n\n".join(str(d[k]) for k in ("claim_one_line", "scope", "note") if d.get(k))


def test_every_page_that_states_the_zero_carries_the_correction():
    for rel in CARRIED:
        assert MARK.lower() in (ROOT / rel).read_text(encoding="utf-8").lower(), rel
    loose = {}
    for rel, text in _swept():
        if rel in OWN_RECORD or any(rel.startswith(h) or h in rel for h in HISTORY):
            continue
        bare = _bare_statements(text)
        if bare:
            loose[rel] = len(bare)
    assert not loose, loose


def test_the_sweep_sees_what_the_second_reading_found():
    """The shapes that stood on main on 2026-11-11 and that the sweep, as it then was, let through: the walk's own words; the
    statement broken over a line; a table's row; and the correction present in the file but not beside the statement."""
    note = "[CORRECTED 2026-11-11 (the audit's finding E7): " + MARK + ".]"
    shapes = ("Lane I-1's freedom-ledger number (B1028: 0.000 retroactive designer bits against a 4.585-bit floor)",
              "assembling the controls with the freedom-ledger number (B1028: 0.000\nretroactive designer bits against a floor) into one statement",
              "| the global freedom ledger | 0.000 retroactive designer bits against a floor | COMPRESSION (B1028) |",
              "- a forced skeleton, with zero designer freedom to the SM's structure;",
              "B1028 lands COMPRESSION: 0.000 bits of retroactive freedom")
    for s in shapes:
        assert _bare_statements(s), s
        assert _bare_statements(s + "\n\nAnother paragraph of the same page. " + note), s        # elsewhere in the file is not beside it
        assert not _bare_statements(s + " " + note), s                                              # beside it is
    # what must not be taken for it: another ledger's price, and a sentence that carries the correction
    for s in ("the price lock costs 0.000 bits of description length in this fit",
              "the twisted-vs-raw weld convention (0 bits), and the listener member (0 bits)",
              "what B1028 called zero designer freedom: " + MARK):
        assert not _bare_statements(s), s


def test_a_list_is_read_by_its_items_whatever_its_bullets():
    """ADDED 2026-11-13 (C16; a cold reader's finding on R80b's part 3, patch 15, not checked by main, made again first).  The
    list of the test above, with typographic bullets: read as one unit, the correction in its first item excused the zero in
    its third.  Each item is read now, with each bullet a list is written with here; the twin is as above."""
    note = "[CORRECTED 2026-11-11 (the audit's finding E7): " + MARK + ".]"
    plain = "The counterexamples:\n- one thing, noted. " + note + "\n- a second thing\n- **designer freedom 0.000 bits** is a count over the chain"
    assert len(_bare_statements(plain)) == 1
    for bullet in ("\u2022", "\u25e6", "\u2023", "\u2043", "\u2219", "\u25aa", "\u25cf", "\u2013", "\u2014", "1.", "a)"):
        text = plain.replace("\n- ", "\n" + bullet + " ")
        assert len(_bare_statements(text)) == 1, repr(bullet)
        twin = text.replace(" is a count over the chain", " is a count over the chain " + note)
        assert _bare_statements(twin) == [], repr(bullet)

