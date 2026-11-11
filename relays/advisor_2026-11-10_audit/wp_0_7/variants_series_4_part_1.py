#!/usr/bin/env python3
"""WP-0.7, series 4, its first three patches: this seat's own variants on its own mends, before they are sent.

The three patches close three ways a gate was moved by something that is not the commit: the project's own variables in
the environment, git's own variables, and a sentence on the reviews' page that moved the last review's anchor.  Main
verifies with cases this seat has not seen.  These are other shapes of the same, on the real pages in a scratch clone.

    python3 variants_series_4_part_1.py --src CLONE --work DIR      (CLONE: a clone holding the patches at its HEAD)

Nothing is written into CLONE.  DIR is emptied and used for the scratch clone, one export and one linked worktree.

EXPECTATIONS, written before the first run.  "red" = the named gate returns False.  Three of them are PASSES: each is a
limit of a mend, stated in the note, and the variant pins where the limit lies.
  the project's own variables
    u1   every variable named OA_... that the sources name, set at once to a
         value that would move its reader; all 53 gates                         no gate changes its line
    u2   the runner's own review-due, with OA_POINT_REGISTER and
         OA_REVIEW_MERGES set                                                   it prints what it prints without them
  git's own variables
    u3   the whole tree exported, GIT_DIR pointing at the clone                 read as redirected; every gate of the table
                                                                                refused, none passes
    u4   the clone, GIT_INDEX_FILE pointing at an empty file                    the same
    u5   the clone, GIT_WORK_TREE pointing at an empty folder                   no gate of the table passes
    u6   the clone, GIT_DIR naming its own .git                                 read as full: a hook's environment is not
                                                                                a redirection
    u7   a linked worktree of the clone, as the push hook makes one, with
         GIT_DIR naming the clone's own .git                                    read as redirected: git would read the
                                                                                clone's head and index, not the worktree's
  the review's anchor
    u8   the sentence that names the head as an anchor, inside a fenced block
         of the last review's entry                                             review-fires red
    u9   an older review's anchor retyped (Review 77's)                         review-fires says nothing of the anchor:
                                                                                older entries are not re-judged
    u10  a whole made-up entry, Review 79, landed in two commits as a review
         is landed                                                              review-fires PASSES and counts from it: a
                                                                                review that was not run is not a slip
    u11  the last review's heading retitled in a later commit                   review-fires says nothing of the anchor: the
                                                                                review is known by its number

  u9 AND u11 AS FIRST WRITTEN expected the gate to pass.  In the first run (variants_series_4_part_1_first_run_out.txt, 9 of
  11) both read FAILS, and neither on the anchor: the planted commit took the count of landings since the last review to 50,
  where main's waiver ends, and the gate fired on the count.  The harness had tied the expectation to the count.  The two
  now ask what they meant, that the gate says nothing of the anchor, and were rewritten before the run that judges them.
"""
import sys, os, re, json, shutil, subprocess

src = os.path.abspath(sys.argv[sys.argv.index("--src") + 1])
work = os.path.abspath(sys.argv[sys.argv.index("--work") + 1])
WHO = ["-c", "user.name=originaxiom", "-c", "user.email=planted@example.invalid"]
RUN = r'''
import sys, json, importlib.util
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("gates_under_variants", "scripts/gates/gates.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
names = sorted(g.READS_GIT) if sys.argv[1] == "THE-TABLE" else sorted(g.GATES) if sys.argv[1] == "ALL" else sys.argv[1].split(",")
out = {"_state": [g.checkout_state(), "", ""]}
for name in names:
    try:
        r = g.GATES[name](); d = r[1] if isinstance(r[1], str) else " | ".join(map(str, r[1]))
        out[name] = [bool(r[0]), d[:600]]
    except Exception as e:
        out[name] = [None, "RAISED %s: %s" % (type(e).__name__, str(e)[:200])]
print(json.dumps(out))
'''
PLAIN = {k: v for k, v in os.environ.items() if not k.startswith(("OA_", "GIT_"))}


def sh(args, cwd=None, check=True, env=None, binary=False):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=not binary, env=env)
    if check and r.returncode != 0:
        sys.exit("failed: %s\n%s" % (" ".join(map(str, args))[:200], (r.stderr if not binary else r.stderr.decode("utf-8", "replace"))[:400]))
    return r


