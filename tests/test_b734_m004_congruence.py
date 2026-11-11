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

Pure finite-group arithmetic (Gate 5).  O_3 = Z[w], w^2 = -w - 1; Riley's generators A = [[1,1],[0,1]], B = [[1,0],[w^2,1]].
"""
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
           "frontier/B942_l113_bc_falsifier/FINDINGS.md")
OLD = re.compile(r"level \(8\)|\(2\)\^3|\(2\)³|level-\(8\)|congruence `\(8\)`")
MARK = "the congruence level is (4)"
# records of what was said at the time: logs, reviews, handoffs, readers' outputs, sweeps of other arcs, and the addenda themselves
HISTORY = ("PROGRESS_LOG.md", "CHANGELOG.md", "docs/progress/", "docs/handoffs/", "docs/views/", "docs/HINT_LEDGER.md", "docs/IDENTIFICATION_LEDGER.md",
           "docs/THE_LADDER.md", "docs/RETRACTIONS.md", "frontier/B1469_", "frontier/B1490_", "frontier/B1830_", "frontier/B738_", "frontier/B799_",
           "frontier/B734_m004_is_congruence/ADDENDUM", "frontier/B731_object_observer_noncongruence/ADDENDUM", "frontier/B1861_", "frontier/B1870_",
           "frontier/B1067_rayclass_harvest/w1_results.json", "papers/P3_THE_PAPER/verification_package/",
           "frontier/B742_negatives_hunt_p1/reviews/")


def test_every_page_that_stated_level_8_carries_the_correction():
    for rel in CARRIED:
        assert MARK in (ROOT / rel).read_text(encoding="utf-8"), rel
    # and no other page states the old level for this group without the correction in the same file
    loose = []
    for top in ("docs", "frontier", "papers"):
        for p in (ROOT / top).rglob("*.md"):
            rel = p.relative_to(ROOT).as_posix()
            if rel.startswith(HISTORY) or any(h in rel for h in HISTORY):
                continue
            try:
                text = p.read_text(encoding="utf-8")
            except Exception:
                continue
            if MARK in text:
                continue
            for line in text.splitlines():
                if OLD.search(line) and re.search(r"m004|figure-eight|B734|B731", line) and re.search(r"congruen", line, re.I):
                    loose.append(rel); break
    assert not loose, loose
