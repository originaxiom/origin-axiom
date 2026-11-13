"""Review 81: main's machine check of the two readers' quotations at the commit they read (7d7ab1dfa).
Every double-quoted string of 15 characters or more in each reader's file is looked for, verbatim, by `git grep -F` at
7d7ab1dfa (whitespace runs collapsed on both sides is NOT done: verbatim only; a quotation that spans a line break is
tried piece by piece at the break). Prints counts and the strings not found."""
import re, subprocess, sys
REV = "7d7ab1dfa"
FILES = {"the web seat": ("df9569fa5", "relays/REVIEW_81_CHAT1.md"), "the SM seat": ("400259cda", "relays/REVIEW_81_SM.md")}
def found(s):
    r = subprocess.run(["git", "grep", "-F", "-l", "-e", s, REV, "--"], capture_output=True, text=True)
    return r.returncode == 0
out = {}
for who, (rev, path) in FILES.items():
    text = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True, check=True).stdout
    qs = []
    for line in text.splitlines():
        segs = line.replace("\\|", "|").split('"')
        qs += [segs[k] for k in range(1, len(segs) - 1, 2) if len(segs[k]) >= 15]
    ok, miss = 0, []
    for q in qs:
        pieces = [p for p in re.split(r"…|\.\.\.", q) if len(p.strip()) >= 8]
        if pieces and all(found(p.strip()) for p in pieces):
            ok += 1
        else:
            miss.append(q[:100])
    out[who] = (ok, len(qs), miss)
    print(f"{who}: {ok} of {len(qs)} quotations found verbatim at {REV}" + (f"; not found: {miss}" if miss else ""))