def gates(tree, names, env=None):
    arg = names if isinstance(names, str) else ",".join(names)
    r = subprocess.run([sys.executable, "-B", "-c", RUN, arg], cwd=tree, capture_output=True, text=True, env=dict(PLAIN, PYTHONDONTWRITEBYTECODE="1", **(env or {})))
    try:
        return json.loads(r.stdout.strip().split("\n")[-1])
    except Exception:
        sys.exit("the gates did not run in %s: %s" % (tree, (r.stdout + r.stderr)[-400:]))


if os.path.exists(work):
    shutil.rmtree(work)
os.makedirs(work)
clone = os.path.join(work, "clone")
sh(["git", "clone", "-q", "file://" + src, clone])
tip = sh(["git", "-C", clone, "rev-parse", "HEAD"]).stdout.strip()
print("variants on the patches at %s" % tip[:9])
path = lambda rel: os.path.join(clone, rel)
read = lambda rel: open(path(rel), encoding="utf-8").read()


def write(rel, text):
    os.makedirs(os.path.dirname(path(rel)), exist_ok=True)
    with open(path(rel), "w", encoding="utf-8") as fh:
        fh.write(text)


def reset():
    sh(["git", "-C", clone, "reset", "-q", "--hard", tip]); sh(["git", "-C", clone, "clean", "-q", "-fd"])


def commit(text):
    sh(["git", "-C", clone, "add", "-A"]); sh(["git", "-C", clone, *WHO, "commit", "-q", "-m", text])
    return sh(["git", "-C", clone, "rev-parse", "--short=9", "HEAD"]).stdout.strip()


results = []


def line(tag, ok, text):
    results.append(bool(ok)); print("%-4s %-6s %s" % (tag, "HOLDS" if ok else "FAILS", text), flush=True)


def table(folder, env):
    out = gates(folder, "THE-TABLE", env); state = out.pop("_state")[0]
    passing = sorted(n for n, v in out.items() if v[0]); refused = sorted(n for n, v in out.items() if v[0] is False and "refused" in v[1])
    return state, out, passing, refused


# ---- the project's own variables
names = set()
for folder in ("scripts/gates", "scripts/checks"):
    for f in sorted(os.listdir(path(folder))):
        if f.endswith(".py"):
            names.update(re.findall(r"\bOA_[A-Z0-9_]+\b", read(folder + "/" + f)))
empty = os.path.join(work, "a_page_with_no_row.md")
open(empty, "w", encoding="utf-8").write("# a page with no row\n")
hostile = {n: ("2099-01-01" if n.endswith("_TODAY") else "0" if n.endswith("_MERGES") else "x=y" if n.endswith("_OVERRIDE")
               else work if n == "OA_ROOT" else empty) for n in sorted(names)}
hostile["OA_REVIEW_MERGES"] = "0"
base = gates(clone, "ALL"); base.pop("_state")
moved = gates(clone, "ALL", hostile); moved.pop("_state")
changed = sorted(n for n in base if base[n] != moved[n])
line("u1", len(base) == 53 and not changed, "%d variables named OA_... set at once, all %d gates: %d change their line%s" % (
    len(hostile), len(base), len(changed), (": " + ", ".join(changed)) if changed else ""))
due = lambda env: subprocess.run([sys.executable, "-B", os.path.join("scripts", "gates", "gates.py"), "review-due"], cwd=clone, capture_output=True, text=True,
                                 env=dict(PLAIN, PYTHONDONTWRITEBYTECODE="1", **env)).stdout
a, b = due({}), due({"OA_POINT_REGISTER": empty, "OA_REVIEW_MERGES": "0"})
line("u2", bool(a.strip()) and a == b, "review-due with two of the variables set: %s (%d lines)" % ("prints the same" if a == b else "PRINTS SOMETHING ELSE", len(a.splitlines())))

