"""Review 81: the faults main plants in the readers' reading commit (register row of the opening; R80-12, P-824).
SEALED: this file's sha256 is published in the opening commit before the reading commit is made; the file itself is
published at the entry. Each plant must occur exactly once and must change its file (a plant that changes nothing stops
the run). Run from the root of a worktree at main's 0e637ea9e:  python3 plants.py ROOT"""
import sys, pathlib

PLANTS = [
    ("P1", "a number that differs from its source (quote_check_agyexp.json gives 14)",
     "frontier/B1898_review_80_one_hundred_findings_and_what_main_checked/FINDINGS.md",
     "| agy-exp | `relays/REVIEW_80_AGY-EXP.md` @ `42ac86532` | 14 | 14 of 14 |",
     "| agy-exp | `relays/REVIEW_80_AGY-EXP.md` @ `42ac86532` | 14 | 15 of 15 |"),
    ("P2", "a label stronger than its evidence, and a claim wider than computed (1,332 sequences were computed)",
     "frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/FINDINGS.md",
     "**On row A1** [NOTED 2026-11-12 (Review 80; a reader's finding, checked by main with a computation of its own)]",
     "**On row A1** [NOTED 2026-11-12 (Review 80; a reader's finding, proved by main for every sequence)]"),
    ("P3", "a check that cannot fail (a count of 1,332 sequences is never above 1,332)",
     "frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/verification/test_b1895_the_mends_of_b1881_read.py",
     "== conj(_word(seq, *_SEAT))) < 1332",
     "== conj(_word(seq, *_SEAT))) <= 1332"),
    ("P4", "a session written as an authority (P-797)",
     "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/FINDINGS.md",
     "found by a reading on another family of model and reproduced by main).** Five, not",
     "confirmed by agy-002, whose reading settles it).** Five, not"),
    ("P5", "a claim wider than what was computed (three tests were found)",
     "frontier/B1896_the_third_enforcement_series_verified_and_landed/FINDINGS.md",
     "with three tests on main's pages that are of this shape",
     "with every test on main's pages that is of this shape"),
    ("P6", "a number that differs from its source (the run file gives 5.8 x 10^-31)",
     "docs/POINT_REGISTER.md",
     "within 5.8 × 10⁻³¹ over Re τ",
     "within 5.8 × 10⁻³³ over Re τ"),
]

if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1])
    for pid, kind, path, old, new in PLANTS:
        p = root / path; t = p.read_text(encoding="utf-8")
        assert t.count(old) == 1, (pid, "the site must occur exactly once", t.count(old))
        u = t.replace(old, new)
        assert u != t, (pid, "a plant that changes nothing")
        p.write_text(u, encoding="utf-8")
        print(pid, "planted in", path)
