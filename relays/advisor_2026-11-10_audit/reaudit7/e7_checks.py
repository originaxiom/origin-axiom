#!/usr/bin/env python3
"""Re-audit 7, the finding E7: main's mend of the freedom ledger (B1028), at b99bf8a2b.

The acceptance row: the verdict is not PROVED; the unpriced row and the embedding choice are in the claim line; one
endpoint is credited and named.

Everything runs in a SCRATCH CLONE of main, never in the working tree.

    python3 e7_checks.py --repo REPO --ref origin/main --work DIR        (DIR outside the repository)

SEEN BEFORE THIS FILE WAS WRITTEN, so not blind (read on main while deciding what to check): the verdict is OPEN; the
claim line begins with the correction and keeps the claim as first asserted after it; the generated spine's line for
B1028 begins with the correction; three arcs list B1028 among what they depend on (B1030, B1643, B1858).

EXPECTATIONS, written before the first run.
 A. the facts the correction states
  a1  the walk's source types the price 0.0 eleven times and no price is anything else
  a2  the walk, run as it stands, still exits 0 and still prints 0.000: the fault is in the script as it was run
  a3  B997's claim line holds both the phrase the walk matches and its correction ("the door set is {1, 4}"), and the
      walk's citation check passes on it
  a4  the claim line names the three unpriced choices, and one endpoint: the algebra of dimension 14
 B. a wider sweep than the lock's (READ-OUT, no expectation): every tracked text file, of any kind, that states the zero
    and neither carries the correction nor is one of the lock's records of what was said at the time
 C. planted cases against the lock, tests/test_b1028_freedom_ledger.py.  "caught" = the lock fails
  c0  nothing planted                                                                    passes (control)
  r1  the verdict set back to PROVED                                                     caught
  r2  the correction removed from the claim line                                         caught
  r3  a new page under docs/: "B1028: 0.000 bits of designer freedom, machine-checked."  caught
  r4  the same statement over two lines                                                  not caught
  r5  "the freedom ledger (B1028) shows that the chain has no designer freedom at all"   not caught
  r6  r3's sentence in a new .tex file under papers/                                     not caught
  r7  r3's sentence appended to the README at the root                                   caught (this lock reads five
      pages at the root, which the lock of E2 did not)
  r8  the correction removed from a page that carries it (docs/THE_CLAIM.md)             caught
  r9  one of the eleven prices typed 1.0 in the walk                                     caught
  r10 a new arc_verdict.json whose claim line is r3's sentence                           not caught
"""
import sys, os, re, json, shutil, subprocess

repo = os.path.abspath(sys.argv[sys.argv.index("--repo") + 1])
ref = sys.argv[sys.argv.index("--ref") + 1]
work = os.path.abspath(sys.argv[sys.argv.index("--work") + 1])
LOCK = "tests/test_b1028_freedom_ledger.py"
ARC = "frontier/B1028_freedom_ledger"
MARK = "the freedom ledger's zero is not a computed quantity"
SENTENCE = "B1028: 0.000 bits of designer freedom, machine-checked.\n"
HISTORY = ("PROGRESS_LOG.md", "CHANGELOG.md", "docs/CAMPAIGN_STATUS.md", "docs/progress/", "docs/handoffs/", "docs/views/", "docs/THE_WHY_CAMPAIGN.md", "docs/CROSSING_REQUIREMENTS.md",
           "docs/FIELD_EXPLORATION_REPORT.md", "docs/GRAND_COMPUTATION_v0.md", "docs/THE_FINAL_ACTS_BAR_2026-10-29.md", "frontier/B1015_", "frontier/B1128_", "frontier/B1349_",
           "frontier/B1861_", "frontier/B1870_", "frontier/B1028_freedom_ledger/ADDENDUM", "frontier/B1028_freedom_ledger/PREREGISTRATION")      # the lock's own list


def sh(args, cwd=None, check=True, env=None):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, env=env)
    if check and r.returncode != 0:
        sys.exit("failed: %s\n%s" % (" ".join(args)[:160], r.stderr[:300]))
    return r


if os.path.exists(work):
    shutil.rmtree(work)
