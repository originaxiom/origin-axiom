#!/usr/bin/env python3
"""The four findings of part 4 that main's table gives as not checked, each made again on the tree before the part.

    python3 the_four_findings_main_had_not_checked_made_again.py <a checkout of the commit before part 4>

It runs the tree's own listener in a small repository made in a temporary folder, and the tree's own query of the atlas.
It changes nothing in the checkout.  The findings are the SM seat's 37, 38, 39 and 40."""
import importlib.util, json, pathlib, subprocess, sys, tempfile
root = pathlib.Path(sys.argv[1]).resolve()
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
T = load("the_listeners_tests", root / "tests" / "test_seat_listener.py")       # for its helpers: a small origin, a clone, a run
L = load("the_listener", root / "scripts" / "seats" / "listen.py")

print("1. The SM seat's 37: two paths on which the listener could not look")
with tempfile.TemporaryDirectory() as d:
    origin, clone = T._origin_and_clone(pathlib.Path(d))
    assert T._listen(clone, "--seat", "x").returncode == 0
    mem = pathlib.Path(L.memory(str(clone))) / "x.json"
    (origin / "docs" / "seats" / "x.md").write_text(T._page(1, 2), encoding="utf-8"); T._git(origin, "commit", "-q", "-a", "-m", "a second message")
    for bad in ({"blob": "x", "read": "two"}, {"blob": "x", "read": None}):
        mem.write_text(json.dumps(bad), encoding="utf-8")
        r = T._listen(clone, "--seat", "x")
        print("   a memory with %r as what was read: status %d; ends with an error of the language: %s; says it could not look: %s"
              % (bad["read"], r.returncode, "Traceback" in r.stderr, "could not look" in r.stderr))
    mem.unlink()
    real = L.git
    L.git = lambda *a, **k: (124, "", "git rev-parse did not answer within 180 seconds") if a and a[0] == "rev-parse" and ":" in a[-1] else real(*a, **k)
    status, text, _ = L.look_seat("x", str(clone), "origin", False)
    L.git = real
    print("   a git that does not answer while the page is looked for: status %d, and the listener says: %r" % (status, text))

print("2. The SM seat's 38: the docstring and main's first look")
with tempfile.TemporaryDirectory() as d:
    origin, clone = T._origin_and_clone(pathlib.Path(d)); T._git(origin, "branch", "a-seat")
    r = T._listen(clone, "--main")
    print("   main's first look: status %d; prints FIRST LOOK: %s" % (r.returncode, r.stdout.startswith("FIRST LOOK")))
doc = " ".join(L.__doc__.split())
print("   the docstring names the first look: %s; its line on --once: %r" % ("FIRST LOOK" in doc.upper().replace("FIRST LOOK", "FIRST LOOK") and "first look" in doc.lower(), doc[doc.index("--once"):doc.index("--interval")].strip()))

print("3. The SM seat's 39: the atlas's tag printed as a status")
sys.path.insert(0, str(root / "scripts" / "atlas"))
import query
G = query.load()
v = json.loads(next((root / "frontier").glob("B57_*/arc_verdict.json")).read_text(encoding="utf-8"))["verdict"]
print("   B57's verdict: %s; revive B57 prints: %r" % (v, query.revive("B57", G)["text"].split("\n")[0]))
print("   the meeting points print: %r" % query.meeting_points(G)["text"].split("\n")[1][:34])
print("   the context card's tally: %r" % query.context_card(G)["text"].split("\n")[1][:70])
print("   the obstacle oracle: %r" % query.resolutions_for("particle_dict", G)["text"].split("\n")[0])
print("   the gap finder: %r" % query.gaps(G)["text"].split("\n")[0])

print("4. The SM seat's 40: the card of B58")
for f in sorted((root / "frontier").glob("B58_*/arc_verdict.json")):
    print("   the folder %-22s verdict %s" % (f.parent.name, json.loads(f.read_text(encoding="utf-8"))["verdict"]))
card = query.arc_card("B58", G)["text"].split("\n")
print("   the card's head: %r" % card[0])
print("   the folders the card names: %s" % [l.split("folder: ")[1] for l in card if "folder: " in l])
print("   the card holds the word RETRACTED: %s" % any("RETRACTED" in l.split("claim:")[0] for l in card))
