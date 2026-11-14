"""B734 lock -- m004 IS congruence, and its level is (4) (correcting B731's 'non-congruence').

CORRECTED 2026-11-11 (the audit's finding E2; the theorem ledger's link C9 and its note of 2026-09-16; the error ledger's E23;
B734's addenda of 2026-07-21 and 2026-09-16).  Until this date this lock asserted "congruence at level (2)^3 = (8)" and that
"the index plateaus at 6 through level 4".  Both are readings in one of THREE groups, and not in the one that decides the level:

    SL(2, O/I)                                          order 3840 at I = (4)
    SL(2, O/I) / {+-1}                                  order 1920: the group PSL(2, O_3) maps to, O_3 being a domain whose only
                                                        square roots of 1 are +-1.  THE STANDARD ONE: Gamma contains Gamma(I)
                                                        exactly when the image of Gamma has the geometric index, 12, here
    SL(2, O/I) / (every central unit of square one)     order 960 at (4), where there are four such units and the image holds
                                                        two.  Containment in this filtration is sufficient for congruence
                                                        and is not necessary

In the standard group the index is 6 at (2) and 12 at (4).  2 is inert in O_3, so the only ideals dividing (4) are (1), (2), (4):
THE LEVEL IS (4).  The old numbers, 6 at (4) and 12 at (8), are the third group's and are kept below as what they are.

What could fail: the image's order at a level; the count of the ambient group; 2 not being inert; or a page of the record
stating the old level with no correction in the same file.

Pure finite-group arithmetic (Gate 5).  O_3 = Z[w], w^2 = -w - 1; the generators A = [[1,1],[0,1]], B = [[1,0],[w^2,1]].

CORRECTED 2026-11-11, later (the advisor seat's sixth re-audit, which computed every number here again in code that shares
none with this file).  This docstring called the pair "Riley's".  Riley's second generator is [[1,0],[-w,1]]; this B is the
inverse of [[1,0],[-w^2,1]], the conjugate of Riley's.  The pair satisfies the knot's relation once B, or A, is inverted and
generates the same group; the two roots of z^2 - z + 1 give the same orders and the same indices, so every number stands.
The same re-audit found that the arc's own claim line still led with level (8), so that the generated spine, which keeps a
line's first 150 characters, showed the old claim alone; and that seven shapes of the old statement passed this file's
sweep.  The line now leads with the correction and the sweep is widened: both are tested below.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _ring(m):
    def mul(p, q):
        (a, b), (c, d) = p, q
        return ((a*c - b*d) % m, (a*d + b*c - b*d) % m)   # O_3 = Z[w], w^2 = -w-1
    def add(p, q): return ((p[0]+q[0]) % m, (p[1]+q[1]) % m)
    def sub(p, q): return ((p[0]-q[0]) % m, (p[1]-q[1]) % m)
    return mul, add, sub


def _image(m, cap=60000):
    mul, add, sub = _ring(m); E, Z = (1 % m, 0), (0, 0)
    def MM(X, Y):
        return (add(mul(X[0], Y[0]), mul(X[1], Y[2])), add(mul(X[0], Y[1]), mul(X[1], Y[3])),
                add(mul(X[2], Y[0]), mul(X[3], Y[2])), add(mul(X[2], Y[1]), mul(X[3], Y[3])))
    def inv(X): return (X[3], sub(Z, X[1]), sub(Z, X[2]), X[0])
    w = (0, 1)
    A = (E, E, Z, E); B = (E, Z, sub(Z, add(E, w)), E)           # figure-eight Riley generators
    gens = [A, inv(A), B, inv(B)]
    seen = {(E, Z, Z, E)}; fr = [(E, Z, Z, E)]
    while fr:
        nf = []
        for X in fr:
            for g in gens:
                Y = MM(X, g)
                if Y not in seen:
                    seen.add(Y); nf.append(Y)
                    if len(seen) > cap: return None
        fr = nf
    return seen


def _sl_order_by_count(m):
    """|SL(2, O_3/m)|, counted: for each (a, d) the pairs (b, c) with b c = a d - 1"""
    mul, _, sub = _ring(m); R = [(a, b) for a in range(m) for b in range(m)]
    products = {}
    for b in R:
        for c in R:
            products[mul(b, c)] = products.get(mul(b, c), 0) + 1
    return sum(products.get(sub(mul(a, d), (1 % m, 0)), 0) for a in R for d in R)


_SL = {2: 60, 4: 3840, 8: 245760}          # 60 * 64^(k-1) at (2)^k; the first two are counted in a test below


def _central(m):
    mul, _, _ = _ring(m)
    return [(a, b) for a in range(m) for b in range(m) if mul((a, b), (a, b)) == (1 % m, 0)]


def _standard_index(m):
    """the index of +-(image) in SL(2, O_3/m): the index of the image in SL(2, O_3/m)/{+-1}, the group PSL(2, O_3) maps to"""
    _, _, sub = _ring(m); Z = (0, 0); img = _image(m)
    minus = (sub(Z, (1 % m, 0)), Z, Z, sub(Z, (1 % m, 0)))
    order = len(img) if minus in img else 2 * len(img)
    return _SL[m] // order


def _index_by_every_central_unit(m):
    """the lock's reading until 2026-11-11: the image and the ambient group each divided by the central units of square one
    that IT holds.  Equivalently the index of image.Z in SL, Z the full group of such units: not the group PSL(2, O_3) maps to."""
    Z = (0, 0); img = _image(m); cen = _central(m)
    in_img = [c for c in cen if (c, Z, Z, c) in img]
    return (_SL[m] // len(cen)) // (len(img) // len(in_img)), len(cen), len(in_img)


def test_the_ambient_orders_are_counted_and_two_is_inert():
    assert _sl_order_by_count(2) == _SL[2] == 60 and _sl_order_by_count(4) == _SL[4] == 3840
    assert _SL[8] == 60 * 64 ** 2
    # no element of O_3 has norm 2 (a^2 - ab + b^2 = 2 has no solution), so (2) is prime and the divisors of (4) are (1), (2), (4)
    assert not [(a, b) for a in range(-3, 4) for b in range(-3, 4) if a * a - a * b + b * b == 2]


def test_m004_is_congruence_at_level_4():
    assert len(_image(2)) == 10 and len(_image(4)) == 320 and len(_image(8)) == 20480
    assert _standard_index(2) == 6             # Gamma does not contain Gamma((2))
    assert _standard_index(4) == 12            # the geometric index: Gamma contains Gamma((4)).  160 in 1920
    assert _standard_index(8) == 12            # and so Gamma((8)), a smaller group, as well
    assert _SL[4] // 2 == 1920 and len(_image(4)) // 2 == 160


def test_the_old_reading_was_the_quotient_by_every_central_unit():
    # the three groups at level (4) (E23): 3840, 1920 and 960
    assert (_SL[4], _SL[4] // 2, _SL[4] // len(_central(4))) == (3840, 1920, 960)
    assert _index_by_every_central_unit(2) == (6, 1, 1)
    assert _index_by_every_central_unit(4) == (6, 4, 2)      # four central units of square one, and the image holds two: +-1
    assert _index_by_every_central_unit(8) == (12, 8, 8)     # at (8) the image holds all eight
    # so "6 through level 4, then 12 at level 8" is this filtration's reading, and the "plateau" was the quotient and not the group
    assert [_standard_index(m) for m in (2, 4, 8)] == [6, 12, 12]


# the pages that stated the old level, each of which now carries the correction (a correction is swept for: Review 78)
CARRIED = ("frontier/B734_m004_is_congruence/FINDINGS.md", "frontier/B734_m004_is_congruence/arc_verdict.json",
           "frontier/B731_object_observer_noncongruence/FINDINGS.md", "frontier/B731_object_observer_noncongruence/arc_verdict.json",
           "frontier/B732_conjugation_is_out_A5/FINDINGS.md", "frontier/B733_observer_space/FINDINGS.md",
           "frontier/B1067_rayclass_harvest/FINDINGS.md", "docs/LAW_MAP.md", "docs/THEOREM_REGISTRY.md", "docs/ERROR_LEDGER.md",
           "papers/candidates/PC27_one_arithmetic_knot/PAPER.md", "papers/candidates/PC27_one_arithmetic_knot/PAPER_CARD.md",
           "papers/P3_THE_PAPER/CLAIM_CANDIDATES.md", "frontier/B736_ABC_campaign/p1_consolidation.md",
           "frontier/B779_convergence_probe/R3_scattering_assessment.md", "frontier/B779_convergence_probe/R6_maass_assessment.md",
           "frontier/B942_l113_bc_falsifier/FINDINGS.md",
           # found by the widened sweep of 2026-11-11: a verdict line, a dated note among the open leads, a row of the relay ledger
           "frontier/B942_l113_bc_falsifier/arc_verdict.json", "docs/OPEN_LEADS.md", "docs/RELAY_LEDGER.md")
# the old statement's spellings.  Four were added on 2026-11-11 from the advisor seat's sixth re-audit (its § 2.4), and the last
# four on the same date from a second reading that planted eleven errors against this lock, of which it caught five: the group
# of level (8) written with one bracket, and the level written as a power with none
OLD = re.compile(r"level \(8\)|(?<![A-Za-z])\(2\)\^3|(?<![A-Za-z])\(2\)³|level-\(8\)|congruence `\(8\)`|level 8(?![\w.])|Γ\(\(8\)\)|Gamma\(\(8\)\)|level \$\(8\)\$"
                 r"|Γ\(8\)|Gamma\(8\)|level 2\^3|level 2³")
MARK = "the congruence level is (4)"
ABOUT = re.compile(r"m004|figure-eight|B734|B731|4₁|4_1")          # the knot by its name in the tables, added with the spellings above
# records of what was said at the time: logs, reviews, handoffs, readers' outputs, sweeps of other arcs, and the addenda themselves
HISTORY = ("PROGRESS_LOG.md", "CHANGELOG.md", "docs/progress/", "docs/handoffs/", "docs/views/", "docs/HINT_LEDGER.md", "docs/IDENTIFICATION_LEDGER.md",
           "docs/THE_LADDER.md", "docs/RETRACTIONS.md", "frontier/B1469_", "frontier/B1490_", "frontier/B1830_", "frontier/B738_", "frontier/B799_",
           "frontier/B734_m004_is_congruence/ADDENDUM", "frontier/B731_object_observer_noncongruence/ADDENDUM", "frontier/B1861_", "frontier/B1870_",
           "frontier/B1067_rayclass_harvest/w1_results.json", "papers/P3_THE_PAPER/verification_package/",
           "frontier/B742_negatives_hunt_p1/reviews/",
           # added 2026-11-11 with the widened sweep: two sealed preregistrations, which are never edited, and a reader's report
           "frontier/B736_ABC_campaign/PREREGISTRATION.md", "frontier/B737_candidate_zero/PREREGISTRATION.md", "papers/P3_THE_PAPER/reads_s12/")


# the root pages: the same five that the lock on the freedom ledger's zero reads (until 2026-11-11 this lock read the README alone)
ROOT_PAGES = ("README.md", "ROADMAP.md", "GENESIS.md", "CLAIMS.md", "GOVERNANCE.md")


def _states_the_old_level(text):
    """True where a paragraph of `text` states the old level for this group.  A paragraph and not a line, so that the statement
    broken over two lines is seen (the re-audit's first shape)."""
    for para in re.split(r"\n\s*\n", text):
        rows = [l for l in para.split("\n") if l.lstrip().startswith("|")]
        units = rows + [" ".join(l for l in para.split("\n") if not l.lstrip().startswith("|"))]      # a table's row is a unit of its own
        for u in units:
            u = " ".join(u.split())
            if OLD.search(u) and ABOUT.search(u) and re.search(r"congruen", u, re.I):
                return True
    return False


def _swept():
    """every page that could state it: the .md and .tex files under docs/, frontier/ and papers/, the README at the root, and
    every arc's verdict line"""
    for top in ("docs", "frontier", "papers"):
        for ext in ("*.md", "*.tex"):
            for p in (ROOT / top).rglob(ext):
                yield p.relative_to(ROOT).as_posix(), p
    for rel in ROOT_PAGES:
        yield rel, ROOT / rel
    for p in (ROOT / "frontier").glob("*/arc_verdict.json"):
        yield p.relative_to(ROOT).as_posix(), p


def test_every_page_that_stated_level_8_carries_the_correction():
    for rel in CARRIED:
        assert MARK in (ROOT / rel).read_text(encoding="utf-8"), rel
    # and no other page states the old level for this group without the correction in the same file
    loose = []
    for rel, p in _swept():
        if rel.startswith(HISTORY) or any(h in rel for h in HISTORY):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        if MARK in text:
            continue
        if rel.endswith(".json"):
            try:
                text = _of_a_verdict_file(text)
            except Exception:
                continue
        if _states_the_old_level(text):
            loose.append(rel)
    assert not loose, loose


def _of_a_verdict_file(raw):
    """What is swept of a verdict file: its claim line, its scope and its note, each a paragraph of its own.
    CHANGED 2026-11-12 (Review 80; a reader's finding F14, not checked by main, made again here).  The line was
        text = json.loads(text).get("claim_one_line", "")
    and the sweep of B1028's lock beside it reads the three fields.  The old level stated in a verdict's scope or note was
    not seen here."""
    d = json.loads(raw)
    return "\n\n".join(str(d[k]) for k in ("claim_one_line", "scope", "note") if d.get(k))


def test_the_sweep_reads_a_verdict_files_scope_and_note_as_well_as_its_line():
    """Planted: a verdict file that states the old level in its scope, and one that states it in its note, with a claim line
    that says nothing of it.  Read by the claim line alone, as this lock read a verdict file, neither is seen."""
    by_the_line_alone = lambda raw: _states_the_old_level(json.loads(raw).get("claim_one_line", ""))
    base = {"id": "B0", "claim_one_line": "A statement about another matter. 0 of 19.",
            "scope": {"frame": "none", "object": "the figure-eight knot group", "reach": "single", "hypotheses": "none"}}
    in_the_scope = json.dumps(dict(base, scope=dict(base["scope"], hypotheses="m004 is a congruence subgroup of level 8")))
    in_the_note = json.dumps(dict(base, note="The figure-eight knot group is congruence at level (8)."))
    for what, raw in (("in the scope", in_the_scope), ("in the note", in_the_note)):
        assert not by_the_line_alone(raw), what
        assert _states_the_old_level(_of_a_verdict_file(raw)), what
    assert not _states_the_old_level(_of_a_verdict_file(json.dumps(base)))                 # a twin: the same file with neither
    corrected = json.dumps(dict(base, note="The figure-eight knot group is congruence at level (8). [Corrected: " + MARK + ".]"))
    assert MARK in corrected                                                              # and a file that carries the correction is not read further, as before


def test_the_sweep_sees_the_shapes_the_re_audit_planted():
    """the advisor seat's sixth re-audit, § 2.4: six shapes of the old statement that passed.  (Its seventh, the statement added
    to a page that carries the correction in another row, still passes: a page that carries the correction is not read
    further, which is the rule this sweep states.)"""
    shapes = ["The figure-eight knot group m004 is congruence\nat level (8).",                              # over two lines
              "m004 is a congruence subgroup of level 8, deeper than its sister.",                          # no brackets
              "the figure-eight knot group first becomes congruence at Γ((8))",
              "The figure-eight knot group is congruence at level $(8)$ \\cite{b734}."]                     # as a .tex source would write it
    for s in shapes:
        assert _states_the_old_level(s), s
    assert not _states_the_old_level("m004 is congruence at level (4); it also contains the group of level 16.")
    assert not _states_the_old_level("a level 8 subgroup of another manifold altogether")                  # not about this group
    assert not _states_the_old_level("| B306 | the saddle is SU(2)^3 |\n| B734 | m004 is congruence |")      # another row, another object
    assert _states_the_old_level("| B734 | m004 IS congruence at level (2)³=(8) |")
    kinds = {rel.rsplit(".", 1)[-1] for rel, _ in _swept()}
    assert {"md", "tex", "json"} <= kinds and set(ROOT_PAGES) <= {rel for rel, _ in _swept()}


def test_the_sweep_sees_the_shapes_a_second_reading_planted():
    """Of eleven errors a second reading planted against this lock on 2026-11-11 it caught five.  Five of the six it missed are
    seen now: the statement in the foundation and in the claims ledger (two root pages it did not read), the knot written by
    its name in the tables, the group of level (8) with one bracket, and the level as a power with no bracket.  THE SIXTH IS
    NOT: a statement on the programme's page, which this lock still lists among the records of the audit; and the correction
    still has only to stand somewhere in the same file, not beside the statement (twenty units in twelve files would need it,
    counted on that date).  Both are owed."""
    for s in ("The knot 4₁ has a congruence group of level (8).",
              "the figure-eight knot group contains Γ(8) and not Γ(4), so it is congruence at that level",
              "the figure-eight knot group is a congruence subgroup of level 2³",
              "m004 is congruence of level 2^3 in its Bianchi group"):
        assert _states_the_old_level(s), s
    assert not _states_the_old_level("the figure-eight knot group contains Γ(4), hence is congruence of level (4)")
    assert not _states_the_old_level("the knot 5₂ is not congruence at any level; 4₁ is treated in B734")      # names the knot, states no level (8)


def test_the_arcs_own_line_leads_with_the_correction():
    """the advisor seat's sixth re-audit, § 2.3: the correction stood after the old claim, the spine keeps a line's first 150
    characters, and so a generated page marked as proved the statement the record says is wrong"""
    c = json.loads((ROOT / "frontier" / "B734_m004_is_congruence" / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert c.startswith("CORRECTED 2026-11-11 (the audit's finding E2): THE FIGURE-EIGHT KNOT GROUP IS A CONGRUENCE SUBGROUP OF LEVEL (4)")
    assert not OLD.search(c[:150]) and "LEVEL (4)" in c[:150]
    assert "ORIGINAL CLAIM AS ASSERTED: π₁(m004) reaches the geometric index 12 at level (2)³=(8)" in c
    assert c.index(MARK) < c.index("ORIGINAL CLAIM AS ASSERTED")


def test_the_withdrawn_gloss_is_withdrawn_where_it_stood():
    """the same re-audit, § 2.5: the theorem ledger withdrew the gloss that the group defies a base rate on 2026-09-16, and it
    still stood in three places"""
    for rel in ("frontier/B734_m004_is_congruence/FINDINGS.md", "docs/LAW_MAP.md", "docs/THEOREM_REGISTRY.md"):
        assert "the gloss that the group defies a base rate is withdrawn" in (ROOT / rel).read_text(encoding="utf-8"), rel
    assert "gloss is withdrawn" in (ROOT / "docs" / "THEOREM_LEDGER.md").read_text(encoding="utf-8")


# ---------------------------------------------------------------------------------------------------------------------------
# 2026-11-12 (R80b, part 6; a reader's supplement on the arcs main changed at Review 80, its findings 4, 5, 6, 8, 9 and 10).
# Not checked by main, but the orders of finding 6, which main computed and which are computed again below.  Nothing above this
# line is changed.  What the supplement found: the correction stood beside one place of a page and not beside the others; it
# stood in one file of an arc and not in its siblings; the scripts were never swept; the withdrawn gloss stood in two more
# pages; and the note on the image's order at (8) did not say in which group.
THE_ORDERS = ("The image in SL(2, O₃/(2ᵏ)) has order 10, 320, 20,480 at k = 1, 2, 3 (index 6, 12, 12). At (8): 10,240 in 122,880 modulo ±1; "
              "2,560 in 30,720 modulo all eight units of square one.")
THE_GLOSS = "The gloss that the group defies a base rate is withdrawn"
# file -> the sentences it must hold.  MARK is main's own, above.
PLACED_AT_REVIEW_80 = {
    "frontier/B732_conjugation_is_out_A5/FINDINGS.md": (MARK, "how to read this page. Where it says level (8) or (2)^3 for m004, read the"),
    "frontier/B733_observer_space/FINDINGS.md": (MARK, "Where this page\nsays (8)-door, level (8) or level 8 for m004, read that correction."),
    "frontier/B942_l113_bc_falsifier/FINDINGS.md": (MARK, "At (8): 10,240 in 122,880 modulo ±1; 2,560 in 30,720 modulo all eight units of square one.",
                                                    "The order this page quotes, 2560, is the second"),
    "frontier/B1067_rayclass_harvest/FINDINGS.md": (MARK, THE_GLOSS),
    "frontier/B736_ABC_campaign/p1_consolidation.md": (MARK, THE_GLOSS, THE_ORDERS, "the gloss \"Serre-defying\" is withdrawn; see the note at the head of this page",
                                                       "row 1.3 of the table above calls B734 Serre-defying. The gloss is withdrawn"),
    "frontier/B736_ABC_campaign/FINDINGS.md": (MARK, THE_ORDERS, "Where this page says G₈, level (8) or (2)³ for m004, read that."),
    "frontier/B736_ABC_campaign/p2_kms.py": (MARK, "Where this script says level (8), (2)^3 or G_8 for m004, read that.", "2,560 in 30,720 modulo all eight units of square one."),
    "frontier/B736_ABC_campaign/p3_reduction.py": (MARK, "Where this script says level (8), (2)^3 or G_8 for m004, read that."),
    "frontier/B779_convergence_probe/R6_maass_assessment.py": (MARK, "Where this script says level (8), (2)^3 or G_8 for m004, read that."),
    "frontier/B779_convergence_probe/R7_functor_assessment.md": (MARK, "Where this page says level (8) for m004, read that."),
}
# scripts that state the old level and carry no correction, as found on 2026-11-12: three cells of other arcs, which the
# supplement does not name and this patch does not read.  A name leaves this table when its script carries the correction.
SCRIPTS_AS_FOUND = ("frontier/B754_p2_spectral/cells/TOMB-L30/compute.py", "frontier/B771_phase1_wave1/cells/OI-146/compute.py",
                    "frontier/B773_chord_recompute/cells/OI-146-fix/compute.py")


def _what_the_places_of_review_80_lack(read):
    """(file, sentence) for each sentence a file of the table does not hold.  `read` gives a file's text by its name."""
    return [(rel, s) for rel, ss in PLACED_AT_REVIEW_80.items() for s in ss if s not in read(rel)]


def _the_scripts_that_state_the_old_level(files):
    """of (name, text) pairs: the names whose text states the old level for this group and does not carry the correction"""
    return sorted(rel for rel, text in files if MARK not in text and _states_the_old_level(text))


def _the_scripts():
    for p in sorted((ROOT / "frontier").rglob("*.py")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(HISTORY) or any(h in rel for h in HISTORY):
            continue
        try:
            yield rel, p.read_text(encoding="utf-8")
        except Exception:
            continue


def test_the_orders_at_level_8_are_computed_and_are_the_ones_the_notes_give():
    img = {m: len(_image(m)) for m in (2, 4, 8)}
    commas = lambda n: format(n, ",")
    cen = _central(8)
    Z = (0, 0)
    assert len(cen) == 8 and all((c, Z, Z, c) in _image(8) for c in cen)          # the image at (8) holds all eight, so both quotients divide it evenly
    said = ("The image in SL(2, O₃/(2ᵏ)) has order %s, %s, %s at k = 1, 2, 3 (index %d, %d, %d). At (8): %s in %s modulo ±1; "
            "%s in %s modulo all eight units of square one." % (
                commas(img[2]), commas(img[4]), commas(img[8]), _SL[2] // img[2], _SL[4] // img[4], _SL[8] // img[8],
                commas(img[8] // 2), commas(_SL[8] // 2), commas(img[8] // len(cen)), commas(_SL[8] // len(cen))))
    assert said == THE_ORDERS
    # the index is 12 in either quotient at (8); what differs is the group, and so the image's order
    assert (_SL[8] // 2) // (img[8] // 2) == (_SL[8] // 8) // (img[8] // 8) == 12 and img[8] // 2 != img[8] // 8


def test_the_correction_stands_where_review_80_found_it_missing():
    read = lambda rel: (ROOT / rel).read_text(encoding="utf-8")
    assert _what_the_places_of_review_80_lack(read) == []
    # planted: each file as it stood before the notes, by taking out the lines that hold a sentence of the table
    for rel, ss in PLACED_AT_REVIEW_80.items():
        new = [s for s in ss if s != MARK or rel.endswith((".py", "R7_functor_assessment.md", "B736_ABC_campaign/FINDINGS.md"))]
        text = read(rel)
        for s in new:
            without = text.replace(s, "")
            lack = _what_the_places_of_review_80_lack(lambda r, rel=rel, without=without: without if r == rel else read(r))
            assert (rel, s) in lack, (rel, s)
    # the pages that call the result by the withdrawn gloss say that it is withdrawn, as many times as they use it or once at their head
    for rel in ("frontier/B1067_rayclass_harvest/FINDINGS.md", "frontier/B736_ABC_campaign/p1_consolidation.md"):
        assert "Serre-defying" in read(rel) and THE_GLOSS in read(rel)


def test_no_script_states_the_old_level_without_the_correction_but_the_three_held_as_found():
    assert _the_scripts_that_state_the_old_level(_the_scripts()) == sorted(SCRIPTS_AS_FOUND)
    # planted: a script as B736's stood, and its twin with the correction; a script about another group; one that names no congruence
    as_it_stood = "# the observer of m004: congruence at level (2)^3=(8), image order 2560\nk = 3\n"
    assert _the_scripts_that_state_the_old_level([("a.py", as_it_stood)]) == ["a.py"]
    assert _the_scripts_that_state_the_old_level([("a.py", "# " + MARK + "\n" + as_it_stood)]) == []
    assert _the_scripts_that_state_the_old_level([("a.py", "# the sister m003 is congruence at level (2)\n")]) == []
    assert _the_scripts_that_state_the_old_level([("a.py", "# the ring at (2)^3: 64 elements\n")]) == []
    # the three scripts of this patch were among them before it
    for rel in ("frontier/B736_ABC_campaign/p2_kms.py", "frontier/B736_ABC_campaign/p3_reduction.py", "frontier/B779_convergence_probe/R6_maass_assessment.py"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        i, j = text.index("# [PLACED HERE 2026-11-12"), text.index("is not made again.]\n")
        before = text[:i] + text[j + len("is not made again.]\n"):]
        assert MARK not in before and _the_scripts_that_state_the_old_level([(rel, before)]) == [rel], rel


def test_the_note_on_b736s_page_leaves_the_opening_that_the_atlas_reads_as_it_was():
    """A fault of the patch that placed the notes, found before it was sent: a note at the head of B736's page moved the tag
    the atlas guesses from a page's first 1,500 characters, from dead to banked.  The note stands below that opening."""
    page = (ROOT / "frontier/B736_ABC_campaign/FINDINGS.md").read_text(encoding="utf-8")
    assert page.index("[PLACED HERE 2026-11-12") > 1500 and page.index("G₈=PSL(2,O₃/(8))") < page.index("[PLACED HERE 2026-11-12") < page.index("### Path C")
    atlas = json.loads((ROOT / "scripts" / "atlas" / "atlas_data.json").read_text(encoding="utf-8"))
    assert atlas["probes"]["B736"]["status"] == "dead"
    # the other pages that this patch placed a note on: none is placed in the opening of a page of findings but B732's, whose tag it does not move
    assert atlas["probes"]["B732"]["status"] == "banked" and "[ADDED 2026-11-12" in (ROOT / "frontier/B732_conjugation_is_out_A5/FINDINGS.md").read_text(encoding="utf-8")[:1500]