sh(["git", "clone", "-q", "--no-checkout", "file://" + repo, work])
sha = sh(["git", "-C", repo, "rev-parse", ref]).stdout.strip()
sh(["git", "-C", work, "fetch", "-q", "file://" + repo, sha])
sh(["git", "-C", work, "checkout", "-q", "--detach", sha])
print("re-audit of the finding E7 at main %s" % sha[:9], flush=True)
path = lambda rel: os.path.join(work, rel)
read = lambda rel: open(path(rel), encoding="utf-8", errors="replace").read()


def write(rel, text, mode="w"):
    os.makedirs(os.path.dirname(path(rel)), exist_ok=True)
    with open(path(rel), mode, encoding="utf-8") as fh:
        fh.write(text)


def reset():
    sh(["git", "-C", work, "checkout", "-q", "--", "."]); sh(["git", "-C", work, "clean", "-q", "-fd"])


held, total = 0, 0


def line(tag, ok, text):
    global held, total
    total += 1; held += bool(ok)
    print("%-4s %-6s %s" % (tag, "HOLDS" if ok else "FAILS", text), flush=True)


# ---- A
src = read(ARC + "/b1028_walk.py")
prices = re.findall(r"price\s*=\s*([-+0-9.eE]+)", src)
line("a1", prices.count("0.0") == 11 and all(p == "0.0" for p in prices), "prices typed in the walk's source: %d, of which 0.0: %d" % (len(prices), prices.count("0.0")))
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
r = subprocess.run([sys.executable, "-B", path(ARC + "/b1028_walk.py")], cwd=work, capture_output=True, text=True, env=env)
zero_lines = [l.strip() for l in r.stdout.splitlines() if "0.000" in l]
line("a2", r.returncode == 0 and bool(zero_lines), "the walk as it stands: exit %d; lines that print 0.000: %d%s" % (r.returncode, len(zero_lines), (" -- e.g. \"" + zero_lines[0][:110] + "\"") if zero_lines else ""))
dirty = sh(["git", "-C", work, "status", "--short"]).stdout.strip()
print("     tracked files the walk changed by running: %s" % (dirty.replace("\n", "; ") if dirty else "none"))
reset()
b997 = json.loads(read("frontier/B997_golden_conductor_uniqueness/arc_verdict.json"))["claim_one_line"]
code = ("import importlib.util, sys; s = importlib.util.spec_from_file_location('w', %r); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); "
        "print(m._cite('B997_golden_conductor_uniqueness', 'UNIQUE METALLIC GRAMMAR', 'INFINITE FAMILY'))" % path(ARC + "/b1028_walk.py"))
rc = subprocess.run([sys.executable, "-B", "-c", code], cwd=work, capture_output=True, text=True, env=env)
line("a3", "UNIQUE METALLIC GRAMMAR" in b997 and "the door set is {1, 4}" in b997 and rc.returncode == 0 and rc.stdout.strip().endswith("B997"),
     "B997's line holds the matched phrase: %s; its correction: %s; the walk's check on it: %s" % ("UNIQUE METALLIC GRAMMAR" in b997, "the door set is {1, 4}" in b997, "passes" if rc.returncode == 0 else "fails"))
v = json.loads(read(ARC + "/arc_verdict.json")); c = v["claim_one_line"]
head = c.split("ORIGINAL CLAIM AS ASSERTED")[0]
need = {"the family declaration": "the family declaration" in head, "the selection within the family": "selection within the family" in head,
        "the principal embedding": "principal embedding" in head, "one endpoint, of dimension 14": "THE ONE ENDPOINT IT CREDITS is the algebra of dimension 14" in head}
line("a4", v["verdict"] != "PROVED" and all(need.values()), "verdict %s; in the correction, before the claim as first asserted: %s" % (v["verdict"], "; ".join("%s: %s" % (k, "yes" if ok else "NO") for k, ok in need.items())))
reset()

