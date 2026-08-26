"""B8143 step 4 -- the enumeration REDONE with the FULL anomaly set.

Steps 2-3 omitted the pure [SU(3)]^3 anomaly. That was a real error: it killed the
13-state "witness" those steps produced. Redone here with every condition.

Alphabet, all left-handed Weyl (this is the SM-visible alphabet, and it now includes the
(3,1) that the 27 actually contains):

  letter  rep        states  A3   triplets  doublets
  A       (3,2)        6     +2      2         3
  a       (3bar,2)     6     -2      2         3
  B       (3,1)        3     +1      1         0
  b       (3bar,1)     3     -1      1         0
  C       (1,2)        2      0      0         1
  D       (1,1)        1      0      0         0

Conditions:
  [SU(3)]^3     sum A3                        = 0     <-- OMITTED BEFORE
  [SU(3)]^2 Y   sum triplets * Y              = 0
  [SU(2)]^2 Y   sum doublets * Y              = 0
  grav^2 Y      sum states * Y                = 0
  [Y]^3         sum states * Y^3              = 0
  Witten        sum doublets                 even
"""
import itertools
import sympy as sp

REP = {
    "A": dict(st=6, a3=+2, tri=2, dbl=3),
    "a": dict(st=6, a3=-2, tri=2, dbl=3),
    "B": dict(st=3, a3=+1, tri=1, dbl=0),
    "b": dict(st=3, a3=-1, tri=1, dbl=0),
    "C": dict(st=2, a3=0,  tri=0, dbl=1),
    "D": dict(st=1, a3=0,  tri=0, dbl=0),
}
Y = sp.symbols("Y0:5")

def su3_cubed(c):  return sum(REP[r]["a3"] for r in c)
def witten(c):     return sum(REP[r]["dbl"] for r in c) % 2 == 0
def eqs(c, ys):
    return [sum(REP[r]["tri"] * y for r, y in zip(c, ys)),
            sum(REP[r]["dbl"] * y for r, y in zip(c, ys)),
            sum(REP[r]["st"]  * y for r, y in zip(c, ys)),
            sum(REP[r]["st"]  * y**3 for r, y in zip(c, ys))]

rows, n_examined, n_su3_killed = [], 0, 0
for c in itertools.combinations_with_replacement("AaBbCD", 5):
    n_examined += 1
    if su3_cubed(c) != 0:
        n_su3_killed += 1
        continue
    if not witten(c):
        continue
    sols = sp.solve(eqs(c, list(Y)), list(Y), dict=True)
    keep = []
    for s in sols:
        vals = [sp.simplify(s.get(y, y)) for y in Y]
        fs = set()
        for v in vals: fs |= v.free_symbols
        free = [y for y in Y if y in fs]
        if len(free) != 1:                      # rigid: isolated up to one overall scale
            continue
        cc = [sp.simplify(v.subs({free[0]: 1})) for v in vals]
        if any(x == 0 for x in cc):             # no sterile field
            continue
        keep.append(tuple(sp.nsimplify(x) for x in cc))
    if keep:
        rows.append((sum(REP[r]["st"] for r in c), "".join(c),
                     sorted({str(t) for t in keep})))

rows.sort()
print("contents examined            : %d" % n_examined)
print("killed by [SU(3)]^3 alone    : %d   <-- the condition steps 2-3 omitted" % n_su3_killed)
print("\nRIGID + CHIRAL + fully anomaly-free 5-field contents:\n")
print("  states  content   charges (up to scale)")
for t, c, ex in rows:
    tag = "   <-- the SM generation" if c in ("AbbCD", "ABBCD") else ""
    print("  %5d   %-8s  %s%s" % (t, c, ex[0], tag))
print("\n  total: %d" % len(rows))
