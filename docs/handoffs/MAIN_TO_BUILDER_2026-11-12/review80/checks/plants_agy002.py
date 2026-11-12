#!/usr/bin/env python3
"""Review 80: main's own plants for the rows of agy-002's file that say a lock does not hold what its page says.

Run INSIDE a scratch checkout of main (never in the working tree):

    cd <scratch checkout> && python3 <this file> [name-prefix ...]

Each plant changes one thing, runs the arc's lock, records whether the lock still passes, and puts the checkout back
with git.  The first entry of each arc plants nothing and must pass.  A plant that "passes" is a change the lock does
not hold.  Main wrote these from the reader's descriptions and ran none of its code."""
import json, pathlib, re, subprocess, sys, time

ROOT = pathlib.Path.cwd()
assert (ROOT / "scripts" / "gates" / "gates.py").is_file() and "wt_" in str(ROOT), "run in a scratch checkout"


def arc(n):
    return next(p for p in (ROOT / "frontier").iterdir() if p.name.startswith(n + "_"))


def lock(n):
    return sorted((arc(n) / "verification").glob("test_*.py"))[0]


def run(n):
    t = time.time()
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x", str(lock(n))], capture_output=True, text=True, cwd=str(ROOT))
    tail = (r.stdout.strip().split("\n") or [""])[-1]
    return r.returncode == 0, tail[:90], time.time() - t


def restore():
    subprocess.run(["git", "checkout", "-q", "--", "."], cwd=str(ROOT), check=True)
    subprocess.run(["git", "clean", "-q", "-fd", "frontier", "scripts", "docs"], cwd=str(ROOT), check=True)


def verdict(n, fn):
    p = arc(n) / "arc_verdict.json"; v = json.loads(p.read_text(encoding="utf-8")); fn(v)
    p.write_text(json.dumps(v, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def text(path, fn):
    t = path.read_text(encoding="utf-8"); t2 = fn(t)
    assert t2 != t, "the plant changed nothing in %s" % path
    path.write_text(t2, encoding="utf-8")


def setv(key, val):
    def f(v): v[key] = val
    return f


G = ROOT / "scripts" / "gates" / "gates.py"
PLANTS = [
    # --- B1893 (row 23)
    ("B1893", "nothing planted", None),
    ("B1893", "the verdict changed from PROVED to NEGATIVE", lambda: verdict("B1893", setv("verdict", "NEGATIVE"))),
    ("B1893", "the verdict line made to open with ZERO CAUGHT", lambda: verdict("B1893", lambda v: v.__setitem__("claim_one_line", "ZERO CAUGHT. " + v["claim_one_line"]))),
    ("B1893", "the rows of the cases U10 to U19 deleted from the page", lambda: text(arc("B1893") / "FINDINGS.md", lambda t: "\n".join(l for l in t.split("\n") if not re.match(r"\| U1\d", l)))),
    ("B1893", "'still passes' turned into 'IS REFUSED' on the page", lambda: text(arc("B1893") / "FINDINGS.md", lambda t: t.replace("still passes", "IS REFUSED"))),
    # --- B1896 (row 26)
    ("B1896", "nothing planted", None),
    ("B1896", "'Five are not caught' turned into 'None is not caught' on the page", lambda: text(arc("B1896") / "FINDINGS.md", lambda t: t.replace("Five are not caught", "None is not caught"))),
    ("B1896", "every '17' on the page's first forty lines turned into '22'", lambda: text(arc("B1896") / "FINDINGS.md", lambda t: "\n".join([l.replace("17", "22") for l in t.split("\n")[:40]] + t.split("\n")[40:]))),
    ("B1896", "the runner of the sealed cases deleted", lambda: (arc("B1896") / "verification" / "run_unseen_s3.py").unlink()),
    ("B1896", "the runner of the cases written after reading deleted", lambda: (arc("B1896") / "verification" / "after_reading_s3.py").unlink()),
    ("B1896", "the verdict line made to open with ALL TWENTY-TWO CAUGHT", lambda: verdict("B1896", lambda v: v.__setitem__("claim_one_line", "ALL TWENTY-TWO CAUGHT. " + v["claim_one_line"]))),
    # --- B1878 (row 29)
    ("B1878", "nothing planted", None),
    ("B1878", "the dated note of 2026-11-12 removed from the page", lambda: text(arc("B1878") / "FINDINGS.md", lambda t: "\n".join(l for l in t.split("\n") if not (l.startswith(">") and ("NOTE 2026-11-12" in l or "planted cases against them" in l))))),
    ("B1878", "the verdict file made invalid JSON", lambda: (arc("B1878") / "arc_verdict.json").write_text("{ this is not json\n", encoding="utf-8")),
    # --- B1885 (row 31)
    ("B1885", "nothing planted", None),
    ("B1885", "the verdict changed from PROVED to REFUTED", lambda: verdict("B1885", setv("verdict", "REFUTED"))),
    ("B1885", "the note on the grid's 18 digits taken out of the verdict line", lambda: verdict("B1885", lambda v: v.__setitem__("claim_one_line", re.sub(r", and 18 for the grid and the two checks made on it \[[^\]]*\]", "", v["claim_one_line"])))),
    # --- B1890 (row 32)
    ("B1890", "nothing planted", None),
    ("B1890", "the verdict file made invalid JSON", lambda: (arc("B1890") / "arc_verdict.json").write_text("{ this is not json\n", encoding="utf-8")),
    ("B1890", "the table of gates that read history shrunk to two names", lambda: text(G, lambda t: re.sub(r"READS_HISTORY = frozenset\(\{.*?\}\)", 'READS_HISTORY = frozenset({"retraction-sweep", "test-vacuity"})', t, count=1, flags=re.S))),
    ("B1890", "the refusal of an empty checkout switched off", lambda: text(G, lambda t: t.replace('            if state == "empty":\n                return False, REFUSED_EMPTY', '            if state == "never":\n                return False, REFUSED_EMPTY'))),
]

if __name__ == "__main__":
    want = sys.argv[1:]
    out = []
    restore()
    for n, name, fn in PLANTS:
        if want and not any(n.startswith(w) for w in want):
            continue
        try:
            if fn is not None:
                fn()
            ok, tail, dt = run(n)
            res = "passes" if ok else "FAILS"
        except AssertionError as e:
            res, tail, dt = "PLANT NOT MADE", str(e)[:90], 0.0
        finally:
            restore()
        out.append({"arc": n, "plant": name, "the lock": res, "tail": tail, "seconds": round(dt, 1)})
        print("%-6s %-78s %-14s %5.1fs  %s" % (n, name[:78], res, dt, tail), flush=True)
    pathlib.Path(__file__).with_name("plants_agy002.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
