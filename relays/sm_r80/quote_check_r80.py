#!/usr/bin/env python3
"""SM-R80: every quotation of relays/REVIEW_80_SM.md's findings, checked by machine in its file at c40446392 (whitespace
joined, as the files wrap).  The control: the first quotation altered by one character must be reported missing.
Usage (from a clone that has the commit): quote_check_r80.py OUT.json"""
import json, subprocess, sys
R = "c40446392"
B92 = "frontier/B1892_review_79_read_by_those_who_did_not_build_it/"
B93 = "frontier/B1893_the_second_enforcement_series_verified_and_landed/"
B95 = "frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/"
B97 = "frontier/B1897_b1881s_lock_tested_by_a_session_that_did_not_write_it/"
B81 = "frontier/B1881_the_whole_and_the_value_verified/"
B61 = "frontier/B1861_the_closure_programme/verification/"
T93 = B93 + "verification/test_b1893_the_second_enforcement_series_verified_and_landed.py"
Q = [
 ("01", B92 + "arc_verdict.json", "Every arc of the window was read in full, all but one by two sessions"),
 ("02", B92 + "FINDINGS.md", "| the governing pages | 2 | 3 | 0, and two things the first wrote as notes are findings of the second |"),
 ("03", B92 + "FINDINGS.md", "Of this window's 49, eighteen touched nothing but generated pages or a session's"),
 ("04", B92 + "FINDINGS.md", "nothing was landed between the last message to the readers and this entry"),
 ("05", B92 + "ANSWERS.md", "Each row was reproduced by main at its source before a word was changed."),
 ("05", B92 + "arc_verdict.json", "ALL 99 HELD ON MAIN'S OWN REPRODUCTION"),
 ("06", B92 + "FINDINGS.md", "- **One reading misses most of what is there.** The 99 are 88 distinct faults. Ten were found by two readers."),
 ("07", B92 + "ANSWERS.md", "lines, which the rule does not count: A9 with X13. So the 99 are 88 distinct faults, of which ten were found twice."),
 ("08", B92 + "FINDINGS.md", "`38d2a36dc` to `0dda7b472`: 49 commits. The readers read `323f92327` and, for what was added to their cards,"),
 ("09", B92 + "FINDINGS.md", "- **The full suite on a fresh clone,** at `323f92327`: 15 failed, 8,422 passed, 72 skipped."),
 ("10", B92 + "verification/quote_check.py", 'out.append((arc if arc != "M4" else "window", None, q))'),
 ("11", B93 + "FINDINGS.md", "Each patch's lock fails on the commit before it, in"),
 ("11", B93 + "verification/each_patchs_lock_on_the_commit_before_run.txt", "not run by main.  The patch adds one assertion that holds before it as well"),
 ("12", T93, "When the seat closes it, the first assertion of each pair fails"),
 ("13", B93 + "FINDINGS.md", "| U13.c | the identification ledger cut to its header, with the baseline left as it is | identification-register |"),
 ("14", T93, 'other = [x for x in r["gates newly failing"] if x != "attribution"]'),
 ("15", B93 + "FINDINGS.md", "pass are for the series after it."),
 ("15", B93 + "FINDINGS.md", "the fourth patch of its fourth series"),
 ("16", B93 + "verification/planted_suite_on_the_series_out.txt", "planted-violation suite at f6e89032a (f6e89032a)"),
 ("17", B93 + "FINDINGS.md", "`896cae025`: 2 failed, 8,454 passed, 73 skipped"),
 ("18", B93 + "FINDINGS.md", "| U12.b | every lock in `tests/` kept and marked to skip: the tests exist and never run. 1,407 files |"),
 ("19", B95 + "FINDINGS.md", "B1897, and the lock has fourteen tests now.]"),
 ("19", B97 + "FINDINGS.md", "The lock has four more tests. Main made the six again from the"),
 ("19", B81 + "verification/test_b1881_the_whole_and_the_value_verified.py", "The four tests below hold the six."),
 ("20", B95 + "FINDINGS.md", "**18 of 18 caught.** The plants are main's own, written after the tests. The reader's planted errors were not run"),
 ("21", B97 + "FINDINGS.md", "own, all caught. It said that the count that matters is the reader's."),
 ("22", B95 + "verification/test_b1895_the_mends_of_b1881_read.py", "on sequences the arc's script did not try: length 2 with runs to 12, length 4 with"),
 ("23", B95 + "FINDINGS.md", "every word of the second convention is the seat's word conjugated by the swap of the two coordinates, with the order of the letters kept"),
 ("24", B95 + "FINDINGS.md", "- **Whether the allowed set is closed under reversal for a mark that does not annihilate its own line** is not"),
 ("25", B97 + "FINDINGS.md", "locks do not, and the ones whose scripts take minutes cannot in the default lane."),
 ("25", "docs/POINT_REGISTER.md", "The reader is asked to run its 23 again"),
 ("26", "frontier/B874_measurement_ladder/arc_verdict.json", "The measurement ladder, exact over Q on the banked B854 build"),
 ("26", "frontier/B874_measurement_ladder/arc_verdict.json", "COMPUTED ON MAIN (B892): on the line through a wall point the nullity jumps at four points, all imaginary, to 14 and to 18"),
 ("27", "CHANGELOG.md", "a unit on one line gives index one, by main's own formula"),
 ("27", "docs/LAW_MAP.md", "a unit on one line gives one (B1796, and"),
 ("27", "frontier/B1894_review_79_the_second_round/verification/test_b1894_review_79_the_second_round.py", 'old = "the index is their sum above its value at no unit, so a unit on one line gives one"'),
 ("27", "tests/test_b1641_w46_on_main_and_the_two_objects.py", "index is their sum above its value at no unit."),
 ("28", B61 + "programme_source.py", "# is a living page and not the past: it gives what he answered in plain words.  The arcs, the register's rows and the dated logs"),
 ("28", B61 + "build_programme.py", '"", "> \\"%s\\"" % S.CONFIRMATION[1], "",'),
 ("28", B61 + "build_programme.py", 'fails.append("rulings are marked confirmed with no date or no words of the owner")'),
 ("28", B61 + "programme_source.py", "verbatim"),
 ("29", B61 + "test_b1861_the_closure_programme.py", 'assert "the option the owner chose, in main\'s label" in page and "NOT CONFIRMED: the owner, \\"" not in page'),
 ("30", B81 + "FINDINGS.md", "- **Main adds three things.** The rate is derived, not only observed (§ 4). The seat's convention and main's name"),
 ("31", B81 + "verification/test_b1881_the_whole_and_the_value_verified.py", "script is passed a constant, with two planted lines the scan must report;"),
 ("32", "docs/handoffs/CC_TO_CHAT1_2026-11-11_YOUR_TWO_RELAYS_VERIFIED.md", "Every exact fact of both relays is reproduced by main's own code: 65 checks, none failing."),
 ("33", "frontier/B1882_the_v1_card_run_on_main/verification/test_b1882_the_v1_card_run_on_main.py", 'assert "2026-11-12" in line[i:i + len(old) + 120], old'),
 ("34", "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md", "LR keeps exactly one point at N = 5, and two at other levels.]"),
 ("35", "frontier/B1884_what_level_a_ground_names_verified/arc_verdict.json", "The same counts hold in main's own convention."),
 ("36", "scripts/seats/listen.py", "if not new and not amended and read and not sums:"),
 ("36", "scripts/seats/listen.py", "amended = {n: t for n, t in ms.items() if n <= read and str(n) in sums and sums[str(n)] != _sum(t)}"),
 ("37", "scripts/seats/listen.py", 'read, sums = int(state.get("read", 0)), state.get("sums") or {}'),
 ("37", "scripts/seats/listen.py", 'return 2, "main has no page %s" % path, None'),
 ("38", "scripts/seats/listen.py", "It fetches every branch and exits when one that is not main has moved, appeared or gone, printing the names and the"),
 ("39", "scripts/atlas/query.py", "text = [f\"revive {probe_id} [{p['status']}]  -- \\\"{p['slug']}\\\"\","),
 ("40", "scripts/atlas/query.py", "text = [f\"{arc_id} [{head}]  -- \\\"{p['slug']}\\\"\","),
 ("41", "tests/test_b874_ladder.py", 'assert "SCOPED 2026-11-12" in after[:400] and "COMPUTED ON MAIN (B892)" in after'),
]


def text(path):
    r = subprocess.run(["git", "show", f"{R}:{path}"], capture_output=True, text=True)
    return " ".join(r.stdout.split()) if r.returncode == 0 else None


rows = [{"finding": "R80-SM-" + f, "file": p, "quote": q, "found": (text(p) or "").find(" ".join(q.split())) >= 0} for f, p, q in Q]
f, p, q = Q[0]
alt = q[:-1] + ("X" if q[-1] != "X" else "Y")
out = {"commit": R, "quotations": len(rows), "found": sum(r["found"] for r in rows), "rows": rows,
       "control": {"altered": alt, "reported_missing": " ".join(alt.split()) not in (text(p) or "")}}
json.dump(out, open(sys.argv[1], "w"), indent=1, ensure_ascii=False)
print(out["quotations"], "quotations,", out["found"], "found; control reported missing:", out["control"]["reported_missing"])
for r in rows:
    if not r["found"]:
        print("MISSING", r["finding"], r["file"], r["quote"][:80])
