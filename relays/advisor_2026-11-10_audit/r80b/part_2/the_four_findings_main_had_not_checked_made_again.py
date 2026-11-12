#!/usr/bin/env python3
"""The four findings of part 2 that main's table gives as not checked, each made again on the tree before the part.

    python3 the_four_findings_main_had_not_checked_made_again.py <a checkout of the commit before part 2>

It reads files and counts; it changes nothing.  The findings are the SM seat's 22, 25 and 30 and a reader's F9, as main's
table of the 57 gives them."""
import itertools, json, pathlib, re, sys
root = pathlib.Path(sys.argv[1])
F = root / "frontier"
b81 = next(F.glob("B1881_*")); b95 = next(F.glob("B1895_*")); b97 = next(F.glob("B1897_*"))

print("1. The SM seat's 22: B1895's lock says its sequences are ones the arc's script did not try")
seqs = [q for q in itertools.product(range(1, 13), repeat=2)] + [q for q in itertools.product(range(1, 5), repeat=4)]
seqs += [(2,) * n for n in (2, 4, 6, 8, 10)] + [(2,) + (1,) * (n - 1) for n in (2, 4, 6, 8, 10)] + [(1,) * n for n in (2, 4, 6, 8, 10)]
tried = {q for n, top in ((2, 6), (4, 6), (6, 3)) for q in itertools.product(range(1, top + 1), repeat=n)}
d = set(seqs)
print("   the lock's sequences, as its test lists them: %d, distinct %d; the script's: %d" % (len(seqs), len(d), len(tried)))
print("   of the distinct ones, tried by the script: %d; new: %d (of length 2 with a run of 7 to 12: %d; of length 8 and 10: %d)"
      % (len(d & tried), len(d - tried), sum(1 for q in d - tried if len(q) == 2), sum(1 for q in d - tried if len(q) > 6)))
lock = (b95 / "verification" / "test_b1895_the_mends_of_b1881_read.py").read_text(encoding="utf-8")
print("   the lock's sentence stands: %s" % ("on sequences the arc's script did not try: length 2 with runs to 12, length 4 with" in lock))

print("2. The SM seat's 25: two things owed with no open row")
reg = (root / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8").split("\n")
row = [l for l in reg if l.startswith("| P-822 |")][0]
cells = [c.strip() for c in row.strip("|").split("|")]
print("   P-822 reads %s; its cell of what was done ends: ...%s" % (cells[4], cells[5][-48:]))
page = (b97 / "FINDINGS.md").read_text(encoding="utf-8")
print("   B1897 section 5 still asks it: %s" % ("**The reader's own 23 against the new lock.** It is asked to run them." in page))
print("   B1897 section 4 states the debt: %s" % ("Most of main's\n  locks do not, and the ones whose scripts take minutes cannot in the default lane." in page))
rows = [l for l in reg if re.match(r"\| P-\d+ \|", l)]
hold = [l.split("|")[1].strip() for l in rows if "QUEUED" in l.split("|")[5] and re.search(r"hold[s]? (a|the) committed output|committed output and not", l)]
print("   open register rows that carry that debt: %s" % (hold or "none"))

print("3. The SM seat's 30: the first section of B1881 lists the agreement of the two conventions as a thing main adds")
p81 = (b81 / "FINDINGS.md").read_text(encoding="utf-8")
i = p81.index("- **Main adds three things.**"); j = p81.index("- **Nothing is selected.**")
bullet = p81[i:j]
print("   the bullet names it: %s; it has a bracket: %s" % ("name\n  one allowed set (§ 5)" in bullet, "[" in bullet))
print("   section 5 calls the agreement an instance of an identity: %s" % ("The agreement on 47,988 sequences is an instance of an identity." in p81))
p95 = (b95 / "FINDINGS.md").read_text(encoding="utf-8")
print("   B1895 section 6 counts it among main's errors: %s" % ("**It did not see the identity.** B1881 reported an agreement that had to hold as if it were a finding." in p95))

print("4. A reader's F9: B1895's lock reads a verdict file as one block")
olds = ("is its transpose and is this arc's own", "the columns are the transpose that B1881 used", "the transpose of B1872's rows", "the second one compared here is the transpose",
        "the columns are named as the transpose", "the transpose, which B1881 used")
marks = ("not the transpose", "CORRECTED AGAIN", "CORRECTED 2026-11-12, a second time", "this label read")
print("   the lock reads a json file as one block: %s" % ('blocks = [text] if f.endswith(".json") else text.split("\\n\\n")' in lock))
v = json.loads((b81 / "arc_verdict.json").read_text(encoding="utf-8"))
reported = lambda t: any(o in t for o in olds) and not any(m in t for m in marks)
print("   B1881's verdict file as it is: holds the old words %d time(s); reported: %s" % (sum(json.dumps(v, ensure_ascii=False).count(o) for o in olds), reported(json.dumps(v, ensure_ascii=False))))
planted = dict(v, scope=dict(v["scope"], hypotheses=v["scope"]["hypotheses"] + "; the columns are the transpose that B1881 used"))
t = json.dumps(planted, indent=1, ensure_ascii=False)
print("   with the old words a second time, uncorrected, in another field: holds them %d times; reported: %s" % (sum(t.count(o) for o in olds), reported(t)))
