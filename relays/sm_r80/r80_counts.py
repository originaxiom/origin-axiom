#!/usr/bin/env python3
"""SM-R80: counts behind several findings of relays/REVIEW_80_SM.md, by this seat's own code, from git objects only.
Run from inside a clone that has the commits named.  Usage: r80_counts.py OUT.json"""
import json, re, subprocess, sys

git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
out = {}
# 1. Review 79's window: arcs added, and arcs changed and not added; which seat page names each changed arc at 0dda7b472
A, Z = "38d2a36dc", "0dda7b472"
names = [l for l in git("diff", "--name-only", A, Z, "--", "frontier").split() if l.endswith(("/arc_verdict.json", "/FINDINGS.md"))]
added = {l.split("/")[1] for l in git("diff", "--name-only", "--diff-filter=A", A, Z, "--", "frontier").split() if l.endswith("arc_verdict.json")}
arcs = {}
for l in names:
    arcs.setdefault(l.split("/")[1], set()).add(l.split("/")[-1])
changed = sorted(a for a in arcs if a not in added)
pages = {s: git("show", f"{Z}:docs/seats/{s}.md") for s in ("chat1", "agy-exp", "agy-002", "sm")}
mention = {}
for a in changed:
    b = re.match(r"(B\d+)_", a).group(1)
    mention[b] = {s: [ln.strip()[:160] for ln in t.split("\n") if re.search(r"\b%s\b" % b, ln)] for s, t in pages.items()}
out["review79_window"] = {"added": len(added), "changed_not_added": len(changed),
                          "verdict_changed": sum("arc_verdict.json" in arcs[a] for a in changed),
                          "findings_only": sum("arc_verdict.json" not in arcs[a] for a in changed),
                          "named_on_no_seat_page": sorted(b for b, m in mention.items() if not any(m.values())),
                          "named_but_lines_shown": {b: m for b, m in mention.items() if any(m.values()) and b in ("B1028", "B1222", "B1643")}}
# 2. B1892 § 5's table: the two readers' columns, and the total with B1889's three
f92 = git("show", "c40446392:frontier/B1892_review_79_read_by_those_who_did_not_build_it/FINDINGS.md")
rows = [l for l in f92.split("\n") if re.match(r"^\| .* \| \d+ \| \d+ \| ", l)]
c1 = sum(int(l.split("|")[2]) for l in rows); c2 = sum(int(l.split("|")[3]) for l in rows)
out["b1892_table5"] = {"rows": len(rows), "first_reader_column": c1, "second_reader_column": c2, "with_B1889s_three": c1 + c2 + 3}
# 3. commits of the window that touch only generated pages (views, the atlas data, README's state block) or a seat's page
def only_generated(c):
    fs = git("show", "--name-only", "--format=", c).split()
    return bool(fs) and all(f.startswith("docs/views/") or f in ("scripts/atlas/atlas_data.json", "README.md") or f.startswith("docs/seats/") for f in fs)
out["generated_only_commits"] = {z: {"commits": len(git("rev-list", f"{A}..{z}").split()),
                                     "only_generated": sum(only_generated(c) for c in git("rev-list", f"{A}..{z}").split())}
                                 for z in ("57f604898", "323f92327", Z)}
# 4. the order of the last message to the readers, a landing, and the entry
t = lambda c: git("log", "-1", "--format=%ci", c).strip()
anc = lambda a, b: subprocess.run(["git", "merge-base", "--is-ancestor", a, b]).returncode == 0
out["b1892_order"] = {"last_message_f8b5e6769": t("f8b5e6769"), "landing_c66c8ccae": t("c66c8ccae"), "entry_84baf38fb": t("84baf38fb"),
                      "in_that_order": anc("f8b5e6769", "c66c8ccae") and anc("c66c8ccae", "84baf38fb"),
                      "c66c8ccae_files": git("show", "--name-only", "--format=", "c66c8ccae").split()}
# 5. B1893: the planted suite's commit; the locks in tests/ at the series' anchor
out["b1893"] = {"f6e89032a_is_an_object_here": subprocess.run(["git", "cat-file", "-t", "f6e89032a"], capture_output=True).returncode == 0,
                "tests_test_py_recursive_at_e6298271a": sum(1 for p in git("ls-tree", "-r", "--name-only", "e6298271a", "tests/").split()
                                                           if re.search(r"/test_[^/]*\.py$", p)),
                "tests_test_b_py_top_level_at_e6298271a": sum(1 for p in git("ls-tree", "--name-only", "e6298271a", "tests/").split()
                                                              if re.match(r"tests/test_b[^/]*\.py$", p))}
# 6. B1881's lock: tests per commit
L = "frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py"
out["b1881_lock_tests"] = {c: len(re.findall(r"(?m)^def test_", git("show", f"{c}:{L}"))) for c in ("87bfa1f05", "a36a28ac6", "738be0e5f", "644d5b40f", "c40446392")}
json.dump(out, open(sys.argv[1], "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "review79_window"}, indent=1)); print(json.dumps(out["review79_window"], indent=1)[:1500])
