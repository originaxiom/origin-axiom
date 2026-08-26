"""B8143 step 3 -- verify the 13-state competitor exactly, and tighten the chirality test.

Step 2 found FOUR rigid+chiral 5-field contents. Two of them (AAACD, AAABC) came through a
chirality test that was too weak -- it only demanded that SOME (3,2) be charged, so contents
with a NEUTRAL (3,2) and neutral singlets passed. Those are sterile-field contents, not
competitors. Tightened here: EVERY field must carry nonzero charge.

The one that survives properly is ABCDD at 13 states -- smaller than the SM's 15.
"""
import itertools
import sympy as sp
from fractions import Fraction as F

ST = {"A": 6, "B": 3, "C": 2, "D": 1}
TRI = {"A": 2, "B": 1, "C": 0, "D": 0}
DBL = {"A": 3, "B": 0, "C": 1, "D": 0}

FAIL = []
def check(n, ok, d=""):
    print(("  PASS  " if ok else "  FAIL  ") + n + (("   " + d) if d else ""))
    if not ok: FAIL.append(n)


def anom(content, ys):
    return [sum(TRI[r]*y for r, y in zip(content, ys)),
            sum(DBL[r]*y for r, y in zip(content, ys)),
            sum(ST[r]*y for r, y in zip(content, ys)),
            sum(ST[r]*y**3 for r, y in zip(content, ys))]


print("A  the SM generation, as a control")
sm = ("A", "B", "B", "C", "D")
smY = [F(1,6), F(-2,3), F(1,3), F(-1,2), F(1)]
res = anom(sm, smY)
check("SM (1/6,-2/3,1/3,-1/2,1) satisfies all four anomaly conditions",
      all(r == 0 for r in res), str(res))

print("\nB  the 13-state competitor  ABCDD")
comp = ("A", "B", "C", "D", "D")
compY = [F(1,2), F(-1), F(-3,2), F(2), F(1)]
res = anom(comp, compY)
check("ABCDD (1/2,-1,-3/2,2,1) satisfies all four anomaly conditions",
      all(r == 0 for r in res), str(res))
check("it has 13 states, FEWER than the SM's 15",
      sum(ST[r] for r in comp) == 13 and sum(ST[r] for r in sm) == 15,
      "%d vs %d" % (sum(ST[r] for r in comp), sum(ST[r] for r in sm)))
check("every field carries NONZERO charge (no sterile field)", all(y != 0 for y in compY))
check("Witten global anomaly: doublet count is even",
      sum(DBL[r] for r in comp) % 2 == 0, "%d doublets" % sum(DBL[r] for r in comp))

print("\nC  is it RIGID -- isolated up to scale, like the SM?")
Y = sp.symbols("Y0:5")
sols = sp.solve(anom(comp, list(Y)), list(Y), dict=True)
iso = []
for s in sols:
    vals = [sp.simplify(s.get(y, y)) for y in Y]
    fs = set()
    for v in vals: fs |= v.free_symbols
    free = [y for y in Y if y in fs]
    if len(free) == 1:
        c = [sp.nsimplify(sp.simplify(v.subs({free[0]: 1}))) for v in vals]
        if any(x != 0 for x in c): iso.append(tuple(c))
print("   isolated branches:", sorted({str(t) for t in iso}))
check("ABCDD's solution is isolated up to scale (rigid), like the SM's", len(set(map(str, iso))) >= 1)

print("\nD  re-run the census with the TIGHTENED chirality test (no sterile fields)")
rows = []
for content in itertools.combinations_with_replacement("ABCD", 5):
    if sum(DBL[r] for r in content) % 2: continue
    sols = sp.solve(anom(content, list(Y)), list(Y), dict=True)
    keep = []
    for s in sols:
        vals = [sp.simplify(s.get(y, y)) for y in Y]
        fs = set()
        for v in vals: fs |= v.free_symbols
        free = [y for y in Y if y in fs]
        if len(free) != 1: continue
        c = [sp.simplify(v.subs({free[0]: 1})) for v in vals]
        if any(x == 0 for x in c): continue           # TIGHTENED: no sterile field
        keep.append(tuple(sp.nsimplify(x) for x in c))
    if keep:
        rows.append((sum(ST[r] for r in content), "".join(content),
                     sorted({str(t) for t in keep})[0]))
rows.sort()
print("   states  content   example")
for t, c, ex in rows:
    tag = "   <-- the SM generation" if c == "ABBCD" else ""
    print("   %5d   %-7s  %s%s" % (t, c, ex, tag))
check("the SM is NOT the minimal rigid chiral content over this alphabet",
      rows and rows[0][1] != "ABBCD", "minimum is %s at %d states" % (rows[0][1], rows[0][0]) if rows else "")

print("\n%d/%d checks passed" % (7 - len(FAIL), 7))
