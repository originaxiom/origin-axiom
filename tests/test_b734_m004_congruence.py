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
# the old statement's spellings.  The last four were added on 2026-11-11 from the advisor seat's sixth re-audit (its § 2.4)
OLD = re.compile(r"level \(8\)|(?<![A-Za-z])\(2\)\^3|(?<![A-Za-z])\(2\)³|level-\(8\)|congruence `\(8\)`|level 8(?![\w.])|Γ\(\(8\)\)|Gamma\(\(8\)\)|level \$\(8\)\$")
MARK = "the congruence level is (4)"
ABOUT = re.compile(r"m004|figure-eight|B734|B731")
# records of what was said at the time: logs, reviews, handoffs, readers' outputs, sweeps of other arcs, and the addenda themselves
HISTORY = ("PROGRESS_LOG.md", "CHANGELOG.md", "docs/progress/", "docs/handoffs/", "docs/views/", "docs/HINT_LEDGER.md", "docs/IDENTIFICATION_LEDGER.md",
           "docs/THE_LADDER.md", "docs/RETRACTIONS.md", "frontier/B1469_", "frontier/B1490_", "frontier/B1830_", "frontier/B738_", "frontier/B799_",
           "frontier/B734_m004_is_congruence/ADDENDUM", "frontier/B731_object_observer_noncongruence/ADDENDUM", "frontier/B1861_", "frontier/B1870_",
           "frontier/B1067_rayclass_harvest/w1_results.json", "papers/P3_THE_PAPER/verification_package/",
           "frontier/B742_negatives_hunt_p1/reviews/",
           # added 2026-11-11 with the widened sweep: two sealed preregistrations, which are never edited, and a reader's report
           "frontier/B736_ABC_campaign/PREREGISTRATION.md", "frontier/B737_candidate_zero/PREREGISTRATION.md", "papers/P3_THE_PAPER/reads_s12/")


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
    yield "README.md", ROOT / "README.md"
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
                text = json.loads(text).get("claim_one_line", "")
            except Exception:
                continue
        if _states_the_old_level(text):
            loose.append(rel)
    assert not loose, loose


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
    assert {"md", "tex", "json"} <= kinds and any(rel == "README.md" for rel, _ in _swept())


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
