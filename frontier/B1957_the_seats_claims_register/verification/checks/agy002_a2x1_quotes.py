"""agy-002's A2-X1 note (its branch agy-002/verify at 55f72ee3f), section 1: each source it quotes, at the commit, file and
lines it names, read by main; every quoted line is looked for in the file at that commit within the named lines (a quoted
line counts when it equals a line there, or is part of one, after trimming the indent). The two cited commits of the
physical lane and the one of the SM seat are looked for on those seats' branches. Nothing of the seat's is run."""
import re, subprocess
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True)
NOTE = "relays/AGY002_TO_CC_2026-11-18_M47_M48_A2_X1_D1_HIGGS_CROSS_READ_AND_SM_C21.md"
text = git("show", "55f72ee3f:" + NOTE).stdout.split("\n")
start = next(i for i, l in enumerate(text) if l.startswith("## 1.")); stop = next(i for i, l in enumerate(text) if l.startswith("## 2."))
cites = []; i = start
while i < stop:
    m = re.match(r"\s*- `([0-9a-f]{9}):([^:`]+):([0-9, -]+)`", text[i])
    if m:
        rng = []
        for part in m.group(3).split(","):
            a, _, b = part.strip().partition("-"); rng.append((int(a), int(b or a)))
        blocks = []; j = i + 1
        while j < stop and not re.match(r"\s*- `[0-9a-f]{9}:", text[j]) and not re.match(r"\s*- \*\*", text[j]) and not text[j].startswith("### "):
            if text[j].strip().startswith("```text"):
                k = j + 1
                while not text[k].strip().startswith("```"): blocks.append(text[k]); k += 1
                j = k
            j += 1
        cites.append((i + 1, m.group(1), m.group(2), rng, blocks)); i = j
    else: i += 1
bad = []; total = 0
for ln, c, path, rng, blocks in cites:
    src = git("show", "%s:%s" % (c, path)).stdout.split("\n")
    window = [src[k - 1] for a, b in rng for k in range(a, b + 1) if 0 < k <= len(src)]
    for q in blocks:
        if not q.strip(): continue
        total += 1
        if not any(q.strip() == w.strip() or q.strip() in w for w in window): bad.append((ln, c, path, q.strip()[:60]))
print("Q1: %d citations with quoted text in the note's section 1; %d quoted lines; not found at the commit, file and lines named: %d %s" % (len(cites), total, len(bad), bad[:5]))
on = {}
for c, who in (("a69cee901", "the SM seat's branch"), ("a47e76da6", "the physical lane's branch"), ("aa9facef6", "the physical lane's branch")):
    refs = git("branch", "-r", "--contains", c).stdout.split()
    on[c] = (who, bool(refs))
print("Q2: the other seats' commits it reads at are on their branches: %s" % on)
# Q3: the seat's two manifests against the files they name at 55f72ee3f, and the commit at which each file last changed
import hashlib
man = {}
for mf in ("relays/a2_x1/SCRIPT_SHA256.txt", "relays/a2_x1/OUTPUT_SHA256.txt"):
    for l in git("show", "55f72ee3f:" + mf).stdout.split("\n"):
        if l.strip(): h, p = l.split(); man[p] = h
ok = {p: hashlib.sha256(subprocess.run(["git", "show", "55f72ee3f:" + p], capture_output=True).stdout).hexdigest() == h for p, h in man.items()}
last = {p: git("log", "--format=%h", "-1", "55f72ee3f", "--", p).stdout.strip() for p in man}
print("Q3: the manifests name %d files; each matches its hash at 55f72ee3f: %s; the commit at which each last changed: %s" % (len(man), ok, last))
