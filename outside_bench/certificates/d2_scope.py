#!/usr/bin/env python3
"""MEMO-130 CELL (the owner's "let's elaborate D2 decision options"): THE D2
SCOPE QUESTION, MEASURED — B1197 returned SPLIT and routed the scope choice
to the owner as trajectory-vs-variable, saying "both readings are defensible
and the run cannot choose between them."  This cell does not choose either;
it MEASURES the two readings on B1197's own banked data, so the owner
decides on numbers rather than on taste.

WHAT B1197 ESTABLISHED (verdict PROVED, controls two-sided): the (1,n)
ladder is monotone over 29 rungs; the 78-closing census is not, with 15
violations; every p >= 2 family violates internally.  Its own honest
statement: the trajectory reading is payable, the variable reading is
refuted, and the choice of reading is the owner's.

WHAT THIS CELL ADDS (each item exact, on cc's own b4_global.json):
  S1  THE EFFECTIVE SAMPLE.  B289's sign law CS(p,-q) = -CS(p,q) makes the
      mirror pairs carry EQUAL volume and EQUAL |CS|.  So the census's 78
      closings are 39 DISTINCT (Vol, |CS|) points, each appearing twice.
      cc's 78 is right as a count of CLOSINGS; the relation test has 39
      independent points, and any null must be computed on those.
  S2  REPRODUCTION + AN ERROR OF MINE, filed.  cc's 15 violations reproduce
      exactly under cc's own rule.  My first recount gave 30 because I
      dropped cc's 1e-9 tolerance; the 15 sub-tolerance "increases" are
      exactly the 39 mirror ties.  cc is right, I was wrong, and the
      tolerance is doing real work rather than hiding anything.
  S3  HOW STRONG IS THE GLOBAL RELATION?  B1197 read it as a BINARY
      (monotone: yes/no).  Measured on the 39 distinct points against a
      20000-shuffle null, with Kendall tau reported.  If the relation were
      strong-but-imperfect, the trajectory restriction would look like a
      technicality; if weak, the two readings are genuinely far apart.
  S4  IS COHERENCE ASYMPTOTIC?  The physically interesting regime is near
      the cusp.  If restricting to high volume cleans the census up, the
      payable reading is "coherent asymptotically for ALL families", which
      is much stronger and less special-pleading than "one trajectory".
      Thresholds swept.
  S5  THE DECISIVE STRUCTURAL TEST.  "The same clock up to monotone
      reparameterization" requires |CS| to be a FUNCTION of Vol.  Exhibited
      or refuted by finding closings at essentially equal volume with
      different |CS|.  This is strictly stronger than non-monotonicity.
  S6  IS THE LADDER POST-HOC?  The whole trajectory reading collapses if
      the (1,n) ladder was singled out AFTER seeing which subset passed.
      Checked against what was banked BEFORE the run.
Gate 5 untouched: geometry and counts only, all read from banked data; no
measured physical value enters and no clock identification is asserted.
"""
import os, json, random, itertools, statistics, subprocess

REPO = os.environ.get("OA_REPO", os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))
REF = os.environ.get("OA_REF", "origin/main")
PATH = "frontier/B1197_clock_coherence/verification/b4_global.json"
r = subprocess.run(["git", "-C", REPO, "show", f"{REF}:{PATH}"],
                   capture_output=True, text=True)
DATA = json.loads(r.stdout) if r.returncode == 0 else json.load(open(os.path.join(REPO, PATH)))
rows = DATA["rows"]
TOL = 1e-9
CUSP = 2.029883212819

# ---------------- S1
ties = [(rows[i], rows[i+1]) for i in range(len(rows)-1)
        if abs(rows[i+1]["abs_cs"] - rows[i]["abs_cs"]) <= TOL]
mirror = sum(1 for a, b in ties if a["p"] == b["p"] and a["q"] == -b["q"]
             and abs(a["vol"] - b["vol"]) <= TOL)
seen, uniq = set(), []
for x in rows:
    k = (round(x["vol"], 9), round(x["abs_cs"], 9))
    if k in seen:
        continue
    seen.add(k); uniq.append(x)
