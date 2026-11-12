"""the lock of B1898 and the gate on a review's action items, tested against planted changes.

    python3 the_lock_of_b1898_against_planted_changes.py <a checkout that holds the patch, with nothing uncommitted>

Each plant changes one thing in the checkout, runs the arc's lock (or the gate), records whether it still passes, and
puts the checkout back with git.  The first entry plants nothing and must pass.  A plant that "passes" is a change the
lock does not hold."""
import json, pathlib, re, subprocess, sys
ROOT = pathlib.Path(sys.argv[1]).resolve()
ARC = ROOT / "frontier" / "B1898_review_80_one_hundred_findings_and_what_main_checked"
def git(*a): return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True)
assert git("status", "--porcelain").stdout.strip() == "", "the checkout holds something uncommitted"
def lock():
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-p", "no:randomly", "--tb=no", str(ARC / "verification")], cwd=str(ROOT), capture_output=True, text=True)
    return r.returncode == 0, (r.stdout.strip().splitlines() or ["?"])[-1]
def gate(name):
    code = ("import sys, json, importlib.util\nsys.dont_write_bytecode = True\ns = importlib.util.spec_from_file_location('g', 'scripts/gates/gates.py')\n"
            "g = importlib.util.module_from_spec(s); s.loader.exec_module(g)\nr = g.GATES[%r]()\nprint(json.dumps([bool(r[0]), str(r[1])[:160]]))\n" % name)
    r = subprocess.run([sys.executable, "-B", "-c", code], cwd=str(ROOT), capture_output=True, text=True)
    ok, detail = json.loads(r.stdout.strip().splitlines()[-1])
    return ok, detail
def edit(rel, fn):
    p = ROOT / rel; t = p.read_text(encoding="utf-8"); t2 = fn(t)
    assert t2 != t, "the plant changed nothing in " + rel
    p.write_text(t2, encoding="utf-8")
A = "frontier/B1898_review_80_one_hundred_findings_and_what_main_checked/"
def drop_row(pattern):
    return lambda t: "\n".join(l for l in t.split("\n") if not re.match(pattern, l))
