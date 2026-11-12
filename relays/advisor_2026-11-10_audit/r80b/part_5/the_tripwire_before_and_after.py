#!/usr/bin/env python3
"""B1862's tripwire on the planted pages of its new test, as the tripwire stood on the commit before and as it stands.

    python3 the_tripwire_before_and_after.py <a checkout of the patch> <the commit before the patch>

The pages are made in a temporary repository.  The checkout is not changed."""
import importlib.util, pathlib, subprocess, sys, tempfile
root = pathlib.Path(sys.argv[1]).resolve(); before = sys.argv[2]
rel = "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py"
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
PAGES = [
 ("1. no old form for E11", "docs/sine.md", "As is known, sin(π/7) has no radical closed form.", "an old form, no correction"),
 ("   its twin", "docs/sine_good.md", "sin(π/7) has no radical closed form [corrected: none in real radicals; it is expressible by complex radicals].", "corrected"),
 ("2. a script outside an arc", "scripts/tool.py", '"""The charge premise: a departure is invisible to every state."""', "an old form, no correction"),
 ("   a test", "tests/test_x.py", "# B567 found 21 distinct eigenvalues at level 165", "an old form, no correction"),
 ("   a page of another tree", "knowledge/K1.md", "LR fixes a point only at N = 5.", "an old form, no correction"),
 ("3. a mark that was one word in any case", "docs/principal.md", "There is no non-abelian continuous symmetry commuting with the holonomy, for the principal embedding or any other.", "an old form, no correction"),
 ("   its twin", "docs/principal_good.md", "There is no non-abelian continuous symmetry commuting with the holonomy. [Scoped: this holds for the PRINCIPAL embedding of 2T, the only one computed.]", "corrected"),
 ("4. a cue in a later quoted paragraph", "docs/quoted.md", "> The charge is invisibility to every state.\n>\n> In another matter one has E = +I on the even block and E = −I on the odd, by parity.", "an old form, no correction"),
 ("   its twin", "docs/quoted_good.md", "> The charge is invisibility to every state\n> [corrected: that holds for E = +I only; E = −I is invisible only under parity].", "corrected"),
 ("5. a word of the form in bold", "docs/bold.md", "B567 finds **21** distinct eigenvalues at level 165.", "an old form, no correction"),
 ("   in italics", "docs/italic.md", "At five a departure is *invisible* to every state.", "an old form, no correction"),
 ("   as code", "docs/code.md", "On the real line no real `nullity-14` point exists there.", "an old form, no correction"),
 ("   its twin", "docs/bold_good.md", "This read **21** distinct eigenvalues; there are 20 distinct.", "corrected"),
]
with tempfile.TemporaryDirectory() as d:
    d = pathlib.Path(d)
    old_file = d / "the_lock_before.py"
    old_file.write_text(subprocess.run(["git", "-C", str(root), "show", before + ":" + rel], capture_output=True, text=True, check=True).stdout.replace("pathlib.Path(__file__).resolve().parents[3]", "pathlib.Path(%r)" % str(root)), encoding="utf-8")
    old, new = load("the_lock_before", old_file), load("the_lock_now", root / rel)
    repo = d / "repo"; repo.mkdir()
    git = lambda *a: subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True, check=True)
    git("init", "-q")
    for _, path, text, _ in PAGES:
        (repo / path).parent.mkdir(parents=True, exist_ok=True); (repo / path).write_text(text + "\n", encoding="utf-8")
    git("add", "-A")
    def read(lock):
        got = {}
        for r, _, ok in lock._hits(repo):
            got[r] = got.get(r, True) and ok
        return got
    b, a = read(old), read(new)
    say = lambda got, p: "not read" if p not in got else ("corrected" if got[p] else "an old form, no correction")
    print("%-42s %-24s %-28s %-28s %s" % ("", "the page", "before", "now", "what it is"))
    for what, path, _, is_ in PAGES:
        print("%-42s %-24s %-28s %-28s %s" % (what, path, say(b, path), say(a, path), is_))
    plants = [p for _, p, _, is_ in PAGES if is_ == "an old form, no correction"]; twins = [p for _, p, _, is_ in PAGES if is_ == "corrected"]
    print("\nof the %d planted pages, reported as an old form with no correction: %d before, %d now" % (len(plants), sum(1 for p in plants if say(b, p) == "an old form, no correction"), sum(1 for p in plants if say(a, p) == "an old form, no correction")))
    print("of the %d twins, reported so: %d before, %d now" % (len(twins), sum(1 for p in twins if say(b, p) == "an old form, no correction"), sum(1 for p in twins if say(a, p) == "an old form, no correction")))
