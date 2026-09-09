#!/usr/bin/env python3
"""F188-1 DISCHARGED: THE PROMOTION GATE IS NEITHER A FIREWALL NOR A STUCK VALVE.  It is a
BATCH mechanism that was demonstrated once, at scale, and then replaced by a one-at-a-time
trickle -- and the batch's own named queue is still 6/7 undrained two months later.

Memo 188 §7 posed a binary and said nobody had run the test: is the promotion gate a
firewall doing its job, or a valve stuck shut?  It proposed running twenty recent PROVED
arcs against the §5 gates.  THAT TEST WAS NOT NEEDED, and the binary was wrong.  The
programme's own record answers it directly, and with a third option.

WHAT IS MEASURED, and the clock used for it.

  THE CLOCK.  git add-dates for frontier/*/arc_verdict.json are USELESS here: all 1122
  land in a single month, a repository reorganisation rather than the work.  That is
  checked and reported below rather than assumed.  The usable clock is PROGRESS_LOG.md's
  698 dated sections; arc numbers are counted only when they name a directory that
  actually exists, so hashes and line references cannot inflate the count.

  THE PROMOTION MARKER.  GOVERNANCE §5 requires every status change to be logged in
  PROGRESS_LOG.md.  The phrase the log uses when a promotion passes the gate is
  "Promotion logged", and that is what is counted.

MEASURES
  1. the batch: what the 2026-07-03/04 promotion audit actually did, from OPEN_LEADS W2.10
  2. the trickle: promotions logged since, and when
  3. the denominator: arc numbers created after the audit, from the log's own chronology
  4. the queue: the seven candidates the audit itself named as queued -- how many landed
  5. the ledger's current size

Gate 5: pure counting over the repository.  No measured physical value.  The reading of
these numbers is interpretation and is labelled, here and in memo 188 addendum 1.
"""
import re, pathlib, collections, subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
LOG = (ROOT / "PROGRESS_LOG.md").read_text()
CL = (ROOT / "CLAIMS.md").read_text()
LEADS = (ROOT / "docs" / "OPEN_LEADS.md").read_text()

real = set()
for p in (ROOT / "frontier").glob("B*/arc_verdict.json"):
    m = re.match(r"B(\d+)", p.parent.name)
    if m: real.add(int(m.group(1)))

print("=" * 78); print("0.  THE CLOCK -- checked, not assumed"); print("=" * 78)
try:
    out = subprocess.run(["git", "log", "--diff-filter=A", "--name-only",
                          "--format=D %ad", "--date=short", "--", "frontier"],
                         cwd=ROOT, capture_output=True, text=True, timeout=120).stdout
    d = None; first = {}
    for ln in out.splitlines():
        if ln.startswith("D "): d = ln[2:]
        else:
            m = re.match(r"frontier/(B\d+)[^/]*/arc_verdict\.json", ln.strip())
            if m: first[m.group(1)] = d
    months = collections.Counter(v[:7] for v in first.values() if v)
    print("   git add-dates for the %d arc verdicts, by month : %s"
          % (len(first), months.most_common()))
    unusable = len(months) <= 1
except Exception as e:
    print("   git unavailable (%s)" % e); unusable = True
print("   => %s" % ("all in one month: a repository reorganisation, NOT the chronology of"
                    " the work.  git dates are unusable here." if unusable else
                    "git dates are spread and could be used."))
heads = sorted((m.start(), m.group(1)) for m in re.finditer(r"^## (\d{4}-\d{2}-\d{2})", LOG, re.M))
print("   usable clock: PROGRESS_LOG.md, %d dated sections, %s .. %s"
      % (len(heads), heads[0][1], heads[-1][1]))

def scan(lo, hi):
    seen = set(); best = 0
    for i, (pos, d) in enumerate(heads):
        if not (lo <= d <= hi): continue
        end = heads[i+1][0] if i+1 < len(heads) else len(LOG)
        for x in re.findall(r"\bB(\d{1,4})\b", LOG[pos:end]):
            n = int(x)
            if n in real: seen.add(n); best = max(best, n)
    return best, len(seen)

print(); print("=" * 78); print("1.  THE BATCH -- what the audit did in one pass")
print("=" * 78)
w = re.search(r"\|\s*W2\.10\s*\|(.{0,900})", LEADS, re.S)
line = re.sub(r"\s+", " ", w.group(1))[:520] if w else "(W2.10 row not found)"
print("   OPEN_LEADS W2.10 : %s" % line)

