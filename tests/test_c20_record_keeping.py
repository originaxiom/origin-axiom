"""Card C20 (2026-11-14, main's M31): three record-keeping debts of the register, each written down where it belongs.
Every statement in the notes is a quotation of the register's row or of the arcs it names; none is the builder's."""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTER = ROOT / "docs" / "POINT_REGISTER.md"


def _row(pid):
    return next(l for l in REGISTER.read_text(encoding="utf-8").split("\n") if l.startswith("| %s |" % pid))


# --- P-310: B335's sentence on the generation Z/3 overstates, as its reader found ---

B335 = ROOT / "frontier" / "B335_generation_symmetry_exact"
B325 = ROOT / "frontier" / "B325_z3_protection_refuted"
OLD_310 = "so every real geometric invariant (and any mass) is exactly degenerate"
NOTE_310 = "**[NOTED 2026-11-14 (the building session, at main's word in M31, card C20; register row P-310):"


def _p310_problems(page, claim):
    bad = []
    at = page.find(NOTE_310)
    if at < 0:
        return ["no note on the page"]
    note = page[at:page.index("]\n", at)]
    if "masses (real, positive" not in page[:at]:
        bad.append("the note does not stand after the old words")
    for words in (OLD_310, "B325 and a 3×3 circulant check split the masses",
                  "Refuted the claimed Z/3-protection of the two light eigenvalues: they are distinct 1-dim irreps a Z/3-invariant cubic can split",
                  "the verdict is unchanged"):
        if words not in note:
            bad.append("the note lacks: " + words[:40])
    if "[NOTED 2026-11-14 (P-310)" not in claim:
        bad.append("the verdict line has no note")
    return bad