# ---- B
print()
wide = re.compile(r"0\.000\s*bits|zero (?:retroactive )?(?:designer )?freedom|no (?:retroactive )?designer freedom|designer freedom (?:is|=|of) (?:zero|0)\b|RETROACTIVE DESIGNER FREEDOM = 0", re.I)
about = re.compile(r"designer|freedom ledger|B1028", re.I)
tracked = sh(["git", "-C", work, "ls-files"]).stdout.splitlines()
kinds = (".md", ".tex", ".json", ".py", ".txt", ".bib", ".yaml", ".yml", ".html")
n_hist = n_carried = 0; loose = []
for rel in tracked:
    if not rel.endswith(kinds):
        continue
    try:
        if os.path.getsize(path(rel)) > 5_000_000:
            continue
        text = read(rel)
    except Exception:
        continue
    hits = [l for l in text.splitlines() if wide.search(l) and about.search(l)]
    if not hits:
        continue
    if any(rel.startswith(h) or h in rel for h in HISTORY):
        n_hist += 1
    elif MARK.lower() in text.lower():
        n_carried += 1
    else:
        loose.append((rel, len(hits), hits[0].strip()[:150]))
print("B    read-out: tracked text files that state the zero: %d under the lock's records of what was said at the time; %d that carry the correction; %d that do neither:" % (n_hist, n_carried, len(loose)))
for rel, n, first in sorted(loose)[:40]:
    print("       %s  (%d line%s)  %s" % (rel, n, "" if n == 1 else "s", first))
print()

# ---- C
def run_lock():
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", LOCK], cwd=work, capture_output=True, text=True, env=env)
    return r.returncode != 0, sorted(set(re.findall(r"^FAILED \S+::(\S+)", r.stdout, re.M)))


def r1():
    j = json.loads(read(ARC + "/arc_verdict.json")); j["verdict"] = "PROVED"
    write(ARC + "/arc_verdict.json", json.dumps(j, ensure_ascii=False, indent=1) + "\n")


def r2():
    j = json.loads(read(ARC + "/arc_verdict.json"))
    j["claim_one_line"] = j["claim_one_line"].split("ORIGINAL CLAIM AS ASSERTED: ", 1)[1]
    write(ARC + "/arc_verdict.json", json.dumps(j, ensure_ascii=False, indent=1) + "\n")


def r8():
    text = read("docs/THE_CLAIM.md"); assert MARK.lower() in text.lower()
    write("docs/THE_CLAIM.md", "\n".join(l for l in text.splitlines() if MARK.lower() not in l.lower()) + "\n")


def r9():
    text = read(ARC + "/b1028_walk.py"); assert text.count("price=0.0") == 11
    write(ARC + "/b1028_walk.py", text.replace("price=0.0", "price=1.0", 1))


CASES = [
    ("c0", "nothing planted", lambda: None, False),
    ("r1", "the verdict set back to PROVED", r1, True),
    ("r2", "the correction removed from the claim line", r2, True),
    ("r3", "a new page under docs/ states the zero", lambda: write("docs/PLANTED_PAGE.md", "# A planted page\n\n" + SENTENCE), True),
    ("r4", "the same statement over two lines", lambda: write("docs/PLANTED_PAGE.md", "# A planted page\n\nB1028: the designer freedom of the whole chain, machine-checked,\nis 0.000 bits.\n"), False),
    ("r5", "\"no designer freedom at all\"", lambda: write("docs/PLANTED_PAGE.md", "# A planted page\n\nThe freedom ledger (B1028) shows that the chain has no designer freedom at all.\n"), False),
    ("r6", "r3's sentence in a new .tex file under papers/", lambda: write("papers/planted/planted.tex", "\\section{Planted}\n" + SENTENCE), False),
    ("r7", "r3's sentence appended to the root README", lambda: write("README.md", "\n" + SENTENCE, "a"), True),
    ("r8", "the correction removed from docs/THE_CLAIM.md", r8, True),
    ("r9", "one of the eleven prices typed 1.0 in the walk", r9, True),
    ("r10", "a new arc_verdict.json whose claim line states the zero", lambda: write("frontier/B99998_planted/arc_verdict.json", json.dumps({"id": "B99998", "verdict": "PROVED", "claim_one_line": SENTENCE.strip()}) + "\n"), False),
]
for tag, what, plant, expect_caught in CASES:
    reset(); plant()
    caught, failed = run_lock()
    line(tag, caught == expect_caught, "%-11s expected %-11s %s%s" % ("CAUGHT" if caught else "NOT CAUGHT", "caught" if expect_caught else "not caught", what, ("  [red: " + ", ".join(failed) + "]") if failed else ""))
reset()
print()
print("expectations that hold: %d of %d" % (held, total))
