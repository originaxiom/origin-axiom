#!/usr/bin/env python3
"""SM-R79b: every quotation of relays/REVIEW_79B_SM.md, checked by machine in its file at its commit (whitespace joined, as
the files wrap).  The control: the first quotation altered by one character must be reported missing.
Usage (from a clone that has the commits): quote_check_b.py OUT.json"""
import json, subprocess, sys
M = "896cae025"
OWN = "6a9e86148"          # this seat's branch, for its own earlier file
Q = [
 ("R79b-SM-01", M, "GENESIS.md", "the option he chose stood here in quotation marks; it is given in plain words under his ruling of the same day that his messages are private (P-796)"),
 ("R79b-SM-01", M, "frontier/B1891_the_foundation_at_version_1_66/FINDINGS.md", "How many others stand in the file was not counted."),
 ("R79b-SM-02", M, "frontier/B1889_the_seats_digested/FINDINGS.md", "Fourteen of its rows carry a refutation, a decline or a correction by main."),
 ("R79b-SM-02", M, "frontier/B1889_the_seats_digested/FINDINGS.md", "| recomputed by main | parts of ten rows, on the mathematics that uses no value |"),
 ("R79b-SM-03", M, "frontier/B1892_review_79_read_by_those_who_did_not_build_it/ANSWERS.md", "\"LR fixes a point only at N = 5\" stood unscoped in five places"),
 ("R79b-SM-03", M, "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md", "that LR fixes a point only at N = 5, stood unscoped in five places"),
 ("R79b-SM-03", M, "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py", "(r\"(?:fixes a point of|fixed points on) P[¹^1]{1,2}\\((?:ℤ|Z)/N\\) only at N = 5\", r\"exactly one point at N = 5\", \"B1884\"),"),
 ("R79b-SM-04", M, "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py", "(r\"no real nullity-14 point exists there\", r\"the audit's finding E5|refinement never ran|walls_on_the_line\", \"E5\"),"),
 ("R79b-SM-04", M, "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py", "an unrelated \"E = +I\" within 900 characters counted as the correction -> the correction must name the split, not the sign alone;"),
 ("R79b-SM-05", M, "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py", "(r\"21 distinct eigenvalues\", r\"\\b20 distinct|at most 20|\\(20; B1862\\)|where 20 is the most possible|corrected 2026-11-10 \\(B1862\", \"E13\"),"),
 ("R79b-SM-06", M, "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py", "ROOT_PAGES = (\"README.md\", \"ROADMAP.md\", \"GENESIS.md\", \"CLAIMS.md\", \"GOVERNANCE.md\", \"TERMINOLOGY.md\", \"WORKING_RULES.md\", \"CHANGELOG.md\")"),
 ("R79b-SM-06", M, "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py", "if not rel.endswith((\".md\", \".json\", \".tex\", \".txt\")) or any(x in rel for x in NOT_READ):"),
 ("R79b-SM-06", M, "tests/test_b892_walls_on_the_line.py", "SKELETON.md"),
 ("R79b-SM-07", M, "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py", "assert \"Z6\" in res[\"global_form\"]"),
 ("R79b-SM-07", M, "frontier/B862_global_form/FINDINGS.md", "**exactly ℤ₆**"),
 ("R79b-SM-08", M, "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py", "_SPLIT = r\"(?:only|E\\s*[=≡]\\s*[-−]\\s*[I1]\\b|parity)\""),
 ("R79b-SM-09", OWN, "relays/REVIEW_79_SM.md", "| E13 | B1862 test_e13 | 9 | 4 | see below |"),
 ("R79b-SM-09", OWN, "relays/REVIEW_79_SM.md", "- **Missed (5):** - a wrong multiplicity list in the findings"),
 ("R79b-SM-10", M, "frontier/B1885_the_golden_state_on_the_whole_verified/arc_verdict.json", "data-free; 30 digits; 31 checks"),
 ("R79b-SM-11", M, "frontier/B1890_the_first_enforcement_series_verified_and_landed/verification/other_checks_run.txt", "14 passed in 118.54s"),
]


def text(rev, path):
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True)
    return " ".join(r.stdout.split()) if r.returncode == 0 else None


rows = []
for fid, rev, path, q in Q:
    t = text(rev, path)
    rows.append({"finding": fid, "commit": rev, "file": path, "quote": q, "found": t is not None and " ".join(q.split()) in t})
fid, rev, path, q = Q[0]
altered = q[:-1] + ("X" if q[-1] != "X" else "Y")
control = {"altered_quote": altered, "reported_missing": " ".join(altered.split()) not in (text(rev, path) or "")}
out = {"quotations": len(rows), "found": sum(r["found"] for r in rows), "rows": rows, "control": control}
json.dump(out, open(sys.argv[1], "w"), indent=1, ensure_ascii=False)
print(out["quotations"], "quotations,", out["found"], "found; control reported missing:", control["reported_missing"])
for r in rows:
    if not r["found"]:
        print("MISSING", r["finding"], r["file"], r["quote"][:80])
