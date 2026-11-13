#!/usr/bin/env python3
"""Follow-up to verify_r80b_p45.py's P-796 check on Part 5 patch 3.  That check reported three files of the patch holding
six-word slices of lines that GENESIS.md loses.  Here each slice is traced to the line it comes from, and each line is
classed: the old version line or an old entry of the list of versions (which the patch moves or rewrites and may quote),
or one of the passages that quoted the owner.  Nothing of a passage is printed: only counts, per file and per class."""
import pathlib, subprocess, sys, tempfile, shutil, os
REPO = pathlib.Path(__file__).resolve().parents[2]
ENV = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", PYTHONDONTWRITEBYTECODE="1")
C = "origin/cld/cool-hamilton-k9eqvo"; D = "relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_5"
show = lambda s: subprocess.check_output(["git", "-C", str(REPO), "show", s]).decode("utf-8")
words = lambda s: " ".join(s.lower().split()).split()
old = show("bf76e5ab1:GENESIS.md")
# the new page as the builder's tree has it is not on a ref; take it from the diff's own statement: lines of the old page that
# the version-1.67 page drops are the 7 hunks.  Rebuild the new page by the patch's script would need a checkout; use git
# apply in a temporary worktree of the tree after Part 5 patch 2 is not needed here: the classes are read from the old lines.
patch = show("%s:%s/0003_all_of_the_patch_but_the_foundations_own_page.patch" % (C, D))
added = {}
for c in patch.split("\ndiff --git ")[1:]:
    name = c.split("\n", 1)[0].split(" b/")[-1]
    added[name] = " ".join("\n".join(l[1:] for l in c.split("\n") if l.startswith("+") and not l.startswith("+++")).lower().split())
added["(the script) 0003_the_foundation_at_version_1_67.py"] = " ".join(show("%s:%s/0003_the_foundation_at_version_1_67.py" % (C, D)).lower().split())
added["(the message) 0003_message.txt"] = " ".join(show("%s:%s/0003_message.txt" % (C, D)).lower().split())
tmp = pathlib.Path(tempfile.mkdtemp()); wt = tmp / "wt"
try:
    subprocess.run(["git", "-C", str(REPO), "worktree", "add", "-q", "--detach", str(wt), "bf76e5ab1"], check=True, env=ENV)
    (tmp / "p.patch").write_text(patch, encoding="utf-8")
    subprocess.run(["git", "-C", str(wt), "apply", "--include=frontier/B1904*", "--include=frontier/B1898*", str(tmp / "p.patch")], check=True, env=ENV)
    r = subprocess.run([sys.executable, "-B", "frontier/B1904_the_foundation_at_version_1_67/verification/write_version_1_67.py", "--write"], cwd=str(wt), capture_output=True, text=True, env=ENV)
    new = (wt / "GENESIS.md").read_text(encoding="utf-8")
finally:
    subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(wt)], capture_output=True); shutil.rmtree(tmp, ignore_errors=True)
print("the arc's script on bf76e5ab1 with only B1904 applied: rc=%d" % r.returncode)
newset = set(new.split("\n"))
gone = [l for l in old.split("\n") if l.strip() and l not in newset]
common = {" ".join(w[i:i + 6]) for l in new.split("\n") for w in [words(l)] for i in range(max(0, len(w) - 5))}
def cls(l):
    return "the version line or an entry of the list of versions" if ("**version 1." in l.lower() or l.lstrip().lower().startswith("- **v1.")) else "a passage"
print("lines GENESIS.md loses: %d (%s)" % (len(gone), ", ".join("%d %s" % (sum(1 for l in gone if cls(l) == k), k) for k in sorted({cls(l) for l in gone}))))
for name, text in sorted(added.items()):
    per = {}
    for l in gone:
        w = words(l)
        n = sum(1 for i in range(max(0, len(w) - 5)) if " ".join(w[i:i + 6]) not in common and " ".join(w[i:i + 6]) in text)
        if n:
            per[cls(l)] = per.get(cls(l), 0) + n
    if per:
        print("  %s: %s" % (name, per))
print("files with no slice of any line lost: the rest")