PLANTS = [
 ("the lock", "nothing planted", None),
 ("the lock", "a row of the second table deleted (the SM seat's 22)", lambda: edit(A + "STATUS_OF_THE_57.md", drop_row(r"^\| 22 \|"))),
 ("the lock", "a row of the first table deleted (agy-002's 7)", lambda: edit(A + "ANSWERS_the_first_43.md", drop_row(r"^\| A7 \|"))),
 ("the lock", "a finding that only its reader looked at written as checked (the SM seat's 22: 'not checked' to 'the line read')", lambda: edit(A + "STATUS_OF_THE_57.md", lambda t: t.replace("| 22 | B1895's lock | 295 of its 409 sequences were tried by the arc's script; 114 are new | not checked |", "| 22 | B1895's lock | 295 of its 409 sequences were tried by the arc's script; 114 are new | the line read |"))),
 ("the lock", "a finding that waits written as mended (agy-exp's F1: 'held. **To build**' to 'held; mended')", lambda: edit(A + "STATUS_OF_THE_57.md", lambda t: t.replace("| main's plant: 15 of 15 pass (`plants_b1881_third`) | held. **To build** |", "| main's plant: 15 of 15 pass (`plants_b1881_third`) | held; mended |"))),
 ("the lock", "the entry's count of findings changed by one (100 to 101, wherever the entry says it)", lambda: edit("docs/progress/REVIEWS.md", lambda t: t[:t.index("\n# Review 80 ")] + t[t.index("\n# Review 80 "):].replace("100 findings", "101 findings"))),
 ("the lock", "the page's count of what main checked in full changed by one (80 to 81)", lambda: edit(A + "FINDINGS.md", lambda t: t.replace("**80 of them main checked in full", "**81 of them main checked in full"))),
 ("the lock", "the verdict line's count of what waits changed (41 to 14)", lambda: edit(A + "arc_verdict.json", lambda t: t.replace("and 41 WAIT TO BE BUILT", "and 14 WAIT TO BE BUILT"))),
 ("the lock", "the verdict changed from PROVED to NEGATIVE", lambda: edit(A + "arc_verdict.json", lambda t: t.replace('"verdict": "PROVED"', '"verdict": "NEGATIVE"'))),
 ("the lock", "the kept recount changed and the tables left as they are (17 not checked made 16)", lambda: edit(A + "verification/recount.json", lambda t: t.replace('"22",\n   "25",', '"25",', 1))),
 ("the lock", "an output main kept changed (a quotation of the SM seat's marked as not placed)", lambda: edit(A + "verification/checks/quote_check_sm.json", lambda t: t.replace('"placed": 50', '"placed": 49', 1))),
 ("the lock", "one of main's checks changed (the commit the web seat's quotations are looked for at)", lambda: edit(A + "verification/checks/quote_check_chat1.py", lambda t: t.replace('AT = "c40446392"', 'AT = "10fbbc1c2"'))),
 ("the lock", "the entry's anchor changed to main's head at the handing over", lambda: edit("docs/progress/REVIEWS.md", lambda t: t.replace("**anchor-commit: `c40446392`**", "**anchor-commit: `10fbbc1c2`**"))),
 ("the lock", "the planted suite's output changed: a case that is not caught written as caught", lambda: edit(A + "verification/planted_suite_on_main_c40446392_out.txt", lambda t: t.replace("PV27  L10  NOT CAUGHT", "PV27  L10  CAUGHT    ", 1))),
 ("the lock", "the page's sentence on the plant of main's that passes taken out", lambda: edit(A + "FINDINGS.md", lambda t: t.replace("One plant of main's own passes", "No plant of main's own passes"))),
 ("review-actions", "nothing planted", None),
 ("review-actions", "one of Review 79's items left open (R79-4)", lambda: edit("docs/progress/REVIEWS.md", lambda t: t.replace("- [>] R79-4:", "- [ ] R79-4:", 1))),
 ("review-actions", "a carried item of Review 79 that stands in no later block (R80-9's line taken out)", lambda: edit("docs/progress/REVIEWS.md", lambda t: "\n".join(l for l in t.split("\n") if not l.startswith("- [ ] R80-9:")).replace("R79-9 to R79-18", "R79-10 to R79-18").replace("R79-5 to R79-9", "R79-5 to R79-8"))),
 ("review-core", "nothing planted", None),
 ("review-core", "the line of the sample's seed taken out of the entry", lambda: edit("docs/progress/REVIEWS.md", lambda t: t[:t.index("\n# Review 80 ")] + t[t.index("\n# Review 80 "):].replace("sample seed:", "the sample's seed:"))),
]
out = []
for what, name, plant in PLANTS:
    try:
        if plant: plant()
        ok, tail = lock() if what == "the lock" else gate(what)
        answer = "passes" if ok else "FAILS"
    except AssertionError as e:
        answer, tail = "PLANT NOT MADE", str(e)[:100]
    finally:
        git("checkout", "--", ".")
    out.append({"what is run": what, "the plant": name, "it": answer, "its last line": tail})
    print("%-15s %-112s %-8s %s" % (what, name[:112], answer, tail[:70]), flush=True)
plants = [o for o in out if o["the plant"] != "nothing planted"]
print("\nnothing planted: %s; plants made: %d; caught: %d; passed: %d; not made: %d" % (
    all(o["it"] == "passes" for o in out if o["the plant"] == "nothing planted"), len(plants) - sum(1 for o in plants if o["it"] == "PLANT NOT MADE"),
    sum(1 for o in plants if o["it"] == "FAILS"), sum(1 for o in plants if o["it"] == "passes"), sum(1 for o in plants if o["it"] == "PLANT NOT MADE")))