# ---- git's own variables
export = os.path.join(work, "export"); os.makedirs(export)
tar = sh(["git", "-C", clone, "archive", tip], binary=True).stdout
subprocess.run(["tar", "-x", "-C", export], input=tar, check=True)
state, out, passing, refused = table(export, {"GIT_DIR": os.path.join(clone, ".git")})
line("u3", state == "redirected" and not passing and len(refused) == len(out), "the whole tree exported, GIT_DIR pointing at the clone: read as %r; %d of %d refused, %d pass" % (state, len(refused), len(out), len(passing)))
shutil.rmtree(export, ignore_errors=True)
nothing = os.path.join(work, "an_empty_index"); open(nothing, "w").close()
state, out, passing, refused = table(clone, {"GIT_INDEX_FILE": nothing})
line("u4", state == "redirected" and not passing and len(refused) == len(out), "the clone, GIT_INDEX_FILE pointing at an empty file: read as %r; %d of %d refused, %d pass" % (state, len(refused), len(out), len(passing)))
hollow = os.path.join(work, "an_empty_folder"); os.makedirs(hollow)
state, out, passing, refused = table(clone, {"GIT_WORK_TREE": hollow})
line("u5", not passing, "the clone, GIT_WORK_TREE pointing at an empty folder: read as %r; %d of %d refused, %d pass" % (state, len(refused), len(out), len(passing)))
state, out, passing, refused = table(clone, {"GIT_DIR": os.path.join(clone, ".git")})
line("u6", state == "full" and not any("sends git" in v[1] for v in out.values()), "the clone, GIT_DIR naming its own .git: read as %r; refused as redirected: %d" % (
    state, sum(1 for v in out.values() if "sends git" in v[1])))
wt = os.path.join(work, "a_linked_worktree")
sh(["git", "-C", clone, "worktree", "add", "-q", "--detach", wt, tip])
state, out, passing, refused = table(wt, {"GIT_DIR": os.path.join(clone, ".git")})
line("u7", state == "redirected" and not passing, "a linked worktree with GIT_DIR naming the clone's .git: read as %r; %d of %d refused, %d pass" % (state, len(refused), len(out), len(passing)))
plain_state = gates(wt, ["review-fires"])["_state"][0]
print("     (the same worktree with no variable set is read as %r)" % plain_state)
sh(["git", "-C", clone, "worktree", "remove", "--force", wt])

# ---- the review's anchor
PAGE = "docs/progress/REVIEWS.md"
one = lambda: gates(clone, ["review-fires"])["review-fires"]
control = one()
assert control[0] is True, "review-fires must pass before any variant: %s" % control[1]
page = read(PAGE); head = tip[:9]
reset(); write(PAGE, page + "\n```\n**anchor-commit: `%s`**\n```\n" % head); commit("planted: an anchor inside a fenced block")
r = one(); line("u8", r[0] is False and "names an anchor 2 time(s)" in r[1], "an anchor line inside a fenced block at the end of the page: %s" % r[1][:110])
reset(); heads = [(int(m.group(1)), m.start()) for m in re.finditer(r"^# Review (\d+) ", page, re.M)]
last = max(heads); before = [h for h in heads if h[0] == last[0] - 1][0]
older = page[before[1]:last[1]]; typed = re.findall(r"anchor-commit: `([0-9a-f]{7,40})`", older)[-1]
write(PAGE, page[:before[1]] + older.replace("`%s`" % typed, "`%s`" % head) + page[last[1]:]); commit("planted: an older review's anchor retyped")
r = one(); line("u9", "anchor" not in r[1] and "entry of Review" not in r[1], "Review %d's anchor retyped: the gate says nothing of the anchor (%s)" % (before[0], r[1][:70]))
reset(); n = last[0] + 1
entry = "\n# Review %d (2026-11-12) — a review that was not run\n\nfresh-clone: PASS @ %s\nsample seed: %s\ngate controls: 53 registered\n\n### Action items (Review %d)\n\n- [x] R%d-1 nothing\n" % (n, head, head, n, n)
write(PAGE, page + entry); landed = commit("planted: a made-up review")
write(PAGE, page + entry + "\n**anchor-commit: `%s`**\n" % landed); commit("planted: and its anchor")
r = one(); line("u10", r[0] is True and r[1].startswith("1 merges since the last review"), "a whole made-up entry, landed in two commits: passes and counts from it (%s)" % r[1][:60])
reset(); title = re.search(r"^# Review %d .*$" % last[0], page, re.M).group(0)
write(PAGE, page.replace(title, title + " (retitled)")); commit("planted: the last review's heading retitled")
r = one(); line("u11", "anchor" not in r[1] and "entry of Review" not in r[1], "the last review's heading retitled: the gate says nothing of the anchor (%s)" % r[1][:70])

print("\n%d of %d expectations hold" % (sum(results), len(results)))
