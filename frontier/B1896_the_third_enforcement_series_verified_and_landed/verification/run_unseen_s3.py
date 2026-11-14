"""main's unseen cases for series 3 of WP-0.7 (U16.a-d, U17.a-c, U21.a-d, U20.a-c, U24.a-h, and U9.b again), run on main's head with
the series applied.  Each case is planted in the scratch checkout and COMMITTED there under the repository's author, so that the
attribution gate can fail only for what is planted; a control, an empty commit, must change no gate.  Every gate is run through
the runner.  Written by main before it read a patch of the series.

AS COMMITTED this file differs from the one that was first run in five places: four marked CHANGED FOR THE COMMIT, and the call
of the mask in the loop.  The two banned phrases are read from the gate's own list and not typed, and the phrase a gate's
message names is masked in the output.  The reason is the series itself: its framing gate reads every text file under
frontier/.  The six cases those changes touch were run again with this file and gave what the first run gave; the two of
them that plant a retracted phrase were run a third time, after the mask was made to see an apostrophe that a message
escapes.  This paragraph was written after the last run; no line of code differs from what ran."""
import json, os, pathlib, re, shutil, subprocess, sys, tempfile
T = pathlib.Path(__file__).resolve().parent
W = pathlib.Path(sys.argv[1]).resolve()
HEAD = subprocess.run(["git", "-C", str(W), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()

def git(*a):
    return subprocess.run(["git", "-C", str(W), "-c", "user.name=originaxiom", "-c", "user.email=originaxiom@users.noreply.github.com", *a], capture_output=True, text=True)

def gates(where=None):
    where = where or W
    env = {k: v for k, v in os.environ.items() if not k.startswith("OA_") and not k.startswith("GIT_")}
    r = subprocess.run([sys.executable, "-B", str(where / "scripts/gates/gates.py")], cwd=str(where), env=env, capture_output=True, text=True)
    res = {}
    for l in r.stdout.splitlines():
        m = re.match(r"\s*(PASS|FAIL|SKIP)\s+([\w-]+):\s?(.*)$", l)
        if m:
            res[m.group(2)] = (m.group(1), m.group(3))
    return res

def reset():
    git("reset", "-q", "--hard", HEAD); git("clean", "-fdq")

def P(rel):
    return W / rel

def add(rel, text):
    p = P(rel); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text, encoding="utf-8")

def append(rel, text):
    p = P(rel); p.write_text(p.read_text(encoding="utf-8").rstrip("\n") + "\n\n" + text + "\n", encoding="utf-8")

def controls(fn):
    f = P("tests/GATE_CONTROLS.json"); d = json.loads(f.read_text(encoding="utf-8")); fn(d)
    f.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

def u16a():
    def fn(d):
        for k in d: d[k] = "tests/test_seat_listener.py::test_the_messages_of_a_page_are_read_whole_and_in_their_numbers"
    controls(fn)
def u16b():
    add("tests/test_planted_controls.py", "import pytest\n\n\n@pytest.mark.xfail\ndef test_planted_xfail():\n    assert False\n")
    def fn(d):
        for k in d: d[k] = "tests/test_planted_controls.py::test_planted_xfail"
    controls(fn)
def u16c():
    add("tests/test_planted_controls.py", "import pytest\n\n\n@pytest.mark.skipif(True, reason=\"\")\ndef test_planted_skipif():\n    assert sum([1, 1]) == 2\n")
    def fn(d):
        for k in d: d[k] = "tests/test_planted_controls.py::test_planted_skipif"
    controls(fn)
def u16d():
    def fn(d):
        ks = sorted(d); d[ks[0]] = d[ks[1]]
    controls(fn)
    return "one entry pointed at another gate's control"

def phrase():
    sys.path.insert(0, str(W / "scripts" / "checks"))
    import importlib, retraction_sweep
    importlib.reload(retraction_sweep)
    ps = retraction_sweep.phrases_in(P("docs/RETRACTED_PHRASES.md").read_text(encoding="utf-8"))
    return [p for p in ps if " " in p and len(p) > 14][-1]
def u17a():
    ph = phrase(); add("papers/planted_note.tex", "\\section{A planted note}\nWe find that " + ph + " holds.\n"); return "phrase of %d characters" % len(ph)
def u17b():
    ph = phrase(); k = ph.index(" ", len(ph) // 2 - 1) if " " in ph[len(ph) // 2 - 1:] else ph.rindex(" ")
    append("README.md", "A planted line: " + ph[:k] + "\n" + ph[k + 1:] + "."); return "broken after %d characters" % k
def u17c():
    ph = phrase(); append("README.md", "A planted line: " + ph.upper() + ".")

def _banned():
    """the framing gate's first two phrases, read from its own list.  CHANGED FOR THE COMMIT: they were typed here when the cases
    were run; the framing gate of this series reads every text file under frontier/, this one too."""
    src = P("scripts/gates/gates.py").read_text(encoding="utf-8")
    block = src[src.index("BANNED = ["):]
    return re.findall(r'^    "([^"]+)",', block[:block.index("\n]")], flags=re.M)[:2]
BANNED = _banned()
def u21a():
    w = BANNED[0].split(" ")          # CHANGED FOR THE COMMIT: built from the gate's phrase; the planted text is the same
    append("README.md", "A planted line: here " + " ".join(w[:3]) + "\n" + " ".join(w[3:]) + ", it is said.")
def u21b():
    add("docs/planted.rst", "A planted page\n==============\n\nHere " + BANNED[0] + ".\n"); add("docs/planted.html", "<html><body><p>Here " + BANNED[0] + ".</p></body></html>\n")
def u21c():
    w, v = BANNED[0].split(" "), BANNED[1].split(" ")          # CHANGED FOR THE COMMIT: as above; two spaces, and a no-break space
    append("README.md", "A planted line: " + " ".join(w[:2]) + "  " + " ".join(w[2:]) + ". And " + " ".join(v[:4]) + "\u00a0" + " ".join(v[4:]) + ".")
def u21d():
    add("planted_note.txt", "Here " + BANNED[0] + ".\n")

def proven_row(make):
    f = P("CLAIMS.md"); t = f.read_text(encoding="utf-8")
    sec = t.index("## Proven"); nxt = t.index("\n## ", sec + 5)
    rows = [m for m in re.finditer(r"^\| P\d+[a-z]? \|.*$", t[sec:nxt], flags=re.M)]
    last = rows[-1]; row = last.group(0)
    new = make(re.sub(r"^\| P\d+[a-z]? \|", "| P998 |", row))
    at = sec + last.end()
    f.write_text(t[:at] + "\n" + new + t[at:], encoding="utf-8")
    return "a row P998 added after %s" % row.split("|")[1].strip()
strip_locks = lambda row: re.sub(r"`tests/[A-Za-z0-9_./]+\.py`", "its lock", row)
def u20a():
    return proven_row(lambda row: strip_locks(row).rstrip("| ").rstrip() + " Lock: `tests/conftest.py` |")
def u20b():
    return proven_row(lambda row: strip_locks(row).rstrip("| ").rstrip() + " Locked by the B730 locks |")
def u20c():
    add("tests/planted_only_a_directory.py/.gitkeep", "")
    return proven_row(lambda row: strip_locks(row).rstrip("| ").rstrip() + " Lock: `tests/planted_only_a_directory.py` |")

def vac(body, rel="tests/test_planted_vacuity.py", head=""):
    add(rel, head + "def test_planted():\n" + body + "\n")
def u24a(): vac("    assert len([1, 2]) == 2")
def u24b(): vac('    assert "a" in "abc"')
def u24c(): vac("    assert True is not False")
def u24d(): vac("    if False:\n        assert 1 == 2")
def u24e(): vac("    assert not None")
def u24f(): vac("    with pytest.raises(ZeroDivisionError):\n        1 / 0", head="import pytest\n\n\n")
def u24g(): vac("    assert len([1, 2]) == 2", rel="frontier/B9002_planted/verification/test_b9002_planted.py")
def u24h(): vac("    x = 3\n    assert x == 3")

CASES = [("U16.a", u16a, ["gate-controls"]), ("U16.b", u16b, ["gate-controls"]), ("U16.c", u16c, ["gate-controls"]), ("U16.d", u16d, ["gate-controls"]),
         ("U17.a", u17a, ["retraction-sweep"]), ("U17.b", u17b, ["retraction-sweep"]), ("U17.c", u17c, ["retraction-sweep"]),
         ("U21.a", u21a, ["framing"]), ("U21.b", u21b, ["framing"]), ("U21.c", u21c, ["framing"]), ("U21.d", u21d, ["framing"]),
         ("U20.a", u20a, ["claims"]), ("U20.b", u20b, ["claims"]), ("U20.c", u20c, ["claims"]),
         ("U24.a", u24a, ["test-vacuity"]), ("U24.b", u24b, ["test-vacuity"]), ("U24.c", u24c, ["test-vacuity"]), ("U24.d", u24d, ["test-vacuity"]),
         ("U24.e", u24e, ["test-vacuity"]), ("U24.f", u24f, ["test-vacuity"]), ("U24.g", u24g, ["test-vacuity"]), ("U24.h", u24h, ["test-vacuity"])]
def masked(msg):
    """CHANGED FOR THE COMMIT: a gate's message with the banned or retracted phrase it names replaced by a mark, since this
    file's output is committed under frontier/, where the framing gate would read the phrase"""
    for ph in list(BANNED) + [phrase()]:
        for form in (ph, ph.replace("'", "\\'")):          # a message that prints a list escapes an apostrophe
            msg = re.sub(re.escape(form), "[the phrase]", msg, flags=re.I)
    return msg


only = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
reset()
base = gates(); base_fail = sorted(k for k, v in base.items() if v[0] != "PASS")
print("series head", HEAD[:9], "| gates", len(base), "| not passing before any plant:", base_fail, flush=True)
OUT = {"head": HEAD, "gates": len(base), "not passing before any plant": base_fail}
git("commit", "-q", "--allow-empty", "-m", "control: an empty commit under the repository's author")
res = gates(); OUT["control"] = {"gates newly failing": sorted(k for k, v in res.items() if v[0] == "FAIL" and k not in base_fail)}
print("control (an empty commit): newly failing", OUT["control"]["gates newly failing"], flush=True)
for name, plant, must in CASES:
    if only and name not in only:
        continue
    reset()
    try:
        note = plant() or ""
    except Exception as ex:
        OUT[name] = {"note": "THE PLANT COULD NOT BE MADE: %r" % (ex,), "committed": False, "CAUGHT": None}
        # (2026-11-12: the line below ended in `continue`, and the run went on to the next case.  It stops the run, as below.)
        print(name, "PLANT FAILED", repr(ex)[:200], flush=True)
        reset()
        raise SystemExit("STOPPED at %s: the plant could not be made (%r). Mend the case" % (name, ex))
    git("add", "-A"); c = git("commit", "-q", "-m", "planted case " + name)
    # ADDED 2026-11-12 (Review 80; owed by main's word in its third folder for the builder, section 6, item 4).  A PLANT THAT
    # CHANGES NOTHING STOPS THE RUN.  A case is committed in the scratch checkout.  Where the case had changed nothing there was
    # nothing to commit: the gates were then run on the tree as it stood, and the case was written down with "committed": false
    # and "not caught".  No case of the kept output is so; the run now ends there, with a sentence.
    if c.returncode != 0:
        reset()
        raise SystemExit("STOPPED at %s: the planted case changed nothing in the checkout, and no commit was made. Gates that pass on it show nothing: mend the case" % name)
    res = gates()
    new = sorted(k for k, v in res.items() if v[0] == "FAIL" and k not in base_fail)
    OUT[name] = {"note": note, "committed": c.returncode == 0, "named gate": must, "gates newly failing": {k: masked(res[k][1][:300]) for k in new},
                 "CAUGHT BY THE NAMED GATE": all(m in new for m in must), "CAUGHT BY SOME GATE": bool(new)}
    print("%-6s committed=%s named=%s any=%s  newly failing: %s  %s" % (name, c.returncode == 0, OUT[name]["CAUGHT BY THE NAMED GATE"], bool(new), new, note[:70]), flush=True)
    (T / "unseen_s3.json").write_text(json.dumps(OUT, indent=1, ensure_ascii=False))
reset()
# ---- U9.b again: a folder that is a repository with no commit, holding the gates, their checkers and three pages
if not only or "U9.b" in only:
    E = pathlib.Path(tempfile.mkdtemp(prefix="oa-u9b-"))
    for d in ("scripts/gates", "scripts/checks"):
        shutil.copytree(W / d, E / d, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for f in ("README.md", "CLAIMS.md", "GENESIS.md"):
        shutil.copy(W / f, E / f)
    subprocess.run(["git", "init", "-q"], cwd=str(E), capture_output=True)
    src = (W / "scripts/gates/gates.py").read_text(encoding="utf-8")
    spec = {}
    res = gates(E)
    tables = re.search(r"READS_TRACKED = frozenset\(\{(.*?)\}\).*?READS_HISTORY = frozenset\(\{(.*?)\}\)", src, re.S)
    names = sorted(set(re.findall(r'"([a-z0-9-]+)"', tables.group(1) + tables.group(2))))
    t = {k: res.get(k) for k in names}
    OUT["U9.b git init and no commit"] = {"gates in the two tables": len(names),
        "refused": sorted(k for k, v in t.items() if v and v[0] == "FAIL" and "refused" in v[1]),
        "failing otherwise": {k: v[1][:110] for k, v in t.items() if v and v[0] == "FAIL" and "refused" not in v[1]},
        "PASSING": {k: v[1][:110] for k, v in t.items() if v and v[0] != "FAIL"}, "absent": sorted(k for k, v in t.items() if not v)}
    print("U9.b:", {k: (len(v) if not isinstance(v, int) else v) for k, v in OUT["U9.b git init and no commit"].items()}, flush=True)
    shutil.rmtree(E, ignore_errors=True)
    (T / "unseen_s3.json").write_text(json.dumps(OUT, indent=1, ensure_ascii=False))
print("written", flush=True)