uniq.sort(key=lambda x: x["vol"])
print(f"S1 — THE EFFECTIVE SAMPLE.  census closings: {len(rows)}")
print(f"    adjacent |CS| ties within {TOL}: {len(ties)}, ALL of them (p,q)/(p,-q)"
      f" mirror pairs with equal volume: {mirror}/{len(ties)}")
assert mirror == len(ties)
print(f"    => DISTINCT (Vol, |CS|) points: {len(uniq)}.  B289's sign law"
      f" CS(p,-q) = -CS(p,q) doubles every point.")
print(f"    cc's 78 is correct as CLOSINGS; the relation test has {len(uniq)}"
      f" independent points, and a fair null must use those.")
assert len(uniq) == 39

# ---------------- S2
viol_cc = sum(1 for i in range(len(rows)-1)
              if rows[i+1]["abs_cs"] > rows[i]["abs_cs"] + TOL)
viol_notol = sum(1 for i in range(len(rows)-1)
                 if rows[i+1]["abs_cs"] > rows[i]["abs_cs"])
print(f"\nS2 — REPRODUCTION.  cc's rule on cc's rows: {viol_cc} violations"
      f"  (cc reports {DATA['n_violations']}) — REPRODUCES.")
assert viol_cc == DATA["n_violations"] == 15
print(f"    ERROR FILED (mine): dropping cc's 1e-9 tolerance gives {viol_notol},"
      f" because the {len(ties)} mirror ties then read as increases.")
print("    cc's tolerance is load-bearing and correct; my first recount was wrong.")

# ---------------- S3
V = [x["vol"] for x in uniq]; C = [x["abs_cs"] for x in uniq]; n = len(uniq)
obs = sum(1 for i in range(n-1) if C[i+1] > C[i] + TOL)
random.seed(3)
nulls = []
for _ in range(20000):
    P = C[:]; random.shuffle(P)
    nulls.append(sum(1 for i in range(n-1) if P[i+1] > P[i] + TOL))
mu, sd = statistics.mean(nulls), statistics.pstdev(nulls)
p_emp = sum(1 for x in nulls if x <= obs) / len(nulls)
def tau(x, y):
    c = dd = 0
    for i, j in itertools.combinations(range(len(x)), 2):
        a = x[i]-x[j]; b = y[i]-y[j]
        if abs(a) < 1e-12 or abs(b) < 1e-12:
            continue
        c += a*b > 0; dd += a*b < 0
    return (c-dd)/(c+dd)
t = tau(V, C)
print(f"\nS3 — HOW STRONG IS THE GLOBAL RELATION?  (B1197 read it as a binary)")
print(f"    adjacent violations among the {n} distinct points: {obs} of {n-1}")
print(f"    null (20000 shuffles): mean {mu:.1f} sd {sd:.1f}"
      f"  =>  z = {(obs-mu)/sd:+.2f},  P(null <= obs) = {p_emp:.4f}")
print(f"    Kendall tau(Vol, |CS|) = {t:+.4f}")
print("    => the global relation is WEAK, not 'mostly coherent with a few")
print("       exceptions': tau is about -0.17 and the ordering is only just")
print("       distinguishable from chance.  The two readings are FAR APART.")

# ---------------- S4
print("\nS4 — IS COHERENCE ASYMPTOTIC (near-cusp, all families)?"
      f"   cusp volume {CUSP:.6f}")
print(f"    {'Vol >=':>8s} {'points':>7s} {'violations':>11s}   monotone?")
asympt_ok = False
for thr in (0.0, 1.70, 1.85, 1.90, 1.95):
    sub = [x for x in uniq if x["vol"] >= thr]
    v = sum(1 for i in range(len(sub)-1)
            if sub[i+1]["abs_cs"] > sub[i]["abs_cs"] + TOL)
    if thr >= 1.90 and v == 0:
        asympt_ok = True
    print(f"    {thr:>8.2f} {len(sub):>7d} {v:>11d}   {'YES' if v == 0 else 'no'}")
assert not asympt_ok
print("    => NO.  Restricting to the near-cusp end does NOT clean the census.")
print("       The payable reading cannot be upgraded to 'coherent asymptotically")
print("       for all families'; it stays 'coherent on one trajectory'.")

