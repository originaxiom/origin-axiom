#!/usr/bin/env python3
"""Review 81, the web seat's file: every quotation of its findings, and the further strings it states of a file, looked for
by machine in the file it names, in a scratch worktree of c40446392 with the window's difference applied (7d7ab1dfa's
content). The control: each quotation with its last word doubled must not be found.

    python3 -I r81_quotes.py CHECKOUT
"""
import pathlib, sys

W = pathlib.Path(sys.argv[1]).resolve()
B98 = "frontier/B1898_review_80_one_hundred_findings_and_what_main_checked/"
B92 = "frontier/B1892_review_79_read_by_those_who_did_not_build_it/FINDINGS.md"
Q = [
    (B98 + "FINDINGS.md", "| agy-exp | `relays/REVIEW_80_AGY-EXP.md` @ `42ac86532` | 14 | 15 of 15 |"),
    (B98 + "STATUS_OF_THE_57.md", "| 18 | B1893, row U12.b | 1,407 files marked, 1,537 by the series' own definition | recount at `e6298271a` | held; noted |"),
    ("docs/POINT_REGISTER.md", "which reproduces the ratio to (−i)^⌊(Re τ + 1)/2⌋ within 5.8 × 10⁻³³ over Re τ ∈ [−5.5, 5.5]"),
    (B92, "the first reader has 52 findings, the second 43, and 9 are common"),
    (B98 + "STATUS_OF_THE_57.md", '| 06 | B1892 § 1 | "one reading misses most" is more than the table supports | the table: 52, 43, 9 in common | held; mended |'),
    (B98 + "STATUS_OF_THE_57.md", "The check's output is in `checks/`."),
    (B98 + "FINDINGS.md", "**80 of them main checked in full, and every one held.**"),
    # further strings the file states of a file
    (B98 + "STATUS_OF_THE_57.md", "and 14 of 14"),
    (B98 + "arc_verdict.json", "14 of 14)"),
    (B92, "the two columns sum to 53 and 43"),
    ("frontier/B1836_the_seats_past_s300_verified/FINDINGS.md", "by at most 5.8 × 10⁻³¹"),
    ("docs/POINT_REGISTER.md", "to 6 × 10⁻³¹"),
    ("docs/POINT_REGISTER.md", "its tracked page is docs/THE_BANG_PROGRAMME.md"),
    ("docs/seats/cld-advisor.md", "Card C15 (register row P-239, its next action)"),
    ("CHANGELOG.md", "B805's two attachment locks (P-239, now card C15)"),
    ("CHANGELOG.md", "five of seven steps done"),
    ("PROGRESS_LOG.md", "the paired pole"),
    ("docs/POINT_REGISTER.md", "taken up after the paired pole's last two steps"),
    ("frontier/B1880_the_third_and_fourth_re_audits_answered/verification/measure_all_hash_lists.py",
     '(HERE / "measure_all_hash_lists_run.txt").write_text'),
    ("frontier/B1893_the_second_enforcement_series_verified_and_landed/FINDINGS.md", "1,537 files at the series' anchor `e6298271a`"),
    ("frontier/B1892_review_79_read_by_those_who_did_not_build_it/verification/quote_check.py",
     "'named' (in the file the finding names, or one of that name where the path is not at"),
    ("papers/P3_THE_PAPER/verification_package/MANIFEST.json", '"git_commits": 4218'),
    ("papers/P3_THE_PAPER/verification_package/MANIFEST.json", '"git_tree_clean": false'),
    ("scripts/checks/point_debt.py", "FLOOR = 836"),
]
bad = 0
for f, q in Q:
    t = (W / f).read_text(encoding="utf-8")
    found = q in t
    w = q.rstrip(" |.*)").split()[-1]
    control = q.replace(w, w + " " + w, 1) if w else q + "x"
    ctrl = control in t
    bad += (not found) + ctrl
    print("%-6s %-7s %s" % ("FOUND" if found else "MISSING", "ctrl!" if ctrl else "ctrl ok", f))
print("quotations and strings: %d; not found or control found: %d" % (len(Q), bad))
