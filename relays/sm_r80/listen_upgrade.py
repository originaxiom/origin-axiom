"""H2 made concrete: a seat's memory written by the listener of 84baf38fb (first round, in the instrument window) on a page
whose M2 holds a prose line that begins with a span of code (that version's fence rule then hides M1), read next by the
listener of c40446392.  argv: old listen.py, new listen.py, work dir."""
import importlib.util, json, pathlib, shutil, subprocess, sys
def load(p, name):
    spec = importlib.util.spec_from_file_location(name, p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
OLD, NEW = load(sys.argv[1], "old"), load(sys.argv[2], "new")
work = pathlib.Path(sys.argv[3]); shutil.rmtree(work, ignore_errors=True); work.mkdir(parents=True)
def git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True); assert r.returncode == 0, r.stderr
page = ("# a seat's page\n\n## Messages from main (newest first)\n\n### M2 — a day — a span\n\n```git status``` shows it.\n\nthen stop.\n\n"
        "### M1 — a day — plain\n\nTHE TEXT OF MESSAGE ONE\n\n## What main is waiting for from you\n\nnothing yet\n")
o = work / "origin"; (o / "docs/seats").mkdir(parents=True); (o / "docs/seats/x.md").write_text(page, encoding="utf-8")
git(o, "init", "-q", "-b", "main"); git(o, "add", "-A"); git(o, "commit", "-q", "-m", "p")
c = work / "clone"; subprocess.run(["git", "clone", "-q", "file://" + str(o), str(c)], check=True, capture_output=True)
st, txt, rem = OLD.look_seat("x", str(c), "origin", False); rem()
print("old listener: status", st, "| M1 shown:", "THE TEXT OF MESSAGE ONE" in txt, "| memory:", json.loads((pathlib.Path(OLD.memory(str(c))) / "x.json").read_text())["read"], sorted(json.loads((pathlib.Path(OLD.memory(str(c))) / "x.json").read_text())["sums"]))
print("new listener, same page: status", NEW.look_seat("x", str(c), "origin", False)[0])
(o / "docs/seats/x.md").write_text(page.replace("nothing yet", "your card"), encoding="utf-8"); git(o, "commit", "-q", "-a", "-m", "elsewhere")
st, txt, rem = NEW.look_seat("x", str(c), "origin", False)
print("new listener, page changed elsewhere: status", st, "| M1 shown:", "THE TEXT OF MESSAGE ONE" in txt, "| says:", txt.splitlines()[1][:80])
print("new listener's parse of the page:", sorted(NEW.messages(page)))
# variant: no look in between; main amends M1 in place after the old listener wrote the memory
shutil.rmtree(work / "v2", ignore_errors=True); (work / "v2").mkdir()
o = work / "v2" / "origin"; (o / "docs/seats").mkdir(parents=True); (o / "docs/seats/x.md").write_text(page, encoding="utf-8")
git(o, "init", "-q", "-b", "main"); git(o, "add", "-A"); git(o, "commit", "-q", "-m", "p")
c = work / "v2" / "clone"; subprocess.run(["git", "clone", "-q", "file://" + str(o), str(c)], check=True, capture_output=True)
st, txt, rem = OLD.look_seat("x", str(c), "origin", False); rem()
(o / "docs/seats/x.md").write_text(page.replace("THE TEXT OF MESSAGE ONE", "THE TEXT OF MESSAGE ONE, AMENDED IN PLACE"), encoding="utf-8"); git(o, "commit", "-q", "-a", "-m", "amend M1")
st, txt, rem = NEW.look_seat("x", str(c), "origin", False)
print("variant: new listener after main amends M1: status", st, "| amended M1 text shown:", "AMENDED IN PLACE" in txt, "| M1 named as changed:", "M1" in txt.splitlines()[1] if len(txt.splitlines()) > 1 else None, "| says:", txt.splitlines()[1][:80])
rem(); print("variant: next look status", NEW.look_seat("x", str(c), "origin", False)[0], "(the amended M1 is now stored as read)")
