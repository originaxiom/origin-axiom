#!/usr/bin/env python3
"""A second dry run of gathering old front pages into one folder: NO KEPT DOCUMENT IS EDITED.

    python3 archive_dry_run_2.py SCRATCH_CHECKOUT FRONT_PAGES_JSON [--folder docs/retired] [--page docs/MOVED.md]

SCRATCH_CHECKOUT is a throw-away checkout of main's head: THIS SCRIPT CHANGES IT AND COMMITS IN IT.  The same example
set as the first dry run (the front pages that no code names and that last changed before 2026-10-01), chosen by a rule
and by no reading.

What it does: (1) moves the pages with git mv; (2) writes ONE page, a table of where each page was and where it is;
(3) teaches the path checker to read that table, so that a citation of an old path names the page where it went;
(4) lets the one entry of a data file that is keyed by a page's path follow the page (the attribution baseline); (5) commits;
(6) runs every gate before and after.  No citation is rewritten anywhere, and no page that is kept is touched.
Standard library only."""
import json, os, re, subprocess, sys

root = os.path.abspath(sys.argv[1])
rows = json.load(open(sys.argv[2], encoding="utf-8"))
opt = lambda name, default: sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default
folder, page = opt("--folder", "docs/retired"), opt("--page", "docs/MOVED.md")
WHO = ["-c", "user.name=originaxiom", "-c", "user.email=dryrun@example.invalid"]
PLAIN = {k: v for k, v in os.environ.items() if not k.startswith(("OA_", "GIT_"))}
PLAIN["PYTHONDONTWRITEBYTECODE"] = "1"


def git(*a):
    r = subprocess.run(["git", "-C", root, *a], capture_output=True, text=True, env=PLAIN)
    if r.returncode != 0:
        sys.exit("git %s failed: %s" % (" ".join(a)[:80], r.stderr[:300]))
    return r.stdout


def gates():
    code = ("import sys, json, importlib.util\nsys.dont_write_bytecode = True\n"
            "s = importlib.util.spec_from_file_location('g', 'scripts/gates/gates.py'); g = importlib.util.module_from_spec(s); s.loader.exec_module(g)\n"
            "out = {}\n"
            "for n, f in g.GATES.items():\n"
            "    try:\n        r = f(); out[n] = [bool(r[0]), (r[1] if isinstance(r[1], str) else ' | '.join(map(str, r[1])))[:500]]\n"
            "    except Exception as e:\n        out[n] = [None, 'RAISED %s: %s' % (type(e).__name__, str(e)[:200])]\n"
            "print('@@' + json.dumps(out))\n")
    r = subprocess.run([sys.executable, "-B", "-c", code], cwd=root, capture_output=True, text=True, env=PLAIN)
    return json.loads(r.stdout.split("@@")[-1])


chosen = sorted(r["page"] for r in rows if not r["named by code"] and r["last changed"] < "2026-10-01")
moved = {p: folder + "/" + os.path.basename(p) for p in chosen}
assert len(set(moved.values())) == len(moved), "two pages of the set have one name"
before = gates()
print("the example set: %d front pages; gates before the move: %d of %d pass" % (len(chosen), sum(1 for v in before.values() if v[0]), len(before)))

os.makedirs(os.path.join(root, folder), exist_ok=True)
for old, new in moved.items():
    git("mv", old, new)
lines = ["# A page you were sent to is not where it was",
         "",
         "Pages that no longer describe the programme as it stands were moved out of the reader's way, into `%s/`." % folder,
         "Nothing was deleted, and nothing in them was changed. Find the old place on the left; the page is on the right.",
         "",
         "| where it was | where it is |", "|---|---|"]
lines += ["| `%s` | `%s` |" % (old, new) for old, new in moved.items()]
lines += ["", "*This page is the only record of the move. No other page was edited for it.*", ""]
open(os.path.join(root, page), "w", encoding="utf-8").write("\n".join(lines))