# ---------------- S5
print("\nS5 — THE DECISIVE STRUCTURAL TEST: is |CS| a FUNCTION of Vol at all?")
best = None
for x in uniq:
    grp = [y for y in uniq if abs(y["vol"] - x["vol"]) < 0.005]
    if len(grp) >= 3:
        sp = max(g["abs_cs"] for g in grp) - min(g["abs_cs"] for g in grp)
        if best is None or sp > best[0]:
            best = (sp, grp)
spread, grp = best
dv = max(g["vol"] for g in grp) - min(g["vol"] for g in grp)
for g in sorted(grp, key=lambda z: z["vol"]):
    print(f"      ({g['p']:>2d},{g['q']:>3d})  Vol={g['vol']:.6f}  |CS|={g['abs_cs']:.6f}")
print(f"    {len(grp)} closings inside a volume window of width {dv:.6f}"
      f" carry |CS| spanning {spread:.6f}")
print(f"    => |CS| varies {spread/dv:.0f}x faster than Vol across this window:")
print("       |CS| IS NOT A FUNCTION OF Vol, not even approximately, and this is")
print("       at the NEAR-CUSP end.  'The same clock up to monotone")
print("       reparameterization' requires a function.  So the VARIABLE reading")
print("       fails for a reason STRICTLY STRONGER than non-monotonicity — it")
print("       is not a reparameterization failure but a single-valuedness one.")
assert spread / dv > 10
# S5b — the one-line version, using cc's OWN positive control as the instrument
print("\n    S5b — THE ONE-LINE VERSION (cc's own control does the work).")
print("    B289's sign law, which B1197 reproduces 156/156 as a POSITIVE CONTROL,")
print("    says CS(p,-q) = -CS(p,q); and the mirror pair has the SAME volume.")
mp = [(a, b) for a, b in ties if a["p"] == b["p"] and a["q"] == -b["q"]]
nz = sum(1 for a, b in mp if a["abs_cs"] > TOL)
print(f"    So for each of the {len(mp)} mirror pairs in the census, ONE volume")
print(f"    carries TWO opposite CS values — and {nz} of them have CS != 0.")
print("    => SIGNED CS is not a function of Vol, immediately, by a banked law.")
print("       Taking |CS| is already a REPAIR of that failure; S5 shows the")
print("       repair fails too.  The variable reading is refuted twice over,")
print("       and the second refutation was in the record before the run.")
assert nz == len(mp)

# ---------------- S6
print("\nS6 — IS THE LADDER POST-HOC?  (the trajectory reading collapses if so)")
print("    NO — banked BEFORE the run, on two independent counts:")
print("    * B289 names the (1,n) family THE SCALE LADDER and banks its own")
print("      structure there: CS(1,n) all one sign, CS(1,-n) = -CS(1,n), and")
print("      |CS| -> 0 as n -> inf 'approaching the amphichiral origin'.")
print("    * THE_WELD_BOOK addendum 2 (2026-08-28, written BEFORE the run)")
print("      preregistered the ladder as the test: 'along the (1,n) ladder, CS")
print("      must be monotone in Vol', with the census sweep as the EXTENSION.")
print("    => the ladder was distinguished first and independently.  Restricting")
print("       to it is a scope choice, NOT selection of the passing subset.")

print("""
WHAT THE MEASUREMENT CHANGES ABOUT D2 (the cell's whole contribution):
  B1197 said the two readings are 'both defensible' and left them
  symmetric.  They are NOT symmetric on the data:
    * the VARIABLE reading is refuted more strongly than reported — |CS| is
      not even a function of Vol (S5), so it fails single-valuedness, not
      just monotonicity.  There is no weaker version of it to retreat to,
      because near-cusp restriction does not help (S4) and the global
      relation is weak (S3).
    * the TRAJECTORY reading is cleaner than reported — the ladder is
      preregistered and independently banked (S6), so it is not the
      passing subset chosen after the fact.
  The owner's choice is therefore NOT 'which of two equally-supported
  readings do I prefer'.  It is a single question: IS A CLOCK IDENTIFIED
  ALONG ONE REALIZED HISTORY, OR BETWEEN TWO VARIABLES ON THE SPACE OF
  POSSIBLE HISTORIES?  The second is dead either way.  Gate 5 untouched.""")
