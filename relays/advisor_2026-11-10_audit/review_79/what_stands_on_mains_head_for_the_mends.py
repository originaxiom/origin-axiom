#!/usr/bin/env python3
"""What stands on main's head for the mends of Review 79's findings in the enforcement package's files (card C6).

    python3 what_stands_on_mains_head_for_the_mends.py <a checkout at main's head>

Measured before any mend is built, so that each mend is known to meet what is there.  Nothing is written into the checkout."""
import collections
import datetime
import importlib.util
import os
import re
import subprocess
import sys

MAIN = os.path.abspath(sys.argv[1])


def git(*a):
    r = subprocess.run(["git", "-C", MAIN, *a], capture_output=True, text=True, errors="replace")
    assert r.returncode == 0, r.stderr[-400:]
    return r.stdout


spec = importlib.util.spec_from_file_location("gates_read", os.path.join(MAIN, "scripts", "gates", "gates.py"))
g = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True
spec.loader.exec_module(g)
print("main's head: " + git("rev-parse", "--short=9", "HEAD").strip())

# ---- the arrival gate: what it reads today, and what it excuses --------------------------------------------------------
found = excused = 0
by_word = collections.Counter()
for rel in g._arrival_files(MAIN):
    if rel in g.ARRIVAL_EXEMPT:
        continue
    try:
        text = open(os.path.join(MAIN, rel), encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    low = text.lower()
    for phrase in g.ARRIVAL_PHRASES:
        for m in re.finditer(re.escape(phrase), low):
            found += 1
            before = low[:m.start()]
            ends = [e.end() for e in g._ARRIVAL_SENTENCE_END.finditer(before)]
            own = before[ends[-1]:] if ends else before
            neg = g._ARRIVAL_NEG_RE.search(" " + own[-160:] + " ")
            if neg:
                excused += 1
                by_word[neg.group(0).strip()] += 1
print("\nTHE ARRIVAL GATE, on the pages it reads and does not exempt")
print("   a phrase of arrival stands %d time(s); %d of them are excused by a word in their own sentence" % (found, excused))
print("   the word that excuses, as the pattern first meets it: " + ", ".join("%s (%d)" % kv for kv in by_word.most_common()))

# ---- the day: the commit's own day and the day of its time in UTC ------------------------------------------------------
root = g.COMMIT_DAY_FROM
line = [l.split() for l in git("log", "--first-parent", "--format=%H %ct %cs %P", root + "..HEAD").splitlines()]
reach = [l.split() for l in git("log", "--format=%H %ct %cs %P", root + "..HEAD").splitlines()]
when = {l[0]: (int(l[1]), l[2]) for l in reach}
utc = lambda t: datetime.datetime.fromtimestamp(t, datetime.timezone.utc).date().isoformat()
print("\nTHE DAY, after %s" % root[:9])
print("   commits on main's own line: %d;   reachable from the head: %d;   on a side line: %d" % (len(line), len(reach), len(reach) - len(line)))
print("   on main's own line, the commit's own day differs from the day of its time in UTC: %d" % sum(1 for l in line if l[2] != utc(int(l[1]))))
back_time = back_day = 0
for l in reach:
    for p in l[3:]:
        if p in when:
            back_time += when[l[0]][0] < when[p][0]
            back_day += when[l[0]][1] < when[p][1]
print("   reachable commits whose time is before a parent's: %d;   whose own day is before a parent's own day: %d" % (back_time, back_day))
on_line = {l[0] for l in line}
side_back = sum(1 for l in reach if l[0] not in on_line and any(p in when and when[l[0]][0] < when[p][0] for p in l[3:]))
print("   of those before a parent's time, on a side line: %d" % side_back)

# ---- the hash lists: who touches one off main's own line ---------------------------------------------------------------
lists_now = [p for p in git("ls-files").splitlines() if re.search(r"(^|/)(ARTIFACT_HASHES[^/]*|[^/]*SHA256[^/]*|[^/]*hashes[^/]*)\.txt$", p)]
since = getattr(g, "HASH_LISTS_FROM", None) or getattr(g, "SEAL_IMMUTABLE_FROM", root)
touch_all = set(git("log", "--format=%H", since + "..HEAD", "--", *lists_now).split()) if lists_now else set()
touch_line = set(git("log", "--first-parent", "--format=%H", since + "..HEAD", "--", *lists_now).split()) if lists_now else set()
print("\nTHE HASH LISTS, by a first pattern of their names: %d tracked" % len(lists_now))
print("   commits after %s that touch one: %d on main's own line, %d more on a side line" % (since[:9], len(touch_line), len(touch_all - touch_line)))

# ---- the runner: which passing sentences hold a word that prints SKIP --------------------------------------------------
src = open(os.path.join(MAIN, "scripts", "gates", "gates.py"), encoding="utf-8").read()
at = src.index("def result_line(")
words = re.findall(r'"([^"]+)" in detail', src[at:src.index("\n\n\n", at)])
print("\nTHE RUNNER'S LINE: a passing sentence that holds one of these prints SKIP, or prints whole: " + (", ".join(repr(w) for w in words) or "(not read)"))
passing = {}
for name, gate in g.GATES.items():
    try:
        ok, detail = gate()[:2]
    except Exception:
        continue
    if ok and isinstance(detail, str) and g.result_line(name, ok, detail).strip().startswith("SKIP"):
        passing[name] = detail
print("   gates that pass on this checkout and are printed SKIP: %d" % len(passing))
for name, detail in sorted(passing.items()):
    print("      %s: %s" % (name, detail[:150]))
