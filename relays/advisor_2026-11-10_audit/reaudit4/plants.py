#!/usr/bin/env python3
"""Re-audit 4: planted violations against main's two gates of B1878 (a sentence of arrival; commit messages), the gate
that compares the closure map and programme with their builders (Review 78), and the lock that checks three
corrections reached every place (Review 78).

Each case is planted in a scratch clone of main, committed there, the gate is run from that clone on the clean tree,
and the clone is reset. The seat's expectation of each case is written here before the run.
    python3 -B plants.py CLONE_DIR"""
import sys, os, re, json, glob, subprocess, importlib.util

C = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("pv", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "planted_violations.py"))
pv = importlib.util.module_from_spec(spec); spec.loader.exec_module(pv)
sh, read, write, WHO, VENDOR = pv.sh, pv.read, pv.write, pv.WHO, pv._V
OTHER = ["-c", "user.name=someone-else", "-c", "user.email=someone@example.invalid"]
base = sh(["git", "rev-parse", "HEAD"], C).stdout.strip()
print("re-audit 4: plants at", base[:9], "\n")

def reset():
    sh(["git", "checkout", "-q", "--detach", base], C); sh(["git", "reset", "-q", "--hard", base], C); sh(["git", "clean", "-fdq"], C)
    for b in sh(["git", "branch", "--format=%(refname:short)"], C).stdout.split():
        if b.startswith("side"): sh(["git", "branch", "-q", "-D", b], C)
def commit(msg="a planted violation", who=WHO):
    sh(["git", "add", "-A"], C); sh(["git"] + who + ["commit", "-q", "-m", msg], C)
    return sh(["git", "rev-parse", "HEAD"], C).stdout.strip()
def gate(name):
    code = ("import sys, json; sys.path.insert(0, 'scripts/gates'); import gates\n"
            "try:\n    r = gates.GATES[%r](); out = [bool(r[0]), str(r[1])]\n"
            "except Exception as exc:\n    out = [False, 'EXCEPTION ' + repr(exc)]\n"
            "print('@@' + json.dumps(out))\n" % name)
    r = sh([sys.executable, "-B", "-c", code], C)
    m = re.search(r"@@(\[.*\])", r.stdout)
    return json.loads(m.group(1)) if m else [None, "no output: " + (r.stderr or r.stdout)[-300:]]
def show(tag, what, gates_, expect):
    res = {g: gate(g) for g in gates_}
    caught = [g for g, r in res.items() if r[0] is False]
    print("%-4s %-11s %s" % (tag, "CAUGHT" if caught else "NOT CAUGHT", what))
    for g, r in res.items(): print("       %-18s %-5s %s" % (g, "FAIL" if r[0] is False else "PASS", r[1][:210]))
    print("       expected by the seat before running: %s" % expect)

# ---------------------------------------------------------------- a clean tree first
reset()
for g in ("arrival-phrases", "attribution", "closure-generated"):
    r = gate(g); print("clean tree: %-18s %-5s %s" % (g, "FAIL" if r[0] is False else "PASS", r[1][:170]))
print()

# ---------------------------------------------------------------- a sentence of arrival
def arrive(tag, path, sentence, expect):
    reset(); old = read(C, path) if os.path.exists(os.path.join(C, path)) else ""
    write(C, path, old + "\n" + sentence + "\n"); commit()
    show(tag, "%s <- %r" % (path, sentence), ["arrival-phrases"], expect)
arrive("r1", "README.md", "The Standard Model is derived.", "caught (the audit's own planted sentence)")
arrive("r2", "README.md", "We claim that the Standard Model is derived.", "NOT caught: the list of words that excuse a sentence holds 'aim', and 'claim' contains it")
arrive("r3", "README.md", "Nothing stands in the way now. The Standard Model is derived.", "NOT caught: 'Nothing' stands within the window before the phrase")
arrive("r4", "README.md", "All nineteen parameters now follow from the object with no free input.", "NOT caught: other words (main discloses this limit)")
tex = sorted(f for f in sh(["git", "ls-files", "papers"], C).stdout.split() if f.endswith(".tex"))
arrive("r5", tex[0] if tex else "papers/planted.tex", "The Standard Model is derived.", "NOT caught: the gate reads the root pages and docs/*.md only")
arrive("r6", "docs/handoffs/PLANTED_NOTE.md", "The Standard Model is derived.", "NOT caught: a folder below docs/ is not read")

