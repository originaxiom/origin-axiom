#!/usr/bin/env python3
"""Review 80: main's own plants for the rows of agy-002's file that say a lock does not hold what its page says.

Run INSIDE a scratch checkout of main (never in the working tree):

    cd <scratch checkout> && python3 <this file> [name-prefix ...]

Each plant changes one thing, runs the arc's lock, records whether the lock still passes, and puts the checkout back
with git.  The first entry of each arc plants nothing and must pass.  A plant that "passes" is a change the lock does
not hold.  Main wrote these from the reader's descriptions and ran none of its code."""
# NOTE OF THE MEND, 2026-11-12 (R80b, part 6; owed by main's word in its third folder for the builder, section 6, item 4:
# in every script of main's that plants, a plant that changes nothing stops the run; and a check names a commit, never a
# branch).  Main's script stands as main wrote it in ../checks/, held there by its hash.  This copy differs in the marked
# places: the lines main wrote stand after "#| ", the lines that replace them follow, to "# END OF THE MEND".  With each
# marked block put back, and this note taken out, the file is main's, byte for byte: the arc's lock holds that.
#   0. a plant made through verdict() was written back without asking whether it changed the file.  One did not: the
#      plant on B1885's verdict line, whose pattern matched nothing (main's own finding at the landing of this arc).  The
#      helper now refuses a plant that leaves the file as it was, as text() did already;
#   1. a plant that could not be made was recorded as "PLANT NOT MADE" and the run went on to the next.  It stops the run;
#   2. after every plant the checkout is asked what changed.  Where nothing did, the run stops: this holds for a plant made
#      by any means, and not only through the two helpers;
#   3. with these, the run stops at the plant on B1885's verdict line, whose pattern matches nothing.  So that the script can
#      run to its end, that plant is made as main made it properly at the landing (../main_at_the_landing/): the note is
#      taken out from its first words to the bracket that closes it;
#   4. the same for the plant "'still passes' turned into 'IS REFUSED' on the page" of B1893.  The page does not hold the
#      words "still passes", and did not at the commit the review read: main's kept output gives that plant as not made.
#      It is made on the words the page has ("still pass", across a line break as well).  That is the builder's reading of
#      the plant's name, and is said here.
# END OF THE NOTE
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
# MENDED (0).  Main wrote:
#|     p = arc(n) / "arc_verdict.json"; v = json.loads(p.read_text(encoding="utf-8")); fn(v)
#|     p.write_text(json.dumps(v, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    p = arc(n) / "arc_verdict.json"; was = json.loads(p.read_text(encoding="utf-8")); v = json.loads(json.dumps(was)); fn(v)
    assert v != was, "the plant changed nothing in %s" % p
    p.write_text(json.dumps(v, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
# END OF THE MEND


def text(path, fn):
    t = path.read_text(encoding="utf-8"); t2 = fn(t)
    assert t2 != t, "the plant changed nothing in %s" % path
    path.write_text(t2, encoding="utf-8")


def setv(key, val):
    def f(v): v[key] = val
    return f


# MENDED (2).  Main wrote:
#| G = ROOT / "scripts" / "gates" / "gates.py"
def _the_note_taken_out(c):
    """main's own, from ../main_at_the_landing/the_plant_on_b1885_made_properly.py: the note, to the bracket that closes it"""
    i = c.index(", and 18 for the grid"); j = c.index("[", i); depth = 0
    for k in range(j, len(c)):
        depth += (c[k] == "[") - (c[k] == "]")
        if depth == 0: return c[:i] + c[k + 1:]
    raise RuntimeError("the note's bracket does not close")


G = ROOT / "scripts" / "gates" / "gates.py"
# END OF THE MEND
PLANTS = [
    # --- B1893 (row 23)
    ("B1893", "nothing planted", None),
    ("B1893", "the verdict changed from PROVED to NEGATIVE", lambda: verdict("B1893", setv("verdict", "NEGATIVE"))),
    ("B1893", "the verdict line made to open with ZERO CAUGHT", lambda: verdict("B1893", lambda v: v.__setitem__("claim_one_line", "ZERO CAUGHT. " + v["claim_one_line"]))),
    ("B1893", "the rows of the cases U10 to U19 deleted from the page", lambda: text(arc("B1893") / "FINDINGS.md", lambda t: "\n".join(l for l in t.split("\n") if not re.match(r"\| U1\d", l)))),
# MENDED (4).  Main wrote:
#|     ("B1893", "'still passes' turned into 'IS REFUSED' on the page", lambda: text(arc("B1893") / "FINDINGS.md", lambda t: t.replace("still passes", "IS REFUSED"))),
    ("B1893", "'still passes' turned into 'IS REFUSED' on the page", lambda: text(arc("B1893") / "FINDINGS.md", lambda t: re.sub(r"still(\s+)pass(es)?", r"IS\1REFUSED", t))),
# END OF THE MEND
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
# MENDED (3).  Main wrote:
#|     ("B1885", "the note on the grid's 18 digits taken out of the verdict line", lambda: verdict("B1885", lambda v: v.__setitem__("claim_one_line", re.sub(r", and 18 for the grid and the two checks made on it \[[^\]]*\]", "", v["claim_one_line"])))),
    ("B1885", "the note on the grid's 18 digits taken out of the verdict line", lambda: verdict("B1885", lambda v: v.__setitem__("claim_one_line", _the_note_taken_out(v["claim_one_line"])))),
# END OF THE MEND
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
# MENDED (1).  Main wrote:
#|         try:
#|             if fn is not None:
#|                 fn()
#|             ok, tail, dt = run(n)
#|             res = "passes" if ok else "FAILS"
#|         except AssertionError as e:
#|             res, tail, dt = "PLANT NOT MADE", str(e)[:90], 0.0
#|         finally:
#|             restore()
        try:
            if fn is not None:
                fn()
                changed = subprocess.run(["git", "status", "--porcelain"], cwd=str(ROOT), capture_output=True, text=True).stdout.strip()
                assert changed, "the plant changed nothing in the checkout"
            ok, tail, dt = run(n)
            res = "passes" if ok else "FAILS"
        except AssertionError as e:
            restore()
            raise SystemExit("STOPPED at the plant %r of %s: %s. A lock that passes on a plant that was not made shows nothing: mend the plant" % (name, n, str(e)[:160]))
        finally:
            restore()
# END OF THE MEND
        out.append({"arc": n, "plant": name, "the lock": res, "tail": tail, "seconds": round(dt, 1)})
        print("%-6s %-78s %-14s %5.1fs  %s" % (n, name[:78], res, dt, tail), flush=True)
    pathlib.Path(__file__).with_name("plants_agy002.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