p = os.path.join(root, "scripts", "checks", "check_path_references.py")
s = open(p, encoding="utf-8").read()
old_def = "def scan():\n"
old_rule = ("            if os.path.exists(os.path.join(ROOT, target)) or \\\n"
            "               os.path.exists(os.path.join(citing_dir, target)):\n"
            "                continue\n")
assert s.count(old_def) == 1 and s.count(old_rule) == 1
s = s.replace(old_def, ('MOVED_PAGE = "%s"\n\n\n'
                         'def moved_pages():\n'
                         '    """where each moved page was -> where it is, read from the one page that records the moves"""\n'
                         '    p = os.path.join(ROOT, MOVED_PAGE)\n'
                         '    if not os.path.isfile(p):\n'
                         '        return {}\n'
                         '    return dict(re.findall(r"^\\| `([^`]+)` \\| `([^`]+)` \\|", open(p, encoding="utf-8").read(), re.M))\n\n\n' % page) + old_def)
s = s.replace("    unexplained, total = [], 0\n", "    unexplained, total = [], 0\n    moved = moved_pages()\n")
s = s.replace(old_rule, old_rule + ("            # a page that was moved is where it went: the citation is left as it was written\n"
                                     "            if target in moved and os.path.exists(os.path.join(ROOT, moved[target])):\n"
                                     "                continue\n"))
open(p, "w", encoding="utf-8").write(s)
# a data file that is keyed by a page's path: its entry follows the page
BASELINE = "docs/ATTRIBUTION_BASELINE.json"
followed = 0
bp = os.path.join(root, BASELINE)
if os.path.isfile(bp):
    text = open(bp, encoding="utf-8").read()
    for old, new in moved.items():
        key = '"%s"' % old
        if key in text:
            text = text.replace(key, '"%s"' % new); followed += 1
    if followed:
        open(bp, "w", encoding="utf-8").write(text)
git("add", "-A"); git(*WHO, "commit", "-q", "-m", "a dry run: %d front pages moved into %s, one page that says where each went, one rule in the path checker" % (len(moved), folder))
names = [l.split("\t") for l in git("show", "--name-status", "-M", "--format=", "HEAD").strip().splitlines()]
renames = [n for n in names if n[0].startswith("R")]
other = [n[-1] for n in names if not n[0].startswith("R")]
print("the commit: %d pages moved (each a rename, its text unchanged: %s); other files in it: %d %s" % (
    len(renames), "yes" if all(n[0] == "R100" for n in renames) else "NO", len(other), other))
print("entries of the attribution baseline that followed their page: %d" % followed)
for gen in ("scripts/views/generate.py", "scripts/views/spine.py"):
    subprocess.run([sys.executable, "-B", gen], cwd=root, capture_output=True, text=True, env=PLAIN)
changed = [l[3:] for l in git("status", "--porcelain").split("\n") if l]
print("generated pages that changed when the views were built again: %d %s" % (len(changed), changed[:6]))
if changed:
    git("add", "-A"); git(*WHO, "commit", "-q", "-m", "a dry run: the views generated")
after = gates()
print("gates after the move: %d of %d pass" % (sum(1 for v in after.values() if v[0]), len(after)))
for k in after:
    if before[k][0] and not after[k][0]:
        print("   TURNED RED: %s: %s" % (k, after[k][1][:300]))
print("path-refs after: %s" % after["path-refs"][1][:120])
sys.path.insert(0, os.path.join(root, "scripts", "checks"))
import importlib; c = importlib.import_module("check_path_references")
md = [t for t in git("ls-files", "-z", "*.md").split("\0") if t and os.path.isfile(os.path.join(root, t))]
through = sum(1 for t in md if not t.startswith(c.EXEMPT_CITERS) and t != page
              for m in c.PATH_RE.finditer(open(os.path.join(root, t), encoding="utf-8", errors="replace").read()) if m.group(1) in moved)
print("citations of an old path, left as they were written, that the checker now reads through the one page: %d" % through)
print("front pages directly under docs/: %d; at the root: %d; in %s/: %d" % (
    sum(1 for f in md if f.startswith("docs/") and f.count("/") == 1), sum(1 for f in md if "/" not in f), folder, len(moved)))