# ---------------------------------------------------------------- commit messages
TRAILER = "\n\nCo-Authored-By: %s <noreply@example.invalid>" % VENDOR
reset(); write(C, "docs/zz_planted.txt", "x\n"); commit("a change" + TRAILER)
show("c1", "a commit on the line whose message carries a co-author trailer naming a vendor", ["attribution"], "caught")
reset(); write(C, "docs/zz_planted.txt", "x\n"); commit("a change", who=OTHER)
show("c2", "a commit on the line by another author", ["attribution"], "caught")
reset(); sh(["git", "checkout", "-q", "-b", "side1"], C); write(C, "docs/zz_side.txt", "x\n"); commit("work on a side branch" + TRAILER)
sh(["git", "checkout", "-q", "--detach", base], C); write(C, "docs/zz_main.txt", "y\n"); commit("the line moves on")
sh(["git"] + WHO + ["merge", "-q", "--no-ff", "-m", "merge the side branch", "side1"], C)
show("c3", "the same trailer on a commit of a side branch, merged into the line with a clean message", ["attribution"],
     "NOT caught: the gate reads the first-parent line, and the trailer is on the second parent's side")
reset(); sh(["git", "checkout", "-q", "-b", "side2"], C); write(C, "docs/zz_side.txt", "x\n"); commit("work on a side branch", who=OTHER)
sh(["git", "checkout", "-q", "--detach", base], C); write(C, "docs/zz_main.txt", "y\n"); commit("the line moves on")
sh(["git"] + WHO + ["merge", "-q", "--no-ff", "-m", "merge the side branch", "side2"], C)
show("c4", "a commit by another author on a side branch, merged into the line", ["attribution"], "NOT caught, for the same reason")

# ---------------------------------------------------------------- generated files against their builders
reset(); p = "frontier/B1861_the_closure_programme/PROGRAMME.md"; s = read(C, p)
m = re.search(r"\*\*(\d+) packages\*\*", s); assert m
write(C, p, s.replace(m.group(0), "**%d packages**" % (int(m.group(1)) - 1), 1)); commit()
show("g1", "one count on the generated programme page changed by hand", ["closure-generated"], "caught")
reset(); p = "frontier/B1858_the_closure_map/NODES.json"; N = json.loads(read(C, p))
i = next(i for i, n in enumerate(N) if n["id"] == "G:SE2"); N[i]["grade"] = "DERIVED"
write(C, p, json.dumps(N, indent=1, ensure_ascii=False) + "\n"); commit()
show("g2", "one node's grade changed by hand in the generated map (the orientation choice typed DERIVED)", ["closure-generated"], "caught")

# ---------------------------------------------------------------- the lock that a correction reached every place
T = glob.glob(os.path.join(C, "frontier/B1862_*/verification/test_*.py"))[0]
def lock(tag, text, expect):
    reset(); write(C, "docs/ZZ_PLANTED_PAGE.md", "# a planted page\n\n" + text + "\n"); commit()
    r = sh([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", T + "::test_no_place_still_carries_an_old_form_unmarked"], C)
    tail = (r.stdout.strip().splitlines() or [""])[-1]
    print("%-4s %-11s a new page states: %r" % (tag, "CAUGHT" if r.returncode != 0 else "NOT CAUGHT", text[:110]))
    print("       the lock: %s" % tail[:150]); print("       expected by the seat before running: %s" % expect)
print()
lock("p1", "The premise at level 5 is a charge (invisibility to every state), and nothing more need be said.", "caught: the old form in the lock's own words, with no correction beside it")
lock("p2", "The premise at level 5 is a charge, which no state of any kind can detect.", "NOT caught: the same old claim in other words")
reset(); print("\nclone reset to", sh(["git", "rev-parse", "--short", "HEAD"], C).stdout.strip(), "| clean:", sh(["git", "status", "--short"], C).stdout.strip() == "")
