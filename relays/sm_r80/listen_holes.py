"""Run scripts/seats/listen.py of c40446392 (scratch copy, argv[1]) on crafted inputs, in throwaway repositories under argv[2].
H1: a memory written by the older listener (no 'sums'), main amends M1 in place AND adds M2 -> is the amendment said?
H2: a message numbered at or below 'read' that is not in 'sums' (e.g. one the older fence rule had swallowed) -> is it shown?
H3: a memory that is valid JSON and a table but holds a wrong type -> does the listener say it could not look, or crash?
H4: git rev-parse of the page times out -> what does the listener say?"""
import importlib.util, json, pathlib, shutil, subprocess, sys
LISTEN = pathlib.Path(sys.argv[1]) / "scripts/seats/listen.py"
work = pathlib.Path(sys.argv[2]); shutil.rmtree(work, ignore_errors=True); work.mkdir(parents=True)
spec = importlib.util.spec_from_file_location("L", LISTEN); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)

def git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr

def page(msgs):   # msgs: {n: text}
    b = "# a seat's page\n\n## Messages from main (newest first)\n\n"
    for n in sorted(msgs, reverse=True):
        b += "### M%d — a day — a subject\n\n%s\n\n" % (n, msgs[n])
    return b + "## What main is waiting for from you\n\nnothing yet\n"

def setup(name, msgs):
    o = work / name / "origin"; (o / "docs/seats").mkdir(parents=True)
    (o / "docs/seats/x.md").write_text(page(msgs), encoding="utf-8")
    git(o, "init", "-q", "-b", "main"); git(o, "add", "-A"); git(o, "commit", "-q", "-m", "p")
    c = work / name / "clone"; subprocess.run(["git", "clone", "-q", "file://" + str(o), str(c)], check=True, capture_output=True)
    return o, c

def commit(o, msgs):
    (o / "docs/seats/x.md").write_text(page(msgs), encoding="utf-8"); git(o, "commit", "-q", "-a", "-m", "q")

# H1
o, c = setup("h1", {1: "text one"})
st, txt, rem = L.look_seat("x", str(c), "origin", False); rem()
mem = pathlib.Path(L.memory(str(c))) / "x.json"; s = json.loads(mem.read_text()); mem.write_text(json.dumps({"blob": s["blob"], "read": s["read"]}))
commit(o, {1: "text one, AMENDED IN PLACE", 2: "text two"})
st, txt, rem = L.look_seat("x", str(c), "origin", False); rem()
print("H1 status", st, "| shows M2:", "text two" in txt, "| says M1 changed or that it cannot tell:", ("CHANGED since" in txt) or ("holds no record" in txt), "| shows the amended text:", "AMENDED IN PLACE" in txt)
st2, txt2, _ = L.look_seat("x", str(c), "origin", False)
print("H1 next look status", st2, "(3 = nothing new): the amendment of M1 is now stored as read")

# H2
o, c = setup("h2", {1: "text one", 2: "text two"})
st, txt, rem = L.look_seat("x", str(c), "origin", False)
mem = pathlib.Path(L.memory(str(c))) / "x.json"
ms = L.messages((o / "docs/seats/x.md").read_text(encoding="utf-8"))
mem.write_text(json.dumps({"blob": "0" * 40, "read": 2, "sums": {"2": L._sum(ms[2])}}))   # M1 never seen: absent from sums
st, txt, rem = L.look_seat("x", str(c), "origin", False)
print("H2 status", st, "| M1's text shown:", "text one" in txt, "| first line of what is printed after the head:", txt.splitlines()[1][:90])

# H3
for bad in ({"blob": None, "read": "two"}, {"blob": None, "read": 1, "sums": ["x"]}, {"blob": None, "read": None}):
    o, c = setup("h3_%d" % len(str(bad)), {1: "text one"})
    mem = pathlib.Path(L.memory(str(c))) / "x.json"; mem.write_text(json.dumps(bad))
    r = subprocess.run([sys.executable, "-I", "-B", str(LISTEN), "--once", "--repo", str(c), "--seat", "x"], capture_output=True, text=True)
    print("H3 memory %s -> rc %d; stderr last line: %s" % (json.dumps(bad), r.returncode, (r.stderr.strip().splitlines() or [""])[-1][:110]))

# H4
o, c = setup("h4", {1: "text one"})
real = L.git
L.git = lambda *a, cwd=None: (124, "", "git rev-parse did not answer within 180 seconds") if a and a[0] == "rev-parse" and ":" in a[-1] else real(*a, cwd=cwd)
try:
    print("H4", L.look_seat("x", str(c), "origin", False)[:2])
finally:
    L.git = real