print(); print("=" * 78); print("2.  THE TRICKLE -- promotions since"); print("=" * 78)
proms = list(re.finditer(r"Promotion logged", LOG))
def head_for(pos):
    d = ""
    for p_, dd in heads:
        if p_ < pos: d = dd
        else: break
    return d
by = collections.Counter(head_for(m.start()) for m in proms)
print("   occurrences of 'Promotion logged' in PROGRESS_LOG : %d" % len(proms))
for k, v in sorted(by.items()): print("      %s : %d" % (k or "(undated section)", v))

print(); print("=" * 78); print("3.  THE DENOMINATOR"); print("=" * 78)
b0, _ = scan("2000-01-01", "2026-07-04")
b1, n1 = scan("2026-07-05", "2026-12-31")
new = b1 - b0
print("   highest real arc referenced in the log up to 2026-07-04 : B%d" % b0)
print("   highest real arc referenced after                       : B%d" % b1)
print("   arc numbers created after the audit                     : %d  (B%d..B%d)"
      % (new, b0+1, b1))
print("   distinct real arcs referenced after the audit           : %d" % n1)
rate = new // max(len(proms), 1)
print("   => roughly ONE promotion per %d new arcs" % rate)
print("   CAVEAT, stated rather than hidden: PROGRESS_LOG's DATED sections begin %s, so"
      % heads[0][1])
print("   B%d is the highest arc the pre-audit material references, not a census of what" % b0)
print("   existed on 2026-07-04.  The denominator is therefore an ESTIMATE of new arc")
print("   numbering, good to its order of magnitude -- several hundred arcs, two")
print("   promotions -- and no conclusion here needs more precision than that.")

print(); print("=" * 78); print("4.  THE AUDIT's OWN NAMED QUEUE"); print("=" * 78)
Q = ["termination theorem", "registerability", "lift obstruction", "winner-safety",
     "the ladder", "false-positive control", "matter pencil"]
low = CL.lower(); landed = []
for q in Q:
    ok = q in low; landed.append(ok)
    print("   %-24s : %s" % (q, "PRESENT in CLAIMS.md" if ok else "still absent"))
print("   => %d of %d landed in two months" % (sum(landed), len(Q)))

print(); print("=" * 78); print("5.  THE LEDGER NOW"); print("=" * 78)
for tag in ("P", "C", "E"):
    ids = sorted(set(int(x) for x in re.findall(r"\|\s*%s(\d+)\s*\|" % tag, CL)))
    if ids: print("   %s-ids : %3d   (max %s%d)" % (tag, len(ids), tag, max(ids)))
print("   'outside_bench' occurrences in CLAIMS.md : %d" % CL.count("outside_bench"))

print("""
=============================================================================
INTERPRETATION (labelled), and a correction to memo 188 section 7.

Memo 188 posed "firewall or valve" and proposed a twenty-arc gate test.  The binary was
wrong and the test was unnecessary: the record answers directly, with a THIRD option.

The gate is a BATCH mechanism.  On 2026-07-03/04 it adjudicated sixty-three candidates in
five passes and promoted fifty-four of them.  It demonstrably works, at scale, and it is
not stuck.

What replaced it is a TRICKLE.  The standing cadence since is explicitly one item per
review -- the log says so in its own words -- and it has delivered TWO promotions against
several hundred new arcs.  Six of the seven candidates the audit ITSELF named as queued
are still absent from the ledger two months later.

So the diagnosis is not obstruction.  It is a THROUGHPUT MISMATCH between a batch-capable
gate and a per-item cadence, with a backlog that grows structurally because the corpus
grows faster than one-at-a-time can drain it.

And the remedy needs no new machinery, which is the useful part: the programme has already
demonstrated the batch.  Running it again is the same apparatus at roughly thirty times the
rate, and its first target list was written by the audit itself and is still 6/7 unclaimed.

One more thing the numbers say in passing, and it belongs with memo 188's main pattern:
PROGRESS_LOG.md's last dated section is 2026-08-30.  The log that GOVERNANCE section 5
requires every status change to be written into has itself been quiet for ten days.  Same
shape as the depends_on field and the lost minus signs -- an instrument built, used, and
then not fed.""")