def test_p310_the_note_stands_after_the_old_words_and_quotes_its_sources():
    page = (B335 / "FINDINGS.md").read_text(encoding="utf-8")
    claim = json.loads((B335 / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert _p310_problems(page, claim) == []
    # what it quotes is where it says: the register's row, B325's verdict line, B335's own sentence
    assert "B325 and a 3×3 circulant check split the masses" in _row("P-310")
    assert "Refuted the claimed Z/3-protection of the two light eigenvalues: they are distinct 1-dim irreps a Z/3-invariant cubic can split" \
        in json.loads((B325 / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert "every real geometric invariant (and any mass) is exactly degenerate" in claim          # the old words kept
    # planted: the note taken out of the page; the note moved above the old words; the verdict line's note taken out
    at = page.index(NOTE_310); end = page.index("]\n", at) + 2
    assert _p310_problems(page[:at] + page[end:], claim) == ["no note on the page"]
    moved = page[at:end] + page[:at] + page[end:]
    assert _p310_problems(moved, claim) == ["the note does not stand after the old words"]
    assert _p310_problems(page, claim[:claim.index(" [NOTED 2026-11-14 (P-310)")]) == ["the verdict line has no note"]


# --- P-334: the sweep's answered items, each written down where it belongs ---

import re

NOTE_334 = "**[NOTED 2026-11-14 (the building session, at main's word in M31, card C20; register row P-334):"
ITEMS_334 = (   # (where the note stands: a lead or an arc, the row's words for the item)
    ("L206", "L206 (b = mer⁻¹a⁻¹mer⁻¹a⁻³, J(m003) ≤ 4)"),
    ("L215", "L215 (the graded trace is ε₃·f₅, the squares mod 15; a note on B1406)"),
    ("L207", "L207 (∣κ − 2∣ invariant on depth-one generating pairs, the sign of Im κ the hand)"),
    ("L230", "L230 (c) (three classes; GAP), (d), (f)"),
    ("L193", "L193 (CS-silent ⇔ amphichiral on 1490 word states)"),
    ("L194", "L194 (b) (a theorem on the one-cusped census)"),
    ("L191", "L191 (B502 dead at depth 4)"),
    ("B1406", "L215 (the graded trace is ε₃·f₅, the squares mod 15; a note on B1406)"),
    ("B507", "B507's closed form g_M(κ) = Cl₂(2θ)/(π − θ)"),
    ("B499", "B499 (W3, W5 killed)"),
)


def _lead_section(text, lead):
    m = re.search(r"^## %s\b" % lead, text, re.M)
    nxt = re.search(r"^## ", text[m.end():], re.M)
    return text[m.start():m.end() + nxt.start() if nxt else len(text)]


def _arc_page(arc):
    for v in sorted(ROOT.glob("frontier/%s_*/arc_verdict.json" % arc)):
        if json.loads(v.read_text(encoding="utf-8")).get("id") == arc:
            return (v.parent / "FINDINGS.md").read_text(encoding="utf-8")


def _p334_unwritten(leads, pages):
    bad = []
    for where, words in ITEMS_334:
        text = _lead_section(leads, where) if where.startswith("L") else pages[where]
        if text.count(NOTE_334) != 1 or "“%s”" % words not in text[text.find(NOTE_334):]:
            bad.append(where)
    return bad


def test_p334_each_answered_item_is_written_down_where_it_belongs():
    row = _row("P-334")
    assert all(words in row for _, words in ITEMS_334)                    # each quotation is the row's
    leads = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    pages = {w: _arc_page(w) for w, _ in ITEMS_334 if not w.startswith("L")}
    assert _p334_unwritten(leads, pages) == []
    assert leads.count(NOTE_334) == 7 and sum(p.count(NOTE_334) for p in pages.values()) == 3
    # planted: one lead's note taken out; one note moved into the next lead; one arc's quotation altered
    sec = _lead_section(leads, "L193")
    out = leads.replace(sec, sec[:sec.index("\n" + NOTE_334)] + "\n\n", 1)
    assert _p334_unwritten(out, pages) == ["L193"]
    s206, s207 = _lead_section(leads, "L206"), _lead_section(leads, "L207")
    note206 = s206[s206.index("\n" + NOTE_334):]
    moved = leads.replace(s206, s206.replace(note206, "\n\n"), 1).replace(s207, s207 + note206, 1)
    assert _p334_unwritten(moved, pages) == ["L206", "L207"]
    assert _p334_unwritten(leads, dict(pages, B507=pages["B507"].replace("Cl₂(2θ)/(π − θ)", "Cl₂(θ)/(π − θ)"))) == ["B507"]


# --- P-319: the frozen paper's two citations with successors, and the supersession generator ---

import importlib.util, sys as _sys

P9 = ROOT / "papers" / "P9_what_a_grammar_fixes"


def _generator():
    spec = importlib.util.spec_from_file_location("supersession_tier_for_c20", ROOT / "scripts" / "checks" / "supersession_tier.py")
    m = importlib.util.module_from_spec(spec); _sys.dont_write_bytecode = True; spec.loader.exec_module(m)
    return m


def test_p319_the_errata_sets_out_each_pair_in_its_sources_words_and_enters_no_correction():
    errata = (P9 / "ERRATA.md").read_text(encoding="utf-8")
    assert "**no correction is entered**" in errata and "main's to decide" in errata
    s02 = (P9 / "tex" / "sections" / "s02_grammar_seed.tex").read_text(encoding="utf-8")
    s05 = (P9 / "tex" / "sections" / "s05_couplings.tex").read_text(encoding="utf-8")
    b1662 = next(ROOT.glob("frontier/B1662_*/FINDINGS.md")).read_text(encoding="utf-8")
    b1658 = next(ROOT.glob("frontier/B1658_*/FINDINGS.md")).read_text(encoding="utf-8")
    for quoted, source in (
            ("The place where a hand can be registered on a spin structure (B1479, B1481) is generated by the moves.", s02),
            ("In the twisted frame of B1656, under equal framed data, one Higgs keeps the sectors' values of $t+1/t$ within a factor",
             " ".join(s05.split())),
            ('**B1479:** "not yet generated" superseded; P1–P3 stand.', b1662),
            ('So "one Higgs, under equal framed data, in B1656\'s frame" is refuted', " ".join(b1658.split()))):
        assert quoted.replace('"', '\\"') in errata or quoted in errata, quoted[:40]
        assert quoted in source, quoted[:40]


def test_p319_the_generator_flags_the_two_pairs_and_can_fail():
    g = _generator()
    rows = g.report(["P9"])
    pairs = {(n, later) for _, n, later, _, _ in rows}
    assert (1479, 1662) in pairs and (1656, 1658) in pairs
    # planted: the successors' lines read without their words of supersession are not flagged
    said = g.said_of()
    said_without = {n: [r for r in v if not (r[0] in (1662, 1658) and n in (1479, 1656))] for n, v in said.items()}
    pairs_without = {(n, later) for _, n, later, _, _ in g.report(["P9"], said_without)}
    assert (1479, 1662) not in pairs_without and (1656, 1658) not in pairs_without
    # and a line with no word of supersession is not read as one
    assert not g.WORDS.search("B1656's twisted frame under equal framed data") and g.WORDS.search("B1479 (wording) re-graded")
