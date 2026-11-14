"""main's cases for series 3 of WP-0.7 written AFTER reading the six patches (AR1 to AR5).  They are not among the cases sealed
beforehand and are not counted with them.  The harness is that of run_unseen_s3.py: each case planted and committed in the
scratch checkout under the repository's author, every gate run, an empty commit as the control.

AS COMMITTED the harness above the cases is that of the committed run_unseen_s3.py, which reads the gate's banned phrases
from the gate and types none; the cases below and the loop are as they were run."""
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

# ---- written by main AFTER it read the six patches; not among the cases sealed beforehand
def ar1():
    add("tests/test_planted_a_directory.py/.gitkeep", "")
    return proven_row(lambda row: strip_locks(row).rstrip("| ").rstrip() + " Lock: `tests/test_planted_a_directory.py` |")
def ar2(): vac("    x, y = 3, 3\n    assert x == y")
def ar3(): vac("    assert (1, 2) == (1, 2)")
def ar4(): vac('    assert 2 > 1 and "a" < "b"')
def ar5(): vac("    x = 3\n    x = 3\n    assert x == 3")
CASES = [("AR1", ar1, ["claims"]), ("AR2", ar2, ["test-vacuity"]), ("AR3", ar3, ["test-vacuity"]), ("AR4", ar4, ["test-vacuity"]), ("AR5", ar5, ["test-vacuity"])]
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
    OUT[name] = {"note": note, "committed": c.returncode == 0, "named gate": must, "gates newly failing": {k: res[k][1][:300] for k in new},
                 "CAUGHT BY THE NAMED GATE": all(m in new for m in must), "CAUGHT BY SOME GATE": bool(new)}
    print("%-6s committed=%s named=%s any=%s  newly failing: %s  %s" % (name, c.returncode == 0, OUT[name]["CAUGHT BY THE NAMED GATE"], bool(new), new, note[:70]), flush=True)
    (T / "after_reading_s3.json").write_text(json.dumps(OUT, indent=1, ensure_ascii=False))
reset()
print("written", flush=True)
